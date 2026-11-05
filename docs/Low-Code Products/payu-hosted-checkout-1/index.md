---
title: PayU Hosted Checkout
excerpt: >-
  Accept online payments by redirecting customers to PayU's secure, prebuilt
  payment page. Minimal development effort — PayU handles the payment experience
  for you.
deprecated: false
hidden: true
metadata:
  title: PayU Hosted Checkout — Overview
  description: 'PayU Hosted Checkout: redirect customers to a secure PayU-hosted payment '
  robots: index
next:
  description: Explore related information and resources.
---
<Banner
  isInline={true}
  message="Integration effort: Some technical setup required"
  color="#FFC107"
  textColor="#000000"
  fontSize="14px"
  fontWeight="bold"
/>

## How Does PayU Hosted Checkout Simplify My Business?

<Accordion title="Redirect to PayU's secure checkout without the need to build a payment UI">
  When a customer proceeds to pay, you send them to PayU's hosted payment page. PayU handles the entire payment experience such as page rendering, mobile optimisation, 3DS authentication, UPI flows, and net banking redirects. Your application is no longer involved in the payment interaction once the customer is redirected.
</Accordion>

<Accordion title="Accept all major Indian payment methods ">
  A single integration with PayU Hosted Checkout enables cards (credit and debit), UPI, netbanking, wallets, EMI, and BNPL payment modes. PayU's checkout page automatically presents the payment methods enabled on your account.<br />

  To add or remove a payment method such as enabling international payments or BNPL, you make a configuration change in your PayU Dashboard.
</Accordion>

<Accordion title="PCI-DSS scope reduced to near zero">
  Card numbers and other sensitive payment data are entered directly on PayU's infrastructure, not on your website or your server. The most demanding parts of PCI-DSS compliance such as handling, storing, and transmitting raw card data are PayU's responsibility.<br />

  Your integration deals with transaction parameters and response verification. Your application never receives or handles raw card data.
</Accordion>

<Accordion title="Go live quickly, stay low-effort">
  PayU Hosted Checkout can be integrated in hours, not days. The essentials are: generate a SHA-512 hash on your server, POST a form to PayU's endpoint, and verify the response when it returns. There is no payment UI to build or maintain, and no ongoing infrastructure to manage as payment methods evolve.
</Accordion>

<Accordion title="Mobile-optimised and branded out of the box">
  The PayU checkout page adapts to mobile screens automatically. UPI deep-linking for Google Pay, PhonePe, and Paytm works on mobile web without extra configuration on your side.<br />

  You can customise the checkout experience by adding your logo, setting a colour scheme, and choosing the checkout language (Hindi, Kannada, Tamil, Telugu, Gujarati, Marathi, or English) from the PayU Dashboard. See <Anchor target="_blank" href="https://docs.payu.in/docs/customise-payu-hosted-checkout">Customise PayU Hosted Checkout</Anchor>.
</Accordion>

<Callout icon="📘" theme="info">
  ### **Tips:**

  You can initiate the redirect using an HTML form POST or by calling the <Anchor target="_blank" href="https://docs.payu.in/reference/_payment_payu_hosted_checkout">Collect Payment API</Anchor> directly from your server.
</Callout>

***

## Is PayU Hosted Checkout Right for Me?

