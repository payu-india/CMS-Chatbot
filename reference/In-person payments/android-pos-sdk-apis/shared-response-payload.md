---
title: Shared Response Payload
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Some of the APIs of the POS SDK shares common response parameters. This topic contains such parameters. However, to obtain a clear understanding of each APIs, it is recommended to read the corresponding documentation.

## ICCTransactionResponse

| Parameter            | Description                                               | Example                                |
| :------------------- | :-------------------------------------------------------- | :------------------------------------- |
| Transaction Response | `object` Returns the list of transaction response object. | Refer \<\<TransactionResponse>> table. |
| Response             | `object` Returns the list of response object.             | Refer \<\<Response>> table.            |
|                      |                                                           |                                        |

## TransactionResponse fields description

| Parameter          | Description                                                                       | Example         |
| :----------------- | :-------------------------------------------------------------------------------- | :-------------- |
| Reference number   | `string` Returns the transaction reference number.                                | 859451235845123 |
| Amount             | `double` Returns the transaction Amount.                                          | 200.00          |
| Authorized Amount  | `double` Returns the Cashback amount or tip amount.                               | 12.00           |
| RRN                | `string` Returns the receipt reference number after the transaction is completed. | d054d           |
| Transaction status | `string` Returns the status of that transaction.                                  | Approved        |

## Response

| Parameter        | Description                                | Example                |
| :--------------- | :----------------------------------------- | :--------------------- |
| Date             | `string` The date of the transaction.      | 03/08/2017             |
| Time             | `string` The time of transaction.          | 11:5:2                 |
| Response Code    | `string` The transaction response code.    | “200”                  |
| Response Message | `string` The transaction response message. | “Transaction Approved” |

## TransactionStatusResponse

| Parameter           | Description                      | Sample                                    |
| :------------------ | :------------------------------- | :---------------------------------------- |
| TransactionResponse | `object` The transaction details | Refer \<\<ICCTransactionResponse>> table. |
| Response            | `object` The payment details     | Refer \<\<Response>> Table.               |

## Acquirer banks

| Parameter | Description                               | Sample                |
| :-------- | :---------------------------------------- | :-------------------- |
| EMI       | list Returns a list of \<\<EMI>> objects. | Refer \<\<EMI>> table |

## EMI

| Parameter     | Description                                                                           | Example   |
| :------------ | :------------------------------------------------------------------------------------ | :-------- |
| acquirerId    | `long` The bank id.                                                                   | 0         |
| minBankAmount | `double` The minimum transaction amount specified by the bank to be eligible for EMI. | 2500.00   |
| emiPercentage | `double` The interest percentage of the EMI.                                          | 25.75     |
| emiAmount     | `double` The monthly instalment amount.                                               | 2555.75   |
| bankName      | `string` The bank name.                                                               | Axis Bank |
| Tenure        | `long` The tenure of emi.                                                             | 6         |

<br />
