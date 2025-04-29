---
title: Get Customer Rewards Balance API
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
This API is used to fetch the balance in customer account using the customer mobile number or customer hash.

## Request Parameters

| **Field** | **Description**                                                                                                                                                         | **Example**                                                                                                                      |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| key       | `Varchar` This parameter is the unique Merchant Key provided by PayU for your merchant account.                                                                         | CbgsJ2                                                                                                                           |
| command   | `Varchar` This parameter contains the command for this API. In this case, it is get\_twid\_customer\_details.                                                           | get\_twid\_customer\_details                                                                                                     |
| hash      | `Varchar` This parameter contains the hash. For hash calculation, you need to generate a string using certain parameters and apply the sha512 algorithm on this string. | c6febddfaaf6986dd8bd982d3769f856ab149e4de92dbad995c8df808ffcfbcb2c227a3fae38b69eb39ad7b6ce4e06e6b12289f70cc500cea5a2cda449c7dcba |
| var1      | `Varchar` This parameter must contain the hash returned during first successful transaction.                                                                            | f084619809b1467dcd02434ba29322c8624f10a5da3cc5c07949d397d37dcca4547c24e20eafe971427cc5835f48b00a                                 |

## Sample Request

```curl

curl --location --request GET 'https://info.payu.in/merchant/postservice.php?form=2' \\
\--header 'Content-Type: application/x-www-form-urlencoded' \\
\--data-urlencode 'key=CbgsJ2' \\
\--data-urlencode 'command=get\_twid\_customer\_details' \\
\--data-urlencode 'hash=c6febddfaaf6986dd8bd982d3769f856ab149e4de92dbad995c8df808ffcfbcb2c227a3fae38b69eb39ad7b6ce4e06e6b12289f70cc500cea5a2cda449c7dcba' \\
\--data-urlencode 'var1=f084619809b1467dcd02434ba29322c8624f10a5da3cc5c07949d397d37dcca4547c24e20eafe971427cc5835f48b00a'
```

## Sample Response

```plaintext
{
  "error_code": "0",
  "status": 1,
  "message": "Request sent successfully",
  "data": {
    "total_points_redeemable": "10",
    "total_amount_redeemable": "10.00"
  }
}
```
