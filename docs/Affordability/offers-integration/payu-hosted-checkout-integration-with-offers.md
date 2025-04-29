---
title: Integrate with PayU Hosted Checkout
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: Integrate with PayU Hosted Checkout for Offers
  description: ''
  keywords:
    - Integrate an Offer with PayU Hosted Checkout
    - Integrate an PayU Hosted Checkout with Offer
    - Integrate an Offer with Non-Seamless Integration
    - Offer with Non-Seamless Integration
  robots: index
next:
  description: ''
---
With the PayU Hosted Checkout integration, the entire payment experience is controlled by PayU. The following sections describe how to use the PayU Hosted Integration to collect payments with various types of offers:

- [Instant Discount or Cashback Offer](#instant-discount-or-cashback-offer)
- [SKU-Based Offer](#sku-based-offer)

## General customer journey

1. Customer clicks **Pay** on your mobile application or website.
2. Customer is redirected to the PayU Hosted Checkout page.

   The PayU Hosted Checkout page on Desktop is similar to the following screenshot. In case offer keys have been passed by the merchant, the same would be filtered and displayed to the customer.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Web.L1.Offers_Without-Global-vault-Copy-1-1024x858.png)

   The PayU Hosted Checkout page on Mobile is similar to the following screenshot:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Mweb.L1.Offers_Without-Global-vault-a-Copy.png)

3. Customer is shown the applicable offers on the checkout page for that transaction.
4. Customer will have an option to apply the offer. If the offer is applicable on a specific payment option, the customer will be redirected to the specific payment option.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Web.L2.Without-Global-Vault_Cards_Filled-Copy-2-1024x863.png)

```
The PayU Hosted Checkout page for specify payment option on Mobile is similar to the following screenshot:
```

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Mweb.L2.Without-Global-Vault_Cards_Filled-Copy.png)

5. Alternatively, the customer can choose the payment option. If only an offer is applicable for that payment option, the offer will be automatically applied.

![Picture 1522098393](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/picture-1522098393.png)

6. For Instant Discount, the amount is reduced after the offer is applied, whereas, in the case of cashback, the amount will not be reduced after the offer is applied.
7. Customer completes the 2FA payment on the adjusted amount.
8. Customer is redirected back to the merchant mobile application or website.

## Instant Discount or Cashback

With the PayU Hosted Checkout integration, the entire payment experience is controlled by PayU. This section describes how to use the PayU Hosted Integration to collect payments with offers.

### **Customer journey on PayU Hosted Checkout**

1. Customer clicks **Pay** on your mobile application or website.
2. Customer is redirected to the PayU Hosted Checkout page.

   The PayU Hosted Checkout page on Desktop is similar to the following screenshot. In case offer keys have been passed by the merchant, the same would be filtered and displayed to the customer.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Web.L1.Offers_Without-Global-vault-Copy-1-1024x858.png)

   The PayU Hosted Checkout page on Mobile is similar to the following screenshot:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Mweb.L1.Offers_Without-Global-vault-a-Copy.png)

3. Customer is shown the applicable offers on the checkout page for that transaction.
4. Customer will have the option to apply the offer. If the offer is applicable to a specific payment option, the customer will be redirected to the specific payment option.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Web.L2.Without-Global-Vault_Cards_Filled-Copy-2-1024x863.png)

   The PayU Hosted Checkout page for specific payment option on Mobile is similar to the following screenshot:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Mweb.L2.Without-Global-Vault_Cards_Filled-Copy.png)

5. Alternatively, the customer can choose the payment option. If only an offer is applicable for that payment option, the offer will be automatically applied.

![Picture 1522098393](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/picture-1522098393.png)

6. For Instant Discount, the amount is reduced after the offer is applied, whereas, in the case of cashback, the amount will not be reduced after the offer is applied.
7. Customer completes the 2FA payment on the adjusted amount.
8. Customer is redirected back to the merchant’s mobile application or website.

### Integration steps

To integrate offers using PayU Hosted Checkout integration:

> 📘 **Reference**:
> 
> For the PayU Hosted Checkout flow, refer to [PayU Hosted Checkout](doc:prebuilt-checkout-payu-hosted).

