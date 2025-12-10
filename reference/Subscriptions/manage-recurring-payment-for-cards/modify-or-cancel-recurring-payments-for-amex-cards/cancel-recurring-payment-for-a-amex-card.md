---
title: Cancel Recurring Payment for an AMEX Card
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
This section describes how to use the **_payment** API with  to cancel a recurring payment registration for an AMEX card.

> 📘 Notes:
>
> * This API is mandatory for merchants to go live with all cards.
> * The 2FA is required for cancelling recurring payment with AMEX cards.

Method: **POST**

**Environment**

|                            |                                                                    |
| :------------------------- | :----------------------------------------------------------------- |
| **Test Environment**       | [https://test.payu.in/_payment](https://test.payu.in/_payment)     |
| **Production Environment** | [https://secure.payu.in/_payment](https://secure.payu.in/_payment) |

## Request parameters

The following table describes the parameters for delete the recurring payment details for a card.

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th align="left">Parameter</th>
      <th align="left">Description</th>
      <th align="left">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <strong>key</strong><br/>
        <code>mandatory</code>
      </td>
      <td><code>varchar</code> This parameter is the unique Merchant Key provided by PayU for your merchant account.</td>
      <td>Your Test Key</td>
    </tr>
    <tr>
      <td>
        <strong>txnid</strong><br/>
        <code>mandatory</code>
      </td>
      <td>
        <code>varchar</code> This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction.<br/>
        <code>Character limit</code>: 25<br/>
        <strong>Note</strong>: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID.'
      </td>
      <td>fd3e847h2</td>
    </tr>
    <tr>
      <td>
        <strong>amount</strong><br/>
        <code>mandatory</code>
      </td>
      <td>
        <code>float</code> This parameter should contain the payment amount of the particular transaction.<br/><br/>
        <strong>Note</strong>: Type-cast the amount to float type<br/>
        Depending upon the merchant use case, this value will vary.<br/><br/>
        - It can be either 0 INR (for Net Banking) or min 1 INR (for Cards & UPI) in penny transaction use case.<br/><br/>
        - In the case of first instalment use cases, this amount can be equal to initiate setup amount, but this use case will be supported only against selected Net Banking (ICICI and HDFC), all Credit / Debit Cards, and UPI
      </td>
      <td>1000</td>
    </tr>
    <tr>
      <td>
        <strong>productinfo</strong><br/>
        <code>mandatory</code>
      </td>
      <td>
        <code>varchar</code> This parameter should contain a brief product description. It should be a string describing the product.<br/>
        <code>Character limit</code>: 100
      </td>
      <td>Time Magazine Subscription</td>
    </tr>
    <tr>
      <td>
        <strong>firstname</strong><br/>
        <code>mandatory</code>
      </td>
      <td>
        <code>varchar</code> Must contain the first name of the customer.<br/>
        <code>Character limit</code>: 60
      </td>
      <td>Ashish</td>
    </tr>
    <tr>
      <td>
        <strong>email</strong><br/>
        <code>mandatory</code>
      </td>
      <td>
        <code>varchar</code> Must contain the email of the customer.<br/>
        This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information.<br/>
        Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.<br/>
        Character limit: 50
      </td>
      <td>Ashish@test.com</td>
    </tr>
    <tr>
      <td>
        <strong>phone</strong><br/>
        <code>mandatory</code>
      </td>
      <td>
        <code>varchar</code> Must contain the phone number of the customer.<br/><br/>
        This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.<br/>
        Character limit: 50
      </td>
      <td>9843176540</td>
    </tr>
    <tr>
      <td>
        <strong>api_version</strong><br/>
        <code>mandatory</code>
      </td>
      <td>This parameter must always needs to be passed as 7.</td>
      <td>7</td>
    </tr>
    <tr>
      <td>
        <strong>si</strong><br/>
        <code>mandatory</code>
      </td>
      <td>This parameter must be passed with the value as 3 to cancel an already existing subscription/consent.</td>
      <td>3</td>
    </tr>
    <tr>
      <td>
        <strong>pg</strong><br/>
        <code>mandatory</code>
      </td>
      <td><code>String</code> This parameter defines the payment category that the merchant wants the customer to see by default on the PayU's payment page. In this example, "CC" must be specified. For more information, refer to Payment Mode Codes.</td>
      <td>AMEXSI</td>
    </tr>
    <tr>
      <td>
        <strong>bankcode</strong><br/>
        <code>mandatory</code>
      </td>
      <td>Each payment option is identified with a String unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. For more information, refer to <a href="http://docs.payu.in/reference/card-type-codes-and-supported-banks-for-cards">Card Type Codes and Supported Banks for Cards</a></td>
      <td>AMEXSI</td>
    </tr>
    <tr>
      <td>
        <strong>ccnum</strong><br/>
        <code>mandatory</code>
      </td>
      <td>This parameter must contain the 13 to 19-digit card number for credit or debit cards in general.</td>
      <td></td>
    </tr>
    <tr>
      <td>
        <strong>ccname</strong><br/>
        <code>mandatory</code>
      </td>
      <td>This parameter must contain the name on card – as entered by the customer for the transaction.</td>
      <td></td>
    </tr>
    <tr>
      <td>
        <strong>ccvv</strong><br/>
        <code>mandatory</code>
      </td>
      <td>This parameter must contain the 3-digit CVV number for credit cards or debit cards. For AMEX cards, 4-digit security code (4DBC) number of the card must be posted. Also, known as CID (Card Identification) number.</td>
      <td></td>
    </tr>
    <tr>
      <td>
        <strong>ccexpmon</strong><br/>
        <code>mandatory</code>
      </td>
      <td>
        This parameter must contain the card's expiry month – as entered by the user for the transaction. It must always be in 2 digits or in MM format.<br/>
        For months 1-9, this parameter must be appended with 0 – like 01, 02…09. For months 10-12, this parameter must not be appended – It should be 10,11 and 12 respectively.
      </td>
      <td></td>
    </tr>
    <tr>
      <td>
        <strong>ccexpyr</strong><br/>
        <code>mandatory</code>
      </td>
      <td>This parameter must contain the card's expiry year – as entered by the customer for the transaction. It must be of four digits.</td>
      <td></td>
    </tr>
    <tr>
      <td>
        <strong>si_details</strong><br/>
        <code>mandatory</code>
      </td>
      <td>
        This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.<br/><br/>
        <strong>Note</strong>: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers ( for more details refer – https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668&Mode=0 )<br/><br/>
        This is a JSON object and it includes a set of parameters are described in the the <a href="https://docs.payu.in/reference/cancel-recurring-payment-for-a-amex-card#si_details-parameter-json-details">si_details Parameter – JSON Details</a> table.
      </td>
      <td>Refer the example below the si_details Parameter Description table.</td>
    </tr>
    <tr>
      <td>
        <strong>Storecard_token</strong><br/>
        <code>mandatory for SITokenRequestor 2 flow and tokenized flow</code>
      </td>
      <td>
        <code>varchar</code>  This parameter contains the network token value. For more information on SITokenRequestor 2 flow, refer to <a href="https://docs.payu.in/reference/credit-card-recurring-payment-consent-transaction#storecard_token_type">Cards Consent Transaction > Request Parameters</a>
      </td>
      <td>{{network token value}}</td>
    </tr>
    <tr>
      <td>
        <strong>TokenFlowType</strong><br/>
        <code>mandatory for SITokenRequestor 2 flow and tokenized flow</code>
      </td>
      <td>
        <code>integer</code> This parameter must be set to 1. For more information on SITokenRequestor 2 flow, refer to <a href="https://docs.payu.in/reference/credit-card-recurring-payment-consent-transaction#storecard_token_type">Cards Consent Transaction > Request Parameters</a>

      </td>
      <td>1</td>
    </tr>
    <tr>
      <td>
        <strong>Additional info for tokenized flow</strong><br/>
        <code>mandatory for tokenized flow</code> 
      </td>
      <td>
        <code>json</code> Contains additional information needed for token processing. For more information on tokenized flow, refer to <a href="https://docs.payu.in/reference/credit-card-recurring-payment-consent-transaction#storecard_token_type">Cards Consent Transaction > Request Parameters</a>
      </td>
      <td>({"tavv":"1997","last4digits":"1005","par":"A0009WTYMUG6ANFB3F9Z8CNYAKCX9"})</td>
    </tr>
    <tr>
      <td>
        <strong>token_expiry</strong><br/>
        <code>mandatory for SITokenRequestor 2 flow and tokenized flow</code>
      </td>
      <td>
        <code>varchar</code> Contains the expiry date of the token. For more information on SITokenRequestor 2 flow, refer to <a href="https://docs.payu.in/reference/credit-card-recurring-payment-consent-transaction#storecard_token_type">Cards Consent Transaction > Request Parameters</a>
      </td>
      <td></td>
    </tr>
    <tr>
      <td>
        <strong>hash</strong><br/>
        <code>mandatory</code>
      </td>
      <td>
        Hash is a crucial parameter used to ensure that any date is not tampered while redirecting customer from the merchant website to PayU's payment interface while registration transactions.<br/><br/>
        It is SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si_details by merchant salt.<br/><br/>
        In the case of registration transaction, the formula is used to calculate this hash is similar to the following:<br/>
        <code>SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si_details|SALT))</code>
      </td>
      <td></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

