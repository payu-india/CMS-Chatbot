---
title: Check your API Key and Salt
excerpt: >-
  This section describes the prerequisites and how to check your API Key and
  Salt.
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Before you Begin

You need to activate your account with PayU to get the key and salt details on PayU Dashboard. You account gets activated only if you had submitted all the basic documents while onboarding. For more information, refer to Complete your KYC.

> **Notes**: The API key and Salt will not be visible or accessible for merchants who have not completed onboarding or website was verified by PayU. While onboarding, the website verification takes 1-2 days.\
> The API key and Salt will not be visible for merchants without a website.

## Check Key and Salt

To integrate PayU payment gateway into your website, you need to generate an API key and salt. Please follow the below-mentioned steps to generate the same:

1. Navigate to the following URL and log in to Merchant Dashboard.:
2. Select **Payment Gateway** under **Collect Payments** from the menu on the left-pane.\
   The Payment Gateway Integrations page is displayed similar to the following screenshot.
3. Under the **API Keys** section, click on the **Generate New Key** button
4. Enter a name for the API key and click on the **Save** button\
   Once the API key is generated, click on the **Download** button to download the **API Key** and **Salt** in a `.txt` file
5. Store the downloaded API key and salt securely in your server

> **Note**: Keep the API key and salt secure and do not share it with anyone. If you suspect any unauthorized access to your API key and salt, immediately regenerate a new API key and salt from the PayU Dashboard and update it in your server. If you face any issues while generating the API key and salt or integrating PayU payment gateway in your website, please contact PayU support for assistance.
