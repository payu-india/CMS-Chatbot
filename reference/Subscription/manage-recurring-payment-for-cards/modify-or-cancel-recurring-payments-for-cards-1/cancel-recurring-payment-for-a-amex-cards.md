---
title: Cancel Recurring Payment for a AMEX Cards
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
This section describes how to use the **\_payment** API with  to cancel a recurring payment registration for AMEX cards.

> 📘 Notes:
>
> * This API is mandatory for merchants to go live with all cards.
> * The 2FA is required for cancelling recurring payment with AMEX cards.

Method: **POST**

**Environment**

|                            |                                                                     |
| :------------------------- | :------------------------------------------------------------------ |
| **Test Environment**       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |
| **Production Environment** | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |

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
      <td>Each payment option is identified with a String unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. For more information, refer to <a href="doc:card-type-codes-and-supported-banks-for-cards">Card Type Codes and Supported Banks for Cards</a></td>
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
        This is a JSON object and it includes a set of parameters are described in the the <a href="#si_details-parameter-json-details">si_details Parameter – JSON Details</a> table.
      </td>
      <td>Refer the example below the si_details Parameter Description table.</td>
    </tr>
    <tr>
      <td>
        <strong>Storecard_token</strong><br/>
        <code>conditional</code>
      </td>
      <td>
        <code>varchar</code> Required in case of SITokenRequestor 2 flow and tokenized flow. This parameter contains the network token value.
      </td>
      <td>{{network token value}}</td>
    </tr>
    <tr>
      <td>
        <strong>TokenFlowType</strong><br/>
        <code>conditional</code>
      </td>
      <td>
        <code>integer</code> Required in case of SITokenRequestor 2 flow and tokenized flow. This parameter must be set to 1.
      </td>
      <td>1</td>
    </tr>
    <tr>
      <td>
        <strong>Additional info for tokenized flow</strong><br/>
        <code>conditional</code>
      </td>
      <td>
        <code>json</code> Required for tokenized flow. Contains additional information needed for token processing.
      </td>
      <td>({"tavv":"1997","last4digits":"1005","par":"A0009WTYMUG6ANFB3F9Z8CNYAKCX9"})</td>
    </tr>
    <tr>
      <td>
        <strong>token_expiry</strong><br/>
        <code>conditional</code>
      </td>
      <td>
        <code>varchar</code> Required in case of SITokenRequestor 2 flow and tokenized flow. Contains the expiry date of the token.
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
        <code>SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||si_details|SALT)</code>
      </td>
      <td></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

<br />

## si\_details JSON fields description

The description for the **si\_details** parameter (JSON format):

> 📘 Note:
>
> If the request was to modify a subscription, **si\_consent\_action** parameter needs to be validated in the response. The field must return values modify based on the action sent in billing details JSON. Also, the payment source returned in such cases will be payu.

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
        <code>mandatory for modifying subscription with cards</code>
      </td>
      <td>This parameter is used only to modify an existing subscription/consent. Modification means modifying billing details like startDate, endDate, billing cycle, billing interval, billing amount.</td>
      <td></td>
    </tr>
    <tr>
      <td>
        <strong>action</strong><br/>
        <code>mandatory for cards</code>
      </td>
      <td>This parameter is used to cancel an existing subscription. Pass the values as <strong>cancel</strong> to cancel an existing subscription or consent.</td>
      <td>cancel</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

<br />

### si\_details Parameter Example Values

For a yearly plan starting from 1st January 2019, having a monthly billing amount INR 100, the plan details:

```
{"billingAmount": "100.00","billingCurrency": "INR","billingCycle": "MONTHLY","billingInterval": 1,"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"}
```

## Sample request

```
curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=56bb2e3fcb510f1c1521&amount=10000&firstname=Payu-Admin&email=test@example.com&phone=1234567890&productinfo=iPhone&api_version=7&si=2&pg=CC&bankcode=UTIBENCC&surl=https://test.payu.in/admin/test_response/&furl=https://test.payu.in/admin/test_response&ccnum=5123456789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=Test User&si_details={"authpayuid":"403993715525316543","action":"cancel"}&hash=e36568b2dfc460eab0eb3387fb7d90543ed861154f273b9593d6fcc152ed93a91e529c2f4be0965eeb57104e82d58889fa5efb52811ec78cbd1ad646e39c29a0"

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
      <td>This parameter contains the code indicating the payment option used for the transaction. For example, Visa Debit Card – VISA, Master Debit Card – MAST.</td>
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
      <td>This parameter holds the status of a transaction in PayU's internal database, which can include intermediate states. Possible values include: dropped, bounced, captured, auth, failed, usercancelled, or pending. For information on status description, refer to <a href="ref:payment-state-explanations">Payment State Explanations</a>.</td>
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
      <td>This parameter contains the error message. For the list of error message, refer to <a href="ref:error-codes">Error Codes</a>.</td>
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
      <td>This parameter is crucial and is similar to the hash parameter used in the transaction request. For more information, refer to <a href="doc:generate-hash-merchant-hosted">Generate Hash</a>.</td>
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

<br />

## Sample response

* Sample response for successful cancellation of a card mandate:

```
{"status":1,"message":"Mandate Revoked Successfully","action":"MANDATE_REVOKE"}
```

<br />

* Sample Response for failed cancellation

```
{"status":0,"message":"Mandate entry not found","action":"MANDATE_REVOKE"}
```