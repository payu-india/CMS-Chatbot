---
title: Authentication for Payouts
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
Payouts Integration begins with generation of authentication token. You should have an Access Token to access Payouts Endpoints. Without authentication, payouts core APIs can’t be accessed.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/09/image-5.png)

For this purpose, PayU provides two ways to generate the authentication token as follows:

## Generate Token Using Merchant’s Username/Password

You can generate the auth token through merchant’s username and password where Username is either a registered mobile number or an email address. For more information, refer to [Generate Token using Merchant's Credentials API](ref:generate-token-using-merchants-credentials-api).

## Generate Token Using Private Client ID​

You can generate the auth token through merchant’s private Client ID and Client secret. You need to login to the Payouts Dashboard and complete OTP verification to obtain these ID’s successfully. Each account will have unique private Client ID and Client secret. For more information refer to [Generate Token using Private Client ID](ref:generate-token-using-private-client-id).

## Refresh Tokens

A Refresh Token is a special kind of token that can be used to obtain a renewed access token. The authentication tokens have a TTL (Time To Live) and are required to be refreshed after a fixed interval of time.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/09/image-6.png)

Once an access token is generated using the Username and Passwords, a Refresh Token API can be requested to obtain a renewed access token. For more information on this, refer to [Refresh Token API - Payouts](ref:refresh-token-api-payouts).