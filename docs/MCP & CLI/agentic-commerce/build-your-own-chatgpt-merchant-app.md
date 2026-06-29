---
title: >-
  AI Guide Prompt to Build your own ChatGPT Merchant apps sdk compliant MCP
  server with PayU Payment links
excerpt: 'Building a PayU Payment Links Apps SDK (MCP) Server — Merchant Guide. '
deprecated: false
hidden: false
metadata:
  robots: index
---
Using PayU's Payment Links, now accepting payments on ChatGPT is a one-shot prompt on your AI coding tool of choice such as Cursor , Claude, Codex.&#x20;

A language-agnostic guide for PayU merchants who want to build their own **OpenAI Apps SDK** server backed by **PayU Payment Links**. The server exposes MCP tools (catalog, payment-link create/fetch, payment verification) and a widget that ChatGPT can render. The data model described here lets you plug your own catalog into a chat-first checkout experience.

> Scope: this guide covers **payment-link based collection only**. The merchant generates a hosted payment link and PayU handles every sensitive payment step on its hosted page.
>
> **PII rule (read first).** Buyer PII — name, email, phone, shipping address — is **collected in the widget, never in chat**. The widget submits it via `window.openai.callTool` to a private server-side tool; the model only ever sees an opaque `buyerRef`. The model must never ask for, accept, or echo PII in chat. See §4 (system prompt), §5.3 (`submitBuyerDetails`), and §5.4 (`createPaymentLink`).

***

## 1. What you are building

Three layers, regardless of the language you implement them in:

| Layer                | Purpose                                                                                                                                                                         |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **MCP Server**       | Exposes tools (`listProducts`, `getProduct`, `createPaymentLink`, `getPaymentLinkStatus`, `verifyPayment`) and a widget resource (`app://app`) over the Apps SDK MCP transport. |
| **Catalog DB**       | Persists merchants and their product inventory using the entity model below.                                                                                                    |
| **PayU Integration** | Calls PayU Payment Links APIs (token → create → fetch) and PayU’s server-to-server `verify_payment` API.                                                                        |

A merchant runs the server, points ChatGPT at it (via the developer console / connector URL), and the buyer can browse products, get a payment link, and have the assistant verify the final status — all from chat.

***

## 2. Runtime model — MCP transport, connector URL, hosting

The Apps SDK speaks the **Model Context Protocol (MCP)** to your server. The bare-minimum surface your server must implement is:

| Method (JSON-RPC) | What it does                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------ |
| `initialize`      | Handshake. Return server name, version, and the capabilities you support (`tools`, `resources`). |
| `tools/list`      | Returns the tool descriptors (see §4) with `_meta`.                                              |
| `tools/call`      | Executes a tool and returns `{ structuredContent, content, _meta }`.                             |
| `resources/list`  | Returns resource descriptors for `app://app` and `merchant://*`.                                 |
| `resources/read`  | Returns the widget HTML or the merchant JSON.                                                    |

**Transport**: use **Streamable HTTP** (the current Apps SDK default). Your server exposes one HTTPS endpoint (typically `POST /mcp`) that accepts JSON-RPC messages. Any language that can serve HTTPS + JSON works — there are official and community MCP libraries for TypeScript, Python, Java, Go, Rust, .NET; you can also implement the protocol directly if you prefer.

**Connector URL pattern**:

```
https://<your-mcp-host>/mcp?merchantKey=<MERCHANT_KEY>
```

- HTTPS is mandatory (ChatGPT will refuse plaintext).
- `merchantKey` arrives as a URL query parameter. On every request, your server must extract it from the request URL and bind it to the request context **before** invoking the tool handler. All tool/resource handlers then read it from that context — never from a tool argument.
- Each merchant gets their own connector URL; the same server binary handles many merchants.

**Hosting checklist**:

- [ ] Public HTTPS endpoint (managed cert or behind a load balancer that terminates TLS).
- [ ] Sticky/idempotent — Streamable HTTP allows multiple JSON-RPC messages per HTTP call.
- [ ] CORS / CSP configured (see §6 for the exact widget meta keys).
- [ ] Long-running connection support if you stream tool progress (optional but useful).

***

## 3. PayU Payment Links — APIs you will call

Three Payment Links endpoints plus one reconciliation endpoint are in scope. Always treat the merchant docs as the source of truth; this section is a synthesis you can lean on when writing the system prompt.

> **Currency-unit reminder.** PayU Payment Links `subAmount` is in the **major unit** of the currency (e.g. rupees, **not** paise). Internally this guide stores `price` and `amount` in the **smallest unit** (paise, cents, etc.) because that avoids floating-point error in the catalog and widget. **At the PayU boundary you must divide by 100 (or your currency’s smallest-unit factor) when calling Create Payment Links, and multiply back when reading any response that returns the major unit.** Be explicit about this in your codebase.

### 3.1 Get Token API for Payment Links

- Reference: `https://docs.payu.in/reference/get-token-api-for-payment-links`
- Purpose: Exchange the merchant `clientId` / `clientSecret` for a short-lived **bearer access token** used to authorize Payment Links calls.
- Inputs: `clientId`, `clientSecret`, `grant_type=client_credentials`, `scope=create_payment_links`.
- Output: `access_token`, `expires_in`, `token_type=Bearer`.
- Cache & reuse the token until \~60s before expiry. Never expose it to the model or the widget — it stays server-side.

### 3.2 Create Payment Links

