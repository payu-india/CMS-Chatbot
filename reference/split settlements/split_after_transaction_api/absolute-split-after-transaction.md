---
title: Absolute Split After Transaction
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
You must specify two decimal places for each split, but ensure the sum split amounts are equal to the transaction amount.

> 📘 Note:
>
> You must specify two decimal places for each split, but ensure the sum of the percentage of all splits is equal to 100.

HTTP Method: **POST**

**Environment**

|                            |                                                                                                                  |
| :------------------------- | :--------------------------------------------------------------------------------------------------------------- |
| **Test Environment**       | \<[https://test.payu.in/merchant/postservice.php?form=2>](https://test.payu.in/merchant/postservice.php?form=2>) |
| **Production Environment** | \<[https://info.payu.in/merchant/postservice.php?form=2>](https://info.payu.in/merchant/postservice.php?form=2>) |

## Request parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Sample Value</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>key</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> This parameter must include the Merchant key that was provided by PayU.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>vDy3i7</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>command</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> The parameter must contain the name of the web service.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>payment_split</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>hash</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The hash string encryption is specified in this parameter. The format of the hash is:<br>|sha512(key|command|var1|salt)<br>Where, var1 contains the fields as described in the var1 description.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var1</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string (JSON)</code> This parameter is in a JSON format and fields included in the JSON format are explained the <a href="#json-request-structure">JSON request structure table</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>For an example, refer the <a href="#request-structure-for-var1-to-be-included-in--payment_split-api">Request Structure</a> subsection.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## JSON request structure

The **var1** parameter is in JSON format. The fields in the JSON format are described in the following table:

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>type</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The type of split is specified in this field. Use <strong>absolute</strong> in this field. The absolute amount is specified for each part of the split. The absolute amount is specified in the aggregatorSubAmt field of the JSON for each child or aggregator.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>absolute</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>payuId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The payment identifier provided by PayU for the transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>403993715525003544</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>splitInfo</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter must include the list of aggregator sub transaction IDs and sub amounts as specified in the <a href="#request-structure-for-var1-to-be-included-in--payment_split-api">Request Structure for var1</a> subsection:  </p>
<ul>
<li><strong>aggregatorSubTxnId</strong>: The aggregator sub transaction ID is specified in this field.</li>
<li><strong>aggregatorSubAmt</strong>: The aggregator sub amount is specified in this field.</li>
<li><strong>aggregatorCharges</strong>: The aggregator charges is specified in this field.<strong>Note</strong>: The aggregatorCharges field can only be used by parent merchant to get the aggregator commission.</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Refer to <a href="#request-structure-for-var1-to-be-included-in--payment_split-api">Request Structure for var1</a> subsection.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Request structure for var1 to be included in payment_split API

```plaintext
{  "type": "absolute",  
    "payuId": "xxxxxxxx", # PayuID of parent transaction which needs to be split.  
   "splitInfo": 
    {    
       "merchantKey1": 
       {
       "aggregatorSubTxnId": "30nknyhkhib",
       "aggregatorSubAmt": "8",
       "aggregatorCharges": "2" // parent merchant commission (Optional)    
       },
      "merchantKey2":
      {
       "aggregatorSubTxnId": "13u0nknou0",
       "aggregatorSubAmt": "2"
      },
       "merchantKey3":
       {
        "aggregatorSubTxnId": "13u0nknou02",
        "aggregatorSubAmt": "2",
        "aggregatorCharges": "1" // parent merchant commission (Optional)
       }
     }
}
```

## Sample response

Sample response for a successful split:

```plaintext
{  
 "status": 1,  
 "message": "Splits creation successful.",  
 "splitStatus": "success",  "splitSegments": 
   [
         {
           "merchantKey": "merchantKey1",
           "amount": 8,
           "subvention_amount": 0,
            "txnId": "30nknyhkhib",
           "additional_charges": 0,
           "transaction_fee": 8    },
           {
             "merchantKey": "merchantKey2",
            "amount": 2,
```
