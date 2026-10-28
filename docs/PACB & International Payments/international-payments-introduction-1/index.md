---
title: International Payments Introduction
deprecated: false
hidden: true
metadata:
  robots: index
---
<Banner color="#FFC107">Minimal technical setup required</Banner>

## What are international payments?

International card payments are payments made with a card issued outside India, for goods or services you sell from India. With PayU, you can accept cards issued in over 150 countries on Visa, Mastercard and American Express, without building a separate payment setup for each country.

PayU offers two ways to handle the currency:

* **Dynamic Currency Conversion (DCC):** you price in INR. When the customer enters an international card, PayU shows the amount in the card's currency and lets the customer choose which currency to pay in. PayU manages the <Glossary>exchange rate</Glossary>, and you're settled in INR.
* **Multi-Currency Conversion (MCC):** you show prices in the customer's currency, for example USD or AED, and send that currency in the payment request. You manage the exchange rate, and the customer pays in the currency you set.

Watch this overview of international payments:

<Embed title="" typeOfEmbed="youtube" url="https://www.youtube.com/watch?v=rEBQ5ZF9KkI" href="https://www.youtube.com/watch?v=rEBQ5ZF9KkI" providerName="YouTube" providerUrl="https://www.youtube.com" />

***

## Is it right for me?

International payments suit you if:

* you sell online to customers outside India, for example in travel, education, software or e-commerce
* your customers pay with cards issued abroad
* you want customers to see prices or pay in a currency they understand

### <Glossary>DCC</Glossary> or <Glossary>MCC</Glossary>?

|                                 | **Dynamic Currency Conversion (DCC)**                                                     | **Multi-Currency Conversion (MCC)**                                                                                                            |
| :------------------------------ | :---------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| **Who sets the currency**       | The customer chooses on the PayU currency page                                            | You set it in the payment request                                                                                                              |
| **Price shown on your website** | INR                                                                                       | The customer's currency                                                                                                                        |
| **Exchange rate**               | Managed by PayU                                                                           | Managed by you, from PayU's rates or your own source                                                                                           |
| **Currencies**                  | 135+                                                                                      | 27+                                                                                                                                            |
| **Settlement**                  | INR                                                                                       | INR or other currencies                                                                                                                        |
| **Refunds**                     | Raised in INR                                                                             | Raised in the original payment currency                                                                                                        |
| **Integration change**          | None on PayU Hosted Checkout. On Merchant Hosted Checkout, handle the PayU currency page. | Send `<Glossary>transactionCurrency</Glossary>` and `<Glossary>api_version</Glossary>`, and add the currency to the <Glossary>hash</Glossary>. |

{/* REVIEW: currency counts follow the 2025 International Card Payments Dev Guide (135+ DCC, 27+ MCC). The MCC currency table currently lists 24 codes. */}

<Callout icon="💡" theme="info">
  ### **Not sure which option to choose?**

  Choose **DCC** if you want to keep pricing in INR and let PayU handle conversion. Choose **MCC** if you want to show local prices on your website and control the exchange rate. Your PayU Key Account Manager can help you decide.
</Callout>

***

## What will I need?

* A PayU merchant account. If you don't have one, [register for a merchant account](doc:register-for-a-merchant-account-on-dashboard).
* International payments enabled on your account. Contact your PayU Key Account Manager, and say whether you want DCC, MCC or both.
* The documents PayU asks for when enabling international payments, such as bank statements or <Glossary>ITR</Glossary>s, audited balance sheets, and any licence your business needs (for example an import/export, <Glossary>FSSAI</Glossary> or <Glossary>IATA</Glossary> certificate). For the full list, see the [FAQs](doc:faqs-dynamic-currency-conversion).
* For Merchant Hosted Checkout with cards: PCI DSS compliance, because card details are collected on your page.
* Test cards for international payments. See [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets).

<Anchor target="_self" href="doc:payu-hosted-checkout-integration-dynamic-currency-conversion">Start integrating</Anchor>

***

## Supported cards

| Card type     | Networks                           |
| :------------ | :--------------------------------- |
| Credit cards  | Visa, Mastercard, American Express |
| Debit cards   | Visa, Mastercard                   |
| Prepaid cards | Visa, Mastercard                   |

<Callout icon="📘" theme="info">
  ### **Note**

  DCC and MCC apply to **card payments only**. The card's issuing currency is identified from the card number.
</Callout>

{/* REVIEW: confirm networks supported for international debit and prepaid cards. */}

***

## How does my customer pay?

### With DCC

1. The customer chooses a product on your website. The price is in INR.
2. The customer enters an international card on your checkout or on PayU Hosted Checkout.
3. PayU detects that the card's currency isn't INR and shows the amount in both currencies, with the exchange rate.
4. The customer chooses to pay in their card's currency or in INR.
5. The customer completes <Glossary>3D Secure</Glossary> authentication and the payment is processed in the chosen currency.
6. The customer returns to your website and sees the order confirmation.

### With MCC

1. The customer sees prices on your website in their own currency.
2. You start the payment with PayU in that currency.
3. The customer enters their international card details and completes authentication.
4. The payment is captured in the currency you sent.
5. The customer returns to your website and sees the order confirmation.

For screenshots of both journeys, see [How International Payments Work](doc:dynamic-currency-conversion-workflow).

***

## What happens after a payment

* **Confirmation:** PayU sends the result to your `surl` or `furl`. Always check the response hash and confirm the status with the Verify Payment API or a webhook before you fulfil the order.
* **Settlement:**
  * **DCC:** you're settled in INR.
  * **MCC:** you can be settled in INR or in other currencies, depending on your account setup.
* **Refunds:**
  * **DCC:** raise the refund in INR, for the original INR amount. PayU converts it to the currency the customer paid in.
  * **MCC:** raise the refund in the original payment currency.

<Callout icon="🚧" theme="warn">
  ### **Watch Out!**

  For DCC payments, card networks require your invoice or receipt to show the INR amount, the exchange rate and <Glossary>markup</Glossary>, the converted amount and currency, and that the customer chose the currency. Check that your order confirmation includes these details.
</Callout>

***

## Why use it?

<Accordion title="Key benefits" icon="fa-star">
  * **Global reach:** accept cards issued in over 150 countries.
  * **Pay in a familiar currency:** customers see and pay in their own currency, which makes the payment clearer.
  * **No exchange-rate work with DCC:** PayU manages the rate and you're settled in INR.
  * **Local pricing with MCC:** show prices in 27+ currencies and refund in the original currency, which reduces exchange-rate losses.
  * **Flexible settlement:** receive funds in INR or in other currencies.
  * **Secure:** 3D Secure 2.0 authentication and real-time fraud checks, with rules you can customise.
  * **Reporting:** track and filter international payments on the PayU Dashboard.
  * **More options:** <Glossary>EEFC</Glossary> accounts for foreign-currency earnings, and pre-authorisation and capture.
</Accordion>

***

## Next steps

<Cards columns="3">
  <Card title="How it works" href="doc:dynamic-currency-conversion-workflow" icon="fa-network-wired">
    See the DCC and MCC customer journeys.
  </Card>

  <Card title="Integrate" href="doc:payu-hosted-checkout-integration-dynamic-currency-conversion" icon="fa-code">
    Integrate with PayU Hosted or Merchant Hosted Checkout.
  </Card>

  <Card title="FAQs" href="doc:faqs-dynamic-currency-conversion" icon="fa-circle-question">
    Find answers on settlement, refunds and documents.
  </Card>
</Cards>
