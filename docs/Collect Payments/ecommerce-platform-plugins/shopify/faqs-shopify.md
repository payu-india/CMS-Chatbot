---
title: FAQS - Shopify
deprecated: false
hidden: true
metadata:
  robots: index
---
<br />

## Cross-Border Payments integration

#### With the PayU India plug-in and additional APIs, will all requirements of global merchants be catered to for processing their transactions from Indian customers via PayU?

From a transaction processing standpoint, this solution will work with additional integration effort from the merchant to provide invoice details. Settlement flow will remain via PayU dashboard/reports/APIs - as in the case for currently live domestic merchants.

#### Have we thought of how the Multi Currency Payments will be handled, and whether we need the amount to be sent in INR after conversion by the merchant? In such cases, how can the merchant do this conversion?

The transaction request received is expected to be in INR. Shopify has a product construct called "Markets" - where the merchants can define different currency & pricing for geos. Based on the user's location, the catalog priced in local currency is shown. Once the INR catalog is defined, we expect the entire transaction to be processed in INR. For more information, refer to [Shopify Markets Documentation](https://shopify.dev/docs/apps/build/markets).

#### Will refund, discounts, etc., work properly for our PACB use case through this plug-in?

Refunds (partial + full) will work natively via the current plugin.

On discounts:

* Native Shopify discount codes will work.
* Merchant subvention discounts on PayU can also be supported, if required; however, we are not live on this currently with any merchant so far.
* Bank subvention offers, payment method-based offers will not be supported, as we do not have a cross-border arrangement for bank subvention. This is a PACB limitation, not specific to Shopify.

#### Will the Shopify dashboard correctly show the reports with currency, MDR, settlement status/UTR, etc.?

As described earlier, Shopify currently does not have any construct to show PG settlement details on their dashboard. They will have to be consumed from us directly through the dashboard, reports, or APIs - which will include full details: settlement status, currency, FX rate applied, UTR, etc.

#### Will the merchant have to build routing logic to use PayU services only for Indian customers? Any simple way that can be suggested to merchants?

There are third-party tools which allow merchants to control visibility of payment apps based on the user's geo - which can be leveraged here.

For more information, check these apps on on the Shopify App Store:

* [Localized Payments](https://apps.shopify.com/localized-payments)
* [HidePay](https://apps.shopify.com/hidepay)

#### Is there a PayU Integration Support which can guide these merchants for integration when required?

Yes, the International Integration team will be able to support. We can have a refresher KT session this week to ensure there are no disconnects.

#### I presume these global merchants cannot follow the OAuth or redirection to PayU for onboarding & will have to be done as Assisted onboarding prior to starting transactions?

Yes, that understanding is correct. We will need to onboard them via KAM assisted flow - as our current sign-up process requires an Indian phone number. Once onboarding is complete, the merchant can complete the Shopify store linking via OAuth - or we can support that in an offline way.

#### Since the PACB plugin will not be available on Shopify marketplace, we will have to separately provide the plug-ins & APIs to such merchants. Also, it cannot be self-discovery by merchants?

Yes, PayU can help you in this regard. Contact your PayU key account manager (KAM).
