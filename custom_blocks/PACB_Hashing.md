---
name: PACB_Hashing
---
Parameters in the below sequence needs to be checked before generating the hash, if these params are being posted, it needs to be added in the hash calculation:

```
|additional_charges|miles|base_payuid|base_merchantid|paisa_mecode|subvention_amount|subvention_eligibility|merchant_data|payoutdetails|loan_id|twid_customer_hash|splitrequest|percentage_additional_charges|force_pa|udf_params|buyer_type_business|tcs_amount|
```

* **Case1 example**: Simple Hashing, if the merchant is not sending the api_version in the payment request, then it will be treated as hash sequence version 1.

```
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si_details|salt
```

* **Case2 example**:  if the merchant is passing the additional_charges in the payment request then they have to append the additional_charges value in the raw hash sequence as below.

```
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si_details|salt|additional_charges
```

* **Case3 example**: If the merchant wants to pass additional_charges, buyer_type_business in the payment request, then hash formula for payment request will be:

```
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si_details|salt|additional_charges|buyer_type_business
```

* **Case4 example**: if the merchant wants to pass the api_version = 7 and buyer_type_business, udf_params in the payment request.

```
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si_details|salt|udf_params|buyer_type_business
```
