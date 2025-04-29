---
title: BNPL Link and Pay
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: Buy Now Pay Later (BNPL) Link and Pay
  description: >-
    Streamline your e-commerce transactions with PayU’s Buy Now Pay Later Link &
    Pay integration. Integrate with PayU’s Pay Later stack to enable the
    one-click checkout feature on the payment page. Get started with our
    comprehensive guide.
  keywords:
    - BNPL Link & Pay
    - BNPL Link and Pay
    - Buy Now Pay Later Link & Pay
    - BNPL 1-click checkout
    - BNPL one-click checkout
    - OTP-Less BNPL Integration
    - BNPL without OTP integration
    - PayU BNPL Link and Pay
    - Deferred Payment Link and Pay
  robots: index
next:
  description: ''
---
<Glossary>BNPL</Glossary> like Lazypay and Simpl allow your customers to checkout in "Click and Pay Later" with no hidden charges, while you get paid upfront. 

You can integrate with PayU’s Pay Later stack to enable the one-click checkout feature on the payment page, across BNPLs that support link and pay flow.

## Benefits for your customers

* 100% secure payments.
* Frictionless one-tap checkout experience.
* Pay later with 0% interest and no hidden charges.
* An easy sign-up process.

## Advantages

* 90%+ payment success rates.
* Increase in cart conversion rates.
* Improve user retention by providing a seamless checkout experience.
* Bump in average order value.

> 📘 Note:
>
> * PayU will extend this solution for other payment options within BNPL and be expanded to wallet partners shortly. 
> * The same integration will enable you to integrate all such supported payment options.

## Customer Journey

The customer journey involves the First-time User and Repeat User flows:

![](https://files.readme.io/8358f4e-image.png)

The following steps demonstrate how Rahul (for example) makes his first transaction using Pay Later on your website or mobile app (let’s call it Demoshop):

### First Time Flow

* Rahul logs in to your Demoshop, adds products/services to the cart, and proceeds to the checkout page.
* Even before landing on the checkout page, Demoshop initiates Eligibility API to check if Rahul is eligible.
* Post getting a successful eligibility response, the respective BNPL option will be shown to Rahul. (In case Rahul is not eligible, the respective lender option will be hidden/disabled on Demoshop.)
* Rahul clicks on his preferred BNPL lender’s button for which he is eligible, say Lazypay in this case. If Rahul is transacting for the first time on your Demostore, he will have to link his Lazypay account with Demoshop. (While for subsequent transactions, the transactions would be 1-click)
* Rahul will continue his transaction and go in the OTP authentication step.
* Lazypay sends an OTP for verification which John enters as part of the linking flow and also to complete his first transaction
* Once the linking is completed successfully, Lazypay shares an access token which is used for further subsequent transactions.

### Repeat User Flow

The following steps demonstrate how Rahul makes his subsequent transactions using Lazypay on Demoshop:

* Rahul comes to Demoshop again. Demoshop initiates the eligibility API of the checkout page to check for his present status. Lazypay sends the current eligibility status as success.
* Rahul clicks on Lazypay and Demoshop initiates the transaction directly. Demoshop initiates the payment call to successfully place the order.

> 📘 Note:
>
> User credentials will be the unique identifier for each user that will have to be passed by the merchant and will be used to identify each unique user. It will be string with the following format. abc:xyz (data type: string),abc corresponds to the merchant key and xyz corresponds to the user identifier. For example, **BmzSVc:userid**
