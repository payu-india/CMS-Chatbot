---
title: Making Your First API Request
deprecated: false
hidden: true
metadata:
  robots: index
---
Go through this guide and make your first successful PayU API call in the test environment.

## Workflow overview

```
1. Get Test key + salt
2. Choose API and base URL
3. Generate hash (or OAuth token)
4. Send request
5. Handle response / redirect
6. Verify payment server-to-server
```

## Step 1 — Get Test credentials

1. Sign in to the PayU Dashboard.
2. Generate or copy your **Test** merchant key and salt.
3. Keep the salt on your server only.

References:

- [Generate Merchant Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard)
- [API Authentication and Security](doc:api-authentication-and-security)

## Step 2 — Choose your first API

| Goal                             | First API                    | Base URL (Test)                                        |
| :------------------------------- | :--------------------------- | :----------------------------------------------------- |
| Create a hosted checkout payment | Collect Payment (`_payment`) | `https://test.payu.in/_payment`                        |
| Confirm an existing payment      | Verify Payment (General API) | `https://test.payu.in/merchant/postservice.php?form=2` |

If you are unsure which product fits, start with [Which API should I use?](doc:which-api-should-i-use).

## Step 3 — Generate authentication

### For Collect Payment / General APIs

Compute a SHA-512 hash on your server.

**Collect Payment hash (standard):**

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
```

**Verify Payment / General API hash:**

```
sha512(key|command|var1|salt)
```

Deep dive: [Generate Hash](doc:hashing-request-and-response).

### For Payouts / Partner APIs

Generate an OAuth token first, then call the resource API. See [Generate Token using Merchant's Credentials API](ref:generate-token-using-merchants-credentials-api).

## Step 4 — Send a Test Collect Payment request

Example shape for PayU Hosted Checkout:

```bash
curl -X POST 'https://test.payu.in/_payment' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=<YOUR_TEST_KEY>' \
  --data-urlencode 'txnid=<UNIQUE_TXNID>' \
  --data-urlencode 'amount=10.00' \
  --data-urlencode 'productinfo=Test Product' \
  --data-urlencode 'firstname=Ashish' \
  --data-urlencode 'email=test@example.com' \
  --data-urlencode 'phone=9999999999' \
  --data-urlencode 'surl=https://example.com/success' \
  --data-urlencode 'furl=https://example.com/failure' \
  --data-urlencode 'hash=<YOUR_HASH>'
```

Use only [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) in Test.

API Reference: [Collect Payment — PayU Hosted Checkout](ref:_payment_payu_hosted_checkout).

## Step 5 — Handle redirect or API response

Depending on integration type:

| Integration           | What happens next                                                                     |
| :-------------------- | :------------------------------------------------------------------------------------ |
| Hosted Checkout       | Customer completes payment on PayU; browser returns to `surl` / `furl`                |
| Merchant Hosted / S2S | You receive API responses and may need additional auth steps (OTP, intent, bank page) |

Always:

1. Parse the callback/response on your server.
2. Verify reverse hash.
3. Do **not** mark an order paid from frontend alone.

Related:

- [Handling Web Checkout](doc:handling-web-checkout)
- [Webhooks and Callbacks](doc:webhooks-and-callbacks)

## Step 6 — Verify payment status

Call Verify Payment with the merchant `txnid`:

```bash
curl -X POST 'https://test.payu.in/merchant/postservice.php?form=2' \
  -d 'key=<YOUR_TEST_KEY>' \
  -d 'command=verify_payment' \
  -d 'var1=<TXNID>' \
  -d 'hash=<YOUR_HASH>'
```

API Reference: [Verify Payment API](ref:verify_payment_api).

## Try It in API Reference

For many APIs you can use the API Reference **Try It** playground:

1. Open the operation page in [API Reference](ref:introduction-api-reference).
2. Enter required fields.
3. Generate hash where prompted.
4. Click **Try It** and inspect the response.

Note the Test limitations listed on the API Reference introduction page.

## First-request checklist

- [ ] Using Test base URL
- [ ] Using Test key and salt
- [ ] `txnid` is unique
- [ ] Hash formula matches the API family
- [ ] `surl` / `furl` are reachable HTTPS endpoints (for checkout flows)
- [ ] Reverse hash validated on callback
- [ ] Final status confirmed with Verify Payment or webhook + verify

## What to read next

- [Common API Workflows](doc:common-api-workflows)
- [Error Handling for APIs](doc:error-handling-for-apis)
- [Testing PayU APIs](doc:testing-payu-apis)
- [API Best Practices](doc:api-best-practices)

## Related APIs

- [Collect Payment API — PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
- [Verify Payment API](ref:verify_payment_api)
- [Create Payment Link API](ref:create-payment-links)