- Reference: `https://docs.payu.in/reference/create-payment-links`
- Purpose: Create a hosted payment link the buyer can pay on.
- Required inputs (typical): `subAmount` (major unit), `description`, `source`, `isPartialPaymentAllowed`, customer info (`name`, `email`, `phone`), `expiryDate`, `transactionId` / merchant reference, optional `successURL` / `failureURL` / notify URL.
- Output (typical): `paymentLink` (URL the buyer opens), `invoiceNumber`, `status`.
- Notes:
  - Always supply your own merchant transaction id — you’ll use it to verify later.
  - Set `expiryDate` short enough to align with cart freshness (e.g. `now + 30 minutes`).
  - Auth header: `Authorization: Bearer <access_token>` from §3.1.
  - Set `successURL` and `failureURL` to a buyer-facing page on your domain (a simple "thanks, return to chat" landing). Set the **notify URL** (the server-to-server callback) to a webhook on your MCP server — see §5 for what to do when it fires.

### 3.3 Get Single Payment Link

- Reference: `https://docs.payu.in/reference/get-single-payment-link`
- Purpose: Fetch the current state of a previously created link (paid / pending / expired / refunded), including the underlying PayU transaction id once paid.
- Lookup key: `invoiceNumber` (preferred) or your `merchantTransactionId`.
- Use this for _link lifecycle_ status. For deep transaction reconciliation, follow with `verify_payment` (see §5.6).

### 3.4 verify\_payment (server-to-server reconciliation)

- Endpoint: `POST https://api.payu.in/merchant/postservice.php?form=2` (production) / `https://test.payu.in/...` (sandbox).
- Used by `verifyPayment` (§5.6). Auth is by SHA-512 hash (not bearer token).
- **Hash format**: lowercase hex digest of `SHA-512( <key> | verify_payment | <var1> | <salt> )`. No spaces, no uppercase.

***

## 4. The system prompt (drop-in, language-agnostic)

Use this prompt verbatim as your MCP server’s _server instructions_ — the block the Apps SDK passes to ChatGPT before tools are invoked. Replace the `{{...}}` placeholders during server bootstrap.

```
You are the shopping & checkout assistant for {{MERCHANT_NAME}}, a PayU merchant.
Your job is to help the buyer (1) browse the merchant's catalog, (2) get a PayU
Payment Link for what they want to buy, and (3) confirm the final payment status.
You DO NOT collect any sensitive payment credentials in chat — PayU's hosted
payment page handles every sensitive step.

# Identity & context
- Merchant key: {{MERCHANT_KEY}} (already bound to this server; never ask the user for it).
- Currency: {{CURRENCY}}. All prices in catalog are in the currency's smallest
  unit unless the `currency` field on the product says otherwise.
- Catalog source: {{CATALOG_SOURCE}}  (one of: api | feed | database | scrape).
  This is informational — you should always trust the values returned by
  listProducts / getProduct as the current truth, regardless of source.
- Freshness expectation: {{CATALOG_FRESHNESS}}  (e.g. "real-time",
  "updated hourly", "updated daily"). If the user questions whether a price or
  stock value is current, you may reference this expectation, but never invent
  one.
- All tool calls are scoped to this merchant — never ask the user "which merchant".

# Available tools (call them, do not describe them)
1. listProducts(category?, searchQuery?, page?, limit?)
   - READ-ONLY. Use this whenever the user wants to browse / search / discover.
   - Always render the returned list in the widget; never re-list products as text
     when the widget is showing them.
2. getProduct(productId)
   - READ-ONLY. Use for "tell me more about X" / variant questions.
3. requestBuyerDetails(reason?)
   - PRIVATE / widget-only. Opens a buyer-details form INSIDE the widget so the
     user can enter their name / email / phone / shipping address there — NOT in
     chat. Call this when you need a buyerRef and you don't have one yet.
     Returns an opaque `buyerRef`. You do NOT see the PII; the server stores it.
4. createPaymentLink(items, buyerRef, amount, description?, expiryMinutes?, idempotencyKey)
   - WRITE. Call ONLY after the user has explicitly confirmed:
       a. the exact list of items + quantities,
       b. that they've filled the buyer-details form in the widget (you have a
          buyerRef),
       c. the total amount you computed.
   - You pass `buyerRef` — NEVER name/email/phone. The server resolves the
     buyerRef to the buyer PII at the PayU boundary.
   - `idempotencyKey` MUST be a fresh UUID per attempt — never reuse one.
   - On success you will receive `{ paymentLink, invoiceNumber, expiresAt }`.
     Render the link in the widget (a button "Pay now") AND say one short
     sentence: "Your payment link is ready — it expires in {{N}} minutes."
   - Never paste secrets (bearer token, clientId, clientSecret) into chat.
5. getPaymentLinkStatus(invoiceNumber)
   - READ-ONLY. Call this:
       a. when the user asks "did my payment go through?",
       b. ~30s after they say they've paid,
       c. before you escalate to verifyPayment.
   - Possible statuses: `paid`, `pending`, `expired`, `cancelled`, `refunded`.
6. verifyPayment(invoiceNumber OR merchantTransactionId)
   - READ-ONLY. Use this for the *final*, authoritative reconciliation once the
     link reports `paid`. Returns the underlying PayU transaction details. Tell
     the user the order is confirmed only when the returned status indicates
     success AND the unmapped status indicates the funds are captured.

# Flow you must follow
A. Discover  →  listProducts / getProduct until the user has chosen items.
B. Identify  →  If you don't already have a buyerRef, call requestBuyerDetails.
                The user fills the form in the widget — DO NOT ask for their
                name / email / phone / address in chat.
C. Confirm   →  Read back the cart + total (NOT the PII) and wait for "yes".
                You can say "Shipping to the details you entered" — never echo
                the email/phone/address back.
D. Collect   →  createPaymentLink(buyerRef, fresh idempotencyKey). Share the link.
E. Wait      →  Do not poll aggressively. When the user signals they've paid OR
                ~30s passes, call getPaymentLinkStatus once.
F. Reconcile →  If status=paid, call verifyPayment and confirm to the user.
                If status=pending, ask them to wait 20–30s and try once more.
                If status=expired/cancelled, offer to regenerate the link
                (new idempotencyKey).

# Hard rules
- PII (name, email, phone, address) is collected in the widget ONLY. Never ask
  for it in chat. If the user volunteers any PII in chat, politely redirect:
  "Please enter that in the form so it stays private." Do not store, repeat, or
  echo PII back. Never include PII in `content` text or `structuredContent`.
- Never invent product IDs, prices, or stock — always read them from listProducts /
  getProduct.
- Never ask for or accept sensitive payment credentials in chat. If the user
  types them, refuse politely and remind them to enter them on the PayU page.
- Never reveal merchant secrets (clientId, clientSecret, access token, merchant salt).
- Never re-use an idempotencyKey across different create attempts. Generate a new
  UUID each time.
- Prices are integers in the unit returned by the catalog. Do not round, do not
  convert silently.
- If a tool returns an error, surface a one-line, user-facing summary and offer
  the next concrete step. Never dump raw JSON to the user.

# Widget behavior
- The widget (app://app) renders structuredContent. Keep narration minimal —
  one short sentence per tool call ("Catalog loaded.", "Link ready.",
  "Payment confirmed."). The widget shows the detail.
- Sensitive / bulky data (full product objects, payment link object) belongs in
  `_meta` (widget-only). Keep `structuredContent` lean.
```

