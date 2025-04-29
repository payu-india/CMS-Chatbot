---
title: SKU-Based Offer using Merchant Hosted Checkout
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: SKU-Based Offer using Merchant Hosted Checkout - Offers Integration
  description: ''
  keywords:
    - Integrate an SKU-Based Offer with Merchant Hosted Checkout
    - Integrate Merchant Hosted Checkout with Cashback Offer
    - Integrate Cashback Offer with Seamless Integration
    - SKU-Based Offer with Seamless Integration
    - Integrating SKU-Based Offers with Merchant Hosted Checkout
    - Stock Keeping Units-based Offer Integration with Merchant Hosted Checkout
    - ' Stock Keeping Units-based Offer Integration with Seamless Integration'
  robots: index
next:
  description: ''
---
After you create a SKU-based offer on PayU Dashboard, you can start collecting payments for products with SKU-based offer.  For more information on creating a SKU-based offer, refer to [Create a SKU-Based Offer](doc:create-a-sku-based-offer).

> 📘 Note:
> 
> For payment journey of instant discount offers using Merchant Hosted Checkout, refer to [Instant Discount or Cashback using Merchant Hosted Checkout](doc:instant-discount-or-cashback-offers-integration-using-merchant-hosted-checkout).

### Steps to integrate

1. [Fetch offers](#step-1-fetch-offers)
2. [Validate offer](#step-2-validate-offer)
3. [Payment request](#step-3-payment-request)
4. [Check the response from PayU](#step-4-check-the-response-fro-payU)

## Step 1: Fetch offers

### Additional request parameter skusDetail for SKU

In addition to the request parameters listed in the [Fetch Offers API](ref:fetch-offers-api) section, the **skusDetail** parameter is posted with the following fields are posted in an array:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "0-0": "skuAmount  \n**optional**",
    "0-1": "_String_ The price of one/ single unit of SKU is specified in this field.",
    "1-0": "skuId  \n**mandatory**",
    "1-1": "_String_ The product identifier to select offer is specified in this field.",
    "2-0": " quantity   \n**optional**",
    "2-1": "_String_ The quantity for the product is specified in this field.\\*\\*\\*\\*",
    "3-0": "offerKeys  \n**optional**",
    "3-1": "\\_String The offer keys to filter at SKU-level is specified in this field."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    null,
    null
  ]
}
[/block]


### skusDetail parameter in sample request

The sample request posted will include the **skusDetail** parameter similar to the following:

```curl
"skusDetail": [
    {
      "skuAmount": 600,
      "quantity": 3,
      "skuId": "123",
      "offerKeys": null
    }
```

Sample Response

```
"skusDetail": [
    {
      "skuAmount": 600,
      "quantity": 3,
      "skuId": "123",
      "offerKeys": null
    }
```

## Step 2: Validate Offer

### Additional request parameters

In addition to the request parameters listed in  [Validate Offer API](ref:validate-offer-api), the **skusDetail** parameter with **skus** in an JSON array is posted, where each **skus** contain the following fields are posted in an array:

| **Field** | **Description**                                                                                                  |
| --------- | ---------------------------------------------------------------------------------------------------------------- |
| autoApply | The flag to specify to automatically apply the offer.                                                            |
| skuAmount | The price of one/ single unit of SKU is specified in this field.                                                 |
| offerKeys | The offer keys to filter at SKU-level is specified in this field.                                                |
| quantity  | The quantity for the product is specified in this field.                                                         |
| skuId     | The product identifier to select offer is specified in this field. For more information on creating a SKU offer. |

### skusDetail Object in request

```curl
  "skusDetail": {
    "skus": [
      {
      "autoApply": false,
        "skuAmount": 1000,
        "offerKeys": [
          "SummerSpecialOffer2021@q1Bh0jsogwqP"
        ],
        "quantity": 1,
        "skuId": "1"
      }
    ]
  }
```

### skusDetail Object in response

```
        "skusDetail": {
            "skusDiscountDetail": {
                "totalCashbackDiscount": null,
                "totalInstantDiscount": 100,
                "totalDiscountedAmount": 900
            },
            "skus": [
                {
                    "skuId": "1",
                    "quantity": 1,
                    "name": "One Plus",
                    "skuAmount": 1000,
                    "isValid": true,
                    "autoApply": false,
                    "discountDetail": {
                        "offerKey": "SummerSpecialOffer2021@q1Bh0jsogwqP",
                        "offerType": "INSTANT",
                        "discount": 100,
                        "discountedAmount": 900,
                        "discountType": "PERCENTAGE"
                    },
         "offerDetail":{
         "offerId":10005,
         "offerKey":"SummerSpecialOffer2021@q1Bh0jsogwqP",
         "offerType":"INSTANT",
         "title":"SummerSpecialOffer",
         "description":"SummerSpecialOffer discount",
         "validFrom":"2021-07-01 17:02:11",
         "validTo":"2022-08-05 15:53:16",
         "tnc":"abc",
         "tncLink":"abcd",
         "discountType":"ABSOLUTE",
         "offerPercentage":null,
         "maxDiscountPerTxn":100.00,
         "minTxnAmount":10.00,
         "maxTxnAmount":25000.00,
         "status":"ACTIVE",
         "isNce":false,
         "disallowTransactionInvalidOffer": false,
         "isSkuOffer": true,
         "isSubventedOffer": true
      }
```

## Step 3: Payment request

### Additional request parameters for SKU-Based offer

> 📘 Reference:
> 
> For the checkout flow and list of request parameters required for the Offer integration, refer to [Instant Discount or Cashback using Merchant Hosted Checkout](doc:instant-discount-or-cashback-offers-integration-using-merchant-hosted-checkout).

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "0-0": "cart\\_details  \n`mandatory for SKU`",
    "0-1": "_JSON Object_ The card details is specified in this parameter in a JSON format.  \n**Note**: If given null, no cart will be created for the transaction.",
    "1-0": "cart\\_details.amount  \n`mandatory`",
    "1-1": "_String_ The amount for the SKU-based offer.",
    "2-0": "cart\\_details.items  \n`mandatory`",
    "2-1": "_String_ The number of the items for the SKU-based offer.",
    "3-0": "cart\\_details.surcharges  \n`conditional`",
    "3-1": "_String_ Total txn amount is now increased, but the cart_details.amount is lesser, to handle the difference, the additional amount added by the merchant should be passed in surcharges field",
    "4-0": "cart\\_details.pre_discount  \n`conditional`",
    "4-1": "_String_ If there are any pre discount given by merchant on their checkout page. Total txn amount is now reduced, but the cart_details.amount is higher, to handle the difference, the discount given by the merchant should be passed in pre_discount field",
    "5-0": "cart\\_details.sku\\_details  \n`mandatory`",
    "5-1": "_JSON Object_ The SKU details is specified in this parameter in a JSON format.",
    "6-0": "cart\\_details.sku\\_details.sku\\_id  \n`mandatory`",
    "6-1": "_String_ This parameter contains the unique identifier for SKU.  \n**Note**: The Product ID in the Excel file as described in the [Create a SKU-Based Offer](doc:create-a-sku-based-offer) section and the **skuId** request parameter used in the Merchant Hosted Checkout Integration for SKU-based offer have the same function, Hence, after you create Product IDs on Dashboard, use them as values for the skuId parameter.",
    "7-0": "sku\\_details.sku\\_name  \n`mandatory`",
    "7-1": "_String _ This parameter contains the SKU name.",
    "8-0": "sku\\_details.quantity  \n`mandatory`",
    "8-1": "_String _ The parameter must contain the quantity of SKU added in cart.",
    "9-0": "sku\\_details.amount\\_per\\_sku  \n`mandatory`",
    "9-1": "_String _ The parameter must contain the per SKU amount.",
    "10-0": "sku\\_details.offer\\_key  \n`optional`",
    "10-1": "_String_ This parameter must contain the Offer Key(s) which can be used for this transaction. |",
    "11-0": "sku\\_details.offer\\_auto\\_apply  \n`optional`",
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


> **Notes**:  
>
> - The following order must be used for hashing:  
>   `key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|offer_key|offer_auto_apply|SALT`  
>   For more information on hash generation process, refer to [Hashing Request and Response](ref:generate-hash-merchant-hosted).
> - If any of the keys is null/not configured, "|" character must be concatenated.
> - The above hash logic is for \_payment API version 10 or later.

### cart\_details Object in sample request

```curl
"cart_details": {
    "amount": 55000,
    "items": 2,
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

## Step 4: Check the response from PayU

You need to look for the skusDetail object in the response. For the complete response, refer to [Merchant Hosted Checkout](doc:custom-checkout-merchant-hosted).

### Success scenario

The skusDetail JSON in the following sample response:

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

## Step 5: Verify the payment

Verify the payment using the **Verify Payment** API. For the sample response using the **Verify Payment **API from PayU involving offers, refer to <a href="addl-info-general-apis#sample-response" target="_blank">Additional Info for General APIsI</a>.