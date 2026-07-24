---
title: Create Transaction API
deprecated: false
hidden: false
metadata:
  robots: index
---
Initiates payment for the order using the selected payment method. Supports Net Banking, UPI Intent, UPI Collect, Cards (Credit/Debit), EMI, and other payment modes.

## Endpoint

| Environment | Base URL |
|-------------|----------|
| UAT / Test | `https://apitest.payu.in/v1/payment` |
| Production | `https://api.payu.in/v1/payment` |

## Sample Request

### Net Banking

```bash
curl -X POST 'https://apitest.payu.in/v1/payment' \
  -H 'accessToken: <access_token>' \
  -H 'orderId: <encrypted_order_id>' \
  -H 'X-Credential-Username: <merchant_key>' \
  -H 'Content-Type: application/json' \
  -d '{
    "txnId": "txn123",
    "offerKeys": ["OfferTest2ZLHN@T23WBwMVnHw7"],
    "promocode": ["AIRINDIA123"],
    "paymentMethod": {
      "bankCode": "ICIB",
      "name": "NetBanking"
    }
  }'
```

### UPI Intent

```bash
curl -X POST 'https://apitest.payu.in/v1/payment' \
  -H 'accessToken: <access_token>' \
  -H 'orderId: <encrypted_order_id>' \
  -H 'X-Credential-Username: <merchant_key>' \
  -H 'Content-Type: application/json' \
  -d '{
    "txnId": "txn123",
    "paymentMethod": {
      "bankCode": "INTENT",
      "name": "UPI"
    }
  }'
```

### Credit/Debit Card

```bash
curl -X POST 'https://apitest.payu.in/v1/payment' \
  -H 'accessToken: <access_token>' \
  -H 'orderId: <encrypted_order_id>' \
  -H 'X-Credential-Username: <merchant_key>' \
  -H 'Content-Type: application/json' \
  -d '{
    "txnId": "txn123",
    "paymentMethod": {
      "name": "CreditCard",
      "bankCode": "CC",
      "paymentCard": {
        "cardNumber": "<card_number>",
        "ownerName": "JOHN DOE",
        "cvv": "<cvv>",
        "expiryMonth": "12",
        "expiryYear": "2028",
        "storeCard": true
      }
    },
    "customer": {
      "address": {
        "billingAddress": {
          "name": "John Doe",
          "email": "john.doe@example.com",
          "addressLine": "123 Main Street",
          "city": "New Delhi",
          "pincode": "110001"
        }
      }
    }
  }'
```

## Sample Response

### Net Banking Response

```json
{
  "result": {
    "acsTemplate": "PGh0bWw+PGJvZHk+...[Base64 encoded HTML form]",
    "otpPostUrl": "https://test.payu.in/ResponseHandler.php"
  },
  "metaData": {
    "message": null,
    "referenceId": "d723a7f7a930ba5acfa65a56c704a3155d3f0910468861d6a3ffb2749622a578",
    "statusCode": null,
    "txnId": "OrderidUATabc021",
    "txnStatus": "pending",
    "unmappedStatus": "pending"
  }
}
```

### UPI Intent Response

```json
{
  "metaData": {
    "referenceId": "8de55018dfed6a00b290ba45f0cd2361",
    "txnId": "7417319597600821248",
    "txnStatus": "pending",
    "unmappedStatus": "pending"
  },
  "result": {
    "paymentId": "26856810726",
    "merchantName": "Air India",
    "merchantVpa": "airtel.payu@axisbank",
    "amount": "10.00",
    "intentURIData": "pa=airtel.payu@axisbank&pn=AIRTEL PAYMENTS BANK LIMITED&tr=26856810726&am=10.00&cu=INR&tn=UPIIntent",
    "acsTemplate": "PGh0bWw+..."
  }
}
```

## Request Parameters
## Header Authentication Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| accessToken<br/>`mandatory` | `string` Access token from the Create Order response (`transaction.accessToken`). | `<access_token>` |
| orderId<br/>`mandatory` | `string` Encrypted order ID from the Create Order response (`transaction.orderid`). | `<encrypted_order_id>` |
| X-Credential-Username<br/>`mandatory` | `string` Merchant key configured for Air India. | `<merchant_key>` |
| Content-Type<br/>`mandatory` | `string` Media type of the JSON request body. | `application/json` |

