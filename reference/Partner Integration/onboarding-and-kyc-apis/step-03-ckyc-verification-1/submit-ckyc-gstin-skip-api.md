---
title: Skip CKYC & GSTIN API
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
## Overview

The Submit CKYC & GSTIN Skip API records a consent for an existing merchant onboarding record. Use it when a partner needs to submit a named onboarding or verification consent for a merchant identified by its PayU UUID.

The request accepts one or more consent objects. Each object identifies the consent by `name` and associates it with the partner that provided it through `provided_by_uuid`.

## Authentication

Authenticate each request with an access token in the `Authorization` header:

```http
Authorization: Bearer <BEARER_TOKEN>
```

The bearer token must include the `refer_merchant` scope. Keep the token confidential and do not embed it in client-side code or commit it to source control.

## Endpoints

| Environment | Base URL                      |
| ----------- | ----------------------------- |
| UAT         | `https://uat-partner.payu.in` |
| Production  | `https://partner.payu.in`     |

## Operation

| Property      | Value                                                |
| ------------- | ---------------------------------------------------- |
| HTTP method   | `POST`                                               |
| Endpoint path | `{base_url}/api/v1/merchants/{uuid}/submit_consents` |
| Content type  | `application/json`                                   |

Replace `{uuid}` with the UUID of the merchant whose consent is being submitted.

## Request

### Headers

```http
Authorization: Bearer <BEARER_TOKEN>
Content-Type: application/json
```

### Parameters

| Location           | Field              | Type   | Description                                                                                            |
| ------------------ | ------------------ | ------ | ------------------------------------------------------------------------------------------------------ |
| Path               | `uuid`             | string | UUID of the merchant onboarding record for which the consent is being submitted.                       |
| Body               | `consents`         | array  | Collection of consent objects to submit.                                                               |
| Body: `consents[]` | `name`             | string | Name of the consent being submitted. Use the consent name configured for the relevant onboarding flow. |
| Body: `consents[]` | `provided_by_uuid` | string | UUID of the partner or provider submitting the consent.                                                |

### Example request

The following example uses placeholders for both UUIDs and the bearer token.

#### Request body

```json
{
  "consents": [
    {
      "name": "gst_consent",
      "provided_by_uuid": "<PROVIDER_UUID>"
    }
  ]
}
```

#### cURL

```curl Skip GST
curl --request POST \\
  --url 'https://test-partner.payu.in/api/v1/merchants/<MERCHANT_UUID>/submit_ckyc_consent' \\
  --header 'Authorization: Bearer <BEARER_TOKEN>' \\
  --header 'Content-Type: application/json' \\
  --data '{
    "consents": [
      {
        "name": "gst_consent",
        "provided_by_uuid": "<PROVIDER_UUID>"
      }
    ]
  }'
```
```curl Skip CKYC
curl --request POST \\
  --url 'https://test-partner.payu.in/api/v1/merchants/<MERCHANT_UUID>/submit_ckyc_consent' \\
  --header 'Authorization: Bearer <BEARER_TOKEN>' \\
  --header 'Content-Type: application/json' \\
  --data '{
    "consents": [
      {
        "name": "skip_ckyc_flow",
        "provided_by_uuid": "<PROVIDER_UUID>"
      }
    ]
  }'
```

## Example response

The following response preserves the supplied response structure and values. Sensitive or environment-specific request credentials are not included.

```json Skip GSTIN
{
  "message": "Consent submitted successfully",
  "data": {
    "consents": [
      {
        "uuid": "11f1-3337-6b2a03aa-8306-02f4a48620c1",
        "name": "gst_consent",
        "provided_by_uuid": "11f1-1d1b-a73f183a-b5f2-02111e9ad6d9",
        "provided_by": "PAYU PAYMENTS PRIVATE LIMITED",
        "record_id": 27986,
        "record_type": "ProductAccount",
        "merchant_id": null,
        "active": true,
        "product_account_uuid": "11f1-3335-5e00033e-b7b7-02f4a48620c1",
        "merchant_uuid": null
      }
    ]
  }
}
```
```text Skip CKYC
{
  "message": "Consent submitted successfully",
  "data": {
    "consents": [
      {
        "uuid": "11f1-3337-6b2a03aa-8306-02f4a48620c1",
        "name": "skip_ckyc_flow",
        "provided_by_uuid": "11f1-1d1b-a73f183a-b5f2-02111e9ad6d9",
        "provided_by": "PAYU PAYMENTS PRIVATE LIMITED",
        "record_id": 27986,
        "record_type": "ProductAccount",
        "merchant_id": null,
        "active": true,
        "product_account_uuid": "11f1-3335-5e00033e-b7b7-02f4a48620c1",
        "merchant_uuid": null
      }
    ]
  }
}
```

## Response parameters

### Top-level fields

| Field           | Type   | Description                                            |
| --------------- | ------ | ------------------------------------------------------ |
| `message`       | string | Confirmation message for the consent submission.       |
| `data`          | object | Container for the consent records returned by the API. |
| `data.consents` | array  | Consent records associated with the submission.        |

### Nested consent fields

| Field                                  | Type           | Description                                                                                                 |
| -------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------- |
| `data.consents[].uuid`                 | string         | UUID assigned to the consent record.                                                                        |
| `data.consents[].name`                 | string         | Name of the consent record. Supported Types are `skip_ckyc_flow `&` gst_consent`                            |
| `data.consents[].provided_by_uuid`     | string         | UUID of the partner associated with the submitted consent.                                                  |
| `data.consents[].provided_by`          | string         | Name of the partner or provider associated with the `provided_by_uuid`.                                     |
| `data.consents[].record_id`            | integer        | Numeric identifier of the consent record.                                                                   |
| `data.consents[].record_type`          | string         | Type of record to which the consent is attached; the supplied response returns `ProductAccount`.            |
| `data.consents[].merchant_id`          | string or null | Merchant identifier associated with the consent record, when present. The supplied response returns `null`. |
| `data.consents[].active`               | boolean        | Indicates whether the returned consent record is active.                                                    |
| `data.consents[].product_account_uuid` | string         | UUID of the product account associated with the consent record.                                             |
| `data.consents[].merchant_uuid`        | string or null | Merchant UUID associated with the consent record, when present. The supplied response returns `null`.       |

## Notes

- Send the request body as valid JSON with `Content-Type: application/json`.
- Use the UAT base URL for testing and the Production base URL for live requests.
- The merchant UUID in the path and the provider UUID in each consent object should be the identifiers applicable to the request.
- A successful response returns a confirmation `message` and the consent record under `data.consents`.
