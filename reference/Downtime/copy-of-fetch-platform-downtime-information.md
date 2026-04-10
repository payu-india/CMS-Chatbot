---
title: Fetch Scheduled Maintenance Activities Information
excerpt: >-
  Retrieve scheduled maintenance activity details using the PayU API. Access
  upcoming and past maintenance schedules across payment systems with
  customizable date ranges and filters.
deprecated: false
hidden: true
metadata:
  title: Scheduled Maintenance API | PayU Developer Documentation
  description: >-
    Retrieve platform-level downtime information using the PayU API. Fetch
    real-time and historical downtime data across all payment entities with
    flexible date range and filtering options.
  keywords:
    - PayU maintenance API
    - scheduled maintenance API
    - fetch maintenance activities
    - payment gateway maintenance schedule
    - PayU API maintenance updates
    - platform maintenance API
    - payment system maintenance data
    - API for maintenance tracking
    - scheduled downtime API
    - payment service maintenance status
    - PayU developer API
    - maintenance notification API
    - transaction maintenance data
    - payment infrastructure maintenance
  robots: noindex
---
Use this endpoint to retrieve scheduled maintenance activity information. The response includes details of maintenance activities that overlap with the given time range.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /v2/payments/platform/downtime
  </Card>
</Cards>

## Environment

| **Environment** | **URL**                                                              |
| :-------------- | :------------------------------------------------------------------- |
| **Production**  | [https://info.payu.in/v2/payments](https://info.payu.in/v2/payments) |

## Sample Request

```curl
curl -X POST 'https://info.payu.in/v2/payments/platform/downtime' \
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
  "downtime_type":"platform",
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
      "entity_name":"TEST UPI(123)",
      "entity_type":"pg_id",
      "method":"upi",
      "started_at":"2026-03-25T02:52:00+05:30",
      "ended_at":"2026-03-25T02:56:00+05:30",
      "status":"recovered",
      "instrument":{
        "pg_id":"TEST UPI"
      },
      "severity":"LOW"
    },
    {
      "entity_name":"@ybl",
      "entity_type":"vpa_handle",
      "method":"upi",
      "started_at":"2026-03-25T01:02:00+05:30",
      "ended_at":"2026-03-25T01:16:00+05:30",
      "status":"recovered",
      "instrument":{
        "vpa_handle":"@ybl"
      },
      "severity":"LOW"
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

| **Parameter**                               | **Description**                                                                                                                                                                                                                                                                                                      |
| :------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **from**<sup style={{color: 'red'}}>*</sup> | `string` \| `number` The start timestamp. Refer to the [Time Format and Validation Rules section](/reference/fetch-merchant-downtime-information#time-format-and-validation-rules) for format and validation information.                                                                                            |
| **to**<sup style={{color: 'red'}}>*</sup>   | `string` \| `number` The end timestamp. Refer to the [Time Format and Validation Rules section](/reference/fetch-merchant-downtime-information#time-format-and-validation-rules)  for format and validation information.                                                                                             |
| **categories**                              | `array` \| `string` Represents the downtime category. If the value is not passed, no category filter is applied. Possible values: <ul><li>`upi`</li> <li>`nb`</li> <li>`cards`</li> <li>`emi`</li></ul> Accepted formats: <ul><li>Array: `["upi", "cards"]`</li> <li>Comma-separated string: `"upi,cards"`</li></ul> |
| **page**                                    | `number` The page number used for pagination. Defaults to `1`.                                                                                                                                                                                                                                                       |
| **per_page**                                | `number` Items displayed per page. Defaults to `50`. The maximum items per page is `100`.                                                                                                                                                                                                                            |

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

| **Parameter**     | **Description**                                                                                                                                                   |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **downtime_type** | `number` The downtime type. Here it is `platform` always.                                                                                                         |
| **categories**    | `array` The applied category filters.                                                                                                                             |
| **from**          | `string` The start time of the downtime in the ISO8601 format.                                                                                                    |
| **to**            | `string` The end time of the downtime in the ISO8601 format.                                                                                                      |
| **count**         | `number` The total count of matching downtimes.                                                                                                                   |
| **page**          | `number` The current page number of the received response.                                                                                                        |
| **per_page**      | `number` The total number of items displayed per page.                                                                                                            |
| **total_pages**   | `number` The total number of pages the response contains.                                                                                                         |
| **downtimes**     | `array` The array of downtime objects. Parameters are described in the [Downtime Object](/reference/fetch-merchant-downtime-information#downtime-object) section. |

### Downtime Object

<Accordion title="Parameters and Description" icon="fa-table">
  | **Parameter**    | **Description**                                                                                         |
  | :--------------- | :------------------------------------------------------------------------------------------------------ |
  | **entity\_name** | `string` The complete entity name with identifiers.                                                     |
  | **entity\_type** | `string` The entity type. For example `merchant_id-pg_id`, `merchant_id-mode`, and `bank`               |
  | **method**       | `string` The payment method or category. For example `upi`                                              |
  | **started\_at**  | `string` The start time of the downtime in the ISO8601 format.                                          |
  | **ended\_at**    | `string` The end time of the downtime in the ISO8601 format.                                            |
  | **status**       | `string` The downtime status. Possible values: <ul><li>`ongoing`</li> <li>`recovered`</li></ul>         |
  | **instrument**   | `object` The entity part details.                                                                       |
  | **severity**     | `string` The severity level: Possible values: <ul><li>`LOW`</li> <li>`MEDIUM`</li> <li>`HIGH`</li></ul> |
</Accordion>

## Error Response Parameters

| **Error**                                      | **Description**                                                                                                                                     | **Solution**                                                                                                                                  |
| :--------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| `Invalid JSON: ...`                            | This error occurs when the json is invalid.                                                                                                         | Make sure the json is valid.                                                                                                                  |
| `Unknown parameters: ...`                      | This error occurs when you pass unknown parameters.                                                                                                 | Make sure to pass valid parameters.                                                                                                           |
| `from is required`                             | This error occurs when you do not pass the `from` parameter value.                                                                                  | The `from` is mandatory parameter. Ensure to pass the value.                                                                                  |
| `to is required`                               | This error occurs when you do not pass the `to` parameter value.                                                                                    | The `to` is mandatory parameter. Ensure to pass the value.                                                                                    |
| `from must include time as HH:MM:SS (...)`     | This error occurs when the `from` parameter value format is invalid.                                                                                | Make sure to pass the `from` parameter value in the valid format. Refer to the Time Format and Validation Rules section for more information. |
| `to must not be greater than the current time` | This error occurs when the timestamp of the `to` parameter is a past time.                                                                          | Ensure the `to` parameter timestamp is greater than the current time.                                                                         |
| `from must be within the last 3 months`        | This error occurs when the timestamp of the `from` parameter is greater than 3 months.                                                              | Make sure the `from` timestamp is less than 3 months.                                                                                         |
| `from must be before to`                       | This error occurs when the `from` timestamp exceeds the `to` timestamp.                                                                             | Make sure the `from` timestamp is within the `to` timestamp.                                                                                  |
| `categories must be from: upi, nb, cards, emi` | This error occurs when the category value is other than the following values: <ul><li>`upi`</li> <li>`nb`</li> <li>`cards`</li> <li>`emi`</li></ul> | Make sure the category value is any of the following values: <ul><li>`upi`</li> <li>`nb`</li> <li>`cards`</li> <li>`emi`</li></ul>            |
