---
title: FAQs for Dashboard
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: FAQs for Dashboard
  description: >-
    Find answers to frequently asked questions about the PayU Merchant Dashboard
    including transactions, settlements, API keys, webhooks, onboarding, and
    account management for India merchants. Covers FAQs for Dashboard.
  keywords:
    - payu dashboard faqs
    - payu merchant dashboard frequently asked questions
    - payu dashboard help guide
    - payment gateway dashboard faq payu
    - payu dashboard troubleshooting guide
    - payu merchant dashboard common questions
    - payu dashboard support faq india
    - payment gateway merchant dashboard help payu
    - payu dashboard faq vs razorpay cashfree
    - payu merchant account dashboard questions
  robots: index
next:
  description: ''
---
## **General**

* **What are the system requirements for using the PayU Dashboard?**

The PayU Dashboard is a web-based tool that can be accessed from any web browser. There are no specific system requirements, but it’s recommended that you use a modern web browser and a stable internet connection.

* **How do I log in to the PayU Dashboard?**

To log in to the PayU Dashboard, go to the [PayU website](https://payu.in/) and click **Login** at the top-right corner. Enter your email address and password, and then click **Log In**. For more information, refer to [Log in to Dashboard](doc:log-in-to-dashboard).

* **I am unable to log in to my PayU Dashboard and getting an invalid password message.**

You can perform any of the following:

* Use the **Login using OTP** to get the OTP to your registered mobile number and log in.
* Use the **Forgot Password** option to reset your password on the Dashboard Login page. For more information, refer to [Reset Password for PayU Dashboard Login](doc:reset-password-for-payu-dashboard-login).
* **How do I reset my Dashboard login password?**

Use the Forgot Password option to reset your password on the Dashboard Login page. For more information, refer to [Reset Password for PayU Dashboard Login](doc:reset-password-for-payu-dashboard-login).

* **What should I do if I have a problem using the PayU Dashboard?**

If you have a problem using the PayU Dashboard, you can refer to the [Explore Dashboard](doc:payu-dashboard). For any further issues, contact PayU’s customer support team for assistance or [raise a ticket with PayU](https://help.payu.in/).

* **I am not able to access certain features on Dashboard. How can I enable them?**

Some features may be restricted to certain membership levels or require additional permissions. Check your access privileges with your company account administrator and ensure you have the necessary permissions.

* **How to check the pricing plans for the various PayU products on Dashboard? How can I get more information?**

You can get the pricing information for a few of the products such as Priority Settlements. You can contact your PayU Key Account Manager for more information about the pricing plans of various products.

* **What are Chargebacks?**

A chargeback is raised by the customer to issuing bank, owing to many reasons like a fraudulent transaction or unsatisfactory product or service delivery, etc.

* **Where I can check the chargeback raised by my customers?**

You can view or filter the chargebacks on the Chargeback page under the **Track** section of the Dashboard. For more information, refer to [Chargeback](doc:chargeback).

* **Can I link my Amazon, Flipkart, or Meesho account to check my earnings?**

Yes, you can link your Amazon, Flipkart, or Meesho account and check the earnings in the **Sales and Earnings** section of the Dashboard.

* **What are various reports that can be generated for the various modules on Dashboard?**

You can generate the following reports on the Dashboard:

* **Transaction**: These reports will fetch data for your transactions like payment, Customer Information, and Status.
* **Settlements**: These reports will show you settlements initiated, paused, and processed with details like service fees.
* **Refunds**: These reports will fetch you the details of refunds that were initiated and their statuses through the cycle.
* **TDRReport**: These are monthly invoices from PayU for service fees and tax.
* **Payouts**: These reports will show you the Payouts data like the amount disbursed, beneficiary, and status.
* **Buttons**: These reports will fetch you the transactional data like the amount collected and the status of your payment buttons
* **PaymentsLinks**: These reports will fetch you transactional data like the amount collected and the status of your payment links.
* **Invoices**: These reports will fetch you transactional data like the amount collected and the status of your invoices. 
* **Can I schedule reports on Dashboard?**

Yes, you can schedule reports on Dashboard so that they will be generated at the scheduled time. For more information, refer to [Reports](doc:reports).

* **Can I collect payments using Dashboard?**

Yes, you collect payments using Dashboard. For more information, refer to [Payment Links](doc:payment-links-dashboard).

* **How to create payment buttons that can be embedded in my website?**

You can easily create payment buttons on the Dashboard and copy the HTML code that can be embedded on your website. For more information, refer to [Payment Buttons](doc:payment-buttons-dashboard).

## Key or Salt

* **I am unable to view the Key and Salt or not able to access it on Dashboard.**

If your website is not validated or onboarding is not completed by PayU, you will not be able to access or view the Key and Salt. To generate key and salt, refer to [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)

* **The Key and Salt which I copied from Dashboard are not working**

Check whether you are using the **Production** endpoint for Production Key and Salt. For PayU Hosted or Merchant Hosted integrations, you have to use the following endpoints with **\_payment** API:

<table style={{border:"0.1rem solid rgb(242, 242, 242)"}}><tbody><tr><td style={{border:"0.1rem solid rgb(242, 242, 242)", padding:"0.8em"}}><strong>Test Environment</strong></td><td style={{border:"0.1rem solid rgb(242, 242, 242)", padding:"0.8em"}}>https://test.payu.in/_payment</td></tr><tr><td style={{border:"0.1rem solid rgb(242, 242, 242)", padding:"0.8em"}}><strong>Production Environment</strong></td><td style={{border:"0.1rem solid rgb(242, 242, 242)", padding:"0.8em"}}>https://secure.payu.in/_payment</td></tr></tbody></table>

If the Key and Salt are still not working, contact your KAM or raise a ticket with PayU support on [help.payu.in](https://help.payu.in/).

* **Can I get the Test Key and Salt from PayU for testing**?\
  Yes, you can get the test Key and Salt. For more information refer to [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).
* **Can I create a test account on Dashboard for Key and Salt so that I can use them for testing**?

OR

* **I was trying to create a new test account and the Dashboard page got stuck at loading or requesting KYC after signing up.**

No, you can ignore KYC for the test account and you can generate a test Key and Salt. For more information, refer to [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).

## Profile or Configure Website

* **How can I add a new website to my PayU account? What are the steps involved?**

Log in to your PayU merchant Dashboard, navigate to the settings or configuration section. For more information, refer to [Update Profile on Dashboard](doc:update-profile-on-dashboard). If you encounter issues, contact support.

* **I am not receiving any emails or updates from your PayU. What should I do?**

Please check your spam or junk mail folder to make sure the emails are not being sent there. You can also add our email address to your contact list to ensure that our emails are delivered to your inbox.

* **How do I update my basic details on the PayU Dashboard?**

  To update your basic details such as your mobile number and password, refer to [Update Profile on Dashboard](https://docs.payu.in/docs/update-profile-on-dashboard).
* **What business details can I update on the PayU Dashboard?** 

  You can update your business website/app details, GST details, and display name. For more information, refer to [Update Profile on Dashboard](https://docs.payu.in/docs/update-profile-on-dashboard).
* **How do I update my bank details on the PayU Dashboard?** 

  To update your bank details, go to the “Bank Details” tab on the Profile page. For more information, refer to [Update Profile on Dashboard](https://docs.payu.in/docs/update-profile-on-dashboard). 
* **Can I update my profile details before completing the onboarding process?** 

  Yes, you can update your profile details before completing the onboarding process. This includes uploading documents for verification.  For more information, refer to [Update Profile on Dashboard](https://docs.payu.in/docs/update-profile-on-dashboard).
* **What should I do if I encounter issues while updating my profile on the PayU Dashboard?** 

  If you encounter any issues while updating your profile, ensure that you have entered the correct information and that your internet connection is stable.  For more information, refer to [Update Profile on Dashboard](https://docs.payu.in/docs/update-profile-on-dashboard).
* **How do I verify my password when updating profile details?** 

  When you try to update your profile details, a “Verify Your Password” pop-up page will be displayed for security. For more information, refer to [Update Profile on Dashboard](https://docs.payu.in/docs/update-profile-on-dashboard).

## KYC

* **Why do I need to complete my KYC?**

Completing your KYC is a regulatory requirement that helps prevent fraud and money laundering. It also allows you to access certain features and services on the PayU Dashboard.

* **Do I need to complete KYC for the test account on Dashboard?**

No, KYC is not required for a test account and you can generate test Key and Salt. For more information, refer to [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).

* **I am unable to complete my KYC based on the documents I had submitted**.\
  Contact your PayU Key Account Manager and raise a request to complete the KYC.
* **What documents do I need to complete my KYC?**

The specific documents you need may vary depending on the type of business you have. In general, you’ll need to provide your/business PAN card and proof of address (such as a utility bill or bank statement).

* **How do I submit my KYC documents?**

You can submit your KYC documents through the PayU Dashboard. Click **Complete Your KYC** displayed on the top after your login, upload your documents, and follow the instructions provided.

* **How long does it take to complete my KYC?**

The time it takes to complete your KYC can vary depending on several factors, such as the completeness and accuracy of your documents, and the volume of KYC requests being processed by PayU. Generally, it can take anywhere from a few days to a few weeks.

* **What happens if my KYC is not approved?**

If your KYC is not approved, PayU will notify you and provide an explanation for the rejection. You may need to provide additional or different documents to meet the requirements.

* **Is my personal information secure with PayU during the KYC process?**

PayU takes care of the security and privacy of your personal information. PayU uses industry-standard security measures to protect your data, and will only use your information for the purpose of completing your KYC.

## **Transactions**

* **Where can view the transactions made by my customers?**

You can view, filter, categorize, or export transactions on the *Transactions* page under the **Track** section of the Dashboard. For more information, refer to [Transactions Dashboard](doc:transactions).

* **How can I manage my transactions in the PayU Dashboard?**

To manage your transactions in the Dashboard, navigate to the *Transactions* page under the **Track** section. You can view a list of your transactions, search for specific transactions, and filter transactions based on various criteria. You can also perform actions such as refunds and cancellations on individual transactions. For more information, refer to  [Transactions Dashboard](doc:transactions).

* **Can I cancel a transaction and refund the customer?**

 An authorized transaction can be canceled to get the money refunded in the customer account using the **Cancel** menu option from the **Actions** menu. The cancel function does not work for Captured transactions. For more information, refer to  [Transactions Dashboard](doc:transactions).

* **I am unable to view my transactions on the Dashboard**

You need to use the **Date** filter to filter the transactions based on the date range. For more information, refer to [Transactions Dashboard](doc:transactions).

## **Refunds**

* **How to get a Refund for payments made using various PayU India products**?

You can Initiate a refund on Dashboard in the **Refunds** module. For more information, refer to [Refunds Dashboard](doc:refunds-dashboard).

* **How long does it take to get a refund?**

Refunds will take between 5-21 days for the refund amount to reflect in your customer’s bank account. In the case of Net Banking transactions, certain government banks may take some more days. You will be communicated over email with the status (successful or failed) once the request for a refund is processed.

* **How to track my refunds?**

You can track refunds using the **Refunds** tab of the *Transactions* page. For more information, refer to [Refunds Dashboard](doc:refunds-dashboard).

* **How does Chargeback differ from Refunds?**

A chargeback is raised by the customer to the issuing bank for many reasons like a fraudulent transaction, unsatisfactory product or service delivery, etc., but a refund is initiated by you (merchants) after your customer requests a refund or a transaction has failed for the customer.

## **Settings and Webhooks**

* **Can I change the logo or theme on the PayU Payment page that is redirected from my website**?

Yes, you can change the logo or theme on the PayU Payment page. For more information, refer to [Configure User Settings](doc:configure-user-settings).

* **How do I control the permissions for the users addedto the Dashboard?**

You can create roles and then configure or assign those roles to a user while adding to Dashboard. For more information, refer to [Manage User and Permissions](doc:manage-user-and-permissions).

* **Does PayU offers Vernacular support or can I change the language of the content displayed on the PayU Payment page that is redirected from my website**?

Currently, you can change the language or display the content on the PayU Payment page when posting the **\_payment** API transaction with PayU Hosted Checkout Integration. For more information, refer to [Change the Language](doc:configure-user-settings#change-display-language--vernacular-support).

* **I am unable to view International Payments,<Glossary>BNPL</Glossary> , Recurring Payments (ENACH), or EMI payment mode on the PayU Payment page on my website.**

You can enable the payment modes or request PayU to enable by using the *Payment Modes* page on Dashboard. For more information, refer to [Configure User Settings](doc:configure-user-settings#checkout-payment-modes).

* **I am unable to view PayPal payment mode on the PayU Payment page that is redirected from my website.**

You can enable PayPal as an international payment mode using the International Payment tab of the Payment Modes page on the Dashboard. For more information, refer to [Configure User Settings](doc:configure-user-settings#checkout-payment-modes).

* **Can I add users from my company to access the Dashboard?**

You can add users on Dashboard and grant permissions to the users. For more information, refer to [Manage User and Permissions](doc:manage-user-and-permissions).

* **What is the purpose of User Settings in the PayU Dashboard?**

User settings allow you to customize your personal and organizational information, notifications, access, and security settings, and enable payment modes.

* **How do I access my user settings on the Dashboard?**

To access your user settings in the PayU Dashboard, click the drop-down menu (with your Login Name) at the top-right corner of the Dashboard and select **Settings**.

* **How do I change my bank or business details on the Dashboard**?

To change your bank or business details on the Dashboard, click the drop-down menu (with your Login Name) at the top-right corner of the Dashboard and select **Profile**.

* **How do I change my organization information in the PayU Dashboard?**

To change your bank or business details on the Dashboard, click the drop-down menu (with your Login Name) at the top-right corner of the Dashboard and select **Profile**. Select the **Business Details** tab. Here, you can update your business website, GST, and Display Name. If you update the business website or GST, PayU will verify it.

* **How do I configure my notifications in the PayU Dashboard?**

To configure your notifications in the PayU Dashboard, select the **Notifications** tile on the *Settings* page. You can select the types of notifications you want to receive and specify the channels through which you want to receive them.

* **How do I manage users of my organization on Dashboard?**

To manage the users of your organization in the PayU Dashboard, select the **User and Permissions** tile on the *Settings* page. You can manage users and roles and enable two-step verification (two-factor authentication).

* **How do I change the language on the PayU Checkout page (that is redirected from my website) in the PayU Dashboard?**

To manage the users of your organization in the PayU Dashboard, select the **Checkout Settings** tile on the *Settings* page. In the **Language Settings** section of the **Checkout Settings** pane, you can select your preferred language from a list of available options. For more information, refer to [Change Display Language](doc:configure-user-settings#change-display-language--vernacular-support).

* **What do I do if I forget my login credentials for the PayU Dashboard?**

If you forget your login credentials for the Dashboard, you can use the **Forgot Password** option on the Login page to reset your password. For more information, refer to [Reset Password for PayU Dashboard Login](doc:reset-password-for-payu-dashboard-login).

If you have any trouble resetting your password, you can contact PayU’s customer support team for assistance or [raise a ticket with PayU](https://help.payu.in/).

* **What is a webhook?**

A webhook is a way for PayU to send real-time notifications to your application or server whenever a transaction or event occurs in the PayU system. This allows you to automate and streamline your payment processing workflow.

* **How do I set up a webhook on the Dashboard?**

To set up a webhook, select the **Webhook** tile on the *Settings* page and then click **Add Webhook**. Enter the URL of your application or server where you want to receive the webhook notifications and select the events you want to be notified about. For more information, refer to [Manage Webhooks using Dashboard](doc:manage-webhooks-using-dashboard).

* **Can I create webhooks manually?**

You can webhooks easily using Dashboard or manually. To create webhooks manually, refer to [Webhooks](doc:webhooks).

* **What events can I receive webhook notifications for?**

PayU supports a wide range of events so you can receive webhook notifications for, such as successful payments, failed payments, refunds, and chargebacks.

* **How do I update or delete a webhook?**

To update or delete a webhook, click the **Update** button or **Delete** button to modify or delete on the *Create Webhooks* page. For more information, refer to [Manage Webhooks using Dashboard](doc:manage-webhooks-using-dashboard).

* **Is there a limit to the number of webhooks I can set up?**

No, there is no limit to the number of webhooks you can set up in the PayU Dashboard. You can set up as many webhooks as you need to support your payment processing workflow.

* **Is my data and payment information secure when using webhooks?**

PayU takes care of the security and privacy of your data and payment information. PayU uses industry-standard security measures to protect your data and money, and will only use your information for the purpose of sending webhook notifications. However, it’s important to ensure that your application or server is also secure to prevent any potential data breaches or security incidents.

* **Do I need to whitelist any IP address on my Firewall to receive a response from the PayU servers?**

For webhooks created using Dashboard, you need not do any whitelisting of the IP addresses.

## **Settlements**

* **What does a settlement mean?**

Settlement is the process through which a merchant receives the money paid by their customers/consumers for a particular product or service, in their bank account.

* **Where can I view my Settlements on the Dashboard?**

You can view or filter the settlement on the *Settlements* page under the **Track** section of the Dashboard. For more information, refer to [Settlements Dashboard](doc:settlements-dashboard).

* **How long does it take to get my first payment in my bank account?**

The time that it takes to receive payments in your bank account depends on if you have completed your bank verification process and the type of settlement you have chosen. Generally, payments are automatically transferred to your bank account in the cycle of 2 business days from the successful transaction date, i.e. T+2 (excluding bank holidays).

**Note:** Verification of your bank account registered with PayU and uploading the required documents along with a signed service agreement is mandatory for receiving settlements.

* **What is the settlement cycle that PayU offers?**

Our standard settlement cycle is T+2 working days, with T being the date of the successful transaction. This means that payments will be settled in your bank account after two working days of the date of the transaction registered with us, excluding bank holidays.

* **Where can I see my settlement summary?**

You are notified of your settlements on your Dashboard. To view your settlement summary, refer to [Settlements Dashboard](doc:settlements-dashboard)..

* **How can I check the details of my particular settlement?**

To check the details of a particular settlement, refer to [Settlements Dashboard](doc:settlements-dashboard).

* **I can see my settlement status as in progress. What does that mean?**

It means your settlement has been initiated from our end, and it will be processed in the next payment cycle.

* **The status of my settlement shows as on hold. What do I do?**

Your settlements are placed on hold if there are some risk issues with your payments. You will be required to upload the proof of delivery and other details to confirm the delivery of the service/product. Our team will review the shared documents and help you resolve the issue.

* **How to export the Settlement records?**

You can export Settlement records using the **Export** button on the *Settlements* page. For more information, refer to [Settlements Dashboard](doc:settlements-dashboard).

* **My company has an Admin Dashboard where we want to view and download the transaction reports. Which APIs must be used to fetch transactions so that they can be used to integrate into our Admin Dashboard?**

You can use the following APIs to get the transaction details:

* The following Transaction Details APIs are used to extract the transaction details between two given periods.
  * [Get Transaction Info API](ref:get_transaction_info_api)
  * [Get Transaction Details API](ref:get_transaction_details_api)
* The following Settlement Details API is used to retrieve settlement details that the bank has to settle you.
  * [Settlement Details](ref:settlement-details-range-api)

## **Collect or Send Payments**

* **How do I create an invoice?**

To create an invoice, navigate to the *Invoices* page of the **Collect Payments** section of the Dashboard and click **Create Invoice**. You’ll need to enter the details of the transaction, such as the buyer’s name and contact information, the products or services sold, and the price. For more information, refer to [Payment Invoices](doc:invoices-dashboard).

* **Can I customize the tax details of my invoices?**

Yes, you can customize the tax details on the invoice. For more information, refer to [Payment Invoices](doc:invoices-dashboard).

* **How do I send an invoice to a buyer?**

You can send an invoice to a buyer directly from the PayU Dashboard. After you provide the details while you create an invoice, click **Send Invoice**. You can also copy the invoice link and send it to the buyer through email or any other communication channel. For more information, refer to [Payment Invoices](doc:invoices-dashboard).

* **How can my customers pay the invoice?**

Your customers can pay the invoice online using any of the payment methods which you have enabled on the PayU Payment page (PayU Hosted Checkout), such as Credit/Debit cards, Net Banking, UPI, or Wallets. They have to click the payment link in the invoice and they will be redirected to the PayU Payment page.

* **Can I track the status of my invoices?**

Yes, you can track the status of your invoices on the *Invoices* page of the **Collect Payments** section of the Dashboard. You’ll be able to see whether the invoice has been sent, viewed, paid, or canceled. For more information, refer to [Payment Invoices](doc:invoices-dashboard).

* **Is there a fee for using the invoice feature on the Dashboard?**

Yes, there is a fee for using the invoice feature. The fee varies depending on the number of invoices you create and the payment methods used by your customers. For more information, contact your PayU Key Account Manager.

## **Offers**

* **I am getting Transaction Failed with the Offers key applied.**

The Offer keys that you are using would have not been in the “Live” state, Use only the “Live” offer keys to go ahead with the transaction. For more information on managing offers on Dashboard, refer to [Manage Offers](doc:manage-offers).