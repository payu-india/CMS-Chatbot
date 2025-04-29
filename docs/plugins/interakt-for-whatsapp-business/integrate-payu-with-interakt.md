---
title: Integrate PayU with Interakt
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
To Integrate PayU with Interakt:

1. Go to <https://app.interakt.ai/login> to **Sign in** to your Interakt account. If you do not have an Interakt account, go to <https://app.interakt.ai/signup> to **Sign Up**.
2. Go to **Settings** > **Integrations**

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/11/Screenshot-2022-11-30-at-3.49.38-PM-468x1024.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "322px",
      "border": true
    }
  ]
}
[/block]


3. Select PayU under all apps and click **Connect to Interakt**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/11/Screenshot-2022-11-30-at-3.36.46-PM-1024x587.png",
        null,
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


4. Login to PayU with valid credentials. If you are new to PayU click **Sign Up**to create an account.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/12/Screenshot-2022-12-05-at-11.36.36-AM.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "322px",
      "border": true
    }
  ]
}
[/block]


5. Click **Allow Access to this Account** to authorize the integration.
6. Click **Back to Interakt** to go back to the Interakt dashboard.

### Collect payment with WhatsApp

To send embedded PayU payment links on WhatsApp using Interakt:

1. Sign in to your Interakt account on the following link: <https://app.interakt.ai/login>.
2. Navigate to Inbox and click the **dollar($)** button in the reply pane as highlighted in the screenshot below.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/11/Screenshot-2022-11-09-at-1.56.44-PM-1024x514.png",
        null,
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


3. Select the currency and enter the amount that you want to accept and click **Generate PaymentLink**.
4. Click **Send Link** to embed it in your message.
5. Click **Send** to send the message to your customer.

[block:image]{"images":[{"image":["https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/11/Screenshot-2022-11-09-at-2.02.17-PM-1024x481.png",null,null],"align":"center","border":true}]}[/block]

```
   Your customer receives the payment link on WhatsApp and completes the payment with PayU.
```

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/11/Screenshot-2022-11-09-at-2.08.44-PM-1-1024x635.png)

## Collect payment with WhatsApp

To send embedded PayU payment links on WhatsApp using Interakt:

1. Sign in to your Interakt account on the following link: <https://app.interakt.ai/login>.
2. Navigate to Inbox and click the **dollar($)** button in the reply pane as highlighted in the screenshot below.

[block:image]{"images":[{"image":["https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/11/Screenshot-2022-11-09-at-1.56.44-PM-1024x514.png",null,null],"align":"center","border":true}]}[/block]

3. Select the currency and enter the amount that you want to accept and click **Generate PaymentLink**.
4. Click **Send Link** to embed it in your message.
5. Click **Send** to send the message to your customer.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/11/Screenshot-2022-11-09-at-2.02.17-PM-1024x481.png)

   Your customer receives the payment link on WhatsApp and completes the payment with PayU.

[block:image]{"images":[{"image":["https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/11/Screenshot-2022-11-09-at-2.08.44-PM-1-1024x635.png",null,null],"align":"center","border":true}]}[/block]

> 📘 Note:
> 
> PayU recommends this step to reconcile with PayU’s database after you receive the response. Verify the transaction details using the** Verification Payment **API. For API reference, refer to <a href="verify_payment_api" target="_blank">Verify Payment API</a>..