---
title: FAQs
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
* **Is it mandatory to become a merchant with PayU to get Maximizer product?**

        Yes, it is mandatory to become a merchant of PayU to avail the Router services from us. 

* **What are the gateways available with the Maximizer product?**

        PayU supports the following aggregators or payment gateways.

<SwitchPaySupportedAggregators />

* **Which checkouts are available in the Maximizer solution?**

        Standard checkout (pre-built checkout and custom checkout) and Server-to-Server integrations are supported by PayU.

* **What payment modes will be supported and shown to the user?**

<SwitchPaySupportedAggregators />

* **How the funds for the transactions routed to aggregators other than PayU will be credited to merchants account?**

        For the transactions routed by Maximizer to other aggregators, respective aggregator will settle funds to merchant’s bank account. PayU is responsible to settle funds only for the transactions which are routed through PayU and not for others.

* **How is the refund raised in Maximizer?**

        Merchant can raise refund via PayU’s refund API or PayU Dashboard

* **What happens if the refund fails with the aggregator other than PayU?**

        Status will be updated on the PayU Dashboard. You can cross check the failure reason with respective aggregators.

* **Do I have to raise refund request from aggregator's Dashboard?**

        No, refund request should be raised from PayU Dashboard only. PayU will initiate the refund request with concerned aggregator and update the status in PayU Dashboard for reference.  For more information, refer to [Refunds Dashboard](doc:refunds-dashboard).

* **What is the logic to identity the particular transaction is routed through which gateway?**

        In the response packet, the **field5** parameter that will have aggregator name through which transaction is processed. For example, if the transaction is routed via Pinelabs aggregator then field 5 will have Pinelabs value.