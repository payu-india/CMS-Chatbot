---
title: FAQs - Payment Links
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## General

* **What is a payment link, and how does it work?**

A payment link is a URL that merchants can send to their customers to initiate a payment. Customers can open the link, select a payment method, and complete the payment process. Payment links are an alternative to traditional payment methods like Credit/Debit cards and Net Banking. For more information, refer to [Payment Links](doc:payment-links-dashboard).

* **How can I create a payment link using PayU’s API?**

You can create a payment link using **Create Payment Link** API. You need to provide some mandatory parameters such as merchant key, transaction amount, product info, customer details, and callback URL to create a payment link. PayU will return a URL that you can share with your customers to initiate a payment. For more information, refer to [Create Payment Link API](ref:create-payment-links)

* **Can I customize the payment link according to my business requirements?**

Yes, you can customize the payment link by providing additional parameters such as product code, product price, product description, shipping address, and tax amount. You can also add your logo and branding to the payment page. For more information, refer to [Create a Payment Link](doc:create-a-new-payment-link).

* **Which payment methods are supported by PayU’s payment links?**

PayU’s payment links support multiple payment methods such as

* Credit or Debit cards
* Net Banking
* UPI
* Wallets
* EMI
* **How secure are PayU’s payment links?**

PayU’s payment links are secure and compliant with the Payment Card Industry Data Security Standards (PCI DSS). PayU uses advanced encryption and tokenization technologies to protect customer data and prevent fraud.

***

## APIs

* **What is the Get Token API, and how does it work?**

The **Get Token** API is used to retrieve a payment token for a customer, which can be used to initiate a payment using payment links. The API generates a unique token for each customer and returns it to the merchant. The merchant can then use this token to create payment links for the customer. For more information, refer to [Get Token API - Payment Links](ref:get-token-api-payment-links).

* **What are the parameters required to use the Get Token API?**

To use the **Get Token** API, you need to provide the client ID & secret, grant type, and scope. For more information, refer to  [Get Token API - Payment Links](ref:get-token-api-payment-links).

* **How is the payment token generated, and what is its validity?**

The payment token is generated using a combination of the client ID & secret, grant type, and scope. The token is valid for a limited period and can be used to create payment links for the customer during that period.

* **What is the purpose of using a payment token instead of the customer’s details?**

Using a payment token instead of the customer’s details provides an additional layer of security as the customer’s sensitive information is not shared with you. This helps to prevent fraud and ensure the privacy of customer data.

* **What does it mean to have a wrong scope perspective in API usage?** 
  A wrong scope perspective occurs when the scope of an API request is incorrectly defined or misunderstood, leading to errors or unexpected behavior. This can happen if the permissions or access levels required for the API are not correctly specified.
* **How can I identify if I am using the wrong scope in my API request?**
  You can identify a wrong scope by checking the error messages returned by the API. Common indicators include unauthorized access errors, permission denied messages, or responses indicating that the requested resource is not available.
* **What are the common causes of wrong scope issues in API requests?** Common causes include:
  * Incorrectly configured API keys or tokens.
  * Misunderstanding the required permissions for specific API endpoints.
  * Using outdated or incorrect documentation.
  * Not updating the scope when the API’s requirements change.
* **How can I avoid wrong scope issues when using APIs?** 
  To avoid wrong scope issues:
  * Always refer to the latest API documentation.
  * Ensure that your API keys or tokens have the correct permissions.
  * Regularly review and update your API configurations.
  * Test your API requests in a development environment before deploying them to production.
* **What should I do if I encounter a wrong scope error?** 
  If you encounter a wrong scope error:
  * Review the error message for specific details.
  * Check the API documentation to confirm the required scope.
  * Update your API request with the correct scope.
  * If the issue persists, contact the API provider’s support team for assistance.
* **Can wrong scope issues affect the security of my application?** 
  Yes, wrong scope issues can affect security. Using an incorrect scope might grant excessive permissions, leading to potential security vulnerabilities. Conversely, insufficient scope can prevent your application from functioning correctly.
* **How often should I review the scopes used in my API requests?** 

  It’s a good practice to review the scopes used in your API requests regularly, especially when there are updates to the API or changes in your application’s functionality. This helps ensure that your application remains secure and functions as expected.
* **Can I use the same payment token for multiple transactions?**

No, each payment token is valid for a single transaction only. If you want to create payment links for multiple transactions, you need to generate a new payment token for each transaction.

* **How secure is the Get Token API, and what measures are taken to protect customer data?**

PayU follows industry-standard security practices and complies with the Payment Card Industry Data Security Standards (PCI DSS). The **Get Token** API uses advanced encryption and tokenization technologies to protect customer data and prevent fraud. PayU also offers additional security features such as two-factor authentication and fraud detection to further enhance security.

* **What is the Revoke Token API, and how does it work?**

The **Revoke Token** API is used to invalidate a payment token for a customer, which prevents the customer from using it to initiate a payment using payment links. The API requires the merchant key and the payment token to be revoked. For more information, refer to [Revoke Token API - Payment Links](ref:revoke-token-api-payment-links).

* **When should I use the Revoke Token API?**

You should use the **Revoke Token** API when you no longer want a customer to use a payment token to initiate a payment. This may be necessary if the customer has canceled the order or if you suspect fraudulent activity.

* **Can I revoke a token that has already been used for a payment?**

No, you cannot revoke a token that has already been used for payment. Once a payment has been processed using a token, it cannot be revoked.

* **What happens if I revoke a token that has not been used for payment?**

If you revoke a token that has not been used for a payment, the token becomes invalid, and the customer cannot use it to initiate a payment.

Is it possible to revoke a token that has expired? No, it is not possible to revoke a token that has expired. Once a token has expired, it becomes invalid and cannot be used to initiate a payment.

* **Why the following cURL request is failing for Payment Links?**

```curl
curl --location --request POST 'https://uatoneapi.payu.in/payment-links' \
--header 'Authorization: Bearer 715edfd876f240dec9a436961b1ded46' \
--header 'merchantId: XXXXXXX' \
--header 'Content-Type: application/json' \
--data-raw '{
    ""subAmount"": 2.0,
    ""isPartialPaymentAllowed"": false,
    ""description"": ""paymentLink for testing"",
    ""source"": ""API"",
    ""invoiceNumber"": ""123q2315"",
    ""customerName"": null,
    ""customerPhone"": null,
    ""customerEmail"": null,
    ""udf"": {
        ""udf1"": ""TETSPAYU1234""
    },
    ""furl"": ""test.payu.in"",
    ""surl"": ""test.payu.in"",
    ""expiryDate"": ""2024-06-04 13:53:08""
}'
```

The spelling for the following parameters are incorrect:

* furl: it must be failureUrl
* surl : it must be successUrl
