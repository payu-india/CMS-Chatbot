---
title: Escalation Checklist
excerpt: >-
  Information to collect before escalating PayU payment, webhook, hash, or
  recurring-payment issues.
deprecated: false
hidden: true
metadata:
  robots: index
---
Before contacting PayU Support or Integration Team, collect enough evidence to reproduce and trace the issue.

## Include These Details

<Accordion title="Details List" icon="fa-list">
  * Merchant key, not salt.
  * Environment: test or production.
  * PayU `txnid`.
  * PayU `mihpayid`, if generated.
  * Timestamp with timezone.
  * Payment mode and `PG_TYPE`.
  * Error code and `error_Message`.
  * `status` and `unmappedstatus`.
  * `field7`, `field8`, and `field9`.
  * `bank_ref_num` or `bank_ref_no`, if present.
  * Webhook endpoint and delivery HTTP status, if relevant.
  * Sanitized request payload.
  * Confirmation that response hash validation was performed.
</Accordion>

## Do Not Share

Do not share these details:

<Accordion title="Not to Share" icon="fa-list">
  * Salt.
  * CVV, OTP, card PIN, or full card number.
  * Customer authentication secrets.
  * Raw logs containing unmasked sensitive data.
</Accordion>

If you are unable to resolve the issue, contact [PayU Support](https://help.payu.in/).