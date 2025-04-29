---
title: Create or Register Beneficiary API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The Create Beneficiary API command is used to register a beneficiary under the merchant. After registering, the merchant can use the beneficiary id to make the payout.

HTTP Method: **POST**

**Environment**

|                            |                                                   |
| -------------------------- | ------------------------------------------------- |
| **Test Environment**       | <https://uatoneapi.payu.in/payout/beneficiary>    |
| **Production Environment** | <https://payout.payumoney.com/payout/beneficiary> |

## Request header

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "Authorization`\nmandatory`",
    "0-1": "`String` Specify the access token generated earlier in this parameter.",
    "0-2": "Bearer {access\\_token}",
    "1-0": "payoutMerchantId  \nmandatory\\`",
    "1-1": "`String` Specify the payout merchant id provided while onboarding or creating Payout account.",
    "1-2": "1111126",
    "2-0": "Content-Type  \n`mandatory`",
    "2-1": "`String` Indicates the format in which the request is sent.",
    "2-2": "application/json"
  },
  "cols": 3,
  "rows": 3,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


> 📘 Note:
> 
> The **pid** is **payoutMerchantId**, however it is different from the PayU merchant id. Check the Payouts Dashboard or call the PayU Customer Support if you don’t know your **payoutsMerchantID**.

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameters**",
    "h-1": "**Description**",
    "0-0": "accountNo`\nconditional`",
    "0-1": "`String`Indicates Account number of customer",
    "1-0": "ifsc  \n`conditional`",
    "1-1": "`String`Indicates IFSC code of the bank account",
    "2-0": "vpa  \n`conditional`",
    "2-1": "`String`Indicates UPI ID of customer  \n**Note:** Same value will be used by the merchant in the status check of transfer.",
    "3-0": "name`\noptional`",
    "3-1": "`String`Indicates of the customer",
    "4-0": "email  \n`optional`",
    "4-1": "`String`Indicates Email Address of customer",
    "5-0": "mobile`\nconditional`",
    "5-1": "`String`Indicates Mobile Number of customer"
  },
  "cols": 2,
  "rows": 6,
  "align": [
    null,
    null
  ]
}
[/block]


## Sample request

```curl
curl --location 'https://uatoneapi.payu.in/payout/beneficiary' \
--header 'Content-Type: application/json' \
--header 'payoutMerchantId: 2225335' \
--header 'Authorization: Bearer 6e47dc301158318020af04917b256422cf7f8e11147807102abe5b984c7a03e7' \
--data-raw '{ 
        "name": "test", 
        "email": "test@gmail.com", 
        "mobile": "1234567890", 
        "ifsc": "ABCD0123456", 
        "vpa": "test@upi", 
        "cardNo": "", 
        "beneCode": "BENECODE123" 
    }'
```

## Response parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "0-0": "status",
    "0-1": "This parameter returns the status of web service call. The status can be any of the following:  \n  \n- **0** - If web service call succeeded\n- ** 1** - If web service call failed",
    "1-0": "msg",
    "1-1": "This parameter returns the success or failure message.",
    "2-0": "code",
    "2-1": "This parameter returns the error code if the API failed to verify or invalid details.",
    "3-0": "data",
    "3-1": "This parameter returns the saved card details in a JSON format. For more information, refer to the next table."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    null,
    null
  ]
}
[/block]


### Description of data JSON Fields

| **Field**     | **Description**                                                                                                                                           |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| beneficiaryId | This field returns PayU beneficiary ID for the beneficiary added.                                                                                         |
| name          | This field returns the beneficiary name.                                                                                                                  |
| email         | This field returns the email ID of the beneficiary.                                                                                                       |
| mobile        | This field returns the mobile number of the beneficiary.                                                                                                  |
| accountNo     | This fields returns the account number of the beneficiary.                                                                                                |
| ifsc          | This field returns the IFSC code of the bank brach with which the beneficiary holds the account.                                                          |
| vpa           | This field returns the VPA ID of the beneficiary if they have registered for UPI.                                                                         |
| merchantId    | This field returns the PayU merchant ID of the beneficiary.                                                                                               |
| isValid       | This field returns any of the following values to indicate whether the account is valid or not:                                                           |
| addedOn       | This field returns any of the date and time stamp when the beneficiary was added with PayU.                                                               |
| updatedOn     | This field returns any of the date and time stamp when the beneficiary details were updated with PayU.                                                    |
| isVerified    | This field returns any of the following values to indicate account was verified by PayU. The value null is returned if the account is yet to be verified. |
| nameWithBank  | This field returns the beneficiary name as in the bank records.                                                                                           |
| cardNo        | This field returns the card number if the beneficiary holds a card with bank.                                                                             |

## Sample response

- Success scenario

```
{ 

    "status": 0, 
    "msg": "Beneficiary Created with Id :16", 
    "code": null, 
    "data": { 
        "beneficiaryId": 16, 
        "name": "Deepak", 
        "email": "deepak@gmail.com", 
        "mobile": "1234567890", 
        "accountNo": "12", 
        "ifsc": "ICIC1234567", 
        "vpa": null, 
        "merchantId": 1111167, 
        "isValid": true, 
        "addedOn": "2020-06-22T08:13:37.000+0000", 
        "updatedOn": "2020-06-22T08:13:37.000+0000", 
        "isVerified": null, 
        "nameWithBank": null, 
        "cardNo": null 
} 
```

- Failure scenario

```
{
  "status": 0,
  "msg": null,
  "code": null,
  "data": {
    "error": "card beneficiary creation is not supported",
    "errorCodes": [
      1018
    ]
  }
}
```