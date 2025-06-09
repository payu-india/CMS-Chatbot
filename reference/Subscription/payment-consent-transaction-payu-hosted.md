---
title: Payment Consent Transaction using PayU Hosted Checkout
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Payment Consent Transaction using PayU Hosted Checkout
  description: >-
    Learn how to set up a Payment Consent or Registration transaction using PayU
    Hosted Checkout. This API documentation provides detailed instructions for
    integrating PayU's payment consent feature, enabling seamless recurring and
    subscription payments.
  keywords:
    - PayU Payment Consent API
    - ' PayU Hosted Checkout Subscription Registration Transaction'
    - ' Payment Consent Transaction for PayU Hosted Checkout'
    - ' PayU recurring payments registration transaction'
    - ' PayU hosted checkout subscription payments registration'
    - ' PayU hosted checkout subscription transaction consent'
    - ' Prebuilt Autopay integration'
    - ' Autopay for UPI non-PACB flow'
    - ' Pre-built Autopay Consent Transaction'
    - ' PayU Hosted Autopay'
    - ' Autopay for PayU Hosted non-PACB flow'
    - ' PayU Hosted Autopay Consent Transaction'
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: customer-experience-and-workflow-recurring-payments
      title: Customer Experience and Workflow
    - type: basic
      slug: introduction-recurring-payments-integration
      title: Introduction
---
This section describes how to set up a Payment Consent or Registration transaction using PayU Hosted Checkout integration.

HTTP Method: **POST**

**Environment**

|                            |                                                                     |
| :------------------------- | :------------------------------------------------------------------ |
| **Production Environment** | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |
| **Test Environment**       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |

## Request parameters

In the merchant-initiated POST REQUEST, Hash is a mandatory parameter. It is critical to calculate the hash correctly and post it to PayU in the request.

\<style>
/\* Target only the second column in the table \*/
.markdown-body table td:nth-child(2) \{
&#x20; word-break: break-word !important;
}

/\* Keep the first column from breaking unnecessarily \*/
.markdown-body table td:nth-child(1) \{
&#x20; word-break: normal;
&#x20; white-space: nowrap;
}
\</style>
\<table style="width: 100%; border-collapse: collapse;">
\<!-- Rest of your table HTML remains the same -->

\<table style="width: 100%; border-collapse: collapse;">
\<thead>
\<tr>
\<th>
Parameter
\</th>

\<th>
Description
\</th>

\<th>
Example
\</th>
\</tr>
\</thead>

