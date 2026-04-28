---
title: Escalation Checklist
excerpt: Details to collect before contacting PayU Support or Integration Team.
deprecated: false
hidden: true
metadata:
  title: Escalation Checklist
  description: Information to collect before escalating PayU payment, webhook, hash, or recurring-payment issues.
  robots: index
next:
  description: ''
---

Before contacting PayU Support or Integration Team, collect enough evidence to reproduce and trace the issue.

## Include these details

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

## Do not share

* Salt.
* CVV, OTP, card PIN, or full card number.
* Customer authentication secrets.
* Raw logs containing unmasked sensitive data.

## Useful context by issue type

| Issue type | Add this context | Recommended fix |
| --- | --- | --- |
| Invalid hash | Hash sequence used, raw request fields excluding salt, endpoint, environment. | Recreate the hash server-side with exact posted values, correct delimiters, and matching environment key/salt. |
| Payment failed | Error code, issuer/bank message, `field7`, `field8`, `field9`, payment mode. | Verify final status, classify customer/issuer vs technical failure, and offer retry with a new `txnid` only when safe. |
| Pending transaction | First response timestamp, latest status-check response, webhook status. | Keep order pending, poll Transaction Detail APIs, and reconcile webhook/status before fulfillment or retry. |
| Webhook failure | Endpoint URL, HTTP status, response body, WAF/firewall logs, content type accepted. | Fix endpoint method/auth/content-type/firewall issues and return `2xx` after durable receipt. |
| Recurring/SI failure | Mandate ID/auth reference, billing rule, billing amount, debit date, sequence details. | Validate mandate dates, billing rules, debit sequence, and duplicate debit protection before retrying. |

If you are unable to resolve the issue, contact [PayU Support](https://help.payu.in/).
