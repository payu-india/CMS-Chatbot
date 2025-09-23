---
title: Integration Steps (COPY)
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  title: PayU Hosted Checkout Integration
  keywords:
    - PayU Hosted Checkout Integration
    - Integrate PayU Hosted Checkout
    - Steps for PayU Hosted Checkout Integration
    - PayU Hosted Checkout Integration Steps
  robots: index
---
# What you're building

A simple server-generated redirect that sends customers from your site/app to the PayU-hosted payment page, then returns them to your success/failure URLs. You pass order & customer fields + a server-generated SHA-512 hash for integrity; PayU handles the payment UI and authentication.

The PayU Hosted Checkout integration involves the following steps:

<Cards columns={3}>
  <Card title="1. Start Integration" href="https://docs.payu.in/docs/integration-steps-copy#step-1--start-integration" target="_blank" className="bg-gradient-to-r from-emerald-400 to-emerald-600 hover:from-emerald-500 hover:to-emerald-700 text-white shadow-lg rounded-xl border-5">
    Integrate pre-built checkout solution
  </Card>

  <Card title="2. Test Integration" href="https://docs.payu.in/docs/integration-steps-copy#step-2-test-integration" className="bg-gradient-to-r from-amber-400 to-amber-600 hover:from-amber-500 hover:to-amber-700 text-white shadow-lg rounded-xl border-5">
    Test the integration by making a test transaction
  </Card>

  <Card title="3. Go live Checklist" href="https://docs.payu.in/docs/integration-steps-copy#step-3-going-live-your-final-checklist" className="bg-gradient-to-r from-purple-400 to-purple-600 hover:from-purple-500 hover:to-purple-700 text-white shadow-lg rounded-xl border-5">
    Follow the production checklist to go live
  </Card>
</Cards>

<Callout icon="📘" theme="info">
  **Pre-requisite**

  * Create an <Anchor label="account with PayU" target="_blank" href="https://onboarding.payu.in/app/account/signup">account with PayU</Anchor>
  * Get your key and salt for test and production environment. <Anchor label="Click here to access detail guide on accessing your key and salt " target="_blank" href="https://docs.payu.in/docs/generate-test-merchant-key-and-salt">Click here to access detail guide on accessing your key and salt </Anchor>
  * Keep https success & failure URLs (surl, furl) ready,  reachable from the public internet.
  * Ability to generate SHA-512 on the server (not recommended to do it in browser).
</Callout>

<Accordion title="Environment" icon="fa-globe">
  |                        |                                                                     |
  | :--------------------- | :------------------------------------------------------------------ |
  | Test Environment       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |
  | Production Environment | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |
</Accordion>

## Step 1:  Start Integration

Follow the below steps to complete the integration:

