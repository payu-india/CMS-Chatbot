---
title: FAQs - Recurring Payments
excerpt: >-
  This section lists the frequently asked questions on Recurring Payments with
  PayU and answers.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
---
title: FAQs - Recurring Payments
excerpt: >-
  This section lists the frequently asked questions on Recurring Payments with
  PayU and answers.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Impact of Tokenization FAQs on Recurring Payments

<Accordion title="What will happen to existing mandates?" icon="fa-info-circle">

  All existing mandates will have to be tokenized, and a migration activity using the **Update SI** API has to be performed. For more information, refer to [Modify the Recurring Payments for a Card](ref:modify-the-recurring-payments-for-a-card)

  To tokenize the card, the consent of a customer has to be present. A successful customer consent means that the AFA on that card should have been successful.

  1. If merchant wants to do migration, then the merchant can update the mandate with the token using the **Update SI** API.
  2. If merchant wants PayU to do the migration, same has to be informed to their respective PayU Key Account Manager. PayU will do the migration and inform about the successful migrations through an excel report.

</Accordion>

<Accordion title="What will happen to new mandates?" icon="fa-info-circle">

  * Mandates through plain card
    * Merchant will pass plain card number. PayU post-authentication will tokenize the card and then authorize the transaction.
    * There can be cases where merchants might not want PayU as a token requestor. This case is possible but will lead to an additional leg where PayU will authorize and return an intermediate response of authorization. The merchant will have to tokenize with the token requestor and then update the token through the **Update SI** API. For more information, refer to [Update SI API](ref:update-si-api).
  * Mandates through already generated tokens
    * The merchant will initiate the transaction with a token. PayU will set up the subscription, initiate the AFA and activate the subscription basis of the token passed.

</Accordion>

<Accordion title="If the merchant has not taken consent for a token, can they update the token without customer intervention?" icon="fa-info-circle">

  Yes, the merchant can tokenize the card and call our S2S API to update the token without any customer intervention.

</Accordion>

<Accordion title="Is this tokenization approach final?" icon="fa-info-circle">

  * Representation to the regulator has been already made for SI hub to store the card, which means that if the approval comes, there is no change for the merchant in the recurring leg for the merchant to process existing mandates and new mandates through plain cards. For mandates setups where instead of the plain card, there is only a token available, in that case, the merchant will need to pass the token in the **_payment** API and PayU will set up and do AFA basis token.
  * If the above approach is not feasible, the merchant will have to tokenize the card and update the subscription with the token. Now, if the regulator approves of treating SI consent as tokenization consent, the merchant can start doing bulk migration without customer intervention; otherwise, the merchant needs explicit tokenization consent.
  * PayU suggests to follow the new approach and go live with it asap.

</Accordion>

<Accordion title="Can cards saved through SI be used for saved cards transactions?" icon="fa-info-circle">

  SI Consent can be used to tokenise cards for SI. If merchant wants to use the token for other purposes, then an explicit consent is required and whether same token can be used or an additional token has to be created, that still requires clarity from regulator.

</Accordion>

## General

<Accordion title="What are the payment instruments for Subscriptions?" icon="fa-info-circle">

  The following are the payment instruments available for Subscriptions:

  * Cards (Credit, Debit)
  * Net Banking
  * UPI Autopay

</Accordion>

