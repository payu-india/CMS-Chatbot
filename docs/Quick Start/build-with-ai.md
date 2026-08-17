---
title: Build with AI
excerpt: >-
  Give your AI assistant the right prompt and point it at PayU's official
  documentation as the source of truth.
deprecated: false
hidden: true
metadata:
  robots: index
---
Any developer wants to use an AI assistant — ChatGPT, Claude, or Gemini — to help write the code, below prompts built to keep that assistant grounded in PayU's actual documentation, rather than guessing.

<Callout icon="❗" theme="error">
  ### Review Before You Go Live

  Your AI assistant will write real code from this — review it carefully before using it with real payments, especially anything with credentials or customer data.
</Callout>

***

## Easy to Use prompts

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

## Where the Facts Live

This page intentionally does not restate PayU's technical reference — that content is maintained in one place so it can't drift out of sync. Point your AI assistant (and yourself) at:

- [Prerequisites and credentials](#)
- [API endpoints and request/response structure](#)
- [Hash/signature requirements](#)
- [Security requirements](#)
- [Error codes](#)
- [Testing and test data](#)
- [Production requirements and go-live checklist](#)
