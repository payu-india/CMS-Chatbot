---
title: Integrate PayU Hosted Checkout with AI
excerpt: >-
  Integrate PayU Hosted Checkout (web redirect) into your Java, Node.js, PHP, or
  Python backend in one prompt. An AI coding skill that fetches live PayU docs,
  generates hash logic, callback handlers, and the Verify Payment call, with
  credentials and secrets fully protected.
deprecated: false
hidden: false
metadata:
  robots: index
---
The **PayU Hosted Checkout AI skill** is a prompt you load into Claude Code, Cursor, or any MCP-enabled AI coding assistant. It automatically detects your backend stack, fetches the latest integration code and hash formulas from the [PayU Developer MCP](doc:payu-devguide-builder-mcp-configuration), and scaffolds a complete PayU Hosted Checkout integration — including security, callbacks, and payment verification — adapted to your existing codebase.

<Callout icon="🔒" theme="error">
  ### **Important: Security-first design**

  The skill is hardcoded never to touch your `.env` file, never to log or echo your merchant key or salt, and never to call any live PayU API. It only queries the PayU docs MCP. Your credentials never leave your environment.
</Callout>

***
## Skill prompt

Copy the full prompt below and save it as `.claude/commands/payu-hosted-checkout.md` in your project (Claude Code), or paste it into your AI assistant's system prompt / instructions pane (Cursor, VS Code Copilot, or any MCP-enabled assistant).

<Callout icon="📋" theme="info">
  The prompt is self-contained. Do not modify the GUARDRAILS or CREDENTIALS sections — they enforce the security properties described above. You can safely customise the OPERATION ORDER or add project-specific notes at the bottom.
</Callout>

````markdown
---
name: payu-hosted-checkout
description: Integrates PayU Hosted Checkout (web redirect) into Java, Node.js, PHP, or Python merchant apps using the payu-docs MCP. Use when the user asks to integrate PayU hosted checkout, PayU web redirect, PayU payment, surl/furl, or verify_payment.
---

Integrate PayU Hosted Checkout (web redirect integration) into this codebase.

## CREDENTIALS

Environment variable names (values are NEVER provided to you):

```text
PAYU_MERCHANT_KEY
PAYU_MERCHANT_SALT
PAYU_HASH_MODE      (v1 | dual; default v1 — single hex hash. Use dual only if PayU requires JSON {"v1","v2"})
PAYU_ENV            (test | production; defaults to test)
APP_BASE_URL        (public base URL of this app, used to build surl / furl)
```

The Merchant Key and Salt belong to the USER. They place them into their own environment. Never write them into any file (including .env), source code, comment, README, or output. Refer to them only by environment-variable name.

Credentials must NEVER be pasted into chat with any LLM / IDE agent. If the user pastes a key or salt into the chat:

- Do NOT use, repeat, store, or echo it anywhere (files, code, commands, MCP queries, output).
- Tell the user to treat it as exposed, rotate it in the PayU dashboard, and set the new value only in their own environment.

Because you must not read .env files (see GUARDRAILS), you cannot inspect the values. BEFORE writing any code, ask the user exactly this and wait for the answer:

> "Have you set PAYU_MERCHANT_KEY and PAYU_MERCHANT_SALT in your own environment (not in this chat)? Do not paste the values here."

If the answer is no or unclear, STOP and guide them to add the variables to their own environment (Test credentials: PayU test dashboard; Production credentials: PayU merchant dashboard). Do NOT continue without this: a missing or wrong key/salt produces an incorrect hash, PayU redirects fine, but the hosted payment page fails to load.

## TASK

Detect the project stack (Java, Node.js, PHP, or Python ONLY) and implement PayU Hosted Checkout by following these steps in order:

1. Hash generation (server-side request hash)
2. Response hash verification (reverse hash), performed when key and salt are configured
3. Integration code scaffolding (initiate endpoint + frontend auto-submit form to PayU)
4. sURL / fURL (success and failure URL handlers)
5. Backend route implementation
6. Verify Payment API call (transaction status)
7. Debugging support (logging + troubleshooting guide)

## PAYU DOCS MCP (MANDATORY SOURCE OF TRUTH)

Use the `payu-docs` MCP server to fetch the web checkout integration code and details for the detected language. Expected MCP configuration:

```json
{
  "mcpServers": {
    "payu-docs": {
      "url": "https://ask-ai-mcp-710575177112.asia-south1.run.app/mcp"
    }
  }
}
```

If the MCP needs an API key header, the user sets it in their own IDE MCP settings. Never ask for it in chat and never write it into any project file.

BEFORE writing any code, query the MCP for the language/framework you detected and retrieve:

1. The PayU Hosted (Web) Checkout integration code sample for that language
2. The request hash formula and the exact field order
3. The response (reverse) hash formula, including the additionalCharges variant
4. Test and production `_payment` endpoint URLs
5. The Verify Payment API (`verify_payment`): endpoint per environment, request fields, hash formula, response shape
6. Known error messages and troubleshooting notes

Rules:

- Adapt the MCP-provided code to this project's structure, router, and style; do not paste it blindly.
- Do NOT write PayU formulas, endpoints, or field names from memory. The REFERENCE VALUES at the bottom of this file are for cross-checking only. If the MCP and this file disagree, follow the MCP and mention the discrepancy in your final output.
- If the MCP is unreachable, errors, or returns no usable code for the detected language: STOP and tell the user (it is on an internal network, so the IDE may need VPN access). Do NOT fall back to memory or guesses.
- NEVER include the merchant key, salt, hashes, or customer data in an MCP query. Ask documentation-style questions only (e.g. "PayU hosted checkout request hash formula for Python").
- Querying the MCP for documentation is the ONLY external call you may make (see GUARDRAILS).

## GUARDRAILS (STRICT — DO NOT VIOLATE)

### Environment & secrets

- Do NOT read, open, print, or otherwise access any .env file (or .env.*, .envrc) at any point, not to inspect values and not to write new ones. Ask the user to confirm the variables are set instead.
- Never hardcode, log, echo, or write PAYU_MERCHANT_SALT (or the key) into any file, source code, comment, README, log line, or output. Refer to them only by environment-variable name.
- The salt is BACKEND-ONLY. It must never appear in any frontend file, HTML template, JS bundle, API response, or redirect URL. Only the computed hash may reach the browser.
- The code you WRITE may load environment variables at runtime (process.env / os.environ / getenv / System.getenv); the no-.env-access rule applies to you performing this task, not to the generated code.

### Version control

- Do NOT commit any changes (no git add / git commit).
- Do NOT push to any remote (no git push).
- Do NOT create branches or tags, amend history, or modify git config/hooks.
- Do NOT run destructive git commands (git reset, git checkout/restore to discard changes, git clean, git stash drop). Never discard or revert existing changes; assume uncommitted changes belong to the user.
- Leave all changes uncommitted in the working tree for the user to review.

### Execution

- Do NOT run the application or any dev server.
- Do NOT run tests, builds, linters, formatters, migrations, or package scripts.
- Do NOT execute package-manager install commands (npm/yarn/pnpm/pip/composer/mvn/gradle). Declare dependencies by editing the manifest only, and give the user the exact install command to run themselves.
- Do NOT call any PayU API (payment, verify_payment, or otherwise) yourself. Only write code that calls them. The only permitted external call is the documentation lookup on the payu-docs MCP.

### Scope

- Create or modify only the files strictly required for this integration. Do not refactor, reformat, rename, or delete unrelated code.
- Do NOT perform destructive actions: never delete files, data, databases, or configurations, and never overwrite existing functionality.
- If an existing PayU integration is present, extend only the missing pieces. Do not duplicate or rewrite it.

### Stack & monorepo detection (do this FIRST, after the credentials check)

- Determine the stack from manifests and workspace configs: package.json, requirements.txt / pyproject.toml, composer.json, pom.xml / build.gradle / settings.gradle, workspace configs, etc.
- Supported backends: Java, Node.js, PHP, Python. If the detected language is anything else, STOP and tell the user it is not yet supported.
- If the repository is a monorepo, identify the specific package that will own these routes and use that package's language only.
- Identify the frontend separately (static pages, server-rendered templates, or a JS framework). The auto-submit form goes in the frontend; hash generation and all verification go in the backend.
- If the target package, language, or framework is ambiguous, STOP and ask the user which to integrate into. Do not guess.

## IMPLEMENTATION DETAILS

Flow: the merchant backend builds payment parameters and a hash. The browser auto-submits a POST form to PayU's hosted page (full-page redirect). The customer pays on PayU. PayU POSTs the result back to the merchant's surl (success) or furl (failure). The merchant verifies the response hash and can confirm the status through the Verify Payment API.

Use MCP-provided formulas and endpoints. The formulas below are for structure and cross-checking.

### STEP 1: HASH GENERATION (backend only)

- Compute the request hash server-side with SHA-512, using the exact field order from the MCP. Reference form:

  ```text
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
  ```

- Default PAYU_HASH_MODE=v1: output a lowercase hex digest. If the merchant's PayU account requires dual hash, output JSON `{"v1":"<hex>","v2":"<hex>"}` using Salt-32 bit (v1) and Merchant Salt v2 — only when that is documented for the account.
- Unused udf fields still occupy their position as empty strings; the pipe count must be exact.
- The hash input must use exactly the same values that are submitted in the form (same amount string, productinfo, firstname, email). Any difference causes "hash mismatch" on PayU's page.
- amount: a string with 2 decimal places (e.g. "500.00"), computed SERVER-SIDE from the order record. Never accept an amount from the browser.
- txnid: unique per payment attempt, generated server-side, alphanumeric (plus - and _), max 25 characters. A retry after failure needs a NEW txnid. Store it on the internal order. If the internal order id is longer than 25 characters or not unique per attempt, do not reuse it as txnid; generate a separate one.
- Output: lowercase hex digest.

### STEP 2: RESPONSE HASH (REVERSE HASH) VERIFICATION (backend only)

