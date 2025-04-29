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
> * General APIs
>   * Certain Refund flows
> * UPI flows with Server-to-Server
> * Refund Transaction
> * Recurring Payments or Subscriptions
>   * Flows involving UPI payment mode
> * Save Cards
>   * Model 2 - Zero Code Change flows
>   * Collect Payments
> * Split Settlements (only a few APIs supported)
> * TPV
> * Pre-authorize payment (with PayU Hosted Checkout integration)
> * Omnichannel
>
> For the test card numbers, test UPI handle, test wallet, etc. to be used in API Reference, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets).

## How to use API Reference

You can try using the Test Environment or Sandbox with most of the PayU India APIs in API Reference. Enter the values for the parameters/field in the form data and then click **Try It**.  The response is displayed based on the values entered in the form data. 

PayU recommends you to follow these so that you will integrate easily:

* Understand the product integration steps on the **Integration Guide** and later refer to API Reference.
* The API Reference pages for various APIs allows you to make mock API calls with most of the PayU APIs (using a static test key for General or Integration APIs).  Also, it provides support in 16 language bindings, so you can get the source code in apart from cURL.
* It is recommended to follow the **Integration Checklist** for checkout or SDK integrations to ensure that your integration is complete before making your integration live.

> 📘 Notes:
>
> * A static Test key is used with Test environment across the Collect Payment, General, Split Settlements and Pre-authorize APIs under [API Reference](/reference/). Hence, when you peruse the code on the API Reference, you need to replace the Test key with your Production key and Product environment URL.
> * All the parameters marked **required** must be filled to enable the **Generate Hash** button. 
> * The example listed (like a cookie) in each parameter field is  for reference purposed only, so it is suggested to type the values similar to the listed example.
> * Use only the the test card numbers, test UPI handle, test wallet, etc. in [API Reference,](/reference/) refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets).

<Image align="center" className="border" border={true} src="https://files.readme.io/e146999-api-reference-instructions.png" />

## List of PayU India APIs

