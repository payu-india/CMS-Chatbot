---
title: Understanding Baseline Logic
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
This baseline logic ensures that priority-based routing maintains a smooth transaction flow. For instance, if the priority order is Razorpay, Cashfree, and PayU, and Razorpay experiences downtime, it is not logical to direct traffic to it again. Therefore, the baseline logic acts as a check on priority-based routing. The baseline value can be set at both the static and the global level. If not specified at the static baseline, the global level baseline will be used.

For example, if the priority order is Razorpay, Cashfree, and PayU, and the baseline is set at 50%, a check will be performed on all payment aggregators (PAs) to see how many have exceeded the baseline. If none have, the PA with the highest SRT (Success Rate Threshold) will be chosen. If some have exceeded the baseline, the PA with the highest priority among them will be selected. In case of a tie, the PA with the highest priority will be picked. The table below illustrates various scenarios:

| SRT of Razorpay | SRT of Cashfree | SRT of PayU | Final PA to be chosen |
| --------------- | --------------- | ----------- | --------------------- |
| 55              | 79              | 99          | Razorpay              |
| 45              | 79              | 99          | Cashfree              |
| 30              | 45              | 40          | Cashfree              |
| 45              | 45              | 45          | Razorpay              |

## Static baseline Logic

The static baseline logic ensures that priority-based routing maintains a smooth transaction flow. For instance, if the priority order is Razorpay, Cashfree, and PayU, and Razorpay experiences downtime, it wouldn’t be logical to direct traffic to it again. Therefore, the baseline logic acts as a check on priority-based routing. The baseline value can be set at both the static and the global level. If not specified at the static level, the global level baseline will be used.

In the static baseline, you can set a static baseline (threshold configured by the merchant) at the rule level on the Maximizer Dashboard. If the priority PA exceeds the baseline, all transactions according to that rule will be routed to the priority PA set by the merchant. If the priority PA does not exceed the baseline, the preferences will be dissolved, and transactions will be routed to the fallback PA.

- **Scenario 1:** For example, there is a rule for HDFC cards set by the merchant. Suppose the baseline for HDFC cards is 60%. The priority rule set by the merchant with the order as Razorpay, Cashfree, and PayU. If Razorpay does not exceed the 60% baseline for card transactions, the traffic will be routed to the fallback PA, which is Cashfree. If the priority PA exceeds the baseline, transactions will be routed to the highest priority aggregator, which is RP. If none of the aggregators exceed the baseline, the PA with the highest SRT will be used.
- **Scenario 2:** For example, there is another rule for HDFC Netbanking set by the merchant. Suppose the baseline for HDFC Netbanking is 70%. The priority rule set by the merchant is in the order as Cashfree, BillDesk, PayU. If Cashfree does not exceed the 70% baseline for Netbanking transactions, the traffic will be routed to the fallback PA, which is BillDesk. If the priority PA exceeds the baseline, transactions will be routed to the highest priority aggregator, which is CF. If none of the aggregators exceed the baseline, the PA with the highest SRT will be used.

## Dynamic baseline logic

Same as static baseline, but in dynamic baseline instead of looking if the PA is above the baseline defined, the baseline would be calculated based on the best performing PA. For example, if a priority rule is set for Razorpay, Paytm, PayU. In the below example, if static baseline is implemented, then RP would get chosen, as the SRT of Razorpay (70%) is greater than static baseline of 60%. However if dynamic baseline is implemented, then the highest SRT of all configured PAs (Razorpay, Paytm, PayU) is picked. In this case, PayU is picked and it’s SRT is multipled by the dynamic baseline set. 80*10%=8%. In this case, only PAs with SRT of 72% (80-8%) will be picked. Hence RP will **not** be choosen. The transaction would be routed to PayU. If the SRT of RP is greater than 72, say 75, then Razorpay would be selected to route the transaction to.

| PA (priority) | SRT | Static baseline | Dynamic baseline |
| ------------- | --- | --------------- | ---------------- |
| Razorpay (1)  | 70  | 60%             | 10%              |
| Paytm (2)     | 40  |                 |                  |
| PayU (3)      | 80  |                 |                  |