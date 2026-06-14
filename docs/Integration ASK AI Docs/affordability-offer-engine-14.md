---
title: 'Affordability (Offer Engine) 1/4 '
deprecated: false
hidden: false
metadata:
  robots: index
---
Affordability refers to the ability of customers to pay for products or services using flexible and convenient payment options, such as EMIs (equated monthly instalments), Pay Later, No Cost EMI, and other offers.

Offer Engine solutions can help online businesses attract more customers, increase sales, and improve customer loyalty by providing them with payment plans that suit their budget and preferences.

\===================================================================== ====

Offers Type:-

1\)Instant discount offer

2\)Cashback offer

3\)No-Cost /Low cost EMI offer

4\)Pre- discounted offers

5\)Sku based offers

6\)Coupons

\===================================================================== =====

Enforce offer - disabled

Merchants need not send any offer key in the \_payment request. PayU will automatically show all offers created by the merchant to the user on PayU’s checkout page and the user will be able to apply any of the offers applicable.

Enforce offer - enabled

Merchant should always send offer keys that need to be shown to the customer in the “offe&#x72;_&#x6B;ey” parameter in_ payment request. If the “offer\_key” is not sent or null, no offers would be applied in this case.

Note: This flag is relevant only for non-seamless merchants, this doesn't have any impact on seamless merchants

\===================================================================== ====
Payment Request Parameter's:-
You need to send additional parameters like below in your existing \_payment API request for offer integrations.

1\)PayU Hosted Checkout:- (using \_payment request)
i)user\_token (Non-Mandatory):- This param is to allow the offer engine to apply velocity rules at a user level. It mandatory for UPI, NB, Wallet & conditional on card
ii)offer\_key(Non-Mandatory) :- This parameter is Mandatory if enforced\_offers is enabled on MID, else it is not required to pass.

iii)offer\_auto\_apply(Non-Mandatory):- This will help to fetch best of offer from multiple offers pass in offer\_key and same offer will get auto apply at the time of checkout
1\)Merchant Hosted Checkout:-
i)user\_token (Non-Mandatory):- This param is to allow the offer engine to apply velocity rules at a user level. It mandatory for UPI, NB, Wallet & conditional on card.

ii)offer\_key(Mandatory) :- This parameter is Mandatory to apply the offer at the time of transaction
iii)offer\_auto\_apply(Non-Mandatory):- This will help to fetch best of offer from multiple offers pass in offer\_key and same offer will get auto apply at the time of checkout
Best offer basis discount value to be auto-applied during the transaction
Hash Formula:-
using version 14 -
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|ud f7|udf8|udf9|udf10|offer\_key|offer\_auto\_apply|SALT

• If any of the keys is null/not configured, "|" character must be concatenated.
