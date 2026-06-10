---
title: Multiple Offers - Merchant Hosted
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
With the Merchant Hosted Checkout integration, the entire payment experience is controlled by PayU. This section describes how to use the Merchant Hosted Integration to collect payments with offers grouping. 

## **Integration Steps**

To integrate offers using Merchant Hosted Checkout integration:

**Reference**: For the Merchant Hosted Checkout flow, refer [Merchant Hosted Checkout Integration.](https://devguide.payu.in/merchant-integration/web-checkout/merchant-hosted-checkout/)

1. On the checkout page (or earlier on PDP, Cart, Offers) use the **Fetch Offers** API to get the offers and display all the offers. For more information, refer to [Fetch Offers API](https://devguide.payu.in/offers-integration/offers-api/fetch-offer-api/).
2. Use the **Validate Offer** API to validate if the offer will be applied on this transaction or not. For more information, refer to [Validate Offer API](https://devguide.payu.in/offers-integration/offers-api/validate-offer-api/).
3. Make the payment request using the **\_payment** API using the following additional parameters for Offers. You need to send an additional parameter (**user token)**, **api\_version** as 14, and hash as described in the following table. This user token would be used to identify the customer for applying velocity rules.


4. Check the response from PayU.

For a sample response from PayU, refer to [Web Checkout Integration > PayU Hosted Checkout Integration](https://devguide.payu.in/merchant-integration/payu-hosted-checkout/payu-hosted-checkout-integration/#Step3).

- For Merchant Hosted or Server-to-Server integration, you are expected to pass both the offer keys (NCE/LCE, ID/CB) in the payment request as part of the **offer**parameter
- For PayU Hosted checkout, you don’t need to do any additional steps in integration for multiple offers, PayU will automatically apply the “best of base offer + best of ID/CB“. Merchants can however pass specific offer keys in the request to ensure only those offers are considered for auto-application of offers
- Transaction-Level offers

`transaction_offer` is added as a new object which will have all the details of both offers.

```plaintext
[transaction_offer] => {
  "offer_data": [
    {
      "status": "SUCCESS",
      "discount": 1000,
      "isNoCost": false,
      "offer_key": "RmAKSXf5GDuR",
      "offer_type": "INSTANT",
      "offer_title": "EMIINSTATN",
      "flag_to_fail": false,
      "failure_reason": "Offer Applied Successfully",
      "offer_description": "NO COST "
    },
    {
      "status": "SUCCESS",
      "discount": 258.76,
      "isNoCost": true,
      "offer_key": "nceinstantbase@uiWD77ShtABG",
      "offer_type": "INSTANT",
      "offer_title": "nce instant base",
      "flag_to_fail": true,
      "failure_reason": "Offer Applied Successfully",
      "offer_description": "nce instant base"
    }
  ],
  "discount_data": {
    "total_discount": 1258.76,
    "instant_discount": 1258.76,
    "cashback_discount": 0,
    "total_nce_discount": 258.76,
    "instant_nce_discount": 258.76,
    "cashback_nce_discount": 0
  }
}
```

The description of parameters for a Transaction-Level offer:

| **Object or Field**                                                                 | **Description**                                                               |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| offer\_data                                                                         | This object contains the fields containing the details of the offer.          |
| **Note**: You have one or more offer\_data object as it is part of multiple offers. |                                                                               |
| offer\_data.status                                                                  | Indicates whether the offer was successfully applied or failed to apply.      |
| offer\_data.discount                                                                | This field contains the discount amount                                       |
| offer\_data.isNoCost                                                                | Indicates whether it is a No-Cost EMI offer.                                  |
| offer\_data.offer\_key                                                              | This field contains the offer key                                             |
| offer\_data.offer\_type                                                             | This field contains the offer type                                            |
| offer\_data.offer\_title                                                            | This field contains the offer tittle                                          |
| offer\_data.flag\_to\_fail                                                          | Indicates whether flag to fail is enabled or not.                             |
| offer\_data.failure\_reason                                                         | This field contains the message success or failure with a reason.             |
| offer\_data.offer\_description                                                      | This field contains the offer description                                     |
| discount\_data                                                                      | This object contains the fields containing the discount details of the offer. |
| discount\_data.total\_discount                                                      | This field contains the total discount                                        |
| discount\_data.instant\_discount                                                    | This field contains instant discount in case of Instant Discount offer.       |
| discount\_data.cashback\_discount                                                   | This field contains the cashback discount in case of Cashback offer.          |
| discount\_data.total\_nce\_discount                                                 | This field contains the total No-Cost EMI discount.                           |
| discount\_data.instant\_nce\_discount                                               | This field contains the instant discount part of the No-Cost EMI discount.    |
| discount\_data.cashback\_nce\_discount                                              | This field contains the cashback part of the No-Cost EMI discount.            |

- SKU-Based Offers

`raw_response` has been added as a new object which will have all the details of both offers. This will be under `sku_details` of the `cart_details` object.

```plaintext
[cart_details] => {
  "total_items": "3",
  "total_cart_amount": "10000.00",
  "offer_applied": "ncebaseinstantsku@tbQAriEg8WhZ,instantsku@eKyZ8WnEy6Hs,ncebaseinstantsku@tbQAriEg8WhZ,instantsku@eKyZ8WnEy6Hs,ncebaseinstantsku@tbQAriEg8WhZ,instantsku@eKyZ8WnEy6Hs",
  "offer_availed": "instantsku@eKyZ8WnEy6Hs,ncebaseinstantsku@tbQAriEg8WhZ,instantsku@eKyZ8WnEy6Hs,ncebaseinstantsku@tbQAriEg8WhZ,instantsku@eKyZ8WnEy6Hs,ncebaseinstantsku@tbQAriEg8WhZ",
  "offer_auto_apply": "0",
  "instant_discount": "578.88",
  "cashback_discount": "0.00",
  "total_discount": "578.88",
  "net_cart_amount": "9421.12",
  "sku_details": [
    {
      "sku_id": "Boat-handfree234",
      "sku_name": "Iphone 11",
      "amount_per_sku": "5000.00",
      "quantity": "1",
      "amount_before_discount": "5000.00",
      "discount": "240.88",
      "amount_after_discount": "4759.12",
      "offer_applied": "ncebaseinstantsku@tbQAriEg8WhZ,instantsku@eKyZ8WnEy6Hs",
      "offer_availed": "instantsku@eKyZ8WnEy6Hs,ncebaseinstantsku@tbQAriEg8WhZ",
      "offer_status": "success",
      "offer_type": "INSTANT,INSTANT",
      "offer_auto_apply": "0",
      "is_nce": "1",
      "failure_reason": "",
      "instant_discount": "240.88",
      "cashback_discount": "0.00",
      "raw_response": [
        {
          "status": "SUCCESS",
          "discount": 100,
          "isNoCost": false,
          "offer_key": "instantsku@eKyZ8WnEy6Hs",
          "offer_type": "INSTANT",
          "offer_title": "instant sku",
          "flag_to_fail": false,
          "nce_discount": 0,
          "failure_reason": "Offer Applied Successfully",
          "instant_discount": 100,
          "cashback_discount": 0,
          "offer_description": "instant sku",
          "nce_instant_discount": 0,
          "nce_cashback_discount": 0
        },
        {
          "status": "SUCCESS",
          "discount": 140.88,
          "isNoCost": true,
          "offer_key": "ncebaseinstantsku@tbQAriEg8WhZ",
          "offer_type": "INSTANT",
          "offer_title": "nce base instant sku",
          "flag_to_fail": true,
          "nce_discount": 140.88,
          "failure_reason": "Offer Applied Successfully",
          "instant_discount": 240.88,
          "cashback_discount": 0,
          "offer_description": "nce base instant sku",
          "nce_instant_discount": 140.88,
          "nce_cashback_discount": 0
        }
      ]
    },
    {
      "sku_id": "abc",
      "sku_name": "Apple Airpods",
      "amount_per_sku": "2500.00",
      "quantity": "1",
      "amount_before_discount": "2500.00",
      "discount": "169.00",
      "amount_after_discount": "2331.00",
      "offer_applied": "ncebaseinstantsku@tbQAriEg8WhZ,instantsku@eKyZ8WnEy6Hs",
      "offer_availed": "instantsku@eKyZ8WnEy6Hs,ncebaseinstantsku@tbQAriEg8WhZ",
      "offer_status": "success",
      "offer_type": "INSTANT,INSTANT",
      "offer_auto_apply": "0",
      "is_nce": "1",
      "failure_reason": "",
      "instant_discount": "169.00",
      "cashback_discount": "0.00",
      "raw_response": [
        {
          "status": "SUCCESS",
          "discount": 100,
          "isNoCost": false,
          "offer_key": "instantsku@eKyZ8WnEy6Hs",
          "offer_type": "INSTANT",
          "offer_title": "instant sku",
          "flag_to_fail": false,
          "nce_discount": 0,
          "failure_reason": "Offer Applied Successfully",
          "instant_discount": 100,
          "cashback_discount": 0,
          "offer_description": "instant sku",
          "nce_instant_discount": 0,
          "nce_cashback_discount": 0
        },
        {
          "status": "SUCCESS",
          "discount": 69,
          "isNoCost": true,
          "offer_key": "ncebaseinstantsku@tbQAriEg8WhZ",
          "offer_type": "INSTANT",
          "offer_title": "nce base instant sku",
          "flag_to_fail": true,
          "nce_discount": 69,
          "failure_reason": "Offer Applied Successfully",
          "instant_discount": 169,
          "cashback_discount": 0,
          "offer_description": "nce base instant sku",
          "nce_instant_discount": 69,
          "nce_cashback_discount": 0
        }
      ]
    },
    {
      "sku_id": "abc-123",
      "sku_name": "Samsung AC",
      "amount_per_sku": "2500.00",
      "quantity": "1",
      "amount_before_discount": "2500.00",
      "discount": "169.00",
      "amount_after_discount": "2331.00",
      "offer_applied": "ncebaseinstantsku@tbQAriEg8WhZ,instantsku@eKyZ8WnEy6Hs",
      "offer_availed": "instantsku@eKyZ8WnEy6Hs,ncebaseinstantsku@tbQAriEg8WhZ",
      "offer_status": "success",
      "offer_type": "INSTANT,INSTANT",
      "offer_auto_apply": "0",
      "is_nce": "1",
      "failure_reason": "",
      "instant_discount": "169.00",
      "cashback_discount": "0.00",
      "raw_response": [
        {
          "status": "SUCCESS",
          "discount": 100,
          "isNoCost": false,
          "offer_key": "instantsku@eKyZ8WnEy6Hs",
          "offer_type": "INSTANT",
          "offer_title": "instant sku",
          "flag_to_fail": false,
          "nce_discount": 0,
          "failure_reason": "Offer Applied Successfully",
          "instant_discount": 100,
          "cashback_discount": 0,
          "offer_description": "instant sku",
          "nce_instant_discount": 0,
          "nce_cashback_discount": 0
        },
        {
          "status": "SUCCESS",
          "discount": 69,
          "isNoCost": true,
          "offer_key": "ncebaseinstantsku@tbQAriEg8WhZ",
          "offer_type": "INSTANT",
          "offer_title": "nce base instant sku",
          "flag_to_fail": true,
          "nce_discount": 69,
          "failure_reason": "Offer Applied Successfully",
          "instant_discount": 169,
          "cashback_discount": 0,
          "offer_description": "nce base instant sku",
          "nce_instant_discount": 69,
          "nce_cashback_discount": 0
        }
      ]
    }
  ]
}
```

The description of the object and fields in the response are described in the following table:

| **Object or Field**               | **Description**                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------- |
| cart\_details                     | This parameter contains object in a JSON format which has the SKU-based offer cart details. |
| cart\_details.total\_items        | This field contains total SKU-based offer items in the cart.                                |
| cart\_details.total\_cart\_amount | This field contains the total cart amount.                                                  |
| cart\_details.offer\_applied      | This field contains the offer applied for the transaction.                                  |
| cart\_details.offer\_availed      | This field contains the offer availed for the transaction.                                  |
| cart\_details.offer\_auto\_apply  | This field contains the offer that was automatically applied.                               |
| cart\_details.instant\_discount   | This field contains the instant discount amount for the offer.                              |
| cart\_details.cashback\_discount  | This field contains the cashback discount amount for the offer.                             |

| cart\_details.total\_discount  
  | This field contains the total discount amount for the offer. |  
| cart\_details.net\_cart\_amount | This field contains the net cart amount. |  
| sku\_details | This parameter contains an object in a JSON format that has the SKU details.  
**Note**: The response can have multiple sku\_details object as an offer can have multuple SKUs. |  
| sku\_details.sku\_name | This parameter contains the SKU name |  
| sku\_details.sku\_id | This parameter contains the SKU ID |  
| sku\_details.amount\_per\_sku | The parameter must contain the per SKU amount. |  
| sku\_details.quantity | The parameter must contain the quantity of SKU added in cart. |  
| sku\_details.offer\_key  | This parameter must contain the Offer Key(s) which can be used for this transaction. |  
| sku\_details.offer\_auto\_apply  | This parameter contains the flag for when to enable auto application of best offer on this SKU. |  
| sku\_details.offer\_applied | This field contains the offer applied for the SKU. |  
| sku\_details,offer\_availed | This field contains the offer availed for the SKU. |  
| sku\_details,offer\_status | This field contains the status of the offer for the SKU. |  
| sku\_details,offer\_type | This field contains the type of the offer for the SKU. |  
| sku\_details,offer\_auto\_apply | This field contains the offer that was automatically applied for the SKU. |  
| sku\_details,is\_nce | This field specified whether the SKU is No-Cost-EMI offer. |  
| sku\_details,failure\_reason | This field contains the failure or success reason. |  
| sku\_details,instant\_discount | This field contains the instant discount amount for the SKU. |  
| sku\_details,cashback\_discount | This field contains the cashback discount amount for the SKU. |

1. Verify the payment.

Similar to the payment response, the same parameters can be handled as part of the **verify\_payment** API. For more information, refer to [Verify Payment Status by Transaction ID](https://devguide.payu.in/api/payments/transaction-verification-apis/verify_payment-api/).

| **Parameter**       | **Description**                                                                                                                                                                                  | **Example** |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| transaction\_amount | This parameter contains the total transaction amount before discount.                                                                                                                            | 50000.00    |
| net\_amount\_debit  | This parameter contains the actual amount deducted from the customer’s payment instrument. In case of Instant discount this amount would be lesser than the amount passed by you in the request. | 47500.00    |
| discount            | This parameter contains the offer value provided to the user. This value will specify the offer amount for both Instant discount and Cashback offers.                                            | 2500.00     |

For the sample request and response from PayU, refer to [Web Checkout Integration > PayU Hosted Checkout Integration.](https://devguide.payu.in/merchant-integration/payu-hosted-checkout/payu-hosted-checkout-integration/)

1. If you want to refund the payment to the customer. refer to [Refund Transaction.](https://devguide.payu.in/api/refund-apis-2/cancel_refund_transaction/)

**Note**: You can enable the **Enforce Offer** flag by requesting your PayU Key Account Manager. If you enable the **Enforce Offer** flag, all the offers passed are visible to the customer and the customer chooses the offer that they wish to apply.

### **Response Parameters Description**

The response parameters related to multiple offers are described in the following table. For more information on other parameters in the response, refer to [Integrate with PayU Hosted Checkout](https://devguide.payu.in/web-checkout/payu-hosted-checkout/payu-hosted-checkout-integration/) \> [Response Parameters](https://devguide.payu.in/web-checkout/payu-hosted-checkout/payu-hosted-checkout-integration#response_params).