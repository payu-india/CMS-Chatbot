---
title: Token Generate API - Mobikwik
deprecated: false
hidden: false
metadata:
  robots: index
---
This API generates a wallet token after successful OTP verification, enabling secure and seamless wallet transactions.

## Environment

| Environment    | URL                                            |
| -------------- | ---------------------------------------------- |
| **Test**       | `https://test.mobikwik.com/tokengenerate`      |
| **Production** | `https://walletapi.mobikwik.com/tokengenerate` |

**Method:** `POST`

## Request parameters

| Parameter                                       | Description                                                                   | Example           |
| ----------------------------------------------- | ----------------------------------------------------------------------------- | ----------------- |
| mid<br /><code>mandatory</code>                 | <code>String</code> Unique parent merchant ID                                 | `MBK9006`         |
| cell<br /><code>mandatory</code>                | <code>String</code> Mobile number of the user                                 | `9311032820`      |
| msgcode<br /><code>mandatory</code>             | <code>String</code> Message code to be sent                                   | `504`             |
| merchantname<br /><code>mandatory</code>        | <code>String</code> Alias for the merchant                                    | `TestMerchant`    |
| amount<br /><code>mandatory</code>              | <code>Integer</code> Maximum cap amount (not transaction amount)              | `200`             |
| otp<br /><code>mandatory</code>                 | <code>Integer</code> OTP received on registered mobile number                 | `123456`          |
| tokentype<br /><code>mandatory</code>           | <code>Integer</code> Token type (1 for token generation)                      | `1`               |
| checksum<br /><code>mandatory</code>            | <code>String</code> Calculated checksum for validation                        | `calculated_hash` |
| aggregatedMerchantId<br /><code>optional</code> | <code>String</code> Unique ID for aggregated merchants (For Aggregators Only) | `AGG123`          |

<Callout icon="📘" theme="info">
  **Notes**:

  * The `amount` parameter represents the maximum cap amount, not the actual transaction amount
  * Token validity is 365 days (one year) by default, but can be customized per merchant requirements
  * If the user doesn't have a MobiKwik account, it will be created after submitting OTP
</Callout>

### Checksum generation

#### For aggregators

**Format:** `'amount''cell''merchantname''mid''msgcode''otp''tokentype''aggregatedMerchantId'`

#### For direct merchants

**Format:** `'amount''cell''merchantname''mid''msgcode''otp''tokentype'`

**Algorithm:** HMAC SHA256\
**Secret Key:** Provided by Mobikwik during merchant onboarding

📘 **Note:** For merchant `MBK9006`, the secret key is `ju6tygh7u7tdg554k098ujd5468o`. Each merchant will receive their unique secret key.

## Sample request

```bash
POST https://test.mobikwik.com/tokengenerate
Content-Type: application/x-www-form-urlencoded

mid=MBK9006&cell=9311032820&msgcode=504&merchantname=TestMerchant&amount=200&otp=123456&tokentype=1&checksum=calculated_hash_value
```

## Response parameters

| Field             | Description                                          | Example                                                            |
| ----------------- | ---------------------------------------------------- | ------------------------------------------------------------------ |
| messagecode       | <code>String</code> Message code from request        | `504`                                                              |
| status            | <code>String</code> Transaction status               | `SUCCESS`                                                          |
| statuscode        | <code>String</code> Numeric status code              | `0`                                                                |
| statusdescription | <code>String</code> Description of the status        | `Token generated successfully`                                     |
| token             | <code>String</code> Generated wallet token           | `MBK_TOKEN_123456789`                                              |
| checksum          | <code>String</code> Response checksum for validation | `8feac7700a4efd1ef08ea0ec5bf5921c3f1fc3398944421978794b9ada1c2c47` |

### Response attributes

