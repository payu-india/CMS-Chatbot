---
title: FAQs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: FAQs for Web Checkout Integration
  description: ''
  robots: index
next:
  description: ''
---
## General

* **I am an SMB merchant. Which Web Checkout Integration I need to choose for the website?**

  OR

* **I am an SMB merchant and do not have the resources to design pages for collecting payments on my website.**

  PayU Hosted Checkout, Pre-Built Pages, or Redirect-based integration is recommended for your website as you need to design or develop pages to accept payment. For more information, refer to [PayU Hosted Checkout](doc:prebuilt-checkout-payu-hosted).

* **What is my authentication header or signature to be included in the payment requests or other APIs?**

  You have to include the Key and Salt in the API requests with API provided by PayU. For getting your Key and Salt on the Dashboard, refer to [Access Production Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard)

* **Which Web Checkout will be suitable for me as a merchant?**

  The choice of Web Checkout option depends on your resources and requirements and choose as follows:

* If you want a quick and easy checkout integration without any development effort, the **PayU Hosted Checkout** integration is suitable.

* If you have the resources to develop and maintain your own checkout page and want more control over the checkout process, the Merchant Hosted Checkout integration is suitable.

* If you want to customize the checkout page without the need for coding skills, the **PayU Web SDK** (Low Code) integration is suitable.

* **I am a small merchant or developer and not an expert in developing websites with payment integration. Could you recommend the best approach for Web Checkout integration?**

  PayU recommends you first do the Web Checkout integration using Low-Code SDK as it allows you to integrate low-coding efforts and to integrate with PayU much faster and swiftly. For more information, refer to [No-Code Integration](doc:introduction-no-code-payments-integration) and [Checkout Plus](doc:checkout-plus-integration).

  Later, you can integrate using Prebuilt Checkout Pages or PayU Hosted Checkout integration. For more information, refer to [PayU Hosted Checkout](doc:prebuilt-checkout-payu-hosted).

* **What is PayU Hosted Checkout Integration and will it suit my payment integration needs?**

  PayU Hosted Checkout is a fully hosted solution where PayU handles the entire checkout process on behalf of the merchant. It can also be known as Prebuilt Checkout Page or Redirection-based checkout as the customer is redirected from your website to collect payment. This is the simplest checkout option to integrate and requires no development effort on the merchant’s side. PayU provides a ready-made checkout page, which is hosted on PayU’s servers. The page is optimized for conversion and provides a seamless checkout experience for customers. Merchants can customize the look and feel of the checkout page to match their brand and can choose from multiple payment methods. This option is suitable for merchants who want a quick and easy checkout integration and don’t have the resources to develop and maintain their own checkout page.

* **What is PayU Web SDK and is it easy to integrate?**

  PayU Web SDK is a low-code checkout solution that allows merchants to create a checkout page using a visual interface. This option requires no coding skills and provides a faster integration than the Merchant Hosted Checkout option. Merchants can customize the look and feel of the checkout page and can choose from multiple payment methods. PayU handles the payment processing through their API. This option is suitable for merchants who want to create a customized checkout page without the need for coding skills or a dedicated development team. It is also suitable for merchants who want a faster checkout integration than the Merchant Hosted Checkout option.

