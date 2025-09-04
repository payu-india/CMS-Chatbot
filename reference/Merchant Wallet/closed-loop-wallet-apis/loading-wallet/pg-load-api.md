---
title: PG Load API
deprecated: false
hidden: false
metadata:
  robots: index
---
The \*\*PG Load \*\*API allows you to create a credit transaction entry directly into the wallet without going through a payment gateway. This is useful for scenarios like cashback, rewards, or direct fund transfers.

## Environment

| Environment | URL                                                             |
| ----------- | --------------------------------------------------------------- |
| Test        | `https://apitest.payu.in/loyalty-points/v1/wallet/load-account` |
| Production  | `https://api.payu.in/loyalty-points/v1/wallet/load-account`     |

**HTTP Method**: PATCH

## Request Headers

<Closed_Loop_HMAC />

## Request Parameters

### Body Parameters

The request body contains both encrypted and decrypted parameters.

#### Encrypted

| Parameter                         | Description                                                                                    |
| --------------------------------- | ---------------------------------------------------------------------------------------------- |
| token<br /><code>mandatory</code> | <code>String</code> AES-192-CBC encrypted request body containing all the decrypted parameters |

#### Decrypted

| Parameter                                     | Description                                                                              | Example          |
| --------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------- |
| messageCode<br /><code>mandatory</code>       | <code>Numeric(4)</code> Load card request type code                                      | 1080             |
| clientTxnId<br /><code>mandatory</code>       | <code>Alphanumeric(14)</code> Unique transaction ID for this request                     | Reload\_V3\_1234 |
| requestDateTime<br /><code>mandatory</code>   | <code>Numeric(14)</code> Timestamp of the transaction (YYYYMMDDHHMMSS format)            | 20230822183015   |
| customerMobile<br /><code>conditional</code>  | <code>Numeric(13)</code> Customer's mobile number with country code                      | 919988776655     |
| urn<br /><code>conditional</code>             | <code>Numeric(11)</code> Unique wallet reference number generated during wallet creation | 70000000008      |
| transactionAmount<br /><code>mandatory</code> | <code>Numeric(12)</code> Amount to load (expressed in implied decimals)                  | 1500             |
| sourceType<br /><code>mandatory</code>        | <code>Numeric(2)</code> Source of funding (0 = Wallet, 1 = Account)                      | 1                |
| sender<br /><code>mandatory</code>            | <code>String(100)</code> Name identifying the funding source                             | Amazon           |
| fundFlowType<br /><code>mandatory</code>      | <code>String(20)</code> Type of fund flow (I = Inward, O = Outward)                      | I                |
| implId<br /><code>mandatory</code>            | <code>String(100)</code> Implementing identifier matching a mapped configuration         | I\|70190         |
| implType<br /><code>mandatory</code>          | <code>String(100)</code> Implementation type                                             | PG\_W2A\_I       |

> **Note**: Either `customerMobile` or `urn` must be provided.

## Response Parameters

| Parameter           | Description                                   | Example          |
| ------------------- | --------------------------------------------- | ---------------- |
| responseCode        | Response status code                          | 00               |
| messageCode         | Code indicating the load transaction's result | 1081             |
| clientTxnId         | Echoes the request's clientTxnId              | Reload\_V3\_1234 |
| urn                 | Wallet reference number                       | 1000019          |
| accosaTransactionId | Internal transaction ID for this load         | 1234567890       |
| accosaRefNo         | System-generated reference sequence           | 20230822001      |
| availableBalance    | Updated wallet balance after the transaction  | 1500             |
| responseMessage     | Response message                              | SUCCESS          |

## Sample Request

### Encrypted Packet

```bash
curl --location --request PATCH 'https://apitest.payu.in/loyalty-points/v1/wallet/load-account' \
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
  "messageCode": "1080",
  "clientTxnId": "Reload_V3_1234",
  "requestDateTime": "20230822183015",
  "urn": 70000000008,
  "transactionAmount": 1500,
  "sourceType": 1,
  "sender": "Amazon",
  "fundFlowType": "I",
  "implId": "I|70190",
  "implType": "PG_W2A_I"
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
  "messageCode": 1081,
  "clientTxnId": "Reload_V3_1234",
  "urn": 1000019,
  "accosaTransactionId": 1234567890,
  "accosaRefNo": 20230822001,
  "availableBalance": 1500,
  "responseMessage": "SUCCESS"
}
```

## HTTP Status Codes

| Status Code | Description                              |
| ----------- | ---------------------------------------- |
| 200         | OK - Request processed successfully      |
| 400         | Bad Request - Invalid request parameters |
| 401         | Unauthorized - Authentication failed     |
| 404         | Not Found - Wallet not found             |
| 500         | Internal Server Error                    |

## Error Codes

| Error Code | Description                 |
| ---------- | --------------------------- |
| 1081       | Load transaction successful |
| 1010       | Invalid message code        |
| 1020       | Missing required parameters |
| 1040       | Wallet not found            |
| 1050       | Transaction limit exceeded  |