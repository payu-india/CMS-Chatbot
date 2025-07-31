---
title: Seamless Debit Enquiry API
deprecated: false
hidden: false
metadata:
  robots: index
---
The Seamless Debit Enquiry API provides transaction status for a debit request. This API is essential for reconciliation and transaction verification purposes, allowing you to confirm the final status of payment transactions.

## Environment

| Environment | URL |
| ----------- | --- |
| Test | `https://test.payu.in/merchant/postservice.php?form=2` |
| Production | `https://info.payu.in/merchant/postservice.php?form=2` |

**HTTP Method**: POST

## Authentication

This API uses hash-based authentication. The hash is calculated using SHA512 algorithm with specific parameters.

## Request Headers
<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Content-Type<br/><code>mandatory</code></td>
      <td><code>String</code> application/x-www-form-urlencoded</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Request Parameters

### Body Parameters

The request body contains both encrypted and decrypted parameters.

#### Encrypted
<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>encdata<br/><code>mandatory</code></td>
      <td><code>String</code> Encrypted request body containing all the decrypted parameters</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

#### Decrypted
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
<td>key<br/><code>mandatory</code></td>
<td><code>String(50)</code> Merchant key provided by PayU</td>
<td>JPM7Fg</td>
</tr>
<tr>
<td>command<br/><code>mandatory</code></td>
<td><code>String(20)</code> Set to 'verify_payment'</td>
<td>verify_payment</td>
</tr>
<tr>
<td>var1<br/><code>mandatory</code></td>
<td><code>String(25)</code> Transaction ID (txnid) for the transaction to be verified</td>
<td>IhfgcZnXR...</td>
</tr>
<tr>
<td>hash<br/><code>mandatory</code></td>
<td><code>String(128)</code> SHA512 hash calculated for the request</td>
<td>a0ae79...</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>
## Response Parameters
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
      <td>status</td>
      <td>Status of the verification request</td>
      <td>1</td>
    </tr>
    <tr>
      <td>msg</td>
      <td>Message indicating verification result</td>
      <td>Transaction found</td>
    </tr>
    <tr>
      <td>transaction_details</td>
      <td>JSON object with detailed transaction information. For more information, refer to <a href=#transaction-detail-object> Transaction details object</a> </td>
      <td>Refer to <a href=#transaction-detail-object> Transaction details object</a> </td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

### Transaction details object
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
<td>mihpayid</td>
<td>PayU transaction reference number</td>
<td>1735903830180094</td>
</tr>
<tr>
<td>request_id</td>
<td>Original request ID</td>
<td>56882</td>
</tr>
<tr>
<td>bank_ref_num</td>
<td>Bank reference number</td>
<td>123456789</td>
</tr>
<tr>
<td>amt</td>
<td>Transaction amount</td>
<td>41.00</td>
</tr>
<tr>
<td>disc</td>
<td>Discount amount</td>
<td>0.00</td>
</tr>
<tr>
<td>mode</td>
<td>Payment mode used</td>
<td>CLW</td>
</tr>
<tr>
<td>PG_TYPE</td>
<td>Payment gateway type</td>
<td>CLW</td>
</tr>
<tr>
<td>status</td>
<td>Transaction status</td>
<td>success/failure</td>
</tr>
<tr>
<td>unmappedstatus</td>
<td>Detailed status</td>
<td>captured</td>
</tr>
<tr>
<td>Merchant_UTR</td>
<td>Merchant UTR number</td>
<td>UTR123456</td>
</tr>
<tr>
<td>txnid</td>
<td>Transaction ID</td>
<td>56882</td>
</tr>
<tr>
<td>key</td>
<td>Merchant key</td>
<td>JPM7Fg</td>
</tr>
<tr>
<td>net_amount_debit</td>
<td>Net amount debited</td>
<td>41.00</td>
</tr>
<tr>
<td>addedon</td>
<td>Transaction date and time</td>
<td>2023-08-22 18:30:15</td>
</tr>
<tr>
<td>productinfo</td>
<td>Product information</td>
<td>iPhone</td>
</tr>
<tr>
<td>firstname</td>
<td>Customer first name</td>
<td>Sourav</td>
</tr>
<tr>
<td>lastname</td>
<td>Customer last name</td>
<td>Mishra</td>
</tr>
<tr>
<td>email</td>
<td>Customer email</td>
<td>sourav.mishra@gmail.com</td>
</tr>
<tr>
<td>phone</td>
<td>Customer phone</td>
<td>919988776655</td>
</tr>
<tr>
<td>hash</td>
<td>Response hash</td>
<td>def456ghi789...</td>
</tr>
<tr>
<td>error_code</td>
<td>Error code (if failed)</td>
<td>E000</td>
</tr>
<tr>
<td>error_Message</td>
<td>Error message (if failed)</td>
<td>Insufficient balance</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample Request

### Encrypted Packet
```bash
curl --location --request POST 'https://test.payu.in/merchant/postservice.php?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'encdata=h/0YSUd9jKOQ8+2Dc3Phr4s7vxyz123...'
```

### Decrypted Packet
```
key=JPM7Fg&command=verify_payment&var1=IhfgcZnXR&hash=a0ae79...
```

## Sample Response

### Successful Transaction Found
```json
{
  "status": 1,
  "msg": "Transaction found",
  "transaction_details": {
    "mihpayid": "1735903830180094",
    "request_id": "56882",
    "bank_ref_num": "123456789",
    "amt": "41.00",
    "disc": "0.00",
    "mode": "CLW",
    "PG_TYPE": "CLW",
    "status": "success",
    "unmappedstatus": "captured",
    "Merchant_UTR": "UTR123456",
    "txnid": "56882",
    "key": "JPM7Fg",
    "net_amount_debit": "41.00",
    "addedon": "2023-08-22 18:30:15",
    "productinfo": "iPhone",
    "firstname": "Sourav",
    "lastname": "Mishra",
    "email": "sourav.mishra@gmail.com",
    "phone": "919988776655",
    "hash": "def456ghi789..."
  }
}
```

### Transaction Not Found
```json
{
  "status": 0,
  "msg": "Transaction not found"
}
```

## HTTP Status Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | OK - Request processed successfully |
| 400 | Bad Request - Invalid request parameters |
| 401 | Unauthorized - Authentication failed |
| 500 | Internal Server Error |
