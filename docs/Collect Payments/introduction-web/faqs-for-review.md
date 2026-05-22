---
title: '[Internal Review]FAQs for Review'
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
<br />

## Checkout Plus

* **What is PayU Checkout Plus and how is it different from PayU Hosted Checkout?**

  PayU Checkout Plus is a redirectionless payment experience that opens as a pop-up (modal) on your website, keeping customers in the context of your website throughout the payment process. Unlike PayU Hosted Checkout which redirects customers to PayU's payment page, Checkout Plus displays the payment form as an inline modal on your website. The modal is served from PayU servers, ensuring you don't need PCI-DSS compliance while providing a seamless payment experience. For more information, refer to [Checkout Plus](doc:checkout-plus-integration).

* **Can I use Checkout Plus for mobile app integrations?**

  Checkout Plus is not recommended for app browsers such as WebView, Chrome Custom Tab, etc. For mobile apps, PayU recommends using PayU Hosted Checkout (redirection-based) or PayU Mobile SDKs. For more information, refer to [Webview configurations](doc:integrate-webview-for-mobile-apps-checkout-plus) or [PayU Hosted Checkout](doc:prebuilt-checkout-payu-hosted).

* **What payment methods are supported in Checkout Plus?**

  Checkout Plus supports the following payment methods:

  * Credit Card
  * Debit Card
  * Net Banking
  * UPI
  * Wallet
  * EMI
  * BNPL

  For more information, refer to [Checkout Plus](doc:checkout-plus-integration).

* **How does the retry feature work in Checkout Plus?**

  Checkout Plus includes a retry feature that helps reduce transaction failures. If a transaction fails at the bank or 3D Secure page (which accounts for approximately 15% of failures), customers can retry seamlessly without restarting the entire checkout process. The customer remains in the payment context and can retry from the inline payment form without compromising the current order. For more information, refer to [Checkout Plus](doc:checkout-plus-integration).

* **Can I customize the Checkout Plus payment modal to match my brand?**

  Yes, you can customize the payment page UI, colors, and logo to suit your brand identity. Checkout Plus allows you to create a branded payment experience while leveraging PayU's secure payment infrastructure. For more information, refer to [Checkout Plus](doc:checkout-plus-integration).

* **What happens if a customer closes the Checkout Plus modal without completing the payment?**

  If a customer closes the Checkout Plus modal without completing the payment, the transaction is not processed. The customer can initiate a new payment by clicking the payment button again. You can implement your own logic to handle abandoned checkouts, such as showing a reminder or offering alternative payment options.

***

## CommercePro Checkout (Checkout Express)

* **What is CommercePro Checkout and how is it different from other PayU checkout options?**

  CommercePro Checkout (also known as Checkout Express) is a comprehensive checkout solution that helps minimize COD RTO by analyzing customer shopping history and address quality. It allows customers to securely save their payment details and addresses and use them across PayU network businesses. CommercePro optimizes the checkout experience end-to-end by configuring the PayU offer engine and recommendation engine. Key features include no form filling, pre-filled addresses, payment reminders, and offer engine integration. For more information, refer to [CommercePro Checkout](doc:checkout-express).

* **How do I enable CommercePro Checkout for my account?**

  CommercePro Checkout needs to be enabled by PayU. If it's not enabled, contact your PayU Key Account Manager (KAM) or click **Help** at the top-right corner of PayU Dashboard to raise a ticket with PayU Support. For more information, refer to [CommercePro Checkout](doc:checkout-express).

* **What platforms support CommercePro Checkout?**

  PayU supports CommercePro on the following platforms:

  * WooCommerce
  * Magento
  * Custom websites (using Response Handler or Callback URL)

  For more information, refer to [CommercePro Checkout](doc:checkout-express).

* **How does the pre-fill address feature work in CommercePro Checkout?**

  CommercePro Checkout pre-fills addresses for first-time users from a database of 15.5 million+ addresses, making the journey similar to that of repeat customers. This feature helps reduce form filling time and improves the checkout experience. For more information, refer to [CommercePro Checkout](doc:checkout-express).

