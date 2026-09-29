---
title: AI Assistance to Create a Payment Link
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
  message="Integration effort: No code required for Ask AI · MCP setup required for agent automation"
  color="#6B21A8"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

These are the two ways to use AI to create a Payment Link. Choose based on how much automation you want.

|                    | Ask AI                               | AI Agent (Remote MCP)                                |
| ------------------ | ------------------------------------ | ---------------------------------------------------- |
| **What you do**    | Type a question, follow the guidance | Give a single natural language instruction           |
| **What happens**   | AI guides you through the Dashboard  | Agent creates the link for you — no Dashboard needed |
| **Setup required** | None                                 | Remote MCP server connection                         |
| **Best for**       | Occasional use, learning the product | High-volume or workflow-embedded link creation       |

***

## Option 1: Ask AI for Guidance

The PayU Ask AI chatbot knows the full Payment Links product. Instead of reading the docs, ask it directly — it will walk you through every field, answer edge-case questions, and suggest the right settings for your situation.

<Callout icon="📘" theme="info">
  Access Ask AI from the **Ask AI** button in the PayU documentation or Dashboard. No account or login required for basic queries.
</Callout>

### What to ask

The following prompts work well. Copy them directly or adapt them to your situation.

**To create a standard payment link:**

> "How do I create a payment link for ₹2,500 that I can share with a customer via WhatsApp?"

**To set an expiry:**

> "How do I create a payment link that expires at midnight tonight? What format does the date need to be in?"

**To collect customer details at checkout:**

> "I want my customer to enter their name, email, and GST number before they pay. How do I add those fields to a payment link?"

**To send the link automatically by SMS and email:**

> "Can PayU send the payment link to my customer by SMS and email automatically when I create it?"

**To handle a partial payment:**

> "My customer wants to pay in two instalments. Can I create a payment link that allows partial payment?"

**To limit a link to one use:**

> "How do I make sure a payment link can only be used once, even if I share it multiple times?"

### What Ask AI can do on this topic

Ask AI can explain any Payment Links feature, walk you through Dashboard steps, suggest field values, clarify error messages, and point you to the right documentation. It cannot create links on your behalf — you still complete the action in the Dashboard yourself.

→ [Open Payment Links in the Dashboard](https://onboarding.payu.in/)

***

## Option 2 — AI Agent Creates the Link for You

If you connect an AI assistant (Claude, ChatGPT, or any MCP-compatible agent) to the PayU Remote MCP server, you can create a payment link with a single natural language message — no Dashboard, no form-filling.

<Callout icon="🔑" theme="warning">
  This requires the PayU Remote MCP server to be configured with your merchant credentials. See [PayU Remote MCP Server Integration](doc:payu-remote-mcp-server-integration) for setup steps.
</Callout>

### How it works

Once the Remote MCP is connected, you type a plain-language instruction into your AI assistant. The agent extracts the details, calls the PayU API, and returns the payment link URL — ready to share.

### Sample instructions

**Standard link:**

> "Create a payment link for ₹5,000 for customer Priya Sharma, email [priya@example.com](mailto:priya@example.com), phone +919876543210. Description: Invoice #INV-2026-042. Expires 31 December 2026."

**Quick invoice:**

> "Make a ₹1,200 payment link for Rahul for his October subscription. No expiry."

**Variable amount (customer enters the amount):**

> "Create an open-amount donation link for our NGO campaign. Description: Support a Child's Education."

**With partial payment:**

> "Create a ₹15,000 payment link for Ananya for interior design work. Allow partial payments."

### What the agent returns

The agent confirms the created link and hands back the shareable URL:

```
Payment link created successfully.
Link: https://pp72.pmny.in/AbCdEfGhIjKl
Invoice Number: INV-2026-042
Amount: ₹5,000
Expires: 2026-12-31 23:59:59
Status: Active

Share this URL with your customer to collect payment.
```

### What the agent can do with Payment Links

Once connected, the agent can create, share, fetch status, and deactivate payment links — all from natural language instructions in the same conversation.

| Instruction                              | What happens                                |
| ---------------------------------------- | ------------------------------------------- |
| "Create a link for ₹X for \[customer]"   | Creates the link                            |
| "Send the link to \[email] and \[phone]" | Shares via SMS and email                    |
| "What's the status of invoice INV-001?"  | Fetches current status and amount collected |
| "Cancel the link for INV-001"            | Deactivates the link                        |

→ [Set up the Remote MCP Server](doc:payu-remote-mcp-server-integration)

***

## Which Option Is Right for You?

Use **Ask AI** if you create payment links occasionally and want guidance without any setup. It answers questions, explains fields, and makes sure you fill in everything correctly — you stay in control of the Dashboard.

Use the **AI Agent** if you create payment links frequently, want to embed link creation inside a customer-facing chatbot or workflow, or simply want to type one sentence and get a ready-to-share link back. It requires a one-time Remote MCP setup but saves every click after that.

***

## Related Pages

<Cards>
  <Card title="Manage Payment Links" href="doc:manage-payment-links" icon="fa-list-check">
    View, duplicate, share, and export links from the Dashboard.
  </Card>

  <Card title="Payment Link Options" href="doc:payment-link-options" icon="fa-sliders">
    Expiry, partial payments, custom fields, and more.
  </Card>

  <Card title="Remote MCP Server Integration" href="doc:payu-remote-mcp-server-integration" icon="fa-robot">
    Connect an AI agent to your PayU account.
  </Card>

  <Card title="Payment Links FAQs" href="doc:payment-links-faqs" icon="fa-circle-question">
    Common questions answered.
  </Card>
</Cards>