- Runs when key and salt are configured. Recompute the response hash with the exact reverse formula from the MCP. Reference forms:

  ```text
  With UDFs:
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)

  Without UDFs:
  sha512(SALT|status|||||||||||email|firstname|productinfo|amount|txnid|key)

  If additional_charges is present:
  sha512(additional_charges|SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)

  If splitInfo is present:
  sha512(SALT|status|splitInfo||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  The six pipes after status (or splitInfo) stay empty. Do not include beneficiarydetail. Try both the with-UDF and without-UDF strings.

- Use the values PayU POSTed back (status, txnid, amount, productinfo, firstname, email, udf1..udf5, additional_charges if present) with the merchant salt from the environment. Recompute SHA-512 and compare with constant-time compare. If `hash` is JSON `{"v1","v2"}`, compare against both hex values.
- Web Checkout Pro (PayU hosted UI at api.payu.in/webcheckoutpro) often posts extra fields (udf6–udf10, shipping_*, meCode) and a hash that does not match the documented string built only from env key + posted udfs. After the documented with-UDF / without-UDF / additional_charges / splitInfo strings, also try these using POST body values only (never log the pipe string or salt):
  - merchant key from env AND the `key` field PayU posted
  - `status` and, if different, `unmappedstatus`
  - `firstname` and `firstname`+`lastname`
  - `amount` and `net_amount_debit` if present
  - six or seven empty pipes after status
- Missing hash/status/txnid, or mismatch after those variants → log a warning (txnid and reason only). Do NOT mark paid from the callback body alone. Then call the Verify Payment API (Step 6) with the stored txnid. If PayU returns success or failure, treat that as authoritative: update the order and redirect to success/failure. If verify is unavailable or errors, leave the order unchanged and redirect to the failure page.
- After the hash matches (or verify fallback confirms), also check that the txnid belongs to a known order and that the returned amount equals the server-side order amount. Reject if not.
- Only then act on status: "success" → paid; "failure" → failed; anything else (e.g. "pending") → leave as is and let the Verify API resolve it.

### STEP 3: INTEGRATION CODE SCAFFOLDING

- Backend route (create this): POST /api/payu/initiate
  - Body from the browser: { order_id } only. Load the order from the existing store. Not found → 404; already paid → 409.
  - Build params: key, txnid, amount, productinfo, firstname, email, phone, surl, furl, hash (plus udf1..udf5 if used, e.g. udf1 = internal order id).
  - Return JSON: { action, params }. `action` is the PayU `_payment` URL for the configured PAYU_ENV; `params` holds all form fields including the hash. NEVER include the salt.
  - Persist the txnid on the internal order record and set status per the project's existing model (e.g. pending).
- PAYU_ENV = "test" | "production" (default "test") selects the endpoint URLs (from the MCP).
- Build surl/furl from APP_BASE_URL (env), not from request headers.
- Frontend: in the project's existing pay hook (e.g. a startPayment(order) function or checkout submit handler), call POST /api/payu/initiate, then create a hidden <form method="POST" action="{action}"> with one hidden input per param and call form.submit(). Do NOT use fetch/XHR to post to PayU; it must be a real browser form POST. If initiate fails, show a friendly error and do not redirect.
- Use the MCP-provided code sample for the detected language as the basis for the hash and form logic.

### STEP 4: SURL / FURL (success and failure URLs)

- Backend routes (create these): POST /api/payu/success (surl) and POST /api/payu/failure (furl).
- PayU sends an application/x-www-form-urlencoded POST via the customer's browser. Parse form data, not JSON. Handle GET gracefully (redirect to the failure page) in case of a reload.
- Exempt these routes from CSRF protection if the framework has any, and do not require auth/session for them.
- Both handlers run the SAME verification (Step 2). The verified `status` decides the outcome, not which URL was hit.
- After processing, redirect (302/303) the browser to the frontend result page with only the internal order id (e.g. /order-success.html?order_id=... or /order-failure.html?order_id=...). Never put payment fields or hashes in the redirect URL.
- Idempotency: PayU or the browser may hit these routes more than once. Verify the hash FIRST; then if the order is already in a final state, redirect without re-processing. A tampered hash is rejected even when the order is already paid. Never downgrade a paid order to failed from a later callback.

### STEP 5: BACKEND ROUTE IMPLEMENTATION

- Register the routes (POST /api/payu/initiate, POST /api/payu/success, POST /api/payu/failure, GET /api/payu/verify/<order_id>) in the project's existing router / blueprint / controller structure, matching its error-response shape (e.g. { "error": "<message>" }).
- Reuse the project's existing order repository/service to read orders and update status. Do not create DB tables; store txnid and payment status on the existing order record (or the project's existing store).
- Keep PayU logic in its own module/service (hash generation, reverse-hash check, verify call) so route handlers stay thin.
- Do not modify unrelated routes.

### STEP 6: VERIFY PAYMENT API CALL

- Backend route (create this): GET /api/payu/verify/<order_id> (path style per the framework).
- Load the order, take its stored txnid, and call PayU's Verify Payment API (endpoint from the MCP; test and production differ) with form-urlencoded fields: key, command=verify_payment, var1=<txnid>, hash. Hash reference form: sha512(key|command|var1|salt). Confirm with the MCP.
- Use a request timeout. Parse the response, find this txnid's entry, and read its status. Map: success → paid; failure/failed → failed; pending → leave pending. Apply the same idempotency and amount-check rules as Step 2.
- Return { order_id, txnid, status }. Never return the raw PayU response or any hash.
- PayU reports results in three ways: (1) surl/furl redirect, (2) the merchant calling this Verify API, (3) PayU's own transaction data/notifications. This route covers (2). Also invoke the same verify call from the surl/furl handler when reverse-hash verification fails (Step 2), so Cash on Delivery / Web Checkout Pro still updates the order. Recommend the user also configure PayU webhooks for full reliability; that is a separate concern and out of scope here.

### STEP 7: DEBUGGING

- Add structured logging at each stage (initiate, callback received, hash verified/failed, verify API called) with: order id, txnid, status, outcome. NEVER log the key, salt, hash inputs, hash values, raw request bodies, or customer PII (email/phone).
- Add a short "PayU troubleshooting" section to the project's README (or docs file). See the DEBUGGING GUIDE below.
- When the user reports a PayU issue: ask for the txnid and the exact error text shown on the page (never the key/salt), query the payu-docs MCP for that error, and walk through the DEBUGGING GUIDE before changing any code.

## ENVIRONMENT SETUP

Do not read, create, or modify any .env file (see GUARDRAILS). Instead:

1. Create or update .env.example with variable NAMES only (no real values):

```text
PAYU_MERCHANT_KEY=
PAYU_MERCHANT_SALT=
PAYU_HASH_MODE=v1
PAYU_ENV=test
APP_BASE_URL=
```

2. Ensure .env is listed in .gitignore (edit .gitignore only; never touch .env itself).
3. Wire the backend to read these variables from the environment via the project's existing config mechanism (dotenv, config module, framework config). At startup or first use, fail fast with a clear error naming any missing variable (never its value).
4. In your final output, instruct the user to set the real values themselves. Remind them: never paste key/salt into chat; use test credentials while testing; switch PAYU_ENV and credentials together for production.
5. PAYU_MERCHANT_SALT is backend-only. Never prefix it with NEXT_PUBLIC_, VITE_, or REACT_APP_, and never reference it in client-side code. The key reaches the browser only as the `key` form field returned by /api/payu/initiate.

## DEPENDENCIES (DECLARE ONLY — DO NOT INSTALL)

PayU Hosted Checkout needs no official SDK: it uses SHA-512 and an HTTP call. Prefer the standard library and the project's EXISTING HTTP client. Declare a new dependency only if the project has no HTTP client for the verify call, and give the user the install command:

- Python: hashlib/hmac (stdlib). For the verify call use the existing HTTP client or urllib; else add `requests` to requirements.txt (or pyproject.toml) → user runs pip install -r requirements.txt
- Node.js: built-in crypto; built-in fetch (Node 18+) or the existing client; else add `axios` to package.json → user runs npm install
- PHP: hash() / hash_equals(); existing HTTP client, curl extension, or `guzzlehttp/guzzle` in composer.json → user runs composer install
- Java: java.security.MessageDigest and java.net.http.HttpClient (Java 11+) or the project's existing client; add to pom.xml/build.gradle only if strictly required → user runs mvn compile (or Gradle sync)

The frontend needs no package.

## OPERATION ORDER

1. Ask the user to confirm PAYU_MERCHANT_KEY / PAYU_MERCHANT_SALT are set in their own environment (do not read .env). Stop if not.
2. Detect the stack / target package and the frontend; stop and ask if ambiguous or unsupported.
3. Query the payu-docs MCP for the language-specific web checkout code, hash formulas, endpoints, and verify API. Stop if unavailable.
4. Declare any needed dependency in the manifest (do not install).
5. Create/update .env.example and .gitignore; wire env loading with fail-fast validation.
6. Create the PayU module: request hash (Step 1), reverse hash (Step 2), verify call (Step 6).
7. Create POST /api/payu/initiate and the frontend auto-submit form (Step 3).
8. Create the surl / furl handlers (Step 4).
9. Register routes and create the verify route (Steps 5 and 6).
10. Add logging and the README troubleshooting section (Step 7).
11. Write the OUTPUT summary, listing every manual step left to the user.

## ERROR HANDLING

Implement BOTH classes below. They are distinct problems.

### A) Integration-time errors (configuration, wiring, contract), detected at startup or first use, fail fast with actionable messages:

- Missing or empty PAYU_MERCHANT_KEY / PAYU_MERCHANT_SALT → refuse to serve the PayU routes; return 500 "payment provider misconfigured" and log the missing variable NAME (never its value).
- PAYU_ENV not "test" or "production" → fail fast naming the variable.
- Missing APP_BASE_URL → fail fast; surl/furl cannot be built.
- Verify API response missing expected transaction data → integration failure; log and return 502.
- payu-docs MCP unavailable (at skill time) → stop and tell the user; do not guess.

### B) Runtime errors (per-request):

- /api/payu/initiate: order_id missing → 400; order not found → 404; order already paid → 409; server-computed amount not a positive number with 2 decimals → 400; firstname/email/phone missing → 400. Validate BEFORE hashing.
- surl/furl: missing fields or reverse-hash mismatch → do not trust the callback body; log; call verify_payment; only then update status. If verify fails, redirect to the failure page without changing the order.
- Verify API: network timeout / 5xx → retry with bounded exponential backoff (max 2 retries), then return 503. Do not retry 4xx blindly.
- Never log credentials, hash values, or raw bodies containing customer data.

### Frontend (runtime):

- /api/payu/initiate failed → friendly error, do not submit the form to PayU.
- Result pages read the status from the backend by internal order id, never from URL parameters.
- Failed/cancelled payment → allow retry; retry calls initiate again and gets a NEW txnid.

## DEBUGGING GUIDE (use when the user reports an issue)

| Symptom | Likely cause | What to check |
|---|---|---|
| PayU page shows invalid hash / does not load | Wrong pipe count; amount string differs between hash and form ("500" vs "500.00"); udf fields missing or misordered; whitespace/encoding differences in productinfo/firstname/email; wrong or missing key/salt; test credentials on production URL or vice versa | Rebuild the pre-hash string per the MCP formula; confirm identical values in hash and form; count pipes; log field NAMES and pipe count only (never the salt); ask the user to re-confirm the env variables are set (not their values) and that PAYU_ENV matches the credentials |
| Duplicate transaction id error | txnid reused | Generate a new txnid per attempt |
| Amount error | Wrong format or below minimum | Use 2-decimal string computed server-side |
| surl/furl never reached, or 400/403 on callback | CSRF middleware, auth on the route, wrong APP_BASE_URL, route only accepts JSON | Exempt the callback routes from CSRF/auth, accept form-urlencoded, check APP_BASE_URL |
| Callback received but order not updated | Reverse-hash mismatch (Web Checkout Pro extra fields, additionalCharges, udf order), txnid not stored, amount mismatch | Recheck reverse formula per MCP plus Step 2 variants; confirm txnid persisted at initiate; GET /api/payu/verify/<order_id> |
| Order stuck pending | Callback lost or status pending | Call GET /api/payu/verify/<order_id> |
| verify_payment returns an error | Wrong hash order (key|command|var1|salt); wrong endpoint for the environment; txnid unknown to PayU (payment never started) | Check formula/endpoint against the MCP; treat "not found" as "no payment yet" |
| Works in test, fails in production | PAYU_ENV not switched, or production key/salt not set | Switch PAYU_ENV and credentials together |

## EDGE CASES

- No backend (pure static site): a serverless function is required for hash generation and callbacks; never generate the hash in the browser. If no server-side option exists, tell the user PayU hosted checkout cannot be integrated safely.
- Amount tampering: never read the amount from the client; compute it from the order.
- Already integrated: do not duplicate. If initiate exists, add only what is missing (e.g. reverse-hash verification or the verify route), or vice versa.
- Existing CSRF/auth middleware: exempt only the two callback routes.
- Content-Security-Policy: if the site sets CSP headers, allow form-action to PayU's domains. If headers live outside the repo, list it as a MANUAL USER STEP; never attempt it yourself.
- Localhost: surl/furl work on localhost because PayU redirects through the customer's browser. Webhooks would need a public URL and are out of scope.
- Production: production credentials must only be used with PAYU_ENV=production. Recommend a full test-mode payment first.

## REQUIREMENTS

- Never hardcode credentials; load from environment
- Salt must never reach the frontend, logs, or output
- Compute the request hash server-side only
- Verify the response hash (constant-time) before trusting any payment status
- Cross-check amount and txnid against the server-side order before marking paid
- Callback handling must be idempotent
- Get all PayU formulas, endpoints, and code samples from the payu-docs MCP
- Match the project's existing code style, router, and error-response shape
- Don't create DB tables; store txnid/payment status on the existing order record

## REFERENCE VALUES (cross-check only; the payu-docs MCP is authoritative)

- Test payment endpoint: https://test.payu.in/_payment
- Production payment endpoint: https://secure.payu.in/_payment
- Verify Payment API: form-urlencoded POST with key, command=verify_payment, var1=<txnid>, hash (test: https://test.payu.in/merchant/postservice.php?form=2; production: https://info.payu.in/merchant/postservice.php?form=2)
- Docs: https://docs.payu.in

## MCP vs REFERENCE (dummy-shop-python implementation)

The following came from payu-docs MCP and matched SKILL reference values:

- Request hash: `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)`
- Reverse hash: documented `sha512(salt|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)` plus without-UDF / additionalCharges / splitInfo. On dummy-shop-python, Web Checkout Pro callbacks matched SHA-512 only after also trying posted `key`, extra pipe counts, and name/amount variants; verify_payment remains the fallback when the documented string still mismatches.
- Payment URLs: `https://test.payu.in/_payment`, `https://secure.payu.in/_payment`
- Verify hash: `sha512(key|command|var1|salt)` with `command=verify_payment`

