---
title: Create Child Merchant API - Hyundai
deprecated: false
hidden: true
metadata:
  title: Create Child Merchant API - Hyundai
  robots: index
---
This section describes how to create and onboard child merchants using the **Create Child Merchant** API as part of the Aggregator workflow. Creating a child merchant using this API involves the following steps:

1. [Add a child merchant](#step-1-add-child-merchant)
2. [Update bank details.](#step-2-update-bank-details)
3. [Upload Schedule C document](#step-3-upload-schedule-c-document)

<Callout icon="📘" theme="info">
  **Notes**:

  * After adding the child merchant in[ Step 1: Add a child merchant](#step-1-add-child-merchant), update the bank details of the child merchant using this API again as in [Step 2: Update bank details.](#step-2-update-bank-details).
  * After completing  [Step 2](#step-2-update-bank-details), you must upload the Schedule C document for the child merchant. For more information on how to upload the Schedule C document of the child merchant, refer to [Add a Sub-Account](doc:add-a-sub-account).
</Callout>

HTTP Method: **POST**

**Environment**

|                            |                                                                                                                                    |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Test Environment**       | \<[https://uat-onepayuonboarding.payu.in/api/v3/product_accounts>](https://uat-onepayuonboarding.payu.in/api/v3/product_accounts>) |
| **Production Environment** | \<[https://onboarding.payu.in/api/v3/product_accounts>](https://onboarding.payu.in/api/v3/product_accounts>)                       |

## Step 1: Add child merchant

<Callout icon="📘" theme="info">
  **Authorization**:  Generate token using the [Get Client Token API](ref:get-client-token-api) and pass it in header along with the following request parameters.

  For the Postman collection, refer to [Postman Collection](https://documenter.getpostman.com/view/7484238/TVCcZAJC#auth-info-60abdedd-6640-49c8-9497-fe181220c2fd). Merchant access token or client token with scope ‘refer_child_merchant’ from Hub.
</Callout>

### Request Parameters

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>product<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter must be passed with the following value: &quot;PayUBiz&quot;</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>PayUBiz</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>name<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The display name of the child merchant</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Harsh Agarwal</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>email<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The child merchant email.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="mailto:test.user94@payu.in">test.user94@payu.in</a></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>mobile<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The mobile number of the child merchant</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>995315***1</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>merchant_defined_identifier<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>A custom identifier used to identify the submerchant or child merchant. This can be any merchant-specific identifier such as a dealer code, branch code, or internal reference ID.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>fhvbjs324</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>aggregator_parent_mid<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The parent merchant MID is specified in this parameter.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>7210921</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>merchant_type<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter is used to specify the merchant type as aggregator.<br><strong>Note</strong>: The value for this parameter must be posted as <strong>aggregator</strong>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>aggregator</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>business_entity_id<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The business entity ID of the merchant. The business entity ID and corresponding business entity is listed in the <a href="#business-entity-mapping">Business Entity Mapping</a> table of this section.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>P</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>pancard_number<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The PAN card number of the child merchant.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>DBZPK4951B</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>pancard_name<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The name of the child merchant as in the PAN card.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>kapil kumar</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>business_category_id<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The business category ID of the child merchant. For the list business category ID, refer to <a href="https://docs.payu.in/reference/business-category-sub-category-uuids-for-split-settlements/" target="_blank">Business Category &amp; Sub-category UUIDs List</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>16</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>business_sub_category_id<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The business sub category ID of the child merchant. For the list business sub-category ID, refer to <a href="https://docs.payu.in/reference/business-category-sub-category-uuids-for-split-settlements/" target="_blank">Business Category &amp; Sub-category UUIDs List</a> .<br><strong>Note</strong>: Each business sub-category is dependent on business category. Hence, you must enter the sub-category according to the value you post in the <strong>business_category_id</strong> parameter.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>128</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>gst_number<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The GST number of the child merchant registered with the Sales tax department.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>09ABQFA5416M1ZX</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>monthly_expected_volume<br>&quot;<strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The monthly expected volume of the child merchant.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>60000</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>business_name<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The business name of the child merchant, similar to PAN.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Harsh Agarwal</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### Business Entity Mapping

The business entity ID (**business_entity_id**) and corresponding business entity mapping are:

| Entity Code | Business Entity Types                               |
| :---------- | :-------------------------------------------------- |
| A           | Society                                             |
| P           | Individual, Sole Proprietorship                     |
| F           | Partnership, LLP                                    |
| C           | Private Limited, Public Limited, One Person Company |
| T           | Trust                                               |
| G           | Government                                          |
| H           | Hindu Undivided Family                              |
| L           | Local Authority                                     |
| J           | Artificial Juridical Person                         |

### Sample request

* Success Scenario

```curl
curl --location 'https://uat-onepayuonboarding.payu.in/api/v3/product_accounts' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data-raw '{
    "product_account": {
        "product": "PayUbiz",        
        "email": "chagg232509_4@yopmail.com",
        "mobile": "8447644143",
        "merchant_defined_identifier":"fhvbjs324",
        "aggregator_parent_mid": "30939561", 
        "merchant_type": "aggregator",
        "pancard_number": "AUKPA1386M",    
        "business_name": "Harsh Agarwal",     
        "business_entity_id": 14,
        "business_category_id": 37,
        "business_sub_category_id": 313,
        "monthly_expected_volume": 220955
  }
}'
```

* Failure Scenario

**Token is invalid**

```curl
curl --location -g --request POST 'https://uat-onepayuonboarding.payu.in/api/v3/product_accounts' \
--header 'Authorization: Bearer {{access_token}}' \
--data-raw '{
	"merchant": {
        "product": "PayUbiz",
	"email": "test.user5.aggregator@payutest.in", 
	"mobile": "8860890284",
        "aggregator_parent_mid": "149726", 
        "merchant_type": "aggregator" 
	}
}'
```

**Token has expired**

```curl
curl --location -g --request POST 'https://uat-onepayuonboarding.payu.in/api/v3/product_accounts' \
--header 'Authorization: Bearer {{access_token}}' \
--data-raw '{
	"merchant": {
        "product": "PayUbiz", // Mandatory to pass
		"email": "test.user5.aggregator@payutest.in", // child merchant email, mandatory
		"mobile": "8860890284", // Child merchant user mobile, mandatory
        "aggregator_parent_mid": "149726", // Parent merchant mid, mandatory
        "merchant_type": "aggregator" // Mandatory field
	}
}'
```

### Sample Response

* Success Scenario

Create Child Merchant Success Scenario

```json
{
    "product_account": {
        "id": 25636,
        "uuid": "11f0-badd-c184cc6c-8834-02975f21d323",
        "identifier": 30949833,
        "product_id": 1,
        "type": "PayUbizAccount",
        "merchant_account_id": 25297,
        "active": true,
        "status": null,
        "business_entity_id": null,
        "business_category_id": null,
        "business_sub_category_id": null,
        "business_name": null,
        "pancard_name": null,
        "pancard_number": null,
        "gst_number": null,
        "notification_email": "chagg232509_5@yopmail.com",
        "flag": 1040,
        "settlement_status": null,
        "merchant_type": "child_aggregator",
        "onboarding_status": "Profile Completion in progress",
        "account_id": null,
        "pan_verification_status": "Pending",
        "admin_user_id": 19118,
        "terms_and_condition_accepted_at": null,
        "created_at": "2025-11-06T06:56:45.000Z",
        "updated_at": "2025-11-06T06:56:47.000Z",
        "partner_uuid": null,
        "business_origin": "SMB-ENT",
        "shop_number": null,
        "area_code": null,
        "gst_verification_status": "Pending",
        "cin_number": null,
        "vkyc_exemption": "",
        "sf_payload_version": -1,
        "stop_txns": null,
        "copy_mid_parent": null,
        "flag1": 32,
        "udyam_number": null,
        "vkyc_exempt_status": "not_applicable",
        "trade_name": null,
        "merchant_defined_identifier": "kjvbjs324",
        "mid": 30949833,
        "name": "ChAgg5",
        "email": "chagg232509_5@yopmail.com",
        "first_name": "",
        "last_name": "ChAgg5",
        "business_type": "LongTail",
        "bank_update_attempt_count": 0,
        "merchant_vertical": null,
        "partner_source": null,
        "android_url": null,
        "ios_url": null,
        "integration_type": "Tools",
        "integration_status": "Not Integrated",
        "merchant_comments": null,
        "monthly_expected_volume": null,
        "gmv_amount": null,
        "website_approval_status": null,
        "website_url": null,
        "website_remarks": null,
        "registered_mobile": "8447644143",
        "product": "PayUbiz",
        "bank_update_attempt_left": 11,
        "is_service_agreement_accepted": false,
        "is_service_agreement_esigned": false,
        "is_sbqr_addendum_accepted": true,
        "acl_role_name": null,
        "is_authorisation_letter_required": true,
        "saved_kyc_address": null,
        "kyc_status": {
            "status": "LOCKED",
            "kyc_status": "LOCKED"
        },
        "document_status": "Pending",
        "service_intent": "default",
        "nb_eligible": false,
        "lending_eligible": false,
        "offer_engine_enabled": false,
        "revamp_merchant": true,
        "is_cs_eligible": true,
        "onboarding_completed": false,
        "re_kyc_required": false,
        "dashboard_preference": "one_dashboard",
        "migration_status": 0,
        "is_service_agreement_present": false,
        "next_bank_update_time": "2025-11-06T12:26:47.504+05:30",
        "business_pan_name_match": false,
        "mfa_enabled": false,
        "team_mfa_enabled": false,
        "business_category_name": null,
        "business_sub_category_name": null,
        "device": "Desktop",
        "display_name": "ChAgg5",
        "campaign_name": null,
        "campaign_medium": null,
        "campaign_source": null,
        "campaign_term": null,
        "source_url": null,
        "source_type": null,
        "sub_source": null,
        "source_details": null,
        "ubo_exist": false,
        "mobile": "8447644143",
        "new_settlement_embargo": false,
        "lending_interest": false,
        "mobile_disabled": false,
        "re_kyc_document_status": "Pending",
        "re_kyc_kyc_status": {
            "status": "LOCKED",
            "kyc_status": "LOCKED"
        },
        "dormancy_date": null,
        "is_dormant": false,
        "priority_settlement_eligible": false,
        "is_working_hours": true,
        "vkyc_status": null,
        "vkyc": null,
        "working_hours_start_end": "11:00 am - 06:00 pm",
        "stop_onboarding": false,
        "prob_tools": false,
        "logo": null,
        "offline_merchant": false,
        "sf_agent_comments": {
            "latest_comment": null,
            "latest_sf_comment": null,
            "agent_remarks": null,
            "req_doc_category": 127
        },
        "allow_vkyc": true,
        "unlock_steps_till_website": false,
        "allow_sole_prop_tools_onboarding": false,
        "is_good_quality_lead": null,
        "outlet_flow_enabled": false,
        "bundle_subscription_eligible": false,
        "allow_fetch_cin_doc": null,
        "ucic": null,
        "br_exemption": false,
        "dashboard_url": "https://staging.payu.in/business",
        "skip_vkyc_eligible": true,
        "new_ui_enabled": false,
        "business_entity_uuid": null,
        "business_category_uuid": null,
        "business_sub_category_uuid": null,
        "account_uuid": null,
        "merchant_account_uuid": "11f0-badd-c1d3e20c-8834-02975f21d323",
        "product_uuid": "a12c-f114-ce1bac7d-058c-0f95d535aca3",
        "admin_user_uuid": "11f0-9992-2579bcae-a2db-02111e9ad6d9",
        "bank_detail": null,
        "operating_address": null,
        "registration_address": null,
        "business_entity": null,
        "product_account_statuses": [
            {
                "status_type": "WEBSITE",
                "status_value": null,
                "updated_at": "2025-11-06T06:56:45.000Z"
            },
            {
                "status_type": "KYC_DOCUMENTS",
                "status_value": "Pending",
                "updated_at": "2025-11-06T06:56:45.000Z"
            },
            {
                "status_type": "Agreement",
                "status_value": "Not Generated",
                "updated_at": "2025-11-06T06:56:46.000Z"
            },
            {
                "status_type": "RE_KYC_DOCUMENTS",
                "status_value": "Pending",
                "updated_at": "2025-11-06T06:56:46.000Z"
            }
        ],
        "website_detail": null,
        "attached_configs": [
            {
                "id": 7222,
                "name": "skip_onboarding_steps",
                "config": {
                    "onboarding_steps": {
                        "documentation": {
                            "agreement_required": false,
                            "kyc_docs_upload_required": true
                        },
                        "pan_details_required": true,
                        "bank_details_required": true,
                        "website_details_required": false,
                        "business_details_required": true,
                        "aadhar_ckyc_address_required": false,
                        "business_members_details_required": false,
                        "signing_authority_details_required": true
                    }
                },
                "configuration_id": null,
                "active": true,
                "configurable_type": null,
                "configurable_id": null,
                "uuid": "11f0-badd-c2ebbb6a-8834-02975f21d323",
                "created_at": "2025-11-06T06:56:46.000Z",
                "updated_at": "2025-11-06T06:56:46.000Z",
                "record_id": 25636,
                "record_type": "ProductAccount"
            }
        ],
        "kyc_documents": [],
        "cs_plan": null,
        "product_account_detail": {
            "id": 25530,
            "merchant_id": null,
            "dob": null,
            "pep": null,
            "aml_flag": false,
            "created_at": "2025-11-06T06:56:45.000Z",
            "updated_at": "2025-11-06T06:56:46.000Z",
            "uuid": "11f0-badd-c21291a0-8834-02975f21d323",
            "gst_addendum_status": null,
            "sign_up_ip": null,
            "max_same_day_settlement_amt": null,
            "emi_approval_status": null,
            "mcp_approval_status": null,
            "product_account_id": 25636,
            "integration_type": "Tools",
            "integration_status": "Not Integrated",
            "monthly_expected_volume": null,
            "gmv_amount": null,
            "average_delivery_time": null,
            "next_rekyc_date": null,
            "industry_type": null,
            "annual_turnover": null,
            "lead_id": null,
            "city_of_incorporation": null,
            "country_of_incorporation": null,
            "purpose_of_payouts": null,
            "team_mfa_enabled": false,
            "team": null,
            "pg_key": "zuHLVs",
            "flag": 0,
            "priority_settlement_plan": null,
            "mcp_ticket_id": null,
            "uat_merchant_detail": null,
            "ie_code": null,
            "purpose_code": null,
            "dormancy_date": null,
            "business_details_rekyced": null,
            "pep_onboarding_status": null,
            "copy_mid": null,
            "uat_mid": null,
            "lob_status_prerisk": null,
            "screenza_response": null,
            "clw_ticket_id": null,
            "copy_mid_type": null,
            "taxation_id": null,
            "cin_doc_request_id": null,
            "cin_doc_requested_at": null,
            "cin_doc_fetched_at": null,
            "merchant_segment": null,
            "uin_number": null,
            "uin_verification_status": 0,
            "npo": false
        },
        "custom_parameters": [],
        "ultimate_beneficiaries": [],
        "business_members": [],
        "consents": [],
        "signatory_contact_details": []
    }
}
```

* Failure Scenarios

**The token is invalid or expired**

```json
{
    "status": "Unauthorized"
}
```

**The bank details are passed**

```
{
    "errors": {
        "bank_holder_name": [
            "Bank holder name does not match either with business name or pancard name"
        ]
    },
    "error": "does not match either with business name or pancard name"
}
```

## Step 2: Update bank details

After adding the child merchant in[ Step 1: Add a child merchant](##step-1-add-child-merchant), update the bank details of the child merchant using the following request parameters.

<Callout icon="📘" theme="info">
  **Reference**: Generate token using the [Get Client Token API](ref:get-client-token-api) and pass it in header along with the following request parameters.
</Callout>

### Request Parameters

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p> bank_detail<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The details of bank account of the child merchant is specified in the following JSON format. The details of the fields are described in the next table.<br><code>{   &quot;bank_account_number&quot;: &quot;6633809947434&quot;,   &quot;holder_name”:”Harsh Agarwal”,   &quot;ifsc_code&quot;: &quot;ICIC0000031&quot;   }</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

<Callout icon="📘" theme="info">
  **Authorization**: This request is using Bearer Token from the collection. For more information, refer to [Postman Collection](https://documenter.getpostman.com/view/7484238/TVCcZAJC#auth-info-60abdedd-6640-49c8-9497-fe181220c2fd). Merchant access token or client token with scope `refer_child_merchant `from Hub.
</Callout>

The **bank_detail** parameter is in a JSON parameter, and the fields in this parameter are described in the following table:

| Field               | Description                                                                      | Example       |
| ------------------- | -------------------------------------------------------------------------------- | ------------- |
| bank_account_number | The account number of the child merchant is specified in this field.             | 6633809947434 |
| holder_name         | The name of the child merchant who holds the account is specified in this field. | Harsh Agarwal |
| ifsc_code           | The IFSC code of the bank branch where the child merchant has the account.       | ICIC0000031   |

### Sample request

```curl
curl --location -g --request PUT '{{host}}/api/v3/product_accounts/{{product_account_uuid}}' \
--header 'Authorization: Bearer adf9092d141031a6ec1be0e297e91aff313f1c427c384cc18d747b9848a67cbf' \
--header 'Content-Type: application/json' \
--data-raw '{
    "product_account": {
        "bank_detail": {
            "bank_account_number": "123456789",
            "ifsc_code": "SBIN0010650",
            "holder_name": "ABC"
        }
    }
}'
```

### Sample response

```json
{
    "product_account": {
        "mid": 20000012,
        "id": 12,
        "uuid": "11ec-d682-8f22ad2c-a539-38f9d3c6b9ac",
        "identifier": 20000012,
        "product_id": 1,
        "type": "PayUbizAccount",
        "merchant_account_id": 15,
        "active": true,
        "status": null,
        "quality_score": null,
        "business_entity_id": null,
        "business_category_id": null,
        "business_sub_category_id": null,
        "business_name": "Rajat Mishra Corp",
        "pancard_name": null,
        "pancard_number": null,
        "gst_number": "07CPBPP3374Q1Z1",
        "average_delivery_time": 10,
        "notification_email": "rajat.mishra@payu.in",
        "flag": 0,
        "settlement_status": null,
        "merchant_type": null,
        "onboarding_status": "Profile Completion in progress",
        "account_id": null,
        "temp_account_id": null,
        "pan_verification_status": "Pending",
        "admin_user_id": 2,
        "terms_and_condition_accepted_at": null,
        "generate_agreement": "312ad30b7766ec5167ae99e0",
        "agreement_status": null,
        "document_status": "Pending",
        "lob_approval_status": null,
        "created_at": "2022-05-18T08:14:37.000Z",
        "updated_at": "2022-05-18T08:14:37.000Z",
        "partner_uuid": null,
        "business_origin": null,
        "name": "Rajat Mishra",
        "email": "rajat.mishra@payu.in",
        "first_name": "Rajat",
        "last_name": "Mishra",
        "business_type": "LongTail",
        "bank_update_attempt_count": 1,
        "merchant_vertical": null,
        "partner_source": null,
        "android_url": null,
        "ios_url": null,
        "integration_type": "Not Selected",
        "integration_status": "Not Integrated",
        "monthly_expected_volume": 100,
        "gmv_amount": null,
        "website_approval_status": null,
        "website_url": "
www.youtube.com"
,
        "website_remarks": null,
        "registered_mobile": "9582787489",
        "product": "PayUbiz",
        "bank_update_attempt_left": 10,
        "is_service_agreement_accepted": false,
        "is_service_agreement_esigned": false,
        "acl_role_name": null,
        "is_authorisation_letter_required": true,
        "saved_kyc_address": null,
        "kyc_status": {
            "status": "LOCKED",
            "kyc_status": "LOCKED"
        },
        "service_intent": "default",
        "nb_eligible": false,
        "lending_eligible": false,
        "offer_engine_enabled": false,
        "revamp_merchant": false,
        "is_cs_eligible": true,
        "onboarding_completed": false,
        "next_bank_update_time": "2022-05-18T13:44:48.000+05:30",
        "business_pan_name_match": false,
        "business_entity_uuid": null,
        "business_category_uuid": null,
        "business_sub_category_uuid": null,
        "account_uuid": null,
        "merchant_account_uuid": "11ec-d682-8e3639c4-a539-38f9d3c6b9ac",
        "product_uuid": "a12c-f114-ce1bac7d-058c-0f95d535aca3",
        "admin_user_uuid": "11eb-7bef-25b9799a-b893-02f413145cce",
        "bank_detail": {
            "id": 1,
            "branch_name": "VASTRAPUR",
            "bank_account_number": "99999999999",
            "ifsc_code": "UTIB0000032",
            "holder_name": "Tony Stark",
            "nodal_code": null,
            "nodal_status": "Not Activated",
            "active": true,
            "status": 0,
            "penny_deposit_status": "Not Initiated",
            "penny_attempt_count": 0,
            "penny_deposit_method": "IMPS",
            "bank_verification_status": "Pending",
            "uuid": "11ec-d682-8f4262de-a539-38f9d3c6b9ac",
            "created_at": "2022-05-18T08:14:38.000Z",
            "updated_at": "2022-05-18T08:14:38.000Z",
            "bank_name": "AXIS BANK",
            "bank_type": "saving",
            "addendum_status": null,
            "holder_name_by_bank": null,
            "flag": 8,
            "bank_verification_proof": null,
            "penny_attempt_left": 10,
            "bank_error_comments": {
                "error": null,
                "remarks": null
            }
        },
        "operating_address": {
            "id": 24,
            "addressable_id": null,
            "address_type": "Operating",
            "pincode": 110066,
            "city": "South West Delhi",
            "state": "DELHI",
            "address_line": "Operating, UP",
            "uuid": "11ec-d682-8f42e9d4-a539-38f9d3c6b9ac",
            "created_at": "2022-05-18T08:14:38.000Z",
            "updated_at": "2022-05-18T08:14:38.000Z",
            "addressable_type": null,
            "active": true,
            "record_id": 12,
            "record_type": "ProductAccount"
        },
        "registration_address": {
            "id": 23,
            "addressable_id": null,
            "address_type": "Registered",
            "pincode": 110066,
            "city": "South West Delhi",
            "state": "DELHI",
            "address_line": "Registered, UP",
            "uuid": "11ec-d682-8f4431c2-a539-38f9d3c6b9ac",
            "created_at": "2022-05-18T08:14:38.000Z",
            "updated_at": "2022-05-18T08:14:38.000Z",
            "addressable_type": null,
            "active": true,
            "record_id": 12,
            "record_type": "ProductAccount"
        },
        "business_entity": null,
        "product_account_statuses": [
            {
                "id": 4,
                "record_type": null,
                "record_id": null,
                "status_type": "WEBSITE",
                "status_value": null,
                "uuid": "11ec-d682-8fde098c-a539-38f9d3c6b9ac",
                "created_at": "2022-05-18T08:14:38.000Z",
                "updated_at": "2022-05-18T08:14:38.000Z",
                "product_record_id": 12,
                "product_record_type": "ProductAccount"
            },
            {
                "id": 5,
                "record_type": null,
                "record_id": null,
                "status_type": "KYC_DOCUMENTS",
                "status_value": "Pending",
                "uuid": "11ec-d682-8fe20992-a539-38f9d3c6b9ac",
                "created_at": "2022-05-18T08:14:38.000Z",
                "updated_at": "2022-05-18T08:14:38.000Z",
                "product_record_id": 12,
                "product_record_type": "ProductAccount"
            },
            {
                "id": 6,
                "record_type": null,
                "record_id": null,
                "status_type": "Agreement",
                "status_value": "Not Generated",
                "uuid": "11ec-d682-8fe60b46-a539-38f9d3c6b9ac",
                "created_at": "2022-05-18T08:14:38.000Z",
                "updated_at": "2022-05-18T08:14:38.000Z",
                "product_record_id": 12,
                "product_record_type": "ProductAccount"
            }
        ],
        "website_detail": null,
        "attached_configs": [],
        "kyc_documents": [],
        "cs_plan": null,
        "contact_details": [],
        "product_account_detail": {
            "id": 2,
            "merchant_id": null,
            "dob": null,
            "pep": null,
            "aml_flag": false,
            "uuid": "11ec-d682-8ff10d0c-a539-38f9d3c6b9ac",
            "created_at": "2022-05-18T08:14:39.000Z",
            "updated_at": "2022-05-18T08:14:39.000Z",
            "gst_addendum_status": null,
            "sign_up_ip": null,
            "max_same_day_settlement_amt": null,
            "product_account_id": 12,
            "website_url": "
www.youtube.com"
,
            "android_url": null,
            "ios_url": null,
            "integration_type": "Not Selected",
            "integration_status": "Not Integrated",
            "monthly_expected_volume": 100,
            "website_approval_status": null,
            "gmv_amount": null,
            "average_delivery_time": 10
        }
    }
}
```

<br />

## Step 3: Upload Schedule C document

After you add a child merchant, you must upload the Schedule C document for the child merchant. For more information on how to upload the Schedule C document of the child merchant, refer to [Add a Sub-Account](doc:add-a-sub-account).
