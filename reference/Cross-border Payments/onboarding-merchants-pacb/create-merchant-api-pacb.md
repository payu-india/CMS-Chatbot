---
title: Create Merchant API - PACB
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Create Merchant** API creates a new merchant account on PayU and posts all KYC details. This API returns the Merchant ID (MID) in the response.

> 📘 Note:
>
> After using this API to create merchants, you can use the Update Merchant API to update the merchant details. For more information, refer to [Update Merchant Details API](ref:update_merchant_details_api).

### Authentication

This API is authorised through a client token generated using the client ID and secret. To create a token, call the get token API with `refer merchant` as a scope. Refer to the [Get Token API](ref:get_token_api) doc for more information.

> ❗️ Important considerations for using this API
>
> 1. The mobile, PAN number, GSTIN passed in the request has to be valid as checks are performed in real-time.
> 2. If Business Entity type is passed in the create merchant API, ensure that the PAN also belongs to the same entity.

## Request Parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        merchant\[display\_name]<br /><code>mandatory</code>
      </td>

      <td>
        <code>string</code> The display name of the merchant shown on PayU dashboard and reports. This is the "brand name" under which they are operating.
      </td>

      <td>
        Merchant.com
      </td>
    </tr>

    <tr>
      <td>
        merchant\[email]<br /><code>mandatory</code>
      </td>

      <td>
        <code>string</code> Primary email address of the merchant for communication and notifications.

        In case of PA-PA model, same email as primary owner of parent MID to be shared.
      </td>

      <td>
        [merchant@example.com](mailto:merchant@example.com)
      </td>
    </tr>

    <tr>
      <td>
        merchant\[mobile]<br /><code>optional</code>
      </td>

      <td>
        <code>string</code> Primary mobile number of the merchant for communication and notifications. A valid 10-digit Indian phone number is expected.

        In case of PA-PA model, same email as primary owner of parent MID to be shared.
      </td>

      <td>
        9911100364
      </td>
    </tr>

    <tr>
      <td>
        merchant\[business\_details]\[pan]<br /><code>mandatory</code>
      </td>

      <td>
        <code>string</code> Taxation Registration Number of the merchant (in their home country)
      </td>

      <td>
        FANPS6362D
      </td>
    </tr>

    <tr>
      <td>
        merchant\[business\_details]\[business\_entity\_type]<br /><code>optional</code>
      </td>

      <td>
        <code>string</code> Type of business entity (e.g.. LLP, LLC etc.)
      </td>

      <td>
        LLC
      </td>
    </tr>

    <tr>
      <td>
        merchant\[business\_details]\[registered\_name]<br /><code>mandatory</code>
      </td>

      <td>
        <code>string</code> The registered legal name of the merchant business.
      </td>

      <td>
        Merchant LLC
      </td>
    </tr>

    <tr>
      <td>
        merchant\[business\_details]\[business\_category]<br /><code>mandatory</code>
      </td>

      <td>
        <code>string</code> The primary business category of the merchant.
      </td>

      <td>
        E-Commerce
      </td>
    </tr>

    <tr>
      <td>
        merchant\[business\_details]\[business\_sub\_category]<br /><code>optional</code>
      </td>

      <td>
        <code>string</code> A more specific subcategory related to the business.
      </td>

      <td>
        Online Marketplace
      </td>
    </tr>

    <tr>
      <td>
        merchant\[product]<br /><code>optional</code>
      </td>

      <td>
        <code>string</code> The PayU product the merchant wants to use (e.g. PayUbiz, PayUmoney).
      </td>

      <td>
        PACB
      </td>
    </tr>

    <tr>
      <td>
        merchant\[registration\_number]<br /><code>mandatory</code>
      </td>

      <td>
        <code>string</code> Business registration / incorporation number
      </td>

      <td>
        20162049547
      </td>
    </tr>

    <tr>
      <td>
        merchant\[website\_details]\[website\_url]<br /><code>mandatory</code>
      </td>

      <td>
        <code>string</code> The merchant's website URL.
      </td>

      <td>
        [www.merchant-website.com](www.merchant-website.com)
      </td>
    </tr>

    <tr>
      <td>
        merchant\[registered\_address]\[address]<br /><br /><code>mandatory</code>
      </td>

      <td>
        <code>string</code> Registered office address
      </td>

      <td>
        877 E 1200 S #970397, Orem, UT, USA 84097
      </td>
    </tr>

    <tr>
      <td>
        merchant\[registered\_address]\[settlement\_country]<br /><br /><code>mandatory</code>
      </td>

      <td>
        <code>string</code> Settlement country
      </td>

      <td>
        USA
      </td>
    </tr>

    <tr>
      <td>
        merchant\[settlement\_currency]<br /><br /><code>mandatory</code>
      </td>

      <td>
        <code>string</code> Settlement currency
      </td>

      <td>
        USD
      </td>
    </tr>

    <tr>
      <td>
        merchant\[purpose\_code]<br /><br /><code>mandatory</code>
      </td>

      <td>
        <code>string</code> Applicable Purpose code as per Reserve Bank of India's [list](https://www.rbi.org.in/upload/notification/pdfs/52220.pdf)(Refer to "Imports" section)
      </td>

      <td>
        S0102
      </td>
    </tr>

    <tr>
      <td>
        merchant\[bank\_details]\[account\_no]<br /><code>optional</code>
      </td>

      <td>
        <code>string</code> Bank account number of the merchant for settlements. All bank fields must be sent together if any is sent.

        It can be either the IBAN or local bank account number.
      </td>

      <td>
        919010067278549
      </td>
    </tr>

    <tr>
      <td>
        merchant\[bank\_details]\[account\_holder\_name]<br /><code>optional</code>
      </td>

      <td>
        <code>string</code> Name of the account holder as per bank records.
      </td>

      <td>
        Merchant LLC
      </td>
    </tr>

    <tr>
      <td>
        merchant\[bank\_details]\[ifsc\_code]<br /><code>optional</code>
      </td>

      <td>
        <code>string</code> SWIFT/IBAN code of the bank branch for settlements.
      </td>

      <td>
        ABCDUS33XXX
      </td>
    </tr>

    <tr>
      <td>
        merchant\[signing\_authority\_details]\[name]<br /><code>optional</code>
      </td>

      <td>
        <code>string</code> Name of the authorized representative or signing authority.
      </td>

      <td>
        JOHN DOE
      </td>
    </tr>

    <tr>
      <td>
        merchant\[signing\_authority\_details]\[pancard\_number]<br /><code>optional</code>
      </td>

      <td>
        <code>string</code> Indian PAN card number of the signing authority. If posted, pancard\_name is required.
      </td>

      <td>
        FANPS6362D
      </td>
    </tr>

    <tr>
      <td>
        merchant\[signing\_authority\_details]\[email]<br /><code>optional</code>
      </td>

      <td>
        <code>string</code> Email of the authorized representative or signing authority.
      </td>

      <td>
        [auth\_email@example.com](mailto:auth_email@example.com)
      </td>
    </tr>

    <tr>
      <td>
        merchant\[integration\_type]<br /><code>optional</code>
      </td>

      <td>
        <code>string</code> Type of integration for the merchant's account.
      </td>

      <td>
        Seamless
      </td>
    </tr>
  </tbody>
