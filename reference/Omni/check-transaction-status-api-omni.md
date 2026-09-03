---
title: Check Transaction Status API - Omni
deprecated: false
hidden: true
metadata:
  robots: index
---
The Check Transaction Status API allows merchants to query the status and retrieve complete details of transactions initiated via the PayU Omni Integrated Flow. This API is essential for payment verification and reconciliation.

***

## Endpoint

**HTTP Method:** `POST`

**URL:** `/v1/transaction/?mode=bqr`

**Content-Type:** `application/json`

**Info-Command:** `check_bqr_txn_status` (required header)

***

## Environment URLs

| Environment | URL                                             |
| ----------- | ----------------------------------------------- |
| Production  | `https://info.payu.in/v1/transaction/?mode=bqr` |

<Warning>
⚠️ **Info Gap:** Test/sandbox environment URL not documented. Contact PayU support for test endpoint details.
</Warning>

***

## Sample Request

### cURL

```bash
curl --location 'https://info.payu.in/v1/transaction/?mode=bqr' \
--header 'mid: merchant_12345' \
--header 'Content-Type: application/json' \
--header 'Info-Command: check_bqr_txn_status' \
--header 'date: Tue, 15 Nov 2023 08:12:31 GMT' \
--header 'authorization: hmac username="your_merchant_key", algorithm="sha512", headers="date", signature="a1b2c3d4e5f6..."' \
--data '{
  "txnId": ["ORD_20231115_001", "ORD_20231115_002"]
}'
```

> **Note:** Replace all placeholder values with your actual credentials.

### Python

```python
import requests
import json

url = "https://info.payu.in/v1/transaction/?mode=bqr"

headers = {
    "mid": "merchant_12345",
    "Content-Type": "application/json",
    "Info-Command": "check_bqr_txn_status",
    "date": "Tue, 15 Nov 2023 08:12:31 GMT",
    "authorization": "hmac username=\"your_merchant_key\", algorithm=\"sha512\", headers=\"date\", signature=\"a1b2c3d4e5f6...\""
}

payload = {
    "txnId": ["ORD_20231115_001", "ORD_20231115_002"]
}

try:
    response = requests.post(url, headers=headers, json=payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {str(e)}")
```

### PHP

```php
<?php
$url = "https://info.payu.in/v1/transaction/?mode=bqr";

$headers = [
    "mid: merchant_12345",
    "Content-Type: application/json",
    "Info-Command: check_bqr_txn_status",
    "date: Tue, 15 Nov 2023 08:12:31 GMT",
    "authorization: hmac username=\"your_merchant_key\", algorithm=\"sha512\", headers=\"date\", signature=\"a1b2c3d4e5f6...\""
];

$payload = json_encode([
    "txnId" => ["ORD_20231115_001", "ORD_20231115_002"]
]);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

curl_close($ch);

echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";
?>
```

### Java

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class CheckTransactionStatus {
    public static void main(String[] args) throws Exception {
        String url = "https://info.payu.in/v1/transaction/?mode=bqr";
        
        String payload = """
        {
          "txnId": ["ORD_20231115_001", "ORD_20231115_002"]
        }
        """;

        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("mid", "merchant_12345")
            .header("Content-Type", "application/json")
            .header("Info-Command", "check_bqr_txn_status")
            .header("date", "Tue, 15 Nov 2023 08:12:31 GMT")
            .header("authorization", "hmac username=\"your_merchant_key\", algorithm=\"sha512\", headers=\"date\", signature=\"a1b2c3d4e5f6...\"")
            .POST(HttpRequest.BodyPublishers.ofString(payload))
            .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response: " + response.body());
    }
}
```

### JavaScript

```javascript
const url = "https://info.payu.in/v1/transaction/?mode=bqr";

