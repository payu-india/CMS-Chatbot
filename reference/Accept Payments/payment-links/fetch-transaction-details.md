---
api:
  file: pl-test-oas.yaml
  operationId: GetTransactionDetailsAPI
hidden: true
metadata:
  title: Fetch Transaction Details | Payment Links API
next:
  description: Explore related information and resources.
---
Use this endpoint to fetch all payment attempts such as successful, failed, and pending recorded against a payment link.<br />

Use this to verify payment completion, reconcile partial payments, or displaypayment history. An empty `result` array is a valid success response when no payments have been attempted yet.

***

<Cards>
  <Card title="Method">
    GET
  </Card>

  <Card title="Endpoint">
    /payment-links/{invoiceNumber}/transactions
  </Card>
</Cards>

***

## Environments

| Environment                | URL                         |
| :------------------------- | :-------------------------- |
| **Test Environment**       | `https://uatoneapi.payu.in` |
| **Production Environment** | `https://oneapi.payu.in`    |

***

<PLbearertoken />

***

## Sample Request

<Tabs>
  <Tab title="Request Payload">
    ```curl
      curl --location '
      https://uatoneapi.payu.in/payment-links/INV2669646610062/txns?pageSize=10&dateFrom=2024-10-16&dateTo=2024-10-17'
      \
      --header 'merchantId: 8237736' \
      --header 'Authorization: Bearer 8e400beadad72c5d00c22d98df690bcf04cff2eff4be51cc30e0783492bd8091'
    ```
  </Tab>

  <Tab title="Parameter Description">
    Refer to the [Path Params](https://docs.payu.in/v3.0/reference/fetch-transaction-details#path-params) and [Headers](https://docs.payu.in/v3.0/reference/fetch-transaction-details#header-params) sections for a full description of all parameters and use cases.
  </Tab>
</Tabs>

***

## Sample Response

<Tabs>
  <Tab title="Success and Error Response">
    ```json Success Respone
    {
      "status": 0,
      "message": null,
      "result": {
        "pageSize": 10,
        "pages": 1,
        "rows": 1,
        "pageOffset": 0,
        "data": [
          {
            "createdOn": "2024-10-16 15:34:52.0",
            "transactionId": "403993715532491867",
            "merchantReferenceId": "80203",
            "paymentId": null,
            "settledAmount": 19,
            "customerEmail": "ganesh.desai@payu.in",
            "status": "success",
            "mode": "CC",
            "bankCode": "CC",
            "cardNum": "XXXXXXXXXXXX2346",
            "subscriptionDetails": null
          }
        ]
      },
      "errorCode": null,
      "guid": "3755efc8-60d3-4a8e-b0dc-642d02c77c8f"
    }
    ```
    ```json Error Response
    ```
  </Tab>

  <Tab title="Parameter Description">
    Refer to the [Response](https://docs.payu.in/v3.0/reference/fetch-transaction-details#response-schemas) section for a full description of all response fields.
  </Tab>
</Tabs>
