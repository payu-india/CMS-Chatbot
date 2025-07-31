---
title: Update Profile API - Closed Loop
deprecated: false
hidden: false
metadata:
  robots: index
---
The Update Profile API allows you to update a customer's profile information including name, email, mobile number, address, and other personal details. This API is useful for maintaining accurate customer information and compliance requirements.

## Environment

| Environment | URL |
| ----------- | --- |
| Test | `https://apitest.payu.in/loyalty-points/v1/wallet/onboarding/v3/updateProfile` |
| Production | `https://api.payu.in/loyalty-points/v1/wallet/onboarding/v3/updateProfile` |

**HTTP Method**: POST

## Authentication

This API uses HMAC-SHA512 authentication. Refer to the [Authentication Guide](/docs/authentication) for detailed implementation.

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
<td>encdata<br/><code>mandatory</code></td>
<td><code>String</code> Encrypted request body containing all the decrypted parameters</td>
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
      <td>token<br/><code>mandatory</code></td>
      <td><code>String</code> AES-192-CBC encrypted request body containing all the decrypted parameters</td>
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
      <td>messageCode<br/><code>mandatory</code></td>
      <td><code>Numeric(4)</code> Unique identifier for the Update Profile API</td>
      <td>1280</td>
    </tr>
    <tr>
      <td>clientTxnId<br/><code>mandatory</code></td>
      <td><code>String(100)</code> Unique ID generated per request</td>
      <td>ABC0987654321</td>
    </tr>
    <tr>
      <td>requestDateTime<br/><code>mandatory</code></td>
      <td><code>Numeric(14)</code> Request timestamp (YYYYMMDDHHMMSS format)</td>
      <td>20230804182306</td>
    </tr>
    <tr>
      <td>productId<br/><code>mandatory</code></td>
      <td><code>String(10)</code> Product ID shared by PayU</td>
      <td>9</td>
    </tr>
    <tr>
      <td>customerId<br/><code>conditional</code></td>
      <td><code>String(50)</code> Unique identifier for the customer</td>
      <td>62508</td>
    </tr>
    <tr>
      <td>urn<br/><code>conditional</code></td>
      <td><code>Numeric(11)</code> Unique wallet reference number</td>
      <td>7000000008</td>
    </tr>
    <tr>
      <td>firstName<br/><code>optional</code></td>
      <td><code>String(50)</code> Customer's first name</td>
      <td>Jacob</td>
    </tr>
    <tr>
      <td>lastName<br/><code>optional</code></td>
      <td><code>String(50)</code> Customer's last name</td>
      <td>James</td>
    </tr>
    <tr>
      <td>emailId<br/><code>optional</code></td>
      <td><code>String(50)</code> Customer email address</td>
      <td>jacob12@example.com</td>
    </tr>
    <tr>
      <td>mobileNumber<br/><code>optional</code></td>
      <td><code>Numeric(15)</code> Customer mobile number with country code</td>
      <td>919988776655</td>
    </tr>
    <tr>
      <td>dateOfBirth<br/><code>optional</code></td>
      <td><code>Numeric(8)</code> Customer's DOB (YYYYMMDD format)</td>
      <td>19951201</td>
    </tr>
    <tr>
      <td>gender<br/><code>optional</code></td>
      <td><code>String(10)</code> Customer's gender</td>
      <td>Male</td>
    </tr>
    <tr>
      <td>riskCategory<br/><code>optional</code></td>
      <td><code>String(20)</code> Risk category of the customer</td>
      <td>high</td>
    </tr>
    <tr>
      <td>address.line1<br/><code>optional</code></td>
      <td><code>String(100)</code> Address line 1</td>
      <td>123 Main Street</td>
    </tr>
    <tr>
      <td>address.line2<br/><code>optional</code></td>
      <td><code>String(100)</code> Address line 2</td>
      <td>Apartment 4B</td>
    </tr>
    <tr>
      <td>address.city<br/><code>optional</code></td>
      <td><code>String(50)</code> City</td>
      <td>Mumbai</td>
    </tr>
    <tr>
      <td>address.state<br/><code>optional</code></td>
      <td><code>String(50)</code> State</td>
      <td>Maharashtra</td>
    </tr>
    <tr>
      <td>address.country<br/><code>optional</code></td>
      <td><code>String(50)</code> Country</td>
      <td>India</td>
    </tr>
    <tr>
      <td>address.pincode<br/><code>optional</code></td>
      <td><code>String(10)</code> PIN/ZIP code</td>
      <td>400001</td>
    </tr>
    <tr>
      <td>updateVectors<br/><code>optional</code></td>
      <td><code>String(255)</code> Comma-separated list of fields to update</td>
      <td>emailId,address</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

> **Note**: Either `customerId` or `urn` must be provided.

## Response Parameters
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


## Sample Request

### Encrypted Packet
```bash
curl --location --request POST 'https://apitest.payu.in/loyalty-points/v1/wallet/onboarding/v3/updateProfile' \
--header 'walletIdentifier: CLW' \
--header 'date: Wed, 12 Jun 2024 08:53:43 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="hmac_generated_signature"' \
--header 'Content-Type: application/json' \
--data-raw '{
  "token": "h/0YSUd9jKOQ8+2Dc3Phr4s7vxyz123..."
}'
```

### Decrypted Packet
```json
{
  "messageCode": 1280,
  "clientTxnId": "ABC0987654321",
  "requestDateTime": "20230804182306",
  "productId": "9",
  "customerId": "62508",
  "firstName": "Jacob",
  "lastName": "James",
  "emailId": "jacob12@example.com",
  "mobileNumber": "919988776655",
  "dateOfBirth": "19951201",
  "gender": "Male",
  "address": {
    "line1": "123 Main Street",
    "line2": "Apartment 4B",
    "city": "Mumbai",
    "state": "Maharashtra",
    "country": "India",
    "pincode": "400001"
  },
  "updateVectors": "emailId,address"
}
```

## Sample Response

### Encrypted Response
```json
{
  "result": "h/0YSUd9jKOQ8+2Dc3Phr4s7vxyz789..."
}
```

### Decrypted Response
```json
{
  "responseCode": "00",
  "messageCode": 1281,
  "clientTxnId": "ABC0987654321",
  "customerId": "62508",
  "urn": 7000000008,
  "bankId": "123",
  "cardProfileId": "CP001",
  "responseMessage": "PROFILE UPDATED SUCCESSFULLY"
}
```

## HTTP Status Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | OK - Request processed successfully |
| 400 | Bad Request - Invalid request parameters |
| 401 | Unauthorized - Authentication failed |
| 404 | Not Found - Customer not found |
| 500 | Internal Server Error |

## Error Codes

| Error Code | Description |
| ---------- | ----------- |
| 1281 | Profile updated successfully |
| 1010 | Invalid message code |
| 1020 | Missing required parameters |
| 1040 | Customer not found |
| 1282 | Invalid update vector |
| 1283 | Profile update failed |
