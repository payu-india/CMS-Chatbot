---
title: UPI Integration
excerpt: >-
  Integrate <<glossary:TPV>> through UPI using the procedure described in this
  section.
deprecated: false
hidden: false
metadata:
  title: ''
  description: >-
    Discover how to integrate UPI with Third Party Validation (TPV) using PayU's
    detailed guide. This documentation offers step-by-step instructions, API
    specifications, and best practices for efficient and secure payment
    processing. Streamline your online payment solutions with seamless UPI
    integration.
  keywords:
    - UPI Integration for TPV
    - ' Third Party Validation UPI Integration'
    - API Integration for UPI TPV
    - ' PayU UPI TPV Integration'
    - TPV UPI Setup Guide
  robots: index
next:
  description: ''
---
## Prerequisites

Merchant Hosted or S2S (Seamless) integration has to be done as per the standard kit. For more information, refer to  [UPI Integration](doc:collect-payments-with-upi-seamless).

## Step 1: Validate VPA

When your customer makes payment through UPI, you can validate the customer’s Virtual Payment Address (VPA) and then initiate payment. The **validateVpa** API is used to validate the UPI handle. Validate the VPA (UPI handle) using the **validateVpa** API. For more information, refer to [Validate VPA Handle API](https://docs.payu.in/v2/reference/v2-validate-vpa-api/).

***

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
<td><code>{"name": "UPI", "bankCode": "UPI"}</code></td>
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
<td><code>{"txnS2sFlow": "seamless", "vpa": "test@payu", "enforcePaymethod": "UPI"}</code></td>
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
        `String` Payment method type. Must be set to `"UPI"`. Character limit: 10
      </td>
    </tr>

    <tr>
      <td>
        bankCode
        `mandatory`
      </td>

      <td>
        `String` Specify "UPI" for UPI. Character limit: 10.
      </td>
    </tr>
  </tbody>
</Table>


#####order object

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
                  <td style="border: 1px solid #ddd; padding: 8px;">UPI</td>
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
                <tr>
                  <td style="border: 1px solid #ddd; padding: 8px;"> <strong>vpa</strong><br/><code>optional</code></td>
                  <td style="border: 1px solid #ddd; padding: 8px;">The UPI handle of the customer</td>
                  <td style="border: 1px solid #ddd; padding: 8px;">test@payu</td>
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
      "name": "UPI",
      "bankCode": "UPI"
    },
    "order": {
      "productInfo": "UPI Payment",
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
      "enforcePaymethod": "UPI",
      "vpa": "test@payu",
      "txnS2sFlow": "2"
    }
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
> After creating a payment, you **must** call the <Anchor label="Verify Payment API" target="_blank" href="ref:v2/reference/v2_verify_payment_api">Verify Payment API</Anchor> to get the final transaction status. Net Banking transactions may require additional verification steps.