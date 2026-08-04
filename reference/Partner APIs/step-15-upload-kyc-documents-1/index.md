---
title: Step 15 — Upload KYC Documents
hidden: false
---
Uploads KYC documents for each required category from Step 14. 

**Call this API once per required document category.**

## Prerequisite Steps
Step 14: Fetch required docs to know what to upload
## Response-to-Request Mapping from Step 14`
``Step 14 response.document_categories[i].name       → merchant[document_category]Step 14 response.document_categories[i].document_types[j].name → merchant[document_type]Actual file from merchant                           → merchant[processed_document]```

## File Constraints- Formats
JPG, PNG, PDF- Max size: 5 MB per file

## Document Statuses (check via GetMerchant or Show KYC Document) `DOCUMENT_SUBMITTED` — Uploaded, pending review- `DOCUMENT_APPROVED` — Verified successfully- `DOCUMENT_REJECTED` — Rejected — delete and re-upload