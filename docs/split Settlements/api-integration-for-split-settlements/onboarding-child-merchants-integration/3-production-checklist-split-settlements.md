---
title: 3. Production Checklist - Split Settlements
deprecated: false
hidden: false
metadata:
  robots: index
---
## Validation Checklist

Before going live, verify:

* [ ] Child merchants can successfully register and activate accounts
* [ ] KYC documents are properly uploaded and verified
* [ ] Payment splits are correctly calculated and distributed
* [ ] Settlement reconciliation works as expected
* [ ] Webhook notifications are received and processed
* [ ] Error scenarios are handled gracefully

## Going Live

### Production Environment

Switch to production when testing is complete:

* **API Base URL**: `https://secure.payu.in`
* **Dashboard URL**: `https://secure.payu.in/merchant/dashboard`

### Final Steps

1. **Update API URLs**: Change all test URLs to production
2. **Verify Credentials**: Ensure production keys and salts are configured
3. **Monitor Settlements**: Set up monitoring for settlement success rates
4. **Customer Support**: Prepare support processes for child merchants