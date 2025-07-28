---
title: v2 Cards Integration
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
This document provides a comprehensive guide for integrating with **PayU Cards Seamless Integration v2** using the `v2/payments` API. The seamless integration allows you to process card payments directly through server-to-server communication, providing a streamlined payment experience while maintaining control over the user interface.

We recommend testing your integration in the PayU test environment before going live.

## Supported Card Types

PayU v2 Cards integration supports the following card types:

* **American Express (AMEX)**
* **Visa**
* **Mastercard**
* **Diners Club**
* **RuPay**

Both domestic and international transactions are supported (international transactions require special enablement).

The v2 Cards seamless integration consists of three main steps:

1. **Validate card type** using the BIN API (check\_isDomestic)
2. **Create the payment request** to PayU's v2/payments API with card payment method
3. **Verify the payment** status using the verification API

## Step 1: Validate Card Type (Optional)

Before processing the payment, you can validate the card type using PayU's BIN API to check if the card is domestic or international.

## Step 2: Create the payment request

#### Environment

<Accordion title="Environment" icon="fa-code">
  <V2_payment_envrionment />
</Accordion>

#### Request Headers

<Accordion title="Request Headers" icon="fa-code">
  <V2_payment_header_params />
</Accordion>

### Request body

The v2/payments API request for Cards seamless integration contains the following main parameters:

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
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>accountId</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Represents the merchant key provided by PayU during onboarding.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">MERCHANT123</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>txnId</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Transaction ID for transaction tracking. Must be unique for every transaction.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">TXN123456</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>amount</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Amount of the transaction. This will not be considered as the transaction amount, only the order.paymentChargeSpecification.price field will be considered.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">1000</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>paymentMethod</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains details of the payment method. For more information, refer to <a href="https://docs.payu.in/v2/docs/v2-cards-merchant-hosted-integration/#payment-method-object">Payment Method Object</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>order</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains transaction order details such as product info, ordered items, user-defined fields, and payment charge details. For more information, refer to <a href="https://docs.payu.in/v2/docs/v2-cards-merchant-hosted-integration/#order-object">Order Object</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Additional metadata for the transaction. For more information, refer to <a href="https://docs.payu.in/v2/docs/v2-cards-merchant-hosted-integration/#additional-info-object">Additional Info Object</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>callBackActions</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">URL actions for payments (e.g., success, failure, cancel). For more information, refer to <a href="https://docs.payu.in/v2/docs/v2-cards-merchant-hosted-integration/#callback-actions-object">Callback Actions Object</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>billingDetails</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Customer billing details including name, phone, and address. For more information, refer to <a href="https://docs.payu.in/v2/docs/v2-cards-merchant-hosted-integration/#billing-details-object">Billing Details Object</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>authorization</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Authorization details for the payment process, including 3DS metadata. For more information, refer to <a href="https://docs.payu.in/v2/docs/v2-cards-merchant-hosted-integration/#authorization-object">Authorization Object</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

<br />

#### Payment method object

<Accordion title="Payment Method Object" icon="fa-code">
  For Cards seamless integration, the payment method object should contain:

  | Parameter     | Type   | Description                                                                     | Required |
  | ------------- | ------ | ------------------------------------------------------------------------------- | -------- |
  | `name`        | String | Must be "CreditCard" for credit cards or "DebitCard" for debit cards            | Yes      |
  | `bankCode`    | String | Bank code for the card type (e.g., "CC" for credit cards, "DC" for debit cards) | Yes      |
  | `paymentCard` | Object | Card details including card number, CVV, expiry, etc.                           | Yes      |

  **Example:**

  ```json
  {
    "name": "CreditCard",
    "bankCode": "CC",
    "paymentCard": {
      "cardNumber": "5004461234560000",
      "validThrough": "04/2025",
      "ownerName": "John Doe",
      "cvv": "123"
    }
  }
  ```
</Accordion>

#### Payment Card Object

