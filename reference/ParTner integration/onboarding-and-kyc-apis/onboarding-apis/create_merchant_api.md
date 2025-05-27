---
title: Create Merchant API
api:
  file: Partner_Onboarding_APIs_with_Create_Merchant.json
  operationId: CreateMerchant
hidden: false
---
The **Create Merchant** API creates a new merchant account on PayU and posts all KYC details. This API returns the Merchant ID (MID) in the response.

## Authentication

This API is authorised through a client token generated using the client ID and secret. To create a token, call the get token API with `refer merchant` as a scope.  Refer to the  [Get Token API](ref:get_token_api) doc for more information.

> ❗️ Important considerations for using this API
>
> 1. The mobile, Pan number, GSTIN passed in the request has to be valid as checks are performed in real time.
> 2. If Business Entity type is passed in the create merchant API, ensure that the PAN also belong to the same entity.

| \*\* Environment\*\* | \*\* URL\*\*                                                                         |
| :------------------- | :----------------------------------------------------------------------------------- |
| production           | [https://partner.payu.in/api/v3/merchants](https://partner.payu.in/api/v3/merchants) |
| UAT                  | uat-partner.payu.in/api/v3/merchants                                                 |

\<details>
&#x20; \<summary>Sample request\</summary>

```
curl --location 'https://uat-partner.payu.in/api/v3/merchants' \
--header 'Authorization: Bearer 27a6389ec4d74fb8c3f2baf68b220a5780bf4cfc4cce004505d2c20ead6e1fba' \
--form '[merchant][display_name]="DIVY HARESHKUMAR SHAH"' \
--form 'merchant[email]="boro5@yomail.com"' \
--form 'merchant[mobile]="9916965905"' \
--form 'merchant[business_details][pan]="FANPS6362D"' \
--form 'merchant[business_details][business_entity_type]="Sole Proprietorship"' \
--form 'merchant[product]="PayUbiz"' \
--form 'merchant[bank_details][account_no]="919010067278549"' \
--form 'merchant[bank_details][account_holder_name]="DIVY HARESHKUMAR SHAH"' \
--form 'merchant[bank_details][ifsc_code]="UTIB0003557"' \
--form 'merchant[business_details][registered_name]="DIVY HARESHKUMAR SHAH"' \
--form 'merchant[business_details][business_category]="Arts, Gifts & Stationery"' \
--form 'merchant[business_details][business_sub_category]="Art Dealers and Galleries"' \
--form 'merchant[website_details][website_url]="https://www.google.com"' \
--form 'merchant[monthly_expected_volume]="12000"' \
--form 'merchant[signing_authority_details][name]="DIVY HARESHKUMAR SHAH"' \
--form 'merchant[signing_authority_details][pancard_number]="FANPS6362D"' \
--form 'merchant[signing_authority_details][email]="email_test1213@yopmail.com"' \
--form 'merchant[business_details][pancard_name]="DIVY HARESHKUMAR SHAH"'
```

\</details>

\<details>
&#x20; \<summary>Sample response\</summary>

### Success scenario

```
{
    "merchant": {
        "name": "DIVY HARESHKUMAR SHAH",
        "email": "boro13@yomail.com",
        "registered_mobile": "9916965913",
        "mid": 760069002,
        "product": "PayUbiz",
        "business_type": "LongTail",
        "business_name": null,
        "pancard_name": null,
        "pancard_number": null,
        "website_url": null,
        "android_url": null,
        "ios_url": null,
        "gst_number": "24FANPS6362D1ZM",
        "created_at": "2025-05-22T11:00:04.000Z",
        "mobile": "9916965913",
        "blocked": false,
        "first_name": "DIVY",
        "last_name": "HARESHKUMAR SHAH",
        "bank_detail": {
            "bank_account_number": null,
            "ifsc_code": null,
            "holder_name": null,
            "nodal_code": null,
            "nodal_status": null
        },
        "operating_address": {
            "address_line": null,
            "city": null,
            "state": null,
            "pincode": null
        },
        "registration_address": {
            "address_line": null,
            "city": null,
            "state": null,
            "pincode": null
        },
        "business_entity": "Sole Proprietorship",
        "status": "account_created",
        "partner_source": "Create Merchant API",
        "pan_verification_status": "Pending",
        "website_approval_status": null,
        "notification_email": "boro13@yomail.com",
        "settlement_status": null,
        "is_service_agreement_accepted": false,
        "is_authorisation_letter_required": false,
        "monthly_expected_volume": null,
        "business_category": null,
        "business_sub_category": null,
        "bank_verification_status": null,
        "uuid": "11f0-36fb-ea0981e8-9d1a-02975f21d323",
        "penny_deposit_status": null,
        "document_status": "Pending",
        "kyc_status": {
            "status": "LOCKED",
            "kyc_status": "LOCKED"
        },
        "agreement_status": "Not Generated",
        "integration_type": "Not Selected",
        "service_intent": "default"
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

\</details>

\<details>
&#x20; \<summary>Response parameters\</summary>

### merchant JSON object field descriptions

| Field                               | Description                                                                                                                                                                                     | Example                                                       |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| name                                | Full name of the merchant                                                                                                                                                                       |                                                               |
| email                               | Email address of the merchant                                                                                                                                                                   |                                                               |
| registered\_mobile                  | Registered mobile number of the merchant                                                                                                                                                        | 10-digit mobile number                                        |
| mid                                 | Merchant ID, a unique identifier in the system                                                                                                                                                  |                                                               |
| product                             | The product associated with the merchant                                                                                                                                                        | PayUbiz                                                       |
| business\_type                      | Type of business                                                                                                                                                                                | LongTail                                                      |
| business\_name                      | Name of the business. This field can be null.                                                                                                                                                   |                                                               |
| pancard\_name                       | Name as it appears on the PAN card. This field can be null.                                                                                                                                     |                                                               |
| pancard\_number                     | PAN card number                                                                                                                                                                                 | AAAAA0000A                                                    |
| website\_url                        | URL of the merchant's website. This field can be null.                                                                                                                                          |                                                               |
| android\_url                        | URL of the merchant's Android app. This field can be null.                                                                                                                                      |                                                               |
| ios\_url                            | URL of the merchant's iOS app. This field can be null.                                                                                                                                          |                                                               |
| gst\_number                         | GST registration number                                                                                                                                                                         | 22AAAAA0000A1Z5                                               |
| created\_at                         | Timestamp when the merchant was created                                                                                                                                                         | ISO 8601 format (UTC)                                         |
| mobile                              | Mobile number of the merchant                                                                                                                                                                   | 10-digit mobile number                                        |
| blocked                             | Indicates if the merchant is blocked                                                                                                                                                            | true/false                                                    |
| first\_name                         | First name of the merchant                                                                                                                                                                      |                                                               |
| last\_name                          | Last name of the merchant                                                                                                                                                                       |                                                               |
| business\_entity                    | Type of business entity                                                                                                                                                                         | "Sole Proprietorship", "Partnership", "Private Limited", etc. |
| status                              | Current status of the merchant account                                                                                                                                                          | "account\_created", "active", "suspended", etc.               |
| partner\_source                     | Source of the merchant registration                                                                                                                                                             | "Create Merchant API"                                         |
| pan\_verification\_status           | Status of PAN verification                                                                                                                                                                      | "Pending", "Verified", "Failed", etc.                         |
| website\_approval\_status           | Status of website approval                                                                                                                                                                      | "Pending", "Approved", "Rejected", etc.                       |
| notification\_email                 | Email address for notifications                                                                                                                                                                 |                                                               |
| settlement\_status                  | Status of settlement account. This field can be null                                                                                                                                            | "Pending", "Active", etc.                                     |
| is\_service\_agreement\_accepted    | Whether service agreement is accepted                                                                                                                                                           | true/false                                                    |
| is\_authorisation\_letter\_required | Whether authorization letter is required                                                                                                                                                        | true/false                                                    |
| monthly\_expected\_volume           | Expected monthly transaction volume. This field can be null.                                                                                                                                    |                                                               |
| business\_category                  | Category of the business. This field can be null.                                                                                                                                               | "Retail", "Services", etc.                                    |
| business\_sub\_category             | Sub-category of the business. This field can be null.                                                                                                                                           |                                                               |
| bank\_verification\_status          | Status of bank verification. This field can be null.                                                                                                                                            | "Pending", "Verified", "Failed", etc.                         |
| uuid                                | Universally Unique Identifier                                                                                                                                                                   | Format: UUID v4                                               |
| penny\_deposit\_status              | Status of penny deposit verification. This field can be null.                                                                                                                                   | "Pending", "Verified", "Failed", etc.                         |
| document\_status                    | Status of document verification                                                                                                                                                                 | "Pending", "Verified", "Rejected", etc.                       |
| agreement\_status                   | Status of merchant agreement                                                                                                                                                                    | "Not Generated", "Generated", "Signed", etc.                  |
| integration\_type                   | Type of integration                                                                                                                                                                             | "Not Selected", "API", "SDK", etc.                            |
| service\_intent                     | Service intent of the merchant                                                                                                                                                                  | "default"                                                     |
| bank\_detail                        | Contains the bank\_detail in a JSON format. For more information, refer to [bank\_detail JSON object field descriptions](bank_detail-json-object-field-descriptions).                           |                                                               |
| operating\_address                  | Contains the operating\_address in a JSON format. For more information, refer to \[operating\_address JSON object field descriptions]\(#operating\_address-json-object-field descriptions)      |                                                               |
| registration\_address               | Contains the registration address in a JSON format. For more information, refer to [registration\_address JSON object field descriptions](registration_address-json-object-field-descriptions). |                                                               |
| kyc\_status                         | Contains the KYC in a JSON format. For more information, refer to [KYC status JSON object field descriptions.](#kyc-status-json-object-field-descriptions.)                                     |                                                               |

### bank\_detail JSON object field descriptions

The `bank_detail` object contains information about the merchant's bank account.

| Field                 | Description                     | Possible Values/Notes            |
| --------------------- | ------------------------------- | -------------------------------- |
| bank\_account\_number | Bank account number             | Can be null                      |
| ifsc\_code            | IFSC code of the bank branch    | Can be null, Format: AAAA0000000 |
| holder\_name          | Name of the account holder      | Can be null                      |
| nodal\_code           | Nodal code for the bank account | Can be null                      |
| nodal\_status         | Status of nodal account         | Can be null                      |

### operating\_address JSON object field descriptions

The `operating_address` object contains the merchant's operating address details.

| Field         | Description          | Possible Values/Notes                          |
| ------------- | -------------------- | ---------------------------------------------- |
| address\_line | Street address       | Can be null                                    |
| city          | City name            | Can be null                                    |
| state         | State name           | Can be null                                    |
| pincode       | PIN code/postal code | Can be null, 6-digit code for Indian addresses |

### registration\_address JSON object field descriptions

The `registration_address` object contains the merchant's registration address details.

| Field         | Description          | Possible Values/Notes                          |
| ------------- | -------------------- | ---------------------------------------------- |
| address\_line | Street address       | Can be null                                    |
| city          | City name            | Can be null                                    |
| state         | State name           | Can be null                                    |
| pincode       | PIN code/postal code | Can be null, 6-digit code for Indian addresses |

### kyc\_ status JSON object field descriptions

The `kyc_status` object contains information about the merchant's KYC verification status.

| Field       | Description         | Possible Values/Notes                                    |
| ----------- | ------------------- | -------------------------------------------------------- |
| status      | Overall KYC status  | e.g., "LOCKED", "UNLOCKED", "VERIFIED", etc.             |
| kyc\_status | Detailed KYC status | e.g., "LOCKED", "UNLOCKED", "VERIFIED", "REJECTED", etc. |

> 📘 Notes:
>
> * The `kyc_document_status` field can have the following values:
>   * `DOCUMENT_SUBMITTED`: Document has been submitted but not yet verified
>   * `VERIFIED`: Document has been verified and approved
>   * `REJECTED`: Document was rejected during verification
>   * `PENDING`: Document is pending verification
> * The `error_message` field will only contain a value if the document was rejected or there was an issue with the submission.
> * All timestamps are in ISO 8601 format with UTC timezone.

\</details>

## Request parameters

<details>
  <summary>Reference information for request parameters</summary>

  | Parameter                          | Reference                                                                                                                  |
  | :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
  | merchant\[business\_category]      | For the list of business categories, refer to [Business. Category List](ref:partner-category-list).                        |
  | merchant\[business\_entity\_type]  | For the list of business entity type, refer to [Business Entity Type](ref:partner-category-list#business-entity-type).     |
  | merchant\[business\_sub\_category] | For the list of business subcategories, refer to [Business Sub-Category](ref:partner-category-list#business-sub-category). |
</details>