<br />

## si_details JSON fields description

The description for the **si_details** parameter (JSON format):

> 📘 Note:
>
> If the request was to modify a subscription, **si_consent_action** parameter needs to be validated in the response. The field must return values modify based on the action sent in billing details JSON. Also, the payment source returned in such cases will be payu.

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

### si_details Parameter Example Values

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
curl 'https://test.payu.in/_payment' \
 --data-raw 'key=JP***g&txnid=d5e7e5e6324a7860fbc6&amount=1&firstname=Payu-Admin&email=test%40example.com&phone=1234567890&productinfo=Product+Info&api_version=1&si=3&pg=CC&bankcode=AMEX&surl=https%3A%2F%2Fpp58admin.payu.in%2Ftest_response&furl=https%3A%2F%2Fpp58admin.payu.in%2Ftest_response&ccnum=&ccname=Test+User&ccexpmon=05&ccexpyr=2025&ccvv=123&si_details={"action":"delete","authPayuId":83674692837}&hash=3b0eec9b39c5866af2d6b1346df434efe800ea3ad7ea1d59ce22bf935178434383aa3316a0151ea9a6248c5785996d19a25f9aa819b8097af612c9ac76d55689'
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
        This parameter describes the payment category by which the transaction was completed/attempted by the customer. The values are:<br/>
        • Credit Card – CC<br/>
        • Debit Card – DC
      </td>
    </tr>
    <tr>
      <td>bankcode</td>
      <td>This parameter contains the code indicating the payment option used for the transaction. For AMEX, use AMEX.</td>
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

