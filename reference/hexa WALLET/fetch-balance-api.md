---
title: Fetch Balance API
excerpt: 'API Command: **check\_balance**'
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **check_balance** API command is used to check the balance using the customer’s mobile number. When using Seamless Integration, integrate this API and display the balance on the Checkout page to your customers.

**Environment**

|                        |                                                 |
| :--------------------- | :---------------------------------------------- |
| Test Environment       | \<https://test.payu.in/merchant/postservice.php> |
| Production Environment | \<https://info.payu.in/merchant/postservice.php> |

## Request parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>command<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameters must contain the API command as <strong>check_balance</strong>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>check_balance</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>key<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter must contain your merchant key shared by PayU during onboarding.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Your Test Key</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>hash<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the hash. Use the following hash generation format:
sha512(key|command|var1|salt) sha512</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var1<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter must be in a JSON format as described in <a href="#var1-fields-description">var1 fields description</a> table.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>{sodexoSourceId&quot;:&quot;src_81e2c860-631b-4b01-aefa-19cfa9c63415&quot;}</code></p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

> 📘 Notes:
> 
> - var1 is in a JSON format. 
> - All the sub fields are to be sent as a json in var1. 
> - The whole JSON string should be used for hash generation.

### var1 fields description

The var1 is posted in the following format:

```
{"walletIdentifier":"AMUL","mobile":"9886575652","ibibo_code":"PAY"}
```

| Field            | Desscription                 |
| :--------------- | :--------------------------- |
| walletidentifier | Name of the wallet.          |
| ibibo_code       | The bank code of the wallet. |
| mobile           | Customer's mobile number.    |

## Sample request

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
"key=JP***g&command=check_balance&  var1={\"walletIdentifier\":\"AMUL\",\"mobile\":\"9886575652\",\"ibibo_code\":\"PAY\"}&hash=fbd44e564f49aaa271250df4fc9fdc5a7eff98d961d6ca8e8049ae0f830d7ee7ff73a4b74c69c9742ccfe0c0478e737c4c685a3fe614ba5ef7edf706097e3346"
```

## Response parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>status</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter returns the status of web service call. The status can be any of the following:  </p>
<ul>
<li>0 - If web service call failed.</li>
<li>1 - If web service call succeeded.</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cardBalance</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter returns the card balance (in rupees).</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>3000.00</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cardName</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains name of the customer as on the Sodexo card.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>test</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample response

### Success scenario

```plaintext
{"status":1,"cardBalance":"117.83","cardName":"Madhu Sudhan"}
```

### Failure scenarios

- Hash is invalid

```plaintext
{"status":0,"msg":"Invalid Hash."}
```

- Unable to fetch balance

```plaintext
{"status":0,"msg":"Unable to fetch balance"}
```

- Sodexo Source ID is not found

```plaintext
{"status":0,"msg":"Source not found."}
```