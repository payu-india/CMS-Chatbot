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

<Callout icon="📘" theme="success">
  Accelerate your integration workflow with our Postman collection for Partner Integration. Click the Download Postman Collection button below to download and get started.

  <HTMLBlock>{`
                  <style>
                  .tooltip-btn {
                      position: relative;
                      background-color: #4CAF50;
                      color: white;
                      padding: 10px 20px;
                      border: none;
                      border-radius: 5px;
                      cursor: pointer;
                      font-weight: bold; /* Added this line */
                  }
                  .tooltip-btn:hover::after {
                      content: attr(data-tooltip);
                      position: absolute;
                      bottom: 125%;
                      left: 50%;
                      transform: translateX(-50%);
                      background-color: #333;
                      color: white;
                      padding: 5px 10px;
                      border-radius: 4px;
                      white-space: nowrap;
                      font-size: 12px;
                      z-index: 1;
                  }
                  </style>

                  <button onclick="window.open('https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/collection/8fpyicz/partners-merchant-onboarding-apis', '_blank')" 
                          class="tooltip-btn" 
                          data-tooltip="Click to download the Postman collection and explore APIs.">
                      Access Postman Collection
                  </button>
  `}</HTMLBlock>






</Callout>

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
