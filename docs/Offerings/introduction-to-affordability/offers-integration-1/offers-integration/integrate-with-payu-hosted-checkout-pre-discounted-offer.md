---
title: Integrate with PayU Hosted Checkout - Pre-Discounted Offer
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
With the PayU Hosted Checkout integration, the entire payment experience is controlled by PayU. This section describes how to use the PayU Hosted Integration to collect payments with offers. 

**Notes**:

- In PayU Hosted Checkout Integration, By default, the Pre-Discounted offer is applied and it will not be listed in the list of offers. To avoid confusion for your customers, use the **enforce\_payment** flag to show only the payments for which you have the Pre-Discounted offers enabled. For more information, [Enforce Pay Method](https://devguide.payu.in/web-checkout/payu-hosted-checkout/checkout-customisations/).
- If you allow your customer to apply any other offer on your website, the transaction will fail from PayU end.
- Only one Pre-Discounted offer key can be sent in the payment request using the **Collect Payment** (\_payment) API.
- For the Pre-Discounted offers applied on cards, PayU recommends you validate the card number after the customer enters it.

## **Customer Journey on PayU Hosted Checkout**

1. Customer clicks **Pay** on your mobile application or website.
2. Customer is redirected to the PayU Hosted Checkout page.

The PayU Hosted Checkout page on Desktop is similar to the following screenshot. In case offer keys have been passed by the merchant, the same would be filtered and displayed to the customer.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Web.L1.Offers_Without-Global-vault-Copy-1-1024x858.png)

The PayU Hosted Checkout page on Mobile is similar to the following screenshot:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Mweb.L1.Offers_Without-Global-vault-a-Copy.png)

1. Customer is shown the applicable offers on the checkout page for that transaction.
2. Customer will have the option to apply the offer. If the offer is applicable to a specific payment option, the customer will be redirected to the specific payment option.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Web.L2.Without-Global-Vault_Cards_Filled-Copy-2-1024x863.png)

The PayU Hosted Checkout page for specify payment option on Mobile is similar to the following screenshot:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Mweb.L2.Without-Global-Vault_Cards_Filled-Copy.png)

1. Alternatively, the customer can choose the payment option. If only an offer is applicable for that payment option, the offer will be automatically applied.

![Picture 1522098393](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/picture-1522098393.png)

1. For Instant Discount, the amount is reduced after the offer is applied, whereas, in case of cashback, the amount will not be reduced after the offer is applied.
2. Customer completes the 2FA payment on the adjusted amount.
3. Customer is redirected back to the merchant’s mobile application or website.

## **Integration Steps**

To integrate offers using PayU Hosted Checkout integration:

**Reference**: For the PayU Hosted Checkout flow, refer to [PayU Hosted Checkout Integration](https://devguide.payu.in/merchant-integration/payu-hosted-checkout/payu-hosted-checkout-integration/).

1. Make the payment request to PayU:

You need to send additional parameters (**user token)**, **api\_version** as 14, and hash as described in the following table. This user token would be used to identify the customer for applying velocity rules.

| **Parameter** | **Description** | **Example** |
| ------------- | --------------- | ----------- |

| api\_version  
**mandatory** | The API version of the \_payment API must be specified as **14**. | 14 |  
| user\_token  
**mandatory for UPI, NB, Wallet** \|  
The use for this param is to allow the offer engine to apply velocity rules at a user level.  

 

- **Card Based Offers (CC, DC, EMI)**: In case of card payment mode offers, if this parameter is passed the velocity rules would be applied on this token, if not passed the same would be applied on the card number.
- **UPI, NB, Wallet**: It is mandatory for UPI, NB, and Wallet payment modes. If not passed the validation rules would not apply.

 | User123456 |  
| hash  
**mandatory** | It is used to avoid the possibility of transaction tampering.  
**Note**: The following order must be used for hashing:  
`key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|offer_key|offer_auto_apply|SALT`  
For more information on hash generation process, refer to [Hashing Request and Response](https://devguide.payu.in/wordpress/index.php/encryption-of-request/). |   |

1. Check the response from PayU.

You need to understand the following parameters to handle the payment response as the net amount debit may be different from the amount sent by you in the request.

| **Parameter**      | **Description**                                                                                                                                                                            | **Example**    |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- |
| discount           | This will specify the offer value provided to the user.                                                                                                                                    | 10.00          |
| net\_amount\_debit | This will specify the actual amount deducted from the customer’s payment instrument. In case of Instant discount this amount would be lesser than the amount passed by you in the request. | 100.00         |
| offer              | This parameter is used to post the offer key.                                                                                                                                              | newoffer1@5686 |
| offer\_type        |                                                                                                                                                                                            |                |

This parameter is used to post any of the following offer\_type:  

 

- instant
- cashback

 | instant |

The sample response from PayU is similar to the following:

```plaintext
Array
(
    [mihpayid] => 999000000001078
    [mode] => CC
    [status] => success
    [unmappedstatus] => captured
    [key] => KOEfPI
    [txnid] => 6623dafa9c010d5f47c0
    [amount] => 10000.00
    [cardCategory] => domestic
    [discount] => 0.00
    [net_amount_debit] => 10000
    [addedon] => 2023-01-16 19:13:13
    [productinfo] => Product Info
    [firstname] => Payu-Admin
    [lastname] => 
    [address1] => 
    [address2] => 
    [city] => 
    [state] => 
    [country] => 
    [zipcode] => 
    [email] => test@example.com
    [phone] => 1234567890
    [udf1] => 
    [udf2] => 
    [udf3] => 
    [udf4] => 
    [udf5] => 
    [udf6] => 
    [udf7] => 
    [udf8] => 
    [udf9] => 
    [udf10] => 
    [hash] => 98a5252e3326ce318e0f6c0a938e3c71771898ec5d9ff603b6fd93e77daa3e1368d1b05297de2d859c146f6782f29c2e4f4fd7afe4123a2abc63cff191fd3134
    [field1] => 770436
    [field2] => 309805
    [field3] => 20230116
    [field4] => 0
    [field5] => 725942224752
    [field6] => 00
    [field7] => AUTHPOSITIVE
    [field8] => Approved or completed successfully
    [field9] => No Error
    [payment_source] => payu
    [PG_TYPE] => CC-PG
    [bank_ref_num] => 770436
    [bankcode] => CC
    [error] => E000
    [error_Message] => No Error
    [offer] => prediscountedoffer@8X93OPhqFVr2
    [offer_availed] => prediscountedoffer@8X93OPhqFVr2
    [transaction_offer] => {"offer_data":[{"status":"SUCCESS","discount":0,"isNoCost":false,"offer_key":"prediscountedoffer@8X93OPhqFVr2","offer_type":"PRE_DISCOUNTED","offer_title":"pre discounted offer","failure_code":null,"flag_to_fail":true,"failure_reason":"Offer Applied Successfully","offer_description":"pre discounted offer"}],"discount_data":{"total_discount":0,"instant_discount":0,"cashback_discount":0,"total_nce_discount":0,"instant_nce_discount":0,"cashback_nce_discount":0}}
    [cardnum] => XXXXXXXXXXXX0000
    [cardhash] => This field is no longer supported in postback params.
    [issuing_bank] => ICICI
    [card_type] => VISA
    [offer_type] => cashback
)
```

1. Verify the payment.

Similar to the payment response, the same parameters can be handled as part of the **verify\_payment** API. For more information, refer to [Verify Payment Status by Transaction ID](https://devguide.payu.in/api/payments/transaction-verification-apis/verify_payment-api/).

| **Parameter**       | **Description**                                                                                                                                                                                  | **Example** |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| transaction\_amount | This parameter contains the total transaction amount before discount.                                                                                                                            | 50000.00    |
| net\_amount\_debit  | This parameter contains the actual amount deducted from the customer’s payment instrument. In case of Instant discount this amount would be lesser than the amount passed by you in the request. | 47500.00    |
| discount            | This parameter contains the offer value provided to the user. This value will specify the offer amount for both Instant discount and Cashback offers.                                            | 2500.00     |

For the sample request and response from PayU, refer to [Web Checkout Integration > PayU Hosted Checkout Integration.](https://devguide.payu.in/merchant-integration/payu-hosted-checkout/payu-hosted-checkout-integration/)

1. If you want to refund the payment to the customer. refer to [Refund Transaction.](https://devguide.payu.in/api/refund-apis-2/cancel_refund_transaction/)

**Note**: You can enable the **Enforce Offer** flag by requesting your PayU Key Account Manager. If you enable the **Enforce Offer** flag, all the offers passed are visible to the customer and the customer choose an offer that they wish to apply.