const headers = {
    "mid": "merchant_12345",
    "Content-Type": "application/json",
    "Info-Command": "check_bqr_txn_status",
    "date": "Tue, 15 Nov 2023 08:12:31 GMT",
    "authorization": "hmac username=\"your_merchant_key\", algorithm=\"sha512\", headers=\"date\", signature=\"a1b2c3d4e5f6...\""
};

const payload = {
    "txnId": ["ORD_20231115_001", "ORD_20231115_002"]
};

async function checkStatus() {
    try {
        const response = await fetch(url, {
            method: "POST",
            headers: headers,
            body: JSON.stringify(payload)
        });
        
        const data = await response.json();
        console.log("Status Code:", response.status);
        console.log("Response:", data);
    } catch (error) {
        console.error("Error:", error);
    }
}

checkStatus();
```

***

## Sample Response

### Success Response - DBQR/UPI Payment

```json
{
  "status": 1,
  "message": "Success",
  "result": [
    {
      "txnId": "ORD_20231115_001",
      "mihpayId": "403993715534895620",
      "bankReferenceNumber": "332116831375",
      "amount": "1500.00",
      "mode": "DBQR",
      "originalAmount": "1500.00",
      "additionalCharges": "0.00",
      "discount": "0.00",
      "netDebitAmount": "1500.00",
      "productInfo": "Coffee and Pastry",
      "bankcode": "DBQR",
      "errorCode": "E000",
      "errorMessage": "No Error",
      "addedOn": "2023-11-15 08:15:23",
      "pgType": "DBQR-PG",
      "merchantUTR": "332116831375",
      "originalCurrency": "INR",
      "message": "SUCCESS",
      "bqrTxnStatusMessage": "Transaction Successful",
      "status": "success",
      "unmappedStatus": "captured",
      "field0": "b5f29799-9999-8798-9990-012345678901",
      "field1": "Table 5",
      "field2": "Server: John",
      "field6": "success@payu",
      "field7": "OmniPOS_DBQR",
      "field9": "DBQR",
      "reverseHash": "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
      "omniChannelDetails": {
        "posDeviceId": "DEVICE_POS_12345",
        "posPaymentMethod": "qr"
      }
    }
  ]
}
```

### Success Response - Card Payment

```json
{
  "status": 1,
  "message": "Success",
  "result": [
    {
      "txnId": "ORD_20231115_002",
      "mihpayId": "403993715534895621",
      "bankReferenceNumber": "332116831376",
      "amount": "2500.00",
      "mode": "CARD",
      "originalAmount": "2500.00",
      "additionalCharges": "0.00",
      "discount": "0.00",
      "netDebitAmount": "2500.00",
      "productInfo": "Dinner for Two",
      "bankcode": "VISA",
      "errorCode": "E000",
      "errorMessage": "No Error",
      "addedOn": "2023-11-15 09:20:45",
      "pgType": "CARD-PG",
      "merchantUTR": "332116831376",
      "originalCurrency": "INR",
      "message": "SUCCESS",
      "bqrTxnStatusMessage": "Transaction Successful",
      "status": "success",
      "unmappedStatus": "captured",
      "nameOnCard": "JOHN DOE",
      "cardNo": "XXXXXXXXXXXX1234",
      "field1": "Table 8",
      "field5": "JOHN DOE",
      "field6": "success@payu",
      "field7": "CARD",
      "field8": "XXXXXXXXXXXX1234",
      "field9": "VISA",
      "reverseHash": "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
      "omniChannelDetails": {
        "posDeviceId": "DEVICE_POS_12345",
        "posPaymentMethod": "sale"
      }
    }
  ]
}
```

### Failure Response

```json
{
  "status": 1,
  "message": "Success",
  "result": [
    {
      "txnId": "ORD_20231115_003",
      "mihpayId": "403993715534895622",
      "bankReferenceNumber": "",
      "amount": "500.00",
      "mode": "DBQR",
      "originalAmount": "500.00",
      "additionalCharges": "0.00",
      "discount": "0.00",
      "netDebitAmount": "500.00",
      "productInfo": "Test Order",
      "bankcode": "DBQR",
      "errorCode": "E001",
      "errorMessage": "Transaction failed",
      "addedOn": "2023-11-15 10:05:12",
      "pgType": "DBQR-PG",
      "merchantUTR": "",
      "originalCurrency": "INR",
      "message": "FAILED",
      "bqrTxnStatusMessage": "Transaction Failed",
      "status": "failed",
      "unmappedStatus": "failed",
      "reverseHash": ""
    }
  ]
}
```

***

## Request Headers

| Parameter       | Type   | Description                                                                                                                            | Example                                                                                              |
| :-------------- | :----- | :------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------- |
| `mid`           | String | Merchant identifier provided by PayU                                                                                                   | `merchant_12345`                                                                                     |
| `Content-Type`  | String | Must be `application/json`                                                                                                             | `application/json`                                                                                   |
| `Info-Command`  | String | Must be `check_bqr_txn_status`                                                                                                         | `check_bqr_txn_status`                                                                               |
| `date`          | String | Current request date and time in GMT format (RFC 7231)                                                                                 | `Tue, 15 Nov 2023 08:12:31 GMT`                                                                      |
| `authorization` | String | HMAC-SHA512 signature header. Format: `hmac username="<merchantKey>", algorithm="sha512", headers="date", signature="<hex-signature>"` | `hmac username="your_merchant_key", algorithm="sha512", headers="date", signature="a1b2c3d4e5f6..."` |

<Info>
**HMAC Signature Generation:**
1. Use your merchant key (not `mid`) as username
2. Use your merchant salt to compute HMAC-SHA512 hash
3. Hash the exact value of the `date` header
4. Output as lowercase hexadecimal
5. Format: `hmac username="<merchantKey>", algorithm="sha512", headers="date", signature="<hex>"`
</Info>

***

## Request Parameters

| Parameter | Type             | Description                                                                                                                   | Example                                    |
| :-------- | :--------------- | :---------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------- |
| `txnId`   | Array of Strings | Array of transaction IDs to check status for. You can query multiple transactions in a single request (up to 10 recommended). | `["ORD_20231115_001", "ORD_20231115_002"]` |

***

## Response Schema

### Top-Level Fields

| Field     | Type    | Description                                            | Example          |
| :-------- | :------ | :----------------------------------------------------- | :--------------- |
| `status`  | Integer | Web service call status. `1` = success, `0` = failure  | `1`              |
| `message` | String  | Human-readable message                                 | `Success`        |
| `result`  | Array   | Array of transaction objects (one per queried `txnId`) | `[{...}, {...}]` |

### Transaction Object (result\[])

| Field                 | Type   | Description                                                                           | Example                  |
| :-------------------- | :----- | :------------------------------------------------------------------------------------ | :----------------------- |
| `txnId`               | String | Your transaction ID                                                                   | `ORD_20231115_001`       |
| `mihpayId`            | String | PayU's unique transaction ID                                                          | `403993715534895620`     |
| `bankReferenceNumber` | String | Bank reference number (empty if failed)                                               | `332116831375`           |
| `amount`              | String | Transaction amount                                                                    | `1500.00`                |
| `mode`                | String | Payment mode: `DBQR`, `CARD`                                                          | `DBQR`                   |
| `originalAmount`      | String | Original amount before discounts/charges                                              | `1500.00`                |
| `additionalCharges`   | String | Additional charges if any                                                             | `0.00`                   |
| `discount`            | String | Discount applied                                                                      | `0.00`                   |
| `netDebitAmount`      | String | Net amount debited from customer                                                      | `1500.00`                |
| `productInfo`         | String | Product/service description                                                           | `Coffee and Pastry`      |
| `bankcode`            | String | Bank/payment code: `DBQR`, `VISA`, `MASTERCARD`, `RUPAY`                              | `DBQR`                   |
| `errorCode`           | String | Error code. `E000` = success                                                          | `E000`                   |
| `errorMessage`        | String | Error message. `No Error` = success                                                   | `No Error`               |
| `addedOn`             | String | Transaction creation timestamp                                                        | `2023-11-15 08:15:23`    |
| `pgType`              | String | Payment gateway type                                                                  | `DBQR-PG`                |
| `merchantUTR`         | String | Merchant UTR (bank reference)                                                         | `332116831375`           |
| `originalCurrency`    | String | Currency code                                                                         | `INR`                    |
| `message`             | String | Transaction result message                                                            | `SUCCESS`                |
| `bqrTxnStatusMessage` | String | Human-readable status message                                                         | `Transaction Successful` |
| `status`              | String | **Merchant-facing status:** `success`, `failure`, `pending`                           | `success`                |
| `unmappedStatus`      | String | **Internal PayU status:** `captured`, `failed`, `in progress`, `initiated`, `dropped` | `captured`               |
| `nameOnCard`          | String | Cardholder name (Card mode only)                                                      | `JOHN DOE`               |
| `cardNo`              | String | Masked card number (Card mode only)                                                   | `XXXXXXXXXXXX1234`       |
| `field0` - `field9`   | String | Mode-specific fields (see Field Mapping section)                                      | Various                  |
| `reverseHash`         | String | HMAC hash for response verification                                                   | `abcdef123...`           |
| `omniChannelDetails`  | Object | Omni device details                                                                   | `{...}`                  |

### omniChannelDetails Object

| Field              | Type   | Description                                       | Example            |
| :----------------- | :----- | :------------------------------------------------ | :----------------- |
| `posDeviceId`      | String | Device ID where payment was accepted              | `DEVICE_POS_12345` |
| `posPaymentMethod` | String | Payment method used: `sale` (card) or `qr` (DBQR) | `qr`               |

***

## Field Mapping: field0 - field9

The `field0` through `field9` fields contain different data depending on the payment mode.

### DBQR/UPI Mode

| Field               | Contains                              | Example                                |
| ------------------- | ------------------------------------- | -------------------------------------- |
| `field0`            | UPI Transaction ID                    | `b5f29799-9999-8798-9990-012345678901` |
| `field1`            | Custom UDF1 (from `printInfo.field1`) | `Table 5`                              |
| `field2`            | Custom UDF2 (from `printInfo.field2`) | `Server: John`                         |
| `field3` - `field5` | Custom UDF3-5 (from `printInfo`)      | (as provided)                          |
| `field6`            | UPI VPA (customer's UPI ID)           | `success@payu`                         |
| `field7`            | Payment flow type                     | `OmniPOS_DBQR`                         |
| `field8`            | Reserved                              | (empty)                                |
| `field9`            | Payment mode                          | `DBQR`                                 |

### Card/POS Mode

| Field               | Contains                         | Example                       |
| ------------------- | -------------------------------- | ----------------------------- |
| `field0`            | (Empty)                          |                               |
| `field1` - `field4` | Custom UDF1-4 (from `printInfo`) | `Table 8`                     |
| `field5`            | Cardholder name                  | `JOHN DOE`                    |
| `field6`            | Callback URL used                | `success@payu`                |
| `field7`            | Payment mode                     | `CARD`                        |
| `field8`            | Masked card number               | `XXXXXXXXXXXX1234`            |
| `field9`            | Card network                     | `VISA`, `MASTERCARD`, `RUPAY` |

<Info>
**Parsing Custom Fields:**
- Always check the `mode` field first (`DBQR` or `CARD`)
- Then extract the relevant fields based on the mode
- Custom fields (`field1`-`field4` or `field1`-`field5`) contain data you passed in `printInfo` during payment initiation
</Info>

***

## Transaction Status Values

### Merchant-Facing Status (`status` field)

| Value     | Meaning                        | Action Required                                                  |
| :-------- | :----------------------------- | :--------------------------------------------------------------- |
| `success` | Payment completed successfully | Mark order as paid. Deliver goods/services.                      |
| `failed`  | Payment failed                 | Do NOT mark as paid. Inform customer of failure.                 |
| `pending` | Payment still processing       | Poll the API again after 10-15 seconds. Do not mark as paid yet. |

### Internal PayU Status (`unmappedStatus` field)

| Value         | Meaning                             | Typical Mapping       |
| :------------ | :---------------------------------- | :-------------------- |
| `captured`    | Funds captured by PayU              | → `status: "success"` |
| `failed`      | Payment failed at bank/network      | → `status: "failed"`  |
| `in progress` | Payment processing in progress      | → `status: "pending"` |
| `initiated`   | Payment initiated but not completed | → `status: "pending"` |
| `dropped`     | Payment dropped/abandoned           | → `status: "failed"`  |

<Warning>
⚠️ **Only mark an order as paid if:**
- `status == "success"` **AND**
- `unmappedStatus == "captured"` **AND**
- `errorCode == "E000"` **AND**
- Reverse hash verification passes (if implemented)
</Warning>

***

## Error Codes

| Code       | Meaning                           | Status               | Action Required                                                 |
| :--------- | :-------------------------------- | :------------------- | :-------------------------------------------------------------- |
| `E000`     | No Error - Transaction successful | `success`            | Mark order as paid                                              |
| `E001`     | Transaction failed                | `failed`             | Do not mark as paid. Inform customer.                           |
| _(Others)_ | Various failure reasons           | `failed` / `pending` | Log the error. Contact PayU support if repeated failures occur. |

<Info>
⚠️ **Info Gap:** Full error code enumeration not documented. `E000` indicates success; any other code indicates an issue. Contact PayU support for a complete error code reference.
</Info>

***

## Reverse Hash Verification

The `reverseHash` field allows you to verify the integrity of the response. This is a security best practice.

<Warning>
⚠️ **Info Gap:** The exact reverse hash computation formula is not documented in the provided PDFs. Contact PayU support for the reverse hash generation sequence.

**Typical formula for PayU APIs:**
```
reverseHash = sha512(merchantSalt|status|...|txnId|...|amount|productInfo)
```
</Warning>

**Verification Steps:**

1. Extract response fields in the correct sequence (obtain from PayU docs)
2. Concatenate with `|` separator, prepending merchant salt
3. Compute SHA512 hash
4. Compare (case-insensitive) with the `reverseHash` field in the response
5. If mismatch, reject the response (potential tampering)

**Example (Pseudocode):**

```python
import hashlib

