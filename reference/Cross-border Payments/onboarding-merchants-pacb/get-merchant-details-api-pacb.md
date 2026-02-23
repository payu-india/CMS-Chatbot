---
title: Get Merchant Details API - PACB
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Get Merchant** API is used to get the merchant details. You require the access token to get the merchant details using this API. The access token can be fetched using the Get Token API. For more information, refer to [Get Token API - Partner Integration](ref:get_token_api).

> 📘 Notes:
>
> * The access token with the scope as **refer_merchant** is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).
> * For the **Get Merchant** API , the path parameter is the merchant ID or mid of the merchant. The mid is in the response of the [Create Merchant API](ref:create_merchant_api).

## Environment

<PARTNEROnboardingEnvironment />

## Request parameters

### Path parameters

| Parameter                        | Description                                                                                                                      | Example                              |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| uuid<br /><code>mandatory</code> | <code>string</code> Unique identifier for the merchant. Use the mid (merchant ID) or uuid from the Create Merchant API response. | 11ea-bf88-5c1eb1f4-9363-0acb18027a2a |

### Headers

| Parameter                                 | Description                             | Example                   |
| ----------------------------------------- | --------------------------------------- | ------------------------- |
| Authorization<br /><code>mandatory</code> | Bearer token with scope refer_merchant. | Bearer \{\{access_token}} |
| accept<br /><code>optional</code>         | Use for JSON response.                  | application/json          |

## Sample request

```curl
curl --location -g --request GET '{{partner_base_url}}/api/v1/merchants/7060013' \
--header 'Authorization: bearer \{\{access_token}}'
```

## Sample response

**Success scenario**

```json
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

```json
{
  "status": "Unauthorized"
}
```

* 404: When merchant was not referred by partner

```json
{
  "data": {
    "message": "Invalid merchant mid"
  }
}
```

* 422: When token is not of partner or not valid

```json
{
  "error": "Partner Not Found"
}
```

* 404: When merchant is not found:

```json
{
  "status": "NotFound"
}
```

## Response parameters

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
        business_entity
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
        partner_source
      </td>

      <td>
        This parameter returns the source through which the merchant joined or onboarded.
      </td>
    </tr>

    <tr>
      <td>
        pan_verification_status
      </td>

      <td>
        This parameter contains any of the following PAN verification statuses:

           
        	•	Success  
        	•	Pending  
        	•	Failed
      </td>
    </tr>

    <tr>
      <td>
        website_approval_status
      </td>

      <td>
        This parameter contains any of the following website approval statuses:

           
        	•	Website Not live  
        	•	Website Incomplete  
        	•	Website Under Construction  
        	•	Website Error  
        	•	Website OK  
        	•	Verification in Process
      </td>
    </tr>

    <tr>
      <td>
        notification_email
      </td>

      <td>
        This parameter contains the email to which the notification was sent to the merchant on onboarding.
      </td>
    </tr>

    <tr>
      <td>
        settlement_status
      </td>

      <td>
        This parameter contains any of the following settlement statuses:\

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
        is_service_agreement_accepted
      </td>

      <td>
        This parameter contains the flag whether the service agreement was accepted or not.
      </td>
    </tr>

    <tr>
      <td>
        is_authorisation_letter_required
      </td>

      <td>
        This parameter contains the flag whether the authorization letter is required or not required.
      </td>
    </tr>

    <tr>
      <td>
        monthly_expected_volume
      </td>

      <td>
        This parameter contains the monthly expected volume from the merchant.
      </td>
    </tr>

    <tr>
      <td>
        business_category
      </td>

      <td>
        This parameter contains the business category of the merchant that was provided while onboarding.
      </td>
    </tr>

    <tr>
      <td>
        business_sub_category
      </td>

      <td>
        This parameter contains the business sub-category of the merchant that was provided while onboarding.
      </td>
    </tr>

    <tr>
      <td>
        bank_verification_status
      </td>

      <td>
        This parameter contains any of the following bank verification statuses:\

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
        penny_deposit_status
      </td>

      <td>
        This parameter contains any of the following penny deposit statuses when bank account verification was performed:\

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
        document_status
      </td>

      <td>
        This parameter contains the document status and can be any of the following:

           
        	•	Pending: It indicates that document not yet submitted  
        	•	Docs Received: It indicates that documents are submitted  
        	•	Docs Approved: It indicates that documents are approved  
        	•	Docs Error: It indicates that mismatch in data or wrong document
      </td>
    </tr>
  </tbody>
</Table>
