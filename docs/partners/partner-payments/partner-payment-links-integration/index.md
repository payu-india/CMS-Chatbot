---
title: Partner Payment Links Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
Partner Payment Links enables partners (resellers) to initiate PayU payments on behalf of their merchants using pre-generated payment links. This API-first integration supports both hosted checkout (HPP) and UPI Intent flows.

<Note>
**Prerequisites**

Before you begin, ensure you have:
- Registered as a PayU reseller with a valid `reseller_uuid`
- Linked merchants to your reseller account
- OAuth application configured with `partner_payment_links` scope
- Valid `client_id` and `client_secret` issued by PayU
- Merchant credentials: `merchant_id`, `merchant_key`, and `salt`
</Note>

***

## Step 1: Start Integration

### Step 1.1: Obtain OAuth2 Access Token

<Accordion title="Step 1.1: Obtain OAuth2 Access Token" icon="key">
  **What you need:** Your `client_id` and `client_secret` issued by PayU

  All Partner Payment Links API calls require OAuth2 authentication. Generate an access token using the `client_credentials` grant.

  **Request Parameters**

  | Parameter       | Type & Description                                    | Example                 |
  | :-------------- | :---------------------------------------------------- | :---------------------- |
  | `client_id`     | `string` — Reseller client ID issued by PayU          | `a1b2c3d4e5f6`          |
  | `client_secret` | `string` — Reseller client secret (keep confidential) | `s3cr3t_K3y_9xZ`        |
  | `grant_type`    | `string` — Must be `client_credentials`               | `client_credentials`    |
  | `scope`         | `string` — Must be `partner_payment_links`            | `partner_payment_links` |

  **Request**

  ```bash
  curl --location 'https://uat-accounts.payu.in/oauth/token' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'client_id=YOUR_CLIENT_ID' \
  --data-urlencode 'client_secret=YOUR_CLIENT_SECRET' \
  --data-urlencode 'grant_type=client_credentials' \
  --data-urlencode 'scope=partner_payment_links'
  ```

  **Sample Response**

  ```json
  {
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "Bearer",
    "expires_in": 3600,
    "scope": "partner_payment_links"
  }
  ```

  Store the `access_token` securely and use it in the `Authorization: Bearer <TOKEN>` header for all subsequent API calls.

  <Callout icon="📖" theme="default">
    ### **Full API Reference:** [OAuth Token Generation API](page2_oauth_token_api.md)
  </Callout>

  **Checkpoint:** ✅ You should receive a `200 OK` response with a valid `access_token`. Token is valid for 3600 seconds (1 hour).
</Accordion>

***

### Step 1.2: Fetch Payment Link Metadata

<Accordion title="Step 1.2: Fetch Payment Link Metadata" icon="magnifying-glass">
  **What you need:**

  - OAuth access token from Step 1.1
  - Full PayU payment link URL (e.g., `https://v.payu.in/PAYUMN/abc123`)

  Before initiating a payment, retrieve the payment link metadata to validate its status, amount, currency, and expiry.

  **Request Parameters**

  | Parameter                 | Type & Description                          | Example                           |
  | :------------------------ | :------------------------------------------ | :-------------------------------- |
  | `payment_link` 📍 Query   | `string` — Full PayU payment link URL       | `https://v.payu.in/PAYUMN/abc123` |
  | `Authorization` 📍 Header | `string` — OAuth Bearer token from Step 1.1 | `Bearer eyJhbGciOi...`            |

  **Request**

  ```bash
  curl --location 'https://uat-api.payu.in/apilayer/partner/payment-link/metadata?payment_link=https://v.payu.in/PAYUMN/abc123' \
  --header 'Authorization: Bearer YOUR_ACCESS_TOKEN'
  ```

  **Sample Response**

  ```json
  {
    "amount": 10000,
    "currency": "INR",
    "description": "Order #12345 payment",
    "payment_link_id": "https://v.payu.in/PAYUMN/abc123",
    "payment_link_status": "PENDING",
    "expiry_time": 1735689600
  }
  ```

  <Callout icon="📖" theme="default">
    ### **Full API Reference:** [Fetch Payment Link Metadata API](page3_fetch_metadata_api.md)
  </Callout>

  **Checkpoint:** ✅ Response contains `payment_link_status: "PENDING"` and `expiry_time` is greater than current Unix timestamp.
</Accordion>

***

### Step 1.3: Prepare Payment Request Parameters

