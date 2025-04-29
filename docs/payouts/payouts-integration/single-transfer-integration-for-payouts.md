---
title: Single Transfer Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Single Transfer Integration
  description: >-
    Integrate PayU's Single Transfer Payouts seamlessly with our comprehensive
    API guide. Learn how to automate and manage your business payouts securely
    and efficiently. Explore the step-by-step process for integrating PayU's
    payout solutions to enhance your financial operations.
  keywords:
    - PayU Payouts integration
    - Single transfer payouts
    - Automate payouts with PayU
    - Secure payouts Integration with PayU
    - Real-time payouts API
    - Business payouts with PayU
    - Integrate PayU payouts
    - ' Salary Payouts integration with PayU Payouts API'
    - Amount Disbursements with Payouts API
  robots: index
next:
  description: ''
---
Single Transfer Integration with Payouts allows you to make instant payments to a beneficiary through the APIs using different payment modes as illustrated in the following figure:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Frame-5-1024x304.png)

***

**Environment**

|                            |                                            |
| -------------------------- | ------------------------------------------ |
| **Test Environment**       | <https://uat-accounts.payu.in/oauth/token> |
| **Production Environment** | <https://accounts.payu.in/oauth/token>     |

## Step 1. Generate authentication token

Payouts Integration begins with access token generation. You should have an Access Token for authentication while accessing Payouts Endpoints. Without authentication, payouts core APIs can’t be accessed.

For this purpose, PayU provides two methods to generate the authentication token as follows:

1. [Generate Token using Merchant's Credentials API](ref:generate-token-using-merchants-credentials-api)
2. [Generate Token using Private Client ID](ref:generate-token-using-private-client-id)

> 📘 Note:
> 
> The authentication tokens have a TTL (Time To Live) and are required to be refreshed after a fixed interval of time. A Refresh Token API can be requested to obtain a renewed access token. For more information on this, refer to [Refresh Token API - Payouts](ref:refresh-token-api-payouts)

***

## Step 2. Get account details

The Get Account Details API returns complete account details of the merchant’s Payouts account. For more information, refer to [Get Account Details API](ref:get-account-details-api-payouts)

## Step 3. Initiate single transfer

Request for initiation of a single transfer to the beneficiary using Initiate Single Transfer API. For more information, refer to [Initiate Transfer API](ref:initiate-transfer-api).

You can transfer through various payment modes described in [Initiate Transfer API](ref:initiate-transfer-api):

- IMPS, NEFT or RTGS Payment Request
- UPI Payment Request
- Phone Payment Request
- MasterCard Payment Request
- VISA Card Payment Request
- Credit Card Payment Request

## Step 4. Check transfer status

Fetch the status of the transfer by posting the merchant’s reference ID as a parameter using the Check Transfer Status API. For more information on Payouts statuses, refer to [Payouts Lifecycle](doc:payouts-lifecycle) For more information on Check Transfer Status API, refer to the

## Step 5. Integrate with webhooks

You can integrate with webhooks to track the status of your payment. For more information, refer to the [Payouts Webhooks](doc:payouts-webhooks).