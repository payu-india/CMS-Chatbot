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

<Callout icon="📘" theme="info">
  **Mandatory Parameters**

  Parameters marked with <sup style={{color: 'red'}}>*</sup> are mandatory.
</Callout>

| **Parameter**                                  | **Description**                                                                                                                                                                                                          |
| :--------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **key**<sup style={{color: 'red'}}>*</sup>     | `varchar` The unique Merchant Key provided by PayU for your merchant account.                                                                                                                                            |
| **command**<sup style={{color: 'red'}}>*</sup> | `varchar` Determines the API command. Here, it is `upi_mandate_modify`.                                                                                                                                                  |
| **hash**<sup style={{color: 'red'}}>*</sup>    | `string` The calculated hash value using the following logic. `hash = sha512(key\|command\|var1\|SALT)`. You can use the **Generate Hash** button to generate a hash by providing the parameter values as per the logic. |
| **var1**                                       | `json` The variable details. Parameters are described in the var1 JSON Parameters section.                                                                                                                               |

<HTMLBlock>{`
<p>Use this button to generate the hash value.</p>

<style>
                .tooltip-btn {
                    position: relative;
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-weight: bold; /* Added this line */
                }
                .tooltip-btn:hover::after {
                    content: attr(data-tooltip);
                    position: absolute;
                    bottom: 125%;
                    left: 50%;
                    transform: translateX(-50%);
                    background-color: #333;
                    color: white;
                    padding: 5px 10px;
                    border-radius: 4px;
                    white-space: nowrap;
                    font-size: 12px;
                    z-index: 1;
                }
                </style>

                <button onclick="window.open('https://payu-india.github.io/CMS-Chatbot/', '_blank')" 
                        class="tooltip-btn" 
                        data-tooltip="Click to generate hash.">
                    Generate Hash
                </button>
`}</HTMLBlock>

### var1 JSON Parameters

| **Parameter**                                     | **Description**                                                                                                                                                                                                                                                                                                                                                                                                               |
| :------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **authPayuId**<sup style={{color: 'red'}}>*</sup> | `string` You should pass the `mihpayid` returned in the payment response of the <Anchor label="recurring payment registration" target="_blank" href="https://docs.payu.in/reference/upi-recurring-payment-consent-transaction">recurring payment registration</Anchor> transaction. The merchant needs to map this value against the customer profile at their end so that the correct `authPayuid` is passed in the request. |
| **amount**                                        | `float` The new amount that has been modified.                                                                                                                                                                                                                                                                                                                                                                                |
| **endDate**                                       | `datetime` The end date of the mandate.                                                                                                                                                                                                                                                                                                                                                                                       |
| **requestId**<sup style={{color: 'red'}}>*</sup>  | `string` This parameter must contain the unique request value generated at merchant’s end to distinguish independent request call.                                                                                                                                                                                                                                                                                            |

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
        **status**
      </td>

      <td>
        `string` The status of the transaction. Possible values:

        * `active`: The mandate is active.
        * `revoked`: The mandate is revoked/cancelled.
        * `pause`: The mandate is paused.
        * `unpause`: The mandate is unpaused.
      </td>
    </tr>

    <tr>
      <td>
        **authpayuid**
      </td>

      <td>
        `string` The consent transaction ID.
      </td>
    </tr>

    <tr>
      <td>
        **action**
      </td>

      <td>
        `string` The action performed. Possible values:

        * `MANDATE_UPDATE`
        * `MANDATE_PRE_DEBIT`
        * `MANDATE_REVOKE`
        * `MANDATE_STATUS`
      </td>
    </tr>

    <tr>
      <td>
        **dateTime**
      </td>

      <td>
        `datetime` The start date of the mandate.
      </td>
    </tr>

    <tr>
      <td>
        **amount**
      </td>

      <td>
        `string` The amount of the transaction.
      </td>
    </tr>

    <tr>
      <td>
        **endDate**
      </td>

      <td>
        `datetime` The end date of the mandate.
      </td>
    </tr>

    <tr>
      <td>
        **mandateNumber**
      </td>

      <td>
        `string` The unique mandate number (UMN).
      </td>
    </tr>

    <tr>
      <td>
        **hash**
      </td>

      <td>
        `string` The hash value generated and sent in the request.
      </td>
    </tr>
  </tbody>
</Table>

## Errors

Below are the failure scenarios associated with UPI.

<Accordion title="My Accordion Title" icon="fa-info-circle">
  Lorem ipsum dolor sit amet, **consectetur adipiscing elit.** Ut enim
  ad minim veniam, quis nostrud exercitation ullamco. Excepteur sint
  occaecat cupidatat non proident!
</Accordion>

<br />
