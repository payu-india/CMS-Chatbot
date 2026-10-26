---
title: Visa Payment Passkey
deprecated: false
hidden: true
metadata:
  robots: index
---
Visa Payment Passkey lets your customers authenticate Visa card payments with the same method they use to unlock their phone or laptop: fingerprint, Face ID or device PIN. They don't need to enter a one-time password (OTP) on the bank's page.

Visa Payment Passkey is built on the FIDO2 industry standard. The passkey stays on the customer's device and can't be shared or phished the way an OTP can. This makes checkout faster and more secure.

### How it works

Visa Payment Passkey has two parts:

**1. Setting up the passkey (first payment)**

- The customer pays with an eligible Visa card as usual.
- They complete the standard OTP verification once.
- They're then asked to create a passkey on their device using fingerprint, Face ID or device PIN.

**2. Paying with the passkey (later payments)**

- When the customer pays with the same card on the same device, they're asked to confirm the payment with biometrics or device PIN.
- Authentication takes a few seconds and doesn't need an OTP.

### Benefits

**For your customers**

- **Faster checkout:** they don't wait for an OTP, switch apps or type a code.
- **Familiar experience:** it works the same way as unlocking their device.
- **Better security:** the passkey is tied to their device and can't be shared or intercepted.

**For you**

- **Less checkout friction:** fewer steps at authentication, so fewer drop-offs from OTP delays or failures.
- **Lower fraud risk:** authentication can't be phished, which reduces fraud from shared or stolen OTPs.
- **No extra integration work:** PayU handles the passkey flow during card authentication.

### Eligibility

Visa Payment Passkey is available when:

- The customer pays with an **India-issued Visa card** from a **supported issuing bank**.
- Your account is enabled for **3DS 2.0 card authentication** through PayU.
- Your account is processed through an **acquiring bank that supports Visa Payment Passkey**.

Other cards continue to use the standard 3DS/OTP flow.

### Fallback

If passkey authentication can't be completed, the payment automatically switches to the standard OTP flow. This covers cases such as an unsupported device, the customer cancelling, or a technical error. The customer can still finish the payment, and you don't need to do anything.

### How to enable

To enable Visa Payment Passkey for your account, contact [PayU Support](<redacted URL>). The team will check whether your account is eligible and turn on the feature.
