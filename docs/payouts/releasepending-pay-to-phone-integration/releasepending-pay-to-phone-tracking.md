---
title: Pay to Phone Transaction Tracking
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
Status of the transaction can be traced from the Payouts Dashboard and Status Check API. You can also configure webhooks to receive notifications from PayU on transactions status updates. 

## Dashboard  

Transaction status can be traced on the Dashboard along with:

* [View Payouts Details](doc:view-payouts-details) for transaction initiation
* Transaction processing details – Name Match and VPA details
* [Payouts Lifecycle](https://docs.payu.in/docs/payouts-lifecycle)  for significance of various transfer status.

## Status Check API 

To check status of any payouts to phone requests, you can using the **Check Transfer Status** API to pull real-time transfer status of any request from PayU. 

* For a date range 
* For particular status 
* For single or a list of merchant reference id 

> 📘 Reference:
>
> * [Check Transfer Status API](https://docs.payu.in/reference/check-transfer-status-api) for **Check Transfer Status** API.
> * [Payouts Lifecycle](https://docs.payu.in/docs/payouts-lifecycle) for significance of various transfer status.

## Webhooks 

You can also configure Payouts webhooks URLs to receive callbacks from PayU on update of any pay to phone request status to terminal states. For more information, refer to [Payouts Webhooks](doc:payouts-webhooks) > [System Rejections Tracking](doc:payouts-webhooks#system-rejections-tracking).
