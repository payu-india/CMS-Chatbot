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

## Sample response

<details>
  <summary>Sample response</summary>

  ```
  {
    "merchant": {
      "name": "test",
      "email": "test@payu.in",
      "registered_mobile": "9999910014",
      "mid": 129463,
      "product": "PayUbiz",
      "business_type": "LongTail",
      "business_name": "Test",
      "pancard_name": "Test",
      "pancard_number": "ABCPG1234J",
      "cin_number":"U72400MH2006PTC293037",
      "website_url": null,
      "android_url": null,
      "ios_url": null,
      "gst_number": null,
      "created_at": "2020-12-08T11:03:56.000Z",
      "mobile": "9999910014",
      "blocked": false,
      "first_name": "",
      "last_name": "test",
      "bank_detail": {
        "bank_account_number": "234567891",
        "ifsc_code": "ICIC0000734",
        "holder_name": "Test"
      },
      "operating_address": {
        "address_line": "operational addr",
        "city": "Sant Ravidas Nagar",
        "state": "UTTAR PRADESH",
        "pincode": 221304
      },
      "registration_address": {
        "address_line": "busenaddres line",
        "city": "Sant Ravidas Nagar",
        "state": "UTTAR PRADESH",
        "pincode": 221303
      },
      "business_entity": "LLP",
      "status": "account_created",
      "partner_source": "Create Merchant API",
      "pan_verification_status": "Pending",
      "website_approval_status": "Pending",
      "notification_email": "test@payu.in",
      "settlement_status": null,
      "is_service_agreement_accepted": false,
      "is_authorisation_letter_required": false,
      "monthly_expected_volume": 120000,
      "business_category": "Ecommerce",
      "business_sub_category": "Flowers and Gifts",
      "bank_verification_status": "Pending",
      "uuid": "11eb-3945-0fcf623a-86d9-026e3e71538e",
      "penny_deposit_status": "Not Initiated",
      "signing_authority": {
        "name": "test_auth",
        "email": "test_auth@payu.in"
      },
      "director1_details": {
        "name": "test1_dir",
        "email": "test1_dir@payu.in"
      },
      "director2_details": {
        "name": "test2_dir",
        "email": "test2_dir@payu.in"
      }
    }
  }
  ```
</details>

<details>
  <summary>Response parameters</summary>

  <Table>
    <thead>
      <tr>
        <th>
          **Parameter**
        </th>

        <th>
          **Description**
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          merchant
        </td>

        <td>
          This parameter contains the following details of the merchant in an array format.
        </td>
      </tr>

      <tr>
        <td>
          business\_entity
        </td>

        <td>
          This parameter contains the business entity of the merchant that was provided while onboarding.
        </td>
      </tr>

      <tr>
        <td>
          status
        </td>

        <td>
          This parameter contains any of the following statuses:\\

          ```
          •	documents_pending
          •	bank_verified
          •	document_upload_in_progress
          •	account_created
          •	document_verification_in_progress
          •	website_verification_in_progress
          •	documents_rejected
          •	live
          •	settlement_on_hold
          •	agreement_pending
          •	agreement_rejected
          •	not_available
          •	website_error
          •	profile_rejected
          •	documents_pending
          •	bank_verified
          •	document_upload_in_progress
          •	account_created
          •	document_verification_in_progress
          •	website_verification_in_progress
          •	documents_rejected
          •	live
          •	settlement_on_hold
          •	agreement_pending
          •	agreement_rejected
          •	not_available
          •	website_error
          •	profile_rejected
          ```
        </td>
      </tr>

      <tr>
        <td>
          partner\_source
        </td>

        <td>
          This parameter returns the source through which the merchant joined or onboarded.
        </td>
      </tr>

      <tr>
        <td>
          pan\_verification\_status
        </td>

        <td>
          This parameter contains any of the following PAN verification statuses:

           \
          &#x9;•	Success\
          &#x9;•	Pending\
          &#x9;•	Failed
        </td>
      </tr>

      <tr>
        <td>
          website\_approval\_status
        </td>

        <td>
          This parameter contains any of the following website approval statuses:

           \
          &#x9;•	Website Not live\
          &#x9;•	Website Incomplete\
          &#x9;•	Website Under Construction\
          &#x9;•	Website Error\
          &#x9;•	Website OK\
          &#x9;•	Verification in Process
        </td>
      </tr>

      <tr>
        <td>
          notification\_email
        </td>

        <td>
          This parameter contains the email to which the notification was sent to the merchant on onboarding.
        </td>
      </tr>

      <tr>
        <td>
          settlement\_status
        </td>

        <td>
          This parameter contains any of the following settlement statuses:\\

          ```
          •	Risk Hold
          •	Thirdparty Hold
          •	Active
          •	Suspended
          •	Risk & Thirdparty hold
          •	NEFT Return
          •	Terminate
          ```
        </td>
      </tr>

      <tr>
        <td>
          is\_service\_agreement\_accepted
        </td>

        <td>
          This parameter contains the flag whether the service agreement was accepted or not.
        </td>
      </tr>

      <tr>
        <td>
          is\_authorisation\_letter\_required
        </td>

        <td>
          This parameter contains the flag whether the authorization letter is required or not required.
        </td>
      </tr>

      <tr>
        <td>
          monthly\_expected\_volume
        </td>

        <td>
          This parameter contains the monthly expected volume from the merchant.
        </td>
      </tr>

      <tr>
        <td>
          business\_category
        </td>

        <td>
          This parameter contains the business category of the merchant that was provided while onboarding.
        </td>
      </tr>

      <tr>
        <td>
          business\_sub\_category
        </td>

        <td>
          This parameter contains the business sub-category of the merchant that was provided while onboarding.
        </td>
      </tr>

      <tr>
        <td>
          bank\_verification\_status
        </td>

        <td>
          This parameter contains any of the following bank verification statuses:\\

          ```
          •	Pending
          •	Success
          •	Verification Attempts Exhausted
          •	Failed
          ```
        </td>
      </tr>

      <tr>
        <td>
          penny\_deposit\_status
        </td>

        <td>
          This parameter contains any of the following penny deposit statuses when bank account verification was performed:\\

          ```
          •	Not Initiated
          •	Pending
          •	SENT_TO_BANK
          •	Success
          •	Failed
          ```
        </td>
      </tr>

      <tr>
        <td>
          uuid
        </td>

        <td>
          This parameter contains the Universal Unique Identifier (UUID).
        </td>
      </tr>

      <tr>
        <td>
          document\_status
        </td>

        <td>
          This parameter contains the document status and can be any of the following:

           \
          &#x9;•	Pending: It indicates that document not yet submitted\
          &#x9;•	Docs Received: It indicates that documents are submitted\
          &#x9;•	Docs Approved: It indicates that documents are approved\
          &#x9;•	Docs Error: It indicates that mismatch in data or wrong document
        </td>
      </tr>
    </tbody>
  </Table>
</details>

## Request Parameters

<details>
  <summary>Reference information for request parameters</summary>

  | Parameter                          | Reference                                                                                                                  |
  | :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
  | merchant\[business\_category]      | For the list of business categories, refer to [Business. Category List](ref:partner-category-list).                        |
  | merchant\[business\_entity\_type]  | For the list of business entity type, refer to [Business Entity Type](ref:partner-category-list#business-entity-type).     |
  | merchant\[business\_sub\_category] | For the list of business subcategories, refer to [Business Sub-Category](ref:partner-category-list#business-sub-category). |
</details>