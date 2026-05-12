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
        **txnid**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `varchar` A unique transaction ID (or order ID). It is the order reference number generated at your end. You can use this ID to track a particular order. This ID should be unique and you can duplicate it. The parameter value can be maximum of 25 characters.
      </td>
    </tr>

    <tr>
      <td>
        **amount**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `float` The transaction amount in `INR`.

        **Note**: Type-cast the amount to float type Depending upon the merchant use case, this value will vary.

        * The value should be minimum of `1.00` INR for Cards for penny testing.
        * For first installment, this can be initiate setup amount However, this is supported only for selected NetBanking (ICICI and HDFC), all Credit / Debit Cards, and UPI.
      </td>
    </tr>

    <tr>
      <td>
        **firstname**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `varchar` The first name of the customer. For example, `Gaurav`. The value can contain maximum of 60 characters.
      </td>
    </tr>

    <tr>
      <td>
        **email**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `varchar` The email of the customer. For example, `gaurav@example.com`.  The value can contain maximum of 50 characters.

        **Note:** The email is used in case of fraud detection and chargebacks. Additionally, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.
      </td>
    </tr>

    <tr>
      <td>
        **phone**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `varchar` The customer phone number. For example, `1234567890`.

        **Note:** The email is used in case of fraud detection and chargebacks. Additionally, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.
      </td>
    </tr>

    <tr>
      <td>
        **productinfo**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `string` A product description. The value can contain maximum of 100 characters.
      </td>
    </tr>

    <tr>
      <td>
        **api_version**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `number` The API version. You should always pass this value as `7`.
      </td>
    </tr>

    <tr>
      <td>
        **si**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `number` The standing instruction. You should pass the value as `3` to modify the card mandate.
      </td>
    </tr>

    <tr>
      <td>
        **pg**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `string` This parameter describes the payment category by which the transaction was completed/attempted by the customer. Possible values:

        * `DC`: For debit cards
        * `CC`: For credit cards
      </td>
    </tr>

    <tr>
      <td>
        **bankcode**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `string` This parameter contains the code indicating the payment option used for the transaction. Possible values:

        * `CC`: For Visa and Mastercard credit cards
        * `AMEX`: For American Express credit and debit cards
        * `RUPAYCC`: For RuPay credit cards
        * `VISA`: For Visa debit cards
        * `MAST`: For Mastercard debit cards
        * `RUPAY`: For RuPay debit cards
      </td>
    </tr>

    <tr>
      <td>
        **surl**
      </td>

      <td>
        `string` The success URL customers are redirected to if the transaction is successful.
      </td>
    </tr>

    <tr>
      <td>
        **furl**
      </td>

      <td>
        `string` The failure URL customers are redirected to if the transaction is unsuccessful.
      </td>
    </tr>

    <tr>
      <td>
        **ccnum**
      </td>

      <td>
        `number` The credit card number used to register the mandate.
      </td>
    </tr>

    <tr>
      <td>
        **ccexpmon**
      </td>

      <td>
        `number` The expiry month of the CC.
      </td>
    </tr>

    <tr>
      <td>
        **ccexpyr**
      </td>

      <td>
        `number` The expiry year of the CC.
      </td>
    </tr>

    <tr>
      <td>
        **ccvv**
      </td>

      <td>
        `number` The CVV of the CC.
      </td>
    </tr>

    <tr>
      <td>
        **ccname**
      </td>

      <td>
        `string` The name of the CC owner.
      </td>
    </tr>

    <tr>
      <td>
        **si_details**
      </td>

      <td>
        `json` The SI mandatory details that need to be passed during registration transaction from your system to PayU. Parameters are described in the si_details Object section.
      </td>
    </tr>

    <tr>
      <td>
        **hash**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `string` The calculated hash value using the following logic. `SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si_details|SALT)`. You can use the below button to generate a hash by providing the parameter values as per the logic.
      </td>
    </tr>
  </tbody>
</Table>

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

<Callout icon="📘" theme="info">
  **Handy Tips:**

  * One or more fields (marked optional) in the following table must be posted to modify the subscription:
    * `billingCycle`
    * `billingInterval`
    * `billingAmount`
  * If the request was to modify a subscription, si_consent_action parameter needs to be validated in the response. The field must return values modify based on the action sent in billing details JSON. Also, the payment source returned in such cases will be payu.
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
        `number` The billing amount is passed in the XX format. In use cases where `billingCycle` = `ADHOC`, amount passed is treated as maximum amount since the billing amount and billing cycle varies as per the usage of the subscription service.  In this case, the merchant is free to charge any amount for customer up to the amount specified in the defined subscription call.
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
        **mihpayid**
      </td>

      <td>
        `string` It is a unique reference number created for each transaction at PayU's end which is used to identify a transaction in case of a refund.
      </td>
    </tr>

    <tr>
      <td>
        **mode**
      </td>

      <td>
        `string` This parameter describes the payment category by which the transaction was completed/attempted by the customer. The values are:

        * `CC`: Credit Card
        * `DC`: Debit Card
      </td>
    </tr>

    <tr>
      <td>
        **bankcode**
      </td>

      <td>
        `string` This parameter contains the code indicating the payment option used for the transaction. Possible values:

        * `CC`: For Visa and Mastercard credit cards
        * `AMEX`: For American Express credit and debit cards
        * `RUPAYCC`: For RuPay credit cards
        * `VISA`: For Visa debit cards
        * `MAST`: For Mastercard debit cards
        * `RUPAY`: For RuPay debit cards
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
