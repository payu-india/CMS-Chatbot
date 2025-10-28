---
name: RefundStates
---
* **QUEUED** : This indicates that the refund is accepted by PayU, but not sent to the downstream banking partner for processing.
* **SUCCESS** : This indicates that the refund is processed successfully.
* **FAILURE** : This indicates that refund processing failed. No funds are deducted for such refunds from the merchant’s settlement.
* **IN PROGRESS** : This indicates that the refund is raised to the bank for processing.
* **REQUESTED** : This indicates that the refund is sent to the bank for offline processing. In such cases, it takes upto 5-7 business days for the credit to reflect into the customer’s account.
* **od_hit** (Overdraft Hit): This indicates that the Overdraft has occurred( Insufficient funds in account ) In such cases, it takes upto 5-7 business days for the credit to reflect into the customer’s account.
