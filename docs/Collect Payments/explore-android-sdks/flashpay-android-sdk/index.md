---
title: 'FlashPay Android SDK '
deprecated: false
hidden: false
metadata:
  robots: index
---
PayU's FlashPay is a mobile payment authentication solution that enables customers to complete card transactions using their device's biometric authentication (fingerprint or face recognition) without leaving the merchant's app. The solution operates within industry-standard 3DS (3D Secure) protocols while complying with Reserve Bank of India (RBI) guidelines for multi-factor authentication.

PayU's FlashPay SDK solution provides merchants with a comprehensive toolkit to offer customers a superior, secure, and efficient payment experience. Instead of entering OTP codes or being redirected to a bank portal, customers can authenticate card transactions directly within your app using biometrics—fingerprint, face ID, or other device-supported methods.

**Key highlights:**

* Customers authenticate payments using device biometrics without leaving your app
* Full compliance with RBI's multi-factor authentication requirements
* Works seamlessly with existing 3DS security infrastructure
* Reduced payment completion time and improved success rates

## What Problem Does FlashPay Solve?

If you're a merchant accepting card payments, you likely face these challenges:

1. **Slow checkouts** – Customers wait for OTP entry and bank redirects
2. **Cart abandonment** – Lengthy authentication processes cause customers to drop off
3. **Failed transactions** – OTP delivery delays or customer errors lead to payment failures
4. **Poor user experience** – Switching between your app and banks is disruptive

FlashPay eliminates these friction points by keeping customers within your app during the entire payment authentication process.

## Key Benefits for Your Business and Customers

Integrating FlashPay brings measurable value:

| Benefit                        | Impact                                                                                                       |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| **4x faster payments**         | Biometric authentication reduces end-to-end transaction time significantly compared to traditional OTP flows |
| **1.5–2% higher success rate** | Fewer payment failures mean more completed transactions and higher revenue                                   |
| **Better security**            | Continuous monitoring and lifecycle management enhance fraud prevention                                      |
| **Flexible fallback**          | If biometrics fail, the system automatically offers OTP as an alternative                                    |
| **Works with all cards**       | Supports all card networks, guest checkouts, saved cards, network tokens, and issuer tokens                  |
| **No major changes needed**    | Runs on existing 3DS infrastructure with minimal merchant modifications                                      |

***

## Technical Requirements

### Supported Mobile Platforms

FlashPay works on **Android: Version 6.0** and above (phones only; tablets are not supported)

<Callout icon="📘" theme="info">
  **Note:** FlashPay is designed for smartphone users only to ensure optimal biometric capture and authentication.
</Callout>

### Integration Approach

To integrate FlashPay, you'll need to:

1. Integrate the **FlashPay 3DS SDK** into your mobile app
2. Implement **Payment Aggregator (PA) APIs** for backend communication
3. Refer to the technical documentation (FlashPay_3DS SDK guide and Merchant_PA_API specifications)

## How to check whether customers can use FlashPay?

Not all cards can use FlashPay yet. Banks must first enable their card BINs (Bank Identification Numbers) with PayU.

### How to Check Card Eligibility

Use the **BIN Info API** to check whether a customer's card is eligible for FlashPay:

**What this API does:**

* Receives a card's BIN (first 6 digits)
* Returns whether that card/bank supports FlashPay biometric authentication
* Provides real-time eligibility status

**When to call it:**

* Every time a customer enters new card details (guest checkout)
* Every time a customer selects a saved card
* You need the latest eligibility information for accurate UX decisions

### Important Points to Remember

1. **Control your app's experience** – Use BIN eligibility to show or hide FlashPay options to customers
2. **Works for all card types** – The API supports guest checkouts and saved/tokenized cards
3. **Call it every transaction** – Banks enable/disable BINs over time; always fetch fresh data
4. **Future-proof** – The API expands automatically as more banks and BINs are onboarded

## Customer Registration Flow (First-Time Setup)

