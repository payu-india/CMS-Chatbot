---
title: Cancel Recurring Payment for RuPay Cards
deprecated: false
hidden: false
metadata:
  title: Cancel the Recurring Payment for a Card
  description: >-
    Learn how to cancel recurring payment registrations for cards using PayU's
    API. This documentation provides detailed instructions for revoking
    mandates, ensuring compliance with RBI guidelines and enabling seamless
    management of subscription cancellations.
  keywords:
    - PayU Cancel Recurring Payments for Cards API
    - Revoke Recurring Payment for Cards
    - PayU recurring billing cancellation for Cards
    - PayU subscription cancellation for Cards
    - Cancel recurring transactions for Cards API
    - _payment cancel card recurring
  robots: index
next:
  pages:
    - slug: using-api-integration-recurring-payments
      title: Using API Integration
      type: basic
    - slug: modify-the-recurring-payments-for-a-card
      title: Modify the Recurring Payments for a Card
      type: endpoint
    - slug: check-mandate-status-api
      title: Check Mandate Status for Cards API
      type: endpoint
---
This section describes how to use the **\_payment** API with  to cancel a recurring payment registration for RuPay cards.

<Callout icon="📘" theme="info">
  ### Notes:

  - This API is mandatory for merchants to go live with all cards.
  - The 2FA is required for cancelling recurring payment with RuPay cards.
</Callout>

Method: **POST**

**Environment**

|                            |                                                                     |
| :------------------------- | :------------------------------------------------------------------ |
| **Test Environment**       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |
| **Production Environment** | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |

## Request parameters

The following table describes the parameters for delete the recurring payment details for a card.