* **What is the difference between CommercePro Checkout using Response Handler and Callback URL?**

  * **Response Handler**: The payment response is handled directly in your JavaScript code using a response handler function. This is suitable for single-page applications or when you want to handle the response immediately without server-side processing.

  * **Callback URL**: The payment response is sent to a server-side URL that you configure. This is suitable when you need to process the response on your server, update your database, or perform server-side validations.

  For more information, refer to [Integrate CommercePro Checkout using Response Handler](doc:integration-checkout-express-response-handler) or [Integrate CommercePro Checkout using Callback URL](doc:integrate-commercepro-checkout-using-callback-url).

* **How does the payment reminder feature work in CommercePro Checkout?**

  CommercePro Checkout can automatically send payment links via WhatsApp whenever a customer drops off during checkout or if payment fails. This feature helps recover abandoned transactions and improve conversion rates. The feature needs to be configured in your PayU Dashboard. For more information, refer to [CommercePro Checkout](doc:checkout-express).

* **Can I use CommercePro Checkout for COD (Cash on Delivery) transactions?**

  Yes, CommercePro Checkout allows you to offer COD as a payment option for customers unwilling to use or without access to digital payment methods. This feature helps minimize COD RTO by analyzing customer shopping history and address quality. For more information, refer to [CommercePro Checkout](doc:checkout-express).

***

## Merchant Hosted Checkout (Additional FAQs)

* **What are the PCI-DSS compliance requirements for Merchant Hosted Checkout?**

  If you are using Merchant Hosted Checkout, you will collect card details on your own website and therefore you must be PCI-DSS compliant. You need to fill out the "[Self-Assessment Questionnaire A-EP and Attestation of Compliance](https://www.pcisecuritystandards.org/documents/PCI-DSS-v3_2-SAQ-A_EP-rev1_1.pdf)" form. For more information, refer to [Merchant Hosted Checkout](doc:custom-checkout-merchant-hosted).

* **Can I use Merchant Hosted Checkout if I only want to accept UPI and Wallets?**

  Yes, if you are using only UPI and Wallet payment modes with Merchant Hosted checkout, you need to ensure that your website is secure (HTTPS), but you may not need full PCI-DSS compliance. However, PayU still recommends following security best practices. For more information, refer to [Merchant Hosted Checkout](doc:custom-checkout-merchant-hosted).

* **What is the difference between Merchant Hosted Checkout and Server-to-Server (S2S) Integration?**

  * **Merchant Hosted Checkout**: The customer is redirected to the bank's website for OTP authentication. The payment flow involves browser redirections between your website, PayU, and the bank.

  * **Server-to-Server (S2S) Integration**: The transaction is processed entirely at the server level without browser redirections. The customer enters OTP on your website, and your server communicates directly with PayU's servers. S2S requires PCI-DSS compliance and eliminates intermediate browser hops.

  For more information, refer to [Merchant Hosted Checkout](doc:custom-checkout-merchant-hosted) and [Server-to-Server Integration](doc:server-to-server-integration).

* **How do I handle 3D Secure authentication in Merchant Hosted Checkout?**

  PayU supports 3D Secure 2.0 transactions with Merchant Hosted Checkout integration. When a customer uses a card that requires 3D Secure authentication, they will be redirected to the bank's ACS (Access Control Server) page to complete the authentication. After authentication, the customer is redirected back to your website. For more information, refer to [Merchant Hosted Checkout](doc:custom-checkout-merchant-hosted).

* **Can I save card details for future transactions in Merchant Hosted Checkout?**

  Yes, you can save card details for future transactions using PayU's Save Cards feature. However, you must ensure PCI-DSS compliance if you're storing card details. PayU recommends using tokenization to replace sensitive card details with non-sensitive tokens. For more information, refer to [Save Cards Integration](doc:introduction-save-cards).

* **What should I do if I receive a hash mismatch error in Merchant Hosted Checkout?**

  If you receive a hash mismatch error, verify the following:

  * Check that the hash is calculated using the correct formula and parameter order
  * Ensure that empty UDF parameters are represented with empty pipes (||) in the hash string
  * Verify that you're using the correct salt value for your environment (test or production)
  * Check for any extra spaces or special characters in parameter values

  For more information, refer to [Generate Hash - Merchant Hosted](doc:generate-hash-merchant-hosted).

***

## Webhooks 

