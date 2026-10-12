---
title: BNPL Link & Pay - Merchant Hosted
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: BNPL Link and Pay (Merchant Hosted)
excerpt: >-
  Enable one-click BNPL checkout. Customers link their BNPL account with an OTP
  on the first payment, and repeat payments go through without an OTP.
deprecated: false
hidden: true
metadata:
  title: BNPL Link and Pay One-Click Checkout | PayU Docs
  description: >-
    Integrate PayU BNPL Link and Pay: check eligibility and linking status, pay
    with linkAndPayFlowType=1 and txn_s2s_flow=4, handle OTP fallback, pass
    payuToken for repeat payments, and de-link accounts.
  keywords:
    - payu bnpl link and pay
    - lazypay one click checkout payu
    - bnpl otp-less repeat payment
    - linkAndPayFlowType payu
    - payu bnpl payuToken store_card_token
    - get_emi_checkout_details link and pay eligibility
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: bnpl-merchant-hosted-integration
      title: BNPL with Merchant Hosted Checkout
      type: basic
    - slug: bnpl-test-integration
      title: Test BNPL Integration
      type: basic
    - slug: bnpl-errors-and-troubleshooting
      title: BNPL Errors and Troubleshooting
      type: basic
---
<Banner
  isInline={true}
  message="Integration effort: Moderate — server-side integration required"
  color="#FF9800"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
 />

Link and Pay gives returning customers one-click BNPL checkout. On the first payment, the customer authenticates with an OTP and their BNPL account (for example, LazyPay) is linked to your merchant account. Later payments are debited from the linked account without an OTP, as long as the link is still valid.

<Callout icon="📘" theme="info">
  ### **API References:**

  - [Link and Pay Eligibility API](ref:get_emi_checkout_details)
  - [Collect Payment API (Merchant Hosted)](ref:collect-payments-with-merchant-hosted-checkout)
  - [Delete Payment Instrument API](ref:delete_payment_instrument)
  - [Verify Payment API](ref:verify_payment_api)
</Callout>

{/* REVIEW: Confirm the reference slugs above before publishing. */}

***

## Prerequisites

- **Link and Pay approval:** Link and Pay is enabled only after approval from PayU and the lender. Contact your PayU Key Account Manager.
- **BNPL enabled** on your merchant account, with the lender you want to offer.
- A working [Merchant Hosted BNPL integration](doc:bnpl-merchant-hosted-integration), including native OTP handling (`otpPostUrl` / `acsTemplate`).
- A stable customer identifier to use in `user_credentials` (`merchantKey:userIdentifier`).

***

## Overview of Steps

