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

> ❗️ **Watch Out!**
>
> The 2FA is required for cancelling recurring payment with AMEX and RuPay cards.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /\_payment
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
  ```php Success Response
  Array
  (
    [mihpayid] => 28191285790
    [mode] => DC
    [status] => success
    [unmappedstatus] => cancelled
    [key] => BmTY3G
    [txnid] => bab0b573ae32cf4677ee
    [amount] => 1.00
    [cardCategory] => domestic
    [discount] => 0.00
    [net_amount_debit] => 1
    [addedon] => 2026-04-15 21:50:44
    [productinfo] => Product Info
    [firstname] => Payu-Admin
    [lastname] => 
    [address1] => 
    [address2] => 
    [city] => 
    [state] => 
    [country] => 
    [zipcode] => 
    [email] => test@example.com
    [phone] => 1234567890
    [udf1] => 
    [udf2] => 
    [udf3] => 
    [udf4] => 
    [udf5] => 
    [udf6] => 
    [udf7] => 
    [udf8] => 
    [udf9] => 
    [udf10] => 
    [hash] => {{hash_value}}
    [field1] => 
    [field2] => 
    [field3] => 
    [field4] => 
    [field5] => 
    [field6] => 05
    [field7] => AUTHPOSITIVE
    [field8] => SUCCESS
    [field9] => Transaction is Successful
    [payment_source] => payu
    [meCode] => {"MID":"hdfc_89052104","TKey":"u2+JwlMyPmC+VkPEeAqBmiinElUkgQw0TeOYOjujBQOG+uVlXBphmVAzXcUgejbxdCwUSNBv72SdwUUQDcQQ4k9XZShrpgOL29fqAyY5GyPQ/iLmyWd9Z6lJeU8fnl+9ZTuz3+cy/SLSTOpLACc/anStKOaMY9DjvwEdkAZACu2wgxvwvS8ORFvQhXuJI9CRmDxAQP/CYOj469P7PFVzN8MlUaBxTt1104zOEjE4M/2Tw7w+541attHFZQgSEhQLRVB7ANgwRmV3GZR4xlgYd0DtgJcNplJAO+AWUN0VkQku/2g2vd/XFCFJFj0NrzleIzI9FXe9r6I9N/p5nf+muw=="}
    [PG_TYPE] => DC-PG
    [bank_ref_num] => 7762700774896643105912
    [bankcode] => RUPAY
    [error] => E000
    [error_Message] => No Error
    [cardnum] => XXXXXXXXXXXX2656
    [cardhash] => This field is no longer supported in postback params.
  )
  ```
</Accordion>

## Request Parameters

