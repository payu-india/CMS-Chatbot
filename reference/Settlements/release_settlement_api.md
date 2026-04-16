---
title: Release Settlement API
excerpt: 'API Command: **release\_settlement**'
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The** Release Settlement** API is used to flag the sub-payment you want to settle; after adding splits for a particular payment, the money will not be settled directly into the child merchants account unless you call a release event corresponding to the individual suborder you want to settle.

**Use Case**: Most marketplace model owners wait for the delivery or dispatch to happen first from the sub-seller’s end. Only after the successful dispatch, the owner will release the funds into the sub-seller’s bank account. This API gives them the flexibility to do so.

The Release Settlement API can be used to release the settlement of all the blocked child transactions in the aggregator workflow.

HTTP Method: **POST**

**Environment**

|                        |                                                                     |
| :--------------------- | :------------------------------------------------------------------ |
| Test Environment       | \<[https://test.payu.in/merchant/](https://test.payu.in/merchant/)> |
| Production Environment | \<[https://info.payu.in/merchant/](https://info.payu.in/merchant/)> |

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>varchar</code> The merchant key is included in this parameter.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Your Test Key</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>command<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>varchar</code> The <strong>release_settlement</strong> must be included in this parameter</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>release_settlement</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>hash<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>varchar</code> The hash string encryption is specified in this parameter.<br>The format of the hash is:<br>string key|command|var1|salt<br>Where var1 is your mihpayuid</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var1<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>varchar</code> The mihpayuId is specified in this parameter</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>8000123</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var2<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>varchar</code> The childMid is specified in this parameter.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>393437</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2"
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
"key=A****r&command=release_settlement&var1=8000123&var2=8000123&hash=6692a8b560c51e8a4bb830206d3b8fac3678fb5b0844"
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>status</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The status can contain any of the following values:  </p>
<ul>
<li>Status will be 1 if API call is a success  </li>
<li>Status will be 0 in case of failure you&#39;ll get system handled failure reasons in this case</li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>msg</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Message string for both success and failure cases. </p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample Response

### Success Scenario

* Successful Transaction

Sample Success Response for Release Settlement

```json
{"status":0,"msg":"Release request is accepted"}
```

## Failure Scenarios

* Failure Response when PayU ID is empty

Failure Response when PayUID is empty

```json
{"status":1,"msg":"payuId is empty"}
```

* Failure response when child merchant ID is empty

Failure response when child merchant ID is empty

```json
{"status":1,"msg":"Mid passed is empty"}
```

* Failure Response when child merchant ID and PayU ID do not match

Failure Response when child merchant ID and PayU ID do not match

```json
{"status":1,"msg":"Invalid childMid and payuId"}
```

* Failure response when attempting to release an already released sub-payment

Failure response when attempt to release an already released sub- payment

```json
{"status":1,"msg":"Release request is already accepted"}
```