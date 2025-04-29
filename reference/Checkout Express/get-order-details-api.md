---
title: Get Order Details API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Get Order Details API
  description: >-
    Access the PayU Get Order Details API to retrieve detailed information and
    status for a specific transaction ID. Ideal for developers integrating
    PayU's payment solutions, this API provides comprehensive order data for
    seamless transaction management.
  keywords:
    - Get Order Details API
    - Fetch order details
    - order status API
    - order details endpoint
  robots: index
next:
  description: ''
---
You can use the Get Order Details API to fetch the order details and order status for a given transaction id (txn id).

## Environment

| Environment | URL                                                                                              |
| :---------- | :----------------------------------------------------------------------------------------------- |
| Test        | [https://apitest.payu.in/cart/order/\{\{txnid}}](https://apitest.payu.in/cart/order/\{\{txnid}}) |
| Production  | [https://api.payu.in/cart/order/\{\{txnid}}](https://api.payu.in/cart/order/\{\{txnid}})         |

## Sample Request

```Text cURL
curl --location 'https://apitest.payu.in/cart/order/768_240214:64' \
--header 'Date: Thu, 15 Feb 2024 06:18:04 GMT' \
--header 'Authorization: hmac username="Tr7xQY", algorithm="sha512", headers="date", signature="3fda67023027f0cd57f604a408eb670e56fb04e562f79c88876b568eb407b63cfc53f5ae2113ea442c2109ba9d3c373da63abe6c913746fed8ec36205f968e91"' \
--data ''
```

> 🚧 Keep in mind
>
> Date and Authorization headers are also needed to authenticate the request. Sample Java code to create the authentication headers - V2 SHA512 Authentication

### Create V2 SHA512 Authentication

**Required Headers**

1. Date
2. Authorization

### Sample JAVA code to create an authentication header

```Text JAVA
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

## Sample response

### Success scenario

```Text JSON
{
    "message": "Order Fetched Successfully",
    "status": 1,
    "traceId": "27896297-a758-4428-af1b-0a2fb82aa242#272398",
    "data": {
        "orderReferenceId": 2635,
        "orderId": "4fea9",
        "merchantId": 8245446,
        "txnId": "768_240214:64",
        "finalAmount": 45.00,
        "originalAmount": 45.00,
        "cartAmount": 45.00,
        "orderStatus": "PAYMENT_INITIATED",
        "skus": [
            {
                "skuId": "woo-hoodie-with-logo",
                "skuName": "Hoodie with Logo",
                "amountPerSku": 45.00,
                "originalQuantity": 1,
                "finalQuantity": 1,
                "enforcedOfferKeys": [],
                "skuStatus": "PAYMENT_INITIATED",
                "logo": "https://payu.in/demo/checkoutExpress/utils/images/MicrosoftTeams-image%20(31).png"
            }
        ],
        "addressVersion": "ac84a9039a34c5edfe2c1",
        "address": [
            {
                "shippingAddress": {
                    "id": 65,
                    "name": "prashantshukla",
                    "email": "shukla.prashant@orangemantra.in",
                    "addressLine": "Saket Area demo57",
                    "addressLine2": "Delhi",
                    "addressPhoneNumber": "9810263726",
                    "landmark": "",
                    "pincode": 110062,
                    "city": "New Delhi",
                    "state": "HR",
                    "tag": "Home",
                    "isDefault": true,
                    "isCodAvailable": true,
                    "version": "ac84a9039a34c5edfe2c1"
                },
                "consent": false
            }
        ],
        "enforcedOfferKeys": [],
        "isUpdated": false
    }
}
```

### Failure scenario

**Order not found**

```Text JSON
{
	"message" : "Order Not found"
}
```
