---
title: Create KYC Document
excerpt: ''
api:
  file: partner-apis-6.json
  operationId: create_document
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Create KYC Document** API is used to create an instance to upload the KYC document (PAN Card). The access token is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get-token-api).

> 📘 Note:
> 
> The access token with the scope as **refer_merchant** is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).

<PARTNEROnboardingEnvironment />

<details><summary>List of acceptable documents</summary>

[block:parameters]
{
  "data": {
    "h-0": "Individuals",
    "h-1": "_ For individuals, merchant KYC can be done through Aadhaar or CKYC.  \n_  In case validation fails through the above two mechanisms, the merchant will have to submit document proofs ( POI, POA).",
    "0-0": "**Sole Proprietors**",
    "0-1": "For sole proprietors, merchant KYC can be done through Aadhaar or CKYC. If validation fails through the above two mechanisms, the merchant will have to submit document proofs ( POI, POA & government certificate)."
  },
  "cols": 2,
  "rows": 1,
  "align": [
    null,
    null
  ]
}
[/block]


The list of acceptable documents for each category: 

**POI/ POA:** 

- Passport
- Aadhar
- Voter’s ID
- Driving Licence
- Utilities Bill (electricity, water, landline, gas connection)”(recent only) 
- Address Verification Letter from Bank

**Government proof** 

- GST Registration Certificate 
- Udyog Aadhar Card Certificate 
- NOC by Gram Panchayat 
- TIN Certificate 
- Service Tax Registration Certificate 
- Shop & Establishment registration 

### List of Acceptable Bank Proofs

The following are acceptable bank proofs ( with validations):

**Passbook**

- Must have your name printed 
- Must have your account number & IFSC printed 
- Must have your photograph & bank stamp 

**Bank statement**

- Must have your name printed 
- Must have your account number & IFSC printed 
- Mobile banking screenshots & SMS will not be considered valid 

**Bank verification letter**

- Must be on a bank/ your letterhead 
- Must have the sign & stamp of a bank manager 
- Must have your name, account number & IFSC 

**Cancelled cheque**

- Must have your name printed 
- Must have your account number & IFSC printed

The merchant ID in the request header must be included as a query parameter in the **mid** field.

</details>

<details><summary>Sample request</summary>

```
curl --location -g --request POST '{{partner_base_url}}/api/v3/merchants/7210405/kyc_document' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--form 'merchant[document_category]="PAN Card of Signing Authority"' \
--form 'merchant[document_type]="PAN Card"' \
--form 'merchant[processed_document]=@"fVVJ4Dn25/logo_1.jpeg"'
```

</details>

<details><summary>Sample response</summary>

```
{
  "merchant": {
    "mid": 7210405,
    "kyc_document_name": "PAN Card of Signing Authority",
    "kyc_document_uuid": "11eb-95ea-acebe9f6-b75f-acbc3279eaa7",
    "kyc_document_status": "DOCUMENT_SUBMITTED",
    "error_message": "null",
    "created_at": "2021-04-05T08:41:13.000Z"
  }
}
```

</details>

## Request parameters