**Discrepancy (implementation follows MCP integration guides + SKILL REFERENCE):**

- Verify Payment **test** URL: MCP sample curl uses `https://test.payu.in/merchant/postservice?form=2` (no `.php`). SKILL REFERENCE and other MCP pages use `https://test.payu.in/merchant/postservice.php?form=2`. Use the `.php` URL for test; switch to the non-`.php` test URL if verify calls fail in your environment.

## OUTPUT

1. List files created or modified
2. Show sample curls for POST /api/payu/initiate and GET /api/payu/verify/<order_id> with expected responses (placeholders only; documentation only, do not execute). Note that surl/furl are called by PayU via the browser redirect and are not meant to be curled by hand.
3. List the manual steps the user must perform (you must NOT perform any of these):
   - Run the dependency install command, if any (state it exactly)
   - Set PAYU_MERCHANT_KEY / PAYU_MERCHANT_SALT / PAYU_ENV / APP_BASE_URL in their own environment
   - If CSP headers are managed outside the repo: allow form-action to PayU's domains
   - Connect the payu-docs MCP in their IDE if it was not already connected
4. Explain how the user can verify manually in TEST mode: start the app, place an order, click pay, confirm redirect to PayU's test page, pay with a PayU test card, confirm redirect to the success page and that the order status flips to paid, then call the verify route and confirm it returns success. Repeat with a failed/cancelled payment and confirm the order is NOT marked paid.
5. State which items came from the payu-docs MCP and any place where the MCP output differed from the reference values above.
6. Confirm compliance with the GUARDRAILS: nothing committed, nothing pushed, nothing executed, no .env file read or written, no credentials seen or written, no PayU API called (only the docs MCP).

