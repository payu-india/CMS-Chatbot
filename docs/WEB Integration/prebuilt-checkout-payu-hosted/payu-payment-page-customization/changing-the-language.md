---
title: Change the Language
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Change the Language for your PayU Checkout Page
  description: >-
    Learn how to change the display language of PayU’s hosted checkout page to
    match your customers’ preferences. This page provides information on how to
    use the udf1 parameter to specify the language code for your checkout page.
  robots: index
next:
  description: ''
---
To change the display language in PayU Hosted Checkout, add the `language` parameter to the payment request API call. The following video shows how vernacular support can improve your business:


[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2F7UCT0jFbB90%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D7UCT0jFbB90&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2F7UCT0jFbB90%2Fhqdefault.jpg&key=7788cb384c9f4d5dbbdbeffd9fe4b92f&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen; encrypted-media; picture-in-picture;\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=7UCT0jFbB90",
  "title": "PayU Checkout For Bharat - A solution to expand your business beyond the top 10 cities of India!",
  "favicon": "https://www.google.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/7UCT0jFbB90/hqdefault.jpg",
  "provider": "https://www.youtube.com/",
  "href": "https://www.youtube.com/watch?v=7UCT0jFbB90",
  "typeOfEmbed": "youtube"
}
[/block]




The `display_lang` parameter should be set to one of the following values (same as corresponding language spelling):

- English
- Hindi
- Tamil
- Telugu
- Kannada
- Gujarati
- Marathi

Here is an example payment request API call with the `display_lang` parameter set to Hindi:

```curl
curl -X POST "https://test.payu.in/_payment -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=PQI6MqpYrjEefU&amount=10.00 &firstname=PayU User&email=test@gmail.com&phone=9876543210 &productinfo=iPhone&surl= https://apiplayground-response.herokuapp.com/ &furl=https://apiplayground-response.herokuapp.com/ &display_lang=Hindi&hash=05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072”
```

The PayU payment page is displayed with the display language as “Hindi” similar to the following screenshot:

![](https://files.readme.io/3aae0ef-hindipage.png)