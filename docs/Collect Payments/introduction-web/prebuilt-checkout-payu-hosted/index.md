---
title: PayU Hosted Checkout
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Prebuilt Web Checkout or PayU Hosted Checkout Integration
  description: >-
    Integrate PayU Hosted Checkout with PayU to redirect customers to a secure,
    prebuilt payment page. Accept UPI, cards, net banking, and wallets with
    SHA-512 hash, surl/furl callbacks, and test-to-production go-live steps for
    India merchants.
  keywords:
    - payu hosted checkout integration guide india
    - prebuilt payment page redirect checkout payu
    - payment gateway hosted checkout api _payment payu
    - payu web checkout sha512 hash surl furl integration
    - online payment collection website checkout payu india
    - payu hosted checkout test sandbox go live checklist
    - razorpay cashfree alternative payu hosted checkout india
    - payment gateway integration for websites payu hosted
    - payu collect payment api hosted checkout developer guide
    - accept upi cards netbanking wallet hosted checkout payu
  robots: index
next:
  description: ''
---
Prebuilt Web Checkout or PayU Hosted Checkout is a payment integration method provided by PayU for merchants who want to accept payments on their website. It offers a secure way to collect payments from customers by redirecting them to a PayU-hosted payment page.

## How it works?

To use PayU Hosted Checkout, merchants need to integrate the PayU payment gateway into their website. Once integrated, customers can select the payment method they want to use and enter their payment details on the payment form. When they click the **Pay** button, they will be redirected to a PayU-hosted payment page where they will complete the payment process.

Once the payment is processed, the customer will be redirected back to the merchant's website where they can view the payment result.


<Image src="https://files.readme.io/932f800-payuhosted_wf.png" alt="workflow diagram - How it works?" align="center" border={true} />


## Customer journey

The following diagram illustrates the overall customer journey:


<Image src="https://files.readme.io/bc1c758a83c0c601d161a5621e1fe47a6d4c757e847a893b33b05419972e693a-b7b3bc19c28693be346591ec8a2c29ee07fcf47cb088bc6c9a6c34950c2af0dc-payu_hosted_checkout-workflow.png" alt="workflow diagram - Customer journey" align="center" />


The following sample customer journey is for cards payment mode:

1. The customer clicks **Pay Now** on merchant website after checkout.
2. The customer is redirected to _PayU Payment_ page.


<Image src="https://files.readme.io/1ee3893480e6e3d3c1e28d6ecffc4c52d1b3e8f2aba0247c9eb486dfef0fafc5-Screenshot_2024-09-06_at_11.54.02_AM.png" alt="PayU Dashboard - The customer is redirected to _PayU Payment _page" align="center" width="622px" border={true} />


3. The customer chooses a payment mode from the _PayU Payment_ page. For example, **Cards (Debit/Credit)**.
4. The card details are provided by the customer and clicks **Proceed**.


<Image src="https://files.readme.io/fd09cbd284ffe7fb3b60d03e2acd8a5a51d850dd1795f1eca9879893b3569603-Screenshot_2024-09-06_at_11.56.40_AM.png" alt="card payment screen - The card details are provided by the customer and clicks Proceed" align="center" width="622px" border={true} />


A consent message is displayed whether the card the details can be stored.


<Image src="https://files.readme.io/caa8481-Screenshot_2023-10-05_at_10.37.33_AM.png" alt="card payment screen - A consent message is displayed whether the card the details can be stored." align="center" width="622px" />


5. Customer clicks **Save and Continue**.
6. The OTP page is displayed where the customer enters OTP sent to the them.


<Image src="https://files.readme.io/289fa82-Screenshot_2023-10-05_at_10.37.42_AM.png" alt="OTP verification screen - The OTP page is displayed where the customer enters OTP sent to the them" align="center" width="422px" />


6. PayU redirects back to the merchant website based on the success URL (surl) or failure URL (furl) specified.

## Features of PayU Hosted Checkout

PayU manages the checkout experience on your website. The features of PayU Hosted Checkout are:

- Enables the customer to select the payment option through the readymade payment page hosted on the PayU server, and accept corresponding payment details. After submitting the details, PayU will take the customer to the desired payment options webpage for further authentication. For configuring payment modes on payment page, refer to [Configure Checkout Payment Methods](https://docs.payu.in/docs/payu-payment-page-customization#configure-checkout-payment-methods-and-settings).
- Facilitates access to color schemes, customize logo, and display language (some Indian languages supported) though PayU owns this page. For more information, refer to [Change the Language](https://docs.payu.in/docs/payu-payment-page-customization#change-the-language)  and  [Configure Checkout Settings](https://docs.payu.in/docs/payu-payment-page-customization#configure-checkout-payment-methods-and-settings).
- Enables easy and quick integration so you can integrate with minimal technical knowledge.

Web Checkout provides multiple payment options that can be easily pre-configured by you on-demand, according to your business case. You can execute PayU Hosted Checkout integration efficiently with PayU web payments systems using a PG integration kit provided by PayU.

## Benefits of PayU Hosted Checkout

The following is a list of benefits of PayU Hosted Checkout:

- Simplified payment workflow for your customers while reducing the cost of designing complex payment functionalities within your environment.
- Going live with new payment modes requires zero development. They can be enabled with a simple switch.
- Assures the security of your customer payment credentials.
- PCI-DSS certifications to operate your facility are not mandatory.
- PayU Hosted Checkout extends cross-functional support at organizational roles within the organization.
- The Native UI feature of Web Checkout Pro allows you to ensure continuous usability (UX) and brand coherence by customizing the PayU-hosted environment with the business logo and color scheme of your choice, simulating your business website.
- Offers zero direction OTP authentication flow for cards with Native OTP.
- Supports specific and generic intent for UPI payments on mobile web
- Personalized payment experience (using recommendations) and offers.

## List of APIs used for integration

| Use case → Reference                                                                                                                            | `command` / primary value                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Collect payment (redirect to PayU) — [Collect Payment API (PayU Hosted Checkout)](https://docs.payu.in/reference/_payment_payu_hosted_checkout) | Browser form `POST` to `_payment API` (see below table) |
| Verify a payment — [Verify Payment API](https://docs.payu.in/reference/verify_payment_api)                                                      | `verify_payment`                                        |
| Check transaction info — [Check Action Status with PayU ID](https://docs.payu.in/reference/check_action_status_api_with_payu_id)                | `check_action_status`                                   |
| Get transaction by txnid — [Get Transaction Info API](https://docs.payu.in/reference/get_transaction_info_api)                                  | `get_transaction_info`                                  |
| Refund a transaction — [Refund Transaction API](https://docs.payu.in/reference/refund_transaction_api)                                          | `cancel_refund_transaction`                             |

> **Collect Payment endpoint:** `POST https://test.payu.in/_payment` (test) · `POST https://secure.payu.in/_payment` (production)<br />`hash`**&#x20;on&#x20;**`_payment`**&#x20;(standard sequence):** `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)`<br />**Post-service (**`command`**&#x20;APIs) endpoint:** `POST https://info.payu.in/merchant/postservice.php?form=2`<br />**Post-service hash formula:** `sha512(key|command|var1|SALT)`

## Next Steps

To integrate PayU Hosted Integration on your website or mobile, refer to:

- [Web Integration - PayU Hosted](https://docs.payu.in/docs/prebuilt-checkout-page-integration) using the **Collect Payment API (\_payment** API),

- [Integrate WebView for Mobile Apps](https://docs.payu.in/docs/webview-for-mobile-apps) by embedding PayU's Hosted Checkout experience inside a WebView container within your mobile app.

<br />

> 📮
>
> **Postman Collection**: Download the PayU Hosted Checkout Postman Collection from the following location:
>
> [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/collection/rocz44o/payu-hosted-checkout-collection-complete-integration](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/collection/rocz44o/payu-hosted-checkout-collection-complete-integration)

<br />
