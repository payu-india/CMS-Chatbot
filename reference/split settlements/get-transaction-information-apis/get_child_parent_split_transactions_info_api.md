---
title: Get Child/Parent Split Transaction Info API
excerpt: ''
api:
  file: get-aggregatorparent-transaction-info-4.json
  operationId: GetChildParentSplitTransactionInfo
deprecated: false
hidden: false
metadata:
  title: Get Child/Parent Split Transaction Info API
  description: ''
  keywords:
    - get_split_transactions API Command
    - Get Child Split Transaction Info
    - API Command get_split_transactions
    - Get Parent Split Transaction Info API
  robots: index
next:
  description: ''
---
The **Get Child/Parent Split Transactions** API is for getting the transaction info of a child or parent split in Aggregator Flow.

> 📘 Note:
> 
> You can check the transaction info only for a single child or parent split. You need to submit separate requests for multiple splits to get the corresponding split information.

### Environment

|                        |                                         |
| ---------------------- | --------------------------------------- |
| Test Environment       | <https://uat-onepayuonboarding.payu.in> |
| Production Environment | <https://onboarding.payu.in>            |

<details> <summary>Sample request</summary>

```curl
curl --location --request POST 'https://info.payu.in/merchant/postservice?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=A***J' \
--data-urlencode 'command=get_split_transactions' \
--data-urlencode 'var1=2021-12-30 00:00' \
--data-urlencode 'hash=586e3379b3d9f90682329cf7efd27273aeb290936d9edf98686370bc59fdc67b06c57a5201b9bd193dc0f00fe6ecd821f60d81d5789ca2ee516db309f28025e9' \
--data-urlencode 'var2=2021-12-30 14:00' \
--data-urlencode 'var3=1' \
--data-urlencode 'var4=10' \
--data-urlencode 'var5=A****J'
```

</details> 

<details> <summary>Response parameters</summary>

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
    "2-1": "This parameter contains the transaction details in an array format and it is displayed only when the **status** field returns the value as **1**. For more information on each field in the array, refer to the next table."
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

**Success scenario**

```
{
    "status": 1,
    "msg": "Transaction Fetched Successfully",
    "Transaction_details": [
        {
            "id": "412345678912384187",
            "status": "captured",
            "key": "A****J",
            "merchantname": "Aggregator-OwnChild",
            "txnid": "6de4dc8abc38473122cb",
            "base_id": "412345678912384184",
            "firstname": "Payu-Admin",
            "lastname": "",
            "addedon": "2021-12-30 13:59:01",
            "bank_name": "Credit Cards",
            "payment_gateway": "AxisCYBER",
            "phone": "1234567890",
            "email": "test@example.com",
            "transaction_fee": "2.00",
            "amount": "2.00",
            "discount": "0.00",
            "additional_charges": "0.00",
            "productinfo": "Product Info",
            "error_code": "E000",
            "bank_ref_no": "2516463285587866763243",
            "ibibo_code": "CC",
            "mode": "CC",
            "address2": "",
            "city": "",
            "zipcode": "",
            "pg_mid": null,
            "offer_type": null,
            "splitCreated": null,
            "is_parent_transaction": false,
            "splitInfo": null
        },
        {
            "id": "412345678912384190",
            "status": "captured",
            "key": "A****J",
            "merchantname": "Aggregator-OwnChild",
            "txnid": "6de4dc8abc38473122cb",
            "base_id": "412345678912384184",
            "firstname": "Payu-Admin",
            "lastname": "",
            "addedon": "2021-12-30 13:59:06",
            "bank_name": "Credit Cards",
            "payment_gateway": "AxisCYBER",
            "phone": "1234567890",
            "email": "test@example.com",
            "transaction_fee": "2.00",
            "amount": "2.00",
            "discount": "0.00",
            "additional_charges": "0.00",
            "productinfo": "Product Info",
            "error_code": "E000",
            "bank_ref_no": "2516463285587866763243",
            "ibibo_code": "CC",
            "mode": "CC",
            "address2": "",
            "city": "",
            "zipcode": "",
            "pg_mid": null,
            "offer_type": null,
            "splitCreated": null,
            "is_parent_transaction": false,
            "splitInfo": null
        }
    ]
}
```

> 📘 Note:
> 
> If the response has three pages and you submit 4 in the var3 parameter of the request, you will get the Transaction_Details parameter value in the response as blank.

**Failure scenario**

```
{
    "status": 0,
    "msg": "Invalid Hash."
}
```

</details>

## Request parameters