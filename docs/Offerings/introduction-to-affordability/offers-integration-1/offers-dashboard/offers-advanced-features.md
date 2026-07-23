---
title: Offers Advanced Features
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Understanding User Limits or Velocity

### User Limits or Velocity

User limit helps in restricting the number of offers/budgets availed by a customer.

Here the velocity has been set to 2, which means during the whole offer period, your customer can avail the offer only twice.


<Image src="https://files.readme.io/67e894e5c8b00ecd3d918f680d4b4797f833695e1aed1160e5396a3622202e51-Screenshot_2025-06-06_at_10.05.59_AM.png" align="center" border={true} />


Along with restricting the number of offers, we have added a budget limit of Rs 800 per user. Now, the user can avail two offers, but to a maximum budget of Rs 800. Lets the user avail an offer of ₹600 in the first transaction, during the second transaction, the customer will only be able to avail a discount of ₹200. If the second transaction has an eligible discount of more than ₹200, the customer will not be able to get any discount here

### Refresh Limits

The customer limits configured can be reset at regular intervals of X days/weeks/months from the time of the user’s last transaction date.

## User Limits or Velocity check with Tokenization

This section describes how user limits/velocity works with tokenized cards.

### Merchant Using PayU’s Tokenization Service

PayU uses the card hash against which velocity will be run.

#### Plain Card Transaction

During a plain card transaction, a card hash will be generated against the card number and the velocity will be run against this card hash

> 📘 Note:
>
> Card hash is a unique identifier that is generated from the card number but cannot be used to trace back the card number

#### During Card Tokenization\*

PayU saves the card hash mapped with the token number during the tokenization of the card. For any future tokenized transactions, the card hash mapped against the token number will be used for the velocity checks

#### Saved Card/Token Card Transaction

For a transaction initiated with a tokenized card, the card hash mapped (at the time of token creation) against the tokenized card will be used to run the velocity. This will ensure that the velocity is maintained against both a plain card and a token card transaction

### Merchant Using Third-Party Tokenization

In this case, the velocity check will be run on the user token, that is using the **user\_token** parameter that’s passed in the payment request. This user token sent needs to be unique across the plain card and tokenized card for the velocity check to work properly. 

> 📘 Note:
>
> PAR solution is not fully implemented by all the networks, hence velocity check via PAR is not available currently.

## Automatic apply  best offer

You can enable the **Enforce Offer** flag by requesting your PayU Key Account Manager. If you enable the Enforce Offer flag, the best offer out of the all the offers passed will be applied for the customer. While using the [Fetch Offers API](ref:fetch-offers-api) and [Validate Offer API](ref:validate-offer-api),  the **autoApply** parameter must be set to true if the offer is automatically applied.
