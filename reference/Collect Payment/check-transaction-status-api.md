---
title: Check Transaction Status API
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
---
title: Omni Transaction Status Check API (Merchant)
excerpt: Check transaction status and retrieve comprehensive payment details for Dynamic Bharat QR (DBQR) and POS Card transactions.
deprecated: false
hidden: false
metadata:
  robots: index
---

## Overview

The **Omni Transaction Status Check API** is used by merchants using PayU's Omni product to check the real-time transaction status and retrieve payment details for transactions initiated via **Dynamic Bharat QR (DBQR)** and **Point of Sale (POS) Card** payments.

Merchants can use this server-to-server endpoint to verify transaction outcomes, reconcile payment records, and retrieve acquiring bank and terminal metadata.

---

## Environments & Endpoints

| Environment | Method | Endpoint URL |
| :--- | :--- | :--- |
| **Production** | `POST` | `https://info.payu.in/v1/transaction/?mode=bqr` |
| **Sandbox / Test** | `POST` | `<redacted URL>` |

---

## Request Headers

### Mandatory Headers

| Header | Description |
| :--- | :--- |
| mid | _String_<br>Merchant identifier (MID) used in the request header.<br>**Example:** `2` |
| Content-Type | _String_<br>Request payload content type. Must be set to `application/json`. |
| Info-Command | _String_<br>Name of the PayU information command. Pass `check_bqr_txn_status`. |
| authorization | _String_<br>HMAC authorization header generated using the merchant credentials and request date.<br>**Format:** `hmac username="<merchantKey>", algorithm="sha512", headers="date", signature="<signature>"` |
| date | _String_<br>Request timestamp formatted in GMT according to RFC 1123.<br>**Example:** `Thu, 16 Apr 2026 06:01:44 GMT` |

---

## Request Parameters

### Mandatory Parameters

| Parameter | Description |
| :--- | :--- |
| txnId | _Array of Strings_<br>Transaction ID list sent in the JSON request body. Pass one or more merchant transaction IDs in an array.<br>**Example:** `["b5f29799999987989990012345"]` |

---

## Sample Request

```bash cURL
curl --location 'https://info.payu.in/v1/transaction/?mode=bqr' \
--header 'mid: 2' \
--header 'Content-Type: application/json' \
--header 'Info-Command: check_bqr_txn_status' \
--header 'authorization: hmac username="<merchantKey>", algorithm="sha512", headers="date", signature="0742db17cbab1a1881a0ecbb2d950fb19b4da2a061acbb42c184e68d7a44bc2e0c78ad97b457f15fe7008f6b6b27d40cafd774da3d2b64d5159a918a58ceed74"' \
--header 'date: Thu, 16 Apr 2026 06:01:44 GMT' \
--data '{
    "txnId": ["b5f29799999987989990012345"]
}'
```

---

## Response Parameters

### Top-Level Parameters

| Parameter | Description |
| :--- | :--- |
| status | _Integer_<br>Status of the web service call:<br>• `1`: Web service call succeeded.<br>• `0`: Web service call failed. |
| message | _String_<br>Message returned by the API (e.g., `Success`). |
| result | _Array of Objects_<br>Encoded transaction and status details. Includes transaction status, merchant details, payment mode, amount, UTR or bank reference information, error details, and related transaction metadata. For more details, refer to the following tables|

### result Object Fields Description
#### Response Parameters for Dynamic Bharat QR (DBQR)

Returned inside `result[]` when `mode` is `DBQR`:

