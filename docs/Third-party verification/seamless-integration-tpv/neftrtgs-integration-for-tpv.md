---
title: NEFT/RTGS Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - NEFT Integration for TPV
    - ' Third Party Validation NEFT Integration'
    - API Integration for NEFT TPV
    - ' PayU NEFT TPV Integration'
    - TPV NEFT Setup Guide
    - RTGS Integration for TPV
    - ' Third Party Validation RTGS Integration'
    - API Integration for RTGS TPV
    - ' PayU RTGS TPV Integration'
    - TPV RTGS Setup Guide
  robots: index
next:
  description: ''
---
Integrate <Glossary>TPV</Glossary> through NEFT/RTGS using the procedure described in this section.

## Step 1: List the Account Numbers

Collect or prepare a list of account numbers that must be posted to PayU for TPV at step 2.

This section describes the step-by-step procedure to integrate TPV with non-seamless flow.

## Step 2: Post the payment request with PayU

**Environment**

<V2_payment_envrionment />

### Request header

<Accordion title="Request headers" icon="fa-list">
  <V2_payment_header_params />
</Accordion>

### Request parameters

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
<td>order<br/><code>paymentMethod</code></td>
<td><code>Object</code> JSON object contains payment method details. <a href="#paymentMethod-object">Refer to paymentMethod object</a></td>
<td><code>{"name": "NetBanking", "bankCode": "AXNBTPV"}</code></td>
</tr>
<tr>
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
<td><code>Object</code> Additional transaction parameters including flow type. <a href="#additionalinfo-object">For more information, refer to additionalInfo object</a></td>
<td><code>{"txnFlow": "non-seamless", "enforcePaymethod": "NB"}</code></td>
  </tr>
<tr>
<td>beneficiaryDetail<br/><code>mandatory</code></td>
<td><code>Object</code> JSON object to include TPV beneficiary details. <a href="#beneficiaryDetail-object">For more information, refer to beneficiaryDetail object</a></td>
<td><a href="#beneficiaryDetail-object">For more information, refer to beneficiaryDetail object</a></td>
</tr>

</tbody>
</table>
`}</HTMLBlock>

#### paymentMethod Object

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
        `String`Bank code for the selected bank. Character limit: 10. For more information, refer to

        <Anchor label="TPV Codes" target="_blank" href="https://docs.payu.in/docs/bank-codes-for-tpv">TPV Codes</Anchor>
      </td>
    </tr>
  </tbody>
</Table>

#### beneficiaryDetail Object

**Sample object**

```
{"beneficiaryAccountNumber":"6612262_**5|323132312**_3123", "ifscCode":"KKBK0006749|HDFC000231|SBIN213213213"}
```

<Accordion title="beneficiaryDetail Object" icon="fa-user">
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

  \#####order object
</Accordion>

<Accordion title="order Object" icon="fa-box">
  <V2_order_object />
</Accordion>

##### billingDetails object object

<Accordion title="billingDetails Object" icon="fa-code">
  <BillingDetails_object />
</Accordion>

##### callBackActions object

<Accordion title="callBackActions Object" icon="fa-globe">
  <CallbackActions_object />
</Accordion>

##### additionalInfo object

<Accordion title="additionalInfo Object" icon="fa-info">
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
                      <td style="border: 1px solid #ddd; padding: 8px;">Force a transaction with a specified method..</td>
                      <td style="border: 1px solid #ddd; padding: 8px;">NB</td>
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
</Accordion>

### Sample request

<Accordion title="Sample request" icon="fa-code">
  ```json
  curl -X POST \
    https://apitest.payu.in/v2/payments \
    -H 'date: Mon, 05 Oct 2024 11:00:00 GMT' \
    -H 'authorization: HMAC smsplus:4d1ea4e74243ea5b2b5b8b1d8a7b1a2e3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9' \
    -H 'content-type: application/json' \
    -d '{
    "accountId": "smsplus",
    "referenceId": "REF_" + Math.random().toString(36).substring(7),
    "paymentMethod": {
      "name": "NEFTRTGS",
      "bankCode": "EFTAXTPV"
    },
    "order": {
      "productInfo": "Net Banking Payment",
      "paymentChargeSpecification": {
        "price": 10000.00,
        "convenienceFee": "NB:15"
      },
      "userDefinedFields": {
        "udf1": "NEFT/RTGS Transaction",
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
    "beneficiaryDetail": {"beneficiaryAccountNumber":"6612262_**5|323132312**_3123", "ifscCode":"KKBK0006749|HDFC000231|SBIN213213213"}
  }'
  ```
</Accordion>

## Step 3: Check the response from PayU

### Response parameters

<Accordion title="Response parameters" icon="fa-list">
  <V2_payment_response_params />
</Accordion>

### Sample response

<Accordion title="Sample response" icon="fa-code">
  ```json
  Array
  (
      [txnId] => b5f2d8785768087678fm9
      [paymentId] => 1999110000001769
      [message] => Please call verify api to get the transaction status
  )
  ```
</Accordion>

### Verify Payment

> ⚠️ **Important**
>
> After creating a payment, you **must** call the [Verify Payment API](ref:v2_verify_payment_api) to get the final transaction status. Net Banking transactions may require additional verification steps.
