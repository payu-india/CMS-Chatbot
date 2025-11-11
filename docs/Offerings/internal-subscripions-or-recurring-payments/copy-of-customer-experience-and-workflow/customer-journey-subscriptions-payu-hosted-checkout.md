---
title: Customer Journey - Subscriptions > PayU Hosted Checkout
deprecated: false
hidden: false
metadata:
  robots: index
---
## Net Banking

Net Banking recurring like cards are processed seamlessly without the customer’s intervention and any 2FA.
There are two common terms in Net Banking recurring:

* <Glossary>Registration transaction</Glossary>(also known as e-Mandate transaction)
* Payment transaction (also known as e-NACH transaction or SI transaction).

<Callout icon="📘" theme="info">
  **Note**: Effective from 1st April 2024, mandates can be issued for a maximum duration of 40 years from the date of issuance.
</Callout>

## Registration transaction workflow

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

### eNACH Aadhaar Authentication

In Step 5 above, the customer is redirected to NPCI page for the Aadhaar authentication, so the additional steps involved for Aadhaar authentication are:

1. Customer enter their Aadhaar card number in the **Aadhaar Card Number** field and clicks **Confirm**.

<Image align="center" border={true} src="https://files.readme.io/b3f6343-enach-aadhaar-step1.png" className="border" />

2. Customer enter the OTP in the **OTP** and **Confirm OTP** fields that is received to the mobile phone registered with Aadhaar, and then clicks **Continue**.

<Image align="center" border={true} src="https://files.readme.io/4d3d281-enach-aadhaar-step2.png" className="border" />

3. Customer enter the OTP that is sent by to bank to the registered mobile number and clicks **Continue**.

<Image align="center" border={true} src="https://files.readme.io/be47075-enach-aadhaar-step3.png" className="border" />

The transaction status is displayed similar to the following screenshot:

<Image align="center" border={true} src="https://files.readme.io/b3f78b9-enach-aadhaar-step4.png" className="border" />

## Recurring transaction workflow

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

## Transaction limits

The transaction limit for recurring payments using Net Banking is as follows:

* Net Banking: Rs.10,00,000
* Aadhaar based eSign or eNACH Aadhaar Authentication: Rs.1,00,000
