---
title: Offers API Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Offers integration APIs
  description: >-
    This page provides PayU's various API Integration for Offers that can be
    created such as Instant Discounts, Cashback, No Cost EMI, and
    Product/SKU-based Offers. It also includes details on the different payment
    modes supported, such as Cards (credit and debit), Net banking, EMI (Credit
    and Debit), Wallets, UPI, and No Cost EMI, along with explanations on how
    each type of offer works.
  robots: index
next:
  description: ''
---
---
title: Offers API Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Offers integration APIs
  description: >-
    This page provides PayU's various API Integration for Offers that can be
    created such as Instant Discounts, Cashback, No Cost EMI, and
    Product/SKU-based Offers. It also includes details on the different payment
    modes supported, such as Cards (credit and debit), Net banking, EMI (Credit
    and Debit), Wallets, UPI, and No Cost EMI, along with explanations on how
    each type of offer works.
  robots: index
next:
  description: ''
---
PayU Offers allows merchants to create a wide range of offers across different payments mode. The self-serve Dashboard portal allows merchants to add advanced configuration for offers and monitor offer associated performances and transactions.

<Callout icon="👍" theme="okay">
  ###

  **Before you begin**: Register for a account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Callout>

The following offers can be created using APIs:

- [Integrate with PayU Hosted Checkout](doc:payu-hosted-checkout-integration-with-offers)
  - [Instant Discount or Cashback Offer](doc:payu-hosted-checkout-integration-with-offers#instant-discount-or-cashback)
  - [SKU-Based Offer](doc:payu-hosted-checkout-integration-with-offers#sku-based-offer)
- [Instant Discount or Cashback using Merchant Hosted Checkout](doc:instant-discount-or-cashback-offers-integration-using-merchant-hosted-checkout)
- [SKU-Based Offer using Merchant Hosted Checkout](doc:collect-payments-with-sku-based-offer-using-merchant-hosted-checkout-offers-integration)

## APIs used in Offers integration

The following APIs are referenced across the integration guides in this section:

| API name | Purpose |
| --- | --- |
| [Fetch Offers API](ref:fetch-offers-api) | Retrieve applicable offers for a transaction context to display on checkout, cart, product detail, or offers pages. **Used in:** [Instant Discount or Cashback (Merchant Hosted)](doc:instant-discount-or-cashback-offers-integration-using-merchant-hosted-checkout), [SKU-Based Offer (Merchant Hosted)](doc:collect-payments-with-sku-based-offer-using-merchant-hosted-checkout-offers-integration), [Multiple Offers (Merchant Hosted)](doc:multiple-offers-merchant-hosted), [Pre-Discounted Offer (Merchant Hosted)](doc:pre-discounted-offer-merchant-hosted-checkout). |
| [EMI Calculator API](ref:emi-calculator-api) | Return EMI tenure plans with monthly instalments, interest rates, and applicable EMI offers when the customer selects EMI. |
| [Validate Offer API](ref:validate-offer-api) | Confirm that the selected offer applies to the transaction before initiating payment. |
| [Collect Payment API – Merchant Hosted Checkout](ref:_payment_merchant_hosted) | Submit the payment request with offer parameters (`offer_key`, `api_version`, `user_token`, and related fields) for merchant-hosted checkout.|
| [Collect Payment API – PayU Hosted Checkout](ref:_payment_payu_hosted_checkout) | Initiate a PayU-hosted checkout payment with offer parameters for instant discount, cashback, or SKU-based offers. |
| [Verify Payment API](ref:verify_payment_api) | Reconcile transaction and offer details server-side after payment.  |
| [Refund APIs](ref:refund-apis) | Refund the payment amount passed in the refund request when reversing an offer transaction. |


The following videos explain how to create an offer:

<Embed title="" typeOfEmbed="youtube" url="https://www.youtube.com/watch?v=8kqhGkLHOj0" href="https://www.youtube.com/watch?v=8kqhGkLHOj0" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252F8kqhGkLHOj0%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253D8kqhGkLHOj0%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252F8kqhGkLHOj0%252Fhqdefault.jpg%26key%3D7788cb384c9f4d5dbbdbeffd9fe4b92f%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />

<Embed title="" typeOfEmbed="youtube" url="https://www.youtube.com/watch?v=WvHrgeVMpf4" href="https://www.youtube.com/watch?v=WvHrgeVMpf4" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252FWvHrgeVMpf4%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DWvHrgeVMpf4%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252FWvHrgeVMpf4%252Fhqdefault.jpg%26key%3D7788cb384c9f4d5dbbdbeffd9fe4b92f%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />

## Features

- Discovery, product experience, ease of offer creation, customer purchase behavior inference
- Higher checkout conversion for merchants
- Incremental GMV from offers by increasing share of wallet and new acquisition
- Monetization through offer sourcing from banks or merchants
- Log in to PayU Dashboard and create offers
- Collect Payments on offers with the simplest integration.
- Manage your offers by viewing offer performance, editing offers, etc. on PayU Dashboard

## Types of Offers

<Accordion title="Instant Discount" icon="fa-tag">
  Instant discount as a percentage of the transaction amount or a flat amount. For example, if the transaction is of the amount ₹10,000, the offer discount will be ₹1000. The amount that is posted to the bank for debiting is ₹10000 – ₹1000 = ₹9000. The offer discount is applied before the transaction is initiated.
</Accordion>

<Accordion title="Cashback" icon="fa-money-bill">
  Cashback as a percentage of the transaction or a flat amount. For example, if the transaction amount is of Rs. 10,000, offer discount is of Rs. 1000, amount initiated in the transaction for debit would be Rs. 10,000 as cashback are settled later.

  <Callout icon="📘" theme="info">
    **Note:** Cashbacks need to be processed by the merchants with the banks. Create Cashback Offers only if you have an agreement with them or reach out to the Key Account Manager for additional support.
  </Callout>

  The cashback time period would be aligned basis merchant requirements.

  Merchants can create both instant discount and cashback offers across the following payment modes:

  - Cards (credit and debit)
  - Net banking
  - EMI (Credit and Debit)
  - Wallets
  - UPI
</Accordion>

<Accordion title="No Cost EMI" icon="fa-calendar">
  Interest charged from the customer can be completely discounted or given as a cashback. Please note that in case of Instant discount the principal amount would be discounted by a certain amount so that the amount customer pays as a sum of all the EMIs would be exactly as the amount of products/services purchased. In case of cashback the entire interest to be paid by the customer is provided as cashback to the customer.

  For example:

  - Product Amount:10000
  - Interest Rate: 12%
  - Tenure: 3 months
  - Interest Paid by customer in case of Interest-Bearing EMI is Rs. 201
  - **Instant Discount:** Principal to be discounted by Rs 197 (Customer would pay Rs 3,333 every month)
  - **Cashback**: In case of Rs 201 cashback will be refunded back to the customer (Customer would pay Rs 3400 every month)

  <Callout icon="📘" theme="info">
    **Notes**

    - The offer value will change depending on the bank and tenure selected by the customer. Additionally, there is a small difference between the offer cost borne by the merchant in case of Instant Discount or Cashback as in the above example.
    - Cashbacks need to be processed by the merchants with the banks. Create Cashback Offers only if you have an agreement with them or reach out to Key Account Manager for additional support. The cashback time-period would be aligned basis the merchant requirement.
  </Callout>
</Accordion>
