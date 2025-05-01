---
title: Fetch Masked VPAs API
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
The **fetchMaskedVpa** API is used to fetch the list of masked UPI IDs against any mobile number.

HTTP Method: **POST**

**Environment**

|                            |                                                              |
| -------------------------- | ------------------------------------------------------------ |
| **Test Environment**       | &lt;https://uatoneapi.payu.in/payout/payment/fetchMaskedVpa&gt; |
| **Production Environment** | &lt;https://payout.payumoney.com/payout/payment/fetchMaskedVpa&gt; |

## Header parameters

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Authorization<code> mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Specify the access token generated during authentication in this parameter.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Bearer <code>{access_token}</code></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>payoutMerchantId<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Specify the merchant ID provided while onboarding for Payouts in this parameter.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1111126</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Content-Type<code> mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Indicates the format in which the request is sent.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>application/x-www-form-urlencoded</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

> 📘 Note:
> 
> The payoutMerchantId is different from PayU Merchant Id. Check the Payouts Dashboard or call the PayU Customer Support if you don’t know your payoutMerchantId.

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>mobileNumber<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Indicates the mobile number of the beneficiary</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>9999999999</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

```
curl --location --request GET 'https://test.payumoney.com/payout/payment/fetchMaskedVpa?mobileNumber=1234567890' \
--header 'Authorization: Bearer 0f8188bfdf6ff8c630376c63497f3745ff3e21b9dfdc9a4955b4561cec9bb05e' \
--header 'payoutMerchantId: 2222740' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: Path=/; Path=/' \
--data-urlencode 'mobileNumber=1234567890'
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter returns the status of web service call. The status can be any of the following:<br>   -** 0** - If web service call succeeded<br>   -**  1** - If web service call failed</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>msg</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter returns the success or failure message.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>code</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter returns the error code if the API failed to verify or invalid details.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>data</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter returns the saved card details in a JSON format. For more information, refer to the next table.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### Description of data JSON fields

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>result</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The version of the results displayed for this API.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>VPA ID</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field returns the following details in an array format:  </p>
<ul>
<li><strong>Token</strong>: The token for the VPA. For example, &quot;13e3a8caa1ede3c56a524&quot;  </li>
<li><strong>name</strong>: The name of the account holder.<br>- <strong>App_Name</strong>: The name of the UPI provider through which the UPI is used by beneficiary. For example, Google Pay</li>
</ul>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample response

- Success response

```
{
    "status": 0,
    "msg": null,
    "code": null,
    "data": {
        "result": 1.0,
        "9x1x3x5x8x@okaxis": {
            "Token": "13e3a8caa1ede3c56a524",
            "name": "",
            "App_Name": "Google Pay"
        },
        "9x3x5x0x9x@ybl": {
            "Token": "291dc5886ed5a13f50ccd",
            "name": "Sajan Bhadrike ",
            "App_Name": "PhonePe"
        }
    }
}
```

- Failure response
- ```
  {
      "status": 0,
      "msg": null,
      "code": null,
      "data": null
  }
  ```