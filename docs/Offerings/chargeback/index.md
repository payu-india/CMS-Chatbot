---
title: Chargeback
deprecated: false
hidden: false
metadata:
  robots: index
---
A chargeback is a transaction reversal that occurs when a customer successfully disputes a charge on their debit or credit card. It results in the payment amount being returned to the card. Buyers typically request chargebacks from their credit card issuing bank when they want to dispute a charge from their credit card statement.

The chargeback involves the following steps:


<Image src="https://files.readme.io/37be493-untitled.png" align="center" width="550px" />


## Chargeback Support

The Chargeback is supported for the following:

- Cards
- Card-Not-Present (<Glossary>CNP</Glossary>) transactions
- Net Banking
- EMI
  - Cards
  - UPI
- UPI
- Cross-Border Payments (OPGSP)
- Wallets
  - PayTM
  - Freecharge
  - Amazon Pay
  - Airtel Money
  - Oxigen
  - Ola Money
  - Jio Money
  - ItzCash
  - HDFC PayZapp
  - Yes Bank
  - MobiKwik
  - PhonePe
  - Apple Pay

## PayU Chargeback process

1. PayU receives chargeback notification from Acquiring bank.​
2. PayU notifies merchants . The merchant needs to provide their response ​ within **Reply date** mentioned by PayU.​
3. PayU verifies the documents against the chargeback raised and shares​ the same with the acquiring bank.​
4. If merchant does not provide response before the **Reply date**, ​ the acquiring bank will close the case in favour of the customer.​

You can handle the chargebacks using Chargeback APIs or PayU Dashboard > Chargeback. This part of the document includes the following:

- [Chargeback Dashboard](doc:chargeback-dashboard)
- [Webhooks for Chargeback](doc:webhooks-for-chargeback)

## Chargeback Integration APIs

The following  APIs are used in chargeback:

| API                                                                           | Purpose                                                                                                                           |
| :---------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| [Read Chargeback API](https://docs.payu.in/reference/read-chargeback-api)     | Responds with the all the chargebacks corresponding to the merchant.                                                              |
| [Read Reasons API](https://docs.payu.in/reference/read-reasons-api)           | Lists all the reasons required for the merchant to provide in order to accept or contest the chargeback.                          |
| [Accept Chargeback API](https://docs.payu.in/reference/accept-chargeback-api) | Accept the chargeback by providing the appropriate reasons in the request body against the chargeback and merchant ID.            |
| [Accept/Contest Chargeback API](ref:accept-contest-chargeback-api)            | Accept or context a chargeback by providing appropriate reasons in the request body against the chargeback and merchant ID.       |
| [Contest Chargeback API](ref:contest-chargeback-api)                          | Allows to contest the chargeback by providing the appropriate reasons in the request body against the chargeback and merchant ID. |

<br />
