---
title: Model 3 - Simple REST API Integration
excerpt: >-
  You can choose this model integration for better flexibility and control. You
  can choose to keep only the PayU token with them and/or network/issuer tokens.
deprecated: false
hidden: false
metadata:
  title: Simple REST APIs for Vault Integration - Model 3
  description: >-
    Learn how to use Simple REST APIs to integrate PayU’s Save Cards feature
    into your website. This guide explains how to create, update, and delete
    cards using Model 3 of the Vault Integration.
  keywords:
    - Integrate saved cards with Merchant Hosted Checkout
    - Integrate saved cards with Custom Checkout
    - Secure card storage with Merchant Hosted Checkout
    - API integration for saved cards
    - Vault integration with Merchant Hosted Checkout
  robots: index
next:
  description: ''
---
To integrate vault with the Simple REST APIs, this section describes the following:

> 📘 Note:
>
> To use tokenization, you need to get the Token Requestor onboarding to be done. Contact your PayU Key Account Manager (KAM) to get the onboarding done.

* [First-time transaction](#first-time-transaction)
* [Repeat transaction with token](#repeat-transaction-with-token)

## First-time transaction

1. Get the customer’s consent on token creation on their checkout page.

> **Note**: This 2FA is done as per RBI guidelines and you need to be PCI-DSS compliant to store your customer’s card details.

2. Initiate the payment call to process the transaction with the card details.
3. After the payment response is received as successful, you will trigger the **save\_user\_card** API to get **save\_card\_token**. For more information, refer to [Save a Card API](ref:save_card_api)
4. The response received will provide the PayU reference ID and the network/issuer tokens, if the merchant is PCI-DSS compliant.

## Repeat transaction with token

1. If the transaction is to be processed through PayU:
   * Send the card token, network token, or issuer token and other details in the **\_payment** API. For more information, refer to [Collect Payments - Save Card](ref:collect-payments-save-card)
2. If the transaction is to be processed outside PayU:
   * Call the **get\_payment\_details** API with the PayU/Network token and get the TAVV/cryptogram. For more information, refer to [Get User Cards API](ref:get_user_cards_api)
   * After the token and cryptogram is available, you will be able to do transaction with the preferred PA/PG.

## Manage the tokens

1. To make any changes in the card token already created, you need to call the **edit\_user\_card** API. For more information, refer to [Edit a Tokenized Card API](ref:edit_saved_card_api).
2. To delete any token to comply with customer consent management, you need to call **delete\_user\_card**. For more information, refer to [Delete a Tokenized Card API](ref:delete_saved_card_api)