<Accordion title="Does PayU support Aadhaar eNACH?" icon="fa-info-circle">

  Yes, PayU supports Aadhaar eNACH. For more information, refer to [Net Banking Consent Transaction](ref:netbanking-recurring-payment-consent-transaction#sample-request-with-aadhaar-as-verification-mode)

</Accordion>

<Accordion title="Which UPI banks or mobile apps are supported for UPI Autopay?" icon="fa-info-circle">

  PayU supports UPI Autopay. for banks or mobile apps. For the list of UPI banks or mobile apps. For more information, refer to [UPI Handles](doc:upi-handles)

</Accordion>

<Accordion title="Which banks are supported for Net Banking recurring payments?" icon="fa-info-circle">

  PayU supports NetBanking recurring payments for banks and cards. For a list of banks and cards, refer to [Bank Codes - Recurring Payments](doc:bank-codes-recurring-payments)

</Accordion>

<Accordion title="What happens when users get the ‘Card not Supported’ error while registering a mandate?" icon="fa-info-circle">

  This error indicates that the specific customer’s card does not support recurring payments. Hence, the customer needs to use another card. To check if a card supports recurring payments using seamless integration (Merchant Hosted or S2S), use the **Get BIN Info** API. For more information, refer to [Get Bin Info API](ref:get_bin_info_api).

</Accordion>

<Accordion title="What can be the maximum end date for a mandate with cards?" icon="fa-info-circle">

  The maximum end date for a card mandate is the card’s expiry.

</Accordion>

<Accordion title="Do I need to use separate APIs to create cards, Net Banking, and UPI Autopay mandates?" icon="fa-info-circle">

  No, only the **_payment** API is required to create Cards, Net Banking, and UPI Autopay mandates.

</Accordion>

<Accordion title="Is pre-debit necessary for Net Banking to enable recurring transactions?" icon="fa-info-circle">

  No, pre-debit is required only for Cards and UPI.

</Accordion>

<Accordion title="Is pre-debit mandatory for recurring transactions using cards and UPI?" icon="fa-info-circle">

  Yes, pre-debit is mandatory for cards. You must use pre-debit at least 24 hours before the recurring charge transaction.

</Accordion>

<Accordion title="What are the possible ways to integrate recurring payments with PayU?" icon="fa-info-circle">

  You can integrate recurring payments with PayU using the following methods:

  * [Using API Integration](doc:using-api-integration-recurring-payments)
  * [Using PayUBiz Dashboard](doc:recurring-payments-using-payubiz-dashboard) (Zero-Code Change)
  * [Using Zion Subscription Automation](doc:using-zion-subscription-automation-platform)

</Accordion>

<Accordion title="Does PayU support the interoperability of eNACH mandates?" icon="fa-info-circle">

  No, PayU is currently developing this feature and will communicate it to you after it is released.

</Accordion>

<Accordion title="What is a Consent or Registration Transaction in the context of recurring payments?" icon="fa-info-circle">

  A Consent or Registration Transaction is the first transaction in a recurring payment series, in which the customer provides consent to the merchant to charge their card or bank account for future transactions. This transaction typically involves storing the payment information securely in the payment gateway for future use.

</Accordion>

<Accordion title="What is the workflow for a Consent or Registration Transaction?" icon="fa-info-circle">

  For the workflow for a Consent or Registration Transaction, refer to [Customer Experience and Workflow - Recurring Payments](doc:customer-experience-and-workflow-recurring-payments) based on the payment mode.

</Accordion>

<Accordion title="What are the benefits of using a Consent or Registration Transaction for recurring payments?" icon="fa-info-circle">

  The benefits of using a Consent or Registration Transaction for recurring payments include improved customer experience, reduced payment friction, and increased convenience for both customers and merchants. By storing payment information securely in the payment gateway, merchants can process future transactions more easily and reduce the need for customers to enter payment information repeatedly.

</Accordion>

<Accordion title="How does PayU ensure the security of payment information in a Consent or Registration Transaction?" icon="fa-info-circle">

  PayU uses various security measures such as PCI-DSS compliance, encryption, tokenization, and fraud detection to ensure the security of payment information in a Consent or Registration Transaction. PayU also stores payment information in a secure, encrypted format, and allows merchants to access the information only when needed.

</Accordion>

<Accordion title="Can customers cancel Consent or Registration Transactions at any time?" icon="fa-info-circle">

  Yes, your customers can cancel Consent or Registration Transactions at any time, by contacting the merchant or the payment gateway directly. You should have a clear cancellation policy in place and make it easy for customers to cancel Consent or Registration Transactions if they choose to do so.

</Accordion>

<Accordion title="Can I use different payment methods for Consent or Registration Transactions and subsequent transactions in a recurring payment series?" icon="fa-info-circle">

  Yes, you can use different payment methods for Consent or Registration Transactions and subsequent transactions in a recurring payment series. However, it is recommended that you use the same payment method for all transactions in a recurring payment series to avoid confusion and potential errors.

</Accordion>

<Accordion title="What is a Payment Consent Transaction?" icon="fa-info-circle">

  A Payment Consent Transaction is the initial transaction in a recurring payment series, in which the customer provides consent to the merchant to charge their payment method for future transactions. This transaction typically involves storing the payment information securely in the payment gateway for future use.

</Accordion>

<Accordion title="How can a Payment Consent Transaction be registered using the PayU API?" icon="fa-info-circle">

  A Payment Consent Transaction can be registered using the PayU API by sending a request to the PayU server with the payment information and transaction details. The API supports various payment methods, including credit cards, debit cards, net banking, and UPI.

</Accordion>

<Accordion title="What are the steps involved in registering a Payment Consent Transaction using the PayU API?" icon="fa-info-circle">

  For the steps involved in registering a payment consent, refer to the following based on the integration:

  * [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted)
  * [Payment Consent Transaction using Merchant Hosted Checkout](ref:payment-consent-transaction-merchant-hosted)

</Accordion>

<Accordion title="What are the benefits of using the PayU API to register a Payment Consent Transaction?" icon="fa-info-circle">

  The benefits of using the PayU API to register a Payment Consent Transaction include faster implementation, improved checkout experience for customers, and reduced risk of fraud and chargebacks. By using the API, merchants can automate the payment process and avoid manually handling payment information, which reduces the effort required to implement the feature.

</Accordion>

## SI of International Cards

<Accordion title="International SI is supported on which banks?" icon="fa-info-circle">

  International SI is supported with cards issued by non-Indian banks.

</Accordion>

<Accordion title="Is it mandatory to use Pre-Debit Notifications API for International Cards?" icon="fa-info-circle">

  Yes, it is mandatory to use the **Pre-Debit Notification** API for international cards. For more information, refer to [Pre-Debit Notification API](ref:pre_debit_notification_api).

</Accordion>

<Accordion title="Can recurring happen in real-time after the mandate is set up?" icon="fa-info-circle">

  Yes, Recurring Payments can happen in real-time after the mandate is set up.

</Accordion>

<Accordion title="Is there any role of mandate providers in approving the mandates to make them active?" icon="fa-info-circle">

  No, Mandate providers does not any role in approving the mandates to make them active.

</Accordion>

<Accordion title="Which acquirer is supported for International SI?" icon="fa-info-circle">

  AXIS Bank is the acquirer bank supported for International SI.

</Accordion>

<Accordion title="What is the frequency supported for International SI?" icon="fa-info-circle">

  Only the **Adhoc** frequency is supported for International SI.

</Accordion>

<Accordion title="International SI is supported on which merchants?" icon="fa-info-circle">

  Only non-MCP Merchants is supported for International SI.

</Accordion>

<Accordion title="Which all networks are supported by International SI?" icon="fa-info-circle">

  * Visa
  * Mastercard

</Accordion>

<Accordion title="Is Authentication required to create a mandate?" icon="fa-info-circle">

  Yes, authentication is required to create a mandate.

</Accordion>

<Accordion title="Can recurring happen if the mandate is inactive?" icon="fa-info-circle">

  No, recurring payment cannot be performed if the mandate is inactive.

</Accordion>

<Accordion title="Is Modification allowed for International SI mandates?" icon="fa-info-circle">

  Yes, modification is allowed for International SI mandates.

</Accordion>

<Accordion title="Is Deletion allowed for International SI mandates?" icon="fa-info-circle">

  Yes, you can delete an existing International SI mandate.

</Accordion>

<Accordion title="Is authentication required for mandate modification with International SI?" icon="fa-info-circle">

  Yes, the authentication is required for mandate modification with International SI.

</Accordion>

<Accordion title="Do merchant require a separate integration for International SI if domestic SI integration has been done already?" icon="fa-info-circle">

  No, you need not require a separate integration International SI if the domestic SI integration is already done.

</Accordion>

<Accordion title="What is the transaction currency for International SI transactions?" icon="fa-info-circle">

  * User issuing card currency
  * INR

</Accordion>
