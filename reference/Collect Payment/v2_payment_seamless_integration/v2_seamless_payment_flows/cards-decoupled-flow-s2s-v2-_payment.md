---
title: Cards Decoupled Flow - v2 Payment API
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
You can collect card payments without redirection to bank page for entering OTP using S2S integration with Seamless Decoupled Flow. This flow enables pure server-to-server transaction processing for a streamlined payment experience.

The Seamless Decoupled Flow uses **txnS2sFlow** set to **2** for Pure S2S transactions, eliminating user interface redirections during the authentication process.

### Environment

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the payment method used. For Seamless Decoupled Flow:<br>• name: "CreditCard" or "DebitCard"<br>• bankCode: Card type code<br>• paymentCard: Card details object</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{"name": "CreditCard", "bankCode": "CC"}</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>order<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the transaction order including product information, ordered items, user-defined fields, and payment charge specifications. For more information, refer to <a href="#order-object-fields-description">order object fields description</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>additionalInfo<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Additional information including S2S flow configuration and seamless decoupled settings. For more information, refer to <a href="#additionalinfo-object-fields-description">additionalInfo object fields description</a>.</p></td>
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

## Object field descriptions

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field must contain the payment mode code. For Seamless Decoupled Flow, use "CreditCard" or "DebitCard". For more information, refer to <a href="https://docs.payu.in/v1/docs/payment-mode-codes">Payment Mode Codes</a>.</p></td>
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

**Seamless Decoupled Flow-specific parameters:**

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Indicates the transaction S2S flow type and must be set to "2" for Pure Seamless Decoupled Flow.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>createOrder<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> Whether to create an order during the payment process. Set to false for decoupled order management.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>false</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>decodedS2sResponse<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Set to "1" to return raw response instead of template format.</p></td>
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
        "productInfo": "Seamless Decoupled Flow Payment",
        "orderedItem": [
            {
                "description": "Product Description",
                "amount": 10.0
            }
        ]
    },
    "additionalInfo": {
        "txnS2sFlow": "2",
        "createOrder": false,
        "decodedS2sResponse": "1"
    },
    "callBackActions": {
        "successAction": "https://yoursite.com/success",
        "failureAction": "https://yoursite.com/failure"
    },
    "billingDetails": {
        "firstName": "John",
        "lastName": "Doe",
        "phone": "9876543210",
        "email": "john.doe@example.com"
    }
}'
```

## Sample response

### Card/EMI Payment Response

```json
{
    "result": {
        "authAction": "https://api.payu.in/payments/21667772394/otps",
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

### UPI Payment Response

```json
{
    "result": {
        "upi": {
            "amount": "10.00",
            "merchantVpa": "merchant.payu@hdfcbank",
            "intentURIData": "pa=merchant@vpa&tr=21667772414&am=10.00"
        },
        "orderId": "ZP6267f0d2996ce"
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>card.binData.pureS2SSupported</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Boolean indicating if the card supports pure server-to-server transactions.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>false</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>upi.amount</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>UPI payment amount (for UPI transactions).</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>10.00</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>upi.merchantVpa</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Merchant's UPI VPA (for UPI transactions).</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>merchant.payu@hdfcbank</p></td>
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
> To check the transaction status, refer to [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api). The Verify Payment API is **mandatory** for Seamless Decoupled Flow to obtain the final transaction status since the initial response is always PENDING.