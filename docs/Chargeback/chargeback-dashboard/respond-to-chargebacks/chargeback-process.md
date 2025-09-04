---
title: Chargeback Process
deprecated: false
hidden: true
metadata:
  robots: index
---
The following flow diagram illustrate the PayU Chargeback flow. PAM 

<Image align="center" width="500px" src="https://files.readme.io/19dacb18db891e46516c1b51f8d732c4d79a573e6d8085e58ed3856385325101-chargeback_flow.png" />

## Step1 : Chargeback Notification

* Merchant receives a chargeback alert from PayU via dashboard and email.
  * Details include:
    • Chargeback amount
    • Reason code
    • "Reply Before" deadline (the date by which you must act)

***

## Step 2: Merchant Response Options

You must act before the "Reply Before" date! Choose one of the following actions:

* **Accept the Chargeback**
* **Contest/Dispute the Chargeback**

***

## Step 3: PayU Review & Submission

* PayU reviews your submission and builds a defense case.
* PayU forwards your response (acceptance or evidence) to the acquiring bank for final evaluation.

***

## Step 4: Resolution & Status Update

* The bank reviews and makes a decision.
* PayU dashboard reflects the final outcome:
  * **Closed in Customer Favor** (if chargeback accepted, or evidence rejected)
  * Other statuses for dispute win or closure.

***

<br />