***

## 5. MCP tool surface — exact shapes

These are the only tools your server needs to expose for a payment-links experience. Names are stable across languages; only the implementation differs.

### Error envelope (used by every tool below on failure)

Whenever a tool fails, return the same envelope shape so the widget and the model can react consistently:

```jsonc
{
  "structuredContent": {
    "ok": false,
    "errorCode": "INVOICE_NOT_FOUND",     // SCREAMING_SNAKE_CASE, stable
    "message": "We couldn't find that payment link." // one user-safe sentence
  },
  "content": [ { "type":"text", "text":"We couldn't find that payment link." } ],
  "_meta": { "openai/outputTemplate":"app://app", "openai/widgetAccessible":true }
}
```

Standard error codes you should use:

- `INVALID_INPUT` — schema validation failed.
- `MERCHANT_NOT_FOUND` / `MERCHANT_INACTIVE` — `merchantKey` doesn’t resolve.
- `PRODUCT_NOT_FOUND` / `PRODUCT_OUT_OF_STOCK` — catalog issues.
- `AMOUNT_MISMATCH` — recomputed cart total doesn’t match supplied `amount`.
- `DUPLICATE_IDEMPOTENCY_KEY` — key seen with different payload.
- `BUYER_REF_INVALID` — `buyerRef` is unknown, expired, or belongs to a different session — re-open the buyer form.
- `PAYU_AUTH_FAILED` — token API rejected credentials.
- `PAYU_API_ERROR` — Create / Get Single / verify\_payment returned a non-2xx or an explicit failure.
- `INVOICE_NOT_FOUND` — link lookup failed.
- `INTERNAL_ERROR` — unexpected; log and return.

The system prompt in §4 already tells the model to "surface a one-line, user-facing summary and offer the next concrete step" — that maps to `message` above.

### 5.1 `listProducts` (READ-ONLY, widget)

```jsonc
// inputSchema
{
  "type": "object",
  "properties": {
    "category":    { "type": "string", "description": "Optional category filter" },
    "searchQuery": { "type": "string", "description": "Optional free-text search" },
    "page":        { "type": "integer", "description": "0-indexed page (default 0)" },
    "limit":       { "type": "integer", "description": "Page size (default 20)" }
  }
}

// _meta on the tool descriptor
{
  "openai/outputTemplate":   "app://app",
  "openai/widgetAccessible": true,
  "openai/toolInvocation/invoking": "Loading products...",
  "openai/toolInvocation/invoked":  "Catalog loaded."
}

// structuredContent (slim — model sees this)
{
  "products": [
    { "id":"sku_1", "name":"Cold-pressed coffee", "price":24900, "currency":"INR",
      "imageUrl":"https://.../coffee.jpg", "category":"beverage" }
  ],
  "pagination": { "page":0, "limit":20, "hasMore":true, "count":20 }
}

// _meta on the response (widget-only — model does NOT see this)
{
  "productsById": { "sku_1": { /* full product incl. description, variants */ } },
  "lastSyncedAt": "2026-06-29T11:30:00Z"
}
```

### 5.2 `getProduct` (READ-ONLY, widget)

- Input: `productId` (required).
- structuredContent: `{ "product": { ...full product... } }`.

### 5.3 `submitBuyerDetails` (PRIVATE, widget-only) — PII intake

