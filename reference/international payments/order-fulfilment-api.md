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
| Test       | \<https://apitest.payu.in/v1/order/fulfill> |
| Production | \<https://api.payu.in/v1/order/fulfill>     |

**HTTP Method**: POST

## Request headers

The request header contains the following fields:

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Date<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The date and time should be in the GMT time conversion(not the IST). For example, current time in India is 18:00:00 IST, the time in the date header should be 12:30:00 GMT.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Thu, 17 Feb 2022 08:17:59 GMT</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Digest<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Base 64 encode of (sha256 hash of the JSON data (post to server).</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=</code></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Authorization<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field is in the following format:<br><code>hmac username=&quot;smsplus&quot;, algorithm=&quot;hmac-sha256&quot;, headers=&quot;date digest&quot;, signature=&quot;CkGfgbho69uTMMOGU0mHWf+1CUAlIp3AjvsON9n9/E4=&quot;</code><br>Where the above format includes the following:  </p>
<ul>
<li><strong>username</strong>: The merchant key of the merchant.</li>
<li><strong>algorithm</strong>: This must have the value as <strong>hmac-sha256</strong> that is used for this API</li>
<li><strong>headers</strong>: This must have the value as <strong>date digest</strong></li>
<li><strong>signature</strong>: This must contain the hmacsha256 of (signing_string, merchant_secret), where:<ul>
<li><strong>signing_string</strong>: This is in the &quot;<strong>Date</strong>&quot;+&quot;\n&quot;+&quot;<strong>Digest</strong>&quot; format. Here, the Date and Digest is the same values in the fields listed in this table For example, &quot;Thu, 17 Feb 2022 08:17:59 GMT&quot;&quot;\n&quot;+“vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=“</li>
<li><strong>merchant_secret</strong>: The merchant Salt of the merchant. For more information on getting the merchant Salt, refer to <a href="doc:generate-merchant-key-and-salt-on-payu-dashboard">Generate Merchant Key and Salt on PayU Dashboard</a></li>
</ul>
</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> hmac username=&quot;smsplus&quot;, algorithm=&quot;hmac-sha256&quot;, headers=&quot;date digest&quot;, signature=&quot;zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI=&quot;</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


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

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"> <strong>sample</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>id<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><em>String</em> This parameter must contain the PayU ID of order.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>12345</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>fulfillments<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><em>Object</em> This parameter must contain the nested object containing fulfillment details for order as described in the <a href="#fulfillments-object-fields-description">fulfillments object fields description</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


### fulfillments object fields description

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"> <strong>sample</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>fulfillment_id<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><em>String</em> This parameter must contain the unique ID for fulfilment.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>COC78FRQ7DR</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>created_at<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><em>String</em> This parameter must contain the Timestamp when fulfilment is created.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2021-08-05T09:12:25.877Z</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>status<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><em>String</em> This parameter must contain the status of fulfilment.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>success/cancelled/error</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>tracking_company<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><em>String</em> This parameter must contain the logistics partner for fulfilment.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>fedex</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>tracking_number<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><em>String</em> This parameter must contain the tracking number for order</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>abc123</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>tracking_urls<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><em>String</em> This parameter must contain the tracking URL</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="http://fedex.com/track?q=abc123">http://fedex.com/track?q=abc123</a></p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


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