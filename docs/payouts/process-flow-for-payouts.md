---
title: Process Flow for Payouts
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Process Flow for Payouts
  description: >-
    Discover the comprehensive workflow for processing payouts with PayU. Learn
    about the various stages involved in disbursing payments, integrating
    payouts, and managing bulk and automated payouts efficiently. Ensure secure
    and seamless payout processing with PayU.
  keywords:
    - PayU payouts workflow
    - PayU payouts process
    - Payouts flow
    - PayU payouts lifecycle
    - PayU bulk payouts workflow
    - PayU automated payouts process
  robots: index
next:
  description: ''
---
Payouts payment workflow is simple and hassle-free. Payouts can be done through **API flow** or **Dashboard flow**. 

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Frame-1-1024x307.png)

## Payouts using API

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Frame-2-1024x170.png)

1. Generate authentication token using the authentication API.
2. Use the generated token and call the transfer API to initiate transfers using different payment modes.
3. Receive SUCCESS or FAILURE response for each of these transfers through webhooks. These webhooks can be configured via API or the merchant dashboard.

For more information, refer to following sections under API Reference:

* [Authentication for Payouts](ref:authentication-for-payouts)
* [Initiation and Tracking](ref:payouts-initiation-and-tracking)
* [Verification and Validation](ref:verification-and-validation)
* [Smart Send APIs](ref:smart-send-apis)
* [Bulk Smart Send](ref:bulk-smart-send)
* [Beneficiary Management](ref:beneficiary-management)

## Payouts using CSV Flow

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Frame-8-1024x170.png)

1. Navigate to Payouts Dashboard.
2. Click Make a Transfer and select the payment method. 
3. Download the CSV template.
4. Enter the necessary details regarding the transfers in this CSV file.
5. Upload the CSV file on the Dashboard. Once the file is uploaded, PayU will show how many entries are added and once submitted, the file is processed. If there are some invalid rows, PayU will show how many rows were processed.
6. Download the error report to check invalid rows.
7. Receive SUCCESS or FAILURE response for each of these transfers through webhooks. These webhooks can be configured via API or the merchant dashboard.

For more information, refer to [Payouts Dashboard](doc:payouts-dashboard).