The API Reference is categorized into following:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Collection
      </th>

      <th>
        Links
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Collect Payment APIs**
      </td>

      <td>
        \- [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)  

        * [Collect Payment API - Merchant Hosted Checkout](ref:_payment_merchant_hosted)  
        * [Collect Payment API - Server-to-Server](ref:_payment-server-to-server)
      </td>
    </tr>

    <tr>
      <td>
        **General APIs**
      </td>

      <td>
        \- [Check Transaction APIs](ref:check-transaction-apis)  

        * [Transaction Detail APIs](ref:transaction-detail-apis)  
        * [Refund APIs](ref:refund-apis)  
        * [Settlement Details](ref:settlement-details)  
        * [BIN APIs](ref:bin-apis)  
        * [EMI APIs](ref:emi-apis)  
        * [Health Check APIs](ref:health-check-apis)
      </td>
    </tr>

    <tr>
      <td>
        **Payment Link APIs**
      </td>

      <td>
        \- [Create Payment Link API](ref:create-payment-links)  

        * [Share Payment Link API](ref:share_payment_link_api)  
        * [Get Single Payment Link API](ref:get-single-payment-link)  
        * [Get All Payment Links API](ref:get-all-payment-links-api)  
        * [Create Invoice API](ref:create_invoice_api)  
        * [Expire Invoice API](ref:expire_invoice_api)
      </td>
    </tr>

    <tr>
      <td>
        **Recurring Payment APIs**
      </td>

      <td>
        \- [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted)  

        * [Payment Consent Transaction with Merchant Hosted Checkout](ref:payment-consent-transaction-merchant-hosted)  
        * [Pre-Debit Notification API](ref:pre_debit_notification_api)  
        * [Recurring Payment API](ref:recurring_payment_api)  
        * [Manage Recurring Payment for Cards](ref:manage-recurring-payment-for-cards)
      </td>
    </tr>

    <tr>
      <td>
        **Zion Subscription API**
      </td>

      <td>
        \- [Associating Plan in Defined Subscription API](ref:associating-plan-in-defined-subscription-interface)  

        * [Define Subscription API](ref:create-a-subscription)  
        * [Update Subscription API](ref:update-subscription-api)  
        * [Get List of Subscriptions API](ref:get-list-of-subscriptions-api)  
        * [Cancel Subscription API](ref:cancel-subscription-api)  
        * [Get Subscription Details API](ref:get-subscription-details-api)  
        * [Get Invoice API](ref:get-invoice-interfaces-api-zion)  
        * [Create Invoice API](ref:create-invoice-api-zion) 
      </td>
    </tr>

    <tr>
      <td>
        **Offers APIs**
      </td>

      <td>
        \- [Fetch Offers API](ref:fetch-offers-api)  

        * [Validate Offer API](ref:validate-offer-api)
      </td>
    </tr>

    <tr>
      <td>
        **Save Cards APIs**
      </td>

      <td>
        \- [Model 2-Zero Code Change](ref:model-2-zero-code-change-for-vault-integration)\
           \* [Get User Cards API](ref:get_user_cards_api)\
            \* [Process Transaction with a Saved Card](ref:process-transaction-with-a-saved-card)  

        * [Model 3 – Simple REST APIs](ref:model-3-simple-rest-apis)\
            \* [Save a Card API](ref:save_card_api)\
            \* [Edit a Saved Card API](ref:edit_saved_card_api)\
                     \* [Get User Cards API](ref:get_user_cards_api_model3)\
             \* [Delete a Saved Card API](ref:delete_saved_card_api)\
             \* [Get Payment Details (Cryptogram)](ref:get_payment_details_cryptogram)  
          * [Collect Payments - Save Card](ref:collect-payments-save-card)
      </td>
    </tr>

    <tr>
      <td>
        **Partner Integration APIs**
      </td>

      <td>
        \- [Get Token API](ref:get_token_api)  

        * [Refresh Token API](ref:refresh_token_api)  
        * [User Token APIs](ref:user-token-apis)  
        * [Onboarding APIs](ref:onboarding-apis)  
        * [Bank Details API](ref:bank-details-api)  
        * [Manage KYC Documents](ref:manage-kyc-documents)
      </td>
    </tr>

    <tr>
      <td>
        **Split Settlements APIs**
      </td>

      <td>
        \- [Split During Transaction using \_payment](ref:split-during-transaction-using-_payment)  

        * [Split After Transaction API](ref:split_after_transaction_api)  
        * [Settlement APIs](ref:settlement-details-1)  
        * [Refund APIs](ref:refund-apis-split-settlements)
      </td>
    </tr>

    <tr>
      <td>
        **Hexa Wallet APIs**
      </td>

      <td>
        \- [Fetch Balance API](https://docs.payu.in/reference/fetch-balance-api)  

        * [Create Wallet/Card API](https://docs.payu.in/reference/create-walletcard-api)  
        * [Retrieve Customer Record API](https://docs.payu.in/reference/retrieve-customer-record-api)  
        * [Update Profile API](https://docs.payu.in/reference/update-profile-api-wallet)  
        * [Block Card API](https://docs.payu.in/reference/block-card-api)  
        * [Unblock Card API](https://docs.payu.in/reference/unblock-card-api)  
        * [Check Status API](https://docs.payu.in/reference/check-status-api)  
        * [Statement Inquiry API](https://docs.payu.in/reference/statement-inquiry-api)  
        * [Unload API](https://docs.payu.in/reference/unload-api)  
        * [Load API](https://docs.payu.in/reference/l)  
        * [Fund Transfer API](https://docs.payu.in/reference/fund-transfer-api)  
        * [Create Beneficiary API](https://docs.payu.in/reference/create-beneficiary-api)  
        * [Fetch Beneficiary API](https://docs.payu.in/reference/fetch-beneficiary-api)  
        * [Update Beneficiary API](https://docs.payu.in/reference/update-beneficiary-api)  
        * [Delete Beneficiary API](https://docs.payu.in/reference/delete-beneficiary-api)  
        * [Change Card Status API](https://docs.payu.in/reference/change-card-status-api)  
        * [Link Card API](https://docs.payu.in/reference/link-card-api)  
        * [Verify Cardholder API](https://docs.payu.in/reference/verify-cardholder-api)  
        * [Card Inquiry API](https://docs.payu.in/reference/card-inquiry-api)  
        * [Reset PIN API](https://docs.payu.in/reference/reset-pin-api)
      </td>
    </tr>

    <tr>
      <td>
        **Cross-Border Payments APIs**
      </td>

      <td>
        \- [Invoice Upload API](ref:invoice_upload_api)  

        * [UDF Update API](ref:udf_update_api)
      </td>
    </tr>

    <tr>
      <td>
        **Pre-Authorize Payment APIs**
      </td>

      <td>
        \- [Pre-Authorize Payment](ref:pre_authorize_payment)  

        * [Capture a Pre-Authorized Payment](ref:capture-a-payment)
      </td>
    </tr>

    <tr>
      <td>
        **Payouts APIS**
      </td>

      <td>
        \- [Generate Token using Merchant's Credentials API](ref:generate-token-using-merchants-credentials-api)  

        * [Generate Token using Private Client ID](ref:generate-token-using-private-client-id)  
        * [Get Account Details API](https://docs.payu.in/reference/get-account-details-api-payouts)  
        * [Initiate Transfer API](https://docs.payu.in/reference/initiate-transfer-api)  
        * [Check Transfer Status API](https://docs.payu.in/reference/check-transfer-status-api)  
        * [Cancel Transfer API](https://docs.payu.in/reference/cancel-transfer-api)  
        * [Disable Queued Payouts API](https://docs.payu.in/reference/disable-queued-payouts-api)  
        * [Penny Verify API](https://docs.payu.in/reference/penny_verify_api)  
        * [Get IFSC Details API](https://docs.payu.in/reference/get-ifsc-details-api)  
        * [Validate VPA Handle API](https://docs.payu.in/reference/validate_vpa_api)  
        * [Fetch Masked VPAs API](https://docs.payu.in/reference/fetch-masked-vpas-api)  
        * [Create Smart Send Link API](https://docs.payu.in/reference/create-smart-send-link-api)  
        * [Smart Send Status API](https://docs.payu.in/reference/smart-send-status-api)  
        * [Extend Expiry Date API](https://docs.payu.in/reference/extend-expiry-date-api)  
        * [Cancel Smartsend API](https://docs.payu.in/reference/cancel-smartsend-api)  
        * [Bulk File Upload API](https://docs.payu.in/reference/bulk-upload-api)  
        * [Bulk Process File API](https://docs.payu.in/reference/bulk-process-file-api)  
        * [View Beneficiary Details API](https://docs.payu.in/reference/view-beneficiary-details-api)  
        * [Create or Register Beneficiary API](https://docs.payu.in/reference/create-or-register-beneficiary-api)  
        * [Set Name Match Score Threshold API](https://docs.payu.in/reference/set-name-matchscore-threshold-api)  
        * [Get Name Match Score Threshold API](https://docs.payu.in/reference/get-name-matchscore-threshold-api)  
        * [Activate Payout Partner Merchant API](https://docs.payu.in/reference/payout-activate-partner-merchant)  
        * [Update Payouts Partner Merchant API](https://docs.payu.in/reference/update-payout-merchant)  
        * [Update Active Merchant Status API](https://docs.payu.in/reference/payout-update-active-merchant-status)  
        * [Whitelist Partner Merchant IP API](https://docs.payu.in/reference/payouts-whitelist-ip)  
        * [Get Whitelisted Partner Merchant IPs](https://docs.payu.in/reference/get-white-listed-merchant-ips) 
      </td>
    </tr>
  </tbody>
</Table>

## Get support

Should you encounter any issues or have questions during your integration process, our dedicated support team is here to assist you. Visit [https://help.payu.in](https://help.payu.in) and raise a ticket.
