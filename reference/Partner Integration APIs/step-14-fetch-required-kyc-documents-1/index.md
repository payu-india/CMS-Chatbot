---
title: Step 14 — Fetch Required KYC Documents
hidden: false
---
Retrieves the list of document categories and accepted document types required for this merchant. 

**The response from this API is the input for Step 15 (Upload KYC Documents).**

## Prerequisite 
Steps- All prior steps relevant to the entity type

## Entity Applicability

**All entities** — but the required document list differs per entity type.

## How to Use the Response
1. Call this API → get list of `document_categories[]`
2. Each category has a `uuid`, `name`, and `document_types[]` array
3. Each document_type has a `uuid` and `name`
4. In **Step 15**, use the category `name` as `merchant[document_category]` and the type `name` as `merchant[document_type]`5. Upload one document per required category

## Response → Step 15 Mapping

```Step 14 Response:                          Step 15 Request:─────────────────                          ────────────────document_categories[i].name           →    merchant[document_category]document_categories[i].document_types[j].name  →  merchant[document_type]```

## UUID-to-Name Reference Document Categories
Use this table to map the `uuid` values in the API response to human-readable category names.

| UUID | Category Name | Frontend Key |
|------|--------------|--------------|
| `11e8-748f-297c6048-9081-020aca9875be` | Bank Account Proof | BANK_PROOF || `11e8-748f-297824ce-9081-020aca9875be` | PAN Card of Signing Authority | PANCARD_SIGNED_AUTHORITY |
| `11e8-748f-298078c2-9081-020aca9875be` | PAN Card of Company | COMPANY_PAN_COPY |
| `11e8-748f-298c2d98-9081-020aca9875be` | PAN Card of Society | SOCIETY_PAN |
| `11e8-748f-298a29ee-9081-020aca9875be` | PAN Card of Trust | TRUST_PAN |
| `11e8-748f-2982543a-9081-020aca9875be` | PAN Card of Partnership | PATNERSHIP_PAN_CARD |
| `11e8-748f-29844fd8-9081-020aca9875be` | PAN Card of LLP | LLP_PAN_CARD |
| `11e8-748f-297a15b8-9081-020aca9875be` | Address Proof of Signing Authority | ADDRESS_PROOF_SIGNED_AUTHORITY |
| `11e8-748f-297e7cb6-9081-020aca9875be` | Government Issued Certificate | GOVT_ISSUED_CERTIFICATE || `11e8-748f-297e7cb6-9081-020aca9875bc` | Additional Government Issued Certificate | ADDITIONAL_GOVT_ISSUED_CERTIFICATE |
| `11e8-748f-29865bf2-9081-020aca9875be` | Authorisation Letter | SIGNED_AUTHORISATION_LETTER |
| `11e8-748f-29762cc8-9081-020aca9875be` | Service Agreement | SERVICE_AGREEMENT || `11ed-249c-ac52042a-adc7-02053299b2da` | Deed | DEED |
| `11ed-249c-a3b0a330-adc7-02053299b2da` | Memorandum of Association | MEMORANDUM_ASSOCIATION || `11ed-250d-fc38a0a4-9097-acde48001122` | Articles of Association | ARTICLES_ASSOCIATION |
| `11ed-249c-af311ff0-adc7-02053299b2da` | Registration | REGISTRATION |
| `11ed-249c-aff1b1ac-adc7-02053299b2da` | Society | SOCIETY |
| `11ed-1eb5-c0dd9298-b597-02053299b2da` | Beneficiary | BENEFICIARY |
| `11ed-811f-c45ca0f4-836d-aa665a56f33a` | Shareholding Pattern | SHAREHOLDING_PATTERN |
| `11ee-2602-756be2ec-8491-a22c468e1995` | List of Trustees with Shareholding pattern | LIST_OF_TRUSTEES || `11ee-2602-41731942-8491-a22c468e1995` | List of Society Members with Shareholding pattern | LIST_OF_SOCIETY_MEMBERS |
| `11ee-7e33-98896bc6-9300-9ab1aaeb1a02` | Darpan Portal Document | DARPAN_PORTAL |