The first time a customer uses a FlashPay-eligible card, they go through a one-time biometric registration process.

### What Happens During Registration

**Step-by-step process:**

1. **Customer initiates payment** – They enter card details or select a saved card
2. **FlashPay eligibility check** – Your app checks if the card is eligible via BIN Info API
3. **Traditional OTP verification** – Customer enters OTP as usual (this is required for security)
4. **Biometric enrollment offer** – Bank/system offers customer the option to enroll their fingerprint/face for future payments
5. **Customer consents** – Customer agrees to enroll biometric authentication
6. **FlashPay SDK captures biometric** – Device collects fingerprint or face scan
7. **Mobile verification** – Backend verifies the biometric data
8. **Registration complete** – Customer's card is now enrolled for biometric payments
9. **Transaction completes** – Current payment is authorized

### How Your Merchant App Handles Registration

**What your app does during registration:**

1. **Initiate payment normally** – Call the 3DS SDK to collect device attributes and call PA's Payment API
2. **Bank sends response** – Bank ACS (Access Control Server) validates the card and responds (response is encrypted)
3. **Extract FlashPay indicator** – Your app extracts the FlashPay indicator from the bank's encrypted response
4. **Show registration UI** – Pass the response to FlashPay 3DS SDK, which displays:
   * OTP entry screen
   * A checkbox/consent option to enroll for biometric authentication
5. **Receive responses** – After OTP validation and biometric enrollment, FlashPay SDK returns:
   * OTP validation status (success/failure)
   * Whether customer consented to biometric registration
6. **Store registration status** – Save which cards are FlashPay-enrolled so future payments skip registration
7. **Complete authorization** – Call the Authorization API to debit the customer's account

### Key Points for Implementation

* **Registration happens once per card** – After initial enrollment, customers use biometric for that card
* **Happens inline** – Everything occurs within your app during the first payment
* **OTP is still required for registration** – The first payment always needs OTP entry for security
* **Track enrollment status** – Tag enrolled cards in your database to optimize the flow for repeat customers
* **Guest and saved cards** – Registration works for both new card entries and previously saved cards

## Transaction Authentication Flow (Repeat Payments)

Once a customer has registered their card for FlashPay, subsequent payments using that card are much faster and smoother.

### What Happens During Authentication

**Step-by-step process:**

1. **Customer selects enrolled card** – They pick a card that's already registered for FlashPay
2. **Education message shown** – Optional UI reminds customer their card supports biometric auth
3. **Custom biometric screen** – FlashPay SDK displays a custom authentication screen with biometric prompt
4. **Customer provides biometric** – Fingerprint, face scan, or other device-supported biometric
5. **Transaction completes** – Payment is instantly authorized
6. **Optional fallback** – If biometric fails, customer can automatically or manually fall back to OTP

### How Your Merchant App Handles Authentication

**What your app does for repeat payments:**

1. **Initiate payment normally** – Call the 3DS SDK and PA's Payment API as usual
2. **Bank sends response** – Bank ACS responds with FlashPay indicator (encrypted)
3. **Send to FlashPay SDK** – Pass the response to FlashPay 3DS SDK
4. **SDK shows biometric screen** – Custom UI prompts customer for fingerprint/face scan
5. **Customer authenticates** – Biometric is captured and validated locally on the device
6. **Instant result** – FlashPay returns authentication success/failure immediately
7. **Smart fallback** – If biometric fails:
   * System automatically shows OTP fallback option
   * Customer can manually choose OTP if preferred
   * Standard OTP flow takes over
8. **Receive response** – SDK returns authentication result to your app
9. **Complete authorization** – Call the Authorization API to debit the account

### Key Points for Implementation

* **Much faster** – Biometric authentication is near-instant vs. waiting for OTP
* **Automatic fallback** – If biometric fails, OTP is ready as a backup
* **Always available** – Every repeat transaction can use biometric if enrolled
* **Silent retries** – System may automatically retry biometric once before showing fallback
* **Secure capture** – Biometric never leaves the customer's device