<Accordion title="Payment Card Object" icon="fa-code">
  For new card payments:

  | Parameter      | Type   | Description                        | Required |
  | -------------- | ------ | ---------------------------------- | -------- |
  | `cardNumber`   | String | Full card number                   | Yes      |
  | `validThrough` | String | Card expiry date in MM/YYYY format | Yes      |
  | `ownerName`    | String | Cardholder name as on card         | No       |
  | `cvv`          | String | Card Verification Value            | Yes      |

  For saved card payments:

  | Parameter       | Type   | Description                        | Required |
  | --------------- | ------ | ---------------------------------- | -------- |
  | `cardToken`     | String | Saved card token                   | Yes      |
  | `cardTokenType` | String | Token type (PAYU, NETWORK, ISSUER) | Yes      |
  | `tavv`          | String | Cryptogram for saved cards         | Yes      |
  | `last4Digits`   | String | Last 4 digits of saved card        | Yes      |
  | `cvv`           | String | Card Verification Value            | Yes      |

  **Example - New Card:**

  ```json
  {
    "cardNumber": "5004461234560000",
    "validThrough": "04/2025",
    "ownerName": "John Doe",
    "cvv": "123"
  }
  ```

  **Example - Saved Card:**

  ```json
  {
    "cardToken": "29850879bf39848ca078727b8e1a95165a41cea1",
    "cardTokenType": "NETWORK",
    "tavv": "/wAAAAAAPtP+g6IAmbSeg1gAAAA=",
    "last4Digits": "0000",
    "cvv": "123"
  }
  ```
</Accordion>

#### Order object

<Accordion title="Order Object" icon="fa-code">
  <V2_order_object />
</Accordion>

#### Payment charge specification object

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

#### Authorization Object

<Accordion title="Authorization Object" icon="fa-code">
  <V2_authorization_cards />
</Accordion>

#### ThreeDS2 Request Data Object

<Accordion title="ThreeDS2 Request Data Object" icon="fa-code">
  <ThreeDSRequestData_object />
</Accordion>

### Sample request

```json
curl -X POST \
  https://apitest.payu.in/v2/payments \
  -H 'date: Mon, 05 Oct 2024 11:00:00 GMT' \
  -H 'authorization: HMAC smsplus:4d1ea4e74243ea5b2b5b8b1d8a7b1a2e3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9' \
  -H 'content-type: application/json' \
  -d {
  "accountId": "smsplus",
  "referenceId": "b5f2d8785768087678fn4",
  "currency": "INR",
  "paymentSource": "WEB",
  "paymentMethod": {
    "name": "CreditCard",
    "bankCode": "CC",
    "paymentCard": {
      "cardNumber": "5004461234560000",
      "validThrough": "04/2025",
      "ownerName": "John Doe",
      "cvv": "123"
    }
  },
  "order": {
    "productInfo": "Credit Card Test Product",
    "orderedItem": [
      {
        "itemId": "ITEM001",
        "description": "Test Product for Credit Card",
        "quantity": 1
      }
    ],
    "paymentChargeSpecification": {
      "price": 100.00
    },
    "userDefinedFields": {
      "udf1": "",
      "udf2": "",
      "udf3": "",
      "udf4": "",
      "udf5": ""
    }
  },
  "additionalInfo": {
    "txnS2sFlow": "2",
    "createOrder": false,
    "storeCard": "1",
    "oneClickCheckout": "1",
    "preAuthorize": "0"
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
  },
  "authorization": {
    "eci": "05",
    "cavv": "AAABAWFlmQAAAABjRWWZEEFgFz",
    "threeDSTransID": "67b4c71f-4e6b-4f98-9f2a-1234567890ab",
    "threeDSenrolled": "Y",
    "threeDSstatus": "Success"
  },
  "threeDS2RequestData": {
    "threeDSVersion": "2.2.0",
    "deviceChannel": "APP"
  }
  }'
```

**Request Body (Saved Card):**

