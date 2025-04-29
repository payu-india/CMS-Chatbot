---
title: Integrate PayU Hosted Checkout - Offer Grouping
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
With the PayU Hosted Checkout integration, the entire payment experience is controlled by PayU. This section describes how to use the PayU Hosted Integration to collect payments with offers grouping.

## **Customer Journey on PayU Hosted Checkout**

1. Customer clicks **Pay** on your mobile application or website.
2. Customer is redirected to the PayU Hosted Checkout page.

The PayU Hosted Checkout page on Desktop is similar to the following screenshot. In case offer keys have been passed by the merchant, the same would be filtered and displayed to the customer.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Web.L1.Offers_Without-Global-vault-Copy-1-1024x858.png)

The PayU Hosted Checkout page on Mobile is similar to the following screenshot:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Mweb.L1.Offers_Without-Global-vault-a-Copy.png)

1. Customer is shown the applicable offers on the checkout page for that transaction.
2. Customer will have an option to apply the offer. If the offer is applicable on a specific payment option, the customer will be redirected to the specific payment option.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Web.L2.Without-Global-Vault_Cards_Filled-Copy-2-1024x863.png)

The PayU Hosted Checkout page for specify payment option on Mobile is similar to the following screenshot:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Mweb.L2.Without-Global-Vault_Cards_Filled-Copy.png)

1. Alternatively, the customer can choose the payment option. If only an offer is applicable for that payment option, the offer will be automatically applied.

![Picture 1522098393](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/picture-1522098393.png)

1. For Instant Discount, the amount is reduced after the offer is applied, where as, in case of cashback, the amount will not be reduced after the offer is applied.
2. Customer completes the 2FA payment on the adjusted amount.
3. Customer is redirected back to the merchant mobile application or website.

## **Integration Steps**

To integrate offers using PayU Hosted Checkout integration:

**Reference**: For the PayU Hosted Checkout flow, refer to [PayU Hosted Checkout Integration](https://devguide.payu.in/merchant-integration/payu-hosted-checkout/payu-hosted-checkout-integration/).

1. Make the payment request to PayU:

You need to send an additional parameter (**user token)**, **api\_version** as 14, and hash as described in the following table. This user token would be used to identify the customer for applying velocity rules.

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
| Group Name  
**mandatory** | Should be unique |   |  
| Max offers per user  
**atleast one of the fields** | This is the maximum number of times an offer can be availed by a user |   |  
| Max budget per user  
**optional** | This is the maximum budget that can be availed by a user |   |  
| Reset User Limits  
**optional** | This needs to be added only if user limits need to be reset at regular intervals. Examples of value can be 1 day, 3 weeks, 2 months etc |   |  
| Offer Keys  
**optional** | Offer keys can be added after creation of offer group as well |   |

1. Check the response from PayU.

You need to understand the following params to handle the payment response as the net amount debit may be different from the amount sent by you in the request.

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

For a sample response from PayU, refer to [Web Checkout Integration > PayU Hosted Checkout Integration](https://devguide.payu.in/merchant-integration/payu-hosted-checkout/payu-hosted-checkout-integration/#Step3).

1. Verify the payment.

Similar to the payment response, the same parameters can be handled as part of the **verify\_payment** API. For more information, refer to [Verify Payment Status by Transaction ID](https://devguide.payu.in/api/payments/transaction-verification-apis/verify_payment-api/).

| **Parameter**       | **Description**                                                                                                                                                                                  | **Example** |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| transaction\_amount | This parameter contains the total transaction amount before discount.                                                                                                                            | 50000.00    |
| net\_amount\_debit  | This parameter contains the actual amount deducted from the customer’s payment instrument. In case of Instant discount this amount would be lesser than the amount passed by you in the request. | 47500.00    |
| discount            | This parameter contains the offer value provided to the user. This value will specify the offer amount for both Instant discount and Cashback offers.                                            | 2500.00     |

For the sample request and response from PayU, refer to [Web Checkout Integration > PayU Hosted Checkout Integration.](https://devguide.payu.in/merchant-integration/payu-hosted-checkout/payu-hosted-checkout-integration/)

1. If you want to refund the payment to customer. refer to [Refund Transaction.](https://devguide.payu.in/api/refund-apis-2/cancel_refund_transaction/)

**Notes**: PayU would refund the exact amount passed by you in the Refund request:

<table style="border:0.1rem solid rgb(242, 242, 242);"><tbody><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;"><strong>Offer Type</strong></td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;"><strong>Refund Detail</strong></td></tr><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Instant discount</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">You would need to adjust the discount amount before calling the <strong>Cancel Refund Transaction </strong>API. Any refund request where the refund amount exceeds the actual amount deducted from the customer will fail.&nbsp;For more information, refer to <a href="https://devguide.payu.in/api/refund-apis-2/cancel_refund_transaction/">Cancel Refund Transaction API</a>.<br>For example, if the amount was INR 100 and the discount was INR 10 and if you wish to process a full refund, you will need to pass INR 90 as the refund amount.&nbsp;<br>For partial refunds, you can decide whether to deduct the discount amount or not. You need to pass the exact value to be refunded back to the user.</td></tr><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Cashback</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">There is no need for adjustment of refunds where cashback was applied earlier with the transaction. If the cashback has been processed by the bank, the cashback amount will not be refunded.&nbsp;<br>For example, if the amount was INR 100 and the cashback was INR 10 and if you wish to process a full refund, you will need to pass INR 100 as the refund amount.<br>In case you wish to adjust the cashback amount, reduce the cashback amount from the refund amount and submit it in the request.<br>In the above example, pass INR 90 as the refund amount.</td></tr></tbody></table>

**Note**: You can enable the **Enforce Offer** flag by requesting your PayU Key Account Manager. If you enable the **Enforce Offer** flag, all the offers passed are visible to customer and the customer choose the an offer that they wish to apply.