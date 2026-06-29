---
title: BNPL Integration
excerpt: >-
  Buy Now Pay Later (<<glossary:BNPL>>) is a payment method that allows your
  customers to purchase goods or services and defer payment for a period of
  time, usually ranging from a few weeks to several months. With BNPL, your
  customers can make a purchase without paying the full amount upfront, and
  instead, pay the cost of the purchase in installments over a set period of
  time.
deprecated: false
hidden: false
metadata:
  title: ''
  description: >-
    Buy Now, Pay Later (BNPL) allows customers to pay for purchases over time,
    with flexible payment options and instant approval, while also offering
    interest-free instalments. Merchants benefit from increased sales and risk
    management solutions provided by PayU.
  keywords:
    - PayU Checkout BNPL Integration
    - ' Deferred Payment Integration with PayU'
    - PayU BNPL integration
    - Buy Now Pay Later Integration with PayU PayU
    - ' BNPL API Integration Pay Later Services with PayU'
    - PayU BNPL Merchant Integration
    - Flexible Payment Options PayU
    - PayU BNPL Checkout Flow
  robots: index
next:
  description: ''
---
BNPL is offered by third-party payment providers or financial institutions that partner with retailers to offer this service at checkout. Customers select **BNPL** as a payment option during checkout and then enter into an agreement with the payment provider or financial institution to pay for their purchase over time. Some BNPL providers charge interest or fees, while others offer interest-free installment plans.

BNPL can be a convenient option for customers who may not have the funds to make a large purchase upfront, but still want to make the purchase and pay for it over time. However, customers should be aware of the terms and conditions of their BNPL agreement, including any interest or fees that may be charged, as well as the potential impact on their credit score.

<Callout icon="👍" theme="okay">
  ### Before you begin:

  Register for a account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Callout>

## Integration guides

- [PayU Hosted Checkout BNPL Workflow](doc:bnpl-workflow-payu-hosted-checkout)
- [Merchant Hosted BNPL Workflow](doc:general-flow-bnpl-integration-with-merchant-hosted)
- [BNPL Link and Pay](doc:link-and-pay)
- [Collect Payments with BNPL using Link and Pay](doc:collect-payments-with-bnpl-using-link-and-pay)
- [BNPL Codes](doc:bnpl-codes)
- [Error Codes for BNPL Integration](doc:error-codes-1)

The following video describes PayU’s BNPL offering:

<Embed title="" typeOfEmbed="youtube" url="https://www.youtube.com/watch?v=PdEHY2_fYj4" href="https://www.youtube.com/watch?v=PdEHY2_fYj4" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252FPdEHY2_fYj4%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DPdEHY2_fYj4%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252FPdEHY2_fYj4%252Fhqdefault.jpg%26key%3D7788cb384c9f4d5dbbdbeffd9fe4b92f%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22640%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />

## BNPL Benefits

<Glossary>BNPL</Glossary> offers the following benefits to both customers and merchants:

<Accordion title="Benefits for Customers" icon="fa-user">
  * **Flexible payment options**: Customers can make purchases and pay for them over time, with flexible payment options ranging from a few weeks to several months.
  * **Instant approval**: Customers can get instant approval for BNPL, which means they can complete their purchase and receive their goods or services without any delay.
  * **Interest-free instalments**: Offers interest-free instalments, which means customers can spread the cost of their purchase over time without incurring any additional interest charges.
  * **Easy checkout**: Easy to use and is integrated with many online merchants, allowing customers to complete their purchase quickly and easily.
</Accordion>

<Accordion title="Benefits for Merchants" icon="fa-store">
  * **Increased sales for merchants**: Merchants can increase sales by offering customers a convenient payment option that allows them to make purchases they might not have been able to afford otherwise.
  * **Risk management**: PayU provides risk management solutions to merchants, including fraud detection and prevention, to help minimize the risk of chargebacks and other payment-related issues.
</Accordion>

## APIs used in BNPL integration

| API name                                                                                   | Purpose                                                                                                                      |
| ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| [Get Checkout Details API](ref:get_checkout_details)                                       | Check customer BNPL eligibility before initiating payment on merchant-hosted checkout.                                       |
| [Get EMI Checkout Details API](ref:get-emi-checkout-details-api)                           | Check BNPL Link & Pay eligibility and retrieve checkout details for supported lenders.                                       |
| [Collect Payment API – BNPL (Merchant Hosted Checkout)](ref:_payment_merchant_hosted_bnpl) | Submit a BNPL payment request with `pg=BNPL` and the provider `bankcode` on merchant-hosted checkout.                        |
| [Collect Payment API – BNPL Link & Pay](ref:collect-payment-api-bnpl-link-pay)             | Initiate BNPL Link & Pay transactions, including one-click repeat-user flows after wallet linking.                           |
| [Collect Payment API – S2S Link and Pay](ref:_payment_s2s_link_pay)                        | Server-to-server payment initiation for BNPL Link & Pay with OTP-based authentication.                                       |
| [Submit OTP API](ref:submit-otp-to-payu)                                                   | Submit the customer OTP along with the reference ID from the `_payment` response to complete BNPL Link & Pay authentication. |
|  [Verify Payment API](ref:verify_payment_api)                                              | Server-side reconciliation of transaction status after payment.                                                              |

<br />
