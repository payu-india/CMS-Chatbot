---
title: Offers Dashboard
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: >-
    The Offers Dashboard page is designed for PayU India merchants to manage and
    create different types of offers for their customers. This dashboard
    provides a convenient interface for merchants to easily create offers such
    as Instant Discounts, Cashback, No Cost EMI, and Product/SKU based Offers.
  keywords:
    - PayU India Offers Dashboard
    - ' PayU Checkout Offer Integration'
    - ' PayU Offers Payment Modes'
    - Dashboard to Create Offers
    - Offers for  PayU India Checkout integrations
  robots: index
next:
  description: ''
---
The following offers can be created using PayU Dashboard:

* [Instant Discount ](doc:create-an-offer)
* [Cashback](doc:create-an-offer)
* [No Cost EMI](doc:create-a-no-cost-emi-offer)
* [Pre-Discounted Offer](doc:create-a-pre-discounted-offer)
* [Product/SKU based Offer](doc:create-a-sku-based-offer)

> 👍 Before you begin:
>
> Register for a account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

## Enable Offers on Dashboard

By default, the Offers feature is not enabled on PayU Dashboard.

> 📘 Enable Offers & Promotion:
>
> If the **Offers & Promotion** menu is not appearing on the main menu of the PayU Dashboard similar to the following screenshot, contact your PayU Key Account Manager (KAM) or click Help at the top-right corner to raise a ticket with PayU Support.

To enable Offers:

1. Select **Offers & Promotions**.
2. Click **Activate Now**.

<Image align="center" className="border" border={true} src="https://files.readme.io/fb28ab08a65467c0f0091833def79fc2c2e9c2609f645b0544e76d32c8c29d27-Screenshot_2025-06-03_at_9.56.40_AM.png" />

The following pop-up page is displayed.

<Image align="center" src="https://files.readme.io/9f4dddb-Screenshot_2023-09-28_at_2.12.29_PM.png" />

3. Select **Pro Plan** or contact your PayU Key Account Manager (KAM) for the **Enterprise** plan.

# Navigate to Offers Dashboard

After logging in to PayU Dashboard, select Offers & Promotions from the main menu (on the left side), the Offers Overview page similar to the following is displayed to begin setting up an offer.

<Image align="center" className="border" border={true} src="https://files.readme.io/fa61f2023a607a59049b2036ba980d7ea4c3b3cdc6a58505081d13f6c64de053-Screenshot_2025-06-03_at_10.14.21_AM.png" />

## Understanding User Limits and Velocity

User limit helps in restricting the number of offers/budgets availed by a customer.

Here the velocity has been set to 2, which means during the whole offer period, your customer can avail the offer only twice.

<Image align="center" className="border" border={true} src="https://files.readme.io/67e894e5c8b00ecd3d918f680d4b4797f833695e1aed1160e5396a3622202e51-Screenshot_2025-06-06_at_10.05.59_AM.png" />

Along with restricting the number of offers, we have added a budget limit of Rs 800 per user. Now, the user can avail two offers, but to a maximum budget of Rs 800. Lets the user avail an offer of ₹600 in the first transaction, during the second transaction, the customer will only be able to avail a discount of ₹200. If the second transaction has an eligible discount of more than ₹200, the customer will not be able to get any discount here

### Refresh Limits

The customer limits configured can be reset at regular intervals of X days/weeks/months from the time of the user’s last transaction date.

### User Limits or Velocity check with Tokenization

This section describes how user limits/velocity works with tokenized cards.

#### Merchant Using PayU’s Tokenization Service

PayU uses the card hash against which velocity will be run.

#### Plain Card Transaction

During a plain card transaction, a card hash will be generated against the card number and the velocity will be run against this card hash

> 📘 Note:
>
> Card hash is a unique identifier that is generated from the card number but cannot be used to trace back the card number

#### During Card Tokenization

PayU saves the card hash mapped with the token number during the tokenization of the card. For any future tokenized transactions, the card hash mapped against the token number will be used for the velocity checks

#### Saved Card/Token Card Transaction

For a transaction initiated with a tokenized card, the card hash mapped (at the time of token creation) against the tokenized card will be used to run the velocity. This will ensure that the velocity is maintained against both a plain card as well as a token card transaction

### Merchant Using Third-Party Tokenization

In this case, the velocity check will be run on the user token, that is using the **user\_token** parameter that’s passed in the payment request. This user token sent needs to be unique across the plain card and tokenized card for the velocity check to work properly. 

> 📘 Note:
>
> PAR solution is not fully implemented by all the networks, hence velocity check via PAR is not available currently.