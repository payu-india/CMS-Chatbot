---
title: Integration Checklist - S2S
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Use the following checklist to ensure your S2S integration is complete:

* Completed all the required checkout details have been collected correctly on your website and validated.

> **Reference:** For more information on collecting and submitting the request parameter, refer to [General Integration](doc:integrate-with-s2s).

* Verified the Response from PayU. For more information on responses, refer to [Collect Payment API - Server-to-Server](ref:_payment_server_to_server)
* Completed the callback response (reverse hashing) is not tampered with. For more information, refer to [Generate Hash](doc:hashing-request-and-response)
* Confirmed the transaction status on the Server-side, if the callback fail. Use Webhooks for hearing callbacks. For more information, refer to [Verify Payment API](ref:verify_payment_api) and [Webhooks](doc:webhooks).
* Completed the integration on Production. The endpoint for the  Production environment is:

[https://secure.payu.in/](https://secure.payu.in/)