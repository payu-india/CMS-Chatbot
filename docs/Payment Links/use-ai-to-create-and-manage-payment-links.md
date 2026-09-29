---
title: Use AI to Create and Manage Payment Links
deprecated: false
hidden: true
metadata:
  robots: index
---
<Banner
  isInline={true}
  message="Three paths — pick yours and follow the steps. No support needed to go live."
  color="#6B21A8"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

Go through every path for using AI with PayU Payment Links. Pick the one that matches what you are trying to build, follow the steps in order, and you will have a working integration at the end.

***

## Which Path Are You On?

| I want to…                                                                 | Path                            | Time to live |
| -------------------------------------------------------------------------- | ------------------------------- | ------------ |
| Write backend code that creates links automatically when orders come in    | **Path 1 — Direct API**         | \~2 hours    |
| Connect Claude, ChatGPT, or a custom agent to manage links by conversation | **Path 2 — AI Agent via MCP**   | \~20 minutes |
| Use an AI assistant to help me create and manage links — no code           | **Path 3 — Merchant / No-code** | \~5 minutes  |

<Callout icon="📘" theme="info">
  These paths are not mutually exclusive. Many teams use Path 1 for automated backend flows and Path 2 for the merchant-facing assistant layer. Start with the one you need first.
</Callout>

***

## Path 1 — Developer: Direct API Integration

Build a backend service that creates payment links, delivers them to customers, and receives payment confirmation via webhook.

### What you need before starting

<Callout icon="🔑" theme="warning">
  Get these from **PayU Dashboard → Settings → API Keys** before writing a single line of code. Without them, nothing works.

  | Credential           | What it is                                                                 | Where to find it                                |
  | -------------------- | -------------------------------------------------------------------------- | ----------------------------------------------- |
  | `PAYU_CLIENT_ID`     | OAuth2 Client ID                                                           | Dashboard → Settings → API Keys → Client ID     |
  | `PAYU_CLIENT_SECRET` | OAuth2 Client Secret — used for both API auth **and** webhook verification | Dashboard → Settings → API Keys → Client Secret |
  | `PAYU_MERCHANT_ID`   | Your Merchant ID (MID)                                                     | Dashboard → Settings → Merchant ID              |
  | `PAYU_ENVIRONMENT`   | `test` for UAT, `production` for live                                      | You set this yourself                           |
</Callout>

<Callout icon="🚧" theme="warning">
  **PAYU_CLIENT_SECRET is not your merchant salt.** It is the OAuth credential from API Keys. These are two different values. Using the wrong one breaks webhook verification.
</Callout>

### Environment base URLs

| Environment | Auth base URL                  | API base URL                |
| ----------- | ------------------------------ | --------------------------- |
| Test (UAT)  | `https://uat-accounts.payu.in` | `https://uatoneapi.payu.in` |
| Production  | `https://accounts.payu.in`     | `https://oneapi.payu.in`    |

Start with UAT. No real money moves in test mode.

### Steps

<Accordion title="Step 1 — Build the token cache module" icon="fa-key">
  Every API call needs a Bearer token. Tokens last 3,600 seconds. **Never request a new token per API call** — you will hit rate limits.

  **POST** `{auth_base}/oauth/token`

  ```
  Content-Type: application/x-www-form-urlencoded

  client_id     = PAYU_CLIENT_ID
  client_secret = PAYU_CLIENT_SECRET
  grant_type    = client_credentials
  scope         = create_payment_links update_payment_links read_payment_links
  ```

  **Successful response:**

  ```json
  {
    "access_token": "eyJhbGc...",
    "token_type": "Bearer",
    "expires_in": 3600,
    "created_at": 1694934000
  }
  ```

  **Cache logic to implement:**

  - Store `access_token` and calculate `expiry = created_at + expires_in`
  - Before every API call, check: is the token within 60 seconds of expiry?
  - If yes, refresh it. If no, reuse it.
  - Add a mutex/lock to prevent multiple simultaneous refresh calls when the token expires under load.

  **Token errors:**

  - `401 invalid_client` → wrong CLIENT_ID or CLIENT_SECRET, or UAT credentials hitting production URL
  - `400 invalid_scope` → wrong scope name — use exact spelling from the request above
</Accordion>

