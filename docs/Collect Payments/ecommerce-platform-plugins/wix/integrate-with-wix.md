---
title: Integrate with Wix
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
After you set up your account in Wix, you can integrate PayU India as the payment platform for your customers. If you face any issues while integration, refer to [Troubleshooting Wix Integration](doc:troubleshooting-wix-integration).

The following video explains how to integrate Wix with PayU as the payment gateway:

<Embed url="https://www.youtube.com/watch?v=fHhOQOj-5OA" href="https://www.youtube.com/watch?v=fHhOQOj-5OA" typeOfEmbed="youtube" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252FfHhOQOj-5OA%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DfHhOQOj-5OA%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252FfHhOQOj-5OA%252Fhqdefault.jpg%26key%3D7788cb384c9f4d5dbbdbeffd9fe4b92f%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />

## Prerequisites

* Credentials to log in to your Wix account.
* Ensure that a store or site is set up on your Wix account where you want to configure the PayU as the payment provider
* If any PayU India plugin is installed, it must be removed.

## Procedure

To integrate Wix with PayU as a payment gateway:

1. Log in to your Wix account if not already logged in.

   Your Wix account home page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/wix_home_page-1024x461.png)

2. Select **Settings** from the menu (at the bottom of the left navigation pane).

   The _Settings_ page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Wix_Accept_Payments_menu_selection-1024x473.png)

3. Select **Accept Payments** on the **Settings** page.

   The _Accept Payments_ page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Wix_See_More_Pymt_Options-1024x539.png)

4. Click **See More Payment Options** at the bottom.

   The _More Payment Options_ page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Wix_More_Pymt_Options_Page-1024x512.png)

5. Click **Connect** on the **PayU India** tile.

   The _Connect PayU_ India page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Wix_Connect_PayU_India_Page1-1024x571.png)

```
Scroll down to navigate to the **Account Information** section.
```

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Wix_Connect_PayU_India_Options-1024x672.png)

6. Configure the merchant key and Salt.
7. Enter your merchant key in the **Merchant Key** field.

**Reference**: For more information on how to generate the Key and Salt, refer to any of the following:

* **Production**:  [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
* **Test / Sandbox**: [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)

8. Enter your Salt in the **Merchant Salt** field.
9. Click **Connect**.

The “PayU India connected” message is displayed similar to the following screenshot.

<Image align="center" width="512px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Wix_Connect_Success-1024x648.png" />

<Callout icon="📘" theme="info">
  **Note**: PayU recommends this step to reconcile with PayU’s database after you receive the response. Verify the transaction details using the **Verification Payment**API. For API reference, refer to <a href="https://docs.payu.in/reference/verify_payment_api" target="_blank">Verify Payment API</a>..
</Callout>
