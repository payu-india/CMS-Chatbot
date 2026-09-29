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

Go through every path available to use AI with PayU Payment Links. Pick the one that matches what you are trying to build, follow the steps in order, and you will have a working integration at the end.

***

## Which Path Are You On?

| I want to…                                                                 | Path                   | Time to live |
| -------------------------------------------------------------------------- | ---------------------- | ------------ |
| Write backend code that creates links automatically when orders come in    | **Direct API**         | \~2 hours    |
| Connect Claude, ChatGPT, or a custom agent to manage links by conversation | **AI Agent via MCP**   | \~20 minutes |
| Use an AI assistant to help me create and manage links — no code           | **Merchant / No-code** | \~5 minutes  |

<Callout icon="📘" theme="info">
  ### **Note:**

  These paths are not mutually exclusive. Many teams use Path 1 for automated backend flows and Path 2 for the merchant-facing assistant layer. Start with the one you need first.
</Callout>

***

## Developer: Direct API Integration

Build a backend service that creates payment links, delivers them to customers, and receives payment confirmation via webhook.

### Get your credentials first

Before writing any code, grab these three values from **PayU Dashboard → Settings → API Keys**:

| Credential           | Where to find it                                |
| -------------------- | ----------------------------------------------- |
| `PAYU_CLIENT_ID`     | Dashboard → Settings → API Keys → Client ID     |
| `PAYU_CLIENT_SECRET` | Dashboard → Settings → API Keys → Client Secret |
| `PAYU_MERCHANT_ID`   | Dashboard → Settings → Merchant ID              |

Set `PAYU_ENVIRONMENT` to `test` to start — no real money moves in UAT. Switch to `production` only when you are ready to go live.

<Callout icon="🚧" theme="warning">
  **PAYU_CLIENT_SECRET is not your merchant salt.** It is the OAuth credential from API Keys — a different value. It serves double duty: it authenticates your API calls and verifies your webhooks. Using the wrong one breaks webhook verification silently.
</Callout>

### Steps

| Step | What to build                                                                                                 | Full reference                                        |
| ---- | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| 1    | Acquire an OAuth2 Bearer token and cache it — tokens expire in 3,600s, never request one per call             | [Authentication (Token)](doc:api-auth-token)          |
| 2    | Build a backend endpoint that calls `POST /payment-links/` and returns the shareable link and `invoiceNumber` | [Create & Share a Payment Link](doc:api-create-share) |
| 3    | Build a webhook endpoint that verifies the SHA-512 signature and marks orders as paid on `status=success`     | [Webhook Notifications](doc:webhook-notifications)    |
| 4    | Register your webhook URL in PayU Dashboard → Settings → Webhooks                                             | [Webhook Notifications](doc:webhook-notifications)    |
| 5    | Test end-to-end using UAT credentials — create a link, pay, confirm the webhook fires                         | [Key & Salt Reference](doc:key-salt-reference)        |

### Fastest path to implementation

Instead of building from scratch, paste the ready-made coding agent prompt from [AI Coding Assistants](doc:use-with-ai) into Cursor, Claude Code, or GitHub Copilot. Fill in your three credentials at the top and the AI writes the entire integration — token cache, create endpoint, webhook handler — for your existing stack in one shot.

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
