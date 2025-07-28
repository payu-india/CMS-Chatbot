---
title: Cards Classic Integration - v2 Payment API
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
You can collect card payments using classic seamless integration. For seamless Classic integration, the **additionalInfo.txnS2sFlow** field is set to **4**.

The Classic Seamless Integration supports both physical card details and saved card tokens, providing a complete server-to-server payment solution with 3DS authentication redirection.

## Environment

<V2_payment_envrionment />

## Request header

<V2_payment_header_params />

## Request body

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>accountId<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The merchant key provided by PayU during onboarding.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>UMXDPA</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txnId<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Transaction ID provided by the merchant and this must be unique for every transaction.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>ZP6267f0d2996ce</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentMethod<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the payment method used. For Classic Integration:<br>• name: "CreditCard" or "DebitCard"<br>• bankCode: Card type code<br>• paymentCard: Card details object</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{"name": "CreditCard", "bankCode": "CC"}</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>order<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the transaction order including product information, ordered items, user-defined fields, and payment charge specifications. For more information, refer to <a href="#order-object-fields-description">order object fields description</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>additionalInfo<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Additional information including S2S flow configuration and authentication settings. For more information, refer to <a href="#additionalinfo-object-fields-description">additionalInfo object fields description</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>callBackActions<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Actions to perform on the payment server in different scenarios. For more information, refer to <a href="#callbackactions-object-fields-description">callBackActions object fields description</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>billingDetails<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Billing details of the customer including name, address, phone number, email, etc. For more information, refer to <a href="#billingdetails-object-fields-description">billingDetails object fields description</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### paymentMethod object fields description

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

### paymentCard object fields description

<V2_paymentCard />

### order object fields description

<V2_order_object />

### additionalInfo object fields description

<AdditionalI_Info_object />

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txnS2sFlow<br><code>mandatory for S2S</code></p></td>
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

### callBackActions object fields description

<CallbackActions_object />

### billingDetails object fields description

<BillingDetails_object />

## Sample request

```curl
curl --location 'https://apitest.payu.in/v2/payments' \
--header 'date: Thu, 27 Mar 2025 10:12:27 GMT' \
--header 'authorization: hmac username="UMXDPA", algorithm="sha512", headers="date", signature="ec84843a663143bb89391f6fa2d4b9404bab1543a3eee81263b4a507ebf5d289d8fad1fbcdd59da820951e3e0f9b0b0b3d1bad9b41338804e7c42a8a6197c6e9"' \
--header 'Content-Type: application/json' \
--data-raw '{
    "accountId": "UMXDPA",
    "txnId": "ZP6267f0d2996ce",
    "amount": 10,
    "paymentMethod": {
        "name": "CreditCard",
        "bankCode": "CC",
        "paymentCard": {
            "cardNumber": "5004461234560000",
            "validThrough": "04/2025",
            "ownerName": "John Doe",
            "cvv": "987"
        }
    },
    "order": {
        "productInfo": "Classic Integration Payment",
        "orderedItem": [
            {
                "itemId": "1",
                "description": "Product Description",
                "quantity": 1,
                "amount": 10.0
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
            "netAmountDebit": 10,
            "convenienceFee": "CC:12,AMEX:19,SBIB:98,DINR:2,DC:25,NB:55"
        }
    },
    "additionalInfo": {
        "txnS2sFlow": "4",
        "authenticationFlow": "REDIRECT",
        "createOrder": false,
        "preAuthorize": "1"
    },
    "callBackActions": {
        "successAction": "https://yoursite.com/success",
        "failureAction": "https://yoursite.com/failure"
    },
    "billingDetails": {
        "firstName": "John",
        "lastName": "Doe",
        "address1": "123 Main Street",
        "city": "Mumbai",
        "state": "Maharashtra",
        "country": "India",
        "zipCode": "400001",
        "phone": "9876543210",
        "email": "john.doe@example.com"
    }
}'
```

## Sample response

```json
{
    "result": {
        "redirectUrl": "https://secure.payu.in/ResponseHandler.php",
        "paymentId": "21667772394",
        "card": {
            "binData": {
                "pureS2SSupported": false,
                "issuingBank": "ICICI",
                "category": "creditcard",
                "cardType": "MAST",
                "isDomestic": true
            }
        }
    },
    "status": "PENDING"
}
```

## Response parameters

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>redirectUrl</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>URL to which the user is redirected after the payment process is completed.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>https://secure.payu.in/ResponseHandler.php</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentId</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Unique identifier for the payment transaction.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>21667772394</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>card.binData.issuingBank</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Name of the bank that issued the card.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>ICICI</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>card.binData.category</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Category of the card (creditcard, debitcard).</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>creditcard</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>card.binData.cardType</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Type of the card (MAST for Mastercard, VISA, etc.).</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>MAST</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>card.binData.isDomestic</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Boolean indicating if the card is domestic.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>true</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>status</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Status of the payment transaction.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>PENDING</p></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

> 📘 **Reference:**
>
> To check the transaction status, refer to [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api). The Verify Payment API is **mandatory** for Classic Integration to obtain the final transaction status.