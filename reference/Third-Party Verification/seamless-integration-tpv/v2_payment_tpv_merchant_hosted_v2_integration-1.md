---
title: UPI TPV  v2 Integration
deprecated: false
hidden: false
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
> To handle redirect URLs (surl and furl), refer to [Handling the Redirect URLs](https://docs.payu.in/v1/docs/handling-the-redirect-urls).

<Accordion title="Environment" icon="fa-server">

<V2_payment_envrionment />

</Accordion>

<Accordion title="Request header" icon="fa-key">

<V2_payment_header_params />

</Accordion>

<Accordion title="Request body" icon="fa-code">

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
<td><code>{"name": "UPI", "bankCode": "UPI"}</code></td>
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

</Accordion>

<Accordion title="paymentMethod Object" icon="fa-cube">

| Parameter  | Data Type | Required | Description                                                                                                                                                                                                 |
| ---------- | --------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`     | String    | Yes      | Payment method type. Must be set to `"UPI"`. Character limit: 10                                                                                                                                            |
| `bankCode` | String    | Yes      | Bank code for the selected bank. Character limit: 10. <Anchor label="Refer to Bank codes for TPV" target="_blank" href="https://docs.payu.in/docs/bank-codes-for-tpv/">Refer to Bank codes for TPV</Anchor> |

</Accordion>

<Accordion title="order Object" icon="fa-cube">

<V2_order_object />

</Accordion>

<Accordion title="billingDetails Object" icon="fa-cube">

<BillingDetails_object />

</Accordion>

<Accordion title="callBackActions Object" icon="fa-cube">

<CallbackActions_object />

</Accordion>

<Accordion title="additionalInfo Object" icon="fa-cube">

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
          <td style="border: 1px solid #ddd; padding: 8px;">nonseamless</td>
         </tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>vpa<br><code>mandatory for UPI</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> UPI handle of the customer.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>test@payu</p></td>
</tr>
        </tbody>
        </table>
`}</HTMLBlock>

</Accordion>

<Accordion title="beneficiaryDetail object" icon="fa-cube">

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

</Accordion>

<Accordion title="Sample request" icon="fa-code">

```curl
curl --location 'https://apitest.payu.in/v2/payments' \
--header 'date: Thu, 27 Mar 2025 10:12:27 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="ec84843a663143bb89391f6fa2d4b9404bab1543a3eee81263b4a507ebf5d289d8fad1fbcdd59da820951e3e0f9b0b0b3d1bad9b41338804e7c42a8a6197c6e9"' \
--header 'Content-Type: application/json' \
--data-raw '{
    "accountId": "smsplus",
    "referenceId": "b5f2d8785768087678fn4",
    "amount": 10,
    "currency": "INR",
    "paymentSource": "WEB",
    "paymentMethod": {
        "name": "UPI",
        "bankCode": "UPI"
    },
    "order": {
        "productInfo": "UPI Payment for Order",
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
            "price": "10.00"
        }
    },
    "additionalInfo": {
          "txnFlow": "seamless",
       "createOrder": true,
       "txnS2sFlow": "2",
        "vpa": "test@payu"

    },
    "callBackActions": {
        "successAction": "https://yoursite.com/success",
        "failureAction": "https://yoursite.com/failure",
        "cancelAction": "https://yoursite.com/cancel"
    },
    "billingDetails": {
        "firstName": "John",
        "lastName": "Doe",
        "phone": "9876543210",
        "email": "john.doe@example.com",
        "city": "Mumbai",
        "state": "Maharashtra",
        "country": "India",
        "zipCode": "400001"
    }
}'
```

</Accordion>

<Accordion title="Response parameters" icon="fa-list">

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

</Accordion>

<Accordion title="Sample response" icon="fa-reply">

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

</Accordion>