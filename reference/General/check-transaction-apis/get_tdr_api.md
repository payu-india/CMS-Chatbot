---
title: Get TDR API
excerpt: ''
api:
  file: general-33.json
  operationId: get_TDR
deprecated: false
hidden: false
metadata:
  title: Get TDR API
  description: >-
    The Get TDR API retrieves the Transaction Discount Rate (TDR) value of a
    transaction with PayU by providing the PayU ID of the transaction as input.
    The output includes the TDR value, with a sample request and response
    provided in the document.
  keywords:
    - Get Transaction Discount Rate API
    - Get TDR API
    - get_TDR command
    - get_TDR API Command
  robots: index
next:
  description: ''
---
The Get TDR API (**get\_TDR** API) is used to get the Transaction Discount Rate (TDR) value of a transaction with PayU. It is a simple API for which you need to provide the PayU ID of the transaction as input and the TDR value is returned in the output, var1 is Payu id (mihpayid) of the transaction.

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
curl -X POST "https://test.payu.in/merchant/postservice?form=2"-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d"key=JP***g&command=get_TDR&var1=403993715521891555&hash=a0cf2d4ed3fb551388bd9e078f7ace8fb565d3240e06735cfc83330bb604b0f97a26a31160f1987af4ba5f78e126f400826a62d71337395e6e127b28a62b860d"
```

</details>

<details>
  <summary>Sample response</summary>

**Success scenario**

```
{
      "status": 1,
      "msg": "Transaction Fetched Successfully",
      "TDR_details": {
            "TDR": 0
      }
}
```

**Failure scenario**

* If mihpayid is not found

```
{
      "status": 0,
      "msg": "Invalid PayU ID"
}
```

</details>

## Request parameters

<details>
  <summary>Reference information for request parameters</summary>

<KeyHashForGeneralParametersDescription />

</details>

**Sample values**

Use the following sample values while trying out the API:

* `var1` (Payu ID/mihpayid): 403993715521891555