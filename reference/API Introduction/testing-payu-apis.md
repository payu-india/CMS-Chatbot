---
title: Testing PayU APIs
deprecated: false
hidden: true
metadata:
  robots: index
---
Always integrate against PayU **Test** before Production. Testing validates hash generation, callbacks, Verify Payment, and product-specific edge cases without moving real money.

## Testing workflow

```
Create Test credentials
→ Pick Test base URL
→ Use test instruments
→ Call APIs / Try It / Postman
→ Validate callbacks + reverse hash
→ Run Verify Payment
→ Complete go-live checklist
```

## 1. Test credentials and environments

- Generate Test key and salt from the Dashboard: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
- Use Test hosts from [API Environments and Base URLs](doc:api-environments-and-base-urls)
- Do not mix Production keys with Test URLs (or the reverse)

## 2. Test payment instruments

For checkout and Collect Payment testing, use only documented test instruments:

- [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets)

Product-specific fixtures may also exist (for example, EMI test cards/wallets in custom blocks used by Affordability docs).

## 3. API Reference Try It playground

Most API Reference pages support interactive calls:

1. Open an operation from [API Reference](ref:introduction-api-reference).
2. Fill required parameters.
3. Generate hash when prompted.
4. Click **Try It**.
5. Inspect response and copy language bindings as needed.

### Try It limitations

PayU currently does not fully support Test/Try It for all flows. Examples include certain refund flows, some UPI S2S flows, selected subscription UPI flows, some Save Cards Model 2 flows, TPV, parts of Split Settlements, and Omnichannel.

See the limitations callout on [PayU India API Reference](ref:introduction-api-reference).

## 4. Postman and local testing

- Use Postman collections where available — start with [SDKs, Postman, and Tools](doc:sdks-postman-and-tools).
- For cURL mechanics, see the [cURL Walkthrough recipe](https://payu-hosted-checkout.readme.io/v1/recipes/curl-walkthrough).
- Keep secrets in Postman environments, not shared collections.

## 5. What to validate in Test

| Area          | Validate                                             |
| :------------ | :--------------------------------------------------- |
| Auth          | Correct hash/token per API family                    |
| Idempotency   | Unique `txnid` per attempt                           |
| Callbacks     | `surl`/`furl` reachability and reverse hash          |
| Webhooks      | Event receipt, signature checks, duplicate handling  |
| Status truth  | Verify Payment matches final business state          |
| Failure paths | Declines, cancelled payments, missing params         |
| Refunds       | Full/partial refund behavior where supported in Test |

## 6. Go-live readiness

Before switching to Production:

- Replace Test host, key, and salt together
- Re-run smoke tests on Production credentials in a controlled manner
- Confirm webhook URLs and HTTPS certificates
- Follow product Integration Checklists in Collect Payments / SDK guides

Related: [API Best Practices](doc:api-best-practices)

## What to read next

- [Making Your First API Request](doc:making-your-first-api-request)
- [Error Handling for APIs](doc:error-handling-for-apis)
- [API Troubleshooting](doc:api-troubleshooting)
- [Using PayU Hash Verification Tool](doc:using-payu-hash-verification-tool)

## Related APIs

- [Collect Payment API — PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
- [Verify Payment API](ref:verify_payment_api)
- [Create Payment Link API](ref:create-payment-links)
