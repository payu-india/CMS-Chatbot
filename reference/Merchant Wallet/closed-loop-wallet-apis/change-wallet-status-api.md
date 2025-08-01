---
title: Change Wallet Status API
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Change Wallet Status** API allows you to change the operational status of a wallet. This includes temporarily blocking, marking as dormant, or permanently closing a wallet. This API is essential for wallet lifecycle management and compliance requirements.

## Environment

| Environment | URL                                                                        |
| ----------- | -------------------------------------------------------------------------- |
| Test        | `https://apitest.payu.in/loyalty-points/v1/wallet/onboarding/walletStatus` |
| Production  | `https://api.payu.in/loyalty-points/v1/wallet/onboarding/walletStatus`     |

**HTTP Method**: POST

## Authentication

This API uses HMAC-SHA512 authentication. Refer to the [Authentication Guide](/docs/authentication) for detailed implementation.

## Request Headers

| Parameter                                    | Description                                                                  |
| -------------------------------------------- | ---------------------------------------------------------------------------- |
| walletIdentifier<br /><code>mandatory</code> | <code>String</code> Program Type (e.g., CLW)                                 |
| date<br /><code>mandatory</code>             | <code>String</code> GMT formatted date (e.g., Thu, 17 Feb 2022 08:17:59 GMT) |
| Authorization<br /><code>mandatory</code>    | <code>String</code> HMAC-SHA512-based authentication token                   |
| Content-Type<br /><code>mandatory</code>     | <code>String</code> application/json                                         |

## Request Parameters

### Body Parameters

The request body contains both encrypted and decrypted parameters.

#### Encrypted

| Parameter                         | Description                                                                                    |
| --------------------------------- | ---------------------------------------------------------------------------------------------- |
| token<br /><code>mandatory</code> | <code>String</code> AES-192-CBC encrypted request body containing all the decrypted parameters |

#### Decrypted

| Parameter                                   | Description                                                                          | Example                                    |
| ------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------ |
| messageCode<br /><code>mandatory</code>     | <code>Numeric(4)</code> Unique API ID for wallet status change                       | 3530                                       |
| clientTxnId<br /><code>mandatory</code>     | <code>String(100)</code> Unique transaction ID for each request                      | CBL-458                                    |
| requestDateTime<br /><code>mandatory</code> | <code>Numeric(14)</code> Local timestamp when request was initiated (YYYYMMDDHHMMSS) | 20220514181818                             |
| accountNumber<br /><code>mandatory</code>   | <code>String(15)</code> Unique account number for the sub-wallet                     | 2000123hh                                  |
| statusType<br /><code>mandatory</code>      | <code>String(10)</code> Status type to set                                           | CreditDebit                                |
| reason<br /><code>optional</code>           | <code>String(100)</code> Reason for status change                                    | Customer request                           |
| remarks<br /><code>optional</code>          | <code>String(255)</code> Additional remarks                                          | Temporary block due to suspicious activity |

## Response Parameters

| Parameter       | Description                      | Example                            |
| --------------- | -------------------------------- | ---------------------------------- |
| responseCode    | Response status code             | 00                                 |
| messageCode     | API response code                | 3531                               |
| clientTxnId     | Echoes the request's clientTxnId | CBL-458                            |
| accountNumber   | Account number that was updated  | 2000123hh                          |
| statusType      | New status type applied          | CreditDebit                        |
| bankId          | Bank identifier                  | 123                                |
| description     | Description of the status change | Wallet status updated successfully |
| responseMessage | Response message                 | WALLET STATUS UPDATED SUCCESSFULLY |

## Sample Request

### Encrypted Packet

```bash
curl --location --request POST 'https://apitest.payu.in/loyalty-points/v1/wallet/onboarding/walletStatus' \
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
  "messageCode": 3530,
  "clientTxnId": "CBL-458",
  "requestDateTime": "20220514181818",
  "accountNumber": "2000123hh",
  "statusType": "CreditDebit",
  "reason": "Customer request",
  "remarks": "Temporary block due to suspicious activity"
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
  "messageCode": 3531,
  "clientTxnId": "CBL-458",
  "accountNumber": "2000123hh",
  "statusType": "CreditDebit",
  "bankId": "123",
  "description": "Wallet status updated successfully",
  "responseMessage": "WALLET STATUS UPDATED SUCCESSFULLY"
}
```

## HTTP Status Codes

| Status Code | Description                              |
| ----------- | ---------------------------------------- |
| 200         | OK - Request processed successfully      |
| 400         | Bad Request - Invalid request parameters |
| 401         | Unauthorized - Authentication failed     |
| 404         | Not Found - Wallet/Account not found     |
| 500         | Internal Server Error                    |

## Error Codes

| Error Code | Description                        |
| ---------- | ---------------------------------- |
| 3531       | Wallet status updated successfully |
| 1010       | Invalid message code               |
| 1020       | Missing required parameters        |
| 1040       | Account not found                  |
| 3532       | Invalid status type                |
| 3533       | Status change not allowed          |