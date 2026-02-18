---
title: Generate a UPI QR
excerpt: Know how to generate a UPI QR using the payment API.
deprecated: false
hidden: true
metadata:
  robots: index
---
Use this endpoint to generate a UPI QR to collect offline payments. Pass Omnichannel details in the **omniChannelDetails** object.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /v2/payments
  </Card>
</Cards>

### Environment

<V2_payment_envrionment />

## Sample Request

```curl cURL
curl -X POST 'https://api.payu.in/v2/payments' \
  -H 'Content-Type: application/json' \
  -H "date: {{date}}" \
  -H "authorization: {{authorization}}" \
  -d '{
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
      "vpa": "anything@payu"
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

## Sample Response

```json Success Response
{
   "result":{
      "authAction":"https://api.payu.in/payments/999993715527842445/otps",
      "amount":"10.00",
      "merchantVpa":"anything@payu",
      "postToBank":{
         "token":"D60703B2-AC69-CA71-F987-3A1C404954D8",
         "amount":"10.00",
         "mihpayid":"a55a7c603186536fad0d6f9fe9e1a1c9828b7069599cb2623538f0ce18175cfc",
         "payeeVpa":"gauravdua4.payu@indus",
         "payeeName":"TestMerchant180012",
         "transactionFee":"10.00"
      },
      "merchantName":"TestMerchant180012",
      "paymentId":"999993715527842445",
      "qrString":"upi://pay?pa=gauravdua4.payu@indus&pn=Test Company&tr=999993715527842445&tid=PPPL9999937155278424452312250048356&am=10.00&cu=INR&tn=UPI Transaction"
   },
   "status":"PENDING"
}
```

## Request Headers

<V2_payment_header_params />

## Request Parameters

| **Parameter**                                         | **Description**                                                                                                                                                                                                     |
| :---------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **accountId**<sup style={{color: 'red'}}>*</sup>      | `string` The merchant key provided by PayU during onboarding. For example `MERCHANT123`.                                                                                                                            |
| **txnId**<sup style={{color: 'red'}}>*</sup>          | `string` Transaction ID for transaction tracking and this must be unique for every transaction. For example `REF123456`.                                                                                            |
| **paymentMethod**<sup style={{color:'red'}}>*</sup>   | `object` Details about the payment method used. Parameters are described in the paymentMethod Object Parameters section.                                                                                            |
| **order**<sup style={{color:'red'}}>*</sup>           | `object` Details about the transaction order including product information, ordered items, user-defined fields, and payment charge specifications. Parameters are described in the order Object Parameters section. |
| **additionalInfo**<sup style={{color:'red'}}>*</sup>  | `object` Additional information including UPI-specific parameters like VPA. Parameters are described in the additionalInfo Object Parameters section.                                                               |
| **callBackActions**<sup style={{color:'red'}}>*</sup> | `object` Actions to perform on the payment server in different scenarios. Parameters are described in the callBackActions Object Parameters section.                                                                |
| **billingDetails**<sup style={{color:'red'}}>*</sup>  | `object` Billing details of the customer including name, address, phone number, email, and so on. Parameters are described in the billingDetails Object Parameters section.                                         |

### paymentMethod Object

<Accordion title="Parameters and Description" icon="fa-info-circle">
  | **Parameter**                                   | **Description**                                                |
  | :---------------------------------------------- | :------------------------------------------------------------- |
  | **name**<sup style={{color:'red'}}>\*</sup>     | `string` Represents the payment method used. For UPI, use UPI. |
  | **bankCode**<sup style={{color:'red'}}>\*</sup> | `string` Contains the bank code.For UPI, use UPI.              |
</Accordion>

### order Object

<Accordion title="Parameters and Description" icon="fa-info-circle">
  | **Parameters**                                                    | **Description**                                                                                                                                                                                                                                                      |
  | :---------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | **productInfo**<sup style={{color:'red'}}>\*</sup>                | `string` The product details.                                                                                                                                                                                                                                        |
  | **orderedItem**                                                   | `array` Details about the items ordered.                                                                                                                                                                                                                             |
  | **userDefinedFields**                                             | `object` These are user defined fields to collect custom data. You pass the following fields in this object: <ul><li>`udf1`</li> <li>udf2</li> <li>udf3</li> <li>udf4</li> <li>udf5</li> <li>udf6</li> <li>udf7</li> <li>udf8</li> <li>udf9</li> <li>udf10</li></ul> |
  | **paymentChargeSpecification**<sup style={{color:'red'}}>\*</sup> | `object` The payment charge details such as amount and charges.                                                                                                                                                                                                      |

  #### paymentChargeSpecification Object Parameters

  | **Parameters**                               | **Description**                                             |
  | :------------------------------------------- | :---------------------------------------------------------- |
  | **price**<sup style={{color:'red'}}>\*</sup> | `decimal` The transaction amount. For example `1000`        |
  | **netAmountDebit**                           | `decimal` The net amount to be debited. For example `1000`. |
  | **taxSpecification**                         | `object` Tax details of the product or order.               |
  | **convenienceFee**                           | `string` The fess format. For example `CC:12`               |
  | **offers**                                   | `object` Offers applied or available for the payment.       |
</Accordion>

### additionalInfo Object

<Accordion title="Parameters and Description" icon="fa-info-circle">

| **Parameter**                              | **Description**                                                                                                                                                                     |
| :----------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **createOrder**                            | `boolean` Determines whether to store the order details. Possible values: <ul><li>`true`: The order details are stored</li> <li>`false`: The order details are not stored</li></ul> |
| **txnS2sFlow**                             | `string` Determines the transaction flow type. For example `seamless`.                                                                                                              |
| **vpa**<sup style={{color:'red'}}>\*</sup> | `string` The UPI handle of the customer. For example `test@payu`.                                                                                                                   |

</Accordion>

### callBackActions Object

<Accordion title="Parameters and Description" icon="fa-info-circle">

| **Parameter**                                        | **Description**                                                                                    |
| :--------------------------------------------------- | :------------------------------------------------------------------------------------------------- |
| **successAction**<sup style={{color:'red'}}>\*</sup> | `string` The URL to be called on payment success. For example `https://example.com/success`.       |
| **failureAction**<sup style={{color:'red'}}>\*</sup> | `string` The URL to be called on payment failure. For example `https://example.com/failure`.       |
| **cancelAction**<sup style={{color:'red'}}>\*</sup>  | `string` URL to be called if a user cancels the payment. For example `https://example.com/cancel`. |
| **codAction**                                        | `string` The URL for Cash on Delivery (COD) action. For example `https://example.com/cod`.         |

