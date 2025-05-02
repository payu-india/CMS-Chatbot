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
| Production | \<https://apitest.payu.in/loyalty-points/points/v1/refund/eligibility> |
|            |                                                                       |

## Request Parameters

You have to provide either loyaltyTxnId (ledger id - primary Key) or eventId (It will be loyaltyRefId).

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>loyaltyTxnId<br><code>mandatory if eventId  is not posted</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The ledger ID must be posted here.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>eventId<br><code>mandatory if loyaltyTxnId  is not posted</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The merchant&#39;s transaction ID for refund</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>504</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

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