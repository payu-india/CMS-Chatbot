---
title: Customer Journey
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
The customer journey using the Dynamic Storefront QR involves:

<Image align="center" className="border" width="75% " border={true} src="https://files.readme.io/6b53f01-Screenshot_2023-09-13_at_3.02.13_PM.png" />

1. The customer scans the QR or clicks on the payment link and lands on the order summary page.
2. The customer reviews the details on the order summary page.
3. The customer proceeds to PayU’s non-seamless check-out page and sees either enforced or all available modes of payment.
4. The customer authorizes the transaction.
5. The transaction is completed & a payment receipt is shown to the customer.

## Use case

The following steps describe a use case where a customer wants to buy an Apple iPhone from a physical store:

1. After the customer selects the specific model of the phone, he goes to the cashier or sales SPOC for billing.
2. The cashier bills the customer sends the bill data via an API to PayU and gets a QR code or a payment link in response.
3. The customer scans the QR code using a camera or google lens on his smartphone (or clicks on the payment link), reviews the bill information & bill amount and proceeds to make payment through any of the available or enforced modes of payment.
4. After the customer makes the payment, the cashier will receive payment confirmation directly to his ERP system & the order is automatically reconciled.
