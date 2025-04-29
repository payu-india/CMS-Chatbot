---
title: Order Fulfillment API
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
To avail risk-based authentication services for international card transactions, e-commerce merchants need to pass some data points for our risk engines to detect and prevent fraud efficiently. 

Merchants need to pass details around order fulfillment by integrating the **Order Fulfillment** API. This API needs to be invoked when order fulfillment is triggered.

**Environment**

|            |                                            |
| :--------- | :----------------------------------------- |
| Test       | <https://apitest.payu.in/v1/order/fulfill> |
| Production | <https://api.payu.in/v1/order/fulfill>     |

**HTTP Method**: POST

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
    "2-1": "This field is in the following format:  \n`hmac username=\"smsplus\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"CkGfgbho69uTMMOGU0mHWf+1CUAlIp3AjvsON9n9/E4=\"`  \nWhere the above format includes the following:  \n  \n- **username**: The merchant key of the merchant.\n- **algorithm**: This must have the value as **hmac-sha256** that is used for this API\n- **headers**: This must have the value as **date digest**\n- **signature**: This must contain the hmacsha256 of (signing\\_string, merchant\\_secret), where:\n  - **signing\\_string**: This is in the \"**Date**\"+\"\\\\n\"+\"**Digest**\" format. Here, the Date and Digest is the same values in the fields listed in this table For example, \"Thu, 17 Feb 2022 08:17:59 GMT\"\"\\\\n\"+“vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=“\n  - **merchant\\_secret**: The merchant Salt of the merchant. For more information on getting the merchant Salt, refer to [Generate Merchant Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard)",
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

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": " **sample**",
    "0-0": "id  \n`mandatory`",
    "0-1": "_String_ This parameter must contain the PayU ID of order.",
    "0-2": "12345",
    "1-0": "fulfillments  \n`mandatory`",
    "1-1": "_Object_ This parameter must contain the nested object containing fulfillment details for order as described in the [fulfillments object fields description](#fulfillments-object-fields-description).",
    "1-2": ""
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### fulfillments object fields description

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": " **sample**",
    "0-0": "fulfillment\\_id  \n`mandatory`",
    "0-1": "_String_ This parameter must contain the unique ID for fulfilment.",
    "0-2": "COC78FRQ7DR",
    "1-0": "created\\_at  \n`mandatory`",
    "1-1": "_String_ This parameter must contain the Timestamp when fulfilment is created.",
    "1-2": "2021-08-05T09:12:25.877Z",
    "2-0": "status  \n`mandatory`",
    "2-1": "_String_ This parameter must contain the status of fulfilment.",
    "2-2": "success/cancelled/error",
    "3-0": "tracking\\_company  \n`mandatory`",
    "3-1": "_String_ This parameter must contain the logistics partner for fulfilment.",
    "3-2": "fedex",
    "4-0": "tracking\\_number  \n`mandatory`",
    "4-1": "_String_ This parameter must contain the tracking number for order",
    "4-2": "abc123",
    "5-0": "tracking\\_urls  \n`mandatory`",
    "5-1": "_String_ This parameter must contain the tracking URL",
    "5-2": "<http://fedex.com/track?q=abc123>"
  },
  "cols": 3,
  "rows": 6,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Sample request

```curl
curl --location 'https://apitest.payu.in/v1/order/fulfill' \
--header 'Date: Mon, 22 Jul 2024 20:56:50 GMT' \
--header 'Digest: GklVzEXuTEYaTTMks0K1RUVBxdS/mrszfFHCYvlNKJY=' \
--header 'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="UkLDTaJnnyLbyj5Uj4jxRbNxD2gdmUlL6R3xrdIw/9M="' \
--header 'Content-Type: application/json' \
--data '{
 "merchant_id": "8669648",
  "order": 
  {
    "id": "19705182705",
    "fulfillments":[
      {
        "fulfillment_id": "COC78FRQ7DR",
        "created_at": "2024-07-01T03:38:14Z",
        "status": "success",
        "tracking_company": "FEDEX", 
        "tracking_numbers": "12345",
        "tracking_urls": "www.fedex.com/package=12345",
        "message": "put at the front door" 
      }
    ]
  }
}'
```

<br />

## Sample response

### Success scenario

```
{
    "code": 200,
    "message": "fulfillment status updated successfully",
    "result": {
        "empty": false
    }
}
```

### Failure scenario

- Bad request

```
{
    "code": 400,
    "message": "Invalid status"
}
```

- Internal server error

```
{
    "code": 500,
    "message": "Interal Server Error"
}
```