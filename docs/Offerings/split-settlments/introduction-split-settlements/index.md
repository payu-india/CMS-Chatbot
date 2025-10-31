---
title: Onboarding Child Merchants Workflow - Split Settlements
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
After you create a merchant using the** Create a PayU Merchant** API, you can onboard child merchants. For more information, refer to [Create Merchant API](ref:create_merchant_api) under API Reference.

The steps involved in creating a child merchant are:

1. [Get Client Token API](ref:get-client-token-api)
2. [Create Child Merchant API](ref:create-child-merchant-api)

<Callout icon="📘" theme="info">
  **Note**: Before you onboard child merchants, ensure you have followed the [Prerequisites](#prerequisites) (one-time).
</Callout>

## Domains

### Common onboarding

|                        |                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------- |
| Test Environment       | \<[https://uat-onepayuonboarding.payu.in>](https://uat-onepayuonboarding.payu.in>) |
| Production Environment | \<[https://onboarding.payu.in>](https://onboarding.payu.in>)                       |

### Hub service domains

|                        |                                                                  |
| ---------------------- | ---------------------------------------------------------------- |
| Test Environment       | \<[https://uat-accounts.payu.in>](https://uat-accounts.payu.in>) |
| Production Environment | \<[https://accounts.payu.in>](https://accounts.payu.in>)         |

## Prerequisites

Before you onboard child merchants, you need to ensure the following (one-time process):

* Caller client service should be registered on Hub (PayU’s oAuth2 Service ) with the details as described in the following table:

| **Field**                   | **Description**                                                                                                                               |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Customer Name               | The legal name of the customer.                                                                                                               |
| Customer Service Name       | The service name of the customer.                                                                                                             |
| Customer Owner phone number | The phone number of the owner who is assigned for the customer.                                                                               |
| Customer Owner Email        | The customer owner’s email ID.                                                                                                                |
| Scopes                      | The scope to be whitelisted on the client must be **refer_child_merchant**                                                                    |
| Grant type                  | The grant type must be specified as **client_credentials** in this field.                                                                     |
| Client type                 | Provide **External** as input since you are outside the PayU ecosystem.                                                                       |
| Access Token Expiry Time    | The access token expiry time from the times of creation (in seconds). There is no defined limit for configuring the access token expiry time. |

## Step 1: Get client token

Use the **Get Client Token** API with the scope as **refer_child_merchant** to create a client token from Hub. For more information, refer to [Get Client Token API](ref:get-client-token-api).

**Environment**

|                |                                                                  |
| :------------- | :--------------------------------------------------------------- |
| **Test**       | \<[https://uat-accounts.payu.in>](https://uat-accounts.payu.in>) |
| **Production** | \<[https://accounts.payu.in>](https://accounts.payu.in>)         |

## Sample request

```curl
curl --location -g --request POST '{{hub_base_url}}/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id={{client_id}}' \
--data-urlencode 'client_secret={{client_secret}}' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode 'scope=refer_child_merchant'
```

## Sample response

The following sample response for each scenario is in JSON format:

* Create Child Merchant is Successful

```plaintext
{
    "access_token": "453226e88f0e6d18b24fe4eedb817b0ff096cb740f0354e4b133188555d2b151",
    "token_type": "Bearer",
    "expires_in": 2591999,
    "scope": "refer_child_merchant",
    "created_at": 1642509515
}
```

* When the client_ID or secret code is unauthorised:

```plaintext
{
    "error": "invalid_client",
    "error_description": "Client authentication failed due to unknown client, no client authentication included, or unsupported authentication method."
}
```

* Incorrect scope or non-whitelisted scope

```plaintext
{
    "error": "invalid_scope",
    "error_description": "The requested scope is invalid, unknown, or malformed."
}
```

## Step 2: Create a child merchant

You can create child merchants using the **Create Child Merchant** API. For more information, refer to [Create Child Merchant API](ref:create-child-merchant-api) under API Reference.

### Sample request

```curl
curl --location --request POST 'https://onboarding.payu.in/api/v3/product_accounts' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer bearer undefined' \
--header 'Cookie: _merchant_onboarding_session=P2Tk%2BvUW2y9TFk5N2jUeWNrtatIy1czXutTj4JNWqBtMBq5Zb6FYPk9Eg3blgksVkAZHN1ZTVdKgvTwk6HEiN0UJlFxbjUpxV9b1VMz7GNZBc3X%2FBj2Kl2enn3YDfJMkoWYFisXowdXgjvORlTU9fKRL3mQldqSlZaI5ZPIA5sdYsgNjuVsJXh2j9VsNrez3y9uE%2F1a2D3ZB%2BApNOOHCV2OehGb%2FsvrDKE9TG%2FusAbPEXdKbPqb73DELFIRxvsm6x%2FHKGJQsZCJCHnBY7e0cy%2FklmIiIqfSxkOtCzbikyK7WgjLxxsqHhlskTY9M%2BjZmmLRURbUyuOf4uetDq%2FHFtou8kuJ7xIqyB2HPOIdNH%2BepBrN4gYxHJDg4YYbTZmPp9%2FIj8DYbd%2BchnRvavc2uUqDO0EDBql%2FUmq4DlgHBgTVb%2BP4Lxr6O5tnZ9Y6IDCehUKwdA47Cv8FJzOZJADRCqWvwdP%2BANtuei1yBan6RTRgXdZN%2BeAVncXe8SXBSebCgV1nae3AbW%2BDBtqWtsShlg%2BMYsA%2FahBJgwoKrEeR%2Fb6dyWIxiP6OTCTlKPaqxYyjZP1e8MaBrNuX%2FSleuukgIILD1UIEZOIgh5RvDtIsYn%2F%2FqjqxRw43oNVF9TSMVy1F3W18ShPAzAraUukdT9dCwKEA3XY2nVKj4fs4%2F3qzZBjXsKnYtHw51K6XGa7bfvse%2BRPg1dt3xiT6Sdse2Kt5YMpwelKvfbQU1tV5D%2BFICGAnyDMQW8YiFpumg8x5%2BjyrQxRa070DkpAkJ05xbF6YmDurUDIAI%2F5fOPfL%2BPmv3K2psaF2hgrb8VOovjjmplskcmo9jVjBI%2Ba4FRl20tGHcAl2BTiTmTrFIBu0%2BoC3EhYbpcjxYXZk5K1G%2B64g%3D--Sv3HMr8jMcY8UAsH--nCeKeC14tMJNR%2FUzIDJsGg%3D%3D' \
--data-raw '{
    "product_account": {
        "product":"PayUbiz",
        "name":"Gauri Gupta",
        "email":"bflsonartest11@payu.in",
        "mobile":"7310000001",
        "aggregator_parent_mid":"8815827",
        "merchant_type":"aggregator",
        "pancard_number":"CZMPG3718G",
        "pancard_name":"GAURI GUPTA",
        "business_entity_id":14
      }
}'
```

### Sample Response

#### Success Scenario

Create Child Merchant Success Scenario

```plaintext
{
    "merchant": {
        "name": "Merchant",
        "email": "test.user12.aggregator@payutest.in", // email
        "registered_mobile": "8860890286",
        "id": 13131,
        "mid": 8006727, // MID of Child merchant
        "test_mid": null,
        "uuid": "11ec-29e1-9b1030da-a0b8-02053299b2da", // Child merchant uuid
        "product": "PayUbiz",
        "device": "Other",
        "business_type": "LongTail",
        "quality_score": null,
        "display_name": "Merchant",
        "account_id": null,
        "business_entity_id": null,
        "business_category_id": null,
        "business_sub_category_id": null,
        "business_name": null,
        "pancard_name": null,
        "pancard_number": null,
        "website_url": null,
        "android_url": null,
        "ios_url": null,
        "business_origin": "SMB-ENT",
        "gst_number": null,
        "integration_type": "Not Selected",
        "routing_mid": null,
        "average_delivery_time": null,
        "downjones_check": null,
        "aggregator_model": null,
        "aggregator_type": null,
        "monthly_expected_volume": null,
        "sap_id": null,
        "source_type": null,
        "active": true,
        "source_url": null,
        "campaign_name": null,
        "campaign_medium": null,
        "campaign_source": null,
        "campaign_term": null,
        "partner_uuid": null,
        "created_at": "2021-10-10T15:49:14.000Z",
        "updated_at": "2021-10-10T15:49:14.000Z",
        "admin_user_id": 10050,
        "mobile": "8860890286",
        "terms_and_condition_accepted_at": null,
        "website_approval_status": null,
        "sub_source": null,
        "account_uuid": null,
        "blocked": false,
        "pan_verification_status": "Pending",
        "website_remarks": null,
        "settlement_status": null,
        "source_details": null,
        "merchant_vertical": null,
        "notification_email": "test.user12.aggregator@payutest.in",
        "bank_update_attempt_count": 0,
        "partner_source": null,
        "flag": 32,
        "integration_status": "Not Integrated",
        "merchant_type": "child_aggregator",
        "gmv_amount": null,
        "shop_number": null,
        "area_code": null,
        "bank_update_attempt_left": 11,
        "business_entity_uuid": null,
        "business_category_uuid": null,
        "business_sub_category_uuid": null,
        "first_name": "",
        "last_name": "Merchant",
        "is_service_agreement_accepted": false,
        "is_service_agreement_esigned": false,
        "is_authorisation_letter_required": true,
        "acl_role_name": null,
        "dashboard_preference": "one_dashboard",
        "next_bank_update_time": "2021-10-10T21:19:14.916+05:30",
        "business_pan_name_match": false,
        "admin_user_uuid": "11ec-29e1-b00fb80c-9f40-02f413145cce",
        "contact_details": [],
        "migration_status": 0,
        "saved_kyc_address": null,
        "document_status": "Pending",
        "kyc_status": {
            "kyc_status": "LOCKED"
        },
        "service_intent": "default",
        "revamp_merchant": true,
        "is_cs_eligible": true,
        "bank_detail": null,
        "operating_address": null,
        "registration_address": null,
        "business_entity": null,
        "merchant_statuses": [
            {
                "id": 28277,
                "record_type": "Merchant",
                "record_id": 13131,
                "status_type": "WEBSITE",
                "status_value": null,
                "uuid": "11ec-29e1-9e9a998e-a0b8-02053299b2da",
                "created_at": "2021-10-10T15:49:14.000Z",
                "updated_at": "2021-10-10T15:49:14.000Z"
            },
            {
                "id": 28278,
                "record_type": "Merchant",
                "record_id": 13131,
                "status_type": "KYC_DOCUMENTS",
                "status_value": "Pending",
                "uuid": "11ec-29e1-9ea4fc94-a0b8-02053299b2da",
                "created_at": "2021-10-10T15:49:14.000Z",
                "updated_at": "2021-10-10T15:49:14.000Z"
            },
            {
                "id": 28279,
                "record_type": "Merchant",
                "record_id": 13131,
                "status_type": "Agreement",
                "status_value": "Not Generated",
                "uuid": "11ec-29e1-9eafdc2c-a0b8-02053299b2da",
                "created_at": "2021-10-10T15:49:14.000Z",
                "updated_at": "2021-10-10T15:49:14.000Z"
            }
        ],
        "account_statuses": [],
        "website_detail": null,
        "attached_configs": [],
        "kyc_documents": [],
        "cs_plan": null,
        "website_pages": [],
        "product_account_detail": null
    }
}
```

#### Failure Scenarios

* The token is invalid or expired

```plaintext
{
    "status": "Unauthorized"
}
```

## Step 3: Update Bank Details

After adding the child merchant in[ Step 2: Create a child merchant](#step 2:-create-a-child-merchant), update the bank details of the child merchant using the **Create Child Merchant** API again. For more information, refer to [Create Child Merchant API](ref:create-child-merchant-api) under API Reference.

### Sample request

```
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

```
{
    "merchant": {
        "name": "Merchant",
        "email": "test.user12.aggregator@payutest.in", // email
        "registered_mobile": "8860890286",
        "id": 13131,
        "mid": 8006727, // MID of Child merchant
        "test_mid": null,
        "uuid": "11ec-29e1-9b1030da-a0b8-02053299b2da", // Child merchant uuid
        "product": "PayUbiz",
        "device": "Other",
        "business_type": "LongTail",
        "quality_score": null,
        "display_name": "Merchant",
        "account_id": null,
        "business_entity_id": null,
        "business_category_id": null,
        "business_sub_category_id": null,
        "business_name": null,
        "pancard_name": null,
        "pancard_number": null,
        "website_url": null,
        "android_url": null,
        "ios_url": null,
        "business_origin": "SMB-ENT",
        "gst_number": null,
        "integration_type": "Not Selected",
        "routing_mid": null,
        "average_delivery_time": null,
        "downjones_check": null,
        "aggregator_model": null,
        "aggregator_type": null,
        "monthly_expected_volume": null,
        "sap_id": null,
        "source_type": null,
        "active": true,
        "source_url": null,
        "campaign_name": null,
        "campaign_medium": null,
        "campaign_source": null,
        "campaign_term": null,
        "partner_uuid": null,
        "created_at": "2021-10-10T15:49:14.000Z",
        "updated_at": "2021-10-10T15:49:14.000Z",
        "admin_user_id": 10050,
        "mobile": "8860890286",
        "terms_and_condition_accepted_at": null,
        "website_approval_status": null,
        "sub_source": null,
        "account_uuid": null,
        "blocked": false,
        "pan_verification_status": "Pending",
        "website_remarks": null,
        "settlement_status": null,
        "source_details": null,
        "merchant_vertical": null,
        "notification_email": "test.user12.aggregator@payutest.in",
        "bank_update_attempt_count": 0,
        "partner_source": null,
        "flag": 32,
        "integration_status": "Not Integrated",
        "merchant_type": "child_aggregator",
        "gmv_amount": null,
        "shop_number": null,
        "area_code": null,
        "bank_update_attempt_left": 11,
        "business_entity_uuid": null,
        "business_category_uuid": null,
        "business_sub_category_uuid": null,
        "first_name": "",
        "last_name": "Merchant",
        "is_service_agreement_accepted": false,
        "is_service_agreement_esigned": false,
        "is_authorisation_letter_required": true,
        "acl_role_name": null,
        "dashboard_preference": "one_dashboard",
        "next_bank_update_time": "2021-10-10T21:19:14.916+05:30",
        "business_pan_name_match": false,
        "admin_user_uuid": "11ec-29e1-b00fb80c-9f40-02f413145cce",
        "contact_details": [],
        "migration_status": 0,
        "saved_kyc_address": null,
        "document_status": "Pending",
        "kyc_status": {
            "kyc_status": "LOCKED"
        },
        "service_intent": "default",
        "revamp_merchant": true,
        "is_cs_eligible": true,
        "bank_detail": null,
        "operating_address": null,
        "registration_address": null,
        "business_entity": null,
        "merchant_statuses": [
            {
                "id": 28277,
                "record_type": "Merchant",
                "record_id": 13131,
                "status_type": "WEBSITE",
                "status_value": null,
                "uuid": "11ec-29e1-9e9a998e-a0b8-02053299b2da",
                "created_at": "2021-10-10T15:49:14.000Z",
                "updated_at": "2021-10-10T15:49:14.000Z"
            },
            {
                "id": 28278,
                "record_type": "Merchant",
                "record_id": 13131,
                "status_type": "KYC_DOCUMENTS",
                "status_value": "Pending",
                "uuid": "11ec-29e1-9ea4fc94-a0b8-02053299b2da",
                "created_at": "2021-10-10T15:49:14.000Z",
                "updated_at": "2021-10-10T15:49:14.000Z"
            },
            {
                "id": 28279,
                "record_type": "Merchant",
                "record_id": 13131,
                "status_type": "Agreement",
                "status_value": "Not Generated",
                "uuid": "11ec-29e1-9eafdc2c-a0b8-02053299b2da",
                "created_at": "2021-10-10T15:49:14.000Z",
                "updated_at": "2021-10-10T15:49:14.000Z"
            }
        ],
        "account_statuses": [],
        "website_detail": null,
        "attached_configs": [],
        "kyc_documents": [],
        "cs_plan": null,
        "website_pages": [],
        "product_account_detail": null
    }
}
```

<br />

After you onboard your child merchants, you can fetch the child merchant details as described in the following API Reference sections:

* [Fetch Child Merchants Details](doc:fetch-child-merchants-details-1)
* [Sub Account Listing API](ref:sub-account-listing-v3-api)

<br />
