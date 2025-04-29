---
title: Pay to Phone Configuration
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
## Name Match Score Threshold 

By default, the system assigns a name match threshold score (80%) for all pay to phone transfers.   

* Setting a much higher threshold can increase rejections due to name matching below the threshold even for a correct beneficiary, while setting a much lower threshold may lead to untended transfer.  
* You can set your own name match threshold score to override this system threshold as well depending on your use case and observed patterns from Dashboard and APIs 

## Overriding Threshold Score from Dashboard 

You can set up the name match threshold score percentage between 0 to 100 by configuring ‘Name Match Threshold’ score on [Payouts Settings section on Dashboard](https://docs.payu.in/docs/configure-payouts-dashboard-settings).  

<Image align="center" src="https://files.readme.io/51fe7fd-payouts_thresholdc_configuration.png" />

## Overriding Threshold Score using API 

You can set up the name match threshold score percentage between 0 to 100 using the **Set Name Match Score Threshold** API with your payout merchant ID and score. For more information, refer to [Set Name Match Score Threshold API](ref:set-name-matchscore-threshold-api). 

Also, you get the name march score before overriding threshold. For more information, refer to [Get Name Match Score Threshold API](ref:get-name-matchscore-threshold-api).
