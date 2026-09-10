---
title: Webhook Debugging
excerpt: 'PayU Go SDK guide: Webhook Debugging'
deprecated: false
hidden: false
metadata:
  title: 'Webhook Debugging | PayU Go SDK'
  description: 'PayU Go SDK guide: Webhook Debugging'
  keywords:
    - payu go sdk
    - webhook debugging
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Debug webhook delivery issues.

## Checklist

- [ ] URL is HTTPS and publicly accessible
- [ ] Endpoint returns 200 (not 404/500)
- [ ] Webhook enabled in Dashboard
- [ ] Firewall allows PayU IPs

Test: `curl -I https://yoursite.com/webhook`

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
