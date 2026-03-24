---
title: Quick Start Partner Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Quick start (Partner API)
excerpt: >-
  Minimal sequence to create a merchant, add PAN and bank details, trigger CKYC,
  upload KYC documents, and initialize e-sign.
deprecated: false
hidden: false
metadata:
  title: PayU Partner Integration Quick Start
  description: >-
    Five core API calls to get a merchant through onboarding: create merchant,
    update details, CKYC OTP, document upload, e-sign initialize.
  keywords:
    - PayU partner quick start
    - merchant onboarding API
  robots: index
---

Get a merchant onboarded with a small set of API calls: create merchant, update PAN/bank/business, CKYC OTP, upload KYC documents, initialize e-sign.

## Onboarding flow

```mermaid
flowchart LR 
 A --- B[fa:fa-spinner B] 
 B --> C[fa:fa-check C] 
 B --> D[fa:fa-ban D]sequenceDiagram
    participant Partner
    participant Merchant
    participant API as PayU API Gateway
    participant Backend as PayU Onboarding Backend
    participant KYC as KYC Service
    participant ESign as E-Sign Service
    
    Partner->>API: 1. Create Merchant (Name, Email, Phone, PAN)
    API->>Backend: Create Merchant Record
    Backend-->>API: Return Merchant ID
    API-->>Partner: Merchant ID Response
    
    Partner->>API: 2. Update Merchant Details (Business Info)
    API->>Backend: Update Merchant Profile
    Backend-->>API: Update Confirmation
    API-->>Partner: Success Response
    
    Partner->>API: 3. Update Website/App Details
    API->>Backend: Store Digital Presence Info
    Backend-->>API: Update Confirmation
    API-->>Partner: Success Response
    
    Partner->>API: 4. Submit Signing Authority Details
    API->>Backend: Register Signatory
    Backend-->>API: Signatory Registered
    API-->>Partner: Success Response
    
    Partner->>API: 5. Upload KYC Documents
    API->>Backend: Submit Documents for Verification
    Backend->>KYC: Validate Documents
    KYC-->>Backend: Update KYC Status
    Backend-->>API: Verification Result
    API-->>Partner: KYC Status Response
    
    Partner->>API: 6. Request E-Sign Agreement
    API->>Backend: Generate Agreement Document
    Backend->>ESign: Send Signing Request
    Merchant->>ESign: Complete Digital Signature
    ESign-->>Backend: Store Signed Agreement
    Backend-->>API: Signature Confirmation
    API-->>Partner: Agreement Complete Response
    
    Backend->>Merchant: Activate Merchant Account

```

## Steps to integrate

The followings steps will include the env, sample request and response in accordion.

Step 1. Create Merchant (Name, Email, Phone, PAN)
Step 2. Update Merchant Details (Business Info)
Step 3. Update Website/App Details
Step 4. Submit Signing Authority Details
Step 5. Upload KYC Documents
Step 6. Request E-Sign Agreement