<Accordion title="Step 1.3: Prepare Payment Request Parameters" icon="list-check">
  **What you need:** Metadata from Step 1.2 and customer's phone number

  You'll need to construct the payment initiation request with the following parameters:

  **Request Parameters**

  | Parameter                     | Type & Description                              | Example                           | Required       |
  | :---------------------------- | :---------------------------------------------- | :-------------------------------- | :------------- |
  | `Authorization` 📍 Header     | `string` — OAuth Bearer token                   | `Bearer eyJhbGciOi...`            | ✅ Yes          |
  | `Content-Type` 📍 Header      | `string` — Must be `application/json`           | `application/json`                | ✅ Yes          |
  | `payment_link_id` 📍 Body     | `string` — Full payment link URL from metadata  | `https://v.payu.in/PAYUMN/abc123` | ✅ Yes          |
  | `phone_number` 📍 Body        | `string` — Customer phone (5-16 digits only)    | `9876543210`                      | ✅ Yes          |
  | `amount` 📍 Body              | `number` — Amount from metadata response        | `10000`                           | ✅ Yes          |
  | `currency` 📍 Body            | `string` — Currency from metadata response      | `INR`                             | ✅ Yes          |
  | `description` 📍 Body         | `string` — Description from metadata            | `Order #12345 payment`            | ✅ Yes          |
  | `payment_link_status` 📍 Body | `string` — Must be `PENDING` from metadata      | `PENDING`                         | ✅ Yes          |
  | `expiry_time` 📍 Body         | `integer` — Unix timestamp from metadata        | `1735689600`                      | ✅ Yes          |
  | `redirect_url` 📍 Body        | `string` — Partner callback URL (HPP flow only) | `https://partner.com/callback`    | ⚠️ Conditional |

  <Warning>
  **Important Validation Rules**
  - `phone_number` must contain only digits (5-16 characters)
  - `redirect_url` domain must be in your configured allowed payment-link domains
  - If you omit `redirect_url`, the response will contain a UPI Intent URL
  - All metadata fields must match exactly
  </Warning>

  <Callout icon="📖" theme="default">
    ### **Full API Reference:** [Initiate Payment API](page4_initiate_payment_api.md)
  </Callout>

  **Checkpoint:** ✅ All required parameters are prepared and validated.
</Accordion>

***

### Step 1.4: Initiate Payment Link

<Accordion title="Step 1.4: Initiate Payment (HPP or UPI Intent)" icon="credit-card">
  **What you need:** OAuth access token and payment parameters from Step 1.3

  **Request**

  ```bash
  curl --location 'https://uat-api.payu.in/apilayer/partner/payment-link/payment' \
  --header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  --header 'Content-Type: application/json' \
  --data '{
    "payment_link_id": "https://v.payu.in/PAYUMN/abc123",
    "phone_number": "9876543210",
    "redirect_url": "https://yourpartnersite.com/payment/callback",
    "amount": 10000,
    "currency": "INR",
    "description": "Order #12345 payment",
    "payment_link_status": "PENDING",
    "expiry_time": 1735689600
  }'
  ```

  **Sample Response**

  ```json
  {
    "order_ref_id": "ORD_PARTNER_20240101_001",
    "hpp_url": "https://secure.payu.in/checkout?token=abc123xyz456",
    "expiry_time": 1735689600
  }
  ```

  **Checkpoint:** ✅ You receive `order_ref_id` and either `hpp_url` or `upi_intent_url`.
</Accordion>

***

## Step 2: Test Integration

### Step 2.1: Pre-Integration Validation

<Accordion title="Step 2.1: Pre-Integration Validation" icon="clipboard-check">
  Before testing payment flows, verify your setup:

  1. ✅ Verify OAuth credentials work with UAT endpoint
  2. ✅ Check reseller configuration is active
  3. ✅ Test environment URLs are accessible
  4. ✅ Validate allowed domains configuration

  **Checkpoint:** ✅ All credentials and configurations verified.
</Accordion>

***

## Step 3: Going Live

### Step 3.1: Update to Production Credentials

<Accordion title="Step 3.1: Update to Production Credentials" icon="key">
  > **⚠️ Info Gap:** Production OAuth and API base URLs not documented. Contact your PayU integration team to obtain production URLs and credentials.

  **Checkpoint:** ✅ All code references production credentials; no UAT endpoints remain.
</Accordion>

***

**You're now live with Partner Payment Links! 🎉**

For ongoing support and API updates, refer to the individual API reference pages:

- [OAuth Token Generation API](page2_oauth_token_api.md)
- [Fetch Payment Link Metadata API](page3_fetch_metadata_api.md)
- [Initiate Payment API](page4_initiate_payment_api.md)
