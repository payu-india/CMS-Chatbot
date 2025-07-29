---
title: Preauthorize Transaction - Seamless
deprecated: false
hidden: false
metadata:
  title: Preauthorize Transaction with Merchant Hosted Checkout
  robots: index
---
The Collect Payment API (**v2 Payment** API) with the **preAuthorize=1** in the **additionalInfo** object.

> 📘 Note:
>
> You must use the **additionalInfo.txnFlow** must be set to **nonseamless** for PayU Hosted Checkout.

> 📘 Reference:
>
> To handle redirect URLs (surl and furl), refer to [Handling the Redirect URLs](https://docs.payu.in/v1/docs/handling-the-redirect-urls).

**Environment**

|                            |                                                                              |
| :------------------------- | :--------------------------------------------------------------------------- |
| **Test Environment**       | \<[https://apitest.payu.in/v2/payments](https://apitest.payu.in/v2/payments) |
| **Production Environment** | \<[https://api.payu.in/v2/payments>](https://api.payu.in/v2/payments>)       |

## Request header

<V2_payment_header_params />

<br />

## Body

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>referenceId<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Reference ID for transaction tracking. This must be unique for each transaction.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>amount<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Amount of the transaction.<br><strong>Note</strong>: This value will not be considered as the transaction. Only the details in the <code> order.paymentChargeSpecification.price</code> field will be considered.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>currency<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Currency of the transaction. For example, INR.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentSource<code> optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Contains the payment source. For example, WEB.</p>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>enforcePaymethod<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Methods of payment that are enforced in the payment process. For more information, refer to <a href="https://docs.payu.in/v2/docs/enforce-pay-method-or-remove-category">Enforce Pay Method or Remove Category</a>.</p>
</td>
  </tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txnFlow<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Specify "seamless" for Seamless integration</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>preAuthorize<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> When set to "1", the transaction will be in pre-authorized state and funds will be captured later.</p>
</td>
</tr></tbody>
</table>
`}</HTMLBlock>

### callbackActions object

<CallbackActions_object />

<br />

<V2_Error_Handling />

### order object

<V2_order_object />

#### billingDetails object

<BillingDetails_object />

<br />

### Sample request

```curl
curl --location 'https://apitest.payu.in/v2/payments' \
--header 'date: Tue, 05 Nov 2024 06:12:57 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="d583ff8069c7dfa8340464a24bdd01cbebf4432b4dfe4de862065cc9c9dc622c24c77cb1ac1142bf581ec07eca8d0ec78a66db93f6cd557d0da552f05c0825e3"' \
--header 'Content-Type: application/json' \
--header 'mid: 8390470' \
--header 'X-CREDENTIAL-USERNAME: UMXDPA' \
{
  "accountId": "smsplus",
  "referenceId": "b5f2d8785768087678fm9",
  "paymentStatus": "SUCCESS",
  "amount": 10,
  "currency": "INR",
  "paymentSource": "WEB",
  },
  "order": {
    "productInfo": "string",
    "orderedItem": [
      {
        "itemId": null,
        "description": "AAA",
        "quantity": null
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
      "price": 10
  },
  "additionalInfo": {
    "txnFlow": "seamless",
    "createOrder" : "false",
    "preAuthorize": "1"
  },
  "callBackActions": {
    "successAction": "https://pp78admin.payu.in/test_response",
    "failureAction": "https://pp78admin.payu.in/test_response",
    "cancelAction": "https://testapi.payu.in/admin/testresponsev2?action=cancelAction"
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
  }
}
```

## Response parameters

<V2_payment_response_params />

## Sample response

```
{
  "result": {
    "paymentId": "1999110000001769",
    "redirectUrl": "https://secure.payu.in/ResponseHandler.php",
    "authAction": "https://apitest.payu.in/v2/payments/1999110000001769/auth"
  },
  "status": "PENDING"
}
```

<br />

> 📘 Reference:
>
> To check the transaction status, refer to [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api).