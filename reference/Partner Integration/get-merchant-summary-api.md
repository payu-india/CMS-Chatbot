---
title: Get Merchant Summary API
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Get Merchant Summary API
excerpt: Retrieve the real-time onboarding summary and pending KYC status for a linked merchant account.
deprecated: false
hidden: false
metadata:
  robots: index
---

The **Get Merchant Summary API** enables partners to query the onboarding and verification status of a merchant's product account. 

Partners can use this server-to-server endpoint to identify which onboarding steps, KYC verifications, address submissions, stakeholder disclosures, or compliance documents are completed or still pending for a merchant linked to their partner account.

---

## Base URLs

| Environment | Host |
| :--- | :--- |
| **Production** | `https://partner.payu.in` |
| **UAT** | `https://uat-partner.payu.in` |

---

## Endpoint

```http
GET /api/v3/merchants/:merchant_id/get_merchant_summary
```

---

## Authentication & Request Headers

This API requires OAuth 2.0 Bearer token authentication with the `refer_merchant` scope.

### Mandatory Headers

| Header | Description |
| :--- | :--- |
| Authorization | _String_<br>Bearer access token obtained from PayU's OAuth Token API with the `refer_merchant` scope.<br>**Format:** `Bearer <access_token>` |

---

## Request Parameters

### Path Parameters

#### Mandatory Parameters

| Parameter | Description |
| :--- | :--- |
| merchant_id | _String_<br>The unique product account identifier (UUID) of the merchant. The product account must be actively linked to the calling partner/reseller.<br>**Example:** `11f1-addc-1cc7ed88-9770-0ad5848e0da3` |

<Callout icon="📘" theme="info">
  ### **No Request Body Required**
  This is a `GET` endpoint and does not accept a request body.
</Callout>

---

## Sample Request

```bash cURL
curl -X GET "https://partner.payu.in/api/v3/merchants/11f1-addc-1cc7ed88-9770-0ad5848e0da3/get_merchant_summary" \
  -H "Authorization: Bearer <access_token>"
```

---

## Response Parameters

### Top-Level Parameters

