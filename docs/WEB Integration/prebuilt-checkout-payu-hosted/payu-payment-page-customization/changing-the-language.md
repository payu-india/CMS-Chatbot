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

<Embed url="https://www.youtube.com/watch?v=7UCT0jFbB90" title="PayU Checkout For Bharat - A solution to expand your business beyond the top 10 cities of India!" favicon="https://www.google.com/favicon.ico" image="https://i.ytimg.com/vi/7UCT0jFbB90/hqdefault.jpg" provider="youtube.com" href="https://www.youtube.com/watch?v=7UCT0jFbB90" typeOfEmbed="youtube" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252F7UCT0jFbB90%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253D7UCT0jFbB90%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252F7UCT0jFbB90%252Fhqdefault.jpg%26key%3D7788cb384c9f4d5dbbdbeffd9fe4b92f%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />

The `display_lang` parameter should be set to one of the following values (same as corresponding language spelling):

* English
* Hindi
* Tamil
* Telugu
* Kannada
* Gujarati
* Marathi

Here is an example payment request API call with the `display_lang` parameter set to Hindi:

```curl
curl -X POST "https://test.payu.in/_payment -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=PQI6MqpYrjEefU&amount=10.00 &firstname=PayU User&email=test@gmail.com&phone=9876543210 &productinfo=iPhone&surl= https://apiplayground-response.herokuapp.com/ &furl=https://apiplayground-response.herokuapp.com/ &display_lang=Hindi&hash=05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072”
```

The PayU payment page is displayed with the display language as “Hindi” similar to the following screenshot:

![](https://files.readme.io/3aae0ef-hindipage.png)