This tool exists **only to keep buyer PII out of the chat transcript**. The model never calls it directly; the widget calls it via `window.openai.callTool` after the user fills the form rendered by `requestBuyerDetails`.

```jsonc
// Tool descriptor _meta — note the visibility flag
{
  "openai/outputTemplate":   "app://app",
  "openai/widgetAccessible": true,
  "openai/visibility":       "private",            // hidden from the model
  "openai/toolInvocation/invoking": "Saving your details...",
  "openai/toolInvocation/invoked":  "Details saved."
}

// inputSchema (the widget collects these; the model never sees them)
{
  "type":"object",
  "required":["firstName","email","phone"],
  "properties":{
    "firstName":{"type":"string","maxLength":80},
    "lastName": {"type":"string","maxLength":80},
    "email":    {"type":"string","format":"email"},
    "phone":    {"type":"string","pattern":"^[+0-9 \\-()]{6,20}$"},
    "address":  {"type":"object","properties":{
      "line1":{"type":"string"},"line2":{"type":"string"},
      "city":{"type":"string"},"state":{"type":"string"},
      "postalCode":{"type":"string"},"country":{"type":"string"}
    }}
  }
}

// structuredContent (returned to the WIDGET; the model gets only buyerRef)
{
  "buyerRef": "br_8b3c...e7",   // opaque, server-generated, single-use-per-session
  "expiresAt": "2026-06-29T12:30:00Z"
}
```

`requestBuyerDetails` (visible to the model) is a thin sibling: it takes an optional `reason` string, returns `{ formOpen: true }` and instructs the widget to render the form. The widget then calls `submitBuyerDetails`.

Server-side responsibilities:

1. Generate a fresh `buyerRef` (random, server-only).
2. Persist `{ buyerRef → { firstName, lastName, email, phone, address } }` under the current `merchantKey` + session, with a short TTL (e.g. 30 min) and an `expiresAt`.
3. **Never** return the PII fields to the model. The `structuredContent` and `content` of this tool must contain `buyerRef` only.
4. Treat the PII store as restricted — encrypt at rest, redact in logs, purge on `paymentLink` terminal status or TTL expiry.

### 5.4 `createPaymentLink` (WRITE, widget)

```jsonc
// inputSchema
{
  "type": "object",
  "required": ["items","buyerRef","amount","idempotencyKey"],
  "properties": {
    "items":          { "type":"array",  "items": { "type":"object",
                        "properties": {
                          "productId": { "type":"string" },
                          "variantId": { "type":"string" },
                          "quantity":  { "type":"integer", "minimum":1 }
                        },
                        "required": ["productId","quantity"] } },
    "buyerRef":       { "type":"string", "description":"Opaque reference returned by submitBuyerDetails — NEVER pass raw PII" },
    "amount":         { "type":"integer", "description":"Total in the currency's smallest unit" },
    "description":    { "type":"string", "description":"Short description shown on the PayU page" },
    "expiryMinutes":  { "type":"integer", "description":"Link expiry; default 30" },
    "idempotencyKey": { "type":"string", "description":"Fresh UUID per attempt" }
  }
}

// structuredContent
{
  "paymentLink":          "https://pay.payu.in/...",
  "invoiceNumber":        "INV_2026_000123",
  "merchantTransactionId":"txn_e0c9...",
  "amount": 24900,
  "currency":"INR",
  "expiresAt":"2026-06-29T12:00:00Z",
  "status":"created"
}
```

Server-side responsibilities for this tool:

1. Resolve `buyerRef` to the stored PII record (saved by `submitBuyerDetails` in §5.3). If missing or expired → return `BUYER_REF_INVALID` and the widget re-opens the form.
2. Acquire/refresh the **access token** (§3.1) and cache in memory until \~60s before `expires_in`.
3. Validate cart against catalog: re-fetch each `productId`, recompute total, reject if it doesn’t match `amount` (defense against stale prices). On mismatch return `AMOUNT_MISMATCH`.
4. Check idempotency: if `idempotencyKey` was seen with the **same payload**, return the previously created link; if seen with a **different payload**, return `DUPLICATE_IDEMPOTENCY_KEY`.
5. Convert `amount` to the major unit (divide by smallest-unit factor) before sending to PayU as `subAmount`.
6. Call **Create Payment Links** (§3.2) with `Authorization: Bearer <token>`. This is the **only** boundary where buyer PII (`firstName`, `lastName`, `email`, `phone`) leaves your DB — server-to-server, over TLS, never visible to the model. Set `transactionId` to a fresh server-side UUID and store it as `merchantTransactionId`. Set `notifyURL` / `successURL` / `failureURL` to your own domain (see §3.2).
7. Persist `{ invoiceNumber, merchantTransactionId, amount, status:"created", expiresAt, buyerRef }` keyed by `merchantKey` and `idempotencyKey`. **Do not** persist PII on this row — keep PII only in the buyerRef store with its own TTL.
8. Strip PII from the `structuredContent`, `content`, and `_meta` of the response. The widget already has the buyer’s form state if it needs to display the name.

### 5.5 `getPaymentLinkStatus` (READ-ONLY, widget)

```jsonc
// inputSchema
{
  "type":"object",
  "required":["invoiceNumber"],
  "properties": { "invoiceNumber": { "type":"string" } }
}

// structuredContent
{
  "invoiceNumber":"INV_2026_000123",
  "status":"paid",            // paid|pending|expired|cancelled|refunded
  "amount":24900,
  "paidAt":"2026-06-29T11:42:11Z",
  "payuId":"403993715520123456" // populated once paid
}
```