* **What are the prerequisites for Merchant Hosted Checkout integration?**

  You need to design your website to collect the complete details of your customers and collect payment details. Also, fill out the “[Self-Assessment Questionnaire A-EP and Attestation of Compliance](https://www.pcisecuritystandards.org/documents/PCI-DSS-v3_2-SAQ-A_EP-rev1_1.pdf)” form. For more information, refer [Merchant Hosted Checkout](doc:custom-checkout-merchant-hosted).

* **How do I enable Server-to-Server integration for my account?**

  You need to contact your PayU Key Account Manager to enable Server-to-Server integration.

* **We have developed a new website and wanted Web Checkout integration on our new website. How do we perform seamless integration and which encryption mechanism is used?**

  Yes, PayU offers seamless integration or Merchant Hosted Checkout. You have to hash your requests, reverse hash response from PayU, and PayU does use any other encryption mechanism. For seamless integration and hashing logic, refer to the following documentation:

  * [Custom Checkout or Merchant Hosted Checkout](doc:custom-checkout-merchant-hosted)

  * [Generate Hash](doc:generate-hash-merchant-hosted)

* **We are partnering with a PSU Bank to enable their cards on Recurring Payments to PayU Merchants base. How to integrate PayU Recurring Payments APIs?**

  PayU offers a suite of APIs for Recurring Payments or Standing Instructions (SI). For more information, refer to [Recurring Payments](doc:introduction-recurring-payments-integration).

* **We are getting the following exception with Web Checkout Integration:**

Exception :javax.net.ssl.SSLHandshakeException: com.ibm.jsse2.util.h: PKIX path building failed:
com.ibm.security.cert.IBMCertPathBuilderException: unable to find valid certification path to requested target
at com.ibm.jsse2.k.a(k.java:37)

This issue is due to security certificate expiry. If you are using a custom keystore, PayU recommends you add domain’s root certificate to the custom keystore. If you are using the default keystore, enable debug logs and share SSL handshake logs with PayU support.

* **At the time of payment, while entering the card number, the system accepts 19 digits.**

  A card number can have 13-19 digits depending on the card type, so the number of digits depends on the card used. For more information on card number formats and how to validate them, refer to [Card Number Formats](doc:card-number-formats).

* **While entering the card details on the PayU Payment page with PayU Hosted Checkout integration, the expiry date should give the date and year format in separate selection tabs so that a customer can select from the provided drop-down list. Can this be implemented?**

  With PayU Hosted Checkout, this cannot be implemented, however, you can implement it in Merchant Hosted Checkout integration as the website or app is developed and maintained by you (merchant).

* **What are the test card details to test my integration?**

  For test card details, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets).

* **I am using the test card details as described in the** [**Test Card Details**](doc:test-cards-upi-id-and-wallets) **section, but cannot find the card expiry month or year for the test card.**

  You can use any month or year of a future date for test cards mentioned in the [Test Card Details](doc:test-cards-upi-id-and-wallets) section.

* **Where can I find the list of error codes and messages returned in the error and error_message parameter of the response for a payment request?**

  For possible errors (in the **error_message** parameter) and error codes (in the **error** parameter) for a transaction, refer to [Error Codes](ref:error-codes)

* **Which PayUs integration enables us to set up a UPI 2.0 mandate from our users for collection of Rs.1000 on a daily basis for 10 days and to remit the money to the user’s account from the payment aggregator?**

  You can use the recurring payments with UPI. For more information, refer to the following Recurring Payments Integration docs:

* [UPI Payment Experience](doc:upi-recurring-payment-experience-for-upi)

* APIs
  * [Payment Consent Transaction with Merchant Hosted Checkout ](ref:payment-consent-transaction-merchant-hosted)(one-time)
  * [Recurring Payment API](ref:recurring_payment_api) (collect)

* **How do I integrate my Web Checkout integration to collect international payments or** Multi-Currency Pricing (MCP)?**?

  PayU offers Dynamic Currency Conversion (DCC) or Multi-Currency Pricing? API. For more information, refer to [Multi-Currency Pricing or International Payments](doc:introduction-dynamic-currency-conversion).

## PayU Hosted Checkout Integration

* **Can I enforce specific payment modes with PayU Hosted Checkout integration?**

Yes, you can enforce payment modes with PayU Hosted Checkout integration. For more information, refer to [Enforce Pay Method or Remove Category](doc:enforce-pay-method-or-remove-category).

* **What are the prerequisites for using the PayU Hosted Checkout or Redirection-Based Flow integration?**

  There is no prerequisites for using the PayU Hosted Checkout integration.

* **Do I need to create pages to collect payment details from customers and store them for PayU Hosted Checkout integration?**

  No, you need not design pages to collect payment details. After your customer’s checkout, you need to redirect to PayU Payment page where your customers will be provided to collect payment details. PayU does not store your customer’s card information if they had saved their cards on PayU vault.

* **How do I enable QR as a payment mode for my PayU integration?**

  You need to contact your PayU Key Account Manager (KAM) to enable QR payments.

### Request/Response Parameters

* **How do I handle payment failures or errors?**

  When you post a payment request using the **Collect Paymen**t (_payment) API, you may face errors or payment failures. The **Collect Payment API** provides error codes and messages that can help you diagnose and handle payment failures or errors. You may also need to implement error handling and retry logic in your integration to ensure that payments are processed correctly and reliably. For more information, refer to [Error Handling](doc:error-handling)

