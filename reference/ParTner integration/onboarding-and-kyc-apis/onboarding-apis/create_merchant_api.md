---
title: Create Merchant API
excerpt: ''
api:
  file: partner-apis-26.json
  operationId: create_merchantv3
deprecated: false
hidden: false
metadata:
  title: Create Merchant API
  description: >-
    Learn how to use the PayU Create Merchant API to create new merchant
    accounts. This API reference page provides detailed instructions, request
    parameters, and sample responses for efficient merchant onboarding
  keywords:
    - Create Merchant API
    - ' merchant onboarding'
    - ' KYC details'
    - ' secure merchant creation'
    - ' tokenization'
    - ' manage merchants'
    - ' create merchant accounts'
  robots: index
next:
  description: ''
---
The **Create Merchant** API creates a new merchant account on PayU and posts all KYC details. This API returns the Merchant ID (MID) in the response.

## Authentication

This API is authorised through a client token generated using the client ID and secret. To create a token, call the get token API with `refer merchant` as a scope.  Refer to the  [Get Token API](ref:get_token_api) doc for more information.

> ❗️ Important considerations for using this API
>
> 1. The mobile, Pan number, GSTIN passed in the request has to be valid as checks are performed in real time.
> 2. If Business Entity type is passed in the create merchant API, ensure that the PAN also belong to the same entity.

<PARTNEROnboardingEnvironment />

<br />

## Sample response

### Success scenario

```
{
  "merchant": {
    "mid": "8390925",
    "kyc_document_name": "PAN Card of Signing Authority",
    "kyc_document_uuid": "11ef-587e-43837330-95b0-021ec077a271",
    "kyc_document_status": "DOCUMENT_SUBMITTED",
    "error_message": null,
    "created_at": "2024-08-12T07:41:19.000Z"
  }
}
```

### Failure scenario

* Required field missing

```
{
  "success": false,
  "error": {
    "code": "MISSING_REQUIRED_FIELD",
    "message": "Required field 'merchant[display_name]' is missing",
    "details": {
      "field": "merchant[display_name]"
    }
  }
}

```

* Invalid field format

```
{
  "success": false,
  "error": {
    "code": "INVALID_FIELD_FORMAT",
    "message": "Field 'merchant[email]' has invalid format",
    "details": {
      "field": "merchant[email]",
      "expected_format": "valid email address (e.g., example@domain.com)"
    }
  }
}

```

* Duplicate merchant or merchant already exists

```
{
  "success": false,
  "error": {
    "code": "DUPLICATE_MERCHANT",
    "message": "Merchant with the same identifier already exists",
    "details": {
      "identifier": "9916965913",
      "identifier_type": "mobile"
    }
  }
}

```

* Authentication error

```
{
  "success": false,
  "error": {
    "code": "AUTHENTICATION_ERROR",
    "message": "Invalid or missing authentication token"
  }
}

```

* Business entity error

```
{
  "success": false,
  "error": {
    "code": "INVALID_BUSINESS_ENTITY_TYPE",
    "message": "Invalid business entity type provided",
    "details": {
      "provided": "Undefined",
      "allowed_values": [
        "Sole Proprietorship",
        "Partnership",
        "Private Limited",
        "Public Limited",
        "LLP",
        "Trust",
        "Society",
        "NGO"
      ]
    }
  }
}

```

* Dependency error

```
{
  "success": false,
  "error": {
    "code": "DEPENDENCY_ERROR",
    "message": "Field 'merchant[udyam_number]' is required when business entity type is 'Sole Proprietorship'",
    "details": {
      "field": "merchant[udyam_number]",
      "dependent_field": "merchant[business_details][business_entity_type]",
      "dependent_value": "Sole Proprietorship"
    }
  }
}

```

* Rate limit exceeded

```
{
  "success": false,
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded. Please try again later",
    "details": {
      "retry_after": 60,
      "limit": "100 requests per minute"
    }
  }
}

```

* Invalid API version

```
{
  "success": false,
  "error": {
    "code": "INVALID_API_VERSION",
    "message": "The requested API version is not supported",
    "details": {
      "requested_version": "v2",
      "supported_versions": ["v3", "v4"]
    }
  }
}

```

<br />

## Response parameters

### Fields in the merchant object

| Parameter             | Description                                                                        | Example                              |
| :-------------------- | :--------------------------------------------------------------------------------- | :----------------------------------- |
| mid                   | Unique merchant identifier                                                         | 8390925                              |
| kyc\_document\_name   | Name of the KYC document category                                                  | PAN Card of Signing Authority        |
| kyc\_document\_uuid   | Unique identifier for the KYC document submission                                  | 11ef-587e-43837330-95b0-021ec077a271 |
| kyc\_document\_status | Current status of the KYC document (e.g., DOCUMENT\_SUBMITTED, VERIFIED, REJECTED) | DOCUMENT\_SUBMITTED                  |
| error\_message        | Error message if document verification failed, null otherwise                      | null                                 |
| created\_at           | Timestamp when the KYC document was created/submitted.                             | 2024-08-12T07:41:19.000Z             |

> 📘 Notes:
>
> * The `kyc_document_status` field can have the following values:
>   * `DOCUMENT_SUBMITTED`: Document has been submitted but not yet verified
>   * `VERIFIED`: Document has been verified and approved
>   * `REJECTED`: Document was rejected during verification
>   * `PENDING`: Document is pending verification
> * The `error_message` field will only contain a value if the document was rejected or there was an issue with the submission.
> * All timestamps are in ISO 8601 format with UTC timezone.

## Request parameters

<details>
  <summary>Reference information for request parameters</summary>

  | Parameter                          | Reference                                                                                                                  |
  | :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
  | merchant\[business\_category]      | For the list of business categories, refer to [Business. Category List](ref:partner-category-list).                        |
  | merchant\[business\_entity\_type]  | For the list of business entity type, refer to [Business Entity Type](ref:partner-category-list#business-entity-type).     |
  | merchant\[business\_sub\_category] | For the list of business subcategories, refer to [Business Sub-Category](ref:partner-category-list#business-sub-category). |
</details>