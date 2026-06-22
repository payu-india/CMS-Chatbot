---
title: Frequently Asked Questions (FAQs)
deprecated: false
hidden: true
metadata:
  robots: index
---
## Getting Started

1. #### What is PayU Hosted Checkout?
   <Accordion title="Answer" icon="fa-comment-dots">
   PayU Hosted Checkout is a payment integration method where:

   - You redirect customers from your website to a **PayU-hosted payment page**
   - PayU handles the entire payment experience, including security and processing
   - After the payment is completed, customers are redirected back to your website

   This is the **simplest and fastest way** to start accepting payments without building or managing your own payment UI.
   </Accordion>
2. #### What are the minimum prerequisites to integrate PayU hosted checkout?
   <Accordion title="Answer" icon="fa-comment-dots">
   These are the prerequisites to integrate PayU hosted checkout:
   - <a href="https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard" target="_blank">PayU merchant account</a>
   - <a href="https://docs.payu.in/docs/generate-test-merchant-key-and-salt">Merchant test Key and Salt</a> for testing your integration
   - <a href="https://docs.payu.in/docs/generate-merchant-key-and-salt-on-payu-dashboard">Merchant live Key and Salt</a> to go live
   - Backend server
   - HTTPS-enabled callback endpoint
   - Ability to generate SHA-512 hash
   Minimum backend responsibilities:
   - Generate request hash
   - Validate reverse hash
   - Process callbacks/webhooks
   - Prevent duplicate order processing
   </Accordion>
3. #### What are the payment methods supported for PayU Hosted checkout?
   <Accordion title="Answer" icon="fa-comment-dots">
    These are the payment methods enabled by default PayU Hosted checkout:
   - NetBanking
   - Debit Card
   - Credit Card
   - UPI
   - Wallet
   You can enable these payment methods from the PayU dashboard if you are eligible. You should raise a request from the dashboard to enable these payment methods.
   - BNPL
   - EMI
   - International Payments
    
   </Accordion>
4. #### Does Hosted Checkout reduce PCI compliance?
   <Accordion title="Answer" icon="fa-comment-dots">
   Yes. Since card data is collected on PayU infrastructure, PCI scope is reduced.
   You should still secure these:
   - Backend APIs
   - Secrets
   - Callbacks
   - Webhooks
   Never expose these:
   - Salt
   - Internal auth tokens
   - Secret keys
   </Accordion>

***

## Integration Setup

1. #### What are `surl` and `furl`?
   <Accordion title="Answer" icon="fa-comment-dots">
   **`surl`**: This is a success URL PayU redirects your customers to after the payment is successful. This is not the proof of a payment as:
     - Browser redirects can fail
     - Users may close browser
     - Callbacks may be spoofed<br/>

   **`furl`** This is a failure URL PayU redirects you customers to if the payment fails. You can use this page to show:
     - Failure reason
     - Retry button
     - Support guidance

   Do not mark payment failed permanently until server-side verification confirms failure.
   </Accordion>
2. #### Can localhost be used for testing callbacks?
   <Accordion title="Answer" icon="fa-comment-dots">
   No. You cannot use localhost for testing callbacks. PayU servers cannot reach: 
   - Localhost 
   - Private IPs 
   - VPN-only endpoints
   You can use
   - Public staging server 
   - Tunnel service
   Your callback URL should be publicly reachable over HTTPS.
   </Accordion>
3. #### How should I format the `amount` parameter value?
   <Accordion title="Answer" icon="fa-comment-dots">
   The `amount` parameter in the PayU hosted checkout is crucial to generate a hash value. An invalid format or value will esssentially generate a invalid hash and make the integartion fail. Hence, alaways use the consistent decimal formatting.
   These are some of the valid and invalid value examples:
   **Valid format**
   - `100`
   - `100.00`
   - `99.50`
   **Invalid format**
   - `₹100` 
   - `100,00` 
   - `100 INR`
   </Accordion>

***

## Hash Generation

