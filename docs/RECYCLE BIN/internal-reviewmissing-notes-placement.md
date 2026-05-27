---
title: '[Internal Review]Missing Notes Placement'
deprecated: false
hidden: true
metadata:
  robots: index
---
## Summary Table

| Title                                                        | Target Page(s)                                                                         | Severity  |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------- | --------- |
| UPI App List is Platform-Controlled                          | webview-for-mobile-apps, android-checkoutpro-sdk, ios-checkoutpro-sdk                  | 🔴 High   |
| Hash Formula with Partial UDFs — Pipe Count Rule             | hashing-request-and-response, generate-hash-payu-hosted, generate-hash-merchant-hosted | 🔴 High   |
| Webhook `amount` Field — Gross or Net?                       | webhook-events-and-sample-payloads, webhooks                                           | 🔴 High   |
| Verify Payment API — `command` Parameter Value               | Verify Payment / postservice API page                                                  | 🟠 Medium |
| "Too Many Requests" Error — Causes and Fix                   | error-handling, general-faqs                                                           | 🟠 Medium |
| Flutter SDK — Current Version and Install Source             | flutter-checkoutpro-sdk                                                                | 🟠 Medium |
| React Native — Dynamic Hash Common Mistakes                  | reactnative-checkoutpro-android-integration, iOS React Native page                     | 🔴 High   |
| Pluxee Card — Not Supported in Mobile SDK                    | integrate-with-merchant-hosted-checkout-for-pluxee-card                                | 🟠 Medium |
| Split Settlement via Payment Links — Compatibility Statement | absolute-split-during-transaction-integration, payment-links-dashboard                 | 🟠 Medium |
| Bulk Payment Links — `IsPartialPaymentAllowed` Column        | bulk-upload-to-create-multiple-payments-links                                          | 🟡 Low    |
| UAT Offers / No Cost EMI Dashboard — 503 Error               | Offers integration page, general-faqs                                                  | 🟡 Low    |

<br />

## UPI App List is Platform-Controlled

