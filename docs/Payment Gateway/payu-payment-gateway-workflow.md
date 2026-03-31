---
title: PayU Payment Gateway Workflow
deprecated: false
hidden: false
metadata:
  robots: index
---
The following diagram illustrates how PayU payment gateway works.

<Image align="center" border={true} caption="PayU Payment Gateway Workflow" src="https://files.readme.io/e86f46efa326b45231453c864b3c325192d9f70927b617b38891175a73760e89-Payment_Checkout_Process-2026-03-31-063227.png" />

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
