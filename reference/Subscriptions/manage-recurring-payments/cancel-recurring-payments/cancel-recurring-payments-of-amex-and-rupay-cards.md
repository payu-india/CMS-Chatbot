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

<Callout icon="❗️" theme="error">
  **Watch Out!**

  The 2FA is required for cancelling recurring payment with AMEX and RuPay cards.
</Callout>

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
        **productinfo**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `string` A product description. The value can contain maximum of 100 characters.
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
        `number` The standing instruction. You should pass the value as `3` to cancel the card mandate.
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

        * `AMEX`: For American Express credit and debit cards
        * `RUPAYCC`: For RuPay credit cards
        * `RUPAY`: For RuPay debit cards
      </td>
    </tr>

    <tr>
      <td>
        **ccnum**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `number` The credit card number used to register the mandate.
      </td>
    </tr>

    <tr>
      <td>
        **ccname**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `string` The name of the CC owner.
      </td>
    </tr>

    <tr>
      <td>
        **ccvv**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `number` The CVV of the CC.
      </td>
    </tr>

    <tr>
      <td>
        **ccexpmon**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `number` The expiry month of the CC.
      </td>
    </tr>

    <tr>
      <td>
        **ccexpyr**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `number` The expiry year of the CC.
      </td>
    </tr>

    <tr>
      <td>
        **si_details**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `json` The SI mandatory details that need to be passed during registration transaction from your system to PayU. Parameters are described in the si_details Object section.
      </td>
    </tr>

    <tr>
      <td>
        **Storecard_token**<sup style={{color: 'red'}}>*</sup> `mandatory for SITokenRequestor 2 flow and tokenized flow`
      </td>

      <td>
        `varchar` The network token value. Refer to the refer to the Cards Consent Transaction page for more information.
      </td>
    </tr>

    <tr>
      <td>
        **TokenFlowType**<sup style={{color: 'red'}}>*</sup>  `mandatory for SITokenRequestor 2 flow and tokenized flow`
      </td>

      <td>
        `integer` The token flow type. 
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
        **hash**<sup style={{color: 'red'}}>*</sup>
      </td>

      <td>
        `string` The calculated hash value using the following logic. `SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si_details|SALT)`. You can use the below button to generate a hash by providing the parameter values as per the logic.
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
