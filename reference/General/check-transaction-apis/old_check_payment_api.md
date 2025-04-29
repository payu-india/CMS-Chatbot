---
title: Check Payment API
excerpt: ''
api:
  file: general-30.json
  operationId: CheckPaymentAPI
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The Check Payment (**check\_payment**) API functions similar to the [Verify Payment API](ref:verify_payment_api). However, the input parameter in this API is the PayUID or mihpayuID generated at PayU’s Server unlike **verify\_payment** API where the input parameter is the TxnID (Transaction ID generated at merchant’s server). It returns all the parameters for a given transaction.

<GENERALAPIsEnvironment />

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
        This parameter returns the status of web service call. The status can be any of the following:

        * 0 - If web service call failed.
        * 1 - If web service call succeeded
      </td>
      <td>
        0
      </td>
    </tr>
    <tr>
      <td>
        msg
      </td>
      <td>
        This parameter returns the reason string.
      </td>
      <td>
        For example, any of the following messages are displayed:

        * Parameter missing
        * Token is empty
        * Amount is empty
        * Transaction not exists
      </td>
    </tr>
    <tr>
      <td>
        transaction\_details
      </td>
      <td>
        This parameter contains the response in a JSON format. For more information refer to [JSON fields description for transaction\_details parameter ](#json-field-description-for-transaction_details-parameter).
      </td>
      <td>

      </td>
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