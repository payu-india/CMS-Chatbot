---
title: Parse the Verify Payment API response
description: >-
  This recipe helps understand how to parse the response from verify_payment
  API.
hidden: false
recipe:
  color: '#018FF4'
  icon: 🦉
---
```java Java
import org.json.JSONObject;

public class PayUResponseParser {
    public static void main(String[] args) {
        String jsonString = "{\n" +
                "  \"status\": 1,\n" +
                "  \"msg\": \"1 out of 1 Transactions Fetched Successfully\",\n" +
                "  \"transaction_details\": {\n" +
                "    \"7fa6c4783a363b3da573\": {\n" +
                "      \"mihpayid\": \"403993715521889530\",\n" +
                "      \"request_id\": \"\",\n" +
                "      \"bank_ref_num\": \"721522\",\n" +
                "      \"amt\": \"10.00\",\n" +
                "      \"transaction_amount\": \"10.00\",\n" +
                "      \"txnid\": \"7fa6c4783a363b3da573\",\n" +
                "      \"additional_charges\": \"0.00\",\n" +
                "      \"productinfo\": \"Test\",\n" +
                "      \"firstname\": \"K\",\n" +
                "      \"bankcode\": \"CC\",\n" +
                "      \"udf1\": \"\",\n" +
                "      \"udf3\": \"\",\n" +
                "      \"udf4\": \"\",\n" +
                "      \"udf5\": \"\",\n" +
                "      \"field2\": \"177047\",\n" +
                "      \"field9\": \"No Error\",\n" +
                "      \"error_code\": \"E000\",\n" +
                "      \"addedon\": \"2020-10-26 14:12:13\",\n" +
                "      \"payment_source\": \"payu\",\n" +
                "      \"card_type\": \"UNKNOWN\",\n" +
                "      \"error_Message\": \"No Error\",\n" +
                "      \"net_amount_debit\": 10,\n" +
                "      \"disc\": \"0.00\",\n" +
                "      \"mode\": \"CC\",\n" +
                "      \"PG_TYPE\": \"CC-PG\",\n" +
                "      \"card_no\": \"512345XXXXXX2346\",\n" +
                "      \"name_on_card\": \"Test\",\n" +
                "      \"udf2\": \"\",\n" +
                "      \"status\": \"success\",\n" +
                "      \"unmappedstatus\": \"captured\",\n" +
                "      \"Merchant_UTR\": null,\n" +
                "      \"Settled_At\": \"0000-00-00 00:00:00\"\n" +
                "    }\n" +
                "  }\n" +
                "}";
        JSONObject jsonObject = new JSONObject(jsonString);
        JSONObject transactionDetails = jsonObject.getJSONObject("transaction_details");
        JSONObject transaction = transactionDetails.getJSONObject(transactionDetails.keys().next());
        String mihpayid = transaction.getString("mihpayid");
        String bankRefNum = transaction.getString("bank_ref_num");
        String txnid = transaction.getString("txnid");
        String status = transaction.getString("status");
        System.out.println("mihpayid: " + mihpayid);
        System.out.println("bank_ref_num: " + bankRefNum);
        System.out.println("txnid: " + txnid);
        System.out.println("status: " + status);
    }
}

```

```javascript JavaScript
const jsonString = `{
  "status": 1,
  "msg": "1 out of 1 Transactions Fetched Successfully",
  "transaction_details": {
    "7fa6c4783a363b3da573": {
      "mihpayid": "403993715521889530",
      "request_id": "",
      "bank_ref_num": "721522",
      "amt": "10.00",
      "transaction_amount": "10.00",
      "txnid": "7fa6c4783a363b3da573",
      "additional_charges": "0.00",
      "productinfo": "Test",
      "firstname": "K",
      "bankcode": "CC",
      "udf1": "",
      "udf3": "",
      "udf4": "",
      "udf5": "",
      "field2": "177047",
      "field9": "No Error",
      "error_code": "E000",
      "addedon": "2020-10-26 14:12:13",
      "payment_source": "payu",
      "card_type": "UNKNOWN",
      "error_Message": "No Error",
      "net_amount_debit": 10,
      "disc": "0.00",
      "mode": "CC",
      "PG_TYPE": "CC-PG",
      "card_no": "512345XXXXXX2346",
      "name_on_card": "Test",
      "udf2": "",
      "status": "success",
      "unmappedstatus": "captured",
      "Merchant_UTR": null,
      "Settled_At": "0000-00-00 00:00:00"
    }
  }
}`;

const jsonObject = JSON.parse(jsonString);
const transactionDetails = jsonObject.transaction_details;
const transaction = transactionDetails[Object.keys(transactionDetails)[0]];
const mihpayid = transaction.mihpayid;
const bankRefNum = transaction.bank_ref_num;
const txnid = transaction.txnid;
const status = transaction.status;

console.log(`mihpayid: ${mihpayid}`);
console.log(`bank_ref_num: ${bankRefNum}`);
console.log(`txnid: ${txnid}`);
console.log(`status: ${status}`);
```

# Introduction



This code uses the org.json library to parse the JSON response. It extracts the mihpayid, bank_ref_num, txnid, and status fields from the response and prints them to the console. You can modify this code to extract other fields as well.

# Define the JSON response

<!-- java@5 -->
<!-- javascript@1-40 -->

Define the JSON response as a string

# Create a JSONObject from response

<!-- java@45 -->
<!-- javascript@42 -->

Create a JSONObject from the JSON response string

# Get the transaction details

<!-- java@46 -->
<!-- javascript@43 -->

Get the transaction_details object from the JSON response

# Get the first transaction object

<!-- java@47 -->
<!-- javascript@44 -->

Get the first transaction object from the transaction_details object

# Extract the required fields from the transaction object

<!-- java@48-51 -->
<!-- javascript@44-48 -->

Extract the required fields from the transaction object

# Display to customer

<!-- java@52-55 -->
<!-- javascript@50-53 -->

Print the extracted fields to the console