---
title: PayU Hosted Checkout Overview
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Prebuilt Web Checkout or PayU Hosted Checkout Integration
  description: >-
    Understand PayU Hosted Checkout for payment gateway integration. Learn
    payment flow, key concepts, and how to handle online payments securely.
  keywords:
    - PayU Hosted Checkout
    - payment gateway integration
    - payment flow
    - online payments
    - PayU integration
  robots: index
next:
  description: ''
---
This page helps you understand how **PayU Hosted Checkout** works before you begin integration.

## What is PayU Hosted Checkout?

PayU Hosted Checkout is a payment integration method where:

* You redirect users from your website to a **PayU-hosted payment page**
* PayU handles the entire payment experience, including security and processing
* After the payment is completed, users are redirected back to your website

This is the **simplest and fastest way** to start accepting payments without building or managing your own payment UI.

***

## How Payment Flow Works

The payment journey in Hosted Checkout looks like this:

<Image align="center" alt="PayU Hosted Checkout Workflow" border={true} src="https://files.readme.io/932f800-payuhosted_wf.png" className="border" />

<Accordion title="Step 1: Initiate Payment" icon="fa-shopping-cart">
  Customer selects items and initiates the payment on the merchant website.
</Accordion>

<Accordion title="Step 2: Redirect to PayU" icon="fa-external-link-alt">
  Customer is redirected to PayU Checkout to enter payment details.
</Accordion>

<Accordion title="Step 3: Send to Bank" icon="fa-paper-plane">
  PayU sends the payment request with transaction details to the bank or provider.
</Accordion>

<Accordion title="Step 4: Process Payment" icon="fa-university">
  The bank processes the transaction and returns a success or failure status to PayU.
</Accordion>

<Accordion title="Step 5: Return Response" icon="fa-reply">
  PayU redirects the customer back to the merchant website with the payment result.
</Accordion>

This flow ensures that sensitive payment data is handled by PayU, reducing your security and compliance overhead.

## Customer journey

Below diagram depicts the end user experience during a payment using PayU Hosted Checkout:

<Image align="center" src="https://files.readme.io/bc1c758a83c0c601d161a5621e1fe47a6d4c757e847a893b33b05419972e693a-b7b3bc19c28693be346591ec8a2c29ee07fcf47cb088bc6c9a6c34950c2af0dc-payu_hosted_checkout-workflow.png" />

The following is the customer journey using cards as a payment method:

<Accordion title="Customer initiates payment" icon="fa-info-circle">
  The customer clicks **Pay Now** on your website or app.
</Accordion>

<Accordion title="Redirect to Hosted Checkout" icon="fa-info-circle">
  The customer is redirected from your website to the PayU Hosted Checkout page.
</Accordion>

<Accordion title="Customer enters payment details" icon="fa-info-circle">
  On the hosted page, the customer:

  * Selects a payment method. Here is it Cards (Credit/Debit)
  * Enters required payment details
  * Confirms the payment
</Accordion>

<Accordion title="Payment is processed by the gateway" icon="fa-info-circle">

  PayU securely communicates with the bank or payment provider to process the transaction.

</Accordion>

1. The customer clicks **Pay Now** on merchant website after checkout.
2. The customer is redirected to _PayU Payment _page.

<Image align="center" alt="PayU Hosted Checkout Custome Journey Sample with Payment Modes" border={true} width="622px" src="https://files.readme.io/1ee3893480e6e3d3c1e28d6ecffc4c52d1b3e8f2aba0247c9eb486dfef0fafc5-Screenshot_2024-09-06_at_11.54.02_AM.png" className="border" />

3. The customer chooses a payment mode from the _PayU Payment_ page. For example, **Cards (Debit/Credit)**.
4. The card details are provided by the customer and clicks **Proceed**.

<Image align="center" alt="PayU Hosted Checkout Custome Journey Sample with Card Details page" border={true} width="622px" src="https://files.readme.io/fd09cbd284ffe7fb3b60d03e2acd8a5a51d850dd1795f1eca9879893b3569603-Screenshot_2024-09-06_at_11.56.40_AM.png" className="border" />

A consent message is displayed whether the card the details can be stored.

<Image align="center" alt="PayU Hosted Checkout Custome Journey Sample with Save Card Confirmation" width="622px" src="https://files.readme.io/caa8481-Screenshot_2023-10-05_at_10.37.33_AM.png" />

5. Customer clicks **Save and Continue**.
6. The OTP page is displayed where the customer enters OTP sent to the them.

<Image align="center" width="422px" src="https://files.readme.io/289fa82-Screenshot_2023-10-05_at_10.37.42_AM.png" />

6. PayU redirects back to the merchant website based on the success URL (surl) or failure URL (furl) specified.

## Features of PayU Hosted Checkout

PayU manages the checkout experience on your website. The features of PayU Hosted Checkout are:

* Enables the customer to select the payment option through the readymade payment page hosted on the PayU server, and accept corresponding payment details. After submitting the details, PayU will take the customer to the desired payment options webpage for further authentication. For configuring payment modes on payment page, refer to [Configure Checkout Payment Methods](https://docs.payu.in/docs/payu-payment-page-customization#configure-checkout-payment-methods-and-settings).
* Facilitates access to color schemes, customize logo, and display language (some Indian languages supported) though PayU owns this page. For more information, refer to [Change the Language](https://docs.payu.in/docs/payu-payment-page-customization#change-the-language)  and  [Configure Checkout Settings](https://docs.payu.in/docs/payu-payment-page-customization#configure-checkout-payment-methods-and-settings).
* Enables easy and quick integration so you can integrate with minimal technical knowledge.

Web Checkout provides multiple payment options that can be easily pre-configured by you on-demand, according to your business case. You can execute PayU Hosted Checkout integration efficiently with PayU web payments systems using a PG integration kit provided by PayU.

## Benefits of PayU Hosted Checkout

The following is a list of benefits of PayU Hosted Checkout:

* Simplified payment workflow for your customers while reducing the cost of designing complex payment functionalities within your environment.
* Going live with new payment modes requires zero development. They can be enabled with a simple switch.
* Assures the security of your customer payment credentials.
* PCI-DSS certifications to operate your facility are not mandatory.
* PayU Hosted Checkout extends cross-functional support at organizational roles within the organization.
* The Native UI feature of Web Checkout Pro allows you to ensure continuous usability (UX) and brand coherence by customizing the PayU-hosted environment with the business logo and color scheme of your choice, simulating your business website.
* Offers zero direction OTP authentication flow for cards with Native OTP.
* Supports specific and generic intent for UPI payments on mobile web
* Personalized payment experience (using recommendations) and offers.

## Next Steps

To integrate PayU Hosted Integration on your website or mobile, refer to:

* [Web Integration - PayU Hosted](https://docs.payu.in/docs/prebuilt-checkout-page-integration) using the **Collect Payment **API (**_payment** API),

* [Integrate WebView for Mobile Apps](https://docs.payu.in/docs/webview-for-mobile-apps) by embedding PayU's Hosted Checkout experience inside a WebView container within your mobile app.

<br />

<Callout icon="📮" theme="default">
  **Postman Collection**: Download the PayU Hosted Checkout Postman Collection from the following location:

  [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/collection/rocz44o/payu-hosted-checkout-collection-complete-integration](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/collection/rocz44o/payu-hosted-checkout-collection-complete-integration)
</Callout>

<br />
