---
title: Fetch All Transactions API - Loyalty Rewards
deprecated: false
hidden: true
metadata:
  robots: index
---
The \*\*Fetch All Transactions \*\*API gets the list of loyalty points transactions for payments, refunds, and adjustments. It supports filters to retrieve specific transaction types (e.g., earn, burn, refund, etc.).

### Endpint

**HTTP Method**: `POST`

|            |                                                                                                                              |
| :--------- | :--------------------------------------------------------------------------------------------------------------------------- |
| Production | [https://apitest.payu.in/loyalty-points/points/transaction/v1](https://apitest.payu.in/loyalty-points/points/transaction/v1) |

## Request paramters

<br />

Sure! Here's an overview of the **Request Parameters** and **Response Parameters** for both APIs in text format:

<br />

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
        `String` Ledger ID, primary key for fetching transactions. Returns one object.
      </td>
    </tr>

    <tr>
      <td>
        merchantTxnId
        `optional`
      </td>

      <td>
        `String`Reference ID for fetching multiple transactions. Returns an array of objects.
      </td>
    </tr>
  </tbody>
</Table>

***

## Sample Request

```json
{
  "loyaltyTxnId": "1",
  "merchantTxnId": "ref1"
}
```

## Response parameters

| Parameter       | Description                                    |
| --------------- | ---------------------------------------------- |
| status          | Indicates success (1) or failure (0).          |
| message         | Message describing the API response.           |
| result          | Contains the transaction details.              |
| id              | Transaction ID.                                |
| points          | Number of loyalty points involved.             |
| transactionType | Type of transaction (`load`, `unload`, etc.).  |
| status          | Status of the transaction (e.g., success).     |
| referenceId     | Merchant reference ID.                         |
| flowType        | Flow of the transaction (`payment`, `refund`). |
| amount          | Value for the transaction.                     |
| expiryDate      | Time duration before points expire.            |
| createdOn       | Timestamp of transaction creation.             |

## Sample Response

### Success scenario

```json
{
    "status": 1,
    "message": "Transaction fetched successfully",
    "result": [
        {
            "id": 3,
            "points": 100.00,
            "transactionType": "unload",
            "status": "success",
            "referenceId": "ref3",
            "amount": "1",
            "expiryDate": "4 days"
        }
    ]
}
```

### Failure scenarios

* No transaction found

```json
{
    "status": 0,
    "message": "No transaction found"
}
```

* Bad requeest

```json
{
    "errorMessage": "Bad Request",
    "errorType": "APPLICATION_EXCEPTION",
    "issueCode": "LS500_508"
}
```

***