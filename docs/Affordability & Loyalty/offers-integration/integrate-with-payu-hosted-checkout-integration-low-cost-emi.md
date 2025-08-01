---
title: Integrate with PayU Hosted Checkout Integration - Low-Cost EMI
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
With the PayU Hosted Checkout integration, the entire payment experience is controlled by PayU. This section describes how to use the PayU Hosted Integration to collect payments with a Low-Cost EMI Offer.

## Customer Journey on PayU Hosted Checkout

1. Customer clicks **Pay** on your mobile application or website.
2. Customer is redirected to the PayU Hosted Checkout page.

The PayU Hosted Checkout page on Desktop is similar to the following screenshot. In case offer keys have been passed by the merchant, the same would be filtered and displayed to the customer.

1. Customer is shown the applicable offers on the checkout page for that transaction.
2. Customer will have the option to apply the offer. If the offer is applicable to a specific payment option, the customer will be redirected to the specific payment option.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/04/Screenshot-2023-04-10-at-9.45.16-AM-946x1024.png)

For Instant Discount, the amount is reduced after the offer is applied, whereas, for cashback, the amount will not be reduced after the offer is applied.

1. Customer completes the 2FA payment on the adjusted amount.
2. Customer is redirected back to the merchant’s mobile application or website.

## **Integration Steps**

To integrate offers using PayU Hosted Checkout integration:

**Reference**: For the PayU Hosted Checkout flow, refer to [PayU Hosted Checkout Integration](https://devguide.payu.in/merchant-integration/payu-hosted-checkout/payu-hosted-checkout-integration/).

1. Make the payment request to PayU:

You need to send additional parameters (**user token**), **api\_version** as 14, and hash as described in the following table. This user token would be used to identify the customer for applying velocity rules.

| **Parameter** | **Description** | **Example** |
| ------------- | --------------- | ----------- |
| api\_version **mandatory** | The API version of the \_payment API must be specified as **14**. | 14 |  
| user\_token **mandatory for UPI, NB, Wallet** | The use for this param is to allow the offer engine to apply velocity rules at a user level. | User123456 |  
| hash **mandatory** | It is used to avoid the possibility of transaction tampering. **Note**: The following order must be used for hashing: `key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|offer_key|offer_auto_apply|SALT`. For more information on hash generation process, refer to [Hashing Request and Response](https://devguide.payu.in/wordpress/index.php/encryption-of-request/). |   |

1. Check the response from PayU.

You need to understand the following parameters to handle the payment response as the net amount debit may be different from the amount sent by you in the request.

| **Parameter**      | **Description**                                                                                                                                                                            | **Example**    |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- |
| discount           | This will specify the offer value provided to the user.                                                                                                                                    | 10.00          |
| net\_amount\_debit | This will specify the actual amount deducted from the customer’s payment instrument. In case of Instant discount this amount would be lesser than the amount passed by you in the request. | 100.00         |
| offer              | This parameter is used to post the offer key.                                                                                                                                              | newoffer1@5686 |
| offer\_type        | This parameter is used to post any of the following offer\_type: instant, cashback | instant |

The sample response from PayU is similar to the following:

```plaintext
Array
(
    [mihpayid] => 999000000001077
    [mode] => EMI
    [status] => success
    [unmappedstatus] => captured
    [key] => KOEfPI
    [txnid] => a63e9f163303a9859658
    [amount] => 10000.00
    [cardCategory] => domestic
    [discount] => 700.00
    [net_amount_debit] => 9300
    [addedon] => 2023-01-16 19:07:42
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
    [hash] => 8a8785ed5b007aa395578b4158b9b30eaec2edfa730298f5f1ea34b1486ae0fa89235734fe230072b8f6ca341cb191fbd1a1cbf0e232213dc30ea4a5790a0655
    [field1] => 902130
    [field2] => 603271
    [field3] => 20230116
    [field4] => 0
    [field5] => 327230725770
    [field6] => 00
    [field7] => AUTHPOSITIVE
    [field8] => Approved or completed successfully
    [field9] => No Error
    [payment_source] => payu
    [PG_TYPE] => EMI-PG
    [bank_ref_num] => 902130
    [bankcode] => EMIIC12
    [error] => E000
    [error_Message] => No Error
    [offer] => Lowcostemioffer@eWWDVsdbQJil
    [offer_availed] => Lowcostemioffer@eWWDVsdbQJil
    [transaction_offer] => {"offer_data":[{"status":"SUCCESS","discount":700,"isNoCost":false,"offer_key":"Lowcostemioffer@eWWDVsdbQJil","offer_type":"INSTANT","offer_title":"Low cost emi offer ","failure_code":null,"flag_to_fail":false,"failure_reason":"Offer Applied Successfully","offer_description":"low cost emi offer "}],"discount_data":{"total_discount":700,"instant_discount":700,"cashback_discount":0,"total_nce_discount":0,"instant_nce_discount":0,"cashback_nce_discount":0}}
    [cardnum] => XXXXXXXXXXXX0000
    [cardhash] => This field is no longer supported in postback params.
    [offer_type] => instant
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

**Note**: You can enable the **Enforce Offer** flag by requesting your PayU Key Account Manager. If you enable the **Enforce Offer** flag, all the offers passed are visible to the customer and the customer choose the an offer that they wish to apply.