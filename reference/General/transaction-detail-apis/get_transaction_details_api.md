---
title: Get Transaction Details API
excerpt: ''
api:
  file: get-transaction-details-7.json
  operationId: GetTransactionDetails
deprecated: false
hidden: false
metadata:
  title: Get Transaction Details API
  description: >-
    The Get Transaction Details API retrieves transaction details between two
    specified dates, providing information such as transaction status, amount,
    and payment method in an array format.
  keywords:
    - get_Transaction_Details API Command
    - get_Transaction_Details command
    - Get Transaction Details API
  robots: index
next:
  description: ''
---
The Get Transaction Details **(get\_Transaction\_Details)** API works based on input as two dates (initial and final), between which the transaction details are needed. The output consists of the status of the API (success or failure) and all the transaction details in an array format.

### Environment

The Check Payment (**check\_payment**) API functions similar to the [Verify Payment API](ref:verify_payment_api). However, the input parameter in this API is the PayUID or mihpayuID generated at PayU’s Server unlike **verify\_payment** API where the input parameter is the TxnID (Transaction ID generated at merchant’s server). It returns all the parameters for a given transaction.

**Environment**

|                        |                                                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| Test Environment       | [https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2) |
| Production Environment | [https://info.payu.in/merchant/postservice.php?form=2](https://info.payu.in/merchant/postservice.php?form=2) |

<details>
  <summary>Sample request</summary>

```curl
curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=vzKCT7' \
--data-urlencode 'command=check_payment' \
--data-urlencode 'var1=403993715530075847' \
--data-urlencode 'hash=d03c7c49929fd9a07fe7f70c3609a8e245c64b2d7959c01193b4a4f85b6e138b468af8debb44fdb6fbb57d0bd5d96bf881cd88e494f8ce273172297faf5da9db'
```

</details>

<details>
  <summary>Sample response</summary>

### Success scenario

```plaintext
{
    "status": 1,
    "msg": "Transaction Fetched Successfully",
    "transaction_details": {
        "request_id": 135958975,
        "bank_ref_num": "7103714673656711773162",
        "net_amount": null,
        "mihpayid": 403993715530075847,
        "amt": "10.00",
        "disc": "0.00",
        "mode": "CC",
        "txnid": "d721fcf124b54e56989f",
        "amount": "10.00",
        "amount_paid": "10.00",
        "discount": "0.00",
        "additional_charges": "0.00",
        "udf1": "",
        "udf2": "",
        "udf3": "",
        "udf4": "",
        "udf5": "",
        "field1": "7103714673656711773162",
        "field2": "966739",
        "field3": "10.00",
        "field4": null,
        "field5": "100",
        "field6": "02",
        "field7": "AUTHPOSITIVE",
        "field8": null,
        "field9": "Transaction is Successful",
        "addedon": "2023-09-12 14:50:48",
        "status": "success",
        "net_amount_debit": 10,
        "unmappedstatus": "captured",
        "firstname": "Payu-Admin",
        "bankcode": "CC",
        "productinfo": "Product Info",
        "payment_source": "payu",
        "name_on_card": null,
        "card_no": "XXXXXXXXXXXX2346",
        "PG_TYPE": "AxisCYBER",
        "Merchant_UTR": null,
        "Settled_At": null
    }
}
```

### Failure scenario

* If the PayU ID (mihpayuid) is missing:

```
{
"status":0,"msg":"Some error occurred while processing the request."
}
```

</details>

<details>
  <summary>Response parameters</summary>

<Table>
  <thead>
    <tr>
      <th>**Parameter**</th>
      <th>**Description**</th>
      <th>**Example**</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>status</td>
      <td>
        This parameter returns the status of web service call. The status can be any of the following:

        * 0 - If web service call failed.
        * 1 - If web service call succeeded
      </td>
      <td>0</td>
    </tr>
    <tr>
      <td>msg</td>
      <td>This parameter returns the reason string.</td>
      <td>
        For example, any of the following messages are displayed:

        * Parameter missing
        * Token is empty
        * Amount is empty
        * Transaction not exists
      </td>
    </tr>
    <tr>
      <td>transaction\_details</td>
      <td>
        This parameter contains the response in a JSON format. For more information refer to [JSON fields description for transaction\_details parameter ](#json-field-description-for-transaction_details-parameter).
      </td>
      <td></td>
    </tr>
  </tbody>
</Table>

</details>

## Request parameters

<details>
  <summary>Reference information for request parameters</summary>

<KeyHashForGeneralParametersDescription />

</details>

**Sample values**

Use the following sample values while trying out the API:

* `var1` (your transaction ID/order ID): 403993715521889530

<details>
  <summary>Sample request</summary>

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d

"key=JP***g&command=get_Transaction_Details&var1=2020-10-20&var2=2020-10-27&hash=0545c11641bd91ed7ba2b5c937480b0f8737962ccc4959994f2aa950ca16212283e7c440a4251ffebd725e0c2c2c03701186eec82c8dd667e75dfbb3cba8e634"
```

</details>

<details>
  <summary>Sample response</summary>

* Success scenario

```plaintext
{
      "status": 1,
      "msg": "Transaction Fetched Successfully",
      "Transaction_details": [
            {
                  "id": "403993715521889443",
                  "status": "captured",
                  "key": "JPM7Fg",
                  "merchantname": "demo",
                  "txnid": "02fdb4f0a0decd1e4937",
                  "firstname": "Ashish",
                  "lastname": "Kumar",
                  "addedon": "2020-10-26 13:54:52",
                  "bank_name": "Credit Card",
                  "payment_gateway": "AXISPG",
                  "phone": "9876543210",
                  "email": "ashish25@mailinator.com",
                  "transaction_fee": "10.00",
                  "amount": "10.00",
                  "discount": "0.00",
                  "additional_charges": "0.00",
                  "productinfo": "iPhone",
                  "error_code": "E000",
                  "bank_ref_no": "895255",
                  "ibibo_code": "CC",
                  "mode": "CC",
                  "ip": "106.202.49.52",
                  "card_no": "512345XXXXXX2346",
                  "cardtype": "domestic",
                  "offer_key": "",
                  "field2": "171519",
                  "udf1": "",
                  "pg_mid": null,
                  "offer_type": null,
                  "failure_reason": null,
                  "mer_service_fee": "0.00",
                  "mer_service_tax": "0.00"
            },
            {
                  "id": "403993715521889519",
                  "status": "failed",
                  "key": "JPM7Fg",
                  "merchantname": "demo",
                  "txnid": "4c5355da12224188d0ff",
                  "firstname": "K",
                  "lastname": "K",
                  "addedon": "2020-10-26 14:10:02",
                  "bank_name": "Credit Card",
                  "payment_gateway": "AXISPG",
                  "phone": "09599736876",
                  "email": "ashish.25cca@gmail.com",
                  "transaction_fee": "10.00",
                  "amount": "10.00",
                  "discount": "0.00",
                  "additional_charges": "0.00",
                  "productinfo": "i Phone",
                  "error_code": null,
                  "bank_ref_no": "372218",
                  "ibibo_code": "CC",
                  "mode": "CC",
                  "ip": "106.202.49.52",
                  "card_no": "512345XXXXXX2346",
                  "cardtype": "domestic",
                  "offer_key": "",
                  "field2": "603129",
                  "udf1": "",
                  "pg_mid": null,
                  "offer_type": null,
                  "failure_reason": null,
                  "mer_service_fee": null,
                  "mer_service_tax": null
            },
            {
                  "id": "403993715521891555",
                  "status": "captured",
                  "key": "JPM7Fg",
                  "merchantname": "demo",
                  "txnid": "e3bb0408ef94af722de5",
                  "firstname": "Ashish",
                  "lastname": "Kumar",
                  "addedon": "2020-10-26 20:59:41",
                  "bank_name": "Credit Card",
                  "payment_gateway": "AXISPG",
                  "phone": "0987654321",
                  "email": "ashish.kumar@payu.in",
                  "transaction_fee": "10.00",
                  "amount": "10.00",
                  "discount": "0.00",
                  "additional_charges": "0.00",
                  "productinfo": "iPhone",
                  "error_code": "E000",
                  "bank_ref_no": "734154",
                  "ibibo_code": "CC",
                  "mode": "CC",
                  "ip": "106.202.39.89",
                  "card_no": "512345XXXXXX2346",
                  "cardtype": "domestic",
                  "offer_key": "",
                  "field2": "157887",
                  "udf1": "",
                  "pg_mid": null,
                  "offer_type": null,
                  "failure_reason": null,
                  "mer_service_fee": "0.00",
                  "mer_service_tax": "0.00"
            }
      ]
}
```

* Failure scenario

If transaction is not found, the response is similar to the following:

```
{
      "status": 1,
      "msg": "Transaction Fetched Successfully",
      "Transaction_details": []
}
```

If invalid date is posted, the response is similar to the following:

```plaintext
{
      "status": 0,
      "msg": "Invalid Date Entered. Date format should be yyyy-mm-dd"
}
```

</details>

<details>
  <summary>Response parameters</summary>

Transaction\_details parameter of the response is in the JSON format. For the details of the fields in the JSON format, refer to [Additional Info for General APIs](ref:addl-info-general-apis).

To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes). 

</details>

## Request parameters

<details>
  <summary>Reference information for request parameters</summary>

<KeyHashForGeneralParametersDescription />

</details>

**Sample values**

Use the following sample values while trying out the API:

* `var1`: 2020-10-20
* `var2`: 2020-10-27