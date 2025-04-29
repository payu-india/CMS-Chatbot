---
title: Save Card BIN Info API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Save Card BIN Info API
  description: >-
    The Save Card BIN API helps determine whether CVV needs to be collected for
    saved card transactions. It provides request headers, parameters, and sample
    code for encryption.
  keywords:
    - Card BIN Info API
    - Save Card BIN Info API
    - Save BIN Info API
    - Card BIN information API
    - Store BIN info API
    - Card BIN information API
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: collect-payments-using-a-saved-card
      title: Collect Payments using a Saved Card
    - type: endpoint
      slug: collect-payments-save-card
      title: Collect Payments - Save Card
---
The **Save Card BIN **API () helps you determine whether CVV needs to be collected from your customers and validated or not be collected for saved card transactions.

HTTP Method: **POST**

Environment

|                            |                                            |
| -------------------------- | ------------------------------------------ |
| **Test Environment**       | <https://test.payu.in/issuing-bank/v1/bin> |
| **Production Environment** | <https://info.payu.in/issuing-bank/v1/bin> |

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
    "2-2": " hmac username=\"smsplus\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI=\""
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

## Request parameters

In addition to the [Request Headers](#request-headers) listed above, the **data** parameter is posted with the following fields are posted in an array:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "0-0": "bin",
    "0-1": "`String` The Network Token BIN or the first 9-digits of the network token is posted in this parameter.",
    "1-0": "checkCVVRequired",
    "1-1": "`Boolean` This parameter may contain any of the following:  \n   - **True**: Request the API to check if card CVV must be checked for the saved card transaction so that merchant need to validate the CVV accordingly.  \n    - **False**: Request the API not to check if card CVV need to be checked for the saved card transaction"
  },
  "cols": 2,
  "rows": 2,
  "align": [
    null,
    null
  ]
}
[/block]


## Sample request

```curl
curl --location 'https://info.payu.in/issuing-bank/v1/bin' \
--header 'Content-Type: application/json' \
--header 'Date: Thu, 01 Jun 2023 06:59:03 GMT' \
--header 'Digest: sYxiEFksDG+h+sB11nonf9ry31aKynEJ/Hmxwc6M3pM=' \
--header 'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="F8D2PW2/Q2VF7FZKiY3RKJ6+1HU5OH8/HkxvitghvP4="' \
--header 'Cookie: PHPSESSID=lf33il1bio9scn7cars1hqsf05; PHPSESSID=o7bbf6gbociqmroctldtslkc21' \
--header 'mid: 2' \
--data '{
    "bin": "512345789",
    "checkCVVRequired": true
}'
```

## Response parameters

The response involves the following parameters and the **result** parameter contains the offer results:

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "code",
    "0-1": "This parameter returns the status of web service call. The status can be any of the following:  \n0: If web service call failed.  \n1 : If web service call succeeded.",
    "0-2": "200",
    "1-0": "result",
    "1-1": "`JSON Object` This parameter gives the information about the result of the API response in a JSON format. For more information, refer to the [result Field JSON Details](#result-parameter-json-details) subsection.",
    "1-2": "Refer to the [result Field JSON Details](#result-parameter-json-details) subsection."
  },
  "cols": 3,
  "rows": 2,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


### result parameter JSON details

The **result** parameter contains the result in a JSON format and the fields in the JSON are described in the following table:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "status",
    "0-1": "This parameter returns the status of card. The status can be any of the following:",
    "0-2": "1",
    "1-0": "category",
    "1-1": "This field contains the card category of the card.",
    "1-2": "debitcard",
    "2-0": "bin",
    "2-1": "`Integer` This field contains the first 9-digits of the card or Network Token.",
    "2-2": "512345789",
    "3-0": "cvvLessSupported",
    "3-1": "This field contains any of the following values:  \n   - **true**: The card does not require CVV validation  \n   - **false** : The card requires CVV validation.",
    "3-2": "true",
    "4-0": "is\\_domestic",
    "4-1": "`Boolean` This field contains any of the following values:  \n   - **true**: The card is domestic card  \n   - **false** : The card is an international card or issued outside India",
    "4-2": "true",
    "5-0": "card\\_type",
    "5-1": "This field contains the card type or the card network.",
    "5-2": "VISA",
    "6-0": "issuing\\_bank",
    "6-1": "This field contains the card issuing bank.",
    "6-2": "HDFC",
    "7-0": "otp\\_on\\_fly",
    "7-1": "This field contains any of the following values:  \n   - **true**: The OTP needs to be entered by the customer when redirected  \n   - **false** : The customer need not enter the OTP to validate the card",
    "7-2": "false",
    "8-0": "is\\_atmpin\\_card",
    "8-1": "This field contains any of the following values:  \n   - **0**: The card is not an ATM card  \n   - **1**: The card is an ATM card",
    "8-2": "0"
  },
  "cols": 3,
  "rows": 9,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


## Sample response

### Success scenario

```plaintext
{    
 "message": "Success",    
 "status": 1,    
 "result": 
 {        
   "status": 0,      
   "category": "debitcard",        
   "bin": "401151",        
   "cvvLessSupported": false,        
   "is_domestic": true,        
   "card_type": "VISA",        
   "issuing_bank": "HDFC",        
   "otp_on_fly": true,        
   "is_atmpin_card": 1    
  }
}
```