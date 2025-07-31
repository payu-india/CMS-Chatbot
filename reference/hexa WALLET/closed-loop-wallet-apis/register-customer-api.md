---
title: Register Customer API
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Register Customer** API allows you to register a new customer and facilitates the creation of a digital wallet. This API performs onboarding checks when opted by the issuer.

## Environment

| Environment | URL                                                      |
| ----------- | -------------------------------------------------------- |
| Test        | `http://apitest.payu.in/loyalty-points/v1/wallet/enroll` |
| Production  | `https://api.payu.in/loyalty-points/v1/wallet/enroll`    |

**HTTP Method**: POST

## Authentication

This API uses HMAC-SHA512 authentication. Refer to the [Authentication Guide](/docs/authentication) for detailed implementation.

## Request parameters

### Header

| Parameter          | Type   | Mandatory | Description                                              |
| ------------------ | ------ | --------- | -------------------------------------------------------- |
| `walletIdentifier` | String | Yes       | Program Type (e.g., CLW)                                 |
| `date`             | String | Yes       | GMT formatted date (e.g., Thu, 17 Feb 2022 08:17:59 GMT) |
| `Authorization`    | String | Yes       | HMAC-SHA512-based authentication token                   |
| `Content-Type`     | String | Yes       | application/json                                         |

## Body

The request body contains both encrypted and decrypted parameters.

#### Encrypted

| Parameter | Type   | Description                                                                |
| --------- | ------ | -------------------------------------------------------------------------- |
| `token`   | String | AES-192-CBC encrypted request body containing all the decrypted parameters |

#### Decrypted

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Type
      </th>

      <th>
        Mandatory
      </th>

      <th>
        Character Limit
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `messageCode`
      </td>

      <td>
        Numeric
      </td>

      <td>
        Yes
      </td>

      <td>
        4
      </td>

      <td>
        API code to identify Register Customer API
      </td>

      <td>
        3510
      </td>
    </tr>

    <tr>
      <td>
        `clientTxnId`
      </td>

      <td>
        Alphanumeric
      </td>

      <td>
        Yes
      </td>

      <td>
        100
      </td>

      <td>
        Unique transaction ID from the calling application
      </td>

      <td>
        20150701235959xhstiesqfds
      </td>
    </tr>

    <tr>
      <td>
        `requestDateTime`
      </td>

      <td>
        Numeric
      </td>

      <td>
        Yes
      </td>

      <td>
        14
      </td>

      <td>
        Local timestamp of transaction initiation (YYYYMMDDHHMMSS format)
      </td>

      <td>
        20230620123143
      </td>
    </tr>

    <tr>
      <td>
        `customerId`
      </td>

      <td>
        String
      </td>

      <td>
        Optional
      </td>

      <td>
        50
      </td>

      <td>
        Caller-defined unique customer ID. Auto-generated if not provided
      </td>

      <td>
        89342546
      </td>
    </tr>

    <tr>
      <td>
        `customerDetails.firstName`
      </td>

      <td>
        String
      </td>

      <td>
        Yes
      </td>

      <td>
        50
      </td>

      <td>
        Customer first name. No invalid symbols allowed
      </td>

      <td>
        Sourav
      </td>
    </tr>

    <tr>
      <td>
        `customerDetails.middleName`
      </td>

      <td>
        String
      </td>

      <td>
        Optional
      </td>

      <td>
        50
      </td>

      <td>
        Customer middle name
      </td>

      <td>
        Kumar
      </td>
    </tr>

    <tr>
      <td>
        `customerDetails.lastName`
      </td>

      <td>
        String
      </td>

      <td>
        Optional
      </td>

      <td>
        50
      </td>

      <td>
        Customer last name
      </td>

      <td>
        Mishra
      </td>
    </tr>

    <tr>
      <td>
        `customerDetails.mobileNumber`
      </td>

      <td>
        Numeric
      </td>

      <td>
        Yes
      </td>

      <td>
        15
      </td>

      <td>
        ISD-coded, valid unique mobile number
      </td>

      <td>
        919988776655
      </td>
    </tr>

    <tr>
      <td>
        `customerDetails.emailAddress`
      </td>

      <td>
        String
      </td>

      <td>
        Optional
      </td>

      <td>
        50
      </td>

      <td>
        Valid email address
      </td>

      <td>
        [sourav.mishra@gmail.com](mailto:sourav.mishra@gmail.com)
      </td>
    </tr>

    <tr>
      <td>
        `customerDetails.dateOfBirth`
      </td>

      <td>
        String
      </td>

      <td>
        Yes
      </td>

      <td>
        10
      </td>

      <td>
        Date of birth (DD-MM-YYYY format)
      </td>

      <td>
        11-07-1993
      </td>
    </tr>

    <tr>
      <td>
        `kycProfile`
      </td>

      <td>
        Numeric
      </td>

      <td>
        Yes
      </td>

      <td>
        3
      </td>

      <td>
        Type of KYC: Min KYC (30), Shortfall KYC (300), Full KYC (150)
      </td>

      <td>
        150
      </td>
    </tr>

    <tr>
      <td>
        `riskCategory`
      </td>

      <td>
        String
      </td>

      <td>
        Yes
      </td>

      <td>
        20
      </td>

      <td>
        Risk type: Low, Medium, High (Low=100, Medium=500, High=200)
      </td>

      <td>
        Low
      </td>
    </tr>

    <tr>
      <td>
        `productId`
      </td>

      <td>
        Numeric
      </td>

      <td>
        Yes
      </td>

      <td>
        5
      </td>

      <td>
        Program/product ID
      </td>

      <td>
        121
      </td>
    </tr>

    <tr>
      <td>
        `formFactorRequired`
      </td>

      <td>
        Boolean
      </td>

      <td>
        Yes
      </td>

      <td>
        *
      </td>

      <td>
        Indicates whether a form factor is required (True/False)
      </td>

      <td>
        true
      </td>
    </tr>
  </tbody>
