---
title: v2 Payments API for POS Merchants
deprecated: false
hidden: true
link:
  new_tab: false
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
---

## Environments & Endpoints

| Environment | Method | Endpoint URL |
| :--- | :--- | :--- |
| **Production** | `POST` | `https://api.payu.in/apilayer/partner/initiatePayment` |
| **Sandbox / Test (UAT)** | `POST` | `https://apitest.payu.in/apilayer/partner/initiatePayment` |

---

## Authentication & Request Headers

Partner QR APIs require dual authentication: a Bearer OAuth token (`X-Partner-Token`) and an HMAC-SHA512 signature (`Authorization`).

<Callout icon="📘" theme="info">
  ### **Merchant Key Placement**
  Do **not** send `X-PayU-Merchant-Key` in the request headers for this API. Instead, pass the merchant key as `accountId` in the JSON request body.
</Callout>

### Mandatory Headers

| Header | Description |
| :--- | :--- |
| Content-Type | _String_<br>Content type of the request payload. Must be set to `application/json`. |
| X-Partner-Token | _String_<br>OAuth 2.0 Bearer access token obtained from PayU's OAuth Token API with `partner_payments` scope.<br>**Format:** `Bearer <access_token>` |
| X-PayU-Reseller-UUID | _String_<br>Unique partner/reseller identifier (UUID) assigned by PayU. |
| date | _String_<br>Current request timestamp formatted in GMT according to RFC 1123 / RFC 7231 (e.g. `Tue, 15 Jul 2025 07:03:38 GMT`). Used in HMAC signature verification. |
| Authorization | _String_<br>HMAC-SHA512 authorization signature generated using the partner credentials, request date, and request body.<br>**Format:** `hmac username="<clientId>", algorithm="sha512", headers="date", signature="<signature>"` |

---

## Request Parameters

### Mandatory Parameters

| Parameter | Description |
| :--- | :--- |
| accountId | _String_<br>Merchant account key / identifier provided by PayU. |
| txnId | _String_<br>Merchant's unique transaction reference identifier. Must be unique per merchant transaction. |
| amount | _Double_ or _String_<br>Transaction amount payable in INR (e.g., `10`, `10.55`, or `"10.55"`). |
| currency | _String_<br>Three-letter ISO 4217 currency code. Pass `INR`. |
| paymentSource | _String_<br>Source channel identifier for the payment request (e.g., `WEB`). |
| paymentMethod | _Object_<br>Container object holding payment instrument configurations. For DBQR, pass `name = "DBQR"` and `bankCode = "UPIDBQR"`. |
| order | _Object_<br>Container object capturing order details, product information, user-defined fields, and price specifications. |
| additionalInfo | _Object_<br>Container object defining transaction flow type, S2S routing flags, and merchant/customer VPA. |
| callBackActions | _Object_<br>Container object holding callback and redirect URLs for payment outcomes. |
| omniChannelDetails | _Object_<br>Container object holding soundbox terminal identifier, store details, and QR session expiry settings. |



#### paymentMethod Object Fields Descrption

| Parameter | Description |
| :--- | :--- |
| name | _String_<br>Payment method name. Hardcoded value: `DBQR`. |
| bankCode | _String_<br>Payment scheme or bank code. Hardcoded value: `UPIDBQR`. |

---

#### additionalInfo Object Fields Descrption

| Parameter | Description |
| :--- | :--- |
| txnFlow | _String_<br>Transaction integration flow. Hardcoded value: `seamless`. |
| createOrder | _Boolean_<br>Flag to create an order entity. Hardcoded value: `true`. |
| txnS2sFlow | _String_<br>Server-to-server transaction flow identifier. Hardcoded value: `"4"`. |
| vpa | _String_<br>Merchant or customer Virtual Payment Address (VPA) used for the DBQR transaction flow (e.g., `7807305029@ptsbi`). |


### order Object Fields Descrption
**Mandatory Parameters**
| Parameter | Description |
| :--- | :--- |
| paymentChargeSpecification.price | _Double_ or _String_<br>Payable price matching the transaction `amount` (e.g., `10.00` or `"10.00"`). |

*Optional Parameters**
| Parameter | Description |
| :--- | :--- |
| productInfo | _String_<br>Brief description or product title for the transaction (e.g., `UPI Payment for Order`). |
| userDefinedFields | _Object_<br>Container holding custom metadata fields `udf1` through `udf10` for internal reconciliation and tracking. |

#### callBackActions Object Fields Descrption

| Parameter | Description |
| :--- | :--- |
| successAction | _String_<br>HTTPS URL to redirect or notify upon successful transaction completion. |

### Optional Parameters

| Parameter | Description |
| :--- | :--- |
| failureAction | _String_<br>HTTPS URL to redirect or notify if the payment fails or is declined. |
| cancelAction | _String_<br>HTTPS URL to redirect or notify if the payment session is abandoned or cancelled. |


---

### Nested Object: `omniChannelDetails`

#### Mandatory Parameters

| Parameter | Description |
| :--- | :--- |
| soundBoxTerminalId | _String_<br>Unique soundbox or POS terminal identifier mapped to the merchant (e.g., `N820W368427`). |

#### Optional Parameters

| Parameter | Description |
| :--- | :--- |
| outletName | _String_<br>Physical outlet or store name (e.g., `puma pimpri`). |
| vendorId | _String_<br>Partner or vendor reference identifier. |
| tips | _String_<br>Gratuity or tips amount/information, if applicable. |
| childMerchId | _String_<br>Child merchant account identifier for multi-merchant store configurations. |
| expiryTime | _String_<br>QR code session time-to-live / expiry duration in seconds (e.g., `"100"`). |

---

## Sample Request

### Step A: Generate HMAC Signature (Node.js)

