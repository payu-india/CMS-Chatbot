---
title: Get Aggregator/Parent Transaction Info API
excerpt: ''
api:
  file: get-aggregatorparent-transaction-info-2.json
  operationId: GetAggregator/ParentTransactionInfo
deprecated: false
hidden: false
metadata:
  title: Get Aggregator/Parent Transaction Info API
  description: ''
  keywords:
    - Get Aggregator/Parent Transaction Info API
    - Aggregator/Parent Transaction Info API
    - get_aggregator_transactions API Command
    - API Command get_aggregator_transactions
  robots: index
next:
  description: ''
---
The **Get Aggregator Transactions** API is for getting the transaction info of parent merchants in the Aggregator flow.

### Environment

|                            |                                         |
| -------------------------- | --------------------------------------- |
| **Test Environment**       | <https://uat-onepayuonboarding.payu.in> |
| **Production Environment** | <https://onboarding.payu.in>            |

<details> <summary>Response parameters and sample response</summary>

```
curl --location --request POST 'https://info.payu.in/merchant/postservice?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=A****J' \
--data-urlencode 'command=get_aggregator_transactions' \
--data-urlencode 'var1=2021-12-29 22:00' \
--data-urlencode 'hash=586e3379b3d9f90682329cf7efd27273aeb290936d9edf98686370bc59fdc67b06c57a5201b9bd193dc0f00fe6ecd821f60d81d5789ca2ee516db309f28025e9' \
--data-urlencode 'var2=2021-12-29 22:30' \
--data-urlencode 'var3=1' \
--data-urlencode 'var4=100' \
--data-urlencode 'var5='
```

</details> 

<details> <summary>Response parameters and sample response</summary>

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "0-0": "status",
    "0-1": "This parameter contains the status of response. It can be any of the following:  \n  \n- **0:** Failed\n- **1:**Success",
    "1-0": "msg",
    "1-1": "This parameter contains the response or error message.",
    "2-0": "Transaction\\_details",
    "2-1": "This parameter contains the transaction details in an array format and it is displayed only when the **status** field returns the value as **1**. For more information on each field in the array and sample, refer to the next table."
  },
  "cols": 2,
  "rows": 3,
  "align": [
    null,
    null
  ]
}
[/block]


### Fields in the  Transaction\_details array

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "id",
    "0-1": "This field contains the PayU transaction ID.",
    "1-0": "status",
    "1-1": "This field contains the transaction status.",
    "2-0": "key",
    "2-1": "This field contains the parent merchant key.",
    "3-0": "merchantname",
    "3-1": "This field contains the parent merchant name.",
    "4-0": "txnid",
    "4-1": "This field contains the transaction ID.",
    "5-0": "base\\_id",
    "5-1": "This field contains the base PayU Transaction ID. It will be null for a parent transaction.",
    "6-0": "firstname",
    "6-1": "This field contains the first name of the customer who did the transaction.",
    "7-0": "lastname",
    "7-1": "This field contains the last name of the customer who did the transaction.",
    "8-0": "addedon",
    "8-1": "This field contains the transaction created date and time. Format: yyyy-mm-dd hh:ii:ss",
    "9-0": "bank\\_name",
    "9-1": "This field contains the bank name of payment transaction.",
    "10-0": "payment\\_gateway",
    "10-1": "This field contains the payment gateway used in the transaction.",
    "11-0": "phone",
    "11-1": "This field contains the contact number of the customer who did the transaction.",
    "12-0": "email",
    "12-1": "This field contains the email ID of the customer who did the transaction.",
    "13-0": "transaction\\_fee",
    "13-1": "This field contains the transaction fee without discount and additional charges.",
    "14-0": "amount",
    "14-1": "This field contains the total amount paid by customer.",
    "15-0": "discount",
    "15-1": "This field contains the discount or Subvention charges on the transaction.",
    "16-0": "additional\\_charges",
    "16-1": "This field contains the additional charges on transaction.",
    "17-0": "productinfo",
    "17-1": "This field contains the product information provided by merchant.",
    "18-0": "error\\_code",
    "18-1": "This field contains the transaction error code. For more information on errors, refer to [Error Handling](doc:error-handling)",
    "19-0": "bank\\_ref\\_no",
    "19-1": "This field contains the bank reference number.",
    "20-0": "ibibo\\_code",
    "20-1": "This field contains the IBIBO Code or bank\\_code that was submitted in transaction by the merchant to PayU.",
    "21-0": "mode",
    "21-1": "This field contains the Mode of transaction, such as, CC, DC, NB, EMI.",
    "22-0": "address2",
    "22-1": "This field contains the address of the customer.",
    "23-0": "city",
    "23-1": "This field contains the city of the customer.",
    "24-0": "zipcode",
    "24-1": "This field contains the PIN code of the customer.",
    "25-0": "pg\\_mid",
    "25-1": "This field contains the PG ID.",
    "26-0": "offer\\_type",
    "26-1": "This field contains the offer type if any offers were used.",
    "27-0": "splitCreated",
    "27-1": "This field contains no value or null.",
    "28-0": "is\\_parent\\_transaction",
    "28-1": "This field contains any of the the flag to indicate whether it is a Parent Transaction:  \n  \n- **true**; When the transaction is a parent transaction\n- **false **; When the transaction is not a parent transaction",
    "29-0": "splitInfo",
    "29-1": "This field contains no value or null for child transactions."
  },
  "cols": 2,
  "rows": 30,
  "align": [
    null,
    null
  ]
}
[/block]


</details>

<details> <summary>Sample response</summary>

