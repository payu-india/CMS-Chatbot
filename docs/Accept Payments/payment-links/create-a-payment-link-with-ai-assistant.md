---
title: AI Coding Assistants to Create a Payment Link
excerpt: >-
  Two ways to create PayU Payment Links using AI — ask the PayU Ask AI chatbot
  to guide you through the Dashboard, or let an AI agent create the link
  autonomously on your behalf using the Remote MCP server.
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
{/* NEW CONTENT */}

<Banner
  isInline={true}
  message="For developers — paste this prompt into Cursor, Claude Code, or GitHub Copilot"
  color="#6B21A8"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

## AI Prompt

Copy the entire block below into your AI coding assistant of choice. Fill in your credentials where indicated, then let the assistant write the integration for you.

<Callout icon="🔑" theme="info">
  ### **What Do You Need?**

  You need your **Client ID**, **Client Secret**, and **Merchant ID** from the PayU Dashboard before starting. To get them:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin">PayU Dashboard</Anchor>.
  2. Go to **Developers** → **API Keys.**
  3. Click **View details&#x20;**&#x75;nder the **Client ID & Client secret details&#x20;**&#x73;ection.
</Callout>

***

```
You are helping a developer integrate PayU Payment Links into this codebase.
Use only the reference below. Do not invent endpoint paths, parameter names,
or hash formulas — use only what is documented here.

=== CREDENTIALS ===
PAYU_CLIENT_ID: {{clientId}}
PAYU_CLIENT_SECRET: {{clientSecret}}
PAYU_MERCHANT_ID: {{merchantId}}

These values are for the USER to place into their own environment. Never write
them into any file (including .env), source code, or output — refer to them
only by environment-variable name.

If any value above is empty or still looks like an unfilled template placeholder
(e.g. wrapped in {{ }} double curly braces), STOP and ask the user to provide
their Client ID, Client Secret, and Merchant ID before proceeding. These are
obtained from: PayU Dashboard → Settings → API Keys. Never copy placeholder
text into any file, code, or output.

=== TASK ===
Detect the project stack and implement PayU Payment Links with:
1. Token acquisition (POST /oauth/token) with caching and expiry management
2. Backend endpoint to create a Payment Link via the PayU API
3. Delivery of the Payment Link URL to the customer (SMS/email/in response)
4. Backend webhook endpoint to receive and verify payment events using SHA-512

=== GUARDRAILS (STRICT — DO NOT VIOLATE) ===

Environment & secrets:
- Do NOT read, open, print, or otherwise access any .env file (or .env.*,
  .envrc) at any point — not to inspect existing values, not to write new ones.
- Never hardcode, log, echo, or write CLIENT_SECRET into any file, source
  code, comment, README, or output. CLIENT_SECRET is used both as the OAuth
  credential AND as the webhook signature verifier — guard it in both contexts.
- Generated code may load environment variables at runtime (process.env /
  os.environ / getenv); the no-.env-access rule applies to you performing this
  task, not to the generated code.

Version control:
- Do NOT commit any changes (no git add / git commit).
- Do NOT push to any remote (no git push).
- Do NOT create branches, tags, or amend history.
- Leave all changes uncommitted in the working tree for the user to review.

Execution:
- Do NOT run the application or any dev server.
- Do NOT run tests, builds, linters, or package scripts.
- Do NOT execute package-manager install commands. Declare dependencies by
  editing the manifest only and give the user the exact install command.
- Do NOT call the PayU API yourself during this task — only write code that
  calls it.

Scope:
- Create or modify only the files strictly required for this integration.
- Do NOT refactor, reformat, rename, or delete unrelated code.
- If an existing PayU Payment Links integration is present, extend only the
  missing pieces — do not duplicate or rewrite it.

Stack & monorepo detection (do this FIRST):
- Determine the stack from manifests: package.json, requirements.txt /
  pyproject.toml, composer.json, Gemfile, go.mod, pom.xml / build.gradle, etc.
- If this is a monorepo, identify the specific package that will own these
  routes and use the HTTP client for that language in that package only.
- If the target package or framework is ambiguous, STOP and ask the user before
  proceeding. Do not guess.

=== ENVIRONMENTS ===

                Auth base URL                      API base URL
Test (UAT):     https://uat-accounts.payu.in       https://uatoneapi.payu.in
Production:     https://accounts.payu.in            https://oneapi.payu.in

Select environment based on PAYU_ENVIRONMENT env variable:
  "test"        → use UAT base URLs above
  "production"  → use production base URLs above

=== IMPLEMENTATION DETAILS ===

--- STEP 1: TOKEN ACQUISITION AND CACHING ---

Every API call requires a Bearer token. Tokens expire in 3600 seconds.
Build a token cache module: store the token + expiry, check before each
API call, and refresh if within 60 seconds of expiry. Never request a new
token per API call.

Token expiry calculation — get the units right:
  created_at and expires_in in the response are UNIX seconds (not ms).
  - Python/Go/PHP/Ruby: compare against time.time() / time.Now() directly
  - JavaScript/Node.js: Date.now() returns milliseconds, so:
      expiresAtMs = (created_at + expires_in) * 1000
      refresh when: Date.now() > expiresAtMs - 60_000
  Mixing units means the token either never refreshes or refreshes on
  every single call — both break the integration.

POST {auth_base}/oauth/token
Content-Type: application/x-www-form-urlencoded
Body (form-encoded):
  client_id        = PAYU_CLIENT_ID
  client_secret    = PAYU_CLIENT_SECRET
  grant_type       = client_credentials
  scope            = create_payment_links update_payment_links read_payment_links

Success response (200):
{
  "access_token": "eyJhbGc...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "create_payment_links update_payment_links read_payment_links",
  "created_at": 1694934000   ← Unix epoch; expiry = created_at + expires_in
}

Use as: Authorization: Bearer {access_token}

Token errors:
- 401 invalid_client → wrong CLIENT_ID or CLIENT_SECRET, or wrong environment
  URL (UAT creds hitting production URL). Log as config error. Do not retry.
- 400 invalid_scope  → wrong scope name. Use exact spelling from table above.

--- STEP 2: CREATE A PAYMENT LINK ---

Merchant backend route to create: POST /api/create-payment-link

PayU endpoint: POST {api_base}/payment-links/    ← trailing slash required

Required headers (ALL three — missing any causes 401 or 400):
  Authorization: Bearer {access_token}
  merchantId:    {PAYU_MERCHANT_ID}       ← separate HTTP header, not in body
  Content-Type:  application/json

Request body:
{
  "subAmount": <number>,             // REQUIRED. INR value (e.g. 1000.00 = ₹1,000)
  "description": "<string>",         // REQUIRED. Shown at checkout
  "source": "API",                   // REQUIRED. Always literal string "API"
  "expiryDate": "YYYY-MM-DD HH:MM:SS",  // Optional. IST timezone. Must be future.
  "customerName": "<string>",        // Optional. Pre-fills checkout
  "customerEmail": "<string>",       // Optional. Required for email delivery
  "customerPhone": "+91XXXXXXXXXX",  // Optional. E.164 format. Required for SMS
  "successUrl": "<url>",             // Optional. Redirect after success
  "failureUrl": "<url>",             // Optional. Redirect after failure
  "invoiceNumber": "<string>",       // Optional. Must be unique. Auto-generated if omitted.
  "isPartialPaymentAllowed": false,  // Optional. Default false
  "udf": {                           // Optional. Up to 5 user-defined fields
    "udf1": "...", "udf2": "...", "udf3": "...", "udf4": "...", "udf5": "..."
  }
}

Success response (HTTP 200, body.status = 0):
{
  "status": 0,
  "message": "paymentLink generated",
  "result": {
    "invoiceNumber": "INV-...",      // ← Link identifier for all subsequent operations
    "paymentLink": "https://pp72.pmny.in/...",  // ← Shareable URL to send customer
    "totalAmount": 1000.00,
    "active": true,
    "expiryDate": "...",
    "emailStatus": "not opted",
    "smsStatus": "not opted"
  },
  "errorCode": null
}

Failure response (HTTP 200, body.status = -1):
{
  "status": -1,
  "message": "Invoice Number already exists. Please enter new invoice number.",
  "result": null
}

Persist: invoiceNumber (your link identifier), paymentLink (the shareable URL).
Return to caller: { invoiceNumber, paymentLink, totalAmount }.

--- STEP 3: DELIVER LINK TO CUSTOMER ---

Option A (recommended) — let PayU notify on creation:
  Include customerEmail and/or customerPhone in the create request body.
  PayU dispatches automatically; check emailStatus/smsStatus in the response.

Option B — trigger manually after creation:
  POST {api_base}/payment-links/{invoiceNumber}/share
  Headers: Authorization: Bearer {token}, merchantId: {PAYU_MERCHANT_ID},
           Content-Type: application/json
  Body: { "channelList": ["email@example.com", "+91XXXXXXXXXX"] }

Never expose CLIENT_SECRET or the Bearer token in any message or client-side
code.

--- STEP 4: WEBHOOK — VERIFY AND HANDLE PAYMENT EVENTS ---

Merchant backend route to create: POST /api/payu-webhook
Webhook registration: PayU Dashboard → Settings → Webhooks
  (MANUAL USER STEP — document in your output; do not attempt it yourself)

PayU POSTs to your endpoint as: application/x-www-form-urlencoded
Your endpoint must return HTTP 200 to acknowledge receipt.

Signature verification (do this BEFORE processing the payload):

⚠ CRITICAL: Use CLIENT_SECRET with SHA-512 — NOT HMAC-SHA256, NOT a separate
  webhook secret. Using the wrong algorithm or key fails silently.

Hash formula (exact field order — do not rearrange):
  sha512(CLIENT_SECRET|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)

Steps:
  1. Parse the POST body as application/x-www-form-urlencoded — configure
     your route's body parser for urlencoded, NOT json. A JSON parser will
     produce an empty or malformed body.
  2. URL-decode every field value (most framework parsers do this automatically
     when configured for urlencoded — verify your framework does so).
  3. Extract each field by name from the decoded body. Use empty string ""
     for any field not present — never use null or None as a literal string.
  4. Keep the amount field as the exact string received (e.g. "1000.00").
     Do NOT cast to float or int — str(1000.0) = "1000.0" ≠ "1000.00" and
     will produce a different hash, causing every verification to fail.
  5. Concatenate exactly as shown in the formula above. The six pipes after
     status represent five empty fixed fields — do not collapse them even
     if they appear redundant.
  6. Compute sha512(concatenated_string) as a lowercase hex digest.
  7. Compare constant-time to the hash field from the payload.
  8. If mismatch: return HTTP 400 and stop processing.

Key payload fields after verified:
  status      : "success", "failure", or "pending"
  txnid       : the transaction/order ID you passed to the payment link
  mihpayid    : PayU's unique transaction ID — use for refunds and inquiries
  amount      : payment amount as a string (e.g. "1000.00")
  key         : your merchant key (not the same as CLIENT_ID)
  udf1–udf5   : user-defined values set at link creation

On verified status=success:
  - Mark internal order as paid using mihpayid and/or the udf you used for
    your order reference
  - Implementation must be idempotent — PayU may retry the same event

On status=pending:
  - Do not mark as paid yet; wait for a follow-up success or failure webhook
  
Return HTTP 200 quickly; enqueue any slow processing asynchronously.

--- STEP 5 (OPTIONAL): STATUS CHECK ---

Merchant backend route: GET /api/payment-link/:invoiceNumber

PayU endpoint: GET {api_base}/payment-links/{invoiceNumber}
Headers: Authorization: Bearer {token}, merchantId: {PAYU_MERCHANT_ID}

Key response fields:
  result.status              : "active" | "deactivated" | "expired" | "paid"
  result.active              : true if currently accepting payments
  result.totalAmountCollected: total collected so far (useful for partial links)

--- STEP 6 (OPTIONAL): DEACTIVATE A LINK ---

PayU endpoint: PUT {api_base}/payment-links/{invoiceNumber}
Headers: Authorization: Bearer {token}, merchantId: {PAYU_MERCHANT_ID},
         Content-Type: application/json
Body: { "active": false }

To permanently cancel (cannot be reversed):
  DELETE {api_base}/payment-links/{invoiceNumber}

Success response: { "status": 0, "message": "Payment link updated successfully" }

=== CRITICAL DIFFERENCES FROM OTHER PAYMENT PROVIDERS ===
These are the most common integration mistakes. Read before writing any code.

1. WEBHOOK SIGNATURE USES CLIENT_SECRET + SHA-512, NOT HMAC-SHA256
   Stripe and Razorpay use a separate webhook secret with HMAC-SHA256.
   PayU uses your CLIENT_SECRET (the same OAuth credential) with SHA-512.
   Do not create a PAYU_WEBHOOK_SECRET variable — use PAYU_CLIENT_SECRET.
   Do not use HMAC. Use SHA-512 on the concatenated string formula above.

2. AMOUNT IS INR, NOT PAISE
   PayU Payment Links uses actual rupee values: 1000.00 = ₹1,000.
   Razorpay and Stripe use the smallest unit (paise/cents). Do not multiply
   by 100 when setting subAmount.

3. merchantId IS A REQUIRED HTTP HEADER
   Every API call requires: Authorization: Bearer {token} AND merchantId:
   {MERCHANT_ID} as separate HTTP headers. merchantId is not inside the
   OAuth token and not in the request body. Omitting it causes 400 or 401.

4. HTTP STATUS IS ALWAYS 200 — CHECK BODY status FIELD
   PayU returns HTTP 200 for both success and failure on most endpoints.
   Success: body.status === 0   |   Failure: body.status === -1
   Do not rely on HTTP status codes alone. Always check body.status.

5. expiryDate IS IST (UTC+5:30), NOT UTC
   Set expiryDate in India Standard Time. A link set to "2026-12-31 23:59:59"
   expires at 23:59:59 IST, not UTC. Generate the string accordingly.

6. USE successUrl / failureUrl — NOT surl / furl
   The shorthand surl and furl work in the PayU Checkout API but are NOT
   accepted by the Payment Links API. Always use successUrl and failureUrl.

7. LINK IDENTIFIER IS invoiceNumber, NOT id
   All subsequent calls (GET, PUT, DELETE, share) use invoiceNumber as the
   path parameter — returned in result.invoiceNumber from the create response.
   There is no separate numeric id field.

8. source: "API" IS REQUIRED IN CREATE
   The create request body must include "source": "API" (literal string).
   Omitting it will cause the request to fail. This field does not exist in
   Razorpay or Stripe — it is PayU-specific.

9. TOKEN MUST BE CACHED — NEVER REQUEST PER CALL
   The Bearer token expires in 3600s. Unlike a static API key, you must
   implement a cache layer. Requesting a new token on every API call will
   exhaust rate limits and slow your integration.

=== ENVIRONMENT SETUP ===
Do not read, create, or modify any .env file (see GUARDRAILS). Instead:

1. Create or update .env.example with variable NAMES only (no values):
   PAYU_CLIENT_ID=
   PAYU_CLIENT_SECRET=
   PAYU_MERCHANT_ID=
   PAYU_ENVIRONMENT=test

2. Ensure .env is in .gitignore (edit .gitignore only; never touch .env).

3. Wire the backend to read these from the environment at startup. Fail fast
   with a clear error naming any missing variable (never its value). Valid
   PAYU_ENVIRONMENT values: "test" or "production".

4. In final output, instruct user to set:
   - PAYU_CLIENT_ID and PAYU_CLIENT_SECRET: Dashboard → Settings → API Keys
   - PAYU_MERCHANT_ID: Dashboard → Settings (Merchant ID / MID)
   - PAYU_ENVIRONMENT: "test" for UAT, "production" for live

5. CLIENT_SECRET is backend-only. Never prefix with NEXT_PUBLIC_, VITE_, or
   REACT_APP_. Never reference in any client-side or browser-executed code.

=== SDK DEPENDENCY (DECLARE ONLY — DO NOT INSTALL) ===
PayU does not publish a widely-supported SDK for the Payment Links OAuth2 API.
Use the project's existing HTTP client:
- Node.js  : built-in fetch, or existing axios/got — no new dependency needed
- Python   : existing requests or httpx — no new dependency needed
- PHP      : existing Guzzle or cURL — no new dependency needed
- Go       : standard net/http — no new dependency needed
- Other    : use the project's existing HTTP client

Only add a new HTTP dependency if the project has absolutely no existing
mechanism for making HTTP calls.

=== OPERATION ORDER ===
1. Detect stack / target package (per GUARDRAILS); stop if ambiguous
2. Create .env.example and update .gitignore; wire env loading with fail-fast
3. Build token cache module: acquire, store, check expiry, refresh
4. Create POST /api/create-payment-link using token cache
5. Create POST /api/payu-webhook with SHA-512 verification + idempotency
6. Write OUTPUT summary listing every manual step remaining for the user

=== ERROR HANDLING ===

A) Integration-time errors — detect at startup or first use, fail fast:
- Missing PAYU_CLIENT_ID / PAYU_CLIENT_SECRET / PAYU_MERCHANT_ID
  → refuse to serve the route; return 500 "payment provider misconfigured";
    log the missing variable NAME only (never its value)
- Token 401 invalid_client → wrong credentials or environment mismatch;
    log as config error, return 500, do NOT retry
- API returns 401 or body message "Invalid access token" → refresh token once;
    if still failing, return 500 (do not retry indefinitely)

B) Runtime errors — per-request:
Validate inputs BEFORE calling PayU:
  - subAmount must be a positive number greater than 0
  - expiryDate, if provided, must be a future timestamp
  - customerPhone, if provided, must be valid E.164 format

PayU body.status = -1 (e.g. duplicate invoiceNumber, invalid date):
  → return 400 with body.message from PayU to the caller

Network timeout / PayU 5xx:
  → retry with bounded exponential backoff (max 2 retries)
  → then return 503 to caller
  → never retry a body.status = -1 response

Log PayU error messages for debugging. Never log CLIENT_SECRET or the value
of the Authorization header.

Webhook runtime:
- Missing or invalid hash       → HTTP 400, do not process
- Unknown status value          → HTTP 200 (ignore), do not error
- Duplicate mihpayid + success  → idempotency check; no-op, return HTTP 200

=== EDGE CASES ===
- Pure static site (no backend): use a serverless function (Vercel/Netlify/
  Cloud Functions) for all routes; never call the PayU API from the browser.
- Partial payments: set isPartialPaymentAllowed: true; track progress via
  GET /payment-links/{invoiceNumber} → result.totalAmountCollected.
- Already integrated: do not duplicate. Add only the missing pieces.
- Local development (document for user; do not start yourself): the webhook
  endpoint must be publicly reachable. The user must start a tunnel (ngrok or
  cloudflared) and register that URL in Dashboard → Settings → Webhooks.
- Concurrent token refresh: implement a mutex/lock around token refresh to
  prevent multiple simultaneous token requests when the token expires.

=== REQUIREMENTS ===
- Never hardcode credentials; load from environment only
- CLIENT_SECRET must never reach the frontend or appear in logs
- Use constant-time comparison for webhook hash verification
- Webhook handler must be idempotent (same event may arrive multiple times)
- Token must be cached — never request a new token per API call
- Match the project's existing code style, router, and error-response shape
- Do not create database tables unless the project already has a database;
  store invoiceNumber and mihpayid on the existing order record instead

=== REFERENCE ===
- Authentication (token):      https://docs.payu.in/reference/get-token-api-for-payment-links
- Create Payment Link:         https://docs.payu.in/reference/create-payment-links
- Share Payment Link:          https://docs.payu.in/reference/share_payment_link_api
- Fetch a single link:         https://docs.payu.in/reference/get-single-payment-link-by-id
- Update / Deactivate link:    https://docs.payu.in/reference/change-status-of-a-payment-link-api
- Webhook events and payloads: https://docs.payu.in/docs/webhook-events-and-sample-payloads
- Test credentials:            https://docs.payu.in/docs/key-salt-reference

=== OUTPUT ===
1. List every file created or modified
2. Show a sample curl to hit POST /api/create-payment-link (the merchant route)
   and the expected response body — documentation only; do not execute
3. List manual steps the user must perform (you must NOT perform any of these):
   a. Set PAYU_CLIENT_ID, PAYU_CLIENT_SECRET, PAYU_MERCHANT_ID, and
      PAYU_ENVIRONMENT in their environment
   b. Run the dependency install command if any new dependency was added
      (state the exact command)
   c. Register the webhook URL in PayU Dashboard → Settings → Webhooks
   d. For local development: start a tunnel (ngrok / cloudflared) so the
      Dashboard can reach the local webhook endpoint
4. Explain how the user can verify manually: create a payment link, open the
   returned paymentLink URL, complete a test payment using PayU test credentials
   (see reference URL above), then confirm the webhook fires and the internal
   order is marked as paid
5. Confirm compliance with GUARDRAILS: nothing committed, nothing pushed,
   nothing executed, no .env file read or written

Begin integration now.
```