* Sample response for successful cancellation of a card mandate:

```
Array
(
    [mihpayid] => 23501453251
    [mode] => CC
    [status] => success
    [unmappedstatus] => auth
    [key] => BmTY3G
    [txnid] => ecccddc37a328b7bee81
    [amount] => 1.00
    [cardCategory] => domestic
    [discount] => 0.00
    [net_amount_debit] => 1
    [addedon] => 2025-05-12 19:12:04
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
    [hash] => e9a9cee05db5b6d66941a6df1d674d1a3f232d94f5ac4a67b1dbae13e03dd2a9cebaf6bb0f2bb9b54cadcd4215aaacfa51cc1be7ff46af4f1cbfc49456b25994
    [field1] =>
    [field2] => 10VBYWZKESJUJU
    [field3] =>
    [field4] => 23501453251auth
    [field5] =>
    [field6] =>
    [field7] => 3DS_CHALLENGE_POSITIVE
    [field8] =>
    [field9] => Authorization done using Billdesk-AmexSiHub
    [payment_source] => payu
    [meCode] => {"MID":"8366132637","Key":"2a9a271f513eb63778a4ffc31b52bf91"}
    [PG_TYPE] => CC-PG
    [bank_ref_num] => 000061885275422
    [bankcode] => AMEX
    [error] => E000
    [error_Message] => No Error
    [cardnum] => XXXXXXXXXXXX1005
    [cardhash] => This field is no longer supported in postback params.
)
 
```
