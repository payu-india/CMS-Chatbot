---
title: v2 Refund Status API
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Refund Status** API for Split Payments provides a specialized mechanism for tracking refund statuses in split payment scenarios. It's designed for aggregator merchants who process payments divided among multiple recipients. Unlike the v1 API, this enhanced version provides complete visibility into parent-child transaction relationships, refund actions, and settlement details.

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

<br />

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
        requestId
        `optional`
      </td>

      <td>
        `String Array `Array of request IDs for which the refund information is required.
      </td>

      <td>
        `["11763053990", "11763053112"]`
      </td>
    </tr>

    <tr>
      <td>
        payuId
        `optional`
      </td>

      <td>
        `String Array `Array of PayU transaction IDs or PayU ID for which the refund information is required. Payu ID (mihpayuid) that you receive in the response for a successful payment transaction.
      </td>

      <td>
        `["11763053990"]`
      </td>
    </tr>

    <tr>
      <td>
        tokenId
        `optional`
      </td>

      <td>
        `String `This parameter must contain the Token ID (unique token from the merchant) for the refund request. Token ID has to be generated at your end for each new refund request. It is an identifier for each new refund request which can be used for tracking it. It must be unique for every new refund request generated – otherwise the refund request would not be generated successfully. Token ID length should not be greater than 23 characters
      </td>

      <td>
        `["TOKEN12345"]`
      </td>
    </tr>
  </tbody>
</Table>

> 📘 Note:
>
> At least one of the following parameters must be provided: `requestId`, `payuId`, or `tokenId`.

### Sample Request

```bash
curl --location 'http://localhost:8080/v1/transaction' \
--header 'mid: 8759546' \
--header 'Content-Type: application/json' \
--header 'Info-Command: aggregator_check_action_status_txnid' \
--header 'Date: Thu, 17 Feb 2022 08:17:59 GMT' \
--header 'Digest: vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=' \
--header 'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI="' \
--header 'platformId: 1' \
--data '{
    "requestId": null,
    "payuId": ["11763053990"],
    "tokenId": null
}'
```

### Response Parameters

| Parameter                            | Description                                               | Example                                    |
| ------------------------------------ | --------------------------------------------------------- | ------------------------------------------ |
| message                              | Indicates the result of the API call                      | `"Success"`                                |
| status                               | Status of the API call (1 for success, 0 for failure)     | `1`                                        |
| result                               | Array containing the parent and split transaction details | See JSON example                           |
| payuId                               | The PayU ID of the parent transaction                     | `17253043342`                              |
| transactionDetails                   | Basic details of the parent transaction                   | Contains ID, status, amount, etc.          |
| transactionActionDetails             | Actions performed on the parent transaction               | Contains action type, status, amount, etc. |
| splitTransactionDetails              | Array of split transaction details                        | Contains payuId, transactionDetails, etc.  |
| transactionActionDetails (in splits) | Actions performed on each split transaction               | Contains refund actions and their details  |

### Sample Response

#### Success Response

```json
{
    "message": "Success",
    "status": 1,
    "result": [
        {
            "payuId": 17253043342,
            "transactionDetails": {
                "id": 17253043342,
                "transactionId": "PB35163007S",
                "status": "autoRefund",
                "discount": 0.0,
                "amount": 0.0,
                "transactionFee": 2259.0,
                "additionalCharges": 0.0,
                "mode": "CASH",
                "baseTxnId": 0,
                "firstName": "Masood",
                "lastName": "Masood Ahmed Wani",
                "addedOn": "2023-04-27 16:18:16",
                "phone": "8448480680",
                "email": "example@example.com",
                "productInfo": "PBProduct",
                "errorCode": "E000",
                "ibiboCode": "FREC",
                "merchantKey": "iDJYfd",
                "errorMessage": "No Error",
                "paymentSource": "payuS2S"
            },
            "transactionActionDetails": [
                {
                    "id": 12031063143,
                    "bankRefNo": "5jeF8wMyZ9jnZ9_17253043342_1",
                    "token": null,
                    "actionType": "capture",
                    "prevStatus": "failed",
                    "amount": 2259.0,
                    "status": "SUCCESS",
                    "bankArn": "5jeF8wMyZ9jnZ9_17253043342_1",
                    "updatedAt": "2023-04-28 10:09:04",
                    "createdAt": "2023-04-28 10:01:14",
                    "settlementId": null,
                    "amountSettled": null,
                    "refundMode": "-",
                    "settledOn": null,
                    "merchantUTR": null
                }
            ],
            "splitTransactionDetails": [
                {
                    "payuId": 12071315088,
                    "transactionDetails": {
                        "id": 12071315088,
                        "transactionId": "PB35163007S_1",
                        "status": "success",
                        "discount": 0.0,
                        "amount": 2259.0,
                        "transactionFee": 0.0,
                        "additionalCharges": 0.0,
                        "mode": "CASH",
                        "baseTxnId": 17253043342,
                        "firstName": "Masood",
                        "lastName": "Masood Ahmed Wani",
                        "addedOn": "2023-05-06 16:07:40",
                        "phone": "8448480680",
                        "email": "example@example.com",
                        "productInfo": "PBProduct",
                        "errorCode": "E000",
                        "ibiboCode": "FREC",
                        "merchantKey": "iDJYfd",
                        "errorMessage": "No Error",
                        "paymentSource": "payuS2S"
                    },
                    "transactionActionDetails": [
                        {
                            "id": 12071315088,
                            "bankRefNo": "5jeF8wMyZ9jnZ9_12031097474recon__1",
                            "token": "recon_17253043342",
                            "actionType": "refund",
                            "prevStatus": "requested",
                            "amount": 2259.0,
                            "status": "success",
                            "bankArn": "5jeF8wMyZ9jnZ9_12031097474recon__1",
                            "updatedAt": "2023-05-11 11:49:04",
                            "createdAt": "2023-05-06 16:07:40",
                            "settlementId": null,
                            "amountSettled": null,
                            "refundMode": "Back to Source",
                            "settledOn": null,
                            "merchantUTR": null
                        }
                    ]
                }
            ]
        }
    ]
}
```

#### Failure Response

```json
{
  "status": 0,
  "msg": "0 out of 1 Transactions Fetched Successfully",
  "transaction_details": {
    "16988019552": "No action status found value of var1 sent in the request"
  }
}
```