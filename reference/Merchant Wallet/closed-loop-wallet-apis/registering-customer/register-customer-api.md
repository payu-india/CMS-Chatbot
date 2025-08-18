---
title: Register Customer API
deprecated: false
hidden: true
metadata:
  robots: index
---
The Register Customer API allows you to register a new customer and facilitates the creation of a digital wallet. This API performs onboarding checks when opted by the issuer.

## Environment

| Environment | URL                                                      |
| ----------- | -------------------------------------------------------- |
| Test        | `http://apitest.payu.in/loyalty-points/v1/wallet/enroll` |
| Production  | `https://api.payu.in/loyalty-points/v1/wallet/enroll`    |

**HTTP Method**: POST

## Authentication

This API uses HMAC-SHA512 authentication. Refer to the [Authentication Guide](/docs/authentication) for detailed implementation.

<Closed_Loop_HMAC />

## Request Parameters

### Body Parameters

The request body contains both encrypted and decrypted parameters.

#### Encrypted

| Parameter                         | Description                                                                                    |
| --------------------------------- | ---------------------------------------------------------------------------------------------- |
| token<br /><code>mandatory</code> | <code>String</code> AES-192-CBC encrypted request body containing all the decrypted parameters |

#### Decrypted


## Response Parameters

| Parameter                | Description                                            | Example                          |
| ------------------------ | ------------------------------------------------------ | -------------------------------- |
| responseCode             | Response status code                                   | 00                               |
| messageCode              | API response code                                      | 3511                             |
| clientTxnId              | Mirrors the request's clientTxnId                      | 20150701235959xhstiesqfds        |
| formfactor.accountNumber | Generated account number for form factors              | 72623345                         |
| formfactor.uniqueNumber  | Unique number generated for form factors               | 8543213624292443                 |
| formfactor.urn           | Proxy reference number generated for the unique number | 70000000008                      |
| responseMessage          | Response message                                       | CUSTOMER REGISTERED SUCCESSFULLY |

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

| Status Code | Description                              |
| ----------- | ---------------------------------------- |
| 200         | OK - Request processed successfully      |
| 400         | Bad Request - Invalid request parameters |
| 401         | Unauthorized - Authentication failed     |
| 500         | Internal Server Error                    |

## Error Codes

| Error Code | Description                      |
| ---------- | -------------------------------- |
| 3511       | Customer registered successfully |
| 1010       | Invalid message code             |
| 1020       | Missing required parameters      |
| 1030       | Customer already exists          |