| Parameter                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| :----------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **key**<br />`mandatory`                                                             | `varchar` This parameter is the unique Merchant Key provided by PayU for your merchant account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **txnid**<br />`mandatory`                                                           | `varchar` This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction.<br />`Character limit`: 25<br />**Note**: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID.'                      |
| **amount**<br />`mandatory`                                                          | `float` This parameter should contain the payment amount of the particular transaction.<br />**Note**: Type-cast the amount to float type<br />Depending upon the merchant use case, this value will vary.<br />- It can be either 0 INR (for Net Banking) or min 1 INR (for Cards & UPI) in penny transaction use case.<br />- In the case of first instalment use cases, this amount can be equal to initiate setup amount, but this use case will be supported only against selected Net Banking (ICICI and HDFC), all Credit / Debit Cards, and UPI                                                                                                                          |
| **productinfo**<br />`mandatory`                                                     | `varchar` This parameter should contain a brief product description. It should be a string describing the product.<br />`Character limit`: 100                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **firstname**<br />`mandatory`                                                       | `varchar` Must contain the first name of the customer.<br />`Character limit`: 60                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **email**<br />`mandatory`                                                           | `varchar` Must contain the email of the customer.<br />This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information.<br />Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.<br />`Character limit`: 50                                                                                                                                                                                                                                                                                          |
| **phone**<br />`mandatory`                                                           | `varchar` Must contain the phone number of the customer.<br />This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.<br />`Character limit`: 50                                                                                                                                                                                                                                                                                           |
| **api\_version**<br />`mandatory`                                                    | This parameter must always needs to be passed as 7.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **si**<br />`mandatory`                                                              | This parameter must be passed with the value as 3 to cancel an already existing subscription/consent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **pg**<br />`mandatory`                                                              | `String` Indicates the payment category that the merchant wants the customer to see by default on the PayU's payment page. Possible values: <ul><li>`DC`: For debit cards</li> <li>`CC`: For credit cards</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **bankcode**<br />`mandatory`                                                        | `string` A unique bank code of a payment option. Possible values: <ul><li>`RUPAYCC`: For RuPay credit cards</li> <li>`RUPAY`: For RuPay debit cards</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **ccnum**<br />`mandatory`                                                           | This parameter must contain the 13 to 19-digit card number for credit or debit cards in general.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **ccname**<br />`mandatory`                                                          | This parameter must contain the name on card – as entered by the customer for the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **ccvv**<br />`mandatory`                                                            | This parameter must contain the 3-digit CVV number for credit cards or debit cards.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **ccexpmon**<br />`mandatory`                                                        | This parameter must contain the card's expiry month – as entered by the user for the transaction. It must always be in 2 digits or in MM format.<br />For months 1-9, this parameter must be appended with 0 – like 01, 02…09. For months 10-12, this parameter must not be appended – It should be 10,11 and 12 respectively.                                                                                                                                                                                                                                                                                                                                                   |
| **ccexpyr**<br />`mandatory`                                                         | This parameter must contain the card's expiry year – as entered by the customer for the transaction. It must be of four digits.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **si\_details**<br />`mandatory`                                                     | This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.<br />**Note**: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers (for more details refer – [RBI Notification](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0)).<br />This is a JSON object and it includes a set of parameters are described in the [si\_details Parameter – JSON Details](https://docs.payu.in/reference/cancel-recurring-payment-for-a-amex-card#si_details-parameter-json-details) table. |
| **Storecard\_token**<br />`mandatory for SITokenRequestor 2 flow and tokenized flow` | `varchar` This parameter contains the network token value. For more information on SITokenRequestor 2 flow, refer to [Cards Consent Transaction > Request Parameters](https://docs.payu.in/reference/credit-card-recurring-payment-consent-transaction#storecard_token_type)                                                                                                                                                                                                                                                                                                                                                                                                     |
| **TokenFlowType**<br />`mandatory for SITokenRequestor 2 flow and tokenized flow`    | `integer` This parameter must be set to 1. For more information on SITokenRequestor 2 flow, refer to [Cards Consent Transaction > Request Parameters](https://docs.payu.in/reference/credit-card-recurring-payment-consent-transaction#storecard_token_type)                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Additional info for tokenized flow**<br />`mandatory for tokenized flow`           | `json` Contains additional information needed for token processing. For more information on tokenized flow, refer to [Cards Consent Transaction > Request Parameters](https://docs.payu.in/reference/credit-card-recurring-payment-consent-transaction#storecard_token_type)                                                                                                                                                                                                                                                                                                                                                                                                     |
| **token\_expiry**<br />`mandatory for SITokenRequestor 2 flow and tokenized flow`    | `varchar` Contains the expiry date of the token. For more information on SITokenRequestor 2 flow, refer to [Cards Consent Transaction > Request Parameters](https://docs.payu.in/reference/credit-card-recurring-payment-consent-transaction#storecard_token_type)                                                                                                                                                                                                                                                                                                                                                                                                               |
| **hash**<br />`mandatory`                                                            | Hash is a crucial parameter used to ensure that any date is not tampered while redirecting customer from the merchant website to PayU's payment interface while registration transactions.<br />It is SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si\_details by merchant salt.<br />In the case of registration transaction, the formula is used to calculate this hash is similar to the following:<br />\`SHA512(key                                                                                                                                                                                    |

## si\_details JSON fields description

The description for the **si\_details** parameter (JSON format):

<Callout icon="📘" theme="info">
  ### Note:

  If the request was to modify a subscription, **si\_consent\_action** parameter needs to be validated in the response. The field must return values modify based on the action sent in billing details JSON. Also, the payment source returned in such cases will be payu.
</Callout>

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th align="left">JSON Field</th>
      <th align="left">Description</th>
      <th align="left">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <strong>authpayuid</strong><br/>
        <code>mandatory</code>
      </td>
      <td>This parameter is used to cancel  an existing subscription/consent. </td>
      <td></td>
    </tr>
    <tr>
      <td>
        <strong>action</strong><br/>
        <code>mandatory for cards</code>
      </td>
      <td>This parameter is used to cancel an existing subscription. Pass the values as <strong>delete</strong> to cancel an existing subscription or consent.</td>
      <td>delete</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

<br />

### si\_details Parameter Example Values

#### Token requestor 1 flow

```
{"action":"delete","authPayuId":83674692837}
```

#### Token requestor 2 flow

```
{"action":"delete","authPayuId":83674692837,"siTokenRequestor":2}
```

## Sample request

```
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
--data-urlencode 'pg=CC' \ -- CC/DC
--data-urlencode 'bankcode=CC' \ -- RUPAYCC/RUPAY
--data-urlencode 'surl=https://admin.payu.in/test_response' \
--data-urlencode 'furl=https://admin.payu.in/test_response' \
--data-urlencode 'ccnum=' \
--data-urlencode 'ccname=Test User' \
--data-urlencode 'ccexpmon=05' \
--data-urlencode 'ccexpyr=2025' \
--data-urlencode 'ccvv=123' \
--data-urlencode 'si_details={"action":"delete","authPayuId":25630224100}' \
--data-urlencode 'hash={{hash_value}}'
```

## Response parameters

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th align="left">Parameter</th>
      <th align="left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>mihpayid</td>
      <td>It is a unique reference number created for each transaction at PayU's end which is used to identify a transaction in case of a refund.</td>
    </tr>
    <tr>
      <td>mode</td>
      <td>
        This parameter describes the payment category by which the transaction was completed/attempted by the customer. Possible values: <ul><li><code>DC</code>: For debit cards</li> <li><code>CC</code>: For credit cards</li></ul></td>
    </tr>
    <tr>
      <td>bankcode</td>
      <td>This parameter contains the code indicating the payment option used for the transaction. Possible values: <ul><li><code>RUPAYCC</code>: For RuPay credit cards</li> <li><code>RUPAY</code>: For RuPay debit cards</li></ul></td>
    </tr>
    <tr>
      <td>status</td>
      <td>
        This parameter returns the status of the transaction and must be used to map the order status. Possible values are success, failure, or pending. The significance of the values for these values are:<br/>
        • <strong>Success</strong>: If the value of status parameter is 'success', the transaction is successful.<br/>
        • <strong>Failed</strong>: If the value of status parameter is 'failure' or 'pending', must only be treated as a failed transaction.
      </td>
    </tr>
    <tr>
      <td>unmappedstatus</td>
      <td>This parameter holds the status of a transaction in PayU's internal database, which can include intermediate states. Possible values include: dropped, bounced, captured, auth, failed, usercancelled, or pending. For information on status description, refer to <a href="http://docs.payu.in/reference/payment-state-explanations">Payment State Explanations</a>.</td>
    </tr>
    <tr>
      <td>key</td>
      <td>This parameter contains the merchant key.</td>
    </tr>
    <tr>
      <td>error</td>
      <td>For the failed transactions, this parameter provides the reason for failure.</td>
    </tr>
    <tr>
      <td>error_message</td>
      <td>This parameter contains the error message. For the list of error message, refer to <a href="http://docs.payu.in/reference/error-codes">Error Codes</a>.</td>
    </tr>
    <tr>
      <td>bank_ref_num</td>
      <td>For each successful transaction – this parameter contains the bank reference number generated by the bank.</td>
    </tr>
    <tr>
      <td>txnid</td>
      <td>This parameter contains the transaction ID value posted by the merchant during the transaction request.</td>
    </tr>
    <tr>
      <td>amount</td>
      <td>This parameter contains the original amount which was sent in the transaction request by the merchant.</td>
    </tr>
    <tr>
      <td>cardCategory</td>
      <td>This parameter contains the card category to indicate whether it is domestic or international.</td>
    </tr>
    <tr>
      <td>discount</td>
      <td>This parameter contains the discount amount by the merchant.</td>
    </tr>
    <tr>
      <td>net_amount_debit</td>
      <td>This parameter contains the net amount debited.</td>
    </tr>
    <tr>
      <td>addedon</td>
      <td>The transaction date and time of the transaction.</td>
    </tr>
    <tr>
      <td>productinfo</td>
      <td>This parameter contains the same value of product information which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>firstname</td>
      <td>This parameter contains the same value of first name which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>lastname</td>
      <td>This parameter contains the same value of last name which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>email</td>
      <td>This parameter contains the same value of email which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>phone</td>
      <td>This parameter contains the same value of phone which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>hash</td>
      <td>This parameter is crucial and is similar to the hash parameter used in the transaction request. For more information, refer to <a href="http://docs.payu.in/docs/generate-hash-merchant-hosted">Generate Hash</a>.</td>
    </tr>
    <tr>
      <td>PG_TYPE</td>
      <td>This parameter gives information on the payment gateway used for the transaction.</td>
    </tr>
    <tr>
      <td>udf1</td>
      <td>This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>udf2</td>
      <td>This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>udf3</td>
      <td>This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5 which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>udf4</td>
      <td>This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>udf5</td>
      <td>This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>udf6</td>
      <td>This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>udf7</td>
      <td>This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>udf8</td>
      <td>This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>udf9</td>
      <td>This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>success_at</td>
      <td>This parameter contains the date and timestamp when the transaction was successful.</td>
    </tr>
    <tr>
      <td>cardnum</td>
      <td>The parameter contains the card number masked and only last 4 digits are returned.</td>
    </tr>
    <tr>
      <td>issuing_bank</td>
      <td>The parameters contains the card issuing bank.</td>
    </tr>
    <tr>
      <td>si_consent_action</td>
      <td>
        This parameter will be returned only if a modify subscription request has been received. In other cases, this field will not be returned.<br/>
        Values can be<br/>
        modify<br/>
        cancel<br/>
        If, in billing details, the action was to modify, then to validate whether the subscription was modified, this fields need to be validated in response. If this field is not sent in response of modify request, then even if transaction is success, then money would have got deducted but the subscription would not have been modified.
      </td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Sample response

- Sample response for successful cancellation of a card mandate:

```
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

<br />
