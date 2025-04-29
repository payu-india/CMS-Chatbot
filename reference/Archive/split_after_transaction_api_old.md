---
title: OLD-Split After Transaction API
excerpt: ''
api:
  file: payu-biz-aggregator.json
  operationId: paymentsplit
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
You must specify two decimal places for each split, but ensure the sum split amounts are equal to the transaction amount.

> 📘 Note:
>
> You must specify two decimal places for each split, but ensure the sum of the percentage of all splits is equal to 100.

HTTP Method: **POST**

**Environment**

| Test Environment       | [https://test.payu.in/\_payment](https://test.payu.in/_payment) |
| :--------------------- | :-------------------------------------------------------------- |
| Production Environment | [https://info.payu.in/\_payment](https://info.payu.in/_payment) |

## Request parameters

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
        **Sample Value**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key
      </td>

      <td>
        `string` This parameter must include the Merchant key that was provided by PayU.
      </td>

      <td>
        vDy3i7
      </td>
    </tr>

    <tr>
      <td>
        command
      </td>

      <td>
        `string` The parameter must contain the name of the web service.
      </td>

      <td>
        payment\_split
      </td>
    </tr>

    <tr>
      <td>
        hash
      </td>

      <td>
        `String` The hash string encryption is specified in this parameter. The format of the hash is:\
        |sha512(key|command|var1|salt)\
        Where, var1 contains the fields as described in the var1 description.
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        var1
      </td>

      <td>
        `string (JSON)` This parameter is in a JSON format and fields included in the JSON format are explained the [JSON request structure table](#json-request-structure).
      </td>

      <td>
        For an example, refer the [Request Structure](#request-structure-for-var1-to-be-included-in--payment_split-api) subsection.
      </td>
    </tr>
  </tbody>
</Table>

## Request structure for var1 to be included in  payment\_split API

```plaintext
{  "type": "absolute",  
    "payuId": "xxxxxxxx", # PayuID of parent transaction which needs to be split.  
   "splitInfo": 
    {    
       "merchantKey1": 
       {
       "aggregatorSubTxnId": "30nknyhkhib",
       "aggregatorSubAmt": "8",
       "aggregatorCharges": "2" // parent merchant commission (Optional)    
       },
      "merchantKey2":
      {
       "aggregatorSubTxnId": "13u0nknou0",
       "aggregatorSubAmt": "2"
      },
       "merchantKey3":
       {
        "aggregatorSubTxnId": "13u0nknou02",
        "aggregatorSubAmt": "2",
        "aggregatorCharges": "1" // parent merchant commission (Optional)
       }
     }
}
```

## JSON request structure

The **var1** parameter is in JSON format. The fields in the JSON format are described in the following table:

<Table>
  <thead>
    <tr>
      <th>
        **Field**
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
        type
      </td>

      <td>
        The type of split is specified in this field. Use **absolute** in this field. The absolute amount is specified for each part of the split. The absolute amount is specified in the aggregatorSubAmt field of the JSON for each child or aggregator.
      </td>

      <td>
        absolute
      </td>
    </tr>

    <tr>
      <td>
        payuid
      </td>

      <td>
        The payment identifier provided by PayU for the transaction.
      </td>

      <td>
        403993715525003544
      </td>
    </tr>

    <tr>
      <td>
        splitInfo
      </td>

      <td>
        This parameter must include the list of aggregator sub transaction IDs and sub amounts as specified in the [Request Structure for var1](#request-structure-for-var1-to-be-included-in--payment_split-api) subsection:  

        * **aggregatorSubTxnId**: The aggregator sub transaction ID is specified in this field.  

        * **aggregatorSubAmt**: The aggregator sub amount is specified in this field.  

        * **aggregatorCharges**: The aggregator charges is specified in this field.  

        * \*Note\*\*: The aggregatorCharges field can only be used by parent merchant to get the aggregator commission.
      </td>

      <td>
        Refer to [Request Structure for var1](#request-structure-for-var1-to-be-included-in--payment_split-api) subsection.
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```curl
curl -X POST "https://info.payu.in/merchant/postservice?form=2"
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
“key=A6lB8r&command=payment_splity&var1="type":"absolute","payuId":"403993715525003544","splitInfo":{"imAJ7I":{"aggregatorSubTxnId":"CHild101","aggregatorSubAmt":"50"},"qOoYIv":{"aggregatorSubTxnId":"Child202","aggregatorSubAmt":"50"}}}&hash=6692a8b560c51e8a4bb830206d3b8fac3678fb5b08443c7590047545beba66ec97257fec11775abbc339eabbaf1b1bf5e1c50d2c6bbf67e1a69ad597480d3691"
```

## Sample response

* Sample response for a successful split:

When split get saved & created

```plaintext
{
  "status": 1,
  "message": "Splits creation successful.",
  "splitStatus": "success",
  "splitSegments": [
    {
      "merchantKey": "imAJ7I",
      "amount": 50,
      "subvention_amount": 0,
      "txnId": "CHild101",
      "additional_charges": 0,
      "transaction_fee": 50    },
    {
      "merchantKey": "qOoYIv",
      "amount": 50,
      "subvention_amount": 0,
      "txnId": "Child202",
      "additional_charges": 0,
      "transaction_fee": 50    },
  ]
}
```

* Sample response when split gets saved but are not yet created:

When split get saved but aren’t yet created)

```plaintext
{
  "status": 2,
  "message": "Splits saved, but not created yet",
  "splitStatus": "PENDING"
}
```

* Split creation is failed:

In this sample response, the **error\_code** and **error\_desc** parameters display based on the failure. For the list of error\_codes, refer to [Error Codes & Error Messages](https://devguide.payu.in/split-apis/steps-to-create-the-split/payment_split-api/#Error).

```plaintext
{
  "status": 0,
  "error_code": "AGG-107"
  "error_desc": "Invalid split payload in payment request"
}
```

## Error codes & messages

| **Condition**                                           | **error\_code** | **error\_message**                                                    |
| ------------------------------------------------------- | --------------- | --------------------------------------------------------------------- |
| Invalid request posted by merchant in var1              | AGG-107         | Invalid split payload in payment request                              |
| Invalid parent payuId                                   | AGG-103         | This transaction is not a aggregator flow base transaction            |
| Split already exists for requested PayUId               | AGG-104         | Split info already exists for this transaction                        |
| Invalid Child merchant in split requeset                | AGG-102         | One or more child merchant-keys provided are invalid                  |
| If sum amount won’t match wrt parent transaction amount | AGG-108         | Total amount provided in split doesn\\'t match the transaction amount |
| If merchant is not Aggregator flow merchant.            | AGG-101         | This merchant is not an Aggregator flow merchant.                     |
| When transaction is locked in other process             | AGG-110         | Some exception occurred. Try after sometime.                          |

> 📘 Note:
>
> API integration and authentication would be the same as that for general transaction flow.
