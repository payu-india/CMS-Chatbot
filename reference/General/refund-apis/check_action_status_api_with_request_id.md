---
title: Check Refund Status API with Request ID
excerpt: 'API Command: **check_action_status**'
api:
  file: general-23.json
  operationId: check_action_status(1st_usage)
deprecated: false
hidden: false
metadata:
  title: Check Refund Status API with Request ID
  description: >-
    The document provides information on how to use the
    cancel_refund_transaction and check_action_status APIs to cancel and check
    the status of a transaction, respectively, using a Request ID.
  keywords:
    - Check Refund Status API with Request ID
    - ' check_action_status API Command'
    - ' Using Request ID to Check Refund Status API'
  robots: index
next:
  description: ''
  pages:
    - type: endpoint
      slug: refund_transaction_api
      title: Refund Transaction API
    - type: endpoint
      slug: check_action_status_api_with_payu_id
      title: Check Refund Status API with PayU ID
---
Whenever the **cancel\_refund\_transaction** API is executed successfully to cancel a transaction, a Request ID is returned in the output parameters for that particular request. For more information on the cancel\_refund\_transaction API, refer to Refund Transaction.

In **check\_action\_status** API, you need to input this Request ID to get the current status of the request. The return parameters are MIHPayID, Amount, Discount, Mode, and Status of transaction. To learn more about different payment states, refer to [Payment States Explanations](https://docs.payu.in/reference/payment-state-explanations).

**Environment**

|                        |                                                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| Test Environment       | [https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2) |
| Production Environment | [https://info.payu.in/merchant/postservice.php?form=2](https://info.payu.in/merchant/postservice.php?form=2) |

<details>
  <summary>Sample request</summary>

  ```curl
  curl --location --request POST 'https://test.info.payu.in/merchant/postservice.php?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data 'key=JF****g&hash=9f5faabedb7f5d41f519db3a223cf5318ecc0b7e669f49e0a699d4c4879e1ccaed5b99f5cd
  8be4f2cbddefe5272ec983abd8f38480d9c2609a29447f750a3158&command=check_action_status_txnid&var
  1=7043873219"
  ```
</details>

<details>
  <summary>Sample response</summary>

  **Success scenario**

  if successfully fetched

  ```plaintext
  {
        "status": 1,
        "msg": "1 out of 1 Transactions Fetched Successfully",
        "transaction_details": {
              "131278422": {
                    "131278422": {
                          "mihpayid": "403993715521937565",
                          "bank_ref_num": "527013524405",
                          "request_id": "131278422",
                          "amt": "10.00",
                          "mode": "CC",
                          "action": "refund",
                          "token": "20201105secrettokenatur",
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
  <summary>Response parameters and sample response</summary>

  * The **transaction\_details** parameter of the response is in JSON format. For more information, refer to [Additional Info for General APIs](/reference/addl-info-general-apis#response-parameters-check-refund-status-with-request-idpayu-id-or-get-transaction-details).

  > 📘 Note:
  >
  > The error\_code ​value 102​ should be treated as a success; the rest are failures. For the list of error codes, refer to [Error Codes for Refund Initiation](ref:error-codes-for-refund-initiation).
</details>

## Request parameters

<details>
  <summary>Reference information for request parameters</summary>

  <KeyHashForGeneralParametersDescription />
</details>

**Example value**

Use the following sample values while trying out the API:

* `var1` (request\_id): 131278422