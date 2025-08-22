---
title: Virtual Card Integration
deprecated: false
hidden: false
metadata:
  robots: index
---
You can integrate Virtual card using `payu-ppi-react` SDK in React Native. This section describes the procedure to integrate Virtual Card using React-Native SDK.

# Overview

The PayU PPI React Native SDK presents a native Virtual Cards management experience inside your RN a

Launch native card UI via a single showCards entry point.

Provide a dynamic hash on-demand via a callback and respond using hashGenerated.

Receive lifecycle callbacks: onCancel, onError.

The RN wrapper delegates to PayU’s native PPI SDKs under the hood (Android & iOS) and therefore inherits their platform requirements and flows.

<br />

# Prerequisites

Merchant Key & Salt (Test and/or Production) available from PayU.

walletIdentifier (Merchant Wallet Identifier) & walletUrn (User Wallet URN linked to the given mobile).

User mobile number used for the wallet.

Server endpoint to compute dynamic hashes (salted SHA‑512). The hash must be generated on your backend only.

# Install

```
# with npm
npm i payu-ppi-react@1.0.0-alpha.2
# or with yarn
yarn add payu-ppi-react@1.0.0-alpha.2
```

<br />

## React Native Autolinking

RN ≥ 0.60 is supported via autolinking.

iOS: run cd ios && pod install after installing the package.

## Android Gradle Repos

Ensure mavenCentral() is present in your android/build.gradle repositories.

***

# Platform Setup Notes

Because this wrapper embeds/uses the native PPI SDKs, keep these guidelines in mind:

<br />

## Android

Ensure minSdkVersion and Gradle/AGP versions satisfy your app baseline and the PPI SDK.

Internet permission is required (usually present by default), If missing:

```
<!-- android/app/src/main/AndroidManifest.xml --
<uses-permission android:name="android.permission.INTERNET" />
```

<br />

# iOS

After pod install, open the .xcworkspace and build.

Recommended: iOS 13+ (or higher per your app baseline).

Use your existing app signing/capabilities; no special entitlements are typically required for presenting the PPI UI.

# API (React Native)

The public surface mirrors RN concepts.

```
// Environment: 0 = Production, 1 = Test
export type PPIEnvironment = 0 | 1;
const hashName = ""

export type PPIParams = {
  merchantKey: string;
  referenceId: string;      // any unique reference per invocation
  walletUrn: string;        // user wallet URN linked to the mobile number
  environment: PPIEnvironment;  // 0 (Prod) or 1 (Test)
  walletIdentifier: string; // merchant wallet identifier
  mobileNumber: string;     // user’s mobile number
};

export type ShowCardsCallbacks = {
  /**
   * SDK requests a dynamic hash. Your app MUST compute the hash on the server
   * and respond via `hashGenerated({ [hashName]: sha512('hashString' + salt) })`.
   */
  generateHash: (payload: { hashName: string; hashString: string }) => void | Promise<void>;

  /** Invoked when user dismisses the card/OTP screens. */
  onCancel?: () => void;

  /** Invoked if any error occurs in the native flow. */
  onError?: (code: number | string, message?: string) => void;
};

```

## Methods

```
/**
 * Launch the native Virtual Cards UI.
 */
showCards(params: PPIParams, callbacks: ShowCardsCallbacks): void;

/**
 * Respond to a pending hash request.
 * Provide an object mapping the received `hashName` to the computed hash value.
 * Example: hashGenerated({ [hashName]: "<sha512>" })
 */
hashGenerated(map: Record<string, string>): void;

```

<br />

> The parameter keys and callback semantics are intentionally identical to the Flutter wrapper to minimize integration friction.

***

# Quick Start (JS/TS)

<br />

```
import React, { useCallback } from 'react';
import { Button, Alert } from 'react-native';
import PayUPPI from 'payu-ppi-react';

const PPI_DEMO_ENV: 0 | 1 = __DEV__ ? 1 : 0; // 1 = Test, 0 = Prod
const hashName = ""

export default function VirtualCardButton() {
  const onPress = useCallback(() => {
    const params = {
      merchantKey: '<YOUR_MERCHANT_KEY>',
      referenceId: `ref_${Date.now()}`,
      walletUrn: '<USER_WALLET_URN>',
      environment: PPI_DEMO_ENV,
      walletIdentifier: '<YOUR_WALLET_IDENTIFIER>',
      mobileNumber: '<USER_MOBILE_NUMBER>'
    } as const;

    PayUPPI.showCards(params, {
      generateHash: async ({ hashName, hashString }) => {
        // 1) Send hashName + hashString to your backend
        // 2) Backend appends SALT to `hashString` and computes sha512
        // 3) Respond back via hashGenerated
        try {
          const res = await fetch('https://your.api/ppi/hash', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ hashName, hashString })
          });
          const { hash } = await res.json();
          PayUPPI.hashGenerated({ [hashName]: hash });
        } catch (e) {
          console.warn('hash generation failed', e);
        }
      },
      onCancel: () => {
        // User pressed back on Cards or OTP screen
        Alert.alert('Cancelled');
      },
      onError: (code, message) => {
        Alert.alert('Error', `${code}: ${message ?? ''}`);
      }
    });
  }, []);

  return <Button title="Open Virtual Card" onPress={onPress} />;
}

```

