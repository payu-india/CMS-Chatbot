---
title: ' PayU Hosted Customer Journey - Banking Connect'
deprecated: false
hidden: true
metadata:
  robots: index
---
This section describes the customer journey for PayU Hosted integration on Desktop and Mobile devices.

## &#x20;Desktop

### QR Flow

1. Customer selects net banking on PayU Hosted Checkout (desktop)
2. PayU generates dynamic QR code via Banking Connect

<Image align="center" border={true} src="https://files.readme.io/c290c0a2e2e1f247046bbb2727d15edd3c392df8f0b533f8e6e10f6c635471b8-PayU_Hosted_web_QR_Step1.png" className="border" />

3. Customer scans QR with their mobile banking app

<Image align="center" border={true} src="https://files.readme.io/8370aa5e413bb879b168311f1d5f19b9d43b9efeb2be78996c2120dfd6b01b9f-PayU_Hosted_web_QR_Step2.png" className="border" />

4. Banking app decodes transaction details and initiates authentication
5. Payment completion with OTP/biometric verification on mobile
6. Real-time status update displayed on desktop merchant page

<Image align="center" border={true} src="https://files.readme.io/f4963eecea03132e3aaf4707a05bf8cda1a42202bf2ab3a6f6775aeb93451a50-PayU_Hosted_web_QR_Step3.png" className="border" />

### Redirect Flow

1. Customer chooses net banking payment option on desktop
2. PayU redirects to Banking Connect-managed bank pages
3. Customer login with banking credentials on desktop browser
4. Transaction completion on bank website interface
5. Automatic redirect back to merchant confirmation page
6. Transaction status displayed on desktop

## Mobile

### QR Flow

1. Customer accesses PayU Hosted Checkout on mobile browser
2. Banking Connect generates QR code optimized for mobile display

<Image align="center" border={false} src="https://files.readme.io/c482f64ed45db1bb90229403551a697527fa3379b205b4cf642e4dfea47da96c-PayU_Hosted_Mobile_QR_Step3.png" />

3. Customer switches to banking app to scan QR

<Image align="center" border={false} src="https://files.readme.io/01c3ca4d8fb6d0f34b0ca5b13de7b88f940b4e1a52d8b0555b28e0c2719b1307-PayU_Hosted_Mobile_QR_Step4.png" />

4. In-app transaction processing and authentication

<Image align="center" border={false} src="https://files.readme.io/3bac1e0b01559141d24552bfa35c1918b01874731323d73a42cc3c7ef9f213bf-PayU_Hosted_Mobile_QR_Step5.png" />

5. Return to mobile browser with completion status

<Image align="center" border={false} src="https://files.readme.io/24ba78402ed89163b6437a5544ac9fcfb34e5b804e2b5cbb43c0de01270dced3-PayU_Hosted_Mobile_QR_Step6.png" />

6. Mobile-optimized confirmation page display

### App Intent Flow

1. Customer selects net banking on mobile browser/app

<Image align="center" border={true} width="300px" src="https://files.readme.io/f700c55cf1c2b6f1240c8caaef1164ab86079012f3fc16d48e3a710591d491eb-PayU_Hosted_Mobile_Intent_Step1.png" className="border" />

2. PayU creates intent URL for selected bank via Banking Connect

<Image align="center" border={true} width="300px" src="https://files.readme.io/434eb8e964cee3cbd3758edbc891bd8ee3d824c32d87d21e6563c81441937ff2-PayU_Hosted_Mobile_Intent_Step2.png" className="border" />

3. Automatic deep linking to banking app (Android/iOS)

<Image align="center" border={true} width="300px" src="https://files.readme.io/b6ca6678254dd895f2b8943d2fd073938308c07d86c22c6bd1f57c23a51220a8-PayU_Hosted_Mobile_Intent_Step3.png" className="border" />

4. Native in-app authentication and payment authorization

<Image align="center" border={true} width="300px" src="https://files.readme.io/b912d26e6cd7e6a65cd9db35fc7a3a517c74ba635281d4ce5a080d907caaf51c-PayU_Hosted_Mobile_Intent_Step4.png" className="border" />

5. Instant callback to PayU mobile interface

<Image align="center" border={false} width="300px" src="https://files.readme.io/7982763d3af12d7c3c938a7ea20f25dc9e524c0e6df6dea589663352722350ba-PayU_Hosted_Mobile_Intent_Step5.png" />

6. Seamless transaction confirmation

<Image align="center" border={false} width="300px" src="https://files.readme.io/385399cf564718d019b89c6121c163bef58fac909f6f8c28a5ce5c2ca04bb3ae-PayU_Hosted_Mobile_Intent_Step7.png" />

### Mobile Desktop Compatibility

* Cross-platform session management between mobile and desktop
* QR codes generated on desktop can be scanned by mobile app
* Transaction status synchronization across device
* Unified merchant dashboard for multi-device transactions
