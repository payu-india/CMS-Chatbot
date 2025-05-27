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

\<details>\<summary>List of acceptable documents\</summary>

\[block:parameters]
\{
&#x20; "data": \{
&#x20;   "h-0": "Individuals",
&#x20;   "h-1": "\_ For individuals, merchant KYC can be done through Aadhaar or CKYC.  \n\_  In case validation fails through the above two mechanisms, the merchant will have to submit document proofs ( POI, POA).",
&#x20;   "0-0": "\*\*Sole Proprietors\*\*",
&#x20;   "0-1": "For sole proprietors, merchant KYC can be done through Aadhaar or CKYC. If validation fails through the above two mechanisms, the merchant will have to submit document proofs ( POI, POA & government certificate)."
&#x20; },
&#x20; "cols": 2,
&#x20; "rows": 1,
&#x20; "align": \[
&#x20;   null,
&#x20;   null
&#x20; ]
}
\[/block]


The list of acceptable documents for each category: 

\*\*POI/ POA:\*\*&#x20;


* Passport
  * Aadhar
    * Voter’s ID
      * Driving Licence
        * Utilities Bill (electricity, water, landline, gas connection)”(recent only) 
          * Address Verification Letter from Bank
            <br />
            **Government proof**
            * GST Registration Certificate 
              * Udyog Aadhar Card Certificate 
                * NOC by Gram Panchayat 
                  * TIN Certificate 
                    * Service Tax Registration Certificate 
                      * Shop & Establishment registration 
                        <br />

### List of Acceptable Bank Proofs

<br />

The following are acceptable bank proofs ( with validations):

<br />

**Passbook**

<br />

* Must have your name printed 
  * Must have your account number & IFSC printed 
    * Must have your photograph & bank stamp 

<br />

**Bank statement**

<br />

* Must have your name printed 
  * Must have your account number & IFSC printed 
    * Mobile banking screenshots & SMS will not be considered valid 

<br />

**Bank verification letter**

<br />

* Must be on a bank/ your letterhead 
  * Must have the sign & stamp of a bank manager 
    * Must have your name, account number & IFSC 

<br />

**Cancelled cheque**

<br />

* Must have your name printed 
  * Must have your account number & IFSC printed

<br />

The merchant ID in the request header must be included as a query parameter in the **mid** field.

<br />

\</details>

## Request parameters

> ❗️ Watch it
>
> When passing the KYC documents, make sure that the file name does not contain any spaces or special characters to avoid errors.
>
> **For example**, a correct format would be AadharCard.png. Passing Aadhar Card.png or Aadhar-Card.png will result in error.