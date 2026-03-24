---
title: Production Checklist
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
Use the following checklist to ensure your plugin integration is complete:

* Integrate the plugin using the Test Key and Salt. For more information, refer to [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).
* Completed the integration on Production with Production key and salt. For more information, refer to [Generate Merchant Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard). The endpoint for the  Production environment is:

```
   <https://secure.payu.in/>
```

* Make a transaction and confirm the transaction status on the eCommerce platform, if the transaction is passed. For more information, refer to [Verify Payment API](ref:verify_payment_api).