* **What is the difference between webhooks and redirect URLs (surl/furl)?**

  * **Redirect URLs (surl/furl)**: These are browser-based redirects that occur after payment completion. They depend on the customer's browser and may fail if the customer closes the browser or experiences network issues.

  * **Webhooks**: These are server-to-server callbacks that PayU sends directly to your server. Webhooks are more reliable as they don't depend on browser redirection and ensure you receive transaction updates even if the browser redirect fails.

  PayU recommends using webhooks (S2S callbacks) to ensure optimum transaction outcomes. For more information, refer to [Webhooks for Payments](doc:webhooks).

* **How many times will PayU retry sending a webhook if my server doesn't respond?**

  PayU will retry sending webhooks 3 times to get a 200 OK response from your server before flagging it as a timeout. Ensure your webhook endpoint is properly configured to accept key-value pairs or hashmap formats and returns a 200 OK status code. For more information, refer to [Webhooks for Payments](doc:webhooks).

* **What content types should my webhook endpoint support?**

  Your webhook endpoint should be capable of handling the following content types:

  * FormData
  * application/x-www-form-urlencoded

  Ensure your server URL can accept data in these formats. For more information, refer to [Webhooks for Payments](doc:webhooks).

* **What IP addresses should I whitelist for receiving webhooks?**

  You need to whitelist the following IP addresses in your firewall to receive webhooks:

  | IP Addresses    |
  | --------------- |
  | 52.140.8.88     |
  | 52.140.8.89     |
  | 180.179.174.2   |
  | 180.179.165.250 |
  | 52.140.8.64     |
  | 52.140.8.65     |
  | 3.6.73.183      |
  | 3.6.83.44       |
  | 3.7.89.1        |
  | 3.7.89.2        |
  | 3.7.89.3        |
  | 3.7.89.8        |
  | 3.7.89.9        |
  | 3.7.89.10       |

  For more information, refer to [Webhooks for Payments](doc:webhooks).

* **What webhook events are available for payments?**

  PayU supports the following webhook events for payments:

  * **Successful Payment**: Triggered when a payment is successful
  * **Failed Payment**: Triggered when a payment fails
  * **Refund**: Triggered when a payment is refunded
  * **Dispute**: Triggered when a dispute is raised for a payment

  Additionally, you can enable `callback_on_failure` flag to receive webhooks for pending payment statuses in real-time. For more information, refer to [Webhooks for Payments](doc:webhooks).

* **How do I verify that a webhook is coming from PayU and not from a malicious source?**

  You should verify the webhook hash to ensure it's coming from PayU. When PayU sends a webhook, it includes a hash parameter. You should recalculate the hash using the response parameters and your salt, then compare it with the hash received from PayU. If they match, the webhook is authentic. For more information on reverse hashing, refer to [Generate Hash - Merchant Hosted](doc:generate-hash-merchant-hosted).

* **Can I test webhooks without making actual payments?**

  Yes, you can test your webhooks using the Test Webhook feature available in your PayU Dashboard. Navigate to **Settings > Webhooks** and use the test webhook functionality to verify that your endpoint is receiving and processing webhooks correctly. For more information, refer to [Webhooks for Payments](doc:webhooks).

***

### Bank and Card Codes

* **Where can I find the bankcode for a specific bank for Net Banking integration?**

  You can find the bankcode for Net Banking in the [Net Banking Codes](doc:net-banking-codes) documentation. Each bank has a unique code that needs to be passed in the `bankcode` parameter when initiating a Net Banking transaction. For more information, refer to [Net Banking Codes](doc:net-banking-codes).

* **How do I find the correct bankcode for wallet payments?**

  You can find wallet codes in the [Wallet Codes](doc:wallet-codes) documentation. The `bankcode` value should correspond to the specific wallet the customer chooses (e.g., Paytm, PhonePe, etc.). For more information, refer to [Wallet Codes](doc:wallet-codes).

* **What is the difference between pg and bankcode parameters?**

  * **pg (Payment Gateway)**: Specifies the payment method category (e.g., `CC` for cards, `NB` for Net Banking, `UPI` for UPI, `CASH` for wallets).

  * **bankcode**: Specifies the specific bank or payment provider within a payment method category (e.g., `SBIB` for SBI Net Banking, `PAYTM` for Paytm wallet, `AMEX` for American Express card).

  For more information, refer to [Payment Mode Codes](doc:payment-mode-codes).

