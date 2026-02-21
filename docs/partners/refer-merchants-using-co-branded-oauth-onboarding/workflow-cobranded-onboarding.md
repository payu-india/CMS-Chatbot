---
title: Workflow for Co-Branded Onboarding
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
Co-Branded (OAuth) Onboarding or OAuth Workflow (technical workflow) involves the steps as illustrated in the following diagram:

<Image align="center" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/12/diagram-description-automatically-generated.png" className="border" />

The merchant’s workflow involves the following steps:

1. Merchant clicks on the link at the partner website and gets redirected to PayU for onboarding.
2. After onboarding on PayU, they are asked to give consent to their partner for sharing their credentials.
3. On acceptance, the merchant is redirected to the URL specified in the partner account.

> **Example**: If the redirect URL is [https://abc.com](https://abc.com), the merchant will be redirected to the following URL:

[https://abc.com?auth_code=$\{code}&merchantId=$\{mid}](https://abc.com?auth_code=$\{code}\&merchantId=$\{mid})

> **Note**: The steps to get the merchant credentials require only two APIs. This removes the entry of merchant key and salt on a partner website. PayU recommends this for the seamless onboarding of merchants.

4. From the above authorization code, call valid Auth code and client API_**.**_ For more information, refer [Validate Auth Code and Client](ref:validate_authcode_and_client_api).

\{\{hub_base_url}}/oauth/token

Partner will get access token in response

5. Call the Credential API using the access token from Step 4. For more information, refer to [Get Merchant Credentials API](ref:get_merchant_credentials_api)

\{\{partner_base_url}}/api/v1/merchants/\{\{mid}}/credential

## Merchant Sign-Up Workflow with Co-Branded Onboarding

To sign up a merchant using OAuth:

1. Navigate to the OAuth link appended with the new email id in the following format:

`https://onboarding.payu.in/app/account/signup?reseller_id=<Merc ID>&email=<Merchant mail ID to sign-up>`

Where \<`Merchant ID`> is substituted with reseller ID and \<`Merchant mail ID to sign-up`> is substituted with merchant mail ID to sign-up.

For example:

`[https://onboarding.payu.in/app/account/signup?reseller_id=66ed-fc3c-512f47ed-ac95-4319452fbd89&state=Uqnr5ge22U](https://onboarding.payu.in/app/account/signup?reseller_id=66ed-fc3c-512f47ed-ac95-4319452fbd89\&state=Uqnr5ge22U)

The Merchant Sign-up page is displayed.

![Picture 3](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/12/picture-3.png)

2. Enter the merchant’s phone and password.
3. Click **Next**.

> **Note**: If the mobile number already exists, the following message is displayed.

![Picture 5](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/12/picture-5.png)

4. Enter the OTP sent to the mobile number that was entered by you in Step 1.

![Picture 6](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/12/picture-6.png)

1. Enter the OTP sent to your email ID.

![Picture 7](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/12/picture-7.png)

5. Select any of the following roles:
   * Business Owner
   * Developer
   * Customer

![Picture 8](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/12/picture-8.png)

A list of questions is displayed on the _What are you looking for from PayU_? page similar to the following screenshot:

![Picture 9](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/12/picture-9.png)

6. Provide input for each question on the _What are you looking for from PayU_? page.

A welcome message is displayed similar to the following screenshot.

![Picture 10](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/12/picture-10.png)

7. Click **Activate Account**.

The _Complete your full KYC_ page, similar to the following screenshot is displayed. For more information on completing your KYC, refer to [Activate Account](doc:complete-your-kyc)

![Picture 11](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/12/picture-11.png)

## Merchant Login Workflow with Co-Branded Onboarding

The merchant login workflow with Co-Branded (OAuth) Onboarding involves:

1. Navigate to the OAuth link appended with the new email id in the following format:

`https://onboarding.payu.in/app/account?reseller_id=<Merchant ID>&email=<Merchant mail ID to sign-up>`

Where \<`Merchant ID`> is substituted with reseller ID and \<`Merchant mail ID to sign-up`> is substituted with merchant mail ID to sign-up.

For example:

[https://onboarding.payu.in/app/account?reseller_id=11ea-c29b-c691cce0-8256-02aa98a2d2b0&email=[ishikanarang27@gmail.com](mailto:ishikanarang27@gmail.com)](https://onboarding.payu.in/app/account?reseller_id=11ea-c29b-c691cce0-8256-02aa98a2d2b0\&email=\[ishikanarang27@gmail.com]\(mailto:ishikanarang27@gmail.com\))

The Merchant Login page is displayed.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/07/image-10-1.jpg)

2. Enter the merchant password and click **Verify**.

   The _Authorize Your Account_ page is displayed.

![Image](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/12/image-6.png)

3. Click **Allow access to the account** to provide consent.

   A confirmation message is displayed, similar to the following screenshot:

![Image](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/12/image-7.png)

4. Click **Back to\<app name> app**.
