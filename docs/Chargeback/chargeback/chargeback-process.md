---
title: Chargeback Accept or Contest Process
deprecated: false
hidden: false
metadata:
  robots: index
---
The following flow diagram illustrate the PayU Chargeback flow for Accept or Contest process. 

<Image align="center" width="500px" src="https://files.readme.io/41abd752e30c42d3f761fe65da96d0e45ace3b05c6f3241ce87d18dcfc2c6bd0-chargeback_flow_updated.png" />

## Step1 : Chargeback Notification

Merchant receives a chargeback alert from PayU via dashboard and email. The details include:

* Chargeback amount
* Reason code
* "Reply Before" deadline (the date by which you must act)

<Callout icon="📘" theme="info">
  **Reference**: For more information, refer to [View a Case Details](doc:view-a-case-details).
</Callout>

<Callout icon="❗️" theme="error">
  **Notifications from child MIDs**: On the basis of configuration, the notifications from child MIDs can also be displayed.
</Callout>

***

## Step 2: Merchant Response Options

You must act before the "Reply Before" date! Choose one of the following actions:

* **Accept the Chargeback**: For more information, refer to any of the following:
  * **Manually**: [Accept Chargeback on Dashboard](doc:accept-chargeback-on-dashboard)
  * **API**:  [Accept Chargeback API](ref:accept-chargeback-api)
* **Contest/Dispute the Chargeback**: For more information, refer to any of the following:
  * **Manually**: [Contest Chargeback on Dashboard](doc:contest-chargeback-on-dashboard)
  * **API**: [Contest Chargeback API](ref:contest-chargeback-api)

<Callout icon="📘" theme="info">
  **Update evidences**: In order to contest the chargeback, evidences should be uploaded based the reason code.
</Callout>

***

## Step 3: PayU Review & Submission

* PayU Reviews the submission with evidences and then builds the case
* PayU can return the submission because of insufficient documentation for re-submission
* PayU forwards your response (acceptance or contest with evidence) to the acquiring bank for final evaluation.

***

## Step 4: Resolution & Status Update

* The bank reviews and makes a decision.
* PayU dashboard reflects the final outcome:
  * **Closed in Customer Favour** (if chargeback accepted, or evidence rejected)
  * Other statuses for dispute win or closure.

<br />
