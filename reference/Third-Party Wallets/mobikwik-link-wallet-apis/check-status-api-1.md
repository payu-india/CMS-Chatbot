---
title: Check Status API - Mobikwik
deprecated: false
hidden: true
metadata:
  robots: index
---
This API is used to check the status of a transaction to determine whether it was successful, failed, or is still pending.

## Environments

| Environment    | URL                                          |
| -------------- | -------------------------------------------- |
| **Test**       | `https://test.mobikwik.com/checkstatus`      |
| **Production** | `https://walletapi.mobikwik.com/checkstatus` |

**Method:** `POST`

## Request parameters

| Parameter                            | Description                                                 | Example           |
| ------------------------------------ | ----------------------------------------------------------- | ----------------- |
| mid<br /><code>mandatory</code>      | <code>String</code> Unique parent merchant ID               | `MBK9006`         |
| orderid<br /><code>mandatory</code>  | <code>String</code> Unique order identifier to check status | `ORDER_123456`    |
| checksum<br /><code>mandatory</code> | <code>String</code> Calculated checksum for validation      | `calculated_hash` |

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
        orderid
      </td>

      <td>
        <code>String</code> Order identifier from request
      </td>

      <td>
        `ORDER_123456`
      </td>
    </tr>

    <tr>
      <td>
        txnid
      </td>

      <td>
        <code>String</code> Mobikwik transaction ID
      </td>

      <td>
        `MBK_TXN_789012345`
      </td>
    </tr>

    <tr>
      <td>
        status
      </td>

      <td>
        <code>String</code> Transaction status code
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
        `Transaction completed successfully`
      </td>
    </tr>

    <tr>
      <td>
        amount
      </td>

      <td>
        <code>String</code> Transaction amount
      </td>

      <td>
        `250.00`
      </td>
    </tr>

    <tr>
      <td>
        txndate
      </td>

      <td>
        <code>String</code> Transaction date and time
      </td>

      <td>
        `2025-01-17 10:30:00`
      </td>
    </tr>

    <tr>
      <td>
        merchantname
      </td>

      <td>
        <code>String</code> Merchant name
      </td>

      <td>
        `TestMerchant`
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
        8ea0ec5bf5921c3f1fc
        3398944421978794b9
        ada1c2c47`
      </td>
    </tr>
  </tbody>
</Table>

### Response Attributes

The response checksum that will be returned to the users will have the following format:

<Callout icon="📘" theme="info">
  **Note:**

  Always validate the response checksum to ensure data integrity and security.
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
  "orderid": "ORDER_123456",
  "txnid": "MBK_TXN_789012345",
  "status": "0",
  "statusdescription": "Transaction completed successfully",
  "amount": "250.00",
  "txndate": "2025-01-17 10:30:00",
  "merchantname": "TestMerchant",
  "checksum": "8feac7700a4efd1ef08ea0ec5bf5921c3f1fc3398944421978794b9ada1c2c47"
}
```

## Status codes

| Status Code | Status     | Description                          |
| ----------- | ---------- | ------------------------------------ |
| **0**       | SUCCESS    | Transaction completed successfully   |
| **1**       | FAILURE    | Transaction failed                   |
| **2**       | PENDING    | Transaction is still being processed |
| **3**       | NOT\_FOUND | Transaction not found in system      |