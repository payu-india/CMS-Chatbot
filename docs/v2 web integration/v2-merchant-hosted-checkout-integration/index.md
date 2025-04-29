---
title: v2 Merchant Hosted Checkout
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
Custom Checkout or Merchant Hosted Checkout integration is used to process credit/debit card payments on your website using PayU, collect card details on your website and submit them to PayU via API. This eliminates the need for redirection to PayU’s payment page, resulting in a more secure and efficient transaction.

> 👍 Before you begin:
>
> PayU recommends you to integrate with Test environment initially. For more information, contact you PayU Key Account Manager (KAM) or PayU Support.

> 📘 v2/payment Recommended for new integrations:
>
> PayU recommends v2/payment API for your new integration or if you are new merchant onboarded to PayU from March 2025. 
>
> If you have already integrated with **\_payment** (v1) API, refer to\[Merchant Hosted Checkout Integration v1\]\([https://docs.payu.in/v1/docs/custom-checkout-merchant-hosted](https://docs.payu.in/v1/docs/custom-checkout-merchant-hosted)).

## Workflow

The following process diagram illustrates the Merchant Hosted Checkout workflow:

<Image align="center" className="border" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/08/Merchant_Hosted_Flow-2048x989.png" />

1. It operates through a form post-call directly from the customer’s browser, sending their payment data into the PayU’s systems.
2. A payment process initiated from your e-commerce website travels through the PayU’s secured environment before reaching the card ACS or a bank’s Net Banking page.
3. After the transaction is completed in the bank’s website environment, the customer is redirected to your website.

## Customer Experience

**Step 1:** The customer completes shopping at your website and initiates a transaction with saved card (for example, VISA) credentials.

**Step 2:** The customer enters the CVV and proceeds to complete the payment.

<Image align="center" className="border" width="300px" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/05/MicrosoftTeams-image-1.png" />

**Step 3:** After the credentials are entered, and the payment flow is launched, the user is navigated through a secured PayU environment that reflects the transaction ID.

**Step 4:** The flow takes the user to the login ACS page of the bank, where the user needs to complete the transaction by using the OTP sent by the bank to the registered mobile number.

<Image align="center" className="border" width="300px" border={true} src="https://files.readme.io/1764f1a919d1e2a65ea7af0227bbb1b649c85cfde4cdbc4b435be8e6fb722fd3-merchant_hosted_acs_page.png" />

**Step 5:** Customer is shown the status (failed/successful) on your website based on the transaction status from PayU.

## Features

The features of Merchant Hosted Checkout are:

* Collects the customer payment credentials directly through a customized payments interface hosted as part of your business website
* Allows a fast and coherent payment process
* Builds the e-commerce website using a readily available shopping cart or custom-built from scratch, as per business requirements
* Provides the freedom to build your own payment experience and add elements as per your requirements to ensure continuity
* Grants you total control over your customer’s payment data and improves your brand appeal

## Prerequisites

The prerequisites for integrating with Merchant Hosted Checkout are:

* Develop a business website to collect the complete payment details of the customers at your end.
* Fill the “[Self-Assessment Questionnaire A-EP and Attestation of Compliance](https://www.pcisecuritystandards.org/documents/PCI-DSS-v3_2-SAQ-A_EP-rev1_1.pdf)” form from PCI, which is mandatory for all entities seeking to store, process, and transmit cardholder data.

> 🚧 Remember
>
> If you are using only the UPI and Wallet payment modes with Merchant Hosted checkout, ensure that your website is secure.

* You must have an understanding of the following concepts:
  * workflows
  * various payment processes
  * website designing fundamentals
  * Usability (UX) management principles necessary to build the complete online payments infrastructure on your website.
* Sufficient technical bandwidth dedicated to managing the end-to-end web checkout processes in-house consistently.

The Merchant Hosted Checkout integration supports following payment method:

* [v2 Net Banking Integration](https://docs.payu.in/v2/docs/v2-net-banking-integration)
* [v2 Cards Integration](https://docs.payu.in/v2/docs/v2-cards-merchant-hosted-integration)
* [v2 UPI Integration](https://docs.payu.in/v2/docs/v2-upi-merchant-hosted-integration)
* [v2 Wallets Integration](https://docs.payu.in/v2/docs/v2-wallets-merchant-hostede-integration)
* [v2 EMI Integration](https://docs.payu.in/v2/docs/v2-emi-merchant-hosted-integration)
* [v2 BNPL Integration](https://docs.payu.in/v2/docs/v2-bnpl-merchant-hosted-integration)
