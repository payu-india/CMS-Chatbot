---
title: Statement Inquiry API - CLW
deprecated: false
hidden: true
metadata:
  title: Statement Inquiry API - CLW
  robots: index
---
The **Statement Inquiry** API allows you to retrieve wallet transaction details, including both financial and non-financial transactions, within a specific date range. This is useful for generating account statements and transaction history.

## Environment

| Environment | URL                                                                  |
| ----------- | -------------------------------------------------------------------- |
| Test        | `https://apitest.payu.in/loyalty-points/v1/wallet/statement-inquiry` |
| Production  | `https://api.payu.in/loyalty-points/v1/wallet/statement-inquiry`     |

**HTTP Method**: POST

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

<HTMLBlock>{`
<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Description</th>
            <th>Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>messageCode<br><code>mandatory</code></td>
            <td><code>Numeric(4)</code> API identifier for statement inquiry</td>
            <td>1072</td>
        </tr>
        <tr>
            <td>clientTxnId<br><code>mandatory</code></td>
            <td><code>String(100)</code> Unique identifier for this inquiry transaction</td>
            <td>StatementReq2023</td>
        </tr>
        <tr>
            <td>fromDate<br><code>mandatory</code></td>
            <td><code>String(10)</code> Start date of the statement period (DD/MM/YYYY format)</td>
            <td>01/07/2023</td>
        </tr>
        <tr>
            <td>toDate<br><code>mandatory</code></td>
            <td><code>String(10)</code> End date of the statement period (DD/MM/YYYY format)</td>
            <td>31/07/2023</td>
        </tr>
        <tr>
            <td>urn<br><code>mandatory</code></td>
            <td><code>Numeric(11)</code> Unique wallet reference number</td>
            <td>7000123456</td>
        </tr>
    </tbody>
</table>
`}</HTMLBlock>

## Response Parameters

| Parameter        | Description                                             | Example          |
| ---------------- | ------------------------------------------------------- | ---------------- |
| responseCode     | Response status code                                    | 00               |
| messageCode      | API response code                                       | 1073             |
| clientTxnId      | Echoes the request's clientTxnId                        | StatementReq2023 |
| urn              | Wallet reference number                                 | 7000123456       |
| availableBalance | Current balance in the wallet                           | 10000            |
| openingBalance   | Wallet balance at the beginning of the specified period | 5000             |
| closingBalance   | Wallet balance at the end of the specified period       | 15000            |
| statementDetails | Array of transaction details within the date range      | \[...]           |
| responseMessage  | Response message                                        | SUCCESS          |

### Statement Details Object

| Parameter         | Description                            | Example         |
| ----------------- | -------------------------------------- | --------------- |
| transactionId     | Unique transaction identifier          | TXN123456789    |
| transactionDate   | Date of transaction (DD/MM/YYYY)       | 15/07/2023      |
| transactionTime   | Time of transaction (HH:MM:SS)         | 14:30:25        |
| transactionType   | Type of transaction (CREDIT/DEBIT)     | CREDIT          |
| transactionAmount | Transaction amount in implied decimals | 5000            |
| availableBalance  | Balance after this transaction         | 10000           |
| merchantName      | Name of merchant or source             | Amazon          |
| description       | Transaction description                | Cashback reward |
| status            | Transaction status                     | SUCCESS         |
| referenceNumber   | Reference number for the transaction   | REF789012345    |

## Sample Request

### Encrypted Packet

```bash
curl --location --request POST 'https://apitest.payu.in/loyalty-points/v1/wallet/statement-inquiry' \
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
  "messageCode": "1072",
  "clientTxnId": "StatementReq2023",
  "fromDate": "01/07/2023",
  "toDate": "31/07/2023",
  "urn": "7000123456"
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
  "messageCode": 1073,
  "clientTxnId": "StatementReq2023",
  "urn": 7000123456,
  "availableBalance": 10000,
  "openingBalance": 5000,
  "closingBalance": 15000,
  "statementDetails": [
    {
      "transactionId": "TXN123456789",
      "transactionDate": "15/07/2023",
      "transactionTime": "14:30:25",
      "transactionType": "CREDIT",
      "transactionAmount": 5000,
      "availableBalance": 10000,
      "merchantName": "Amazon",
      "description": "Cashback reward",
      "status": "SUCCESS",
      "referenceNumber": "REF789012345"
    }
  ],
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

| Error Code | Description                  |
| ---------- | ---------------------------- |
| 1073       | Statement inquiry successful |
| 1010       | Invalid message code         |
| 1020       | Missing required parameters  |
| 1040       | Wallet not found             |
| 1074       | Invalid date range           |

## Transaction Types

| Type   | Description                    |
| ------ | ------------------------------ |
| CREDIT | Money added to the wallet      |
| DEBIT  | Money deducted from the wallet |

## Transaction Status Values

| Status    | Description                        |
| --------- | ---------------------------------- |
| SUCCESS   | Transaction completed successfully |
| FAILED    | Transaction failed                 |
| PENDING   | Transaction is still in progress   |
| CANCELLED | Transaction was cancelled          |

## Date Range Limitations

* Maximum date range: 90 days
* Date format: DD/MM/YYYY
* Both `fromDate` and `toDate` are inclusive
* Future dates are not allowed