Begin integration now.
````

***

## What the skill builds

A single invocation produces a complete server-side PayU Hosted Checkout flow, wired into your existing router and order model:

| Component               | What is created                                                                                                               |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Hash module**         | Server-side SHA-512 request hash; constant-time reverse-hash verification for callbacks; Verify Payment hash                  |
| **Initiate route**      | `POST /api/payu/initiate` — builds payment params, returns `{ action, params }` for the browser form                          |
| **Frontend form**       | Auto-submit hidden `<form>` POST to PayU's hosted page (never XHR/fetch)                                                      |
| **Callback handlers**   | `POST /api/payu/success` and `POST /api/payu/failure` — verify hash, check amount and txnid, update order status idempotently |
| **Verify route**        | `GET /api/payu/verify/<order_id>` — calls PayU Verify Payment API with retry logic, returns clean status                      |
| **Environment wiring**  | `.env.example` (variable names only), `.gitignore` update, fail-fast startup validation                                       |
| **Structured logging**  | Order id, txnid, status, outcome at each stage — no credentials, no PII, no hash values                                       |
| **Troubleshooting doc** | README section with a debugging table for every known PayU error symptom                                                      |

***

## Supported stacks

| Backend                               | Frontend                                                                               |
| ------------------------------------- | -------------------------------------------------------------------------------------- |
| Java (Java 11+)                       | Static HTML, server-rendered templates, or any JS framework                            |
| Node.js                               | Same — the auto-submit form is injected into whichever template layer the project uses |
| PHP                                   |                                                                                        |
| Python (Flask, Django, FastAPI, etc.) |                                                                                        |

