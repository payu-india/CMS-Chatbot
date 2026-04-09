---
title: Collect Payment API - PayU Hosted v2 Payment
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
The PayU v2 Payment API enables merchants to process payments through a hosted checkout flow where customers are redirected to PayU's payment page to complete the transaction.

<Callout icon="📘" theme="info">
  **Note**: This documentation covers the **non-seamless (hosted checkout)** integration. For seamless payment flows, refer to [Seamless Payment Integration](ref:v2_payment_seamless_integration).
</Callout>

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
<td><code>Object</code> Order details containing product information and pricing. For more information, refer to<a href="#order-object"> order object</a></td>
<td><code>{"productInfo": "Product Name", "paymentChargeSpecification": {"price": 1000.00}}</code></td>
</tr>
<tr>
<td>billingDetails<br/><code>mandatory</code></td>
<td><code>Object</code> Customer billing information. For more information, refer to<a href="#billingdetails-object"> billingDetails object</a></td>
<td><code>{"firstName": "John", "email": "john@example.com", "phone": "9876543210"}</code></td>
</tr>
<tr>
<td>callBackActions<br/><code>mandatory</code></td>
<td><code>Object</code> Callback URLs for different payment outcomes. For more information, refer to<a href="#callbackactions-object"> callBackActions object</a></td>
<td><code>{"successAction": "https://merchant.com/success", "failureAction": "https://merchant.com/failure"}</code></td>
</tr>
<tr>
<td>additionalInfo<br/><code>mandatory</code></td>
<td><code>Object</code> Additional transaction parameters including flow type. For more information, refer to<a href="#additionalinfo-object"> additionalInfo object</a></td>
<td><code>{"txnFlow": "non-seamless", "enforcePaymethod": "NB"}</code></td>
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

## Sample Request

<V2_Dev_Plugin />

```bash
curl --location 'https://apitest.payu.in/v2/payments' \
--header 'date: Thu, 09 Apr 2026 11:29:38 GMT' \
--header 'authorization: hmac username="PRiQvJ", algorithm="sha512", headers="date", signature="838a71fe9e3802640b0d0e2f2346d1fab14634cf58c4a78587ba1d55579f2bcfcb1db6bf4db718b7d7775f57e869aca90dfe7944c1eb5520ce055060b83b7870"' \
--header 'Content-Type: application/json' \
--data-raw '{
    "currency": "INR",
    "accountId": "PRiQvJ",
    "txnId": "Txn_98765344",
    "order": {
        "productInfo": "string",
        "userDefinedFields": {
            "udf1": "12",
            "udf2": "34",
            "udf3": "56",
            "udf4": "78",
            "udf5": "INVOICE_2345"
        },
        "paymentChargeSpecification": {
            "price": 1000
        }
    },
    "additionalInfo": {
        "txnFlow": "nonseamless"
    },
    "callBackActions": {
        "successAction": "https://test.payu.in/admin/test_response",
        "failureAction": "https://test.payu.in/admin/test_response"
    },
    "billingDetails": {
        "firstName": "sartaj",
        "lastName": "kumar",
        "address1": "Test Payu Gurgaon",
        "address2": "",
        "city": "Bharatpur",
        "state": "Rajasthan",
        "country": "India",
        "zipCode": "321028",
        "phone": "9876543210",
        "email": "testv2@example.in"
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
> After creating a payment, you **must** call the [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api/) to get the final transaction status. The initial payment creation response will typically show "PENDING" status.