* **l migrated my payment integration from PayUMoney to PayU. What is the endpoint or environment for the Collect Payment API?**

  The endpoint for PayUMoney or PayU remains the same, that is:

  [https://secure.payu.in/_payment](https://secure.payu.in/_payment)

* **I migrated from PayUMoney to PayU and I am getting the payment failed error in the response with the following request parameters:**

| key'=>9JpriI, 'productinfo'=>XYZ, 'UDF1'=>null, 'UDF2'=>null, 'UDF3'=>null, 'UDF4'=>null, 'UDF5'=>null, 'surl'=>[https://careuat.careinsurance.com/cms/public/payumoney/response](https://careuat.careinsurance.com/cms/public/payumoney/response), 'furl'=>[https://careuat.careinsurance.com/cms/public/payumoney/response](https://careuat.careinsurance.com/cms/public/payumoney/response), 'curl'=>[https://careuat.careinsurance.com/cms/public/payumoney/response](https://careuat.careinsurance.com/cms/public/payumoney/response), 'one_click_checkout'=>1, 'Hash'=>**********************************, 'PG'=>CC, 'bankcode'=>CC, 'txnid'=>********************, 'amount'=>3755, 'Firstname'=>Ashish, 'Email'=>[ashish.kumar@payu.in](mailto:ashish.kumar@payu.in), 'Phone'=>980********, 'ccnum'=>5123 4567 8901 2346, 'ccname'=>test, 'ccvv'=>123, 'ccexpmon'=>03, 'ccexpyr'=>2023, 'CHECKSUMHASH'=>'', |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

You need to remove the ‘**one_click_checkout’=>1**‘ parameter and its value (on Line 11) from the request as it is applicable only for PayUMoney only. For more information on the request parameters, refer to any of the following based on the integration:

* [Integration Steps for PayU Hosted Checkout](doc:prebuilt-checkout-page-integration)

* [Custom Checkout](doc:custom-checkout-merchant-hosted)

* **I am trying to verify payment by API for recurring transactions with the following endpoint, but it is throwing an error.**

  [https://secure.payu.in/merchant](https://secure.payu.in/merchant)

  You must use the following URL for the **Production** environment:

  [https://info.payu.in/merchant/postservice.php?form=2](https://info.payu.in/merchant/postservice.php?form=2)

* **I used the following endpoint or environment for Verify Payment API (verify_payment) API and got the below response:**

[https://secure.payu.in/merchant](https://secure.payu.in/merchant)

| \{  "status": 1,  "msg": "1 out of 1 Transactions Fetched Successfully",  "transaction_details": \{  "a01bb54681889e62fe917e37ed70c78e": \{  "mihpayid": "16475396216",  "request_id": "",  "bank_ref_num": "6721435065356559506102",  "amt": "2.00",  "transaction_amount": "2.00",  "txnid": "a01bb54681889e62fe917e37ed70c78e",  "additional_charges": "0.00",  "productinfo": "Purchasing mediology2913 - Recurring Paid Digi 1",  "firstname": "user60f153242371c",  "bankcode": "CC",  "udf1": null,  "udf3": null,  "udf4": null,  "udf5": null,  "field2": "533085",  "field9": "Transaction is Successful",  "error_code": "E000",  "addedon": "2022-12-27 17:47:00",  "payment_source": "payu",  "card_type": "VISA",  "error_Message": "NO ERROR",  "net_amount_debit": 2,  "disc": "0.00",  "mode": "CC",  "PG_TYPE": "CC-PG",  "card_no": "XXXXXXXXXXXX0002",  "name_on_card": null,  "udf2": null,  "status": "success",  "unmappedstatus": "captured",  "Merchant_UTR": null,  "Settled_At": "0000-00-00 00:00:00"  }  } } |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

You must the following endpoint or environment for the **Verify Payment** API:

[https://info.payu.in/merchant/](https://info.payu.in/merchant/)

* **The Payment page is displaying on the Cards payment mode and not displaying other payment modes such as UPI, Wallets, etc. Please enable other payment modes for my account?**

  Check the request parameters in the payment request that you are posting to PayU. You have to check if the **pg** parameter is posted with **CC**, so only cards payment mode is displayed on PayU Payment page. For more information, refer to the [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout).

### Key and Salt

* **I want Key and Salt for testing my Web Checkout integration. Can I create a test account with PayU?**

  Yes, you can create an account for testing in the following URL:

  [https://uat-onepayuonboarding.payu.in/app/account/signup](https://uat-onepayuonboarding.payu.in/app/account/signup)

  For more information on how to get test Key/Salt, refer to [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).

* **I am unable to view the Key and Salt or not able to access it on Dashboard.**

  If your website is not validated or onboarding is not completed by PayU, you will not be able to access or view the Key and Salt. To generate key and salt, refer to [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).

* **The Key and Salt which I copied from Dashboard are not working**

  Check whether you are using the **Production** endpoint for Production Key and Salt. For PayU Hosted or Merchant Hosted integrations, you have to use the following endpoints with **_payment** API:

| **Test Environment**       | [https://test.payu.in/_payment](https://test.payu.in/_payment)     |
| -------------------------- | ------------------------------------------------------------------ |
| **Production Environment** | [https://secure.payu.in/_payment](https://secure.payu.in/_payment) |

If the Key and Salt are still not working, contact your KAM or raise a ticket with PayU support on [help.payu.in](https://help.payu.in/).

* **Do I need to complete KYC for the test account?**

  No, KYC is not required for a test account and you can generate test Key and Salt. For more information, refer to [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).

* **Can I get the Test Key and Salt from PayU for testing**?

  Yes, to generate the test Key and Salt, refer to [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).

## Integration APIs

* **How do I validate a customer’s VPA before proceeding with UPI payment transaction?**

  You can use the **Validate UPI Handle** API to validate a customer’s VPA. For more information, refer to [Validate UPI Handle API](ref:validate_vpa_api).

* **Which API is used to capture at a transaction level: the TDR, Service Tax, NCEMI / Discount, UTR Number amount along with the other details for a given order ID?**

  You can use the **Transaction Details API** to check these details. For more information, refer to [Transaction Detail APIs](ref:transaction-detail-apis).

* **We want to proactively monitor and alert our users that the bank is down to accept UPI transactions. Is there any API to check this?**

  You can use the **Get Net Banking Status** API with **var1** parameter as UPI. This will help you to get all acquiring and NPCI-related downtime.

* **I tried to get the settlement details using the release_settlement API, but I was not getting the correct response**.

  You need to use the Retrieve Bank Settlement Details (**get_settlement_details**) API to get the settlement details. The **Release Settlement Details** API is used to release the settlements to child merchants in Split Settlements. For more information, refer to [Settlement Details](ref:settlement-details)

* **We are receiving the following error code when trying to enforce payment with PayU Hosted Checkout as in the following payment request. How to resolve this error?**

  HTTP response code: 400

| curl -X POST "[\<[https://test.payu.in/_payment](https://test.payu.in/_payment)>] -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=c52cfa446d&amount=253.00&productinfo=rbl&firstname=ashish&email=[ashish@gmail.com](mailto:ashish@gmail.com)&phone=9876543210&txn_s2s_flow=4&lastname=kumar&surl=\<[https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6935fd3653463af23cf90363e5bfafde89cc403f54f6d6e958fcfcfd9b4a03c87c2c76630b04c3238ed297cbdb9c58932154188b85987c0f9bc3f0862e836a22&enforce_paymethod=netbanking](https://apiplayground-response.herokuapp.com/\&furl=https://apiplayground-response.herokuapp.com/\&hash=6935fd3653463af23cf90363e5bfafde89cc403f54f6d6e958fcfcfd9b4a03c87c2c76630b04c3238ed297cbdb9c58932154188b85987c0f9bc3f0862e836a22\&enforce_paymethod=netbanking) | UPI&s2s_client_ip=0:0:0:0:0:0:0:1&s2s_device_info=PostmanRuntime/7.29.2&salt_version=1>" |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------- |

You must remove the **txn_s2s_flow=4** parameter from the payment request. The **txn_s2s_flow** parameter must be used only for Seamless integration (Merchant Hosted or S2S Integration).

* **I am using verify_payment to check payments made using the AMEX cards.What is the response parameter values for PG_Type and bankcode will be for AMEX card payments with ?**

  The payments made using AMEX card have the following response parameters:

[mode] => **CC**

[PG_TYPE][PG_TYPE] => **CC-PG**

[bankcode] => **AMEX**

## Hashing

* **I am trying to generate hash value with Python language binding and getting hash error.**

  The correct logic of hashing scenarios for payment request are:

* **Scenario 1**: When all the udf parameters (udf1-udf5) are posted by the merchant, hash is calculated as:

sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)

* **Scenario 2**: If only some of the udf parameters are posted . For example, if udf2 and udf4 are posted and udf1, udf3, udf5 are not, hash is calculated as:

sha512(key|txnid|amount|productinfo|firstname|email||udf2||udf4|||||||SALT)

* **Scenario 3**: If none of the udf parameters (udf1-udf5) are posted, hash is calculated as:

sha512(key|txnid|amount|productinfo|firstname|email|||||||||||SALT)

Check the request payload you have passed in the **Payment** API (**_payment**) and accordingly generate the hash value. For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted)

* **If I want to include UDFs (udf1 to udf10) in hash, what is the hash format?**

  You can include upto udf5 (udf1 to udf5) in the following hash format:

key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT

You cannot include only udf1 to udf5, so udf6 to udf10 cannot be included with hash. For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted).

## Test Environment

* Is there any GMW limit for posting transactions in the Test environment?

  You can post transactions amounting to 50 crores of GMV in the Test environment.

* **We are getting the card token info in the card_token parameter and sometimes in the CardToken parameter of the response. Which parameter I must check for the card info?**

  In the test environment, the card token can come to any of these parameters (**cardToken** and **card_token**), PayU suggests you consume both the parameter where you are getting the value.

## UPI

* **What is UPI Intent?**

  UPI Intent allows customers to make payments to a merchant without sharing their bank account details. When a user initiates a UPI Intent payment, they are redirected to their UPI-enabled mobile banking app, where they can review the transaction details and authorize the payment.

* **What is UPI Collect?**

  UPI Collect allows merchants to request payments from their customers. With UPI Collect, the merchant generates a payment link or QR code, which the customer can use to initiate the payment through their UPI-enabled mobile banking app.

* **What is the difference between UPI Intent and UPI Collect?**

  The main difference between UPI Intent and UPI Collect is the direction of the payment flow. With UPI Intent, the user initiates the payment, while with UPI Collect, the merchant initiates the payment request.

## Payment Links

* **I am a PayU’s partner and I onboarded merchants to PayU. How do I my merchants can collect payments?**

  Merchants onboarded by partners using [Refer Merchants using Partner Portal](doc:partner-portal) or [Refer Merchants using Integration APIs](ref:partner-integration-api-introduction)can collect payments using PayU Hosted Checkout. For more information on PayU Hosted Checkout Integration, refer to [PayU Hosted Checkout](doc:custom-checkout-merchant-hosted).

* **Can PayU enable the following payment URL for UPI to create payment links**.

[https://info.payu.in/merchant/postservice.php](https://info.payu.in/merchant/postservice.php)

Payment Link is created in a similar method for both UPI & Non-UPI payment modes. The above URL is for the Production environment and not for the Test environment.

* **After uploading payment links in bulk using an excel, can I use re-use a payment link for multiple transactions?**

  Yes, a payment link can be re-used till the date of expiry as configured by you in the excel file used to generate the link.

## Server-to-Server Integration

* **What is PayU Server-to-Server Integration?**

  PayU Server-to-Server Integration is a method for integrating PayU’s payment gateway into your website or application. This integration allows you to collect payments from your customers securely and efficiently. For more information, refer to [Server-to-Server Integration](doc:server-to-server-integration).

* **What are the benefits of using PayU Server-to-Server Integration of Web Checkout?**

  The benefits of using PayU Server-to-Server Integration of Web Checkout include the ability to collect payments directly on your website, without the need to redirect customers to an external payment page. This method also allows you to accept multiple payment methods, including credit and debit cards, net banking, and mobile wallets. For more information, refer to [Server-to-Server Integration](doc:server-to-server-integration).

* **How does PayU Server-to-Server Integration of Web Checkout handle security?**

  PayU Server-to-Server Integration of Web Checkout uses a secure token-based system to ensure that sensitive customer data is not transmitted or stored on your website or application. All communication between your website and PayU’s servers is encrypted using industry-standard SSL/TLS encryption. For more information, refer to [Server-to-Server Integration](doc:server-to-server-integration).

## Native OTP

* **Is there a limit to the number of attempts to enter OTP for verification?**

  Yes, there is a limit to the number of attempts to enter OTP for verification. After a certain number of failed attempts, the transaction is declined. For more information, refer [Native OTP Flow Integration](doc:native-otp-flow-integration)

* **How is the security of the OTP verification process ensured?**

  The security of the OTP verification process is ensured by using the same secure encryption and authentication mechanisms as regular payment processing.
