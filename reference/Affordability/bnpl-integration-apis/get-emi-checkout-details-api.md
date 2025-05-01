---
title: Get EMI Checkout Details API
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
### Environment

|                        |                                                                   |
| ---------------------- | ----------------------------------------------------------------- |
| Test Environment       | \<https://test.payu.in/info/linkAndPay/get\_emi\_checkout_details> |
| Production Environment | \<https://info.payu.in/linkAndPay/get\_emi\_checkout_details>      |

## Request Parameters

### Header

The request header contains the following fields:

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Date<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The date and time should be in the GMT time conversion(not the IST). For example, current time in India is 18:00:00 IST, the time in the date header should be 12:30:00 GMT.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Thu, 17 Feb 2022 08:17:59 GMT</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Digest<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Base 64 encode of (sha256 hash of the JSON data (post to server).</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=</code></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Authorization<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field is in the following format:<br><code>hmac username=&quot;smsplus&quot;, algorithm=&quot;hmac-sha512&quot;, headers=&quot;date digest&quot;, signature=&quot;CkGfgbho69uTMMOGU0mHWf+1CUAlIp3AjvsON9n9/E4=&quot;</code><br>Where the above format includes the following:  </p>
<ul>
<li><strong>username</strong>: The merchant key of the merchant.</li>
<li><strong>algorithm</strong>: This must have the value as <strong>hmac-sha512</strong> that is used for this API</li>
<li><strong>headers</strong>: This must have the value as <strong>date digest</strong></li>
<li><strong>signature</strong>: This must contain the hmacsha512 of (signing_string, merchant_secret), where:<ul>
<li><strong>signing_string</strong>: This is in the &quot;<strong>Date</strong>&quot;+&quot;\n&quot;+&quot;<strong>Digest</strong>&quot; format. Here, the Date and Digest is the same values in the fields listed in this table For example, &quot;Thu, 17 Feb 2022 08:17:59 GMT&quot;&quot;\n&quot;+“vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=“</li>
<li><strong>merchant_secret</strong>: The merchant Salt of the merchant. For more information on getting the merchant Salt, refer to <a href="doc:generate-merchant-key-and-salt-on-payu-dashboard">Generate Merchant Key and Salt on PayU Dashboard</a></li>
</ul>
</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> hmac username=&quot;smsplus&quot;, algorithm=&quot;hmac-sha256&quot;, headers=&quot;date digest&quot;, signature=&quot;zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI=&quot;</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>platformId<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the platform ID and include the value as <strong>1</strong>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

#### Required parameters for calculating authorization

- Date
- Authorization

The following sample Java code contains the logic used to encrypt as described in the above table:

```javascript
// date
var date = new Date();
// var date = "Wed, 28 Jun 2023 11:25:19 GMT";
date = date.toUTCString();
 
// authorization
var authorization = getAuthHeader(date);
console.log(authorization);
 
function getAuthHeader(date) {
    var AUTH_TYPE = 'sha512';
    var data = isEmpty(request['data'])?"":request['data'];
    var hash_string = data + '|' + date + '|' + pm.variables.get("merchantSalt");
    console.log("Hash String is ", hash_string);
    var hash = CryptoJS.SHA512(hash_string).toString(CryptoJS.enc.Hex);
    var authHeader = 'hmac username="' + pm.variables.get("merchantKey") + '", ' + 'algorithm="' + AUTH_TYPE + '", headers="date", signature="' + hash + '"'
    return authHeader;
}
 
pm.environment.set('date', date);
pm.environment.set('authorization', authorization);
 
function isEmpty(obj) {
    for(var key in obj) {
        if(obj.hasOwnProperty(key))
        return false;
    }
    return true;
}
```

### Body parameters

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Key <br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The merchant key provided by PayU. <br><strong>Reference</strong>: For more information on how to generate the Key and Salt, refer to any of the following:  </p>
<ul>
<li><strong>Production</strong>: <a href="https://docs.payu.in/docs/generate-merchant-key-and-salt-on-payu-dashboard">Generate Production Merchant Key and Sat</a>. </li>
<li><strong>Test</strong>: <a href="https://docs.payu.in/docs/generate-test-merchant-key-and-salt">Generate Test Merchant Key and Salt</a>.</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Your Test Key</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>requestId <br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String </code>This parameter must contain the unique ID for making an eligibility request.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Test1234</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>amount <br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The transaction amount for which the eligibility is checked is to be passed here</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{&quot;amount&quot;:&quot;10000&quot;}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>pg <code> mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>It defines the payment category using the Merchant Hosted Checkout integration. For a BNPL payment, &quot;BNPL&quot; must be specified in the <strong>pg</strong> parameter.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>BNPL</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Bankcode <br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The merchant must post this parameter with the corresponding payment option’s bank code value in it. For the list of bankcodes for BNPL, refer to <a href="https://docs.payu.in/docs/bnpl-codes">BNPL Codes</a>. <br><br>In future, wallet options will also be added.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>LAZYPAY</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>phone<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This parameter must contain the customer’s phone number for which the eligibility is to be checked needs to be passed</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>“9999999999”</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>payuToken<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This parameter must contain is the PayU instrument token for saved card.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Token12345  <br><br>Note: One or multiple payu tokens can be passed and max 10 tokens supported in a request.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>userCredentials<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This parameter must contain an unique user credential mapped against each user, to be passed by the merchant for saved card.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>abc:xyz</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

```
curl --location 'https://test.payu.in/info/linkAndPay/get_emi_checkout_details' \
--header 'x-credential-username: smsplus' \
--header 'Content-Type: application/json' \
--header 'authorization: hmac username="x0i6r2", algorithm="sha512", headers="date", signature="0e0ebc518c085d8ff49058b7c232bfe2e8779e9e9cafd34a4cdf1c11114035eea75b0e404a9b9e152757dbcc4926f78b6f18ba7f6643e2bf687a65942d3bde38"' \
--header 'date: Mon, 28 Oct 2024 10:34:49 GMT' \
--data '{
    "amount": 2000000,
    "userCredentials": "aaa:bbb",
    "phone": "9560012582",
    "bankCode": null,
    "payuToken": null
}'
```

> 📘 Authorization calculation logic:
> 
> For authorization calculation logic, refer to[ Required parameters for calculating authorization](#required-parameters-for-calculating-authorization).

## Sample response

### Success scenario

```
{
   "bnpl":{
      "all":[
         {
            "Lazypay":{
               "status":1,
               "kfsLink":"https://",
               "eligible":true,
               "customerLinked":true,
               "PayuToken":"Token12345"
            },
            "Simpl":{
               "status":1,
               "availableBalance":500,
               "kfsLink":"https://",
               "eligible":true,
               "customerLinked":true,
               "PayuToken":"Token78901"
            }
         }
      ]
   }
}
```

### Failure scenario

- Customer eligible but not linked

```
{
  "bnpl": {
    "all": {
      "Lazypay": {
        "status": 1,
        "kfsLink": "https://www.somekfsLink.com",
        "eligible": true,
        "customerLinked": false
      }
    }
  }
}
```

- Customer not eligible

```
{
  "Lazypay": {
    "status": 1,
    "eligible": false, // based on amount and not to return available balance if eligible is false
    "customerLinked": false,
    "failure_code": "E2408",
    "failure_reason": "The transaction or loan amount is greater than the available credit line with the customer"
  }
}
```