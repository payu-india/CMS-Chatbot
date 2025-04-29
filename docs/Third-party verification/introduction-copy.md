---
title: Introduction to TPV Integration (NEW)
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The global financial industry is coming up with a new paradigm for risk management. If you are a merchant in the BFSI sector, your business is subject to strict guidelines, where various regulatory bodies regulate your day-to-day operations.

Third-Party Verification (TPV) is a mandatory requirement as per Stock Exchange Bureau India (SEBI) mandate for merchants such as stockbrokers and mutual funds operating in the BFSI sector. TPV is a prerequisite that ensures credibility, and it reduces the risk for customers.

## TPV Workflow

![](https://files.readme.io/2bea29d-image.png)

## Comparison of TPV with regular flow

In a regular Net Banking or a UPI transaction, you don’t pass the customer account number from which you want the customer to transact, but in the case of TPV integration, you know the customer account number, and you want the customer only to transact with the same account number.\
You also pass the customer account number in the payment request compared to regular retail banking or UPI.

## Why TPV?

In its constant endeavour to reach out to new categories of merchants, PayU, now provides TPV integration on its payment processing platform.

Third-Party Verification (TPV) procedure is a mandatory requirement for web merchants such as stock brokers and mutual funds, operating in the BFSI (Banking, Financial Services and Insurance) sector. This account authentication procedure is essential for brokerage, Demat Account transfers, investments and other payments specified by the Securities and Exchange Board of India (SEBI).

As per SEBI guidelines, transactions must be made by their customers exclusively from a specific bank account number or CRN (Customer Relationship Number).

PayU will enable these businesses to meet their compliance requirements for online payment collections by offering the TPV integrations of banks. When the customer transacts with the merchant through our payment gateway, his bank account number or CRN is mapped in such a way so as to lock the transaction to ensure that the payment is processed only from his registered bank account.

TPV integration on the payment gateway resembles a Net Banking transaction with the added advantage of having a locked account during fund transfers. The merchant (such as a broker) initially registers the bank account number or CRN of the customer to meet the SEBI guideline. These account parameters will be stored by the merchant and forwarded to PayU, which in turn submits them to the corresponding bank of the customer during the transaction process.

Brokers and other online businesses can now sign up for our services and take advantage of our TPV solution to transact online with their customers securely and conveniently in real-time.

Meet your compliance requirements and start transacting online with your customers by availing the TPV integration of leading banks on PayU’s advanced payment platform.

## TPV integration support

PayU supports the PayU Hosted Checkout (non-seamless), Merchant Hosted Checkout (Seamless) and PayU Server-to-Server Integration are supported

* [PayU Hosted or non-seamless integration](payu-hosted-checkout-tpv-workflow)
* [Seamless Integration](https://docs.payu.in/docs/collect-payments-with-tpv-merchant-hosted-checkout)
  * [Net Banking](/docs/net-banking-integration-for-tpv) 
  * [UPI](/docs/upi-integration-for-tpv) 
    * [UPI Intent Autopay](https://docs.payu.in/docs/upi-intent-autopay-tpv-integration)
    * [UPI Collect Autopay](https://docs.payu.in/docs/upi-collect-autopay-tpv-integration)\ <br />
