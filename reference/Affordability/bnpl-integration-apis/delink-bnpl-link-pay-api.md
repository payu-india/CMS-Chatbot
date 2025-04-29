---
title: Delink BNPL Link & Pay API
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

|                        |                                                         |
| ---------------------- | ------------------------------------------------------- |
| Test Environment       | <https://test.payu.in/info/linkAndPay/delinkInstrument> |
| Production Environment | <https://info.payu.in/linkAndPay/delinkInstrument>      |

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


**Required parameters for calculating authorization**

- Date
- Authorization

The following sample Java code contains the logic used to encrypt as described in the above table:

```java
package com.payu.apilayer.util;

import com.google.gson.Gson;
import com.google.gson.JsonObject;
import org.joda.time.DateTime;
import org.joda.time.format.DateTimeFormat;

import java.math.BigInteger;
import java.security.InvalidKeyException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class HmacAuth {

    public static JsonObject getRequestBody(){
        JsonObject requestJson = new JsonObject();
        requestJson.addProperty("udf1","123");
        return requestJson;
    }

    public static String getSha512Hash(String hashString) {
        {
            try {
                MessageDigest md = MessageDigest.getInstance("SHA-512");
                byte[] messageDigest = md.digest(hashString.getBytes());
                BigInteger signumBytes = new BigInteger(1, messageDigest);
                String hashtext = signumBytes.toString(16);
                while (hashtext.length() < 32) {
                    hashtext = "0" + hashtext;
                }
                return hashtext;
            }
            catch (NoSuchAlgorithmException e) {
                throw new RuntimeException(e);
            }
        }
    }

    public static void main(String[] args) throws NoSuchAlgorithmException, InvalidKeyException {
        String key = "smsplus";
        String secret = "admin";
        Gson gson = new Gson();
        String date = DateTimeFormat.forPattern("EEE, dd MMM yyyy HH:mm:ss 'GMT'").withZoneUTC().print(new DateTime());
        System.out.println(date);
        JsonObject requestJson = getRequestBody();
        String hashString = new StringBuilder()
                .append(gson.toJson(requestJson))
                .append("|")
                .append(date)
                .append("|")
                .append(secret).toString();
        System.out.println("Hash String is " + hashString);
        String hash = getSha512Hash(hashString);
        String authorization = new StringBuilder()
                .append("hmac username=\"")
                .append(key)
                .append("\", algorithm=\"sha512\", headers=\"date\", signature=\"")
                .append(hash)
                .append("\"").toString();
        System.out.println(authorization);
    }
}

```

### Body parameters

> 📘 Note:
> 
> You can use any of the following combination of the mandatory parameters apart from requestId and amount:
> 
> - pg+bankcode+user_credentials
> - payuToken+user_credentials

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "requestId   \n`mandatory`",
    "0-1": "`String `This parameter must contain the unique ID for making an eligibility request.",
    "0-2": "Test1234",
    "1-0": "amount   \n`mandatory`",
    "1-1": "`String`The transaction amount for which the eligibility is checked is to be passed here",
    "1-2": "{\"amount\":\"10000\"}",
    "2-0": "pg `\nmandatory`",
    "2-1": "`String`It defines the payment category using the Merchant Hosted Checkout integration. For a BNPL payment, \"BNPL\" must be specified in the **pg** parameter. This parameter must used in combination with **bankcode** and **user_credentials**. For more information, refer to sample request [With pg, bankcode and user_credentials](#pg-bankcode-and-user-credentials) ",
    "2-2": "BNPL",
    "3-0": "bankcode   \n`mandatory with pg`",
    "3-1": "`String`The merchant must post this parameter with the corresponding payment option’s bank code value in it. For the list of bankcodes for BNPL, refer to [BNPL Codes](https://docs.payu.in/docs/bnpl-codes).   \nThis parameter is mandatory when used in combination with **pg** and **user_credentials**. For more information, refer to [With pg, bankcode and user_credentials](#pg-bankcode-and-user-credentials)  [Sample request](#sample-request)  .",
    "3-2": "LAZYPAY",
    "4-0": "phone  \n`mandatory`",
    "4-1": "`String`This parameter must contain the customer’s phone number for which the eligibility is to be checked needs to be passed",
    "4-2": "“9999999999”",
    "5-0": "payuToken  \n`mandatory`",
    "5-1": "`String`This parameter must contain is the PayU instrument token for saved card. This parameter must used in combination with **user_credentials**. For more information, refer to  [With payuToken and user_credentials](#with-payuToken-and-user_credentials) under  [Sample request](#sample-request)  .",
    "5-2": "Token12345  <br><br>Note: One or multiple payu tokens can be passed and max 10 tokens supported in a request.",
    "6-0": "user_credentials  \n`mandatory`",
    "6-1": "`String`This parameter must contain an unique user credential mapped against each user, to be passed by the merchant for saved card.or more information, refer to [Sample request](#sample-request) .",
    "6-2": "abc:xyz",
    "7-0": "key   \n`optional`",
    "7-1": "`String` The merchant key provided by PayU.   \n**Reference**: For more information on how to generate the Key and Salt, refer to any of the following:  \n  \n- **Production**: [Generate Production Merchant Key and Sat](https://docs.payu.in/docs/generate-merchant-key-and-salt-on-payu-dashboard). \n- **Test**: [Generate Test Merchant Key and Salt](https://docs.payu.in/docs/generate-test-merchant-key-and-salt).",
    "7-2": "Your Test Key"
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

### With pg, bankcode and user_credentials

```
curl --location 'https://test.payu.in/info/linkAndPay/delinkInstrument' \
--header 'Content-Type: application/json' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="55266f0988fbd42114f9d36c395c6cb32ec27b86d204ac06b2e7e580cf1a62b24dc30c987a37f03d628b14f3c7df5950eb513d560f048daa5627a6aeae79fe59"' \
--header 'date: Tue, 14 Jan 2025 10:03:47 GMT' \
--data '{
    "requestId": 12233,
    "pg": "BNPL",
    "bankcode": "LAZYPAY",
    "phone": "9999999999",
    "userCredentials": "abc:xyz"
} ' 

```

### With payuToken and user_credentials

```
curl --location 'https://test.payu.in/info/linkAndPay/delinkInstrument' \
--header 'Content-Type: application/json' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="56cb0e25b6ed0343440946a839db97d9c55c8bc69917611d350ac64b040cd1931a5b3a002bbd7a291d40d5072072a1a8021465616a66d8a32cea71c0b84ed03b"' \
--header 'date: Tue, 14 Jan 2025 10:17:13 GMT' \
--data '{
    "requestId": 12233,
    "phone": "9999999999",
    "payuToken": "beba5b1bb841945c2d881",
    "userCredentials": "abc:xyz"
}'
```

## Sample response

### Success scenario

```
{ 
  "msg": "Instrument deleted", 
  "status": "SUCCESS" 
}
```

### Failure scenario

### User not found

```
{ 
"msg": "User not found", // when user cannot be found uniquely found corresponding to the token and user credentials combination
"status": “FAILURE”
}

```

### Instrument already deleted

```
{ 
"msg": "Instrument already deleted", // when payment instrument has already been deleted against a user
"status": “FAILURE”
}

```

### Instrument not found

```
{ 
"msg": "Instrument not found", // when payment instrument cannot be found uniquely found corresponding to the token and user credentials combination
"status": “FAILURE”
}
```