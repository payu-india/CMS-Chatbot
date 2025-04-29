---
title: v2 PayU Hosted Checkout
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Prebuilt Web Checkout or PayU Hosted Checkout is a payment integration method provided by PayU for merchants who want to accept payments on their website. It offers a secure way to collect payments from customers by redirecting them to a PayU-hosted payment page.

> 📘 v2/payment Recommended for new integrations:
> 
> PayU recommends v2/payment API for your new integration or if you are new merchant onboarded to PayU from March 2025. 
> 
> If you have already integrated with **\_payment** (v1) API, refer to[ PayU Hosted Checkout Integration \[v1\]](https://docs.payu.in/v1/docs/prebuilt-checkout-payu-hosted).

## How it works?

To use PayU Hosted Checkout, merchants need to integrate the PayU payment gateway into their website. Once integrated, customers can select the payment method they want to use and enter their payment details on the payment form. When they click the **Pay** button, they will be redirected to a PayU-hosted payment page where they will complete the payment process.

Once the payment is processed, the customer will be redirected back to the merchant's website where they can view the payment result.

## Customer journey

The following sample customer journey is for cards payment mode:

1. The customer clicks **Pay Now** on merchant website after checkout.
2. The customer is redirected to \_PayU Payment \_page.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1ee3893480e6e3d3c1e28d6ecffc4c52d1b3e8f2aba0247c9eb486dfef0fafc5-Screenshot_2024-09-06_at_11.54.02_AM.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "622px",
      "border": true
    }
  ]
}
[/block]


3. The customer chooses a payment mode from the \_PayU Payment \_page. For example, **Cards (Debit/Credit)**.
4. The card details are provided by the customer and clicks **Proceed**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/fd09cbd284ffe7fb3b60d03e2acd8a5a51d850dd1795f1eca9879893b3569603-Screenshot_2024-09-06_at_11.56.40_AM.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "622px",
      "border": true
    }
  ]
}
[/block]


   A consent message is displayed whether the card the details can be stored.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/caa8481-Screenshot_2023-10-05_at_10.37.33_AM.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "622px"
    }
  ]
}
[/block]


5. Customer clicks **Save and Continue**.
6. The OTP page is displayed where the customer enters OTP sent to the them.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/289fa82-Screenshot_2023-10-05_at_10.37.42_AM.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "422px"
    }
  ]
}
[/block]


6. PayU redirects back to the merchant website based on the success URL (surl) or failure URL (furl) specified.

## Benefits of PayU Hosted Checkout

The following is a list of benefits of PayU Hosted Checkout:

- Simplified payment workflow for your customers while reducing the cost of designing complex payment functionalities within your environment.
- Going live with new payment modes requires zero development. They can be enabled with a simple switch.
- Assures the security of your customer payment credentials.
- PCI-DSS certifications to operate your facility are not mandatory.
- PayU Hosted Checkout extends cross-functional support at organizational roles within the organization.
- The Native UI feature of Web Checkout Pro allows you to ensure continuous usability (UX) and brand coherence by customizing the PayU-hosted environment with the business logo and color scheme of your choice, simulating your business website.
- Offers zero direction OTP authentication flow for cards with Native OTP.
- Supports specific and generic intent for UPI payments on mobile web
- Personalized payment experience (using recommendations) and offers.