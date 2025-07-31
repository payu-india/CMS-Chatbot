---
title: PG Load API
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Load** API allows you to add funds to a wallet via PayU payment gateway using non-seamless integration. This API initiates a payment flow that redirects the customer to complete the transaction.

## Environment

| Environment | URL                                                             |
| ----------- | --------------------------------------------------------------- |
| Test        | `https://apitest.payu.in/loyalty-points/ppi/payment/pg-load/v1` |
| Production  | `https://api.payu.in/loyalty-points/ppi/payment/pg-load/v1`     |

**HTTP Method**: POST

## Authentication

This API uses HMAC-SHA512 authentication. Refer to the [Authentication Guide](/docs/authentication) for detailed implementation.

## Request Headers

| Parameter                                    | Description                                                                  |
| -------------------------------------------- | ---------------------------------------------------------------------------- |
| walletIdentifier<br /><code>mandatory</code> | <code>String</code> Program Type (e.g., CLW)                                 |
| date<br /><code>mandatory</code>             | <code>String</code> GMT formatted date (e.g., Thu, 17 Feb 2022 08:17:59 GMT) |
| Authorization<br /><code>mandatory</code>    | <code>String</code> HMAC-SHA512-based authentication token                   |
| Content-Type<br /><code>mandatory</code>     | <code>String</code> application/json                                         |

## Request Parameters

### Body Parameters

The request body contains both encrypted and decrypted parameters.

#### Encrypted

| Parameter                         | Description                                                                                    |
| --------------------------------- | ---------------------------------------------------------------------------------------------- |
| token<br /><code>mandatory</code> | <code>String</code> AES-192-CBC encrypted request body containing all the decrypted parameters |

#### Decrypted

| Parameter                                         | Description                                                                                | Example                                                    |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| clientTxnId<br /><code>mandatory</code>           | <code>Alphanumeric(100)</code> Unique transaction ID from the calling application          | PGLOAD202400001                                            |
| requestDateTime<br /><code>mandatory</code>       | <code>Numeric(14)</code> Local timestamp of transaction initiation (YYYYMMDDHHMMSS format) | 20230822183015                                             |
| customer.firstName<br /><code>mandatory</code>    | <code>String(50)</code> Customer first name                                                | Alice                                                      |
| customer.lastName<br /><code>optional</code>      | <code>String(50)</code> Customer last name                                                 | Smith                                                      |
| customer.mobileNumber<br /><code>mandatory</code> | <code>Numeric(15)</code> Customer mobile number with country code                          | 919988776655                                               |
| customer.emailAddress<br /><code>optional</code>  | <code>String(50)</code> Customer email address                                             | [alice.smith@example.com](mailto:alice.smith@example.com)  |
| loadAmount<br /><code>mandatory</code>            | <code>Numeric(12)</code> Amount to load in implied decimals (e.g., 4100 = ₹41)             | 4100                                                       |
| currency<br /><code>mandatory</code>              | <code>String(3)</code> Currency code                                                       | INR                                                        |
| surl<br /><code>mandatory</code>                  | <code>String(255)</code> Success URL for redirection after successful payment              | [https://success.example.com](https://success.example.com) |
| furl<br /><code>mandatory</code>                  | <code>String(255)</code> Failure URL for redirection after failed payment                  | [https://failure.example.com](https://failure.example.com) |
| urn<br /><code>conditional</code>                 | <code>Numeric(11)</code> Wallet reference number (if customer exists)                      | 70000000008                                                |

## Response Parameters

| Parameter        | Description                                     | Example                                                                  |
| ---------------- | ----------------------------------------------- | ------------------------------------------------------------------------ |
| responseCode     | Response status code                            | 00                                                                       |
| referenceId      | Unique transaction reference ID                 | e47293311906                                                             |
| data.redirectUrl | URL to redirect customer for payment completion | [https://pp1api.payu.in/...redirect](https://pp1api.payu.in/...redirect) |
| data.payuTxnId   | PayU transaction ID                             | 403993715527015245                                                       |
| responseMessage  | Response message                                | REQUEST PROCESSED SUCCESSFULLY                                           |

## Sample Request

### Encrypted Packet

```bash
curl --location --request POST 'https://apitest.payu.in/loyalty-points/ppi/payment/pg-load/v1' \
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
  "clientTxnId": "PGLOAD123456",
  "requestDateTime": "20230810123015",
  "customer": {
    "firstName": "Alice",
    "lastName": "Smith",
    "mobileNumber": "919988776655",
    "emailAddress": "alice.smith@example.com"
  },
  "loadAmount": 5000,
  "currency": "INR",
  "surl": "https://success.example.com",
  "furl": "https://failure.example.com"
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
  "referenceId": "e47293311906",
  "data": {
    "redirectUrl": "https://pp1api.payu.in/payment/op/v1/redirect?data=eyJhbGciOiJIUzI1NiJ9...",
    "payuTxnId": "403993715527015245"
  },
  "responseMessage": "REQUEST PROCESSED SUCCESSFULLY"
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

| Error Code | Description                 |
| ---------- | --------------------------- |
| 00         | Success                     |
| 1010       | Invalid message code        |
| 1020       | Missing required parameters |
| 1050       | Insufficient wallet balance |
| 1060       | Transaction limit exceeded  |

## Post-Transaction Flow

After receiving the response:

1. Redirect the customer to the `redirectUrl` provided in the response
2. Customer completes the payment on PayU's payment gateway
3. Customer is redirected back to your `surl` (success) or `furl` (failure) URL
4. Use the [PG Load Enquiry API](/reference/pg-load-enquiry-api) to verify the final transaction status