---
title: Get EMI Checkout Details API
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
### Environment

|                        |                                                                   |
| ---------------------- | ----------------------------------------------------------------- |
| Test Environment       | <https://test.payu.in/info/linkAndPay/get\_emi\_checkout_details> |
| Production Environment | <https://info.payu.in/linkAndPay/get\_emi\_checkout_details>      |

## Request Parameters

### Header

The request header contains the following fields:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "Date  \n**mandatory**",
    "0-1": "The date and time should be in the GMT time conversion(not the IST). For example, current time in India is 18:00:00 IST, the time in the date header should be 12:30:00 GMT.",
    "0-2": "Thu, 17 Feb 2022 08:17:59 GMT",
    "1-0": "Digest  \n**mandatory**",
    "1-1": "Base 64 encode of (sha256 hash of the JSON data (post to server).",
    "1-2": "`vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=`",
    "2-0": "Authorization  \n**mandatory**",
    "2-1": "This field is in the following format:  \n`hmac username=\"smsplus\", algorithm=\"hmac-sha512\", headers=\"date digest\", signature=\"CkGfgbho69uTMMOGU0mHWf+1CUAlIp3AjvsON9n9/E4=\"`  \nWhere the above format includes the following:  \n  \n- **username**: The merchant key of the merchant.\n- **algorithm**: This must have the value as **hmac-sha512** that is used for this API\n- **headers**: This must have the value as **date digest**\n- **signature**: This must contain the hmacsha512 of (signing\\_string, merchant\\_secret), where:\n  - **signing\\_string**: This is in the \"**Date**\"+\"\\\\n\"+\"**Digest**\" format. Here, the Date and Digest is the same values in the fields listed in this table For example, \"Thu, 17 Feb 2022 08:17:59 GMT\"\"\\\\n\"+“vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=“\n  - **merchant\\_secret**: The merchant Salt of the merchant. For more information on getting the merchant Salt, refer to [Generate Merchant Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard)",
    "2-2": " hmac username=\"smsplus\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI=\"",
    "3-0": "platformId  \n**mandatory**",
    "3-1": "This field contains the platform ID and include the value as **1**.",
    "3-2": "1"
  },
  "cols": 3,
  "rows": 4,
  "align": [
    null,
    null,
    null
  ]
}
[/block]

#### Required parameters for calculating authorization

- Date
- Authorization

The following sample Java code contains the logic used to encrypt as described in the above table:

```javascript
// date
var date = new Date();
// var date = "Wed, 28 Jun 2023 11:25:19 GMT";
date = date.toUTCString();
 
// authorization
var authorization = getAuthHeader(date);
console.log(authorization);
 
function getAuthHeader(date) {
    var AUTH_TYPE = 'sha512';
    var data = isEmpty(request['data'])?"":request['data'];
    var hash_string = data + '|' + date + '|' + pm.variables.get("merchantSalt");
    console.log("Hash String is ", hash_string);
    var hash = CryptoJS.SHA512(hash_string).toString(CryptoJS.enc.Hex);
    var authHeader = 'hmac username="' + pm.variables.get("merchantKey") + '", ' + 'algorithm="' + AUTH_TYPE + '", headers="date", signature="' + hash + '"'
    return authHeader;
}
 
pm.environment.set('date', date);
pm.environment.set('authorization', authorization);
 
function isEmpty(obj) {
    for(var key in obj) {
        if(obj.hasOwnProperty(key))
        return false;
    }
    return true;
}
```

### Body parameters

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "Key   \n`mandatory`",
    "0-1": "`String` The merchant key provided by PayU.   \n**Reference**: For more information on how to generate the Key and Salt, refer to any of the following:  \n  \n- **Production**: [Generate Production Merchant Key and Sat](https://docs.payu.in/docs/generate-merchant-key-and-salt-on-payu-dashboard). \n- **Test**: [Generate Test Merchant Key and Salt](https://docs.payu.in/docs/generate-test-merchant-key-and-salt).",
    "0-2": "Your Test Key",
    "1-0": "requestId   \n`mandatory`",
    "1-1": "`String `This parameter must contain the unique ID for making an eligibility request.",
    "1-2": "Test1234",
    "2-0": "amount   \n`mandatory`",
    "2-1": "`String`The transaction amount for which the eligibility is checked is to be passed here",
    "2-2": "{\"amount\":\"10000\"}",
    "3-0": "pg `\nmandatory`",
    "3-1": "`String`It defines the payment category using the Merchant Hosted Checkout integration. For a BNPL payment, \"BNPL\" must be specified in the **pg** parameter.",
    "3-2": "BNPL",
    "4-0": "Bankcode   \n`mandatory`",
    "4-1": "`String`The merchant must post this parameter with the corresponding payment option’s bank code value in it. For the list of bankcodes for BNPL, refer to [BNPL Codes](https://docs.payu.in/docs/bnpl-codes). <br><br>In future, wallet options will also be added.",
    "4-2": "LAZYPAY",
    "5-0": "phone  \n`mandatory`",
    "5-1": "`String`This parameter must contain the customer’s phone number for which the eligibility is to be checked needs to be passed",
    "5-2": "“9999999999”",
    "6-0": "payuToken  \n`optional`",
    "6-1": "`String`This parameter must contain is the PayU instrument token for saved card.",
    "6-2": "Token12345  <br><br>Note: One or multiple payu tokens can be passed and max 10 tokens supported in a request.",
    "7-0": "userCredentials  \n`optional`",
    "7-1": "`String`This parameter must contain an unique user credential mapped against each user, to be passed by the merchant for saved card.",
    "7-2": "abc:xyz"
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

## Sample request

```
curl --location 'https://test.payu.in/info/linkAndPay/get_emi_checkout_details' \
--header 'x-credential-username: smsplus' \
--header 'Content-Type: application/json' \
--header 'authorization: hmac username="x0i6r2", algorithm="sha512", headers="date", signature="0e0ebc518c085d8ff49058b7c232bfe2e8779e9e9cafd34a4cdf1c11114035eea75b0e404a9b9e152757dbcc4926f78b6f18ba7f6643e2bf687a65942d3bde38"' \
--header 'date: Mon, 28 Oct 2024 10:34:49 GMT' \
--data '{
    "amount": 2000000,
    "userCredentials": "aaa:bbb",
    "phone": "9560012582",
    "bankCode": null,
    "payuToken": null
}'
```

> 📘 Authorization calculation logic:
> 
> For authorization calculation logic, refer to[ Required parameters for calculating authorization](#required-parameters-for-calculating-authorization).

## Sample response

### Success scenario

```
{
   "bnpl":{
      "all":[
         {
            "Lazypay":{
               "status":1,
               "kfsLink":"https://",
               "eligible":true,
               "customerLinked":true,
               "PayuToken":"Token12345"
            },
            "Simpl":{
               "status":1,
               "availableBalance":500,
               "kfsLink":"https://",
               "eligible":true,
               "customerLinked":true,
               "PayuToken":"Token78901"
            }
         }
      ]
   }
}
```

### Failure scenario

- Customer eligible but not linked

```
{
  "bnpl": {
    "all": {
      "Lazypay": {
        "status": 1,
        "kfsLink": "https://www.somekfsLink.com",
        "eligible": true,
        "customerLinked": false
      }
    }
  }
}
```

- Customer not eligible

```
{
  "Lazypay": {
    "status": 1,
    "eligible": false, // based on amount and not to return available balance if eligible is false
    "customerLinked": false,
    "failure_code": "E2408",
    "failure_reason": "The transaction or loan amount is greater than the available credit line with the customer"
  }
}
```