Implementation: call **Get Single Payment Link** (§3.3) with the cached bearer token.

### 5.6 `verifyPayment` (READ-ONLY, widget) — final reconciliation

Even though we are in a payment-link flow, the authoritative truth comes from PayU’s server-to-server `verify_payment` API. Always reconcile through it before declaring success.

```jsonc
// inputSchema — either is accepted
{
  "type":"object",
  "properties": {
    "invoiceNumber":         { "type":"string" },
    "merchantTransactionId": { "type":"string" }
  }
}
```

PayU `verify_payment` request (server-side, never exposed to model):

```
POST https://api.payu.in/merchant/postservice.php?form=2
Content-Type: application/x-www-form-urlencoded

key=<merchantKey>
command=verify_payment
var1=<merchantTransactionId>
hash=SHA512( <merchantKey> | verify_payment | <merchantTransactionId> | <merchantSalt> )
```

Map the response into a slim shape for `structuredContent`:

```jsonc
{
  "status":"success",        // success|pending|failure
  "unmappedStatus":"captured",
  "txnId":"txn_e0c9...",
  "payuId":"403993715520123456",
  "amount":24900,
  "verifiedAt":"2026-06-29T11:42:35Z"
}
```

The model is instructed (§4) to confirm success only when both `status` indicates success and `unmappedStatus` indicates the funds are captured.

### 5.7 PayU notify-URL handler (NOT a tool — a plain HTTP webhook)

PayU posts a server-to-server callback to the `notifyURL` you passed in §3.2 when a payment terminates. Expose it on your MCP server (e.g. `POST /payu/notify`) and on receipt:

1. Verify the `hash` PayU sends, using the standard reverse-hash formula (`SHA-512( salt | status | || | … | key )` — see PayU response-hash docs).
2. Look up the row in `payment_links` by `merchantTransactionId` (or `txnid`).
3. Update `status` / `payu_id` / `paid_at`.
4. Optionally push a notification to the active chat session so the assistant picks up the change without polling.

This is the **fast path**; the model’s `getPaymentLinkStatus` / `verifyPayment` calls remain the safety net.

***

## 6. Catalog & merchant data model

Use the schema below as the contract for your catalog and merchant configuration.

### 6.1 `merchants` table

| Column                     | Type                            | Notes                                                                      |
| -------------------------- | ------------------------------- | -------------------------------------------------------------------------- |
| `id`                       | bigint, PK, auto                |                                                                            |
| `merchant_key`             | varchar(100), unique, not null  | What the MCP server uses to scope every call.                              |
| `name`                     | varchar(200), not null          | Used in the system prompt (`{{MERCHANT_NAME}}`).                           |
| `merchant_id`              | varchar(50), not null           | PayU merchant id.                                                          |
| `merchant_type`            | varchar(50)                     | Free-form classifier you can use to drive adapter behavior.                |
| `implementation_type`      | varchar(50)                     | Which catalog adapter to load (e.g. `default`, `cms`, `erp`).              |
| `salt`                     | varchar(200)                    | **PayU merchant salt** — used for `verify_payment` hash. Server-side only. |
| `client_id`                | varchar(200)                    | PayU Payment Links clientId. Server-side only.                             |
| `client_secret`            | varchar(300)                    | Encrypted at rest. Server-side only.                                       |
| `active`                   | boolean, not null, default true |                                                                            |
| `created_at`, `updated_at` | timestamp                       |                                                                            |

### 6.2 `products` (per-merchant inventory)

Use these fields on every product so the widget keeps working:

- `id` (string, unique within merchant)
- `name` (string)
- `category`, `subcategory` (string)
- `price` (integer, in the currency’s smallest unit)
- `currency` (ISO 4217, lowercase)
- `imageUrl` (string)
- `description` (string)
- `inStock` (boolean)
- `unit` (string, e.g. `"1 kg"`, `"500 ml"`)
- `variants` (list of `{ id, name, price, ... }`)
- `metadata` (string-string map for adapter-specific data)

A `ProductFilter` for `listProducts` should accept: `category`, `subcategory`, `searchQuery`, `inStock`, `page`, `limit`.

### 6.3 `payment_links` (recommended)

| Column                     | Type                                    | Notes                                                      |
| -------------------------- | --------------------------------------- | ---------------------------------------------------------- |
| `id`                       | bigint, PK                              |                                                            |
| `merchant_key`             | varchar(100), indexed                   |                                                            |
| `idempotency_key`          | varchar(64), unique with `merchant_key` | Prevents duplicate links.                                  |
| `invoice_number`           | varchar(100), indexed                   | Returned by PayU.                                          |
| `merchant_transaction_id`  | varchar(100), indexed                   | Your reference; used by `verify_payment`.                  |
| `amount`                   | integer                                 | In the currency’s smallest unit.                           |
| `currency`                 | varchar(8)                              |                                                            |
| `status`                   | varchar(32)                             | `created` → `paid` / `expired` / `cancelled` / `refunded`. |
| `payu_id`                  | varchar(64), nullable                   | Populated after paid.                                      |
| `expires_at`               | timestamp                               |                                                            |
| `created_at`, `updated_at` | timestamp                               |                                                            |

### 6.4 Populating the catalog — pick one option and provide the data

