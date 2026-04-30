---
title: Rewards Refund Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: TWID Refund Integration
deprecated: false
hidden: true
metadata:
  robots: index
---

Refunds for Rewards integration will be initiated similar to regular checkout integrations and refund at PayU will be initiated for both the child txns. For partial refund, first the primary payment instrument (UPI, CC) will be refunded and post that reward partner will be refunded. For more information, refer to the following API Reference sections:

* [Refund Transaction API](ref:refund_transaction_api)
* [Refund Status API for Split Payments](ref:refund-status-api-for-split-payments)
