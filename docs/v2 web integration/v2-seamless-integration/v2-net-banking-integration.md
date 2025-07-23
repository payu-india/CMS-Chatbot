---
title: v2 Net Banking Integration
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
This document provides a comprehensive guide for integrating with **PayU Net Banking Seamless Integration v2** using the `v2/payments` API. The seamless integration allows you to process Net Banking payments directly through server-to-server communication, providing a streamlined payment experience while maintaining control over the user interface.

PayU recommends testing your integration in the PayU test environment before going live.

## Integration Overview

The v2 Net Banking seamless integration consists of two main steps:

1. **Create the payment request** to PayU's v2/payments API with Net Banking payment method
2. **Verify the payment** status using the verification API

## Step 1: Create the Payment Request

#### Environment

<V2_payment_envrionment />

#### Request Headers

<Accordion title="Request Headers" icon="fa-code">
  <V2_payment_header_params />
</Accordion>

### Request Parameters

The v2/payments API request for Net Banking seamless integration contains the following main parameters:

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
<td>Merchant key provided by PayU. Character limit: 50</td>
<td><code>"smsplus"</code></td>
</tr>
<tr>
<td>txnId<br/><code>mandatory</code></td>
<td>Unique transaction ID for the transaction. Character limit: 50</td>
<td><code>"REF_123456789"</code></td>
</tr>
<tr>  
<td>paymentMethod<br/><code>mandatory</code></td>
<td>Net Banking payment method details. <a href="#paymentmethod-object">See paymentMethod object</a></td>
<td><code>{"name": "NetBanking", "bankCode": "EFTAXIS"}</code></td>
</tr>
<tr>
<td>order<br/><code>mandatory</code></td>
<td>Order details containing product information and pricing. <a href="#order-object">See order object</a></td>
<td><code>{"productInfo": "Net Banking Payment", "paymentChargeSpecification": {"price": 10000.00}}</code></td>
</tr>
<tr>
<td>billingDetails<br/><code>mandatory</code></td>
<td>Customer billing information. <a href="#billingdetails-object">See billingDetails object</a></td>
<td><code>{"firstName": "John", "email": "john@example.com", "phone": "9876543210"}</code></td>
</tr>
<tr>
<td>callBackActions<br/><code>optional</code></td>
<td>Callback URLs for different payment outcomes. <a href="#callbackactions-object">See callBackActions object</a></td>
<td><code>{"successAction": "https://merchant.com/success", "failureAction": "https://merchant.com/failure"}</code></td>
</tr>
<tr>
<td>additionalInfo<br/><code>mandatory</code></td>
<td>Additional transaction parameters including flow type. <a href="#additionalinfo-object">See additionalInfo object</a></td>
<td><code>{"txnFlow": "seamless", "enforcePaymethod": "NB"}</code></td>
</tr>
<tr>
<td>beneficiaryDetail<br/><code>mandatory</code></td>
<td>Beneficiary account details for Net Banking transfer. <a href="#beneficiarydetail-object">See beneficiaryDetail object</a></td>
<td><code>{"beneficiaryName": "Merchant Account", "beneficiaryAccountNumber": "1234567890", "beneficiaryAccountType": "SAVINGS"}</code></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

#### Payment Method Object

<Accordion title="Payment Method Object" icon="fa-code">
  For Net Banking seamless integration, the payment method object should contain:

  | Parameter  | Type   | Description                                                               | Required |
  | ---------- | ------ | ------------------------------------------------------------------------- | -------- |
  | `name`     | String | Must be "NetBanking" for Net Banking payments                             | Yes      |
  | `bankCode` | String | Specific bank code for the selected bank (e.g., "TESTNB", "SBIN", "HDFC") | Yes      |

  **Example:**

  ```json
  {
    "name": "NetBanking",
    "bankCode": "TESTNB"
  }
  ```
