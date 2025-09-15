---
title: Token Expire API - Mobikwik
deprecated: false
hidden: false
metadata:
  robots: index
---
This API is used to explicitly expire a wallet token, providing merchants with control over token lifecycle management and enhanced security.

## Environment

| Environment    | URL                                                     |
| -------------- | ------------------------------------------------------- |
| **Test**       | `https://test.mobikwik.com/walletapis/tokenexpire`      |
| **Production** | `https://walletapi.mobikwik.com/walletapis/tokenexpire` |

**Method:** `POST`

**Content-Type:** `application/json`

## Request parameters

| Parameter                                       | Description                                                                   | Example               |
| ----------------------------------------------- | ----------------------------------------------------------------------------- | --------------------- |
| expiryReason<br /><code>mandatory</code>        | <code>String</code> Reason for token expiry                                   | `User logout`         |
| token<br /><code>mandatory</code>               | <code>String</code> Token to be expired                                       | `MBK_TOKEN_123456789` |
| mid<br /><code>mandatory</code>                 | <code>String</code> Unique parent merchant ID                                 | `MBK9006`             |
| cellNo<br /><code>mandatory</code>              | <code>String</code> Mobile number of the user                                 | `9311032820`          |
| merchantname<br /><code>mandatory</code>        | <code>String</code> Alias for the merchant                                    | `TestMerchant`        |
| aggregatedMerchantId<br /><code>optional</code> | <code>String</code> Unique ID for aggregated merchants (For Aggregators Only) | `AGG123`              |
| checksum<br /><code>mandatory</code>            | <code>String</code> Calculated checksum for validation                        | `calculated_hash`     |

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
        `Token expired successfully`
      </td>
    </tr>

    <tr>
      <td>
        token
      </td>

      <td>
        <code>String</code> Token that was expired
      </td>

      <td>
        `MBK_TOKEN_123456789`
      </td>
    </tr>

    <tr>
      <td>
        expiryReason
      </td>

      <td>
        <code>String</code> Reason for expiry
      </td>

      <td>
        `User logout`
      </td>
    </tr>

    <tr>
      <td>
        expiredAt
      </td>

      <td>
        <code>String</code> Timestamp when token was expired
      </td>

      <td>
        `2025-01-17T10:30:00Z`
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
        `8feac7700a4efd1ef08ea  
        0ec5bf5921c3f1fc339894
        4421978794b9ada1c2c47`
      </td>
    </tr>
  </tbody>
</Table>

### Response Attributes

The response checksum that will be returned to the users will have the following format:

<Callout icon="📘" theme="info">
  **Note:** Always validate the response checksum to ensure data integrity and security.
</Callout>

<HTMLBlock>{`
<table>
    <tbody>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:144.0px;">
                <strong>Status &amp; Status Code</strong>
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:87.0px;">
                <strong>Status Code</strong>
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:205.0px;">
                <strong>Status description</strong>
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:144.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:87.0px;">
                1
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:205.0px;">
                Failed
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:144.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:87.0px;">
                17
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:205.0px;">
                Merchant cancelled transaction
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:144.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:87.0px;">
                16
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:205.0px;">
                User cancelled transaction
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:144.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:87.0px;">
                20
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:205.0px;">
                Transaction expired
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:144.0px;">
                FAILURE
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:87.0px;">
                2
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:205.0px;">
                Pending
            </td>
        </tr>
        <tr>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:144.0px;">
                SUCCESS
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:87.0px;">
                0
            </td>
            <td style="border-color:#000000;border-width:1.0px;height:14.0px;padding:4.0px;width:205.0px;">
                Success / Refund / Partial Refund
            </td>
        </tr>
    </tbody>
</table>
`}</HTMLBlock>

<br />

## Sample response

```json
{
  "status": "SUCCESS",
  "statuscode": "0",
  "statusdescription": "Token expired successfully",
  "token": "MBK_TOKEN_123456789",
  "expiryReason": "User logout",
  "expiredAt": "2025-01-17T10:30:00Z",
  "checksum": "8feac7700a4efd1ef08ea0ec5bf5921c3f1fc3398944421978794b9ada1c2c47"
}
```