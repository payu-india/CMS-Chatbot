---
title: Fetch Child Merchants Details
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
To fetch the child merchant details for a parent merchant:

1. [Get Client Token](#step-1-get-client-token)
2. [Get Sub Account Listing](#step-2-get-sub-account-listing)

## Step 1: Get client token

Use the **get_client_token** API with the scope as **fetch_child_merchants** to create a client token from Hub. For more information, refer to <Anchor label="Get Client Token API" target="_blank" href="ref:get-client-token-api">Get Client Token API</Anchor>

<Callout icon="📘" theme="info">
  **Notes**:

  * Caller client service should be registered on Hub (PayU's oAuth2 Service )
  * **fetch_child_merchants** scope should be whitelisted on caller client on Hub
</Callout>

**Environment**

| Environment    | Domain                                                           |
| -------------- | ---------------------------------------------------------------- |
| **Test**       | \<[https://uat-accounts.payu.in>](https://uat-accounts.payu.in>) |
| **Production** | \<[https://accounts.payu.in>](https://accounts.payu.in>)         |

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location -g --request POST '{{hub_base_url}}/oauth/token' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'client_id={{client_id}}' \
  --data-urlencode 'client_secret={{client_secret}}' \
  --data-urlencode 'grant_type=client_credentials' \
  --data-urlencode 'scope=refer_child_merchant'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-file-code">
  **Success Scenario**

  ```plaintext
  {
    "access_token": "453226e88f0e6d18b24fe4eedb817b0ff096cb740f0354e4b133188555d2b151",
    "token_type": "Bearer",
    "expires_in": 2591999,
    "scope": "refer_child_merchant",
    "created_at": 1642509515
  }
  ```

  **Failure Scenarios**

  * When the `client_id` or secret code is unauthorized:

  ```plaintext
  {
    "error": "invalid_client",
    "error_description": "Client authentication failed due to unknown client, no client authentication included, or unsupported authentication method."
  }
  ```

  * Incorrect scope or non-whitelisted scope:

  ```plaintext
  {
    "error": "invalid_scope",
    "error_description": "The requested scope is invalid, unknown, or malformed."
  }
  ```
</Accordion>

## Step 2: Get sub account listing

Call the **Sub Account Listing** API to fetch all child merchant details linked to a parent merchant. You must pass the UUID in this request. For more information, refer to <Anchor label="Sub Account Listing API" target="_blank" href="ref:sub-account-listing-api">Sub Account Listing API</Anchor>.

<Callout icon="📘" theme="info">
  **Notes**:

  * Use correct Environment URL as base URL in place of \{\{onboarding_base_url}} variable
  * Use parent merchant UUID in place of \{\{merchant_uuid}} variable in request
</Callout>

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location -g --request GET '{{onboarding_base_url}}/api/v1/merchants/{{parent_merchant_uuid}}/sub_accounts' --header 'Authorization: Bearer {{access_token}}'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-code">
  #### Success scenario

  ```plaintext
  {   // List of child merchant and their details under a parent merchant
      "child_merchants": [
          {
              "id": 13044,
              "mid": 7220715,
              "test_mid": null,
              "uuid": "11ec-1c34-13ba0648-b4c9-02053299b2da",
              "product": "PayUmoney",
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
              "business_origin": "PayUmoney",
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
              "created_at": "2021-09-23T06:04:15.000Z",
              "updated_at": "2021-09-23T06:04:15.000Z",
              "admin_user_id": 9952,
              "email": "test.user1.aggregator@payutest.in",
              "mobile": "8860898210",
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
              "notification_email": "test.user1.aggregator@payutest.in",
              "bank_update_attempt_count": 0,
              "partner_source": null,
              "flag": 32,
              "integration_status": "Not Integrated",
              "merchant_type": "child_aggregator",
              "gmv_amount": null,
              "shop_number": null,
              "area_code": null
          },
          {
              "id": 13045,
              "mid": 7220716,
              "test_mid": null,
              "uuid": "11ec-1c34-8946c6a8-b4c9-02053299b2da",
              "product": "PayUmoney",
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
              "business_origin": "PayUmoney",
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
              "created_at": "2021-09-23T06:07:31.000Z",
              "updated_at": "2021-09-23T06:07:31.000Z",
              "admin_user_id": 9953,
              "email": "test.user2.aggregator@payutest.in",
              "mobile": "8860890280",
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
              "notification_email": "test.user2.aggregator@payutest.in",
              "bank_update_attempt_count": 0,
              "partner_source": null,
              "flag": 32,
              "integration_status": "Not Integrated",
              "merchant_type": "child_aggregator",
              "gmv_amount": null,
              "shop_number": null,
              "area_code": null
          },
          {
              "id": 13046,
              "mid": 7220717,
              "test_mid": null,
              "uuid": "11ec-1c35-3684eda4-b4c9-02053299b2da",
              "product": "PayUmoney",
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
              "business_origin": "PayUmoney",
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
              "created_at": "2021-09-23T06:12:21.000Z",
              "updated_at": "2021-09-23T06:12:21.000Z",
              "admin_user_id": 9954,
              "email": "test.user3.aggregator@payutest.in",
              "mobile": "8860890281",
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
              "notification_email": "test.user3.aggregator@payutest.in",
              "bank_update_attempt_count": 0,
              "partner_source": null,
              "flag": 32,
              "integration_status": "Not Integrated",
              "merchant_type": "child_aggregator",
              "gmv_amount": null,
              "shop_number": null,
              "area_code": null
          },
          {
              "id": 13047,
              "mid": 8006683,
              "test_mid": null,
              "uuid": "11ec-1c35-4c1bf900-b4c9-02053299b2da",
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
              "created_at": "2021-09-23T06:12:58.000Z",
              "updated_at": "2021-09-23T06:12:58.000Z",
              "admin_user_id": 9955,
              "email": "test.user4.aggregator@payutest.in",
              "mobile": "8860890282",
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
              "notification_email": "test.user4.aggregator@payutest.in",
              "bank_update_attempt_count": 0,
              "partner_source": null,
              "flag": 32,
              "integration_status": "Not Integrated",
              "merchant_type": "child_aggregator",
              "gmv_amount": null,
              "shop_number": null,
              "area_code": null
          },
          {
              "id": 13048,
              "mid": 8006684,
              "test_mid": null,
              "uuid": "11ec-1c36-066b0ee0-b4c9-02053299b2da",
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
              "created_at": "2021-09-23T06:18:11.000Z",
              "updated_at": "2021-09-23T06:18:11.000Z",
              "admin_user_id": 9956,
              "email": "test.user5.aggregator@payutest.in",
              "mobile": "8860890284",
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
              "notification_email": "test.user5.aggregator@payutest.in",
              "bank_update_attempt_count": 0,
              "partner_source": null,
              "flag": 32,
              "integration_status": "Not Integrated",
              "merchant_type": "child_aggregator",
              "gmv_amount": null,
              "shop_number": null,
              "area_code": null
          },
          {
              "id": 13130,
              "mid": 8006726,
              "test_mid": null,
              "uuid": "11ec-29d9-1753523e-a0b8-02053299b2da",
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
              "created_at": "2021-10-10T14:48:25.000Z",
              "updated_at": "2021-10-10T14:48:25.000Z",
              "admin_user_id": 10049,
              "email": "test.user11.aggregator@payutest.in",
              "mobile": "8860890285",
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
              "notification_email": "test.user11.aggregator@payutest.in",
              "bank_update_attempt_count": 0,
              "partner_source": null,
              "flag": 32,
              "integration_status": "Not Integrated",
              "merchant_type": "child_aggregator",
              "gmv_amount": null,
              "shop_number": null,
              "area_code": null
          },
          {
              "id": 13131,
              "mid": 8006727,
              "test_mid": null,
              "uuid": "11ec-29e1-9b1030da-a0b8-02053299b2da",
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
              "email": "test.user12.aggregator@payutest.in",
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
              "area_code": null
          }
      ]
  }

  ```

  #### Failure Scenario

  * The token is invalid or expired

  ```plaintext
  {
      "status": "Unauthorized"
  }
  ```
</Accordion>
