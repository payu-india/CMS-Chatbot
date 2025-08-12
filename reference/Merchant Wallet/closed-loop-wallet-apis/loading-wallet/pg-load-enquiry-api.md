---
title: PG Load Enquiry API
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Load Enquiry** API allows you to check the status of a wallet load transaction that was initiated using the PG Load API. This is essential for transaction reconciliation and status verification.

## Environment

| Environment | URL                                                                     |
| ----------- | ----------------------------------------------------------------------- |
| Test        | `https://apitest.payu.in/loyalty-points/ppi/payment/pg-load/enquiry/v1` |
| Production  | `https://api.payu.in/loyalty-points/ppi/payment/pg-load/enquiry/v1`     |

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

| Parameter                               | Description                                                                   | Example      |
| --------------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| clientTxnId<br /><code>mandatory</code> | <code>Alphanumeric(100)</code> Unique transaction ID from the PG Load request | PGLOAD123456 |

## Response Parameters

| Parameter                    | Description                                      | Example                |
| ---------------------------- | ------------------------------------------------ | ---------------------- |
| merchantCode                 | Merchant's unique ID provided by PayU            | 180012                 |
| clientTxnId                  | Echoes the client's transaction ID               | PGLOAD123456           |
| txnAmount                    | The amount intended to be loaded into the wallet | 4100                   |
| accosaRefNo                  | Auto-generated sequence number                   | ACC123456789           |
| status                       | Transaction status                               | SUCCESS/FAILED/PENDING |
| responseCode                 | Numeric response code                            | 00                     |
| refundTxnExist               | Indicates if the transaction was refunded        | false                  |
| VerifyPaymentResponse.msg    | Message related to the status                    | Transaction successful |
| VerifyPaymentResponse.result | Status result from payment gateway               | 1                      |

## Sample Request

### Encrypted Packet

```bash
curl --location --request POST 'https://apitest.payu.in/loyalty-points/ppi/payment/pg-load/enquiry/v1' \
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
  "clientTxnId": "PGLOAD123456"
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

#### Successful Transaction

```json
{
  "merchantCode": "180012",
  "clientTxnId": "PGLOAD123456",
  "txnAmount": "4100",
  "accosaRefNo": "ACC123456789",
  "status": "SUCCESS",
  "responseCode": "00",
  "refundTxnExist": false,
  "VerifyPaymentResponse": {
    "msg": "Transaction successful",
    "result": "1"
  }
}
```

#### Failed Transaction

```json
{
  "merchantCode": "180012",
  "clientTxnId": "PGLOAD56894",
  "txnAmount": "4100",
  "status": "FAILED",
  "responseCode": "1303",
  "refundTxnExist": false,
  "refundEnquiryResponse": null
}
```

## HTTP Status Codes

| Status Code | Description                              |
| ----------- | ---------------------------------------- |
| 200         | OK - Request processed successfully      |
| 400         | Bad Request - Invalid request parameters |
| 401         | Unauthorized - Authentication failed     |
| 404         | Not Found - Transaction not found        |
| 500         | Internal Server Error                    |

## Error Codes

| Error Code | Description                 |
| ---------- | --------------------------- |
| 00         | Success                     |
| 1054       | Transaction not found       |
| 1303       | Transaction failed          |
| 1010       | Invalid message code        |
| 1020       | Missing required parameters |