| I want to…                                                     |                                                Works?                                                |
| -------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------: |
| Accept payments on my website with minimal development effort  |                                                   ✅                                                  |
| Support cards, UPI, netbanking, and wallets in one integration |                                                   ✅                                                  |
| Let PayU host and secure the payment page                      |                                                   ✅                                                  |
| Reduce my PCI-DSS compliance scope                             |                                                   ✅                                                  |
| Integrate using an HTML form POST or a server-side API call    |                                                   ✅                                                  |
| Mobile-optimised checkout with UPI deep-linking                |                                                   ✅                                                  |
| Fully customise the payment page design to match my website    | ⚠️ Use [Merchant Hosted Checkout](https://docs.payu.in/docs/custom-checkout-merchant-hosted) instead |
| Accept payments without a website or any technical setup       |           ⚠️ Use [Payment Links](https://docs.payu.in/docs/payment-links-dashboard) instead          |
| Accept payments natively inside a mobile app                   |          ⚠️ Use [PayU Mobile SDK](https://docs.payu.in/docs/mobile-sdk-integration) instead          |
| Set up recurring auto-debit payments                           |           ⚠️ Use [Recurring Payments](https://docs.payu.in/docs/recurring-payments) instead          |

<Callout icon="far fa-face-thinking" theme="warn">
  ### **Not Sure Which PayU Solution is Right For You?**

  Tell us what you want to achieve and how you plan to accept payments. We will recommend the best PayU solution that fits your needs.<br />

  <Anchor target="_blank" href="https://docs.payu.in/docs/start-here">Find the Right Product for You</Anchor> →
</Callout>

***

## Common Use Cases

<Cards columns="3">
  <Card title="E-commerce & Online Retail" icon="fa-bag-shopping">
    Accept product and cart payments on your store. One integration covers cards, UPI, netbanking, and EMI.
  </Card>

  <Card title="EdTech & Online Courses" icon="fa-graduation-cap">
    Collect fees for courses, certifications, and learning programmes. Supports all major payment methods used by students.
  </Card>

  <Card title="SaaS & Subscription Platforms" icon="fa-layer-group">
    Bill customers at sign-up or on plan selection. For auto-debit after the initial payment, combine with [Recurring Payments](https://docs.payu.in/docs/recurring-payments).
  </Card>

  <Card title="Travel & Hospitality" icon="fa-plane">
    Accept booking and reservation payments with a full checkout experience, including EMI for high-value transactions.
  </Card>

  <Card title="Healthcare & Diagnostics" icon="fa-stethoscope">
    Collect consultation fees, lab test payments, and copays. Supports wallets and UPI for patients who prefer low-friction payment.
  </Card>

  <Card title="B2B & Enterprise" icon="fa-building">
    Handle invoice-based payments or multi-product purchases. Supports netbanking NEFT/RTGS for large transfers.
  </Card>
</Cards>

***

## What All I Need to Get Started?

Before you integrate, make sure you have:<br />

- [x] **A PayU merchant account:** <Anchor target="_blank" href="https://docs.payu.in/docs/set-up-your-account">Sign up here</Anchor> if you do not have an account.
- [x] **Access to the PayU Dashboard:** Where you will manage checkout transactions.
- [x] **A website or application**: Where you want to accept payments.
- [x] **Access to your website's technical setup**: Either yourself or through a developer to integrate PayU Hosted checkout.
- [x] **A way to test the integration** before going live.

<HTMLBlock>{`
                <style>
                .tooltip-btn {
                    position: relative;
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-weight: bold; /* Added this line */
                }
                .tooltip-btn:hover::after {
                    content: attr(data-tooltip);
                    position: absolute;
                    bottom: 125%;
                    left: 50%;
                    transform: translateX(-50%);
                    background-color: #333;
                    color: white;
                    padding: 5px 10px;
                    border-radius: 4px;
                    white-space: nowrap;
                    font-size: 12px;
                    z-index: 1;
                }
                </style>

                <button onclick="window.open('https://docs.payu.in/docs/create-a-payment-link#how-do-i-create-a-payment-link', '_blank')" 
                        class="tooltip-btn" 
                        data-tooltip="Follow the guided steps to set up and test your first payment.">
                    Set Up and Test Your First Payment →
                </button>
`}</HTMLBlock>

***

## Supported Payment Methods

These are the payment methods supported in PayU Hosted Checkout:<br />

- Credit Cards
- Debit Cards
- UPI
- NetBanking
- Wallets

***

## Is My Integration Secure?

PayU Hosted Checkout is designed so that the most sensitive part of a payment such as card number entry and bank authentication happens on PayU's infrastructure, not on your website. Your server never handles raw card data.<br />

Your integration has two security responsibilities:

<Tabs>
  <Tab title="Protect the Payment Request">
    Before redirecting the customer to PayU, your server generates a SHA-512 hash of the transaction parameters using your merchant salt. PayU uses this hash to verify that the request came from you and not modified in transit. The salt must stay secret on your server and should never appear in browser code, mobile apps, or anywhere a customer could inspect it.
  </Tab>

  <Tab title="Verify the Payment Response">
    When PayU redirects the customer back with the payment result, your server must verify the response using reverse hash validation and not just read the status from the redirect URL.
  </Tab>
</Tabs>

***

## How Does My Customer Pay?

Below diagram depicts the customer experience during a payment using PayU Hosted Checkout:


<Image src="https://files.readme.io/82a36292bc83035576726e9defb6f5c88591a33556a392867b68144b2a4f8b40-image.png" align="center" caption="Customer Journey" border={true} />


The following is the customer journey using cards as a payment method:<br />

1. Customer clicks **Pay Now**.
2. Your website starts a payment with PayU.
3. Customer is redirected to PayU's payment page.
4. Customer selects a payment method and completes payment.
5. PayU processes the payment.
6. Customer returns to your website with the payment result.<br />

<Columns layout="fixed">
  <Column>
    For request parameters, hash generation, and response handling, see Build Integration.
  </Column>
</Columns>

***

## What Happens After a Payment

After the customer completes a payment:<br />

- PayU determines the transaction result.
- The customer is redirected back to your website.
- A payment response is sent with transaction details.

<Callout icon="⚠️" theme="warn">
  ### **Important:**

  Don't treat the browser redirect alone as confirmation that a payment succeeded. Your integration should verify the payment status using PayU's server-side verification mechanism.
</Callout>

Learn how to verify payment status and handle webhooks in the technical integration guide.

***

## What If My Customer Wants the Money Back?

It depends on:<br />

- Whether you want to return the money yourself. Use PayU refunds to initiate.
  <Cards>
    <Card title="Refunds" href="doc:introduction-refunds" icon="fad fa-arrow-rotate-left" target="_blank">
      Issue a partial or full refund to a customer directly from the Dashboard or via the Refunds API.
    </Card>
  </Cards>
- You are waiting for the amount to reach your account. PayU settlements can help you find out when the amount will be settled.
  <Cards>
    <Card title="Settlements" href="doc:split-settlments" icon="fad fa-building-columns" target="_blank">
      Understand how PayU settles funds to your bank account, view settlement reports, and split funds across multiple beneficiaries.
    </Card>
  </Cards>
- Your customer has raised a complaint with their bank.
  <Cards>
    <Card title="Disputes and Chargebacks" href="doc:chargeback" icon="fad fa-shield-halved" target="_blank">
      Respond to customer disputes and chargebacks raised through their bank — track status and submit evidence from the Dashboard
    </Card>
  </Cards>

## Use AI to Help You

Ask your AI coding assistant using a prompt to get targeted help with your PayU Hosted Checkout integration. Refer to the <Anchor target="_blank" href="https://docs.payu.in/docs/integrate-payu-hosted-checkout-with-ai">Integrate PayU Hosted Checkout with AI</Anchor> page for more details.

<HTMLBlock>{`
<!-- ============================================================
     PayU AI Prompt Component  |  ReadMe CMS Custom HTML Block
     ============================================================ -->
<textarea id="payu-aip-src" style="display:none;" aria-hidden="true" tabindex="-1">
---
name: payu-hosted-checkout
description: Integrates PayU Hosted Checkout (web redirect) into Java, Node.js, PHP, or Python merchant apps using the payu-docs MCP. Use when the user asks to integrate PayU hosted checkout, PayU web redirect, PayU payment, surl/furl, or verify_payment.
---

Integrate PayU Hosted Checkout (web redirect integration) into this codebase.

## CREDENTIALS

Environment variable names (values are NEVER provided to you):

\`\`\`text
PAYU_MERCHANT_KEY
PAYU_MERCHANT_SALT
PAYU_HASH_MODE      (v1 | dual; default v1 — single hex hash. Use dual only if PayU requires JSON {"v1","v2"})
PAYU_ENV            (test | production; defaults to test)
APP_BASE_URL        (public base URL of this app, used to build surl / furl)
\`\`\`

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

Use the \`payu-docs\` MCP server to fetch the web checkout integration code and details for the detected language. Expected MCP configuration:

\`\`\`json
{
  "mcpServers": {
    "payu-docs": {
      "url": "https://ask-ai-mcp-710575177112.asia-south1.run.app/mcp"
    }
  }
}
\`\`\`

If the MCP needs an API key header, the user sets it in their own IDE MCP settings. Never ask for it in chat and never write it into any project file.

BEFORE writing any code, query the MCP for the language/framework you detected and retrieve:

1. The PayU Hosted (Web) Checkout integration code sample for that language
2. The request hash formula and the exact field order
3. The response (reverse) hash formula, including the additionalCharges variant
4. Test and production \`_payment\` endpoint URLs
5. The Verify Payment API (\`verify_payment\`): endpoint per environment, request fields, hash formula, response shape
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

  \`\`\`text
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
  \`\`\`

- Default PAYU_HASH_MODE=v1: output a lowercase hex digest. If the merchant's PayU account requires dual hash, output JSON \`{"v1":"<hex>","v2":"<hex>"}\` using Salt-32 bit (v1) and Merchant Salt v2 — only when that is documented for the account.
- Unused udf fields still occupy their position as empty strings; the pipe count must be exact.
- The hash input must use exactly the same values that are submitted in the form (same amount string, productinfo, firstname, email). Any difference causes "hash mismatch" on PayU's page.
- amount: a string with 2 decimal places (e.g. "500.00"), computed SERVER-SIDE from the order record. Never accept an amount from the browser.
- txnid: unique per payment attempt, generated server-side, alphanumeric (plus - and _), max 25 characters. A retry after failure needs a NEW txnid. Store it on the internal order. If the internal order id is longer than 25 characters or not unique per attempt, do not reuse it as txnid; generate a separate one.
- Output: lowercase hex digest.

### STEP 2: RESPONSE HASH (REVERSE HASH) VERIFICATION (backend only)

- Runs when key and salt are configured. Recompute the response hash with the exact reverse formula from the MCP. Reference forms:

  \`\`\`text
  With UDFs:
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)

  Without UDFs:
  sha512(SALT|status|||||||||||email|firstname|productinfo|amount|txnid|key)

  If additional_charges is present:
  sha512(additional_charges|SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)

  If splitInfo is present:
  sha512(SALT|status|splitInfo||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  \`\`\`

  The six pipes after status (or splitInfo) stay empty. Do not include beneficiarydetail. Try both the with-UDF and without-UDF strings.

- Use the values PayU POSTed back (status, txnid, amount, productinfo, firstname, email, udf1..udf5, additional_charges if present) with the merchant salt from the environment. Recompute SHA-512 and compare with constant-time compare. If \`hash\` is JSON \`{"v1","v2"}\`, compare against both hex values.
- Web Checkout Pro (PayU hosted UI at api.payu.in/webcheckoutpro) often posts extra fields (udf6–udf10, shipping_*, meCode) and a hash that does not match the documented string built only from env key + posted udfs. After the documented with-UDF / without-UDF / additional_charges / splitInfo strings, also try these using POST body values only (never log the pipe string or salt):
  - merchant key from env AND the \`key\` field PayU posted
  - \`status\` and, if different, \`unmappedstatus\`
  - \`firstname\` and \`firstname\`+\`lastname\`
  - \`amount\` and \`net_amount_debit\` if present
  - six or seven empty pipes after status
- Missing hash/status/txnid, or mismatch after those variants → log a warning (txnid and reason only). Do NOT mark paid from the callback body alone. Then call the Verify Payment API (Step 6) with the stored txnid. If PayU returns success or failure, treat that as authoritative: update the order and redirect to success/failure. If verify is unavailable or errors, leave the order unchanged and redirect to the failure page.
- After the hash matches (or verify fallback confirms), also check that the txnid belongs to a known order and that the returned amount equals the server-side order amount. Reject if not.
- Only then act on status: "success" → paid; "failure" → failed; anything else (e.g. "pending") → leave as is and let the Verify API resolve it.

### STEP 3: INTEGRATION CODE SCAFFOLDING

- Backend route (create this): POST /api/payu/initiate
  - Body from the browser: { order_id } only. Load the order from the existing store. Not found → 404; already paid → 409.
  - Build params: key, txnid, amount, productinfo, firstname, email, phone, surl, furl, hash (plus udf1..udf5 if used, e.g. udf1 = internal order id).
  - Return JSON: { action, params }. \`action\` is the PayU \`_payment\` URL for the configured PAYU_ENV; \`params\` holds all form fields including the hash. NEVER include the salt.
  - Persist the txnid on the internal order record and set status per the project's existing model (e.g. pending).
- PAYU_ENV = "test" | "production" (default "test") selects the endpoint URLs (from the MCP).
- Build surl/furl from APP_BASE_URL (env), not from request headers.
- Frontend: in the project's existing pay hook (e.g. a startPayment(order) function or checkout submit handler), call POST /api/payu/initiate, then create a hidden <form method="POST" action="{action}"> with one hidden input per param and call form.submit(). Do NOT use fetch/XHR to post to PayU; it must be a real browser form POST. If initiate fails, show a friendly error and do not redirect.
- Use the MCP-provided code sample for the detected language as the basis for the hash and form logic.

### STEP 4: SURL / FURL (success and failure URLs)

- Backend routes (create these): POST /api/payu/success (surl) and POST /api/payu/failure (furl).
- PayU sends an application/x-www-form-urlencoded POST via the customer's browser. Parse form data, not JSON. Handle GET gracefully (redirect to the failure page) in case of a reload.
- Exempt these routes from CSRF protection if the framework has any, and do not require auth/session for them.
- Both handlers run the SAME verification (Step 2). The verified \`status\` decides the outcome, not which URL was hit.
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

\`\`\`text
PAYU_MERCHANT_KEY=
PAYU_MERCHANT_SALT=
PAYU_HASH_MODE=v1
PAYU_ENV=test
APP_BASE_URL=
\`\`\`

2. Ensure .env is listed in .gitignore (edit .gitignore only; never touch .env itself).
3. Wire the backend to read these variables from the environment via the project's existing config mechanism (dotenv, config module, framework config). At startup or first use, fail fast with a clear error naming any missing variable (never its value).
4. In your final output, instruct the user to set the real values themselves. Remind them: never paste key/salt into chat; use test credentials while testing; switch PAYU_ENV and credentials together for production.
5. PAYU_MERCHANT_SALT is backend-only. Never prefix it with NEXT_PUBLIC_, VITE_, or REACT_APP_, and never reference it in client-side code. The key reaches the browser only as the \`key\` form field returned by /api/payu/initiate.

## DEPENDENCIES (DECLARE ONLY — DO NOT INSTALL)

PayU Hosted Checkout needs no official SDK: it uses SHA-512 and an HTTP call. Prefer the standard library and the project's EXISTING HTTP client. Declare a new dependency only if the project has no HTTP client for the verify call, and give the user the install command:

- Python: hashlib/hmac (stdlib). For the verify call use the existing HTTP client or urllib; else add \`requests\` to requirements.txt (or pyproject.toml) → user runs pip install -r requirements.txt
- Node.js: built-in crypto; built-in fetch (Node 18+) or the existing client; else add \`axios\` to package.json → user runs npm install
- PHP: hash() / hash_equals(); existing HTTP client, curl extension, or \`guzzlehttp/guzzle\` in composer.json → user runs composer install
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

- Request hash: \`sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)\`
- Reverse hash: documented \`sha512(salt|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)\` plus without-UDF / additionalCharges / splitInfo. On dummy-shop-python, Web Checkout Pro callbacks matched SHA-512 only after also trying posted \`key\`, extra pipe counts, and name/amount variants; verify_payment remains the fallback when the documented string still mismatches.
- Payment URLs: \`https://test.payu.in/_payment\`, \`https://secure.payu.in/_payment\`
- Verify hash: \`sha512(key|command|var1|salt)\` with \`command=verify_payment\`

**Discrepancy (implementation follows MCP integration guides + SKILL REFERENCE):**

- Verify Payment **test** URL: MCP sample curl uses \`https://test.payu.in/merchant/postservice?form=2\` (no \`.php\`). SKILL REFERENCE and other MCP pages use \`https://test.payu.in/merchant/postservice.php?form=2\`. Use the \`.php\` URL for test; switch to the non-\`.php\` test URL if verify calls fail in your environment.

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
</textarea>

<style>
.payu-aip-wrap{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;margin:16px 0}
.payu-aip-btn-row{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.payu-aip-btn{background-color:#4CAF50;color:#fff;padding:10px 20px;border:none;border-radius:5px;cursor:pointer;font-weight:bold;font-size:14px;line-height:1.4}
.payu-aip-btn:hover{background-color:#43a047;box-shadow:0 2px 6px rgba(0,0,0,.18)}
.payu-aip-btn:active{background-color:#388e3c}
.payu-aip-status{font-size:13px;font-weight:600;color:#388e3c;min-height:20px;line-height:20px}
.payu-aip-panel{display:none;margin-top:12px;border:1px solid #d0d7de;border-radius:6px;overflow:hidden}
.payu-aip-panel.payu-aip-open{display:block}
.payu-aip-panel-hdr{display:flex;justify-content:space-between;align-items:center;background:#edf0f5;border-bottom:1px solid #d0d7de;padding:7px 14px}
.payu-aip-panel-lbl{font-size:12px;font-weight:600;color:#6b7a90;letter-spacing:.04em;text-transform:uppercase}
.payu-aip-pcopy{background:#fff;color:#4a5568;border:1px solid #c4cdd8;border-radius:4px;padding:3px 12px;font-size:12px;font-weight:600;cursor:pointer;line-height:1.6}
.payu-aip-pcopy:hover{background:#e8edf5;color:#1a202c}
.payu-aip-pcopy:active{background:#dde3ee}
.payu-aip-panel-body{background:#f7f8fa;padding:16px 20px;max-height:420px;overflow-y:auto}
.payu-aip-panel-body pre{margin:0;white-space:pre-wrap;word-break:break-word;font-family:'SFMono-Regular','Consolas','Liberation Mono',monospace;font-size:13px;line-height:1.65;color:#2d3748;user-select:text;-webkit-user-select:text}
</style>

<div class="payu-aip-wrap">
  <div class="payu-aip-btn-row">

    <button class="payu-aip-btn" id="payu-aip-copy"
      onclick="(function(){
        var src=document.getElementById('payu-aip-src');
        var p=src?src.value.trim():'';
        var s=document.getElementById('payu-aip-status');
        function show(m){if(s){s.textContent=m;setTimeout(function(){s.textContent='';},3000);}}
        if(!p){show('No prompt found.');return;}
        var ta=document.createElement('textarea');
        ta.value=p;
        ta.setAttribute('readonly','');
        ta.style.cssText='position:fixed;top:-9999px;left:-9999px;width:1px;height:1px;opacity:0;';
        document.body.appendChild(ta);
        ta.focus();ta.select();ta.setSelectionRange(0,p.length);
        var ok=false;
        try{ok=document.execCommand('copy');}catch(e){}
        document.body.removeChild(ta);
        show(ok?'Prompt copied!':'Copy failed — select the text and copy manually.');
      })()"
    >Copy AI Prompt</button>

    <button class="payu-aip-btn" id="payu-aip-view"
      onclick="(function(){
        var panel=document.getElementById('payu-aip-panel');
        var btn=document.getElementById('payu-aip-view');
        var pre=document.getElementById('payu-aip-text');
        if(!panel||!btn||!pre)return;
        if(!pre.textContent){
          var src=document.getElementById('payu-aip-src');
          if(src)pre.textContent=src.value.trim();
        }
        var open=panel.classList.contains('payu-aip-open');
        if(open){panel.classList.remove('payu-aip-open');panel.setAttribute('aria-hidden','true');btn.textContent='View AI Prompt';}
        else{panel.classList.add('payu-aip-open');panel.setAttribute('aria-hidden','false');btn.textContent='Hide AI Prompt';}
      })()"
    >View AI Prompt</button>

    <span class="payu-aip-status" id="payu-aip-status" role="status" aria-live="polite"></span>
  </div>

  <div class="payu-aip-panel" id="payu-aip-panel" aria-hidden="true">
    <div class="payu-aip-panel-hdr">
      <span class="payu-aip-panel-lbl">AI Prompt</span>
      <button class="payu-aip-pcopy" id="payu-aip-pcopy"
        onclick="(function(){
          var src=document.getElementById('payu-aip-src');
          var p=src?src.value.trim():'';
          if(!p)return;
          var btn=document.getElementById('payu-aip-pcopy');
          var ta=document.createElement('textarea');
          ta.value=p;
          ta.setAttribute('readonly','');
          ta.style.cssText='position:fixed;top:-9999px;left:-9999px;width:1px;height:1px;opacity:0;';
          document.body.appendChild(ta);
          ta.focus();ta.select();ta.setSelectionRange(0,p.length);
          var ok=false;
          try{ok=document.execCommand('copy');}catch(e){}
          document.body.removeChild(ta);
          if(btn){var orig=btn.textContent;btn.textContent=ok?'Copied!':'Failed';setTimeout(function(){btn.textContent=orig;},2000);}
        })()"
      >Copy</button>
    </div>
    <div class="payu-aip-panel-body">
      <pre id="payu-aip-text"></pre>
    </div>
  </div>
</div>
`}</HTMLBlock>

***

## Split the Settlement Across Multiple Accounts

If your business operates as a **marketplace, aggregator, or platform**, collecting payments on behalf of vendors, service providers, or partners, PayU can automatically <Anchor target="_blank" href="https://docs.payu.in/docs/split-settlments">split the settlement</Anchor> from each Payment Link transaction into multiple bank accounts.

You define the split rules: by absolute amount or by percentage, applied either at the time of the transaction or after collection. Each sub-merchant receives their portion directly; you retain your platform fee.

***

## Next Steps

<Cards>
  <Card title="Quick Start" href="https://docs.payu.in/docs/payu-hosted-checkout-quick-start" target="_blank">
    Set up and test your first payment.
  </Card>

  <Card title="How PayU Hosted Checkout Works" href="https://docs.payu.in/docs/payu-hosted-checkout-workflow" target="_blank">
    Understand the Hosted Checkout flow and key concepts.
  </Card>

  <Card title="Integrate PayU Hosted Checkout" href="https://docs.payu.in/docs/integrate-payu-hosted-checkout" target="_blank">
    Build, test, and prepare your integration for production.
  </Card>
</Cards>