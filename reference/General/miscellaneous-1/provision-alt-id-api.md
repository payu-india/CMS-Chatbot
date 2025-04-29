---
title: Provision Alt ID API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Provision Alt ID API
  description: >-
    The document provides information on the Provision Alt ID API used to
    provision Alt ID from PayU for transactions outside PayU, including request
    parameters, sample request and response, and Java code for encryption.
  keywords:
    - Provision Alt ID API
    - ' Alt ID Provisioning API'
  robots: index
next:
  description: ''
---
The **Provision Alt ID API** is used to provision Alt ID from PayU, but process transaction outside PayU. This section describes the request parameters with sample request and response.

HTTP Method: **POST**

**Environment**

|            |                                      |
| :--------- | :----------------------------------- |
| Production | <https://apitest.payu.in/card/altid> |

## Request Headers

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

## Request Parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "clientReferenceId  \n**optional**",
    "0-1": "The alphanumeric value to track the request.",
    "0-2": "DKSAI80033U2BRRE90FD0SDJAOSA",
    "1-0": "cardNumber  \n**mandatory**",
    "1-1": "The card number entered by the customer.",
    "1-2": "XXXXXXXXXXXX3669",
    "2-0": "nameOnCard  \n**optional**",
    "2-1": "The name on card entered by the customer.",
    "2-2": "Ashish K",
    "3-0": "cardType  \n**optional**",
    "3-1": "The type card used by the customer.",
    "3-2": "AMEX",
    "4-0": "expiryMonth  \n**mandatory**",
    "4-1": "The expiry date of card entered by the customer.",
    "4-2": "12",
    "5-0": "expiryYear  \n**mandatory**",
    "5-1": "The expiry year of the card entered by the customer.",
    "5-2": "26",
    "6-0": "cvv  \n**mandatory**",
    "6-1": "The CVV or secret code found behind the cardentered by the customer.",
    "6-2": "000",
    "7-0": "mail  \n**optional**",
    "7-1": "The mail ID of the customer.",
    "7-2": "[testmail@test.com](mailto:testmail@test.com)",
    "8-0": "amount  \n**mandatory**",
    "8-1": "The amount of the transaction.",
    "8-2": "100",
    "9-0": "authenticationCode  \n**conditional**",
    "9-1": "The authentication code for the transaction.  \n**Note**: This parameter is required for RUPAY cards.",
    "9-2": " "
  },
  "cols": 3,
  "rows": 10,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


## Sample Request

```curl
curl --location --request POST 'https://apitest.payu.in/card/altid' \
--header 'Content-Type: application/json' \
--header 'date: Fri, 12 Jan 2024 10:13:08 GMT' \
--header 'digest: n6XDOH1fAUrD+WC47SFsa+mNxmm1+yTrUAupmxbYMoc=' \
--header 'authorization: hmac username="DGy1hY", algorithm="hmac-sha256", headers="date digest", signature="FBp5QsOIxBzxyDnRXPCt76htkdm5ijc4nm/Hvyvaw/s="' \
--data-raw '{
    "clientReferenceId": null,
    "cardNumber": "5299920970259709",
    "nameOnCard": "Jagadesh Reddy",
    "cardType": "MAST",
    "expiryMonth": "06",
    "expiryYear": "2024",
    "cvv": "000",
    "mail": "jagadesh@reddy.com",
    "amount": "100",
    "authenticationCode": null
}'
```

## Response Parameters

| **Parameter**       | **Value**                                        |
| ------------------- | ------------------------------------------------ |
| statusCode          | TK0000, INV001, ONB001, TK0002                   |
| status              | 0(failure), 1(success)                           |
| clientReferenceId   | Same id sent in request                          |
| cryptogram          | Cryptogram details                               |
| altIdToken          | ALT ID                                           |
| expiryMonth         | Expiry month of AltId Token                      |
| expiryYear          | Expiry year of AltId Token                       |
| las4                | Last 4 digits of the card                        |
| par                 | Payment Account Reference(Unique Id of the card) |
| msg                 | Success or failure message                       |
| errorDesc           | Error description                                |
| errorMsgFromNetwork | Message received from the network                |

## Sample Response

### Success Scenario

```plaintext
{
    "statusCode": "EA01",
    "status": 1,
    "clientReferenceId": "339c6c458ac3161da90839",
    "tokenReferenceId": "018b90aa-b9c5-41c0-8528-71dd22b6b65e",
    "cryptogram": "IjDso7oA5xFBdiOd/m035meW5UpImrSRAXWMe7406m0=",
    "altInfo": {
        "altIdToken": "3612143521818338",
        "expiryMonth": "09",
        "expiryYear": "2026",
        "last4": "6622"
    },
    "msg": "AltID created successful",
    "par": "799F3ED865F5965CC760A32682BA8A80F19E99ECB3F7F03574C14F5B6C3EB2C1"
}
```

### Failure Scenarios

- Invalid card number

```
{
    "statusCode": "EA02",
    "errorDesc": "CardNo is Invalid. Please check and initiate again",
    "status": 0
}
```

- Invalid expiry month of card

```
{
    "statusCode": "EA02",
    "errorDesc": "Expiry year is Invalid. Please check and initiate again",
    "status": 0
}
```

- Invalid CVV specified for card

```
{
    "statusCode": "EA02",
    "errorDesc": "CVV is Invalid. Please check and initiate again",
    "status": 0
}
```

- Internal error

```
{
    "statusCode": "EA03",
    "errorDesc": "Technical error. Please try again",
    "status": 0,
    "clientReferenceId": "6751c7ca1365415b6b0a"
}
```

- Invalid Acquired Merchant ID

```
{
    "statusCode": "EA04",
    "errorDesc": "Invalid merchant ID configuration. Please reachout to PayU support team",
    "status": 0,
    "clientReferenceId": "6b831fb451717be74130"
}
```

- Card Network Failure
  ```
  {
      "statusCode": "EA05",
      "errorDesc": "Card network seems to be down. Please retry after some time",
      "status": 0,
      "clientReferenceId": "6700ac2393ec5091af75"
  }
  ```

- Invalid Authentication Code (RUPAY)
  ```
  {
      "statusCode": "EA06",
      "errorDesc": "Invalid auth code configuration. Please raise this to PayU support team",
      "status": 0,
      "clientReferenceId": "6bf002e42595130f3b5d"
  }
  ```

- Invalid AcquirerInstance id Code (MASTER)
  ```
  {
      "statusCode": "EA07",
      "errorDesc": "Invalid Acq ID Code configuration. Please raise this to PayU support team",
      "status": 0,
      "clientReferenceId": "6c3d6d35a5982a3d9637"
  }
  ```

- Merchant Not Onboarded(AMEX)
  ```
  {
      "statusCode": "EA09",
      "errorDesc": "Invalid merchant ID configuration. Please reach out to PayU support team",
      "status": 0,
      "clientReferenceId": "85096f63e4366f9d199"
  }
  ```

- Merchant Invalid Or Merchant AltId is InActive
  ```
  {
      "statusCode": "EA10",
      "errorDesc": "The MID is not active. Please raise this to PayU support team",
      "status": 0
  }
  ```