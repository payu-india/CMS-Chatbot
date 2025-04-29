---
title: EMI
excerpt: ''
deprecated: false
hidden: false
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

[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FzC0arr50GZw%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DzC0arr50GZw&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FzC0arr50GZw%2Fhqdefault.jpg&key=7788cb384c9f4d5dbbdbeffd9fe4b92f&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen; encrypted-media; picture-in-picture;\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=zC0arr50GZw",
  "title": "PayU Payment Gateway - Enable EMI & BNPL For Your Business Today!",
  "favicon": "https://www.google.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/zC0arr50GZw/hqdefault.jpg",
  "provider": "youtube.com",
  "href": "https://www.youtube.com/watch?v=zC0arr50GZw",
  "typeOfEmbed": "youtube"
}
[/block]


The following sections describe the procedure to integrate cards with EMI:

- [PayU Hosted Checkout Integration](doc:collect-payments-using-payu-hosted-checkout-integration-emi)
- Merchant Hosted Checkout Integration
  - [Debit Card](doc:collect-payments-with-emi-using-debit-card)
  - [Credit Card](doc:collect-payments-with-emi-using-credit-card)
  - [Cardless EMI](doc:collect-payments-with-cardless-emi-using-merchant-hosted-checkout)
  - [Native OTP Flow Integration](doc:native-otp-flow-integration)
    - [Debit Card](/docs/native-otp-flow-integration#collect-payments-with-debit-card)
    - [Cardless EMI](/docs/native-otp-flow-integration#collect-payments-with-cardless-emi)

## Supported Banks or Institutions

PayU supports EMI for the following banks or institutions with debit cards & credit cards and No-Cost EMI:

### Credit Cards

- American Express
- HDFC Bank
- ICICI Bank
- Axis Bank
- Citibank
- State Bank of India
- Kotak
- RBL Bank
- IndusInd Bank
- Standard Chartered Bank
- YES Bank
- HSBC Bank
- One Card
- AU Small Finance Bank
- Bank of Baroda
- IDBI Bank
- IDFC First Bank

### Debit Cards

- State Bank of India
- HDFC Bank
- ICICI Bank
- Axis Bank
- Kotak Mahindra Bank
- Federal Bank
- Bank of Baroda

## Cardless

- Bajaj Finserve
- Liquiloan
- Zest Money
- KreditBee