---
title: PayU India API Reference
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: PayU API Documentation
  description: >-
    This document is the PayU India API Reference documentation, which provides
    developers with information on how to integrate PayU's payment processing
    capabilities into their applications and websites. It includes a list of
    APIs and instructions on how to use them.
  keywords:
    - PayU APIs
    - ' PayU API documentation'
    - ' PayU API reference'
  robots: index
next:
  description: ''
---
Welcome to the PayU India API Reference documentation. This comprehensive guide provides developers with the information they need to seamlessly integrate PayU's payment processing capabilities into their applications and websites. Whether you're building an e-commerce platform, a mobile app, or any online service that requires secure and reliable payment processing, our APIs have you covered. 

> 🚧 Limitations with API Reference
> 
> You cannot do test or mock API calls for certain APIs on this API Reference. PayU currently does not support the following APIs related to certain products or features with Test environment:
> 
> - General APIs
>   - Certain Refund flows
> - UPI flows with Server-to-Server
> - Refund Transaction
> - Recurring Payments or Subscriptions
>   - Flows involving UPI payment mode
> - Save Cards
>   - Model 2 - Zero Code Change flows
>   - Collect Payments
> - Split Settlements (only a few APIs supported)
> - TPV
> - Pre-authorize payment (with PayU Hosted Checkout integration)
> - Omnichannel
> 
> For the test card numbers, test UPI handle, test wallet, etc. to be used in API Reference, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets).

## How to use API Reference

You can try using the Test Environment or Sandbox with most of the PayU India APIs in API Reference. Enter the values for the parameters/field in the form data and then click **Try It**.  The response is displayed based on the values entered in the form data. 

PayU recommends you to follow these so that you will integrate easily:

- Understand the product integration steps on the **Integration Guide** and later refer to API Reference.
- The API Reference pages for various APIs allows you to make mock API calls with most of the PayU APIs (using a static test key for General or Integration APIs).  Also, it provides support in 16 language bindings, so you can get the source code in apart from cURL.
- It is recommended to follow the **Integration Checklist** for checkout or SDK integrations to ensure that your integration is complete before making your integration live.

> 📘 Notes:
> 
> - A static Test key is used with Test environment across the Collect Payment, General, Split Settlements and Pre-authorize APIs under [API Reference](/reference/). Hence, when you peruse the code on the API Reference, you need to replace the Test key with your Production key and Product environment URL.
> - All the parameters marked** required** must be filled to enable the **Generate Hash **button. 
> - The example listed (like a cookie) in each parameter field is  for reference purposed only, so it is suggested to type the values similar to the listed example.
> - Use only the the test card numbers, test UPI handle, test wallet, etc. in [API Reference,](/reference/) refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e146999-api-reference-instructions.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


## List of PayU India APIs

The API Reference is categorized into following:

[block:parameters]
{
  "data": {
    "h-0": "Collection",
    "h-1": "Links",
    "0-0": "**Collect Payment APIs**",
    "0-1": "\\- [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)  \n- [Collect Payment API - Merchant Hosted Checkout](ref:_payment_merchant_hosted)  \n- [Collect Payment API - Server-to-Server](ref:_payment-server-to-server)",
    "1-0": "**General APIs**",
    "1-1": "\\- [Check Transaction APIs](ref:check-transaction-apis)  \n- [Transaction Detail APIs](ref:transaction-detail-apis)  \n- [Refund APIs](ref:refund-apis)  \n- [Settlement Details](ref:settlement-details)  \n- [BIN APIs](ref:bin-apis)  \n- [EMI APIs](ref:emi-apis)  \n- [Health Check APIs](ref:health-check-apis)",
    "2-0": "**Payment Link APIs**",
    "2-1": "\\- [Create Payment Link API](ref:create-payment-links)  \n-  [Share Payment Link API](ref:share_payment_link_api)  \n- [Get Single Payment Link API](ref:get-single-payment-link)  \n- [Get All Payment Links API](ref:get-all-payment-links-api)  \n- [Create Invoice API](ref:create_invoice_api)  \n- [Expire Invoice API](ref:expire_invoice_api)",
    "3-0": "**Recurring Payment APIs**",
    "3-1": "\\- [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted)  \n- [Payment Consent Transaction with Merchant Hosted Checkout](ref:payment-consent-transaction-merchant-hosted)  \n- [Pre-Debit Notification API](ref:pre_debit_notification_api)  \n- [Recurring Payment API](ref:recurring_payment_api)  \n- [Manage Recurring Payment for Cards](ref:manage-recurring-payment-for-cards)",
    "4-0": "**Zion Subscription API**",
    "4-1": "\\- [Associating Plan in Defined Subscription API](ref:associating-plan-in-defined-subscription-interface)  \n- [Define Subscription API](ref:create-a-subscription)  \n- [Update Subscription API](ref:update-subscription-api)  \n- [Get List of Subscriptions API](ref:get-list-of-subscriptions-api)  \n- [Cancel Subscription API](ref:cancel-subscription-api)  \n- [Get Subscription Details API](ref:get-subscription-details-api)  \n- [Get Invoice API](ref:get-invoice-interfaces-api-zion)  \n- [Create Invoice API](ref:create-invoice-api-zion) ",
    "5-0": "**Offers APIs**",
    "5-1": "\\- [Fetch Offers API](ref:fetch-offers-api)  \n- [Validate Offer API](ref:validate-offer-api)",
    "6-0": "**Save Cards APIs**",
    "6-1": "\\- [Model 2-Zero Code Change](ref:model-2-zero-code-change-for-vault-integration)  \n &emsp; \\* [Get User Cards API](ref:get_user_cards_api)  \n  &emsp; \\* [Process Transaction with a Saved Card](ref:process-transaction-with-a-saved-card)  \n- [Model 3 – Simple REST APIs](ref:model-3-simple-rest-apis)  \n &emsp; \\* [Save a Card API](ref:save_card_api)  \n &emsp; \\* [Edit a Saved Card API](ref:edit_saved_card_api)  \n          &emsp; \\* [Get User Cards API](ref:get_user_cards_api_model3)  \n  &emsp; \\* [Delete a Saved Card API](ref:delete_saved_card_api)  \n  &emsp; \\* [Get Payment Details (Cryptogram)](ref:get_payment_details_cryptogram)  \n  - [Collect Payments - Save Card](ref:collect-payments-save-card)",
    "7-0": "**Partner Integration APIs**",
    "7-1": "\\- [Get Token API](ref:get_token_api)  \n- [Refresh Token API](ref:refresh_token_api)  \n- [User Token APIs](ref:user-token-apis)  \n- [Onboarding APIs](ref:onboarding-apis)  \n- [Bank Details API](ref:bank-details-api)  \n- [Manage KYC Documents](ref:manage-kyc-documents)",
    "8-0": "**Split Settlements APIs**",
    "8-1": "\\- [Split During Transaction using \\_payment](ref:split-during-transaction-using-_payment)  \n- [Split After Transaction API](ref:split_after_transaction_api)  \n- [Settlement APIs](ref:settlement-details-1)  \n- [Refund APIs](ref:refund-apis-split-settlements)",
    "9-0": "**Hexa Wallet APIs**",
    "9-1": "\\- [Fetch Balance API](https://docs.payu.in/reference/fetch-balance-api)  \n- [Create Wallet/Card API](https://docs.payu.in/reference/create-walletcard-api)  \n- [Retrieve Customer Record API](https://docs.payu.in/reference/retrieve-customer-record-api)  \n- [Update Profile API](https://docs.payu.in/reference/update-profile-api-wallet)  \n- [Block Card API](https://docs.payu.in/reference/block-card-api)  \n- [Unblock Card API](https://docs.payu.in/reference/unblock-card-api)  \n- [Check Status API](https://docs.payu.in/reference/check-status-api)  \n- [Statement Inquiry API](https://docs.payu.in/reference/statement-inquiry-api)  \n- [Unload API](https://docs.payu.in/reference/unload-api)  \n- [Load API](https://docs.payu.in/reference/l)  \n- [Fund Transfer API](https://docs.payu.in/reference/fund-transfer-api)  \n- [Create Beneficiary API](https://docs.payu.in/reference/create-beneficiary-api)  \n- [Fetch Beneficiary API](https://docs.payu.in/reference/fetch-beneficiary-api)  \n- [Update Beneficiary API](https://docs.payu.in/reference/update-beneficiary-api)  \n- [Delete Beneficiary API](https://docs.payu.in/reference/delete-beneficiary-api)  \n- [Change Card Status API](https://docs.payu.in/reference/change-card-status-api)  \n- [Link Card API](https://docs.payu.in/reference/link-card-api)  \n- [Verify Cardholder API](https://docs.payu.in/reference/verify-cardholder-api)  \n- [Card Inquiry API](https://docs.payu.in/reference/card-inquiry-api)  \n- [Reset PIN API](https://docs.payu.in/reference/reset-pin-api)",
    "10-0": "**Cross-Border Payments APIs**",
    "10-1": "\\- [Invoice Upload API](ref:invoice_upload_api)  \n- [UDF Update API](ref:udf_update_api)",
    "11-0": "**Pre-Authorize Payment APIs**",
    "11-1": "\\- [Pre-Authorize Payment](ref:pre_authorize_payment)  \n- [Capture a Pre-Authorized Payment](ref:capture-a-payment)",
    "12-0": "**Payouts APIS**",
    "12-1": "\\- [Generate Token using Merchant's Credentials API](ref:generate-token-using-merchants-credentials-api)  \n- [Generate Token using Private Client ID](ref:generate-token-using-private-client-id)  \n- [Get Account Details API](https://docs.payu.in/reference/get-account-details-api-payouts)  \n- [Initiate Transfer API](https://docs.payu.in/reference/initiate-transfer-api)  \n- [Check Transfer Status API](https://docs.payu.in/reference/check-transfer-status-api)  \n- [Cancel Transfer API](https://docs.payu.in/reference/cancel-transfer-api)  \n- [Disable Queued Payouts API](https://docs.payu.in/reference/disable-queued-payouts-api)  \n- [Penny Verify API](https://docs.payu.in/reference/penny_verify_api)  \n- [Get IFSC Details API](https://docs.payu.in/reference/get-ifsc-details-api)  \n- [Validate VPA Handle API](https://docs.payu.in/reference/validate_vpa_api)  \n- [Fetch Masked VPAs API](https://docs.payu.in/reference/fetch-masked-vpas-api)  \n- [Create Smart Send Link API](https://docs.payu.in/reference/create-smart-send-link-api)  \n- [Smart Send Status API](https://docs.payu.in/reference/smart-send-status-api)  \n- [Extend Expiry Date API](https://docs.payu.in/reference/extend-expiry-date-api)  \n- [Cancel Smartsend API](https://docs.payu.in/reference/cancel-smartsend-api)  \n- [Bulk File Upload API](https://docs.payu.in/reference/bulk-upload-api)  \n- [Bulk Process File API](https://docs.payu.in/reference/bulk-process-file-api)  \n- [View Beneficiary Details API](https://docs.payu.in/reference/view-beneficiary-details-api)  \n- [Create or Register Beneficiary API](https://docs.payu.in/reference/create-or-register-beneficiary-api)  \n- [Set Name Match Score Threshold API](https://docs.payu.in/reference/set-name-matchscore-threshold-api)  \n- [Get Name Match Score Threshold API](https://docs.payu.in/reference/get-name-matchscore-threshold-api)  \n- [Activate Payout Partner Merchant API](https://docs.payu.in/reference/payout-activate-partner-merchant)  \n- [Update Payouts Partner Merchant API](https://docs.payu.in/reference/update-payout-merchant)  \n- [Update Active Merchant Status API](https://docs.payu.in/reference/payout-update-active-merchant-status)  \n- [Whitelist Partner Merchant IP API](https://docs.payu.in/reference/payouts-whitelist-ip)  \n- [Get Whitelisted Partner Merchant IPs](https://docs.payu.in/reference/get-white-listed-merchant-ips) "
  },
  "cols": 2,
  "rows": 13,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Get support

Should you encounter any issues or have questions during your integration process, our dedicated support team is here to assist you. Visit <https://help.payu.in> and raise a ticket.