> 📘 **Mandatory Parameters**
>
> <RequiredStar legend />

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
        <RequiredStar param="key" />
      </td>

      <td>
        `varchar` The unique Merchant Key provided by PayU for your merchant account.
      </td>
    </tr>

    <tr>
      <td>
        <RequiredStar param="txnid" />
      </td>

      <td>
        `varchar` A unique transaction ID (or order ID). It is the order reference number generated at your end. You can use this ID to track a particular order. This ID should be unique and you can duplicate it. The parameter value can be maximum of 25 characters.
      </td>
    </tr>

    <tr>
      <td>
        <RequiredStar param="amount" />
      </td>

      <td>
        `float` The transaction amount in `INR`.

        **Note**: Type-cast the amount to float type Depending upon the merchant use case, this value will vary.

        - The value should be minimum of `1.00` INR for Cards for penny testing.
        - For first installment, this can be initiate setup amount However, this is supported only for selected NetBanking (ICICI and HDFC), all Credit / Debit Cards, and UPI.
      </td>
    </tr>

    <tr>
      <td>
        <RequiredStar param="productinfo" />
      </td>

      <td>
        `string` A product description. The value can contain maximum of 100 characters.
      </td>
    </tr>

    <tr>
      <td>
        <RequiredStar param="firstname" />
      </td>

      <td>
        `varchar` The first name of the customer. For example, `Gaurav`. The value can contain maximum of 60 characters.
      </td>
    </tr>

    <tr>
      <td>
        <RequiredStar param="email" />
      </td>

      <td>
        `varchar` The email of the customer. For example, `gaurav@example.com`.  The value can contain maximum of 50 characters.

        **Note:** The email is used in case of fraud detection and chargebacks. Additionally, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.
      </td>
    </tr>

    <tr>
      <td>
        <RequiredStar param="phone" />
      </td>

      <td>
        `varchar` The customer phone number. For example, `1234567890`.

        **Note:** The email is used in case of fraud detection and chargebacks. Additionally, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.
      </td>
    </tr>

    <tr>
      <td>
        <RequiredStar param="api_version" />
      </td>

      <td>
        `number` The API version. You should always pass this value as `7`.
      </td>
    </tr>

    <tr>
      <td>
        <RequiredStar param="si" />
      </td>

      <td>
        `number` The standing instruction. You should pass the value as `3` to cancel the card mandate.
      </td>
    </tr>

    <tr>
      <td>
        <RequiredStar param="pg" />
      </td>

      <td>
        `string` This parameter describes the payment category by which the transaction was completed/attempted by the customer. Possible values:

        - `DC`: For debit cards
        - `CC`: For credit cards
      </td>
    </tr>

    <tr>
      <td>
        <RequiredStar param="bankcode" />
      </td>

      <td>
        `string` This parameter contains the code indicating the payment option used for the transaction. Possible values:

        - `AMEX`: For American Express credit and debit cards
        - `RUPAYCC`: For RuPay credit cards
        - `RUPAY`: For RuPay debit cards
      </td>
    </tr>

    <tr>
      <td>
        <RequiredStar param="ccnum" />
      </td>

      <td>
        `number` The credit card number used to register the mandate.
      </td>
    </tr>

    <tr>
      <td>
        <RequiredStar param="ccname" />
      </td>

      <td>
        `string` The name of the CC owner.
      </td>
    </tr>

    <tr>
      <td>
        <RequiredStar param="ccvv" />
      </td>

      <td>
        `number` The CVV of the CC.
      </td>
    </tr>

    <tr>
      <td>
        <RequiredStar param="ccexpmon" />
      </td>

      <td>
        `number` The expiry month of the CC.
      </td>
    </tr>

    <tr>
      <td>
        <RequiredStar param="ccexpyr" />
      </td>

      <td>
        `number` The expiry year of the CC.
      </td>
    </tr>

    <tr>
      <td>
        <RequiredStar param="si_details" />
      </td>

      <td>
        `json` The SI mandatory details that need to be passed during registration transaction from your system to PayU. Parameters are described in the [si\_details Object](https://docs.payu.in/reference/cancel-recurring-payments-of-amex-and-rupay-cards#si_details-json-parameters) section.
      </td>
    </tr>

    <tr>
      <td>
        <RequiredStar param="Storecard_token" /> `mandatory for SITokenRequestor 2 flow and tokenized flow`
      </td>

      <td>
        `varchar` The network token generated at your end. You should pass this parameter if you are using the stored card token to register the mandate.
      </td>
    </tr>

    <tr>
      <td>
        <RequiredStar param="TokenFlowType" /> `mandatory for SITokenRequestor 2 flow and tokenized flow`
      </td>

      <td>
        `integer` The token flow type. Pass the value as `1` if you are going for the `SITokenRequestor 2 flow`.
      </td>
    </tr>

    <tr>
      <td>
        <RequiredStar param="additional_info" /> `mandatory for tokenized flow`
      </td>

      <td>
        `json` The additional info json details. Refer to the <Anchor target="_blank" href="https://docs.payu.in/reference/modify-recurring-payments-of-cards#additional_info-object-parameters">`additional_info` Object Parameters</Anchor> for parameters and their description.
      </td>
    </tr>

    <tr>
      <td>
        <RequiredStar param="token_expiry" /> `mandatory for SITokenRequestor 2 flow and tokenized flow`
      </td>

      <td>
        `varchar` Determines the expiry date of the token.
      </td>
    </tr>

    <tr>
      <td>
        `surl`
      </td>

      <td>
        `string` The success URL customers are redirected to if the transaction is successful.
      </td>
    </tr>

    <tr>
      <td>
        `furl`
      </td>

      <td>
        `string` The failure URL customers are redirected to if the transaction is unsuccessful.
      </td>
    </tr>

    <tr>
      <td>
        <RequiredStar param="hash" />
      </td>

      <td>
        `string` The calculated hash value using the following logic. `SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si_details|SALT)`. You can use the below button to generate a hash by providing the parameter values as per the logic.
      </td>
    </tr>
  </tbody>
</Table>

### `si_details` JSON Parameters

> 📘 **Handy Tips**
>
> If the request was to modify a subscription, `si_consent_action` parameter needs to be validated in the response. The field must return values modify based on the action sent in billing details JSON. Also, the payment source returned in such cases will be payu.

<Accordion title="Parameters and Description" icon="fa-table">

> 📘 **Mandatory Parameters**
>
> <RequiredStar legend />

| **Parameter**                                     | **Description**                                                                                                    |
| :------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------- |
| <RequiredStar param="authpayuid" /> | This field is used to cancel an existing subscription/consent.                                                     |
| <RequiredStar param="action" />     | `string` This field is used to cancel an existing subscription. Pass `delete` as a value to modify a subscription. |
| `siTokenRequestor`                | `integer` The SI token requestor. Pass this parameter value as `2` if you opt for `token requestor 2 flow`.        |

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
        `mihpayid`
      </td>

      <td>
        `string` It is a unique reference number created for each transaction at PayU's end which is used to identify a transaction in case of a refund.
      </td>
    </tr>

    <tr>
      <td>
        `mode`
      </td>

      <td>
        `string` This parameter describes the payment category by which the transaction was completed/attempted by the customer. The values are:

        - `CC`: Credit Card
        - `DC`: Debit Card
      </td>
    </tr>

    <tr>
      <td>
        `bankcode`
      </td>

      <td>
        `string` This parameter contains the code indicating the payment option used for the transaction. Possible values:

        - `CC`: For Visa and Mastercard credit cards
        - `AMEX`: For American Express credit and debit cards
        - `RUPAYCC`: For RuPay credit cards
        - `VISA`: For Visa debit cards
        - `MAST`: For Mastercard debit cards
        - `RUPAY`: For RuPay debit cards
      </td>
    </tr>

    <tr>
      <td>
        `status`
      </td>

      <td>
        `string` The status of the transaction and must be used to map the order status. Possible values:

        - `success`: Indicates the transaction is successful.
        - `failed/pending`: If the value is `failure` or `pending`, should be treated as a failed transaction.
      </td>
    </tr>

    <tr>
      <td>
        `unmappedstatus`
      </td>

      <td>
        `string` The status of a transaction in PayU's internal database, which can include intermediate states. Possible values:

        - `dropped`
        - `bounced`
        - `captured`
        - `auth`
        - `failed`
        - `usercancelled`
        - `pending`

        Refer to the <Anchor target="_blank" href="https://docs.payu.in/reference/payment-state-explanations">Payment State Explanations</Anchor>.
      </td>
    </tr>

    <tr>
      <td>
        `key`
      </td>

      <td>
        `string` The merchant key.
      </td>
    </tr>

    <tr>
      <td>
        `error`
      </td>

      <td>
        `string` The error reason in case of the failure transaction.
      </td>
    </tr>

    <tr>
      <td>
        `error_message`
      </td>

      <td>
        `string` The error message in case of the failure transaction.
      </td>
    </tr>

    <tr>
      <td>
        `bank_ref_num`
      </td>

      <td>
        `string` The bank reference number generated by the bank for successful transactions.
      </td>
    </tr>

    <tr>
      <td>
        `txnid`
      </td>

      <td>
        `string` The unique transaction ID value posted by the merchant during the transaction request.
      </td>
    </tr>

    <tr>
      <td>
        `amount`
      </td>

      <td>
        `float`The transaction amount sent in the request in INR.
      </td>
    </tr>

    <tr>
      <td>
        `cardCategory`
      </td>

      <td>
        `string` The card category to indicate whether it is domestic or international.
      </td>
    </tr>

    <tr>
      <td>
        `discount`
      </td>

      <td>
        `float` The discount amount.
      </td>
    </tr>

    <tr>
      <td>
        `net_amount_debit`
      </td>

      <td>
        `float` The net amount debited.
      </td>
    </tr>

    <tr>
      <td>
        `addedon`
      </td>

      <td>
        `datetime` The date and time of the transaction.
      </td>
    </tr>

    <tr>
      <td>
        `productinfo`
      </td>

      <td>
        `string` The product information sent in the request.
      </td>
    </tr>

    <tr>
      <td>
        `firstname`
      </td>

      <td>
        `string` The first name of the customer.
      </td>
    </tr>

    <tr>
      <td>
        `lastname`
      </td>

      <td>
        `string` The last name of the customer.
      </td>
    </tr>

    <tr>
      <td>
        `email`
      </td>

      <td>
        `string` The email address of the customer.
      </td>
    </tr>

    <tr>
      <td>
        `phone`
      </td>

      <td>
        `varchar` The phone number of the customer.
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

    <tr>
      <td>
        `PG_TYPE`
      </td>

      <td>
        `string` Indicates the payment gateway used for the transaction.
      </td>
    </tr>

    <tr>
      <td>
        `udf1-udf10`
      </td>

      <td>
        `string` The user defined field values sent in the request.
      </td>
    </tr>

    <tr>
      <td>
        `success_at`
      </td>

      <td>
        `datetime` The date and time at when the transaction was successful.
      </td>
    </tr>

    <tr>
      <td>
        `cardnum`
      </td>

      <td>
        `integer` The last 4 digits of the card used for the transactions.
      </td>
    </tr>

    <tr>
      <td>
        `issuing_bank`
      </td>

      <td>
        `string` The card issuing bank.
      </td>
    </tr>

    <tr>
      <td>
        `si_consent_action`
      </td>

      <td>
        `string` This parameter will be returned only if a modify subscription request has been received. In other cases, this field will not be returned. Possible values:

        - `modify`
        - `cancel`

        If, in billing details, the action was to modify, then to validate whether the subscription was modified, this fields need to be validated in response. If this field is not sent in response of modify request, then even if transaction is success, then money would have got deducted but the subscription would not have been modified.
      </td>
    </tr>
  </tbody>
</Table>

<br />
