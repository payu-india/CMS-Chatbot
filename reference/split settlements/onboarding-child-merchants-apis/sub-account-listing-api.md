---
title: Sub Account Listing API v3
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Sub Account Listing**  API fetches all child merchant details linked to a parent merchant. You must pass the parent merchant MID for the **parent_merchant_uuid** parameter in this request.

HTTP Method: **GET**

**Environment**

|                            |                                                                                    |
| -------------------------- | ---------------------------------------------------------------------------------- |
| **Test Environment**       | \<[https://uat-onepayuonboarding.payu.in>](https://uat-onepayuonboarding.payu.in>) |
| **Production Environment** | \<[https://onboarding.payu.in>](https://onboarding.payu.in>)                       |

## Post parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;">Parameter Type</th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>parent_merchant_uuid</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Path</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter must contain the parent merchant MID.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Authorization<br>Merchant access token or client token with the scope as<strong>fetch_child_merchants</strong> from Hub.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Query</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Bearer {{access_token}}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>search_term</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Query</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter must contain any of the following search term:  </p>
<ul>
<li>identifier</li>
<li>phone</li>
<li>email</li>
<li>name</li>
<li>brand_name</li>
<li>merchant_defined_identifier</li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>search_text</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Query</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><ul>
<li>This parameter must contain the search text.</li>
</ul>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

### Success scenario

```curl
curl --location '{{onboarding_base_url}}/api/v3/product_accounts/{{product_account_uuid}}/sub_accounts?search_term=email&search_text=abcpayu.in' \
 --header 'Authorization: Bearer {{access_token}}' 
```

### Failure Scenario

```curl
curl --location -g --request GET '{{onboarding_base_url}}/api/v3/product_accounts/{{mid}}/sub_accounts' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response Parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>id</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The ID of the child merchant</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>mid</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The mid of the child merchant</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>uuid</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The uuid (Universally unique identifier) of the child merchant</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>product</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter must be passed with the following value: &quot;PayUBiz&quot;</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>device</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The app device used by child merchant to sell the products.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>business_type</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Business type of the child merchant.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>quality_score</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Quality score of the child merchant based on the verification by PayU.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>display_name</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The display name of the child merchant</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>account_id</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Account ID of the child merchant.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>business_entity_id</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The business entity ID of the merchant. The business entity ID and corresponding business entity is listed in the <a href="https://docs.payu.in/docs/partner-category-list">Partner Category List</a> table of this section.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>business_category_id</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The business category ID of the merchant.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>business_sub_category_id</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The business sub category ID of the merchant.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>business_name</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Business name of the merchant, similar to PAN.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>pancard_name</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Name of the child merchant as in the PAN card.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>pancard_number</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>PAN card number of the child merchant.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>website_url</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Website URL of the child merchant</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>ios_url</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>IOS app URL of the merchant.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>business_origin</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Business origin of the merchant.,</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>gst_number</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>GST number of the merchant registered with the Sales tax department.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>integration_type</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The integration type of the merchant. It can be any of the following:  </p>
<ul>
<li>Tools</li>
<li>ThirdParty</li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>routing_mid</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Routing MID is displayed in this parameter</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>average_delivery_time</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Average delivery time of the merchant</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>downjones_check</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Downjones check details by PayU</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>aggregator_type</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Aggregator type for the child merchant</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>monthly_expected_volume</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Monthly expected volume of the child merchant.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>campaign_name</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Campaign name through which the child merchant joined.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>campaign_medium</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Campaign medium through which the child merchant joined.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>campaign_source</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Campaign source through which the child merchant joined.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>campaign_term</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Campaign period of the campaign through which the child merchant joined.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>partner_uuid</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Parent partner UUID of the child merchant</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>created_at</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Child merchant creation timestamp</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>updated_at</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Child merchant details last updated time stamp.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>admin_user_id</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Admin user ID of the child merchant.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>email</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The child merchant email.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>mobile</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Mobile number of the child merchant</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>terms_and_condition_accepted_at</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Timestamp when the Terms and Conditions was accepted by the child merchant.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>website_approval_statu</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Website approval status of the child merchant</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>sub_source</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Sub source of the child merchant.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>account_uuid</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Account UUID of the child merchant.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>pan_verification_status</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>PAN card verification status of the child merchant.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>website_remarks</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Website verification remarks by PayU.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>settlement_status</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Last settlement status of the child merchant.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>source_details</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Source details of the child merchant.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>merchant_vertical</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Child merchant business vertical.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>notification_email</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Email ID of the child merchant to which the notifications need to be sent by PayU</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>bank_update_attempt_count</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Was the bank update attempt was successful by PayU</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>partner_source</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Partner source of the child merchant</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>integration_status</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Integration status of the child merchant</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>merchant_type</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Merchant type will have the value as &quot;Aggregator.&quot;</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>child_aggregator</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Child aggregator if any of the current child merchant.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>shop_number</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Shop telephone number of the child merchant.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>area_code</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Area code of the child merchant.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample Response

### Success Scenario

* When they are searching using date range:

```plaintext
{
    "child_merchants": {
        "product_accounts": [
            {
                "uuid": "11f0-badd-c184cc6c-8834-02975f21d323",
                "created_at": "2025-11-06T06:56:45.000Z",
                "name": null,
                "mid": 30949833,
                "email": "chagg232509_5@yopmail.com",
                "onboarding_completed": false,
                "merchant_defined_identifier": "kjvbjs324",
                "product_account_detail": {
                    "pg_key": "zuHLVs"
                }
            },
            {
                "uuid": "11f0-b3c3-7b4e4f82-9891-02975f21d323",
                "created_at": "2025-10-28T06:01:02.000Z",
                "name": null,
                "mid": 30949599,
                "email": "verynew@payu.in",
                "onboarding_completed": false,
                "merchant_defined_identifier": null,
                "product_account_detail": {
                    "pg_key": "khxBZY"
                }
            },
            {
                "uuid": "11f0-b2fe-eb006fe2-9095-02975f21d323",
                "created_at": "2025-10-27T06:33:58.000Z",
                "name": null,
                "mid": 30949595,
                "email": "random-001@yopmail.com",
                "onboarding_completed": false,
                "merchant_defined_identifier": null,
                "product_account_detail": {
                    "pg_key": "Vm9b40"
                }
            },
            {
                "uuid": "11f0-b2fe-3c5fb7c2-9886-02975f21d323",
                "created_at": "2025-10-27T06:29:05.000Z",
                "name": null,
                "mid": 30949594,
                "email": "test-ayantika0362@yopmail.com",
                "onboarding_completed": false,
                "merchant_defined_identifier": null,
                "product_account_detail": {
                    "pg_key": "7uHKyT"
                }
            },
            {
                "uuid": "11f0-aa65-5517cda0-be46-02975f21d323",
                "created_at": "2025-10-16T07:54:24.000Z",
                "name": "ESSERE DONNA PRIVATE LIMITED",
                "mid": 30949575,
                "email": "prodbugchild@yopmail.com",
                "onboarding_completed": false,
                "merchant_defined_identifier": null,
                "product_account_detail": {
                    "pg_key": "26ooZx"
                }
            },
            {
                "uuid": "11f0-a991-ed793216-af6c-02975f21d323",
                "created_at": "2025-10-15T06:41:09.000Z",
                "name": "PAYU PAYMENTS PRIVATE LIMITED",
                "mid": 30949571,
                "email": "bulk_upload_test1510_1@yopmail.com",
                "onboarding_completed": false,
                "merchant_defined_identifier": "RHFU4739479347",
                "product_account_detail": {
                    "pg_key": "lsjhaK"
                }
            },
            {
                "uuid": "11f0-a5b9-5584539a-a070-02975f21d323",
                "created_at": "2025-10-10T09:13:09.000Z",
                "name": "PAYU PAYMENTS PRIVATE LIMITED",
                "mid": 30949564,
                "email": "bulk_upload_test0910_9@yopmail.com",
                "onboarding_completed": false,
                "merchant_defined_identifier": "YF749347fh7",
                "product_account_detail": {
                    "pg_key": "6qRbp7"
                }
            },
            {
                "uuid": "11f0-a511-2abc3414-aa2c-02975f21d323",
                "created_at": "2025-10-09T13:09:21.000Z",
                "name": "PAYU PAYMENTS PRIVATE LIMITED",
                "mid": 30949562,
                "email": "bulk_upload_test0910_8@yopmail.com",
                "onboarding_completed": false,
                "merchant_defined_identifier": "Vib473948h",
                "product_account_detail": {
                    "pg_key": "FBD9kH"
                }
            },
            {
                "uuid": "11f0-a50e-20468b40-9ce5-02975f21d323",
                "created_at": "2025-10-09T12:47:36.000Z",
                "name": "PAYU PAYMENTS PRIVATE LIMITED",
                "mid": 30949561,
                "email": "bulk_upload_test0910_6@yopmail.com",
                "onboarding_completed": false,
                "merchant_defined_identifier": "hrth5343",
                "product_account_detail": {
                    "pg_key": "Q5bBFY"
                }
            },
            {
                "uuid": "11f0-a50d-25ca373e-8286-02975f21d323",
                "created_at": "2025-10-09T12:40:35.000Z",
                "name": "PAYU PAYMENTS PRIVATE LIMITED",
                "mid": 30949560,
                "email": "bulk_upload_test0910_5@yopmail.com",
                "onboarding_completed": false,
                "merchant_defined_identifier": "7505385",
                "product_account_detail": {
                    "pg_key": "lUwaI1"
                }
            },
            {
                "uuid": "11f0-a508-6794909c-ab71-02975f21d323",
                "created_at": "2025-10-09T12:06:38.000Z",
                "name": "PAYU PAYMENTS PRIVATE LIMITED",
                "mid": 30949559,
                "email": "bulk_upload_test0910_4@yopmail.com",
                "onboarding_completed": false,
                "merchant_defined_identifier": "syguyg8628",
                "product_account_detail": {
                    "pg_key": "vWXP0L"
                }
            },
            {
                "uuid": "11f0-a506-172aff44-9d62-02975f21d323",
                "created_at": "2025-10-09T11:50:05.000Z",
                "name": "AYANTIKA PRAMANICK",
                "mid": 30949558,
                "email": "ayantikaagg005@yopmail.com",
                "onboarding_completed": false,
                "merchant_defined_identifier": null,
                "product_account_detail": {
                    "pg_key": "izWaWz"
                }
            },
            {
                "uuid": "11f0-a4f6-1bd6a116-a645-02975f21d323",
                "created_at": "2025-10-09T09:55:41.000Z",
                "name": "AYANTIKA PRAMANICK",
                "mid": 30949557,
                "email": "ayantikaagg004@yopmail.com",
                "onboarding_completed": true,
                "merchant_defined_identifier": null,
                "product_account_detail": {
                    "pg_key": "HYBdoP"
                }
            },
            {
                "uuid": "11f0-a4df-3828c432-9938-02975f21d323",
                "created_at": "2025-10-09T07:11:48.000Z",
                "name": "AYANTIKA PRAMANICK",
                "mid": 30949556,
                "email": "ayantikaagg003@yopmail.com",
                "onboarding_completed": false,
                "merchant_defined_identifier": null,
                "product_account_detail": {
                    "pg_key": "q3qskb"
                }
            },
            {
                "uuid": "11f0-a4d8-8664b3b0-9938-02975f21d323",
                "created_at": "2025-10-09T06:23:56.000Z",
                "name": "AYANTIKA PRAMANICK",
                "mid": 30949555,
                "email": "ayantikaagg002@yopmail.com",
                "onboarding_completed": false,
                "merchant_defined_identifier": null,
                "product_account_detail": {
                    "pg_key": "lqZCjz"
                }
            },
            {
                "uuid": "11f0-a432-0cf67000-b4b1-02975f21d323",
                "created_at": "2025-10-08T10:32:12.000Z",
                "name": "AYANTIKA PRAMANICK",
                "mid": 30949549,
                "email": "ayantikaagg001@yopmail.com",
                "onboarding_completed": false,
                "merchant_defined_identifier": null,
                "product_account_detail": {
                    "pg_key": "uVflCt"
                }
            },
            {
                "uuid": "11f0-a42b-f7f97072-b68d-02975f21d323",
                "created_at": "2025-10-08T09:48:42.000Z",
                "name": "AYANTIKA PRAMANICK",
                "mid": 30949547,
                "email": "ayantikaagg@yopmail.com",
                "onboarding_completed": false,
                "merchant_defined_identifier": null,
                "product_account_detail": {
                    "pg_key": "djHFIE"
                }
            }
        ]
    },
    "total_childs": 17
}
```

* When using the merchant defined identifier:

```json
{
    "child_merchants": {
        "product_accounts": [
            {
                "uuid": "11f0-badd-c184cc6c-8834-02975f21d323",
                "created_at": "2025-11-06T06:56:45.000Z",
                "name": null,
                "mid": 30949833,
                "email": "chagg232509_5@yopmail.com",
                "onboarding_completed": false,
                "merchant_defined_identifier": "kjvbjs324",
                "product_account_detail": {
                    "pg_key": "zuHLVs"
                }
            }
        ]
    },
    "total_childs": 1
}
```

### Failure Scenarios

Get Child merchants when token is invalid or expired

```plaintext
{
    "status": "Unauthorized"
}
```