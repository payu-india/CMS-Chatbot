---
excerpt: ''
api:
  file: get-transaction-details-6.json
  operationId: GetTransactionDetailsAPI
deprecated: false
hidden: false
metadata:
  title: Get Transaction Details API for Payment Links
  description: ''
  keywords:
    - Get Transaction Details API for Payment Links
    - Payment Links Get Transaction Details API
    - Get Transaction Details API
  robots: index
next:
  description: ''
---
The **Get Transaction Details** API is used to get the details of transactions for a given date range.

|                            |                                                                                       |
| -------------------------- | ------------------------------------------------------------------------------------- |
| **Test Environment**       | \<[https://uatoneapi.payu.in/payment-links](https://uatoneapi.payu.in/payment-links)> |
| **Production Environment** | \<[https://oneapi.payu.in/payment-links](https://oneapi.payu.in/payment-links)>       |

<Accordion title="Sample request" icon="fa-code">
  ```curl
    curl --location '
    https://uatoneapi.payu.in/payment-links/INV2669646610062/txns?pageSize=10&dateFrom=2024-10-16&dateTo=2024-10-17'
    \
    --header 'merchantId: 8237736' \
    --header 'Authorization: Bearer 8e400beadad72c5d00c22d98df690bcf04cff2eff4be51cc30e0783492bd8091'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  ```json
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
                    "settledAmount": 19.0,
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
</Accordion>

## Request parameters