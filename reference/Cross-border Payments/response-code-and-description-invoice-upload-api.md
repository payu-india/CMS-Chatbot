---
title: Response Code and Description - Invoice Upload API
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
| **Response Code** | **Response Message**               | **Description**                                     |
| ----------------- | ---------------------------------- | --------------------------------------------------- |
| 00                | Uploaded Successfully              | AWB/Invoice has been uploaded successfully          |
| 101               | Invalid Format                     | When format is not pdf, .doc, .docx, .jpg or .jpeg  |
| 102               | Invalid Transaction Status         | If the transaction is not captured/auto-refunded    |
| 103               | Failed to Upload                   | In case of some error in uploading the file         |
| 104               | Invalid upload type                | Only invoice and AWB are allowed                    |
| 105               | Not an PACB merchant, contact KAM  | If the merchant is not mapped as an PACB merchant   |
| 106               | Size exceeding 5 MB                | When file size is greater than 2 MB                 |
| 107               | Invalid PayU ID                    | The PayU ID in the request is missing or invalid    |
| 108               | Empty Invoice/AWB ID               | The invoice/AWB ID is missing                       |
| 109               | Empty file name                    | Mandatory field(s) is/are missing                   |