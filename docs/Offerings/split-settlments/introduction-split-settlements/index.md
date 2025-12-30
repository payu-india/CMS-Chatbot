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
After you create a merchant using the **Create a PayU Merchant** API, you can onboard child merchants. For more information, refer to [Create Merchant API](ref:create_merchant_api) under API Reference.

The steps involved in creating a child merchant are:

1. [Get Client Token API](ref:get-client-token-api)
2. [Create Child Merchant API](ref:create-child-merchant-api)

<Callout icon="📘" theme="info">
  **Note**: Before you onboard child merchants, ensure you have followed the [Prerequisites](#prerequisites) (one-time).
</Callout>

***

### Domains

<Accordion title="Common onboarding" icon="fa-table">
  | Environment            | Domain                                                                             |
  | ---------------------- | ---------------------------------------------------------------------------------- |
  | Test Environment       | \<[https://uat-onepayuonboarding.payu.in>](https://uat-onepayuonboarding.payu.in>) |
  | Production Environment | \<[https://onboarding.payu.in>](https://onboarding.payu.in>)                       |
</Accordion>

<Accordion title="Hub Service Domains" icon="fa-table">
  | Environment            | Domain                                                           |
  | ---------------------- | ---------------------------------------------------------------- |
  | Test Environment       | \<[https://uat-accounts.payu.in>](https://uat-accounts.payu.in>) |
  | Production Environment | \<[https://accounts.payu.in>](https://accounts.payu.in>)         |
</Accordion>

***

## Prerequisites

Before you onboard child merchants, you need to ensure the following (one-time process):

* Caller client service should be registered on Hub (PayU's oAuth2 Service) with the details as described in the following table:

| **Field**                   | **Description**                                                                                                                               |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Customer Name               | The legal name of the customer.                                                                                                               |
| Customer Service Name       | The service name of the customer.                                                                                                             |
| Customer Owner phone number | The phone number of the owner who is assigned for the customer.                                                                               |
| Customer Owner Email        | The customer owner's email ID.                                                                                                                |
| Scopes                      | The scope to be whitelisted on the client must be **refer_child_merchant**                                                                    |
| Grant type                  | The grant type must be specified as **client_credentials** in this field.                                                                     |
| Client type                 | Provide **External** as input since you are outside the PayU ecosystem.                                                                       |
| Access Token Expiry Time    | The access token expiry time from the times of creation (in seconds). There is no defined limit for configuring the access token expiry time. |

***

## Step 1: Get client token

Use the **Get Client Token** API with the scope as **refer_child_merchant** to create a client token from Hub. For more information, refer to [Get Client Token API](ref:get-client-token-api).

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

***

## Step 2: Create a child merchant

You can create child merchants using the **Create Child Merchant** API. For more information, refer to [Create Child Merchant API](ref:create-child-merchant-api) under API Reference.

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location --request POST 'https://onboarding.payu.in/api/v3/product_accounts' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer bearer undefined' \
  --data-raw '{
  	"product_account": {
  		"product": "PayUbiz",
  		"name": "Gauri Gupta",
  		"email": "bflsonartest11@payu.in",
  		"mobile": "7310000001",
  		"aggregator_parent_mid": "8815827",
  		"merchant_type": "aggregator",
  		"pancard_number": "CZMPG3718G",
  		"pancard_name": "GAURI GUPTA",
  		"business_entity_id": 14
  	}
  }'
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-file-code">
  <Accordion title="Success Scenario" icon="fa-check-circle">
    ```plaintext
    {
      "merchant": {
        "name": "Merchant",
        "email": "test.user12.aggregator@payutest.in", // email
        "registered_mobile": "8860890286",
        "id": 13131,
        "mid": 8006727, // MID of Child merchant
        "uuid": "11ec-29e1-9b1030da-a0b8-02053299b2da", // Child merchant uuid
        "product": "PayUbiz",
        "merchant_type": "child_aggregator",
        "created_at": "2021-10-10T15:49:14.000Z",
        "updated_at": "2021-10-10T15:49:14.000Z"
      }
    }
    ```
  </Accordion>

  <Accordion title="Failure Scenarios" icon="fa-exclamation-triangle">
    * The token is invalid or expired

    ```plaintext
    {
      "status": "Unauthorized"
    }
    ```
  </Accordion>
</Accordion>

***

## Step 3: Update Bank Details

After adding the child merchant in [Step 2: Create a child merchant](#step-2-create-a-child-merchant), update the bank details of the child merchant using the **Create Child Merchant** API again. For more information, refer to [Create Child Merchant API](ref:create-child-merchant-api) under API Reference.

<Accordion title="Sample request" icon="fa-code">
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
</Accordion>

<Accordion title="Sample response" icon="fa-file-code">
  ```plaintext
  {
    "merchant": {
      "name": "Merchant",
      "email": "test.user12.aggregator@payutest.in", // email
      "registered_mobile": "8860890286",
      "id": 13131,
      "mid": 8006727, // MID of Child merchant
      "uuid": "11ec-29e1-9b1030da-a0b8-02053299b2da", // Child merchant uuid
      "product": "PayUbiz",
      "merchant_type": "child_aggregator",
      "created_at": "2021-10-10T15:49:14.000Z",
      "updated_at": "2021-10-10T15:49:14.000Z",
      "pan_verification_status": "Pending",
      "integration_status": "Not Integrated"
    }
  }
  ```
</Accordion>

***

After you onboard your child merchants, you can fetch the child merchant details as described in the following API Reference sections:

* [Fetch Child Merchants Details](doc:fetch-child-merchants-details-1)
* [Sub Account Listing API](ref:sub-account-listing-v3-api)

***
