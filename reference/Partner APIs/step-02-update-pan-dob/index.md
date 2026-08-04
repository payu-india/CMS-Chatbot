---
title: Step 02 — Update Merchant Details
hidden: false
---
PAN + DOBSets the merchant's PAN details and date of birth/incorporation. The entity type is already set in Step 01 (Create Merchant) — determining which steps are required, which CKYC method to use, and which documents to upload.## Prerequisite Steps- Step 01 (Create Merchant) — `uuid` required from response
## Entity Applicability
**All entities**
## Allowed Entity Types

| Entity Type | CKYC Method | CIN Required | UBO Required | Business Members | DigiLocker |
|-------------|-------------|--------------|--------------|------------------|------------|
| Individual | OTP | No | No | No | Skip if CKYC ok || Sole Proprietorship | OTP | No | No | No | Skip if CKYC ok |
| Partnership | Fetch | No | Yes | Yes | Always || Pvt Ltd | Fetch | **Yes** | Yes | Yes | Always || Public Limited | Fetch | **Yes** | Yes | Yes | Always |
| LLP | Fetch | No | Yes | Yes | Always || Trust | Fetch | No | Yes | No | Always |
| Society | Fetch | No | Yes | No | Always || One Person Company | Fetch | **Yes** | No | No | Always || Government | Fetch | No | No | No | Always |
| NGO | Fetch | No | No | No | Always |
| Hindu Undivided Family | Fetch | No | No | No | Always |