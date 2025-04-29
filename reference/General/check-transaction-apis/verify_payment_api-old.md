---
title: '[OLD]Verify Payment API'
excerpt: ''
api:
  file: general-29.json
  operationId: verifypayment
deprecated: false
hidden: true
metadata:
  title: ''
  description: >-
    The Verify Payment API provides transaction status information, including
    details such as payment source, card type, and offer availed at cart or
    transaction level. It also includes response parameters like status,
    message, and transaction details in JSON format.
  keywords:
    - verify_payment
    - verify_payment command
    - Verify Payment API
    - Check Transaction Status API
  robots: index
next:
  description: ''
---
The Verify Payment (**verify_payment**) API gives you the status of the transaction. PayU recommends using this API to reconcile with PayU’s database after you receive the response, where var1 is your transaction ID.

<GENERALAPIsEnvironment />

<details><summary>Sample request</summary>

```curl
curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=JP***g' \
--data-urlencode 'command=verify_payment' \
--data-urlencode 'var1=IhfgcZnXR4o4nB' \
--data-urlencode 'hash=a0ae79fdd66c875af6e9b21c4a67f1822deb00f2df5e9f0b1948f3222f536a9bf741b24efbb1874ca0f84f76b036e6c0d641581d0100f7abe4aeed2f3264f5c9'
```

</details>

<details>  <summary>Sample response</summary>

- If credit card payment is made, the response is similar to the following:

```plaintext
{
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
                  "error_Message": "NO ERROR",
                  "net_amount_debit": 10,
                  "disc": "0.00",
                  "mode": "CC",
                  "PG_TYPE": "CC-PG",
                  "card_no": "512345XXXXXX2346",
                  "name_on_card": "Test",
                  "udf2": "",
                  "field5": "211939174867",
                  "field7": "AUTHPOSITIVE",
                  "status": "success",
                  "unmappedstatus": "captured",
                  "Merchant_UTR": null,
                  "Settled_At": "0000-00-00 00:00:00"
            }
      }
}
```

- Offer availed on cart level

```
{
    "status": 1,
    "msg": "1 out of 1 Transactions Fetched Successfully",
    "transaction_details": {
        "4ef9a47883e3618b9256": {
            "mihpayid": "613345678912533633",
            "request_id": "",
            "bank_ref_num": "321980",
            "amt": "9800.00",
            "transaction_amount": "10000.00",
            "txnid": "4ef9a47883e3618b9256",
            "additional_charges": "0.00",
            "productinfo": "Product Info",
            "firstname": "Payu-Admin",
            "bankcode": "CC",
            "udf1": "",
            "udf2": "",
            "udf3": "",
            "udf4": "",
            "udf5": "",
            "field2": "296675",
            "field9": "No Error",
            "error_code": "E000",
            "addedon": "2024-03-05 12:59:40",
            "payment_source": "payu",
            "card_type": "VISA",
            "error_Message": "NO ERROR",
            "net_amount_debit": 10000.00,
            "disc": "200.00",
            "mode": "CC",
            "PG_TYPE": "CC-PG",
            "card_no": "XXXXXXXXXXXX0000",
            "status": "success",
            "unmappedstatus": "captured",
            "Merchant_UTR": null,
            "Settled_At": "0000-00-00 00:00:00",
            "name_on_card": null,
            "offerApplied": "SkuTest@tW3YT0TZ4laU",
            "offerAvailed": "SkuTest@tW3YT0TZ4laU",
            "offerLevel": "CART_LEVEL",
            "cart_details": {
                "id": "21",
                "payu_id": "613345678912533633",
                "total_items": "1",
                "total_cart_amount": "10000.00",
                "offer_applied": "SkuTest@tW3YT0TZ4laU",
                "offer_availed": "SkuTest@tW3YT0TZ4laU",
                "offer_auto_apply": "0",
                "instant_discount": "200.00",
                "cashback_discount": "0.00",
                "total_discount": "200.00",
                "net_cart_amount": "9800.00",
                "created_at": "2024-03-05 12:59:40",
                "updated_at": "2024-03-05 13:00:34",
                "sku_details": [
                    {
                        "id": "26",
                        "cart_id": "21",
                        "payu_id": "613345678912533633",
                        "mid": "180012",
                        "sku_id": "airpodCohort",
                        "sku_name": "airpodCohort",
                        "amount_per_sku": "10000.00",
                        "quantity": "1",
                        "amount_before_discount": "10000.00",
                        "discount": "200.00",
                        "amount_after_discount": "9800.00",
                        "offer_applied": "SkuTest@tW3YT0TZ4laU",
                        "offer_availed": "SkuTest@tW3YT0TZ4laU",
                        "offer_status": "success",
                        "offer_type": "INSTANT",
                        "offer_auto_apply": "0",
                        "is_nce": "0",
                        "failure_reason": "",
                        "created_at": "2024-03-05 12:59:40",
                        "updated_at": "2024-03-05 13:00:34",
                        "offer_title": "SkuTest",
                        "offer_description": "SkuTest",
                        "instant_discount": "200.00",
                        "cashback_discount": "0.00",
                        "offers_raw_response": null,
                        "raw_response": "[{\"status\": \"SUCCESS\", \"discount\": 200, \"isNoCost\": false, \"offer_key\": \"SkuTest@tW3YT0TZ4laU\", \"offer_type\": \"INSTANT\", \"offer_title\": \"SkuTest\", \"record_type\": \"OFFER\", \"failure_code\": null, \"flag_to_fail\": false, \"nce_discount\": 0, \"failure_reason\": \"Offer Applied Successfully\", \"offer_category\": null, \"instant_discount\": 200, \"parent_offer_key\": null, \"cashback_discount\": 0, \"offer_description\": \"SkuTest\", \"gstSubventedViaOffer\": false, \"nce_instant_discount\": 0, \"nce_cashback_discount\": 0}]"
                    }
                ]
            }
        }
    }
}
```

