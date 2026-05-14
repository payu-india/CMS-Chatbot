---
title: Cancel Recurring Payments of AMEX and RuPay Cards
excerpt: >-
  Learn how to cancel recurring payments for AMEX and RuPay cards using PayU
  APIs. Follow the integration steps, request parameters, and response handling
  for seamless mandate cancellation.
deprecated: false
hidden: true
metadata:
  description: >-
    Learn how to cancel recurring payments for AMEX and RuPay cards using PayU
    APIs. Follow the integration steps, request parameters, and response
    handling for seamless mandate cancellation.
  keywords:
    - cancel recurring payments
    - AMEX recurring payments
    - RuPay recurring payments
    - PayU recurring payment cancellation
    - cancel card mandate
    - recurring mandate API
    - AMEX mandate cancellation
    - RuPay mandate cancellation
    - subscription cancellation API
    - recurring payments API
    - PayU subscriptions
    - card mandate cancellation
    - recurring transaction cancellation
    - PayU API documentation
    - merchant recurring payments
  robots: noindex
---
Use this API to cancel card mandates registered via AMEX and RuPay card networks. You cannot restore a cancelled mandate. You should ask customers to register a new mandate.

<Callout icon="❗️">
  **Watch Out!**

  The 2FA is required for cancelling recurring payment with AMEX and RuPay cards.
</Callout>

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /_payment
  </Card>
</Cards>

## Environment

| **Environment**            | **URL**                           |
| :------------------------- | :-------------------------------- |
| **Test Environment**       | `https://test.payu.in/_payment`   |
| **Production Environment** | `https://secure.payu.in/_payment` |

## Sample Request

<Accordion title="Request Payload" icon="fa-code">
  ```curl
  curl --location 'https://secure.payu.in/_payment' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'Cookie: PHPSESSID=jp38t4gvop7ami1ksncksj398v; USERTXNINFO=68ed4df291d9b7.27710642; PHPSESSID=68edd726c95b4' \
  --data-urlencode 'key=BmTY3G' \
  --data-urlencode 'txnid=my_order_96977' \
  --data-urlencode 'amount=1' \
  --data-urlencode 'firstname=Payu-Admin' \
  --data-urlencode 'email=test@example.com' \
  --data-urlencode 'phone=1234567890' \
  --data-urlencode 'productinfo=my_order_96977' \
  --data-urlencode 'api_version=1' \
  --data-urlencode 'si=3' \
  --data-urlencode 'pg=CC' \        # CC/DC
  --data-urlencode 'bankcode=CC' \ # RUPAYCC/RUPAY
  --data-urlencode 'surl=https://admin.payu.in/test_response' \
  --data-urlencode 'furl=https://admin.payu.in/test_response' \
  --data-urlencode 'ccnum=' \
  --data-urlencode 'ccname=Test User' \
  --data-urlencode 'ccexpmon=05' \
  --data-urlencode 'ccexpyr=2025' \
  --data-urlencode 'ccvv=123' \
  --data-urlencode 'si_details={"action":"delete","authPayuId":25630224100,"siTokenRequestor":2}' \
  --data-urlencode 'hash=YOUR_HASH_VALUE'
  ```
</Accordion>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```json Success Response
  {
    "status":1,
    "message":"Mandate Revoked Successfully",
    "action":"MANDATE_REVOKE"
  }
  ```
  ```json Error Response
  {
    "status":0,
    "message":"Mandate not in appropriate state to perform action",
    "action":"MANDATE_REVOKE"
  }
  ```
</Accordion>

## Request Parameters

<Callout icon="📘" theme="info">
  **Mandatory Parameters**

  Parameters marked with <sup style={{color: 'red'}}>*</sup> are mandatory.
</Callout>

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
        `varchar` Determines the API command. Here, it is `mandate_revoke`.
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
        `string` The calculated hash value using the following logic.  
        `hash = sha512(key|command|var1|SALT)`
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

        * `1`: Card mandate is successfully canceled.
        * `0`: Card mandate is not canceled.
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
  </tbody>
</Table>
