---
title: Delink BNPL Link & Pay API
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
This API is used to delink the BNPL Link & Pay that was done earlier using **\_payment** API as in the [Collect Payment API - BNPL Link & Pay](ref:collect-payment-api-bnpl-link-pay).

### Environment

|                        |                                                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Test Environment       | \<[https://test.payu.in/info/linkAndPay/delinkInstrument>](https://test.payu.in/info/linkAndPay/delinkInstrument>) |
| Production Environment | \<[https://info.payu.in/linkAndPay/delinkInstrument>](https://info.payu.in/linkAndPay/delinkInstrument>)           |

## Request Parameters

### Header

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field is in the following format:<br><code>hmac username=&quot;smsplus&quot;, algorithm=&quot;hmac-sha512&quot;, headers=&quot;date digest&quot;, signature=&quot;CkGfgbho69uTMMOGU0mHWf+1CUAlIp3AjvsON9n9/E4=&quot;</code><br>Where the above format includes the following:  </p>
<ul>
<li><strong>username</strong>: The merchant key of the merchant.</li>
<li><strong>algorithm</strong>: This must have the value as <strong>hmac-sha512</strong> that is used for this API</li>
<li><strong>headers</strong>: This must have the value as <strong>date digest</strong></li>

<li><strong>signature</strong>: This must contain the hmacsha512 of (signing_string, merchant_secret), where:<ul>
<li><strong>signing_string</strong>: This is in the &quot;<strong>Date</strong>&quot;+&quot;\n&quot;+&quot;<strong>Digest</strong>&quot; format. Here, the Date and Digest is the same values in the fields listed in this table For example, &quot;Thu, 17 Feb 2022 08:17:59 GMT&quot;&quot;\n&quot;+“vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=“</li>
<li><strong>merchant_secret</strong>: The merchant Salt of the merchant. For more information on getting the merchant Salt, refer to <a href="doc:generate-merchant-key-and-salt-on-payu-dashboard">Generate Merchant Key and Salt on PayU Dashboard</a></li>
</ul>
</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> hmac username=&quot;smsplus&quot;, algorithm=&quot;hmac-sha256&quot;, headers=&quot;date digest&quot;, signature=&quot;zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI=&quot;</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>platformId<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the platform ID and you must include the value as <strong>1</strong>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

**Required parameters for calculating authorization**

- Date
- Authorization

The following sample Java code contains the logic to be used to encrypt as described in the above table:

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

<Callout icon="📘" theme="info">
  ### Note:

  You can use any of the following combination of the mandatory parameters apart from requestId and amount:

  - pg+bankcode+user\_credentials
  - payuToken+user\_credentials
</Callout>

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>requestId <br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String </code>This parameter must contain the unique ID for making an eligibility request.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Test1234</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>amount <br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The transaction amount for which the eligibility is checked is to be passed here</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{&quot;amount&quot;:&quot;10000&quot;}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>pg <code> mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>It defines the payment category using the Merchant Hosted Checkout integration. For a BNPL payment, &quot;BNPL&quot; must be specified in the <strong>pg</strong> parameter. This parameter must used in combination with <strong>bankcode</strong> and <strong>user_credentials</strong>. For more information, refer to sample request <a href="#pg-bankcode-and-user-credentials">With pg, bankcode and user_credentials</a> </p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>BNPL</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>bankcode <br><code>mandatory with pg</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The merchant must post this parameter with the corresponding payment option’s bank code value in it. For the list of bankcodes for BNPL, refer to <a href="https://docs.payu.in/docs/bnpl-codes">BNPL Codes</a>. <br>This parameter is mandatory when used in combination with <strong>pg</strong> and <strong>user_credentials</strong>. For more information, refer to <a href="#pg-bankcode-and-user-credentials">With pg, bankcode and user_credentials</a>  <a href="#sample-request">Sample request</a>  .</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>LAZYPAY</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>phone<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This parameter must contain the customer’s phone number for which the eligibility is to be checked needs to be passed</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>“9999999999”</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>payuToken<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This parameter must contain is the PayU instrument token for saved card. This parameter must used in combination with <strong>user_credentials</strong>. For more information, refer to  <a href="#with-payuToken-and-user_credentials">With payuToken and user_credentials</a> under  <a href="#sample-request">Sample request</a>  .</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Token12345  <br><br>Note: One or multiple payu tokens can be passed and max 10 tokens supported in a request.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>user_credentials<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This parameter must contain an unique user credential mapped against each user, to be passed by the merchant for saved card.or more information, refer to <a href="#sample-request">Sample request</a> .</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>abc:xyz</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>key <br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The merchant key provided by PayU. <br><strong>Reference</strong>: For more information on how to generate the Key and Salt, refer to any of the following:  </p>
<ul>
<li><strong>Production</strong>: <a href="https://docs.payu.in/docs/generate-merchant-key-and-salt-on-payu-dashboard">Generate Production Merchant Key and Sat</a>. </li>
<li><strong>Test</strong>: <a href="https://docs.payu.in/docs/generate-test-merchant-key-and-salt">Generate Test Merchant Key and Salt</a>.</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Your Test Key</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

### With pg, bankcode and user\_credentials

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

### With payuToken and user\_credentials

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

<br />