<HTMLBlock>{`
<table>
    <tbody>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:63.0px;">
                <strong>Status</strong>
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:55.0px;">
                <strong>Status Code</strong>
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:319.0px;">
                <strong>Status description</strong>
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:55.0px;">
                22
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:319.0px;">
                Merchant does not Exist
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:55.0px;">
                50
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:319.0px;">
                Order Id already processed with this merchant
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:55.0px;">
                53
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:319.0px;">
                Parameter email is invalid
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:55.0px;">
                54
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:319.0px;">
                Parameter amount must be numeric with max 2 decimal places only
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:55.0px;">
                55
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:319.0px;">
                Parameter cell is invalid. It must be numeric, have 10 digits and start with 7,8 or 9
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:55.0px;">
                99
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:319.0px;">
                Unexpected Error
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:55.0px;">
                150
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:319.0px;">
                Invalid Message code specified in Input
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:55.0px;">
                155
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:319.0px;">
                Either OTP missing or Invalid OTP
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:55.0px;">
                158
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:319.0px;">
                Please Provide either registered mobikwik Email or Mobile (Not Both) to uniquely identify you
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:55.0px;">
                181
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:319.0px;">
                Either Email or Mobile is required for OTP generation
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:55.0px;">
                190
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:319.0px;">
                Token Or OTP missing
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:55.0px;">
                198
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:319.0px;">
                Either Token missing or Invalid Token or Token Expired
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:55.0px;">
                200
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:319.0px;">
                Provide Either OTP or Token
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:63.0px;">
                SUCCESS
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:55.0px;">
                0
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:319.0px;">
                Transaction completed successfully
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:55.0px;">
                157
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:319.0px;">
                Either Email or Mobile is required for OTP generation
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:55.0px;">
                161
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:319.0px;">
                Invalid OTP generated Wrong transaction details
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:55.0px;">
                162
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:319.0px;">
                Invalid OTP generated Wrong transaction amount
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:55.0px;">
                163
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:319.0px;">
                Invalid OTP generated OTP Exired
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:55.0px;">
                164
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:319.0px;">
                Either Invalid OTP (Expiry or OTP mismatch) or OTP mismatched due to mismatch in order id or transaction amount
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:55.0px;">
                200
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:319.0px;">
                Provide Either OTP or Token
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:55.0px;">
                450
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:319.0px;">
                OTP is expired. Please retry again.
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:55.0px;">
                198
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:319.0px;">
                Either Token missing or Invalid Token or Token Expired
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:44.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:44.0px;padding:4.0px;width:55.0px;">
                199
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:44.0px;padding:4.0px;width:319.0px;">
                Either Invalid Token (Expiry or Token mismatch) or Token mismatched due to transaction amount exceeding authorized amount
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:55.0px;">
                200
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:319.0px;">
                Provide Either OTP or Token
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:63.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:55.0px;">
                154
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:319.0px;">
                Invalid OTP Type Selected
            </td>
        </tr>
    </tbody>
</table>
`}</HTMLBlock>

<br />

📘 **Note:** Always validate the response checksum to ensure data integrity and security.

## Sample response

<Callout icon="📘" theme="info">
  **Notes**:

  * Always validate the response checksum for security
  * Store tokens securely and implement proper token lifecycle management
  * The generated token is required for wallet debit operations
</Callout>

### Success response

```json
{
  "messagecode": "504",
  "status": "SUCCESS",
  "statuscode": "0",
  "statusdescription": "Token generated successfully",
  "token": "MBK_TOKEN_123456789",
  "checksum": "8feac7700a4efd1ef08ea0ec5bf5921c3f1fc3398944421978794b9ada1c2c47"
}
```

### Failure scenarios

* **Failure response - Invalid OTP**

```json
{
  "messagecode": "504",
  "status": "FAILURE",
  "statuscode": "101",
  "statusdescription": "Invalid OTP provided",
  "checksum": "f25ac916fe4806591e16269fc912771456437b784fa144a77fa9842d154920cc"
}
```

* **Failure response - OTP Expired**

```json
{
  "messagecode": "504",
  "status": "FAILURE", 
  "statuscode": "102",
  "statusdescription": "OTP has expired",
  "checksum": "e35bc916fe4806591e16269fc912771456437b784fa144a77fa9842d154920dd"
}
```

## Status codes

| Status  | Status Code | Description                   |
| ------- | ----------- | ----------------------------- |
| SUCCESS | 0           | Token generated successfully  |
| FAILURE | 101         | Invalid OTP provided          |
| FAILURE | 102         | OTP has expired               |
| FAILURE | 103         | Maximum OTP attempts exceeded |
| FAILURE | Various     | Other validation errors       |

## Token Management

### Token Characteristics

* **Default Validity:** 365 days (1 year)
* **Customizable:** Validity period can be modified per merchant requirements
* **Usage:** Required for all wallet debit operations
* **Security:** Each token is unique and tied to specific user-merchant combination

### Token Storage

* Store the generated token securely on your servers
* Use the token for subsequent wallet operations without requiring OTP
* Implement token refresh mechanisms before expiry