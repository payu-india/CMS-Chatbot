---
title: FAQs to be Added - July 2026
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: Web Checkout and General Web FAQs
excerpt: Answers to common questions about PayU Web Checkout integrations, payment methods, refunds, security, and production readiness.
deprecated: false
hidden: false
metadata:
  title: Web Checkout and General Web FAQs
  description: Troubleshoot and configure PayU Web Checkout integrations, payment methods, refunds, webhooks, security, and production setup.
  keywords:
    - PayU Web Checkout FAQs
    - PayU payment integration troubleshooting
    - PayU General Web FAQs
  robots: index
next:
  description: ''
---
This page answers common questions about PayU Web Checkout integrations and general web payment operations.
## Web Checkout integration
<Accordion title="Why is the UPI payment option greyed out or showing an orange dot with no explanation?" icon="fa-info-circle">
  The UPI option can be unavailable when PayU cannot detect a compatible UPI app on the customer's device. Ask the customer to install or enable a supported UPI app, such as Google Pay, PhonePe, or Paytm, and then retry the payment.
  If you control the checkout interface, display a message explaining that a compatible UPI app is required.
  For more information, refer to [UPI Intent Integration](doc:upi-intent-integration).
</Accordion>
<Accordion title="What is NPCI OC190 compliance, and is it handled by PayU Hosted Checkout?" icon="fa-info-circle">
  NPCI OC190 requirements include UPI Smart Intent, appropriate ordering of UPI apps, and support for applicable QR flows.
  PayU handles these requirements on PayU Hosted Checkout. Merchants using a Merchant Hosted or other seamless integration must implement the applicable Smart Intent requirements in their own checkout experience.
  For more information, refer to [PayU Hosted Checkout](doc:prebuilt-checkout-payu-hosted) and [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow).
</Accordion>
<Accordion title="How do I migrate my integration from UPI Collect flow to UPI Intent flow?" icon="fa-info-circle">
  To migrate:
  1. Update your PayU integration or SDK to a version that supports UPI Intent.
  2. Confirm that UPI Intent is enabled for your merchant account.
  3. Configure the required UPI Intent request parameters for your web or mobile integration.
  4. Test the flow on physical devices with supported UPI apps; simulators cannot complete the app-switch flow reliably.
  5. Verify the final transaction status before fulfilling the order.
  For enablement or account configuration, contact your PayU Key Account Manager (KAM).
  For more information, refer to [UPI Intent Integration](doc:upi-intent-integration).
</Accordion>
<Accordion title="How do I configure a webhook URL for payment notifications?" icon="fa-info-circle">
  To configure a webhook:
  1. Sign in to PayU Dashboard and go to **Settings > Webhooks**.
  2. Create a webhook and enter a publicly accessible HTTPS URL.
  3. Select the payment events that your endpoint must receive.
  4. Test the webhook and confirm that your endpoint returns a successful HTTP response.
  5. Validate the hash in every payload and handle duplicate events idempotently.
  A webhook supplements the browser redirect to `surl` or `furl`; it does not replace those URLs.
  For more information, refer to [Create a New Webhook](doc:create-a-new-webhook) and [Webhooks](doc:webhooks).
</Accordion>
<Accordion title="What should I check when a hash mismatch error occurs on the callback or response?" icon="fa-info-circle">
  Check the following:
  * Use the Salt and merchant key for the same environment as the endpoint.
  * Follow the documented reverse-hash formula and parameter order exactly.
  * Preserve empty fields and additional charges in the formula where required.
  * Check UTF-8 and URL-decoding behaviour for special characters.
  * Remove unintended spaces or line breaks from parameter values.
  * Log the pre-hash string securely and compare it with the expected sequence. Never log the Salt.
  Reject a response when hash validation fails.
  For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted) and [Using PayU Hash Verification Tool](doc:using-payu-hash-verification-tool).
</Accordion>
<Accordion title="How do I handle a transaction stuck in pending status?" icon="fa-info-circle">
  Do not fulfil the order while the payment status is pending. Use the Verify Payment API to retrieve the current status and use webhooks to receive subsequent updates. If you poll, use a bounded retry interval and stop after your business-defined timeout.
  Reconcile unresolved transactions before fulfilment. If the status remains pending beyond the normal processing window, raise a PayU support ticket with the transaction ID.
  For more information, refer to [Verify Payment API](ref:verify_payment_api) and [Webhooks](doc:webhooks).
