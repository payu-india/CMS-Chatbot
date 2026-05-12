---
title: Modify Recurring Payments for AMEX and RuPay Cards
deprecated: false
hidden: false
metadata:
  title: Modify the Recurring Payments for a Card
  description: >-
    Learn how to modify existing recurring payment details for a card using
    PayU's API. This documentation provides detailed instructions for updating
    recurring payment information, ensuring compliance with RBI guidelines and
    enabling seamless management of subscription payments.
  keywords:
    - PayU Modify Recurring Payments API
    - Update Recurring Payment for Cards
    - PayU recurring billing updation
    - Update PayU subscription payments for cards
    - Update PayU subscription payments for UPI
    - Modify recurring transactions for Cards
    - _payment modify card recurring
  robots: index
next:
  pages:
    - slug: using-api-integration-recurring-payments
      title: Using API Integration
      type: basic
    - slug: cancel-the-recurring-payment-for-cards
      title: Cancel the Recurring Payment for a Card
      type: endpoint
---
This section describes how to use the **_payment** API to update an existing recurring payment for American Express (AMEX) and RuPay cards.

<Callout icon="📘" theme="info">
  **Note**: As per RBI guidelines while modifying the recurring payment, taking consent from the customer and doing an additional factor of authentication is mandatory. You must ensure this is done before using this API. You need to pass **authPayuId** and **action** fields to modify the billing details as part of JSON using this API as described in this section.
</Callout>

HTTP Method: **POST**

## Request parameters

The following table describes the parameters for modifying the recurring payment details for AMEX and RuPay cards.

Here's the request parameters table in markdown format, following the same two-column pipe-table style used in the sibling Integration page `cancel-recurring-payment-for-a-amex-card.md` (i.e., `**param**<br />\`mandatory``  in the first column and type chip + description in the second).

````markdown
| Parameter                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :--------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **key**<br />`mandatory`           | `varchar` This parameter is the unique Merchant Key provided by PayU for your merchant account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **txnid**<br />`mandatory`         | `varchar` This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction.<br />`Character limit`: 25<br />**Note**: Ensure that the transaction ID sent to us has not been successful earlier. |
| **amount**<br />`mandatory`        | `float` This parameter should contain the payment amount of the particular transaction.<br />**Note**: Type-cast the amount to float type. Depending upon the merchant use case, this value will vary.<br />- It can be either 0 INR (for Net Banking) or min 1 INR (for Cards & UPI) in penny transaction use case.<br />- In the case of first instalment use cases, this amount can be equal to initiate setup amount.                                                                                                                                            |
| **firstname**<br />`mandatory`     | `varchar` Must contain the first name of the customer.<br />`Character limit`: 60                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **email**<br />`mandatory`         | `varchar` Must contain the email of the customer.<br />This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information.<br />Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.<br />`Character limit`: 50                                                                                                                                                                              |
| **phone**<br />`mandatory`         | `varchar` Must contain the phone number of the customer.<br />This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information. Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.<br />`Character limit`: 50                                                                                                                                                                            |
| **productinfo**<br />`mandatory`   | `varchar` This parameter should contain a brief product description. It should be a string describing the product.<br />`Character limit`: 100                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **api_version**<br />`mandatory`   | This parameter must always be passed as **7**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **si**<br />`mandatory`            | This parameter must be passed with the value as **3** to modify an already existing subscription/consent.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **pg**<br />`mandatory`            | `String` Indicates the payment category that the merchant wants the customer to see by default on PayU's payment page. Possible values: <ul><li>`CC`: For credit cards</li><li>`DC`: For debit cards</li></ul>                                                                                                                                                                                                                                                                                                                                                       |
| **bankcode**<br />`mandatory`      | `String` A unique bank code of a payment option. Possible values: <ul><li>`AMEX`: For American Express credit and debit cards</li><li>`RUPAYCC`: For RuPay credit cards</li><li>`RUPAY`: For RuPay debit cards</li></ul> For more information, refer to [Card Type Codes and Supported Banks for Cards](doc:card-type-codes-and-supported-banks-for-cards).                                                                                                                                                                                                           |
| **surl**<br />`mandatory`          | `String` The Success URL where the customer will be redirected after a successful payment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **furl**<br />`mandatory`          | `String` The Failure URL where the customer will be redirected if the payment fails.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **ccnum**<br />`mandatory`         | This parameter must contain the 13 to 19-digit card number for credit or debit cards.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **ccexpmon**<br />`mandatory`      | This parameter must contain the card's expiry month – as entered by the user for the transaction. It must always be in 2 digits or in MM format.<br />For months 1-9, this parameter must be appended with 0 – like 01, 02…09. For months 10-12, this parameter must not be appended – it should be 10, 11 and 12 respectively.                                                                                                                                                                                                                                      |
| **ccexpyr**<br />`mandatory`       | This parameter must contain the card's expiry year – as entered by the customer for the transaction. It must be of four digits.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **ccvv**<br />`mandatory`          | This parameter must contain the 3-digit CVV number for credit cards or debit cards. For AMEX cards, the 4-digit security code (4DBC) number of the card must be posted. Also known as CID (Card Identification) number.                                                                                                                                                                                                                                                                                                                                              |
| **ccname**<br />`mandatory`        | This parameter must contain the name on card – as entered by the customer for the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **si_details**<br />`mandatory`    | This parameter represents mandatory details which need to be passed during the modify transaction from the merchant system to PayU.<br />**Note**: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that the same can be forwarded to acquirers and issuers (for more details refer – [RBI Notification](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0)).<br />This is a JSON object and it includes a set of parameters described in the **si_details Parameter – JSON Details** table. |
| **hash**<br />`mandatory`          | Hash is a crucial parameter used to ensure that any data is not tampered while redirecting the customer from the merchant website to PayU's payment interface during registration transactions.<br />It is a SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si_details by the merchant salt.<br />HASH = `SHA512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|si_details\|SALT)`                                                                      |