**Target page:** (1) "Integrate WebView for Mobile Apps" — [https://docs.payu.in/docs/webview-for-mobile-apps](https://docs.payu.in/docs/webview-for-mobile-apps); <br />**Insert under heading:** "UPI Integration" or "Known Limitations" (add new subsection if absent on any of these pages)<br />**Position:** As the first note block beneath the heading, before any existing paragraphs or steps

### Note content:

> 📘 **UPI App List is platform-controlled:**&#x20;
>
> The list of UPI apps displayed on the payment screen (GPay, PhonePe, Paytm, etc.) is managed globally by PayU and cannot be customised per merchant. If you want to remove specific apps from this list, contact your PayU Key Account Manager (KAM) or<Anchor target="_blank" href="https://help.payu.in">&#x20;PayU Support</Anchor>.

### Why this note is needed:

Multiple tickets (reopened 3–8 times) from merchants confused by unexpected UPI apps appearing or known apps missing, with no error messages to indicate why. Without this note, merchants open tickets assuming they misconfigured something, causing avoidable back-and-forth with support.

***

## Note 2: Hash Formula with Partial UDFs — Pipe Count Rule

<br />**Target page:**&#x20;

(1) "Generate Hash" — [https://docs.payu.in/docs/hashing-request-and-response](https://docs.payu.in/docs/hashing-request-and-response);&#x20;

(2) [https://docs.payu.in/docs/generate-hash-payu-hosted](https://docs.payu.in/docs/generate-hash-payu-hosted);&#x20;

(3) [https://docs.payu.in/docs/generate-hash-merchant-hosted](https://docs.payu.in/docs/generate-hash-merchant-hosted)<br />

**Insert under heading:** The section showing the hash formula (exact heading title varies by page — match the section that displays the `sha512(key|txnid|...)` formula string)<br />**Position:** Immediately after the hash formula line, before any code samples or parameter tables that follow

### Note content:

> 📘 **Partial UDF usage :**&#x20;
>
> The hash string must always contain exactly 5 UDF positions between `email` and `SALT`, regardless of how many UDFs you actually use. Use an empty string `""` for each unused UDF — never omit the pipe separators.**Example — using only udf1 and udf2:**
>
> **Use illustration below:**
>
> ```
> sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2||||||||SALT)
>                                                              ↑↑↑
>                                              udf3, udf4, udf5 = empty strings
> ```
>
> The 6 pipes after udf5 (`||||||`) represent empty positions for additional fields — do not remove them.

### Why this note is needed:

A direct merchant question reopened 3 times — merchants using only 1–2 UDF fields did not know the required pipe count was fixed at 5, causing hash mismatch errors that were hard to debug without this explicit rule.

***

## Webhook `amount` Field — Gross or Net?

**Target page:**&#x20;

(1) "Webhook Events and Sample Payloads" — [https://docs.payu.in/docs/webhook-events-and-sample-payloads](https://docs.payu.in/docs/webhook-events-and-sample-payloads); <br />**Insert under heading:** The section describing webhook payload fields / response parameters (e.g., "Payload Parameters", "Response Fields", or "Webhook Body")<br />**Position:** Immediately after the table row or paragraph that describes the `amount` field; if `amount` and `net_amount_debit` appear in the same table, insert after the table as a callout block

### Note content:

> 📘 **Webhook amount field:**&#x20;
>
> The `amount` field in the webhook payload reflects the **original transaction amount** passed in the payment request — it does not include convenience fees or MDR charges added by the merchant. If you have configured convenience fees, the `net_amount_debit` field (where available) reflects the actual amount debited from the customer's account. Always use `amount` for reconciliation against your order value and `net_amount_debit` for the customer-side amount.

### Why this note is needed:

Reopened 3 times — merchants integrating convenience fees were unsure which amount field to use for reconciliation, leading to incorrect settlement reporting and downstream accounting errors.

***

## General APIs— `command` Parameter Value

**Target page:** Al the General APIs<br />**Insert under heading:** The parameters table or request example section<br />**Position:** At the very top of the page, as a pinned quick-reference callout block, before the introduction paragraph or immediately after the page title

### Note content:

> 📘 **Quick reference — required&#x20;**`command`**&#x20;values:**
>
> | Use case                 | `command` value             |
> | ------------------------ | --------------------------- |
> | Verify a payment         | `verify_payment`            |
> | Check transaction info   | `check_action_status`       |
> | Get transaction by txnid | `get_transaction_info`      |
> | Refund a transaction     | `cancel_refund_transaction` |
>
> **API endpoint:** `POST https://info.payu.in/merchant/postservice.php?form=2`<br />**Hash formula:** `sha512(key|command|var1|SALT)`

### Why this note is needed:

Reopened 4 times — merchants did not know the exact string value required for the `command` parameter and were guessing variations, resulting in API errors that were difficult to diagnose without this explicit enumeration.

***

## &#x20;"Too Many Requests" Error — Causes and Fix

**Target page:**&#x20;

(1) "Error Handling" — [https://docs.payu.in/docs/error-handling](https://docs.payu.in/docs/error-handling);&#x20;

2\) "General FAQs" — [https://docs.payu.in/docs/general-faqs](https://docs.payu.in/docs/general-faqs)<br />**Insert under heading:** Error messages / Common errors section on the Error Handling page; FAQ entry under a "Errors & Troubleshooting" group on the General FAQs page<br />**Position:** After any existing common-error entries, or as a new FAQ item at the end of the Troubleshooting / Errors section

### Note content:

> 📘 **"Too many Requests" error:**&#x20;
>
> If you see _"Sorry, we are unable to process your payment due to Too many Requests. Please try after 60 seconds"_, this is caused by **Rate limit exceeded** — Too many payment requests sent in a short window from the same merchant key. Wait 60 seconds and retry.

### Why this note is needed:

Multiple merchant tickets arrived with this exact error message verbatim, yet no documentation existed for it. Without this note, merchants had no self-service path to resolve a very common integration mistake.

***

## Flutter SDK — Current Version and Install Source

<br />**Target page:** "Flutter Checkout Pro SDK" — [https://docs.payu.in/docs/flutter-checkoutpro-sdk](https://docs.payu.in/docs/flutter-checkoutpro-sdk) (and any Flutter SDK intro/overview page)<br />**Insert under heading:** The very first section of the page (before "Overview" or as a pinned note at the top)<br />**Position:** As the first content block on the page, before the overview or introduction paragraph

### Note content:

> 📘 **Current SDK version and install source:**
>
> | SDK                        | Latest Version                                                     | Install via                       |
> | -------------------------- | ------------------------------------------------------------------ | --------------------------------- |
> | Flutter CheckoutPro SDK    | Check [Version History](https://docs.payu.in/docs/version-history) | `pub.dev` — add to `pubspec.yaml` |
> | Flutter Custom Browser SDK | Check release notes                                                | `pub.dev`                         |
> | Flutter UPI SDK            | Check release notes                                                | `pub.dev`                         |
>
> Always use the latest version. To install: add the package to your `pubspec.yaml` and run `flutter pub get`. Do not download SDK files manually — use the pub.dev package registry.

### Why this note is needed:

Reopened 7 times — the highest reopen count for any Flutter ticket in the dataset. Merchants kept asking support for "the Flutter SDK file" because the install source (`pub.dev`) was not stated prominently, and many assumed there was a downloadable `.aar` or `.zip` file.

***

## React Native — Dynamic Hash Common Mistakes

**Severity:** 🔴 High<br />**Target page:**&#x20;

(1) "React Native CheckoutPro Android Integration" — [https://docs.payu.in/docs/reactnative-checkoutpro-android-integration](https://docs.payu.in/docs/reactnative-checkoutpro-android-integration);&#x20;

(2) The equivalent iOS React Native integration page<br />**Insert under heading:** "Generate Dynamic Hash" section (exact heading text on each page)<br />**Position:** Immediately after the existing code sample in that section, before any "Next steps" or following subsections

### Note content:

> 📘 **Notes during dynamic hash generation:**
>
> The `generateHash` callback receives a JavaScript object (hashMap). You must:
>
> 1. Extract `PayUCheckoutProConstants.CP_HASH_STRING` from the hashMap — this is the pre-built string excluding your salt.
> 2. Send this string to **your server** to append the salt and compute SHA-512.
> 3. Return the computed hash via the callback using `PayUCheckoutProConstants.CP_HASH_NAME` as the key.
>
> **If you return&#x20;**`null`**,&#x20;**`undefined`**, or an incorrect key**, the SDK silently fails with `[PayU] Dynamic hash generation failure` in the console and no payment screen appears.
>
> ```javascript
> // Correct pattern:
> generateHash: (hashMap) => {
>   const hashString = hashMap[PayUCheckoutProConstants.CP_HASH_STRING];
>   const hashName = hashMap[PayUCheckoutProConstants.CP_HASH_NAME];
>   // Send hashString to your server → get computedHash back. Your backend will append the salt at the end of hashstring and convert using SHA512 and then pass it back to front-end.
>   const result = {};
>   result[hashName] = computedHash; // key must be hashName, not a custom string
>   return result;
> }
> ```

### Why this note is needed:

Reopened 6 times — the exact error `[PayU] Dynamic hash generation failure` was confirmed in support logs. The SDK gives no user-visible feedback when hash generation fails silently, making this a difficult bug to diagnose without explicit documentation of the correct callback contract.

***

## Split Settlement via Payment Links — Compatibility Statement

<br />**Target page:** (1) Split Settlement pages — [https://docs.payu.in/docs/absolute-split-during-transaction-integration](https://docs.payu.in/docs/absolute-split-during-transaction-integration); (2) "Payment Links" — [https://docs.payu.in/docs/payment-links-dashboard](https://docs.payu.in/docs/payment-links-dashboard)<br />**Insert under heading:** "Supported Integration Types" or "Before You Begin" on each page (add as a new subsection if absent)<br />**Position:** As the first note block under that heading on both pages, so the cross-feature limitation is visible before a merchant begins the integration steps

### Note content:

> 📘 **Split Settlement and Payment Links:**&#x20;
>
> Split settlement is supported for **direct API integrations** (PayU Hosted Checkout, Merchant Hosted Checkout, and S2S). Split settlement via **Payment Links** has limited support — the split parameters cannot be passed through the Payment Links creation API in the same way as direct payment APIs. If you require split settlement on payment link transactions, contact your KAM to understand the supported configuration for your account.

### Why this note is needed:

Direct merchant ticket asking about this combination — no cross-reference existed between the Split Settlement and Payment Links documentation pages, leaving merchants to discover the limitation only after attempting the integration.

***

## Bulk Payment Links — `IsPartialPaymentAllowed` Column

<br />**Target page:** "Create Payment Links in Bulk" — [https://docs.payu.in/docs/bulk-upload-to-create-multiple-payments-links](https://docs.payu.in/docs/bulk-upload-to-create-multiple-payments-links)<br />**Insert under heading:** The section describing the CSV template columns (e.g., "CSV Template Fields", "Upload Format", or "Column Reference")<br />**Position:** After the last documented column in the table, as an additional row followed by the callout block below

### Note content:

> 📘 **Partial payment option in bulk links:**&#x20;
>
> To enable partial payment on bulk-created payment links, include the column `IsPartialPaymentAllowed` in your CSV upload with value `1` (enabled) or `0` (disabled). If this column is absent, partial payment defaults to disabled.**Known behaviour:** If the partial payment option does not appear on the generated payment link despite setting `IsPartialPaymentAllowed=1`, verify that:
>
> - The partial payment feature is enabled on your merchant account (contact your KAM)
> - The payment link amount is above the minimum partial payment threshold
> - You are using the latest bulk upload template from the Dashboard

### Why this note is needed:

A merchant confirmed the column stopped working on newly created bulk links. The `IsPartialPaymentAllowed` column is entirely undocumented in the current template guide, leaving merchants with no way to discover or troubleshoot this feature without raising a support ticket.

***

## UAT Offers / No Cost EMI Dashboard — 503 Error

<br />**Target page:**&#x20;

(1) Any Offers integration page (e.g., [https://docs.payu.in/docs/integrate-payu-with-interakt](https://docs.payu.in/docs/integrate-payu-with-interakt) or the main Offers documentation page);&#x20;

(2) "General FAQs" — [https://docs.payu.in/docs/general-faqs](https://docs.payu.in/docs/general-faqs)<br />**Insert under heading:** "Testing" or "Troubleshooting" section on the Offers page; a new FAQ item in the "Errors & Troubleshooting" group on the General FAQs page<br />**Position:** At the end of the Testing/Troubleshooting section, after any existing test steps; as the last item in the relevant FAQ group

### Note content:

> 📘 **UAT Offers / No Cost EMI dashboard returning 503:**&#x20;
>
> 1. The Offers section of the PayU UAT/staging Dashboard may intermittently return a 503 error. This is a known environment issue and does not indicate a problem with your integration. If the Offers section is unavailable in UAT:
> 2. Wait 15–30 minutes and refresh.
> 3. If the issue persists beyond 1 hour, raise a support ticket at [integration@payu.in](mailto:integration@payu.in) with your MID and a screenshot.
> 4. Offers created before the downtime remain valid — they are not deleted during a 503 outage.
>    Note: No Cost EMI and Offers features must be activated on your account before they appear in the Dashboard (contact your KAM).

### Why this note is needed:

Reopened 3 times — merchants assumed their integration was broken when the UAT Offers Dashboard returned 503 errors, and spent hours debugging their code when the issue was purely an environment outage. No documentation existed acknowledging this known behaviour.

***

##

<br />
