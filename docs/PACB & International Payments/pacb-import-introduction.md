---
title: PACB Import - Introduction
deprecated: false
hidden: true
metadata:
  robots: index
---
<Banner
  isInline={true}
  message="Integration effort: Some technical setup required"
  color="#FFC107"
  textColor="#000000"
  fontSize="14px"
  fontWeight="bold"
/>

## What is Cross-Border Payments – Import?

Cross-Border Payments – Import lets merchants based outside India accept payments from customers in India, without setting up a business entity in India.<br />

With Cross-Border Payments – Import:<br />

- Your customers in India pay in INR using local payment methods they already use.
- PayU processes the payment and settles the funds to your overseas bank account, in your currency, through Authorised Dealer (AD) banks.
- Settlement happens within T+2 or T+3 days.

This service follows the [RBI guidelines for Payment Aggregators – Cross Border](<redacted URL>) (RBI/DPSS/2025-26/141 CO.DPSS.POLC.No.S-633/02-14-008/2025-26).

<Callout icon="📘" theme="info">
  ### **Note**

  RBI monitors cross-border payments with the support of AD banks. That's why every transaction must carry the buyer and invoice details described on this page.
</Callout>

***

## Is Cross-Border Payments – Import Right for Me?

Cross-Border Payments – Import is a good choice if you:<br />

- **Are a merchant based outside India** and want to sell to customers in India.
- **Don't have a business entity in India** and don't want to set one up.
- **Want to offer local payment methods** such as RuPay and other Indian cards, NetBanking and UPI.
- **Want settlement in your own currency** to your overseas bank account.
- **Can handle some technical setup**, or have a developer to help.

### **Consider another PayU solution if:**<br />

- **Your business is registered in India:** Consider [PayU Hosted Checkout](doc:payu-hosted-checkout) or [Merchant Hosted Checkout](doc:merchant-hosted-checkout).
- **You're an Indian business collecting from customers outside India:** Consider [Cross-Border Payments – Export](doc:cross-border-payments-export). {/* REVIEW: confirm the Export page slug. */}

<Callout icon="far fa-face-thinking" theme="warn">
  ### **Not Sure Which PayU Solution is Right For You?**

  Tell us what you want to achieve and how you plan to accept payments. We'll recommend the PayU solution that fits your needs.<br />

  <Anchor target="_blank" href="<redacted URL>">Find the Right Product for You</Anchor> →
</Callout>

***

## What Will I Need? (Prerequisites)

You need these to get started:
- **A PayU merchant account enabled for Cross-Border Payments – Import:** <Anchor target="_blank" href="<redacted URL>">Sign up here</Anchor> if you don't have an account, then ask PayU to enable cross-border import for it.
- **An overseas bank account:** Where PayU settles your funds in your currency.
- **A website or application:** Where your customers in India will pay.
- **A way to collect buyer details:** First name, last name and billing PIN code for every transaction. Some payment methods also need the buyer's PAN and date of birth.
- **An invoicing process:** An invoice ID for every transaction, and an airway bill (AWB) once physical goods are shipped.
- **Access to your website's technical setup:** Either yourself or through a developer.


<HTMLBlock>{`
                <style>
                .tooltip-btn {
                    position: relative;
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-weight: bold;
                }
                .tooltip-btn:hover::after {
                    content: attr(data-tooltip);
                    position: absolute;
                    bottom: 125%;
                    left: 50%;
                    transform: translateX(-50%);
                    background-color: #333;
                    color: white;
                    padding: 5px 10px;
                    border-radius: 4px;
                    white-space: nowrap;
                    font-size: 12px;
                    z-index: 1;
                }
                </style>

                <button onclick="window.open('<redacted URL>', '_blank')" 
                        class="tooltip-btn" 
                        data-tooltip="Choose an integration and start building.">
                    Start Your Integration →
                </button>
`}</HTMLBlock>

***

## Supported Payment Methods

Your customers in India can pay with:<br />

- Debit Cards (including RuPay)
- Credit Cards
- NetBanking
- UPI (one-time and UPI Autopay for subscriptions)
- NEFT/RTGS bank transfers through virtual accounts

***

## Rules for Every Transaction

To meet RBI requirements, every cross-border import transaction must follow these rules:<br />