| Parameter | Description |
| :--- | :--- |
| pan_status | _String_<br>Status of PAN verification.<br>**Possible values:** `Success`, `Pending`, `Failed` |
| gst_status | _String_<br>Status of GST verification.<br>**Possible values:** `Success`, `Pending`, `Failed`, `Skipped` |
| bank_status | _String_<br>Status of bank account penny-drop / verification.<br>**Possible values:** `Success`, `Pending`, `Failed`, `IN_PROGRESS` |
| website_status | _String_<br>Status of merchant website / app URL compliance verification (e.g., `Verification in Process`). |
| auto_kyc_status | _Boolean_<br>Indicates whether automated KYC verification has been completed. |
| aadhaar_kyc_status | _Boolean_<br>Indicates whether Aadhaar-based KYC verification has been completed. |
| document_status | _String_<br>Overall document verification status (e.g., `Pending`, `Success`). |
| all_doc_statuses | _Array of Objects_<br>Itemized status list of individual onboarding documents submitted by the merchant. For more information, refer to [all_doc_statuses Object Fields Description](all_doc_statuses-object-fields-description) |
| doc_reviewer_assigned | _Boolean_<br>Indicates whether an operations/compliance reviewer has been assigned to verify uploaded documents. |
| vkyc_status | _String_<br>Status of Video KYC verification (e.g., `skipped`, `Pending`, `Success`). |
| ckyc_status | _String_<br>Status of Central KYC (CKYC) registry verification.<br>**Possible values:** `Success`, `Failed`, `Pending`, `skipped` |
| is_rekyc | _Boolean_<br>Indicates whether the merchant account is undergoing a re-KYC verification cycle. |
| agreement_status | _String_<br>Status of the merchant onboarding agreement (e.g., `Sent`, `Signed`). |
| op_addr_present | _Boolean_<br>Indicates whether operating address details have been submitted. |
| reg_addr_present | _Boolean_<br>Indicates whether registered office address details have been submitted. |
| signatory_present | _Boolean_<br>Indicates whether signing authority details have been submitted. |
| lob_status | _String_ or _Null_<br>Line of Business (LOB) / category verification status. Returns `null` if not applicable or not evaluated. |
| cpv_status | _String_<br>Contact Point Verification (CPV) status (e.g., `pending`, `Success`). |
| business_members | _Array of Objects_<br>List of declared business stakeholders, partners, or directors. For more information, refer to [business_members Object Fields Description](#business_members-object-fields-description) |
| business_members_required | _Boolean_<br>Indicates whether declaring business members is mandatory for the merchant's business entity type. |
| director_or_partner_present | _Boolean_<br>Indicates whether details for at least one director or partner have been submitted. |
| kmp_present | _Boolean_<br>Indicates whether Key Managerial Personnel (KMP) details are submitted. |
| ultimate_beneficiaries | _Array of Objects_<br>List of declared Ultimate Beneficial Owners (UBOs). For more information, refer to [ultimate_beneficiaries Object Fields Description](#ultimate_beneficiaries-object-fields-description)|
| ubo_statuses | _Object_<br>Container holding UBO declaration and verification status flags. For more information, refer to [ubo_statuses Object Fields Description](#ubo_statuses-object-fields-description)|

---

### all_doc_statuses Object Fields Description

| Parameter | Description |
| :--- | :--- |
| name | _String_<br>Display title or name of the document (e.g., `Address Proof of Signing Authority`). |
| status | _String_<br>Verification status of the document (e.g., `No Document Uploaded`, `Pending`, `Approved`, `Rejected`). |

---

### business_members Object Fields Description

| Parameter | Description |
| :--- | :--- |
| name | _String_<br>Full legal name of the business member or director (e.g., `Sample Director`). |
| designation | _String_<br>Designation or corporate role within the business (e.g., `Director`, `Partner`). |
| dob | _String_<br>Date of birth of the business member formatted as `YYYY-MM-DD`. |

---

### ultimate_beneficiaries Object Fields Description

| Parameter | Description |
| :--- | :--- |
| name | _String_<br>Full legal name of the Ultimate Beneficial Owner (UBO) (e.g., `Sample UBO`). |
| ownership_percent | _String_<br>Percentage of equity or beneficial ownership held by the stakeholder (e.g., `"17.0"`). |

---

### ubo_statuses Object Fields Description

| Parameter | Description |
| :--- | :--- |
| required | _Boolean_<br>Indicates whether UBO declaration is required for this merchant entity type. |
| present | _Boolean_<br>Indicates whether UBO details have been submitted. |
| aadhaar_kyc_present | _Boolean_<br>Indicates whether Aadhaar KYC has been completed for the declared UBOs. |

---

## Sample Response

### 200 OK (Success Response)

```json
{
  "pan_status": "Success",
  "gst_status": "Pending",
  "bank_status": "IN_PROGRESS",
  "website_status": "Verification in Process",
  "auto_kyc_status": true,
  "aadhaar_kyc_status": true,
  "document_status": "Pending",
  "all_doc_statuses": [
    {
      "name": "Address Proof of Signing Authority",
      "status": "No Document Uploaded"
    }
  ],
  "doc_reviewer_assigned": false,
  "vkyc_status": "skipped",
  "ckyc_status": "skipped",
  "is_rekyc": false,
  "agreement_status": "Sent",
  "op_addr_present": false,
  "reg_addr_present": true,
  "signatory_present": true,
  "lob_status": null,
  "cpv_status": "pending",
  "business_members": [
    {
      "name": "Sample Director",
      "designation": "Director",
      "dob": "1980-01-01"
    }
  ],
  "business_members_required": true,
  "director_or_partner_present": true,
  "kmp_present": true,
  "ultimate_beneficiaries": [
    {
      "name": "Sample UBO",
      "ownership_percent": "17.0"
    }
  ],
  "ubo_statuses": {
    "required": true,
    "present": true,
    "aadhaar_kyc_present": false
  }
}
```

---

## Errors & Status Codes

| Status Code | Condition / Trigger | Error Response Body |
| :--- | :--- | :--- |
| **401 Unauthorized** | Token is missing, invalid, or does not have `refer_merchant` scope | ```json\n{\n  "status": "Unauthorized"\n}\n``` |
| **404 Not Found** | Product account is not linked to this partner | ```json\n{\n  "data": {\n    "message": "Reseller is not allowed to modify merchant with uuid: <uuid>"\n  }\n}\n``` |
| **422 Unprocessable Entity** | `merchant_id` path parameter is blank | ```json\n{\n  "data": {\n    "message": "product_account_uuid cannot be blank"\n  }\n}\n``` |