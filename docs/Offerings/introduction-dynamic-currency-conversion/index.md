---
title: International Payments
excerpt: ''
deprecated: false
hidden: false
icon: far fa-globe-pointer
metadata:
  title: PayU India International Payments
  description: >-
    Do you want to offer your customers the option to pay in their preferred
    currency? Learn how to integrate PayU’s Dynamic Currency Conversion (DCC)
    feature into your hosted checkout page and boost your conversion rates.
  keywords:
    - Dynamic Currency Conversion
    - DCC
    - PayU Integration Multi-Currency Payment Gateway
    - Currency Conversion API Introduction.International Payment Processing
    - Global Payment Solutions
    - Dynamic Pricing Integration
    - Foreign Currency Payment
    - Seamless Currency Conversion Integration Introduction
    - Dynamic Currency Conversion Benefits
  robots: index
next:
  description: ''
---
International card payments refer to financial transactions where a cardholder makes a purchase using a payment card issued in one country for goods or services from a merchant located in another country. These transactions involve currency conversion and cross-border processing, requiring specialized payment infrastructure to handle the complexities of international commerce.

With PayU’s international card payment solution, businesses can accept payments from cards issued in over 150 countries through major card networks. This enables merchants to expand their business globally while providing customers with a familiar and convenient payment experience regardless of their location.

<Callout icon="👍" theme="okay">
  ### Before you begin:

  Register for a account with PayU before you start integration. Contact your PayU Key Account Manager to enable international payments. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Callout>

## Integration guides

The following sections describe how to integrate international payments and currency conversion with PayU:

- [Workflow – DCC and MCC](doc:dynamic-currency-conversion-workflow)
- [PayU Hosted Checkout Integration](doc:payu-hosted-checkout-integration-dynamic-currency-conversion)
- [Merchant Hosted Checkout Integration](doc:merchant-hosted-checkout-dynamic-currency-conversion)
- Reference
  - [Supported Currencies for International Payments](doc:supported-currencies-for-international-payments)
  - [MCC Currency Codes](doc:mcc-currency-codes)
  - [FAQs – Dynamic Currency Conversion](doc:faqs-dynamic-currency-conversion)

Check the following video that provides an overview on International Payments:

<Embed title="" typeOfEmbed="youtube" url="https://www.youtube.com/watch?v=rEBQ5ZF9KkI" href="https://www.youtube.com/watch?v=rEBQ5ZF9KkI" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252FrEBQ5ZF9KkI%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DrEBQ5ZF9KkI%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252FrEBQ5ZF9KkI%252Fhqdefault.jpg%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" providerName="YouTube" providerUrl="https://www.youtube.com/" />

## Why Choose PayU for International Payments?

PayU offers a comprehensive solution for businesses looking to accept payments from customers around the world. Our international payment platform combines global reach with localized expertise to help you expand your business beyond borders.

## Key Benefits of PayU’s International Payment Solution

<Accordion title="International Card Acceptance" icon="fa-credit-card">
  * Accept all major international cards including Visa, Mastercard, and American Express
  * Process payments from over 150 countries worldwide
</Accordion>

<Accordion title="Convenient Settlement Options" icon="fa-money-bill">
  * Flexibility to receive settlements in INR or non-INR currencies based on your business needs
  * Consolidated reporting across all international transactions
</Accordion>

<Accordion title="Compliant with Global Security Standards" icon="fa-shield">
  * 3DS2.0 compliant solution to prevent fraud and secure transactions
  * Eliminate risk exposure during refunds with advanced security protocols
  * Adhere to international compliance requirements for cross-border transactions
</Accordion>

<Accordion title="Real-time Transaction Analytics" icon="fa-chart-line">
  * Track, filter, and analyze your international transactions from the PayU dashboard
</Accordion>

<Accordion title="Real-time Fraud Detection" icon="fa-exclamation-triangle">
  * Evaluate and prevent risk in real-time to protect your business
  * Customize fraud detection with your own rules as per your business needs
</Accordion>

<Accordion title="Additional Value-Added Features" icon="fa-plus-circle">
  * **Dynamic Currency Conversion (DCC)**: Allow customers to pay in their preferred currency
  * **Multi-Currency Conversion (MCC)**: Display prices in multiple currencies
  * **EEFC (Exchange Earners’ Foreign Currency Account)**: Manage foreign currency earnings efficiently
  * **Pre-auth & Capture**: Verify card validity before completing transactions
</Accordion>

PayU’s international payment solution provides both the technical infrastructure and business tools needed to successfully expand your global footprint while maintaining a seamless customer experience.

## APIs used in Integration

<Table>
  <thead>
    <tr>
      <th>
        API
      </th>

      <th>
        Purpose
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ### Card Check
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Check is Domestic API](ref:check_is_domestic_api)
      </td>

      <td>
        Validate whether the customer's card BIN is domestic or international before initiating payment, to avoid failures on international-only flows.
      </td>
    </tr>

    <tr>
      <td>
        ### \_payment to Collect Payment
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
      </td>

      <td>
        Initiate an international card payment on the PayU-hosted page; PayU displays DCC conversion when the customer enters an international card.
      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – Merchant Hosted Checkout](ref:_payment_merchant_hosted)
      </td>

      <td>
        Submit the card payment request with international payment parameters (including optional `transactionCurrency` for MCC merchants).
      </td>
    </tr>

    <tr>
      <td>
        ### Verify the Payment
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Verify Payment API](ref:verify_payment_api)
      </td>

      <td>
        Server-side reconciliation of transaction status after payment.
      </td>
    </tr>
  </tbody>
</Table>

<br />