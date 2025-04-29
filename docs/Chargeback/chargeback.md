---
title: Introduction - Chargeback
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
A chargeback is a transaction reversal that occurs when a customer successfully disputes a charge on their debit or credit card. It results in the payment amount being returned to the card. Buyers typically request chargebacks from their credit card issuing bank when they want to dispute a charge from their credit card statement.

The chargeback involves the following steps:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/37be493-untitled.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "550px"
    }
  ]
}
[/block]


## PayU Chargeback process

1. PayU receives chargeback notification from Acquiring bank.​ 
2. PayU notifies merchants . The merchant needs to provide their response ​ within** Reply date** mentioned by PayU.​ 
3. PayU verifies the documents against the chargeback raised and shares​ the same with the acquiring bank.​ 
4. If merchant does not provide response before the **Reply date**, ​ the acquiring bank will close the case in favour of the customer.​

This part of the document includes the following:

- [Chargeback Dashboard](doc:chargeback)
- [Chargeback APIs](doc:chargeback-apis)
  - [Read Chargeback API](https://docs.payu.in/reference/read-chargeback-api)
  - [Read Reasons API](ref:read-reasons-api)
  - [Accept Chargeback API](https://docs.payu.in/reference/accept-chargeback-api)
  - [Contest Chargeback API](ref:contest-chargeback-api)