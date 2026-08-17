---
title: Who is Setting This UP?
deprecated: false
hidden: true
metadata:
  robots: index
---
Let us know who is setting up your chosen PayU product:

- I have no developer. I will do it myself → guided setup inline.
- I have a developer who can set it up for me → Send this to your developer
- I will use an AI assistant to integrate the chosen product → Build with AI
- I am confused and not sure how and where to start → guided setup (default) + handoff note

***

## Send This to Your Developer

Share this If a developer, a freelancer, an agency, or a colleague is doing the technical work for you.

### **What to Send**

```
What I want to achieve: [merchant's stated goal]
Where I want to accept payments: [merchant's stated setup]
Recommended PayU solution: [recommended product]
What's needed before starting: [filtered prerequisites from the result]
Technical guide: [link to the specific product's developer documentation]
```

**Getting your developer access to your PayU account**

<Callout icon="⚠️" theme="warn">
  ### \[REQUIRES SECURITY/ENGINEERING VALIDATION — NOT YET RESOLVED]

  This page does not specify how a developer who is not the account owner should obtain or use PayU credentials. Do not instruct merchants to share their Merchant Salt directly until PayU confirms an approved mechanism. This section stays blank until Security signs off — see the validation checklist.
</Callout>

**The technical guide you share with  the developer covers:**

- Sandbox and production credentials, clearly labeled
- Complete, copy-paste, runnable code
- Webhook and callback handling
- Error codes and how to read logs
- A production go-live checklist

[Open the developer documentation →](#)

***

## Build with AI

If you or any developer wants to use an AI assistant such as ChatGPT, Claude, or any other application to help write the code, below prompts are built to keep that assistant grounded in PayU's actual documentation, rather than guessing.

<Callout icon="❗" theme="error">
  ### Review Before You Go Live

  Your AI assistant will write real code from this — review it carefully before using it with real payments, especially anything with credentials or customer data.
</Callout>

***

### Easy to Use Prompts

Use these prompts one after the other.

<Tabs>
  <Tab title="Prompt 1 - core integration">
    ```text Prompt
    Help me integrate [recommended product] into my [platform]. My goal is
    [goal].

    Use the PayU documentation linked below as the authoritative source of
    truth. Do not invent or infer implementation details — endpoints,
    parameters, hashing logic, credentials, security requirements, or
    response fields — that are not present in the documentation. If
    something isn't covered there, tell me instead of guessing.

    Documentation: [link to the specific product's canonical technical guide]
    ```
  </Tab>

  <Tab title="Prompt 2 — success and failure handling">
    ```text Prompt
    Now help me handle the response PayU sends back after a payment attempt,
    using the same rule: rely only on what's in the documentation below, and
    tell me if something isn't covered rather than guessing.

    Documentation: [link to webhooks/callback documentation]
    ```
  </Tab>
</Tabs>

***

### Where the Facts Live

Point your AI assistant (and yourself) at:

- [Prerequisites and credentials](#)
- [API endpoints and request/response structure](#)
- [Hash/signature requirements](#)
- [Security requirements](#)
- [Error codes](#)
- [Testing and test data](#)
- [Production requirements and go-live checklist](#)
