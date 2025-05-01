---
title: Subvention Refund for Aggregators API
excerpt: 'API Command: **subvention_refund_aggregator**'
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API will help in posting only subvention amount refunds. Also, transaction refunds must be initiated beforehand to get these refunds processed. Subvention Refund of the given transaction will not be allowed otherwise.

> 📘 Note:
>
> Subvention Refunds will only be processed if it is activated on the respective merchant by PayU.

HTTP Method: **POST**

**Environment**

|                        |                                  |
| :--------------------- | :------------------------------- |
| Test Environment       | &lt;https://test.payu.in/merchant/&gt; |
| Production Environment | &lt;https://info.payu.in/merchant/&gt; |

## Request parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>key<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> This parameter must contain the merchant key provided by PayU.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Your Test Key</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>command <br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> command to be used to invoke subvention API for aggregator merchants</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>subvention_refund_aggregator</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>hash  <br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code>  sha512(key|command|var1|salt)<br>sha512 is the encryption method used here.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>command</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var1  <br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> Parent Payuid</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>8768769869678678</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var2 <br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> unique alphanumeric token to distinguish refund</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>PLYH68898398TGHKL</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var3  <br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string(json)</code> This parameter contains the refund mode and beneficiary details in the following format:  </p>
<p>{&quot;subvention_mode&quot;:3, &quot;beneficiary_full_name&quot;:&quot; Nucleus&quot;,&quot; beneficiary_account_no&quot;:&quot; 50100002965304&quot;,&quot; beneficiary_ifsc&quot;:&quot;HDFC0001626&quot;}  </p>
<p>Where:  </p>
<ul>
<li><strong>Payout to Account Number</strong> : &quot;subvention_m ode&quot;:3<br>-** Payout to Internal Cards** : &quot;subvention_mode&quot;:1</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var4<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string(json)</code> This parameters contains the refunds split for each child payuid in the following format:   </p>
<p>{&quot;5****8&quot;:{&quot;subventionAmount&quot;:5,&quot; originalRefundAmount&quot;:1},&quot;73gAMf&quot;:{&quot;subventionAmount&quot;:5,&quot; originalRefundAmount&quot;:3}}  </p>
<p>Where:<br><strong>originalRefundAmount</strong> is the value of the refund that has been fired prior to calling this API.<br>**subventionAmount **is the amount to be deducted from the subvented amount.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

The valid values for **subvention_mode** are listed in the following table:

| **Refund mode** | **Value** | **Description**                |
| --------------- | --------- | ------------------------------ |
| Source          | 1         | Refunds with Normal or to card |
| UPI             | 2         | Refunds with UPI method        |
| IMPS            | 3         | Refunds with IMPS method       |
| NEFT            | 4         | Refunds with NEFT method       |

## Sample request

```
curl --request POST \
     --url 'https://info.payu.in/merchant/postservice.php?form=2' \
     --header 'content-type: application/x-www-form-urlencoded' \
     --data 'var3={"subvention_mode":3, "beneficiary_full_name":" Nucleus"," beneficiary_account_no":" 50100002965304","beneficiary_ifsc":"HDFC0001626"}' \
     --data 'var4={"5***8":{"subventionAmount":5," originalRefundAmount":1},"7****f":{"subventionAmount":5," originalRefundAmount":3}}' \
     --data key=5***8 \
     --data command=subvention_refund_aggregator \
     --data var1=403993715525150780 \
     --data var2=test567
```

## Response parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>request_id</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The unique reference number of the refund request is returned in this parameter.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>subvention-refund_status</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The status of Subvention refund is returned with any of the following:<br>    - <strong>1</strong>: Returns this values if request has been accepted<br>    - <strong>0</strong>: Returns this value if the request is not successful</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>mihpayid</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The transaction reference number provided by PayU.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>msg</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The message statement is returned in this parameter.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txn status</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The current status of the transaction for the given token is returned in this parameter.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>amount</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The amount of the transaction for the given token is returned in this parameter.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample responses

- When original transaction refunds are not initiated

```plaintext
{"5XAPG8":{"subvention_refund_status":0,"msg":"Please initiate or get
processed the original refund of this
transaction."},"73gAMf":{"subvention_refund_status":0,"msg":"Please
initiate or get processed the original refund of
this transaction."},"mihpayid":"999000000001122"}
```

- When an invalid subvention amount is refunded

```plaintext
{"5XAPG8":{"subvention_refund_status":0,"msg":" Subvention Amount is
invalid"},"73gAMf":{"subvention_refund_status":0,"msg":" Subvention
Amount is invalid"},"mihpayid":"999000000001122"}
```

- Response for successful queued subvention refund

```plaintext
{"5XAPG8":{"subvention_refund_status":1,"msg":"Subvention refund will be
processed.","request_id":"698"},"73gAMf":{"subvention_refund_status":1,"
msg":"Subvention refund will be
processed.","request_id":"699"},"mihpayid":"999000000001122"}
```

- When an invalid subvention mode is requested:

```plaintext
{"5XAPG8":{"subvention_refund_status":0,"msg":"Invalid Subvention Mode
Received"},"73gAMf":{"subvention_refund_status":0,"msg":"Invalid
Subvention Mode
Received"},"mihpayid":"999000000001122"}
```

- When proper beneficiary details are not passed:

```plaintext
{"5XAPG8":{"subvention_refund_status":0,"msg":"Beneficiary details
missing required for Subvention
Refund."},"73gAMf":{"subvention_refund_status":0,"msg":"Beneficiary
details missing required for Subvention
Refund."},"mihpayid":"999000000001122"}
```