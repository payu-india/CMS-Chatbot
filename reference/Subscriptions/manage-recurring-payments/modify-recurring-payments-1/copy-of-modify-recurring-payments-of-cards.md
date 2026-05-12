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
        **status**
      </td>

      <td>
        `string` The status of the transaction and must be used to map the order status. Possible values:

        * `success`: Indicates the transaction is successful.
        * `failed/pending`: If the value is `failure` or `pending`, should be treated as a failed transaction.
      </td>
    </tr>

    <tr>
      <td>
        **unmappedstatus**
      </td>

      <td>
        `string` The status of a transaction in PayU's internal database, which can include intermediate states. Possible values:

        * `dropped`
        * `bounced`
        * `captured`
        * `auth`
        * `failed`
        * `usercancelled`
        * `pending`

        Refer to the <Anchor label="Payment State Explanations" target="_blank" href="https://docs.payu.in/reference/payment-state-explanations">Payment State Explanations</Anchor>.
      </td>
    </tr>

    <tr>
      <td>
        **key**
      </td>

      <td>
        `string` The merchant key.
      </td>
    </tr>

    <tr>
      <td>
        **error**
      </td>

      <td>
        `string` The error reason in case of the failure transaction.
      </td>
    </tr>

    <tr>
      <td>
        **error_message**
      </td>

      <td>
        `string` The error message in case of the failure transaction.
      </td>
    </tr>

    <tr>
      <td>
        **bank_ref_num**
      </td>

      <td>
        `string` The bank reference number generated by the bank for successful transactions.
      </td>
    </tr>

    <tr>
      <td>
        **txnid**
      </td>

      <td>
        `string` The unique transaction ID value posted by the merchant during the transaction request.
      </td>
    </tr>

    <tr>
      <td>
        **amount**
      </td>

      <td>
        `float`The transaction amount sent in the request in INR.
      </td>
    </tr>

    <tr>
      <td>
        **cardCategory**
      </td>

      <td>
        `string` The card category to indicate whether it is domestic or international.
      </td>
    </tr>

    <tr>
      <td>
        **discount**
      </td>

      <td>
        `float` The discount amount.
      </td>
    </tr>

    <tr>
      <td>
        **net_amount_debit**
      </td>

      <td>
        `float` The net amount debited.
      </td>
    </tr>

    <tr>
      <td>
        **addedon**
      </td>

      <td>
        `datetime` The date and time of the transaction.
      </td>
    </tr>

    <tr>
      <td>
        **productinfo**
      </td>

      <td>
        `string` The product information sent in the request.
      </td>
    </tr>

    <tr>
      <td>
        **firstname**
      </td>

      <td>
        `string` The first name of the customer.
      </td>
    </tr>

    <tr>
      <td>
        **lastname**
      </td>

      <td>
        `string` The last name of the customer.
      </td>
    </tr>

    <tr>
      <td>
        **email**
      </td>

      <td>
        `string` The email address of the customer.
      </td>
    </tr>

    <tr>
      <td>
        **phone**
      </td>

      <td>
        `varchar` The phone number of the customer.
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

    <tr>
      <td>
        **PG_TYPE**
      </td>

      <td>
        `string` Indicates the payment gateway used for the transaction.
      </td>
    </tr>

    <tr>
      <td>
        **udf1-udf10**
      </td>

      <td>
        `string` The user defined field values sent in the request.
      </td>
    </tr>

    <tr>
      <td>
        **success_at**
      </td>

      <td>
        `datetime` The date and time at when the transaction was successful.
      </td>
    </tr>

    <tr>
      <td>
        **cardnum**
      </td>

      <td>
        `integer` The last 4 digits of the card used for the transactions.
      </td>
    </tr>

    <tr>
      <td>
        **issuing_bank**
      </td>

      <td>
        `string` The card issuing bank.
      </td>
    </tr>

    <tr>
      <td>
        **si_consent_action**
      </td>

      <td>
        `string` This parameter will be returned only if a modify subscription request has been received. In other cases, this field will not be returned. Possible values:

        * `modify`
        * `cancel`

        If, in billing details, the action was to modify, then to validate whether the subscription was modified, this fields need to be validated in response. If this field is not sent in response of modify request, then even if transaction is success, then money would have got deducted but the subscription would not have been modified.
      </td>
    </tr>
  </tbody>
