---
title: Check Offer Status API
excerpt: 'API Command: **check\_offer\_status**'
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The Check Offer Status API (**check\_offer\_status**) can be used for the following scenarios:

- [Check Merchant Specific Offers](https://devguide.payu.in/api/integration-apis/offers/check_offer_status#merchant)
- [Check Card Specific Offers](https://devguide.payu.in/api/integration-apis/offers/check_offer_status#card)

**Environment**

<table style="border:0.1rem solid rgb(242, 242, 242);"><tbody><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Test Environment</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">https://test.payu.in/merchant/postservice.php?form=2</td></tr><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Production Environment</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">https://info.payu.in/merchant/postservice?form=2</td></tr></tbody></table>

## Check Merchant Specific Offers

The Check Offer Status API is used to check the status of an offer for a particular merchant when all the details are passed. The return parameters are status, msg, discount/error\_code, category, offer\_key, offer\_type (instant or cashback), offer\_availed\_count and offer\_remaining\_count.

### Request Parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Sample Value**",
    "0-0": "var1  \n**mandatory**",
    "0-1": "The offer Key must be specified in this parameter.",
    "0-2": "offer@123",
    "1-0": "var2  \n**mandatory**",
    "1-1": "The payment amount of the particular transaction must be specified in this parameter.",
    "1-2": "10000",
    "2-0": "var3  \n**optional**",
    "2-1": "This parameter must contain the payment category that the merchant wants the user to see by default on the PayU’s payment page.",
    "2-2": "CC",
    "3-0": "var4  \n**optional**",
    "3-1": "This parameter must contain the bank code.",
    "3-2": "AMEX",
    "4-0": "var5  \n**mandatory**",
    "4-1": "This parameter must contain the card number.",
    "4-2": "5432112345678901",
    "5-0": "var6  \n**optional**",
    "5-1": "This parameter must contain name of the customer as on the card.",
    "5-2": "Nitesh",
    "6-0": "var7  \n**optional**",
    "6-1": "This parameter must contain the phone number of the customer.",
    "6-2": "9988776655",
    "7-0": "var8  \n**optional**",
    "7-1": "This parameter must contain email address of the customer.",
    "7-2": "[abc@xyz.com](mailto:abc@xyz.com)"
  },
  "cols": 3,
  "rows": 8,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


Error Codes:

- ‘INVALID\_OFFER’=>’E001′
- ‘INVALID\_PAYMENT\_METHOD’=>’E002’

**In the Output:**  
Parameter ‘status’ = 1, means offer is valid  
Parameter ‘status’ = 0, means offer is invalid

### Sample Request

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2"
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d

"key=JP***g&command=check_offer_status&var1=offer1@7788&var2=1000&var3=CC&var4=CC&var5=5123456789012346&var6=test&var7=987654321&var8=tesmm@jm.com&hash=862503800fbd33ac040473bc20e1b6c33b4a575893c0ec48813122f6971e8af2c24d05f1e3da32bc00e416a179f0ae4c46d330141b39d68ba22ff250167d2eb0"
```

### Sample Response

> 📘 Note:
> 
> In the response, the category will be the passed Category.

#### Success Scenario

If the offer is valid:

```plaintext
{
      "status": 1,
      "msg": "Valid offer",
      "discount": 100,
      "category": "creditcard",
      "offer_key": "offer1@7788",
      "offer_type": "instant",
      "offer_availed_count": 0,
      "offer_remaining_count": 0
}
```

#### Failure Scenario

- If the offer has expired:

If the offer has expired

```plaintext
Array 
(
[status] => 0
[msg] => Offer expired. 
[error_code] => E001
[category] => creditcard 
[offer_key] => newoffer1@5686 
[offer_type] => instant 
[offer_availed_count] => Unknown 
[offer_remaining_count] => Unknown
)
```

- If the card limit is exhausted:

If the card limit is exhausted

```plaintext
Array 
(
[status] => 0
[msg] => Offer Exhausted 
[error_code] => E001
[category] => creditcard 
[offer_key] => newoffer1@568 
[offer_type] => Unknown 
[offer_availed_count] => Unknown 
[offer_remaining_count => Unknown
)
```

- If the offer\_key is invalid:

If the offer\_key is invalid

```plaintext
Array 
(
[status] => 0
[msg] => Invalid offer Key 
[error_code] => E001
[offer_key] => newoffer1@568 
[offer_type] => Unknown 
[offer_availed_count] => Unknown 
[offer_remaining_count] => Unknown
)
```

## Check Card Specific Offers

The check\_offer\_status API is used to check the status of an offer when only the parameters Offer Key and card number are passed as input. This API is used to check the offer status when the offer is created using bin only. In this case, we can depict that the offer has been created for which category (like CC, DC, NB, or EMI). Hence, for using this API, you need to pass the Offer Key and Card Number in var1 and var5 fields as inputs and leave the remaining fields empty.

The return parameters are status, msg, error\_code (In case of error), category, offer\_key, offer\_type (instant/cashback), offer\_availed\_count, ‘offer\_remaining\_count’.

### Request Parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "var1  \n**mandatory**",
    "0-1": "This parameter contains the Offer Key of the merchant.",
    "0-2": "offer@123",
    "1-0": "var2  \n**mandatory**",
    "1-1": "This parameter must be contain the amount.",
    "1-2": "10000",
    "2-0": "var3  \n**optional**",
    "2-1": "This parameter must be left blank.",
    "2-2": "–",
    "3-0": "var4  \n**optional**",
    "3-1": "This parameter must be left blank.",
    "3-2": "–",
    "4-0": "var5  \n**mandatory**",
    "4-1": "This parameter must contain the card number.",
    "4-2": "5432112345678901"
  },
  "cols": 3,
  "rows": 5,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


Error Codes

- ‘INVALID\_OFFER’=>’E001′
- ‘INVALID\_PAYMENT\_METHOD’=>’E002’

**In the Output:**

- Parameter ‘status’ = 1, means offer is valid
- Parameter ‘status’ = 0, means offer is invalid

### Sample Request

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2"
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d

"key=JP***g&command=check_offer_status&var1=offer1@7788&var2=&var3=&var4=&var5=512345&hash=862503800fbd33ac040473bc20e1b6c33b4a575893c0ec48813122f6971e8af2c24d05f1e3da32bc00e416a179f0ae4c46d330141b39d68ba22ff250167d2eb0"
```

### Sample Response

> 📘 Note:
> 
> In the response, the category will be the passed Category.

#### Success Scenario

If the offer is valid:

```plaintext
{
      "status": 1,
      "msg": "Valid offer",
      "discount": 100,
      "category": "creditcard",
      "offer_key": "offer1@7788",
      "offer_type": "instant",
      "offer_availed_count": 0,
      "offer_remaining_count": 0
}
```

#### Failure Scenario

- If the offer has expired:

If the offer has expired

```plaintext
Array 
(
[status] => 0
[msg] => Offer expired. 
[error_code] => E001
[category] => creditcard 
[offer_key] => newoffer1@5686 
[offer_type] => instant 
[offer_availed_count] => Unknown 
[offer_remaining_count] => Unknown
)
```

- If the card limit is exhausted:

If the card limit is exhausted

```plaintext
Array 
(
[status] => 0
[msg] => Offer Exhausted 
[error_code] => E001
[category] => creditcard 
[offer_key] => newoffer1@568 
[offer_type] => Unknown 
[offer_availed_count] => Unknown 
[offer_remaining_count => Unknown
)
```

- If the offer\_key is invalid:

If the offer\_key is invalid

```plaintext
Array 
(
[status] => 0
[msg] => Invalid offer Key 
[error_code] => E001
[offer_key] => newoffer1@568 
[offer_type] => Unknown 
[offer_availed_count] => Unknown 
[offer_remaining_count] => Unknown
)
```