```
{
    "status": 1,
    "msg": "Transaction Fetched Successfully",
    "Transaction_details": [
        {
            "id": "412345678912384148",
            "status": "captured",
            "key": "A***J",
            "merchantname": "Aggregator-Parent",
            "txnid": "2c1c4431f3fcf5a98a66",
            "base_id": null,
            "firstname": "Payu-Admin",
            "lastname": "",
            "addedon": "2021-12-29 22:11:08",
            "bank_name": "Credit Cards",
            "payment_gateway": "AxisCYBER",
            "phone": "1234567890",
            "email": "test@example.com",
            "transaction_fee": "10.00",
            "amount": "10.00",
            "discount": "0.00",
            "additional_charges": "0.00",
            "productinfo": "Product Info",
            "error_code": "E000",
            "bank_ref_no": "5192296867061049177385",
            "ibibo_code": "CC",
            "mode": "CC",
            "address2": "",
            "city": "",
            "zipcode": "",
            "pg_mid": null,
            "offer_type": null,
            "splitCreated": true,
            "is_parent_transaction": true,
            "splitInfo": [
                {
                    "id": "412345678912384152",
                    "status": "captured",
                    "merchantId": "39032915",
                    "key": "P****Y",
                    "txnid": "2c1c4431f3fcf5a98a661",
                    "addedon": "2021-12-29 22:11:53",
                    "transaction_fee": "3.00",
                    "amount": "3.00",
                    "discount": "0.00",
                    "additional_charges": "0.00"
                },
                {
                    "id": "412345678912384153",
                    "status": "captured",
                    "merchantId": "39032916",
                    "key": "P****K",
                    "txnid": "2c1c4431f3fcf5a98a662",
                    "addedon": "2021-12-29 22:11:53",
                    "transaction_fee": "5.00",
                    "amount": "5.00",
                    "discount": "0.00",
                    "additional_charges": "0.00"
                },
                {
                    "id": "412345678912384154",
                    "status": "captured",
                    "merchantId": "39032914",
                    "key": "A****J",
                    "txnid": "2c1c4431f3fcf5a98a66",
                    "addedon": "2021-12-29 22:11:53",
                    "transaction_fee": "2.00",
                    "amount": "2.00",
                    "discount": "0.00",
                    "additional_charges": "0.00"
                }
            ]
        },
        {
            "id": "412345678912384155",
            "status": "bounced",
            "key": "A****J",
            "merchantname": "Aggregator-Parent",
            "txnid": "02b3e5b6bc97dc3a3418",
            "base_id": null,
            "firstname": "Payu-Admin",
            "lastname": "",
            "addedon": "2021-12-29 22:13:08",
            "bank_name": "Credit Cards",
            "payment_gateway": "AxisCYBER",
            "phone": "1234567890",
            "email": "test@example.com",
            "transaction_fee": "11.00",
            "amount": "11.00",
            "discount": "0.00",
            "additional_charges": "0.00",
            "productinfo": "Product Info",
            "error_code": "E501",
            "bank_ref_no": null,
            "ibibo_code": "CC",
            "mode": "CC",
            "address2": "",
            "city": "",
            "zipcode": "",
            "pg_mid": null,
            "offer_type": null,
            "splitCreated": false,
            "is_parent_transaction": true,
            "splitInfo": null
        },
        {
            "id": "412345678912384156",
            "status": "captured",
            "key": "A****J",
            "merchantname": "Aggregator-Parent",
            "txnid": "61c21439bbd4609e258b",
            "base_id": null,
            "firstname": "Payu-Admin",
            "lastname": "",
            "addedon": "2021-12-29 22:14:23",
            "bank_name": "Credit Cards",
            "payment_gateway": "AxisCYBER",
            "phone": "1234567890",
            "email": "test@example.com",
            "transaction_fee": "11.00",
            "amount": "11.00",
            "discount": "0.00",
            "additional_charges": "0.00",
            "productinfo": "Product Info",
            "error_code": "E000",
            "bank_ref_no": "6333825950714879001604",
            "ibibo_code": "CC",
            "mode": "CC",
            "address2": "",
            "city": "",
            "zipcode": "",
            "pg_mid": null,
            "offer_type": null,
            "splitCreated": true,
            "is_parent_transaction": true,
            "splitInfo": [
                {
                    "id": "412345678912384160",
                    "status": "captured",
                    "merchantId": "39032915",
                    "key": "P****Y",
                    "txnid": "61c21439bbd4609e258b1",
                    "addedon": "2021-12-29 22:14:40",
                    "transaction_fee": "3.00",
                    "amount": "3.00",
                    "discount": "0.00",
                    "additional_charges": "0.00"
                },
                {
                    "id": "412345678912384161",
                    "status": "captured",
                    "merchantId": "39032916",
                    "key": "P****K",
                    "txnid": "61c21439bbd4609e258b2",
                    "addedon": "2021-12-29 22:14:40",
                    "transaction_fee": "6.00",
                    "amount": "6.00",
                    "discount": "0.00",
                    "additional_charges": "0.00"
                },
                {
                    "id": "412345678912384162",
                    "status": "captured",
                    "merchantId": "39032914",
                    "key": "A****J",
                    "txnid": "61c21439bbd4609e258b",
                    "addedon": "2021-12-29 22:14:40",
                    "transaction_fee": "2.00",
                    "amount": "2.00",
                    "discount": "0.00",
                    "additional_charges": "0.00"
                }
            ]
        }
    ]
}
```

For the sample response, refer to  [Additional Info for Split Settlements APIs](ref:additional-info-for-split-settlements-apis#sample-response-for-get-aggregatorparent-transaction-info).

</details>

## Request parameters