If your backend is in a different language, the skill stops and tells you. If you are in a monorepo, it identifies the correct package before writing any code.

***

## Prerequisites

Before invoking the skill, you need three things in place:

**1. PayU credentials in your own environment — not in chat**

The skill will ask you to confirm this before it writes a single line. Your `PAYU_MERCHANT_KEY` and `PAYU_MERCHANT_SALT` must be set as environment variables on your machine or CI. Never paste the real values into the chat window.

**2. The PayU Developer MCP configured in your AI assistant**

The skill fetches hash formulas, endpoint URLs, and code samples live from PayU's documentation MCP. Without it, the skill stops — it will not fall back to hardcoded values.

Add the MCP server to your AI assistant's MCP settings:

```json
{
  "mcpServers": {
    "payu-docs": {
      "url": "https://ask-ai-mcp-710575177112.asia-south1.run.app/mcp"
    }
  }
}
```

For full setup steps and optional API key configuration, see [PayU Developer MCP Server](doc:payu-devguide-builder-mcp-configuration).

**3. An existing backend with an order model**

The skill plugs into your existing router, order repository, and config mechanism. It does not create a database schema or a new project from scratch.

***

## Environment variables

The skill expects these five variables. It only ever refers to them by name — the values are yours.

| Variable             | Purpose                                                                                         | Default      |
| -------------------- | ----------------------------------------------------------------------------------------------- | ------------ |
| `PAYU_MERCHANT_KEY`  | Your PayU merchant key                                                                          | _(required)_ |
| `PAYU_MERCHANT_SALT` | Your PayU merchant salt (backend only — never reaches frontend)                                 | _(required)_ |
| `PAYU_HASH_MODE`     | `v1` for standard hex hash; `dual` only if your PayU account requires a JSON `{"v1","v2"}` hash | `v1`         |
| `PAYU_ENV`           | `test` for test environment; `production` for live                                              | `test`       |
| `APP_BASE_URL`       | Public base URL of your app, used to build `surl` and `furl`                                    | _(required)_ |

