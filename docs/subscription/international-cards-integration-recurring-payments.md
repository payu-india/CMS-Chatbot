---
title: SI on International Cards
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Recurring Payments Integration for International Cards
  description: "Integrate recurring payments for international cards effortlessly with PayU’s robust API. PayU has made tokenization obligatory for\_international cards SI. Currently, PayU only permits a challenge-based process for mandate registration, that is, OTP verification is required for an active mandate setup. PayU India devguide covers everything from setup to execution, ensuring a smooth subscription experience."
  keywords:
    - International Recurring Payments Workflow
    - International Subscription Payment Workflow
    - International Automated Billing Workflow
    - International Recurring Transaction Steps
    - International Membership Payment System
    - International Scheduled Payment Integration Workflow
    - International Recurring Charge Mechanism
    - International Periodic Billing Workflow
    - Continuous Payment Setup Workflow
    - APIs for International Recurring Payments
  robots: index
next:
  description: ''
---
PayU supports recurring payments for international cards. PayU has made tokenization obligatory for international cards SI. Currently, PayU only permits a challenge-based process for mandate registration, that is, OTP verification is required for an active mandate setup.

## Workflow

1. Use Card Bin Info API to check if the card BIN is international. For more information, refer to [Check is Domestic API](ref:check_is_domestic_api).

2. The registration and recurring process is same as the current workflow for cards issued in India, where, authentication and authorisation will be done on user’s card.  For more information, refer to  [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted) or [Payment Consent Transaction with Merchant Hosted Checkout](ref:payment-consent-transaction-merchant-hosted)

   In the response of the \*\*\_payment\*\* API used for register a payment consent transaction, you can check the carttype response parameter to check if it is a domestic or international card.

3. After authorisation, the card must be tokenised either via PayU or by merchants. In case of Network token flow, authentication will be done directly through tokenised cards.

4. Post tokenisation, the registration procedure will be executed, and consent will become active in the system.

5. The merchant will initiate the **Pre-Debit Notification** API, and PayU will respond with a successful confirmation in realtime. For more information, refer to [Pre-Debit Notification API](ref:pre_debit_notification_api)

6. Following the Pre-Debit Notification call, the merchant will independently handle all the subsequent transactions based on subscription setup ie. billing amount, start date, end date.

7. The **Recurring Payment** API will directly deduct the required amount. For more information, refer to [Recurring Payment Transaction API](ref:recurring_payment_api).

### Supported Flow and Scope

- **Flow Supported**: PayU Tokenised Flow, Merchant Tokenised Flow (Plain Card Registration + Update Token) &  Network Token Registration. For more information, refer to the following:
  - [Payment Consent Transaction](ref:payment-consent-transaction-merchant-hosted)
  - [Modify the Recurring Payments for a Card](ref:modify-the-recurring-payments-for-a-card)
- **Current Scope**: Card Issuer is Non-Indian, Merchant is registered in India, and Transaction currency is INR. 
- **Frequency Supported:** ADHOC

## Supported payment instruments

PayU supports the following networks and card types:

### Supported networks

- Visa 
- MasterCard

### Supported card types

- Credit Card
- Debit Card