---
title: Versioning
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU uses a **capability-driven versioning model**. Unlike a single global `/v1` surface for every product, versioning appears as:

- an `api_version` request parameter on many Collect Payment flows
- path-based versions for selected APIs (for example, `/v2/payments`)
- feature-specific request fields that change hash formulas

## Versioning Mechanisms

| Mechanism                        | Where you see it                                      | What it controls                                        |
| :------------------------------- | :---------------------------------------------------- | :------------------------------------------------------ |
| `api_version`**&#x20;parameter** | `_payment` and related checkout/subscription requests | Enables fields and behaviors for a given capability set |
| **URL path version**             | e.g. `https://api.payu.in/v2/payments`                | Selects a distinct API contract                         |
| **Feature payload fields**       | `si_details`, `splitRequest`, offers fields, etc.     | Adds required hash segments and validation rules        |

## Using `api_version` with Collect Payment

Some integrations require a specific `api_version` value. Examples commonly seen in docs include values such as `7` or `19`, depending on the feature.

<Accordion title="Rules of Thumb" icon="far fa-circle-user-circle-minus">
  - Set `api_version` exactly as required by the Integration Guide / API Reference for that feature.

  - Regenerate `hash` after including version-dependent fields.

  - Do not assume a newer number is always better — use the version documented for your flow.
</Accordion>

<Accordion title="Example: hash changes with version 19" icon="far fa-exclamation">
  For `_payment` with `api_version=19`, hash input expands to include additional fields such as `udf6…udf10`, `user_token`, offer fields, cart details, extra charges, and phone.
</Accordion>

Refer to [API Authentication and Security](doc:api-authentication-and-security) and [Generate Hash](doc:hashing-request-and-response) for more information.

## Path-Based Versions

Selected products expose versioned hosts/paths:

<Tabs>
  <Tab title="Test">
    `https://apitest.payu.in/v2/payments`
  </Tab>

  <Tab title="Production">
    `https://api.payu.in/v2/payments`
  </Tab>
</Tabs>

When an API is on a versioned path, treat it as a separate contract. Different auth, headers, or response shapes may apply.

## How to Choose the Correct Version

<Accordion title="Decision Table" icon="far fa-table">
  | Question                                         | Action                                                           |
  | :----------------------------------------------- | :--------------------------------------------------------------- |
  | Does my Integration Guide specify `api_version`? | Use that exact value                                             |
  | Does the API Reference path include `/v2/`?      | Use the v2 base URL and schema                                   |
  | Am I enabling SI, split, offers, or TPV fields?  | Confirm whether hash formula changes                             |
  | Am I copying an old sample?                      | Different required fields against the current API Reference page |
</Accordion>