<Callout icon="🚫" theme="danger">
  ### Merchant Salt Security

  `PAYU_MERCHANT_SALT`**&#x20;is backend-only.** Never prefix it with `NEXT_PUBLIC_`, `VITE_`, or `REACT_APP_`. Never reference it in any client-side file, HTML template, API response, or redirect URL. Only the computed hash may reach the browser — never the salt that produced it.
</Callout>

***

## How to invoke the skill

### In Claude Code

If you have the skill saved in your project's `.claude/` directory, invoke it directly:

```
/payu-hosted-checkout
```

Or start a new conversation and describe what you need — the skill activates when you mention any of: _PayU hosted checkout_, _PayU web redirect_, _PayU payment_, _surl/furl_, or _verify_payment_.

### In Cursor or other MCP-enabled assistants

Paste the skill prompt into your assistant's context (system prompt or instructions pane) and then describe the task:

> "Integrate PayU Hosted Checkout into this Node.js Express app."

The assistant will follow the skill's operation order automatically.

### What the skill does before writing any code

1. Asks you to confirm your credentials are set in your own environment (stops if you have not)
2. Detects your stack from manifest files (`package.json`, `requirements.txt`, `pom.xml`, etc.) — stops and asks if ambiguous
3. Queries the `payu-docs` MCP for your language's code sample, hash formulas, endpoints, and Verify API details — stops if the MCP is unreachable
4. Declares any new dependency in your manifest (does not run install commands)
5. Proceeds with code generation in the order below

***

## Integration steps produced

The skill works through seven ordered steps:

**Step 1 — Request hash (server-side only)**
SHA-512 of `key|txnid|amount|productinfo|firstname|email|udf1–udf5||||||salt`. The exact field order and pipe count come from the MCP. The `amount` is always a server-computed two-decimal string (`"500.00"`); the `txnid` is generated server-side, unique per payment attempt, max 25 characters.

**Step 2 — Response hash verification**
Reverse SHA-512 checked with constant-time comparison on every callback. Covers the documented UDF, without-UDF, `additionalCharges`, and `splitInfo` variants, plus Web Checkout Pro variants (extra pipes, posted `key`, `net_amount_debit`). A mismatch does not mark the order failed — it falls through to Step 6 (Verify API) before deciding.

**Step 3 — Initiate route and frontend form**
`POST /api/payu/initiate` accepts `{ order_id }` from the browser. It loads the order from your existing store, builds PayU params, computes the hash, persists the `txnid` on the order, and returns `{ action, params }`. The frontend creates a hidden `<form method="POST" action="{action}">` and calls `form.submit()` — no XHR, no fetch.

**Step 4 — sURL / fURL handlers**
`POST /api/payu/success` and `POST /api/payu/failure` parse `application/x-www-form-urlencoded` bodies (not JSON), are exempt from CSRF protection, and run identical verification regardless of which URL was called. After processing, they redirect the browser to your internal result page using only the order id.

**Step 5 — Route registration**
All routes are registered in your project's existing router/blueprint/controller. Error responses follow your existing shape.

**Step 6 — Verify Payment**
`GET /api/payu/verify/<order_id>` fetches PayU's Verify Payment API (`command=verify_payment`) with bounded exponential-backoff retry. Also called automatically from the callback handlers when reverse-hash verification fails, ensuring Web Checkout Pro and edge-case flows still update the order correctly.

**Step 7 — Logging and troubleshooting**
Structured log lines at each stage (order id, txnid, status, outcome — never credentials or PII). A debugging table is appended to your project's README.

***

## Security model

The skill enforces the following at every step. None of these can be overridden by the way you phrase your request.

| Rule                          | What it means in practice                                                                                                                                                                        |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| No `.env` access              | The skill never reads, creates, or modifies any `.env` file. It asks you to confirm credentials are set and moves on.                                                                            |
| Salt never leaves the backend | The salt is loaded from the environment at runtime and used only inside the hash function. It is not returned by any route, not included in redirect URLs, and not present in any frontend file. |
| No git operations             | Nothing is committed, pushed, stashed, or branched. All changes stay uncommitted for you to review.                                                                                              |
| No code execution             | The skill does not run your app, install packages, run tests, or call any PayU API. It declares dependencies and gives you the exact install command.                                            |
| No scope creep                | Only files required for the PayU integration are created or modified. Unrelated code is untouched.                                                                                               |
| MCP-only external calls       | The only external call the skill makes is documentation queries to the `payu-docs` MCP.                                                                                                          |

***

## Debugging guide

