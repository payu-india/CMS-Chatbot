---
title: Merchant Hosted Checkout
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Custom Checkout Integration
  description: >-
    Learn how to process credit/debit card, UPI, EMI or any other payments on
    your website using PayU's Merchant Hosted Checkout API. This approach
    eliminates redirection to PayU's payment page, enhancing transaction
    security and efficiency.
  keywords:
    - Merchant Hosted Checkout
    - ' Custom Hosted Checkout'
    - ' Merchant Hosted Checkout Prerequisites'
  robots: index
next:
  description: ''
---
Custom Checkout or Merchant Hosted Checkout integration is used to process credit/debit card payments on your website using PayU, to collect card details on your website, and to submit them to PayU through API.. This eliminates the need for redirection to PayU’s payment page, resulting in a more secure and efficient transaction.

> 👍 Before you Begin:
> 
> - PayU strongly recommends you test your integration using the test merchant Key or Salt. To create a test merchant account, refer to [Register for a Merchant Account on Dashboard](doc:register-for-a-merchant-account-on-dashboard). After you create a test merchant account, you can access the test Key or Salt as described in [Generate Merchant Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard).
> - Later, register for a production account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

## Workflow

The following process diagram illustrates the Merchant Hosted Checkout workflow:

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/08/Merchant_Hosted_Flow-2048x989.png",
        null,
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


1. It operates through a form post-call directly from the customer’s browser, sending their payment data into the PayU’s systems.
2. A payment process initiated from your e-commerce website travels through PayU’s secured environment before reaching the card ACS or a bank’s Net Banking page.
3. After the transaction is completed in the bank’s website environment, the customer is redirected to your website.

## Customer Experience

**Step 1:** The customer completes shopping at your website and initiates a transaction with saved card (for example, VISA) credentials.

**Step 2:** The customer enters the CVV and proceeds to complete the payment.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/05/MicrosoftTeams-image-1.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "300px",
      "border": true
    }
  ]
}
[/block]


**Step 3:** After the credentials are entered, and the payment flow is launched, the user is navigated through a secured PayU environment that reflects the transaction ID.

**Step 4:** The flow takes the user to the login ACS page of the bank, where the user needs to complete the transaction by using the OTP sent by the bank to the registered mobile number.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1764f1a919d1e2a65ea7af0227bbb1b649c85cfde4cdbc4b435be8e6fb722fd3-merchant_hosted_acs_page.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "300px",
      "border": true
    }
  ]
}
[/block]


**Step 5:** Customer is shown the status (failed/successful) on your website based on the transaction status from PayU.

## Features

The features of Merchant Hosted Checkout are:

- Collects the customer payment credentials directly through a customized payments interface hosted as part of your business website
- Allows a fast and coherent payment process
- Builds the e-commerce website using a readily available shopping cart or custom-built from scratch, as per business requirements
- Provides the freedom to build your own payment experience and add elements as per your requirements to ensure continuity
- Grants you total control over your customer’s payment data and improves your brand appeal

## Prerequisites

The prerequisites for integrating with Merchant Hosted Checkout are:

- Develop a business website to collect the complete payment details of the customers at your end.
- Fill the “[Self-Assessment Questionnaire A-EP and Attestation of Compliance](https://www.pcisecuritystandards.org/documents/PCI-DSS-v3_2-SAQ-A_EP-rev1_1.pdf)” form from PCI, which is mandatory for all entities seeking to store, process, and transmit cardholder data.

> 🚧 Remember
> 
> If you are using only the UPI and Wallet payment modes with Merchant Hosted checkout, ensure that your website is secure.

- You must have an understanding of the following concepts:
  - workflows
  - various payment processes
  - website designing fundamentals
  - Usability (UX) management principles necessary to build the complete online payments infrastructure on your website.
- Sufficient technical bandwidth dedicated to managing the end-to-end web checkout processes in-house consistently.

## Integration Steps

The Merchant Hosted Checkout integration involves the following steps:

1. Payment Methods Integration (one or more)
   - [Net Banking Integration](https://docs.payu.in/docs/collect-payments-with-net-banking-seamless)
   - [Cards Integration](https://docs.payu.in/docs/collect-payments-with-cards-seamless)
   - [EMI Integration](https://docs.payu.in/docs/collect-payments-with-emi-seamless)
   - [UPI Integration](https://docs.payu.in/docs/collect-payments-with-upi-seamless)
   - [Wallets Integration](https://docs.payu.in/docs/collect-payments-with-wallets-seamless)
   - [BNPL Integration](https://docs.payu.in/docs/collect-payments-with-bnpl)
   - [Pluxee Card Integration](https://docs.payu.in/docs/integrate-with-merchant-hosted-checkout-for-pluxee-card)
   - [EFTNET (NEFT/RTGS) Integration](https://docs.payu.in/docs/collect-payments-with-eftnet-neftrtgs-seamless)
   - [QR Integration](https://docs.payu.in/docs/merchant-hosted-qr-integration)
2. [Test the Integration](https://docs.payu.in/docs/ios-checkoutprosdk-test-integration)
3. [Go-live Checklist](https://docs.payu.in/docs/ios-checkoutprosdk-go-live-checklist)

During the integration, refer the [Generate Hash](https://docs.payu.in/docs/generate-hash-merchant-hosted) for hash generation details.