1. [Check eligibility and linking status](#step-1-check-eligibility-and-linking-status).
2. [Prepare the payment request and hash](#step-2-prepare-the-payment-request-and-hash).
3. [Post the payment request](#step-3-post-the-payment-request).
4. [Handle the response](#step-4-handle-the-response): OTP for first-time or fallback payments, direct debit for repeat payments.
5. [Verify the response and the payment](#step-5-verify-the-response-and-the-payment).
6. [Let customers de-link their account](#step-6-de-link-a-bnpl-account-optional) (optional).

<Cards columns="3">
  <Card title="1. Check Eligibility" href="#step-1-check-eligibility-and-linking-status">
    Find out whether the customer is eligible and already linked.
  </Card>

  <Card title="2. Initiate Payment" href="#step-3-post-the-payment-request">
    Post `_payment` with `linkAndPayFlowType=1` and `txn_s2s_flow=4`.
  </Card>

  <Card title="3. Handle OTP or Debit" href="#step-4-handle-the-response">
    Submit the OTP when PayU asks for it. Otherwise, process the final result.
  </Card>
</Cards>

***

## Build Integration Steps

### Step 1: Check Eligibility and Linking Status

Call the Link and Pay eligibility API from your server before you show BNPL. For each lender, it tells you whether the customer is eligible, whether they're already linked, and gives you their `payuToken` if they're linked.

<Accordion title="Eligibility API Details" icon="fa-server">
  #### Environment

  |                |                                                                       |
  | -------------- | --------------------------------------------------------------------- |
  | **Test**       | `<redacted URL>`        |
  | **Production** | `https://info.payu.in/linkAndPay/get_emi_checkout_details`            |

  {/* REVIEW: Production eligibility URL isn't confirmed in Confluence. Get Product/Engineering to confirm before publishing. */}

  #### Request Parameters

  | Parameter                         | Description                                                                                                                         | Example              |
  | --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
  | `amount` <br />_mandatory_        | `number` Transaction amount.                                                                                                        | `21`                 |
  | `userCredentials` <br />_mandatory_ | `string` Customer identifier in the format `merchantKey:userIdentifier`.                                                          | `yFbXg3:test_sud`    |
  | `phone` <br />_conditional_       | `string` Customer's 10-digit mobile number. **You must send either `phone` or `payuToken`.** You can send both.                    | `9999999999`         |
  | `payuToken` <br />_conditional_   | `string` Token of a linked BNPL account. **You must send either `phone` or `payuToken`.**                                          | `8891bb01498a2f6750b9d` |
  | `bankCode` <br />_optional_       | `string` Filters the response to one lender. Pass `null` (or leave it out) to get every BNPL lender enabled on your account.        | `LAZYPAY`            |
  | `requestId` <br />_optional_      | `string` Your reference for tracing the request.                                                                                    | `Testing_111`        |

  <Callout icon="📘" theme="info">
    ### **Validation Behaviour**

    - `userCredentials` + `phone`: returns every enabled lender with its eligibility and linking status.
    - `userCredentials` + `phone` + `bankCode`: returns that lender only. The combination must match the saved details.
    - `userCredentials` + `payuToken`: returns the lender linked to that token.
    - If you send `bankCode`, it must be enabled on your account. Otherwise, you get an error.
  </Callout>

  #### Sample Request

  ```bash
  curl --location --request POST '<redacted URL>' \
  --header 'Authorization: hmac username="yFbXg3", algorithm="sha512", headers="date", signature="<HMAC_SIGNATURE>"' \
  --header 'date: Thu, 21 Aug 2025 10:22:41 GMT' \
  --header 'x-credential-username: yFbXg3' \
  --header 'Content-Type: application/json' \
  --data '{
    "amount": 21,
    "userCredentials": "yFbXg3:test_sud",
    "phone": "9999999999",
    "bankCode": null,
    "payuToken": null,
    "requestId": "Testing_111"
  }'
  ```
  ```python
  import requests

  url = "<redacted URL>"
  headers = {
      "Authorization": 'hmac username="yFbXg3", algorithm="sha512", headers="date", signature="<HMAC_SIGNATURE>"',
      "date": "Thu, 21 Aug 2025 10:22:41 GMT",
      "x-credential-username": "yFbXg3",
      "Content-Type": "application/json",
  }
  payload = {
      "amount": 21,
      "userCredentials": "yFbXg3:test_sud",
      "phone": "9999999999",
      "bankCode": None,
      "payuToken": None,
      "requestId": "Testing_111",
  }
  response = requests.post(url, headers=headers, json=payload)
  print(response.json())
  ```

  For how to generate the HMAC `signature`, see the [API reference](ref:get_emi_checkout_details).

  #### Sample Response

  ```json
  {
    "httpCode": "200",
    "message": "",
    "status": 1,
    "data": {
      "pg": {
        "BNPL": {
          "bankCode": {
            "LAZYPAY": {
              "phone": "9999999999",
              "payuToken": "8891bb01498a2f6750b9d",
              "kfsLink": "",
              "isLinked": true,
              "isEligible": true,
              "linkFailureReason": null,
              "eligibilityFailureReason": null,
              "availableBalance": null
            },
            "SIMPL": {
              "phone": "9999999999",
              "payuToken": null,
              "kfsLink": "",
              "isLinked": false,
              "isEligible": false,
              "linkFailureReason": "Never Linked",
              "eligibilityFailureReason": "Clear your previous dues on the SIMPL to Proceed",
              "availableBalance": null
            }
          }
        }
      }
    }
  }
  ```

  #### Response Fields

  | Field                      | Description                                                                         |
  | -------------------------- | ----------------------------------------------------------------------------------- |
  | `isEligible`               | Whether the customer can pay with this lender now.                                  |
  | `isLinked`                 | Whether the customer's account with this lender is already linked.                  |
  | `payuToken`                | Token of the linked account. Store it against the customer for repeat payments.     |
  | `kfsLink`                  | The lender's Key Fact Statement link, if provided. Show it to the customer.         |
  | `availableBalance`         | Available credit, if the lender provides it.                                        |
  | `eligibilityFailureReason` | Message you can show the customer when `isEligible=false`.                          |
  | `linkFailureReason`        | Why the account isn't linked, for example, `Never Linked` or `Token Expired. Relink Required`. |
</Accordion>

**Decide what to show:**

| `isEligible` | `isLinked` | What to show                                                                                       |
| ------------ | ---------- | -------------------------------------------------------------------------------------------------- |
| `true`       | `true`     | The lender as a one-click option. Pay with `payuToken` (an OTP may still be needed as a fallback). |
| `true`       | `false`    | The lender with a "Link and pay" prompt. The first payment needs an OTP.                           |
| `false`      | any        | Hide the lender, or show it as disabled with `eligibilityFailureReason`.                           |

**Checkpoint:** ✅ You show only eligible lenders, and you know whether each customer is linked.

***

### Step 2: Prepare the Payment Request and Hash

Use the [Merchant Hosted mandatory parameters](doc:bnpl-merchant-hosted-integration#step-2-prepare-payment-request-parameters), plus these Link and Pay parameters:

| Parameter                              | Description                                                                                                 | Example          |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------- |
| `pg` <br />_mandatory_                 | `string` Use `BNPL`.                                                                                        | `BNPL`           |
| `bankcode` <br />_mandatory_           | `string` Lender code.                                                                                       | `LAZYPAY`        |
| `txn_s2s_flow` <br />_mandatory_       | `string` Must be `4`.                                                                                       | `4`              |
| `linkAndPayFlowType` <br />_mandatory_ | `string` Must be `1` for Link and Pay, for first-time and repeat payments alike.                            | `1`              |
| `user_credentials` <br />_mandatory_   | `string` The same `merchantKey:userIdentifier` you used in the eligibility check.                           | `a4vGC2:SLP3`    |
| `phone` <br />_mandatory_              | `string` The customer's linked or to-be-linked mobile number. Must match the eligibility check.             | `9999999999`     |
| `store_card_token` <br />_repeat payments_ | `string` The `payuToken` from the eligibility response. Pass it when the customer is already linked.    | `8891bb01498a2f6750b9d` |

The hash formula is the same as a standard payment:

```Text Logic
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
```

For code samples, see [Generate Secure Hash](doc:bnpl-merchant-hosted-integration#step-3-generate-secure-hash).

***

### Step 3: Post the Payment Request

#### Environment

|                |                                   |
| -------------- | --------------------------------- |
| **Test**       | `<redacted URL>`   |
| **Production** | `https://secure.payu.in/_payment` |

<Tabs>
  <Tab title="First-Time Payment (Not Linked)">
    ```bash
    curl --location --request POST '<redacted URL>' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'key=a4vGC2' \
    --data-urlencode 'txnid=my_order_30827' \
    --data-urlencode 'amount=500.00' \
    --data-urlencode 'productinfo=productinfo' \
    --data-urlencode 'firstname=Payu-Admin' \
    --data-urlencode 'lastname=User' \
    --data-urlencode 'email=test@example.com' \
    --data-urlencode 'phone=9999999999' \
    --data-urlencode 'pg=BNPL' \
    --data-urlencode 'bankcode=LAZYPAY' \
    --data-urlencode 'txn_s2s_flow=4' \
    --data-urlencode 'linkAndPayFlowType=1' \
    --data-urlencode 'user_credentials=a4vGC2:SLP3' \
    --data-urlencode 'surl=https://your-surl.com' \
    --data-urlencode 'furl=https://your-furl.com' \
    --data-urlencode 'hash=YOUR_GENERATED_HASH'
    ```
  </Tab>

  <Tab title="Repeat Payment (Linked)">
    ```bash
    curl --location --request POST '<redacted URL>' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'key=a4vGC2' \
    --data-urlencode 'txnid=my_order_30828' \
    --data-urlencode 'amount=500.00' \
    --data-urlencode 'productinfo=productinfo' \
    --data-urlencode 'firstname=Payu-Admin' \
    --data-urlencode 'lastname=User' \
    --data-urlencode 'email=test@example.com' \
    --data-urlencode 'phone=9999999999' \
    --data-urlencode 'pg=BNPL' \
    --data-urlencode 'bankcode=LAZYPAY' \
    --data-urlencode 'txn_s2s_flow=4' \
    --data-urlencode 'linkAndPayFlowType=1' \
    --data-urlencode 'user_credentials=a4vGC2:SLP3' \
    --data-urlencode 'store_card_token=8891bb01498a2f6750b9d' \
    --data-urlencode 'surl=https://your-surl.com' \
    --data-urlencode 'furl=https://your-furl.com' \
    --data-urlencode 'hash=YOUR_GENERATED_HASH'
    ```
  </Tab>
</Tabs>

***

### Step 4: Handle the Response

Always read `metaData.txnStatus` and `result` to decide the next step. **Don't assume a repeat payment skips the OTP.**

| Response                                                              | Meaning                                       | What to do                                                                                    |
| --------------------------------------------------------------------- | --------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `txnStatus=pending` + `otpPostUrl`                                    | OTP required (first payment or fallback)      | Show your OTP screen and submit the OTP to `otpPostUrl` with `referenceId`.                   |
| `txnStatus=pending` + `acsTemplate` only                              | OTP or linking on PayU's or the lender's page | Base64-decode `acsTemplate` and render it. This is expected on a customer's first Simpl payment. |
| Final result (`statusCode=E000`, `result.status=success`)             | Payment completed without an OTP              | Verify the reverse hash and confirm the order.                                                |
| `txnStatus=failed` / non-`E000` `statusCode`                          | Payment failed                                | Show an error and offer another payment method. See [error codes](doc:bnpl-errors-and-troubleshooting). |

{/* REVIEW: Add a confirmed sample response for an OTP-less repeat debit from a sandbox run. */}

<Accordion title="Submit the OTP (First-Time or Fallback)" icon="fa-key">
  ```json _payment Response — OTP Required
  {
    "metaData": {
      "message": null,
      "referenceId": "748e033af87f1bb7b6aefd405bec9473",
      "statusCode": null,
      "txnId": "my_order_30827",
      "txnStatus": "pending",
      "unmappedStatus": "pending"
    },
    "result": {
      "acsTemplate": "PGh0bWw+PGJvZHk+...",
      "otpPostUrl": "<redacted URL>"
    }
  }
  ```

  Submit the OTP to the `otpPostUrl` you received:

  ```bash
  curl --location --request POST '<otpPostUrl from the _payment response>' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'referenceId=748e033af87f1bb7b6aefd405bec9473' \
  --data-urlencode 'otp=<customer-entered OTP>'
  ```

  - **Success:** `metaData.statusCode=E000`, `submitOtp.status=success`, and the transaction details in `result`. The customer's account is now linked.
  - **Wrong OTP:** `submitOtp.status=in progress` with `retryAttemptCount` (attempts left). Ask the customer to re-enter the OTP.

  For full response samples, see [Handle the Native OTP Response](doc:bnpl-merchant-hosted-integration#step-41-handle-the-native-otp-response).
</Accordion>

<Callout icon="⚠️" theme="warn">
  ### **When Does a Repeat Payment Need an OTP?**

  The OTP flow runs again if:

  - The saved link has expired, or the account was de-linked.
  - The lender or PayU needs extra verification for the transaction.
  - For LazyPay, an expired link can't be renewed silently. The customer authenticates with an OTP again.
  - For Simpl, a link stays valid only for a short time (about 10 minutes) after eligibility is confirmed.

  After a successful re-authentication, update the stored `payuToken` with the latest value from the eligibility API.
</Callout>

***

### Step 5: Verify the Response and the Payment

1. **Reverse hash:** Verify the `hash` in the final result:

   ```Text Reverse Hash Logic
   sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
   ```

2. **Webhooks:** Use webhooks as the reliable server-to-server confirmation. See [Manage Webhooks](https://docs.payu.in/docs/webhook-events-and-sample-payloads).
3. **Verify Payment API:** If you don't get a final result (for example, the customer drops off on the OTP screen), call the [Verify Payment API](ref:verify_payment_api).

<Callout icon="✅" theme="okay">
  ### **Validation Rules:**

  - The hash you generate must match the response hash.
  - The `amount` and `txnid` must match your stored order.
  - The order must not already be marked paid.
</Callout>

***

### Step 6: De-link a BNPL Account _(Optional)_

Let customers remove a linked BNPL account from your app (for example, under **Saved payment methods**). Call the [Delete Payment Instrument API](ref:delete_payment_instrument) with either:

- `user_credentials` + `payuToken`, or
- `user_credentials` + `pg=BNPL` + `bankcode`

After de-linking, the customer's next payment goes through the first-time OTP flow again. Customers can also de-link from the lender's own app.

{/* REVIEW: Confirm the Delete Payment Instrument API supports pg + bankcode for BNPL on production. */}

***

## Security

| Requirement                                                                | Why                                                                     |
| -------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Generate the hash and HMAC signature **server-side only**                  | Keeps your salt and secret off the client.                              |
| Store `payuToken` securely against your customer record                    | It identifies a linked BNPL account. Don't expose it in URLs or logs.   |
| Use a stable, non-guessable identifier in `user_credentials`               | Links stay tied to the right customer.                                  |
| Take the customer's consent before linking on your own UI                  | You must collect linking consent in a merchant-hosted flow.             |
| Verify the reverse hash on every final response and webhook                | Prevents spoofed results.                                               |

***

## Going Live: Final Checklist

- [ ] Confirm Link and Pay is approved and enabled on your **production** account.
- [ ] Switch `_payment` to `https://secure.payu.in/_payment` and the eligibility API to its production endpoint.
- [ ] Replace the test key, salt, and HMAC credentials with production values.
- [ ] Test first-time linking, a repeat OTP-less payment, and an OTP fallback in the sandbox.
- [ ] Confirm webhooks are configured and reverse hash validation is on.
- [ ] Offer a de-link option in your app.

***

## Next Steps

<Cards columns="2">
  <Card title="Test Integration" href="doc:bnpl-test-integration" icon="fa-flask">
    Test linking, repeat payments, and OTP fallback.
  </Card>

  <Card title="Errors and Troubleshooting" href="doc:bnpl-errors-and-troubleshooting" icon="fa-triangle-exclamation">
    Eligibility messages and lender error codes.
  </Card>
</Cards>
