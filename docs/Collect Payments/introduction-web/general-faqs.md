---
title: General FAQs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - troubleshooting
    - PayU India Troubleshooting
    - Integration Troubleshooting
  robots: index
next:
  description: ''
---
---
title: General FAQs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - troubleshootingPric
    - PayU India Troubleshooting
    - Integration Troubleshooting
  robots: index
next:
  description: ''
---
This section provides answers to general frequently asked questions (FAQs) on payment integration.

<Callout icon="📘" theme="info">
  **Reference**: For the product-specific FAQs or refunds, refer to:

  * [FAQs for Refunds](doc:faqs-for-refunds)
  * [FAQs - Recurring Payments](doc:faqs-recurring-payments)
  * [FAQs for Split Settlements](doc:faqs-for-split-settlements)
  * [FAQs for International Payments](doc:faqs-dynamic-currency-conversion)
  * [FAQs for Cross-Border Payments](doc:faqs-for-cross-border-payments)
</Callout>

## Test Environment and Key/Salt

<Accordion title="1. How do I test my payment integration?" icon="fa-info-circle">
  PayU provides a test environment that allows you to test your payment integration without processing real payments. You can access the test key/salt and simulate different payment scenarios to ensure that your integration works correctly. For more information, refer to [Access Test Merchant Key and Salt](doc:generate-merchant-key-and-salt-copy#).
</Accordion>

<Accordion title="2. Where can I get the test Key/Salt details?" icon="fa-info-circle">
  You can get the Key/Salt details from the PayU Dashboard. After you log in to PayU Dashboard, navigate to **Collect Payments> Payment Gateway** and scroll down to view the Key/Salt. For more information, refer to [Access Test Merchant Key and Salt](doc:generate-merchant-key-and-salt-copy#).
</Accordion>

<Accordion title="3. What is the role of Key/Salt in the encryption process?" icon="fa-info-circle">
  Key/Salt are secret values used to encrypt and decrypt data, while salts are random values added to data before it is encrypted to make it more secure. The role of the key is to encrypt the data, while the salt adds randomness to the data to make it more difficult to crack.
</Accordion>

<Accordion title="4. What happens if I lose my Key/Salt?" icon="fa-info-circle">
  A: If you lose your key/salt, you may not be able to access or decrypt your encrypted data. It is important to keep your Key/Salt secure and backed up in a safe place. If you lose your key/salt, you may need to create a new key/salt and re-encrypt your data.
</Accordion>

<Accordion title="5. How do I get my Key/Salt?" icon="fa-info-circle">
  You can get the Key/Salt details from the PayU Dashboard. After you log in to PayU Dashboard, navigate to **Collect Payments> Payment Gateway** and scroll down to view the Key/Salt. For the procedure to get the test Key and Salt, refer to [Access Production Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-copy#).
</Accordion>

<Accordion title="6. Can I share my Key/Salt with others?" icon="fa-info-circle">
  No, it is not recommended to share your key/salt with others. Key/Salt are secret values that should only be known by the owner of the data. Sharing Key/Salt can compromise the security of the data.
</Accordion>

<Accordion title="7. What is Cross-Origin Resource Sharing (CORS)?" icon="fa-info-circle">
  Cross-Origin Resource Sharing (CORS) is a security feature implemented by web browsers that restrict HTTP requests made across different origins. CORS requires that servers include specific headers in their responses to allow or deny access to client-side JavaScript.
</Accordion>

<Accordion title="8. How can I handle CORS errors?" icon="fa-info-circle">
  To handle CORS errors, you can add the appropriate headers to your server-side response, such as Access-Control-Allow-Origin or Access-Control-Allow-Methods. You can also use third-party libraries or frameworks to handle CORS, such as CORS middleware in Node.js or Flask-CORS in Python.
</Accordion>

<Accordion title="9. Can I use my Production Key and Salt details on API Reference?" icon="fa-info-circle">
  No, you can only use your test credentials or Key and Salt from your UAT account. For more information on how to get Key/Salt for Test environment, refer to [Access Test Merchant Key and Salt](doc:generate-merchant-key-and-salt-copy#).
</Accordion>

## Request/Response

<Accordion title="1. What should I do if my request parameters are not working?" icon="fa-info-circle">
  If your request parameters are not working, you should check to make sure that they are correctly formatted and that their values are valid. You should also check the documentation for the API or web service you are using to make sure that you are using the correct parameters and values. If you are still having issues, you may need to contact PayU support for assistance.
</Accordion>

<Accordion title="2. I am receiving a “bad request” error message when posting my API request. What could be causing this?" icon="fa-info-circle">
  A “bad request” error message typically indicates that there is something wrong with the request parameters being sent. Double-check that all required parameters are included in the request and that they are in the correct format. Check the API documentation for the specific endpoint being used to ensure that all required parameters are included.
</Accordion>

<Accordion title="3. I am not receiving any response when posting my API request. What could be causing this?" icon="fa-info-circle">
  The causes for not receiving a response when posting an API request can be any of the following:

  * Check whether your Internet or Broadband connection is working.
  * Check that all required parameters are included in the request and that they are in the correct format.
  * Check the API documentation for the specific endpoint being used to ensure that the correct HTTP method is being used (e.g., POST vs GET).
</Accordion>

<Accordion title="4. I am receiving an “invalid parameter” error message when posting my API request. What does this mean?" icon="fa-info-circle">
  An “invalid parameter” error message typically means that one or more of the parameters being sent in the API request is not valid. Check that all parameters are spelled correctly and that they are in the correct format. Also, refer to the API documentation for the specific endpoint being used to ensure that all parameters are being sent correctly.
</Accordion>

<Accordion title="5. The response from PayU is not in JSON format and it is in an encrypted format. How do I get the response in JSON format?" icon="fa-info-circle">
  You need to append “?form=2” with the endpoint to get the response in JSON format. For example, the following endpoints are used for integration APIs such as **Verify Payment**, **Get Transaction Details**, **Get TDR**, **Eligible Bins for EMI**, **Create Invoice**, and **Get BIN Info** APIs:

  | **Test Environment**       | [https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2) |
  | -------------------------- | ------------------------------------------------------------------------------------------------------------ |
  | **Production Environment** | [https://info.payu.in/merchant/postservice?form=2](https://info.payu.in/merchant/postservice?form=2)         |
</Accordion>

<Accordion title="6. When I posted an API with all the necessary values to PayU, I got a response similar to the following, and not sure why?" icon="fa-info-circle">
  a:2:\{s:6:""status"";i:0;s:3:""msg"";s:21:""Merchant key is empty"";}"

  In the cURL request, if there are unwanted spaces in the key, Salt, or with any other parameter’s value, the response is similar to the above. Check and remove the unwanted spaces in the cURL request.
</Accordion>

## Webhooks

<Accordion title="1. What is a webhook?" icon="fa-info-circle">
  A webhook is an HTTP callback. The callback is done to a URL specified while creating a webhook. The webhook callbacks are event-driven i.e. a callback to a webhook will be done whenever the event associated with the webhook occurs. For example, Successful Payment Webhook – The event associated with this webhook is Successful Payment.
</Accordion>

<Accordion title="2. How do I configure a webhook URL for payment notifications?" icon="fa-info-circle">
  To configure a webhook:
  1. Sign in to PayU Dashboard and go to **Settings > Webhooks**.
  2. Create a webhook and enter a publicly accessible HTTPS URL.
  3. Select the payment events that your endpoint must receive.
  4. Test the webhook and confirm that your endpoint returns a successful HTTP response.
  5. Validate the hash in every payload and handle duplicate events idempotently.
  A webhook supplements the browser redirect to `surl` or `furl`; it does not replace those URLs.
  For more information, refer to [Create a New Webhook](doc:create-a-new-webhook) and [Webhooks](doc:webhooks).
</Accordion>

<Accordion title="3. How do I create a webhook using PayU Dashboard?" icon="fa-info-circle">
  You can create a webhook using Dashboard or manually:

  * **Using Dashboard**

    To create a webhook, you need to follow these steps:

    1. Log in to your PayU Dashboard.
    2. Navigate to the **Settings> Webhook**.
    3. Click **Create Webhook**.
    4. Select any of the following types from the Type drop-down list:
       * **Payments**
       * **Payouts**
    5. Select the event type from the **Event** drop-down list.
    6. Enter the URL where you want to receive the webhook callbacks in the **Webhook URL** field.
    7. Click **Create**.

  * **Manually**

    To create webhooks manually during integration with PayU:

    1. Create a server URL from your business server landscape and share it with PayU, along with its server IP address. It is the URL at which the transaction response from PayU will hit. For example, [www.test.payu.in/success/response](http://www.test.payu.in/success/response)
    2. PayU will configure the merchant’s server URL at its backend, mapping it against the MID and key of that particular merchant.
    3. PayU will whitelist the webhook URL provided by the merchant in its systems. For more information, contact the PayU Integration Team by email: [integration@payu.in](mailto:integration@payu.in).
</Accordion>

<Accordion title="What are the different types of events for which webhooks can be created?" icon="fa-info-circle">
  Currently, PayU provides two types of webhook events:

  1. When a payment is successful
  2. When a payment fails
</Accordion>

<Accordion title="4. How do I test my webhooks?" icon="fa-info-circle">
  You can test your webhooks by using the Test Webhook feature available in your PayU Dashboard.
</Accordion>

<Accordion title="5. How do I create a webhook?" icon="fa-info-circle">
  To create a webhook, you will need to create a URL at your server which will be able to receive the callback message that will be sent. Once you have created the URL, you can go to your PayU merchant account -> Settings -> My Account ->Webhook Click on Create New Webhook button.
</Accordion>

<Accordion title="Do I need to whitelist any PayU Server IP addresses for webhooks?" icon="fa-info-circle">
  Yes, you need to whitelist the following IP addresses in your firewall so that the webhooks you had created or configured work:

  | **52.140.8.88**     | **3.7.89.1**    |
  | ------------------- | --------------- |
  | **180.179.174.1**   | **3.7.89.2**    |
  | **180.179.174.2**   | **3.7.89.3**    |
  | **180.179.165.250** | **3.7.89.8**    |
  | **180.179.174.1**   | **3.7.89.9**    |
  | **180.179.174.2**   | **3.7.89.10**   |
  | **52.140.8.64**     | **52.140.8.89** |
  | **10.251.7.118**    | **52.140.8.65** |
</Accordion>

<Accordion title="6. Can I create webhooks manually?" icon="fa-info-circle">
  To use Webhooks during integration with PayU:

  1. Create a server URL from your business server landscape and share it with PayU, along with its server IP address. It is the URL at which the transaction response from PayU will hit. For example, [www.test.payu.in/success/response](http://www.test.payu.in/success/response)
  2. PayU will configure the merchant’s server URL at its backend, mapping it against the MID and key of that particular merchant.
  3. PayU will whitelist the webhook URL provided by the merchant in its systems. For more information, contact the PayU Integration Team by email: [integration@payu.in](mailto:integration@payu.in).
</Accordion>

## Pricing

<Accordion title="7. What is the fee or TDR for using PayU’s payment gateway?" icon="fa-info-circle">
  PayU charges fees for processing payments through its gateway, which may vary depending on factors such as transaction volume and payment method. For more information, contact your PayU Key Account Manager (KAM) or customer support.
</Accordion>

## UPI
<Accordion title="8. Why is the UPI payment option greyed out or showing an orange dot with no explanation?" icon="fa-info-circle">
  The UPI option can be unavailable when PayU cannot detect a compatible UPI app on the customer's device. Ask the customer to install or enable a supported UPI app, such as Google Pay, PhonePe, or Paytm, and then retry the payment.
  If you control the checkout interface, display a message explaining that a compatible UPI app is required.
  For more information, refer to [UPI Intent Integration](doc:upi-intent-integration).
</Accordion>
<Accordion title="9. What is NPCI OC190 compliance, and is it handled by PayU Hosted Checkout?" icon="fa-info-circle">
  NPCI OC190 requirements include UPI Smart Intent, appropriate ordering of UPI apps, and support for applicable QR flows.
  PayU handles these requirements on PayU Hosted Checkout. Merchants using a Merchant Hosted or other seamless integration must implement the applicable Smart Intent requirements in their own checkout experience.
  For more information, refer to [PayU Hosted Checkout](doc:prebuilt-checkout-payu-hosted) and [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow).
</Accordion>
<Accordion title="10. How do I migrate my integration from UPI Collect flow to UPI Intent flow?" icon="fa-info-circle">
  To migrate:
  1. Update your PayU integration or SDK to a version that supports UPI Intent.
  2. Confirm that UPI Intent is enabled for your merchant account.
  3. Configure the required UPI Intent request parameters for your web or mobile integration.
  4. Test the flow on physical devices with supported UPI apps; simulators cannot complete the app-switch flow reliably.
  5. Verify the final transaction status before fulfilling the order.
  For enablement or account configuration, contact your PayU Key Account Manager (KAM).
  For more information, refer to [UPI Intent Integration](doc:upi-intent-integration).
</Accordion>
## Payment methods and merchant configuration
<Accordion title="1. Is there an API to fetch an EMI schedule for a payment amount and offer ID?" icon="fa-info-circle">
  Use the applicable EMI checkout-details API to retrieve eligible tenures and the amount breakdown before initiating the payment. The request typically requires the merchant key, transaction amount, relevant bank or offer details, and a hash. Use the returned tenure, interest, and instalment details to display the schedule.
  For more information, refer to [Get EMI Amount according to Interest API](ref:get_emi_according_to_interest_api).
</Accordion>
<Accordion title="2. What test cards are available for successful, failed, pending, EMI, and 3DS scenarios?" icon="fa-info-circle">
  PayU maintains test credentials and scenario-specific instructions for cards, UPI IDs, and wallets. Use only the values documented for the PayU test environment; do not use test credentials in production.
  For more information, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets).
</Accordion>
<Accordion title="3. How do I activate American Express card payments for my merchant account?" icon="fa-info-circle">
  American Express enablement is account-specific and can require additional underwriting, documentation, commercial terms, and acquiring-bank approval. Contact your PayU Key Account Manager (KAM) to confirm eligibility, required documents, and the expected activation timeline.
</Accordion>
<Accordion title="4. What is a dynamic descriptor for card payments, and how do I configure it?" icon="fa-info-circle">
  A dynamic descriptor controls the merchant text that can appear on the customer's card statement. A recognisable descriptor can reduce customer confusion and chargebacks.
</Accordion>
<Accordion title="5. What should I check when a hash mismatch error occurs on the callback or response?" icon="fa-info-circle">
  Check the following:
  * Use the Salt and merchant key for the same environment as the endpoint.
  * Follow the documented reverse-hash formula and parameter order exactly.
  * Preserve empty fields and additional charges in the formula where required.
  * Check UTF-8 and URL-decoding behaviour for special characters.
  * Remove unintended spaces or line breaks from parameter values.
  * Log the pre-hash string securely and compare it with the expected sequence. Never log the Salt.
  Reject a response when hash validation fails.
  For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted) and [Using PayU Hash Verification Tool](doc:using-payu-hash-verification-tool).
</Accordion>
<Accordion title="6. How do I handle a transaction stuck in pending status?" icon="fa-info-circle">
  Do not fulfil the order while the payment status is pending. Use the Verify Payment API to retrieve the current status and use webhooks to receive subsequent updates. If you poll, use a bounded retry interval and stop after your business-defined timeout.
  Reconcile unresolved transactions before fulfilment. If the status remains pending beyond the normal processing window, raise a PayU support ticket with the transaction ID.
  For more information, refer to [Verify Payment API](ref:verify_payment_api) and [Webhooks](doc:webhooks).
</Accordion>
<Accordion title="7. What checkout page customization options are available?" icon="fa-info-circle">
  The available customization depends on the integration:
  * **PayU Hosted Checkout:** Configure supported branding options such as the logo and theme while PayU hosts the payment page.
  * **Merchant Hosted Checkout:** Control the checkout UI and payment-mode presentation on your website, subject to security and PCI-DSS requirements.
  * **CheckoutPro mobile SDKs:** Configure supported themes, colours, fonts, and payment-mode ordering through the SDK.
  For more information, refer to [PayU Payment Page Customization](doc:payu-payment-page-customization) and [Merchant Hosted Checkout](doc:custom-checkout-merchant-hosted).
</Accordion>
<Accordion title="8. How do I implement offer or discount codes in a payment request?" icon="fa-info-circle">
  Create and configure the offer in PayU Dashboard, then pass the offer identifier required by your integration in the payment request. Validate the offer's dates, eligibility rules, payment modes, and discount configuration before going live. Use the payment response to reconcile the applied discount.
  Contact your PayU Key Account Manager (KAM) for enablement or configuration of account-specific and bank-funded offers.
  For more information, refer to [Offers Integration](doc:offers-integration).
</Accordion>
<Accordion title="9. How can I control payment mode ordering or sequencing on checkout?" icon="fa-info-circle">
  The available control depends on the integration:
  * **PayU Hosted Checkout:** Use the supported parameters to enforce or remove payment categories. Contact your PayU Key Account Manager (KAM) for account-level sequencing options.
  * **Merchant Hosted Checkout:** Retrieve the available payment options and render them in the required order.
  * **Mobile SDKs:** Use the SDK's payment-mode ordering configuration.
  Ordering must comply with applicable NPCI requirements for UPI.
  For more information, refer to [Enforce Pay Method or Remove Category](doc:enforce-pay-method-or-remove-category).
</Accordion>