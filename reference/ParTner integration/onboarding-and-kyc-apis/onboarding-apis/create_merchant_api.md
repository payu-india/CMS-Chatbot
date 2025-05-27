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

> ❗️ Important considerations for using this API
>
> 1. The mobile, Pan number, GSTIN passed in the request has to be valid as checks are performed in real time.
> 2. If Business Entity type is passed in the create merchant API, ensure that the PAN also belong to the same entity.

| \*\* Environment\*\* | \*\* URL\*\*                                                                         |
| :------------------- | :----------------------------------------------------------------------------------- |
| production           | [https://partner.payu.in/api/v3/merchants](https://partner.payu.in/api/v3/merchants) |
| UAT                  | uat-partner.payu.in/api/v3/merchants                                                 |

## Sample response

```
```

<br />

## Response parameters

<Table>
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
        name
      </td>

      <td>
        The business name of the merchant.
      </td>

      <td>
        ABC Retail Store
      </td>
    </tr>

    <tr>
      <td>
        legalName
      </td>

      <td>
        The legal registered name of the merchant business.
      </td>

      <td>
        ABC Retail Enterprises Ltd.
      </td>
    </tr>

    <tr>
      <td>
        type
      </td>

      <td>
        Type of merchant (individual, business, etc.).
      </td>

      <td>
        business
      </td>
    </tr>

    <tr>
      <td>
        email
      </td>

      <td>
        Primary email address for the merchant account.
      </td>

      <td>
        [contact@abcretail.com](mailto:contact@abcretail.com)
      </td>
    </tr>

    <tr>
      <td>
        phone
      </td>

      <td>
        Primary contact phone number for the merchant.
      </td>

      <td>
        +1234567890
      </td>
    </tr>

    <tr>
      <td>
        address.
        street
      </td>

      <td>
        Street address of the merchant's business location.
      </td>

      <td>
        123 Commerce St
      </td>
    </tr>

    <tr>
      <td>
        address.
        city
      </td>

      <td>
        City of the merchant's business location.
      </td>

      <td>
        Metropolis
      </td>
    </tr>

    <tr>
      <td>
        address.
        state
      </td>

      <td>
        State/province of the merchant's business location.
      </td>

      <td>
        NY
      </td>
    </tr>

    <tr>
      <td>
        address.
        country
      </td>

      <td>
        Country of the merchant's business location.
      </td>

      <td>
        USA
      </td>
    </tr>

    <tr>
      <td>
        address.
        postalCode
      </td>

      <td>
        Postal/ZIP code of the merchant's business location.
      </td>

      <td>
        10001
      </td>
    </tr>

    <tr>
      <td>
        businessDetails.
        registrationNumber
      </td>

      <td>
        Business registration or license number.
      </td>

      <td>
        BRN7890123
      </td>
    </tr>

    <tr>
      <td>
        businessDetails.
        taxId
      </td>

      <td>
        Tax identification number of the merchant.
      </td>

      <td>
        TAX456789
      </td>
    </tr>

    <tr>
      <td>
        businessDetails.
        yearEstablished
      </td>

      <td>
        Year the merchant business was established.
      </td>

      <td>
        2010
      </td>
    </tr>

    <tr>
      <td>
        category.
        primaryCategory
      </td>

      <td>
        Primary business category of the merchant.
      </td>

      <td>
        Retail
      </td>
    </tr>

    <tr>
      <td>
        category.
        subCategory
      </td>

      <td>
        Sub-category or specific business type.
      </td>

      <td>
        Electronics
      </td>
    </tr>

    <tr>
      <td>
        status
      </td>

      <td>
        Current status of the merchant account (active, pending, etc.).
      </td>

      <td>
        active
      </td>
    </tr>

    <tr>
      <td>
        bankDetails.
        accountNumber
      </td>

      <td>
        Bank account number associated with the merchant (partially masked).
      </td>

      <td>
        \*\*\*\*3456
      </td>
    </tr>

    <tr>
      <td>
        bankDetails.
        bankName
      </td>

      <td>
        Name of the bank where the merchant has an account.
      </td>

      <td>
        National Bank
      </td>
    </tr>

    <tr>
      <td>
        bankDetails.
        branchCode
      </td>

      <td>
        Branch code or routing number of the bank.
      </td>

      <td>
        BR001234
      </td>
    </tr>

    <tr>
      <td>
        bankDetails.
        accountType
      </td>

      <td>
        Type of bank account (checking, savings, etc.).
      </td>

      <td>
        checking
      </td>
    </tr>

    <tr>
      <td>
        contactPerson.
        name
      </td>

      <td>
        Name of the primary contact person for the merchant.
      </td>

      <td>
        John Smith
      </td>
    </tr>

    <tr>
      <td>
        contactPerson.
        title
      </td>

      <td>
        Job title of the primary contact person.
      </td>

      <td>
        Owner
      </td>
    </tr>

    <tr>
      <td>
        contactPerson.
        email
      </td>

      <td>
        Email of the primary contact person.
      </td>

      <td>
        [john.smith@abcretail.com](mailto:john.smith@abcretail.com)
      </td>
    </tr>

    <tr>
      <td>
        contactPerson.
        phone
      </td>

      <td>
        Phone number of the primary contact person.
      </td>

      <td>
        +1987654321
      </td>
    </tr>

    <tr>
      <td>
        settings.
        payoutFrequency
      </td>

      <td>
        Frequency of payouts to the merchant (daily, weekly, etc.).
      </td>

      <td>
        weekly
      </td>
    </tr>

    <tr>
      <td>
        settings.
        notificationPreferences
      </td>

      <td>
        Merchant's preferences for receiving notifications.
      </td>

      <td>
        \{"email": true, "sms": true}
      </td>
    </tr>

    <tr>
      <td>
        createdAt
      </td>

      <td>
        Timestamp when the merchant account was created.
      </td>

      <td>
        2023-05-15T10:30:45Z
      </td>
    </tr>

    <tr>
      <td>
        updatedAt
      </td>

      <td>
        Timestamp when the merchant account was last updated.
      </td>

      <td>
        2023-05-15T10:30:45Z
      </td>
    </tr>

    <tr>
      <td>
        urls.website
      </td>

      <td>
        Website URL of the merchant's business.
      </td>

      <td>
        [https://www.abcretail.com](https://www.abcretail.com)
      </td>
    </tr>

    <tr>
      <td>
        urls.logo
      </td>

      <td>
        URL to the merchant's logo image.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        verificationStatus
      </td>

      <td>
        Status of the merchant's verification process.
      </td>

      <td>
        verified
      </td>
    </tr>

    <tr>
      <td>
        kycStatus
      </td>

      <td>
        Status of Know Your Customer (KYC) verification.
      </td>

      <td>
        approved
      </td>
    </tr>
  </tbody>
</Table>

## Request parameters

<details>
  <summary>Reference information for request parameters</summary>

  | Parameter                          | Reference                                                                                                                  |
  | :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
  | merchant\[business\_category]      | For the list of business categories, refer to [Business. Category List](ref:partner-category-list).                        |
  | merchant\[business\_entity\_type]  | For the list of business entity type, refer to [Business Entity Type](ref:partner-category-list#business-entity-type).     |
  | merchant\[business\_sub\_category] | For the list of business subcategories, refer to [Business Sub-Category](ref:partner-category-list#business-sub-category). |
</details>