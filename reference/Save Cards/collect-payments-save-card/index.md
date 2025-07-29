---
title: Collect Payments - Save Card
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: collect-payments-using-a-saved-card
      title: Collect Payments using a Saved Card
---
When your customer has an account on your shopping website, they may store their card details to use when they revisit your website (repeat payment).

PayU offers you API to save the card details and retrieves them using the Store Card APIs. For example, the stored cards are displayed when your customer performs checkout and lands on the payment page.

This section explains the procedure for getting a customer’s card details and using a saved card to initiate payment.

***

## Step 1: Get the Saved Card Details

1. Get the customer’s card details your merchant key and customer’s registered mail ID to PayU using the **Get User Details** API. For more information, refer to [Get User Cards API](ref:v2_get_user_cards_api).
2. Check the response for the last four digits of the card number:

```plaintext
{
      "status": 1,
      "msg": "Cards fetched Succesfully",
      "user_cards": {
            "57cb996f2eaeee525765a": {
                  "expiry_month": "03",
                  "card_mode": "CC",
                  "is_expired": 0,
                  "card_cvv": 0,
                  "card_no": "XXXXXXXXXXXX2346",
                  "card_token": "57cb996f2eaeee525765a",
                  "card_name": "test card",
                  "card_type": "CC",
                  "expiry_year": "2026",
                  "name_on_card": "Test",
                  "card_brand": "MASTERCARD",
                  "card_bin": "512345",
                  "isDomestic": "Y"
            }
      }
}
```

2. List the saved cards if the customer is having more than one card and ask them make a selection.
3. Collect the CVV of the saved card that customer has selected for payment.

***

## Step 2: Post Payment to PayU

Make the transaction request with the payment details along with the card nickname to PayU based on the following scenarios of tokenization:

* [Using Complete Card Details](ref:/v2/reference/complete-card-details-payment)
* [Using Network Tokens](ref:/v2/reference/using-network-tokens)

> 📘 Notes
>
> * In addition to the request parameters used for Merchant Hosted Checkout (Seamless integration) payment request, you need to ensure the additional parameters as specified in each scenario specified in this step. For more information on the complete list of parameters, refer to [Seamless Integration](https://docs/payu.in/v2/docs/v2-seamless-integration).
> * The additional response parameters (if any) are specified for each scenario. For the sample response for a card payment using Merchant Hosted Checkout response, refer to [Cards Integration](https://docs.payu.in/v2/docs/v2-cards-merchant-hosted-integration/).

***

## Step 3: Check the PayU Response

1. Check the response for the status of the transaction. The response for each scenario is specified in [Step 2](#step-2-post-payment-to-payu).

***

## Step 4: Verify the Payment

Verify the transaction details using the Verification APIs. Post the transaction ID using the **verify\_payment** API to verify the payment. For more information, refer to <Anchor label="Verify Payment API" target="_blank" href="https://docs.payu.in/v2/reference/v2_verify_payment_api/">Verify Payment API</Anchor>/

> 📘 Note:
>
> The transaction ID that you posted in Step 3 with PayU must be used here.