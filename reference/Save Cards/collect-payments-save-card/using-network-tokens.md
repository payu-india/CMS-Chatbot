---
title: Using Network Tokens
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Collecting Payments from Saved card using Tokens
  description: >-
    Discover how to use the _payment API to process payments with saved card
    tokens. This guide provides detailed instructions, request parameters, and
    sample responses for collecting payment with saved card tokens.
  robots: index
next:
  description: ''
---
This scenario is applicable if you wanted to collect payments using network tokens.

HTTP Method: **POST**

## Applicable scenarios

* Merchant has the card token, TAVV(Cryptogram), and the last four digits of the card 
* The token could be created by the merchant or through another partner 

> 📘 Note
>
> This scenario is applicable if you are PCI compliant and got the network token and TAVV from any other aggregator or schemes and then sending the card transaction request in the form of authentication.

## Request Parameters

> 📘 Notes for additional\_info:
>
> * The last 4 digits of cards is mandatory for all transactions.
> * Some payment gateways require the Token Requester ID (trid) and Token Reference Number (tokenRefNo) to be passed for processing the transaction. Not passing these values will restrict the number of payment gateways available for processing the transaction.
> * Token Requester ID (trid) and Token Reference Number (tokenRefNo) are mandatory for Diners token transactions.

<HTMLBlock>{`
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
`}</HTMLBlock>

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

#### Order object

<V2_order_object />

#### Additional Info Object

<AdditionalI_Info_object />

#### Callback Actions Object

<CallbackActions_object />

#### Billing Details Object

<BillingDetails_object />

#### Authorization Object

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
 <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Field</th>
 <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
 <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
<tr>
 <td style="border: 1px solid #ddd; padding: 8px;">eci<br/><code>optional</code></td>
 <td style="border: 1px solid #ddd; padding: 8px;">Electronic Commerce Indicator.</td>
 <td style="border: 1px solid #ddd; padding: 8px;">05</td>
</tr>
<tr>
 <td style="border: 1px solid #ddd; padding: 8px;">cavv<br/><code>optional</code></td>
 <td style="border: 1px solid #ddd; padding: 8px;">Cardholder Authentication Verification Value.</td>
 <td style="border: 1px solid #ddd; padding: 8px;">AAABAWFlmQAAAABjRWWZEEFgFz</td>
</tr>
<tr>
 <td style="border: 1px solid #ddd; padding: 8px;">threeDSTransID<br/><code>optional</code></td>
 <td style="border: 1px solid #ddd; padding: 8px;">3DS Transaction ID.</td>
 <td style="border: 1px solid #ddd; padding: 8px;">67b4c71f-4e6b-4f98-9f2a-1234567890ab</td>
</tr>
<tr>
 <td style="border: 1px solid #ddd; padding: 8px;">threeDSenrolled<br/><code>optional</code></td>
 <td style="border: 1px solid #ddd; padding: 8px;">Indicates if the card is enrolled in 3D Secure.</td>
 <td style="border: 1px solid #ddd; padding: 8px;">Y</td>
</tr>
<tr>
 <td style="border: 1px solid #ddd; padding: 8px;">threeDSstatus<br/><code>optional</code></td>
 <td style="border: 1px solid #ddd; padding: 8px;">Status of the 3D Secure authentication.</td>
 <td style="border: 1px solid #ddd; padding: 8px;">Success</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

#### ThreeDS2 Request Data Object

<ThreeDSRequestData_object />

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

### Sample response

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