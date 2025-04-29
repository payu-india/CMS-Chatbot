---
title: Enable Pluxee Card on Checkout
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Enable Sodexo Payments for PayU Hosted Checkout
  description: >-
    Integrate Sodexo with PayU Hosted Checkout effortlessly. This guide provides
    detailed steps to seamlessly incorporate Sodexo payments into your checkout
    process. Elevate your payment options and offer convenient Sodexo payment
    solutions to your customers using PayU India's API.
  robots: index
next:
  description: ''
---
Pay Hosted Checkout (non-seamless) integration provides you to collect payments from customers using Pluxee (earlier Sodexo BRS) meal card on specific merchant categories such as restaurants, groceries etc.

> 📘 Note
> 
> PayU supports only PayU Hosted Checkout (non-seamless) and Merchant Hosted Checkout integration (seamless) using this API. Server-to-Server (S2S) integration is not be supported for Sodexo.

This section describes the parameters required to collect payments using the Pluxee card with PayU Hosted Checkout integration (using the  **\_payment** API) with parameters to enforce only the Pluxee card in the **mealcard** category or hide it.

***

### **Steps to Integrate:**

1. [Post the transaction request to PayU](#step-1-post-the-transaction-request-to-payu)
2. [Customer submits payment details on PayU Page](#step-2-customer-submits-payment-details-on-payu-page)
3. [Check the response from PayU](#step-3-check-the-response-from-payu)

## Pluxee using PayU Hosted Integration workflow

The following describe the characteristics and workflow involved using PayU Hosted Checkout Integration with Pluxee:

- The existing **\_payment** API used to initiate payments for online transactions will be used to initiate payments for Pluxee payment option.
- In case the merchant wants to enforce Pluxee payment option on our check out page, **enforce\_paymethod** value should be passed as **SODEXO**.
- In case merchant wants to drop the Pluxee payment option under the **mealcard** category on the PayU checkout page, then **drop\_category** value should be passed as **MC|SODEXO**. In case the **entire mealcard category** need to be dropped, then value should be passed as **MC**. Currently, PayU only supports the Sodexo payment option in the **mealcard** category.

For more information enforcing or hiding Pluxee payment option, refer to [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)

### Workflow on PayU Payment Page

1. Merchant initiates payment & redirects the customer to PayU’s check out page to choose a payment option of their choice.

![Picture 5](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/03/picture-5.png)

2. Customer selects the Pluxee payment option available on the PayU’s check out page & either enters new card details or selects already saved Pluxee card.

![Picture 6](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/03/picture-6.png)

3. In case customer want’s to use an already saved Pluxee card, PayU will only allow that, provided the balance available in the card is greater than or equal to transaction amount.

![Picture 7](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/03/picture-7.png)

4. The customer is then re-directed to Pluxee ACS page, where the customer can enter the PIN and complete the payment.

![Picture 8](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/03/picture-8.png)

5. Once PayU receives a successful confirmation from Sodexo, we will provide a confirmation to merchant via webhook or merchant can use our status check API to fetch the transaction status.

![Picture 10](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/03/picture-10.png)

## Step 1: Post the transaction request to PayU

The parameters for the Sodexo card remain the same for as mentioned in the [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout).

### Enforcing Sodexo Card payment

If you wish to enforce the Sodexo card payment and hide other cards, you can use the following parameters and other PayU Hosted Checkout parameters according to your requirements.

| **Parameter**      | **Description**                                                                                                                                               | **Example** |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| enforce\_paymethod | This parameter allows you to customize the payment options for each individual transaction. To enforce Sodexo card as the payment method, specify **SODEXO**. | SODEXO      |

### Dropping the Sodexo Card payment

If you wish to hide the Sodexo card payment in the **mealcard** category, you can use the following parameters and other PayU Hosted Checkout parameters according to your requirements.

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "drop\\_category  \n**optional**",
    "0-1": "This parameter is used to customize the payment options for each individual transaction. To drop the Sodexo card payment with PayU Hosted Checkout integration, specify **mealcard|SODEXO**.",
    "0-2": "mealcard|SODEXO"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


|Currently, PayU India only supports the Sodexo payment option under the **mealcard** category.

### Sample request

For a sample request, refer to  [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout). under API Reference..

***

## Step 2: Customer submits payment details on PayU page

The customer selects the Sodexo payment option on PayU’s page.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/10/Screenshot-2022-10-28-at-12.14.55-PM-837x1024.png)

After the customer selects the **Sodexo** payment mode, PayU gets the Sodexo card details from the customer.

The customer performs the authorization or authentication process on the bank’s login page, and the bank communicates the success or failure response back to PayU.

## Step 3: Check the response from PayU

PayU marks the transaction status based on the response received from the bank. PayU communicates the success URL to you if the payment is successful. Verify the authenticity of the hash value before accepting or rejecting the invoice order. For the list of parameters in the response body for the PayU Hosted integration, refer to\~~ Collect Payments with PayU Hosted Checkout\~~ under API Reference.

***