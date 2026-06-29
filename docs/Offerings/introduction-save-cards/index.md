---
title: Tokenization or Save Cards
deprecated: false
hidden: false
metadata:
  title: Save Cards Introduction
  description: >-
    Learn how to use PayU’s Save Cards feature to enable your customers to
    securely store their card details and make faster payments on your website.
    Find out how to integrate the Save Cards API, manage tokens, and customize
    the user experience.
  keywords:
    - Tokenizing Card with PayU India Introduction
    - Save Cards Integration with PayU Introduction
    - PayU India card saving Introduction
    - Saving card with PayU Introduction
    - Save card details PayU integration Introduction
    - Tokenization of cards Introduction
    - PayU India save card functionality Introduction
    - Save cards PayU integration Introduction
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: what-is-tokenization
      title: What is Tokenization?
    - type: basic
      slug: which-model-you-should-choose
      title: Which Model you Should Choose for Tokenization?
---
PayU Vault APIs allow users to store multiple credit card or debit card details on PayU Vault (Cloud) easily and safely. PayU Vault stores the card details and provides access to you (merchant) when your customer provides his/her user credentials accompanied with or without a card token.

Your users save invaluable time when they use their cards that are stored on PayU Vault instead of entering the card details when they make payments safely on your website. Customers can use tokenization on all the merchant websites where they support PayU Vault.

Users can update or delete their card details on the PayU vault when required. You may need to enable this on their website.

The workflow for users with PayU Vault are:

1. Customer visit the merchant’s website, adds items to the cart, or utilize the merchant’s services, and then enter the card details.
2. Customer provides consent to the merchant and the merchant [tokenize the card details](doc:zero-code-change-for-vault-integration-model-2#first-time-payment-workflow) on PayU Vault
3. Customer visits the same merchant and uses the saved card details to proceed with the transaction.
4. Customer provides his/her user credentials, the merchant [retrieves the card details](ref:get_user_cards_api) and the user enters the CVV or 3DBC number to complete payment.

> **Note**: While CVV is not mandatory from the network perspective, some banks may impose the necessity of the same for doing transactions with a saved card. Also, if the bank does not mandate the CVV but the merchant captures the same, CVV will be verified. It is recommended that for the banks where CVV is not required, merchants should not ask for the same

5. User can update or  delete the card details when required.

<Callout icon="📘" theme="info">
  ### Note:

  You need to ensure that you have filled the “[Self-Assessment Questionnaire A-EP and Attestation of Compliance](https://www.pcisecuritystandards.org/documents/PCI-DSS-v3_2-SAQ-A_EP-rev1_1.pdf)” form from PCI, which is mandatory for all entities seeking to store, process, and transmit cardholder data.
</Callout>

## APIs used in Save Cards integration

<Table>
  <thead>
    <tr>
      <th>
        API name
      </th>

      <th>
        Purpose
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ### Model 1
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
      </td>

      <td>
        Initiate first-time or repeat card payments on PayU Hosted Checkout with vault consent and `user_credentials` for saved cards.&#x20;
      </td>
    </tr>

    <tr>
      <td>
        ### Model 2
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Model 2 – Zero Code Change for Vault Integration](ref:model-2-zero-code-change-for-vault-integration)
      </td>

      <td>
        Tokenize a card during the first `_payment` request with customer consent; PayU manages token creation and storage.&#x20;
      </td>
    </tr>

    <tr>
      <td>
        [Get User Cards API](ref:get_user_cards_api)
      </td>

      <td>
        Retrieve a customer's tokenized cards for display at checkout.&#x20;
      </td>
    </tr>

    <tr>
      <td>
        [Process Transaction with a Saved Card](ref:process-transaction-with-a-saved-card)
      </td>

      <td>
        Initiate a repeat payment using a stored PayU vault token.
      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – Merchant Hosted Checkout](ref:_payment_merchant_hosted)
      </td>

      <td>
        Submit merchant-hosted card payment requests with saved-card or token parameters.&#x20;
      </td>
    </tr>

    <tr>
      <td>
        [Save a Card API](ref:save_card_api)
      </td>

      <td>
        Create a card token after a successful payment (Model 3).&#x20;
      </td>
    </tr>

    <tr>
      <td>
        ### Model 3
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Get User Cards API – Model 3](ref:get_user_cards_api_model3)
      </td>

      <td>
        Retrieve saved card tokens created via Model 3 REST APIs.&#x20;
      </td>
    </tr>

    <tr>
      <td>
        [Get Payment Details (Cryptogram) API](ref:get_payment_details_cryptogram)
      </td>

      <td>
        Fetch TAVV/cryptogram for a PayU or network token before initiating payment.
      </td>
    </tr>

    <tr>
      <td>
        [Edit a Tokenized Card API](ref:edit_saved_card_api)
      </td>

      <td>
        Update a stored card token when the customer changes card details.
      </td>
    </tr>

    <tr>
      <td>
        [Delete a Tokenized Card API](ref:delete_saved_card_api)
      </td>

      <td>
        Delete a stored card token for customer consent management.
      </td>
    </tr>

    <tr>
      <td>
        ### General
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Verify Payment API](ref:verify_payment_api)
      </td>

      <td>
        Server-side reconciliation of transaction status after payment.
      </td>
    </tr>
  </tbody>
</Table>

<br />