</Table>

Use the following references to get additional information:

- [Business Entity Types](ref:partner-category-list#business-entity-type)
- [Business Categories](ref:partner-category-list)
- [Business Sub-Category List](ref:partner-category-list#business-sub-category)
- [Get Token API](ref:get_token_api)
- [Update Merchant Details API](ref:update_merchant_details_api)

## Sample Request

```curl
curl --location 'https://uat-partner.payu.in/api/v3/merchants' \
--header 'accept: application/json' \
--header 'authorization: Bearer 74ff89df8ff4aeb3d7cb2c0297cfcb358a8c4c1d69b3980d509bf300c5e82e5f' \
--header 'content-type: application/x-www-form-urlencoded' \
--data-urlencode 'merchant[display_name]=DIVY HARESHKUMAR SHAH' \
--data-urlencode 'merchant[email]=merchant@example.com' \
--data-urlencode 'merchant[mobile]=9911100364' \
--data-urlencode 'merchant[business_details][pan]=FANPS6362D' \
--data-urlencode 'merchant[business_details][business_entity_type]=Sole Proprietorship' \
--data-urlencode 'merchant[business_details][registered_name]=DIVY HARESHKUMAR SHAH' \
--data-urlencode 'merchant[business_details][business_category]=Arts, Gifts & Stationery' \
--data-urlencode 'merchant[business_details][business_sub_category]=Art Dealers and Galleries' \
--data-urlencode 'merchant[business_details][pancard_name]=DIVY HARESHKUMAR SHAH' \
--data-urlencode 'merchant[product]=PayUbiz' \
--data-urlencode 'merchant[bank_details][account_no]=919010067278549' \
--data-urlencode 'merchant[bank_details][account_holder_name]=DIVY HARESHKUMAR SHAH' \
--data-urlencode 'merchant[bank_details][ifsc_code]=UTIB0003557' \
--data-urlencode 'merchant[website_details][website_url]=https://www.example.com' \
--data-urlencode 'merchant[monthly_expected_volume]=12000' \
--data-urlencode 'merchant[signing_authority_details][name]=DIVY HARESHKUMAR SHAH' \
--data-urlencode 'merchant[signing_authority_details][pancard_number]=FANPS6362D' \
--data-urlencode 'merchant[signing_authority_details][email]=auth_email@example.com' \
--data-urlencode 'merchant[integration_type]=ThirdParty' \
--data-urlencode 'merchant[gst_number]=24FANPS6362D1ZE' \
--data-urlencode 'merchant[udyam_number]=UDYAM-UP-19-0002053' \
--data-urlencode 'merchant[gst_consent]=false'
```

## Sample Response

### Success Scenario

```json
{
  "merchant": {
    "name": "DIVY HARESHKUMAR SHAH",
    "email": "boro15@yomail.com",
    "registered_mobile": "9916965913",
    "mid": 8791796,
    "product": "PayUbiz",
    "business_type": "LongTail",
    "business_name": null,
    "pancard_name": null,
    "pancard_number": null,
    "website_url": null,
    "android_url": null,
    "ios_url": null,
    "gst_number": null,
    "created_at": "2025-06-26T07:16:25.000Z",
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
    "notification_email": "boro15@yomail.com",
    "settlement_status": "Active",
    "is_service_agreement_accepted": false,
    "is_authorisation_letter_required": false,
    "monthly_expected_volume": null,
    "business_category": null,
    "business_sub_category": null,
    "bank_verification_status": null,
    "uuid": "11f0-525d-76182ba4-954a-021ec077a271",
    "penny_deposit_status": null,
    "document_status": "Docs Approved",
    "kyc_status": {
      "status": "LOCKED",
      "kyc_status": "LOCKED"
    },
    "agreement_status": "Approved",
    "integration_type": "Not Selected",
    "service_intent": "default"
  }
}
```

### Failure Scenario

Various error responses can be received when the API fails. Here are some common examples:

**401 Unauthorized**

```json
{
  "error": "invalid_token",
  "error_description": "The access token provided is invalid"
}
```

**Action**: Regenerate the token using the Get Token API.

**422 Unprocessable Entity**

```json
{
  "errors": {
    "detail": [
      "Merchant already exists with given PAN details or email id"
    ]
  }
}
```

**Action**: Use a different PAN or email ID.

**422 Unprocessable Entity**

```json
{
  "errors": {
    "detail": [
      "Missing param: business_entity_id"
    ]
  }
}
```

**Action**: Include the missing parameter in your request.

## Response Parameters

### merchant JSON object descriptions

| Field                               | Description                                      |
| ----------------------------------- | ------------------------------------------------ |
| name                                | Name of the merchant                             |
| email                               | Email address of the merchant                    |
| registered\_mobile                  | Registered mobile number of the merchant         |
| mid                                 | Merchant ID generated by PayU                    |
| product                             | Product type (e.g., PayUbiz)                     |
| business\_type                      | Type of business (e.g., LongTail)                |
| business\_name                      | Name of the business                             |
| pancard\_name                       | Name as on PAN card                              |
| pancard\_number                     | PAN card number                                  |
| website\_url                        | URL of the merchant's website                    |
| android\_url                        | URL of Android app                               |
| ios\_url                            | URL of iOS app                                   |
| gst\_number                         | GST registration number                          |
| created\_at                         | Timestamp of merchant creation (ISO 8601 format) |
| mobile                              | Contact mobile number                            |
| blocked                             | Whether the merchant is blocked (true/false)     |
| first\_name                         | First name of the merchant                       |
| last\_name                          | Last name of the merchant                        |
| business\_entity                    | Business entity type                             |
| status                              | Current account status                           |
| partner\_source                     | Source of merchant creation                      |
| pan\_verification\_status           | Status of PAN verification                       |
| website\_approval\_status           | Status of website approval                       |
| notification\_email                 | Email for notifications                          |
| settlement\_status                  | Status of settlement account                     |
| is\_service\_agreement\_accepted    | Whether service agreement is accepted            |
| is\_authorisation\_letter\_required | Whether authorization letter is required         |
| monthly\_expected\_volume           | Expected monthly transaction volume              |
| business\_category                  | Category of business                             |
| business\_sub\_category             | Sub-category of business                         |
| bank\_verification\_status          | Status of bank verification                      |
| uuid                                | Unique identifier                                |
| penny\_deposit\_status              | Status of penny deposit verification             |
| document\_status                    | Status of document verification                  |
| kyc\_status                         | KYC verification status                          |
| agreement\_status                   | Status of agreement                              |
| integration\_type                   | Type of integration                              |
| service\_intent                     | Service intent type                              |

### registration\_address or operating\_address JSON object description

| Field         | Description                    |
| ------------- | ------------------------------ |
| address\_line | Street address of the merchant |
| city          | City of the merchant           |
| state         | State of the merchant          |
| pincode       | Postal code of the merchant    |

### bank\_detail JSON object description

| Field                 | Description                         |
| --------------------- | ----------------------------------- |
| bank\_account\_number | Bank account number of the merchant |
| ifsc\_code            | IFSC code of the bank branch        |
| holder\_name          | Name of the account holder          |
| nodal\_code           | Nodal code (if applicable)          |
| nodal\_status         | Status of nodal account             |

### KYC and Document Status

The following statuses can be returned for KYC and document verification:

| Status              | Description                                    |
| ------------------- | ---------------------------------------------- |
| DOCUMENT\_SUBMITTED | Documents have been submitted for verification |
| VERIFIED            | Documents have been verified successfully      |
| REJECTED            | Documents have been rejected                   |
| LOCKED              | KYC process is locked (cannot be modified)     |
| PENDING             | Documents are pending verification             |

If a document is rejected, the `error_message` field will contain the reason for rejection.

> 📘 Note:<br />All timestamps are provided in ISO 8601 format (YYYY-MM-DDThh:mm:ss.sssZ).

<br />

> 📘 Mandatory and interdependent parameters:
>
> - The merchant display name, email, mobile, and business entity type parameters are mandatory. For the list of sample errors, refer to the [Failure scenario](#failure-scenario) table.
> - If the PAN number is posted, PAN name must also be posted along with it. When posting bank account details, all the bank account details should be sent, i.e., account no, IFSC, account holder name.

<br />
