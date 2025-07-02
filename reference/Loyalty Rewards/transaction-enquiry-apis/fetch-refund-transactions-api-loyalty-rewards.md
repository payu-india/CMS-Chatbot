---
title: Fetch Refund Transactions API - Loyalty Rewards
deprecated: false
hidden: false
metadata:
  robots: index
---
Fetch refund-related loyalty points transactions using this API.

* **Endpoint**: `https://apitest.payu.in/loyalty-points/points/refund/details/v1`
* **HTTP Method**: `POST`

## Request parameters:

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

### Sample request

```json
{
  "loyaltyTxnId": "1",
  "eventId": "eventId"
}
```

### Responses:

* **Success:**

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

* **Failure:**

```json
{
    "status": 0,
    "message": "No transaction found"
}
```

* **Error:**

```json
{
    "errorMessage": "Bad Request",
    "errorType": "APPLICATION_EXCEPTION",
    "issueCode": "LS500_508"
}
```

#### Response Parameters:

| Parameter       | Type       | Description                                         |
| --------------- | ---------- | --------------------------------------------------- |
| status          | `integer`  | Indicates success (1) or failure (0).               |
| message         | `string`   | Message describing the API response.                |
| result          | `array`    | Contains the refund details.                        |
| id              | `integer`  | Refund transaction ID.                              |
| points          | `float`    | Number of loyalty points refunded.                  |
| transactionType | `string`   | Type of transaction (`Credit`, etc.).               |
| status          | `string`   | Status of the refund (e.g., success).               |
| referenceId     | `string`   | Merchant reference ID.                              |
| flowType        | `string`   | Flow indicating the refund process.                 |
| amount          | `string`   | Value of the refund in monetary terms.              |
| expiryDate      | `string`   | Time duration before refunded points expire.        |
| createdOn       | `datetime` | Timestamp of refund creation.                       |
| adjustmentInfo  | `object`   | Contains details of any adjustments, if applicable. |