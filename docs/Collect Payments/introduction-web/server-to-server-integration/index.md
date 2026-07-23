---
title: Server-to-Server
deprecated: false
hidden: false
metadata:
  title: Server-to-Server Integration
  description: >-
    The Server-to-Server integration is performed at the server level, that is,
    your server (merchant server) and PayU server. The transaction is initiated
    from your server; hence redirection hop is eliminated. Since the details are
    captured on your page, customers gain confidence and enhance the checkout
    experience.
  keywords:
    - Server-to-Server integration
    - ' Server to Server Integration'
    - ' No Redirection hops'
  robots: index
next:
  description: ''
---
The legacy flow such as the PayU Hosted Checkout and Merchant Hosted Checkout involves intermediate browser hops. Server-to-Server (S2S) involves communication between the merchant’s server and PayU servers that operate in the backend. S2S is unlike the legacy flow, where the data is fetched through a direct call on the customer’s browser, and its progress can be witnessed through the change of the URLs.

## Prerequisites for S2S workflow

The prerequisites for integrating with S2S are:

- You must have Payment Card Industry Data Security Standard (PCI-DSS) certification, which is mandatory for all entities seeking to store, process, and transmit cardholder data.
- Sufficient technical bandwidth dedicated to managing the end-to-end web checkout processes in-house consistently.

> 👍 Before you Begin:
>
> - PayU strongly recommends you test your integration using the test merchant Key or Salt. To create a test merchant account, refer to [Register for a Merchant Account on Dashboard](doc:register-for-a-merchant-account-on-dashboard). After you create a test merchant account, you can access the test Key or Salt as described in [Generate Merchant Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard).
> - PayU recommends you integrate with Test environment initially. For merchants registered before August 3rd, 2023, use the following URL to sign up for the Test environment:
>
> [https://uat-onepayuonboarding.payu.in/app/account/signup](https://uat-onepayuonboarding.payu.in/app/account/signup)
>
> - Later, register for a Production account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

## Benefits of S2S workflow

The benefits of the S2S flow are:

- Delivers a better functional experience by eliminating intermediate browser hops that consume the customer’s internet bandwidth and procedural lags.
- Reduces the number of jumps in the forward leg, so the S2S flow significantly reduces the probability of errors.

With the above benefits, there are reduced chances of customers abandoning shopping cart during their shopping experience.

## Which integration works for you?

| Use Case                          | Description                                  | Integration Type                                                                      |
| --------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------- |
| Complete card details control     | Highest level of control, collect CVV/OTP    | [Classic Integration for Cards](doc:integrate-with-s2s-for-cards-classic-integration) |
| Card details control, but not OTP | PayU manages the OTP step                    | [Decoupled Flow Integration](doc:integrate-with-decoupled-flow-s2s)                   |
| Simple card auth with no capture  | Pre-authorize funds for later capture        | [Direct Authorization Integration](doc:integrate-with-direct-authorization-s2s)       |
| UPI on mobile via deep linking    | Initiates payment in a UPI app on the device | [UPI Intent with S2S Integration](doc:upi-intent-server-to-server)                    |

## Customer journey

The merchant server hosts the complete data sets necessary to take the customer from your website to the bank’s website and send it directly to the PayU server that operates in the backend. Unlike the Merchant Hosted Checkout integration, your customer will not be redirected to the bank site for OTP. This section describes the customer experience with S2S Flow.

To get started with Server-to-Server integration, refer to [General Integration](doc:integrate-with-s2s).

**Step 1:** The customer completes shopping at your website and initiates a transaction with card credentials.


<Image src="https://devguide.payu.in/wordpress/wp-content/uploads/2021/06/MicrosoftTeams-image-6-576x1024.jpg" align="center" width="350px" border={true} />


**Step 2:** The customer enters the CVV and proceeds to complete the payment.


<Image src="https://devguide.payu.in/wordpress/wp-content/uploads/2021/06/MicrosoftTeams-image-7-576x1024.jpg" align="center" width="350px" border={true} />


**Step 3:** The merchant collects the Bank OTP for authentication where the customer needs to complete the transaction by using the OTP sent by the bank to the registered mobile number.

## Cards Server-to-Server integration

PayU offers the following S2S integrations to collect card payments:

- [Classic Integration for Cards](doc:integrate-with-s2s-for-cards-classic-integration)
- [Decoupled Flow Integration](doc:integrate-with-decoupled-flow-s2s)
- [Direct Authorization Integration](doc:integrate-with-direct-authorization-s2s)

> 📘
>
> Note: If you are using legacy integration of decoupled flow for S2S, refer to [Legacy Flow for Server-to-Server](doc:legacy-flow-for-server-to-server).

<br />

<Cards_PayU_Labs />

## UPI Server-to-Server Integration

The UPI integration for S2S in general is described in the following sections:

> ❗️
>
> **Important UPI Integration Changes as per NPCI Mandate on UPI Collect Disablement**
>
> **Recommendation for Mobile Apps**: For Android and iOS apps, consider using PayU SDKs which have Smart Intent implementation built-in for higher success rates:
>
> - [Android Mobile SDKs](doc:explore-android-sdks)
> - [iOS Mobile SDKs](doc:explore-ios-sdks)

- [UPI Collection S2S Integration](doc:upi-collection-s2s)
- [UPI Intent S2S Integration](doc:upi-intent-server-to-server)

The UPI S2S integration for PhonePe Offers and Omnichannel is described in the following sections:

- [PhonePe Deep Offers S2S Integration](doc:phonepe-deep-offers-integration)
- [UPI Omnichannel S2S Integration](doc:upi-omnichannel-integration)

The [UPI Number Mapper API](ref:upi-number-mapper-api) describes how to get VPA for the given UPI number.