<Callout icon="fad fa-brake-warning" theme="error">
  ### **Confidential!**

  Never share your `CLIENT_SECRET` or paste it into a public chat, a GitHub issue, or any client-side code. It is used both to authenticate API calls and to verify incoming webhook signatures.
</Callout>

***

## How this Prompt Works

The prompt is a self-contained spec that tells your AI coding assistant exactly what to build and how PayU behaves. Here is what you need to do at each stage:

### Stage 1: Before You Paste

Open the prompt and find the `=== CREDENTIALS ===` block at the very top. It looks like this:

```
PAYU_CLIENT_ID: {{clientId}}
PAYU_CLIENT_SECRET: {{clientSecret}}
PAYU_MERCHANT_ID: {{merchantId}}
```

Replace the `{{...}}` placeholders with your actual values:

| Placeholder        | What to put here                           | Where to find it                                                                    |
| ------------------ | ------------------------------------------ | ----------------------------------------------------------------------------------- |
| `{{clientId}}`     | Your OAuth2 Client ID in the Test Mode     | **Dashboard** → **Settings** → **API Keys** → **Client ID & Client secret details** |
| `{{clientSecret}}` | Your OAuth2 Client Secret in the Test Mode | **Dashboard** → **Settings** → **API Keys** → **Client ID & Client secret details** |
| `{{merchantId}}`   | Your Merchant test ID (MID)                | **Dashboard** → **Settings** → **Profile Details** → **Merchant test ID**           |

