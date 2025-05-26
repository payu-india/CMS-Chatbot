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

## Authentication

The access token with the scope as **refer\_merchant** is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).

## Environments

<PARTNEROnboardingEnvironment />

<br />

\<details>
&#x20; \<summary>List of acceptable documents\</summary>

&#x20; \<Table>
&#x20;   \<thead>
&#x20;     \<tr>
&#x20;       \<th>
&#x20;         Individuals
&#x20;       \</th>

&#x20;       \<th>
&#x20;         \*For individuals, merchant KYC can be done through Aadhaar or CKYC.\*

&#x20;         In case validation fails through the above two mechanisms, the merchant will have to submit document proofs ( POI, POA).
&#x20;       \</th>
&#x20;     \</tr>
&#x20;   \</thead>

&#x20;   \<tbody>
&#x20;     \<tr>
&#x20;       \<td>
&#x20;         \*\*Sole Proprietors\*\*
&#x20;       \</td>

&#x20;       \<td>
&#x20;         For sole proprietors, merchant KYC can be done through Aadhaar or CKYC. If validation fails through the above two mechanisms, the merchant will have to submit document proofs ( POI, POA & government certificate).
&#x20;       \</td>
&#x20;     \</tr>
&#x20;   \</tbody>
&#x20; \</Table>

&#x20; The list of acceptable documents for each category:

&#x20; \*\*POI/ POA:\*\*


## Request parameters

> ❗️ Watch it
>
> When passing the KYC documents, make sure that the file name does not contain any spaces or special characters to avoid errors.
>
> **For example**, a correct format would be AadharCard.png. Passing Aadhar Card.png or Aadhar-Card.png will result in error.