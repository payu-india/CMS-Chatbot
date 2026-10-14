---
title: PG Load API
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: PG Load API
deprecated: false
hidden: false
metadata:
  robots: index
---
The **PG Load** API allows you to create a credit transaction entry through a payment gateway.

## Environment

| Environment | URL                                                            |
| ----------- | -------------------------------------------------------------- |
| Test        | `https://apitest.payu.in/loyalty-points/ppi/payment/pg-load/v1` |
| Production  | `https://api.payu.in/loyalty-points/ppi/payment/pg-load/v1`     |

**HTTP Method**: POST

## Request Headers

<Closed_Loop_HMAC />

<Callout icon="🔐" theme="info">
  Sign every request with **HMAC-SHA256** over the `date` and `digest` headers:

  * `date`: Current time in GMT (RFC 1123 format), for example, `Tue, 13 Oct 2026 07:05:59 GMT`.
  * `digest`: `Base64(SHA-256(raw JSON request body))`
  * `authorization`: `hmac username="<merchant_key>", algorithm="hmac-sha256", headers="date digest", signature="<signature>"`, where `signature = Base64(HMAC-SHA256("date: <date>\ndigest: <digest>", <merchant_secret>))`
</Callout>

## Request Parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
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
        clientTxnId<br /><code>mandatory</code>
      </td>

      <td>
        <code>Alphanumeric(14)</code> Unique transaction ID for this request
      </td>

      <td>
        Reload_V3_1234
      </td>
    </tr>

    <tr>
      <td>
        requestDateTime<br /><code>mandatory</code>
      </td>

      <td>
        <code>Numeric(14)</code> Timestamp of the transaction (YYYYMMDDHHMMSS format)
      </td>

      <td>
        20230822183015
      </td>
    </tr>

    <tr>
      <td>
        customerId<br /><code>optional</code>
      </td>

      <td>
        <code>Numeric(20)</code> A unique customer ID from the calling application. If the value is not passed in the request, the platform will auto-generate a unique value for this field.
      </td>

      <td>
        89342546
      </td>
    </tr>

    <tr>
      <td>
        customer.firstName<br /><code>mandatory</code>
      </td>

      <td>
        <code>String(50)</code> Customer first name. The following validations are done for this field:

        1. Start and end with valid characters (no extra characters outside the allowed set).
        2. Contain only: Uppercase letters (A-Z), Lowercase letters (a-z), Periods (.), Spaces ( ). Have at least one character and no invalid symbols like numbers, special characters outside the allowed set, etc.
        3. Total length of string should be max 50 chars (including space) and it can only contain characters, hyphens and single spaces in between words. No double spaces allowed between two words.
      </td>

      <td>
        Ashish
      </td>
    </tr>

    <tr>
      <td>
        customer.lastName<br /><code>mandatory</code>
      </td>

      <td>
        <code>String(50)</code> Customer last name. The following validations are done for this field:

        1. Start and end with valid characters (no extra characters outside the allowed set).
        2. Contain only: Uppercase letters (A-Z), Lowercase letters (a-z), Periods (.), Spaces ( ). Have at least one character and no invalid symbols like numbers, special characters outside the allowed set, etc.
        3. Total length of string should be max 50 chars (including space) and it can only contain characters, hyphens and single spaces in between words. No double spaces allowed between two words.
      </td>

      <td>
        Mishra
      </td>
    </tr>

    <tr>
      <td>
        customer.mobileNumber<br /><code>mandatory</code>
      </td>

      <td>
        <code>Numeric(13)</code> Customer's mobile number with country code
      </td>

      <td>
        919988776655
      </td>
    </tr>

    <tr>
      <td>
        customer.email<br /><code>optional</code>
      </td>

      <td>
        <code>String(50)</code> Valid email address in a valid email format
      </td>

      <td>
        ashish@gmail.com
      </td>
    </tr>

    <tr>
      <td>
        surl<br /><code>mandatory</code>
      </td>

      <td>
        <code>String</code> The URL to which the customer is redirected if the PG transaction is a success
      </td>

      <td>
        <redacted URL>
      </td>
    </tr>

    <tr>
      <td>
        furl<br /><code>mandatory</code>
      </td>

      <td>
        <code>String</code> The URL to which the customer is redirected if the PG transaction is a failure
      </td>

      <td>
        <redacted URL>
      </td>
    </tr>

    <tr>
      <td>
        currency<br /><code>mandatory</code>
      </td>

      <td>
        <code>String</code> Currency code of the currency used.
      </td>

      <td>
        INR
      </td>
    </tr>

    <tr>
      <td>
        loadAmount<br /><code>mandatory</code>
      </td>

      <td>
        <code>Numeric(12)</code> Amount to load (expressed in implied decimals)
      </td>

      <td>
        1500
      </td>
    </tr>

    <tr>
      <td>
        seamlessTxn<br /><code>mandatory</code>
      </td>

      <td>
        <code>Boolean</code> Identifies whether it is a seamless or non-seamless transaction. This must be either true or false, where:

        * **false** indicates it is a non-seamless transaction.
        * **true** indicates it is a seamless transaction.
      </td>

      <td>
        false
      </td>
    </tr>
  </tbody>
