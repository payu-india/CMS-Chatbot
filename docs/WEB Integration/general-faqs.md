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
This section provides answers to general frequently asked questions (FAQs) on payment integration.

<Callout icon="📘" theme="info">
  **Reference**: For the product-specific FAQs or refunds, refer to:

  * [FAQs for Refunds](doc:faqs-for-refunds)
  * [FAQs - Recurring Payments](doc:faqs-recurring-payments)
  * [FAQs for Split Settlements](doc:faqs-for-split-settlements)
  * [FAQs for International Payments](doc:faqs-dynamic-currency-conversion)
  * [FAQs for Cross-Border Payments](doc:faqs-for-cross-border-payments)
</Callout>

## Test Environment

* **How do I test my payment integration?**

  PayU provides a test environment that allows you to test your payment integration without processing real payments. You can access the test key/salt and simulate different payment scenarios to ensure that your integration works correctly. For more information, refer to [Access Test Merchant Key and Salt](doc:generate-merchant-key-and-salt-copy#)

## Key/Salt

* **Where can I get the test Key/Salt details?**

  You can get the Key/Salt details from the PayU Dashboard. After you log in to PayU Dashboard, navigate to **Collect Payments> Payment Gateway** and scroll down to view the Key/Salt. For more information, refer to [Access Test Merchant Key and Salt](doc:generate-merchant-key-and-salt-copy#).

* **What is the role of Key/Salt in the encryption process?**

  Key/Salt are secret values used to encrypt and decrypt data, while salts are random values added to data before it is encrypted to make it more secure. The role of the key is to encrypt the data, while the salt adds randomness to the data to make it more difficult to crack.

* **What happens if I lose my Key/Salt?**

  A: If you lose your key/salt, you may not be able to access or decrypt your encrypted data. It is important to keep your Key/Salt secure and backed up in a safe place. If you lose your key/salt, you may need to create a new key/salt and re-encrypt your data.

* **How do I get my Key/Salt?**

  You can get the Key/Salt details from the PayU Dashboard. After you log in to PayU Dashboard, navigate to **Collect Payments> Payment Gateway** and scroll down to view the Key/Salt. For the procedure to get the test Key and Salt, refer to [Access Production Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-copy#).

* **Can I share my Key/Salt with others?**

  No, it is not recommended to share your key/salt with others. Key/Salt are secret values that should only be known by the owner of the data. Sharing Key/Salt can compromise the security of the data.

* **What is Cross-Origin Resource Sharing (CORS)?**

  Cross-Origin Resource Sharing (CORS) is a security feature implemented by web browsers that restrict HTTP requests made across different origins. CORS requires that servers include specific headers in their responses to allow or deny access to client-side JavaScript.

* **How can I handle CORS errors?**

  To handle CORS errors, you can add the appropriate headers to your server-side response, such as Access-Control-Allow-Origin or Access-Control-Allow-Methods. You can also use third-party libraries or frameworks to handle CORS, such as CORS middleware in Node.js or Flask-CORS in Python.

* **Can I use my Production Key and Salt details on API Reference?**

  No, you can only use your test credentials or Key and Salt from your UAT account. For more information on how to get Key/Salt for Test environment, refer to [Access Test Merchant Key and Salt](doc:generate-merchant-key-and-salt-copy#).

## Request/Response

* **What should I do if my request parameters are not working?**

  If your request parameters are not working, you should check to make sure that they are correctly formatted and that their values are valid. You should also check the documentation for the API or web service you are using to make sure that you are using the correct parameters and values. If you are still having issues, you may need to contact PayU support for assistance.

* **I am receiving a “bad request” error message when posting my API request. What could be causing this?**

  A “bad request” error message typically indicates that there is something wrong with the request parameters being sent. Double-check that all required parameters are included in the request and that they are in the correct format. Check the API documentation for the specific endpoint being used to ensure that all required parameters are included.

* **I am not receiving any response when posting my API request. What could be causing this?**

  The causes for not receiving a response when posting an API request can be any of the following:

* Check whether your Internet or Broadband connection is working.

* Check that all required parameters are included in the request and that they are in the correct format.

* Check the API documentation for the specific endpoint being used to ensure that the correct HTTP method is being used (e.g., POST vs GET).

* **I am receiving an “invalid parameter” error message when posting my API request. What does this mean?**

  An “invalid parameter” error message typically means that one or more of the parameters being sent in the API request is not valid. Check that all parameters are spelled correctly and that they are in the correct format. Also, refer to the API documentation for the specific endpoint being used to ensure that all parameters are being sent correctly.

* **The response from PayU is not in JSON format and it is in an encrypted format. How do I get the response in JSON format?**

  You need to append “?form=2” with the endpoint to get the response in JSON format. For example, the following endpoints are used for integration APIs such as **Verify Payment**, **Get Transaction Details**, **Get TDR**, **Eligible Bins for EMI**, **Create Invoice**, and **Get BIN Info** APIs:

| **Test Environment**       | [https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2) |
| -------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Production Environment** | [https://info.payu.in/merchant/postservice?form=2](https://info.payu.in/merchant/postservice?form=2)         |

* **When I posted an API with all the necessary values to PayU, I got a response similar to the following, and not sure why?**

a:2:\{s:6:""status"";i:0;s:3:""msg"";s:21:""Merchant key is empty"";}"

In the cURL request, if there are unwanted spaces in the key, Salt, or with any other parameter’s value, the response is similar to the above. Check and remove the unwanted spaces in the cURL request.

## Webhooks

* **What is a webhook?**

  A webhook is an HTTP callback. The callback is done to a URL specified while creating a webhook. The webhook callbacks are event-driven i.e. a callback to a webhook will be done whenever the event associated with the webhook occurs. For example, Successful Payment Webhook – The event associated with this webhook is Successful Payment.

* **How do I create a webhook using PayU Dashboard?**

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

* **What are the different types of events for which webhooks can be created?**

  Currently, PayU provides two types of webhook events:

1. When a payment is successful
2. When a payment fails

* **How do I test my webhooks?**

  You can test your webhooks by using the Test Webhook feature available in your PayU Dashboard.

* **How do I create a webhook?**

  To create a webhook, you will need to create a URL at your server which will be able to receive the callback message that will be sent. Once you have created the URL, you can go to your PayU merchant account -> Settings -> My Account ->Webhook Click on Create New Webhook button.

* **Do I need to whitelist any PayU Server IP addresses for webhooks?**

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

* **Can I create webhooks manually?**

  To use Webhooks during integration with PayU:

1. Create a server URL from your business server landscape and share it with PayU, along with its server IP address. It is the URL at which the transaction response from PayU will hit. For example, [www.test.payu.in/success/response](http://www.test.payu.in/success/response)
2. PayU will configure the merchant’s server URL at its backend, mapping it against the MID and key of that particular merchant.
3. PayU will whitelist the webhook URL provided by the merchant in its systems. For more information, contact the PayU Integration Team by email: [integration@payu.in](mailto:integration@payu.in).

## Pricing

**What is the fee or TDR for using PayU’s payment gateway?**

PayU charges fees for processing payments through its gateway, which may vary depending on factors such as transaction volume and payment method. For more information, contact your PayU Key Account Manager (KAM) or customer support.
