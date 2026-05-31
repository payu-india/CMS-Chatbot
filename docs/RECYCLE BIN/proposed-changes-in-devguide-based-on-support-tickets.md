---
title: Proposed Changes in Devguide Based on Support Tickets
deprecated: false
hidden: true
metadata:
  robots: index
---
## Summary Table

| Title                                                              | Fix Type                                  | Pages Affected               |
| ------------------------------------------------------------------ | ----------------------------------------- | ---------------------------- |
| Cordova SDK — `surl` validation stricter than web                  | New callout note                          | 2                            |
| React Native SDK — `generateHash` error message is misleading      | New callout + correction                  | 2                            |
| UPI Intent/Collect overlap by device type                          | New section                               | 3                            |
| `GetUserCards` API — saved cards not returned for same credentials | New troubleshooting section               | 2                            |
| CheckoutPro — disabled payment modes re-appear after timeout       | New callout note                          | 3                            |
| `merchant_key_not_register_for_phonepe` error undocumented         | New entry in troubleshooting table        | 2                            |
| `intentURIData` returns a single URL, not per-app URLs             | Clarification to existing content         | 2                            |
| SI `billingCycle: ADHOC` not in parameter table                    | New row in parameter table                | 2 (3rd page already correct) |
| Webhook UI — delete and duplicate event creation                   | Correction to existing content + new note | 3                            |
| "Convenience Fee" vs "Internet Handling Charges (IHC)"             | New terminology note                      | 5                            |
| UPI QR test transactions failing with undocumented error           | New troubleshooting note                  | 2                            |

## Cordova SDK — `surl` validation stricter than web

**Severity:** 🟠 High<br />**Fix type:** New callout note

### Affected Page(s)

