---
title: 2. Test Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: >-
    Learn how to test your integration with PayU’s Hosted Checkout solution
    before going live. This page provides information on how to use PayU’s Test
    Environment with a test card example, and test scenarios to verify your
    payment flow.
  robots: index
next:
  description: ''
---
<UPIIntentCallout />

<TestingChecklist />

To test the PayU Hosted Checkout integration:

1. After the items are added to cart, click Pay to redirect to the _PayU Payment_ page.

   If any error message is displayed, refer to [Error Handling ](/docs/error-handling)and troubleshoot the error accordingly.

2. Check if all the payment modes are listed. 

   If any payment of the payment modes are listed not listed, contact your KAM or PayU Support.

3. Select a payment mode. For example, **Credit Card**.

4. Enter the card details and click **Proceed**. For example, use the following test credit card details:

   - Card No.: 5123-4567-8901-2346
   - Expiry Date: Any future date
   - CVV: 123
   - Name on Card: Any name 

    For more test card details, refer to [Test Cards, UPI ID and Wallets](/docs/test-cards-upi-id-and-wallets).

    A dummy bank OTP page is displayed.

5. Enter the OTP as 123456 for the test card.