\<Accordion title="Step 1.1: Prepare the request parameters" icon="fa-list-check">
  First, you need to collect all the necessary information for the transaction. Below is the list of parameters where some are mandatory and others are optional.

  \<HTMLBlock>\{`
                                            \<div >
                                              \<table>
                                                \<thead>
                                                  \<tr>
                                                    \<th style="width: 10%;">Parameter\</th>
                                                    \<th style="width: 75%; white-space: normal; word-break: break-word;">Type & Description\</th>
                                                    \<th style="width: 15%;">Example\</th>
                                                  \</tr>
                                                \</thead>
                                                \<tbody>
                                                  \<tr>
                                                    \<td>
                                                      key\<br>
                                                      \<code>mandatory\</code>
                                                    \</td>
                                                    \<td style="white-space: normal; word-break: break-word;">
                                                      \<code>String\</code> Merchant key provided by PayU during onboarding.
                                                    \</td>
                                                    \<td>JPG****.k\</td>
                                                  \</tr>
                                                  \<tr>
                                                    \<td>
                                                      txnid\<br>
                                                     \<code class="inline-block rounded-full bg-red-100 px-2 py-0.5 text-xs font-semibold text-red-800 ring-1 ring-inset ring-red-200">mandatory\</code>

```
```

  \<Callout icon="📘" theme="info">
    Swap the form action to the production endpoint: [[https://secure.payu.in/\_payment](https://secure.payu.in/_payment) when you go live.
  \</Callout>
\</Accordion>

\<Accordion title="Step 1.2: Generate Hash" icon="fa-key">
  Concatenate fields in this exact sequence, then SHA-512:

```
```

* Use empty strings for missing udf\*.
  * Compute on your server and include the lowercase hex digest as hash.

  For more information, refer to  \<a href="generate-hash-payu-hosted" target="_blank"> Generate Hash\</a>.
\</Accordion>

\<Accordion title="Step 1.3: POST the html form (server renders)" icon="fa-code">
  ```html
  \<!doctype html>
  \<html>
    \<body onload="document.forms.payu.submit()">
      \<form name="payu" method="post" action="[https://test.payu.in/\_payment](https://test.payu.in/_payment)">
        \<input type="hidden" name="key" value="JP***g">
        \<input type="hidden" name="txnid" value="t6svtqtjRdl4ws">
        \<input type="hidden" name="amount" value="499.00">
        \<input type="hidden" name="productinfo" value="Pro Plan">
        \<input type="hidden" name="firstname" value="Aditi">
        \<input type="hidden" name="email" value="[test@example.com](mailto:test@example.com)">
        \<input type="hidden" name="phone" value="9999999999">
        \<input type="hidden" name="surl" value="[https://yourapp.com/payu/success](https://yourapp.com/payu/success)">
        \<input type="hidden" name="furl" value="[https://yourapp.com/payu/failure](https://yourapp.com/payu/failure)">
        \<input type="hidden" name="hash" value="sha512(...hash sequence...)">
        \<input type="submit" value="Submit" />
      \</form>
    \</body>
  \</html>
  ```

  **Replace the value attributes with your actual data and the generated hash. You can add more parameters to this form as needed.**

  \<Callout icon="📘" theme="info">
    **Important**

```
```

\<Accordion title="Step 1.4: Response handling & hash verification" icon="fa-shield-check">
  **Response Handling:**

  After the customer completes or abandons the payment, PayU POSTs back to your return URL with URL-encoded fields (form post). This payload includes the transaction status, txnid, mihpayid, and a hash you must verify (reverse hashing) before trusting the result.

  Sample surl/furl payload:

```
```

```
```

  **Step 1.4.1: Response verification using reverse hashing**

  Verify the response received above by recomputing SHA-512 using the reverse sequence:

```
```

* Compare the computed digest to hash from the POST payload (**case-insensitive**).
  * Trust the result only if the hash matches. Then update your order state.
    \</Accordion>

\<Accordion title="Step 1.5: Verify the payment" icon="fa-magnifying-glass">
  Upon receiving the response, We recommend performing a reconciliation step by querying the verification APIs to validate all transaction details.

  **Environment**

|                  |    |
| :--------------- | :- |
| Test Environment | [  |

  \<Accordion title="Sample request" icon="fa-code">
    ```curl
    curl --location '[https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2)' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'key=JP***g' \
    --data-urlencode 'command=verify_payment' \
    --data-urlencode 'var1=IhfgcZnXR4o4nB' \
    --data-urlencode 'hash=a0ae79fdd66c875af6e9b21c4a67f1822deb00f2df5e9f0b1948f3222f536a9bf741b24efbb1874ca0f84f76b036e6c0d641581d0100f7abe4aeed2f3264f5c9'
    ```
  \</Accordion>

  \<Accordion title="Sample response" icon="fa-reply">
    * If credit card payment is made, the response is similar to the following:

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

  \<Accordion title="Response parameters" icon="fa-list">
    \<Table align=\{["left","left","left"]}>
      \<thead>
        \<tr>
          \<th style=\{\{ textAlign: "left" }}>
            **Parameter**
          \</th>

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

<br />

## Step 2: Test Integration

Before going live, it's crucial to test your integration thoroughly in the PayU test environment. Follow these steps to ensure your setup is correct and to simulate different transaction scenarios.

<Accordion title="Step 2.1: Pre-Payment Validation" icon="fa-check-circle">
  **Configure Webhooks**
  Configure the webhooks to monitor the status of payments. Webhooks emable a server to communicate with another server by sending an HTTP callback or message. These callbacks are triggered by specific events or instances and they operate at the server-to-server (S2S) level.  For more information, refer to [Webhooks for Payments](https://docs.payu.in/docs/webhooks).

  **Verify Payment**

  Before initiating a transaction, ensure your server-side implementation is correct.

  1. **Verify API Credentials:** Double-check that you are using the correct key and salt for the test environment.
  2. **Validate Hash Calculation:** The most common point of failure is an incorrect hash.
     1. Temporarily print the string that you are passing into the hash function on your server.
     2. Ensure the order of the parameters (key|txnid|amount|productinfo|firstname|email...|salt) exactly matches the format specified in the documentation.
     3. Verify that there are no empty or null values for mandatory parameters in the hash string.
     4. If you encounter a "Checksum failed" error upon redirection, this is the first thing to debug.
</Accordion>

<Accordion title="Step 2.2: Simulate a Successful Transaction (The Happy Path)" icon="fa-thumbs-up">
  This test ensures that a successful payment is correctly processed and recorded.

  1. **Initiate Payment:** On your website or app, add items to the cart and proceed to payment. This should trigger your code to send the transaction details to PayU and redirect the user to the PayU payment page.
  2. **Error Check:** If you are not redirected and see an error message on your own site, check your server-side logs. If you are redirected to a PayU error page, refer to the Error Handling section to diagnose the issue.
  3. **Verify Payment Page:** Once on the PayU page, confirm the following:
     1. The transaction amount and product details are displayed correctly.
     2. All the payment methods (Credit/Debit Card, UPI, Net Banking, etc.) that should be active on your account are visible. If a payment method is missing, please contact your Key Account Manager (KAM) or PayU Support.
  4. **Test a Card Transaction**:
     1. Select Credit Card as the payment method.
     2. Use the following test card details:
        1. Card Number: 5123456789012346
        2. Expiry Date: Any valid future date (e.g., 12/2030)
        3. CVV: 123
        4. Name on Card: Test Name
     3. Click Pay Now. You will be redirected to a dummy bank page to simulate 3D Secure authentication.
     4. Enter the test OTP 123456 and click Submit.
  5. **Test a UPI Transaction:**
     1. Select UPI as the payment method.
     2. Enter a test UPI ID: testsuccess\@gpay
     3. Click Verify and then Pay Now. This will simulate a successful UPI transaction.

  For more test credentials, refer to the [Test Cards, UPI ID and Wallets guide](https://docs.payu.in/docs/test-cards-upi-id-and-wallets).
</Accordion>

<Accordion title="Step 2.3: Simulate a Failed Transaction" icon="fa-times-circle">
  It's equally important to test how your system handles failed payments.

  1. Initiate a New Payment as you did in Step 2.
  2. Test a Failing Card Transaction:
     1. Select Credit Card as the payment method.
     2. Use a test card designed to fail, for example:
        1. Card Number: 5123456789012340 (Payment failed by user)
     3. Complete the payment flow. The transaction should fail.
</Accordion>

<Accordion title="Step 2.4: Post-Transaction Verification" icon="fa-magnifying-glass">
  After both the successful and failed transactions, you must verify the final status at multiple points.

  1. **Check the Return URL (surl / furl):**
     1. After a successful payment, PayU will redirect the user to the Success URL (surl) you provided. Verify that your application handles this redirect correctly and displays an appropriate success message to the user.
     2. After a failed payment, PayU will redirect the user to the Failure URL (furl). Verify that your application displays a clear failure message and provides the user with options to retry.
  2. **Verify the Server-to-Server (S2S) Webhook:**
     1. This is the most reliable way to confirm transaction status.
     2. Check your server logs to ensure that you have received the S2S POST request from PayU for the transaction.
     3. Validate the hash in the webhook response to ensure the data is authentic.
     4. Update the transaction status in your database based on the status received in the S2S webhook, not based on the browser redirect (surl/furl).
  3. **Cross-Verify in the PayU Dashboard:**
     1. Log in to your PayU test dashboard.
     2. Navigate to the "Transactions" section.
     3. Verify that both the successful and failed transactions are logged correctly with the corresponding status (success, failure). Check that details like txnid and amount match your records.
</Accordion>

## Step 3: Going Live: Your Final Checklist

You've successfully tested your integration. Now, follow these critical steps to switch to the live environment and start accepting real payments from your customers.

<Accordion title="Step 3.1. Update to Production Credentials" icon="fa-key">
  First, you must switch your integration from using test credentials to production credentials.

  1. **Generate Live Keys:**
     * Log in to your **PayU Dashboard**.
     * Use the toggle at the top to switch from **Test Mode** to **Live Mode**.
     * Navigate to **Developer Tools** → **API Keys** from the sidebar.
     * Copy the **Live Merchant Key** and **Live Salt**.
  2. **Update Your Code:**
     * In your integration code, replace the test `key` and `salt` with your new live credentials.
  3. **Update the Endpoint URL:**
     * Ensure all API requests are now being sent to the production endpoint:
       `https://secure.payu.in/_payment`
</Accordion>

<Accordion title="Step 3.2. Final Integration Verification" icon="fa-clipboard-check">
  Before you announce that you're live, run through this checklist to ensure everything is configured correctly.

  * **✅ Conduct a Live Transaction:** Make a small, real transaction with a genuine credit card or UPI ID. This is the best way to confirm that your production credentials are correct and that the end-to-end flow is working.

  * **✅ Verify the Server-to-Server (S2S) Webhook:** This is the most crucial step for confirming transaction status reliably.
    * After your live test transaction, check your server logs to confirm that you received the webhook from PayU.
    * Ensure your system correctly processes this webhook and updates the order status in your database.
    * **Important:** Your system should rely on this S2S webhook as the primary source of truth for a transaction's final status, not the browser redirect. For more details, refer to **Webhooks**.

  * **✅ Validate the Response Hash:**
    * Confirm that your code correctly validates the hash for the response sent to your return URL (`surl`/`furl`) and for the S2S webhook. This security measure prevents tampering and confirms the response is genuinely from PayU. For more information, refer to **Hashing Request and Response**.

  * **✅ Check Success and Failure Pages (`surl` / `furl`):**
    * Ensure that after a successful payment, your customer is redirected to your success page and sees a clear confirmation message.
    * Simulate a failed live payment (if possible, with a card that has insufficient funds) to ensure the customer is redirected to your failure page and given instructions to retry.

  * **✅ Implement a Reconciliation Plan:**
    * In case of any discrepancy (e.g., a webhook is missed), use the **Verify Payment API** to programmatically fetch the status of a transaction from PayU and reconcile your records.
</Accordion>

<br />