</Accordion>

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
    <td style="border: 1px solid #ddd; padding: 8px;"><strong>partnerHoldTime</strong><br/><code>optional</code></td>
    <td style="border: 1px solid #ddd; padding: 8px;">Time held by the partner for the transaction.</td>
    <td style="border: 1px solid #ddd; padding: 8px;">60</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><strong>createOrder</strong><br/><code>optional</code></td>
    <td style="border: 1px solid #ddd; padding: 8px;">A flag to store the order details (true/false).</td>
    <td style="border: 1px solid #ddd; padding: 8px;">true</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><strong>txnS2sFlow</strong><br/><code>optional</code></td>
    <td style="border: 1px solid #ddd; padding: 8px;">For defining seamless/non-seamless flows in handling payments.</td>
    <td style="border: 1px solid #ddd; padding: 8px;">seamless</td>
  </tr>
  </tbody>
  </table>
  `}</HTMLBlock>
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
  "referenceId": "b5f2d8785768087678fn4",
  "currency": "INR",
  "paymentSource": "WEB",
  "paymentMethod": {
    "name": "NetBanking",
    "bankCode": "TESTNB"
  },
  "order": {
    "productInfo": "Net Banking Test Product",
    "orderedItem": [
      {
        "itemId": "ITEM001",
        "description": "Test Product for Net Banking",
        "quantity": 1
      }
    ],
    "paymentChargeSpecification": {
      "price": 100.00
    }
  },
  "additionalInfo": {
    "txnS2sFlow": "2",
    "createOrder": false,
    "enforcePaymethod": "1"
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
  "result": {
    "paymentId": "1999110000001769",
    "redirectUrl": "https://secure.payu.in/ResponseHandler.php",
    "authAction": "https://apitest.payu.in/v2/payments/1999110000001769/auth"
  },
  "status": "PENDING"
}
```

## Step 2: Verify the Payment

After the payment is processed, you must verify the payment status using the verification API to get the final transaction status.

### Environment

| Environment | URL                                   |
| ----------- | ------------------------------------- |
| Test        | `https://test.payu.in/v3/transaction` |
| Production  | `https://api.payu.in/v3/transaction`  |

### Request Headers

The verification API requires the following headers:

| Header          | Description                       | Required |
| --------------- | --------------------------------- | -------- |
| `Content-Type`  | Must be `application/json`        | Yes      |
| `date`          | Current date in GMT format        | Yes      |
| `authorization` | HMAC signature for authentication | Yes      |
| `Info-Command`  | Must be `verify_payment`          | Yes      |

### Request Parameters

| Parameter | Type  | Description                                  | Required |
| --------- | ----- | -------------------------------------------- | -------- |
| `txnId`   | Array | Array of transaction reference IDs to verify | Yes      |

#### Response Parameters

<Accordion title="Response Parameters" icon="fa-code">
  <V2_payment_response_params />
</Accordion>

### Sample Verification Request

**Request Headers:**

```
Content-Type: application/json
date: Thu, 27 Mar 2025 06:35:21 GMT
authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="<calculated_hmac_signature>"
Info-Command: verify_payment
```

**Request Body:**

```json
{
  "txnId": ["b5f2d8785768087678fn4"]
}
```

### Sample Verification Success Response

```json
{
  "message": "Success",
  "status": 1,
  "result": [
    {
      "mihpayId": 1999110000001769,
      "bankReferenceNumber": "NB12345678",
      "amount": 100.00,
      "mode": "NB",
      "requestId": "",
      "originalAmount": 100.00,
      "additionalCharges": 0.00,
      "discount": 0.00,
      "netDebitAmount": 100.00,
      "productInfo": "Net Banking Test Product",
      "firstName": "John",
      "bankcode": "TESTNB",
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
      "pgType": "NB-PG",
      "status": "success",
      "unmappedStatus": "captured",
      "merchantUTR": null,
      "originalCurrency": "INR",
      "message": "Found TxnId",
      "txnId": "b5f2d8785768087678fn4"
    }
  ]
}
```

### Sample Verification Failure Response

```json
{
  "status": 0,
  "msg": "Invalid Transaction ID"
}
```