## Body Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| txnId<br/>`optional` | `string` Merchant transaction reference. If not passed, orderId will be used as payment identifier. | `txn123` |
| paymentMethod<br/>`mandatory` | `object` Payment method container. See [paymentMethod object parameters](#paymentmethod-object-parameters) for details. | - |
| offerKeys<br/>`optional` | `array` One or more offer keys selected by user. | `["OFFER123"]` |
| promocode<br/>`optional` | `array` Promocode against the offer, filled by user. | `["AIRINDIA123"]` |
| customer<br/>`optional` | `object` Customer information including address. Recommended for card payments. | - |
| deviceInfoDetails<br/>`optional` | `object` Device information with fields: userAgent, ipAddress, screenResolution. | - |
| additionalPaymentParams<br/>`optional` | `object` Additional payment parameters like language. | `{"language": "en"}` |

### paymentMethod object parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| name<br/>`mandatory` | `string` Payment method name: `NetBanking`, `UPI`, `CreditCard`, `DebitCard`. | `NetBanking` |
| bankCode<br/>`mandatory` | `string` Bank/payment code (e.g., `ICIB` for ICICI Bank, `CC` for cards, `UPI` for UPI, `INTENT` for UPI Intent). | `ICIB` |
| vpa<br/>`conditional` | `string` UPI Virtual Payment Address. Required for UPI Collect. | `user@upi` |
| paymentCard<br/>`conditional` | `object` Card details. Required for card payments unless a stored card token is used. See [paymentCard object parameters](#paymentcard-object-parameters) for details. | - |
| storeCard<br/>`optional` | `boolean` Flag to save card with PayU. | `true` |
| storeCardToken<br/>`optional` | `string` Stored card token (for saved card transactions). | `xyz789token` |
| storecardTokenType<br/>`optional` | `string` Token type. Set to `1` for PayU tokens. | `1` |

### paymentCard object parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| cardNumber<br/>`conditional` | `string` Full card number. Required when a stored card token is not used. | `<card_number>` |
| ownerName<br/>`conditional` | `string` Cardholder name. Required when `paymentCard` is sent. | `JOHN DOE` |
| cvv<br/>`conditional` | `string` Card CVV. Required when `paymentCard` is sent. | `<cvv>` |
| expiryMonth<br/>`conditional` | `string` Expiry month in `MM` format. Required when `paymentCard` is sent. | `12` |
| expiryYear<br/>`conditional` | `string` Expiry year in `YYYY` format. Required when `paymentCard` is sent. | `2028` |
| storeCard<br/>`optional` | `boolean` Whether to save card. | `true` |

## Response Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| result | `object` Contains acsTemplate and payment-specific data. | - |
| result.acsTemplate | `string` **Base64 encoded HTML form** - Decode and render for 3DS/bank authentication. | `PGh0bWw+...` |
| result.postUri | `string` Redirection URL for authentication (if provided). | `https://bank.com/auth` |
| result.intentURIData | `string` **For UPI Intent**: Add prefix `upi://pay?` and suffix `&package={psp_app_package_name}`. | `pa=airtel.payu@axisbank&...` |
| result.paymentId | `string` PayU payment ID. | `26856810726` |
| result.merchantVpa | `string` Merchant VPA (for UPI). | `airtel.payu@axisbank` |
| metaData | `object` Transaction metadata. | - |
| metaData.referenceId | `string` **Important**: PayU reference ID for transaction. | `8de55018dfed6a00b290ba45f0cd2361` |
| metaData.txnId | `string` Transaction ID. | `7417319597600821248` |
| metaData.txnStatus | `string` Transaction status. | `pending` |
| metaData.unmappedStatus | `string` `pending` (for success), `failure` (if createTxn failed). | `pending` |
| binData | `object` Bank card BIN information (for card payments). Contains: issuingBank, category, cardType, isDomestic. | - |
