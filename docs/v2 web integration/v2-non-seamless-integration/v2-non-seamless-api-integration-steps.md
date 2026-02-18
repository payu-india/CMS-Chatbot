---
title: API Integration - PayU Hosted Checkout
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
This document provides a comprehensive guide for integrating with **PayU Hosted Checkout** or **v2 Non-Seamless** using the `v2/payments` API. The hosted checkout integration allows you to redirect customers to PayU's secure payment page, minimising PCI compliance requirements while providing a seamless payment experience.

<V2_Prerequisite_Payment_Integration />

## Integration Overview

The v2 non-seamless integration consists of two main steps:

1. **Make the transaction request** to PayU's v2/payments API
2. **Verify the payment** status using the verification API

## Step 1: Make the Transaction Request to PayU

#### Environment

<V2_payment_envrionment />

#### Request Headers

<Accordion title="Request Headers" icon="fa-code">
  <V2_payment_header_params />
</Accordion>

### Request Parameters

The v2/payments API request contains the following main parameters:

<HTMLBlock>{`
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>accountId<br/><code>mandatory</code></td>
<td><code>String</code> Merchant key provided by PayU. Character limit: 50</td>
<td><code>"smsplus"</code></td>
</tr>
<tr>
<td>txnId<br/><code>mandatory</code></td>
<td><code>String</code> Unique transaction ID for the transaction. Character limit: 50</td>
<td><code>"REF_123456789"</code></td>
</tr>
<tr>
<td>order<br/><code>mandatory</code></td>
<td><code>Object</code> Order details containing product information and pricing. For more information, refer to<a href="#order-object"> order object</a></td>
<td><code>{"productInfo": "Product Name", "paymentChargeSpecification": {"price": 1000.00}}</code></td>
</tr>
<tr>
<td>billingDetails<br/><code>mandatory</code></td>
<td><code>Object</code> Customer billing information. For more information, refer to<a href="#billingdetails-object">billingDetails object</a></td>
<td><code>{"firstName": "John", "email": "john@example.com", "phone": "9876543210"}</code></td>
</tr>
<tr>
<td>callBackActions<br/><code>mandatory</code></td>
<td><code>Object</code> Callback URLs for different payment outcomes. For more information, refer to<a href="#callbackactions-object"> callBackActions object</a></td>
<td><code>{"successAction": "https://merchant.com/success", "failureAction": "https://merchant.com/failure"}</code></td>
</tr>
<tr>
<td>additionalInfo<br/><code>mandatory</code></td>
<td><code>Object</code> Additional transaction parameters including flow type. For more information, refer to<a href="#additionalinfo-object">additionalInfo object</a></td>
<td><code>{"txnFlow": "non-seamless", "enforcePaymethod": "NB"}</code></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

#### Order Object

<Accordion title="Order Object" icon="fa-code">
  <V2_order_object />
</Accordion>

#### Payment Charge Specification Object

<Accordion title="Payment Charge Specification Object" icon="fa-code">
  <V2_paymentChargeSpecification_object />
</Accordion>

#### Additional Info Object

<Accordion title="Additional Info Object" icon="fa-code">
  <AdditionalI_Info_object />
</Accordion>

#### Callback Actions Object

<Accordion title="Callback Actions Object" icon="fa-code">
  <CallbackActions_object />
</Accordion>

#### Billing Details Object

<Accordion title="Billing Details Object" icon="fa-code">
  <BillingDetails_object />
</Accordion>

### Sample Request

**Request Headers:**

```
Content-Type: application/json
date: Wed, 28 Jun 2023 11:25:19 GMT
authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="<calculated_hmac_signature>"
```

**Request Body:**

```json
{
  "accountId": "smsplus",
  "referenceId": "b5f2d8785768087678fm9",
  "order": {
    "productInfo": "Test Product",
    "orderedItem": [
      {
        "itemId": "ITEM001",
        "description": "Test Product Description",
        "quantity": 1
      }
    ],
    "paymentChargeSpecification": {
      "price": 10.00
    }
  },
  "additionalInfo": {
    "txnFlow": "nonseamless"
  },
  "callBackActions": {
    "successAction": "https://example.com/success",
    "failureAction": "https://example.com/failure",
    "cancelAction": "https://example.com/cancel"
  },
  "billingDetails": {
    "firstName": "John",
    "lastName": "Doe",
    "phone": "9876543210",
    "email": "john.doe@example.com",
    "address": {
      "address1": "123 Main Street",
      "city": "Mumbai",
      "state": "Maharashtra",
      "country": "India",
      "zipCode": "400001"
    }
  }
}
```

### Sample Response

```json
{
  "message": "Success",
  "status": 1,
 {
  "result": {
     "checkoutUrl": "https://pp78secure.payu.in/_payment_options?mihpayid=<mihpayuid>&userToken="
     },
     "status": "PENDING"
 }
}
```

## Step 2: Verify the Payment

After the customer completes the payment on the PayU checkout page, you must verify the payment status using the verification API.

### Environment

| Environment | URL                                   |
| ----------- | ------------------------------------- |
| Test        | `https://test.payu.in/v3/transaction` |
| Production  | `https://info.payu.in/v3/transaction` |

### Request parameters

#### Request Headers

The verification API requires the following headers:

| Header          | Description                       | Required |
| --------------- | --------------------------------- | -------- |
| `Content-Type`  | Must be `application/json`        | Yes      |
| `date`          | Current date in GMT format        | Yes      |
| `authorization` | HMAC signature for authentication | Yes      |
| `Info-Command`  | Must be `verify_payment`          | Yes      |

#### Request Body

| Parameter | Type  | Description                                  | Required |
| --------- | ----- | -------------------------------------------- | -------- |
| `txnId`   | Array | Array of transaction reference IDs to verify | Yes      |

### Sample request to verify

```curl
curl --location 'https://test.payu.in/v3/transaction' \
--header 'Content-Type: application/json' \
--header 'date: Thu, 27 Mar 2025 06:35:21 GMT' \
--header 'authorization: hmac username="PRiQvJ", algorithm="sha512", headers="date", signature="42a54cc7450fe1e7a3cf35ebfaed1b828e37062964266fd33186c7b2526e85e3ea2d46946a728ca50e46423ea9a6b2edb8c1315b58fa69297e1e91d3d34804a1"' \
--header 'Info-Command: verify_payment' \
--data '{
    "txnId":["512345678901234"]
}'
```

### Response Parameters

<Accordion title="Response Parameters" icon="fa-code">
  <V2_payment_response_params />
</Accordion>

### Sample success response

```json
{
  "message": "Success",
  "status": 1,
  "result": [
    {
      "mihpayId": 21612493009,
      "bankReferenceNumber": "2411194544",
      "amount": 10.00,
      "mode": "CC",
      "requestId": "",
      "originalAmount": 10.00,
      "additionalCharges": 0.00,
      "discount": 0.00,
      "netDebitAmount": 10.00,
      "productInfo": "Test Product",
      "firstName": "John",
      "bankcode": "VISA",
      "nameOnCard": "JOHN DOE",
      "cardNo": "XXXXXXXXXXXX1234",
      "cardType": "VISA",
      "udf1": null,
      "udf2": null,
      "udf3": null,
      "udf4": null,
      "udf5": null,
      "field2": "140455",
      "field9": "Transaction is Successful",
      "errorCode": "E000",
      "errorMessage": "No Error",
      "addedOn": "2024-11-19 21:17:55",
      "settledAt": "0000-00-00 00:00:00",
      "paymentSource": "WEB",
      "pgType": "CC-PG",
      "status": "success",
      "unmappedStatus": "captured",
      "merchantUTR": null,
      "rupayAuthRefNo": null,
      "authRefNo": "123456789",
      "threeDSVersion": "2.2.0",
      "message": "Found TxnId",
      "txnId": "b5f2d8785768087678fm9"
    }
  ]
}
```

### Sample failure response

```json
{
  "status": 0,
  "msg": "Invalid Transaction ID"
}
```
