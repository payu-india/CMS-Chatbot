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

<br />

## Sample response

<br />

\<details>
&#x20; \<summary>Sample request\</summary>
&#x20;&#x20;
&#x20; \`\`\`
&#x20; curl --location 'https\://uat-partner.payu.in/api/v3/merchants' \\
\--header 'accept: application/json' \\
\--header 'authorization: Bearer 27b005a9961c3a871704e88fce574df72aff3cb34cfa67315250589e7c38b745' \\
\--header 'content-type: application/x-www-form-urlencoded' \\
\--header 'Cookie: USERTXNINFO=678e2ef51c8dc2.87238836' \\
\--data-urlencode 'merchant%5Bdisplay\_name%5D=DIVY HARESHKUMAR SHAH' \\
\--data-urlencode 'merchant%5Bemail%5D=divy51\@yomail.com' \\
\--data-urlencode 'merchant%5Bmobile%5D=9911100364' \\
\--data-urlencode 'merchant%5Bbusiness\_details%5D%5Bpan%5D=FANPS6362D' \\
\--data-urlencode 'merchant%5Bbusiness\_details%5D%5Bbusiness\_entity\_type%5D=Sole Proprietorship' \\
\--data-urlencode 'merchant%5Bbank\_details%5D%5Baccount\_no%5D=919010067278549' \\
\--data-urlencode 'merchant%5Bbank\_details%5D%5Baccount\_holder\_name%5D=DIVY HARESHKUMAR SHAH' \\
\--data-urlencode 'merchant%5Bbank\_details%5D%5Bifsc\_code%5D=UTIB0003557' \\
\--data-urlencode 'merchant%5Bbusiness\_details%5D%5Bregistered\_name%5D=DIVY HARESHKUMAR SHAH' \\
\--data-urlencode 'merchant%5Bbusiness\_details%5D%5Bbusiness\_category%5D=Arts, Gifts & Stationery' \\
\--data-urlencode 'merchant%5Bbusiness\_details%5D%5Bbusiness\_sub\_category%5D=Art Dealers and Galleries' \\
\--data-urlencode 'merchant%5Bwebsite\_details%5D%5Bwebsite\_url%5D=https\://www\.google.com' \\
\--data-urlencode 'merchant%5Bmonthly\_expected\_volume%5D=12000' \\
\--data-urlencode 'merchant%5Bsigning\_authority\_details%5D%5Bname%5D=DIVY HARESHKUMAR SHAH' \\
\--data-urlencode 'merchant%5Bbusiness\_details%5D%5Bpancard\_name%5D=DIVY HARESHKUMAR SHAH' \\
\--data-urlencode 'merchant%5Bsigning\_authority\_details%5D%5Bemail%5D=email\_test1213\@yopmail.com' \\
\--data-urlencode 'merchant%5Bsigning\_authority\_details%5D%5Bpancard\_number%5D=FANPS6362D'
\`\`\`

\<details>
&#x20; \<summary>Sample response\</summary>

&#x20; \`\`\`
&#x20; \{
&#x20;   "merchant": \{
&#x20;     "name": "test",
&#x20;     "email": "test\@payu.in",
&#x20;     "registered\_mobile": "9999910014",
&#x20;     "mid": 129463,
&#x20;     "product": "PayUbiz",
&#x20;     "business\_type": "LongTail",
&#x20;     "business\_name": "Test",
&#x20;     "pancard\_name": "Test",
&#x20;     "pancard\_number": "ABCPG1234J",
&#x20;     "cin\_number":"U72400MH2006PTC293037",
&#x20;     "website\_url": null,
&#x20;     "android\_url": null,
&#x20;     "ios\_url": null,
&#x20;     "gst\_number": null,
&#x20;     "created\_at": "2020-12-08T11:03:56.000Z",
&#x20;     "mobile": "9999910014",
&#x20;     "blocked": false,
&#x20;     "first\_name": "",
&#x20;     "last\_name": "test",
&#x20;     "bank\_detail": \{
&#x20;       "bank\_account\_number": "234567891",
&#x20;       "ifsc\_code": "ICIC0000734",
&#x20;       "holder\_name": "Test"
&#x20;     },
&#x20;     "operating\_address": \{
&#x20;       "address\_line": "operational addr",
&#x20;       "city": "Sant Ravidas Nagar",
&#x20;       "state": "UTTAR PRADESH",
&#x20;       "pincode": 221304
&#x20;     },
&#x20;     "registration\_address": \{
&#x20;       "address\_line": "busenaddres line",
&#x20;       "city": "Sant Ravidas Nagar",
&#x20;       "state": "UTTAR PRADESH",
&#x20;       "pincode": 221303
&#x20;     },
&#x20;     "business\_entity": "LLP",
&#x20;     "status": "account\_created",
&#x20;     "partner\_source": "Create Merchant API",
&#x20;     "pan\_verification\_status": "Pending",
&#x20;     "website\_approval\_status": "Pending",
&#x20;     "notification\_email": "test\@payu.in",
&#x20;     "settlement\_status": null,
&#x20;     "is\_service\_agreement\_accepted": false,
&#x20;     "is\_authorisation\_letter\_required": false,
&#x20;     "monthly\_expected\_volume": 120000,
&#x20;     "business\_category": "Ecommerce",
&#x20;     "business\_sub\_category": "Flowers and Gifts",
&#x20;     "bank\_verification\_status": "Pending",
&#x20;     "uuid": "11eb-3945-0fcf623a-86d9-026e3e71538e",
&#x20;     "penny\_deposit\_status": "Not Initiated",
&#x20;     "signing\_authority": \{
&#x20;       "name": "test\_auth",
&#x20;       "email": "test\_auth\@payu.in"
&#x20;     },
&#x20;     "director1\_details": \{
&#x20;       "name": "test1\_dir",
&#x20;       "email": "test1\_dir\@payu.in"
&#x20;     },
&#x20;     "director2\_details": \{
&#x20;       "name": "test2\_dir",
&#x20;       "email": "test2\_dir\@payu.in"
&#x20;     }
&#x20;   }
&#x20; }
&#x20; \`\`\`
\</details>

\<details>
&#x20; \<summary>Response parameters\</summary>

&#x20; \<Table>
&#x20;   \<thead>
&#x20;     \<tr>
&#x20;       \<th>
&#x20;         \*\*Parameter\*\*
&#x20;       \</th>

&#x20;       \<th>
&#x20;         \*\*Description\*\*
&#x20;       \</th>
&#x20;     \</tr>
&#x20;   \</thead>

&#x20;   \<tbody>
&#x20;     \<tr>
&#x20;       \<td>
&#x20;         merchant
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the following details of the merchant in an array format.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         business\\\_entity
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the business entity of the merchant that was provided while onboarding.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         status
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains any of the following statuses:\\\\

&#x20;         \`\`\`
&#x20;         •	documents\_pending
&#x20;         •	bank\_verified
&#x20;         •	document\_upload\_in\_progress
&#x20;         •	account\_created
&#x20;         •	document\_verification\_in\_progress
&#x20;         •	website\_verification\_in\_progress
&#x20;         •	documents\_rejected
&#x20;         •	live
&#x20;         •	settlement\_on\_hold
&#x20;         •	agreement\_pending
&#x20;         •	agreement\_rejected
&#x20;         •	not\_available
&#x20;         •	website\_error
&#x20;         •	profile\_rejected
&#x20;         •	documents\_pending
&#x20;         •	bank\_verified
&#x20;         •	document\_upload\_in\_progress
&#x20;         •	account\_created
&#x20;         •	document\_verification\_in\_progress
&#x20;         •	website\_verification\_in\_progress
&#x20;         •	documents\_rejected
&#x20;         •	live
&#x20;         •	settlement\_on\_hold
&#x20;         •	agreement\_pending
&#x20;         •	agreement\_rejected
&#x20;         •	not\_available
&#x20;         •	website\_error
&#x20;         •	profile\_rejected
&#x20;         \`\`\`
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         partner\\\_source
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter returns the source through which the merchant joined or onboarded.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         pan\\\_verification\\\_status
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains any of the following PAN verification statuses:

&#x20;          \\
&#x20;         \&#x9;•	Success\\
&#x20;         \&#x9;•	Pending\\
&#x20;         \&#x9;•	Failed
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         website\\\_approval\\\_status
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains any of the following website approval statuses:

&#x20;          \\
&#x20;         \&#x9;•	Website Not live\\
&#x20;         \&#x9;•	Website Incomplete\\
&#x20;         \&#x9;•	Website Under Construction\\
&#x20;         \&#x9;•	Website Error\\
&#x20;         \&#x9;•	Website OK\\
&#x20;         \&#x9;•	Verification in Process
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         notification\\\_email
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the email to which the notification was sent to the merchant on onboarding.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         settlement\\\_status
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains any of the following settlement statuses:\\\\

&#x20;         \`\`\`
&#x20;         •	Risk Hold
&#x20;         •	Thirdparty Hold
&#x20;         •	Active
&#x20;         •	Suspended
&#x20;         •	Risk & Thirdparty hold
&#x20;         •	NEFT Return
&#x20;         •	Terminate
&#x20;         \`\`\`
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         is\\\_service\\\_agreement\\\_accepted
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the flag whether the service agreement was accepted or not.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         is\\\_authorisation\\\_letter\\\_required
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the flag whether the authorization letter is required or not required.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         monthly\\\_expected\\\_volume
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the monthly expected volume from the merchant.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         business\\\_category
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the business category of the merchant that was provided while onboarding.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         business\\\_sub\\\_category
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the business sub-category of the merchant that was provided while onboarding.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         bank\\\_verification\\\_status
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains any of the following bank verification statuses:\\\\

&#x20;         \`\`\`
&#x20;         •	Pending
&#x20;         •	Success
&#x20;         •	Verification Attempts Exhausted
&#x20;         •	Failed
&#x20;         \`\`\`
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         penny\\\_deposit\\\_status
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains any of the following penny deposit statuses when bank account verification was performed:\\\\

&#x20;         \`\`\`
&#x20;         •	Not Initiated
&#x20;         •	Pending
&#x20;         •	SENT\_TO\_BANK
&#x20;         •	Success
&#x20;         •	Failed
&#x20;         \`\`\`
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         uuid
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the Universal Unique Identifier (UUID).
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         document\\\_status
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the document status and can be any of the following:

&#x20;          \\
&#x20;         \&#x9;•	Pending: It indicates that document not yet submitted\\
&#x20;         \&#x9;•	Docs Received: It indicates that documents are submitted\\
&#x20;         \&#x9;•	Docs Approved: It indicates that documents are approved\\
&#x20;         \&#x9;•	Docs Error: It indicates that mismatch in data or wrong document
&#x20;       \</td>
&#x20;     \</tr>
&#x20;   \</tbody>
&#x20; \</Table>
\</details>

## Request Parameters

<details>
  <summary>Reference information for request parameters</summary>

  | Parameter                          | Reference                                                                                                                  |
  | :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
  | merchant\[business\_category]      | For the list of business categories, refer to [Business. Category List](ref:partner-category-list).                        |
  | merchant\[business\_entity\_type]  | For the list of business entity type, refer to [Business Entity Type](ref:partner-category-list#business-entity-type).     |
  | merchant\[business\_sub\_category] | For the list of business subcategories, refer to [Business Sub-Category](ref:partner-category-list#business-sub-category). |
</details>