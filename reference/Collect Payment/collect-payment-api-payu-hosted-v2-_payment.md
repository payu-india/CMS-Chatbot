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

| Parameter                                   | Description                                                                                                                                                            | Example        |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| accountId<br /><code>mandatory</code>       | Merchant key provided by PayU. Type: <code>String</code>. Character limit: 50                                                                                          | jBR7XXXXXXXXXX |
| currency<br /><code>mandatory</code>        | Transaction currency code. Type: <code>String</code>                                                                                                                   | INR            |
| txnId<br /><code>mandatory</code>           | Unique transaction ID. Type: <code>String</code>. Character limit: 50                                                                                                  | txn_12345      |
| order<br /><code>mandatory</code>           | Order details containing product information and pricing. Type: <code>Object</code>. See [order object](#order-object) for detailed field descriptions.                |                |
| billingDetails<br /><code>mandatory</code>  | Customer billing information. Type: <code>Object</code>. See [billingDetails object](#billingdetails-object) for detailed field descriptions.                          |                |
| callBackActions<br /><code>mandatory</code> | Callback URLs for different payment outcomes. Type: <code>Object</code>. See [callBackActions object](#callbackactions-object) for detailed field descriptions.        |                |
| additionalInfo<br /><code>mandatory</code>  | Additional transaction parameters including flow type. Type: <code>Object</code>. See [additionalInfo object](#additionalinfo-object) for detailed field descriptions. |                |

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
curl -X POST \
  https://apitest.payu.in/v2/payments \
  -H 'date: <RFC_7231_DATE_UTC>' \
  -H 'authorization: <AUTHORIZATION_HEADER>' \
  -H 'content-type: application/json' \
  -d '{
  "accountId": "<YOUR_TEST_KEY>",
  "txnId": "<EXAMPLE_TXN_ID>",
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
{
  "txnId": "<EXAMPLE_TXN_ID>",
  "mihpayId": "<EXAMPLE_PAYU_TRANSACTION_ID>",
  "message": "Please call Verify Payment API to get the transaction status"
}
```

## Verify Payment

<Callout icon="⚠️" theme="warn">
  ### **Important**

  After creating a payment, you **must** call the [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api/) to get the final transaction status. The initial payment creation response will typically show "PENDING" status.
</Callout>
