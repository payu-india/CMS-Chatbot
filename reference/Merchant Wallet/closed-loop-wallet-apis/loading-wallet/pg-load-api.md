---
title: PG Load API
deprecated: false
hidden: false
metadata:
  robots: index
---
The **PG Load **API allows you to create a credit transaction entry directly into the wallet without going through a payment gateway. This is useful for scenarios like cashback, rewards, or direct fund transfers.

## Environment

| Environment | URL                                                           |
| ----------- | ------------------------------------------------------------- |
| Test        | https://apitest.payu.in/loyalty-points/ppi/payment/pg-load/v1 |
| Production  | `https://api.payu.in//loyalty-points/ppi/payment/pg-load/v1   |

**HTTP Method**: PATCH

## Request Headers

<Closed_Loop_HMAC />

## Request Parameters

### Body Parameters

The request body contains both encrypted and decrypted parameters.

#### Encrypted

| Parameter                         | Description                                                                                    |
| --------------------------------- | ---------------------------------------------------------------------------------------------- |
| token<br /><code>mandatory</code> | <code>String</code> AES-192-CBC encrypted request body containing all the decrypted parameters |

#### Decrypted

<Table>
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
        customerId
        <code>optional</code>
      </td>

      <td>
        <code>Numeric(20)</code> A unique customer ID from calling application to be shared. If the value is not passed in the request, the platform will auto-generate a unique value for this
        field."
      </td>

      <td>
        89342546
      </td>
    </tr>

    <tr>
      <td>
        customer.firstName
        <code>mandatory</code>
      </td>

      <td>
        <code>String(50)</code> Customer first Name. The following validations for this field :  

        1. Start and end with valid characters (no extra characters outside the allowed set).   
        2. Contain only:   Uppercase letters (A-Z)   Lowercase letters (a-z)   Periods (.)   Spaces ( )   Have at least one character and no invalid symbols like numbers, special characters outside the allowed set, etc.
        3. Total length of string should be max 50 chars (including space) and it can only contain characters, hyphens and single spaces in b/w words. No double spaces allowed b/w 2 words
      </td>

      <td>
        Ashish
      </td>
    </tr>

    <tr>
      <td>
        customer.lastName
        <code>mandatory</code>
      </td>

      <td>
        <code>String(50)</code> Customer last name. The following validations are done for this field: 

        1. Start and end with valid characters (no extra characters outside the allowed set). 
        2. Contain only:   Uppercase letters (A-Z)   Lowercase letters (a-z)   Periods (.)   Spaces ( )   Have at least one character and no invalid symbols like numbers, special characters outside the allowed set, etc.
        3. Total length of string should be max 50 chars (including space) and it can only contain characters, hyphens and single spaces in b/w words. No double spaces allowed b/w 2 words
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
        customer.email
        <br/> <code>mandatory</code>
      </td>

      <td>
        <code>String(50)</code> Valid Email address with valid email format
      </td>

      <td>
        ashsih@gmail.com
      </td>
    </tr>

    <tr>
      <td>
        surl<br /><code>mandatory</code>
      </td>

      <td>
        <code>String</code> This is the URL to which customer is redirected incase if PG Transaction
        is a success
      </td>

      <td>
        https://pp1admin.payu.in/test_response
      </td>
    </tr>

    <tr>
      <td>
        furl<br /><code>mandatory</code>
      </td>

      <td>
        <code>String</code> This is the URL to which customer is redirected incase if PG Transaction
        is a failure
      </td>

      <td>
        https://pp1admin.payu.in/test_response
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
        seamlessTransaction<br /><code>mandatory</code>
      </td>

      <td>
        <code>String</code> Identifier if it is a seamless transaction or non seamless. This must be either true or false, where:

        * **false** indicates it is a non-seamless transaction. 
        * **true**indicates it is a seamless transaction.
      </td>

      <td>
        false
      </td>
    </tr>
  </tbody>
</Table>

## Response Parameters

<HTMLBlock>{`
<table>
    <tbody>
        <tr>
            <td style="background-color:#9d9d9d;border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;vertical-align:top;width:96.0px;">
                Field
            </td>
            <td style="background-color:#9d9d9d;border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;vertical-align:top;width:87.0px;">
                Description
            </td>
            <td style="background-color:#9d9d9d;border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;vertical-align:top;width:136.0px;">
                Example
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:32.0px;padding:4.0px;vertical-align:top;width:96.0px;">
                referenceId
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:32.0px;padding:4.0px;vertical-align:top;width:87.0px;">
                Reference ID of Transaction
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:32.0px;padding:4.0px;vertical-align:top;width:136.0px;">
                e47293311906aeb0eb65168adacdce01
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:56.0px;padding:4.0px;vertical-align:top;width:96.0px;">
                data.redirectUrl
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:56.0px;padding:4.0px;vertical-align:top;width:87.0px;">
                Redirection link
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:56.0px;padding:4.0px;vertical-align:top;width:136.0px;">
                "<a href="https://pp1api.payu.in/public/#/e47293311906aeb0eb65168adacdce0">https://pp1api.payu.in/public/#/e47293311906aeb0eb65168adacdce0</a>”
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:57.0px;padding:4.0px;vertical-align:top;width:96.0px;">
                seamlessTxn
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:57.0px;padding:4.0px;vertical-align:top;width:87.0px;">
                Identifier if it is a seamless transaction or non seamless
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:57.0px;padding:4.0px;vertical-align:top;width:136.0px;">
                true/false
            </td>
        </tr>
    </tbody>
</table>
`}</HTMLBlock>

<br />

## Sample Request

### Encrypted Packet

```bash
curl --location --request PATCH 'https://apitest.payu.in/loyalty-points/v1/wallet/load-account' \
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
  "messageCode": "1080",
  "clientTxnId": "Reload_V3_1234",
  "requestDateTime": "20230822183015",
  "urn": 70000000008,
  "transactionAmount": 1500,
  "sourceType": 1,
  "sender": "Amazon",
  "fundFlowType": "I",
  "implId": "I|70190",
  "implType": "PG_W2A_I"
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
  "messageCode": 1081,
  "clientTxnId": "Reload_V3_1234",
  "urn": 1000019,
  "accosaTransactionId": 1234567890,
  "accosaRefNo": 20230822001,
  "availableBalance": 1500,
  "responseMessage": "SUCCESS"
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
