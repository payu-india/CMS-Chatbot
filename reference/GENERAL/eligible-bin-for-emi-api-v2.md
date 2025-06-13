---
title: Eligible Bin for EMI API v2
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
The Eligible Bin for EMI API v2 is used only when the merchant needs the EMI feature of PayU. If you are managing card details on your website, this API can tell the issuing bank of the card bin. It also provides the minimum eligible amount for a particular bank.

<Image align="center" src="https://files.readme.io/2eaac64-emi_eligible_bins_flow.png" />

HTTP Method: **POST**

You can post a request using any of the following methods:

* [Request without bank selection](#request-without-bank-selection)
* [Request with bank selection](#request-with-bank-selection)

## Request headers

The request header contains the following fields:

<Table>
  <thead>
    <tr>
      <th>
        **Field**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Date
        **mandatory**
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
        Digest\
        **mandatory**
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
        Authorization\
        **mandatory**
      </td>

      <td>
        This field is in the following format:\
        `hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="CkGfgbho69uTMMOGU0mHWf+1CUAlIp3AjvsON9n9/E4="`\
        Where the above format includes the following:  

        * **username**: The merchant key of the merchant.
        * **algorithm**: This must have the value as **hmac-sha256** that is used for this API
        * **headers**: This must have the value as **date digest**
        * **signature**: This must contain the hmacsha256 of (signing\_string, merchant\_secret), where:
          * **signing\_string**: This is in the "**Date**"+"\\n"+"**Digest**" format. Here, the Date and Digest is the same values in the fields listed in this table For example, "Thu, 17 Feb 2022 08:17:59 GMT""\\n"+“vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=“
          * **merchant\_secret**: The merchant Salt of the merchant. For more information on getting the merchant Salt, refer to [Generate Merchant Key and Salt on PayU Dashboard](https://docs.payu.in/v1/docs/generate-merchant-key-and-salt-on-payu-dashboard)
      </td>

      <td>
         hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI="
      </td>
    </tr>

    <tr>
      <td>
        platformId\
        **mandatory**
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

## Request without bank selection

### Request parameters

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        bintype
        **mandatory**
      </td>

      <td>
        This parameter needs can include any of the following the values:  

        * **bin**: If you want to check on the basis of the first 6/8/9 digits of card number or network token.
        * **NET**: If you want to check on the basis of network token.
      </td>

      <td>
        bin
      </td>
    </tr>

    <tr>
      <td>
        value\
        **mandatory**
      </td>

      <td>
        This parameter can contain any of the following:  

        * If **bin** used in var1 parameter, the first 6/8/9 digits of card number or network token.
        * If **NET** used in the var1 parameter, the entire network token must be passed.
      </td>

      <td>
        4161041969147181
      </td>
    </tr>

    <tr>
      <td>
        amount\
        **conditional**
      </td>

      <td>
        This parameter needs to include the transaction amount.  

        * \*Note\*\*: Amount is a non-mandatory field, but is mandatory if bank code is ONEC or BAJFIN .
      </td>

      <td>
        10000
      </td>
    </tr>
  </tbody>
</Table>

### Response parameters

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        status
      </td>

      <td>
        This parameter returns the status of web service call.\
        The status can be any of the following:\
            \- 0 - If web service call failed.\
             \- 1 - If web service call succeeded
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        msg
      </td>

      <td>
        This parameter returns whether the EMI details were fetched successfully or not found.
      </td>

      <td>
        Details fetched successfully
      </td>
    </tr>

    <tr>
      <td>
        details
      </td>

      <td>
        The details of the EMI offer is displayed in a JSON format and it contains the following fields:
      </td>

      <td>
         
      </td>
    </tr>
  </tbody>
</Table>

### Sample response

* If successfully fetched:

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

* If not found:

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

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        bintype
        **mandatory**
      </td>

      <td>
        This parameter needs can include any of the following the values:  

        * **bin**: If you want to check on the basis of the first 6/8/9 digits of card number or network token.
        * **NET**: If you want to check on the basis of network token.
      </td>

      <td>
        bin
      </td>
    </tr>

    <tr>
      <td>
        value\
        **mandatory**
      </td>

      <td>
        This parameter can contain any of the following:  

        * If **bin** used in var1 parameter, the first 6/8/9 digits of card number or network token.
        * If **NET** used in the var1 parameter, the entire network token must be passed.
      </td>

      <td>
        4161041969147181
      </td>
    </tr>

    <tr>
      <td>
        amount\
        **conditional**
      </td>

      <td>
        This parameter needs to include the transaction amount. **Note**: Amount is a non-mandatory field, but is mandatory if bank code is ONEC or BAJFIN .
      </td>

      <td>
        10000
      </td>
    </tr>

    <tr>
      <td>
        bank\
        **mandatory**
      </td>

      <td>
        This parameter contains the bank code for which the request is sent.
      </td>

      <td>
        ICICI
      </td>
    </tr>
  </tbody>
</Table>

### Response parameters

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        status
      </td>

      <td>
        This parameter returns the status of web service call.\
        The status can be any of the following:\
            \- 0 - If web service call failed.\
             \- 1 - If web service call succeeded
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        msg
      </td>

      <td>
        This parameter returns whether the EMI details were fetched successfully or not found.
      </td>

      <td>
        Details fetched successfully
      </td>
    </tr>

    <tr>
      <td>
        details
      </td>

      <td>
        The details of the EMI offer is displayed in a JSON format and it contains the following fields:\
            \- **isEligible** - This paraAny of the following values are:\
                 \- .0 - If EMI offers are not available for the given card BIN.\
                 \- 1 - If EMI offers are available for the given card BIN.  

        * **bank** - The name of bank that corresponds to the given card BIN
        * **minAmount** - The minimum amount for which the EMI offer is available
      </td>

      <td>
        "isEligible": 0, 
      </td>
    </tr>
  </tbody>
</Table>

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

* If **var3** (input bank name) does not match with the bank name in the PayU Database, the bin given in the input is of a different bank name:

```plaintext
Array (
[status] => 0
[msg] => Invalid Bin )
```

* When the BIN passed does not match with the bankName passed in the request:”

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