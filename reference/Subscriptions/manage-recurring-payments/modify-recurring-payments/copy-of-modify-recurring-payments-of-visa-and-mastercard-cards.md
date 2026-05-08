---
title: Modify Recurring Payments of AMEX and RuPay Cards
excerpt: >-
  Modify card recurring payments and mandates of AMEX and RuPay using PayU APIs.
  Update billing rules, subscription settings, mandate details, and recurring
  payment configurations securely for card-based transactions.
deprecated: false
hidden: true
metadata:
  robots: noindex
---
Use this endpoint to modify card recurring payments and mandates of Visa and Mastercard.

<Callout icon="❗️" theme="error">
  **RBI Guidelines:**

  While modifying the recurring payment, taking consent from the customer and doing an additional factor of authentication is mandatory. You must ensure this is done before using this API. You need to pass `authPayuId` and `action` parameters to modify the billing details as a part of JSON using this API.
</Callout>

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /\_payment
  </Card>
</Cards>

<PaymentAPIEnvironment />

## Sample Request

<Accordion title="Request Payload" icon="fa-code">
  ```curl
curl --location 'https://secure.payu.in/_payment' \
--header 'accept: application/json' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: PHPSESSID=jp38t4gvop7ami1ksncksj398v; USERTXNINFO=68ed4df291d9b7.27710642; PHPSESSID=68edd726c95b4' \
--data-urlencode 'key=BmTY3G' \
--data-urlencode 'txnid=my_order_47719' \
--data-urlencode 'amount=1.00' \
--data-urlencode 'firstname=Payu-Admin' \
--data-urlencode 'email=test@example.com' \
--data-urlencode 'phone=1234567890' \
--data-urlencode 'productinfo=my_order_47719' \
--data-urlencode 'api_version=7' \
--data-urlencode 'si=3' \
--data-urlencode 'pg=CC' \ -- CC/DC
--data-urlencode 'bankcode=CC' \ -- RUPAYCC/RUPAY
--data-urlencode 'surl=https://admin.payu.in/test_response' \
--data-urlencode 'furl=https://admin.payu.in/test_response' \
--data-urlencode 'ccnum=5123456789012346' \
--data-urlencode 'ccexpmon=05' \
--data-urlencode 'ccexpyr=2030' \
--data-urlencode 'ccvv=123' \
--data-urlencode 'ccname=Test User' \
--data-urlencode 'si_details={"action":"modify","paymentEndDate":"2030-04-13","billingAmount":"400.00","authPayuId":"999990000006391"}' \
--data-urlencode 'hash={{hash_value}}'
  ```
</Accordion>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```php
  Array
  (
      [mihpayid]         => 25603951365
      [mode]             => CC
      [status]           => success
      [unmappedstatus]   => captured
      [key]              => BmTY3G
      [txnid]            => 5527fc7d02f2bfc00eb4
      [amount]           => 1.00
      [cardCategory]     => signature_premium
      [discount]         => 0.00
      [net_amount_debit] => 1
      [addedon]          => 2025-10-14 15:44:41
      [productinfo]      => Product Info
      [firstname]        => Payu-Admin
      [lastname]         => 
      [address1]         => 
      [address2]         => 
      [city]             => 
      [state]            => 
      [country]          => 
      [zipcode]          => 
      [email]            => test@example.com
      [phone]            => 1234567890
      [udf1]             => 
      [udf2]             => 
      [udf3]             => 
      [udf4]             => 
      [udf5]             => 
      [udf6]             => 
      [udf7]             => 
      [udf8]             => 
      [udf9]             => 
      [udf10]            => 
      [hash]             => YOUR_HASH_VALUE
      [field1]           => CBC10141015051509EGR573
      [field2]           => 185869
      [field3]           => 
      [field4]           => 
      [field5]           => 
      [field6]           => 05
      [field7]           => AUTHPOSITIVE
      [field8]           => 0 | Transaction Completed
      [field9]           => Transaction Completed
      [payment_source]   => payu
      [meCode]           => {
                                  "wibmo_merchant_id":"16329672",
                                  "hash_key":"YOUR_HASH_VALUE",
                                  "acquirer_merchant_id":"175645866049780",
                                  "mcc":"5499"
                              }
      [PG_TYPE]          => CC-PG
      [bank_ref_num]     => 528710004895
      [bankcode]         => CC
      [error]            => E000
      [error_Message]    => No Error
      [cardnum]          => XXXXXXXXXXXX4879
  )
  ```
</Accordion>

## Request Parameters

<Callout icon="📘" theme="info">
  **Mandatory Parameters**

  Parameters marked with <sup style={{color: 'red'}}>*</sup> are mandatory.
</Callout>

