---
title: PayU Hosted Checkout - CB
api:
  file: PayU_Hosted_Checkout_Non_Seamless_API_Corrected.json
  operationId: MerchantHostedCheckout-Cards
hidden: true
---
```
curl --location 'https://test.payu.in/_payment' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=PRiQvJ' \
--data-urlencode 'txnid=my_order_64240' \
--data-urlencode 'amount=5' \
--data-urlencode 'productinfo=asfas' \
--data-urlencode 'email=test@test.com' \
--data-urlencode 'phone=8688359250' \
--data-urlencode 'hash={{hash}}' \
--data-urlencode 'surl=https://test.payu.in/admin/test_response' \
--data-urlencode 'furl=https://test.payu.in/admin/test_response' \
--data-urlencode 'udf1=' \
--data-urlencode 'udf2=' \
--data-urlencode 'udf3=' \
--data-urlencode 'udf4=' \
--data-urlencode 'udf5=' \
--data-urlencode 'firstname=sudhanshu' \
--data-urlencode 'lastname=kr' \
--data-urlencode 'address1=308,third floor' \
--data-urlencode 'address2=testing' \
--data-urlencode 'city=ggn' \
--data-urlencode 'state=UP' \
--data-urlencode 'country=IND' \
--data-urlencode 'zipcode=122018' \
--data-urlencode 'buyer_type_business=1' \
--data-urlencode 'lrs_mandatory_limit_declaration=I declare that the remittance is within my annual LRS limit' \
--data-urlencode 'lrs_tnc=I agree to the terms and conditions for LRS transactions' \
--data-urlencode 'lrs_tcs_declaration_under_limit=I declare that this transaction is under the specified limit'

```