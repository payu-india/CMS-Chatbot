---
title: 'Integrate Cross-Border Payments with PayU '
deprecated: false
hidden: false
metadata:
  title: Integrate Cross-Border Payments for PayU
  description: ' Learn how to integrate cross-border payments using PayUBiz. This guide provides detailed instructions, request parameters, and sample responses for seamless international transactions.'
  keywords:
    - Integrate Import for PayUBiz
    - Cross-Border Import for PayUBiz Integration
    - Cross Border Import for PayUBiz Integration
    - Integrate Cross-Border Import for PayUBiz
    - Cross-Border Import for PayUBiz Integration
    - ''' cross-border payments'''
    - ''' PayUBiz'''
    - ''' international transactions'''
    - ''' secure payment integration'''
    - ''' tokenization'''
    - ''' cross-border payments'''
    - ''' cross border payments'''
    - ''' PayUBiz integration for cross-border payments'''
    - ''' PayUBiz integration for cross border payments'''
  robots: index
---
This part of the document includes the steps-to-integrate for the following payment modes with various integrations:

- [ PayU Hosted Payment Integration](doc:cb-integration-non-seamless) (**Non-seamless**)
- Server-to-Server Integration (**Seamless**)
  - [ NetBanking Integration](doc:netbanking-integration-merchant-hosted-integration-cb)
  - **Cards**
    - [ Plain Cards Integration](doc:plain-cards-integration-one-time-pacb)
    - [Tokenize Card with PayU Tokenization Integration](doc:plain-cards-with-tokenization-integration-one-time-pacb)
    - [Saved Cards with a PayU Token Integration](doc:cards-with-payu-tokenization-one-time-pacb)
    - [Saved Cards with a Network Token Integration](doc:network-tokens-one-time-payment-pacb)
  - [ UPI Intent with S2S Integration](doc:pacb-upi-intent-with-s2s-integration)

<Callout icon="📘" theme="info">
  ###

  **Note:** For collecting Cross-Border Payments using PayU token, you have to perform the integration steps as in [ Tokenize Card with PayU Tokenization](doc:plain-cards-with-tokenization-integration-one-time-pacb) and then use the [Saved Cards with a PayU Token Integration](doc:cards-with-payu-tokenization-one-time-pacb).
</Callout>

The cross-border payment integration for PayU involves the following steps for the various payment methods in general:

<Cards columns={3}>
  <Card title="1. Make Payment Using Web Checkout Integration" href="step-1-make-payment-using-web-checkout-integration">
    Complete the payment process using PayU's web checkout integration

    <br />
  </Card>

  <Card title="2. Update Invoice ID (Conditional)" href="#step-2-update-invoice-id-optional">
    Optionally update the invoice ID associated with the transaction

    <br />
  </Card>

  <Card title="3. Upload the Invoices / Shipping Document (Conditional)" href="#step-3-upload-the-invoices">
    Upload invoice documents related to the completed transaction
  </Card>
</Cards>

<Callout icon="📘" theme="info">
  ###

  **Reference**: After completing the above steps, you update the invoice, as in [Integrate Cross Border Payments  ](doc:integrate-cross-border-payments-with-payu-new)>  <Anchor target="_blank" href="doc:integrate-cross-border-payments-with-payu-new#step-2-update-invoice-id-conditional">Step 2: Update Invoice ID</Anchor>
</Callout>

## Step 1: Make Payment using Web Checkout Integration

The following parameters (mandatory) must be posted using any of the following Web Checkout integration:

- [PayU Hosted Payment](https://docs.payu.in/docs/cb-integration-non-seamless)
- Merchant Hosted Checkout
  - [NetBanking Integration](https://docs.payu.in/docs/netbanking-integration-merchant-hosted-integration-cb)
  - Cards
    - [Plain Cards](https://docs.payu.in/docs/plain-cards-integration-one-time-pacb)
    - [Cards with PayU Tokenization](https://docs.payu.in/docs/cards-with-payu-tokenization-one-time-pacb)
    - [Network Tokens Integration](https://docs.payu.in/docs/network-tokens-one-time-payment-pacb)
  - [UPI Intent with S2S Integration ](https://docs.payu.in/docs/pacb-upi-intent-with-s2s-integration)

<Callout icon="👍" theme="okay">
  ###

  Experience the end-to-end **PayU Hosted > Cross-Border Payments** flow and instantly generate the complete code for seamless, zero-coding integration into your website.

    

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
                                                          font-weight: bold; /* Added this line */
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

                                                      <button onclick="window.open('https://payu.in/integrationlab/crossborder', '_blank')" 
                                                              class="tooltip-btn" 
                                                              data-tooltip="Automatically generate code including hashing for your eCommerce website to integrate Offers - PayU Hosted Checkout with zero coding knowledge.">
                                                           Experience the flow and get the code
                                                      </button>
  `}</HTMLBlock>
</Callout>

***

## Step 2: Update Invoice ID \[Conditional]

<Update_Invoice_ID />

***

## Step 3: Upload the Invoices \[Optional]

<Upload_Invoices />

<br />
