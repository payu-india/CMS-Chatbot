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

- [Instant Discount ](doc:create-an-offer)
- [Cashback](doc:create-an-offer)
- [No Cost EMI](doc:create-a-no-cost-emi-offer)
- [Pre-Discounted Offer](doc:create-a-pre-discounted-offer)
- [Product/SKU based Offer](doc:create-a-sku-based-offer)

> 👍 Before you begin:
> 
> Register for a account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

The following video explains how to create an offer:

[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FWvHrgeVMpf4%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DWvHrgeVMpf4&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FWvHrgeVMpf4%2Fhqdefault.jpg&key=7788cb384c9f4d5dbbdbeffd9fe4b92f&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen; encrypted-media; picture-in-picture;\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=WvHrgeVMpf4",
  "title": "PayU Offers Engine: How to create offers using PayU Offers Engine?",
  "favicon": "https://www.google.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/WvHrgeVMpf4/hqdefault.jpg",
  "provider": "youtube.com",
  "href": "https://www.youtube.com/watch?v=WvHrgeVMpf4",
  "typeOfEmbed": "youtube"
}
[/block]


## Enable Offers on Dashboard

By default, the Offers feature is not enabled on PayU Dashboard. 

> 📘 Enable Offers & Promotion:
> 
> If the **Offers & Promotion** menu is not appearing on the main menu of the PayU Dashboard similar to the following screenshot, contact your PayU Key Account Manager (KAM) or click Help at the top-right corner to raise a ticket with PayU Support.

To enable Offers:

1. Select** Offers & Promotions**.
2. Click **Activate Now**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7fac27f-Screenshot_2023-09-28_at_1.35.36_PM.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


   The following pop-up page is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9f4dddb-Screenshot_2023-09-28_at_2.12.29_PM.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


3. Select **Pro Plan ** or contact your PayU Key Account Manager (KAM) for the **Enterprise** plan.

# Navigate to Offers Dashboard

After logging in to PayU Dashboard, select Offers & Promotions from the main menu (on the left side), the Offers Overview page similar to the following is displayed to begin setting up an offer.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0caf651-Screenshot_2023-09-28_at_2.19.42_PM.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


## Understanding User Limits and Velocity

User limit helps in restricting the number of offers/budgets availed by a customer.

Here the velocity has been set to 2, which means during the whole offer period, your customer can avail the offer only twice.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/04/userlimits1-1024x401.png",
        null,
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/04/userlimits2-1024x458.png",
        null,
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


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