| Parameter | Description |
| :--- | :--- |
| txnId | _String_<br>Merchant transaction identifier. |
| mihpayId | _Number_ or _String_<br>Unique PayU reference identifier (PayU ID). |
| mode | _String_<br>Payment mode of the transaction. Returns `DBQR`. |
| status | _String_<br>Merchant-facing mapped payment status:<br>• `success`: Transaction completed successfully.<br>• `failure`: Transaction failed or declined.<br>• `pending`: QR code generated, awaiting customer payment. |
| unmappedStatus | _String_<br>Internal PayU status before merchant mapping (e.g., `captured`, `failed`, `in progress`, `initiated`, `dropped`). |
| bqrTxnStatusMessage | _String_<br>Status description message for the transaction (e.g., `Transaction is Successful`). |
| message | _String_<br>Per-transaction lookup message (e.g., `Found TxnId`, `Transaction is Successful`, `Transaction is Pending`). |
| errorCode | _String_<br>PayU error code (`E000` on success). |
| errorMessage | _String_<br>Human-readable error description for `errorCode` (`No Error` on success). |
| amount | _Number_<br>Transaction base amount payable. |
| originalAmount | _Number_<br>Original transaction amount before promotional or offer discounts. |
| additionalCharges | _Number_<br>Extra charges on top of base amount (e.g., convenience fees, surcharges). |
| discount | _Number_<br>Total promotional discount applied to the transaction. |
| instantDiscount | _Number_<br>Instant discount deducted during checkout. |
| netDebitAmount | _Number_<br>Net amount debited from customer: `originalAmount - discount + additionalCharges` (+ TCS if any). Returns `0` on non-successful transactions. |
| originalCurrency | _String_<br>Transaction currency code (default: `INR`). |
| bankcode | _String_<br>Payment option / scheme code. Returns `UPIDBQR`. |
| pgType | _String_<br>Payment gateway label formatted as `{mode}-PG`. Returns `DBQR-PG`. |
| bankReferenceNumber | _String_<br>Bank or acquirer reference for the payment (RRN / UTR at acquirer level). |
| productInfo | _String_<br>Product description provided for the QR transaction (e.g., `Offline Dynamic`, `UPI Payment for Order`). |
| addedOn | _String_<br>Transaction creation timestamp in PayU (`YYYY-MM-DD HH:MM:SS`). |
| merchantUTR | _String_<br>Settlement UTR credited to the merchant bank account. Returns `null` if not yet settled. |
| appName | _String_<br>UPI application used by the payer (e.g., `GooglePay`, `PhonePe`, `Paytm`). |
| surl | _String_<br>Success redirect URL sent in request payload. |
| furl | _String_<br>Failure redirect URL sent in request payload. |
| curl | _String_<br>Cancel redirect URL sent in request payload. |
| reverseHash | _String_<br>SHA-512 security hash generated by PayU for verifying response authenticity. |
| field0 | _String_<br>PayU reference / QR reference ID. |
| field1 | _String_<br>Customer name as registered on UPI. |
| field2 | _String_<br>Approval code from Bank. |
| field3 | _String_<br>Customer / Payer Virtual Payment Address (VPA). |
| field4 | _String_<br>Merchant Virtual Payment Address (VPA). |
| field5 | _String_<br>NPCI UPI transaction reference ID. |
| field6 | _String_<br>Multiple details about customer / payer in delimited format (`Account|Mobile|IFSC`). |
| field7 | _String_<br>UPI response code from Bank (e.g., `APPROVED OR COMPLETED SUCCESSFULLY|00`). |
| field8 | _String_<br>UPI transaction note. |
| field9 | _String_<br>Status trail (e.g., `success|Transaction success|Completed Using Callback`). |

#### Response Parameters for POS Card Payments

Returned inside `result[]` when `mode` is `POS`:

| Parameter | Description |
| :--- | :--- |
| txnId | _String_<br>Merchant transaction identifier. |
| mihpayId | _Number_ or _String_<br>Unique PayU reference identifier (PayU ID). |
| mode | _String_<br>Payment mode of the transaction. Returns `POS`. |
| status | _String_<br>Merchant-facing mapped payment status:<br>• `success`: Transaction authorized and captured on terminal.<br>• `failure`: Transaction declined or cancelled on terminal.<br>• `pending`: Transaction pushed to terminal, awaiting customer action. |
| unmappedStatus | _String_<br>Internal PayU status before merchant mapping (e.g., `captured`, `failed`, `in progress`, `initiated`, `dropped`). |
| bqrTxnStatusMessage | _String_<br>Status description message for the transaction (e.g., `Transaction is Successful`). |
| message | _String_<br>Per-transaction lookup message (e.g., `Found TxnId`, `Transaction is Successful`, `Transaction is Pending`). |
| errorCode | _String_<br>PayU error code (`E000` on success). |
| errorMessage | _String_<br>Human-readable error description for `errorCode` (`No Error` on success). |
| amount | _Number_<br>Transaction base amount payable. |
| originalAmount | _Number_<br>Original transaction amount before promotional or offer discounts. |
| additionalCharges | _Number_<br>Extra charges on top of base amount (e.g., convenience fees, tips, surcharges). |
| discount | _Number_<br>Total promotional discount applied to the transaction. |
| instantDiscount | _Number_<br>Instant discount deducted during checkout. |
| netDebitAmount | _Number_<br>Net amount debited from customer card: `originalAmount - discount + additionalCharges` (+ TCS if any). Returns `0` on non-successful transactions. |
| originalCurrency | _String_<br>Transaction currency code (default: `INR`). |
| bankcode | _String_<br>Payment option / scheme code as per the scheme of the card (e.g., `VISA`, `MAST`, `RUPAY`). |
| pgType | _String_<br>Payment gateway label formatted as `{mode}-PG`. Returns `POS-PG`. |
| bankReferenceNumber | _String_<br>Bank or acquirer reference for the payment (RRN / UTR at acquirer level). |
| productInfo | _String_<br>Product description configured for POS payments (e.g., `Non-Integrated POS`, `Integrated POS`). |
| addedOn | _String_<br>Transaction creation timestamp in PayU (`YYYY-MM-DD HH:MM:SS`). |
| merchantUTR | _String_<br>Settlement UTR credited to the merchant bank account. Returns `null` if not yet settled. |
| nameOnCard | _String_<br>Customer name as embossed on the card (e.g., `Navnath Gawade`). |
| cardNo | _String_<br>Masked card number (e.g., `XXXXXXXXXXXX1234`). |
| appName | _String_<br>Always returns `null` for POS card transactions. |
| surl | _String_<br>Success redirect URL sent in request payload. |
| furl | _String_<br>Failure redirect URL sent in request payload. |
| curl | _String_<br>Cancel redirect URL sent in request payload. |
| reverseHash | _String_<br>SHA-512 security hash generated by PayU for verifying response authenticity. |
| field0 | _String_<br>POS Device ID / Terminal ID (e.g., `TERM123456`). |
| field1 | _String_<br>Customer name on the card. |
| field2 | _String_<br>Authorization code from acquirer (e.g., `482911`). |
| field3 | _String_<br>Card mode and PIN verification indicator (e.g., `CTLESSEMV|false`). |
| field4 | _String_<br>Merchant mobile number and username in delimited format (`Mobile|Username`). |
| field5 | _String_<br>Acquirer Terminal ID (TID) (e.g., `28I01743`). |
| field6 | _String_<br>Empty string for POS card transactions. |
| field7 | _String_<br>Terminal status and response message on initiation or failure (e.g., `200|payment Initiated successfully`). |
| field8 | _String_<br>Empty string for POS card transactions. |
| field9 | _String_<br>Acquirer approval trail (e.g., `00|APPROVED|Transaction approved successfully`). |

