---
title: 'v2 Refund Transaction API '
deprecated: false
hidden: true
metadata:
  robots: index
---
The Refund Transaction API allows merchants to initiate refunds for transactions. It is functionally similar to the Cancel Refund Transaction API, but is maintained only for backward compatibility with existing integrations. This API is not exposed to new merchants, who are directed to use the Refund Initiate API instead. The v2 API offers enhanced functionality and improved response formats compared to the v1 API.

### Endpoint

```
POST /v1/transaction
```

### Request Headers

The request header contains the following fields:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Date
        `mandatory`
      </td>

      <td>
        The date and time should be in the GMT time conversion(not the IST). For example, current time in India is 18:00:00 IST, the time in the date header should be 12:30:00 GMT.
      </td>

      <td>
        Thu, 17 Feb 2022 08:17:59 GMT
      </td>
    </tr>

    <tr>
      <td>
        Digest
        `mandatory`
      </td>

      <td>
        Base 64 encode of (sha256 hash of the JSON data (post to server).
      </td>

      <td>
        `vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=`
      </td>
    </tr>

    <tr>
      <td>
        Authorization
        **mandatory**
      </td>

      <td>
        This field is in the following format:
        `hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="CkGfgbho69uTMMOGU0mHWf+1CUAlIp3AjvsON9n9/E4="`
        Where the above format includes the following:

        * **username**: The merchant key of the merchant.
        * **algorithm**: This must have the value as **hmac-sha256** that is used for this API
        * **headers**: This must have the value as **date digest**
        * **signature**: This must contain the hmacsha256 of (signing\_string, merchant\_secret), where:
          * **signing\_string**: This is in the "**Date**"+"
            "+"**Digest**" format. Here, the Date and Digest is the same values in the fields listed in this table For example, "Thu, 17 Feb 2022 08:17:59 GMT""
            "+"vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0="
          * **merchant\_secret**: The merchant Salt of the merchant. For more information on getting the merchant Salt, refer to [Generate Merchant Key and Salt on PayU Dashboard](https://docs.payu.in/v1/docs/generate-merchant-key-and-salt-on-payu-dashboard)
      </td>

      <td>
        hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI="
      </td>
    </tr>

    <tr>
      <td>
        platformId\
        `mandatory`
      </td>

      <td>
        This field contains the platform ID and include the value as **1**.
      </td>

      <td>
        1
      </td>
    </tr>
  </tbody>
</Table>

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

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key
        `mandatory`
      </td>

      <td>
        Merchant key for authentication
      </td>

      <td>
        `iDJYfd`
      </td>
    </tr>

    <tr>
      <td>
        mihpayid
        `mandatory`
      </td>

      <td>
        PayU transaction ID (also called PayU ID)
      </td>

      <td>
        `999091000003794`
      </td>
    </tr>

    <tr>
      <td>
        request
        `mandatory`
      </td>

      <td>
        JSON string containing additional parameters
      </td>

      <td>
        See JSON Fields below
      </td>
    </tr>
  </tbody>
</Table>

### JSON Fields in the `request` Parameter:

| Parameter                          | Description                                                 | Example           |
| ---------------------------------- | ----------------------------------------------------------- | ----------------- |
| txn\_mode<br />`mandatory`         | Transaction refund mode (must be 1 for Source)              | `1`               |
| token<br />`mandatory`             | Unique token for the refund transaction                     | `11358998`        |
| amount<br />`mandatory`            | The specific amount that needs to be refunded               | `0.21`            |
| refundDetails<br />`optional`      | Additional details for the refund                           | `{}`              |
| refundSplitRequest<br />`optional` | JSON object containing refund split details (if applicable) | See example below |

### Sample Request

```bash
curl --location 'http://localhost:8085/apilayer/v2/refund/secure' \
--header 'Content-Type: application/json' \
--header 'mid: 8006653' \
--header 'Date: Thu, 17 Feb 2022 08:17:59 GMT' \
--header 'Digest: vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=' \
--header 'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI="' \
--header 'platformId: 1' \
--data '{
    "mihpayId": "999000000000478",
    "refundToken": "abbv98vqw",
    "amount": 0.1,
    "refundDetails": {},
    "refundSplitRequest": {
        "33rOiT": {
            "amount": 0.21
        }
    }
}'
```

### Response Parameters

| Parameter   | Description                                                        | Example                     |
| ----------- | ------------------------------------------------------------------ | --------------------------- |
| status      | Indicates success (1) or failure (0) of the refund request         | `1`                         |
| statusCode  | Numeric code representing the status of the refund request         | `102`                       |
| message     | Descriptive message about the status of the refund request         | `"Refund request accepted"` |
| payuId      | Unique PayU transaction ID for which the refund was processed      | `999091000003794`           |
| refundToken | Unique token identifying the refund request                        | `11358934598`               |
| requestId   | Unique identifier for the refund request (if available)            | `4993824108552`             |
| refundId    | Unique identifier for the refund transaction (if successful)       | `123456789`                 |
| splitInfo   | Contains details of refunds for split transactions (if applicable) | See JSON example            |

### Sample Response

#### Success Response

```json
{
  "status": 1,
  "statusCode": 102,
  "message": "Refund request accepted",
  "refundId": "123456789"
}
```

#### Failure Response

```json
{
  "status": 0,
  "errorcode": "4000",
  "message": "Refund request rejected"
}
```