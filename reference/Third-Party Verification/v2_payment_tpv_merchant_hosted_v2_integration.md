---
title: NEFT TPV  v2 Integration
deprecated: false
hidden: true
metadata:
  title: v2 PreAuth Integration with PayU Hosted Checkout
  robots: index
---
The Collect Payment API (**v2 Payment** API) is used along with **beneficiaryDetails** object included in **additionalInfo** JSON object.

> 📘 Reference:
>
> To handle redirect URLs (surl and furl), refer to [Handling the Redirect URLs](https://docs.payu.in/v1/docs/handling-the-redirect-urls).

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
<td><code>{"name": "NetBanking", "bankCode": "AXNBTPV"}</code></td>
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
<td>Additional transaction parameters including flow type. <a href="#additionalinfo-object">Refer to additionalInfo object</a></td>
<td><code>{"txnFlow": "seamless"}</code></td>
</tr>
<tr>
<td>beneficiaryDetail<br/><code>mandatory</code></td>
<td>Beneficiary account details for Net Banking transfer. For more information, refer to <a href="#beneficiarydetail-object"> beneficiaryDetail object</a></td>
<td><code>{"beneficiaryName": "Merchant Account", "beneficiaryAccountNumber": "1234567890", "beneficiaryAccountType": "SAVINGS"}</code></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### paymentMethod Object

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        name
        `mandatory`
      </td>

      <td>
        `String` Payment method type. Must be set to `"NetBanking"`. Character limit: 10
      </td>
    </tr>

    <tr>
      <td>
        bankCode
        `mandatory`
      </td>

      <td>
        `String`Bank code for the selected bank. Character limit: 10. <Anchor label="Refer to Bank codes for TPV" target="_blank" href="https://docs.payu.in/docs/bank-codes-for-tpv/">Refer to Bank codes for TPV</Anchor>
      </td>
    </tr>
  </tbody>
</Table>

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
          <td style="border: 1px solid #ddd; padding: 8px;"><strong> enforcePaymethod </strong><br/><code>optional</code></td>
          <td style="border: 1px solid #ddd; padding: 8px;">Force a transaction with a specified method. For TPV, it is NetBanking.</td>
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

### Sample request

```curl
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
    "bankCode": "KTKNBTPV"
  },
  "order": {
    "productInfo": "TPV Payment",
    "paymentChargeSpecification": {
      "price": 10000.00,
      "convenienceFee": "NB:15"
    },
    "userDefinedFields": {
      "udf1": "TPV Transaction",
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
    "txnS2sFlow": "2"
  },
  "beneficiaryDetail": {
    "beneficiaryName": "Merchant Account",
    "beneficiaryAccountNumber": "1234567890",
    "beneficiaryAccountType": "SAVINGS"
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

## Sample response

```
{
  "result": {
    "checkoutUrl": "https://pp78secure.payu.in/_payment_options?mihpayid=<mihpayuid>&userToken="
  },
  "status": "PENDING"
}

```

> 📘 Reference:
>
> To check the transaction status, refer to [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api).