If a payment fails or behaves unexpectedly, provide the `txnid` and the exact error text shown on PayU's page (never your key or salt). The skill will query the `payu-docs` MCP for that error and walk through this table:

| Symptom                                         | Likely cause                                                                                                                                                                                | What to check                                                                                           |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| PayU page shows "invalid hash" or does not load | Wrong pipe count; `amount` string differs between hash and form; udf fields misordered; whitespace in `productinfo`/`firstname`/`email`; wrong key/salt; test credentials on production URL | Rebuild pre-hash string per MCP formula; confirm identical values in hash and form; count pipes         |
| Duplicate transaction id error                  | `txnid` reused across attempts                                                                                                                                                              | Generate a new `txnid` per payment attempt                                                              |
| Amount error                                    | Wrong format or below minimum                                                                                                                                                               | Use server-computed two-decimal string (`"500.00"`)                                                     |
| surl/furl returns 400/403 or is never reached   | CSRF middleware or auth on the callback route; wrong `APP_BASE_URL`; route accepts JSON only                                                                                                | Exempt callback routes from CSRF/auth; accept `application/x-www-form-urlencoded`; check `APP_BASE_URL` |
| Callback received but order not updated         | Reverse-hash mismatch (Web Checkout Pro extra fields, `additionalCharges`, udf order); `txnid` not persisted at initiate                                                                    | Recheck reverse formula variants; confirm `txnid` was stored; call `GET /api/payu/verify/<order_id>`    |
| Order stuck in pending                          | Callback lost or `status=pending`                                                                                                                                                           | Call `GET /api/payu/verify/<order_id>` manually                                                         |
| `verify_payment` returns an error               | Wrong hash field order (`key\|command\|var1\|salt`); wrong endpoint for the environment                                                                                                     | Check formula and endpoint against the MCP                                                              |
| Works in test, fails in production              | `PAYU_ENV` not switched; production credentials not set                                                                                                                                     | Switch `PAYU_ENV` and credentials together                                                              |

***

## Manual steps left to you

After the skill finishes, you must do these yourself (the skill explicitly cannot do them):

1. **Install dependencies** — run the exact command the skill prints (e.g. `pip install -r requirements.txt`, `npm install`, `composer install`, `mvn compile`)
2. **Set environment variables** — add `PAYU_MERCHANT_KEY`, `PAYU_MERCHANT_SALT`, `PAYU_ENV`, `APP_BASE_URL` to your own environment
3. **CSP headers** — if your site sets `Content-Security-Policy` outside the repo, allow `form-action` to PayU's domains (`test.payu.in`, `secure.payu.in`)
4. **Test end to end** — start the app, place a test order, confirm redirect to PayU's test page, pay with a [PayU test card](doc:test-credentials), confirm the success page loads and the order flips to paid, then call the verify route and confirm it returns success. Repeat with a cancelled payment and confirm the order is **not** marked paid.
5. **Switch credentials** — when moving to production, change both `PAYU_ENV=production` **and** your key/salt together

<Callout icon="📘" theme="info">
  **Webhooks are out of scope for this skill.** The skill generates the surl/furl browser-redirect callbacks and the on-demand Verify API route. For full reliability — especially for callbacks that may be lost in transit — also configure PayU server-to-server webhooks from your PayU dashboard.
</Callout>

***

## Reference endpoints

The skill always fetches the authoritative values from the `payu-docs` MCP. These are provided for orientation only.

|                        | Test                                                   | Production                                             |
| ---------------------- | ------------------------------------------------------ | ------------------------------------------------------ |
| **Payment page**       | `https://test.payu.in/_payment`                        | `https://secure.payu.in/_payment`                      |
| **Verify Payment API** | `https://test.payu.in/merchant/postservice.php?form=2` | `https://info.payu.in/merchant/postservice.php?form=2` |

<Callout icon="⚠️" theme="warning">
  A known discrepancy: the Verify Payment API MCP sample curl uses `postservice?form=2` (without `.php`) for test, while other MCP pages and the reference above use `postservice.php?form=2`. The skill uses the `.php` URL for test. If verify calls fail, try the non-`.php` variant.
</Callout>

***


## Related pages

<Cards>
  <Card title="PayU Developer MCP Server" href="doc:payu-devguide-builder-mcp-configuration" icon="fa-server">
    Set up the payu-docs MCP in Cursor, VS Code, or Claude — required before invoking this skill.
  </Card>

  <Card title="Hashing Request and Response" href="doc:hashing-request-and-response" icon="fa-key">
    Full reference for PayU's SHA-512 hash formulas — request hash, reverse hash, and all edge-case variants.
  </Card>

  <Card title="Hosted Checkout Integration Demo" href="doc:hosted-checkout-integration-demo" icon="fa-play">
    A working Node.js reference implementation of the full PayU Hosted Checkout flow.
  </Card>

  <Card title="Verify Payment API" href="doc:verify-payment-api" icon="fa-circle-check">
    PayU Verify Payment API reference — fields, hash formula, response shape, and error codes.
  </Card>
</Cards>