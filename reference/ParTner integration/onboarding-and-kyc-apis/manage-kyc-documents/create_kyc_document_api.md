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
> If the **bank\_verification\_status** parameter of the **Get Merchant API** response is unsuccessful, the [Create KYC Document](ref:create_kyc_document_api) is used to submit the KYC details.

## Authentication

The access token with the scope as **refer\_merchant** is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).

## Environments

<PARTNEROnboardingEnvironment />

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

## Request parameters

> ❗️ Watch it
>
> When passing the KYC documents, make sure that the file name does not contain any spaces or special characters to avoid errors.
>
> **For example**, a correct format would be AadharCard.png. Passing Aadhar Card.png or Aadhar-Card.png will result in error.