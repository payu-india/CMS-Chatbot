---
title: Maximizer Routing Rules
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
Maximizer Routing Rules allows you to seamlessly utilize multiple routing strategies that will optimize your business outcomes, without requiring extensive technical expertise or complex rule-building knowledge.

Currently, PayU support the following primary types of routing:

* **Success Rate-Based Routing** (SRT): This approach directs transactions based on the success rates of payment gateways. For instance, all HDFC Cards or Cards or MASTER,VISA cards can be routed to either PayU or Razorpay, depending on which gateway has the highest success rate. Additionally, rules can be defined at a granular level.
* **Priority-Based Routing**: Transactions are routed based on predefined priorities. Merchants can set rules to prioritize specific gateways over others, ensuring efficient payment processing.
* **Percentage Based Routing**: Percentage-based routing rule involving single or multiple payment methods.

By leveraging Maximizer routing, merchants can enhance their payment flow, improve success rates, and provide a seamless experience for their customers.

This part of the document describes the following procedures with examples:

* [Add a SRT Routing Rule](doc:add-a-routing-rule)
* [Add a Priority-Based Routing Rule](doc:add-a-routing-rule-with-srt-copy)
* [Add a Percentage-Based Routing Rule](doc:add-a-percentage-based-routing-rule)
* [Include an Amount Range with a Routing Rule](doc:include-an-amt-range-with-routing-rule)
* [Understanding Baseline Logic](doc:understanding-baseline-logic)
* [Modify an Existing Routing Rule](doc:modify-an-existing-routing-rule)
* [Mark a Routing Rule Inactive](doc:mark-a-routing-rule-inactive)
* [View Audit Trials](doc:view-audit-trials)