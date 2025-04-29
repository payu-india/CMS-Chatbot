---
title: Register for a Merchant Account
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  keywords:
    - merchant registration
    - ' register merchant'
    - ' create a PayU account'
    - ' merchant account'
    - ' checkout integration account'
  robots: index
next:
  description: ''
---
To integrate your website with PayU products and access PayU Dashboard, you require a merchant account. This section describes the procedure to register as a merchant.

> 📘 Note:
>
> After you register, PayU takes upto two days to validate your website (specified during registration). After your website is validated, you can get your merchant Key and Salt for integration. For more information, refer to [Generate Merchant Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard)

To register for a merchant account:

1. Navigate to the following URL using an internet browser:

[https://onboarding.payu.in/app/account](https://onboarding.payu.in/app/account)

   The *Create your PayU account* page is displayed.

<Image align="center" src="https://files.readme.io/2bbcb2c-register1.png" />

2. Provide the details for the following fields:

<Table>
  <thead>
    <tr>
      <th>
        **Field**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Email
      </td>

      <td>
        Enter your email address that will be used as user name and receiving communication from PayU.
      </td>
    </tr>

    <tr>
      <td>
        Set a Password
      </td>

      <td>
        Enter the password that you wish to use while logging into your merchant account with PayU. Your password must strictly meet these requirements:  

        * at least eight characters
        * at least one uppercase alphabet
        * at least one lowercase alphabet
        * at least one numeral
        * at least one special character
      </td>
    </tr>

    <tr>
      <td>
        Mobile
      </td>

      <td>
        Enter your 10-digit mobile phone number in this field.
      </td>
    </tr>

    <tr>
      <td>
        Do you want collect payments for your website?
      </td>

      <td>
        Select **Yes** (if required) and enter your website URL in the **Enter your Website URL** field.
      </td>
    </tr>

    <tr>
      <td>
        Monthly expected sales (in Rupees) 
      </td>

      <td>
        Enter your monthly expected sales or revenue.
      </td>
    </tr>
  </tbody>
</Table>

3. Click **Send OTP & Create Account**.

   The OTP is sent to the mobile number you have specified in the Phone Number field earlier.

> **Note**: At Step 4, the following message is displayed if you had already registered on PayU Merchant Onboarding site based the mobile number you have provided in the Phone Number field:\
> *Mobile Number already exists with PayU. Please continue with your old password to add new merchant account*.

4. Enter OTP sent to your mobile number that you specified earlier in the **Phone Number** field.
5. Click **Verify Mobile**.

> **Note**: After registration is completed, you cannot change the user type in Step 7.

6. Click **Confirm** to complete the registration.

> 📘 Reference:
>
> You need to activate your account after registration. For more information, refer to [Activate Account](doc:complete-your-kyc).
