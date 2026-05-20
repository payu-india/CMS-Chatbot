---
title: Cancel Recurring Payments of NetBanking and UPI
excerpt: >-
  Cancel recurring payment mandates created using NetBanking and UPI with PayU
  APIs. Learn the card mandate cancellation flow, request parameters, response
  handling, and recurring payment management.
deprecated: false
hidden: true
metadata:
  robots: noindex
---
Use this API to cancel mandates registered using NetBanking and UPI as payment methods. You cannot restore a cancelled mandate. You should ask customers to register a new mandate.

> ❗️
>
> **Watch Out!**
>
> Your customers cannot use Recurring Payments without implementing the **Cancel Recurring Registration** API.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /merchant/postservice.php?form=2
  </Card>
</Cards>

## Environment

| **Environment**            | **URL**                                                |
| :------------------------- | :----------------------------------------------------- |
| **Test Environment**       | `https://test.payu.in/merchant/postservice.php?form=2` |
| **Production Environment** | `https://info.payu.in/merchant/postservice.php?form=2` |

## Sample Request

<Accordion title="Request Payload" icon="fa-code">
  ```curl
  curl --location 'https://info.payu.in/merchant/postservice.php' \
    --header 'Cookie: PHPSESSID=jp38t4gvop7ami1ksncksj398v; USERTXNINFO=68ed4df291d9b7.27710642' \
    --form 'form="2"' \
    --form 'key="BmTY3G"' \
    --form 'command="mandate_revoke"' \
    --form 'var1={"authpayuid":"19504273314","requestId":"test000212"}' \
    --form 'hash="YOUR_HASH_VALUE"' \
  ```
</Accordion>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```json Success Response - NetBanking
  {
  "action":"MANDATE_REVOKE",
  "status":1,
  "Message":"Mandate Cancel Initiated",
  "authpayuid":26734617195
  }
  ```
  ```json Success Response - UPI
  {
  "status":1,
  "action":"MANDATE_REVOKE",
  "message":"Mandate Revoke request processed successfully"
  }
  ```
  ```json Error Response
  {
  "status":0,
  "action":"MANDATE_REVOKE",
  "message":"Mandate is not active"
  }
  ```
</Accordion>

## Request Parameters

<sup style={{color: 'red'}}>*</sup>: Manadatory Parameters

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
        **key**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `varchar` The unique Merchant Key provided by PayU for your merchant account.
      </td>
    </tr>

    <tr>
      <td>
        **command**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `varchar` Determines the API command. Possible values:

        - **For NetBanking:** `mandate_revoke`
        - **For UPI:** `upi_mandate_revoke`
      </td>
    </tr>

    <tr>
      <td>
        **var1**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `json` The variable details. Parameters are described in the var1 JSON Parameters section.
      </td>
    </tr>

    <tr>
      <td>
        **hash**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `string` The calculated hash value using the following logic.<br />`hash = sha512(key|command|var1|SALT)`
      </td>
    </tr>
  </tbody>
</Table>

### var1 JSON Parameters

<Accordion title="Parameters and Description" icon="fa-info-circle">
  | **Parameter**                                      | **Description**                                                                                                                                                                                                                                                                                                                                                                                                               |
  | :------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | **authPayuId**<sup style={{color: 'red'}}>\*</sup> | `string` You should pass the `mihpayid` returned in the payment response of the <Anchor label="recurring payment registration" target="_blank" href="https://docs.payu.in/reference/upi-recurring-payment-consent-transaction">recurring payment registration</Anchor> transaction. The merchant needs to map this value against the customer profile at their end so that the correct `authPayuid` is passed in the request. |
  | **requestId**<sup style={{color: 'red'}}>\*</sup>  | `string` This parameter must contain the unique request value generated at merchant’s end to distinguish independent request call.                                                                                                                                                                                                                                                                                            |
</Accordion>

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
        **action**
      </td>

      <td>
        `varchar` Determines the API action. Here, it is `MANDATE_REVOKE`.
      </td>
    </tr>

    <tr>
      <td>
        **status**
      </td>

      <td>
        `integer` The status of the action performed. Possible values:

        - `1`: Card mandate is successfully canceled.
        - `0`: Card mandate is not canceled.
      </td>
    </tr>

    <tr>
      <td>
        **Message**
      </td>

      <td>
        `string` The description of the mandate cancellation process.
      </td>
    </tr>

    <tr>
      <td>
        **authpayuid**
      </td>

      <td>
        `string`  The auth PayU ID. This parameter is returned only while cancelling the NetBanking mandate.
      </td>
    </tr>
  </tbody>
</Table>

<br />
