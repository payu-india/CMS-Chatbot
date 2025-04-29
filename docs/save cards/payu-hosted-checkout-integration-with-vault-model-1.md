---
title: Model 1 - PayU Hosted Checkout Integration
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: PayU Hosted Checkout Integration with Vault - Model 1
  description: >-
    Discover how to integrate PayU’s Hosted Checkout with the Vault model to
    offer your customers a seamless and secure payment experience with Save
    Cards. Learn how to create a payment request, redirect the customer to the
    Hosted Checkout page, and handle the payment response.
  keywords:
    - Save Cards Integration with PayU Hosted Checkout
    - ' Pre-built Checkout Integration with Save Cards'
    - Payment Vault Integration with PayU Hosted Checkout
    - Card Vaulting with PayU Hosted Checkout
  robots: index
next:
  description: ''
---
This part of the documentation describes the workflow and how the cards are saved in the vault with PayU Hosted Checkout Integration.

> 📘 Note:
> 
> If you are an existing PayU vault user, you do not need to make any changes.

If you are not using the PayU vault, you need to ensure the following:

- You need to contact your PayU Key Account Manager to get the vault enabled for your merchant ID.
- After your customer logs on to your website, pass the customer’s user ID to identify and list the user’s saved cards on the PayU Checkout page. This is an extra parameter in the \_payment API with which you already integrated. For more information, refer to [Repeat Transaction Workflow-Model 1](#repeat-transaction-workflow).

For more information on the complete list of parameters for PayU Hosted Checkout Integration, refer to the [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout) under API Reference.

## First-time transaction workflow

The first-time transaction workflow for Redirection Flow (PayU Hosted) integration with vault involves:

1. The customer lands on the PayU checkout page.
2. The customer enters the card details on the PayU Checkout page.

[block:image]{"images":[{"image":["https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/11/payu_inititate_transaction-3-1024x986.png",null,null],"align":"center","border":true}]}[/block]

3. The customer gives explicit consent to save the cards.

[block:image]{"images":[{"image":["https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/11/payu_hosted_model1_customer_gives_consent-3-1024x976.png",null,null],"align":"center","border":true}]}[/block]

4. PayU completes the transaction and saves the card in PayU Vault.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/11/tokenization_payuhosted_model1_customer_enters_otp.png",
        null,
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


PayU displays the payment confirmation similar to the following screenshot.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/11/transaction_is_confirmed-3-1024x868.png)

## Repeat transaction workflow

The repeat or subsequent transactions workflow for Redirection Flow (PayU Hosted Checkout) integration involves the following steps:

1. The customer lands on the PayU Checkout page.

[block:image]{"images":[{"image":["https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/11/payu_model1_repeat_workflow_landing_page-1.png",null,null],"align":"center","border":true}]}[/block]

2. The customer is listed with the saved cards on the PayU Checkout page along with the payment options.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/11/payu_hosted_model1_list_saved_cards_updated.png)

3. The customer only enters the CVV in case of cards and proceeds with the transaction.