---
title: S2S Classic Integration
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
This is server-to-server integration over the Redirect experience for cards using **v2/payments** API involves the following steps:

### Steps to Integrate

1. [Initiate payment request with PayU](#step-1-Initiate-payment-request-with-payU)
2. [Redirect the customer](#step-2-redirect-the-customer)
3. [Check the response from PayU](#step-3-check-the-response-from-payu)

> 👍 Before you begin:
>
> PayU recommends you to integrate with Test environment initially. For more information, contact you PayU Key Account Manager (KAM) or PayU Support.

## Step 1: Initiate payment request with PayU

The merchant initiates PayU with the required transaction mandatory or optional parameters. This needs to be a server-to-server cURL call request. URL, parameters, and descriptions. The response for the S2S payment request is not similar to Merchant Hosted or PayU Hosted Checkout.

You can collect card payments using Server-to-Server integration using classic integration. For S2S Classic integration, the **additionalInfo.txnFlow** field is set to **4**.

### Environment

<V2_payment_envrionment />

> 📘 Reference:
>
> For the **Try It** experience and response, refer to <a href="https://docs.payu.in/v2/reference/cards-classic-integration" target="_blank">Cards Classic Integration</a> under API Reference.

### Request header

<V2_payment_header_params />

### Request body

The following table describes the request body parameters:
<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>accountId<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The merchant key provided by PayU during onboarding.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>MERCHANT123</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txnId<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Transaction ID for transaction tracking and this must be unique for every transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>REF123456</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentMethod<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the payment method used. For more information, refer to <a href="#paymentmethod-object-fields-description">paymentMethod object fields description</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>order<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the transaction order including product information, ordered items, user-defined fields, and payment charge specifications. For more information, refer to <a href="#order-object-fields-description">order object fields description</a></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>additionalInfo<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Additional information including enforced payment methods, single instalment, virtual payment address (VPA), and various options for user preferences during the transaction. For more information, refer to <a href="#additionalinfo-object-fields-description">additionalInfo object fields description</a></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>callBackActions<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Actions to perform on the payment server in different scenarios. For example, success, failure, cancellation, cash on delivery, etc. For more information, refer to <a href="#callbackactions-object-fields-description">callbackActions object fields description</a></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>billingDetails <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Billing details of the customer including name, address, phone number, email, etc. For more information, refer to <a href="#billingdetails-object-field-descriptions">billingDetails object field descriptions</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

##### paymentMethod object fields description
<Accordion title="paymentMethod object" icon="fa-code">
<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>name<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field must contain the payment mode code. For Classic Integration, use "CreditCard" or "DebitCard". For more information, refer to <a href="https://docs.payu.in/v1/docs/payment-mode-codes">Payment Mode Codes</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>CreditCard</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>bankCode<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field must contain the card type code. For more information, refer to <a href="https://docs.payu.in/v1/docs/card-type-codes-and-supported-banks-for-cards">Card Type Codes and Supported Banks for Cards</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>CC</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentCard<br><code>mandatory for cards</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> This object contains the physical card or saved card token details. For more information, refer to <a href="#paymentcard-object-fields-description">paymentCard object fields description</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>
</Accordion>

#### paymentCard object fields description
<Accordion title="paymentCard object" icon="fa-code">
<V2_paymentCard />
</Accordion>

#### order object fields description
<Accordion title="order object" icon="fa-code">
<V2_order_object />
</Accordion>

#### additionalInfo object fields description

<AdditionalI_Info_object />
<Accordion title="AdditionalInfo object" icon="fa-code">
<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txnFlow<br><code>mandatory for S2S</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Indicates the transaction S2S flow type and must be set to "4" for Classic Integration.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>4</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>authenticationFlow<br><code>mandatory for S2S</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Indicates the authentication flow type and must be set to "REDIRECT" for Classic Integration.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>REDIRECT</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>createOrder<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> Whether to create an order during the payment process.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>false</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>preAuthorize<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Set to "1" for authorization-only transactions.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>
</Accordion>

#### callBackActions object fields description
<CallbackActions_object />

#### billingDetails object fields description
<Accordion title="callBackActions object" icon="fa-code">
<BillingDetails_object />
</Accordion>


> ❗️ Error Handling
>
> If any error message is displayed with an error code, refer to the [Error Codes](https://docs.payu.in/v1/reference/error-codes) section to understand the reason for these error codes.

### Sample request

```curl
curl --location 'https://apitest.payu.in/v2/payments' \
--header 'date: Tue, 05 Nov 2024 06:12:57 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="d583ff8069c7dfa8340464a24bdd01cbebf4432b4dfe4de862065cc9c9dc622c24c77cb1ac1142bf581ec07eca8d0ec78a66db93f6cd557d0da552f05c0825e3"' \
--header 'Content-Type: application/json' \
--header 'mid: 8390470' \
--header 'X-CREDENTIAL-USERNAME: UMXDPA' \
--data-raw '{
    "accountId": "UMXDPA",
    "referenceId": "ZP6267f0d2996ce",
    "amount": 10,
    "paymentMethod": {
        "name": "CreditCard",	
        "bankCode": "CC", 		
        "paymentCard": {	
            "cardNumber": 500***1234560***,	
            "validThrough": "04/2027",
            "ownerName": "Ashish",
            "cvv": ***,		
            "tavv": "/wAAAAAAPtP+g6IAmbSeg1gAAAA=",
            "last4Digits": "0000",
            "cardTokenType": "NETWORK",	
            "cardToken": "29850879bf39848ca078727b8e1a95165a41cea1"
        }
    },
    "order": {
        "productInfo": "string",
        "orderedItem": [
            {
                "itemId": null,	
                "description": "AAA", 
                "quantity": null,
                "amount" : 10.0
            }
        ],
        "userDefinedFields": {
            "udf1": "",
            "udf2": "",
            "udf3": "",
            "udf4": "",
            "udf5": "",
            "udf6": "",
            "udf7": "",
            "udf8": "",
            "udf9": "",
            "udf10": ""
        },
      "paymentChargeSpecification": {
            "price": 10,
        }  
    },
    "additionalInfo": { 
        "txnS2sFlow": "4",
        "authenticationFlow": "REDIRECT"	
    },
    "callBackActions": {
        "successAction": "https://testapi.payu.in/admin/testresponsev2?action=successAction",
        "failureAction": "https://testapi.payu.in/admin/testresponsev2?action=failureAction",
        "cancelAction": "https://testapi.payu.in/admin/testresponsev2?action=cancelAction",
        "codAction": "https://testapi.payu.in/admin/testresponsev2?action=codAction",
        "termAction": "string",
        "timeOutAction": null,
        "returnAction": "https://testapi.payu.in/admin/testresponsev2?action=successAction"
    },
   "billingDetails": {
         "firstName": "sartaj",
         "lastName": "",
         "phone": "9876543210",
         "email": "testv2@example.in",
         "city": "Bharatpur",
         "state": "Rajasthan",
         "country": "India",
         "zipCode": "321028"
    },
   "deviceInfo": {
         "platform": null,
         "version": null,
         "ip": null,
         "userAgent": null,
         "acceptHeader": null,
         "language": null,
         "colorDepth": null,
         "screenHeight": null,
         "screenWidth": null,
         "timeZone": null,
         "javaEnabled": null
   }
}'
```

### Sample response

```
curl --location 'https://apitest.payu.in/v2/payments' \
--header 'date: Thu, 27 Mar 2025 10:12:27 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="ec84843a663143bb89391f6fa2d4b9404bab1543a3eee81263b4a507ebf5d289d8fad1fbcdd59da820951e3e0f9b0b0b3d1bad9b41338804e7c42a8a6197c6e9"' \
--header 'Content-Type: application/json' \
--header 'Cookie: PHPSESSID=sclorpmpb4ngion5e996os22ao' \
--data-raw '{
    "accountId": "smsplus",
    "referenceId": "b5f2d8785768087678fn4",
    "amount": 10,
    "currency": "INR",
    "paymentSource": "WEB",
    "paymentMethod": {
        "name": "CreditCard",
        "bankCode": "CC",
        "paymentCard": {
            "cardNumber": 5497774415170603,
            "validThrough": "05/2025",
            "cvv": 123,
            "cardToken": "29850879bf39848ca078727b8e1a95165a41cea1",
            "ownerName": "Ashish",
            "issuer": "ICICI",
            "bin": "500446",
            "last4Digits": "0000",
            "cardHash": null,
            "cardTokenType": "NETWORK",
            "tavv": "/wAAAAAAPtP+g6IAmbSeg1gAAAA="
        }
    },
    "order": {
        "productInfo": "qwertyuiopasdfghjkl",
        "orderedItem": [
            {
                "itemId": "1",
                "description": "string",
                "quantity": 1
            }
        ],
        "userDefinedFields": {
            "udf1": "",
            "udf2": "",
            "udf3": "",
            "udf4": "",
            "udf5": "",
            "udf6": "",
            "udf7": "",
            "udf8": "",
            "udf9": "",
            "udf10": ""
        },
        "paymentChargeSpecification": {
            "price": 10,
            "convenienceFee": "CC:12,AMEX:19,SBIB:98,DINR:2,DC:25,NB:55",
            "offers": {
                "applied": [
                    {
                        "offerId": "no_offer",
                        "amount": null
                    }
                ]
            }
        }
    },
    "additionalInfo": {
        "txnS2sFlow": "4",
        "authenticationFlow": "REDIRECT"
    },
    "callBackActions": {
        "successAction": "https://apitest.payu.in/test_response",
        "failureAction": "https://apitest.payu.in/test_response",
        "cancelAction": "https://apitest.payu.in/test_response"
    },
    "billingDetails": {
        "firstName": "sartaj",
        "lastName": "",
        "phone": "9876543210",
        "email": "testv2@example.in",
        "city": "Bharatpur",
        "state": "Rajasthan",
        "country": "India",
        "zipCode": "321028"
    },
    "authorization": {
        "eci": "05",
        "cavv": "AAABAWFlmQAAAABjRWWZEEFgFz",
        "flowType": "Frictionless",
        "threeDSTransID": "67b4c71f-19bf-4d97-bd09-4e3687dc9e42",
        "threeDSServerTransID": "eea30d14-71cf-41af-b961-f95b7d67dc93",
        "threeDSTransStatus": "Y",
        "threeDSTransStatusReason": "01",
        "aquirer_bin": "401200",
        "additionalInfo": {
            "authUdf1": "string",
            "authUdf2": "string"
        }
    },
    "threeDS2RequestData": {
        "threeDSVersion": "2.2.0",
        "deviceChannel": "APP"
    }
}'
```

## Step 2: Redirect the customer

Redirect the customer to the bank page using the **acsTemplate** as received in [Step 1](#Initiate-payment-request-with-payu).

## Step 3: Verify payment

### Sample response

The sample response after the customer makes payment will be similar to v2 merchant hosted checkout payments.

> 📘 Note:
>
> Reverse hashing of the response is not required with that of v2/payment API.

```plaintext
Array
(
    [referenceId] => b5f2d8785768087678fm9
    [paymentId] => 1999110000001769
    [message] => Please call verify api to get the transaction status
)
```

Verify the transaction details using the Verification APIs. For API reference, refer to [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api) under API Reference.

> 📘 Tip
>
> The transaction ID that you posted in Step 1 with PayU must be used here.