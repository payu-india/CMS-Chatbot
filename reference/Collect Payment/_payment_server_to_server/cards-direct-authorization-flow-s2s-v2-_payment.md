---
title: Cards Direct Authorization Flow S2S - v2 Payment API
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
PayU enables merchants to process direct authorization for pre-authenticated transactions (external MPI/3DSS). This section describes how to integrate with PayU's direct authorization flow. Initiate an authorization request with the payment details provided post a successful authentication through the MPI/3DSS as explained in this API Reference.

The Cards Redirect Flow provides structured redirection handling for card authentication and transaction processing with comprehensive 3DS support.

> 📘 **Note:**
>
> This API is backward compatible and you can continue to use the existing integration parameters to process the 3DS 1.0.2 transactions.

## Environment

<V2_payment_envrionment />

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the payment method used. For Cards Redirect Flow:<br>• name: "CreditCard" or "DebitCard"<br>• bankCode: Card type code<br>• paymentCard: Card details object</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{"name": "CreditCard", "bankCode": "CC"}</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>order<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the transaction order including product information, ordered items, user-defined fields, and payment charge specifications. For more information, refer to <a href="#order-object-fields-description">order object fields description</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>additionalInfo<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Additional information including S2S flow configuration and redirect flow settings. For more information, refer to <a href="#additionalinfo-object-fields-description">additionalInfo object fields description</a>.</p></td>
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
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>authorization<br><code>mandatory for S2S Direct Auth</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> 3DS authorization information for direct authentication. For more information, refer to <a href="#authorization-object-fields-description">authorization object fields description</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>threeDS2RequestData<br><code>mandatory for S2S</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> 3DS2 request data for enhanced authentication. For more information, refer to <a href="#threeds2requestdata-object-fields-description">threeDS2RequestData object fields description</a>.</p></td>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field must contain the payment mode code. For Cards Redirect Flow, use "CreditCard" or "DebitCard". For more information, refer to <a href="https://docs.payu.in/v1/docs/payment-mode-codes">Payment Mode Codes</a>.</p></td>
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

**Cards Redirect Flow-specific parameters:**

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txnS2sFlow<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Indicates the transaction S2S flow type. Set to "1" for partial S2S or "2" for pure S2S-like flow.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>createOrder<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> Whether to create an order during the payment process.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>false</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>placeOrder<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> Use to indicate if saved order details should be utilized.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>false</p></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### callBackActions object fields description

<CallbackActions_object />

### billingDetails object fields description

<BillingDetails_object />

### authorization object fields description

<V2_authorization_cards />

### threeDS2RequestData object fields description

<ThreeDSRequestData_object />

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
            "cvv": "987",
            "last4Digits": "0000",
            "cardTokenType": "NETWORK",
            "cardToken": "29850879bf39848ca078727b8e1a95165a41cea1"
        }
    },
    "order": {
        "productInfo": "Cards Redirect Flow Payment",
        "orderedItem": [
            {
                "itemId": "1",
                "description": "Product Description",
                "quantity": 1,
                "amount": 10.0
            }
        ],
        "paymentChargeSpecification": {
            "price": 10,
            "netAmountDebit": 10
        }
    },
    "additionalInfo": {
        "createOrder": false,
        "placeOrder": false,
        "txnS2sFlow": "1"
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
    },
    "authorization": {
        "eci": "05",
        "cavv": "AAABAWFlmQAAAABjRWWZEEFgFz",
        "flowType": "Frictionless",
        "threeDSTransID": "67b4c71f-19bf-4d97-bd09-4e3687dc9e42",
        "threeDSServerTransID": "eea30d14-71cf-41af-b961-f95b7d67dc93",
        "threeDSTransStatus": "Y",
        "threeDSTransStatusReason": "01",
        "acquirer_bin": "401200",
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

## Sample response

```json
{
    "result": {
        "redirectUrl": "https://secure.payu.in/ResponseHandler.php",
        "authAction": "https://api.payu.in/payments/21667772394/otps",
        "paymentId": "21667772394",
        "redirectTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vbmV0YmFua2luZy5oZGZjYmFuay5jb20vbmV0YmFua2luZy9tZXJjaGFudD9DbGllbnRDb2RlPTE1NDkxMyZNZXJjaGFudENvZGU9UEFZVUZBQ0VCT09LJlR4bkN1cnJlbmN5PUlOUiZUeG5BbW91bnQ9MjUwMDAuMDAmVHhuU2NBbW91bnQ9MCZNZXJjaGFudFJlZk5vPWs0cWh3NGVsYXY2MmxwNjJjbSZTdWNjZXNzU3RhdGljRmxhZz1OJkZhaWx1cmVTdGF0aWNGbGFnPU4mRGF0ZT0yNi8xMS8yMDI0IDAwOjAwOjAwJlJlZjE9JlJlZjI9NDAzYmIzODkxY2Y5NGEzNmI0ZGQxOTlkOWNjZWVjNmUmUmVmMz0mUmVmND0mUmVmNT0mRHluYW1pY1VybD1odHRwczovL3NlY3VyZS5wYXl1LmluL2I0NDdmZmViZDg4NDNjZTEzYzlmODVhZjhlOTA0ZmQyL0NvbW1vblBnUmVzcG9uc2VIYW5kbGVyLnBocCZDaGVja1N1bT0zMTAxMzgyNDM2",
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>authAction</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>URL for authentication actions like OTP submission during the payment process.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>https://api.payu.in/payments/21667772394/otps</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentId</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Unique identifier for the payment transaction.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>21667772394</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>redirectTemplate</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Encoded HTML template used for auto-redirecting or displaying information post-payment.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Base64 encoded HTML</p></td>
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
> To check the transaction status, refer to [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api). The Verify Payment API is **mandatory** for Cards Redirect Flow to obtain the final transaction status.