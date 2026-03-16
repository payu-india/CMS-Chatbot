---
title: Decoupled Flow - AuthN AuthZ Flow
deprecated: false
hidden: true
metadata:
  robots: index
---
You can perform the payment authentication using **_payment** S2S4 flow with **auth_only=2** and then perform the authorization  using **_payment** S2S3 flow itself.

## AuthN AuthZ Flow

The Authentication and Authorization flow with PayU S2S involves the following steps:

<Image align="center" border={true} src="https://files.readme.io/e5e129a5d6bc805c134c5568f647422234d58423f9c50c6f6a626228b1489bca-s2s-autn-authz-flow-diagram.png" className="border" />

### Phase 1: Authentication

**Step 1:** Customer provides card details to the Merchant.

**Step 2:** Merchant initiates authentication by sending a `_payments` (s2s4 auth_only 2) request to PayU.

**Step 3:** PayU forwards the authentication request via 3DSS (3D Secure Server) to the Issuing Bank.

**Step 4:** Issuing Bank returns the ACS (Access Control Server) URL to PayU.

**Step 5:** PayU sends a payment response to Merchant containing either ACS URL or Post OTP URL with reference ID.

**Step 6:** Merchant redirects User to the ACS URL.

**Step 7:** User enters OTP (One-Time Password) on the authentication page and submits authentication parameters.

**Step 8:** Merchant calls the AuthData API with the reference ID from the previous step to PayU.

**Step 9:** PayU returns the authentication results to Merchant.

### Phase 2: Authorization

**Step 1:** Merchant sends a new `_payments` (s2s3) request to PayU with authentication results from Phase 1 and a new request ID.

**Step 2:** PayU forwards the authorization request to the Issuing Bank via the Payment Gateway.

**Step 3:** Issuing Bank processes the authorization and sends back an authorization response to PayU.

**Step 4:** PayU returns the transaction status to Merchant.

**Step 5:** Merchant completes the transaction flow with the User.

## Steps to Integrate

1. [S2S Decoupled Authentication Flow Integration](doc:s2s-decoupled-authentication-flow)
2. [S2S Authorization Flow Integration](doc:s2s-authorization-flow)