The schema in §6.2 only defines _what_ a product looks like; the merchant still needs to tell us _how_ their live inventory will reach it. Before any code is written, the merchant must answer **one** question and ship **one** payload to the integration team.

#### The intake question (ask the merchant before kickoff)

> **How will you provide your product inventory to the MCP server?**
>
> Choose one of:
>
> - **A. Direct API integration** — we pull live from your commerce backend.
> - **B. File-based feed** — you push us a CSV / XML / JSON / Excel on a schedule.
> - **C. Direct database / read-replica access** — we read straight from your store-of-record.
> - **D. Web scraping / crawling** — no API, no feed, no DB — last resort only.

Once they pick, ask them for the artefacts in the matching subsection. **Do not start building until you have the items in the “What the merchant must provide” checklist for the chosen option.**

***

#### Option A — Direct API integration (real-time, most efficient)

Pull live data directly from the merchant’s commerce backend.

- **Platform APIs**: Shopify, WooCommerce, BigCommerce, Magento, Salesforce Commerce Cloud, etc. — connect to their REST or GraphQL APIs to pull stock, SKUs, prices, images.
- **Custom APIs**: For in-house systems, use the merchant’s own product/inventory endpoints. A Swagger / OpenAPI definition is the cleanest contract — import it into Postman or generate a client to map and test the exact calls you need.
- **Sync model**: webhooks for change notifications when supported; otherwise a short-interval poll for the volatile fields (price, stock).

**Best for**: real-time accuracy, mid-to-large catalogs, merchants with a modern commerce stack.

**What the merchant must provide**

- [ ] Platform name + API version (e.g. _Shopify Admin API 2024-10_) **or** Swagger/OpenAPI spec for a custom API.
- [ ] Base URL(s) for each environment (sandbox + production).
- [ ] Auth method + credentials (API key, OAuth client id/secret, access token, signing secret). Share via a secure channel.
- [ ] Field mapping from their product object → the canonical fields in §6.2 (especially `price` unit, `currency`, `inStock` source).
- [ ] Rate limits and pagination conventions.
- [ ] Webhook URL options (if change-event push is available) and the events that fire (`product.update`, `inventory.update`, etc.).
- [ ] Sample payloads: at least 5 real products, 1 multi-variant, 1 out-of-stock.

***

#### Option B — File-based feed (batch / scheduled)

The merchant exports their inventory on a cadence and ships it to us.

- **Formats**: `.csv`, `.xml`, `.json`, Excel, Google Merchant Center product feed.
- **Delivery**: SFTP/FTP, an S3/GCS/Azure blob bucket, an HTTP(S) endpoint, or a managed feed (e.g. Google Merchant Center data source).
- **Sync model**: scheduled ingestion job (hourly / daily) that upserts into `products`. Use a stable external id → `products.id` mapping so re-imports are idempotent.

**Best for**: merchants without an inventory API, smaller catalogs, or where “fresh within the hour” is good enough.

**What the merchant must provide**

- [ ] Format + a documented column/field schema with data types and units.
- [ ] Delivery channel + credentials (SFTP host/user/key, S3 bucket + IAM role, HTTPS URL + auth, etc.).
- [ ] Drop cadence (e.g. _every hour at :05_) and timezone.
- [ ] File naming convention and whether each drop is a full snapshot or a delta.
- [ ] Field mapping from their columns → the canonical fields in §6.2.
- [ ] Handling rules: what marks a product as deleted? how are variants represented?
- [ ] A real sample file (≥ 50 rows, covering variants, out-of-stock, and edge cases).

***

#### Option C — Direct database / read-replica access (enterprise)

The merchant grants secure read-only access to their store-of-record.

- **Read replicas / mirrors**: read-only credentials to a SQL replica (MySQL, PostgreSQL, MSSQL) or a NoSQL store (MongoDB, DynamoDB).
- **Change data capture**: CDC streams (Debezium, AWS DMS, Kafka Connect) for near-instant propagation.
- **Network**: typically over VPN, VPC peering, or a private link — never over the open internet.

**Best for**: high-volume enterprise merchants who need sub-minute freshness and already have a hardened data platform.

**What the merchant must provide**

- [ ] Engine + version (e.g. _PostgreSQL 15_, _MongoDB 6_, _DynamoDB_).
- [ ] Read-only connection details (host, port, database/keyspace, username, password / IAM role).
- [ ] Network access path (VPN config, VPC peering id, PrivateLink endpoint, allowlisted IPs).
- [ ] Schema / collection definitions for product, variant, inventory, pricing tables.
- [ ] Field mapping from their columns → the canonical fields in §6.2.
- [ ] (If CDC) stream name, format (Debezium / DMS / custom), and offset-management expectations.
- [ ] SLA on read load: how many QPS are we allowed to send?

***

#### Option D — Web scraping / crawling (last resort)

Used only when the merchant has no API, no feed, and no DB access.

- Respect `robots.txt`, rate-limit, identify the crawler, and obtain the merchant’s explicit written permission.
- Treat scraped data as best-effort: prices and stock can lag, and structure can break on a UI change.

**Best for**: a stop-gap until one of A/B/C is in place. Not recommended as a long-term ingestion strategy.

**What the merchant must provide**

