---
title: Customer Journey for Merchant Hosted Checkout
deprecated: false
hidden: true
metadata:
  robots: index
---
This section describes the customer journey for Subscriptions with Merchant Hosted Checkout (Seamless) integration.

## Net Banking

Net Banking recurring like cards are processed seamlessly without the customer’s intervention and any 2FA.
There are two common terms in Net Banking recurring:

* <Glossary>Registration transaction</Glossary>(also known as e-Mandate transaction)
* Payment transaction (also known as e-NACH transaction or SI transaction).

<Callout icon="📘" theme="info">
  **Note**: Effective from 1st April 2024, mandates can be issued for a maximum duration of 40 years from the date of issuance.
</Callout>

### Registration transaction workflow

The steps involved in a registration transaction (e-Mandate) are:

1. This is usually an INR 0.00 (zero rupee) transaction hence it is called a registration transaction.

> 📘 Notes:
>
> * Upfront payment can be collected only through direct integration – HDFC Bank and ICICI Bank. For all the 40+ banks supported through NPCI, you cannot collect the upfront amount and perform only the INR 0.00 authentication.
> * Upfront payment can be collected only through direct integration – HDFC Bank**(₹1 Lakh)** and ICICI Bank.

2. Merchant presents an option to sign up for a recurring platform where the customer needs to provide his/her consent.
3. Billing details like amount, frequency, start date, and end date of the subscription need to be presented to the customer and passed to PayU during payment request.
4. On redirecting to PayU:
   * **Non-Seamless Integration**: The customer selects preferred bank and enters account details like account number, name of the account, and account type: Savings or Current.
   * **Seamless Integration**: Merchant has to send all the parameters, that is, preferred bank, account number, name of the account, and account type.

<Image align="center" border={true} width="512px" src="https://files.readme.io/6cccafc-recurring_payment_netbanking_workflow_step4.png" className="border" />

<Image align="center" border={true} width="512px" src="https://files.readme.io/6ba7e05-recurring_payment_aadhaar_step1.png" className="border" />