```javascript
const crypto = require('crypto');

const CLIENT_ID = 'YOUR_PARTNER_CLIENT_ID';
const CLIENT_SECRET = 'YOUR_PARTNER_CLIENT_SECRET';

const requestPayload = {
  "accountId": "gtKFFx",
  "txnId": "b5f1212001123",
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
    "soundBoxTerminalId": "N820W368427",
    "outletName": "puma pimpri",
    "vendorId": "vendorId",
    "tips": "tips",
    "childMerchId": "childMerchId",
    "expiryTime": "100"
  }
};

const requestBody = JSON.stringify(requestPayload);
const date = new Date().toUTCString();
const hashString = `${requestBody}|${date}|${CLIENT_SECRET}`;
const signature = crypto.createHash('sha512').update(hashString).digest('hex');
const authorization = `hmac username="${CLIENT_ID}", algorithm="sha512", headers="date", signature="${signature}"`;
```

### Step B: Call Initiate Payment API

```bash cURL
curl --location --request POST 'https://api.payu.in/apilayer/partner/initiatePayment' \
--header 'Content-Type: application/json' \
--header 'X-Partner-Token: Bearer YOUR_ACCESS_TOKEN' \
--header 'X-PayU-Reseller-UUID: YOUR_RESELLER_UUID' \
--header 'date: Tue, 15 Jul 2025 07:03:38 GMT' \
--header 'Authorization: hmac username="YOUR_CLIENT_ID", algorithm="sha512", headers="date", signature="YOUR_SIGNATURE"' \
--data-raw '{
   "accountId": "gtKFFx",
   "txnId": "b5f1212001123",
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
       "soundBoxTerminalId": "N820W368427",
       "outletName": "puma pimpri",
       "vendorId": "vendorId",
       "tips": "tips",
       "childMerchId": "childMerchId",
       "expiryTime": "100"
   }
}'
```

---

## Response Parameters

The response contains two main objects: `metaData` and `result`.

### Nested Object: `metaData`

| Parameter | Description |
| :--- | :--- |
| txnId | _String_<br>Unique transaction ID passed by the merchant in the request. |
| referenceId | _String_<br>Encoded unique identifier generated by PayU for the transaction session. |
| txnStatus | _String_<br>Payment status. Initiated transactions return `pending`. |
| unmappedStatus | _String_<br>Status at different transaction lifecycle stages (e.g., `pending`, `failure`). |
| statusCode | _String_<br>PayU internal status code (e.g., `E342`). Returned on failure or non-success. |
| message | _String_<br>Status code description or error reason. |

---

### Nested Object: `result`

| Parameter | Description |
| :--- | :--- |
| otpPostUrl | _String_<br>PayU internal endpoint URL for handling authentication and OTP responses. |
| authAction | _String_<br>PayU authentication/action URL generated for the payment transaction. |
| paymentId | _String_<br>Unique payment reference identifier (`mihpayId`) generated by PayU for the DBQR transaction. |
| merchantName | _String_<br>Business display name of the merchant account associated with the QR. |
| merchantVpa | _String_<br>Merchant Virtual Payment Address (VPA) encoded into the generated DBQR payment string. |
| qrString | _String_<br>UPI QR intent string. Render this value as a QR code image or stream it to a soundbox device for customer scanning. |
| amount | _String_<br>Transaction amount for which the DBQR payment was created (e.g., `"10.00"`). |

---

## Sample Success Response

When the DBQR transaction is initiated successfully, PayU returns an HTTP `200 OK` with the transaction in `pending` status:

```json
{
  "metaData": {
    "referenceId": "d663c7315932183ab92c095a1774d778cb4dc640bdc9fcd2bfc5138695da65dc",
    "txnId": "b5f1212001123",
    "txnStatus": "pending",
    "unmappedStatus": "pending"
  },
  "result": {
    "otpPostUrl": "https://test.payu.in/ResponseHandler.php",
    "authAction": "https://apitest.payu.in/payments/613345778913213977/otps",
    "paymentId": "613345778913213977",
    "merchantName": "PayUTestAccount",
    "merchantVpa": "yellowqr.testing121@indus",
    "qrString": "upi://pay?pa=yellowqr.testing121@indus&pn=PayU Test Account&tr=613345778913213977&tid=PPPL6133457789132139772309261525576&am=10.00&cu=INR&tn=UPI Transaction",
    "amount": "10.00"
  }
}
```

---

## Transaction Lifecycle & Webhook Notification

1. **Pending Status on Initiation**: Upon successful invocation, the transaction is created in `pending` status awaiting the customer's UPI payment.
2. **Asynchronous Webhook**: When the customer scans the QR code and completes payment via their UPI app, PayU sends an asynchronous Server-to-Server (S2S) webhook notification to the configured partner/merchant webhook URL.
3. **Status Enquiry**: Partners can also verify and reconcile the final transaction status using the **Omni Transaction Status Check API**.

### Sample Webhook Payload

```json
{
  "vendorTxnId": "1499262399",
  "txnId": "b5f29799999987989990012345",
  "mihpayId": 27447252485,
  "flowType": "Non-Integrated",
  "message": "Please call check status api to get the transaction details",
  "status": "captured"
}
```

| Parameter | Description |
| :--- | :--- |
| vendorTxnId | _String_<br>Partner or vendor transaction reference identifier. |
| txnId | _String_<br>Merchant transaction identifier. |
| mihpayId | _Number_<br>Unique PayU reference identifier for the completed transaction. |
| flowType | _String_<br>Payment flow type (e.g., `Non-Integrated`). |
| message | _String_<br>Actionable guidance message to verify transaction details via the Check Status API. |
| status | _String_<br>Final payment capture state (e.g., `captured`). |