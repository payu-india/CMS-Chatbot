---
title: Register Customer API
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: "Register Customer API"
description: "API to register a new customer and create a digital wallet with onboarding checks when opted by the issuer."
---

# Register Customer API

The Register Customer API allows you to register a new customer and facilitates the creation of a digital wallet. This API performs onboarding checks when opted by the issuer.

## Environment

| Environment | URL |
| ----------- | --- |
| Test | `http://apitest.payu.in/loyalty-points/v1/wallet/enroll` |
| Production | `https://api.payu.in/loyalty-points/v1/wallet/enroll` |

**HTTP Method**: POST

## Authentication

This API uses HMAC-SHA512 authentication. Refer to the [Authentication Guide](/docs/authentication) for detailed implementation.

## Request Headers

| Parameter | Description |
| --------- | ----------- |
| walletIdentifier<br/><code>mandatory</code> | <code>String</code> Program Type (e.g., CLW) |
| date<br/><code>mandatory</code> | <code>String</code> GMT formatted date (e.g., Thu, 17 Feb 2022 08:17:59 GMT) |
| Authorization<br/><code>mandatory</code> | <code>String</code> HMAC-SHA512-based authentication token |
| Content-Type<br/><code>mandatory</code> | <code>String</code> application/json |

## Request Parameters

### Body Parameters

The request body contains both encrypted and decrypted parameters.

#### Encrypted
| Parameter | Description |
| --------- | ----------- |
| token<br/><code>mandatory</code> | <code>String</code> AES-192-CBC encrypted request body containing all the decrypted parameters |

#### Decrypted
| Parameter | Description | Example |
| --------- | ----------- | ------- |
| messageCode<br/><code>mandatory</code> | <code>Numeric(4)</code> API code to identify Register Customer API | 3510 |
| clientTxnId<br/><code>mandatory</code> | <code>Alphanumeric(100)</code> Unique transaction ID from the calling application | 20150701235959xhstiesqfds |
| requestDateTime<br/><code>mandatory</code> | <code>Numeric(14)</code> Local timestamp of transaction initiation (YYYYMMDDHHMMSS format) | 20230620123143 |
| customerId<br/><code>optional</code> | <code>String(50)</code> Caller-defined unique customer ID. Auto-generated if not provided | 89342546 |
| customerDetails.firstName<br/><code>mandatory</code> | <code>String(50)</code> Customer first name. No invalid symbols allowed | Sourav |
| customerDetails.middleName<br/><code>optional</code> | <code>String(50)</code> Customer middle name | Kumar |
| customerDetails.lastName<br/><code>optional</code> | <code>String(50)</code> Customer last name | Mishra |
| customerDetails.mobileNumber<br/><code>mandatory</code> | <code>Numeric(15)</code> ISD-coded, valid unique mobile number | 919988776655 |
| customerDetails.emailAddress<br/><code>optional</code> | <code>String(50)</code> Valid email address | sourav.mishra@gmail.com |
| customerDetails.dateOfBirth<br/><code>mandatory</code> | <code>String(10)</code> Date of birth (DD-MM-YYYY format) | 11-07-1993 |
| kycProfile<br/><code>mandatory</code> | <code>Numeric(3)</code> Type of KYC: Min KYC (30), Shortfall KYC (300), Full KYC (150) | 150 |
| riskCategory<br/><code>mandatory</code> | <code>String(20)</code> Risk type: Low, Medium, High (Low=100, Medium=500, High=200) | Low |
| productId<br/><code>mandatory</code> | <code>Numeric(5)</code> Program/product ID | 121 |
| formFactorRequired<br/><code>mandatory</code> | <code>Boolean</code> Indicates whether a form factor is required (True/False) | true |

## Response Parameters

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| responseCode | Response status code | 00 |
| messageCode | API response code | 3511 |
| clientTxnId | Mirrors the request's clientTxnId | 20150701235959xhstiesqfds |
| formfactor.accountNumber | Generated account number for form factors | 72623345 |
| formfactor.uniqueNumber | Unique number generated for form factors | 8543213624292443 |
| formfactor.urn | Proxy reference number generated for the unique number | 70000000008 |
| responseMessage | Response message | CUSTOMER REGISTERED SUCCESSFULLY |

## Sample Request

### Encrypted Packet
```bash
curl --location --request POST 'http://apitest.payu.in/loyalty-points/v1/wallet/enroll' \
--header 'walletIdentifier: CLW' \
--header 'date: Wed, 12 Jun 2024 08:53:43 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="hmac_generated_signature"' \
--header 'Content-Type: application/json' \
--data-raw '{
  "token": "h/0YSUd9jKOQ8+2Dc3Phr4s7vxyz123..."
}'
```

### Decrypted Packet
```json
{
  "messageCode": 3510,
  "clientTxnId": "txn12345",
  "requestDateTime": "20230810123015",
  "customerDetails": {
    "firstName": "Alice",
    "lastName": "Smith",
    "dateOfBirth": "12-12-2000",
    "mobileNumber": "917001122334"
  },
  "kycProfile": 150,
  "riskCategory": "Low",
  "productId": 35,
  "formFactorRequired": true
}
```

## Sample Response

### Encrypted Response
```json
{
  "result": "h/0YSUd9jKOQ8+2Dc3Phr4s7vxyz789..."
}
```

### Decrypted Response
```json
{
  "responseCode": "00",
  "messageCode": 3511,
  "clientTxnId": "txn12345",
  "formFactor": {
    "uniqueNumber": "7262334512345678",
    "urn": 10000234
  },
  "responseMessage": "CUSTOMER REGISTERED SUCCESSFULLY"
}
```

## HTTP Status Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | OK - Request processed successfully |
| 400 | Bad Request - Invalid request parameters |
| 401 | Unauthorized - Authentication failed |
| 500 | Internal Server Error |

## Error Codes

| Error Code | Description |
| ---------- | ----------- |
| 3511 | Customer registered successfully |
| 1010 | Invalid message code |
| 1020 | Missing required parameters |
| 1030 | Customer already exists |
