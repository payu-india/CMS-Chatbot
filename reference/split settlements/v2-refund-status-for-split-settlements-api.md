---
title: Refund Status API for Split Settlements
deprecated: false
hidden: true
metadata:
  robots: index
---
The *** API helps you to fetch the refund status of transactions where the refunds are for split payments.

> 📘 Note:
>
> The **aggregator\_check\_action\_status\_txnid** must be used only to check the split transactions’ refund status

**Endpoint**

|                        |                                                                              |
| :--------------------- | :--------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/v2/refundstatus](https://test.payu.in/v2/refundstatus) |
| Production Environment | [https://info.payu.in/v2/refundstatus](https://info.payu.in/v2/refundstatus) |

## Request parameters

### Request headers

<V2_payment_header_params />

### Body parameters

> 📘 Note:
>
> At least one of the following parameters must be provided: `requestId`, `payuId`, or `tokenId`.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        requestId
        `conditional`
      </td>

      <td>
        `String Array `Array of request IDs for which the refund information is required.
      </td>

      <td>
        `["11763053990", "11763053112"]`
      </td>
    </tr>

    <tr>
      <td>
        payuId
        `conditional`
      </td>

      <td>
        `String Array `Array of PayU transaction IDs or PayU ID for which the refund information is required. Payu ID (mihpayuid) that you receive in the response for a successful payment transaction.
      </td>

      <td>
        `["11763053990"]`
      </td>
    </tr>

    <tr>
      <td>
        tokenId
        `conditional`
      </td>

      <td>
        `String Array `This parameter must contain the Token ID (unique token from the merchant) for the refund request. Token ID has to be generated at your end for each new refund request. It is an identifier for each new refund request which can be used for tracking it. It must be unique for every new refund request generated – otherwise the refund request would not be generated successfully. Token ID length should not be greater than 23 characters
      </td>

      <td>
        `["TOKEN12345"]`
      </td>
    </tr>
  </tbody>
</Table>

### Sample request

```bash
curl --location 'https://test.payu.in/v2/refundstatus' \
--header 'mid: 8759546' \
--header 'Content-Type: application/json' \
--header 'Info-Command: aggregator_check_action_status_txnid' \
--header 'Date: Thu, 17 Feb 2022 08:17:59 GMT' \
--header 'Digest: vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=' \
--header 'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI="' \
--header 'platformId: 1' \
--data '{
    "requestId": null,
    "payuId": ["11763053990"],
    "tokenId": null
}'
```

## Response parameters

| Parameter        | Description                                                                                                                                                                                    | Example                                             |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| status           | This parameter returns the status of web service call. The status can be any of the following:<br /><br />\_ **0** - If web service call failed.<br />\_ **1** - If web service call succeeded | 1                                                   |
| msg              | Displays the response message.                                                                                                                                                                 |                                                     |
| payuid           | Displays the PayU ID that was submitted in the request.                                                                                                                                        | 14370578416                                         |
| transactionItems | A JSON returning the details of transaction before the split.                                                                                                                                  | Refer to [transactionItems](#transactionitems-json) |
| splitItems       | A JSON returning the details of transaction and refunds against each merchant key (including child key)                                                                                        | Refer to [splititems JSON](#splititems-json)        |

### transactionItems JSON

The **transactionItems** JSON that is part of the response for a successful transaction is similar to the following:

```
  "transactionItems": {
    "iDJYfd": {
      "capture": {
        "txnid": "PB21524761S",
        "merKey": "iDJYfd",
        "mihpayid": "14706907828",
        "bank_ref_num": "220448967168",
        "request_id": "10208412464",
        "amt": "2445.00",
        "payu_code": "NB",
        "action": "capture",
        "token": "",
        "status": "SUCCESS",
        "bank_arn": null,
        "settlement_id": null,
        "isSubvention": "0",
        "amount_settled": "0.0000",
        "UTR_no": null,
        "value_date": null,
        "prev_status": null,
        "refund_mode": "-"
      }
    }
```

### splitItems JSON

The **splitItems** JSON that is part of the response for a successful transaction is similar to the following:

```
"splitItems": {
    "Slcv2Q": {
      "capture": {
        "mihpayid": "14707170968",
        "bank_ref_num": "220448967168",
        "request_id": "10208598167",
        "amt": "2445.00",
        "payu_code": "NB",
        "action": "capture",
        "token": null,
        "status": "SUCCESS",
        "bank_arn": null,
        "settlement_id": "202202151245",
        "isSubvention": "0",
        "amount_settled": "2445.0000",
        "UTR_no": "202150832553",
        "value_date": "2022-02-15",
        "refund_mode": "-"
      },
      "refund": {
        "969750": {
          "mihpayid": "14707170968",
          "bank_ref_num": null,
          "request_id": "10241480197",
          "amt": "2445.00",
          "payu_code": "NB",
          "action": "refund",
          "token": "969750",
          "status": "SUCCESS",
          "bank_arn": "220448967168",
          "settlement_id": "202202251245",
          "isSubvention": "0",
          "amount_settled": "-2445.0000",
          "UTR_no": "202254321504",
          "value_date": "2022-02-25",
          "refund_mode": "Back to Source"
        }
      }
    }
  }
```

### Failure response

```json
{
  "status": 0,
  "msg": "0 out of 1 Transactions Fetched Successfully",
  "transaction_details": {
    "16988019552": "No action status found value of var1 sent in the request"
  }
}
```