- [ ] Written permission to crawl, including allowed paths and forbidden ones.
- [ ] Storefront URL(s) (sitemap and/or product listing pages).
- [ ] Field-locator hints (CSS selectors / DOM structure) for `name`, `price`, `inStock`, etc. — saves weeks of reverse-engineering.
- [ ] Acceptable crawl frequency + concurrency.
- [ ] A staging URL for any planned redesign, so we can re-fit selectors before the change goes live.

***

#### Whichever option you pick, normalize into the §6.2 shape

Regardless of the source, the ingestion layer maps the external record into the canonical fields (`id`, `name`, `category`, `price`, `currency`, `imageUrl`, `description`, `inStock`, `unit`, `variants`, `metadata`) and upserts into `products` keyed by `(merchant_key, id)`. The MCP tools (`listProducts` / `getProduct`) read the canonical shape — so swapping the ingestion source later requires no widget or tool changes.

The **system prompt in §4 does not need to know which option you chose** — that is an internal concern. The assistant just calls `listProducts` / `getProduct` and trusts whatever the ingestion pipeline has loaded.

### 6.5 Merchant-scoped resources (Apps SDK MCP resources)

Register three MCP resources whose handlers read per-merchant JSON files (or any equivalent store) and return them as `application/json`:

- `merchant://capabilities` — supported features for this merchant (always include `PAYMENT_LINK`), currency, min/max order, etc.
- `merchant://fulfillment/options` — delivery modes / slots, only if you fulfill physically.
- `merchant://order/rules` — substitution / cancellation / refund policy text the model should follow.

ChatGPT reads these _before_ tools are called and adapts the conversation. Keep these files merchant-scoped so the same server can host many merchants.

***

## 7. The Apps SDK contract — what every tool response must contain

Every tool you expose returns the same envelope (independent of language). This is what makes the widget render and keeps the model honest about what it can and cannot see.

```jsonc
{
  // What the model SEES — keep it small, semantic, no secrets.
  "structuredContent": { /* slim domain shape, e.g. products[], paymentLink, etc. */ },

  // Short human narration — model uses this for one-line replies.
  "content": [ { "type":"text", "text":"Catalog loaded." } ],

  // Widget-only — bulky / sensitive data, plus Apps SDK hints.
  "_meta": {
    "openai/outputTemplate":   "app://app",
    "openai/widgetAccessible": true,
    "openai/visibility":       "public",          // or "private" to hide from model
    "openai/toolInvocation/invoking": "...",
    "openai/toolInvocation/invoked":  "...",
    // Any extra fields here are visible to the widget but NOT to the model:
    "productsById":  { /* full product objects */ },
    "paymentLinkRaw":{ /* full PayU response */ }
  }
}
```

Register one widget resource at `app://app` whose `mimeType` is `text/html+skybridge`. Inline your built JS + CSS into a single HTML blob. Send `_meta` (CSP + widget domain) on the resource contents so the widget can call back to your backend.

### 7.1 Widget resource — required `_meta` keys

Return these in the `_meta` of `resources/read` for `app://app`:

```jsonc
{
  "openai/widgetDomain":   "https://<your-mcp-host>",          // exact origin
  "openai/widgetCSP": {
    "connect_src": ["https://<your-mcp-host>"],                // for callTool() callbacks
    "resource_src":["https://<your-mcp-host>", "https://cdn.example.com"],
    "font_src":    ["https://fonts.gstatic.com"]
  },
  "openai/widgetDescription":      "Catalog & payment-link widget for {{MERCHANT_NAME}}.",
  "openai/widgetPrefersBorder":    true                         // optional
}
```

The widget _will_ fail to load if `openai/widgetDomain` doesn’t match the origin serving the HTML, or if a required host is missing from `connect_src`.

### 7.2 Widget runtime API (what the inlined JS can do)

Inside your widget bundle, ChatGPT exposes a `window.openai` object. The handles you’ll actually use:

- `window.openai.toolOutput` — read the `structuredContent` + `_meta` from the most recent tool call. This is how the React/JS code paints products / the pay button.
- `window.openai.callTool(name, args)` — invoke another tool from the widget without going back to the model. Use this for widget-only actions (e.g. a "refresh status" button calling `getPaymentLinkStatus`). Only tools with `openai/widgetAccessible: true` are callable.
- `window.openai.sendFollowupMessage(text)` — inject a message into the chat as if the user typed it.
- `window.openai.requestDisplayMode("expanded" | "inline" | "pip")` — ask ChatGPT to resize the widget.

Tools marked `"openai/visibility": "private"` are invisible to the model but still callable via `callTool` — use that for purely UI-driven actions (e.g. a cancel button).

***

## 8. End-to-end flow

```
User: "I want to buy 2 packs of cold-pressed coffee"
  └─ listProducts(searchQuery="cold pressed coffee")        → widget shows results
User: "yes that one"
  └─ getProduct(productId="sku_1")                          → widget shows detail
Model: "Please enter your shipping details in the form."
  └─ requestBuyerDetails(reason="checkout")                 → widget opens form
User fills the form IN THE WIDGET (name/email/phone/address — never typed in chat)
  └─ widget → callTool("submitBuyerDetails", {...})         → returns { buyerRef:"br_..." }
Model: "Total is ₹498. Confirm to generate the payment link?"
User: "yes"
  └─ createPaymentLink(
       items=[{productId:"sku_1", quantity:2}],
       buyerRef="br_8b3c...e7",
       amount=49800,
       expiryMinutes=30,
       idempotencyKey="<fresh-uuid>")
     → server: resolve buyerRef → getToken → create payment link → persist → return paymentLink+invoiceNumber
User opens link in PayU's hosted page, pays
User: "I paid"
  └─ getPaymentLinkStatus(invoiceNumber="INV_2026_000123") → "paid"
  └─ verifyPayment(invoiceNumber="INV_2026_000123")        → status=success, unmappedStatus=captured
Model: "Payment confirmed — order is on its way."
```

