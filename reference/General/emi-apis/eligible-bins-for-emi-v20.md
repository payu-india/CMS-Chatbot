---
title: Eligible BINs for EMI API v2.0
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: EMI Eligibility Check API v2.0
  description: >-
    The Eligible Bin for EMI API v2.0 is used to determine EMI eligibility for
    PayU merchants based on card bin and bank selection, providing minimum
    eligible amounts for specific banks.
  keywords:
    - Check EMI eligibility API version 2.0
    - ' EMI Eligibility Check API v2.0'
  robots: index
next:
  description: ''
---
The Eligible Bin for EMI API v2.0 is used only when the merchant needs the EMI feature of PayU. If you are managing card details on your website, this API can tell the issuing bank of the card bin. It also provides the minimum eligible amount for a particular bank.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2eaac64-emi_eligible_bins_flow.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


HTTP Method: **POST**

<GENERALAPIsEnvironment />

You can post a request using any of the following methods:

- [Request without bank selection](#request-without-bank-selection)
- [Request with bank selection](#request-with-bank-selection)

## Request headers

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
    "2-1": "This field is in the following format:  \n`hmac username=\"smsplus\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"CkGfgbho69uTMMOGU0mHWf+1CUAlIp3AjvsON9n9/E4=\"`  \nWhere the above format includes the following:  \n- **username**: The merchant key of the merchant.  \n- **algorithm**: This must have the value as **hmac-sha256** that is used for this API  \n- **headers**: This must have the value as **date digest**  \n- **signature**: This must contain the hmacsha256 of (signing\\_string, merchant\\_secret), where:  \n  - **signing\\_string**: This is in the \"**Date**\"+\"\\\\n\"+\"**Digest**\" format. Here, the Date and Digest is the same values in the fields listed in this table For example, \"Thu, 17 Feb 2022 08:17:59 GMT\"\"\\\\n\"+“vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=“  \n  - **merchant\\_secret**: The merchant Salt of the merchant. For more information on getting the merchant Salt, refer to [Generate Merchant Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard)",
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


The following sample Java code contains the logic used to encrypt as described in the above table:

```java
import com.google.gson.Gson;
import com.google.gson.JsonObject;
import org.apache.commons.codec.binary.Base64;
import org.joda.time.DateTime;
import org.joda.time.format.DateTimeFormat;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.security.InvalidKeyException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class HmacAuth {

    public static String getSha256(String input) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] digest = md.digest(input.getBytes());
            return Base64.encodeBase64String(digest);
        } catch (NoSuchAlgorithmException ignored) {}
        return null;
    }

    public static JsonObject getRequestBody(){
        JsonObject requestJson = new JsonObject();
        requestJson.addProperty("firstname","John");
        requestJson.addProperty("lastname","Doe");
        return requestJson;
    }

    public static void main(String[] args) throws NoSuchAlgorithmException, InvalidKeyException {
        String key = "smsplus";
        String secret = "admin";
        Gson gson = new Gson();
        String date = DateTimeFormat.forPattern("EEE, dd MMM yyyy HH:mm:ss 'GMT'").withZoneUTC().print(new DateTime());
        System.out.println(date);
        JsonObject requestJson = getRequestBody();
        String digest = getSha256(gson.toJson(requestJson));
        System.out.println(digest);
        String signingString = new StringBuilder()
            .append("date: " + date)
            .append("\ndigest: " + digest).toString();
        Mac sha256_HMAC = Mac.getInstance("HmacSHA256");
        SecretKeySpec secret_key = new SecretKeySpec(secret.getBytes(), "HmacSHA256");
        sha256_HMAC.init(secret_key);
        String signature = Base64.encodeBase64String(sha256_HMAC.doFinal(signingString.getBytes()));
        String authorization = new StringBuilder()
            .append("hmac username=\"")
            .append(key)
            .append("\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"")
            .append(signature)
            .append("\"").toString();
        System.out.println(authorization);
    }
}
```

## Request without bank selection

### Request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "bintype  \n**mandatory**",
    "0-1": "This parameter needs can include any of the following the values:  \n   - **bin**: If you want to check on the basis of the first 6/8/9 digits of card number or network token.  \n   - **NET**: If you want to check on the basis of network token.",
    "0-2": "bin",
    "1-0": "value  \n**mandatory**",
    "1-1": "This parameter can contain any of the following:  \n   - If **bin** used in var1 parameter, the first 6/8/9 digits of card number or network token.  \n   - If **NET** used in the var1 parameter, the entire network token must be passed.",
    "1-2": "4161041969147181",
    "2-0": "amount  \n**conditional**",
    "2-1": "This parameter needs to include the transaction amount.  \n**Note**: Amount is a non-mandatory field, but is mandatory if bank code is ONEC or BAJFIN .",
    "2-2": "10000"
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


### Response parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "status",
    "0-1": "This parameter returns the status of web service call.  \nThe status can be any of the following:  \n    - 0 - If web service call failed.  \n     - 1 - If web service call succeeded",
    "0-2": "1",
    "1-0": "msg",
    "1-1": "This parameter returns whether the EMI details were fetched successfully or not found.",
    "1-2": "Details fetched successfully",
    "2-0": "details",
    "2-1": "The details of the EMI offer is displayed in a JSON format and it contains the following fields:",
    "2-2": " "
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


### Sample response

- If successfully fetched:

If successfully fetched:

```plaintext
{ 
    "message": "Details fetched successfully", 
    "status": 1, 
    "result": [ 
        { 
            "isEligible": 1, 
            "bank": "ICICI", 
            "minAmount": 1500.0 
        } 
    ] 
```

- If not found:

If not found:

```plaintext
{ 

    "message": "Details fetched successfully", 

    "status": 1, 

    "result": [ 

        { 

            "isEligible": 0, 

            "bank": "ICICI", 

            "minAmount": 1500.0 

        } 

    ] 

} 
```

## Request with bank selection

### Request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "bintype  \n**mandatory**",
    "0-1": "This parameter needs can include any of the following the values:  \n   - **bin**: If you want to check on the basis of the first 6/8/9 digits of card number or network token.  \n   - **NET**: If you want to check on the basis of network token.",
    "0-2": "bin",
    "1-0": "value  \n**mandatory**",
    "1-1": "This parameter can contain any of the following:  \n   - If **bin** used in var1 parameter, the first 6/8/9 digits of card number or network token.  \n   - If **NET** used in the var1 parameter, the entire network token must be passed.",
    "1-2": "4161041969147181",
    "2-0": "amount  \n**conditional**",
    "2-1": "This parameter needs to include the transaction amount. **Note**: Amount is a non-mandatory field, but is mandatory if bank code is ONEC or BAJFIN .",
    "2-2": "10000",
    "3-0": "bank  \n**mandatory**",
    "3-1": "This parameter contains the bank code for which the request is sent.",
    "3-2": "ICICI"
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


### Response parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "status",
    "0-1": "This parameter returns the status of web service call.  \nThe status can be any of the following:  \n    - 0 - If web service call failed.  \n     - 1 - If web service call succeeded",
    "0-2": "1",
    "1-0": "msg",
    "1-1": "This parameter returns whether the EMI details were fetched successfully or not found.",
    "1-2": "Details fetched successfully",
    "2-0": "details",
    "2-1": "The details of the EMI offer is displayed in a JSON format and it contains the following fields:  \n    - **isEligible** - This paraAny of the following values are:  \n         _.0 - If EMI offers are not available for the given card BIN.  \n         _ 1 - If EMI offers are available for the given card BIN.  \n   - **bank** - The name of bank that corresponds to the given card BIN  \n   - **minAmount** - The minimum amount for which the EMI offer is available",
    "2-2": "\"isEligible\": 0, "
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


### Sample response

#### Success scenario

Formatted JSON Response:

If successfully fetched:

```plaintext
Array
(
    [status] => 1
    [msg] => Details fetched successfully
    [details] => Array
        (
            [isEligible] => 1
            [bank] => AXIS
            [minAmount] => 2500
        )

)
```

#### Failure scenarios

- If **var3** (input bank name) does not match with the bank name in the PayU Database, the bin given in the input is of a different bank name:

```plaintext
Array (
[status] => 0
[msg] => Invalid Bin )
```

- When the BIN passed does not match with the bankName passed in the request:”

```plaintext
{
    "message": "This Card does not belong to Axis Bank Credit Card. Please make the payment via ICICI Bank Credit Card",
    "status": 0,
    "result": [
        {
            "isEligible": 0,
            "bank": "Axis"
        }
    ]
}
```