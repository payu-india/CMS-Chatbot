---
title: Testing and Go Live - Partner Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
This section includes the Testing and Go Live checklist for Partner Integration onboarding and collect payment after onboarding.

## Test environment

| Resource                       | URL                                        |
| ------------------------------ | ------------------------------------------ |
| Authentication (Get Token API) | `https://uat-accounts.payu.in/oauth/token` |
| Onboarding APIs                | `https://uat-partner.payu.in`              |
| Collect Payment                | `https://test.payu.in`                     |

## Postman collection

Import the collection for onboarding APIs:

<br />

## Go-live checklist

- [ ] Partner Reseller Agreement signed
- [ ] Data Processing Addendum in place
- [ ] Production `resellerToken` obtained
- [ ] Full onboarding flow tested end-to-end
- [ ] Webhook endpoint deployed; **200 OK** within SLA
- [ ] Idempotent webhook handling verified
- [ ] Error handling and retry logic
- [ ] Status polling fallback
- [ ] PII handling compliant (minimize persistent PAN/bank storage)
- [ ] Consent captured at CKYC / DigiLocker / VKYC steps
- [ ] Payment hash generation tested
- [ ] Refund flow tested (full + partial)
- [ ] Production URLs and credentials
