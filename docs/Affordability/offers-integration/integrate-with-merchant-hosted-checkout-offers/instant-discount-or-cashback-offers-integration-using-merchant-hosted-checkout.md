---
title: Instant Discount or Cashback using Merchant Hosted Checkout
excerpt: >-
  With the Merchant Hosted Checkout integration, the entire payment experience
  can be controlled by merchants and PayU provides APIs to power this checkout
  experience. This section describes how PayU will help you to discover Offer
  (not only on Checkout page but anywhere on the merchant app/website), validate
  Offer & apply Offer (along with payment).  ##
deprecated: false
hidden: true
metadata:
  title: >-
    Instant Discount or Cashback using Merchant Hosted Checkout - Offers
    Integration
  description: ''
  keywords:
    - Integrate an Instant Discount Offer with Merchant Hosted Checkout
    - Integrate Merchant Hosted Checkout with Cashback Offer
    - Integrate Cashback Offer with Seamless Integration
    - Instant Discount Offer with Seamless Integration
    - Integrating Instant Discount Offers with Merchant Hosted Checkout
    - Integrate an Cashback Offer with Merchant Hosted Checkout
    - Integrate Merchant Hosted Checkout Cashback Offer
    - Integrate a Cashback Offer with Seamless Integration
    - Cashback Offer with Seamless Integration
    - Integrating Cashback Offers with Merchant Hosted Checkout
    - Cash Back Offer Integration
  robots: index
next:
  description: ''
---
## Customer journey on Merchant Hosted Checkout

The following video walks through the customer journey:

The steps involves in the customer journey are:

1. User logs in to the merchant’s app/website.
2. User chooses the product(s)/service(s) he/she wishes to purchase.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/merchant_hosted_offers_checkout1-1024x576.png)

3. User reaches the checkout page. The merchant can use the Fetch offers API to display all the live applicable offers for this transaction. As part of this API the merchant would get all the necessary information to display to the user regarding the offer include Offer Title, description, terms and conditions, applicable payment modes & the offer value.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/merchant_hosted_offers_checkout3-1024x576.png)

4. User would make his/her decision and pay through a specific payment option. After the customer has entered all the required details, the merchant can use the Validate Offer API to check whether the offer would be applied to the transaction or not.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/merchant_hosted_offers_checkout4-1024x576.png)

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/merchant_hosted_offers_checkout7-1.png)

5. The merchant would initiate the payment along with the offer using the **\_payment** API
6. In case of Instant discount, the amount would be reduced on application of offer, in case of cashback the amount would not be charged.
7. User would complete the 2FA (2 Form Authentication) payment on the adjusted amount.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/merchant_hosted_offers_checkout8.png)

8. User would be redirected back to the merchant app/website.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/merchant_hosted_offers_checkout9.png)

The merchant can use the Fetch offers API to display the offers on **Product Display Page** & **Cart** screens or in case merchant wishes to have a separate **Offers section** on their website/app

## Integration steps

To integrate offers using Merchant Hosted Checkout integration:

> 📘 Reference:
> 
> For the Merchant Hosted Checkout workflow, refer [Merchant Hosted Checkout](doc:custom-checkout-merchant-hosted)

1. On the checkout page (or earlier on PDP, Cart, Offers) use the **Fetch Offers** API to get the offers and display all the offers. For more information, refer to [Fetch Offers API](ref:fetch-offers-api).
2. Use the **Validate Offer** API to validate if the offer will be applied on this transaction or not. For more information, refer to [Validate Offer API](ref:validate-offer-api).
3. Make the payment request using the **\_payment** API using the following additional parameters for Offers. For more information on the complete list of parameters to be posted, refer to [Collect Payment API - Merchant Hosted Checkout](ref:_payment-merchant-hosted)

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "api\\_version  \n**mandatory**",
    "0-1": "The API version of the \\_payment API must be specified as **14**.",
    "0-2": "14",
    "1-0": "user\\_token  \n**mandatory for UPI, NB, Wallet**",
    "1-1": "The use for this param is to allow the offer engine to apply velocity rules at a user level.  \n  \n- **Card Based Offers (CC, DC, EMI)**: In case of card payment mode offers, if this parameter is passed the velocity rules would be applied on this token, if not passed the same would be applied on the card number.\n- **UPI, NB, Wallet**: It is mandatory for UPI, NB, and Wallet payment modes. If not passed the validation rules would not apply.",
    "1-2": "",
    "2-0": "hash  \n**mandatory**",
    "2-1": "It is used to avoid the possibility of transaction tampering.  \n**Note**: The following order must be used for hashing:  \n`key\\|txnid\\|amount\\|productinfo\\|firstname\\|email\\|udf1\\|udf2\\|udf3\\|udf4\\|udf5\\|udf6\\|udf7\\|udf8\\|udf9\\|udf10\\|offer_key\\|offer_auto_apply\\|SALT`  \nFor more information on hash generation process, refer to [Generate Hash](doc:generate-hash-merchant-hosted) .",
    "2-2": ""
  },
  "cols": 3,
  "rows": 3,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


> **Notes**:  
>
> - The following order must be used for hashing:  
>   `key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|offer_key|offer_auto_apply|SALT`  
>   For more information on hash generation process, refer to [Hashing Request and Response](ref:generate-hash-merchant-hosted).
> - If any of the keys is null/not configured, "|" character must be concatenated.
> - The above hash logic is for \_payment API version 10 or later

4. Check the following response parameters (for Offers) from PayU to handle the payment response, as the net amount debit may be different from the amount sent by you in the request.

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "discount",
    "0-1": "This will specify the offer value provided to the user.",
    "0-2": "10.00",
    "1-0": "net\\_amount\\_debit",
    "1-1": "This will specify the actual amount deducted from the customer’s payment instrument. In case of Instant discount this amount would be lesser than the amount passed by you in the request.",
    "1-2": "100.00",
    "2-0": "offer",
    "2-1": "This parameter is used to post the offer key.",
    "2-2": "newoffer1@5686",
    "3-0": "offer\\_type",
    "3-1": "This parameter is used to post any of the following offer\\_type:  \n - instant  \n  \n- cashback",
    "3-2": "instant"
  },
  "cols": 3,
  "rows": 4,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


For a sample response, refer to the [Additional Info for Payment APIs](ref:addl_info-payment-apis).

5. Verify the payment.

Similar to the payment response, same params can be handled as part of the **Verify Payment** API. For more information, For API reference, refer to <a href="verify_payment_api" target="_blank">Verify Payment API</a>. For the sample response using the **Verify Payment **API from PayU involving offers, refer to <a href="addl-info-general-apis#sample-response" target="_blank">Additional Info for General APIsI</a>.

| **Parameter**       | **Description**                                                                                                                                                                                  | **Example** |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| transaction\_amount | This parameter contains the total transaction amount before discount.                                                                                                                            | 50000.00    |
| net\_amount\_debit  | This parameter contains the actual amount deducted from the customer’s payment instrument. In case of Instant discount this amount would be lesser than the amount passed by you in the request. | 47500.00    |
| discount            | This parameter contains the offer value provided to the user. This value will specify the offer amount for both Instant discount and Cashback offers.                                            | 2500.00     |

PayU would refund the exact amount passed by you in the Refund request. For more information, refer to [Refunds for Offers](doc:refunds-for-offers)

> 📘 Note:
> 
> You can enable the **Enforce Offer** flag by requesting your PayU Key Account Manager. If you enable the **Enforce Offer** flag, the best offer out of the all the offers passed will be applied for the customer.