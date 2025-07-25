---
title: Net Banking Consent Transaction
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: Net Banking Recurring Payment Consent Transaction
  description: >-
    Explore how to set up a Netbanking Recurring Payment Consent Transaction
    using Merchant Hosted Checkout. This API documentation for integrating
    PayU's Netbanking or Net Banking consent feature, enabling secure and
    efficient recurring payments for your customers.
  keywords:
    - PayU Netbanking Recurring Payment for Custom Checkout
    - ' Netbanking Consent Transaction for Custom Checkout'
    - ' PayU Netbanking Recurring Payment for Merchant Hosted Checkout'
    - ' Netbanking Consent Transaction for Merchant Hosted Checkout'
    - ' PayU recurring payments'
    - ' PayU subscription payments registration for Net Banking'
    - ' Net Banking Registration transaction'
    - Netbbanking Registration transaction
    - ' Netbanking Autopay'
    - ' Autopay for NetBanking non-PACB flow'
    - ' Netbanking Autopay Consent Transaction'
    - ' Net Banking Autopay'
    - ' Autopay for Net Banking non-PACB flow'
    - ' Net Banking Autopay Consent Transaction'
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: using-api-integration-recurring-payments
      title: Using API Integration
    - type: basic
      slug: customer-experience-and-workflow-recurring-payments
      title: Customer Experience and Workflow
---
This section provides the request parameters, sample request and response for a Net Banking Recurring Payment consent transaction or \<\<glossary:Consent transaction>>.

> 📘 Note:
>
> During integration with PayU, first integrate with the Test Server environment. PayU will provide you the necessary Merchant Key for the test serve. After testing is done, you are ready to move to the Production server.

HTTP Method: **POST**

**Environment**

<V2_payment_envrionment />

### Request Header

<V2_payment_header_params />

### Request body

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>accountId<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The merchant key provided by PayU during onboarding.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txnId<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Transaction ID for transaction tracking. This must be unique for each transaction.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentMethod<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the payment method used. For more information, refer to <a href="#paymentmethod-object-fields-description">paymentMethod object fields description</a>.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>order<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON Object</code>Details about the transaction order including product information, ordered items, user defined fields, and payment charge specifications. For more information, refer to <a href="#order-object-fields-description">order object fields description</a></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>additionalInfo<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON Object</code>Additional information including enforced payment methods and various options for user preferences during the transaction. For more information, refer to <a href="#additionalinfo-object-fields-description">additionalInfo object fields description</a>.<br><strong>Note</strong>: The <code>txnFlow</code> field in this JSON object must be set to <strong>nonseamless</strong>.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>callBackActions<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON Object</code>Actions to perform on the payment server in different scenarios. For example, success, failure, cancellation, cash on delivery, etc.  For more information, refer to<a href="#callbackactions-object-fields-description"> callbackActions object fields description</a></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>billingDetails<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON Object</code>Billing details of the customer including name, address, phone number, email, etc.  For more information, refer to<a href="#billingdetails-object-fields-descriptions"> billingDetails object fields descriptions</a>.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>beneficiaryDetaIl <code>mandatory for NetBanking</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the beneficiary for NetBanking. For more information, refer to <a href="#beneficiarydetaIl-object-fields-description">beneficiaryDetaIl object fields description.</a></p>
</tr>

