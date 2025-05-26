---
title: Choose your Integration
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
PayU provides payment gateway solutions to online businesses through its cutting-edge and award-winning technology.

To choose the right products (API Integration) for your business, you need to consider factors like:

* The type of payments you want to accept (cards, UPI, wallets, etc.)
* The currencies you want to support
* The level of security and fraud prevention you need
* The features and functionalities you want to offer your customers (save card, retry option, express checkout, etc.)
* Split the payments while the transaction or later
* Become a partner and onboard your merchants

PayU India offers following products to choose from:

<details>
  <summary>Product Offerings</summary>

  <HTMLBlock>{`
                  <ul>
                    <li>Web Checkout
                      <ul>
                        <li>Choose between Prebuilt Web Checkout (PayU Hosted Checkout), Custom Checkout (Merchant Hosted Checkout) or Low Code Web SDK integration based on your resources and time to integrate as described in Collect Payment from your website. With your Web Checkout integration, you can opt-in for the following PayU products:
                          <ul>
                            <li>Recurring Payments</li>
                            <li>International Payments</li>
                            <li>Cross-Border Payments</li>
                            <li>Split Settlements</li>
                          </ul>
                          You can value add to your existing PayU Web Checkout integration with the following products:
                          <ul>
                            <li>Save Cards</li>
                            <li>Offers</li>
                            <li>Recommendation Engine</li>
                          </ul>
                        </li>
                      </ul>
                    </li>
                    <li>Mobile SDK
                      <ul>
                        <li>PayU offers following mobile SDK platforms to choose from:
                          <ul>
                            <li>[Android](#android)</li>
                            <li>[iOS](#ios)</li>
                            <li>React Native</li>
                            <li>Cordova</li>
                            <li>Flutter</li>
                          </ul>
                          You can choose to integrate using the Checkout Plus, the pre-built GUI for Android, iOS or React Native or use various SDK components as described in <a href="#collect-payment-from-mobile">Collect payment from Mobile</a>.
                        </li>
                      </ul>
                    </li>
                    <li>Payment Links
                      <ul>
                        <li>Send payment links instantly to your customers.</li>
                      </ul>
                    </li>
                    <li>Plugins for eCommerce platforms
                      <ul>
                        <li>PayU offers plugins for major eCommerce platforms including WhatsApp for Business, Shopify, WooCommerce, BigCommerce, etc. as described in <a href="#collect-payment-on-ecommerce-platforms">Collect payment on eCommerce platforms</a>.</li>
                      </ul>
                    </li>
                    <li>Partner Integration
                      <ul>
                        <li>PayU offers you a platform to refer merchants and earn incentives. For more information, refer to <a href="#become-a-partner">Become a partner</a>.</li>
                      </ul>
                    </li>
                    <li>Omnichannel
                      <ul>
                        <li>Share QR codes to your customers instantly. For more information, refer to <a href="#collect-payment-thru-omnichannel">Collect payment thru Omnichannel</a>.</li>
                      </ul>
                    </li>
                    <li>Payouts
                      <ul>
                        <li>Make instant payments to your vendors or employees. For more information, refer to <a href="#make-payments">Make payments</a>.</li>
                      </ul>
                    </li>
                  </ul>
  `}</HTMLBlock>
</details>

# Collect payment from your website

<img src="https://files.readme.io/33fee0f2e261439d0356330a7bf8d2b8fbf93f4eeaf75b2ff7719f853ebbc4be-81ac69e-Web_Checkout_Decision_Tree_2_2.png" alt="" style={{ display: "block", margin: "0 auto" }} width="550px" />

# Collect Payment from Mobile

## Android

<img src="https://files.readme.io/2f1180f-Android_Decision_Tree.png" alt="" style={{ display: "block", margin: "0 auto" }} width="550px" />

## iOS

<img src="https://files.readme.io/f24a567-iOS_Decision_Tree.png" alt="" style={{ display: "block", margin: "0 auto" }} width="550px" />

# Collect payment using Links

You can send payment links using after any one of the following integration:

* **PayU Hosted Checkout**: Send payment links to your customers using PayU Dashboard or using Payment Link APIs. For more information, refer to [Dashboard for Payment Links](doc:payment-links-dashboard) or [Integration APIs for Payment Links](doc:integration-api-for-payment-links).
* **Merchant Hosted Checkout**: Send payment links to your customers using Payment Link APIs. For more information, refer to [Integration APIs for Payment Links](doc:integration-api-for-payment-links).

# Collect payment through Omnichannel

You can collect payments using Omnichannel after any one of the following integration:

* **PayU Hosted Checkout**: Share QR to your customers using Omnichannel Integration APIs. For more information, refer to [Integrated Dynamic Storefront](doc:integrated-dynamic-storefront)
* **Merchant Hosted Checkout**: Share QR to your customers using Omnichannel Integration APIs. For more information, refer to [QR Generation API](doc:qr-generation-api).

# Collect payment on eCommerce Platforms

You can configure PayU plugins for the following eCommerce platforms within few minutes and start collecting payments.

|                                                                      |                              |                                |
| :------------------------------------------------------------------- | :--------------------------- | :----------------------------- |
| [Shopify](doc:shopify)                                               | [Wix](doc:wix)               | [WooCommerce](doc:woocommerce) |
| [Interakt for WhatsApp Business](doc:interakt-for-whatsapp-business) | [Magento](doc:magento)       | [OpenCart](doc:opencart)       |
| [Shopmatic](doc:shopmatic)                                           | [PrestaShop](doc:prestashop) | [BigCommerce](doc:bigcommerce) |
| [Zoho](doc:zoho-integration)                                         |                              |                                |

# Become a partner

Become a partner to onboard merchants and earn incentives for payments collected by merchants onboarded by you. You can onboard merchants through any of the following methods:

* [Using Partner Portal or Dashboard](doc:referral-onboarding)
* [Using Co-Branded (OAuth) Onboarding](doc:refer-merchants-using-co-branded-oauth-onboarding)
* [Using Integration APIs](doc:refer-merchants-using-api)
* [Using Referral Links](doc:refer-merchants-using-referral-links)

For more information, refer to [Partner Integration](doc:payu-partner-program-overview).

# Make payments

PayU offers Payouts as a product for businesses to make instant payments to diverse customers. It is a reliable and secure payment option for all types of businesses that eases substantial monetary transactions. For more information, refer to [Payouts Integration](doc:introduction-to-payouts).