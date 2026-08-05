---
title: Register Webhooks API to Get Real-Time Merchant Status
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
Partners need to register their webhooks using the Register Webhooks API with hub token and webhook URL.

**Environment**

|            |                                                                |
| :--------- | :------------------------------------------------------------- |
| Test       | \<https://uat-partner.payu.in/api/v1/partners/register_webhook> |
| Production | \<https://partner.payu.in/api/v1/partners/register_webhook>     |

## Request header

> 📘 Note:
>
> The access token with the **scope** as **refer\_merchant** is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).

| Authorization | Bearer `{{access_token}}`           |
| :------------ | :-------------------------------- |
| Content-Type  | application/x-www-form-urlencoded |

## Request parameters

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>webhook_url<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter must contain the Webhooks URL to which the status must be notified.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>reseller_uuid<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter must contain the reseller UUID.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

```curl
curl --location --request POST 'https://uat-partner.payu.in/api/v1/partners/register_webhook' \
--header 'Authorization: Bearer 169e576ee0794085e48f0de683bc39563c43c9493f23867e1c53481bdaa9cada' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'webhook_url=https://www.payu.in' \
--data-urlencode 'reseller_uuid=83fe-eb64-021844d8-9397-26535b1bf0c2'
```

## Sample response

```
{
    "message": "Webhook Successfully Registered"
}
```