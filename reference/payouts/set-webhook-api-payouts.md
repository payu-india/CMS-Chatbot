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
| **Production Environment** | <https://payout.payumoney.com/payout/v2/webhook> |
| **Test Environment**       | <https://uatoneapi.payu.in/payout/v2/webhook/>   |

## Request header parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "Authorization`\nmandatory`",
    "0-1": "`String` Specify the access token generated earlier in this parameter.",
    "0-2": "Bearer {access\\_token}",
    "1-0": "payoutMerchantId`\nmandatory`",
    "1-1": "`String` Specify the payout merchant id provided while onboarding or creating Payout account.",
    "1-2": "1111126",
    "2-0": "Content-Type  \n`mandatory`",
    "2-1": "`String` Indicates the format in which the request is sent.",
    "2-2": "application/json"
  },
  "cols": 3,
  "rows": 3,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


> 📘 Note:
> 
> The **pid** is **payoutMerchantId**, however it is different from the PayU merchant id. Check the Payouts Dashboard or call the PayU Customer Support if you don’t know your **payoutsMerchantID**.

## Request Parameters

| **Parameter**                   | **Description**                                                                                                                                                                         | **Example**        |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| webhook` mandatory`             | Configure the webhooks for different type of events. The event can be any of the following:                                                                                             | transfer\_reversed |
| values.url` mandatory`          | This is the post URL of the API where the merchant will listen to PayU events. In other words, this is the webhook URL.                                                                 |                    |
| values.authorization` optional` | Merchant can provide this value which will be sent in the header while pushing the payouts event to the merchant.Using this merchant can authenticate that request is coming from PayU. |  ##                |

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