```json
curl -X POST \
  https://apitest.payu.in/v2/payments \
  -H 'date: Mon, 05 Oct 2024 11:00:00 GMT' \
  -H 'authorization: HMAC smsplus:4d1ea4e74243ea5b2b5b8b1d8a7b1a2e3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9' \
  -H 'content-type: application/json' \
  -d 
{
  "accountId": "smsplus",
  "referenceId": "b5f2d8785768087678fn5",
  "currency": "INR",
  "paymentSource": "WEB",
  "paymentMethod": {
    "name": "CreditCard",
    "bankCode": "CC",
    "paymentCard": {
      "cardToken": "29850879bf39848ca078727b8e1a95165a41cea1",
      "cardTokenType": "NETWORK",
      "tavv": "/wAAAAAAPtP+g6IAmbSeg1gAAAA=",
      "last4Digits": "0000",
      "cvv": "123"
    }
  },
  "order": {
    "productInfo": "Saved Card Test Product",
    "paymentChargeSpecification": {
      "price": 100.00
    }
  },
  "additionalInfo": {
    "txnS2sFlow": "2",
    "oneClickCheckout": "1"
  },
  "callBackActions": {
    "successAction": "https://example.com/success",
    "failureAction": "https://example.com/failure"
  },
  "billingDetails": {
    "firstName": "John",
    "lastName": "Doe",
    "phone": "9876543210",
    "email": "john.doe@example.com"
  }
}'
```

### Sample Response

```json
{
  "result": {
    "paymentId": "1999110000001769",
    "redirectUrl": "https://secure.payu.in/ResponseHandler.php",
    "authAction": "https://apitest.payu.in/v2/payments/1999110000001769/auth",
    "redirectTemplate": "<html><body>...</body></html>",
    "card": {
      "binData": {
        "pureS2SSupported": false,
        "issuingBank": "ICICI",
        "category": "creditcard",
        "cardType": "VISA",
        "isDomestic": true
      }
    }
  },
  "status": "PENDING",
  "message": "Please call verify API to get the transaction status"
}
```

## Step 3: Verify the Payment

After the payment is processed, you must verify the payment status using the verification API to get the final transaction status.

### Sample request

**Environment**

| Environment | URL                                   |
| ----------- | ------------------------------------- |
| Test        | `https://test.payu.in/v3/transaction` |
| Production  | `https://api.payu.in/v3/transaction`  |

<br />

```json
curl --location 'https://test.payu.in/v3/transaction' \
--header 'Content-Type: application/json' \
--header 'date: Thu, 27 Mar 2025 06:35:21 GMT' \
--header 'authorization: hmac username="PRiQvJ", algorithm="sha512", headers="date", signature="42a54cc7450fe1e7a3cf35ebfaed1b828e37062964266fd33186c7b2526e85e3ea2d46946a728ca50e46423ea9a6b2edb8c1315b58fa69297e1e91d3d34804a1"' \
--header 'Info-Command: verify_payment' \
--data '{
    "txnId":["512345678901234"]
}'
```

### Sample response

```json
{
  "message": "Success",
  "status": 1,
  "result": [
    {
      "mihpayId": 1999110000001769,
      "bankReferenceNumber": "CC12345678",
      "amount": 100.00,
      "mode": "CC",
      "requestId": "",
      "originalAmount": 100.00,
      "additionalCharges": 0.00,
      "discount": 0.00,
      "netDebitAmount": 100.00,
      "productInfo": "Credit Card Test Product",
      "firstName": "John",
      "bankcode": "CC",
      "nameOnCard": "JOHN DOE",
      "cardNo": "XXXXXXXXXXXX0000",
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
      "authRefNo": "123456789",
      "originalCurrency": "INR",
      "threeDSVersion": "2.2.0",
      "message": "Found TxnId",
      "txnId": "b5f2d8785768087678fn4"
    }
  ]
}
```

## Card-specific features

### Card storage and tokenization

You can store cards for future use by setting `storeCard: "1"` in the `additionalInfo` object. This enables:

* Card tokenization for PCI compliance
* One-click checkout for returning customers
* Secure card storage without storing sensitive data

### 3D Secure authentication

PayU supports 3D Secure 1.0 and 2.0 for enhanced security:

* **3D Secure 1.0**: Traditional authentication with ACS redirect
* **3D Secure 2.0**: Enhanced authentication with device fingerprinting

### Pre-authorization

Enable pre-authorization mode by setting `preAuthorize: "1"` to:

* Authorize payments without immediate capture
* Capture authorized payments later using capture API
* Handle partial captures and refunds

### EMI support

PayU supports EMI (Equated Monthly Installments) for eligible cards:

* Check EMI eligibility using bank-specific parameters
* Configure subvention amounts for merchant-funded EMI
* Support for both bank EMI and cardless EMI