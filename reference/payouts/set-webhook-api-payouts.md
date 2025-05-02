---
title: Set Webhook API - Payouts
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
You can configure webhooks using PayU Dashboard too. For more information, check PayU Dashboard. This section describes how to configure the webhook URL using API.

|                            |                                                  |
| -------------------------- | ------------------------------------------------ |
| **Production Environment** | &lt;https://payout.payumoney.com/payout/v2/webhook&gt; |
| **Test Environment**       | &lt;https://uatoneapi.payu.in/payout/v2/webhook/&gt;   |

## Request header parameters

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Specify the access token generated earlier in this parameter.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Bearer <code>{access_token}</code></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>payoutMerchantId<code> mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Specify the payout merchant id provided while onboarding or creating Payout account.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1111126</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Content-Type<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Indicates the format in which the request is sent.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>application/json</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

> 📘 Note:
> 
> The **pid** is **payoutMerchantId**, however it is different from the PayU merchant id. Check the Payouts Dashboard or call the PayU Customer Support if you don’t know your **payoutsMerchantID**.

## Request Parameters

| **Parameter**                   | **Description**                                                                                                                                                                         | **Example**        |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| webhook` mandatory`             | Configure the webhooks for different type of events. The event can be any of the following:                                                                                             | transfer\_reversed |
| values.url` mandatory`          | This is the post URL of the API where the merchant will listen to PayU events. In other words, this is the webhook URL.                                                                 |                    |
| values.authorization` optional` | Merchant can provide this value which will be sent in the header while pushing the payouts event to the merchant.Using this merchant can authenticate that request is coming from PayU. |  ##

## Sample request

```
curl --location 'https://uatoneapi.payu.in/payout/v2/webhook' \

--header 'payoutMerchantId: 2xxx79' \

--header 'Content-Type: application/json' \

--header 'Authorization: Bearer 2a641dc44dc488360xxxxxxxxxx19292bce79d341169b67a' \

--data '[

  {

    "webhook" :"default",

     "values": {

                  "url":"https://webhook/443cc175-9aab-44c56d-33157a71cb63",

                  "authorization":"asjafya56%^eyy63547ysrt4"

               }

   }

]'
```

> 📘 Notes:
> 
> - You ned to whitelist PayU for a server call to your webhook API.
> - **Set Webhook API** that you had created should be of type as **POST**

## Sample response

- Success scenario

```
{
 "status": 0,
 "msg": "Webhook saved successfully",
 "code": null,
 "data": null
 }
```

- Failure scenario

```
{
 "status": 1,
 "msg": "Webhook url is invalid",
 "code": 20407,
 "data": null
 }
```