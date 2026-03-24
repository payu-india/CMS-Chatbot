---
title: Testing and Go Live - Partner Integration
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: Testing and go-live
excerpt: >-
  Test URLs, Postman collection, and production checklist for partner integrations.
deprecated: false
hidden: false
metadata:
  title: PayU Partner Testing and Go-Live Checklist
  description: >-
    Test environment endpoints, Postman workspace link, agreements and compliance checklist.
  keywords:
    - PayU partner testing
    - go live PayU partner
  robots: index
---

## Test environment

| Resource | URL |
|----------|-----|
| Onboarding APIs | `https://onboarding.payu.in` (test) |
| Payment | `https://test.payu.in/_payment` |
| Postservice | `https://test.payu.in/merchant/postservice.php` |

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
