---
title: Direct Authentication Integration
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
This section describes direct authentication flow with seamless integration over the Redirect experience for cards involves the following steps:

### Steps to Integrate

1. [Post the transaction to PayU](#step-1-post-the-transaction-to-payu)
2. [Check Response from PayU](#step-2-check-response-from-payu)

> 👍 Before you begin:
>
> PayU recommends you to integrate with Test environment initially. For more information, contact you PayU Key Account Manager (KAM) or PayU Support.

## Step 1: Post the transaction to PayU

Initiate an authorization request with the payment details provided post a successful authentication via the MPI/3DSS.  For the request parameters, refer to  <a href="[[https://docs.payu.in/v2/reference/_payment_s2s_direct_authorization_flow](https://docs.payu.in/v2/reference/cards-direct-authorization-flow-s2s-v2-_payment/)](https://docs.payu.in/v2/reference/cards-direct-authorization-flow-s2s-v2-_payment/)" target="_blank">Cards Direct Authorization Flow</a>.

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
                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Indicates the transaction S2S flow type and must be set to "3" for Direct Authorization Flow.</p></td>
                  <td style="border: 1px solid #ddd; padding: 8px;"><p>3</p></td>
                </tr>
                <tr>
                  <td style="border: 1px solid #ddd; padding: 8px;"><p>authenticationFlow<br><code>mandatory for S2S</code></p></td>
                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Indicates the authentication flow type and must be set to "REDIRECT" for Direct Authorization Integration.</p></td>
                  <td style="border: 1px solid #ddd; padding: 8px;"><p>REDIRECT</p></td>
                </tr>
                <tr>
                  <td style="border: 1px solid #ddd; padding: 8px;"><p>createOrder<br><code>optional</code></p></td>
                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> Whether to create an order during the payment process.</p></td>
                  <td style="border: 1px solid #ddd; padding: 8px;"><p>false</p></td>
                </tr>
                </tbody>
                </table>
  `}</HTMLBlock>
</Accordion>

#### callBackActions object fields description

<Accordion title="callBackActions object" icon="fa-code">
  <CallbackActions_object />
</Accordion>

#### billingDetails object fields description

<Accordion title="billingDetails object" icon="fa-code">
  <BillingDetails_object />
</Accordion>

### authorization object fields description

<Accordion title="authorization object" icon="fa-code">
  <V2_authorization_cards />
</Accordion>

### threeDS2RequestData object fields description

<Accordion title="threeDS2RequestData object" icon="fa-code">
  <ThreeDSRequestData_object />
</Accordion>

> ❗️ Error Handling
>
> If any error message is displayed with an error code, refer to the [Error Codes](https://docs.payu.in/v1/reference/error-codes) section to understand the reason for these error codes.

### Sample request

```curl
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
        "txnS2sFlow": "3",
        "createOrder": "false"
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

### Sample response

```
{
  "result": {
    "redirectUrl": "https://secure.payu.in/ResponseHandler.php",
    "authAction": "https://api.payu.in/payments/21667772394/otps",
    "paymentId": "21667772394",
    "redirectTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vbmV0YmFua2luZy5oZGZjYmFuay5jb20vbmV0YmFua2luZy9tZXJjaGFudD9DbGllbnRDb2RlPTE1NDkxMyZNZXJjaGFudENvZGU9UEFZVUZBQ0VCT09LJlR4bkN1cnJlbmN5PUlOUiZUeG5BbW91bnQ9MjUwMDAuMDAmVHhuU2NBbW91bnQ9MCZNZXJjaGFudFJlZk5vPWs0cWh3NGVsYXY2MmxwNjJjbSZTdWNjZXNzU3RhdGljRmxhZz1OJkZhaWx1cmVTdGF0aWNGbGFnPU4mRGF0ZT0yNi8xMS8yMDI0IDAwOjAwOjAwJlJlZjE9JlJlZjI9NDAzYmIzODkxY2Y5NGEzNmI0ZGQxOTlkOWNjZWVjNmUmUmVmMz0mUmVmND0mUmVmNT0mRHluYW1pY1VybD1odHRwczovL3NlY3VyZS5wYXl1LmluL2I0NDdmZmViZDg4NDNjZTEzYzlmODVhZjhlOTA0ZmQyL0NvbW1vblBnUmVzcG9uc2VIYW5kbGVyLnBocCZDaGVja1N1bT0zMTAxMzgyNDM2IiBtZXRob2Q9InBvc3QiPjwvZm9ybT48c2NyaXB0IHR5cGU9J3RleHQvamF2YXNjcmlwdCc+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB3aW5kb3cub25sb2FkPWZ1bmN0aW9uKCl7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZG9jdW1lbnQuZm9ybXNbJ3BheW1lbnRfcG9zdCddLnN1Ym1pdCgpOwogICAgICAgICAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgICAgICAgICA8L3NjcmlwdD48L2JvZHk+PC9odG1sPg==",
    "card": {
      "binData": {
        "pureS2SSupported": false,
        "issuingBank": "INDUSIND",
        "category": "debitcard",
        "cardType": "MAST",
        "isDomestic": true
      }
    }
  },
  "status": "PENDING"
}
```

## Step 2: Verify the payment

> 📘 Note:
>
> This API is backward compatible and you can continue to the existing integration parameters to process the 3DS 1.0.2 transactions.

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