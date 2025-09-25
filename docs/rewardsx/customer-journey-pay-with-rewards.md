---
title: Customer Journey - Pay with Rewards
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
PayU supports Pay with Rewards with PayU Hosted Checkout and Merchant Hosted Checkout. This section describes the customer workflow for the PayU Hosted Checkout and Merchant Hosted Checkout.

## PayU Hosted Checkout Workflow

After your customer adds the goods to the cart or services and checkouts, the workflow involves the following:

> 📘 Note:
>
> The request parameters for PayU Hosted Checkout remains the same and the response will contain **mode=CASH** and **bankcode=TWID**. For more information, refer to [Collect Payments with PayU Hosted Checkout](https://devguide.payu.in/merchant-integration/payu-hosted-checkout/payu-hosted-checkout-integration/).

1. Customer is redirected to the PayU payment page after checkout.
2. Customer selects **Pay with Rewards** as the payment option.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/10/Pay_with_Rewards_PayU_Page-1-907x1024.png)

1. Customer enters the mobile number that has the rewards to be redeemed and clicks **Proceed**.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/10/Pay_with_Rewards_PayU_Page_Mobile_No-902x1024.png)

1. Customer is redirected to TWID page.

The reward points balance for the linked mobile number is displayed.

**Note**: As customer is paying using reward points, it is shown as savings and amount to be paid is **0** (zero).

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/10/TWID_redirected_page-511x1024.png)

1. Customer clicks **Proceed to Pay**.

> **Note**: If the customer has insufficient reward points, the can choose any other payment instrument and pay the rest of the amount.

1. Customer enters the OTP that is received in the mobile number entered at Step 3 and clicks **Verify & Proceed**.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/10/TWID_OTP_Page-1-683x1024.png)

> **Note**: For a repeat customer, the customer balance will be fetched automatically and the OTP registration step will be bypassed as the merchant would pass the already registered based on customer mobile number, which PayU will use as the registered customer hash for subsequent transactions. Alternatively, merchant can also pass the customer hash themselves.

TWID validates the OTP and checks with the issuer to process the redemption.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/10/TWID_Payment_Processing-571x1024.png)

A message similar to the following is displayed when the redemption is successful:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/10/TWID_Payment_Successful-545x1024.png)

## Merchant Hosted Checkout Workflow

You will be collecting the checkout information from the customer using the fields on your website and submitting it with PayU using the **\_payment** API. The customer workflow when using Pay with Rewards:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/05/Screenshot-2022-05-02-at-12.26.29-PM-1024x460.png)

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/05/Screenshot-2022-05-02-at-12.26.46-PM-1024x380.png)

1. Customer visits your payment page after checkout. For the first-time user, the customer links their account to fetch the balance and pay.
2. Customer selects Pay with Rewards as the payment option
3. PayU redirects to TWID or partner page and the customer registers through mobile OTP (for a repeat customer this step is skipped).
4. Customer selects the desired rewards currency.
5. Customer can bifurcate payment amount into rewards and any other payment instrument.
6. Customer selects a payment instrument for bifurcated payment.
7. Customer initiates payment flow (3DS/OTP/Pin).
8. Success page is displayed after successful payment.

> 📘 Note:
>
> For a repeat customer, the customer balance will be fetched automatically and the OTP registration step will be bypassed as the merchant would pass the already registered based on customer mobile number, which PayU will use as the registered customer hash for subsequent transactions. Alternatively, merchant can also pass the customer hash themselves.

## Refunds

If the payment has failed for the following payment combinations, the refund is initiated by PayU:

* If the payment has failed for the whole amount paid with Pay with Rewards, the refund will be initiated by PayU.
* If the payment has failed for the part of amount paid with Pay with Rewards and rest with any other payment instruments such as Net Banking or Credit Cards, the refund will be initiated by PayU. The time taken to refund depends on the payment instrument used.
