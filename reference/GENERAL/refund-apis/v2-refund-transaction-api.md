---
title: 'Refund Initiation API '
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Refund Initiation** API allows merchants to initiate refunds for transactions. Its functionally similar to the v1 **Cancel Refund Transaction** API, but is maintained only for backward compatibility with existing integrations. The v2 API offers enhanced functionality and improved response formats compared to the v1 API.

**Endpoint**

|                        |                                                                         |
| :--------------------- | :---------------------------------------------------------------------- |
| Production Environment | [https://api.payu.in/v2/refund/](https://api.payu.in/v2/refund/)        |
| Test Environment       | [https://apitest.payu.in/v2/refund/](http://apitest.payu.in/v2/refund/) |

## Request header

<V2_payment_header_params />

## Request body

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>payuId<br/><code>mandatory</code></td>
      <td><code>String</code> The unique PayU transaction identifier for which the refund is being initiated.</td>
      <td>9999999900009081231239182</td>
    </tr>
    <tr>
      <td>refundToken<br/><code>mandatory</code></td>
      <td><code>String</code> Unique token identifier for the refund request.</td>
      <td>adij90</td>
    </tr>
    <tr>
      <td>amount<br/><code>mandatory</code></td>
      <td><code>Number</code> The refund amount to be processed.</td>
      <td>2</td>
    </tr>
    <tr>
      <td>refundDetails<br/><code>optional</code></td>
      <td><code>Object</code> Additional details related to the refund request.</td>
      <td>{}</td>
    </tr>
    <tr>
      <td>refundSplitRequest<br/><code>optional</code></td>
      <td><code>Object</code> Information for split refund requests when applicable.</td>
      <td>null</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Sample request

```bash
curl --location 'http://apitest.payu.in/v2/refund/' \
--header 'Content-Type: application/json' \
--header 'mid: 2' \
--header 'Cookie: PHPSESSID=pemnb8cccqkdqc0d4o0uh6mvg0' \
--header 'authorization: hmac username="a4vGC2", algorithm="sha512", headers="date", signature="d83ee842949292e4f7cf44c6bb32efd44f756e9cd03fc36d9e291b6f336f94bb2ace87fd92571149edbaa2db72eaa65514e4b2d13b44d24b508fdd587e8ee212"' \
--header 'date: Fri, 26 Dec 2025 12:35:10 GMT' \
--data '{
    "payuId": "403993715535403598",
    "amount": 1,
    "token": "4352398",
    "source": 1,
    "merchantCallbackUrl": "https://merchant.example.com/refund/callback"
}'
```

### With Split Settlements

```
curl --location 'https://apitest.payu.in/v2/refund/' \
--header 'Content-Type: application/json' \
--header 'mid: 8006653' \
--data '{
    "mihpayId": "999000000000478",
    "refundToken": "a*bv***w",
    "amount": 0.1,
    "refundDetails": {},
    "refundSplitRequest": {
        "33rOiT": {
            "amount": 0.21
        }
    }
}'
```

##

## Response parameters

| Parameter   | Description                                                        | Example                     |
| ----------- | ------------------------------------------------------------------ | --------------------------- |
| status      | Indicates success (1) or failure (0) of the refund request         | `1`                         |
| statusCode  | Numeric code representing the status of the refund request         | `102`                       |
| message     | Descriptive message about the status of the refund request         | `"Refund request accepted"` |
| payuId      | Unique PayU transaction ID for which the refund was processed      | `999091000003794`           |
| refundToken | Unique token identifying the refund request                        | `11358934598`               |
| requestId   | Unique identifier for the refund request (if available)            | `4993824108552`             |
| refundId    | Unique identifier for the refund transaction (if successful)       | `123456789`                 |
| splitInfo   | Contains details of refunds for split transactions (if applicable) | See JSON example            |

### Sample Response

#### Success Response

* General transaction

```json
{
  "status": 1,
  "statusCode": 102,
  "message": "Refund request accepted",
  "refundId": "123456789"
}
```

* With Split Settlements
  ```
  {
    "message": "Success",
    "status": 1,
    "result": [
      {
        "payuId": "999000000000478",
        "refundToken": "abb342vqw",
        "status": 1,
        "message": "Success",
        "splitInfo": {
          "33rOiT": {
            "status": 1,
            "statusCode": "102",
            "message": "Refund request accepted",
            "requestId": "4993824108553"
          }
        }
      }
    ]
  }

  ```
  ###

#### Failure Response

```json
{
  "status": 0,
  "errorcode": "4000",
  "message": "Refund request rejected"
}
```
