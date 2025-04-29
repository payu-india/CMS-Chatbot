---
title: UPI Payment Experience
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: UPI Recurring Payment Experience
  description: >-
    Merchants can register customers for UPI recurring payments by completing a
    2FA registration transaction, then charge customers without further
    intervention. The registration process involves presenting billing details
    to customers and obtaining their consent, while the recurring transaction
    process requires sending a pre-debit notification to customers before
    debiting their accounts.
  keywords:
    - UPI Recurring Payment Experience
    - ' UPI Recurring Payment Workflow'
  robots: index
next:
  description: ''
---
Merchant performs the registration and mandate for UPI recurring payment with the UPI payment mode. The registration transaction is completed with 2FA, where the customer enters the MPIN (Mobile PIN) and authorizes the mandate details or billing details. After the registration transaction is successful, the merchant calls the recurring API to charge without further customer intervention.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/07/image-5.png)

## UPI registration transaction workflow

The UPI registration is a mandated process. The UPI instrument provides total flexibility in designing the registration flow for merchants.

The steps involved in the UPI <<glossary:Registration transaction>> are:

1. Merchant can deduct the first billing amount as part of the registration transaction and set up the recurring payments for subsequent transactions.
2. Alternatively, the merchant can perform a small transaction minimum of 1 INR as part of the registration transaction and set up the recurring payments for subsequent transactions to the customer.
3. Merchant presents the option to sign up for a recurring platform/subscription plan where the consent from customer is required.
4. Billing details like amount, frequency, start date, and end date of the subscription need to be presented to the customer on the merchant’s website and passed to the PayU during registration transaction request over API interface.
5. While redirecting to PayU, the customer enters the preferred VPA handle and proceeds with the transaction. If the customer’s Payment Service Provider (PSP) app is associated with VPA handle and the underlined bank account supports UPI recurring, the request will be received by the PSP app of the customer.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/07/image-5.png)

   In case the customer’s PSP app and/or bank account associated with the VPA does not support UPI recurring, the transaction will be rejected.

6. On receiving a request over the PSP app, the customer needs to approve the registration request by entering the MPIN.
7. After successful authorization, the registration transaction gets completed and the response of the registration transaction along with the unique registration ID is returned to the merchant over browser redirection.

## UPI recurring transaction workflow

The steps involved in a UPI recurring transaction are:

- After the registration transaction is successful, the merchant can start calling the recurring payment API of PayU by passing a unique PayU ID received in the response to the registration transaction.
- The merchant will be able to debit from the customer for the authorized billing amount without requiring any inputs or interventions from the customer.
- However, before debiting the customer amount, it is mandatory to send a pre-debit notification to the customer informing them about the amount and debit date of the transaction. This needs to be sent at least 24 hours prior to actual debit. If the pre-debit notification is not sent successfully, the recurring transaction will fail. 
- Since payment processing of UPI recurring is an asynchronous process with banks, real-time response for recurring transaction API is always returned as “Pending” if a valid request is passed by the merchant.
- This state then gets converted into either “Success” or “Failure” once the bank confirms the status of the transaction to PayU over call back interface.
- The merchant can either implement the **Inquiry** API or use PayU’s Webhook support to get the real-time status of the recurring transaction once the bank provides real-time confirmation.

### Supported UPI handles

All the major banks (issuers) supporting UPI recurring are HDFC, SBI, ICICI, Axis, IndusInd, HSBC, BOB, IDFC, Paytm, etc. For the list of UPI handles for the banks/apps supported by PayU, refer to [UPI Handles](doc:upi-handles).

> 📘 Notes:
> 
> - In terms of flows, both intent flow and collect flow is supported for setting up the mandate/registration transaction.
> - The major banks (issuers) supporting UPI recurring are: HDFC, SBI, ICICI, Axis, IndusInd, HSBC, BOB, IDFC, Paytm, etc.
> - UPI recurring payments are currently restricted to only INR 15000 per transaction (if the amount exceeds 15000 MPIN is required for the transaction).
> - Apart from Registration and Recurring interfaces, you need to integrate following interfaces implemented which are mandatory before launching support for UPI recurring:
>   - [Pre-Debit Notification API](ref:pre_debit_notification_api)
>   - [Manage UPI Recurring Transaction](ref:api-commands-to-manage-upi-recurring-transaction)

## Transaction limits

The limit for recurring payments using UPI payment mode:

- Auto-debit is Rs.15000\* (the auto-debit limit is higher for below listed purpose)
- With PIN is Rs.1,00,00

\*The auto-debit limit for the following UPI recurring payments is one lakh rupees (Rs.1,00,000):

- Insurance premiums
- Credit card bill payments
- Insurance premium