</Accordion>

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

### omniChannelDetails object fields description

| Field                                | Description                                                                                                                  | Example        |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- | -------------- |
| soundBoxTerminalId <br /> `optional` | string Identifier of the POS or sound box terminal device used for the transaction. Used for in-person/omnichannel payments. | "1"            |
| outletName <br /> `optional`         | string Name of the merchant outlet or store where the transaction takes place.                                               | "puma pimpri"  |
| vendorId <br /> `optional`           | string Vendor or terminal provider identifier associated with the device or outlet.                                          | "vendorId"     |
| tips <br /> `optional`               | string Tips amount or related information for the transaction, if applicable.                                                | "tips"         |
| childMerchId <br /> `optional`       | string Child merchant ID when using split settlements or multiple outlets under a parent merchant.                           | "childMerchId" |
| expiryTime <br /> `optional`         | string or numeric Validity of the QR or transaction in **seconds**. If not sent, merchant-level or global expiry may apply.  | "100" or 3600  |

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
    "vpa": "anything@payu"
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
    "merchantVpa": "anything@payu",
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

The **result** parameter in the response contains the following fields:

<br />

| Field        | Description                                                                                                                                                                               | Example                                                                                                        |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| authAction   | string URL to post OTP or other auth data (e.g. for UPI collect/OTP flows). The client should use this endpoint when the flow requires submitting OTP or auth details.                    | "[https://api.payu.in/payments/999993715527842445/otps](https://api.payu.in/payments/999993715527842445/otps)" |
| amount       | string Transaction amount in the response, in decimal form.                                                                                                                               | "10.00"                                                                                                        |
| merchantVpa  | string Merchant’s UPI VPA (Virtual Payment Address) where the payment is collected.                                                                                                       | "anything@payu"                                                                                                |
| merchantName | string Display name of the merchant as registered with PayU.                                                                                                                              | "TestMerchant180012"                                                                                           |
| paymentId    | string PayU’s unique payment/transaction reference. Use this for status checks, refunds, and support.                                                                                     | "999993715527842445"                                                                                           |
| qrString     | string UPI payment URI to be encoded as a QR code. The client should generate a QR from this string (after removing any line breaks) and show it for the customer to scan with a UPI app. | "upi://pay?pa=...&am=10.00&cu=INR&tn=..."                                                                      |
| postToBank   | object Data required to post the payment request to the bank/UPI app (e.g. for collect or redirect flows). Contains token, payee details, and fee.                                        |                                                                                                                |

 

##

> 📘 **Reference:**
>
> To check the transaction status, refer to <Anchor label="Verify Payment API" target="_blank" href="https://docs.payu.in/v2/reference/v2_verify_payment_api">Verify Payment API</Anchor>.

<br />
