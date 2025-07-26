---
title: PayU Hosted v2 Integration
deprecated: false
hidden: true
metadata:
  title: v2 PreAuth Integration with PayU Hosted Checkout
  robots: index
---
The Collect Payment API (**v2 Payment** API) is used along with **beneficiaryDetails** object included in **additionalInfo** JSON object.

> 📘 Note:
>
> You must use the **additionalInfo.txnFlow** must be set to **nonseamless** for PayU Hosted Checkout.

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
<td>Additional transaction parameters including flow type. <a href="#additionalinfo-object">See additionalInfo object</a></td>
<td><code>{"txnFlow": "seamless", "enforcePaymethod": "NB"}</code></td>
</tr>
<tr>
<td>beneficiaryDetail<br/><code>mandatory</code></td>
<td>Beneficiary account details for Net Banking transfer. <a href="#beneficiarydetail-object">See beneficiaryDetail object</a></td>
<td><code>{"beneficiaryName": "Merchant Account", "beneficiaryAccountNumber": "1234567890", "beneficiaryAccountType": "SAVINGS"}</code></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### paymentMethod Object

| Parameter  | Data Type | Required | Description                                                                                                                                                                                      |
| ---------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`     | String    | Yes      | Payment method type. Must be set to `"NetBanking"`. Character limit: 10                                                                                                                          |
| `bankCode` | String    | Yes      | Bank code for the selected bank. Character limit: 10. <Anchor label="See Net Banking codes" target="_blank" href="https://docs.payu.in/docs/bank-codes-for-tpv/">Refer to Bank codes for TPV</Anchor> |

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
    "txnFlow": "nonseamless",
    "createOrder" : "false",
    "beneficiarydetail": {
      "beneficiaryAccountNumber": "002001600674|00000031957292212|00000035955239352|00000035955239352",
      "ifscCode": "KTKB0000046|KTKB0000023|KTKB0000035|KTKB0000035"
    }
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