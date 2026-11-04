---
title: v2 Payments API for POS Merchants
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: v2 Payments API for POS Merchants
excerpt: Initiate in-store card and UPI payments directly on your mapped POS terminals via PayU's v2 payments endpoint.
deprecated: false
hidden: false
metadata:
  robots: index
---
The **V2 Payments API for POS Merchants** (`POST /v2/payments`) enables billing systems, Point of Sale (POS) software, and ERP platforms to initiate in-store card and UPI transactions directly on connected PayU POS terminals.

When your billing application initiates a transaction via this endpoint, PayU's cloud payment engine pushes the payment request to the designated physical terminal (`posDeviceId`). The customer completes the transaction by dipping/tapping/swiping their card or scanning the dynamic UPI QR code displayed on the terminal screen.

---

## Environment

| Environment | HTTP Method | Base URL | Content-Type |
| :--- | :--- | :--- | :--- |
| **Sandbox (UAT)** | `POST` | `https://apitest.payu.in/v2/payments` | `application/json` |
| **Production** | `POST` | `https://api.payu.in/v2/payments` | `application/json` |

---

## Request Authentication & Headers

Requests to PayU's v2 Payments API must be signed using the PayU V2 HMAC authorization scheme.

### Request Header

| Header | Description |
| :--- | :--- |
| Content-Type | _String_<br>Must be set to `application/json`. |
| date | _String_<br>Current request timestamp formatted according to RFC 1123 / RFC 7231 (e.g. `Wed, 04 Nov 2026 12:00:00 GMT`). Must match the server clock within ±15 minutes. |
| authorization | _String_<br>HMAC-SHA512 authorization signature calculated as per the PayU v2 authentication specification. |

## Request Parameters

### Mandatory Parameters

