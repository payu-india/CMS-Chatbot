---
title: FAQS - Shopify
deprecated: false
hidden: true
metadata:
  robots: index
---
### Cross-Border payments integration

#### Will PayU’s Shopify plug-in and APIs support global merchants who want to process payments from Indian customers?

Yes. The plug-in and additional APIs support transaction processing for global merchants selling to customers in India. Merchants must provide invoice details as part of the integration. Settlement and reconciliation remain available through the PayU dashboard, reports, or APIs.

#### How do multi-currency payments work? Do merchants need to send amounts in INR after converting from another currency?

Send transaction amounts in INR. Shopify’s Markets feature lets you show product prices in local currencies, but PayU expects the final transaction request in INR. Use Shopify Markets to manage regional pricing and present local-currency prices to customers; the merchant should ensure the payment request that reaches PayU is in INR. For more information, refer to [Shopify Markets Documentation](https://shopify.dev/docs/apps/build/markets).

#### Will refunds and discounts work correctly for the PACB scenario through this plug-in?

Yes. Full and partial refunds process natively through the current plug-in. Shopify discount codes work natively. Merchant-funded discounts on PayU can be supported but are not yet live with any merchant. Bank-funded or payment-method subvention offers are not supported because PayU does not have cross-border bank subvention arrangements for PACB.

#### Will Shopify show payment gateway details such as currency, MDR, settlement status, and UTR on its dashboard?

No. Shopify does not display payment gateway settlement details. Merchants should get settlement status, currency, FX rate, UTR, and related fields from the PayU Dashboard, reports, or APIs. 

For more information, check these apps on on the Shopify App Store:

* [Localized Payments](https://apps.shopify.com/localized-payments)
* [HidePay](https://apps.shopify.com/hidepay)

#### Do merchants need to build routing logic to use PayU only for Indian customers? Is there an easier option?

Merchants can use third-party Shopify apps that limit payment app visibility by customer geo. These apps let you show PayU only to customers in India, avoiding custom routing code.

#### Can merchants get PayU integration support for Shopify setups and Cross-Border questions?

Yes. The International Integration team provides integration support. Contact your PayU key account manager for onboarding help or to schedule knowledge-transfer sessions.

#### Can global merchants complete onboarding using OAuth and self-sign-up?

No. Global merchants must complete KAM-assisted onboarding because the current sign-up flow requires an Indian phone number. After onboarding, merchants can link their Shopify store via OAuth or use an offline linking method supported by PayU.

#### If the PACB plugin is not listed on the Shopify marketplace, where will the merchants get it?

PayU will provide the plug-in and APIs directly to merchants who cannot find it on the Shopify marketplace. Contact your PayU key account manager to request the plug-in and receive implementation support.
