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

- [Payment Links on PayU Dashboard](#payment-links-dashboard)
- [Integration APIs for Payment Links](doc:integration-api-for-payment-links)

## Workflow

The following workflow is involved from your customer perspective when using Payment Links API:

1. Merchants can create a form using different input fields to get information such as name, delivery address, customer IDs, DOB etc.
2. Alphanumeric, calendar and dropdown are the supported field types. The name can be customised as per the merchants need
3. Along with other link details like description and amount, the form is sent to the users as in the payment link URL.
4. When customers click on this link, they can see the form.
5. Customer fills in this form before proceeding to make a payment.

## Payment Links Dashboard

Select **Payment Tools **> **Payment Links** from the left pane of the Dashboard.

   The Payment Links Dashboard is displayed with the **Payment Link **and **Bulk Uploads** tabs.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8310ceb-Screenshot_2023-09-29_at_11.58.48_AM.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


The **Payment Link** tab includes the following details:

- **Created On:** Date of creation of the payment link.
- **Payment Link**: The payment link that was created.
- **Purpose of Payment:** The Payment description.
- **Amount**: Amount payed using the payment link.
- **Status:** Provide information on the status of the link Active, Deactivated or Expired.
- **Actions:** Act on the payment link, such as duplicate, share or disable the payment link.
- **Details:** View complete details of an individual payment link.

This part of the documentation includes the following sections:

- [Create a Payment Link](doc:create-a-new-payment-link)
- [Create Payments links in Bulks](doc:bulk-upload-to-create-multiple-payments-links)
- [Customize the Calendar View for Payment Links](doc:customize-the-calendar-view-for-payment-links)
- [Categorize the Payment Links View](doc:categorize-the-payment-links-view)
- [Export the Payment Link History](doc:export-the-payment-link-history)
- [Integration APIs for Payment Links](doc:integration-api-for-payment-links)
- [FAQs - Payment Links](doc:faqs-payment-links)