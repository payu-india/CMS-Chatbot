---
title: Refund Eligibility API
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Refund Eligibility** API is used to check the eligibility for refund for the Loyalty Rewards integration.

HTTP Method: **POST**

### Endpoint

|            |                                                                       |
| :--------- | :-------------------------------------------------------------------- |
| Production | <https://apitest.payu.in/loyalty-points/points/v1/refund/eligibility> |
|            |                                                                       |

## Request Parameters

You have to provide either loyaltyTxnId (ledger id - primary Key) or eventId (It will be loyaltyRefId).

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "loyaltyTxnId  \n`mandatory if eventId \nis not posted`",
    "0-1": "The ledger ID must be posted here.",
    "0-2": "1",
    "1-0": "eventId  \n`mandatory if loyaltyTxnId \nis not posted`",
    "1-1": "The merchant's transaction ID for refund",
    "1-2": "504"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    null,
    null,
    null
  ]
}
[/block]

## Request Body

```plaintext
{ 
  "loyaltyTxnId": "1", 
  "eventId": "eventId" 
} 
```

## Sample Response

The result is an array which will have only one item, Response on eventId could have **adjustmentInfo** if it is not null.

### Success scenario

#### Passing loyaltyTxnId in request

```plaintext
{
    "status": 1,
    "message": "Transaction fetched successfully",
    "result": [
        {
            "id": 2,
            "points": 300.00,
            "transactionType": "Credit",
            "status": "success",
            "referenceId": "ref1",
            "flowType": "refund",
            "eventId": "event2",
            "amount": "4",
            "recovery": "recovery_fiel",
            "expiryDate": "3 days",
            "createdOn": "2024-08-08 22:15:37.0"
        }
    ]
}
```

#### Passing eventId

```plaintext
{
    "status": 1,
    "message": "Transaction fetched successfully",
    "result": [
        {
            "id": 2,
            "points": 300.00,
            "transactionType": "Credit",
            "status": "success",
            "referenceId": "ref1",
            "flowType": "refund",
            "eventId": "event2",
            "amount": "4",
            "recovery": "recovery_fiel",
            "expiryDate": "3 days",
            "createdOn": "2024-08-08 22:15:37.0",
            "adjustmentInfo": {
                "id": 4,
                "points": 100.00,
                "transactionType": "Credit",
                "status": "success",
                "referenceId": "ref1",
                "flowType": "adjustment",
                "eventId": "event2",
                "amount": "1",
                "recovery": "recovery_fiel",
                "expiryDate": "2 days",
                "createdOn": "2024-08-08 22:15:37.0"
            }
        }
    ]
}
```

<br />

### Failure scenario

- No transaction found

```plaintext
{ 
    "status": 0, (Fetch Failure status) 
    "message": "No transaction found" 
} 
```

- Application error

```plaintext
{  
  "errorMessage":"Bad Request ",  
  "errorType":"APPLICATION_EXCEPTION",  
  "issueCode":"LS500_508" 
 } 
```