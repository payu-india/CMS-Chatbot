---
title: Fetch Refund Transactions API - Loyalty Rewards
deprecated: false
hidden: true
metadata:
  robots: index
---
Fetch refund-related loyalty points transactions using this API.

**Endpoint**

**HTTP Method**: `POST`

|            |                                                                                                                                    |
| :--------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| Production | [https://apitest.payu.in/loyalty-points/points/refund/details/v1](https://apitest.payu.in/loyalty-points/points/refund/details/v1) |

## Request parameters

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        loyaltyTxnId
        `optional`
      </td>

      <td>
        `String` Ledger ID for fetching specific refund transactions.
      </td>
    </tr>

    <tr>
      <td>
        eventId
        `optional`
      </td>

      <td>
        `String`ID to identify the refund process (e.g., refundId or loyaltyRefId).
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```json
{
  "loyaltyTxnId": "1",
  "eventId": "eventId"
}
```

## Response parameters

| Parameter       | Description                                                |
| --------------- | ---------------------------------------------------------- |
| status          | Indicates whether API call was success (1) or failure (0). |
| message         | Message describing the API response.                       |
| result          | Contains the refund details.                               |
| id              | Refund transaction ID.                                     |
| points          | Number of loyalty points refunded.                         |
| transactionType | Type of transaction (`Credit`, etc.).                      |
| status          | Status of the refund (e.g., success).                      |
| referenceId     | Merchant reference ID.                                     |
| flowType        | Flow indicating the refund process.                        |
| amount          | Value of the refund in monetary terms.                     |
| expiryDate      | Time duration before refunded points expire.               |
| createdOn       | Timestamp of refund creation.                              |
| adjustmentInfo  | Contains details of any adjustments, if applicable.        |

### Sample response

### Success

```json
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
            "amount": "4",
            "expiryDate": "3 days"
        }
    ]
}
```

### Failure scenarios

* No transactions found

```json
{
    "status": 0,
    "message": "No transaction found"
}
```

* Bad request

```json
{
    "errorMessage": "Bad Request",
    "errorType": "APPLICATION_EXCEPTION",
    "issueCode": "LS500_508"
}
```