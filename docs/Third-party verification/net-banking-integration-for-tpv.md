---
title: Net Banking Integration
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: Net Banking TPV Integration
  description: >-
    Learn how to integrate Net Banking with Third Party Validation (TPV) using
    PayU's comprehensive guide. This documentation provides step-by-step
    instructions, API details, and best practices for seamless and secure
    payment processing. Enhance your online payment solutions with efficient net
    banking integration."
  keywords:
    - Net Banking Integration for TPV
    - ' Third Party Validation Net Banking Integration'
    - API Integration for NetBanking TPV
    - ' PayU NetBanking TPV Integration'
    - TPV Net Banking Setup Guide
  robots: index
next:
  description: ''
---
Integrate <Glossary>TPV</Glossary> through Net Banking using the procedure described in this section.

### Prerequisites

Seamless integration has to be done as per the standard kit. For more information, refer to  <a href="v2_payment_tpv_merchant_hosted_v2_integration" target="_blank">Collect Payments API - TPV</a> under API Reference.

***

## Step 1: List the account numbers

Collect or prepare a list of account numbers that must be posted to PayU for TPV at step 2.

## Step 2: Post the parameters to PayU

With the following additional parameters, make the transaction request with the customer’s bank account number to the PayU using the Collect Payment (**\_payment**) API. For more information, refer to <a href="ref:v2_payment_tpv_merchant_hosted_v2_integration" target="_blank"> Collect Payments API - TPV</a>..

<V2_payment_envrionment />


<Accordion title="Request header" icon="fa-list">

<V2_payment_header_params />

</Accordion>

<Accordion title="Request body" icon="fa-table">

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

<Accordion title="paymentMethod Object" icon="fa-code">

| Parameter  | Data Type | Required | Description                                                                                                                                                                                                 |
| ---------- | --------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`     | String    | Yes      | Payment method type. Must be set to `"NetBanking"`. Character limit: 10                                                                                                                                     |
| `bankCode` | String    | Yes      | Bank code for the selected bank. Character limit: 10. <Anchor label="Refer to Bank codes for TPV" target="_blank" href="https://docs.payu.in/docs/bank-codes-for-tpv/">Refer to Bank codes for TPV</Anchor> |

</Accordion>

<Accordion title="order Object" icon="fa-code">

<V2_order_object />

</Accordion>

<Accordion title="billingDetails Object" icon="fa-code">

<BillingDetails_object />

</Accordion>

<Accordion title="callBackActions Object" icon="fa-code">

<CallbackActions_object />

</Accordion>

<Accordion title="additionalInfo Object" icon="fa-code">

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

</Accordion>

<Accordion title="beneficiaryDetail object" icon="fa-code">

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


## Step 3: Check the response from PayU



### Response Parameters

The following table describes the parameters in the response from PayU:

| **Param Name**   | **Description**                                                                                                                                                                                                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| mihpayid         | It is a unique reference number created for each transaction at PayU’s end. You must note this transaction ID as this will be used as a reference for all the future actions on this transaction like Inquiry or Refund.                                                                                                 |
| merchantid       | It is the unique ID of the merchant.                                                                                                                                                                                                                                                                                     |
| txnid            | This parameter would contain the transaction ID value posted by the merchant during the transaction request.                                                                                                                                                                                                             |
| transaction\_fee | The transaction fee for the TPV transaction. For Net Banking, INR 10 is charged by default.                                                                                                                                                                                                                              |
| discount         | The discount amount given by bank on the transaction fee (if any).                                                                                                                                                                                                                                                       |
| amount           | The net amount after discount (if any) is displayed in this parameter. For Net Banking, INR 10 is charged by default.                                                                                                                                                                                                    |
| paymentgatewayid | The payment gateway identifier for the bank sending the response.                                                                                                                                                                                                                                                        |
| pg               | The payment gateway used for the transaction. In case of Net Banking, it is “NB.”                                                                                                                                                                                                                                        |
| status           | This parameter gives the status of the transaction as either success, failed or pending. Possible values: success, failure, pending If the value of the ‘status’ parameter is ’success’, the transaction is successful. If the value of ‘status’ is ‘failure’ or ‘pending’, must be treated as a failed transaction only |
| PG\_Type         | The bankcode (as in Merchant Hosted Checkout integration) of the bank is returned in the parameter.                                                                                                                                                                                                                      |
| key              | This parameter contains the merchant key for the merchant’s account at PayU. It would be the same as the key used while the transaction request is being posted from the merchant’s end to PayU.                                                                                                                         |
| riskactionStr    | This parameter contains risk action (if any) taken on the account holder.                                                                                                                                                                                                                                                |
| addedon          | The transaction timestamp is returned in this parameter.                                                                                                                                                                                                                                                                 |

> 📘 Store the mihpayid and txnid parameter values in response:
>
> PayU recommends you to make provisions to store the **mihpayid** and **txnid** parameter values (in the response) in your server as proof that TPV has been completed for a customer.

### Sample response

Formatted response:

```
Array
(
    [mihpayid] => 403993715524308236
    [mode] => NB
    [status] => success
    [unmappedstatus] => captured
    [key] => JP***g
    [txnid] => TtEmKjWF2uGliF
    [amount] => 10.00
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2021-10-05 12:44:06
    [productinfo] => iPhone
    [firstname] => Ashish
    [lastname] => 
    [address1] => 
    [address2] => 
    [city] => 
    [state] => 
    [country] => 
    [zipcode] => 
    [email] => test@gmail.com
    [phone] => 9876543210
    [udf1] => 
    [udf2] => 
    [udf3] => 
    [udf4] => 
    [udf5] => 
    [udf6] => 
    [udf7] => 
    [udf8] => 
    [udf9] => 
    [udf10] => 
    [hash] => 74d1039311528b4a7b699db7ce195d6a219d7442271dedb23e516e29490ec743a89c12448698178907e03d32fa05e8178694db8037bc0be53380099e47c3d63f
    [field1] => 
    [field2] => 
    [field3] => 
    [field4] => 
    [field5] => 
    [field6] => 
    [field7] => 
    [field8] => 
    [field9] => Transaction Completed Successfully
    [payment_source] => payu
    [PG_TYPE] => NB-PG
    [bank_ref_num] => 30646df4-69b7-43f4-acdd-21e6a593c037
    [bankcode] => TESTPGNB
    [error] => E000
    [error_Message] => No Error
)
```

> 📘 Verify payment:
>
> PayU recommends you. to verify the transaction details using the **Verification Payment** API. For more information, For API reference, refer to <a href="verify_payment_api" target="_blank">Verify Payment API</a>.