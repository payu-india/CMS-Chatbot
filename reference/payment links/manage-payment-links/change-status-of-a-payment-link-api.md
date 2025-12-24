---
title: Change Status or Expiry for a Payment Link API
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
This API is used to update a payment link's status and expiry date.

HTTP Method: **PUT**

**Environment**

|                            |                                                                                       |
| -------------------------- | ------------------------------------------------------------------------------------- |
| **Test Environment**       | \<[https://uatoneapi.payu.in/payment-links](https://uatoneapi.payu.in/payment-links)> |
| **Production Environment** | \<[https://oneapi.payu.in/payment-links](https://oneapi.payu.in/payment-links)>       |

> 📘 Note:
>
> The access token with the scope as **update_payment_links** is required on the header. For more information on getting the access token, refer to [Get Access Token](ref:get-token-api-for-payment-links).

## Path parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameters</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>ID<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter must contain the payment link invoice number.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>INV8446471886220</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Request headers

| Parameter                 | Description                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| mid`  mandatory`          | `String` This contains the merchant identifier.                                                                                                   |
| Authorization` mandatory` | Bearer `String` This contains the client_token. For more information, refer to [Get Token API - Payment Links](ref:get-token-api-payment-links) . |

## Request parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameters</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>ID<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter must contain the payment link invoice number.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>INV8446471886220</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>subAmount<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter must contain the payment sub amount.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>100.00</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>tax<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter must contain the tax amount for the transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1.00</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>shippingCharge<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter must contain the shipping charge.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>10.00</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>isPartialPaymentAllowed<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> This parameter includes whether partial payment is allowed.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>false</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>active<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> This parameter includes whether the payment link is active.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>true</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>expiry<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter must contain the expiry date.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2024-04-01</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>udf<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON</code>This parameter contains the following UDF parameters in a JSON format as in the example:  </p>
<ul>
<li>udf1	</li>
<li>udf2	</li>
<li>udf3	</li>
<li>udf4	</li>
<li>udf5</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{<br>&quot;udf1&quot;: &quot;string&quot;,<br>&quot;udf2&quot;: &quot;string&quot;,<br>&quot;udf3&quot;: &quot;string&quot;,<br>&quot;udf4&quot;: &quot;string&quot;,<br>&quot;udf5&quot;: &quot;string&quot;<br>}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>userToken<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This parameter must contain the payment link creation from date.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2023-04-01</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>address<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON</code>This parameter must contain the address details in a JSON format as in the example.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{<br>&quot;line1&quot;: &quot;string&quot;,<br>&quot;line2&quot;: &quot;string&quot;,<br>&quot;city&quot;: &quot;string&quot;,<br>&quot;state&quot;: &quot;string&quot;,<br>&quot;country&quot;: &quot;string&quot;,<br>&quot;zipCode&quot;: &quot;string&quot;<br>}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>reminder<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON</code>This parameter must contain the following reminder details in a JSON format (as in the example):  </p>
<ul>
<li>scheduledAt: The time at the which the reminder was scheduled.</li>
<li>channels: The channels used to send the reminder.</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{<br>&quot;id&quot;: 0,<br>&quot;scheduledAt&quot;: &quot;string&quot;,<br>&quot;channels&quot;: [mobile]<br>}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>customAttributes<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON</code>This parameter must contain the  custom attributes in a JSON format as in the example.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{<br>&quot;customAttributeId&quot;: 0,<br>&quot;entityType&quot;: &quot;string&quot;,<br>&quot;toolId&quot;: 0,<br>&quot;customAttributeName&quot;: &quot;string&quot;,<br>&quot;attributeType&quot;: &quot;string&quot;,<br>&quot;options&quot;: [],<br>&quot;checked&quot;: true,<br>&quot;required&quot;: true<br>}</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

```curl
curl --location --request PUT 'https://uatoneapi.payu.in/payment-links/INV1406204187' \
--header 'merchantId: 5018363' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer 010c57cc96af33b84b2de81ee8c30b6f99a1976e74c2bd3fb5f4e5b535f25ae8' \
--header 'Cookie: PHPSESSID=7nv3d144qeh7g102p3uau1o6pm' \
--data '{
"active":false
}'

```

## Sample response

### Success scenario

```json
{
  "status": 0,
  "message": "string",
  "result": {},
  "errorCode": 170,
  "guid": "f529e375-739f-4c8a-b5f5-0e67fa3f533f"
}
```

### Failure scenario

```json
{
  "status": -1,
  "message": "expiry cannot be less than the current date",
  "result": null,
  "errorCode": null,
  "guid": null
}
```
