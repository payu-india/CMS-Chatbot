---
title: Settlement Transaction Details API
deprecated: false
hidden: true
metadata:
  robots: index
---
This API is retrieve detailed information about a specific transaction using the merchant transaction ID. This API provides comprehensive transaction data including status, amount, settlement details, and associated metadata.

### Environment

|                        |                                                                                                                |
| :--------------------- | :------------------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://apitest.payu.in/settlement/transactionDetails](https://apitest.payu.in/settlement/transactionDetails) |
| Production Environment | [https://info.payu.in/settlement/transactionDetails](https://info.payu.in/settlement/transactionDetails)       |

**HTTP Method**: POST

<Accordion title="Request Parameters" icon="fa-table">
  ### Request Header

  <HeaderAuthentication />

  ### Query Parameters

  | Parameter                                         | Description                                                  | Example              |
  | ------------------------------------------------- | ------------------------------------------------------------ | -------------------- |
  | merchantTransactionId<br /><code>mandatory</code> | <code>String</code> The tramnsaaction ID of the transaction. | ZTDUPI2602754D96F47B |

  ### Other Header Parameters

  | Parameter                       | Description                                                                      | Example |
  | ------------------------------- | -------------------------------------------------------------------------------- | ------- |
  | mid<br /><code>mandatory</code> | <code>String</code> Merchant identifier that the integration was registered with | 875546  |
</Accordion>

<Accordion title="Sample Request" icon="fa-code">
  ```curl
  curl --location 'https://apitest.payu.in/settlement/transactionDetails?merchantTransactionId=ZTDUPI2602754D96F47B' \
  --header 'mid: 8759546' \
  --header 'Authorization: {{authorization}}' \
  --header 'Date: {{date}}'
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-reply">
  ### Success Scenarios

  #### Capture Only

  ```json
  {
    "code": "2000",
    "message": "Success",
    "status": 0,
    "result": [
      {
        "merchantId": 180012,
        "merchantTransactionId": "W49OV6KQXR4H",
        "payuId": "943323893640",
        "transactionType": "capture",
        "settlementStatus": "Settled",
        "settlementUTR": "TESTUTR001",
        "settlementDate": "2025-12-10T15:58:43",
        "settlementId": "180012202512101738",
        "settlementAmount": 8.0
      }
    ]
  }
  ```

  #### Capture + Refund + Chargeback

  ```json
  {
    "code": "2000",
    "message": "Success",
    "status": 0,
    "result": [
      {
        "merchantId": 180012,
        "merchantTransactionId": "W49OV6KQXR4H",
        "payuId": "943323893640",
        "transactionType": "capture",
        "settlementStatus": "Settled",
        "settlementUTR": "TESTUTR001",
        "settlementDate": "2025-12-10T15:58:43",
        "settlementId": "180012202512101738",
        "settlementAmount": 8.0
      },
      {
        "merchantId": 180012,
        "merchantTransactionId": "W49OV6KQXR4H",
        "payuId": "943323893640",
        "transactionType": "refund",
        "settlementStatus": "Settled",
        "settlementUTR": "TESTUTR001",
        "settlementDate": "2025-12-10T15:58:43",
        "settlementId": "180012202512101738",
        "settlementAmount": -8.0
      },
      {
        "merchantId": 180012,
        "merchantTransactionId": "W49OV6KQXR4H",
        "payuId": "943323893640",
        "transactionType": "chargeback",
        "settlementStatus": "Settled",
        "settlementUTR": "TESTUTR001",
        "settlementDate": "2025-12-10T15:58:43",
        "settlementId": "180012202512101738",
        "settlementAmount": -8.0
      }
    ]
  }
  ```

  #### Capture + Chargeback + Chargeback Reversal

  ```json
  {
    "code": "2000",
    "message": "Success",
    "status": 0,
    "result": [
      {
        "merchantId": 180012,
        "merchantTransactionId": "W49OV6KQXR4H",
        "payuId": "943323893640",
        "transactionType": "capture",
        "settlementStatus": "Settled",
        "settlementUTR": "TESTUTR001",
        "settlementDate": "2025-12-10T15:58:43",
        "settlementId": "180012202512101738",
        "settlementAmount": 8.0
      },
      {
        "merchantId": 180012,
        "merchantTransactionId": "W49OV6KQXR4H",
        "payuId": "943323893640",
        "transactionType": "chargeback",
        "settlementStatus": "Settled",
        "settlementUTR": "TESTUTR001",
        "settlementDate": "2025-12-10T15:58:43",
        "settlementId": "180012202512101738",
        "settlementAmount": -8.0
      },
      {
        "merchantId": 180012,
        "merchantTransactionId": "W49OV6KQXR4H",
        "payuId": "943323893640",
        "transactionType": "chargebackreversal",
        "settlementStatus": "Settled",
        "settlementUTR": "TESTUTR001",
        "settlementDate": "2025-12-10T15:58:43",
        "settlementId": "180012202512101738",
        "settlementAmount": 8.0
      }
    ]
  }
  ```

  #### Empty Response (No Settlement Records)

  ```json
  {
    "code": "2000",
    "message": "Success",
    "status": 0,
    "result": []
  }
  ```

  ### Failure scenario

  #### Invalid request parameters(4000) 

  * Invalid request parameter

  ```json
  {
    "status": 0,
    "message": "Please provide valid merchantId",
    "result": null
  } 
  ```

  * Request parameter not wthin character limit

  ```json
  {
    "status": 0,
    "message": "Invalid Transaction ID: Must not exceed 50 characters."
    "result": null
  } 
  ```

  * Request parameter value is missing

  ```json
   {
    "status": 0,
    "message":"Merchant Transaction ID is required."
    "result": null
  } 
  ```

  #### Unauthorized / access denied (4001)

  ```json
  {
    "status": 0,
    "message": "Unauthorized",
    "result": null
  }
  ```
</Accordion>

<Accordion title="Response Parameters" icon="fa-table">
  | Parameter | Description                                                                                                                                      |
  | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
  | status    | Response status and it returns either 1 or 0, where 0=Success and 1=Failure.                                                                     |
  | msg       | Response message                                                                                                                                 |
  | result    | Main response data container in a JSON format. For more information, refer to [result JSON Fields Description](#result-json-fields-descriptions) |

  ## result JSON Fields Descriptions

  | Parameter             | Description                                                                                                                                                                                      |
  | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | merchantId            | **Merchant identifier** assigned by PayU to uniquely identify the merchant account. This is the same ID used for authentication and API access.                                                  |
  | merchantTransactionId | **Merchant's unique transaction reference** provided during the original payment request. This is the merchant-generated identifier used to track the transaction in their system.               |
  | payuId                | **PayU's internal unique transaction identifier**. This is generated by PayU for every transaction and can be used for future transaction inquiries, refunds, or support requests.               |
  | transactionType       | **Type of transaction action** processed. Common values include: `capture` (successful payment), `refund`, `chargeback`, `adjustment`, `cancel`, etc.                                            |
  | settlementStatus      | **Current settlement status** of the transaction. Possible values: `Settled` (amount transferred to merchant), `Pending` (awaiting settlement), `On Hold`, `Failed`, etc.                        |
  | settlementUTR         | **Unique Transaction Reference (UTR)** number generated by the bank for the settlement transfer. This is the bank reference for the actual money transfer to the merchant's account.             |
  | settlementDate        | **Date and time when the settlement was completed**. Format: `YYYY-MM-DDTHH:MM:SS`. Represents when the funds were actually transferred to the merchant's bank account.                          |
  | settlementId          | **PayU's internal settlement batch identifier**. This groups multiple transactions that were settled together in the same batch. Format typically includes merchant ID + date + sequence number. |
  | settlementAmount      | **Final amount settled to the merchant** after deducting all applicable fees, taxes, and adjustments. This is the net amount that was actually transferred to the merchant's account.            |
</Accordion>
