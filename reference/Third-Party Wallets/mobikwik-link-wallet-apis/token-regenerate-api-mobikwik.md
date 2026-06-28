---
title: Token Regenerate API - Mobikwik
deprecated: false
hidden: false
metadata:
  robots: index
---
This API regenerates a wallet token using an existing token, ensuring continued wallet access without requiring new OTP verification.

## Environment

| Environment    | URL                                            |
| -------------- | ---------------------------------------------- |
| **Test**       | `https://test.mobikwik.com/tokengenerate`      |
| **Production** | `https://walletapi.mobikwik.com/tokengenerate` |

**Method:** `GET`

<Callout icon="📘" theme="info">
  ###

  **Note:**

  This API uses the same endpoint as Token Generate API but with different parameters and method.
</Callout>

## Request parameters

| Parameter                                       | Description                                                                   | Example               |
| ----------------------------------------------- | ----------------------------------------------------------------------------- | --------------------- |
| mid<br /><code>mandatory</code>                 | <code>String</code> Unique parent merchant ID                                 | `MBK9006`             |
| cell<br /><code>mandatory</code>                | <code>String</code> Mobile number of the user                                 | `9311032820`          |
| msgcode<br /><code>mandatory</code>             | <code>String</code> Message code to be sent                                   | `504`                 |
| merchantname<br /><code>mandatory</code>        | <code>String</code> Alias for the merchant                                    | `TestMerchant`        |
| amount<br /><code>mandatory</code>              | <code>Integer</code> Maximum cap amount (not transaction amount)              | `200`                 |
| token<br /><code>mandatory</code>               | <code>String</code> Existing token to be regenerated                          | `MBK_TOKEN_123456789` |
| tokentype<br /><code>mandatory</code>           | <code>Integer</code> Token type (1 for token generation)                      | `1`                   |
| checksum<br /><code>mandatory</code>            | <code>String</code> Calculated checksum for validation                        | `calculated_hash`     |
| aggregatedMerchantId<br /><code>optional</code> | <code>String</code> Unique ID for aggregated merchants (For Aggregators Only) | `AGG123`              |

📘 **Important:** The `amount` parameter represents the maximum cap amount, not the actual transaction amount. The debit API will work for amounts less than or equal to this value.

### Checksum generation

#### For aggregators

**Format:** `'amount''cell''merchantname''mid''msgcode''token''tokentype''aggregatedMerchantId'`

#### For direct merchants

**Format:** `'amount''cell''merchantname''mid''msgcode''token''tokentype'`

**Algorithm:** HMAC SHA256<br />**Secret Key:** Provided by Mobikwik during merchant onboarding

<Callout icon="📘" theme="info">
  ###

  **Note:**

  For merchant `MBK9006`, the secret key is `ju6tygh7u7tdg554k098ujd5468o`. Each merchant will receive their unique secret key.
</Callout>

## Sample request

```bash
GET https://test.mobikwik.com/tokengenerate?mid=MBK9006&cell=9311032820&msgcode=504&merchantname=TestMerchant&amount=200&token=MBK_TOKEN_123456789&tokentype=1&checksum=calculated_hash_value
```

## Response parameters

<Table>
  <thead>
    <tr>
      <th>
        Field
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
        messagecode
      </td>

      <td>
        <code>String</code> Message code from request
      </td>

      <td>
        `504`
      </td>
    </tr>

    <tr>
      <td>
        status
      </td>

      <td>
        <code>String</code> Transaction status
      </td>

      <td>
        `SUCCESS`
      </td>
    </tr>

    <tr>
      <td>
        statuscode
      </td>

      <td>
        <code>String</code> Numeric status code
      </td>

      <td>
        `0`
      </td>
    </tr>

    <tr>
      <td>
        statusdescription
      </td>

      <td>
        <code>String</code> Description of the status
      </td>

      <td>
        `Token regenerated successfully`
      </td>
    </tr>

    <tr>
      <td>
        token
      </td>

      <td>
        <code>String</code> New generated wallet token
      </td>

      <td>
        `MBK_TOKEN_987654321`
      </td>
    </tr>

    <tr>
      <td>
        checksum
      </td>

      <td>
        <code>String</code> Response checksum for validation
      </td>

      <td>
        `8feac7700a4efd1ef0  
                8ea0ec5bf5921c3f1fc33
                98944421978794b9ada1c2c47`
      </td>
    </tr>
  </tbody>
