---
title: Check Refund Status API with PayU ID
excerpt: 'API Command: **check_action_status**'
api:
  file: general-24.json
  operationId: check_action_status(2ndusage)
deprecated: false
hidden: false
metadata:
  title: Check Refund Status API with PayU ID
  description: >-
    The **check_action_status** API returns the status of capture, refund, and
    cancel requests for a specific PayUID. More information on payment states
    can be found in the [Payment States
    Explanations](https://docs.payu.in/reference/payment-state-explanations)
    document.
  keywords:
    - Check Refund Status API with PayU ID
    - ' check_action_status API Command'
    - ' Using PayU ID to Check Refund Status API'
  robots: index
next:
  description: ''
  pages:
    - type: endpoint
      slug: check_action_status_api_with_request_id
      title: Check Refund Status API with Request ID
    - type: endpoint
      slug: refund_transaction_api
      title: Refund Transaction API
---
The **check\_action\_status** API has another usage too. For a particular PayUID, it returns any of the following the states:

<RefundStates />

<GENERALAPIsEnvironment />

## Reference information for request parameters

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>
      <th>
        Reference
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        key
      </td>
      <td>
        For more information on how to generate the Key and Salt, refer to any of the following:  

        \- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  

        * **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
      </td>
    </tr>
    <tr>
      <td>
        hash
      </td>
      <td>
        Hash logic for this API is: sha512(key\|command\|var1\|salt) sha512
      </td>
    </tr>
  </tbody>
</Table>

<details>
  <summary>Sample request</summary>

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d

"key=JP***g&command=check_action_status&var1=403993715521937565&var2=payuid&hash=81bdb5b8e625f254398d744269844fc6b9d87b3782670331c2a6b856f42f315b9898f397df7292cfd33a6153abf4acac58ce3ac671e41999ff81d98ce432f48e"
```

**Failure scenarios**

* If mihpayid is not found, the response is similar to the following:

```plaintext
{
      "status": 0,
      "msg": "0 out of 1 Transactions Fetched Successfully",
      "transaction_details": {
            "13127842": "No action status found"
      }
}
```

* If mihpayid is missing, the response is similar to the following:

```plaintext
{
      "status": 0,
      "msg": "Parameter missing"
}
```

</details>

<details>
  <summary>Sample response</summary>

On successful processing from PayU, the response is similar to the following:

```plaintext
{
      "status": 1,
      "msg": "1 out of 1 Transactions Fetched Successfully",
      "transaction_details": {
            "403993715521937565": {
                  "131278418": {
                        "mihpayid": "403993715521937565",
                        "bank_ref_num": "399900",
                        "request_id": "131278418",
                        "amt": "100.00",
                        "mode": "CC",
                        "action": "capture",
                        "token": "",
                        "status": "SUCCESS",
                        "bank_arn": null,
                        "settlement_id": null,
                        "amount_settled": null,
                        "UTR_no": null,
                        "value_date": null,
                        "refund_mode": "-"
                  },
                  "131278422": {
                        "mihpayid": "403993715521937565",
                        "bank_ref_num": "527013524405",
                        "request_id": "131278422",
                        "amt": "10.00",
                        "mode": "CC",
                        "action": "refund",
                        "token": "RefundToken1",
                        "status": "success",
                        "bank_arn": null,
                        "settlement_id": null,
                        "amount_settled": null,
                        "UTR_no": null,
                        "value_date": null,
                        "refund_mode": "Back to Source"
                  },
                  "131278430": {
                        "mihpayid": "403993715521937565",
                        "bank_ref_num": "527013524405",
                        "request_id": "131278430",
                        "amt": "10.00",
                        "mode": "CC",
                        "action": "refund",
                        "token": "RefundToken2",
                        "status": "success",
                        "bank_arn": null,
                        "settlement_id": null,
                        "amount_settled": null,
                        "UTR_no": null,
                        "value_date": null,
                        "refund_mode": "Back to Source"
                  },
                  "131278458": {
                        "mihpayid": "403993715521937565",
                        "bank_ref_num": "527013524405",
                        "request_id": "131278458",
                        "amt": "10.00",
                        "mode": "CC",
                        "action": "refund",
                        "token": "RefundToken3",
                        "status": "success",
                        "bank_arn": null,
                        "settlement_id": null,
                        "amount_settled": null,
                        "UTR_no": null,
                        "value_date": null,
                        "refund_mode": "Back to Source"
                  },
                  "131278471": {
                        "mihpayid": "403993715521937565",
                        "bank_ref_num": "527013524405",
                        "request_id": "131278471",
                        "amt": "10.00",
                        "mode": "CC",
                        "action": "refund",
                        "token": "RefundToken4",
                        "status": "success",
                        "bank_arn": null,
                        "settlement_id": null,
                        "amount_settled": null,
                        "UTR_no": null,
                        "value_date": null,
                        "refund_mode": "Back to Source"
                  },
                  "131278484": {
                        "mihpayid": "403993715521937565",
                        "bank_ref_num": "527013524405",
                        "request_id": "131278484",
                        "amt": "10.00",
                        "mode": "CC",
                        "action": "refund",
                        "token": "RefundToken5",
                        "status": "success",
                        "bank_arn": null,
                        "settlement_id": null,
                        "amount_settled": null,
                        "UTR_no": null,
                        "value_date": null,
                        "refund_mode": "Back to Source"
                  },
                  "131278499": {
                        "mihpayid": "403993715521937565",
                        "bank_ref_num": "527013524405",
                        "request_id": "131278499",
                        "amt": "10.00",
                        "mode": "CC",
                        "action": "refund",
                        "token": "RefundToken6",
                        "status": "success",
                        "bank_arn": null,
                        "settlement_id": null,
                        "amount_settled": null,
                        "UTR_no": null,
                        "value_date": null,
                        "refund_mode": "Back to Source"
                  },
                  "131278515": {
                        "mihpayid": "403993715521937565",
                        "bank_ref_num": "527013524405",
                        "request_id": "131278515",
                        "amt": "10.00",
                        "mode": "CC",
                        "action": "refund",
                        "token": "RefundToken7",
                        "status": "success",
                        "bank_arn": null,
                        "settlement_id": null,
                        "amount_settled": null,
                        "UTR_no": null,
                        "value_date": null,
                        "refund_mode": "Back to Source"
                  },
                  "131287648": {
                        "mihpayid": "403993715521937565",
                        "bank_ref_num": "527013524405",
                        "request_id": "131287648",
                        "amt": "10.00",
                        "mode": "CC",
                        "action": "refund",
                        "token": "RefundToken8",
                        "status": "success",
                        "bank_arn": null,
                        "settlement_id": null,
                        "amount_settled": null,
                        "UTR_no": null,
                        "value_date": null,
                        "refund_mode": "Back to Source"
                  },
                  "131295795": {
                        "mihpayid": "403993715521937565",
                        "bank_ref_num": "527013524405",
                        "request_id": "131295795",
                        "amt": "10.00",
                        "mode": "CC",
                        "action": "refund",
                        "token": "RefundToken9",
                        "status": "success",
                        "bank_arn": null,
                        "settlement_id": null,
                        "amount_settled": null,
                        "UTR_no": null,
                        "value_date": null,
                        "refund_mode": "Back to Source"
                  },
                  "131297379": {
                        "mihpayid": "403993715521937565",
                        "bank_ref_num": "527013524405",
                        "request_id": "131297379",
                        "amt": "10.00",
                        "mode": "CC",
                        "action": "refund",
                        "token": "RefundToken10",
                        "status": "success",
                        "bank_arn": null,
                        "settlement_id": null,
                        "amount_settled": null,
                        "UTR_no": null,
                        "value_date": null,
                        "refund_mode": "Back to Source"
                  }
            }
      }
}
```

</details>

<details>
  <summary>Response parameters</summary>

The **transaction\_details** parameter of the response is in JSON format. For more information, refer to [Additional Info for General APIs](/reference/addl-info-general-apis#response-parameters-check-refund-status-with-request-idpayu-id-or-get-transaction-details).

</details>

## Request parameters

<details>
  <summary>Response parameters</summary>

<KeyHashForGeneralParametersDescription />

</details>

**Example values**

Use the following sample values while trying out the API:

* `var1` (mihpayid): 403993715521937565
* `var2`: payuid