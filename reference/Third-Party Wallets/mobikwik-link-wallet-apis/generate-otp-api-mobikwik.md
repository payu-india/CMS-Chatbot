---
title: Generate OTP API - Mobikwik
deprecated: false
hidden: false
metadata:
  robots: index
---
This API generates an OTP for linking Mobikwik wallet account during checkout, enabling seamless wallet payments.

## Environment

| Environment    | URL                                          |
| -------------- | -------------------------------------------- |
| **Test**       | `https://test.mobikwik.com/otpgenerate`      |
| **Production** | `https://walletapi.mobikwik.com/otpgenerate` |

HTTP Method: **POST**

## Request parameters

| Parameter                                       | Description                                                                    | Example           |
| ----------------------------------------------- | ------------------------------------------------------------------------------ | ----------------- |
| mid<br /><code>mandatory</code>                 | <code>String</code> Unique parent merchant ID                                  | `MBK9006`         |
| cell<br /><code>mandatory</code>                | <code>String</code> Mobile number of the user                                  | `9311032820`      |
| msgcode<br /><code>mandatory</code>             | <code>String</code> Message code to be sent                                    | `504`             |
| merchantname<br /><code>optional</code>         | <code>String</code> Alias for the merchant                                     | `TestMerchant`    |
| amount<br /><code>mandatory</code>              | <code>Integer</code> Maximum cap amount (not transaction amount)               | `200`             |
| tokentype<br /><code>mandatory</code>           | <code>Integer</code> Token type (1 for token generation)                       | `1`               |
| checksum<br /><code>mandatory</code>            | <code>String</code> Calculated checksum for validation                         | `calculated_hash` |
| aggregatedMerchantId<br /><code>optional</code> | <code>String</code> Unique ID for aggregateId merchants (For Aggregators Only) | `AGG123`          |

<Callout icon="📘" theme="info">
  ###

  **Notes**:

  - The `amount` parameter represents the maximum cap amount, not the actual transaction amount. The debit API will work for amounts less than or equal to this value.
  - The mobile number must be numeric, have 10 digits, and start with 7, 8, or 9
  - Always validate the response checksum for security
  - Use test environment for integration testing before going live
  - The generated OTP is required for the Token Generate API
</Callout>

### Checksum generation

#### For aggregators

**Format:** `'amount''cell''merchantname''mid''msgcode''tokentype''aggregatedMerchantId'`

#### For direct merchants

**Format:** `'amount''cell''merchantname''mid''msgcode''tokentype'`

**Algorithm:** HMAC SHA256<br />**Secret Key:** Provided by Mobikwik during merchant onboarding

<Callout icon="📘" theme="info">
  ###

  **Note**:

  For merchant `MBK9006`, the secret key is `ju6tygh7u7tdg554k098ujd5468o`. Each merchant will receive their unique secret key.
</Callout>

## Sample request

```bash
POST https://test.mobikwik.com/otpgenerate
Content-Type: application/x-www-form-urlencoded

mid=MBK9006&checksum=0750ff30340013701841399ce85179e90fb186d747d828dbe1d9360d394b9cbc&cell=9311032820&msgcode=504&tokentype=1&amount=200&merchantname=TestMerchant
```

**URL Format:**

```
https://test.mobikwik.com/otpgenerate?mid=MBK9006&checksum=0750ff30340013701841399ce85179e90fb186d747d828dbe1d9360d394b9cbc&cell=9311032820&msgcode=504&tokentype=1&amount=200&merchantname=TestMerchant
```

## Response parameters

<Table align={["left","left","left"]}>
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
        `Message Sent to xxxxxx820`
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
                                                8ea0ec5bf5921c3f1fc3  
                                                398944421978794b  
                                                9ada1c2c47`
      </td>
    </tr>
  </tbody>
</Table>

### Response attributes

The response checksum that will be returned to the users will have the following format:

<Callout icon="📘" theme="info">
  ###

  **Note:**

  Always validate the response checksum to ensure data integrity and security.
</Callout>

<HTMLBlock>{`
<table>
    <tbody>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:98.0px;">
                <strong>Status &amp; Status Code</strong>
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:61.0px;">
                <strong>Status Code</strong>
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:278.0px;">
                <strong>Status description</strong>
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:98.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:61.0px;">
                20
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:278.0px;">
                User Blocked
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:98.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:61.0px;">
                21
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:278.0px;">
                Merchant Blocked
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:98.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:61.0px;">
                23
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:278.0px;">
                Merchant not registered on MobiKwik
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:98.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:61.0px;">
                33
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:278.0px;">
                User does not have sufficient balance in his wallet
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:98.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:61.0px;">
                51
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:278.0px;">
                Length of parameter orderid must be between 8 to 30 characters
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:98.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:61.0px;">
                55
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:278.0px;">
                Parameter cell is invalid. It must be numeric, have 10 digits and start with 7, 8 or 9
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:98.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:61.0px;">
                120
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:278.0px;">
                User does not exist
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:98.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:61.0px;">
                422
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:29.0px;padding:4.0px;width:278.0px;">
                User not allowed to do Transaction. Contact your KAM or raise a support ticket on help.payu.in
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:98.0px;">
                SUCCESS
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:61.0px;">
                0
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:278.0px;">
                Message Sent to xxxxxx208
            </td>
        </tr>
    </tbody>
</table>
`}</HTMLBlock>

## Sample response

### Success response

```json
{
  "messagecode": "504",
  "status": "SUCCESS",
  "statuscode": "0",
  "statusdescription": "Message Sent to xxxxxx820",
  "checksum": "8feac7700a4efd1ef08ea0ec5bf5921c3f1fc3398944421978794b9ada1c2c47"
}
```

### Failure response

```json
{
  "messagecode": "504",
  "status": "FAILURE",
  "statuscode": "55",
  "statusdescription": "Parameter cell is invalid. It must be numeric, have 10 digits and start with 7,8 or 9",
  "checksum": "f25ac916fe4806591e16269fc912771456437b784fa144a77fa9842d154920cc"
}
```

<br />