</Table>

{/* REVIEW: Parameter renamed from seamlessTransaction to seamlessTxn to match the CTP-378 cURL and the response field. Confirm with engineering. */}

## Response Parameters

| Parameter        | Description                                                  | Example                                                              |
| ---------------- | ------------------------------------------------------------ | -------------------------------------------------------------------- |
| referenceId      | Reference ID of the transaction                              | 590bb71a22c54d0db685cdd752da1d2f                                     |
| data.redirectUrl | Redirection link                                             | https://apitest.payu.in/public/#/590bb71a22c54d0db685cdd752da1d2f    |
| seamlessTxn      | Identifies whether it is a seamless or non-seamless transaction | true/false                                                        |

## Sample Request

```curl
curl --location --request POST 'https://apitest.payu.in/loyalty-points/ppi/payment/pg-load/v1' \
--header 'walletIdentifier: CLW' \
--header 'date: Tue, 13 Oct 2026 07:05:59 GMT' \
--header 'digest: BASE64_SHA256_OF_REQUEST_BODY' \
--header 'authorization: hmac username="YOUR_MERCHANT_KEY", algorithm="hmac-sha256", headers="date digest", signature="YOUR_HMAC_SIGNATURE"' \
--header 'Content-Type: application/json' \
--data-raw '{
  "clientTxnId": "testRe9871",
  "requestDateTime": "20250121182438",
  "customer": {
    "firstName": "Ashish",
    "lastName": "Mishra",
    "mobileNumber": "919999999999"
  },
  "surl": "<redacted URL>",
  "furl": "<redacted URL>",
  "currency": "INR",
  "loadAmount": 99999,
  "seamlessTxn": false
}'
```

## Sample Response

```json
{
  "referenceId": "590bb71a22c54d0db685cdd752da1d2f",
  "data": {
    "redirectUrl": "https://apitest.payu.in/public/#/590bb71a22c54d0db685cdd752da1d2f"
  },
  "seamlessTxn": false
}
```

## HTTP Status Codes

| Status Code | Description                              |
| ----------- | ---------------------------------------- |
| 200         | OK - Request processed successfully      |
| 400         | Bad Request - Invalid request parameters |
| 401         | Unauthorized - Authentication failed     |
| 404         | Not Found - Wallet not found             |
| 500         | Internal Server Error                    |

## Error Codes

| Error Code | Description                 |
| ---------- | --------------------------- |
| 1081       | Load transaction successful |
| 1010       | Invalid message code        |
| 1020       | Missing required parameters |
| 1040       | Wallet not found            |
| 1050       | Transaction limit exceeded  |
