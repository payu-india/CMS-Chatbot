---
title: Retrieve Customer Record API
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Retrieve Customer Record** API allows you to fetch customer details using various identifiers such as customerId, mobileNumber, email, or urn.

## Environment

| Environment | URL                                                                   |
| ----------- | --------------------------------------------------------------------- |
| Test        | `https://apitest.payu.in/loyalty-points/v1/wallet/retrieveCustRecord` |
| Production  | `https://api.payu.in/loyalty-points/v1/wallet/retrieveCustRecord`     |

**HTTP Method**: POST

## Request Headers

<Closed_Loop_HMAC />

## Request Parameters

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
            <td>messageCode<br><code>mandatory</code></td>
            <td><code>Numeric(4)</code> API code to identify Retrieve Customer API</td>
            <td>1930</td>
        </tr>
        <tr>
            <td>clientTxnId<br><code>mandatory</code></td>
            <td><code>Alphanumeric(100)</code> Unique transaction ID from the calling application</td>
            <td>retrieval12</td>
        </tr>
        <tr>
            <td>customerMobile<br><code>conditional</code></td>
            <td><code>Numeric(15)</code> Customer mobile number with country code</td>
            <td>918765432123</td>
        </tr>
        <tr>
            <td>customerId<br><code>conditional</code></td>
            <td><code>String(20)</code> Unique customer ID from the calling application</td>
            <td>620934850</td>
        </tr>
        <tr>
            <td>urn<br><code>conditional</code></td>
            <td><code>Numeric(11)</code> Proxy wallet reference number</td>
            <td>70000000008</td>
        </tr>
    </tbody>
</table>
`}</HTMLBlock>

<br />

<Callout icon="📘" theme="info">
  **Note**: At least one of `customerMobile`, `customerId`, or `urn` must be provided.
</Callout>

## Response Parameters

| Parameter        | Description                       | Example                                             |
| ---------------- | --------------------------------- | --------------------------------------------------- |
| responseCode     | Response status code              | 00                                                  |
| messageCode      | API response code                 | 1931                                                |
| clientTxnId      | Mirrors the request's clientTxnId | retrieval12                                         |
| mobile           | Customer mobile number            | 918765432123                                        |
| email            | Customer email address            | [customer@example.com](mailto:customer@example.com) |
| firstName        | Customer first name               | John                                                |
| lastName         | Customer last name                | Doe                                                 |
| kycName          | KYC verified name                 | John Doe                                            |
| urn              | Wallet reference number           | 70000000008                                         |
| accountNumber    | Account number                    | 72623345                                            |
| walletStatus     | Current wallet status             | ACTIVE                                              |
| availableBalance | Current available balance         | 5000                                                |
| responseMessage  | Response message                  | CUSTOMER RECORD RETRIEVED SUCCESSFULLY              |

## Sample Request

### Encrypted Packet

```bash
curl --location --request POST 'https://apitest.payu.in/loyalty-points/v1/wallet/retrieveCustRecord' \
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
  "messageCode": 1930,
  "clientTxnId": "retrieval12",
  "customerMobile": "918765432123"
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
  "messageCode": 1931,
  "clientTxnId": "retrieval12",
  "mobile": "918765432123",
  "email": "customer@example.com",
  "firstName": "John",
  "lastName": "Doe",
  "kycName": "John Doe",
  "urn": 70000000008,
  "accountNumber": "72623345",
  "walletStatus": "ACTIVE",
  "availableBalance": 5000,
  "responseMessage": "CUSTOMER RECORD RETRIEVED SUCCESSFULLY"
}
```

## HTTP Status Codes

| Status Code | Description                              |
| ----------- | ---------------------------------------- |
| 200         | OK - Request processed successfully      |
| 400         | Bad Request - Invalid request parameters |
| 401         | Unauthorized - Authentication failed     |
| 404         | Not Found - Customer record not found    |
| 500         | Internal Server Error                    |

## Error Codes

| Error Code | Description                            |
| ---------- | -------------------------------------- |
| 1931       | Customer record retrieved successfully |
| 1010       | Invalid message code                   |
| 1020       | Missing required parameters            |
| 1040       | Customer not found                     |