| Parameter | Description |
|---|---|
| `mihpayid` | It is a unique reference number created for each transaction at PayU's end which is used to identify a transaction in case of a refund. |
| `mode` | This parameter describes the payment category by which the transaction was completed/attempted by the customer. Possible values:<br/><br/>- `CC`: Credit Card<br/>- `DC`: Debit Card |
| `bankcode` | Indicates the payment option used for the transaction. Possible values:<br/><br/>- `AMEX`: American Express credit and debit cards<br/>- `RUPAYCC`: RuPay credit cards<br/>- `RUPAY`: RuPay debit cards |
| `status` | This parameter returns the status of the transaction and must be used to map the order status. Possible values are `success`, `failure`, or `pending`.<br/><br/>- **Success**: Transaction is successful.<br/>- **Failed**: If status is `failure` or `pending`, it must be treated as a failed transaction. |
| `unmappedstatus` | This parameter holds the status of a transaction in PayU's internal database, which can include intermediate states. Possible values include `dropped`, `bounced`, `captured`, `auth`, `failed`, `usercancelled`, or `pending`.<br/><br/>Refer to [Payment State Explanations](http://docs.payu.in/reference/payment-state-explanations). |
| `key` | This parameter contains the merchant key. |
| `error` | For failed transactions, this parameter provides the reason for failure. |
| `error_message` | This parameter contains the error message. Refer to [Error Codes](http://docs.payu.in/reference/error-codes). |
| `bank_ref_num` | For each successful transaction, this parameter contains the bank reference number generated by the bank. |
| `txnid` | This parameter contains the transaction ID value posted by the merchant during the transaction request. |
| `amount` | This parameter contains the original amount sent in the transaction request by the merchant. |
| `cardCategory` | Indicates whether the card is domestic or international. |
| `discount` | This parameter contains the discount amount applied by the merchant. |
| `net_amount_debit` | This parameter contains the net amount debited. |
| `addedon` | The transaction date and time. |
| `productinfo` | Contains the same `productinfo` value sent in the transaction request from the merchant's end to PayU. |
| `firstname` | Contains the same `firstname` value sent in the transaction request from the merchant's end to PayU. |
| `lastname` | Contains the same `lastname` value sent in the transaction request from the merchant's end to PayU. |
| `email` | Contains the same `email` value sent in the transaction request from the merchant's end to PayU. |
| `phone` | Contains the same `phone` value sent in the transaction request from the merchant's end to PayU. |
| `hash` | This parameter is crucial and is similar to the hash parameter used in the transaction request. Refer to [Generate Hash](http://docs.payu.in/docs/generate-hash-merchant-hosted). |
| `PG_TYPE` | Provides information on the payment gateway used for the transaction. |
| `udf1` | Contains the same value of `udf1` sent in the transaction request from the merchant's end to PayU. |
| `udf2` | Contains the same value of `udf2` sent in the transaction request from the merchant's end to PayU. |
| `udf3` | Contains the same value of `udf3` sent in the transaction request from the merchant's end to PayU. |
| `udf4` | Contains the same value of `udf4` sent in the transaction request from the merchant's end to PayU. |
| `udf5` | Contains the same value of `udf5` sent in the transaction request from the merchant's end to PayU. |
| `udf6` | Contains the same value of `udf6` sent in the transaction request from the merchant's end to PayU. |
| `udf7` | Contains the same value of `udf7` sent in the transaction request from the merchant's end to PayU. |
| `udf8` | Contains the same value of `udf8` sent in the transaction request from the merchant's end to PayU. |
| `udf9` | Contains the same value of `udf9` sent in the transaction request from the merchant's end to PayU. |
| `success_at` | Contains the date and timestamp when the transaction became successful. |
| `cardnum` | Contains the masked card number with only the last 4 digits visible. |
| `issuing_bank` | Contains the card issuing bank. |
| `si_consent_action` | Returned only if a modify subscription request has been received. Possible values:<br/><br/>- `modify`<br/>- `cancel`<br/><br/>If the billing action was `modify`, validate this field in the response to confirm the subscription was modified successfully. If this field is missing, the transaction may succeed and funds may be deducted, but the subscription might not actually be modified. |

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

### si_details JSON Parameters

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
        **action**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `string` This field is used to modify or cancel an existing subscription. Pass `modify` as a value to modify a subscription.
      </td>
    </tr>

    <tr>
      <td>
        **paymentEndDate**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `date` The end date of the billing plan in the YYYY-MM-DD format.

        **Note**: Make sure to pass the correct end date. Depending on the start and end date, number of payment iterations are internally calculated and same is passed to acquirers or banks.
      </td>
    </tr>

    <tr>
      <td>
        **billingAmount**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `number` The billing amount is passed in the XX format. In use cases where **billingCycle = ADHOC**, amount passed is treated as maximum amount since the billing amount and billing cycle varies as per the usage of the subscription service.  In this case, the merchant is free to charge any amount for customer up to the amount specified in the defined subscription call.
      </td>
    </tr>

    <tr>
      <td>
        **authpayuid**<sup style={{color: 'red'}}>*</sup>`mandatory for modifying subscription with cards`
      </td>

      <td>
        This field is used only to modify an existing subscription/consent. You can modify the following details:

        * `startDate`
        * `endDate`
        * `billing cycle`
        * `billing interval`
        * `billing amount`
      </td>
    </tr>
  </tbody>
</Table>

## For Network Tokens

If you are a merchant:

* With card token, TAVV(Cryptogram), and the last four digits of the card
* Who can create a token or through another partner

<Callout icon="📘" theme="info">
  **Handy Tips:**

  This scenario is applicable if you are PCI compliant and got the network token and TAVV from any other aggregator or schemes and then sent the card transaction request in the form of authentication.
</Callout>

| **Parameter**                                               | **Description**                                                                                                                                                                           |
| :---------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **store_card_token**<sup style={{color: 'red'}}>*</sup>     | `string` The Network token generated by you.                                                                                                                                              |
| **storecard_token_type**<sup style={{color: 'red'}}>*</sup> | `integer` Indicates the store card token type. For this scenario, you must include `1`.                                                                                                   |
| **additional_info**<sup style={{color: 'red'}}>*</sup>      | `json` This parameter will contain the additional information in the following JSON format: `{"last4Digits": "1234", "tavv": "ABCDEFGH","trid":"1234567890", "tokenRefNo":"abcde123456"}` |

### `additional_info` Object Parameters

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
