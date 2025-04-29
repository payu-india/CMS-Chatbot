---
title: FAQs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: FAQs - Partner Integration
  description: ''
  robots: index
next:
  description: ''
---
## General

- **What is a PayU Partner Program?** 

  The PayU Partner Program is a referral program through which you can offer the PayU product suite to your clients, merchants, or customers. Partners get rewarded monetarily for their referrals.
- **Who can be a PayU Partner?** 

  Anyone from a student to an e-commerce consultant can partner with PayU for the affiliate program. Here are some popular categories among existing PayU partners:
- Website & app developers
- Digital marketing service providers
- Web hosting services
- Bloggers and influencers
- Freelancers & unregistered businesses
- E-commerce consultants
- Individuals & students

Some of our big partners include Shopify, BigCommerce, E-Planet, Builder.AI, and thousands of freelancers and developers.

- **How to become a PayU partner and start referring merchants/customers?**

  You can become a PayU partner by registering yourself as a partner on PayU Website. For more information, refer to [Register a Partner Account](https://docs.payu.in/docs/register-a-partner-account).
- **What is the benefit of being a PayU partner?** 

  OR

  **I am a developer and how benefit of being a PayU partner?** 

  You get a steady monthly source of additional income from PayU for referring your customers or clients to the PayU product suite. The pricing for partners can be found under the partner dashboard.
- **How do I refer merchants/customers from the partner dashboard?** 

  You have three ways to refer merchants from the partner dashboard:

1. **Add Single Merchant** from the left navigation bar on the partner dashboard. For more information, refer to [Referral Onboarding](https://docs.payu.in/docs/referral-onboarding).
2. **Add Multiple Merchants** using the bulk referral feature from the left navigation bar on the partner dashboard. For more information, refer to [Referral Onboarding](https://docs.payu.in/docs/referral-onboarding#add-multiple-referral-merchants).
3. Using the **referral link** on the partner dashboard. For more information, refer to [Refer Merchants using Referral Links](https://docs.payu.in/docs/refer-merchants-using-referral-links).

- **Can I refer merchants without the partner portal? Using APIs?** 

  Yes, you can refer merchants using APIs:

  - Partner Integration APIs can be used to refer merchants, get merchant status (PAN verification, KYC, settlement, etc.). This is suitable for big platform partners. For more information, refer to [Refer Merchants using Partner Integration APIs](https://docs.payu.in/docs/refer-merchants-using-api).
  - Using OAuth to provide a co-branded solution with PayU with minimal integration. This is suitable for mid-size platform partners, individual resellers, website developers, etc.  For more information, refer to [Refer Merchants using Co-Branded (OAuth) Onboarding](https://docs.payu.in/docs/refer-merchants-using-co-branded-oauth-onboarding).
- **Can I complete the merchant profile on behalf of the merchants?** 

  Yes, you can do it using any of the following methods based on the number of merchants you wish to onboard:

1. **Partner Portal**. Details can be found here.
2. Partner Integration APIs can be used to refer merchants, get merchant status (PAN verification, KYC, settlement, etc.). This is suitable for big platform partners. For more information, refer to [Refer Merchants using Partner Integration APIs](https://docs.payu.in/docs/refer-merchants-using-api).
3. Using OAuth to provide a co-branded solution with PayU with minimal integration. This is suitable for mid-size platform partners, individual resellers, website developers, etc.  For more information, refer to [Refer Merchants using Co-Branded (OAuth) Onboarding](https://docs.payu.in/docs/refer-merchants-using-co-branded-oauth-onboarding).

- **How do I check the status of the referred merchants?** 

  The status of the referred merchants is available on the partner dashboard under referrals. Each merchant successfully referred has a MID (Merchant ID) attached to it once the referral is successful. You can also use our APIs here to get the status of referred merchants.
- **What payment methods are activated for my referred merchants?** 

  Depending on the solution that the merchant chooses, we offer all payment methods including Credit Card, Debit Card, UPI, Netbanking, Wallets, COD, Buy Now Pay Later, EMIs, etc. Even international payments can be activated on request to KAM.

## APIs

### Get Token API

- **What does it mean to have a wrong scope perspective in API usage?**   
  A wrong scope perspective occurs when the scope of an API request is incorrectly defined or misunderstood, leading to errors or unexpected behavior. This can happen if the permissions or access levels required for the API are not correctly specified.
- **How can I identify if I am using the wrong scope in my API request?**  
  You can identify a wrong scope by checking the error messages returned by the API. Common indicators include unauthorized access errors, permission denied messages, or responses indicating that the requested resource is not available.
- **What are the common causes of wrong scope issues in API requests?** Common causes include:
  - Incorrectly configured API keys or tokens.
  - Misunderstanding the required permissions for specific API endpoints.
  - Using outdated or incorrect documentation.
  - Not updating the scope when the API’s requirements change.
- **How can I avoid wrong scope issues when using APIs?**   
  To avoid wrong scope issues:
  - Always refer to the latest API documentation.
  - Ensure that your API keys or tokens have the correct permissions.
  - Regularly review and update your API configurations.
  - Test your API requests in a development environment before deploying them to production.
- **What should I do if I encounter a wrong scope error?**   
  If you encounter a wrong scope error:
  - Review the error message for specific details.
  - Check the API documentation to confirm the required scope.
  - Update your API request with the correct scope.
  - If the issue persists, contact the API provider’s support team for assistance.
- **Can wrong scope issues affect the security of my application?**   
  Yes, wrong scope issues can affect security. Using an incorrect scope might grant excessive permissions, leading to potential security vulnerabilities. Conversely, insufficient scope can prevent your application from functioning correctly.
- **How often should I review the scopes used in my API requests?** 

  It’s a good practice to review the scopes used in your API requests regularly, especially when there are updates to the API or changes in your application’s functionality. This helps ensure that your application remains secure and functions as expected.

## Incentives

- **How are my incentives calculated?** 

  Incentives are the difference between the rates offered to you (partner) and the rate charged to the merchants for different payment methods. You can check your plan in the Menu, under the My Plan section. You can also check the merchant plan while referring a merchant. This can be verified once the merchant onboarding is completed on the merchant agreement.

**Where can I view my incentives?** 

Your incentives are visible on the partner portal. For more information, refer to [Track Incentives](https://docs.payu.in/docs/track-incentives).

- **How do I get my incentives? Are there any mandatory steps?** 

You need to complete the following steps:

1. Complete your profile – enter general details, verify PAN, Bank, and KYC, and upload necessary documents. 
2. Ensure that merchants are transacting for you to earn incentives.
3. Raise a signed invoice with your KAM based on the incentives calculated on the partner dashboard.
4. Once the invoice is approved, incentives will be credited to your registered bank account on the 5th or 20th of every month.

- **I’m unable to see my incentives, what should I do?**

1. Check that your profile is completed.
2. Ensure that referred merchants are transacting and their transactions have been settled.
3. Raise an invoice with your KAM
4. If you have done all these steps and are still facing issues, please raise a query with your KAM.

- **How often can I raise an invoice on PayU Partner Portal?** 

You can raise an invoice once every month. However, invoice payments only happen on the 5th and 20th of every month.

- **I’m not getting the incentives for some of my merchants, what should I do?** 

  Contact your PayU Key Account Manager (KAM) with details or PayU support.
- **I want to refer merchants at non-default rates, what should I do?** 

  Contact your PayU Key Account Manager (KAM) if you want to onboard merchants at different rates.