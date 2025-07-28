---
title: Collect Payment API - Non-Seamless v2 Payment (COPY)
deprecated: false
hidden: true
metadata:
  robots: index
---
The PayU v2 Payment API enables merchants to process payments through a hosted checkout flow where customers are redirected to PayU's payment page to complete the transaction.

> 📘 **Note**
>
> This documentation covers the **non-seamless (hosted checkout)** integration. For seamless payment flows, refer to the [v2 Payment API (Seamless)](doc:v2-payment-api-seamless) documentation.

**Environment**

<V2_payment_envrionment />

## Request header

<V2_payment_header_params />

## Request parameters

<HTMLBlock>{`
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>accountId<br/><code>mandatory</code></td>
<td><code>String</code> Merchant key provided by PayU. Character limit: 50</td>
<td><code>"smsplus"</code></td>
</tr>
<tr>
<td>txnId<br/><code>mandatory</code></td>
<td><code>String</code> Unique transaction ID for the transaction. Character limit: 50</td>
<td><code>"REF_123456789"</code></td>
</tr>
<tr>
<td>order<br/><code>mandatory</code></td>
<td><code>Object</code> Order details containing product information and pricing. <a href="#order-object">See order object</a></td>
<td><code>{"productInfo": "Product Name", "paymentChargeSpecification": {"price": 1000.00}}</code></td>
</tr>
<tr>
<td>billingDetails<br/><code>mandatory</code></td>
<td><code>Object</code> Customer billing information. <a href="#billingdetails-object">See billingDetails object</a></td>
<td><code>{"firstName": "John", "email": "john@example.com", "phone": "9876543210"}</code></td>
</tr>
<tr>
<td>callBackActions<br/><code>mandatory</code></td>
<td><code>Object</code> Callback URLs for different payment outcomes. <a href="#callbackactions-object">See callBackActions object</a></td>
<td><code>{"successAction": "https://merchant.com/success", "failureAction": "https://merchant.com/failure"}</code></td>
</tr>
<tr>
<td>additionalInfo<br/><code>mandatory</code></td>
<td><code>Object</code> Additional transaction parameters including flow type. <a href="#additionalinfo-object">See additionalInfo object</a></td>
<td><code>{"txnFlow": "seamless", "enforcePaymethod": "NB"}</code></td>
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

### additionalInfo Object

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
  <td style="border: 1px solid #ddd; padding: 8px;">enforcePaymethod<br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Force a transaction with a specified method (e.g., CC, DC).</td>
  <td style="border: 1px solid #ddd; padding: 8px;">CC</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>createOrder</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">A flag to store the order details (true/false).</td>
  <td style="border: 1px solid #ddd; padding: 8px;">true</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>txnS2sFlow</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">For defining seamless/non-seamless flows in handling payments.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">nonseamless</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

<br />

## Sample Request

```bash
curl -X POST \
  https://apitest.payu.in/v2/payments \
  -H 'date: Mon, 05 Oct 2024 11:00:00 GMT' \
  -H 'authorization: HMAC test:4d1ea4e74243ea5b2b5b8b1d8a7b1a2e3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9' \
  -H 'content-type: application/json' \
  -d '{
  "accountId": "test",
  "txnId": "ref_" + Math.random().toString(36).substring(7),
  "order": {
    "productInfo": "iPhone 13",
    "paymentChargeSpecification": {
      "price": 25000.00,
      "convenienceFee": "CC:12,AMEX:19"
    },
    "userDefinedFields": {
      "udf1": "value1",
      "udf2": "value2"
    }
  },
  "billingDetails": {
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com",
    "phone": "9876543210",
    "address": "123 Main Street",
    "city": "New Delhi",
    "state": "Delhi",
    "country": "India",
    "zipCode": "110001"
  },
  "callBackActions": {
    "successAction": "https://merchant.com/success",
    "failureAction": "https://merchant.com/failure",
    "cancelAction": "https://merchant.com/cancel"
  },
  "additionalInfo": {
    "txnFlow": "nonseamless",
    "createOrder": true,
    "enforcePaymethod": "CC,NB,UPI"
  }
}'
```

## Response parameters

<V2_payment_response_params />

## Sample response

### Without order

It returns a URL similar to the following:

```
{"result":{"checkoutUrl":"https://pp78secure.payu.in/_payment_options?mihpayid=ff2bd7a285ea39d90d31e8d916ce1305&userToken="},"status":"PENDING"}
```

### With order

```
{"result":{"checkoutUrl":"https://pp78secure.payu.in/_payment_options?mihpayid=ff2bd7a285ea39d90d31e8d916ce1305&userToken="},"orderId":"b5f2d8785768087678f5","status":"PENDING"}
```

The parsed response is similar the following:

```json
Array
(
    [txnId] => b5f2d8785768087678fm9
    [mihpayId] => 1999110000001769
    [message] => Please call verify api to get the transaction status
)
```

## Verify Payment

> ⚠️ **Important**
>
> After creating a payment, you **must** call the [Verify Payment API](doc:verify-payment-api) to get the final transaction status. The initial payment creation response will typically show "PENDING" status.

<br />

## Related APIs

* [Refund API](doc:refund-api)
* [Get Transaction Details API](doc:get-transaction-details-api)
* [Create Order API](doc:create-order-api)