## UUID-to-Name Reference: Document Types
| UUID | Document Type Name | Frontend Key ||------|-------------------|--------------|
| `11e8-748f-2946799c-9081-020aca9875be` | PAN Card | PANCARD || `ca0a-9047-28d705a1-7e97-b530fbec4c41` | Cancelled Cheque | CC |
| `f912-b658-610ce46f-796b-14a515e41ad7` | Bank Verification Letter | BC |
| `11eb-d01a-8322997a-adc5-0242a53cdb42` | Bank Statement | BS |
| `11eb-d01a-456b15f8-adc5-0242a53cdb42` | Passbook | PB |
| `11e8-748f-2948a29e-9081-020aca9875be` | Passport | PASSPORT |
| `11e8-748f-294a800a-9081-020aca9875be` | Aadhar | AADHAR || `11e8-748f-294c6ef6-9081-020aca9875be` | Voter's ID | VOTER |
| `11e8-748f-294e7dea-9081-020aca9875be` | Driving Licence | DL |
| `11e8-748f-29508112-9081-020aca9875be` | Utilities Bill | BMTB |
| `24d8-a849-14f755a1-d49b-12ca65c5cd7a` | Address Verification Letter from Bank | AVFB |
| `11e8-748f-29528674-9081-020aca9875be` | Certificate of Incorporation | CERTIFICATE_OF_INCORPORATION |
| `11e8-748f-29549bc6-9081-020aca9875be` | Certificate of Registration | CR |
| `4b87-a0cd-3f4d0517-8418-5ae7ba077c75` | GST Registration Certificate | GST_CERTIFICATE || `11e8-748f-2956ad12-9081-020aca9875be` | TIN Certificate | TTC |
| `1cf4-2c90-a2766f4b-bede-6a66a28c72f1` | Service Tax Registration Certificate | SERVICE_TAX || `11e8-748f-296cf8a6-9081-020aca9875be` | NOC by Gram Panchayat | NOC |
| `11e8-748f-2970c076-9081-020aca9875be` | Udyog Aadhar Card Certificate | UACC |
| `5efb-91dc-a8eb8e63-6a33-b780b79bfb5d` | Others | OTHERS |
| `11e8-748f-293bbf7a-9081-020aca9875be` | Service Agreement | AGR |
| `1acc-c62c-42362b18-e290-64da3a8b1460` | Authorisation Letter | AUTHL |
| `11ed-179f-1691ce98-ad05-02053299b2da` | Power of Attorney | POA |
| `11e8-748f-29402e52-9081-020aca9875be` | Partnership Deed | PDVR || `11ed-179f-40b0ff5a-ad05-02053299b2da` | LLP Deed | LD || `11ed-17c8-0023eda2-ad05-02053299b2da` | Trust Deed | TD |
| `11ed-179f-220d6340-ad05-02053299b2da` | Memorandum of Association | MOA |
| `11ed-179f-36ffbc9e-ad05-02053299b2da` | Articles of Association | AOA |
| `11ed-179f-4cd1ae74-ad05-02053299b2da` | Beneficiary List | BL |
| `11ed-179f-5b7a6f7e-ad05-02053299b2da` | Evidence of Registration | EOR |
| `11ed-2ab4-03815850-9c9a-02053299b2da` | Evidence of Registration or Office Order | ERROR |
| `11ed-17c8-531b31b4-ad05-02053299b2da` | Bye-laws for Society | BFS |
| `11ed-8120-c3970d5c-836d-aa665a56f33a` | Latest Shareholding Pattern | LATEST_SHAREHOLDING_PATTERN |
| `11ee-2603-a98f1fac-8491-a22c468e1995` | List of Members certified by Registrar of Society | SOCIETY_MEMBERS |
| `11ee-2603-c5d6408c-8491-a22c468e1995` | List of Trustees with Shareholding pattern | TRUSTEES |
| `11ee-7d6d-dd53f418-aa7d-9ab1aaeb1a03` | Darpan Portal Document | DARPAN |
| `11e8-748f-29630274-9081-020aca9875be` | Form 80G and 12A | C80G |
## Required Documents by Entity Type

### Individual
| # | Category | Category UUID | Accepted Types |
|---|----------|--------------|----------------|
| 1 | PAN Card of Signing Authority | `11e8-748f-297824ce...` | PAN Card |
| 2 | Address Proof of Signing Authority | `11e8-748f-297a15b8...` | Passport, Aadhar, Voter's ID, Driving Licence, Utilities Bill, Address Verification Letter from Bank |
| 3 | Bank Account Proof | `11e8-748f-297c6048...` | Cancelled Cheque, Bank Verification Letter, Bank Statement, Passbook |
| 4 | Service Agreement | `11e8-748f-29762cc8...` | Service Agreement |

### Sole Proprietorship