\<tbody>
\<tr>
\<td>
key\<br>\`mandatory\`
\</td>

\<td>
\`varchar\` This parameter is the unique Merchant Key provided by PayU for your merchant account.
\</td>

\<td>
Your Test Key
\</td>
\</tr>

\<tr>
\<td>
txnid\<br>\`mandatory\`
\</td>

\<td>
\`varchar\` This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction. \`Character limit\`: 25 \*\*Note\*\*: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID.'
\</td>

\<td>
fd3e847h2
\</td>
\</tr>

\<tr>
\<td>
amount\<br>\`mandatory\`
\</td>

\<td>
\`float\` This parameter should contain the payment amount of the particular transaction.
\*\*Note\*\*: Type-cast the amount to float type Depending upon the merchant use case, this value will vary. - It can be either 0 INR (for Net Banking) or min 1 INR (for Cards & UPI) in penny transaction use case. - In the case of first instalment use cases, this amount can be equal to initiate setup amount, but this use case will be supported only against selected Net Banking (ICICI and HDFC), all Credit / Debit Cards, and UPI
\</td>

\<td>
1000
\</td>
\</tr>

\<tr>
\<td>
productinfo\<br>\`mandatory\`
\</td>

\<td>
\`varchar\` This parameter should contain a brief product description. It should be a string describing the product. \`Character limit\`: 100
\</td>

\<td>
Time Magazine Subscription
\</td>
\</tr>

\<tr>
\<td>
firstname\<br>\`mandatory\`
\</td>

\<td>
\`varchar\` Must contain the first name of the customer. \`Character limit\`: 60
\</td>

\<td>
Ashish
\</td>
\</tr>

\<tr>
\<td>
email\<br>\`mandatory\`
\</td>

\<td>
\`varchar\` Must contain the email of the customer. This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information. Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions. Character limit: 50
\</td>

\<td>
\[Ashish\@test.com]\(mailto:Ashish\@test.com)
\</td>
\</tr>

\<tr>
\<td>
phone\<br>\`mandatory\`
\</td>

\<td>
\`varchar\` Must contain the phone number of the customer. This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions. Character limit: 50
\</td>

\<td>
9843176540
\</td>
\</tr>

\<tr>
\<td>
surl\<br>\`mandatory\`
\</td>

\<td>
surL is the acronym for Success URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is successful.
\</td>

\<td>

\</td>
\</tr>

\<tr>
\<td>
furl\<br>\`mandatory\`
\</td>

\<td>
furl is the acronym for for Failure URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is failed.
\</td>

\<td>

\</td>
\</tr>

\<tr>
\<td>
api\_version\<br>\`mandatory\`
\</td>

\<td>
This parameter must always needs to be passed as 7.
\</td>

\<td>
7
\</td>
\</tr>

\<tr>
\<td>
si\<br>\`mandatory\`
\</td>

\<td>
This parameter signifies a successful consent taken from the user by the merchant. This parameter must contain 1 for a successful consent. Without this parameter sent as 1, subscription cannot be set up.
\*\*Notes\*\*: You can modify or cancel existing recurring payment registration as described in the following sections: \_. \[Manage Recurring Payment for Cards]\(ref:manage-recurring-payment-for-cards) \_. \[Manage UPI Recurring Transaction]\(ref:api-commands-to-manage-upi-recurring-transaction)
\</td>

\<td>
1
\</td>
\</tr>

\<tr>
\<td>
free\_trial\<br>\`optional\`
\</td>

\<td>
This is mandatory only if the merchant wants to support free trial use case with card and net banking together that too on PayU Hosted Checkout integration. In this case, PayU adjusts the transaction amount as INR 2.00 for cards. INR 0.00 for Net Banking and UPI registration irrespective of what amount is passed against the amount field in the request. This parameter has no significance in the case of seamless flow.
\</td>

\<td>

\</td>
\</tr>

\<tr>
\<td>
si\_details\<br>\`mandatory\`
\</td>

\<td>
This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.
\*\*Note\*\*: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers ( for more details refer \[https\://www\.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0]\(https\://www\.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0) ) This is a JSON object and it includes a set of fields. For more information, refer to \[SI Parameter JSON Details]\(ref:si-parameter-json-details)
\</td>

\<td>
\{"billingAmount": "100.00","billingCurrency": "INR","billingCycle": "MONTHLY","billingInterval": 1,"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"}
\</td>
\</tr>

\<tr>
\<td>
hash\<br>\`mandatory\`
\</td>

\<td>
Hash is a crucial parameter used to ensure that any date is not tampered while redirecting customer from the merchant website to PayU's payment interface while registration transactions. It is SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si\_details by merchant salt. In the case of registration transaction. The formula is used to calculate this hash is similar to the following:\`
HASH = SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|||||si\_details|SALT)\`
\</td>

\<td>
txnid
\</td>
\</tr>
\</tbody>
\</Table>


## Sample request

```curl
curl -X \
 POST "https://test.payu.in/_payment" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=fM3O2HnkpJ8XEC&amount=100.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cc#bankcode=AIRPENCC&si=1&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&si_details={\"billingAmount\": \"100.00\",\"billingCurrency\": \"INR\",\"billingCycle\": \"MONTHLY\",\"billingInterval\": 1,\"paymentStartDate\": \"2022-09-01\",\"paymentEndDate\": \"2022-12-01\"}&hash=2ad878f64de47c7c1149ff554cd00ee44555a8512a1d2cff9690d6ea3c9d9de0bc44b0e77c61dd60a3c64ef970612a9b71761559aa202d2a278d29dc87b998c5"
```

Characters allowed for parameters

For parameters address1, address2, city, state, country, product info, email, and phone following characters are allowed:

* Characters: A to Z, a to z, 0 to 9
* – (Minus)
* \_ (Underscore)
* @ ()
* / (Slash)
* (Space)
* . (Dot)

## Sample response

The response URL returned from PayU is in the form URL format (application/x-www-form-urlencoded).

### Parsed response

```
Array
(
    [mihpayid] => 403993715525331373
    [mode] => ENACH
    [status] => success
    [unmappedstatus] => captured
    [key] => JPM7Fg
    [txnid] => oRWSUMU4XSQBZn
    [amount] => 100.00
    [discount] => 0.00
    [net_amount_debit] => 0
    [addedon] => 2022-02-03 19:06:55
    [productinfo] => iPhone
    [firstname] => Ashish
    [lastname] => 
    [address1] => 
    [address2] => 
    [city] => 
    [state] => 
    [country] => 
    [zipcode] => 
    [email] => test@gmail.com
    [phone] => 9876543210
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
    [hash] => f3f8e4088231b190930fc4b87d3f39397d1a1d02622ef4683a983244e1cd5158f39adbb67c3d87dcb4da25ae4a941ebbf55918e4575fa1c39677a774d02c0d2d
    [field1] => ENACH285259747472911093
    [field2] => 337026657857179355
    [field3] => 
    [field4] => 
    [field5] => 
    [field6] => 
    [field7] => 
    [field8] => 
    [field9] => Mandate successfully scheduled at bank end: Your payment is scheduled successfully
    [payment_source] => sist
    [PG_TYPE] => ENACH-PG
    [bank_ref_num] => 450699821592111537
    [bankcode] => ICICENCC
    [error] => E000
    [error_Message] => No Error
)
```