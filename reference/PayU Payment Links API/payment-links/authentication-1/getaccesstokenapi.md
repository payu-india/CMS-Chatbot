---
api:
  file: pl-test-oas.yaml
  operationId: GetAccessTokenAPI
hidden: false
---
Use this endpoint to generate and cache the token. You do not have to generate a new token before every API call.&#x20;

Token validity is returned as `expires_in` seconds (typically 7200 — 2 hours). You should Calculate expiry as `created_at + expires_in` and regenerate before that moment.