| # | Category | Accepted Types |
|---|----------|----------------|
| 1 | PAN Card of Signing Authority | PAN Card |
| 2 | Address Proof of Signing Authority | Passport, Aadhar, Voter's ID, Driving Licence, Utilities Bill, Address Verification Letter from Bank |
| 3 | Additional Govt Issued Certificate | GST Reg Cert, NOC by Gram Panchayat, TIN Certificate, Service Tax Reg Cert, Others, Udyog Aadhar Card Certificate |
| 4 | Bank Account Proof | Cancelled Cheque, Bank Verification Letter, Bank Statement, Passbook |
| 5 | Government Issued Certificate | GST Reg Cert, NOC by Gram Panchayat, TIN Certificate, Service Tax Reg Cert, Others, Udyog Aadhar Card Certificate |
| 6 | Service Agreement | Service Agreement |
### Partnership
| # | Category | Accepted Types |
|---|----------|----------------|
| 1 | PAN Card of Signing Authority | PAN Card |
| 2 | Address Proof of Signing Authority | Passport, Aadhar, Voter's ID, Driving Licence, Utilities Bill, Address Verification Letter from Bank |
| 3 | Bank Account Proof | Cancelled Cheque, Bank Verification Letter, Bank Statement, Passbook |
| 4 | Deed | Partnership Deed |
| 5 | Government Issued Certificate | GST Reg Cert, NOC, TIN Certificate, Service Tax Reg Cert, Others, Udyog Aadhar Card Certificate |
| 6 | PAN Card of Partnership | PAN Card |
| 7 | Authorisation Letter | Signed Authorisation Letter, Power of Attorney |
| 8 | Service Agreement | Service Agreement |
| 9 | Shareholding Pattern | Latest Shareholding Pattern 
|### LLP| # | Category | Accepted Types |
|---|----------|----------------|
| 1 | PAN Card of Signing Authority | PAN Card |
| 2 | Address Proof of Signing Authority | Passport, Aadhar, Voter's ID, DL, Utilities Bill, Bank Address Letter |
| 3 | Bank Account Proof | Cancelled Cheque, Bank Verification Letter, Bank Statement, Passbook |
| 4 | Government Issued Certificate | Certificate of Incorporation |
| 5 | Deed | LLP Deed |
| 6 | PAN Card of LLP | PAN Card |
| 7 | Authorisation Letter | Signed Authorisation Letter, Power of Attorney |
| 8 | Service Agreement | Service Agreement |
| 9 | Shareholding Pattern | Latest Shareholding Pattern |
### Private Limited| # | Category | Accepted Types |
|---|----------|----------------|
| 1 | PAN Card of Signing Authority | PAN Card |
| 2 | Address Proof of Signing Authority | Passport, Aadhar, Voter's ID, DL, Utilities Bill, Bank Address Letter |
| 3 | Bank Account Proof | Cancelled Cheque, Bank Verification Letter, Bank Statement, Passbook |
| 4 | Government Issued Certificate | Certificate of Incorporation |
| 5 | Memorandum of Association | Memorandum of Association |
| 6 | Articles of Association | Articles of Association |
| 7 | PAN Card of Company | PAN Card |
| 8 | Authorisation Letter | Signed Authorisation Letter, Power of Attorney |
| 9 | Service Agreement | Service Agreement |
| 10 | Shareholding Pattern | Latest Shareholding Pattern |

### Public LimitedSame as Private Limited (see above).
### Trust
| # | Category | Accepted Types |
|---|----------|----------------|
| 1 | PAN Card of Signing Authority | PAN Card |
| 2 | Address Proof of Signing Authority | Passport, Aadhar, Voter's ID, DL, Utilities Bill, Bank Address Letter |
| 3 | Bank Account Proof | Cancelled Cheque, Bank Verification Letter, Bank Statement, Passbook |
| 4 | Government Issued Certificate | Certificate of Registration |
| 5 | Deed | Trust Deed |
| 6 | Beneficiary | Beneficiary list |
| 7 | List of Trustees with Shareholding pattern | List of Trustees with Shareholding pattern |
| 8 | Darpan Portal Document | Darpan Portal Document |
| 9 | PAN Card of Trust | PAN Card |
| 10 | Authorisation Letter | Signed Authorisation Letter, Power of Attorney |
| 11 | Service Agreement | Service Agreement |

### Society| # | Category | Accepted Types |
|---|----------|----------------|
| 1 | PAN Card of Signing Authority | PAN Card |
| 2 | Address Proof of Signing Authority | Passport, Aadhar, Voter's ID, DL, Utilities Bill, Bank Address Letter |
| 3 | Bank Account Proof | Cancelled Cheque, Bank Verification Letter, Bank Statement, Passbook |
| 4 | Government Issued Certificate | Certificate of Registration |
| 5 | Society | Bye-laws for Society |
| 6 | List of Society Members | List of Members certified by Registrar of Society with Shareholding pattern |
| 7 | PAN Card of Society | PAN Card |
| 8 | Authorisation Letter | Signed Authorisation Letter, Power of Attorney |
| 9 | Service Agreement | Service Agreement |
### One Person Company
| # | Category | Accepted Types |
|---|----------|----------------|
| 1 | PAN Card of Signing Authority | PAN Card |
| 2 | Address Proof of Signing Authority | Passport, Aadhar, Voter's ID, DL, Utilities Bill, Bank Address Letter |
| 3 | Bank Account Proof | Cancelled Cheque, Bank Verification Letter, Bank Statement, Passbook |
| 4 | Government Issued Certificate | Certificate of Incorporation |
| 5 | Memorandum of Association | Memorandum of Association |
| 6 | Articles of Association | Articles of Association |
| 7 | PAN Card of Company | PAN Card |
| 8 | Service Agreement | Service Agreement |