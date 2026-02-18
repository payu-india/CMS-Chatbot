---
name: V2_payment_result_JSON_Object
---
| Field               | Description                                                                              | Example (from your response)  |
| ------------------- | ---------------------------------------------------------------------------------------- | ----------------------------- |
| mihpayId            | Unique transaction ID assigned by PayU. Use for future reference, inquiry, or refund.    | `21612493009`                 |
| bankReferenceNumber | Bank reference number for the transaction (provided by bank on success).                 | `"2411194544"`                |
| amount              | Actual amount involved in the transaction.                                               | `10.00`                       |
| mode                | Payment mode used (e.g. CC = Credit Card, DC, UPI, NB).                                  | `"CC"`                        |
| requestId           | Unique identifier for the request (e.g. for refund or other follow-up requests).         | `""`                          |
| originalAmount      | Original transaction amount before any additional charges or discounts.                  | `10.00`                       |
| additionalCharges   | Any additional charges applied to the transaction.                                       | `0.00`                        |
| discount            | Discount amount applied to the transaction.                                              | `0.00`                        |
| netDebitAmount      | Total amount debited from the payer’s account after additional charges and discounts.    | `10.00`                       |
| productInfo         | Short description of the product or service for which the payment was made.              | `"Test Product"`              |
| firstName           | Payer’s first name.                                                                      | `"John"`                      |
| bankcode            | Code of the bank or payment instrument used (e.g. VISA, MAST, AMEX).                     | `"VISA"`                      |
| nameOnCard          | Cardholder name; `null` if not captured.                                                 | `null`                        |
| cardNo              | Masked card number.                                                                      | `"XXXXXXXXXXXX1234"`          |
| cardType            | Type of card (e.g. VISA, MAST, AMEX).                                                    | `"VISA"`                      |
| udf1 – udf5         | User-defined fields for optional merchant data.                                          | `null` (all)                  |
| field2              | Context-specific information from the bank (e.g. codes or values used for verification). | `"140455"`                    |
| field9              | Transaction status or message from the bank/gateway.                                     | `"Transaction is Successful"` |
| errorCode           | Error code; `E000` typically means no error.                                             | `"E000"`                      |
| errorMessage        | Human-readable error message; “No Error” when successful.                                | `"No Error"`                  |
| addedOn             | Timestamp when the transaction was initiated.                                            | `"2024-11-19 21:17:55"`       |
| settledAt           | Timestamp when funds were settled; `0000-00-00 00:00:00` if not yet settled.             | `"0000-00-00 00:00:00"`       |
| paymentSource       | Source/channel of payment (e.g. WEB, payuS2S, express).                                  | `"WEB"`                       |
| pgType              | Payment gateway type (e.g. CC-PG for card, UPI-PG for UPI).                              | `"CC-PG"`                     |
| status              | Overall transaction status (e.g. success, failure, pending).                             | `"success"`                   |
| unmappedStatus      | Internal PayU status (e.g. captured, failed, auth, pending).                             | `"captured"`                  |
| merchantUTR         | Merchant’s Unique Transaction Reference; `null` if not provided.                         | `null`                        |
| rupayAuthRefNo      | RuPay-specific authorization reference; `null` for non-RuPay.                            | `null`                        |
| authRefNo           | Bank/gateway authorization reference number.                                             | `"123456789"`                 |
| threeDSVersion      | Version of 3D Secure used (e.g. 2.2.0).                                                  | `"2.2.0"`                     |
| message             | General status or result message (e.g. “Found TxnId”).                                   | `"Found TxnId"`               |
| txnId               | Merchant-provided transaction/order ID used for tracking.                                | `"b5f2d8785768087678fm9"`     |
