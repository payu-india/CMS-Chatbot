---
title: Fetch Merchant Downtime Information
excerpt: Get the merchant downtime information
deprecated: false
hidden: true
metadata:
  robots: index
---
Use this endpoint to retrieve merchant-specific downtime information. The response includes downtime details for entities associated with the specified merchant.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /v2/payments/merchant/downtime
  </Card>
</Cards>

## Environment

<V2_payment_envrionment />

## Sample Request

```curl
curl -X POST 'https://info.payu.in/v2/payments/merchant/downtime' \
  -H 'Content-Type: application/json' \
  -H "date: {{date}}" \
  -H "authorization: {{authorization}}" \
  -d '{
  "from":"2026-03-22 00:00:00",
  "to":"2026-03-24 23:59:59",
  "categories":[
    "upi"
  ],
  "page":2,
  "per_page":25
}'
```

## Sample Response

```json Success Response
{
  "merchant_id":12965582,
  "categories":[
    "upi",
    "nb"
  ],
  "from":"2026-02-20T00:00:00+05:30",
  "to":"2026-03-25T02:59:59+05:30",
  "count":2,
  "page":1,
  "per_page":50,
  "total_pages":1,
  "downtimes":[
    {
      "entity_name":"MEBIGO LABS PRIVATE LIMITED(12965582)-HDFCU SI(283)",
      "entity_type":"merchant_id-pg_id",
      "method":"upi",
      "started_at":"2026-03-24T18:33:59+05:30",
      "ended_at":"2026-03-24T18:37:59+05:30",
      "status":"recovered",
      "instrument":{
        "merchant_id":"MEBIGO LABS PRIVATE LIMITED",
        "pg_id":"HDFCU SI"
      },
      "summary":{
        "duration_minutes":4.0,
        "failed_count":347,
        "success_rate_during_downtime":6.72,
        "srt_drop_rel":78.52,
        "severity":"LOW"
      }
    },
    {
      "entity_name":"MEBIGO LABS PRIVATE LIMITED(12965582)-SI",
      "entity_type":"merchant_id-mode",
      "method":"upi",
      "started_at":"2026-03-24T14:01:59+05:30",
      "ended_at":"2026-03-24T14:17:59+05:30",
      "status":"recovered",
      "instrument":{
        "merchant_id":"MEBIGO LABS PRIVATE LIMITED",
        "mode":"SI"
      },
      "summary":{
        "duration_minutes":16.0,
        "failed_count":8521,
        "success_rate_during_downtime":1.21,
        "srt_drop_rel":93.66,
        "severity":"HIGH"
      }
    }
  ]
}
```
```json Error Response
{
  "error": "merchant_id is invalid"
}
```

## Request Headers

<V2_payment_header_params />

## Request Parameters

| **Parameter**                                            | **Description**                                                                                                                                                                                                                                                            |
| :------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **from**<sup style={{color: 'red'}}>*</sup>              | `string` \| `number` The start timestamp. Refer to the time format and validation rules section for format and validation information.                                                                                                                                     |
| **txnId**<sup style={{color: 'red'}}>*</sup>             | `string` Transaction ID for transaction tracking and this must be unique for every transaction. For example `REF123456`.                                                                                                                                                   |
| **paymentMethod**<sup style={{color:'red'}}>*</sup>      | `object` Details about the payment method used. Parameters are described in the [paymentMethod Object](https://docs.payu.in/v2/reference/generate-upi-qr#paymentmethod-object) section.                                                                                    |
| **order**<sup style={{color:'red'}}>*</sup>              | `object` Details about the transaction order including product information, ordered items, user-defined fields, and payment charge specifications. Parameters are described in the [order Object](https://docs.payu.in/v2/reference/generate-upi-qr#order-object) section. |
| **additionalInfo**<sup style={{color:'red'}}>*</sup>     | `object` Additional information including UPI-specific parameters like VPA. Parameters are described in the [additionalInfo Object](https://docs.payu.in/v2/reference/generate-upi-qr#additionalinfo-object) section.                                                      |
| **callBackActions**<sup style={{color:'red'}}>*</sup>    | `object` Actions to perform on the payment server in different scenarios. Parameters are described in the [callBackActions Object](https://docs.payu.in/v2/reference/generate-upi-qr#callbackactions-object) section.                                                      |
| **omniChannelDetails**<sup style={{color:'red'}}>*</sup> | `object` The omnichannel details. Parameters are described in the [omniChannelDetails Object](https://docs.payu.in/v2/reference/generate-upi-qr#omnichanneldetails-object) section.                                                                                        |
| **billingDetails**<sup style={{color:'red'}}>*</sup>     | `object` Billing details of the customer including name, address, phone number, email, and so on. Parameters are described in the [billingDetails Object](https://docs.payu.in/v2/reference/generate-upi-qr#billingdetails-object) section.                                |
