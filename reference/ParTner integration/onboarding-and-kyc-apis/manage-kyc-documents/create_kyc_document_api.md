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

<br />

\<details>\
\<summary>List of acceptable documents\</summary>

\<Table>\
\<thead>
\<tr>
\<th>
Individuals
\</th>

```
```

```
```

```
```

```
```

The list of acceptable documents for each category:

**POI/ POA:**

## Request parameters

> ❗️ Watch it
>
> When passing the KYC documents, make sure that the file name does not contain any spaces or special characters to avoid errors.
>
> **For example**, a correct format would be AadharCard.png. Passing Aadhar Card.png or Aadhar-Card.png will result in error.