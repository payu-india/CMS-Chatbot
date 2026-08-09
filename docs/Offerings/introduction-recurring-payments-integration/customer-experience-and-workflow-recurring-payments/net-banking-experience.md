---
title: Net Banking Payment Experience
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Net Banking Experience for Recurring Payments or Standing Instructions
  description: >-
    This document explains the process of Net Banking recurring transactions,
    including registration and payment transactions, as well as the
    authentication methods involved. It also outlines the transaction limits and
    provides information on how to use the Recurring Payment API or bulk upload
    on PayUBiz Dashboard.
  keywords:
    - Net Banking recurring transactions workflow
    - ' Net Banking recurring workflow'
  robots: index
next:
  description: ''
---
Net Banking recurring like cards are processed seamlessly without the customer’s intervention and any 2FA. <br />There are two common terms in Net Banking recurring:

- <Glossary>Registration transaction</Glossary>(also known as e-Mandate transaction)
- Payment transaction (also known as e-NACH transaction or SI transaction).

<Callout icon="📘" theme="info">
  **Note**: Effective from 1st April 2024, mandates can be issued for a maximum duration of 40 years from the date of issuance.
</Callout>

PayU offers the following flows for integration

1. [eNach Direct Integration](#enach-direct-integration)
2. [NPCI Integration](#npci-integration)

## eNACH Direct Integration Flow

After the customer completes eNACH mandate registration, PayU processes the mandate registration with HDFC or ICICI bank. The merchant can initiate a recurring debit after the mandate is successfully registered and available for execution.

Unlike Cards and UPI recurring payments, **eNACH does not require a pre-debit notification**. Do not call the `pre_debit_SI` API for an eNACH recurring debit.

### Major Steps Involved

1. Complete the eNACH consent transaction.
2. Wait for PayU and the participating bank to complete mandate registration. This may take up to **T+2 days**, depending on the bank.
3. Confirm that the mandate is registered and available for execution.
4. Call the Recurring Payment API with the registered mandate details and the amount to be debited.
5. Process the response and use PayU’s status mechanisms to track the final outcome.

> **Important:** The merchant must not initiate a recurring debit until the eNACH mandate has been successfully registered. The exact mandate-status check and recurring-payment API parameters depend on the PayU integration being used.

#### eNACH and pre-debit notifications

| Payment method | Pre-debit notification     |
| -------------- | -------------------------- |
| eNACH          | Not required               |
| Cards          | Required, where applicable |
| UPI            | Required, where applicable |

### Registration transaction workflow

The steps involved in a registration transaction (e-Mandate) are:

1. This is usually an INR 0.00 (zero rupee) transaction hence it is called a registration transaction.

<Callout icon="📘" theme="info">
  ### Notes:

  - Upfront payment can be collected only through direct integration – HDFC Bank and ICICI Bank. For all the 40+ banks supported through NPCI, you cannot collect the upfront amount and perform only the INR 0.00 authentication. To enable direct integration, contact your PayU Key Account Manager (KAM) or <Anchor target="_blank" href="https://help.payu.in">PayU Support</Anchor>.
  - Upfront payment can be collected only through direct integration – HDFC Bank **(₹1 Lakh)** and ICICI Bank.
</Callout>

2. Merchant presents an option to sign up for a recurring platform where the customer needs to provide his/her consent.
3. Billing details like amount, frequency, start date, and end date of the subscription need to be presented to the customer and passed to PayU during payment request.
4. On redirecting to PayU:
   - **Non-Seamless Integration**: The customer selects preferred bank and enters account details like account number, name of the account, and account type: Savings or Current.
   - **Seamless Integration**: Merchant has to send all the parameters, that is, preferred bank, account number, name of the account, and account type.


<Image src="https://files.readme.io/6cccafc-recurring_payment_netbanking_workflow_step4.png" align="center" width="512px" border={true} />


<br />


<Image src="https://files.readme.io/6ba7e05-recurring_payment_aadhaar_step1.png" align="center" width="512px" border={true} />


5. The customer is redirected to the Bank’s login page and authenticates himself with either net banking username and password or debit card number and ATM PIN depending upon the preferred bank.
6. On successful authentication, the customer sees registration details like billing amount, billing frequency, start date, and end date of the subscription plan.
7. The customer approves the subscription details from the bank page using standard 2FA flow and gets redirected back to PayU'
8. On receiving either of the response from the bank, the same is communicated back to the merchant on a real-time basis.

### Recurring transaction workflow

The steps to perform a recurring transaction for Net Banking are:

1. After registration is successful, the merchant can call the recurring payment API of PayU by passing the unique PayU ID received in the response to the registration transaction.
2. All the transaction requests coming from the merchant are queued and forwarded to acquirers through a file. This is performed since most of the time even payment processing for Net Banking recurring is offline.
3. The real-time response for Recurring transactions to the merchant is always returned as Pending. For direct integration with ICICI bank, the response will be real-time.
4. For NPCI-supported banks and HDFC direct Integration, the response of the transaction is received over SFTP from acquirers at the end of the day, which is then stored in PayU’s DB, and the same is communicated to the merchant over a webhook API call.
5. TAT for receiving either Success or Failure case of e-NACH transactions is T+2 similar to the registration transaction.

## NPCI Integration Flow

### Registration transaction workflow

The steps involved in a registration transaction (e-Mandate) are:

1. This is usually an INR 0.00 (zero rupee) transaction hence it is called a registration transaction.

<Callout icon="📘" theme="info">
  ### Notes:

  - Upfront payment can be collected only through direct integration – HDFC Bank and ICICI Bank. For all the 40+ banks supported through NPCI, you cannot collect the upfront amount and perform only the INR 0.00 authentication. To enable direct integration, contact your PayU Key Account Manager (KAM) or <Anchor target="_blank" href="https://help.payu.in">PayU Support</Anchor>.
  - Upfront payment can be collected only through direct integration – HDFC Bank **(₹1 Lakh)** and ICICI Bank.
</Callout>

2. Merchant presents an option to sign up for a recurring platform where the customer needs to provide his/her consent.
3. Billing details like amount, frequency, start date, and end date of the subscription need to be presented to the customer and passed to PayU during payment request.
4. On redirecting to PayU:
   - **Non-Seamless Integration**: The customer selects preferred bank and enters account details like account number, name of the account, and account type: Savings or Current.
   - **Seamless Integration**: Merchant has to send all the parameters, that is, preferred bank, account number, name of the account, and account type.


<Image src="https://files.readme.io/6cccafc-recurring_payment_netbanking_workflow_step4.png" align="center" width="512px" border={true} />


<br />


<Image src="https://files.readme.io/6ba7e05-recurring_payment_aadhaar_step1.png" align="center" width="512px" border={true} />


5. The customer is redirected to the NPCI site for authentication:
6. Customer enter their Aadhaar card number in the **Aadhaar Card Number** field and clicks **Confirm**.


<Image src="https://files.readme.io/b3f6343-enach-aadhaar-step1.png" align="center" border={true} />


7. Customer enter the OTP in the **OTP** and **Confirm OTP** fields that is received to the mobile phone registered with Aadhaar, and then clicks **Continue**.


<Image src="https://files.readme.io/4d3d281-enach-aadhaar-step2.png" align="center" border={true} />


8. Customer enter the OTP that is sent by to bank to the registered mobile number and clicks **Continue**.


<Image src="https://files.readme.io/be47075-enach-aadhaar-step3.png" align="center" border={true} />


The transaction status is displayed similar to the following screenshot:


<Image src="https://files.readme.io/b3f78b9-enach-aadhaar-step4.png" align="center" border={true} />


9. On successful authentication, the customer sees registration details like billing amount, billing frequency, start date, and end date of the subscription plan.
10. On receiving either of the response from the bank, the same is communicated back to the merchant on a real-time basis.

### Recurring transaction workflow

The steps to perform a recurring transaction for Net Banking are:

1. After registration is successful, the merchant can call the recurring payment API of PayU by passing the unique PayU ID received in the response to the registration transaction.
2. All the transaction requests coming from the merchant are queued and forwarded to acquirers through a file. This is performed since most of the time even payment processing for Net Banking recurring is offline.
3. The real-time response for Recurring transactions to the merchant is always returned as Pending. For direct integration with ICICI bank, the response will be real-time.
4. For NPCI-supported banks and HDFC direct Integration, the response of the transaction is received over SFTP from acquirers at the end of the day, which is then stored in PayU’s DB, and the same is communicated to the merchant over a webhook API call.
5. TAT for receiving either Success or Failure case of e-NACH transactions is T+2 similar to the registration transaction.

<Callout icon="📘" theme="info">
  **Note**: Banks do not support refunds for Net Banking Recurring Payment transactions (or e-NACH transaction) so you will get an error message, “Refund not accepted for txn” with the error code 232. PayU provides alternate method to process refunds. To enable refunds on Net Banking or eNACH recurring payments, contact your PayU Key Account Manager (KAM). For the list of banks supporting e-NACH, refer to [Bank Codes - Recurring Payments](doc:bank-codes-recurring-payments).
</Callout>

For Net Banking, there are three methods to authenticate:

1. Net Banking Login credentials
2. Debit Card Number with an OTP
3. Aadhaar number with an OTP

You can use Recurring Payment API or bulk upload on PayU Dashboard. For more information, refer to the following sections:

- [Recurring Payment Transaction API](ref:recurring_payment_api) for Recurring Payment API.
- [Using PayU Dashboard](https://docs.payu.in/docs/subscription-dashboard/) for payment links using PayU Dashboard.

For the list of banks supported for the Net Banking recurring platform and their bank codes, refer to [Bank Codes - Recurring Payments](doc:bank-codes-recurring-payments) .

## Transaction limits and AFA requirements

The transaction limit for recurring payments is as follows:

- Direct Integration or Net Banking: Rs.10,00,000
- Aadhaar based eSign or eNACH Aadhaar Authentication: Rs.1,00,000

### AFA requirements

Additional Factor of Authentication (AFA) may be required at specific stages of a recurring-payment flow. The applicable requirement depends on the payment method and the underlying payment rail.

Under RBI’s **Digital Payments – E-mandate Framework, 2026**, the following scenarios require AFA or may require AFA:

| Scenario                                                                                 | AFA requirement                                                                                                          |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Registering a new e-mandate                                                              | AFA is required before the mandate can be registered.                                                                    |
| Processing the first transaction                                                         | AFA is required. If registration and the first transaction occur together, the same AFA validation may be used for both. |
| Modifying an existing mandate                                                            | AFA validation is required.                                                                                              |
| Withdrawing or revoking a mandate                                                        | AFA validation is required.                                                                                              |
| Opting out of an upcoming transaction or the entire mandate                              | The opt-out request must be validated using AFA.                                                                         |
| Subsequent recurring transaction up to ₹15,000                                           | AFA is generally not required for covered payment methods, subject to the applicable mandate and issuer controls.        |
| Subsequent recurring transaction above ₹15,000                                           | AFA is required.                                                                                                         |
| Insurance premium, mutual-fund subscription, or credit-card bill payment up to ₹1,00,000 | AFA may not be required under the specified RBI exception.                                                               |
| The same categories above ₹1,00,000                                                      | AFA is required.                                                                                                         |

The issuer must also send a pre-transaction notification at least 24 hours before the debit. This notification requirement is separate from the AFA requirement.

<Callout icon="📘" theme="info">
  ## AFA scenario&#x73;**:**&#x20;

  AFA is required when registering, modifying, withdrawing, or opting out of an e-mandate, and for the first transaction under the mandate. For covered payment methods, subsequent recurring payment transactions up to ₹15,000 may be processed without AFA; transactions above ₹15,000 require AFA. Insurance premiums, mutual-fund subscriptions, and credit-card bill payments may be processed without AFA up to ₹1,00,000, subject to RBI requirements.
</Callout>
