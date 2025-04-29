---
title: Access Production Key and Salt
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
Before starting Web Checkout integration or integrating your website with PayU products, you need to generate your API key and Salt using the PayU Merchant Dashboard. For more information on how to toggle between the Live and Test mode on Dashboard, refer to [Toggle between Live and Test Mode](doc:toggle-between-live-and-test-mode).

## Before you Begin

You need to activate your account with PayU to get the key and salt details on PayU Dashboard. You account gets activated only if you had submitted all the basic documents while onboarding. For more information, refer to [Activate Account](doc:complete-your-kyc).

> 📘 Notes:
> 
> - The API key and Salt will not be visible or accessible for merchants who have not completed onboarding or website was verified by PayU. While onboarding, the website verification takes 1-2 days.
> - The API key and Salt will not be visible for merchants without a website.

## Procedure to Access Key and Salt

To generate Salt from the PayU Merchant Dashboard:

1. Log in to PayU Dashboard using the following log on page:

<https://onboarding.payu.in/app/account/signin>

2. Switch to **Live Mode** from the toggle option on the menu bar. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e36828514287161a9b189454dd07463fea3a0697651e04b8f22ba3fc7bffbd54-Screenshot_2024-10-01_at_5.31.20_PM.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "320px",
      "border": true
    }
  ]
}
[/block]


3. Select **Developer** from the menu on the left-pane and select the** API Details **tab if required.

The_ Developers_ page is displayed similar to the following screenshot. The values for the following fields are generated automatically (for the first time) and displayed similar to the following screenshot:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0ddaa94d203d7102154ece7c74b95ec50274d3fc3e4004ed64bbb8eadc0b37f3-dashboard_key_salt_live_mode.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


- **key**: The API key that you must use for all payment requests.
- **Salt-32 bit**: The Salt, v1 is the 32-character string that you must use to generate a hash and further post the hash along with parameters when posting a payment request with PayU.
- **Salt-256 bit**: The Salt, v2 that you must use to generate a hash and further post the hash along with parameters when posting a payment request with PayU.

> 📘 Note:
> 
> Use the** Copy Key** or **Copy Salt** button next to each field to copy them to a text file and save them in a confidential location for your perusal. This will avoid any typos with the merchant key.

## Regenerate and Activate Key and Salt

To regenerate key and salt and then activate them:

1. Log in to PayU Dashboard using the following log on page:

<https://onboarding.payu.in/app/account/signin>

2. Switch to **Live Mode** from the toggle option on the menu bar. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e36828514287161a9b189454dd07463fea3a0697651e04b8f22ba3fc7bffbd54-Screenshot_2024-10-01_at_5.31.20_PM.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "320px",
      "border": true
    }
  ]
}
[/block]


3. Select **Developer** from the menu on the left-pane and select the** API Details **tab if required.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5173f9e018d851a3d01a90a3644ad2f201245305a920e0d53a285d935a5ced95-dashboard_regenerate_salt.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


4. Click the **Regenerate Salt** button to generate new salt.

   A confirmation pop-up message is displayed similar to the following screenshot:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/41a57c7d4a7ad13a27b56634e8eeb0d8f812f71e973fc6ca496f3fa1701c0992-dashboard_regenerate_salt_confirmation.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "450px"
    }
  ]
}
[/block]


5. Click the **Regenerate** button.

   The _Success_ message is displayed at top-right corner similar to the following screenshot:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d5538ab7c7b8a3c8418b58421110d9592b10e9f6bbc83a6d66de17372ab8cce9-dashboard_regenerate_salt_activate.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


6. Click the **Activate** button displayed for **Salt** under the **Actions** column.

> 📘 Notes:
> 
> - New Salt expires in 15 days expiry if not activated.
> - If the new Salt not activated within the 15 days, you will require to regenerate another salt.
> - After the new Salt is activated, the new Salt will be updated to replace of Salt version 1. 
> - PayU recommends you to activate the regenerated Salt to avoid any payment or API call failures with your customers.