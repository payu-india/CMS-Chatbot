---
title: BNPL Link & Pay - Merchant Hosted
deprecated: false
hidden: true
metadata:
  robots: index
---
Integrate with PayU’s Pay Later stack to enable a frictionless, one-click checkout experience across supported BNPL lenders (e.g., LazyPay) using secure account linking.

## Steps to Integrate

<Cards columns="3">
  <Card title="1. Check Eligibility" href="#step-11-check-eligibility">
    Verify customer eligibility for BNPL Link & Pay before proceeding.
  </Card>

  <Card title="2. Initiate Payment" href="#step-12-initiate-payment">
    Start the payment process using S2S Link & Pay flow.
  </Card>

  <Card title="3. Submit OTP" href="#step-13-submit-otp-first-time-flow-only">
    Submit and validate OTP for first-time users to link accounts.
  </Card>
</Cards>

***

## Step 1: Post the Request and Verify

### Step 1.1: Check Eligibility

Before displaying the BNPL option to the customer, check their eligibility using the **Get EMI Checkout Details API**.

* **What you need:** Merchant credentials, customer's phone number, and transaction amount.
* **Instructions:** Call the eligibility endpoint from your backend. If the customer is eligible, display the BNPL option on your checkout page.
* **Checkpoint:** ✅ The API returns `eligible: true` and indicates whether the customer is already linked (`customerLinked: true`).

<Accordion title="Eligibility API Details" icon="fa-server">
  #### Environment

  * **Test:** `https://test.payu.in/info/linkAndPay/get_emi_checkout_details`
  * **Production:** `https://info.payu.in/linkAndPay/get_emi_checkout_details`

  #### Request Parameters

  | Parameter         | Type & Description                             | Example           |
  | :---------------- | :--------------------------------------------- | :---------------- |
  | `Key`             | `String` Merchant key.                         | `yFbXg3`          |
  | `amount`          | `Number` Transaction amount.                   | `21`              |
  | `userCredentials` | `String` Format: `merchantKey:userIdentifier`. | `yFbXg3:test_sud` |
  | `phone`           | `String` Customer's registered mobile number.  | `9999999999`      |
  | `bankCode`        | `String` BNPL provider code.                   | `LAZYPAY`         |
</Accordion>

<Accordion title="Eligibility Code Samples" icon="fa-code">
  ```bash
  curl --location --request POST 'https://test.payu.in/info/linkAndPay/get_emi_checkout_details' \
  --header 'Authorization: hmac username="yFbXg3", algorithm="sha512", headers="date", signature="cd1e0a382807ef7be094dedc4d2fc4cd34906197d3933485b8fab37aef2e5483df3517a711619444715fe795ffddb438e4279637782d0c5d5c1b69986c231af3"' \
  --header 'date: Thu, 21 Aug 2025 10:22:41 GMT' \
  --header 'x-credential-username: yFbXg3' \
  --header 'Content-Type: application/json' \
  --data '{
    "Key": "yFbXg3",
    "amount": 21,
    "userCredentials": "yFbXg3:test_sud",
    "phone": "9999999999",
    "bankCode": "LAZYPAY",
    "payuToken": null,
    "requestId": "Testing_111"
  }'
  ```

  ```python
  import requests

  url = "https://test.payu.in/info/linkAndPay/get_emi_checkout_details"
  headers = {
      "x-credential-username": "yFbXg3",
      "Content-Type": "application/json",
      "authorization": "hmac username=\"yFbXg3\", algorithm=\"sha512\", signature=\"...\"",
      "date": "Thu, 21 Aug 2025 10:22:41 GMT"
  }
  payload = {
      "Key": "yFbXg3",
      "amount": 21,
      "userCredentials": "yFbXg3:test_sud",
      "phone": "9999999999",
      "bankCode": "LAZYPAY",
      "payuToken": None,
      "requestId": "Testing_111"
  }
  response = requests.post(url, headers=headers, json=payload)
  print(response.json())
  ```

  ```json
  {
    "bnpl": {
      "all": [
        {
          "Lazypay": {
            "status": 1,
            "eligible": true,
            "customerLinked": true,
            "PayuToken": "Token12345"
          }
        }
      ]
    }
  }
  ```
</Accordion>

### Step 1.2: Initiate Payment

Initiate the transaction using the `_payment` API. Returning linked users will experience a direct debit, while unlinked users will trigger an OTP.

* **What you need:** Transaction details, `txn_s2s_flow=4`, and `linkAndPayFlowType`.
* **Instructions:** Post the payment request from your server.
* **Checkpoint:** ✅ For repeat linked users, the payment completes immediately. For first-time users, an OTP is triggered.

