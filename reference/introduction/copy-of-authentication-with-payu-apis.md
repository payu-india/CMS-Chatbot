---
title: Copy of Authentication with PayU APIs
deprecated: false
hidden: false
metadata:
  title: Authentication with PayU APIs
  description: >-
    Learn how to securely authenticate and integrate with PayU India’s APIs.
    Explore topics such as merchant keys, salt, REST API authentication, hash
    parameters, and SHA512 encryption. Enhance your payment gateway integration
    with PayU’s robust security features.
  keywords:
    - PayU India API authentication
    - Merchant key and salt for PayU APIs
    - REST API authentication with PayU
    - Hash parameter in PayU API requests
    - SHA512 encryption for PayU API security
    - Reverse hashing using PayU node SDK
    - Generate hash for PayU API parameters
  robots: index
---
The PayU India API requires authentication using a merchant key and a salt. When you post requests using any of the PayU APIs, you will be posting the merchant key as the first parameter, so separate authentication is not required because these are REST APIs  All requests are accompanied by a hash that is appended at the end of the request. While posting parameters for an API, the hash parameter in each API must contain the hash value to be calculated at your end. The following hash logic used in PayU India APIs:

* **Payment** APIs or \_payment API: The string used for calculating the hash:

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
```

* **General** APIs (listed under **General**): The string used for calculating the hash: 

```
sha512(key|command|var1|salt)
```

* **SI Integration** or **Subscription** APIs: The string used to calculating the hash:

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si_details|SALT)
```

* **TPV Integration**: The string used calculating the hash:

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT)
```

* **Split Settlements Integration**: The string used calculating the hash:

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT|splitRequest)
```

Here, sha512 is the encryption method used. For more information on SHA, refer to [Wikipedia 1](https://ind01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdevguide.payu.in%2Fapi-authentication-security\&data=05%7C01%7Craghuram.pandurangan%40payu.in%7Ca0282d941fee47c65e8508dbb8300656%7Ca7242bb643ca445abe2d34c2f02fac89%7C0%7C0%7C638306288620041132%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C\&sdata=D%2BUEpZot6HJW97OQOm1feggy6RQjV9B1vSplhZOQSS8%3D\&reserved=0).

## Hash logic for \_payment API version 19:

The following hash logic must be used for \_payment API with **api\_version=19**:\
`key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|user_token|offer_key|offer_auto_apply|cart_details|extra_charges|phone`

## Reverse Hashing

To perform reverse hashing, you can use the Hash API of the PayU node SDK on Github. Refer to the PayU node SDK Readme, download and install the PayU node SDK from the [PayU node SDK Github location 1](https://ind01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdevguide.payu.in%2Fapi-authentication-security\&data=05%7C01%7Craghuram.pandurangan%40payu.in%7Ca0282d941fee47c65e8508dbb8300656%7Ca7242bb643ca445abe2d34c2f02fac89%7C0%7C0%7C638306288620041132%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C\&sdata=D%2BUEpZot6HJW97OQOm1feggy6RQjV9B1vSplhZOQSS8%3D\&reserved=0).

> 📘 Reference
>
> For hashing or reverse hashing, refer to [Generate Hash](doc:hashing-request-and-response)