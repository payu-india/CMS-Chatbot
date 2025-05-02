---
title: Get Payment Status API
excerpt: ''
api:
  file: bbps-apis-agent-share-5.json
  operationId: GetPaymentStatus(V2)
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
You can use the **Get Payment Status** API to manually request the status of a bill payment transaction. Sometime the response of a **Bill Payment** API can be interrupted due to network failures. To handle such situations you can programmatically use this API to make a manual request.

|            |                                                                                      |
| :--------- | :----------------------------------------------------------------------------------- |
| Production | [https://bbps-sb.payu.in/payu-nbc/v1/nbc/](https://bbps-sb.payu.in/payu-nbc/v1/nbc/) |

> 📘 Note:
>
> Send the scope of the Get Token API as **read\_transactions** to obtain the access\_token for this request. For more information, refer to [Get Token API - BBPS](ref:get-token-api-bbps).

<details>
  <summary>Sample request</summary>

  ```
  curl --location -g --request GET 'https://<hostName>/<host name>/v2/nbc/status/billpayment?refId=`{refId}` ' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer {{access_token}}' 
  ```
</details>

<details>
  <summary>Response parameters</summary>

  <Table>
    <thead>
      <tr>
        <th>
          **Field Name**
        </th>

        <th>
          **Description**
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          code
        </td>

        <td>
          This field contains the global response code and can be any of the following:

          * **0**: If web service call failed
          * **1**: if web service call succeeded
        </td>
      </tr>

      <tr>
        <td>
          status
        </td>

        <td>
          The status of the API command and can be any of the following:

          * **SUCCESS**
          * **FAILURE**
        </td>
      </tr>

      <tr>
        <td>
          payload
        </td>

        <td>
          This parameter contains the bill fetch transaction data. For more information, refer to the [payload](#payload) table.
        </td>
      </tr>
    </tbody>
  </Table>

  ### payload

  | Field            | Description                                                                                                                                                                                                                                                                                           |
  | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | refId            | This field contains the reference ID for the queried payment request.                                                                                                                                                                                                                                 |
  | txnStatus        | This field contains the status related to requested refId. It will contain status as in the Transaction Status Code table. For more information, refer to [Transaction Status Code](https://devguide.vercel.app/agent-api-integration/bill-apis/bill-payment-transaction-status/#Transaction_Status). |
  | requestTimeStamp | This field contains the actual payment requested date time stamp of payment request.                                                                                                                                                                                                                  |
  | paidAmount       | This field contains the payment requested amount                                                                                                                                                                                                                                                      |
  | billerId         | This field contains the payment requested biller ID.                                                                                                                                                                                                                                                  |
  | additionalParams | This field contains the payment related additional params like payment txnRefId.                                                                                                                                                                                                                      |
  | planResponse     | This field contains the activated plan information lists returned by Biller. This field is conditional and BOU will pass if billerResponseType for respective biller is SELECTIVE type                                                                                                                |
</details>

<details>
  <summary>Sample response</summary>

  ### Success scenario

  ```
  {
     "code":200,
     "status":"SUCCESS",
     "payload":{
        "refId":"<refId>",
        "txnStatus":"PAYMENT_SUCCESS",
        "requestTimeStamp":"<Requested Time stamp>",
        "paidAmount":"<Amount Paid>",
        "billerId":"<billerId>",
        "additionalParams":{
           "txnReferenceId":"<txnRefId>",
           "billerReferenceNumber":"<billerReferenceNumber>",
           "key1":"value2",
           "key2":"value2"
        },
        "planResponse":[
           {
              "planType":"ACTIVATED",
              "key1":"value1",
              "key2":"value2",
              "key3":"value3",
              "key4":"value4",
              "key5":"value5"
           }
        ]
     }
  }
  ```

  ### Failure scenario

  * When the PayU Transaction ID does not exist:

  ```
  {
     "code":200,
     "status":"SUCCESS",
     "payload":{
        "refId":"<refId>",
        "txnStatus":"RECORD_NOT_FOUND",
        "requestTimeStamp":"<Requested Time stamp>",
        "paidAmount":0,
        "billerId":"",
        "additionalParams":{
           "txnReferenceId":""
        }
     }
  }
  ```

  * When Payment transaction failed at biller’s end and failure status captured at PayU’s end:

  ```
  {
     "code":200,
     "status":"SUCCESS",
     "payload":{
        "refId":"<refId>",
        "txnStatus":"PAYMENT_FAILURE",
        "requestTimeStamp":"<Requested Time stamp>",
        "paidAmount":"<Amount Paid>",
        "billerId":"<BillerId>",
        "additionalParams":{
           "txnReferenceId":"<txnRefId>"
        }
     }
  }
  ```

  * When Payment transaction is not captured at PayU’s end and PayU is also waiting for the actual status of the transaction:

  ```
  {
     "code":200,
     "status":"SUCCESS",
     "payload":{
        "refId":"<refId>",
        "txnStatus":"PAYMENT_PENDING",
        "requestTimeStamp":"<Requested Time stamp>",
        "paidAmount":"<amount paid>",
        "billerId":"<billerId>",
        "additionalParams":{
           "txnReferenceId":"<txnRefId>"
        }
     }
  }
  ```
</details>

## Request parameters