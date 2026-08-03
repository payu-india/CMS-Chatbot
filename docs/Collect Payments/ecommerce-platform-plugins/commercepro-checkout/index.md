---
title: CommercePro Checkout
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
PayU’s CommercePro Checkout provides a comprehensive checkout solution for merchants. It helps minimize RTO by limiting COD as a payment option based on a customer’s likelihood create a RTO on a particular transaction. It also allows customers to securely save their payment details and addresses and use it across PayU network merchants.

## Supported platforms

PayU supports CommercePro on the following platforms:

* **WooCommerce**: Refer to [CommercePro Checkout for WooCommerce](doc:commercepro-platform-for-woocommerce) for installation and configuration.
* **Magento**: Refer to [CommercePro Checkout for Magento](doc:commercepro-platform-for-magento) for installation and configuration.

## Benefits

* **No form filling** - Enable 2-step login with phone number and OTP, PayU will save customers information and pre-fill in the subsequent transactions.
* **Pre-fill addresses** - Pre-fill addresses for first time users from a database of 15.5 M+, making the journey alike for repeat customers.
* **Offer COD via PayU PG** - Offer COD as payment options for customers unwilling to use/with no access to digital payment methods.
* **Recommendation Engine** - Personalize the checkout experience by recommending payment options and reduce drop-offs.
* **Built-in RTO Intelligence** supporting COD blacklisting based on the following parameters:
  * Based on PIN codes
  * Based on addresses
  * Based on mobile numbers.
  * Setting up a maximum amount limit for COD orders.
* **Refunds** are supported directly from WooCommerce and Magento dashboard.
* **In-built support for PayU offers engine** & reconciliation with WooCommerce & Magento dashboards.

## Customer journey

1. After the products are added to the cart on the store, **PayU Checkout Express** option will be available to the customer during check-out.

<Image align="center" border={true} src="https://files.readme.io/90da7d7-image.png" className="border" />

2. After the checkout button is clicked, PayU in-context checkout flow will open with pre-filled emails (if logged in on the store). Customers will be asked to provide a phone number with OTP verification.

<Image align="center" border={true} src="https://files.readme.io/a9c9a01-image.png" className="border" />

3. After logging in through OTP, pre-filled address details will be shown to buyers automatically:
   1. Buyers can change the address or add a new address. Any updates or new addresses added will be saved in PayU’s address vault to be used later.
   2. Buyers will also be shown if any shipping fee is being charged on the order. After confirming all the details, click **Proceed to Pay**.

<Image align="center" border={true} src="https://files.readme.io/16602d4-image.png" className="border" />

4. Buyers will be redirected to the _PayU Checkout_ page for completing the payment:
   1. Applicable offers on the merchant's MID will be shown automatically.
   2. Payment modes ordering will be dynamic based on recommendation engine for higher conversions.

<Image align="center" border={true} src="https://files.readme.io/2a96c60-image.png" className="border" />
