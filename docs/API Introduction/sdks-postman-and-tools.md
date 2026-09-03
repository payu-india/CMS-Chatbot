---
title: SDKs, Postman, and Tools
excerpt: >-
  Discover PayU mobile SDKs, server SDKs, Postman collections, hash tools, MCP,
  and CLI utilities that accelerate API integration.
deprecated: false
hidden: false
metadata:
  title: PayU SDKs, Postman Collections, and Developer Tools
  description: >-
    Explore PayU developer tools — Android, iOS, React Native, Flutter SDKs,
    Postman collections, hash verification, MCP server, and PayU CLI.
  keywords:
    - PayU SDK
    - PayU Postman collection
    - PayU hash tool
    - PayU mobile SDK
    - PayU MCP
    - PayU CLI
  robots: index
next:
  description: ''
---
PayU provides SDKs and tooling so you can integrate faster than raw API calls alone. Use APIs for control; use SDKs and collections to accelerate common paths.

## Mobile SDKs

| Platform | Start here |
| :------- | :--------- |
| Android | [Explore Android SDKs](doc:explore-android-sdks) |
| iOS | [Explore iOS SDKs](doc:explore-ios-sdks) |
| React Native | [Explore React Native SDKs](doc:explore-reactnative-sdks) |
| Flutter | [Flutter SDK introduction](doc:flutter-sdk-introduction) |
| Cordova | [Cordova SDK introduction](doc:cordova-sdk-introduction) |

For return-URL handling with mobile SDKs, see [Handling Mobile SDK Checkout](doc:handling-mobile-sdk-checkout).

## Server and helper SDKs

* **PayU Node SDK** — useful for hash/reverse-hash helpers: [payu-sdk-node on GitHub](https://github.com/payu-india/payu-sdk-node)
* Language bindings are also available from many API Reference **Try It** pages (multiple language snippets besides cURL)

## Postman collections

Postman is ideal for:

* Exploring Collect Payment and General APIs
* Sharing Test environment variables safely across your team
* Validating hash generation before coding

Hosted Checkout collection entry point (custom block / workspace link used across docs):

* Access from pages that embed `<Postman_collection />`, or open the PayU Integration Postman workspace linked in those docs
* Partner flows may include a dedicated partner Postman guide in custom blocks

See also recipes:

* [cURL Walkthrough](https://payu-hosted-checkout.readme.io/v1/recipes/curl-walkthrough)
* [Basics of cURL](https://payu-hosted-checkout.readme.io/v1/recipes/basics-of-curl)

## Hash generation and verification tools

| Tool | Purpose |
| :--- | :------ |
| [Generate Hash](doc:hashing-request-and-response) | Canonical hash and reverse-hash documentation |
| [Using PayU Hash Verification Tool](doc:using-payu-hash-verification-tool) | Verify callback hashes during debugging |
| API Reference **Generate Hash** controls | Build hashes while using Try It |

## MCP and CLI

For AI-assisted and command-line developer workflows:

* [PayU Remote MCP Server Integration](doc:payu-remote-mcp-server-integration)
* [PayU DevGuide Builder MCP Configuration](doc:payu-devguide-builder-mcp-configuration)
* [PayU CLI](doc:payu-cli)

## API Reference playground

The [API Reference](ref:introduction-api-reference) is itself a tool:

* Interactive Try It requests in Test
* Multi-language code samples
* Per-operation parameter documentation

## When to use which tool

| Situation | Recommended tool |
| :-------- | :--------------- |
| First API exploration | API Reference Try It + Postman |
| Mobile app checkout | Platform SDK |
| Hash debugging | Hash verification tool + Generate Hash docs |
| Automation / scripting | cURL, CLI, server SDK helpers |
| Ask AI / agentic docs workflows | MCP server + this API Introduction section |

## What to read next

* [Making Your First API Request](doc:making-your-first-api-request)
* [Testing PayU APIs](doc:testing-payu-apis)
* [API Best Practices](doc:api-best-practices)
* [API Reference](ref:introduction-api-reference)

## Related APIs

* [Collect Payment API — PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
* [Verify Payment API](ref:verify_payment_api)
* [Generate Token using Merchant's Credentials API](ref:generate-token-using-merchants-credentials-api)