| Page Title                                   | URL                                                                                                                                      | Section/Heading               |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| Steps to Integrate (Cordova CheckoutPro SDK) | [https://docs.payu.in/docs/cordova-checkoutprosdk-integration-steps](https://docs.payu.in/docs/cordova-checkoutprosdk-integration-steps) | `Step 2: Set up Callback`     |
| Cordova CheckoutPro SDK (overview)           | [https://docs.payu.in/docs/cordova-sdk-introduction](https://docs.payu.in/docs/cordova-sdk-introduction)                                 | First section / Prerequisites |

### Where exactly to insert

**Page:** Steps to Integrate (Cordova CheckoutPro SDK)<br />**Heading:** `Step 2: Set up Callback`<br />**Position:** Before the `responseCallBack` code block

**Page:** Cordova CheckoutPro SDK (overview)<br />**Heading:** First section / Prerequisites<br />**Position:** At the top of the page, before "Step 1: SDK Integration"

### What to add or change

```
> ⚠️ **SURL/FURL requirements are stricter in the Cordova SDK than in web integration.**
> The SDK validates the SURL and FURL before initiating a transaction. A valid SURL must:
> - Be a publicly accessible **HTTPS** URL
> - Not be `localhost` or a private IP address
> - Not use a self-signed SSL certificate
> - Be reachable from the internet (not behind a corporate firewall)
>
> If you see a `"surl not correct"` error in the Cordova SDK but the same SURL works in your web integration, the URL likely fails one of the above checks.
> Use a tunnelling tool such as `ngrok` for local development testing.
```

***

## React Native SDK — `generateHash` error message is misleading

**Severity:** 🟠 High<br />**Fix type:** New callout + correction

### Affected Page(s)

| Page Title                           | URL                                                                                                                                            | Section/Heading                                                |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Android Integration (React Native)   | [https://docs.payu.in/docs/reactnative-checkoutpro-android-integration](https://docs.payu.in/docs/reactnative-checkoutpro-android-integration) | `generateHash` section (under the React Native 0.82.0+ notice) |
| Generate Dynamic Hash (React Native) | [https://docs.payu.in/docs/generate-dynamic-hash-react](https://docs.payu.in/docs/generate-dynamic-hash-react)                                 | `Procedure`                                                    |

### Where exactly to insert

**Page:** Android Integration (React Native)<br />**Heading:** `generateHash`<br />**Position:** After the `generateHash` code block (after the `PayUBizSdk.hashGenerated(result)` example)

**Page:** Generate Dynamic Hash (React Native)<br />**Heading:** `Procedure`<br />**Position:** After the last paragraph of the Procedure section ("The server will give that hash back to your app...")

### What to add or change

````
> ⚠️ **Misleading error message:** If you see the following error in your console, it is **NOT** a PayU server error — it is a client-side callback implementation mistake:
> ```
> [PayU] Dynamic hash generation failed: {code: 'UNKNOWN', message: 'Internal server error occurred. Please contact support if the issue persists.'}
> ```
> **Common causes:**
> 1. The callback returns `null` or `undefined` instead of a hash object
> 2. The result object uses a custom string as the key instead of `hashName` / `e.hashName`
> 3. `PayUBizSdk.hashGenerated()` is called before the server responds (async timing issue)
>
> **Correct pattern (React Native ≥ 0.82.0):**
> The result key MUST be the value of `e.hashName`, not a hardcoded string.
````

***

## UPI Intent/Collect overlap by device type

**Severity:** 🟠 High<br />**Fix type:** New section

### Affected Page(s)

| Page Title                          | URL                                                                                                                            | Section/Heading                                                 |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| UPI Integration (Merchant Hosted)   | [https://docs.payu.in/docs/collect-payments-with-upi-seamless](https://docs.payu.in/docs/collect-payments-with-upi-seamless)   | After the `⚠️ Important UPI Integration Changes` callout        |
| UPI Intent with S2S Integration     | [https://docs.payu.in/docs/upi-intent-server-to-server](https://docs.payu.in/docs/upi-intent-server-to-server)                 | `Step 1: Fetch the List of UPI and Smart Intent Supported Apps` |
| UPI Collect Disablement Information | [https://docs.payu.in/docs/upi-collect-disablement-information](https://docs.payu.in/docs/upi-collect-disablement-information) | `Exemptions`                                                    |

### Where exactly to insert

**Page:** UPI Integration (Merchant Hosted)<br />**Heading:** After the `⚠️ Important UPI Integration Changes` callout at the top<br />**Position:** Add a new subsection immediately after the existing NPCI mandate callout

**Page:** UPI Intent with S2S Integration<br />**Heading:** `Step 1: Fetch the List of UPI and Smart Intent Supported Apps`<br />**Position:** After the first paragraph of Step 1

**Page:** UPI Collect Disablement Information<br />**Heading:** `Exemptions`<br />**Position:** After the exemptions table

### What to add or change

**On UPI Integration (Merchant Hosted):**

```
> 📌 **UPI Intent vs UPI Collect — Device-type behaviour:**
> | Device | UPI Intent enabled | UPI Collect enabled | What customer sees |
> |---|---|---|---|
> | Mobile (Android) | ✅ Yes | N/A | UPI app intent chooser |
> | Mobile (iOS) | N/A | ✅ Yes | UPI Collect (VPA entry) |
> | Desktop web | ✅ Yes | ✅ Yes | UPI Collect (Google Pay shows as Collect on desktop even if Intent is enabled) |
>
> **Known behaviour:** Disabling UPI Intent on your MID does **not** prevent UPI Collect from appearing on desktop browsers. Google Pay on desktop always initiates as UPI Collect regardless of Intent configuration.
>
> **"Something went wrong" error:** If a UPI app appears in the payment options but is not installed on the customer's device, the customer sees a "Something went wrong" message when selecting it. This is expected platform behaviour — not an integration error.
```

**On UPI Intent with S2S Integration:**

```
> 📌 **Note on desktop behaviour:** On desktop browsers, even if UPI Intent is configured, Google Pay and similar apps will initiate as **UPI Collect** (VPA-based). UPI Intent (app deep-link) only works on mobile devices. For desktop web, use the QR code approach: generate the `intentURIData` URL and render it as a QR code.
```

**On UPI Collect Disablement Information (after the exemptions table):**

```
> 📌 **Note:** Even with UPI Intent enabled, UPI Collect may still appear on desktop browsers for certain apps (such as Google Pay). This is expected platform behaviour and is not caused by your disablement configuration. Desktop Google Pay always initiates as UPI Collect regardless of Intent settings.
```

***

## `GetUserCards` API — saved cards not returned for same credentials

**Severity:** 🟠 High<br />**Fix type:** New troubleshooting section

### Affected Page(s)

| Page Title                              | URL                                                                                                                            | Section/Heading                               |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- |
| Get User Cards API - Model 3            | [https://docs.payu.in/reference/get\_user\_cards\_api\_model3](https://docs.payu.in/reference/get_user_cards_api_model3)       | After `Sample response` section (end of page) |
| Collect Payments using a Tokenized Card | [https://docs.payu.in/docs/collect-payments-using-a-saved-card](https://docs.payu.in/docs/collect-payments-using-a-saved-card) | `Get the tokenized card details`              |

### Where exactly to insert

**Page:** Get User Cards API - Model 3<br />**Heading:** `Sample response`<br />**Position:** After the Sample response section — add a new `## Troubleshooting` section at the end of the page

**Page:** Collect Payments using a Tokenized Card<br />**Heading:** `Get the tokenized card details`<br />**Position:** After the description of `get_user_details` API

### What to add or change

**On Get User Cards API - Model 3 (new section at end of page):**

```markdown
## Troubleshooting: No cards returned for valid credentials

If the API returns an empty `user_cards` object despite a card being successfully saved, check the following:

**1. User credential format mismatch**
The `var1` parameter must use the exact same format in both the save-card payment request (`user_credentials`) and the GetUserCards API call (`var1`). The format is `merchantKey:uniqueUserId` (e.g., `JPM7Fg:user123`). A mismatch in the `merchantKey` prefix or the `uniqueUserId` will return no cards.

**2. Environment mismatch**
Cards saved in the **test environment** cannot be retrieved in the **production environment** and vice versa. Use the correct endpoint:
- Test: `https://test.payu.in/merchant/postservice.php?form=2`
- Production: `https://info.payu.in/merchant/postservice.php?form=2`

**3. Propagation delay**
There may be a delay of a few minutes between card tokenization and retrieval. If you saved the card very recently, wait 2–3 minutes and retry.

**4. Tokenization not enabled**
The TRID/Store Card feature must be enabled on your merchant account. Contact your KAM if cards are being submitted but not appearing.
```

**On Collect Payments using a Tokenized Card (inline note):**

```
> 📌 Ensure the `user_credentials` passed during payment exactly matches the `var1` format used in GetUserCards. See [Troubleshooting: No cards returned for valid credentials](https://docs.payu.in/reference/get_user_cards_api_model3) for a full checklist.
```

***

## CheckoutPro — disabled payment modes re-appear after timeout

**Severity:** 🟠 High<br />**Fix type:** New callout note

### Affected Page(s)

| Page Title                                       | URL                                                                                                                                            | Section/Heading                                              |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Customise Your Integration (Android CheckoutPro) | [https://docs.payu.in/docs/android-checkoutpro-custom-integrations](https://docs.payu.in/docs/android-checkoutpro-custom-integrations)         | Payment mode customisation / `payUCheckoutProConfig` section |
| Advanced Integration (iOS CheckoutPro)           | [https://docs.payu.in/docs/ios-checkoutprosdk-advanced-integration](https://docs.payu.in/docs/ios-checkoutprosdk-advanced-integration)         | Customising payment options / removing payment modes section |
| Android Integration (React Native)               | [https://docs.payu.in/docs/reactnative-checkoutpro-android-integration](https://docs.payu.in/docs/reactnative-checkoutpro-android-integration) | Payment options customisation section                        |

### Where exactly to insert

**Page:** Customise Your Integration (Android CheckoutPro)<br />**Heading:** `payUCheckoutProConfig` (payment mode customisation section)<br />**Position:** After the code block showing how to disable payment modes using `payUCheckoutProConfig`

**Page:** Advanced Integration (iOS CheckoutPro)<br />**Heading:** Customising payment options / removing payment modes<br />**Position:** After the code block showing disabled payment modes

**Page:** Android Integration (React Native)<br />**Heading:** Payment options customisation section<br />**Position:** After the relevant config code block

### What to add or change

```
> ⚠️ **Payment mode configuration is not persisted across SDK sessions.**
> The `payUCheckoutProConfig` settings (including disabled payment modes) apply only to the current SDK launch. If a transaction times out, the user is taken back to the checkout screen, and the SDK is re-launched, you **must pass the same configuration object again**.
>
> Failure to re-apply the config on re-launch will cause previously disabled payment modes to re-appear.
>
> **Recommended pattern:** Create your `payUCheckoutProConfig` object in a reusable method and call it every time you initialise the SDK — not just on the first launch.
```

_Note: Adapt the callout for Swift/Objective-C syntax context on the iOS page._

***

## `merchant_key_not_register_for_phonepe` error undocumented

**Severity:** 🟠 High<br />**Fix type:** New entry in troubleshooting table

### Affected Page(s)

| Page Title                                | URL                                                                                                                                    | Section/Heading                             |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| Troubleshooting CheckoutPro SDK (Android) | [https://docs.payu.in/docs/android-checkoutpro-troubleshoot-errors](https://docs.payu.in/docs/android-checkoutpro-troubleshoot-errors) | Existing error table / troubleshooting list |
| FAQs - Android SDK                        | [https://docs.payu.in/docs/faqs-android-sdk](https://docs.payu.in/docs/faqs-android-sdk)                                               | FAQ section about errors/troubleshooting    |

### Where exactly to insert

**Page:** Troubleshooting CheckoutPro SDK (Android)<br />**Heading:** Existing error/troubleshooting table<br />**Position:** Add as a new row in the existing error table

**Page:** FAQs - Android SDK<br />**Heading:** FAQ section (errors/troubleshooting)<br />**Position:** Add as a new FAQ entry in the troubleshooting section

### What to add or change

**New row for Troubleshooting CheckoutPro SDK error table:**

| Error                                                                                                | Explanation & Fix                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `onPaymentOptionInitialisationFailure (code=1)` with message `merchant_key_not_register_for_phonepe` | PhonePe Intent/SDK payment mode is not activated for your merchant account at the backend. Enabling UPI from the PayU Dashboard does NOT automatically enable PhonePe SDK — this requires a separate backend activation step. **Fix:** Contact your KAM and request PhonePe Intent/SDK enablement for your MID. Also ensure your app's package name is registered with PayU. |

**New FAQ entry for FAQs - Android SDK:**

```
**Q: I see `merchant_key_not_register_for_phonepe` during SDK initialisation. How do I fix this?**

A: This error means PhonePe payment mode has not been activated at the backend for your merchant key. Enabling UPI in the PayU Dashboard does not automatically enable PhonePe SDK — they are separate activations. To resolve:
1. Contact your Key Account Manager (KAM) and request PhonePe Intent/SDK enablement for your MID.
2. Ensure your Android app's package name (`applicationId`) is registered with PayU.
3. Confirm your app is pointing to the production environment (`setIsProduction(true)`), as this activation only applies to production.
```

***

## `intentURIData` returns a single URL, not per-app URLs

**Severity:** 🟠 High<br />**Fix type:** Clarification to existing content

### Affected Page(s)

| Page Title                      | URL                                                                                                                | Section/Heading                                  |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------ |
| UPI Intent with S2S Integration | [https://docs.payu.in/docs/upi-intent-server-to-server](https://docs.payu.in/docs/upi-intent-server-to-server)     | `Step 2: Invoke UPI Intent on customer's device` |
| UPI Intent - Non SDK Flow       | [https://docs.payu.in/docs/upi-smart-intent-non-sdk-flow](https://docs.payu.in/docs/upi-smart-intent-non-sdk-flow) | `Step 2: Get Intent URI`                         |

### Where exactly to insert

**Page:** UPI Intent with S2S Integration<br />**Heading:** `Step 2: Invoke UPI Intent on customer's device`<br />**Position:** After the paragraph "Using the IntentURIData value in response" and before the sample URL

**Page:** UPI Intent - Non SDK Flow<br />**Heading:** `Step 2: Get Intent URI`<br />**Position:** After the step description, before the request parameters table

### What to add or change

```
> 📌 **`intentURIData` is a single universal URL, not app-specific links.**
> The `intentURIData` field returns one URL formatted as `upi://pay?pa=...&pn=...&tr=...&am=...` — this is the standard NPCI UPI deep-link scheme.
>
> - **On Android:** Firing this URL triggers the OS intent chooser, which lists all installed UPI apps (GPay, PhonePe, Paytm, etc.). The customer selects their preferred app.
> - **On web (desktop):** Render this URL as a QR code for the customer to scan with their phone's UPI app.
>
> Individual app-specific deep links (e.g., `gpay://`, `phonepe://`) are **not** returned by PayU. If you want to open a specific app directly (e.g., "Pay with GPay" button), construct the app-specific intent using the `pa`, `pn`, `tr`, and `am` values from the response and fire it using the app's documented URL scheme.
```

***

## Salt v2 migration undocumented

**Severity:** 🟠 High<br />**Fix type:** New section on existing pages

### Affected Page(s)

| Page Title                        | URL                                                                                                                                                      | Section/Heading                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| Access Production Key and Salt    | [https://docs.payu.in/docs/generate-merchant-key-and-salt-on-payu-dashboard](https://docs.payu.in/docs/generate-merchant-key-and-salt-on-payu-dashboard) | Salt section (currently shows `Salt-32 bit`) |
| Access Test Merchant Key and Salt | [https://docs.payu.in/docs/generate-test-merchant-key-and-salt](https://docs.payu.in/docs/generate-test-merchant-key-and-salt)                           | Section describing Salt-32 bit               |
| Generate Hash (Request/Response)  | [https://docs.payu.in/docs/hashing-request-and-response](https://docs.payu.in/docs/hashing-request-and-response)                                         | `🚧 Salt Security` callout                   |
| Generate Hash (PayU Hosted)       | [https://docs.payu.in/docs/generate-hash-payu-hosted](https://docs.payu.in/docs/generate-hash-payu-hosted)                                               | `🚧 Salt Security` callout                   |
| Generate Hash (Merchant Hosted)   | [https://docs.payu.in/docs/generate-hash-merchant-hosted](https://docs.payu.in/docs/generate-hash-merchant-hosted)                                       | `🚧 Salt Security` callout                   |

### Where exactly to insert

**Page:** Access Production Key and Salt<br />**Heading:** Salt section (currently shows `Salt-32 bit`)<br />**Position:** After the existing salt description — add as a new subsection

**Page:** Access Test Merchant Key and Salt<br />**Heading:** Section describing Salt-32 bit<br />**Position:** After the note about copying the Salt

**Pages:** Generate Hash (all three hash pages)<br />**Heading:** `🚧 Salt Security` callout<br />**Position:** After the existing callout

### What to add or change

**On Access Production Key and Salt (new subsection):**

```markdown
### v1 (32-bit) and v2 (64-bit)

PayU provides two versions of Salt for your merchant account:

| Version | Length | Also called | Used for |
|---|---|---|---|
| Salt v1 | 32 characters | Salt-32 bit | Standard payment hash (legacy) |
| Salt v2 | 64 characters | Salt-64 bit / Merchant Salt (Version 2) | Newer APIs, recommended for all new integrations |

> 📌 **PayU recommends using Salt v2 (64-bit) for all new integrations.** Salt v1 continues to work for existing integrations but may be required to upgrade for certain newer API features.

**How to get Salt v2:**
Log in to PayU Dashboard → Switch to Live Mode → Navigate to Developer → API Keys. Both Salt v1 and Salt v2 are displayed. Use the **Copy** button to avoid transcription errors.

**Salt upgrade:** If you are on Salt v1 and need to migrate to Salt v2, contact your Key Account Manager (KAM) or raise a request at integration@payu.in. After upgrading, update your server-side hash generation code to use the new 64-character salt.

> ⚠️ **Important:** After upgrading to Salt v2, your old Salt v1 hash calculations will fail immediately. Test with Salt v2 in UAT before upgrading in production.
```

**On Access Test Merchant Key and Salt (brief note):**

```
> 📌 The test environment provides Salt v1 (32-bit). Salt v2 (64-bit) is available in the production Dashboard. For more information on Salt versions, refer to [Access Production Key and Salt](https://docs.payu.in/docs/generate-merchant-key-and-salt-on-payu-dashboard).
```

**On all three Generate Hash pages (after the existing&#x20;**`🚧 Salt Security`**&#x20;callout):**

```
> 📌 See [Access Production Key and Salt](https://docs.payu.in/docs/generate-merchant-key-and-salt-on-payu-dashboard) for the difference between Salt v1 (32-bit) and Salt v2 (64-bit) and which to use for your integration.
```

***

## SI `billingCycle: ADHOC` not in parameter table

**Severity:** 🟡 Medium<br />**Fix type:** New row in parameter table

### Affected Page(s)

| Page Title                                       | URL                                                                                                                                    | Section/Heading                                                                             |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Standing Instruction Parameter Details (Android) | [https://docs.payu.in/docs/android-standing-instruction-parameters](https://docs.payu.in/docs/android-standing-instruction-parameters) | `Step 2: Post Parameters` → `billingCycle` row                                              |
| PayU Standing Instructions Parameters (iOS)      | [https://docs.payu.in/docs/ios-standing-instructions-parameters](https://docs.payu.in/docs/ios-standing-instructions-parameters)       | `Step 2: Post parameters` → `billingCycle` field                                            |
| \[S2S] UPI Consent Transaction - Cross Border    | [https://docs.payu.in/docs/upi-consent-transaction-cb](https://docs.payu.in/docs/upi-consent-transaction-cb)                           | `si_details JSON Object` → `billingCycle` field (already includes ADHOC — no change needed) |

### Where exactly to insert

**Page:** Standing Instruction Parameter Details (Android)<br />**Heading:** `Step 2: Post Parameters`<br />**Position:** Within the `billingCycle` parameter row — extend the existing description

**Page:** PayU Standing Instructions Parameters (iOS)<br />**Heading:** `Step 2: Post parameters`<br />**Position:** After the existing billingCycle description

> **Note:** The `[S2S] UPI Consent Transaction - Cross Border` page **already includes ADHOC** in its `billingCycle` field description (`DAILY, WEEKLY, MONTHLY, YEARLY, ADHOC`). No change is needed there — the Android and iOS SDK pages are the ones missing this value.

### What to add or change

**On both Android and iOS Standing Instruction Parameter pages (update the&#x20;**`billingCycle`**&#x20;field description):**

```
**Valid values for `billingCycle`:** `DAILY`, `WEEKLY`, `MONTHLY`, `YEARLY`, `ONCE`, `ADHOC`

> 📌 **`ADHOC`:** Use for on-demand or irregular billing where no fixed schedule is required. With `ADHOC`, each debit is triggered manually via the Pre-Debit Notification and Auto-Debit APIs rather than on a fixed schedule. `billingInterval` should be set to `1` when using `ADHOC`.
```

_Adapt code/syntax examples for Swift context on the iOS page._

***

## Webhook UI — delete and duplicate event creation

**Severity:** 🟡 Medium<br />**Fix type:** Correction to existing content + new note

### Affected Page(s)

| Page Title                      | URL                                                                                                                    | Section/Heading                                            |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Create a New Webhook            | [https://docs.payu.in/docs/create-a-new-webhook](https://docs.payu.in/docs/create-a-new-webhook)                       | Step-by-step webhook creation guide (end of page / Step 4) |
| Delete a Webhook                | [https://docs.payu.in/docs/delete-a-webhook-on-dashboard](https://docs.payu.in/docs/delete-a-webhook-on-dashboard)     | Step-by-step delete guide                                  |
| Manage Webhooks using Dashboard | [https://docs.payu.in/docs/manage-webhooks-using-dashboard](https://docs.payu.in/docs/manage-webhooks-using-dashboard) | Overview section                                           |

### Where exactly to insert

**Page:** Create a New Webhook<br />**Heading:** Step-by-step webhook creation guide<br />**Position:** After the "Click Create to create a webhook" step

**Page:** Delete a Webhook<br />**Heading:** Step-by-step delete guide<br />**Position:** Before or after the existing delete instructions

**Page:** Manage Webhooks using Dashboard<br />**Heading:** Overview section<br />**Position:** After the intro paragraph

### What to add or change

**On Create a New Webhook (after "Click Create" step):**

```
> 📌 **Webhook constraints:**
> - **One URL per event type:** Only one webhook URL can be registered per event (Successful, Failed, Refund, Dispute). You cannot create two separate "Successful" webhooks with different URLs.
> - **To change a URL:** Use **Update a Webhook** — do not delete and re-create.
> - **Multiple events, one URL:** A single webhook URL can receive all event types. You do not need to create separate webhooks for each event if your endpoint handles all events.
```

**On Delete a Webhook (before or after delete instructions):**

```
> ⚠️ **If the Delete button appears unresponsive:** This is a known UI limitation for certain webhook configurations. As an alternative, use **Update a Webhook** to change the URL, or contact integration@payu.in to remove the webhook.
```

**On Manage Webhooks using Dashboard (after intro paragraph):**

Add the same constraint note from Create a New Webhook above:

```
> 📌 **Webhook constraints:**
> - **One URL per event type:** Only one webhook URL can be registered per event (Successful, Failed, Refund, Dispute). You cannot create two separate "Successful" webhooks with different URLs.
> - **To change a URL:** Use **Update a Webhook** — do not delete and re-create.
> - **Multiple events, one URL:** A single webhook URL can receive all event types. You do not need to create separate webhooks for each event if your endpoint handles all events.
```

***

## "Convenience Fee" vs "Internet Handling Charges (IHC)"

**Severity:** 🟡 Medium<br />**Fix type:** New terminology note

### Affected Page(s)

| Page Title                                   | URL                                                                                                                                          | Section/Heading                |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| Collect Additional Charges                   | [https://docs.payu.in/docs/collect-additional-charges](https://docs.payu.in/docs/collect-additional-charges)                                 | First paragraph / introduction |
| Setup Convenience Fee (Android CheckoutPro)  | [https://docs.payu.in/docs/android-checkoutpro-setupconveniencefee](https://docs.payu.in/docs/android-checkoutpro-setupconveniencefee)       | Page title / first section     |
| Setup Convenience Fee (iOS CheckoutPro)      | [https://docs.payu.in/docs/ios-checkoutpro-setupconveniencefee](https://docs.payu.in/docs/ios-checkoutpro-setupconveniencefee)               | Page title / first section     |
| Setup Convenience Fee (Flutter)              | [https://docs.payu.in/docs/setup-convenience-fee-1](https://docs.payu.in/docs/setup-convenience-fee-1)                                       | Page title / first section     |
| UPI CC & CL Integration with Convenience Fee | [https://docs.payu.in/docs/upi-cc-cl-integration-with-convenience-fee](https://docs.payu.in/docs/upi-cc-cl-integration-with-convenience-fee) | `Key Highlights`               |

### Where exactly to insert

**Pages:** Collect Additional Charges; Setup Convenience Fee (Android, iOS, Flutter)<br />**Heading:** Page title / first section<br />**Position:** At the very top of the page, before the existing content

**Page:** UPI CC & CL Integration with Convenience Fee<br />**Heading:** `Key Highlights`<br />**Position:** Before the Key Highlights section

### What to add or change

**Add at the top of all five pages listed above:**

```
> 📌 **Terminology note:** "Convenience Fee" in this documentation refers to the same feature as **"Internet Handling Charges (IHC)"** shown in the PayU Dashboard and merchant communications. The product was recently rebranded. The API parameter name `convenienceFee` (and `additional_charges` in the hash) remains unchanged.
```

***

## UPI QR test transactions failing with undocumented error

**Severity:** 🟡 Medium<br />**Fix type:** New troubleshooting note

### Affected Page(s)

| Page Title                  | URL                                                                                                            | Section/Heading                                                               |
| --------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Integrate UPI QR            | [https://docs.payu.in/docs/integrate-upi-qr](https://docs.payu.in/docs/integrate-upi-qr)                       | `Test the Integration` / `Troubleshooting` section (or end of page if absent) |
| APIs for UPI QR Integration | [https://docs.payu.in/docs/apis-for-upi-qr-integration](https://docs.payu.in/docs/apis-for-upi-qr-integration) | API parameters section / API description                                      |

### Where exactly to insert

**Page:** Integrate UPI QR<br />**Heading:** `Test the Integration` or `Troubleshooting` (if present); otherwise end of page<br />**Position:** End of page, or within an existing testing/troubleshooting section

**Page:** APIs for UPI QR Integration<br />**Heading:** API parameters section<br />**Position:** After the description of required parameters

### What to add or change

**On Integrate UPI QR (new section at end of page or in testing section):**

```markdown
## Testing UPI QR

> ⚠️ **UPI QR test limitations:**
> - UPI QR transactions require the `DBQR` flag to be activated on your merchant account. If you receive an error when posting with `pg=DBQR` and `bankcode=UPIDBQR`, contact your KAM to enable this feature.
> - UPI QR in the test environment may show failures that do not replicate in production. If UPI QR transactions fail consistently in UAT with no clear error, contact integration@payu.in with your MID and a sample transaction ID for investigation.
> - Ensure `txn_s2s_flow=4` is included in your QR payment request. Without this flag, the DBQR flow will not initiate correctly.
```

**On APIs for UPI QR Integration (after required parameters description):**

```
> 📌 **Required flags:** `txn_s2s_flow=4` must be included in every UPI QR payment request. The `DBQR` payment mode (`pg=DBQR`, `bankcode=UPIDBQR`) also requires backend activation on your merchant account — contact your KAM if UPI QR is not working despite correct parameters.
```

<br />