<Callout icon="🚧" theme="warning">
  ### **Watch Out!**

  If you leave a placeholder unfilled (still shows `{{clientId}}` etc.), the prompt instructs the AI to **stop and ask you for the values before writing any code**. This is intentional, the AI will not guess or invent credentials.
</Callout>

### Stage 2: Choose Your Environment

Scroll to the `=== ENVIRONMENTS ===` section in the prompt. It maps two environments to their base URLs:

| Environment  | When to use it                                                                |
| ------------ | ----------------------------------------------------------------------------- |
| `test`       | Start here — uses UAT credentials and sandbox endpoints. No real money moves. |
| `production` | Switch to this only when you are ready to go live with real transactions.     |

The generated code will read a `PAYU_ENVIRONMENT` variable at startup (`"test"` or `"production"`) and automatically switch between UAT and production URLs. You do not need to change any code when you go live.

### Stage 3: Paste into Your AI Coding Assistant

Paste the entire prompt (credentials filled in) into:

- **Cursor**: Open the AI chat panel, paste, and press Enter
- **Claude Code**: Paste in the terminal or chat window
- **GitHub Copilot Chat**: Paste into the chat panel in VS Code

The assistant will then:

1. Detect your project's language and framework from existing files
2. Ask you to clarify the target package if your project is a monorepo
3. Create a token cache module, a route to create payment links, and a webhook endpoint
4. Edit only the files needed. It will not refactor unrelated code
5. Output a summary of every file changed and the manual steps remaining for you

### Stage 4: Manual Steps After the AI Finishes

The AI will list these, but they always apply:

1. **Set environment variables**: Add `PAYU_CLIENT_ID`, `PAYU_CLIENT_SECRET`, `PAYU_MERCHANT_ID`, and `PAYU_ENVIRONMENT` to your environment (`.env` on local, secrets manager in production)
2. **Run the install command**: If the AI added a new HTTP dependency, it will give you the exact command to run
3. **Register the webhook URL**: Go to **PayU Dashboard** → **Developers** → **Webhooks** and add your endpoint URL
4. **Start a Tunnel for Local Testing** — use `ngrok` or `cloudflared` so PayU can reach your local webhook endpoint during development

<Callout icon="📘" theme="info">
  ### **Note:**

  The AI will not commit code, run your server, or touch your `.env` file. These are intentional guardrails built into the prompt. All changes are left uncommitted for you to review.
</Callout>
