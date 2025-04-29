---
title: EMI
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: EMI Integration with PayU APIs
  description: >-
    Explore the process of collecting payments through EMI options using PayU's
    Merchant Hosted Checkout integration. Discover how to determine customer
    eligibility, calculate EMI details, and initiate transactions with EMI
    conversion using EMI APIs. This guide covers various EMI integration flows,
    including debit cards, credit cards, cardless EMI, and native OTP flow.
  keywords:
    - PayU EMI API Integration
    - PayU EMI Conversion Process
  robots: index
next:
  description: ''
---
Equated Monthly Instalment (EMI) refers to the fixed amount of money you pay to a bank or a lender every month as part of the repayment of an outstanding loan. EMI as a payment option gives your customers the freedom and affordability to purchase expensive items without having to deal with banks or NBFCs as intermediaries.

> 👍 Before you begin:
>
> Register for a account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

The following video describes why EMIs are important for your business and gives an overview of PayU’s EMI offerings:

<Embed url="https://www.youtube.com/watch?v=zC0arr50GZw" title="PayU Payment Gateway - Enable EMI & BNPL For Your Business Today!" favicon="https://www.google.com/favicon.ico" image="https://i.ytimg.com/vi/zC0arr50GZw/hqdefault.jpg" provider="youtube.com" href="https://www.youtube.com/watch?v=zC0arr50GZw" typeOfEmbed="youtube" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252FzC0arr50GZw%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DzC0arr50GZw%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252FzC0arr50GZw%252Fhqdefault.jpg%26key%3D7788cb384c9f4d5dbbdbeffd9fe4b92f%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />

The following sections describe the procedure to integrate cards with EMI:

* [PayU Hosted Checkout Integration](doc:collect-payments-using-payu-hosted-checkout-integration-emi)
* Merchant Hosted Checkout Integration
  * [Debit Card](doc:collect-payments-with-emi-using-debit-card)
  * [Credit Card](doc:collect-payments-with-emi-using-credit-card)
  * [Cardless EMI](doc:collect-payments-with-cardless-emi-using-merchant-hosted-checkout)
  * [Native OTP Flow Integration](doc:native-otp-flow-integration)
    * [Debit Card](/docs/native-otp-flow-integration#collect-payments-with-debit-card)
    * [Cardless EMI](/docs/native-otp-flow-integration#collect-payments-with-cardless-emi)

## Supported Banks or Institutions

PayU supports EMI for the following banks or institutions with debit cards & credit cards and No-Cost EMI:

### Credit Cards

* American Express
* HDFC Bank
* ICICI Bank
* Axis Bank
* Citibank
* State Bank of India
* Kotak
* RBL Bank
* IndusInd Bank
* Standard Chartered Bank
* YES Bank
* HSBC Bank
* One Card
* AU Small Finance Bank
* Bank of Baroda
* IDBI Bank
* IDFC First Bank

### Debit Cards

* State Bank of India
* HDFC Bank
* ICICI Bank
* Axis Bank
* Kotak Mahindra Bank
* Federal Bank
* Bank of Baroda

## Cardless

* Bajaj Finserve
* Liquiloan
* Zest Money
* KreditBee
