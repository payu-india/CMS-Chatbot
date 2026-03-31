---
title: Overview
deprecated: false
hidden: false
metadata:
  title: Collect Payments Introduction
  keywords:
    - Collect Payments Introduction
  robots: index
---
A **payment gateway** enables businesses to securely accept payments from customers through their website or mobile application. The **PayU Payment Gateway** acts as a secure bridge between your customer, your application, and the banking networks to process transactions safely and reliably.

<Accordion title="Benefits" icon="fa-lightbulb">
  * **Secure and Reliable Transactions**: The PayU Payment Gateway ensures that every transaction is securely processed using encryption and industry-standard safeguards, helping protect customers from fraud and unauthorized access.
  * **Faster and Smoother Payments**: PayU provides an optimized checkout experience that reduces friction and enables quick transaction processing, ensuring a smooth payment journey for customers.
  * **Reduced Payment Failures**: With real-time transaction handling and intelligent processing, PayU helps minimize failed payments and improves overall payment success rates.
  * **Multiple Payment Options**: PayU enables businesses to accept a wide range of payment methods including cards, UPI, net banking, and wallets, offering flexibility and convenience to customers.
  * **Improved Customer Experience**: A seamless and intuitive payment flow helps customers complete transactions quickly, enhancing trust and satisfaction.
  * **Flexible Integration Options**: PayU offers multiple integration methods such as Hosted Checkout, Web Checkout, and APIs, allowing businesses to choose what best fits their needs.
  * **Better Conversion Rates**: A smoother payment experience leads to fewer drop-offs during checkout, helping businesses improve conversion rates and revenue.
  * **Scalable and Business-Friendly**: PayU is built to handle growing transaction volumes, making it suitable for businesses of all sizes across web and mobile platforms.
  * **Developer-Friendly**: With simple integration options and support for multiple tech stacks, PayU enables developers to go live quickly and efficiently.
  * **Operational Efficiency**: PayU simplifies payment management with centralized tracking and reporting, reducing manual effort and improving operational workflows.
</Accordion>

## How PayU Payment Gateway Works

The following diagram illustrates how PayU payment gateway works.

<Image align="center" border={true} caption="PayU Payment Gateway Workflow" src="https://files.readme.io/c7438f5e473e942bca45e172732f5c92803419d8a7b2ee2869894f73973ec0fe-Payment_Checkout_Process-2026-03-31-063227.png" />

<Accordion title="Step 1: Customer Initiates a Payment" icon="fa-check">
  A customer selects products or services on your website or app and clicks on “Pay Now” at checkout.
</Accordion>

<Accordion title="Step 2: Customer Provides Payment Details" icon="fa-check">
  The customer enters their payment details (card, UPI, net banking, wallet, etc.) on the PayU-hosted or integrated checkout page.
</Accordion>

<Accordion title="Step 3: PayU Encrypts the Data" icon="fa-check">
  PayU securely encrypts the payment information to ensure sensitive data is protected during transmission.
</Accordion>

<Accordion title="Step 4: Request Sent to an Acquiring Bank" icon="fa-check">
  The encrypted payment request is sent to the acquiring bank (the bank that processes payments for the merchant).
</Accordion>

<Accordion title="Step 5: Card Network or Payment Method Routing" icon="fa-check">
  If it is a card payment, the request is routed through the supoorted card network (like Visa, Mastercard, etc.).
</Accordion>

<Accordion title="Step 6: Issuing Bank Verifies Payment" icon="fa-check">
  The issuing bank (customer’s bank):

  * Verifies if the account has sufficient balance and payment details are valid
  * Performs authentication (like OTP or 3D Secure)
</Accordion>

<Accordion title="Step 7: Issuing Bank Gebnerates the Authorization Response" icon="fa-check">
  The issuing bank approves or declines the transaction and sends a response back through the same chain (network → acquiring bank → PayU).
</Accordion>

<Accordion title="Step 8: PayU Shares the Response with Merchant and Customer" icon="fa-check">
  PayU receives the response and displays the final status (success or failure) to the customer on the checkout page. The merchant system is also updated with the transaction result.
</Accordion>

## Types of Checkout

PayU offers the following checkout types:

<HoverCardGrid
  columns={3}
  items={[
    {
      title: 'PayU Hosted (Prebuilt Web)',
      href: '/docs/prebuilt-checkout-payu-hosted',
      text:
        "- Easier and faster integration.\n" +
        "- Redirect customers to PayU pages.\n" +
        "- No PCI-DSS certification required.",
    },
  ]}
/>
