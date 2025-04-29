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

[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FfHhOQOj-5OA%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DfHhOQOj-5OA&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FfHhOQOj-5OA%2Fhqdefault.jpg&key=7788cb384c9f4d5dbbdbeffd9fe4b92f&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen; encrypted-media; picture-in-picture;\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=fHhOQOj-5OA",
  "title": "How To Integrate PayU To Your Wix Store? Key Steps To Follow",
  "favicon": "https://www.google.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/fHhOQOj-5OA/hqdefault.jpg",
  "provider": "https://www.youtube.com/",
  "href": "https://www.youtube.com/watch?v=fHhOQOj-5OA",
  "typeOfEmbed": "youtube"
}
[/block]


## Prerequisites

- Credentials to log in to your Wix account.
- Ensure that a store or site is set up on your Wix account where you want to configure the PayU as the payment provider
- If any PayU India plugin is installed, it must be removed.

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

- **Production**:  [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
- **Test / Sandbox**: [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)

8. Enter your Salt in the **Merchant Salt** field.
9. Click **Connect**.

The “PayU India connected” message is displayed similar to the following screenshot.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Wix_Connect_Success-1024x648.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "512px"
    }
  ]
}
[/block]


> 📘 Note:
> 
> PayU recommends this step to reconcile with PayU’s database after you receive the response. Verify the transaction details using the** Verification Payment **API. For API reference, refer to <a href="verify_payment_api" target="_blank">Verify Payment API</a>..