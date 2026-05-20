---
title: Modify Recurring Payments of UPI
excerpt: >-
  Modify card recurring payments and mandates of UPI using PayU APIs. Update
  billing rules, subscription settings, mandate details, and recurring payment
  configurations securely for UPI-based transactions.
deprecated: false
hidden: true
metadata:
  robots: noindex
---
Use this API to modify mandates created using UPI as a payment method.

> ❗️ **Watch Out!**
>
> You can use this API to modify only UPI Collect registration transactions and not for mandates created using the UPI Intent mode.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /merchant/postservice.php
  </Card>
</Cards>

<PaymentAPIEnvironment />

## Sample Request

<Accordion title="Request Payload" icon="fa-code">
  ```curl
  curl --location 'https://info.payu.in/merchant/postservice.php' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'Authorization: Bearer YOUR_BEARER_TOKEN' \
  --header 'Cookie: YOUR_COOKIE_HEADER_VALUE' \
  --data-urlencode 'form=2' \
  --data-urlencode 'key=YOUR_MERCHANT_KEY' \
  --data-urlencode 'command=upi_mandate_modify' \
  --data-urlencode 'hash=YOUR_HASH_VALUE' \
  --data-urlencode 'var1={"requestId":"YOUR_REQUEST_ID","authPayuId":"YOUR_AUTH_PAYU_ID","endDate":"2025-11-15","amount":1}'
  ```
</Accordion>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```json Success Response
  {
      "status": 1,
      "action": "MANDATE_UPDATE",
      "message": "Mandate modify request processed successfully"
  }
  ```
  ```json Error Response
  {
  "status":0,
  "action": " MANDATE_UPDATE ",
  "message": "authPayuId is mandatory "
  }
  ```
</Accordion>

## Request Parameters

> 📘 **Mandatory Parameters**
>
> <RequiredStar legend />

| **Parameter**                    | **Description**                                                                                                                                                                                                          |
| :------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <RequiredStar param="key" />     | `varchar` The unique Merchant Key provided by PayU for your merchant account.                                                                                                                                            |
| <RequiredStar param="command" /> | `varchar` Determines the API command. Here, it is `upi_mandate_modify`.                                                                                                                                                  |
| <RequiredStar param="hash" />    | `string` The calculated hash value using the following logic. `hash = sha512(key\|command\|var1\|SALT)`. You can use the **Generate Hash** button to generate a hash by providing the parameter values as per the logic. |
| `var1`                           | `json` The variable details. Parameters are described in the [var1 JSON Parameters](https://docs.payu.in/reference/modify-recurring-payments-of-upi#var1-json-parameters) section.                                       |

### var1 JSON Parameters

| **Parameter**                       | **Description**                                                                                                                                                                                                                                                                                                                                                                        |
| :---------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <RequiredStar param="authPayuId" /> | `string` You should pass the `mihpayid` returned in the payment response of the <Anchor target="_blank" href="https://docs.payu.in/reference/upi-recurring-payment-consent-transaction">recurring payment registration</Anchor> transaction. The merchant needs to map this value against the customer profile at their end so that the correct `authPayuid` is passed in the request. |
| `amount`                            | `float` The new amount that has been modified.                                                                                                                                                                                                                                                                                                                                         |
| `endDate`                           | `datetime` The end date of the mandate.                                                                                                                                                                                                                                                                                                                                                |
| <RequiredStar param="requestId" />  | `string` This parameter must contain the unique request value generated at merchant’s end to distinguish independent request call.                                                                                                                                                                                                                                                     |

## Response Parameters

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `status`
      </td>

      <td>
        `string` The status of the transaction. Possible values:

        - `active`: The mandate is active.
        - `revoked`: The mandate is revoked/cancelled.
        - `pause`: The mandate is paused.
        - `unpause`: The mandate is unpaused.
      </td>
    </tr>

    <tr>
      <td>
        `authpayuid`
      </td>

      <td>
        `string` The consent transaction ID.
      </td>
    </tr>

    <tr>
      <td>
        `action`
      </td>

      <td>
        `string` The action performed. Possible values:

        - `MANDATE_UPDATE`
        - `MANDATE_PRE_DEBIT`
        - `MANDATE_REVOKE`
        - `MANDATE_STATUS`
      </td>
    </tr>

    <tr>
      <td>
        `dateTime`
      </td>

      <td>
        `datetime` The start date of the mandate.
      </td>
    </tr>

    <tr>
      <td>
        `amount`
      </td>

      <td>
        `string` The amount of the transaction.
      </td>
    </tr>

    <tr>
      <td>
        `endDate`
      </td>

      <td>
        `datetime` The end date of the mandate.
      </td>
    </tr>

    <tr>
      <td>
        `mandateNumber`
      </td>

      <td>
        `string` The unique mandate number (UMN).
      </td>
    </tr>

    <tr>
      <td>
        `hash`
      </td>

      <td>
        `string` The hash value generated and sent in the request.
      </td>
    </tr>
  </tbody>
</Table>

### Update Pending

It will be an async call to customer for approving the mandate modification in their PSP app by entering their MPIN. After the UPI mandate is modified, you can check the UPI mandate status, or can consume the UPI mandate modification webhooks from PayU end. Poll the <Anchor target="_blank" href="https://docs.payu.in/reference/check-the-mandate-status">Check the Mandate Status</Anchor> API to get the mandate status. Below is the response you get in the case of pending update.

<Accordion title="Update Pending Response Payload" icon="fa-code">
  ```json Sample Response
  {
      "status": 1,
      "action": "MANDATE_UPDATE",
      "message": "Mandate update pending at PG. Please wait for webhook or use upi_mandate_status service to confirm updated status"
  }
  ```
</Accordion>

## Errors

Below are the failure scenarios associated with UPI.

<Accordion title="Invalid Data" icon="fa-exclamation-triangle">
  ```json Error Response
  {
    "status":0,
    "action":" MANDATE_UPDATE ",
    "message":"Invalid Data "
  }
  ```

  **Reason:** This error occurs when you pass invalid data.

  **Recommended Fix:** Make sure you pass valid data in the request.
</Accordion>

<Accordion title="authPayuId is Missing" icon="fa-user-times">
  ```json Error Response
  {
    "status":0,
    "action":" MANDATE_UPDATE ",
    "message":"authPayuId is mandatory "
  }
  ```

  **Reason:** This error occurs when you do not pass the `authPayuId` value.

  **Recommended Fix:** Make sure to pass the `authPayuId` value.
</Accordion>

<Accordion title="requestId is Missing" icon="fa-id-badge">
  ```json Error Response
  {
    "status":0,
    "action":" MANDATE_UPDATE ",
    "message":"requestId is mandatory"
  }
  ```

  **Reason:** This error occurs when you miss to pass the `requestId` parameter value.

  **Recommended Fix:** Make sure to pass the `requestId` parameter value.
</Accordion>

<Accordion title="Amount or endDate Needs to be Updated" icon="fa-refresh">

```json Error Response
{
  "status":0,
  "action":" MANDATE_UPDATE ",
  "message":"amount or endDate required to update"
}
```

**Reason:** This error occurs when you do not pass amount or endDate parameters to update.

**Recommended Fix:** Make sure to pass the either of the parameters to modify.

</Accordion>

<br />