</Table>

## Response Parameters

| Parameter                  | Type    | Mandatory   | Description                                            | Example                          |
| -------------------------- | ------- | ----------- | ------------------------------------------------------ | -------------------------------- |
| `responseCode`             | String  | Yes         | Response status code                                   | 00                               |
| `messageCode`              | Numeric | Conditional | API response code                                      | 3511                             |
| `clientTxnId`              | String  | Conditional | Mirrors the request's clientTxnId                      | 20150701235959xhstiesqfds        |
| `formfactor.accountNumber` | String  | Conditional | Generated account number for form factors              | 72623345                         |
| `formfactor.uniqueNumber`  | Numeric | Conditional | Unique number generated for form factors               | 8543213624292443                 |
| `formfactor.urn`           | Numeric | Conditional | Proxy reference number generated for the unique number | 70000000008                      |
| `responseMessage`          | String  | Yes         | Response message                                       | CUSTOMER REGISTERED SUCCESSFULLY |

## Sample Request

### Encrypted Packet

```bash
curl --location --request POST 'http://apitest.payu.in/loyalty-points/v1/wallet/enroll' \
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
  "messageCode": 3510,
  "clientTxnId": "txn12345",
  "requestDateTime": "20230810123015",
  "customerDetails": {
    "firstName": "Alice",
    "lastName": "Smith",
    "dateOfBirth": "12-12-2000",
    "mobileNumber": "917001122334"
  },
  "kycProfile": 150,
  "riskCategory": "Low",
  "productId": 35,
  "formFactorRequired": true
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
  "messageCode": 3511,
  "clientTxnId": "txn12345",
  "formFactor": {
    "uniqueNumber": "7262334512345678",
    "urn": 10000234
  },
  "responseMessage": "CUSTOMER REGISTERED SUCCESSFULLY"
}
```

## HTTP Status Codes

| Status Code | Description                              |
| ----------- | ---------------------------------------- |
| 200         | OK - Request processed successfully      |
| 400         | Bad Request - Invalid request parameters |
| 401         | Unauthorized - Authentication failed     |
| 500         | Internal Server Error                    |

## Error Codes

| Error Code | Description                      |
| ---------- | -------------------------------- |
| 3511       | Customer registered successfully |
| 1010       | Invalid message code             |
| 1020       | Missing required parameters      |
| 1030       | Customer already exists          |