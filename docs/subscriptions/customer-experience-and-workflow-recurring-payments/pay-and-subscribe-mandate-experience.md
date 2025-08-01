---
title: Pay and Subscribe Experience
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
It allows your customer to make a one-time payment or establish a mandate tailored to their specific needs. It allows merchants to enable their customers with flexible, efficient, and secure payment options. The following are some use cases:

* **Scenario 1**: Merchants, particularly in the insurance sector, can leverage this feature to collect insurance fees directly from users. This eliminates the typical wait time of T+2 days for the first premium, circumventing the prevalent ecosystem challenges associated with eNACH.
* **Scenario 2**: It also offers users the flexibility to opt for the AutoDebit feature according to their preferences, ensuring a more personalized financial management experience.

This feature is specifically designed for Insurance providers, providing them with a streamlined and efficient payment collection process.

The Pay and Subscribe supports a variety of payment flows, including eNACH, UPI Autopay, and Standing Instructions (SI) on Cards, all accessible through the PayU Checkout page. It works with PayU Hosted Checkout integration, ensuring a smooth and secure transaction experience.

> 📘 Note:
>
> The Pay and Subscribe is supported only with PayU Hosted Checkout integration. For the request and response parameters, refer to [Pay and Subscribe Consent Transaction using PayU Hosted Checkout](ref:one-time-mandate-consent-transaction).

Currently, the standard transaction flow for Pay and Subscribe transactions, integrated with a PayU Recommendation Engine and SI capabilities.

## User Journey

### Cards

1. User will land on our payment checkout page for the transaction where all the checkout-supported payment modes will be visible.

<Image align="center" width="222px" src="https://files.readme.io/c8124c0-one-time-mandate-step1.png" />

2. User will select the option for Register AutoPay for cards.

3. User will enter the card details.

<Image align="center" width="222px" src="https://files.readme.io/5460162-ome-time-mandate-cards-step2a.png" />

4. Based on mandate eligibility user will see an option to opt in for registration. 

<Image align="center" width="222px" src="https://files.readme.io/16b7e58-one-time-mandate-cards-3-register-for-subscription.png" />

5. Based on user action flow for normal transaction or mandate transaction will be executed.

<Image align="center" width="222px" src="https://files.readme.io/5611f27-one-time-card-card-otp.png" />

The payment confirmation message is displayed after successful OTP authentication.

<Image align="center" width="222px" src="https://files.readme.io/2430022-one-time-payment-success-for-all.png" />

#### Negative scenarios

If the card is not eligible, an error message is displayed below the **Enter Card Number** field similar to the following screenshot:

<Image align="center" width="222px" src="https://files.readme.io/2fc4992-one-time-time-mandate-cards-not-eligible.png" />

### UPI Intent

1. User will land on our payment checkout page for the transaction where all the checkout-supported payment modes will be visible.

<Image align="center" width="222px" src="https://files.readme.io/c8124c0-one-time-mandate-step1.png" />

2. User will select UPI to proceed with UPI transaction.
3. User will enter the VPA or UPI ID.

<Image align="center" width="222px" src="https://files.readme.io/b7fbb06-one-time-mandate-upi.png" />

4. User will see an option to opt in for registration. 

<Image align="center" width="222px" src="https://files.readme.io/a278ee8-one-time-mandate-upi-common-1.png" />

5. Based on user action flow for normal transaction or mandate transaction will be executed.

<Image align="center" width="222px" src="https://files.readme.io/2430022-one-time-payment-success-for-all.png" />

### UPI Collect

1. User will land on our payment checkout page for the transaction where all the checkout-supported payment modes will be visible.

<Image align="center" width="222px" src="https://files.readme.io/c8124c0-one-time-mandate-step1.png" />

2. User will select UPI to proceed with UPI Collect.

<Image align="center" width="222px" src="https://files.readme.io/c92f623-one-time-mandate-upi-collect.png" />

3. User will enter the UPI ID or UPI number.

<Image align="center" width="222px" src="https://files.readme.io/be181e1-one-time-upi-collect-2.png" />

4. User will see an option to opt in for registration. 

<Image align="center" width="222px" src="https://files.readme.io/00fd7bb-one-time-mandate-upi-common-1.png" />

5. Based on user action card flow for normal transaction or mandate transaction will be executed.

<Image align="center" width="222px" src="https://files.readme.io/2430022-one-time-payment-success-for-all.png" />

### Net Banking

1. User will land on our payment checkout page for the transaction where all the checkout-supported payment modes will be visible.

<Image align="center" width="222px" src="https://files.readme.io/c8124c0-one-time-mandate-step1.png" />

2. User will select **Net Banking** from the list of payment options.

3. User will the select the bank account where the Net Banking transaction will be performed.

<Image align="center" width="222px" src="https://files.readme.io/22a7c62-one-time-mandate-netbanking-1.png" />

4. User will select the checkbox and account details option will become visible to the users.

<Image align="center" width="222px" src="https://files.readme.io/9691907-one-time-mandate-netbanking-2.png" />

5. User will input the Banking details such as Account number, IFSC code, Name and Account Type on the payment page itself.

<Image align="center" width="222px" src="https://files.readme.io/0ffeb5d-one-time-mandate-netbanking-3.png" />

6. User will be asked to enter the Net Banking password.

<Image align="center" width="222px" src="https://files.readme.io/ea7d581-one-time-mandate-netbanking-password.png" />

7. User will be shown payment successful or declined page for one-time Net Banking transaction based on mandate eligibility:

* Case 1: When user opt’s for Mandate Registration along with one time payment:

<Image align="center" width="222px" src="https://files.readme.io/09ede51-one-time-mandate-netbanking-payment-successful.png" />

The user redirected to the bank page for eMandate consent.

<Image align="center" width="222px" src="https://files.readme.io/5bb9743-one-time-mandate-netbanking-emandate-bank-page.png" />

* Case 2: When user does not opt for Mandate Registration along with one time payment:

<Image align="center" className="border" width="222px" border={true} src="https://files.readme.io/46ddde2-one-time-mandate-netbanking-not-opted-mandate.png" />

* Case 3: When one time payment is declined

<Image align="center" width="222px" src="https://files.readme.io/302048b-one-time-mandate-netbanking-failed.png" />

In general, user will not be redirected to NPCI mandate creation page and will redirect back to Merchant’s url with transaction response.

1. After the transaction is successful, user will be redirected to NPCI Page where user gives consent for the mandate.

2. User will be directed to Bank’s Login Page from NPCI portal.

3. User will enter the OTP required for the transaction.