</Table>

### Response Attributes

The response checksum that will be returned to the users will have the following format:

<HTMLBlock>{`
<table>
    <tbody>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:94.0px;">
                <strong>Status &amp; Status Code</strong>
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:58.0px;">
                <strong>Status Code</strong>
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:285.0px;">
                <strong>Status description</strong>
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:94.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:58.0px;">
                22
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:285.0px;">
                Merchant does not Exist
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:94.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:58.0px;">
                50
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:285.0px;">
                Order Id already processed with this merchant
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:94.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:58.0px;">
                53
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:285.0px;">
                Parameter email is invalid
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:94.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:58.0px;">
                54
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:285.0px;">
                Parameter amount must be numeric with max 2 decimal places only
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:94.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:58.0px;">
                55
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:285.0px;">
                Parameter cell is invalid. It must be numeric, have 10 digits and start with 7,8 or 9
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:94.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:58.0px;">
                99
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:285.0px;">
                Unexpected Error
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:94.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:58.0px;">
                150
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:285.0px;">
                Invalid Message code specified in Input
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:94.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:58.0px;">
                155
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:285.0px;">
                Either OTP missing or Invalid OTP
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:94.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:58.0px;">
                158
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:285.0px;">
                Please Provide either registered mobikwik Email or Mobile (Not Both) to uniquely identify you
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:94.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:58.0px;">
                181
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:285.0px;">
                Either Email or Mobile is required for OTP generation
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:94.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:58.0px;">
                190
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:285.0px;">
                Token Or OTP missing
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:94.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:58.0px;">
                198
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:285.0px;">
                Either Token missing or Invalid Token or Token Expired
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:94.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:58.0px;">
                200
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:285.0px;">
                Provide Either OTP or Token
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:94.0px;">
                SUCCESS
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:58.0px;">
                0
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:285.0px;">
                Transaction completed successfully
            </td>
        </tr>
    </tbody>
</table>
`}</HTMLBlock>

<br />

📘 **Note:** Always validate the response checksum to ensure data integrity and security.

## Sample response

<Callout icon="📘" theme="info">
  ###

  **Notes**:

  - Always validate the response checksum for security
  - The old token becomes invalid after successful regeneration
  - Implement proper error handling for token regeneration failures
  - Consider implementing automatic token refresh mechanisms
</Callout>

### Success response

```json
{
  "messagecode": "504",
  "status": "SUCCESS",
  "statuscode": "0",
  "statusdescription": "Token regenerated successfully",
  "token": "MBK_TOKEN_987654321",
  "checksum": "8feac7700a4efd1ef08ea0ec5bf5921c3f1fc3398944421978794b9ada1c2c47"
}
```

### Failure scenarios

- Failure Response - Invalid Token

```json
{
  "messagecode": "504",
  "status": "FAILURE",
  "statuscode": "201",
  "statusdescription": "Invalid or expired token provided",
  "checksum": "f25ac916fe4806591e16269fc912771456437b784fa144a77fa9842d154920cc"
}
```

- Failure Response - Token Regeneration Limit Exceeded

```json
{
  "messagecode": "504",
  "status": "FAILURE",
  "statuscode": "202",
  "statusdescription": "Token regeneration limit exceeded",
  "checksum": "e35bc916fe4806591e16269fc912771456437b784fa144a77fa9842d154920dd"
}
```

<br />