1. Make the payment request to PayU:

   You need to send an additional parameter (**user token)**, **api\_version** as 14, and hash as described in the following table. This user token would be used to identify the customer for applying velocity rules.

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
    "1-1": "The use for this param is to allow the offer engine to apply velocity rules at a user level.  \n  \n- **Card Based Offers (CC, DC, EMI)**: In case of card payment mode offers, if this parameter is passed the velocity rules would be applied on this token, if not passed the same would be applied on the card number.\n- **UPI, NB, Wallet**: It is mandatory for UPI, NB, and Wallet payment modes. If not passed the validation rules would not apply.",
    "1-2": "",
    "2-0": "hash  \n**mandatory**",
    "2-1": "It is used to avoid the possibility of transaction tampering.  \n**Note**: The following order must be used for hashing:  \n`key\\|txnid\\|amount\\|productinfo\\|firstname\\|email\\|udf1\\|udf2\\|udf3\\|udf4\\|udf5\\|udf6\\|udf7\\|udf8\\|udf9\\|udf10\\|offer_key\\|offer_auto_apply\\|SALT`  \nFor more information on hash generation process, refer to [Generate Hash](doc:generate-hash-payu-hosted) .",
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


2. Check the response from PayU.

   You need to understand the following parameters to handle the payment response as the net amount debit may be different from the amount sent by you in the request.

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
    "3-1": "This parameter is used to post any of the following offer\\_type:  \n  \n- instant\n- cashback",
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


3. Verify the payment.

   Similar to the payment response, the same parameters can be handled as part of the **verify\_payment** API. For more information, refer to [Verify Payment API](ref:verify_payment_api),

| **Parameter**       | **Description**                                                                                                                                                                                  | **Example** |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| transaction\_amount | This parameter contains the total transaction amount before discount.                                                                                                                            | 50000.00    |
| net\_amount\_debit  | This parameter contains the actual amount deducted from the customer’s payment instrument. In case of Instant discount this amount would be lesser than the amount passed by you in the request. | 47500.00    |
| discount            | This parameter contains the offer value provided to the user. This value will specify the offer amount for both Instant discount and Cashback offers.                                            | 2500.00     |

For the sample request and response from PayU, refer to [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout).

4. If you want to refund the payment to customer. refer to [Refund APIs](ref:refund-apis).

PayU would refund the exact amount passed by you in the Refund request. For more information, refer to [Refunds for Offers](doc:refunds-for-offers). 

> 📘 Note:
> 
> You can enable the **Enforce Offer** flag by requesting your PayU Key Account Manager. If you enable the **Enforce Offer** flag, all the offers passed are visible to the customer and the customer chooses an offer that they wish to apply.

## SKU-Based offer

After you create an SKU-based offer on PayU Dashboard, you can start collecting payments for products with an SKU-based offer.

This section describes the customer workflow with an SKU-based offer on the PayU Payment page when redirected from your website for payment and request parameters for the **\_payment** API to collect payments with an SKU-Based Offer.

> 📘 Note:
> 
> For payment journey of instant discount offers using Redirection Flow or PayU Hosted Checkout, refer to [Integrate with PayU Hosted Checkout](doc:payu-hosted-checkout-integration-with-offers).

### Customer journey

After your customer selects the items from your website (for example, mobile online shopping), the customer is redirected to the PayU page for payment and involves the following steps:

1. Select **Offers** at the top-right corner.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Mweb.L1.Offers_L1-523x1024.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "322px"
    }
  ]
}
[/block]


   All the offers for the products in the shopping cart (if any) are listed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Mweb.L1.Offers_AllOffers-1-568x1024.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "322px"
    }
  ]
}
[/block]


2. Select the **Product Offers** tab.

   The **Product Offers** tab is displayed on the _Offer & Discount_ page.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/skuoffers.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "322px"
    }
  ]
}
[/block]


3. Apply an offer using the **Use Offer** button for the offer you wish to apply.

   The _Offer Applied!_ pop-up page is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Mweb.L1.Offer_Applied.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "322px"
    }
  ]
}
[/block]


4. Click **Thanks.**

   The page to collect your credit card details is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Mweb.L1.Offers_L2_Expanded-350x1024.png)

5. Click **Proceed** to make payment and then enter the OTP sent by bank to your mobile to complete the purchase.
6. Close this page to return back to the merchant website.

### Integration steps

#### Step 1: Post request parameters

**Additional request parameters for SKU-Based Offer**