* **How do I validate card numbers before processing payments?**

  You can refer to the [Card Number Formats](doc:card-number-formats) documentation to understand how to validate card numbers. Card numbers can have 13-19 digits depending on the card type. For more information, refer to [Card Number Formats](doc:card-number-formats).

* **What UPI handles are supported by PayU?**

  You can find the list of supported UPI handles in the [UPI Handles](doc:upi-handles) documentation. PayU supports various UPI payment apps and handles. For more information, refer to [UPI Handles](doc:upi-handles).

***

### Error Handling

* **How do I handle payment failures in my integration?**

  When a payment fails, PayU returns error codes and error messages in the response. You should:

  1. Check the `status` parameter in the response (should be "failure" or "pending")
  2. Check the `error` parameter for error codes
  3. Check the `error_Message` parameter for detailed error descriptions
  4. Implement appropriate error handling logic based on the error code
  5. Display user-friendly error messages to customers
  6. Provide options to retry the payment

  For more information, refer to [Error Handling](doc:error-handling) and [Error Codes](ref:error-codes).

* **What should I do if I receive an "Invalid merchant key" error?**

  If you receive an "Invalid merchant key" error, verify the following:

  * Ensure you're using the correct merchant key for your environment (test or production)
  * Check that the key matches the endpoint you're using
  * Verify that there are no extra spaces or special characters in the key
  * Ensure your merchant account is active and properly configured

  For more information, refer to [Error Handling](doc:error-handling).

* **How do I handle pending payment statuses?**

  Pending payment statuses occur when a transaction is initiated but the final status is not yet determined (e.g., waiting for bank confirmation, UPI authorization, etc.). You should:

  1. Implement a polling mechanism to check transaction status using the Verify Payment API
  2. Set up webhooks to receive real-time updates on payment status changes
  3. Enable `callback_on_failure` flag to receive webhooks for pending cases in real-time
  4. Display appropriate messages to customers about pending transactions

  For more information, refer to [Error Handling](doc:error-handling) and [Verify Payment API](ref:verify_payment_api).

* **What should I do if the hash verification fails in the payment response?**

  If hash verification fails, do not process the transaction as it may have been tampered with. You should:

  1. Verify that you're using the correct salt value
  2. Check that you're using the correct reverse hash formula
  3. Ensure parameter order matches the hash formula exactly
  4. Check for any encoding issues (UTF-8, URL encoding, etc.)
  5. Contact PayU support if the issue persists

  For more information, refer to [Generate Hash - Merchant Hosted](doc:generate-hash-merchant-hosted) and [Error Handling](doc:error-handling).

***

### Server-to-Server Integration (Additional FAQs)

* **What are the prerequisites for Server-to-Server (S2S) Integration?**

  The prerequisites for S2S integration are:

  * You must have Payment Card Industry Data Security Standard (PCI-DSS) certification
  * Sufficient technical bandwidth dedicated to managing end-to-end web checkout processes in-house consistently
  * Understanding of workflows, payment processes, website designing fundamentals, and UX management principles

  For more information, refer to [Server-to-Server Integration](doc:server-to-server-integration).

* **What is the difference between Classic Integration, Decoupled Flow, and Direct Authorization for S2S?**

  * **Classic Integration**: You have complete control over card details collection, including CVV and OTP. Highest level of control.

  * **Decoupled Flow**: You collect card details, but PayU manages the OTP step. Provides a balance between control and simplicity.

  * **Direct Authorization**: Used for pre-authorizing funds for later capture. Simple card authentication without capture.

  For more information, refer to [Server-to-Server Integration](doc:server-to-server-integration).

* **Can I use S2S integration for UPI payments?**

  Yes, PayU offers UPI S2S integration options:

  * UPI Collection S2S Integration
  * UPI Intent S2S Integration
  * UPI Omnichannel S2S Integration
  * PhonePe Deep Offers S2S Integration

  For more information, refer to [Server-to-Server Integration](doc:server-to-server-integration).

* **What should I do if I'm using legacy S2S integration for decoupled flow?**

  If you're using legacy integration of decoupled flow for S2S, refer to [Legacy Flow for Server-to-Server](doc:legacy-flow-for-server-to-server) documentation. PayU recommends migrating to the latest S2S integration methods for better features and support.

<br />