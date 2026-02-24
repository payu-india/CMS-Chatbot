---
title: Enable Co-Branded Onboarding (OAuth) for Partners
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
The following are the major steps involved to enable Co-Branded Onboarding (OAuth) for partners:

1. Create a partner account at [https://partner.payu.in](https://partner.payu.in/) if required. For more information, refer to [Register a Partner Account](doc:register-a-partner-account)
2. Request enablement of OAuth with your PayU Key Account Manager. You need to ensure that the following OAuth scope is configured for your account.

```plaintext
Scope name: credentials_using_oauth
```

3. Configure the URLs in the application. For more information, refer to [Configure URLs and Logo](doc:configure-urls-and-logo).
4. Update the brand logo and theme colour for the onboarding journey and save.

> **Note**: Brand Logo should be in jpg/jpeg, less than 5MB in size, and width and height should be 90 pixels. For more information on configuring the brand logo, refer to [Configure URLs and Logo](doc:configure-urls-and-logo).

5. Show case the onboarding URL details at your website so that your merchants can sign up:

   `{{onboarding_base_url}}/app/account?reseller_id={{reseller_id}}`

<Callout icon="📘" theme="info">
  **Note**: The following environment or base URLs must be used based on the Test or Production environment:
</Callout>

|                |                                                                      |
| -------------- | -------------------------------------------------------------------- |
| **Test**       | \<[https://uat-onboarding.payu.in>](https://uat-onboarding.payu.in>) |
| **Production** | \<[https://onboarding.payu.in>](https://onboarding.payu.in>)         |

6. Merchants can perform any of the following steps:
   * For merchants who need to register, refer to [Workflow for Co-Branded Onboarding](doc:workflow-cobranded-onboarding)
   * For merchants who have already registered, refer to [Workflow for Co-Branded Onboarding](doc:workflow-cobranded-onboarding)

The partner can pass the email of the merchant in the URL and the user will be taken to the Sign-in or Signup page. For example:

[https://onboarding.payu.in/app/account/signup?reseller_id=66ed-fc3c-512f47ed-ac95-4319452fbd89&state=Uqnr5ge22U](https://onboarding.payu.in/app/account/signup?reseller_id=66ed-fc3c-512f47ed-ac95-4319452fbd89\&state=Uqnr5ge22U)

Here, the state parameter is the unique identifier of the session. Once the merchant is redirected beck to your platform, PayU will post the merchant id, auth code & the same state parameter to your configured redirect URL.

<br />
