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

<Image align="center" border={true} src="https://files.readme.io/e146999-api-reference-instructions.png" className="border" />

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
        * [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
      </td>
    </tr>

    <tr>
      <td>
        **General APIs**
      </td>

      <td>
        * [Check Transaction APIs](ref:check-transaction-apis)
      </td>
    </tr>

    <tr>
      <td>
        **Payment Link APIs**
      </td>

      <td>
        * [Create Payment Link API](ref:create-payment-links)
      </td>
    </tr>

    <tr>
      <td>
        **Recurring Payment APIs**
      </td>

      <td>
        * [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted)
      </td>
    </tr>

    <tr>
      <td>
        **Zion Subscription API**
      </td>

      <td>
        * [Associating Plan in Defined Subscription API](ref:associating-plan-in-defined-subscription-interface)
      </td>
    </tr>

    <tr>
      <td>
        **Offers APIs**
      </td>

      <td>
        * [Fetch Offers API](ref:fetch-offers-api)
      </td>
    </tr>

    <tr>
      <td>
        **Save Cards APIs**
      </td>

      <td>
        * [Model 2-Zero Code Change](ref:model-2-zero-code-change-for-vault-integration)

            *[Get User Cards API](ref:get_user_cards_api)

            *[Process Transaction with a Saved Card](ref:process-transaction-with-a-saved-card)
      </td>
    </tr>

    <tr>
      <td>
        **Partner Integration APIs**
      </td>

      <td>
        * [Get Token API](ref:get_token_api)
      </td>
    </tr>

    <tr>
      <td>
        **Split Settlements APIs**
      </td>

      <td>
        * [Split During Transaction using _payment](ref:split-during-transaction-using-_payment)
      </td>
    </tr>

    <tr>
      <td>
        **Hexa Wallet APIs**
      </td>

      <td>
        * [Fetch Balance API](https://docs.payu.in/reference/fetch-balance-api)
      </td>
    </tr>

    <tr>
      <td>
        **Cross-Border Payments APIs**
      </td>

      <td>
        * [Invoice Upload API](ref:invoice_upload_api)
      </td>
    </tr>

    <tr>
      <td>
        **Pre-Authorize Payment APIs**
      </td>

      <td>
        * [Pre-Authorize Payment](ref:pre_authorize_payment)
      </td>
    </tr>

    <tr>
      <td>
        **Payouts APIs**
      </td>

      <td>
        * [Generate Token using Merchant's Credentials API](ref:generate-token-using-merchants-credentials-api)
      </td>
    </tr>

    <tr>
      <td>
        **Settlement APIs**
      </td>

      <td>
        * [Settlement Transaction Details API](https://docs.payu.in/reference/settlement_transaction_details_api)
        * [Settlement Detail Range API](https://docs.payu.in/reference/settlement-detail-range-api)
        * [Merchant Upcoming and Pending Settlement API](https://docs.payu.in/reference/merchant_upcoming_settlement_api)
        * [Release Settlement API](https://docs.payu.in/reference/release_settlement_api)
      </td>
    </tr>
  </tbody>
</Table>

## Get support

Should you encounter any issues or have questions during your integration process, our dedicated support team is here to assist you. Visit [https://help.payu.in](https://help.payu.in) and raise a ticket.