| Parameter | Description |
| :--- | :--- |
| accountId | _String_<br>Merchant account identifier (MID or merchant key) registered with PayU (e.g. `smsplus`). |
| txnId | _String_<br>Merchant's unique transaction reference identifier. Special characters allowed: `-`, `_`. Maximum length: 50 characters. |
| amount | _Number_ or _String_<br>Gross transaction amount in INR. Both numeric and decimal string formats are accepted (e.g. `10.00`, `10.55`, or `"10.55"`). |
| currency | _String_<br>Three-letter ISO 4217 currency code. Must be set to `INR` for domestic in-store POS transactions. |
| paymentSource | _String_<br>Source channel identifier for the payment request. Pass `POS` or `WEB` depending on your integration profile. |
| paymentMethod | _Object_<br>Container object specifying the in-store POS payment instrument and channel. For more information, refer to [paymentMethod  JSON Object Fields Description](#paymentmethod--json-object-fields-description) |
| additionalInfo | _Object_<br>Container object holding transaction execution flow directives. For more information, refer to [additionalInfo JSON Object Fields Description](#additionalinfo-json-object-fields-description)|
| callBackActions | _Object_<br>Container object holding callback and redirect endpoints. For more information, refer to [callBackActions JSON Object Fields Description](callbackactions-json-object-fields-description)|
| order | _Object_<br>Container object holding product metadata, custom tracking fields, and price specifications. For more information, refer to [order JSON Object Fields Description](#order-json-object-fields-description) |
| omniChannelDetails | _Object_<br>Container object holding hardware terminal specifications, device routing identifiers, and charge slip display lines. For more information, refer to [omniChannelDetails JSON Object Fields Description](omnichanneldetails-json-object-fields-description)|

### Optional Parameters

| Parameter | Description |
| :--- | :--- |
| gstParams | _Object_<br>Container object holding GST invoice parameters, GSTIN, and tax component breakdowns. For more information, refer to [gstParams JSON Object Fields Description](#gstparams-json-object-fields-description) |

### Nested Object Fields Description
#### paymentMethod  JSON Object Fields Description

Defines the payment instrument and routing channel for POS terminal execution.

**Mandatory Fields**

| Field | Description |
| :--- | :--- |
| name | _String_<br>Payment method name. Must be hardcoded to `POS` for in-store terminal transactions. |
| bankCode | _String_<br>Bank code identifier. Must be hardcoded to `POS` for in-store terminal transactions. |

```json
"paymentMethod": {
  "name": "POS",
  "bankCode": "POS"
}
```

---

#### additionalInfo JSON Object Fields Description

Directs the transaction flow engine inside PayU's payment gateway.

**Mandatory Fields**

| Field | Description |
| :--- | :--- |
| txnFlow | _String_<br>Transaction flow mode. Must be set to `seamless` for in-store POS transactions. |
| txnS2sFlow | _String_<br>Server-to-server flow configuration identifier. Must be set to `"4"` for in-store POS transactions. |

```json
"additionalInfo": {
  "txnFlow": "seamless",
  "txnS2sFlow": "4"
}
```

---

#### order JSON Object Fields Description

Encapsulates order details, product information, user-defined fields, and price specifications.

**Mandatory Fields**

| Field | Description |
| :--- | :--- |
| paymentChargeSpecification | _Object_<br>Financial charge container defining the payable transaction price. |
| paymentChargeSpecification.price | _Number_ or _String_<br>Gross transaction amount in INR. Must match the top-level `amount` value (e.g. `10.00`). |

**Optional Fields**

| Field | Description |
| :--- | :--- |
| productInfo | _String_<br>Concise description or title of the product, service, or retail department (e.g. `POS Payment`). |
| userDefinedFields | _Object_<br>Container object holding custom merchant tracking metadata. |
| userDefinedFields.udf1 | _String_<br>User Defined Field 1 (e.g. store identifier `store-123`). Maximum length: 255 characters. |
| userDefinedFields.udf2 | _String_<br>User Defined Field 2 (e.g. cashier identifier `cashier-456`). Maximum length: 255 characters. |
| userDefinedFields.udf3 | _String_<br>User Defined Field 3 for internal merchant metadata. Maximum length: 255 characters. |
| userDefinedFields.udf4 | _String_<br>User Defined Field 4 for internal merchant metadata. Maximum length: 255 characters. |
| userDefinedFields.udf5 | _String_<br>User Defined Field 5 for internal merchant metadata. Maximum length: 255 characters. |

```json
"order": {
  "productInfo": "POS Payment",
  "userDefinedFields": {
    "udf1": "store-123",
    "udf2": "cashier-456"
  },
  "paymentChargeSpecification": {
    "price": 10.00
  }
}
```
---

#### callBackActions JSON Object Fields Description

Defines callback actions for web redirects. While customer web browser redirection is not performed during offline in-store terminal payments, the V2 gateway schema enforces `successAction`.

**Mandatory Fields**

| Field | Description |
| :--- | :--- |
| successAction | _String_<br>HTTPS URL placeholder for success redirection. Provide your application URL (e.g. `https://yoursite.com/success`). |

**Optional Fields**

| Parameter | Description |
| :--- | :--- |
| failureAction | _String_<br>HTTPS URL placeholder for failure redirection (e.g. `https://yoursite.com/failure`). |
| cancelAction | _String_<br>HTTPS URL placeholder for cancellation redirection (e.g. `https://yoursite.com/cancel`). |

```json
"callBackActions": {
  "successAction": "https://yoursite.com/success",
  "failureAction": "https://yoursite.com/failure",
  "cancelAction": "https://yoursite.com/cancel"
}
```

---

#### omniChannelDetails JSON Object Fields Description

Specifies the target POS hardware terminal, enforced payment mode on the screen, and custom print lines for the charge slip.

**Mandatory Fields**

| Field | Description |
| :--- | :--- |
| posDeviceId | _String_<br>The unique terminal hardware identifier mapped to your merchant account in PayU's terminal management system (e.g. `"134"`). |

**Optional Fields**

| Parameter | Description |
| :--- | :--- |
| posPaymentMethod | _String_<br>Specific payment mode to enforce on the POS terminal screen. Allowed values: `sale` (card swipe, chip dip, or contactless tap) or `qr` (Dynamic UPI QR code). If omitted, the terminal allows the cashier/customer to choose. |
| userId | _String_<br>Cashier, counter, or operator identifier tagged to the transaction for auditing (e.g. `cashier-123`). |
| printInfo | _Object_<br>Container object holding custom text lines printed on the physical thermal receipt slip. |
| printInfo.printInfo1 | _String_<br>Primary custom print line displayed on the printed charge slip (e.g. store branch name `Puma Store Pimpri`). |
| printInfo.printInfo2 | _String_<br>Secondary custom print line displayed on the printed charge slip (e.g. store address `Pimpri, Pune`). |

```json
"omniChannelDetails": {
  "printInfo": {
    "printInfo1": "Puma Store Pimpri",
    "printInfo2": "Pimpri, Pune"
  },
  "userId": "cashier-123",
  "posDeviceId": "134",
  "posPaymentMethod": "sale"
}
```

---

#### gstParams JSON Object Fields Description

Captures itemized GST tax invoices, tax identification numbers, and statutory levy breakdowns.
**All the fields are optional**
| Field | Description |
| :--- | :--- |
| invoiceNo | _String_<br>Unique commercial invoice number associated with the bill (e.g. `INV-1234`). |
| invoiceDate | _String_<br>Invoice creation timestamp in ISO 8601 format with timezone offset (e.g. `1993-01-12T06:42:12+05:30`). |
| invoiceName | _String_<br>Title or descriptive label of the invoice (e.g. `Store Invoice`). |
| gstIn | _String_<br>15-character Goods and Services Tax Identification Number (GSTIN) of the merchant or billing store (e.g. `08TESTF0078P1ZP`). |
| gst | _Number_ or _String_<br>Total cumulative GST amount levied on the order. |
| cgst | _Number_ or _String_<br>Central Goods and Services Tax amount. |
| sgst | _Number_ or _String_<br>State Goods and Services Tax amount. |
| igst | _Number_ or _String_<br>Integrated Goods and Services Tax amount (for inter-state transactions). |
| cess | _Number_ or _String_<br>Statutory cess amount applicable to the purchase. |
| gstIncentive | _Number_ or _String_<br>Government-mandated GST incentive or concession value. |
| gstPercentage | _Number_ or _String_<br>Aggregate GST percentage rate applied (e.g. `18` or `50`). |

```json
"gstParams": {
  "invoiceNo": "INV-1234",
  "invoiceDate": "1993-01-12T06:42:12+05:30",
  "invoiceName": "Store Invoice",
  "gstIn": "08TESTF0078P1ZP",
  "gst": "10",
  "cgst": "10",
  "sgst": "40",
  "igst": "50",
  "cess": "60",
  "gstIncentive": "12.5",
  "gstPercentage": "50"
}
```

---

## Sample Request

The following cURL command demonstrates initiating a ₹10.00 in-store POS sale transaction:

```bash
curl --location 'https://api.payu.in/v2/payments' \
--header 'Content-Type: application/json' \
--header 'date: Wed, 04 Nov 2026 12:00:00 GMT' \
--header 'authorization: {{authorization}}' \
--data-raw '{
  "accountId": "smsplus",
  "txnId": "b5f297999999879895905",
  "amount": 10.00,
  "currency": "INR",
  "paymentSource": "WEB",
  "paymentMethod": {
    "name": "POS",
    "bankCode": "POS"
  },
  "additionalInfo": {
    "txnFlow": "seamless",
    "txnS2sFlow": "4"
  },
  "callBackActions": {
    "successAction": "https://yoursite.com/success",
    "failureAction": "https://yoursite.com/failure",
    "cancelAction": "https://yoursite.com/cancel"
  },
  "order": {
    "productInfo": "POS Payment",
    "userDefinedFields": {
      "udf1": "store-123",
      "udf2": "cashier-456"
    },
    "paymentChargeSpecification": {
      "price": 10.00
    }
  },
  "gstParams": {
    "invoiceNo": "INV-1234",
    "invoiceDate": "1993-01-12T06:42:12+05:30",
    "invoiceName": "Store Invoice",
    "gstIn": "08TESTF0078P1ZP",
    "gst": "10",
    "cgst": "10",
    "sgst": "40",
    "igst": "50",
    "cess": "60",
    "gstIncentive": "12.5",
    "gstPercentage": "50"
  },
  "omniChannelDetails": {
    "printInfo": {
      "printInfo1": "Puma Store Pimpri",
      "printInfo2": "Pimpri, Pune"
    },
    "userId": "cashier-123",
    "posDeviceId": "134",
    "posPaymentMethod": "sale"
  }
}'
```

---

## Response Structure

The API response returns two top-level containers: `metaData` (transaction status and error descriptors) and `result` (generated identifiers).

### Response Container: `metaData`

| Field | Description | Example |
| :--- | :--- | :--- |
| txnId | _String_<br>Unique transaction ID passed by the merchant in the request. | `TXN0001` |
| referenceId | _String_<br>Encrypted 64-character transaction reference generated by PayU. | `39679eb1408864fc5d26b4aaae5c69cf0e633108168442c548c317ff5cfd7239` |
| txnStatus | _String_<br>Overall transaction status. Possible values: `pending`, `failed`. | `pending` |
| unmappedStatus | _String_<br>Granular processing stage status. Possible values: `pending`, `failure`. | `pending` |
| statusCode | _String_<br>Standard PayU response status code (e.g. `E000` for success). | `E000` |
| message | _String_<br>Human-readable description of the status code. | `Payment initiated successfully` |

### Response Container: `result`

| Field | Description | Example |
| :--- | :--- | :--- |
| paymentId | _String_<br>Unique payment identifier generated by PayU. | `1234567890` |
| authAction | _String_<br>Internal authentication action URL generated by PayU's gateway. | `https://api.payu.in:8443/payments/990000000000005335/otps` |
| otpPostUrl | _String_<br>Endpoint for posting OTP (empty for offline POS terminal transactions). | `""` |

---

## Transaction Lifecycle & Status Code Matrix

The following table outlines the status codes, stage flags, and resolutions encountered when initiating in-store POS transactions:

| Scenario | txnStatus | unmappedStatus | statusCode | message | Description & Troubleshooting |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Payment initiated successfully** | pending | pending | `E000` | Payment initiated successfully | The payment request was successfully accepted and dispatched to the POS terminal. The terminal is currently awaiting customer authorization. |
| **Transaction not initiated** | failed | failure | `E342` | Transaction not initiated | The gateway could not initiate payment on the physical terminal. Verify that the terminal is powered on, connected to Wi-Fi/4G, and not in an active payment session. |
| **Inactive payment option** | failed | failure | `EX158` | Merchant Integration Exception occurred | POS payment acceptance is not enabled or configured for the specified merchant account (`accountId`). Contact PayU support to activate POS processing. |
| **Invalid PG & bank code** | failed | failure | `E1101` | Invalid PG & Bank Code Combination | The values passed in `paymentMethod.name` or `paymentMethod.bankCode` are invalid. Both fields must be set strictly to `"POS"`. |
| **Invalid device ID** | failed | failure | `E2081` | Invalid Device Id | The `posDeviceId` supplied in `omniChannelDetails` is invalid, inactive, or not mapped to your merchant MID. |

---

## Sample Responses

### 1. Success — Payment Initiated Successfully (`E000`)

```json
{
  "metaData": {
    "message": "Payment initiated successfully",
    "referenceId": "39679eb1408864fc5d26b4aaae5c69cf0e633108168442c548c317ff5cfd7239",
    "statusCode": "E000",
    "txnId": "454672833901",
    "txnStatus": "pending",
    "unmappedStatus": "pending"
  },
  "result": {
    "otpPostUrl": "",
    "authAction": "https://api.payu.in:8443/payments/990000000000005335/otps",
    "paymentId": "1234567890"
  }
}
```

### 2. Failure — Transaction Not Initiated (`E342`)

```json
{
  "metaData": {
    "message": "Transaction not initiated",
    "referenceId": "39679eb1408864fc5d26b4aaae5c69cf08b672ec877f06e9f41668e3a5e6eb30",
    "statusCode": "E342",
    "txnId": "454672833999",
    "txnStatus": "failed",
    "unmappedStatus": "failure"
  },
  "result": {
    "otpPostUrl": "",
    "authAction": "https://api.payu.in:8443/payments/990000000000005335/otps",
    "paymentId": "1234567890"
  }
}
```

### 3. Failure — Inactive Payment Option (`EX158`)

```json
{
  "metaData": {
    "message": "Merchant Integration Exception occurred",
    "referenceId": "78a03c334c2b487ed65758a197702386967b81a26581af15be45b3063355cc45",
    "statusCode": "EX158",
    "txnId": "pos148",
    "txnStatus": "failed",
    "unmappedStatus": "failure"
  },
  "result": {
    "otpPostUrl": "",
    "authAction": "https://api.payu.in:8443/payments/990000000000005335/otps",
    "paymentId": "1234567890"
  }
}
```

### 4. Failure — Invalid PG & Bank Code (`E1101`)

```json
{
  "metaData": {
    "message": "Invalid PG & Bank Code Combination",
    "referenceId": "78a03c334c2b487ed65758a197702386967b81a26581af15be45b3063355cc45",
    "statusCode": "E1101",
    "txnId": "pos148",
    "txnStatus": "failed",
    "unmappedStatus": "failure"
  },
  "result": {
    "otpPostUrl": "",
    "authAction": "https://api.payu.in:8443/payments/990000000000005335/otps",
    "paymentId": "1234567890"
  }
}
```

### 5. Failure — Invalid Device ID (`E2081`)

```json
{
  "metaData": {
    "message": "Invalid Device Id",
    "referenceId": "f187f77206be8ec89c6935cadc2fc96ae23f1d893472f205ba6e407dd9ce4e06",
    "statusCode": "E2081",
    "txnId": "DBQRp123456789012",
    "txnStatus": "failed",
    "unmappedStatus": "failure"
  },
  "result": {
    "otpPostUrl": "",
    "authAction": "https://api.payu.in:8443/payments/990000000000005335/otps",
    "paymentId": "12312"
  }
}
```

---

## Server-to-Server (S2S) Webhook

Once the customer completes or cancels payment on the physical terminal, PayU dispatches an asynchronous HTTP POST webhook to your configured webhook endpoint.

### Webhook Configuration
- Register your HTTPS webhook endpoint with your PayU Integration Specialist or account manager during onboarding.
- The webhook listener must respond with an HTTP `200 OK` status immediately upon receiving the payload.

### Webhook Payload Schema

| Field | Description | Example |
| :--- | :--- | :--- |
| vendorTxnId | _String_<br>Internal vendor transaction identifier generated during terminal authorization. | `"1499262399"` |
| txnId | _String_<br>Merchant transaction reference ID originally passed in the request. | `"b5f29799999987989990012345"` |
| mihpayId | _Number_<br>PayU unique transaction identifier (`mihpayid`). | `27447252485` |
| flowType | _String_<br>Operational integration flow type. | `"Integrated"` |
| message | _String_<br>Status directive instructing the merchant to confirm state. | `"Please call check status api to get the transaction details"` |
| status | _String_<br>Terminal payment outcome. Possible values: `captured`, `failed`. | `"captured"` |

### Sample Webhook Payload

```json
{
  "vendorTxnId": "1499262399",
  "txnId": "b5f29799999987989990012345",
  "mihpayId": 27447252485,
  "flowType": "Integrated",
  "message": "Please call check status api to get the transaction details",
  "status": "captured"
}
```

<Callout icon="⚠️" theme="warn">
  ### **Mandatory: Verify Final Transaction Status**
  As indicated in the webhook message directive (`"Please call check status api to get the transaction details"`), your billing system should immediately invoke the **Status Enquiry API** using `txnId` to fetch complete payment metadata (card brand, authorization code, terminal RRN, and invoice breakdown) before marking the order as fulfilled in your local database.
</Callout>