1. #### Why should I generate hash?
   <Accordion title="Answer" icon="fa-comment-dots">
   PayU defines two types of hashing:
   **Forward Hash:** The forward hash is to protect the payment request from getting tampered. It is essential for you to create a hash using parameters to create a payment request.
   **Reverse Hash:** The reverse hash is used to authenticate the payment received from customers.
   Refer to the Generate Hash page for more information.
   </Accordion>
2. #### What is the exact PayU Hosted Checkout hash formula to create a payment request?
   <Accordion title="Answer" icon="fa-comment-dots">
   This is the hash logic to create a payment request using the PayU hosted checkout.
   ```text: Forward Hash Logic
   key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT
   ```
   **Hash Logic with Example Values**
   ```text: Example Input Logic
   gtKFFx|TXN001|100.00|Order123|Aarav|aarav@example.com|||||||||||eCwWELxi
   ```
   > 📘 **Points to Remember**
   >
   > - [x] Make sure to add separators (|) even though if you are not passing any user defined fields.
   > - [x] One missing pipe will lead to invalid hash
   > - [x] Ensure to create the hash in server.
   </Accordion>
3. #### How do I troubleshoot an invalid hash error?
   <Accordion title="Answer" icon="fa-comment-dots">
   Use this debugging to troubleshoot the issue:
   1. Verify the parameter order
   2. Verify the amount format
   3. Check for trailing spaces
   4. Check if you have used the valid salt value
   5. Check environment credentials
   6. Check for the separators. Ensure you include separators even if you are not passing user defined fields as mentioned in the logic.
   Most hash failures happen from:
   - Wrong salt
   - Missing pipes (|)
   - Whitespace
   - Amount mismatch
   </Accordion>
4. #### Can I generate hash in frontend?
   <Accordion title="Answer" icon="fa-comment-dots">
   No. You should not generate a hash value from frontend as it will expose the salt value.
   </Accordion>

***

## Checkout Experience

1. #### What happens if customer closes browser mid-payment?
   <Accordion title="Answer" icon="fa-comment-dots">
   The outcomne depends on the step where the customer has closed the browser. For example, if the customer has approved the UPI payment and immediately closes the browser. Then the possible outcomes are:
   - Payment success
   - No redirect
   - Webhook still arrives
   We recommend not to rely on browser state but on:
   - Webhook
   - Callback
   - Status verification API
   </Accordion>
2. #### Can I embed checkout in an iframe?
   <Accordion title="Answer" icon="fa-comment-dots">
   Need clarity
   </Accordion>
3. #### What happens if customers close browser mid-payment?
   <Accordion title="Answer" icon="fa-comment-dots">
   The payment might still succeed if a cutomer closed the browser mid-payment. However, it depends on when a customer has abandoned the payment. These are the possible outcomes:
   - Payment success
   - No redirect
   - Webhook still arrives
   It is a good practice to check the payment status using any of the following:
   - Webhook
   - Callback
   - Status verification API
   </Accordion>
   ***
   ## Reverse Hashing

1) #### What is reverse hash validation?
   <Accordion title="Answer" icon="fa-comment-dots">
   Reverse hash validation a way to verify the authnticity of the payment made by customers.
   After a customer completes a payment PayU returns a response hash in callback.
   You must regenerate it and compare. This is the validation flow:
   1. You receive a callback
   2. Use the returned hash and generate a reverse hash string.
   3. Compare hashes and authenticated if the hash matches. Reject the callback if the hash mismatches.
   </Accordion>
2) #### What causes reverse hash mismatch?
   <Accordion title="Answer" icon="fa-comment-dots">
   These are the common causes of reverse hash mismatch:
   - Wrong sequence
   - Wrong salt
   - Modified response data
   - Whitespace issues
   </Accordion>

## Callback vs Webhook

1. #### What is the difference between callback and webhook?
   <Accordion title="Answer" icon="fa-comment-dots">
   | Callback                | Webhook             |
   | ----------------------- | ------------------- |
   | Browser redirect        | Server-to-server    |
   | Depends on user browser | Independent of user |
   | Less reliable           | More reliable       |
   </Accordion>

<br />
