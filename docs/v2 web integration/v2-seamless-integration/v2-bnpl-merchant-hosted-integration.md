---
title: BNPL Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Buy Now Pay Later (\<\<glossary:BNPL>>) allows your customers to spread their payments over a relatively short period instead of paying upfront. You can collect payments from customers with BNPL using the Merchant Hosted Checkout integration.

You need to ensure that **BNPL** for the **paymentMethod.name** parameter and BNPL code based on the provider and tenure for the **paymentMethod.bankcode** parameter is posted.

> 👍 Before you begin:
>
> PayU recommends you to integrate with Test environment initially. For more information, contact you PayU Key Account Manager (KAM) or PayU Support.
## Environment

<V2_payment_envrionment />

## Request header

<V2_payment_header_params />


### Request body

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>accountId<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The merchant key provided by PayU during onboarding.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>MERCHANT123</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txnId<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Transaction ID for transaction tracking and this must be unique for every transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>REF123456</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentMethod<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the payment method used. For more information, refer to <a href="#paymentmethod-object-fields-description">paymentMethod object fields description</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {<br>        &quot;name&quot;: &quot;NetBanking&quot;,	<br>        &quot;bankCode&quot;: &quot;TESTNB&quot;<br>    }</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>order<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the transaction order including product information, ordered items, user-defined fields, and payment charge specifications. For more information, refer to <a href="#order-object-fields-description">order object fields description</a></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>additionalInfo<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Additional information including enforced payment methods, single instalment, virtual payment address (VPA), and various options for user preferences during the transaction. For more information, refer to <a href="#additionalinfo-object-fields-description">additionalInfo object fields description</a></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>callBackActions<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Actions to perform on the payment server in different scenarios. For example, success, failure, cancellation, cash on delivery, etc. For more information, refer to <a href="#callbackactions-object-fields-description">callbackActions object fields description</a></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>billingDetails<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Billing details of the customer including name, address, phone number, email, etc. For more information, refer to <a href="#billingdetails-object-field-descriptions">billingDetails object field descriptions</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

#### paymentMethod object fields description
<Accordion title="paymentMethod object" icon="fa-code">
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field must contain the payment mode code. For more information, refer to <a href="https://docs.payu.in/v1/docs/payment-mode-codes">Payment Mode Codes</a>. For BNPL, this must contain <strong>BNPL</strong>.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>bankCode<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field must contain the bank code. For BNPL bank codes, refer to <a href="https://docs.payu.in/v1/docs/bnpl-codes">BNPL Codes</a>.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>
</Accordion>

#### order object

<Accordion title="order object" icon="fa-code">
  <V2_order_object />
</Accordion>

#### callBackActions object

<Accordion title="callBackActions object" icon="fa-code">
  <CallbackActions_object />
</Accordion>

#### billingDetails object

<Accordion title="billingDetails object" icon="fa-code">
  <BillingDetails_object />
</Accordion>

#### additionalInfo object

<Accordion title="Additional Info Object" icon="fa-code">
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
                                <td style="border: 1px solid #ddd; padding: 8px;"><strong>partnerHoldTime</strong><br/><code>optional</code></td>
                                <td style="border: 1px solid #ddd; padding: 8px;">Time held by the partner for the transaction.</td>
                                <td style="border: 1px solid #ddd; padding: 8px;">60</td>
                              </tr>
                              <tr>
                                <td style="border: 1px solid #ddd; padding: 8px;"><strong>createOrder</strong><br/><code>optional</code></td>
                                <td style="border: 1px solid #ddd; padding: 8px;">A flag to store the order details (true/false).</td>
                                <td style="border: 1px solid #ddd; padding: 8px;">true</td>
                              </tr>
                              <tr>
                                <td style="border: 1px solid #ddd; padding: 8px;"><strong>txnFlow</strong><br/><code>optional</code></td>
                                <td style="border: 1px solid #ddd; padding: 8px;">For defining seamless/non-seamless flows in handling payments.</td>
                                <td style="border: 1px solid #ddd; padding: 8px;">seamless</td>
                              </tr>
                              </tbody>
                              </table>
  `}</HTMLBlock>
</Accordion>

### Sample request

```curl
curl --location 'https://apitest.payu.in/v2/payments' \
--header 'date: Thu, 27 Mar 2025 10:12:27 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="ec84843a663143bb89391f6fa2d4b9404bab1543a3eee81263b4a507ebf5d289d8fad1fbcdd59da820951e3e0f9b0b0b3d1bad9b41338804e7c42a8a6197c6e9"' \
--header 'Content-Type: application/json' \
--header 'Cookie: PHPSESSID=sclorpmpb4ngion5e996os22ao' \
--data-raw '{
    "accountId": "smsplus",
    "referenceId": "b5f2d8785768087678fn4",
    "amount": 10,
    "currency": "INR",
    "paymentSource": "WEB",
    "paymentMethod": {
        "name": "BNPL",	
        "bankCode": "LAZYPAY" 		
     },
    "order": {
        "productInfo": "qwertyuiopasdfghjkl",
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
            "price": 10
        }
    },
    "additionalInfo": {
        "txnS2sFlow": "4",
        "createOrder": "false"
    },
    "callBackActions": {
        "successAction": "https://apitest.payu.in/test_response",
        "failureAction": "https://apitest.payu.in/test_response",
        "cancelAction": "https://apitest.payu.in//test_response"
    },
    "billingDetails": {
        "firstName": "sartaj",
        "lastName": "",
        "phone": "9876543210",
        "email": "testv2@example.in",
        "city": "Bharatpur",
        "state": "Rajasthan",
        "country": "India",
        "zipCode": "321028"
    }
}'
```

### Response parameters

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

### Sample response

> 📘 Note:
>
> Reverse hashing of the response is not required with that of v2/payment API.

```
Array
(
    [referenceId] => b5f2d8785768087678fm9
    [paymentId] => 1999110000001769
    [message] => Please call verify api to get the transaction status
)
```

## Step 2: Verify the payment

Verify the transaction details using the Verification APIs. For API reference, refer to [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api) under API Reference.

> 📘 Tip
>
> The transaction ID that you posted in Step 1 with PayU must be used here.