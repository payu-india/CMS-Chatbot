---
title: Version Control for BBPS APIs
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
### From Version 1.0 to 3.2

PayU has introduced an Agent API kit with fetch & pay feature and also the prepaid recharge flow to integrate the mobile prepaid recharges. Also, in [Get All Billers By Region API](ref:get-all-billers-by-region-api) or [Get All Billers By Category API](ref:get-all-billers-by-category-api), added new fields which are introduced by NPCI in biller MDM as well.

### Version 3.3

PayU has introduced the additional params in error response as well and also in case of [Bill Payment API](ref:bill-payment-api). Also, added the additional parameters in response to send the `txnRefId` of BBPS biller’s payment.

There is also a minor change in documents related to [Raise BBPS Complaint API](ref:raise-bbps-complaint-api) response for BBPS billers. In the case of transaction CMS API response, there are some extra fields that have been introduced by NPCI .

### Version 3.4

In CMS (Complaint Management system) for BBPS billers, Service based complaints have been removed from the PayU system as per the NPCI new guidelines. According to the NPCI new guidelines, only transaction-based complaint system will be supported and on the basis of the passed disposition message request will be assigned to specific COUs and BOUs and also `complaintStatus` field has been added to the [Check Complaint Status API](ref:check-complaint-status-api) for BBPS transactions. Apart from it there are also some changes in complaint raise API response, some of the new fields has been introduced.The changes have been made in the [Raise BBPS Complaint API](ref:raise-bbps-complaint-api) (for BBPS Transactions) and [Check Complaint Status API](ref:check-complaint-status-api) API.

### Version 3.5

In the case of payment if agents receive failure(with 600 status code) with **payment_request_pending** in the message field of failure response then the agent needs to mark that transaction is pending and if receives **payment_request_failed** in the message field of failure response then that transaction is considered a failure transaction.

### Version 3.6

In the case of biller MDM response there are four new fileds has been introduced `supportBillValidation` and `blrResponseParams` and `blrAdditionalInfo`, `billerMode`. Apart from It,In case of payment API’s `isQuickPay` Field value will change on the basis of combination of type of `billerMode` (like online or offline A or offline B), `adhoc` , `fetchOption` and `supportBillerValidation`. The combination of all these parameters has been mentioned in detail in the [Bill Payment API](ref:bill-payment-api). The is `values` parameter of biller MDM which will optional, that is, it may be available for some of the billers which provide some kind of static information in the biller MDM related to a customer parameters.

### Version 3.8

PayU have added the following payment modes which is supported by NPCI:

- ACCOUNT\_TRANSFER
- BHARAT\_QR
- USSD
- CASH

#### Payment Details Vs Required Params

[Payment Modes  and Required Parameters](ref:payment-modes-and-required-parameters) table has been updated with required information. Also,  more detailed combination information related to initiating channel and payment mode combination in this section.

> 📘 Change for cash payment mode:
> 
> According to NPCI guidelines, agent need to pass remarks as a required params in request and BNK code has been changed to **BNKBRNCH** in initiating channel vs device block code table.

### Version 3.9

[Check Health Status API](ref:check-health-status-api) has been introduced in the system for agents to check the status of Pay U's system. Also, PayU will configure alerts on its end if it does not receive any heartbeat for the configured time then PayU will raise the issue with the agent to check their system whether everything is working fine or not.

### Version 4.0

Bill fetch response’s amount detail field format corrected in the document as it is a list of map. Also added V2 version of **Payment Status** API which will return more information related to a previously requested payment. Also in v2 and v1  of [Get Payment Status API](ref:get-payment-status-api), the `txnRefId` is made as optional parameter.

Also added the following details in biller MDM APIs:

- Region code
- State

### Version 4.1

**Bill Payment Validation** API for BBPS billers has been introduced. For the`isQuickPay` parameter in payment request some new cases added respective to [Bill Validation API](ref:bill-validation-api). For more information, refer to [Biller Types in BBPS](ref:biller-types-in-bbps)

> 📘 Implement Bill Validation API
> 
> Agents need to implement [Bill Validation API](ref:bill-validation-api) for BBPS services and also follow[Biller Types in BBPS](ref:biller-types-in-bbps)to pass the quick pay parameter in payment request. Also Biller Types in BBPS is only applicable for those agents who are implementing the [Bill Validation API](ref:bill-validation-api).