# Extract fields
status = result['status']
txnId = result['txnId']
amount = result['amount']
productInfo = result['productInfo']
reverseHash = result['reverseHash']

# Build hash string (verify sequence with PayU)
hash_string = f"{merchant_salt}|{status}|{txnId}|{amount}|{productInfo}"

# Compute SHA512
computed_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest()

# Compare
if computed_hash.lower() == reverseHash.lower():
    print("✅ Response verified")
else:
    print("❌ Hash mismatch - do not trust response")
```

***

## Polling Best Practices

If a transaction is in `pending` status, implement polling logic:

1. **Initial Poll:** Call immediately after receiving the webhook
2. **Retry Interval:** Wait 10-15 seconds between subsequent polls
3. **Max Retries:** Stop after 5 minutes (20 polls at 15-second intervals)
4. **Exponential Backoff (Optional):** Increase wait time after each poll (15s → 30s → 60s)
5. **Terminal States:** Stop polling when `status` becomes `success` or `failed`

<Warning>
⚠️ **Info Gap:** Official polling interval and timeout recommendations not documented. Contact PayU support for rate limits and recommended polling strategy.
</Warning>

***

## Related Resources

- [Initiate Payment API Reference](#initiate-payment-api)
- [Integration Guide — Check Transaction Status](#integrate-payu-omni-check-transaction-status)
- [PayU Omni Overview](#payu-omni-integrated-flow)