<Accordion title="Step 2 — Build the create payment link endpoint" icon="fa-plus">
  Create a backend route: `POST /api/create-payment-link`

  This route calls PayU on behalf of your user and returns the shareable link.

  **PayU endpoint:** `POST {api_base}/payment-links/` ← trailing slash is required

  **Required headers — all three, every call:**

  | Header          | Value                                                          |
  | --------------- | -------------------------------------------------------------- |
  | `Authorization` | `Bearer {access_token}`                                        |
  | `merchantId`    | `{PAYU_MERCHANT_ID}` — a separate HTTP header, not in the body |
  | `Content-Type`  | `application/json`                                             |

  **Minimum request body:**

  ```json
  {
    "subAmount": 1000.00,
    "description": "Invoice #1042",
    "source": "API"
  }
  ```

  `source: "API"`**&#x20;is required.** Omitting it fails the request. It does not exist in Razorpay or Stripe — it is PayU-specific.

  **Amount is INR, not paise.** `1000.00` means ₹1,000. Do not multiply by 100.

  **Full optional fields:**

  ```json
  {
    "subAmount": 1000.00,
    "description": "Invoice #1042",
    "source": "API",
    "expiryDate": "2026-12-31 23:59:59",
    "customerName": "Priya Sharma",
    "customerEmail": "priya@example.com",
    "customerPhone": "+919876543210",
    "invoiceNumber": "INV-2026-1042",
    "successUrl": "https://yoursite.com/payment/success",
    "failureUrl": "https://yoursite.com/payment/failure",
    "isPartialPaymentAllowed": false,
    "udf": { "udf1": "ORDER-7890" }
  }
  ```

  `expiryDate`**&#x20;is IST, not UTC.** Generate timestamps in India Standard Time (UTC+5:30).

  **Use&#x20;**`successUrl`**&#x20;/&#x20;**`failureUrl`**&#x20;— not&#x20;**`surl`**&#x20;/&#x20;**`furl`**.** The shorthand works in PayU Checkout but is not accepted by the Payment Links API.

  **Success response (HTTP 200,&#x20;**`body.status === 0`**):**

  ```json
  {
    "status": 0,
    "message": "paymentLink generated",
    "result": {
      "invoiceNumber": "INV-2026-1042",
      "paymentLink": "https://pp72.pmny.in/AbCdEfGhIjKl",
      "totalAmount": 1000.00,
      "active": true
    }
  }
  ```

  **HTTP always returns 200 — success or failure.** Check `body.status`: `0` = success, `-1` = failure. Do not rely on HTTP status codes alone.

  **Save&#x20;**`invoiceNumber` — you need it for every subsequent fetch, update, share, or deactivate call. There is no separate numeric ID.
</Accordion>

<Accordion title="Step 3 — Build the webhook endpoint" icon="fa-bell">
  Create a backend route: `POST /api/payu-webhook`

  PayU POSTs to this URL the moment a payment completes. Your endpoint must return HTTP 200.

  **Payload format:** `application/x-www-form-urlencoded`

  **Step 1 — Verify the signature BEFORE processing anything:**

  <Callout icon="🚧" theme="warning">
    PayU Payment Links uses `CLIENT_SECRET` + SHA-512 for webhook verification. **Not HMAC-SHA256. Not your merchant salt. Not a separate webhook secret.** This is the most common integration mistake.
  </Callout>

  Hash formula (exact field order — do not rearrange):

  ```
  sha512(CLIENT_SECRET|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  Steps:

  1. URL-decode all fields from the POST body
  2. Extract each named field (use empty string `""` for any missing field)
  3. The six pipes after `status` represent five empty fields — do not collapse them
  4. Compute `sha512(concatenated_string)` as a lowercase hex digest
  5. Compare using constant-time comparison to the `hash` field in the payload
  6. If mismatch → return HTTP 400, stop processing

  **Key payload fields after verification passes:**

  | Field         | Description                                                       |
  | ------------- | ----------------------------------------------------------------- |
  | `status`      | `success`, `failure`, or `pending`                                |
  | `mihpayid`    | PayU's unique transaction ID — use for refunds and reconciliation |
  | `txnid`       | Your transaction reference                                        |
  | `amount`      | Payment amount as a string, e.g. `"1000.00"`                      |
  | `udf1`–`udf5` | Custom fields you set when creating the link                      |

  **On&#x20;**`status=success`**:** mark the order as paid using `mihpayid`. Implementation must be idempotent — PayU may retry the same event.

  **On&#x20;**`status=pending`**:** do not mark as paid. Wait for a follow-up `success` or `failure` webhook.

  Return HTTP 200 before running any slow processing. Enqueue heavy work asynchronously.
</Accordion>

<Accordion title="Step 4 — Register the webhook URL" icon="fa-gear">
  This is a manual step — do it in the Dashboard, not in code.

  1. Log in to [PayU Dashboard](https://onboarding.payu.in/)
  2. Go to **Settings → Webhooks**
  3. Enter your endpoint URL and click **Save**

  Your endpoint must be publicly accessible over HTTPS. `localhost` URLs will not work — use `ngrok` or `cloudflared` during local development:

  ```
  ngrok http 3000
  ```

  Register the ngrok HTTPS URL in the Dashboard. Update it each time you restart ngrok.
</Accordion>

<Accordion title="Step 5 — Test end-to-end" icon="fa-vial">
  1. Call your `POST /api/create-payment-link` and confirm you get back a `paymentLink` URL and `invoiceNumber`
  2. Open the `paymentLink` URL in a browser
  3. Complete a test payment using PayU test credentials: [Key & Salt Reference](doc:key-salt-reference)
  4. Confirm your webhook fires and your order is marked as paid

  **If your webhook hash keeps failing:** check that you are using `CLIENT_SECRET` (not merchant salt), that you are URL-decoding the payload before building the hash string, and that `amount` uses the exact decimal format from the payload (e.g. `"1000.00"`, not `"1000"`).
</Accordion>

### Fastest way to implement Path 1

Paste the ready-made coding agent prompt from [Integrate with AI Coding Assistants](doc:use-with-ai) into Cursor, Claude Code, or GitHub Copilot. Fill in your three credentials at the top of the prompt and the AI writes the entire integration — token cache, create endpoint, webhook handler — for your existing stack.

***

## Path 2 — Developer: AI Agent via Remote MCP

Connect Claude, ChatGPT, or any MCP-compatible agent to your PayU account. The agent creates, sends, checks, and updates payment links from natural language instructions — no API coding required on your end.

### What you need before starting

<Callout icon="🔑" theme="warning">
  - A **PayU merchant account** with Payment Links enabled
  - An **MCP-compatible client**: Claude Desktop, Cursor, or a custom agent framework
  - **Access to the PayU MCP service** — if you have not been onboarded, email [ai-solutions@payu.in](mailto:ai-solutions@payu.in)
</Callout>

### Steps

<Accordion title="Step 1 — Add the PayU Remote MCP server" icon="fa-plug">
  Add `https://api.payu.in/mcp` as a remote MCP server in your client.

  **Claude Desktop** — add to `claude_desktop_config.json`:

  ```json
  {
    "mcpServers": {
      "payu": {
        "url": "https://api.payu.in/mcp"
      }
    }
  }
  ```

  **Cursor / other clients** — paste the URL into the remote MCP server field in settings.
</Accordion>

<Accordion title="Step 2 — Complete OAuth 2.1 login" icon="fa-lock">
  After adding the server, your MCP client detects authentication is required and opens a browser window automatically. You do not manage tokens.

  1. A PayU login page opens in your browser
  2. Sign in with your PayU merchant account
  3. Approve the requested permissions
  4. Your client stores tokens securely — all subsequent calls are authenticated automatically

  Tokens are refreshed automatically. You never see or manage them.

  **If you are building an agent for a merchant (not your own account):** the merchant must complete this OAuth flow using their own credentials. Tokens are per-account — an agent cannot act across merchants without each one authenticating separately.
</Accordion>

<Accordion title="Step 3 — Verify the connection" icon="fa-circle-check">
  Ask the agent:

  > "List my available PayU merchant accounts"

  The agent calls `list_available_team_accounts`. If it returns your account details, you are fully connected.

  Then test a payment link:

  > "Create a payment link for ₹100, description Test, no expiry"

  If you get back a `paymentLink` URL, everything is working.
</Accordion>

### Available Payment Link tools

| Tool                                      | Triggered by                                               |
| ----------------------------------------- | ---------------------------------------------------------- |
| `payLinks_paymentLink_create`             | "Create a payment link for ₹X for \[customer]"             |
| `payLinks_paymentLink_sendPaymentLink`    | "Send the link to \[email/phone]"                          |
| `payLinks_paymentLink_getByInvoiceNumber` | "Has INV-001 been paid?" / "What's the status of INV-001?" |
| `payLinks_paymentLink_updatePaymentLink`  | "Cancel INV-001" / "Give INV-001 two more weeks"           |

### Key things to know for Path 2

- **Amount is INR, not paise.** Tell your agent: `subAmount=500` means ₹500, not ₹5.
- `expiryDate`**&#x20;is IST.** If your agent generates timestamps, use India Standard Time (UTC+5:30).
- **The link identifier is&#x20;**`invoiceNumber`**.** All follow-up tool calls use `invoiceNumber`, not a numeric ID.
- **Token management is handled by the MCP server.** You do not implement caching.

→ Full guide with example conversations: [Use Payment Links with AI Agents via MCP](doc:use-with-mcp)

***

## Path 3 — Merchant: Conversational AI (No Code)

Use an AI assistant to create and manage payment links by describing what you want — no Dashboard navigation, no code.

### What you need before starting

- A PayU merchant account — that's it.

### Option A — Ask AI for guided help

Open **PayU Ask AI** (or paste into Claude, ChatGPT, or any assistant):

<Callout icon="🤖" theme="info">
  **Copy any of these prompts to get started:**

  - _"You are a PayU merchant assistant. Create a payment link for ₹500 that expires in 24 hours."_
  - _"How do I create a PayU payment link and send it to a customer via WhatsApp?"_
  - _"Walk me through setting up a partial payment link for ₹10,000 deposit."_
  - _"Explain the steps to deactivate a payment link in the PayU Dashboard."_
  - _"Show me all payment link options — expiry, partial payments, custom fields."_
</Callout>

The assistant guides you through the Dashboard step by step. You complete the action yourself — the AI tells you exactly where to click and what to fill in.

### Option B — Agent creates the link for you (requires MCP setup)

If you connect the Remote MCP server (see Path 2, Steps 1–2 above), you can skip the Dashboard entirely:

> "Create a ₹2,500 payment link for Rahul for web design work. Expires 31 December. Send to [rahul@example.com](mailto:rahul@example.com)."

The agent creates and sends the link immediately and confirms with the invoice number and URL.

→ Dedicated page for both options: [Create a Payment Link with AI Assistant](doc:create-with-ai-assistant)

***

## The One Gotcha That Breaks Every Integration

This applies to **Path 1** specifically and is the most common cause of failed webhook verification:

<Callout icon="🚧" theme="warning">
  **PayU Payment Links webhook uses&#x20;**`CLIENT_SECRET`**&#x20;+ SHA-512.**

  Not HMAC-SHA256. Not your merchant salt. Not a separate webhook secret variable.

  Your `CLIENT_SECRET` (the OAuth credential from Dashboard → Settings → API Keys) serves double duty — it authenticates your API calls AND signs your webhooks. They are the same value.

  Using the wrong key or the wrong algorithm fails silently — you get no error, the hash just never matches. If your webhook verification keeps failing, this is the reason in 90% of cases.
</Callout>

***

## Go-Live Checklist

When you are ready to switch from test to production:

<Accordion title="Path 1 — Direct API go-live" icon="fa-rocket">
  - [ ] Change `PAYU_ENVIRONMENT` from `test` to `production`
  - [ ] Replace UAT credentials with production `CLIENT_ID`, `CLIENT_SECRET`, `MERCHANT_ID`
  - [ ] Update webhook URL in PayU Dashboard → Settings → Webhooks to your production endpoint
  - [ ] Confirm webhook endpoint is HTTPS and publicly accessible (no ngrok)
  - [ ] Run one real-money test transaction at a low amount and confirm webhook fires
  - [ ] Check that `CLIENT_SECRET` is not in source control, logs, or any client-side code
</Accordion>

<Accordion title="Path 2 — MCP Agent go-live" icon="fa-rocket">
  - [ ] Confirm the merchant has completed the OAuth login on their production PayU account (not UAT)
  - [ ] Test one payment link creation and confirm the link URL resolves correctly
  - [ ] Verify the agent is using the production MCP endpoint (`https://api.payu.in/mcp`)
  - [ ] Confirm the agent cannot access merchant credentials directly — tokens are managed by the MCP server
</Accordion>

***

## All the Pages, in One Place

<Cards>
  <Card title="AI Coding Assistants (Path 1 prompt)" href="doc:use-with-ai" icon="fa-robot">
    The full coding agent prompt for Cursor, Claude Code, or Copilot — covers token caching, create, webhook, and all gotchas.
  </Card>

  <Card title="Use with AI Agents via MCP (Path 2)" href="doc:use-with-mcp" icon="fa-server">
    Example conversations, MCP vs API decision table, and key behaviours for the MCP path.
  </Card>

  <Card title="Create a Link with AI Assistant (Path 3)" href="doc:create-with-ai-assistant" icon="fa-wand-magic-sparkles">
    Ask AI guidance and MCP agent creation — both options, side by side.
  </Card>

  <Card title="Remote MCP Server Integration" href="doc:payu-remote-mcp-server-integration" icon="fa-plug">
    Full MCP server setup — OAuth 2.1 config, all 13 tools, examples.
  </Card>

  <Card title="Webhook Notifications" href="doc:webhook-notifications" icon="fa-bell">
    SHA-512 verification code, payload reference, IP whitelist, troubleshooting.
  </Card>

  <Card title="Agentic Commerce for Merchants" href="doc:agentic-commerce" icon="fa-store">
    Merchant strategy guide — ChatGPT apps, WhatsApp Commerce, and which option to start with.
  </Card>
</Cards>
