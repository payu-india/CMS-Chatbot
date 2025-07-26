---
title: Net Banking - v2 Payment API
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: Collect Payment using Net Banking with Merchant Checkout API Reference
  description: >-
    Discover the PayU API Reference for integrating NetBanking payments with
    Merchant Hosted Checkout. Access detailed guides on secure authentication
    and transaction processing NetBanking payments or Net Banking.  Ideal for
    developers looking to incorporate efficient NetBanking, internet banking,
    virtual banking or web banking solutions into their custom checkout systems.
  keywords:
    - Net Banking Merchant Hosted Checkout Collect Payment API
    - Simulator for PayU payment collection
    - Net Banking Custom Checkout integration with PayU
    - Collect payments using PayU API
    - Collect Payment API for Net Banking Merchant Hosted Checkout
    - _payment API for Net Banking Merchant Hosted Checkout
    - _payment API simulation for Net Banking Custom Checkout
    - _payment API simulation for Net Banking Merchant Hosted Checkout
    - NetBanking Custom Checkout API Reference
    - NetBanking Merchant Hosted Checkout API Reference
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: collect-payments-with-net-banking-seamless
      title: Net Banking Integration
---
The PayU v2 seamless Net Banking integration allows merchants to collect Net Banking payments directly without redirecting customers to PayU's hosted checkout page.

> 📘 **Note**
>
> This documentation covers **seamless Net Banking** integration. For hosted checkout flows, refer to the [v2 Payment API (Non-Seamless)](doc:v2-payment-api-non-seamless) documentation.

**Environment**

<V2_payment_envrionment />

## Request header

<V2_payment_header_params />

## Request body

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
<td>Merchant key provided by PayU. Character limit: 50</td>
<td><code>"smsplus"</code></td>
</tr>
<tr>
<td>txnId<br/><code>mandatory</code></td>
<td>Unique transaction ID for the transaction. Character limit: 50</td>
<td><code>"REF_123456789"</code></td>
</tr>
<tr>  
<td>paymentMethod<br/><code>mandatory</code></td>
<td>Net Banking payment method details. <a href="#paymentmethod-object">See paymentMethod object</a></td>
<td><code>{"name": "NetBanking", "bankCode": "EFTAXIS"}</code></td>
</tr>
<tr>
<td>order<br/><code>mandatory</code></td>
<td>Order details containing product information and pricing. <a href="#order-object">See order object</a></td>
<td><code>{"productInfo": "Net Banking Payment", "paymentChargeSpecification": {"price": 10000.00}}</code></td>
</tr>
<tr>
<td>billingDetails<br/><code>mandatory</code></td>
<td>Customer billing information. <a href="#billingdetails-object">See billingDetails object</a></td>
<td><code>{"firstName": "John", "email": "john@example.com", "phone": "9876543210"}</code></td>
</tr>
<tr>
<td>callBackActions<br/><code>optional</code></td>
<td>Callback URLs for different payment outcomes. <a href="#callbackactions-object">See callBackActions object</a></td>
<td><code>{"successAction": "https://merchant.com/success", "failureAction": "https://merchant.com/failure"}</code></td>
</tr>
<tr>
<td>additionalInfo<br/><code>mandatory</code></td>
<td>Additional transaction parameters including flow type. <a href="#additionalinfo-object">See additionalInfo object</a></td>
<td><code>{"txnFlow": "seamless", "enforcePaymethod": "NB"}</code></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### paymentMethod Object

| Parameter  | Data Type | Required | Description                                                                                                                                                                                      |
| ---------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`     | String    | Yes      | Payment method type. Must be set to `"NetBanking"`. Character limit: 10                                                                                                                          |
| `bankCode` | String    | Yes      | Bank code for the selected bank. Character limit: 10. <Anchor label="See Net Banking codes" target="_blank" href="https://docs.payu.in/v1/docs/net-banking-codes">See Net Banking codes</Anchor> |

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
          <td style="border: 1px solid #ddd; padding: 8px;"><strong>txnS2sFlow</strong><br/><code>optional</code></td>
          <td style="border: 1px solid #ddd; padding: 8px;">For defining seamless/non-seamless flows in handling payments.</td>
          <td style="border: 1px solid #ddd; padding: 8px;">seamless</td>
        </tr>
<tr>
<td>beneficiaryDetail<br/><code>mandatory</code></td>
<td>Beneficiary account details for Net Banking transfer. <a href="#beneficiarydetail-object">Refer to beneficiaryDetail object</a></td>
<td><code>{"beneficiaryName": "Merchant Account", "beneficiaryAccountNumber": "1234567890", "beneficiaryAccountType": "SAVINGS"}</code></td>
</tr>

        </tbody>
        </table>
`}</HTMLBlock>

### beneficiaryDetail object

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
<td>beneficiaryName<br/><code>mandatory</code></td>
<td><code>String</code> Name of the beneficiary account holder. Character limit: 100</td>
<td><code>"Merchant Account"</code></td>
</tr>
<tr>
<td>beneficiaryAccountNumber<br/><code>mandatory</code></td>
<td><code>String</code> Bank account number of the beneficiary. Character limit: 50</td>
<td><code>"1234567890"</code></td>
</tr>
<tr>
<td>beneficiaryAccountType<br/><code>mandatory</code></td>
<td><code>String</code> Type of beneficiary account (e.g., <code>"SAVINGS"</code>, <code>"CURRENT"</code>). Character limit: 20</td>
<td><code>"SAVINGS"</code></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

```bash
curl -X POST \
  https://apitest.payu.in/v2/payments \
  -H 'date: Mon, 05 Oct 2024 11:00:00 GMT' \
  -H 'authorization: HMAC smsplus:4d1ea4e74243ea5b2b5b8b1d8a7b1a2e3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9' \
  -H 'content-type: application/json' \
  -d '{
  "accountId": "smsplus",
  "referenceId": "REF_" + Math.random().toString(36).substring(7),
  "paymentMethod": {
    "name": "NetBanking",
    "bankCode": "EFTAXIS"
  },
  "order": {
    "productInfo": "Net Banking Payment",
    "paymentChargeSpecification": {
      "price": 10000.00,
      "convenienceFee": "NB:15"
    },
    "userDefinedFields": {
      "udf1": "Net Banking Transaction",
      "udf2": "Seamless Payment"
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
    "txnFlow": "seamless",
    "createOrder": true,
    "enforcePaymethod": "NB",
    "txnS2sFlow": "2"
  },
  "beneficiaryDetail": {
    "beneficiaryName": "Merchant Account",
    "beneficiaryAccountNumber": "1234567890",
    "beneficiaryAccountType": "SAVINGS"
  }
}'
```

## Response parameters

<V2_payment_response_params />

## Sample response

### Success scenario

```json
Array
(
    [txnId] => b5f2d8785768087678fm9
    [paymentId] => 1999110000001769
    [message] => Please call verify api to get the transaction status
)
```

## Verify Payment

> ⚠️ **Important**
>
> After creating a payment, you **must** call the <Anchor label="Verify Payment API" target="_blank" href="ref:v2/reference/v2_verify_payment_api">Verify Payment API</Anchor> to get the final transaction status. Net Banking transactions may require additional verification steps.