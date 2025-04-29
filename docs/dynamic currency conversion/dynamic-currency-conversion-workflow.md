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

<Embed url="https://www.youtube.com/watch?v=JPJ-kjL0V80" title="PayU International Payments - A look at PayU's International Payments Customer Journey" favicon="https://www.google.com/favicon.ico" image="https://i.ytimg.com/vi/JPJ-kjL0V80/hqdefault.jpg" provider="youtube.com" href="https://www.youtube.com/watch?v=JPJ-kjL0V80" typeOfEmbed="youtube" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252FJPJ-kjL0V80%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DJPJ-kjL0V80%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252FJPJ-kjL0V80%252Fhqdefault.jpg%26key%3D7788cb384c9f4d5dbbdbeffd9fe4b92f%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />

## Steps Involved

After your customer completes the checkout, you redirect to PayU Payment page and the following steps are involved on PayU Payment page:

1. Customer clicks **Pay Now** on your website.

   The *PayU Payment* page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/11/Screenshot-2022-11-25-at-12.28.35-PM-1-859x1024.png)

2. Customer selects **Cards (Credit/Debit)** option.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/11/Screenshot-2022-11-25-at-12.28.57-PM-853x1024.png)

3. Customer enters the international card number details and clicks **Proceed**.

The Bank OTP page is displayed to validate the customer’s card.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/11/Screenshot-2022-11-18-at-2.28.39-PM-1024x882.png)

4. Customer enters the OTP sent by bank to their registered mobile number and clicks **Submit**.
5. PayU gets the response and sends to you to process the order.
