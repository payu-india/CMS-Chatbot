---
title: 'Refund Initiation API '
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Refund Initiation** API allows merchants to initiate refunds for transactions. Its functionally similar to the v1 **Cancel Refund Transaction** API, but is maintained only for backward compatibility with existing integrations. The v2 API offers enhanced functionality and improved response formats compared to the v1 API.

**Endpoint**

|                        |                                                   |
| :--------------------- | :------------------------------------------------ |
| Production Environment | [https://api.payu.in](http://api.payu.in)         |
| Test Environment       | [https://apitest.payu.in](http://apitest.payu.in) |

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

<br />

## Sample request

```bash
curl --location 'https://apitest.payu.in/v2/refund/' \
--header 'Content-Type: application/json' \
--header 'date: Tue, 15 Jul 2025 08:47:13 GMT' \
--header 'Authorization: hmac username="KOEfPI", algorithm="sha512", headers="date", signature="33560cfbfe91d98dc4d395de8e212e9f9c8e8d88459c4ac2948962ad5e7ecdd0f23b695d4aacd1ac3a94bf912ece4f61fe9e0a8566b7b016c8a52fc1a0299d3c"' \
--header 'Cookie: PHPSESSID=pemnb8cccqkdqc0d4o0uh6mvg0' \
--data '{
    "payuId" : "9999999900009081231239182",
    "refundToken": "adij90",
    "amount": 2,
    "refundDetails": {},
    "refundSplitRequest": null
}'
```

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

```json
{
  "status": 1,
  "statusCode": 102,
  "message": "Refund request accepted",
  "refundId": "123456789"
}
```

#### Failure Response

```json
{
  "status": 0,
  "errorcode": "4000",
  "message": "Refund request rejected"
}
```