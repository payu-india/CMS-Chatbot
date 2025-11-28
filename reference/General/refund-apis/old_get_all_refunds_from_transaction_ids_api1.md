---
title: '[OLD]Get All Refunds from Transaction IDs API'
api:
  file: get-all-refunds-for-txnid-3.json
  operationId: GetAllRefundsfromTransactionIDs
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  title: Get All Refunds for a Transaction IDs API
  description: >-
    The document describes the **Get All Refunds for a Transaction ID** API
    command, which retrieves the status of all refund requests for a specific
    Transaction ID, providing details such as request ID, payment gateway used,
    refund status, and creation date.
  keywords:
    - getAllRefundsFromTxnIds API Command
    - ' Get All Refunds from Transaction IDs'
    - ' Get All Refunds API'
  robots: index
---
The **Get All Refunds for a Transaction ID** API (getAllRefundsFromTxnIds) command is used to retrieve the status of all the refund requests fired for a particular Transaction ID. The output of this API provides the request ID, and the PG used the status of a refund request and the creation of refund date information. It returns any of the following the states:

<RefundStates />

<GENERALAPIsEnvironment />

<details>
  <summary>Sample request</summary>

  ```curl
  curl -X POST "https://test.payu.in/merchant/postservice?form=2
  -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d

  "key=JP***g&command=getAllRefundsFromTxnIds&var1=db97dd56eff7296e5061&hash=69543c08018121cc882d2f8b1761567367c1806becde3db7f54ab552362677cc08d8dfa4b9411e234e4876e6aba80c05a32e75ed499aff458c7f6027bf4ef2a8"
  ```
</details>

<details>
  <summary>Sample response</summary>

  **Success Scenario**

  On successful processing from PayU, the response is similar to the following:

  ```json
  {
        "status": 1,
        "msg": "Refunds fetched successfully.",
        "Refund Details": {
              "403993715521937565": [
                    {
                          "PayuID": "403993715521937565",
                          "RequestID": "131278422",
                          "RefundToken": "RefundToken1",
                          "PaymentGateway": "AXISPG",
                          "Amount": "10.00",
                          "Status": "success",
                          "RefundCreationDate": "2020-11-05 01:23:19",
                          "bank_ref_no": "527013524405",
                          "bank_arn": null,
                          "success_at": "2020-11-05 01:24:04"
                    },
                    {
                          "PayuID": "403993715521937565",
                          "RequestID": "131278430",
                          "RefundToken": "RefundToken2",
                          "PaymentGateway": "AXISPG",
                          "Amount": "10.00",
                          "Status": "success",
                          "RefundCreationDate": "2020-11-05 01:29:13",
                          "bank_ref_no": "527013524405",
                          "bank_arn": null,
                          "success_at": "2020-11-05 01:30:08"
                    },
                    {
                          "PayuID": "403993715521937565",
                          "RequestID": "131278458",
                          "RefundToken": "RefundToken3",
                          "PaymentGateway": "AXISPG",
                          "Amount": "10.00",
                          "Status": "success",
                          "RefundCreationDate": "2020-11-05 01:47:36",
                          "bank_ref_no": "527013524405",
                          "bank_arn": null,
                          "success_at": "2020-11-05 01:49:04"
                    },
                    {
                          "PayuID": "403993715521937565",
                          "RequestID": "131278471",
                          "RefundToken": "RefundToken4",
                          "PaymentGateway": "AXISPG",
                          "Amount": "10.00",
                          "Status": "success",
                          "RefundCreationDate": "2020-11-05 01:53:28",
                          "bank_ref_no": "527013524405",
                          "bank_arn": null,
                          "success_at": "2020-11-05 01:55:05"
                    },
                    {
                          "PayuID": "403993715521937565",
                          "RequestID": "131278484",
                          "RefundToken": "RefundToken5",
                          "PaymentGateway": "AXISPG",
                          "Amount": "10.00",
                          "Status": "success",
                          "RefundCreationDate": "2020-11-05 01:58:32",
                          "bank_ref_no": "527013524405",
                          "bank_arn": null,
                          "success_at": "2020-11-05 02:00:09"
                    },
                    {
                          "PayuID": "403993715521937565",
                          "RequestID": "131278499",
                          "RefundToken": "RefundToken6",
                          "PaymentGateway": "AXISPG",
                          "Amount": "10.00",
                          "Status": "success",
                          "RefundCreationDate": "2020-11-05 02:05:42",
                          "bank_ref_no": "527013524405",
                          "bank_arn": null,
                          "success_at": "2020-11-05 02:07:04"
                    },
                    {
                          "PayuID": "403993715521937565",
                          "RequestID": "131278515",
                          "RefundToken": "RefundToken7",
                          "PaymentGateway": "AXISPG",
                          "Amount": "10.00",
                          "Status": "success",
                          "RefundCreationDate": "2020-11-05 02:15:11",
                          "bank_ref_no": "527013524405",
                          "bank_arn": null,
                          "success_at": "2020-11-05 02:16:03"
                    },
                    {
                          "PayuID": "403993715521937565",
                          "RequestID": "131287648",
                          "RefundToken": "RefundToken8",
                          "PaymentGateway": "AXISPG",
                          "Amount": "10.00",
                          "Status": "success",
                          "RefundCreationDate": "2020-11-06 19:21:32",
                          "bank_ref_no": "527013524405",
                          "bank_arn": null,
                          "success_at": "2021-01-28 10:25:17"
                    },
                    {
                          "PayuID": "403993715521937565",
                          "RequestID": "131295795",
                          "RefundToken": "RefundToken9",
                          "PaymentGateway": "AXISPG",
                          "Amount": "10.00",
                          "Status": "success",
                          "RefundCreationDate": "2020-11-09 18:59:45",
                          "bank_ref_no": "527013524405",
                          "bank_arn": null,
                          "success_at": "2021-02-10 01:01:14"
                    },
                    {
                          "PayuID": "403993715521937565",
                          "RequestID": "131297379",
                          "RefundToken": "RefundToken10",
                          "PaymentGateway": "AXISPG",
                          "Amount": "10.00",
                          "Status": "success",
                          "RefundCreationDate": "2020-11-10 09:39:33",
                          "bank_ref_no": "527013524405",
                          "bank_arn": null,
                          "success_at": "2021-02-01 15:50:25"
                    }
              ]
        }
  }
  ```

  **Failure scenario**

  If no refunds found for the transaction:

  ```
  {
        "status": 1,
        "msg": "No Refunds Found for the transaction."
  }
  ```
</details>

<details>
  <summary>Response parameters description</summary>

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
          The status of the response can be any of the following:

          * **1:** Success
          * **2:** Failure
        </td>

        <td>
          1
        </td>
      </tr>

      <tr>
        <td>
          msg
        </td>

        <td>
          The description of the response whether the card details were stored successfully or not.
        </td>

        <td>
          Refunds fetched successfully.
        </td>
      </tr>

      <tr>
        <td>
          Refund Details
        </td>

        <td>
          The details are sent by PayU in JSON format for the successful response. For more information, refer to [Additional Info for General APIs](ref:addl-info-general-apis#description-of-the-refund-details-json-fields).
        </td>

        <td />
      </tr>
    </tbody>
  </Table>
</details>

## Request parameters

<details>
  <summary>Reference information for request parameters</summary>

  <KeyHashForGeneralParametersDescription />
</details>

**Example values**

Use the following sample values while trying out the API:

* `var1` (txnid): db97dd56eff7296e5061