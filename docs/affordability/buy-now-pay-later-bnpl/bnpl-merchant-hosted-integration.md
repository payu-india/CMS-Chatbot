---
title: BNPL Merchant Hosted Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
This section  describes how to integrate BNPL directly into your own checkout page using PayU's Merchant Hosted (Seamless) flow.

***

## Step 1: Post the Request and Verify

### Step 1.1: Check Eligibility

Verify customer eligibility for BNPL options before displaying the payment options.

* **What you need:** Customer's phone number and transaction details.
* **Instructions:** Call the **Get Checkout Details API** to check if the customer is eligible for specific BNPL lenders.
* **Checkpoint:** ✅ Display only the BNPL options for which the customer is eligible.

<Accordion title="Eligibility Check API" icon="fa-user-check">
  Refer to the [Get Checkout Details API](ref:get_checkout_details) under the API Reference for request and response schemas.
</Accordion>

### Step 1.2: Initiate Payment

Post the transaction details directly to PayU's payment gateway.

* **What you need:** Standard payment parameters with `pg=BNPL` and the corresponding lender's `bankcode`.
* **Instructions:** Create a secure form post or server-to-server request to PayU's `_payment` endpoint.
* **Checkpoint:** ✅ The customer is redirected to the lender's authentication page or receives an OTP.

<Accordion title="Request Parameters" icon="fa-list">
  | Parameter                       | Type & Description                                    | Example                 |
  | :------------------------------ | :---------------------------------------------------- | :---------------------- |
  | `key` <br />_mandatory_         | `String` Merchant key.                                | `JPg***r`               |
  | `txnid` <br />_mandatory_       | `String` Unique transaction ID.                       | `ypl938459435`          |
  | `amount` <br />_mandatory_      | `String` Payment amount.                              | `10.00`                 |
  | `productinfo` <br />_mandatory_ | `String` Product description.                         | `iPhone`                |
  | `firstname` <br />_mandatory_   | `String` Customer's first name.                       | `Ashish`                |
  | `email` <br />_mandatory_       | `String` Customer's email.                            | `abc@payu.in`           |
  | `pg` <br />_mandatory_          | `String` Payment category. Use `BNPL`.                | `BNPL`                  |
  | `bankcode` <br />_mandatory_    | `String` Lender bank code (e.g., `LAZYPAY`, `SIMPL`). | `LAZYPAY`               |
  | `surl` <br />_mandatory_        | `String` Success redirection URL.                     | `https://your-surl.com` |
  | `furl` <br />_mandatory_        | `String` Failure redirection URL.                     | `https://your-furl.com` |
  | `hash` <br />_mandatory_        | `String` SHA-512 hash calculated on your server.      | `calculated_hash_value` |
</Accordion>

<Accordion title="Sample Request" icon="fa-code">
  ```bash
  curl -X POST "https://test.payu.in/_payment" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JPg***r&txnid=ypl938459435&amount=10.00&firstname=Ashish&email=abc@payu.in&phone=9988776655&productinfo=iPhone&pg=BNPL&bankcode=LAZYPAY&surl=`https://your-surl.com&furl=https://your-furl.com&hash=calculated_hash_value`"
  ```
</Accordion>

### Step 1.3: Response Handling & Verification

Handle the payment response returned to your redirection URLs (`surl`/`furl`) and verify the transaction status.

* **What you need:** The response payload posted to your redirection URL.
* **Instructions:** Parse the response, verify the reverse hash, and call the Verify Payment API to reconcile the transaction.
* **Checkpoint:** ✅ Transaction status is verified and updated in your database.

<Accordion title="Sample Response" icon="fa-code">
  ```json
  {
    "mihpayid": "403993715523409521",
    "mode": "BNPL",
    "status": "success",
    "unmappedstatus": "captured",
    "key": "JPg***r",
    "txnid": "ypl938459435",
    "amount": "10.00",
    "net_amount_debit": "10.00",
    "productinfo": "iPhone",
    "firstname": "Ashish",
    "email": "abc@payu.in",
    "bankcode": "LAZYPAY",
    "error": "E000",
    "error_Message": "No Error",
    "hash": "reverse_hash_value"
  }
  ```
</Accordion>

***

## Step 2: Test Integration

* **Simulate Success:** Use test credentials and a registered test phone number to complete a successful transaction.
* **Simulate Failure:** Use a test phone number configured to trigger a failure or enter an incorrect OTP to verify failure handling.

***

## Step 3: Going Live — Your Final Checklist

* Switch your environment endpoints from `test.payu.in` to `api.payu.in`.
* Replace test keys and salts with your production credentials.
* Ensure your server-side hash generation is secure and uses the correct production SALT.

````

---

### 📄 Page 5: `payu-hosted-bnpl.md`
```markdown
---
title: PayU Hosted Checkout BNPL Integration
deprecated: false
hidden: false
metadata:
  title: PayU Hosted Checkout BNPL Integration Guide | PayU
  description: Enable BNPL on PayU Hosted Checkout with minimal integration effort.
  robots: index
---

For the BNPL payment mode using PayU Hosted Checkout, PayU manages the entire payment page UI and authentication flow. You only need to redirect the customer to PayU's hosted page.

---

## Step 1: Enable BNPL on Dashboard
* **What you need:** Access to your PayU Merchant Dashboard.
* **Instructions:** Log in to your dashboard, navigate to **Payment Modes**, and ensure BNPL (and your preferred lenders like Simpl or LazyPay) is enabled. If not enabled, contact your PayU Key Account Manager or [PayU Support](https://help.payu.in).
* **Checkpoint:** ✅ BNPL appears as an active payment option on your checkout page.

---

## Step 2: Redirect Customer to PayU Hosted Page
* **What you need:** Standard payment request payload.
* **Instructions:** Post the transaction details to PayU's hosted checkout endpoint. Do not pass specific payment methods; the customer will select their preferred BNPL lender on the PayU payment page.
* **Checkpoint:** ✅ The customer is redirected to the PayU Hosted Checkout page where they can select BNPL and complete authentication.

<Accordion title="Hosted Checkout Flow" icon="fa-external-link">
The customer journey on the hosted page:
1. Customer selects **Pay Later** on the PayU payment page.
2. Customer chooses their lender (e.g., Simpl) and enters their mobile number.
3. Customer enters the OTP sent to their mobile number and completes the payment.
</Accordion>

---

## Step 3: Verify the Payment
* **What you need:** Transaction ID (`txnid`) and the Verify Payment API.
* **Instructions:** Upon redirection back to your `surl` or `furl`, call the Verify Payment API from your backend to confirm the final status of the transaction.
* **Checkpoint:** ✅ Confirm the payment status before delivering goods or services.
````
