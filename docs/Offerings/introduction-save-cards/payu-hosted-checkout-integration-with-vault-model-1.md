---
title: Model 1 - PayU Hosted Checkout Integration
excerpt: ''
deprecated: false
hidden: false
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
This part of the documentation describes the workflow and how the cards are tokenized or saved in the vault with PayU Hosted Checkout Integration.

<Callout icon="📘" theme="info">
  **Note**: If you are an existing PayU vault user, you do not need to make any changes.
</Callout>

<Callout icon="👍" theme="okay">
  By default, when your customers make payment using card with PayU Hosted Checkout integration, PayU displays consent whether they want to save the card, so you need to do any implementation in this regard.

  Experience the end-to-end PayU Hosted Checkout flow and instantly generate the complete code for seamless, zero-coding integration into your website. 



  <HTMLBlock>{`
                  <style>
                  .tooltip-btn {
                      position: relative;
                      background-color: #4CAF50;
                      color: white;
                      padding: 10px 20px;
                      border: none;
                      border-radius: 5px;
                      cursor: pointer;
                      font-weight: bold; /* Added this line */
                  }
                  .tooltip-btn:hover::after {
                      content: attr(data-tooltip);
                      position: absolute;
                      bottom: 125%;
                      left: 50%;
                      transform: translateX(-50%);
                      background-color: #333;
                      color: white;
                      padding: 5px 10px;
                      border-radius: 4px;
                      white-space: nowrap;
                      font-size: 12px;
                      z-index: 1;
                  }
                  </style>

                  <button onclick="window.open('https://payu.in/integrationlab/payu-hosted', '_blank')" 
                          class="tooltip-btn" 
                          data-tooltip="Click here to see the PayU Hosted Checkout end-to-end integration and instantly generate the complete code needed for a zero-coding setup on your website.">
                      Experience the flow and get the code
                  </button>
  `}</HTMLBlock>
</Callout>

<br />

If you are not using the PayU vault, you need to ensure the following:

* You need to contact your PayU Key Account Manager to get the vault enabled for your merchant ID.
* After your customer logs on to your website, pass the customer’s user ID to identify and list the user’s tokenized cards on the PayU Checkout page. This is an extra parameter in the _payment API with which you already integrated. For more information, refer to [Repeat Transaction Workflow-Model 1](#repeat-transaction-workflow).

For more information on the complete list of parameters for PayU Hosted Checkout Integration, refer to the <Anchor label="Collect Payment API - PayU Hosted Checkout" target="_blank" href="https://docs.payu.in/v2/reference/v2_payment_seamless_integration/">Collect Payment API - PayU Hosted Checkout</Anchor> under API Reference.

## First-time transaction workflow

The first-time transaction workflow for Redirection Flow (PayU Hosted) integration with vault involves:

1. The customer lands on the PayU checkout page.
2. The customer enters the card details on the PayU Checkout page.
3. The customer gives explicit consent to save the cards.
4. PayU completes the transaction and saves the card in PayU Vault.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/11/transaction_is_confirmed-3-1024x868.png)

## Repeat transaction workflow

The repeat or subsequent transactions workflow for Redirection Flow (PayU Hosted Checkout) integration involves the following steps:

1. The customer lands on the PayU Checkout page.
2. The customer is listed with the saved cards on the PayU Checkout page along with the payment options.
3. The customer only enters the CVV in case of cards and proceeds with the transaction.