<br />

# Server: Dynamic Hash Endpoint

Your backend must compute the hash for various commands requested by the SDK.

Hash input: The SDK sends you { "hashName", "hashString" }.

Compute: sha512( hashString + \<SALT> )

Respond: Pass the result back using hashGenerated(\{ \[hashName]: '\<sha512>' }).

## Example (Node/Express)

```
import crypto from 'crypto';
import express from 'express';

const app = express();
app.use(express.json());

const SALT = process.env.PAYU_SALT!; // NEVER expose this in the app
const hashName = "";
app.post('/ppi/hash', (req, res) => {
  const { hashName, hashString } = req.body || {};
  if (!hashName || !hashString) {
    return res.status(400).json({ error: 'Missing hashName/hashString' });
  }
  // Compute sha512(hashString + SALT)
  const value = crypto
    .createHash('sha512')
    .update(`${hashString}${SALT}`, 'utf8')
    .digest('hex');

  return res.json({ hashName, hash: value });
});

app.listen(3000);

```

<br />

> Implement equivalent logic on your stack (.NET/Java/Go/PHP/etc.). The rule is the same: append your SALT to the hashString received from the SDK, then SHA‑512.

# Event Flow (What to Expect)

1. showCards(params) opens the native PPI UI.
2. When needed, SDK triggers generateHash(\{ 'hashName, 'hashString' }).
3. Your app calls backend → computes SHA‑512 with SALT.
4. App responds via hashGenerated(\{ \[hashName]: '\<sha512>' }).
5. User completes flow; you may receive onCancel (user backs out) or onError (any error surfaced by native SDK).

# Parameter Reference (1:1 with RN)

| Key              | Type   | Description                                      |
| :--------------- | :----- | :----------------------------------------------- |
| merchantKey      | string | Your PayU merchant key.                          |
| referenceId      | string | Unique reference for the invocation/transaction. |
| walletUrn        | string | User Wallet URN linked to the mobile number.     |
| environment      | 0/1    |                                                  |
| walletIdentifier | string | Merchant wallet identifier.                      |
| mobileNumber     | string | User’s mobile number.                            |

> These keys match the RN wrapper’s PayUPPIParamKey mapping and the Android/iOS native models.

# Testing vs. Production

* Use environment: 1 (Test) while integrating. Point your backend to Test merchant credentials (Key/Salt) when computing hashes.
* Switch to environment: 0 (Prod) only after completing your go‑live checklist.

# Go‑Live Checklist

* RN app builds cleanly on both Android & iOS.
* Backend hash endpoint working with proper SALT and rate limiting.
* merchantKey, walletIdentifier, walletUrn, and mobileNumber supplied correctly.
* referenceId is unique per transaction/session.
* QA completed on real devices for both platforms.

<br />

# Troubleshooting

* No callback for generateHash: Ensure showCards is invoked with the callbacks object and that JS isn’t garbage‑collecting it. Keep the callbacks in component scope.
* Flow closes immediately: Verify params (especially walletUrn, walletIdentifier, mobileNumber) match an existing wallet/user mapping.
* Hash rejected: Confirm server computes SHA‑512 of hashString + SALT and you respond using hashGenerated(\{ \[hashName]: value }).
* Android build errors: Ensure mavenCentral() is in repositories and Gradle plugin/AGP are aligned.
* iOS build errors: Run pod repo update && pod install; clean build folder; ensure modern Xcode toolchain.

# Sample: TypeScript Declarations (optional)

```
// payu-ppi-react.d.ts (for app-level typing)
declare module 'payu-ppi-react' {
  export type PPIEnvironment = 0 | 1;
  export interface PPIParams {
    merchantKey: string;
    referenceId: string;
    walletUrn: string;
    environment: PPIEnvironment;
    walletIdentifier: string;
    mobileNumber: string;
  }
  export interface ShowCardsCallbacks {
    generateHash: (payload: { hashName: string; hashString: string }) => void | Promise<void>;
    onCancel?: () => void;
    onError?: (code: number | string, message?: string) => void;
  }
  export function showCards(params: PPIParams, callbacks: ShowCardsCallbacks): void;
  export function hashGenerated(map: Record<string, string>): void;
}

```