---
title: Workflow
excerpt: >-
  The Dynamic Currency Conversion process starts with the consumer payment page,
  and when the customer wishes to make a payment for any goods and services and
  provides the necessary card details.
deprecated: false
hidden: false
metadata:
  title: PayU International Payments Workflow
  description: >-
    Discover how to integrate international payments with PayU, a leading online
    payment service provider in India. Learn how to enable dynamic currency
    conversion for your customers using PayU’s hosted checkout and APIs.
  keywords:
    - Dynamic Currency Conversion Workflow
    - DCC Integration Steps
    - PayU Currency Conversion Workflow
    - Currency Conversion Process
    - DCC Implementation Workflow
    - Multi-Currency Payment Flow.International Payments Workflow
    - Foreign Currency Payment Setup
  robots: index
next:
  description: ''
---
The foreign currency is converted by the PayU’s integration API and then the merchant is given the option to choose the card currency like INR for making the payments.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/07/DCC-Process-Flow-1-1024x486.png)

## Customer Journey with PayU Hosted Checkout

[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FJPJ-kjL0V80%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DJPJ-kjL0V80&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FJPJ-kjL0V80%2Fhqdefault.jpg&key=7788cb384c9f4d5dbbdbeffd9fe4b92f&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen; encrypted-media; picture-in-picture;\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=JPJ-kjL0V80",
  "title": "PayU International Payments - A look at PayU's International Payments Customer Journey",
  "favicon": "https://www.google.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/JPJ-kjL0V80/hqdefault.jpg",
  "provider": "https://www.youtube.com/",
  "href": "https://www.youtube.com/watch?v=JPJ-kjL0V80",
  "typeOfEmbed": "youtube"
}
[/block]


## Steps Involved

After your customer completes the checkout, you redirect to PayU Payment page and the following steps are involved on PayU Payment page:

1. Customer clicks **Pay Now** on your website.

   The _PayU Payment_ page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/11/Screenshot-2022-11-25-at-12.28.35-PM-1-859x1024.png)

2. Customer selects **Cards (Credit/Debit)** option.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/11/Screenshot-2022-11-25-at-12.28.57-PM-853x1024.png)

3. Customer enters the international card number details and clicks **Proceed**.

The Bank OTP page is displayed to validate the customer’s card.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/11/Screenshot-2022-11-18-at-2.28.39-PM-1024x882.png)

4. Customer enters the OTP sent by bank to their registered mobile number and clicks **Submit**.
5. PayU gets the response and sends to you to process the order.