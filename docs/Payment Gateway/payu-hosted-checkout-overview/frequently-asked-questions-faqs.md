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

<br />