### For network tokens

This is applicable for the following scenarios:

* Merchant has the card token, TAVV(Cryptogram), and the last four digits of the card
* The token could be created by the merchant or through another partner

> 📘 Note:
>
> This scenario is applicable if you are PCI compliant and got the network token and TAVV from any other aggregator or schemes and then sent the card transaction request in the form of authentication.

<br />

| Parameter                                                | Description                                                                                                                                                                                 | Value                                                                                         |
| :------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------- |
| store_card_token<br/> `mandatory for store card transactions` | `String` This must include the Network token generated at your end.                                                                                                                         | 1234 4567 2456 3566                                                                           |
| storecard_token_type<br/> `mandatory`                         | `integer` This parameter is used to specify the store card token type. For this scenario, you must include **1**.                                                                           | 1                                                                                             |
| additional_info<br/> `mandatory`                              | `String` This parameter will contain the additional information in the following JSON format: `{"last4Digits": "1234", "tavv": "ABCDEFGH","trid":"1234567890", "tokenRefNo":"abcde123456"}` | `{"last4Digits": "1234", "tavv": "ABCDEFGH","trid":"1234567890", "tokenRefNo":"abcde123456"}` |

> 📘 Notes for **additional_info** parameter:
>
> The JSON format contains the following fields:
>
> * **trid** (Token Requestor ID) is the identity given by the networks for creating the tokens. You should be able to get the same from your token provider.
> * **tokenRefNo** (Token Reference Number) is generated along with the network token. . You should be able to get the same from your token provider.
> * **TAVV** is a token authentication verification value given by schemes or interchange. Also, known as cryptogram.
>
> Additional notes:
>
> * The last 4 digits of cards is mandatory for all transactions.
> * Some payment gateways require the Token Requester ID (trid) and Token Reference Number (tokenRefNo) to be passed for processing the transaction. Not passing these values will restrict the number of payment gateways available for processing the transaction.
> * Token Requester ID (trid) and Token Reference Number (tokenRefNo) are mandatory for Diners token transactions.

#### si_details Parameter – JSON Details

The description for the **si_details** parameter (JSON format):

