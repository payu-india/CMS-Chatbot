---
title: Cards Consent Transaction
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: >-
    Explore how to set up a Cards (Debit or Credit) Recurring Payment Consent
    Transaction using PayU Hosted Checkout. This API documentation provides
    details for integrating Cards consent API, enabling secure and efficient
    recurring payments for your customers
  keywords:
    - PayU Cards Recurring Payment for Custom Checkout
    - ' Cards Consent Transaction for Custom Checkout'
    - ' PayU Cards Recurring Payment for Merchant Hosted Checkout'
    - ' Cards Consent Transaction for Merchant Hosted Checkout'
    - ' PayU recurring payments for Cards'
    - ' PayU subscription payments registration for Credit Cards'
    - ' Credit Card Registration transaction for Custom Checkout'
    - Credit Cards Registration transaction for Merchant Hosted Checkout
    - ' Cards Autopay'
    - ' Autopay for Cards non-PACB flow'
    - ' Cards Autopay Consent Transaction'
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
This section provides the request parameters, sample request and response for a Cards Recurring Payment Consent transaction.

> 📘 Note:
>
> During integration with PayU, first integrate with the Test Server environment. PayU will provide you the necessary Merchant Key for the test serve. After testing is done, you are ready to move to the Production server.

HTTP Method: **POST**

**Environment**

<V2_payment_envrionment />

## Request header

<V2_payment_header_params />

## Request body

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>accountId</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Represents the merchant key provided by PayU during onboarding.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">MERCHANT123</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>txnId</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Transaction ID for transaction tracking. Must be unique for every transaction. </td>
  <td style="border: 1px solid #ddd; padding: 8px;">TXN123456</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>paymentMethod</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains details of the payment method. For more information, refer to <a href="#paymentmethod-object-fields-description">paymentMethod object fields description</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>order</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains transaction order details such as product info, ordered items, user-defined fields, and payment charge details. For more information, refer to <a href="#order-object-fields-description">order Object</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Additional metadata for the transaction. For more information, refer to <a href="#additionalinfo-object-fields-description">additionalInfo Object</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>callBackActions</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">URL actions for payments (e.g., success, failure, cancel). For more information, refer to <a href="#callbackactions-object-fields-description">callBackActions Object</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>billingDetails</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Customer billing details including name, phone, and address. For more information, refer to <a href="#billingdetails-object-fields-description">billingDetails Object</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>authorization</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Authorization details for the payment process, including 3DS metadata. For more information, refer to <a href="#authorization-object-fields-description">authorization Object</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### paymentMethod object fields description

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>name</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Represents the payment method used. For credit card, include CreditCard.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">CreditCard</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>bankCode</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains the bank code. Valid values: CC, MAST, VISA.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">CC</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>paymentCard</strong><br/><code>mandatory for cards</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains physical card or saved card details. For more information, refer to </td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### paymentCard object fields description

<V2_paymentCard />

### order object fields description

<V2_order_object />

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>forcePgid<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Force identification for payment gateway integration.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>si<br><code>mandatory for Subscriptions</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This parameter must contain any of the following:  </p>
<ul>
<li><strong>1</strong>: SI is not enabled.</li>
<li><strong>2</strong>: SI is enabled.</li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>partnerHoldTime<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Time held by partner for the transaction.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>userCredentials<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Credentials for user authentication during payment.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### callBackActions object fields description

<CallbackActions_object />

### billingDetails object fields description

<BillingDetails_object />

### authorization object fields description

<V2_authorization_cards />

### threeDS2RequestData

<ThreeDSRequestData_object />

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
        "name": "CreditCard",	
        "bankCode": "CC", 		
        "paymentCard": {	
            "cardNumber": 5004461234560000,	
            "validThrough": "04/2022",
            "ownerName": "Sartaj",
            "cvv": 987,		
            "tavv": "/wAAAAAAPtP+g6IAmbSeg1gAAAA=",
            "last4Digits": "0000",
            "cardTokenType": "NETWORK",	
            "cardToken": "29850879bf39848ca078727b8e1a95165a41cea1"
        }
    },
    "order": {
        "productInfo": "string",
        "orderedItem": [
            {
                "itemId": null,	
                "description": "AAA", 
                "quantity": null,
                "amount" : 10.0
            }
        ],
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
    },
    "additionalInfo": { 
        "enforcePaymethod": "CC,DC",
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
  "billingDetails": {
    "firstName": "sartaj",
    "lastName": "",
    "address1": "Test Payu Gurgaon",
    "address2": "",
    "city": "Bharatpur",
    "state": "Rajasthan",
    "country": "India",
    "zipCode": "321028",
    "phone": "9876543210",
    "email": "testv2@example.in"
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

## Webhook for Getting Transaction Details

You can expose a webhook by requesting the PayU Integration team to configure the same against the **ws\_online\_response** parameter. If this webhook is configured, you will receive the above response object over HTTP form post method similar to the following:

```plaintext
unmappedstatus=success&phone=9999999999&txnid=FCDA1R100870163781&hash=84e335094bbcb2ddaa0f9a488eb338e143b273765d89c9dfa502402562d0b6f3c7935e28194ca92f380be7c84c3695415b106dcf52cb016a15fcf6adc98d724&status=success&curl=https://www.abc.in/payment/handlepayuresposne&firstname=NA&card_no=519619XXXXXX5049&furl=https://www.abc.in/payment/handlepayuresposne&productinfo=2&mode=DC&amount=800.00&field4=6807112311042810&field3=6807112311042810&field2=838264&field9=SUCCESS&email=NA&mihpayid=175477248&surl=https://www.ABC.in/payment/handlepayuresposne&card_hash=9e88cb0573d4a826b61d808c0a870ed4a990682459b0ec9e95ea421e8e47be8c&field1=42812&payment_source=sist
```

If the mandate is not confirmed by the customer or the mandate is confirmed by the customer, but the mandate registration is rejected from the banks, the status is communicated as a “failure” over webhook. For more information, refer to [Set up WebHook to Receive Cancellation or Modification Update from the Issuer Bank](https://docs.payu.in/v1/reference/set-up-webhook-to-receive-cancellation-or-modification-update-from-the-issuer-bank).