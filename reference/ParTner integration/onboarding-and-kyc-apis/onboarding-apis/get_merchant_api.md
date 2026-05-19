---
api:
  file: GetMerchant_API_Collection.json
  operationId: GetMerchant
hidden: false
metadata:
  title: Get Merchant Details API
  description: >-
    Learn how to use the PayU Get Merchant Details API to retrieve detailed
    information about merchants. This API Reference page provides comprehensive
    instructions, request parameters, and sample responses for efficient
    merchant management.
---
The **Get Merchant** API is used to get the merchant details. You require the access token to get the merchant details using this API. The access token can be fetched using the Get Token API. For more information, refer to [Get Token API - Partner Integration](ref:get_token_api).

> 📘 Notes:
>
> * The access token with the scope as **refer_merchant** is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).
> * For the **Get Merchant** API , the path parameter is the merchant ID or mid of the merchant. The mid is in the response of the [Create Merchant API](ref:create_merchant_api).

<br />

<Partner_Postman />

<br />

## Environment

<PARTNEROnboardingEnvironment />

<details>
  <summary>Sample request</summary>

  ```curl
  curl --location -g --request GET '{{partner_base_url}}/api/v1/merchants/7060013' \
  --header 'Authorization: bearer {{access_token}}'
  ```
</details>

<details>
  <summary>Sample response</summary>

  **Success scenario**

  ```
  {
    "merchant": {
      "name": "test7_6july20",
      "email": "test3_6july20.aman.garg@payutest.in",
      "registered_mobile": "9466811031",
      "mid": 7060013,
      "product": "PayUmoney",
      "business_type": "LongTail",
      "business_name": null,
      "pancard_name": null,
      "pancard_number": null,
      "website_url": null,
      "android_url": null,
      "ios_url": null,
      "gst_number": null,
      "created_at": "2020-07-06T12:58:17.000Z",
      "mobile": "9466811031",
      "blocked": false,
      "first_name": "",
      "last_name": "test7_6july20",
      "bank_detail": {
        "bank_account_number": null,
        "ifsc_code": null,
        "holder_name": null,
        "nodal_code": null,
        "nodal_status": "Not Activated"
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
      "business_entity": null,
      "status": "account_created",
      "partner_source": "Create Merchant API",
      "pan_verification_status": "Pending",
      "website_approval_status": "Not Applicable",
      "notification_email": "test3_6july20.aman.garg@payutest.in",
      "settlement_status": null,
      "is_service_agreement_accepted": false,
      "is_authorisation_letter_required": true,
      "monthly_expected_volume": null,
      "business_category": null,
      "business_sub_category": null,
      "bank_verification_status": null,
      "penny_deposit_status": null,
      "uuid": "11ea-bf88-5c1eb1f4-9363-0acb18027a2a",
      "document_status": "Pending"
    }
  }
  ```

  **Failure Scenarios**

  * 401: Unauthorised request

  ```plaintext
  {
    "status": "Unauthorized"
  }
  ```

  * 404: When merchant was not referred by partner

  ```plaintext
  {
    "data": {
      "message": "Invalid merchant mid"
    }
  }
  ```

  * 422: When token is not of partner or not valid

  ```plaintext
  {
    "error": "Partner Not Found"
  }
  ```

  * 404: When merchant is not found:

  ```plaintext
  {
    "status": "NotFound"
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
          This parameter contains any of the following statuses:

          ```
          * account_created
          * profile_completed
          * bank_verified
          * documents_pending
          * document_upload_in_progress
          * document_verification_in_progress
          * documents_rejected
          * website_verification_in_progress
          * website_error
          * agreement_pending
          * agreement_rejected
          * profile_rejected
          * live
          * settlement_on_hold
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

## Request parameters