> 📘 Notes:
>
> * One or more fields (marked optional) in the following table must be posted to modify the subscription:
>   * billingCycle
>   * billingInterval
>   * billingAmount
> * If the request was to modify a subscription,  **si_consent_action** parameter needs to be validated in the response. The field must return values modify based on the action sent in billing details JSON. Also, the payment source returned in such cases will be payu.

<br />

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        **JSON Field**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        action **mandatory for cards**
      </td>

      <td>
        This field is used to modify an existing subscription. Include **modify** to modify a subscription.
      </td>

      <td>
        modify
      </td>
    </tr>

    <tr>
      <td>
        paymentEndDate **mandatory**
      </td>

      <td>
        The end date of the billing plan is specified in this field with the YYYY-MM-DD format.

        **Note**: Pass the correct end date to PayU. Depending upon start date and end date, number of payment iterations are internally calculated and same information is passed to acquirers or banks.
      </td>

      <td>
        2023-01-14
      </td>
    </tr>

    <tr>
      <td>
        billingAmount **optional**
      </td>

      <td>
        The billing amount is passed in XX. XX format. In use cases where **billingCycle = ADHOC**, amount passed is treated as maximum amount since billing amount and billing cycle varies as per the usage of the subscription service.  In this case, the merchant is free to charge any amount for customer up to the amount specified in the defined subscription call.  For UPI, **billingAmount** should not be more than INR 15000 as it is the maximum limit allowed for UPI currently.
      </td>

      <td>
        INR 2000
      </td>
    </tr>

    <tr>
      <td>
        authpayuid **mandatory for modifying subscription with cards**
      </td>

      <td>
        This field is used only to modify an existing subscription/consent. Modification means modifying billing details like startDate, endDate, billing cycle, billing interval, billing amount.
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

### **si_details JSON example**

For a yearly plan starting from 1st January 2019, having a monthly billing amount of INR 100, the plan details:

```json
{
  "action":"modify",
  "paymentEndDate":"2030-04-13",
  "billingAmount":"400.00",
  "authPayuId":"999990000006391"
}
````

## Sample request

```bash
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

## Sample response

```
Array
(
    [mihpayid] => 25603951365
    [mode] => CC -- CC/DC
    [status] => success
    [unmappedstatus] => captured
    [key] => BmTY3G
    [txnid] => 5527fc7d02f2bfc00eb4
    [amount] => 1.00
    [cardCategory] => signature_premium
    [discount] => 0.00
    [net_amount_debit] => 1
    [addedon] => 2025-10-14 15:44:41
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
    [field1] => CBC10141015051509EGR573
    [field2] => 185869
    [field3] => 
    [field4] => 
    [field5] => 
    [field6] => 05
    [field7] => AUTHPOSITIVE
    [field8] => 0 | Transaction Completed
    [field9] => Transaction Completed
    [payment_source] => payu
    [meCode] => {"wibmo_merchant_id":"1*****72","hash_key":"{{hash_value}}","acquirer_merchant_id":"1********049780","mcc":"5499"}
    [PG_TYPE] => CC-PG
    [bank_ref_num] => 528710004895
    [bankcode] => CC -- RUPAYCC/RUPAY
    [error] => E000
    [error_Message] => No Error
    [cardnum] => XXXXXXXXXXXX4879
)
```

## Response parameters

<HTMLBlock>{`
<style>
/* Target only the second column in the table */
.markdown-body table td:nth-child(2) {
  word-break: break-word !important;
}

/* Keep the first column from breaking unnecessarily */
.markdown-body table td:nth-child(1) {
  word-break: normal;
  white-space: nowrap;
}
</style>
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
        This parameter describes the payment category by which the transaction was completed/attempted by the customer. The values are: <ul><li><code>CC</code>: Credit Card</li> <li><code>DC</code>: Debit Card</li></ul>
      </td>
    </tr>
    <tr>
      <td>bankcode</td>
      <td>Indicates the payment option used for the transaction. Possible values: <ul><li><code>AMEX</code>: For American Express credit and debit cards</li> <li><code>RUPAYCC</code>: For RuPay credit cards</li> <li><code>RUPAY</code>: For RuPay debit cards</li></ul></td>
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

<br />