<Accordion title="Payment Request Parameters" icon="fa-list">
  | Parameter                              | Type & Description                                                                   | Example          |
  | :------------------------------------- | :----------------------------------------------------------------------------------- | :--------------- |
  | `key` <br />_mandatory_                | `String` Merchant key.                                                               | `a4vGC2`         |
  | `txnid` <br />_mandatory_              | `String` Unique transaction ID.                                                      | `my_order_30827` |
  | `amount` <br />_mandatory_             | `String` Transaction amount.                                                         | `5000`           |
  | `pg` <br />_mandatory_                 | `String` Payment category. Use `BNPL`.                                               | `BNPL`           |
  | `bankcode` <br />_mandatory_           | `String` BNPL provider code.                                                         | `LAZYPAY`        |
  | `txn_s2s_flow` <br />_mandatory_       | `String` Set to `4` for Link & Pay.                                                  | `4`              |
  | `linkAndPayFlowType` <br />_mandatory_ | `String` `0` for OTP flow; `1` for first-time linking and subsequent non-OTP debits. | `1`              |
  | `user_credentials` <br />_mandatory_   | `String` Format: `merchantKey:userId`.                                               | `a4vGC2:SLP3`    |
</Accordion>

<Accordion title="Payment Code Samples" icon="fa-code">
  ```bash
  curl --location --request POST 'https://test.payu.in/_payment' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=a4vGC2' \
  --data-urlencode 'txnid=my_order_30827' \
  --data-urlencode 'amount=5000' \
  --data-urlencode 'firstname=Payu-Admin' \
  --data-urlencode 'email=test@example.com' \
  --data-urlencode 'phone=9999999999' \
  --data-urlencode 'productinfo=productinfo' \
  --data-urlencode 'pg=BNPL' \
  --data-urlencode 'bankcode=LAZYPAY' \
  --data-urlencode 'txn_s2s_flow=4' \
  --data-urlencode 'linkAndPayFlowType=1' \
  --data-urlencode 'user_credentials=a4vGC2:SLP3' \
  --data-urlencode 'surl=https://test.payu.in/admin/test_response' \
  --data-urlencode 'furl=https://test.payu.in/admin/test_response' \
  --data-urlencode 'hash=7e365d44567e2980b1ff8e0404ee0b7a16d6b8763bb2c253ad2ed9ee7a067c5b6b2f0682d230ebb30ae3b1b618f9e7bb16d2cf556d79f1c4acc8a24111c4bdfb'
  ```

  ```json
  {
    "metaData": {
      "message": "No Error",
      "referenceId": "748e033af87f1bb7b6aefd405bec9473",
      "statusCode": "E000",
      "txnId": "my_order_30827",
      "unmappedStatus": "success"
    },
    "result": {
      "link_and_pay": {
        "customerLinked": "true",
        "payuToken": "token12345"
      },
      "status": "success"
    }
  }
  ```
</Accordion>

### Step 1.3: Submit OTP (First-Time Flow Only)

If the customer is not linked, capture the OTP natively on your UI and submit it to complete the linking and payment.

* **What you need:** Customer-entered OTP and the `referenceId` from the payment response.
* **Instructions:** Call the **Submit OTP API** with the OTP and reference ID.
* **Checkpoint:** ✅ The account is linked, and the transaction is authorized.

<Accordion title="Submit OTP API Details" icon="fa-key">
  Submit the OTP to complete the linking process.

  ```bash
  curl --location --request POST '`https://test.payu.in/payment/submit_otp`' \
  --header 'Content-Type: application/json' \
  --data '{
    "referenceId": "748e033af87f1bb7b6aefd405bec9473",
    "otp": "123456"
  }'
  ```
</Accordion>

***

## Step 2: Test Integration

### Step 2.1: Simulate First-Time Linking

* **Action:** Use a test phone number not registered with the BNPL provider.
* **Expected Outcome:** The eligibility check returns `customerLinked: false`. Initiating payment triggers an OTP. Submit a test OTP (`123456`) to complete linking.

### Step 2.2: Simulate Repeat One-Click Payment

* **Action:** Run the flow again using the same `user_credentials` and phone number.
* **Expected Outcome:** The eligibility check returns `customerLinked: true`. Initiating payment completes instantly without triggering an OTP.

***

## Step 3: Going Live — Your Final Checklist

### Step 3.1: Update to Production Credentials

* Update your merchant `key` and `SALT` to production values.
* Switch endpoints from `test.payu.in` to `api.payu.in` (or `info.payu.in` for production eligibility).

### Step 3.2: Final Integration Verification

* Verify that the hash is calculated securely on your backend server.
* Ensure your webhook listener is active and configured to receive post-payment callbacks.

```
```