</Table>

## For Network Tokens

For `si=3` (Modify or Cancel Mandate), PayU supports two integration flows based on how card details are processed:

* Standard card flow
* Network token flow

Use the standard card flow when processing mandates using regular card details. Use the network token flow when the card has been tokenized and the transaction must be processed using the network token instead of the physical card number.

<Callout icon="📘" theme="info">
  **Handy Tips:**

  This scenario is applicable if you are PCI compliant and got the network token and TAVV from any other aggregator or schemes and then sent the card transaction request in the form of authentication.
</Callout>

### Additional Object to Pass

Please find below the complete request payload with the additional added.

<Accordion title="Sample Request Payload" icon="fa-code">
  ```curl
  curl --location 'https://test.payu.in/_payment' \
    --header 'accept: application/json' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --header 'Cookie: PHPSESSID=jp38t4gvop7ami1ksncksj398v; USERTXNINFO=68ed4df291d9b7.27710642; PHPSESSID=68edd726c95b4' \
    --data-urlencode 'key=BmTY3G' \
    --data-urlencode 'txnid=my_order_47719' \
    --data-urlencode 'amount=1.00' \
    --data-urlencode 'firstname=Gaurav' \
    --data-urlencode 'email=gaurav@example.com' \
    --data-urlencode 'phone=1234567890' \
    --data-urlencode 'productinfo=my_order_47719' \
    --data-urlencode 'api_version=7' \
    --data-urlencode 'si=3' \
    --data-urlencode 'pg=CC' \
    --data-urlencode 'bankcode=UTIBENCC' \
    --data-urlencode 'surl=https://test.payu.in/admin/test_response' \
    --data-urlencode 'furl=https://test.payu.in/admin/test_response' \
    --data-urlencode 'storecard_token_type=1' \
    --data-urlencode 'storecard_token=5200000000000000001' \
    --data-urlencode 'additional_info_for_tokenized_flow={"tavv":"6726","last4digits":"1005","par":"A0009WTYMUG6ANFB3F9Z8CNYAKCX9"}' \
    --data-urlencode 'ccexpmon=05' \
    --data-urlencode 'ccexpyr=2030' \
    --data-urlencode 'ccname=Test User' \
    --data-urlencode 'si_details={"action":"modify","paymentEndDate":"2030-04-13","billingAmount":"400.00","authPayuId":"999990000006391"}' \
    --data-urlencode 'hash=YOUR_HASH_VALUE'
  ```
</Accordion>

### Additional Parameters

| **Parameter**                                               | **Description**                                                                                                                                                                           |
| :---------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **store_card_token**<sup style={{color: 'red'}}>*</sup>     | `string` The Network token generated by you.                                                                                                                                              |
| **storecard_token_type**<sup style={{color: 'red'}}>*</sup> | `integer` Indicates the store card token type. For this scenario, you must include `1`.                                                                                                   |
| **additional_info**<sup style={{color: 'red'}}>*</sup>      | `json` This parameter will contain the additional information in the following JSON format: `{"last4Digits": "1234", "tavv": "ABCDEFGH","trid":"1234567890", "tokenRefNo":"abcde123456"}` |

#### `additional_info` Object Parameters

| **Parameter**                                     | **Description**                                                                                                                                           |
| :------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **trid**<sup style={{color: 'red'}}>*</sup>       | `string` (Token Requestor ID) is the identity given by the networks for creating the tokens. You should be able to get the same from your token provider. |
| **tokenRefNo**<sup style={{color: 'red'}}>*</sup> | `string` (Token Reference Number) is generated along with the network token. . You should be able to get the same from your token provider.               |
| **TAVV** <sup style={{color: 'red'}}>*</sup>      | `string` A token authentication verification value given by schemes or interchange. Also, known as cryptogram.                                            |

<Callout icon="📘" theme="info">
  **Notes:**

  * The last 4 digits of cards is mandatory for all transactions.
  * Some payment gateways require the Token Requester ID (trid) and Token Reference Number (tokenRefNo) to be passed for processing the transaction. Not passing these values will restrict the number of payment gateways available for processing the transaction.
  * Token Requester ID (trid) and Token Reference Number (tokenRefNo) are mandatory for Diners token transactions.
</Callout>

<br />