5. The customer is redirected to the any of the following based on authentication selected:
   1. Bank’s login page and authenticates himself with either net banking username and password or debit card number and ATM PIN depending upon the preferred bank.
   2. NPCI page for the Aadhaar authentication. For more information, refer to [eNACH Aadhaar Authentication](#enach-aadhaar-authentication).
6. On successful authentication, the customer sees registration details like billing amount, billing frequency, start date, and end date of the subscription plan.
7. The customer approves the subscription details from the bank page using standard 2FA flow and gets redirected back to PayU'
8. On receiving either of the response from the bank, the same is communicated back to the merchant on a real-time basis.

#### eNACH Aadhaar Authentication

In Step 5 above, the customer is redirected to NPCI page for the Aadhaar authentication, so the additional steps involved for Aadhaar authentication are:

1. Customer enter their Aadhaar card number in the **Aadhaar Card Number** field and clicks **Confirm**.

<Image align="center" border={true} src="https://files.readme.io/b3f6343-enach-aadhaar-step1.png" className="border" />

2. Customer enter the OTP in the **OTP** and **Confirm OTP** fields that is received to the mobile phone registered with Aadhaar, and then clicks **Continue**.

<Image align="center" border={true} src="https://files.readme.io/4d3d281-enach-aadhaar-step2.png" className="border" />

3. Customer enter the OTP that is sent by to bank to the registered mobile number and clicks **Continue**.

<Image align="center" border={true} src="https://files.readme.io/be47075-enach-aadhaar-step3.png" className="border" />

The transaction status is displayed similar to the following screenshot:

<Image align="center" border={true} src="https://files.readme.io/b3f78b9-enach-aadhaar-step4.png" className="border" />

### Recurring transaction workflow

The steps to perform a recurring transaction for Net Banking are:

1. After registration is successful, the merchant can call the recurring payment API of PayU by passing the unique PayU ID received in the response to the registration transaction.
2. All the transaction requests coming from the merchant are queued and forwarded to acquirers through a file. This is performed since most of the time even payment processing for Net Banking recurring is offline.
3. The real-time response for Recurring transactions to the merchant is always returned as Pending. For direct integration with ICICI bank, the response will be real-time.
4. For NPCI-supported banks and HDFC direct Integration, the response of the transaction is received over SFTP from acquirers at the end of the day, which is then stored in PayU’s DB, and the same is communicated to the merchant over a webhook API call.
5. TAT for receiving either Success or Failure case of e-NACH transactions is T+2 similar to the registration transaction.

<Callout icon="📘" theme="info">
  **Note**: Banks do not support refunds for Net Banking Recurring Payment transactions (or e-NACH transaction) so you will get an error message, “Refund not accepted for txn” with the error code 232. For the list of banks supporting e-NACH, refer to [Bank Codes - Recurring Payments](doc:bank-codes-recurring-payments).
</Callout>

For Net Banking, there are three methods to authenticate:

1. Net Banking Login credentials
2. Debit Card Number with an OTP
3. Aadhaar number with an OTP

You can use Recurring Payment API or bulk upload on PayU Dashboard. For more information, refer to the following sections:

* [Recurring Payment Transaction API](ref:recurring_payment_api) for Recurring Payment API.
* [Using PayU Dashboard](https://docs.payu.in/docs/subscription-dashboard/) for payment links using PayU Dashboard.

For the list of banks supported for the Net Banking recurring platform and their bank codes, refer to [Bank Codes - Recurring Payments](doc:bank-codes-recurring-payments) .

### Transaction limits

The transaction limit for recurring payments using Net Banking is as follows:

* Net Banking: Rs.10,00,000
* Aadhaar based eSign or eNACH Aadhaar Authentication: Rs.1,00,000

## Cards

For cards, the recurring payments do not require the customer’s involvement for completing the transactions. The transactions are processed without the CVV/CVV2 and Two Factor Authentication (2FA). Recurring Payments provides a hassle-free payment experience to the customer if they had already provided the consent for allowing the merchant to charge their card regularly.

Since Recurring Payments do not have 2FA, the following are the strict guidelines from RBI apply:

* The first transaction must go through the standard 2FA flow (OTP/Mastercard secure password/verified by Visa password) where the customer’s consent for further recurring payments needs to be taken either by merchant (seamless flow) or PayU (non-seamless flow). For more information on PayU workflow to do the first transaction, refer to [Registration Transaction Workflow](#registration-transaction-workflow).
* After the consent is taken, the merchant can use either S2S APIs or the File upload utility of PayU to charge the customer regularly without the 2FA. For more information on PayU Recurring Payment workflow, refer to [Recurring Transaction Workflow](#recurring-transaction-workflow).

<Image align="center" border={false} width="600px" src="https://files.readme.io/b8710f1-rp_cc_workflow_1.png" />

### How do Recurring Payments work?

1. Customer lands on the merchant website and proceeds for payment.
2. Merchant presents an option to sign up for on the recurring platform where the customer must provide his/her consent.
3. Billing details like amount, frequency, start date and end date of the subscription are presented to the customer and passed to the PayU during payment request.
4. After the customer validates the subscription plan and enters the preferred card details, the customer is redirected to the 3D Security (3DS) flow where the authentication and authorization process place.
5. There are multiple ways to process the First transaction/Consent transaction to obtain the customer’s consent:  
   a. A consent transaction can be an actual subscription for the First billing cycle so that the customer will be charged for the whole amount through 3DS (2FA) flow and subsequent transactions will be processed through the recurring payment.
   b. A consent transaction can be a small transaction (like 5 INR) where the customer’s card is taken on file along with consent and the amount is refunded back by the merchant on calling the Refund API. This method is popular where the merchant offers their free services for the first billing cycle and then charges subsequent bills through the recurring payments.
6. After the customer’s consent is taken, the card details are saved in the PayU’s secure vault and a card token is generated.
7. The card token is returned to the merchant in the payment response along with PayU’s ID. Merchant is supposed to map this PayU ID it against customer’s profile so that henceforth it can be used charging customer through the recurring platform.

> 📘 Notes:
>
> * The card token is not an actual card number, and hence merchant is not having any PCI DSS hassles in storing the same at his end.
> * The recurring limit without the requirement of 2FA is increased to ₹15,000. For more information, refer to [Reserve Bank of India - Notifications](https://www.rbi.org.in/scripts/FS_Notification.aspx?Id=12341\&fn=9\&Mode=0) )
> * In addition, the recurring limit for certain merchant categories has been increased from ₹15,000/- to ₹1,00,000/- per transaction for the following categories. For more information, refer to  [Reserve Bank of India - Notifications](https://www.rbi.org.in/scripts/NotificationUser.aspx?Id=12570\&Mode=0)):
>   1. subscription to mutual funds
>   2. payment of insurance premiums
>   3. credit card bill payments

At present, Standing Instruction is supported for the following payment instruments:

* Credit Card (scheme-wise, all issuers are supported)
  * Visa
  * Master Card
  * American Express
* Debit Card (only Visa and Master Card schemes and selected issuers)

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>

      </th>

      <th>

      </th>

      <th>

      </th>

      <th>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        * American Express Banking Corporation
      </td>

      <td>
        * City Union Bank Ltd.Dhanlaxmi Bank Ltd.
      </td>

      <td>
        * IDFC First Bank Ltd.
      </td>

      <td>
        * Punjab National Bank
      </td>
    </tr>
  </tbody>
</Table>

### Cards registration transaction workflow

Merchant presents an option to sign up for a recurring platform where the customer needs to provide his/her consent. Billing details like amount, frequency, start date, and end date of the subscription need to be presented to the customer and passed to PayU during payment request.

The workflow for first-time payment involves:

1. When the customer attempts a transaction for the first time, the customer must complete the transaction by entering the card details (CVV, Expiry and Card number) and the OTP on the Issuing Bank’s webpage. To handle a standing instruction for a customer, the merchant would need to use a post parameter (SI).

<Image border={false} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-14-at-7.40.54-AM-1-1-1024x978.png" />

2. During this first transaction, the merchant must post this parameter depending on the decision of the customer at their website.
3. If the value of the SI parameter is 1 from the merchant, the following message is displayed to the customer.  
   **‘I agree to save card details for Standing Instructions’.**

> 📘 Note:
>
> By default, the **I agree to save card details for Standing Instructions** check box is selected. The customer cannot uncheck the check box and has to transact with the SI option only.

### Cards recurring transaction workflow

#### Prerequisites

For every successful registration, before the recurring charge, a pre-debit notification has to be triggered 48 hours before the charge. This RBI mandate has to be strictly adhered to by merchants. If a pre-debit notification is not triggered, a recurring charge won’t happen.

#### Workflow

The workflow for the Recurring payment involves:

1. Merchants must call the Pre-Debit Notification API before the recurring payment transaction is done. For more information, refer to [Pre-Debit Notification API](ref:pre_debit_notification_api).
2. Merchants can call recurring payment API (**si_transaction**) for subsequent debits. For more information, refer to [Recurring Payment Transaction API](ref:recurring_payment_api).

   OR

   Merchants can use bulk upload recurring feature by uploading the records in an excel file. For more information, refer to [Upload Recurring Transactions in Bulk](doc:upload-recurring-transactions-in-bulk).

Merchants can use Zion Platform where Payu will trigger recurring basis the billing details sent at the time of subscription setup. For more information, refer to [Using Zion Subscription Automation](doc:using-zion-subscription-automation-platform)

You can use Recurring Payment API or bulk upload on PayUBiz Dashboard. For more information, refer to the following sections:

* [Recurring Payment Transaction API](ref:recurring_payment_api) for Recurring Payment Transaction API.
* [Bulk Upload of Payment Links for Recurring Payments](doc:bulk-upload-of-payment-links-for-recurring-payments-pre-debit-notication)+ [Pre-Debit Notification API](ref:pre_debit_notification_api) for bulk upload of payment links using PayUBiz Dashboard.

### Transaction limits

The transaction limit for recurring payments using debit card or credit card are as per the card holders limit or Rs.10,00,000 (if the card limit is more than Rs.10,00,000).

## UPI

Merchant performs the registration and mandate for UPI recurring payment with the UPI payment mode. The registration transaction is completed with 2FA, where the customer enters the MPIN (Mobile PIN) and authorizes the mandate details or billing details. After the registration transaction is successful, the merchant calls the recurring API to charge without further customer intervention.

<Image border={false} src="https://devguide.payu.in/wordpress/wp-content/uploads/2021/07/image-5.png" />

## UPI registration transaction workflow

The UPI registration is a mandated process. The UPI instrument provides total flexibility in designing the registration flow for merchants.

The steps involved in the UPI <Glossary>Registration transaction</Glossary> are:

1. Merchant can deduct the first billing amount as part of the registration transaction and set up the recurring payments for subsequent transactions.
2. Alternatively, the merchant can perform a small transaction minimum of 1 INR as part of the registration transaction and set up the recurring payments for subsequent transactions to the customer.
3. Merchant presents the option to sign up for a recurring platform/subscription plan where the consent from customer is required.
4. Billing details like amount, frequency, start date, and end date of the subscription need to be presented to the customer on the merchant’s website and passed to the PayU during registration transaction request over API interface.
5. While redirecting to PayU, the customer enters the preferred VPA handle and proceeds with the transaction. If the customer’s Payment Service Provider (PSP) app is associated with VPA handle and the underlined bank account supports UPI recurring, the request will be received by the PSP app of the customer.

<Image border={false} src="https://devguide.payu.in/wordpress/wp-content/uploads/2021/07/image-5.png" />

In case the customer’s PSP app and/or bank account associated with the VPA does not support UPI recurring, the transaction will be rejected.

6. On receiving a request over the PSP app, the customer needs to approve the registration request by entering the MPIN.
7. After successful authorization, the registration transaction gets completed and the response of the registration transaction along with the unique registration ID is returned to the merchant over browser redirection.

### UPI recurring transaction workflow

The steps involved in a UPI recurring transaction are:

* After the registration transaction is successful, the merchant can start calling the recurring payment API of PayU by passing a unique PayU ID received in the response to the registration transaction.
* The merchant will be able to debit from the customer for the authorized billing amount without requiring any inputs or interventions from the customer.
* However, before debiting the customer amount, it is mandatory to send a pre-debit notification to the customer informing them about the amount and debit date of the transaction. This needs to be sent at least 24 hours prior to actual debit. If the pre-debit notification is not sent successfully, the recurring transaction will fail. 
* Since payment processing of UPI recurring is an asynchronous process with banks, real-time response for recurring transaction API is always returned as “Pending” if a valid request is passed by the merchant.
* This state then gets converted into either “Success” or “Failure” once the bank confirms the status of the transaction to PayU over call back interface.
* The merchant can either implement the **Inquiry** API or use PayU’s Webhook support to get the real-time status of the recurring transaction once the bank provides real-time confirmation.

#### Supported UPI handles

All the major banks (issuers) supporting UPI recurring are HDFC, SBI, ICICI, Axis, IndusInd, HSBC, BOB, IDFC, Paytm, etc. For the list of UPI handles for the banks/apps supported by PayU, refer to [UPI Handles](doc:upi-handles).

> 📘 Notes:
>
> * In terms of flows, both intent flow and collect flow is supported for setting up the mandate/registration transaction.
> * The major banks (issuers) supporting UPI recurring are: HDFC, SBI, ICICI, Axis, IndusInd, HSBC, BOB, IDFC, Paytm, etc.
> * UPI recurring payments are currently restricted to only INR 15000 per transaction (if the amount exceeds 15000 MPIN is required for the transaction).
> * Apart from Registration and Recurring interfaces, you need to integrate following interfaces implemented which are mandatory before launching support for UPI recurring:
>   * [Pre-Debit Notification API](ref:pre_debit_notification_api)
>   * [Manage UPI Recurring Transaction](ref:api-commands-to-manage-upi-recurring-transaction)

### Transaction limits

The limit for recurring payments using UPI payment mode:

* Auto-debit is Rs.15000* (the auto-debit limit is higher for below listed purpose)
* With PIN is Rs.1,00,00

*The auto-debit limit for the following UPI recurring payments is one lakh rupees (Rs.1,00,000):

* Insurance premiums
* Credit card bill payments
* Insurance premium

## Pay and Subscribe

It allows your customer to make a one-time payment or establish a mandate tailored to their specific needs. It allows merchants to enable their customers with flexible, efficient, and secure payment options. The following are some use cases:

* **Scenario 1**: Merchants, particularly in the insurance sector, can leverage this feature to collect insurance fees directly from users. This eliminates the typical wait time of T+2 days for the first premium, circumventing the prevalent ecosystem challenges associated with eNACH.
* **Scenario 2**: It also offers users the flexibility to opt for the AutoDebit feature according to their preferences, ensuring a more personalized financial management experience.

This feature is specifically designed for Insurance providers, providing them with a streamlined and efficient payment collection process.

The Pay and Subscribe supports a variety of payment flows, including eNACH, UPI Autopay, and Standing Instructions (SI) on Cards, all accessible through the PayU Checkout page. It works with PayU Hosted Checkout integration, ensuring a smooth and secure transaction experience.

> 📘 Note:
>
> The Pay and Subscribe is supported only with PayU Hosted Checkout integration. For the request and response parameters, refer to[ Payment Consent Transaction - PayU Hosted Integration](ref:payment-consent-transaction-payu-hosted).

Currently, the standard transaction flow for Pay and Subscribe transactions, integrated with a PayU Recommendation Engine and SI capabilities.

## User Journey

### Cards

1. User will land on our payment checkout page for the transaction where all the checkout-supported payment modes will be visible.

<Image align="center" border={false} width="222px" src="https://files.readme.io/c8124c0-one-time-mandate-step1.png" />

2. User will select the option for Register AutoPay for cards.

3. User will enter the card details.

<Image align="center" border={false} width="222px" src="https://files.readme.io/5460162-ome-time-mandate-cards-step2a.png" />

4. Based on mandate eligibility user will see an option to opt in for registration.

<Image align="center" border={false} width="222px" src="https://files.readme.io/16b7e58-one-time-mandate-cards-3-register-for-subscription.png" />

5. Based on user action flow for normal transaction or mandate transaction will be executed.

<Image align="center" border={false} width="222px" src="https://files.readme.io/5611f27-one-time-card-card-otp.png" />

The payment confirmation message is displayed after successful OTP authentication.

<Image align="center" border={false} width="222px" src="https://files.readme.io/2430022-one-time-payment-success-for-all.png" />

#### Negative scenarios

If the card is not eligible, an error message is displayed below the **Enter Card Number** field similar to the following screenshot:

<Image align="center" border={false} width="222px" src="https://files.readme.io/2fc4992-one-time-time-mandate-cards-not-eligible.png" />

### UPI Intent

1. User will land on our payment checkout page for the transaction where all the checkout-supported payment modes will be visible.

<Image align="center" border={false} width="222px" src="https://files.readme.io/c8124c0-one-time-mandate-step1.png" />

2. User will select UPI to proceed with UPI transaction.
3. User will enter the VPA or UPI ID.

<Image align="center" border={false} width="222px" src="https://files.readme.io/b7fbb06-one-time-mandate-upi.png" />

4. User will see an option to opt in for registration.

<Image align="center" border={false} width="222px" src="https://files.readme.io/a278ee8-one-time-mandate-upi-common-1.png" />

5. Based on user action flow for normal transaction or mandate transaction will be executed.

<Image align="center" border={false} width="222px" src="https://files.readme.io/2430022-one-time-payment-success-for-all.png" />

### UPI Collect

1. User will land on our payment checkout page for the transaction where all the checkout-supported payment modes will be visible.

<Image align="center" border={false} width="222px" src="https://files.readme.io/c8124c0-one-time-mandate-step1.png" />

2. User will select UPI to proceed with UPI Collect.

<Image align="center" border={false} width="222px" src="https://files.readme.io/c92f623-one-time-mandate-upi-collect.png" />

3. User will enter the UPI ID or UPI number.

<Image align="center" border={false} width="222px" src="https://files.readme.io/be181e1-one-time-upi-collect-2.png" />

4. User will see an option to opt in for registration.

<Image align="center" border={false} width="222px" src="https://files.readme.io/00fd7bb-one-time-mandate-upi-common-1.png" />

5. Based on user action card flow for normal transaction or mandate transaction will be executed.

<Image align="center" border={false} width="222px" src="https://files.readme.io/2430022-one-time-payment-success-for-all.png" />

### Net Banking

1. User will land on our payment checkout page for the transaction where all the checkout-supported payment modes will be visible.

<Image align="center" border={false} width="222px" src="https://files.readme.io/c8124c0-one-time-mandate-step1.png" />

2. User will select **Net Banking** from the list of payment options.

3. User will the select the bank account where the Net Banking transaction will be performed.

<Image align="center" border={false} width="222px" src="https://files.readme.io/22a7c62-one-time-mandate-netbanking-1.png" />

4. User will select the checkbox and account details option will become visible to the users.

<Image align="center" border={false} width="222px" src="https://files.readme.io/9691907-one-time-mandate-netbanking-2.png" />

5. User will input the Banking details such as Account number, IFSC code, Name and Account Type on the payment page itself.

<Image align="center" border={false} width="222px" src="https://files.readme.io/0ffeb5d-one-time-mandate-netbanking-3.png" />

6. User will be asked to enter the Net Banking password.

<Image align="center" border={false} width="222px" src="https://files.readme.io/ea7d581-one-time-mandate-netbanking-password.png" />

7. User will be shown payment successful or declined page for one-time Net Banking transaction based on mandate eligibility:

* Case 1: When user opt’s for Mandate Registration along with one time payment:

<Image align="center" border={false} width="222px" src="https://files.readme.io/09ede51-one-time-mandate-netbanking-payment-successful.png" />

The user redirected to the bank page for eMandate consent.

<Image align="center" border={false} width="222px" src="https://files.readme.io/5bb9743-one-time-mandate-netbanking-emandate-bank-page.png" />

* Case 2: When user does not opt for Mandate Registration along with one time payment:

<Image align="center" border={true} width="222px" src="https://files.readme.io/46ddde2-one-time-mandate-netbanking-not-opted-mandate.png" className="border" />

* Case 3: When one time payment is declined

<Image align="center" border={false} width="222px" src="https://files.readme.io/302048b-one-time-mandate-netbanking-failed.png" />

In general, user will not be redirected to NPCI mandate creation page and will redirect back to Merchant’s url with transaction response.

1. After the transaction is successful, user will be redirected to NPCI Page where user gives consent for the mandate.

2. User will be directed to Bank’s Login Page from NPCI portal.

3. User will enter the OTP required for the transaction.