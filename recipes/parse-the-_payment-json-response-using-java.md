---
title: Parse the _payment JSON response using Java
description: >-
  Sample code to parse the _payment JSON response that is from PayU for PayU
  Hosted Checkout Integration
hidden: false
recipe:
  color: '#018FF4'
  icon: 🦉
---
```java Java
import org.json.JSONObject;

public class PayUResponseParser {
    public static void main(String[] args) {
        String json = "{\n" +
                "      \"status\": 1,\n" +
                "      \"msg\": \"1 out of 1 Transactions Fetched Successfully\",\n" +
                "      \"transaction_details\": {\n" +
                "            \"7fa6c4783a363b3da573\": {\n" +
                "                  \"mihpayid\": \"403993715521889530\",\n" +
                "                  \"request_id\": \"\",\n" +
                "                  \"bank_ref_num\": \"721522\",\n" +
                "                  \"amt\": \"10.00\",\n" +
                "                  \"transaction_amount\": \"10.00\",\n" +
                "                  \"txnid\": \"7fa6c4783a363b3da573\",\n" +
                "                  \"additional_charges\": \"0.00\",\n" +
                "                  \"productinfo\": \"Test\",\n" +
                "                  \"firstname\": \"K\",\n" +
                "                  \"bankcode\": \"CC\",\n" +
                "                  \"udf1\": \"\",\n" +
                "                  \"udf3\": \"\",\n" +
                "                  \"udf4\": \"\",\n" +
                "                  \"udf5\": \"\",\n" +
                "                  \"field2\": \"177047\",\n" +
                "                  \"field9\": \"No Error\",\n" +
                "                  \"error_code\": \"E000\",\n" +
                "                  \"addedon\": \"2020-10-26 14:12:13\",\n" +
                "                  \"payment_source\": \"payu\",\n" +
                "                  \"card_type\": \"MAST\",\n" +
                "                  \"error_Message\": \"NO ERROR\",\n" +
                "                  \"net_amount_debit\": 10,\n" +
                "                  \"disc\": \"0.00\",\n" +
                "                  \"mode\": \"CC\",\n" +
                "                  \"PG_TYPE\": \"CC-PG\",\n" +
                "                  \"card_no\": \"512345XXXXXX2346\",\n" +
                "                  \"name_on_card\": \"Test\",\n" +
                "                  \"udf2\": \"\",\n" +
                "                  \"field5\": \"211939174867\",\n" +
                "                  \"field7\": \"AUTHPOSITIVE\",\n" +
                "                  \"status\": \"success\",\n" +
                "                  \"unmappedstatus\": \"captured\",\n" +
                "                  \"Merchant_UTR\": null,\n" +
                "                  \"Settled_At\": \"0000-00-00 00:00:00\"\n" +
                "            }\n" +
                "      }\n" +
                "}";

        JSONObject jsonObject = new JSONObject(json);
        JSONObject transactionDetails = jsonObject.getJSONObject("transaction_details");
        JSONObject transaction = transactionDetails.getJSONObject(transactionDetails.keys().next());
        String mihpayid = transaction.getString("mihpayid");
        String requestId = transaction.getString("request_id");
        String bankRefNum = transaction.getString("bank_ref_num");
        String amt = transaction.getString("amt");
        String transactionAmount = transaction.getString("transaction_amount");
        String txnid = transaction.getString("txnid");
        String additionalCharges = transaction.getString("additional_charges");
        String productinfo = transaction.getString("productinfo");
        String firstname = transaction.getString("firstname");
        String bankcode = transaction.getString("bankcode");
        String udf1 = transaction.getString("udf1");
        String udf3 = transaction.getString("udf3");
        String udf4 = transaction.getString("udf4");
        String udf5 = transaction.getString("udf5");
        String field2 = transaction.getString("field2");
        String field9 = transaction.getString("field9");
        String errorCode = transaction.getString("error_code");
        String addedon = transaction.getString("addedon");
        String paymentSource = transaction.getString("payment_source");
        String cardType = transaction.getString("card_type");
        String errorMessage = transaction.getString("error_Message");
        int netAmountDebit = transaction.getInt("net_amount_debit");
        String disc = transaction.getString("disc");
        String mode = transaction.getString("mode");
        String pgType = transaction.getString("PG_TYPE");
        String cardNo = transaction.getString("card_no");
        String nameOnCard = transaction.getString("name_on_card");
        String udf2 = transaction.getString("udf2");
        String field5 = transaction.getString("field5");
        String field7 = transaction.getString("field
```

# ImportJSONObject class



Import the JSONObject class from the org.json package.

# Define main method



Define a main method that takes no arguments.

# Define String variable

<!-- java@1-53 -->

Define a string variable json that contains the JSON response from PayU.

# Pass the json string to its constructor

<!-- java@55-107 -->

Create a new JSONObject instance by passing the json string to its constructor.

# Get transaction details



Get the transaction_details object from the jsonObject.
Get the first (and only) transaction object from the transaction_details object.

# Extract the values of various fields

<!-- java@51-80 -->

Extract the values of various fields from the transaction object using the getString and getInt methods.