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

<Callout icon="📘" theme="info">
  **Mandatory Parameters**

  Parameters marked with <sup style={{color: 'red'}}>*</sup> are mandatory.
</Callout>

| **Parameter**                               | **Description**                                                                                                                                                                                                                                                                                                       |
| :------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **from**<sup style={{color: 'red'}}>*</sup> | `string` \| `number` The start timestamp. Refer to the time format and validation rules section for format and validation information.                                                                                                                                                                                |
| **to**<sup style={{color: 'red'}}>*</sup>   | `string` \| `number` The end timestamp. Refer to the time format and validation rules section for format and validation information.                                                                                                                                                                                  |
| **categories**                              | `object` \| `string` Represents the downtime category. If the value is not passed, no category filter is applied. Possible values: <ul><li>`upi`</li> <li>`nb`</li> <li>`cards`</li> <li>`emi`</li></ul> Accepted formats: <ul><li>Array: `["upi", "cards"]`</li> <li>`Comma-separated string: "upi,cards"`</li></ul> |
| **page**                                    | `number` The page number used for pagination. Defaults to `1`.                                                                                                                                                                                                                                                        |
| **per_page**                                | `number` Items displayed per page. Defaults to 50. The maximum items per page is 100.                                                                                                                                                                                                                                 |

### Time Format and Validation Rules

<Accordion title="Supported Input Formats of from and to Parameters" icon="fa-info-circle">
  | **Format**            | **Example**            |
  | :-------------------- | :--------------------- |
  | `YYYY-MM-DD HH:MM:SS` | `2026-03-25 10:30:00`  |
  | ISO8601 with time     | `2026-03-25T10:30:00Z` |
  | Unix epoch (number)   | `1715769600`           |
  | Unix epoch (string)   | "`1715769600`"         |

  **Validation rules:**

  * `from` and `to` values must include time granularity (seconds) unless epoch is used.
  * The `from` value must be before the `to` value.
  * The `from` value must be within the last 3 months.
  * The `to` value must not be greater than the current server time.
</Accordion>

## Response Parameters

| **Parameter**   | **Description**                                                                                 |
| --------------- | ----------------------------------------------------------------------------------------------- |
| **merchant_id** | `number` The unique merchant identifier.                                                        |
| **categories**  | `array` The applied category filters.                                                           |
| **from**        | `string` The start time of the downtime in the ISO8601 format.                                  |
| **to**          | `string` The end time of the downtime in the ISO8601 format.                                    |
| **count**       | `number` The total count of matching downtimes.                                                 |
| **page**        | `number` The current page number of the received response.                                      |
| **per_page**    | `number` The total number of items displayed per page.                                          |
| **total_pages** | `number` The total number of pages the response contains.                                       |
| **downtimes**   | `array` The array of downtime objects. Parameters are described in the Downtime Object section. |
| **summary**     | `array` The downtime summary details. Parameters are described in the Summary Object section.   |

### Downtime Object

<Accordion title="My Accordion Title" icon="fa-table">
  Lorem ipsum dolor sit amet, **consectetur adipiscing elit.** Ut enim
  ad minim veniam, quis nostrud exercitation ullamco. Excepteur sint
  occaecat cupidatat non proident!
</Accordion>
