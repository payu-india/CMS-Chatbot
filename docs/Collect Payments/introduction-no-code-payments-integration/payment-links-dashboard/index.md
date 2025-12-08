---
title: Payment Links
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Dashboard for Payment Links
  description: ''
  keywords:
    - 'Create Payment Link:'
    - ' Payment Link Integration'
    - ' Create Payment Link in a few minutes'
  robots: index
next:
  description: ''
---
You can share the payment link with customers to collect payments from them. You can create and manage payment links using:

* [Payment Links on PayU Dashboard](#payment-links-dashboard)
* [Integration APIs for Payment Links](doc:integration-api-for-payment-links)

Check the following video on PayU Payments Link offerings:

<br />

<Embed typeOfEmbed="youtube" url="https://www.youtube.com/watch?v=rh_FQUMsaT0" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252Frh_FQUMsaT0%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253Drh_FQUMsaT0%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252Frh_FQUMsaT0%252Fhqdefault.jpg%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" href="https://www.youtube.com/watch?v=rh_FQUMsaT0" providerUrl="https://www.youtube.com/" providerName="YouTube" />

## Workflow

The following workflow is involved from your customer perspective when using Payment Links API:

1. Merchants can create a form using different input fields to get information such as name, delivery address, customer IDs, DOB etc.
2. Alphanumeric, calendar and dropdown are the supported field types. The name can be customised as per the merchants need
3. Along with other link details like description and amount, the form is sent to the users as in the payment link URL.
4. When customers click on this link, they can see the form.
5. Customer fills in this form before proceeding to make a payment.

## Payment Links Dashboard

Select **Payment Tools** > **Payment Links** from the left pane of the Dashboard.

The Payment Links Dashboard is displayed with the **Payment Link** and **Bulk Uploads** tabs.

<Image align="center" border={true} src="https://files.readme.io/cc35b704632bded3088580a070ffaf24f203c3713f7880fb0a2cdc6e5b8bc842-Screenshot_2025-06-02_at_7.05.43_PM.png" className="border" />

The **Payment Link** tab includes the following details:

* **Created On:** Date of creation of the payment link.
* **Payment Link**: The payment link that was created.
* **Purpose of Payment:** The Payment description.
* **Amount**: Amount payed using the payment link.
* **Status:** Provide information on the status of the link Active, Deactivated or Expired.
* **Actions:** Act on the payment link, such as duplicate, share or disable the payment link.
* **Details:** View complete details of an individual payment link.

This part of the documentation includes the following sections:

* [Create a Payment Link](doc:create-a-new-payment-link)
* [Create Payments links in Bulks](doc:bulk-upload-to-create-multiple-payments-links)
* [Customize the Calendar View for Payment Links](doc:customize-the-calendar-view-for-payment-links)
* [Categorize the Payment Links View](doc:categorize-the-payment-links-view)
* [Export the Payment Link History](doc:export-the-payment-link-history)
* [Integration APIs for Payment Links](doc:integration-api-for-payment-links)
* [FAQs - Payment Links](doc:faqs-payment-links)