- Offer availed at Transaction level

```
{
    "status": 1,
    "msg": "1 out of 1 Transactions Fetched Successfully",
    "transaction_details": {
        "e4a62ffa2f53ccf4a0e1": {
            "mihpayid": "999000000000521",
            "request_id": "",
            "bank_ref_num": "854334142158",
            "amt": "49900.00",
            "transaction_amount": "50000.00",
            "txnid": "e4a62ffa2f53ccf4a0e1",
            "additional_charges": "0.00",
            "productinfo": "Product Info",
            "firstname": "Payu-Admin",
            "bankcode": "UPI",
            "udf1": "",
            "udf2": "",
            "udf3": "",
            "udf4": "",
            "udf5": "",
            "field2": "1708668284316",
            "field9": "SUCCESS|Completed Using Verify API",
            "error_code": "E000",
            "addedon": "2024-02-23 11:34:27",
            "payment_source": "payu",
            "card_type": null,
            "error_Message": "NO ERROR",
            "net_amount_debit": 49900.00,
            "disc": "100.00",
            "mode": "UPI",
            "PG_TYPE": "UPI-PG",
            "card_no": "",
            "status": "success",
            "unmappedstatus": "captured",
            "Merchant_UTR": null,
            "Settled_At": "0000-00-00 00:00:00",
            "App_Name": "GooglePay",
            "offerApplied": "UpiInstantOffer@nkTu0jJcPlS9",
            "offerAvailed": "UpiInstantOffer@nkTu0jJcPlS9",
            "offerType": "instant",
            "offerLevel": "TRANSACTION_LEVEL",
            "transactionOffer": "\"{\\\"offer_data\\\": [{\\\"status\\\": \\\"SUCCESS\\\", \\\"isDpEmi\\\": false, \\\"discount\\\": 100, \\\"isNoCost\\\": false, \\\"offer_key\\\": \\\"UpiInstantOffer@nkTu0jJcPlS9\\\", \\\"offer_type\\\": \\\"INSTANT\\\", \\\"offer_title\\\": \\\"UpiInstantOffer\\\", \\\"record_type\\\": \\\"OFFER\\\", \\\"failure_code\\\": null, \\\"flag_to_fail\\\": false, \\\"failure_reason\\\": \\\"Offer Applied Successfully\\\", \\\"offer_category\\\": null, \\\"parent_offer_key\\\": null, \\\"offer_description\\\": \\\"instant 100 \\\"}], \\\"discount_data\\\": {\\\"total_discount\\\": 100, \\\"instant_discount\\\": 100, \\\"cashback_discount\\\": 0, \\\"downPaymentAmount\\\": 0, \\\"total_nce_discount\\\": 0, \\\"gstSubventedViaOffer\\\": false, \\\"instant_nce_discount\\\": 0, \\\"cashback_nce_discount\\\": 0}}\""
        }
    }
}
```

#### Failure Responses

- If txnID is not found, the response is similar to the following:

```plaintext
{
"status":0,"msg":"0 out of 1 Transactions Fetched

Successfully","transaction_details":{"IhfgcZnXR4o4nB":{"mihpayid":"Not Found","status":"Not Found"}}
}
```

</details>

<details>  <summary>Response parameters</summary>

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "status",
    "0-1": "This parameter returns the status of web service call. The status can be any of the following:  \n_ 0 - If web service call failed.  \n_ 1 - If web service call succeeded",
    "0-2": "0",
    "1-0": "msg",
    "1-1": "This parameter returns the reason string.",
    "1-2": "For example, any of the following messages are displayed:  \n  \n- Parameter missing\n- Token is empty \n- Amount is empty\n- Transaction not exists",
    "2-0": "transaction\\_details",
    "2-1": "This parameter contains the response in a JSON format. For more information refer to [JSON fields description for transaction_details parameter ](#json-field-description-for-transaction_details-parameter).",
    "2-2": "",
    "3-0": "This parameter may or may not be returned depending on the web service being called.",
    "3-1": "mihpayid,request\\_id, bank\\_ref\\_num etc",
    "3-2": "",
    "4-0": "request\\_id",
    "4-1": "PayU Request ID for a request in a Transaction. For example, a transaction can have a refund request.",
    "4-2": "7800456",
    "5-0": "bank\\_ref\\_num",
    "5-1": "This parameter returns the bank reference number. If the bank provides after a successful action.",
    "5-2": "204519474956"
  },
  "cols": 3,
  "rows": 6,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes). 

[block:tutorial-tile]
{
  "backgroundColor": "#018FF4",
  "emoji": "🦉",
  "id": "65afb6e90a4e0500389d3886",
  "link": "https://docs.payu.in/v1/recipes/parse-the-verify-payment-api-response",
  "slug": "parse-the-verify-payment-api-response",
  "title": "Parse the Verify Payment API response"
}
[/block]


</details>

## Request parameters

<details>  <summary>Reference information for request parameters</summary>

<KeyHashForGeneralParametersDescription />

</details>

**Sample values**

Use the following sample values while trying out the API:

- `var1` (your transaction ID/order ID): 7fa6c4783a363b3da573