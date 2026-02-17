---
title: v2 Dynamic QR Generation API
deprecated: false
hidden: false
metadata:
  robots: index
---
The dynamic QR generation API returns a UPI QR which can be used for offline payment collections.

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>MERCHANT123</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txnId<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Transaction ID for transaction tracking and this must be unique for every transaction.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>REF123456</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentMethod<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the payment method used. For UPI payments:<br>• name: Must be "UPI"<br>• bankCode: Must be "UPI"</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{"name": "UPI", "bankCode": "UPI"}</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>order<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the transaction order including product information, ordered items, user-defined fields, and payment charge specifications. For more information, refer to <a href="#order-object-fields-description">order object fields description</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>additionalInfo<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Additional information including UPI-specific parameters like VPA. For more information, refer to <a href="#additionalinfo-object-fields-description">additionalInfo object fields description</a>.</p></td>
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

### paymentMethod object

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>name</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Represents the payment method used. For UPI, use UPI</td>
  <td style="border: 1px solid #ddd; padding: 8px;">UPI</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>bankCode</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains the bank code.For UPI, use UPI</td>
  <td style="border: 1px solid #ddd; padding: 8px;">UPI</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### order object fields description

<V2_order_object />

### additionalInfo object fields description

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>createOrder</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">A flag to store the order details (true/false).</td>
  <td style="border: 1px solid #ddd; padding: 8px;">true</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>txnS2sFlow</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">For defining seamless/non-seamless flows in handling payments.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">seamless</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>vpa<br><code>mandatory for UPI</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> UPI handle of the customer.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>test@payu</p></td>
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
curl --location 'https://api.payu.in/v2/payments' \
  --header 'Content-Type: application/json' \
  --header 'date: {{date}}' \
  --header 'authorization: {{authorization}}' \
  --data-raw '{
  "accountId": "smsplus",
  "txnId": "b5f29799999987988995",
  "amount": 10,
  "currency": "INR",
  "paymentSource": "WEB",
  "paymentMethod": {
    "name": "DBQR",
    "bankCode": "UPIDBQR"
  },
  "order": {
    "productInfo": "UPI Payment for Order",
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
      "price": "10.00"
    }
  },
  "additionalInfo": {
    "txnFlow": "seamless",
    "createOrder": true,
    "txnS2sFlow": "4",
    "vpa": "7807305029@ptsbi"
  },
  "callBackActions": {
    "successAction": "https://yoursite.com/success",
    "failureAction": "https://yoursite.com/failure",
    "cancelAction": "https://yoursite.com/cancel"
  },
  "omniChannelDetails": {
    "soundBoxTerminalId": "1",
    "outletName": "puma pimpri",
    "vendorId": "vendorId",
    "tips": "tips",
    "childMerchId": "childMerchId",
    "expiryTime": "100"
  },
  "billingDetails": {
    "firstName": "John",
    "lastName": "Doe",
    "phone": "9876543210",
    "email": "john.doe@example.com",
    "city": "Mumbai",
    "state": "Maharashtra",
    "country": "India",
    "zipCode": "400001"
  }
}'
```

## Sample response

```json
{
  "result": {
    "authAction": "https://api.payu.in/payments/999993715527842445/otps",
    "amount": "10.00",
    "merchantVpa": "gauravdua4.payu@indus",
    "postToBank": {
      "token": "D60703B2-AC69-CA71-F987-3A1C404954D8",
      "amount": "10.00",
      "mihpayid": "a55a7c603186536fad0d6f9fe9e1a1c9828b7069599cb2623538f0ce18175cfc",
      "payeeVpa": "gauravdua4.payu@indus",
      "payeeName": "TestMerchant180012",
      "transactionFee": "10.00"
    },
    "merchantName": "TestMerchant180012",
    "paymentId": "999993715527842445",
    "qrString": "upi://pay?pa=gauravdua4.payu@indus&pn=Test Company&tr=999993715527842445&tid=PPPL9999937155278424452312250048356&am=10.00&cu=INR&tn=UPI Transaction"
  },
  "status": "PENDING"
}
```

## Response parameters



> 📘 **Reference:**
>
> To check the transaction status, refer to <Anchor label="Verify Payment API" target="_blank" href="https://docs.payu.in/v2/reference/v2_verify_payment_api">Verify Payment API</Anchor>.

<br />