</tbody>
</table>
`}</HTMLBlock>

### additionalInfo object fields description

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Field</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>si<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter signifies a successful consent taken from the user by the merchant. This parameter must contain 1 for a successful consent. Without this parameter sent as 1, subscription cannot be set up.<br><strong>Notes</strong>: You can modify or cancel existing recurring payment registration as described in the following sections:<br>- <a href="ref:manage-recurring-payment-for-cards">Manage Recurring Payment for Cards</a><br>- <a href="ref:api-commands-to-manage-upi-recurring-transaction">Manage UPI Recurring Transaction</a></p>
</td>
</tr><tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>si_details<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON Object</code> This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.<br><strong>Note</strong>: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers (for more details refer <a href="https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668&Mode=0">https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668&Mode=0</a>). This is a JSON object and it includes a set of fields. For more information, refer to <a href="ref:https://docs.payu.in/v2/reference/si-parameter-json-details/">SI Parameter JSON Details</a>.</p>
</td>
</tr>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>txnS2sFlow</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">For defining seamless/non-seamless flows in handling payments.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">seamless</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### paymentMethod object fields description

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Field</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>name<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field must contain the payment mode code. For more information, refer to <a href="https://docs.payu.in/v1/docs/payment-mode-codes">Payment Mode Codes</a>. For NetBanking, this must contain <strong>NetBanking</strong>.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>bankCode<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field must contain the bank code. For more information, refer to <a href="https://docs.payu.in/v1/docs/net-banking-codes">Net Banking Codes</a>.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### order Object

<V2_order_object />

### billingDetails Object

<BillingDetails_object />

### callBackActions Object

<CallbackActions_object />

## beneficiaryDetaIl object fields description

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Field</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>beneficiaryName<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The name of the beneficiary to whom the funds will be transferred.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Ram</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>beneficiaryAccountNumber<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The account number of the beneficiary&#39;s bank account.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>115501029190</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>beneficiaryAccountType<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The type of the beneficiary&#39;s bank account.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>SAVINGS</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

> ❗️ Error Handling
>
> If any error message is displayed with an error code, refer to the [Error Codes](https://docs.payu.in/v1/reference/error-codes) section to understand the reason for these error codes.

### siDetails object fields description

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Field</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>billingCycle<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The frequency of the billing, indicating how often the payment occurs.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>MONTHLY</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>billingAmount<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The amount to be billed for each cycle.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1.00</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>billingCurrency<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The currency in which the billing amount is denominated.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>INR</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>billingInterval<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The interval between billing cycles, specified in terms of the cycle frequency.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentStartDate<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The date when the payment cycle begins.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2020-09-16</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentEndDate<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The date when the payment cycle ends.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2020-10-16</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>siTokenRequestor<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This is optional and is only needed before 30th September, 2022 to activate new mandate setups in a controlled manner than activating it completely on all users. This involves creating token at the time of susbcription set. You can include any of the following values::<br>1 : PayU will tokenise the card and share it in same subscription setup call with issuers for subscription setup.<br>2: PayU will do the authorization on plain card. Later, the same response will be shared to merchant.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>authpayuid<br><code>mandatory for modifying subscription</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>An identifier used for the authorization of payments via PayU.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>action<br><code>mandatory for cards</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field is used to modify or delete an existing subscription.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### billingDetails object field descriptions

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Field</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>firstName<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>First name of the billing contact</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Ashish</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>lastName<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Last name of the billing contact</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Kumar</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>phone<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Phone number of the billing contact</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>9123456789</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>email<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Email address of the billing contact</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="mailto:ashish@abc.com">ashish@abc.com</a></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>city<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>City of the billing address</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Bengaluru</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>state<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>State of the billing address</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Karnatka</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>country<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Country of the billing address</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Indiia</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>zipCode<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Postal/Zip code of the billing address</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>560071</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

```curl
curl --location 'https://apitest.payu.in/v2/payments' \
--header 'date: Tue, 05 Nov 2024 06:12:57 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="d583ff8069c7dfa8340464a24bdd01cbebf4432b4dfe4de862065cc9c9dc622c24c77cb1ac1142bf581ec07eca8d0ec78a66db93f6cd557d0da552f05c0825e3"' \
--header 'Content-Type: application/json' \
--header 'mid: 8390470' \
--header 'X-CREDENTIAL-USERNAME: UMXDPA' \
--data-raw '{
    "accountId": "UMXDPA",
    "referenceId": "ZP6267f0d2996ce",
    "amount": 10,
    "paymentMethod": {
        "name": "NetBanking",	
        "bankCode": "TESTNB"
    },
    "order": {
        "productInfo": "string"
        "userDefinedFields": {
            "udf1": "",
            "udf2": "",
            "udf3": "",
            "udf4": "",
            "udf5": "",
            "udf6": "",
            "udf7": "",
            "udf8": "",
            "udf9": "",
            "udf10": ""
        },
     "paymentChargeSpecification": {
            "price": 10,
        }   
    },
      "additionalInfo": {
    "txnFlow": "nonseamless",
     "si": "2"
   },
    "callBackActions": {
        "successAction": "https://testapi.payu.in/admin/testresponsev2?action=successAction",
        "failureAction": "https://testapi.payu.in/admin/testresponsev2?action=failureAction",
        "cancelAction": "https://testapi.payu.in/admin/testresponsev2?action=cancelAction",
        "codAction": "https://testapi.payu.in/admin/testresponsev2?action=codAction",
        "termAction": "string",
        "timeOutAction": null,
        "returnAction": "https://testapi.payu.in/admin/testresponsev2?action=successAction"
    },
    "siDetails": {
           "billingCycle": "MONTHLY",
           "billingAmount": "1.00",
           "billingCurrency": "INR",
           "billingInterval": 1,
           "paymentStartDate": "2020-09-16",
           "paymentEndDate": "2020-10-16",
           "siTokenRequestor": "",
           "authpayuid": "",
           "action": ""
        },
    "beneficiaryDetail": {
                  "beneficiaryName": "Ram",
                  "beneficiaryAccountNumber": "115501029190",
                  "beneficiaryAccountType": "SAVINGS"
    }
}'
```

## Response parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>referenceId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the reference ID of the transaction.<br>statusCode</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the payment ID of the transaction.<br>statusCode</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>message</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the status message of the transaction.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample response

```
Array
(
    [referenceId] => b5f2d8785768087678fm9
    [paymentId] => 1999110000001769
    [message] => Please call verify api to get the transaction status
)
```

> 📘 Reference:
>
> To check the transaction status, refer to [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api).

## Webhook for getting transaction details

You can expose a webhook by requesting the PayU Integration team to configure the same against the **ws\_online\_response** parameter. If this webhook is configured, you will receive the above response object over HTTP form post method similar to the following:

```plaintext
unmappedstatus=success&phone=9999999999&txnid=FCDA1R100870163781&hash=84e335094bbcb2ddaa0f9a488eb338e143b273765d89c9dfa502402562d0b6f3c7935e28194ca92f380be7c84c3695415b106dcf52cb016a15fcf6adc98d724&status=success&curl=https://www.abc.in/payment/handlepayuresposne&firstname=NA&card_no=519619XXXXXX5049&furl=https://www.abc.in/payment/handlepayuresposne&productinfo=2&mode=DC&amount=800.00&field4=6807112311042810&field3=6807112311042810&field2=838264&field9=SUCCESS&email=NA&mihpayid=175477248&surl=https://www.ABC.in/payment/handlepayuresposne&card_hash=9e88cb0573d4a826b61d808c0a870ed4a990682459b0ec9e95ea421e8e47be8c&field1=42812&payment_source=sist
```

If the mandate is not confirmed by the customer or the mandate is confirmed by the customer, but the mandate registration is rejected from the banks, the status is communicated as a “failure” over webhook. For more information, refer to [Webhooks](https://docs.payu.in/v1/docs/webhooks).