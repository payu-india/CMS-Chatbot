---
title: Create KYC Document API
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Create KYC Document** API is used to create an instance to upload the KYC document (PAN Card). The access token is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get-token-api).

> 📘 Note:
>
> If the **bank\_verification\_status** parameter of the **Get Merchant API** response is unsuccessful, the [Create KYC Document](ref:create_kyc_document_api) is used to submit the KYC details.

## Authentication

The access token with the scope as **refer\_merchant** is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).

## Environments

<PARTNEROnboardingEnvironment />

The list of acceptable documents for each category: 

**POI/ POA:**

* Passport
* Aadhar
* Voter’s ID
* Driving Licence
* Utilities Bill (electricity, water, landline, gas connection)”(recent only) 
* Address Verification Letter from Bank

**Government proof**

* GST Registration Certificate 
* Udyog Aadhar Card Certificate 
* NOC by Gram Panchayat 
* TIN Certificate 
* Service Tax Registration Certificate 
* Shop & Establishment registration 

### List of Acceptable Bank Proofs

The following are acceptable bank proofs ( with validations):

**Passbook**

* Must have your name printed 
* Must have your account number & IFSC printed 
* Must have your photograph & bank stamp 

**Bank statement**

* Must have your name printed 
* Must have your account number & IFSC printed 
* Mobile banking screenshots & SMS will not be considered valid 

**Bank verification letter**

* Must be on a bank/ your letterhead 
* Must have the sign & stamp of a bank manager 
* Must have your name, account number & IFSC 

**Cancelled cheque**

* Must have your name printed 
* Must have your account number & IFSC printed

The merchant ID in the request header must be included as a query parameter in the **mid** field.

## Request parameters

> ❗️ Watch it
>
> When passing the KYC documents, make sure that the file name does not contain any spaces or special characters to avoid errors.
>
> **For example**, a correct format would be AadharCard.png. Passing Aadhar Card.png or Aadhar-Card.png will result in error.

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        merchant\[document\_category]
        `mandatory`
      </td>

      <td>
        The category of the KYC document (e.g., "PAN Card of Signing Authority")
      </td>
    </tr>

    <tr>
      <td>
        merchant\[document\_type]
        `mandatory`
      </td>

      <td>
        The type of document (e.g., "PAN Card")
      </td>
    </tr>

    <tr>
      <td>
        merchant\[processed\_document]
        `mandatory`
      </td>

      <td>
        The actual document file to upload
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```
curl --request POST \
     --url https://uat-partner.payu.in/api/v3/merchants/7349834/kyc_document \
     --header 'accept: application/json' \
     --header 'content-type: multipart/form-data' \
     --form 'merchant[document_category]=Passbook' \
     --form 'merchant[document_type]=Test' \
     --form 'merchant[processed_document]=test/api'
```

## Sample response

```
{
  "merchant": {
    "mid": "8390925",
    "kyc_document_name": "PAN Card of Signing Authority",
    "kyc_document_uuid": "11ef-587e-43837330-95b0-021ec077a271",
    "kyc_document_status": "DOCUMENT_SUBMITTED",
    "error_message": null,
    "created_at": "2024-08-12T07:41:19.000Z"
  }
}

```