---

## Sample Responses

### 1. Dynamic Bharat QR (DBQR) Response

```json
{
  "message": "Success",
  "status": 1,
  "result": [
    {
      "bqrTxnStatusMessage": "Transaction is Successful",
      "field0": "27447252485",
      "field1": "NAVNATH SAMBHAJI GAWADE",
      "field2": "359524",
      "field3": "navnathgawade99@okhdfcbank",
      "field4": "12096969ofdbqr.payu@indus",
      "field5": "PPPL27447252485250226175136699ee950",
      "field6": "50100330275312|8693817260|HDFC0001602",
      "field7": "APPROVED OR COMPLETED SUCCESSFULLY|00",
      "field8": "UPI Transaction",
      "field9": "success|Transaction success|Completed Using Callback",
      "instantDiscount": 0,
      "reverseHash": "278a47bf669e4e3a3957738e97c0b6668ad344536889e617976a7a1a051987561999db808fc087df0593dd3dd6882d4e4e72b696e257c5c309a615b9cc02ce4b",
      "curl": "<redacted URL>",
      "furl": "<redacted URL>",
      "surl": "<redacted URL>",
      "mihpayId": 27447252485,
      "bankReferenceNumber": "119144221818",
      "amount": 1,
      "mode": "DBQR",
      "originalAmount": 1,
      "additionalCharges": 0,
      "discount": 0,
      "netDebitAmount": 1,
      "productInfo": "UPI Payment for Order",
      "bankcode": "UPIDBQR",
      "errorCode": "E000",
      "errorMessage": "No Error",
      "addedOn": "2026-02-25 17:51:36",
      "pgType": "DBQR-PG",
      "status": "success",
      "unmappedStatus": "captured",
      "merchantUTR": null,
      "appName": "GooglePay",
      "originalCurrency": "INR",
      "message": "Found TxnId",
      "txnId": "b5f29799999987989990012345"
    }
  ]
}
```

### 2. POS Card Payment Response

```json
{
  "status": 1,
  "message": "Success",
  "result": [
    {
      "bqrTxnStatusMessage": "Transaction is Successful",
      "message": "Found TxnId",
      "txnId": "POS20260416001",
      "mihpayId": 28500123456,
      "status": "success",
      "unmappedStatus": "captured",
      "errorCode": "E000",
      "errorMessage": "No Error",
      "mode": "POS",
      "bankcode": "VISA",
      "pgType": "POS-PG",
      "amount": 1500,
      "originalAmount": 1500,
      "additionalCharges": 0,
      "discount": 0,
      "netDebitAmount": 1500,
      "originalCurrency": "INR",
      "bankReferenceNumber": "987654321098",
      "productInfo": "Integrated POS",
      "addedOn": "2026-04-16 10:30:00",
      "merchantUTR": null,
      "field0": "TERM123456",
      "field1": "Navnath Gawade",
      "field2": "482911",
      "field3": "CTLESSEMV|false",
      "field4": "9876543210|store_manager",
      "field5": "28I01743",
      "field6": "",
      "field7": "200|payment Initiated successfully",
      "field8": "",
      "field9": "00|APPROVED|Transaction approved successfully",
      "nameOnCard": "Navnath Gawade",
      "cardNo": "XXXXXXXXXXXX1234",
      "appName": null,
      "surl": "<redacted URL>",
      "furl": "<redacted URL>",
      "curl": "<redacted URL>",
      "reverseHash": "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"
    }
  ]
}
```
