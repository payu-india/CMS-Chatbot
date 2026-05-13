---
title: Fetch Scheduled Maintenance Activities Information
excerpt: >-
  Retrieve scheduled maintenance activity details using the PayU API. Access
  upcoming and past maintenance schedules across payment systems with
  customizable date ranges and filters.
deprecated: false
hidden: false
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
    /v2/payments/platform/maintenance
  </Card>
</Cards>

## Environment

| **Environment** | **URL**                                                              |
| :-------------- | :------------------------------------------------------------------- |
| **Production**  | [https://info.payu.in/v2/payments](https://info.payu.in/v2/payments) |

## Sample Request

```curl
curl -X POST 'https://info.payu.in/v2/payments/platform/maintenance' \
  -H 'Content-Type: application/json' \
  -H "date: {{date}}" \
  -H "authorization: {{authorization}}" \
  -d '{
  "from":"2026-03-01 00:00:00",
  "to":"2026-03-31 23:59:59",
  "page":2,
  "per_page":25
}'
```

## Sample Response

```json Success Response
{
  "from":"2026-02-20T00:00:00+05:30",
  "to":"2026-03-25T02:59:59+05:30",
  "count":20,
  "page":1,
  "per_page":50,
  "total_pages":1,
  "scheduled_maintenances":[
    {
      "id":"2af74f94-9005-4e15-9d74-2e0a01c91b87",
      "activity_name":"SBI NB",
      "description":"Impact:- SBI NB txns will be impacted during an activity.",
      "activity_status":"completed",
      "activity_date":"2026-03-20T01:45:00+05:30",
      "activity_end_time":"2026-03-20T03:15:00+05:30",
      "window_end_at":"2026-03-20T03:15:00+05:30",
      "downtime_duration_minutes":90,
      "manual_impact_entries":[
        
      ],
      "impacted_entities":[
        {
          "entity_name":"SBINB",
          "entity_type":"ibibo_code",
          "entity_category":"nb"
        }
      ]
    },
    {
      "id":"d65cb551-c544-4b5b-9bcb-9b535a7e6c1d",
      "activity_name":"TEST UPI",
      "description":"Scheduled Maintenance Activity for TEST UPI",
      "activity_status":"completed",
      "activity_date":"2026-03-16T22:00:00+05:30",
      "activity_end_time":"2026-03-17T06:00:00+05:30",
      "window_end_at":"2026-03-17T06:00:00+05:30",
      "downtime_duration_minutes":480,
      "manual_impact_entries":[
        
      ],
      "impacted_entities":[
        {
          "entity_name":"TEST UPI(123)",
          "entity_type":"pg_id",
          "entity_category":"upi"
        }
      ]
    },
    {
      "id":"aff33ad9-1d4e-4518-9154-9ede65258bca",
      "activity_name":"Scheduled Maintenance Activity",
      "description":"TEST2 UPI maintenance",
      "activity_status":"completed",
      "activity_date":"2026-03-15T00:01:00+05:30",
      "activity_end_time":"2026-03-15T01:00:00+05:30",
      "window_end_at":"2026-03-15T01:00:00+05:30",
      "downtime_duration_minutes":59,
      "manual_impact_entries":[
        "hdfcupi"
      ],
      "impacted_entities":[
        
      ]
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

| **Parameter**                               | **Description**                                                                                                                                                                                                           |
| :------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **from**<sup style={{color: 'red'}}>*</sup> | `string` \| `number` The start timestamp. Refer to the [Time Format and Validation Rules section](/reference/fetch-merchant-downtime-information#time-format-and-validation-rules) for format and validation information. |
| **to**<sup style={{color: 'red'}}>*</sup>   | `string` \| `number` The end timestamp. Refer to the [Time Format and Validation Rules section](/reference/fetch-merchant-downtime-information#time-format-and-validation-rules)  for format and validation information.  |
| **page**                                    | `number` The page number used for pagination. Defaults to `1`.                                                                                                                                                            |
| **per_page**                                | `number` Items displayed per page. Defaults to `50`. The maximum items per page is `100`.                                                                                                                                 |

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
  * The `to` value can be set up to 1 month from the current date.
</Accordion>

## Response Parameters

| **Parameter**              | **Description**                                                                                                                                                               |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **from**                   | `string` The start time of the downtime in the ISO8601 format.                                                                                                                |
| **to**                     | `string` The end time of the downtime in the ISO8601 format.                                                                                                                  |
| **count**                  | `number` The total count of matching downtimes.                                                                                                                               |
| **page**                   | `number` The current page number of the received response.                                                                                                                    |
| **per_page**               | `number` The total number of items displayed per page.                                                                                                                        |
| **total_pages**            | `number` The total number of pages the response contains.                                                                                                                     |
| **scheduled_maintenances** | `array` The array of maintenance activity objects. Parameters are described in the [Downtime Object](/reference/fetch-merchant-downtime-information#downtime-object) section. |

### Scheduled Maintenance Object

<Accordion title="Parameters and Description" icon="fa-table">
  | **Parameter**                   | **Description**                                                                                                                                                                                                                                                                                       |
  | :------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | **id**                          | `string` The unique identifier (UUID) of the scheduled maintenance.                                                                                                                                                                                                                                   |
  | **activity\_name**              | `string` The Name of the maintenance activity.                                                                                                                                                                                                                                                        |
  | **description**                 | `string` The detailed description of the activity.                                                                                                                                                                                                                                                    |
  | **activity\_status**            | `string` The activity status. Possible values: <ul><li>`scheduled`: Activity is planned but not yet started</li> <li>`active`: Activity is currently in progress</li> <li>`completed`: Activity has been completed</li> <li>`extended`: Activity has been extended beyond original end time</li></ul> |
  | **activity\_date**              | `string` The scheduled start date of the activity in the ISO8601 format.                                                                                                                                                                                                                              |
  | **activity\_end\_time**         | `string` The scheduled end time of the activity in the ISO8601 format.                                                                                                                                                                                                                                |
  | **window\_end\_at**             | `string` The maintenance window end time in the ISO8601 format.                                                                                                                                                                                                                                       |
  | **downtime\_duration\_minutes** | `array` The manually added impact entries.                                                                                                                                                                                                                                                            |
  | **manual\_impact\_entries**     | `array` The expected downtime duration in minutes.                                                                                                                                                                                                                                                    |
  | **impacted\_entities**          | `array` The array of impacted entity objects. Parameters are described in the Impacted Entity Object section.                                                                                                                                                                                         |
</Accordion>

#### Impacted Entity Object

<Accordion title="Parameters and Description" icon="fa-info-circle">
  | **Parameter**        | **Description**                                                                                                       |
  | :------------------- | :-------------------------------------------------------------------------------------------------------------------- |
  | **entity\_name**     | `string` The name of the impacted entity.                                                                             |
  | **entity\_type**     | `string` The type of entity. For example,  `pg_id`, `ibibo_code`, `issuing_bank`.                                     |
  | **entity\_category** | `string` The entity category. Possible values: <ul><li>`upi`</li> <li>`nb`</li> <li>`cards`</li> <li>`null`</li></ul> |
</Accordion>

## Error Response Parameters

| **Error**                                      | **Description**                                                                                           | **Solution**                                                                                                                                  |
| :--------------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| `Invalid JSON: ...`                            | This error occurs when the json is invalid.                                                               | Make sure the json is valid.                                                                                                                  |
| `Unknown parameters: ...`                      | This error occurs when you pass unknown parameters.                                                       | Make sure to pass valid parameters.                                                                                                           |
| `from is required`                             | This error occurs when you do not pass the `from` parameter value.                                        | The `from` is mandatory parameter. Ensure to pass the value.                                                                                  |
| `to is required`                               | This error occurs when you do not pass the `to` parameter value.                                          | The `to` is mandatory parameter. Ensure to pass the value.                                                                                    |
| `from must include time as HH:MM:SS (...)`     | This error occurs when the `from` parameter value format is invalid.                                      | Make sure to pass the `from` parameter value in the valid format. Refer to the Time Format and Validation Rules section for more information. |
| `to must not be greater than 1 month from now` | This error occurs when the timestamp of the `to` parameter is greater than 1 month from the current time. | Ensure the `to` parameter timestamp is less than 1 month from the current time.                                                               |
| `from must be within the last 3 months`        | This error occurs when the timestamp of the `from` parameter is greater than 3 months.                    | Make sure the `from` timestamp is less than 3 months.                                                                                         |
| `from must be before to`                       | This error occurs when the `from` timestamp exceeds the `to` timestamp.                                   | Make sure the `from` timestamp is within the `to` timestamp.                                                                                  |
