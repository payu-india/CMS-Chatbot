---
title: UDF Update API
excerpt: ''
api:
  file: opgsp-invoice-4.json
  operationId: udf_update-OPGSP
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **UDF Update** API is used to update the UDF1-UDF5 values of a transaction. UDFs are the user-defined fields which are posted from the merchant to PayU. This API is specifically used to update the values in these fields in the PayU database. The return parameters are the updated UDF values of the transaction.

<GENERALAPIsEnvironment/>

## Reference info for request parameters



<details>
  <summary>Sample request for Cards </summary>

```
curl --location --globoff 'https://test.payu.in/merchant/postservice.php?form=2' \
--form 'key="PRiQvJ"' \
--form 'command="udf_update"' \
--form 'var1="my_order_642"' \
--form 'var2="AAAPZ1234C"' \
--form 'var4="22/08/1972"' \
--form 'var5="SellerName"' \
--form 'var6="INV000000005"' \
--form 'hash="{{hash}}"'
```

</details>

<details>
  <summary>Sample request for UPI autopay </summary>

```
curl --location --globoff 'https://test.payu.in/merchant/postservice.php?form=2' \
--form 'key="PRiQvJ"' \
--form 'command="udf_update"' \
--form 'var1="my_order_64240"' \
--form 'var2="AAAPZ1234C||22/08/1972"' \
--form 'var4="INV-123_1231||MerchantName"' \
--form 'hash="{{hash}}"'
```

</details>

<details>
  <summary>Sample response</summary>

### Success Scenario

* If successfully updated for cards

```plaintext
{
    "status": "UDF values updated",
    "transaction_id": "my_order_64240",
    "udf1": "AAAPZ1234C",
    "udf2": "",
    "udf3": "22/08/1972",
    "udf4": "SellerName",
    "udf5": "INV000000005"
}
```

* If successfully updated for UPI autopay:

```plaintext
{
    "status": "UDF values updated",
    "transaction_id": "my_order_64240",
    "udf1": "AAAPZ1234C",
    "udf2": "",
    "udf3": "22/08/1972",
    "udf4": "SellerName",
    "udf5": "INV000000005"
}
```

### Failure Scenarios

* If the transaction ID is empty

```plaintext
( 
[status] => 0 
[msg] => Parameter missing 
) 
```

* If the transaction ID is invalid

```plaintext
( 
[status] => 0 
[msg] => Invalid TXN ID 
) 
```

* If Hash is invalid:

```plaintext
{
    "status": 0,
    "msg": "Invalid Hash."
}
```

</details>

## Request parameters