</Accordion>
<Accordion title="What checkout page customization options are available?" icon="fa-info-circle">
  The available customization depends on the integration:
  * **PayU Hosted Checkout:** Configure supported branding options such as the logo and theme while PayU hosts the payment page.
  * **Merchant Hosted Checkout:** Control the checkout UI and payment-mode presentation on your website, subject to security and PCI-DSS requirements.
  * **CheckoutPro mobile SDKs:** Configure supported themes, colours, fonts, and payment-mode ordering through the SDK.
  For more information, refer to [PayU Payment Page Customization](doc:payu-payment-page-customization) and [Merchant Hosted Checkout](doc:custom-checkout-merchant-hosted).
</Accordion>
<Accordion title="How do I implement offer or discount codes in a payment request?" icon="fa-info-circle">
  Create and configure the offer in PayU Dashboard, then pass the offer identifier required by your integration in the payment request. Validate the offer's dates, eligibility rules, payment modes, and discount configuration before going live. Use the payment response to reconcile the applied discount.
  Contact your PayU Key Account Manager (KAM) for enablement or configuration of account-specific and bank-funded offers.
  For more information, refer to [Offers Integration](doc:offers-integration).
</Accordion>
<Accordion title="How can I control payment mode ordering or sequencing on checkout?" icon="fa-info-circle">
  The available control depends on the integration:
  * **PayU Hosted Checkout:** Use the supported parameters to enforce or remove payment categories. Contact your PayU Key Account Manager (KAM) for account-level sequencing options.
  * **Merchant Hosted Checkout:** Retrieve the available payment options and render them in the required order.
  * **Mobile SDKs:** Use the SDK's payment-mode ordering configuration.
  Ordering must comply with applicable NPCI requirements for UPI.
  For more information, refer to [Enforce Pay Method or Remove Category](doc:enforce-pay-method-or-remove-category).
</Accordion>
## Payment methods and merchant configuration
<Accordion title="Is there an API to fetch an EMI schedule for a payment amount and offer ID?" icon="fa-info-circle">
  Use the applicable EMI checkout-details API to retrieve eligible tenures and the amount breakdown before initiating the payment. The request typically requires the merchant key, transaction amount, relevant bank or offer details, and a hash. Use the returned tenure, interest, and instalment details to display the schedule.
  For more information, refer to [Get EMI Amount according to Interest API](ref:get_emi_according_to_interest_api).
</Accordion>
<Accordion title="On Shopify, why are only card payment options showing while UPI, Net Banking, or wallets are missing?" icon="fa-info-circle">
  Check the following:
  1. Confirm that UPI, Net Banking, and wallets are enabled for your merchant account.
  2. Review the payment methods selected in **Shopify Admin > Settings > Payments > PayU**.
  3. Check whether the integration request restricts the checkout to cards.
  4. Save the configuration and test again in a new browser session.
  New merchant accounts can initially have a limited set of payment modes. Contact your PayU Key Account Manager (KAM) if a required mode is not enabled.
  For more information, refer to [Integrate with Shopify](doc:integrate-with-shopify).
</Accordion>
<Accordion title="What test cards are available for successful, failed, pending, EMI, and 3DS scenarios?" icon="fa-info-circle">
  PayU maintains test credentials and scenario-specific instructions for cards, UPI IDs, and wallets. Use only the values documented for the PayU test environment; do not use test credentials in production.
  For more information, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets).
</Accordion>
<Accordion title="What is the difference between merchant-funded and bank-funded EMI?" icon="fa-info-circle">
  * **Bank-funded EMI:** The issuing bank defines and funds the applicable interest or promotional benefit. Availability depends on supported banks, cards, and tenures.
  * **Merchant-funded EMI:** The merchant subsidizes some or all of the customer's interest or discount. The subsidy and applicable fees affect the merchant's net settlement.
  Contact your PayU Key Account Manager (KAM) to confirm eligibility and enable merchant-funded EMI.
  For more information, refer to [EMI](doc:emi-api-integration).
</Accordion>
<Accordion title="How do I activate American Express card payments for my merchant account?" icon="fa-info-circle">
  American Express enablement is account-specific and can require additional underwriting, documentation, commercial terms, and acquiring-bank approval. Contact your PayU Key Account Manager (KAM) to confirm eligibility, required documents, and the expected activation timeline.
</Accordion>
<Accordion title="What is a dynamic descriptor for card payments, and how do I configure it?" icon="fa-info-circle">
  A dynamic descriptor controls the merchant text that can appear on the customer's card statement. A recognisable descriptor can reduce customer confusion and chargebacks.
