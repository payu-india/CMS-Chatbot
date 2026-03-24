---
title: Errors and troubleshooting - Partner Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Errors and troubleshooting
excerpt: >-
  HTTP status codes, common validation mistakes, and fixes for partner onboarding APIs.
deprecated: false
hidden: false
metadata:
  title: PayU Partner Integration Errors
  description: >-
    400/401/422/429/500 handling; API order, PAN format, document categories, e-sign, token issues.
  keywords:
    - PayU partner API errors
    - onboarding troubleshooting PayU
  robots: index
---

## HTTP status codes

| Code | Meaning | What to do |
|------|---------|------------|
| `200` | Success | Process the response |
| `201` | Created | Resource created |
| `400` | Bad request | Check parameters |
| `401` | Unauthorized | Invalid or expired `resellerToken` |
| `403` | Forbidden | No access to this merchant |
| `404` | Not found | Check `uuid`, `mid`, or `merchant_id` |
| `422` | Validation failed | Read error message |
| `429` | Rate limited | Back off and retry |
| `500` | Server error | Retry with exponential backoff |

## Common mistakes

| Error | Cause | Fix |
|-------|-------|-----|
| Missing prerequisite | APIs out of order | PAN → Bank → Business → GST → CIN → Website |
| Invalid PAN | Format | Validate `ABCDE1234F` before submit |
| Invalid document category | Hardcoded or stale | Use Required Docs API |
| File too large | > 5 MB | Compress |
| Unsupported file type | Not JPG/PNG/PDF | Convert |
| E-sign blocked | Verification incomplete | Complete pending steps |
| Token expired | Auth | Refresh / contact KAM |
