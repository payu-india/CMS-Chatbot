---
title: APIs used for Tokenization Integration
deprecated: false
hidden: false
icon: far fa-square-half-stroke-horizontal
metadata:
  title: APIs used for Tokenization Integration
  robots: index
---
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