If `getPaymentLinkStatus` returns `pending`, the model is instructed (§4) to wait \~20–30s and try once more, never to assume success.

If `expired` or `cancelled`, the model offers to regenerate — with a **new** `idempotencyKey`.

***

## 9. Testing & sandbox

Before pointing a real ChatGPT connector at your server, validate end-to-end against PayU sandbox.

1. **PayU sandbox credentials.** Get a test merchant from PayU (test `clientId` / `clientSecret` / `salt`). Use the sandbox base URLs:
   - Get token / Create / Get link: PayU sandbox host (per their docs).
   - `verify_payment`: `https://test.payu.in/merchant/postservice.php?form=2`.
2. **Test cards / UPI.** PayU publishes test cards and a test UPI VPA for sandbox. The hosted page accepts only those.
3. **MCP-level testing without ChatGPT.**
   - Drive your server with `curl` or any MCP-compatible client. Sequence:
     - `initialize`
     - `tools/list`  → expect 5 tool descriptors with `_meta`.
     - `tools/call listProducts` → expect `structuredContent.products`.
     - `tools/call createPaymentLink` with a fresh UUID → expect a `paymentLink` URL.
     - Open the URL in a browser, pay with a test card → expect a notify call hits your webhook.
     - `tools/call getPaymentLinkStatus` → expect `status: paid`.
     - `tools/call verifyPayment` → expect `status: success`, `unmappedStatus: captured`.
4. **Widget testing.** Use the Apps SDK developer console to load your connector URL; it renders `app://app` and lets you fire tool calls. Verify:
   - Products render.
   - The "Pay now" button opens PayU.
   - CSP errors are absent (browser devtools).
5. **Error paths.** Force each error code from §5: missing product, amount mismatch, duplicate idempotency, expired link.

Only after the above passes should you swap to production credentials.

***

## 10. Implementation checklist (any language)

1. **Catalog**
   - [ ] Ask the merchant the intake question in §6.4 and pick **one** option (A: API, B: feed, C: DB, D: scrape).
   - [ ] Collect every item in that option’s “What the merchant must provide” checklist before writing code.
   - [ ] `merchants` and `products` tables with the columns in §6.1 and §6.2.
   - [ ] Ingestion adapter for the chosen option that normalizes into the §6.2 shape and upserts on `(merchant_key, id)`.
   - [ ] Record `CATALOG_SOURCE` and `CATALOG_FRESHNESS` on the merchant config so the system prompt in §4 can pick them up.
2. **Auth & secrets**
   - [ ] Store `clientId` / `clientSecret` / `salt` server-side; never expose to model or widget.
   - [ ] In-memory cache for the PayU bearer token; refresh \~60s before `expires_in`.
3. **MCP server**
   - [ ] Implement the JSON-RPC methods in §2 (`initialize`, `tools/list`, `tools/call`, `resources/list`, `resources/read`) over Streamable HTTP.
   - [ ] Expose a single HTTPS endpoint (e.g. `POST /mcp`).
   - [ ] Register tools: `listProducts`, `getProduct`, `createPaymentLink`, `getPaymentLinkStatus`, `verifyPayment` with the schemas in §5.
   - [ ] Register resource `app://app` with your built widget HTML+CSS+JS, and emit `openai/widgetDomain` + `openai/widgetCSP` (§7.1).
   - [ ] Register resources `merchant://capabilities`, `merchant://fulfillment/options`, `merchant://order/rules`.
   - [ ] Apply `_meta` (`openai/outputTemplate`, `openai/widgetAccessible`, `openai/toolInvocation/invoking|invoked`, `openai/visibility`) on every tool descriptor.
   - [ ] Extract `merchantKey` from the connector URL query parameter and bind it to the request context on every request.
   - [ ] Expose `POST /payu/notify` (§5.7) for server-to-server callbacks.
4. **PayU integration**
   - [ ] Get-token client (§3.1) with caching.
   - [ ] Create-payment-link client (§3.2) with idempotency + cart re-validation + major-unit conversion at the boundary.
   - [ ] Get-single-payment-link client (§3.3).
   - [ ] `verify_payment` client with the exact hash: lowercase hex `SHA-512(key|verify_payment|var1|salt)` (§3.4).
   - [ ] Notify-URL verifier using PayU’s response-hash formula (§5.7).
5. **System prompt**
   - [ ] Ship the prompt in §4 with `{{MERCHANT_NAME}}`, `{{MERCHANT_KEY}}`, `{{CURRENCY}}`, `{{CATALOG_SOURCE}}`, and `{{CATALOG_FRESHNESS}}` substituted at boot. The last two come from the catalog option chosen in §6.4.
6. **Safety**
   - [ ] Reject sensitive payment credentials if they ever appear in user text; remind the user to enter them on the PayU page.
   - [ ] Never log secrets. Strip `Authorization` and any client-secret fields from request logs.
   - [ ] Idempotency keys are required on every write tool; reject reuse across different payloads.
7. **Test**
   - [ ] Run through §9 end-to-end against PayU sandbox before flipping to production.

<br />
