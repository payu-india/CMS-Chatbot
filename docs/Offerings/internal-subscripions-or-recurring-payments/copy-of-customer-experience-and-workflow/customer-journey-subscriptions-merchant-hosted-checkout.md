---
title: Customer Journey - Subscriptions > Merchant Hosted Checkout
deprecated: false
hidden: false
metadata:
  robots: index
---
<br />

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