| Rule              | What you need to do                                                                                  |
| :---------------- | :--------------------------------------------------------------------------------------------------- |
| Transaction limit | Don't sell products or services for more than ₹25,00,000 (about USD 27,000) in a single transaction. |
| Buyer details     | Send the buyer's first name, last name and billing PIN code.                                         |
| Invoice ID        | Send an invoice ID with every transaction, and upload the invoice to PayU.                           |
| Proof of shipment | For physical goods, upload a copy of the airway bill (AWB) once the goods are shipped.               |

***

## How Does My Customer Pay?

The following is the customer journey for a card, NetBanking or UPI payment:

1. Customer clicks **Pay Now** on your website or app.
2. Your website starts a payment with PayU and sends the buyer and invoice details.
3. Customer pays in INR using their Indian card, NetBanking or UPI.
4. PayU processes the payment and sends you the result.
5. You upload the invoice (and the AWB for physical goods) to PayU.
6. PayU settles the funds to your overseas bank account in your currency within T+2 or T+3 days.

For bank transfers, the customer instead sends NEFT/RTGS to a virtual account that PayU provides. See [Virtual Account-Based Local Wire Transfers](doc:virtual-account-based-local-wire-transfers).<br />

<Columns layout="fixed">
  <Column>
    For the full flow between you, PayU and the AD bank, see [Workflow for Cross-Border Payments – Import](doc:workflow-for-cross-border-payments-import).
  </Column>
</Columns>

***

## What Happens After a Payment

After the customer completes a payment:<br />

- PayU determines the transaction result and sends you a payment response.
- You upload the invoice for the transaction, and the AWB once physical goods are shipped.
- PayU settles the funds to your overseas account in your currency through the AD bank.

<Callout icon="⚠️" theme="warn">
  ### **Important**

  - Don't treat the browser redirect alone as confirmation that a payment succeeded. Verify the payment status with PayU's Verify Payment API or webhooks.
  - Settlement depends on the invoice upload. Upload invoices for every successful transaction.
</Callout>

***

## Choose Your Integration

| Integration                               | Best for                                                               | Guide                                                                                        |
| :---------------------------------------- | :--------------------------------------------------------------------- | :------------------------------------------------------------------------------------------- |
| PayU Hosted Checkout                      | Using PayU's ready-made payment page                                   | [PayU Hosted Checkout Integration](doc:cb-integration-non-seamless)                          |
| Merchant Hosted: Cards                    | Collecting card details on your own page (PCI DSS compliance required) | [Plain Cards Integration](doc:plain-cards-integration-one-time-pacb)                         |
| Merchant Hosted: Saved and network tokens | Repeat customers paying with saved cards                               | [Cards with PayU Tokenization](doc:cards-with-payu-tokenization-one-time-pacb)               |
| Merchant Hosted: NetBanking               | Bank payments from your own page                                       | [NetBanking Integration](doc:netbanking-integration-merchant-hosted-integration-cb)          |
| Merchant Hosted: UPI Intent               | UPI payments that open the customer's UPI app                          | [UPI Intent with S2S Integration](doc:pacb-upi-intent-with-s2s-integration)                  |
| Subscriptions                             | Recurring payments with UPI Autopay                                    | [Subscriptions with Cross-Border Payments](doc:cb-subscription-integration-seamless)         |
| Virtual accounts                          | High-value NEFT/RTGS bank transfers                                    | [Virtual Account-Based Local Wire Transfers](doc:virtual-account-based-local-wire-transfers) |

***

## Why Use Cross-Border Payments – Import?

<Accordion title="Key Benefits" icon="fa-rocket">
  - **Enter the Indian market without a local entity:** PayU operates as the payment aggregator, so you don't need a business presence in India.

  - **Local payment methods:** Accept Indian debit cards (including RuPay), NetBanking and UPI, which customers in India prefer and which have higher success rates.

  - **Settlement in your currency:** Receive funds in your currency (100+ options) in your overseas account.

  - **Fast settlement:** Funds are settled within T+2 or T+3 days.

  - **One point of contact:** Raise reconciliation and settlement queries directly with PayU.
</Accordion>

***

## Next Steps

<Cards columns="3">
  <Card title="How It Works" href="doc:workflow-for-cross-border-payments-import">
    Understand the cross-border import flow, roles and settlement.
  </Card>

  <Card title="Integrate Cross-Border Payments" href="doc:integrate-cross-border-payments-for-payubiz">
    Choose an integration, build and test it.
  </Card>

  <Card title="FAQs" href="doc:faqs-for-cross-border-payments">
    Answers on invoices, settlement, currencies and UDFs.
  </Card>
</Cards>