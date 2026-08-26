---
title: Testing and Go Live - Partner Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
## Test environment

| Resource                       | URL                                        |
| ------------------------------ | ------------------------------------------ |
| Authentication (Get Token API) | `https://uat-accounts.payu.in/oauth/token` |
| Onboarding APIs                | `https://uat-partner.payu.in`              |
| Collect Payment API            | `https://test.payu.in/_payment`            |
|                                |                                            |

## Postman collection

Import the collection for onboarding APIs (link from PayU Postman workspace: Partners - Merchant Onboarding APIs).

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