The following request parameters are posted along with request parameters posted for a PayU Hosted Checkout transaction. For the checkout flow and list of request parameters required for the Offer integration, refer to  [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout).

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "0-0": "cart\\_details  \n**mandatory for SKU**",
    "0-1": "_JSON Object_ The card details is specified in this parameter in a JSON format.  \n**Note**: If given null, no cart will be created for the transaction.",
    "1-0": "cart\\_details.amount  \n**mandatory**",
    "1-1": "_String_ The amount for the SKU-based offer.",
    "2-0": "cart\\_details.surcharges  \n**conditional**",
    "2-1": "_String_ Total txn amount is now increased, but the cart_details.amount is lesser, to handle the difference, the additonal amount added by the merchant should be passed in surcharges field",
    "3-0": "cart\\_details.pre_discount  \n**conditional**",
    "3-1": "_String_ If there are any pre discount given by merchant on their checkout page. Total txn amount is now reduced, but the cart_details.amount is higher, to handle the difference, the discount given by the merchant should be passed in pre_discount field",
    "4-0": "cart\\_details.items  \n**mandatory**",
    "4-1": "_String_ The number of the items for the SKU-based offer.",
    "5-0": "cart\\_details.sku\\_details  \n**mandatory**",
    "5-1": "_JSON Object_ The SKU details is specified in this parameter in a JSON format.",
    "6-0": "cart\\_details.sku\\_details.sku\\_id  \n**mandatory**",
    "6-1": "_String_ This parameter contains the unique identifier for SKU.  \n**Note**: The Product ID in the Excel file as described in the [Create a SKU-Based Offer](doc:create-a-sku-based-offer) section and the **skuId** request parameter used in the Merchant Hosted Checkout Integration for SKU-based offer have the same function, Hence, after you create Product IDs on Dashboard, use them as values for the skuId parameter.",
    "7-0": "sku\\_details.sku\\_name  \n**mandatory**",
    "7-1": "_String _ This parameter contains the SKU name.",
    "8-0": "sku\\_details.quantity  \n**mandatory**",
    "8-1": "_String _ The parameter must contain the quantity of SKU added in cart.",
    "9-0": "sku\\_details.amount\\_per\\_sku  \n**mandatory**",
    "9-1": "_String _ The parameter must contain the per SKU amount.",
    "10-0": "sku\\_details.offer\\_key  \n**mandatory**",
    "10-1": "_String_ This parameter must contain the Offer Key(s) which can be used for this transaction. |",
    "11-0": "sku\\_details.offer\\_auto\\_apply  \n**mandatory**",
    "11-1": "\\_String_This parameter contains the flag for when to enable auto application of best offer on this SKU. "
  },
  "cols": 2,
  "rows": 12,
  "align": [
    null,
    null
  ]
}
[/block]


#### cart_details object in sample request

```curl
"cart_details": {
    "amount": 55000,
    "items": 2,
    "surcharges": 10,
    "pre_discount": 5,
    "sku_details": [
      {
        "sku_id": "smartphone234",
        "sku_name": "Smartphone",
        "amount_per_sku": "45000",
        "quantity": 1,
        "offer_key": null,
        "offer_auto_apply": true
      },
      {
        "sku_id": "smartwatch132",
        "sku_name": "Smartwatch",
        "amount_per_sku": "10000",
        "quantity": 1,
        "offer_key": [
          "flat500@2022"
        ],
        "offer_auto_apply": false
      }
    ]
  }
```

#### Step 2: Check the PayU response

**Success scenario**

The **cart\_details** JSON Object in the response (sample):

```
{"cart_details": {
    "id": "18",
    "payu_id": "999000000000983",
    "total_items": "2",
    "total_cart_amount": "55000",
    "offer_applied": null,
    "offer_availed": null,
    "instant_discount": "1000",
    "cashback_discount": "500",
    "total_discount": "1500",
    "net_cart_amount": "54000",
    "created_at": null,
    "updated_at": null,
    "sku_details": [
      {
        "id": "35",
        "cart_id": "18",
        "payu_id": "999000000000983",
        "mid": "180012",
        "sku_id": "smartphone234",
        "sku_name": "Smartphone",
        "amount_per_sku": "45000.00",
        "quantity": "1",
        "amount_before_discount": "45000",
        "discount": "1000",
        "amount_after_discount": "44000",
        "offer_key": null,
        "offer_status": null,
        "offer_type": null,
        "created_at": null,
        "updated_at": null
      },
      {
        "id": "36",
        "cart_id": "18",
        "payu_id": "999000000000983",
        "mid": "180012",
        "sku_id": "smartwatch132",
        "sku_name": "Smartwatch",
        "amount_per_sku": "10000.00",
        "quantity": "1",
        "amount_before_discount": "10000.00",
        "discount": "500",
        "amount_after_discount": "10000.00",
        "offer_key": null,
        "offer_status": null,
        "offer_type": null,
        "created_at": null,
        "updated_at": null
      }
    ]
  }}
```

**Failure scenarios**

For a list of error messages for the failure scenarios, refer to [Error Codes for Offers Integration](doc:error-codes-for-offers-integration).

#### Step 3: Verify Payment

Verify the payment using the **Verify Payment **API. For more information, For API reference, refer to <a href="verify_payment_api" target="_blank">Verify Payment API</a>. For the sample response using the **Verify Payment **API from PayU involving offers, refer to <a href="addl-info-general-apis#sample-response" target="_blank">Additional Info for General APIsI</a>.