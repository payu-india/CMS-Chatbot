---
title: Register for a Merchant Account
excerpt: ''
deprecated: false
hidden: false
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

<https://onboarding.payu.in/app/account>

   The _Create your PayU account_ page is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2bbcb2c-register1.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


2. Provide the details for the following fields:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "0-0": "Email",
    "0-1": "Enter your email address that will be used as user name and receiving communication from PayU.",
    "1-0": "Set a Password",
    "1-1": "Enter the password that you wish to use while logging into your merchant account with PayU. Your password must strictly meet these requirements:  \n  \n- at least eight characters\n- at least one uppercase alphabet\n- at least one lowercase alphabet\n- at least one numeral\n- at least one special character",
    "2-0": "Mobile",
    "2-1": "Enter your 10-digit mobile phone number in this field.",
    "3-0": "Do you want collect payments for your website?",
    "3-1": "Select **Yes** (if required) and enter your website URL in the **Enter your Website URL** field.",
    "4-0": "Monthly expected sales (in Rupees) ",
    "4-1": "Enter your monthly expected sales or revenue."
  },
  "cols": 2,
  "rows": 5,
  "align": [
    null,
    null
  ]
}
[/block]


3. Click **Send OTP & Create Account**.

   The OTP is sent to the mobile number you have specified in the Phone Number field earlier.

> **Note**: At Step 4, the following message is displayed if you had already registered on PayU Merchant Onboarding site based the mobile number you have provided in the Phone Number field:  
> _Mobile Number already exists with PayU. Please continue with your old password to add new merchant account_.

4. Enter OTP sent to your mobile number that you specified earlier in the **Phone Number** field.
5. Click **Verify Mobile**.

> **Note**: After registration is completed, you cannot change the user type in Step 7.

6. Click **Confirm** to complete the registration.

> 📘 Reference:
> 
> You need to activate your account after registration. For more information, refer to [Activate Account](doc:complete-your-kyc).