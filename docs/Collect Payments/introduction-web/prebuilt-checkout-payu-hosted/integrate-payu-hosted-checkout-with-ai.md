---
title: Integrate PayU Hosted Checkout with AI
excerpt: >-
  Integrate PayU Hosted Checkout (web redirect) into your Java, Node.js, PHP, or
  Python backend in one prompt. An AI coding skill that fetches live PayU docs,
  generates hash logic, callback handlers, and the Verify Payment call, with
  credentials and secrets fully protected.
deprecated: false
hidden: true
metadata:
  robots: index
---


The **PayU Hosted Checkout AI skill** is a prompt you load into Claude Code, Cursor, or any MCP-enabled AI coding assistant. It automatically detects your backend stack, fetches the latest integration code and hash formulas from the [PayU Developer MCP](doc:payu-devguide-builder-mcp-configuration), and scaffolds a complete PayU Hosted Checkout integration — including security, callbacks, and payment verification — adapted to your existing codebase.

<Callout icon="🔒" theme="error">
  ### **Important: Security-first design**

  The skill is hardcoded never to touch your `.env` file, never to log or echo your merchant key or salt, and never to call any live PayU API. It only queries the PayU docs MCP. Your credentials never leave your environment.
</Callout>

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
