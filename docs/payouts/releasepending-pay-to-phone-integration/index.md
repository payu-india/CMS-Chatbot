---
title: Pay to Phone Integration
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
Pay to Phone number enables merchants to make instant transfer to beneficiary’s mobile number where the beneficiary account number using the Payouts API integration, IFSC or VPA are not available with this feature. You can optimize on your customer journey of onboarding/refunds/rewards by not collecting account details to improvise conversions.  

## Features

You need to provide the beneficiary mobile number and name to transfer funds to the beneficiary by using this feature.  

* The funds are transferred to the beneficiary’s bank account of the latest primary VPA handle linked to the beneficiary mobile number. 
* Hence, each pay to phone transfer can be of maximum INR 1 lacs as per current Single UPI Transfer limit from NPCI.  

## Workflow 

###  Primary VPA linked to phone 

* On every pay to phone request initiation, the beneficiary’s latest primary VPA and the associated account holder name is extracted from beneficiary bank 
* Request is not processed on any stale database even for repeat beneficiary  
* If there’s no VPA associated to the mobile number, the transaction will not be processed. 

### Beneficiary name match score 

* In order to ensure further that funds are transferred to your intended beneficiary only, the beneficiary's name provided by you is matched with the account holder name linked to the extracted primary VPA  
* For the name match below the system threshold, the transfers are not processed.  

## Payouts to Phone approval flow

The approval flow is to perform the following Payout Dashboard:

* enable and set the amount rules from the Payouts Dashboard 
* Review the VPA and name match details to accept or reject the transfers yourself 

It's advised to provide full beneficiary name as in the beneficiary’s bank to reduce the transfer rejections due to low name match score.

## Payment initiation, tracking and threshold configuration

This part of the document includes the following sections:

* [Pay to Phone Initiation](doc:pay-to-phone-initiation)
* [Pay to Phone Tracking](doc:pay-to-phone-tracking)
* [Pay to Phone Configuration](doc:pay-to-phone-configuration) [Optional]

> 📘 Reference:
>
> To trace the pay to phone requests that are getting auto-rejected for safeguarding transfer to intended beneficiary, refer to [Payouts Webhooks](doc:payouts-webhooks)> [System Rejections Tracking](doc:payouts-webhooks#system-rejections-tracking).
