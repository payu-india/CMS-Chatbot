---
title: Payment Links via UPI Intent
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: 'Payment Links via UPI Intent - Partner Payments'
deprecated: false
hidden: false
metadata:
  title: Payment Links via UPI Intent (UPI_PL) Integration Guide | PayU Partner Payments
  description: Step-by-step developer integration guide for partners to fulfill PayU payment links directly via UPI Intent (UPI_PL) without browser redirection.
  keywords:
    - PayU Payment Links
    - UPI_PL
    - UPI Intent Payment Link
    - Partner Payments
    - Reseller Payments
    - S2S Payment Link
    - verifyPayment
  robots: index
next:
  description: ''
  pages:
    - slug: payment-links-hosted-checkout-partner
      title: Payment Links via Hosted Checkout (NON_UPI_PL)
      type: doc
---

PayU Partner Payments **Payment Links via UPI Intent (`UPI_PL`)** enables partners and resellers to fulfill standard merchant payment links directly on mobile devices using installed UPI applications (Google Pay, PhonePe, Paytm, BHIM, Cred, etc.) without requiring a web browser redirect.

In this integration, the partner queries the metadata of an existing PayU payment link and initiates an S2S transaction request without passing a `redirect_url`. PayU returns an `upi_intent_url` (deep link) which the partner app triggers on the customer's device.

**Key Benefits:**

- **Zero Web Redirection:** Seamless in-app experience without launching web views or browsers.
- **Higher Conversion Rates:** Deep-link intent directly opens the user's preferred UPI app for instant PIN authorization.
- **Conversational & Mobile Commerce:** Ideal for chat platforms (e.g., WhatsApp bots, RCS, SMS-triggered apps) and native mobile apps.
- **Real-Time Webhooks:** Immediate asynchronous confirmation via partner-level webhooks upon transaction completion.

***

## How It Works

```mermaid
sequenceDiagram
    autonumber
    actor Customer
    participant Partner as Partner App / Server
    participant PayU as PayU Partner API Layer
    participant UPI as NPCI / Customer UPI App

    Partner->>PayU: 1. Request Bearer Token (grant_type=client_credentials)
    PayU-->>Partner: Returns access_token (scope: partner_payment_links)
    Partner->>PayU: 2. GET /payment-link/metadata?payment_link=<URL>
    PayU-->>Partner: Returns link metadata (amount, status, expiry)
    Partner->>PayU: 3. POST /payment-link/payment (payment_link_id, phone_number, omit redirect_url)
    PayU-->>Partner: Returns upi_intent_url & order_ref_id
    Partner->>Customer: 4. Invoke installed UPI app with upi_intent_url
    Customer->>UPI: 5. Authorize payment using UPI PIN
    UPI->>PayU: 6. Transaction processed & validated
    PayU->>Partner: 7. Payment Webhook Notification
    Partner->>PayU: 8. GET /payment-link/verifyPayment?order_ref_id=<ID>&payment_link_id=<URL>
    PayU-->>Partner: Returns final transaction status (UPI_PL)
```

***

## Prerequisites

Before integrating the `UPI_PL` flow, ensure that:

1. **Partner Registration:** You have an active reseller account with a valid `reseller_uuid`.
2. **Merchant Linking:** The merchant whose payment link is being fulfilled is linked to your reseller account.
3. **OAuth Scopes:** Your OAuth application has the `partner_payment_links` scope enabled.
4. **UPI Enforcement on Payment Link:** The merchant's payment link must be configured to support or enforce UPI as an accepted payment method.
5. **Eligibility Rules:**
   - Link status must be `PENDING`.
   - Link must not have custom attributes or partial payments enabled.
   - Transaction amount must be greater than zero.
6. **Webhook Registration:** Configure `partner_payment_link_webhook_url` in `partner_merchant_params` to receive asynchronous callbacks.

***

## Step 1: Generate Access Token

Obtain an OAuth Bearer token using the `client_credentials` grant type.

### Endpoint URLs

| Environment | URL |
| :--- | :--- |
| **Sandbox (UAT)** | `POST https://uat-accounts.payu.in/oauth/token` |
| **Production** | `POST https://accounts.payu.in/oauth/token` |

```bash
curl --location 'https://uat-accounts.payu.in/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=<YOUR_RESELLER_CLIENT_ID>' \
--data-urlencode 'client_secret=<YOUR_RESELLER_CLIENT_SECRET>' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode 'scope=partner_payment_links'
```

**Response:**
```json
{
  "access_token": "a1b2c3d4e5f67890abcdef1234567890",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "partner_payment_links"
}
```

***

## Step 2: Fetch Payment Link Metadata

Verify that the payment link is valid, active (`PENDING`), and capture the amount before initiating the transaction.

### Endpoint URLs

| Environment | URL |
| :--- | :--- |
| **Sandbox (UAT)** | `GET https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/metadata?payment_link=<PAYMENT_LINK_URL>` |
| **Production** | `GET https://partnerapilayer.payu.in/apilayer/partner/payment-link/metadata?payment_link=<PAYMENT_LINK_URL>` |

### Request Headers

```http
Authorization: Bearer <access_token>
```

### Sample Request

```curl
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/metadata?payment_link=https://v.payu.in/PAYUMN/abc123' \
--header 'Authorization: Bearer your_access_token_here'
```
```python
import requests

url = "https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/metadata"
params = {"payment_link": "https://v.payu.in/PAYUMN/abc123"}
headers = {"Authorization": "Bearer your_access_token_here"}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```
```javascript
const response = await fetch('https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/metadata?payment_link=https://v.payu.in/PAYUMN/abc123', {
  headers: { 'Authorization': 'Bearer your_access_token_here' }
});
const data = await response.json();
console.log(data);
```

### Response Schema

```json
{
  "amount": 250.0,
  "currency": "INR",
  "description": "Order #48291 Invoice",
  "payment_link_id": "https://v.payu.in/PAYUMN/abc123",
  "payment_link_status": "PENDING",
  "expiry_time": 1735689600
}
```

***

## Step 3: Initiate UPI Intent Payment (`UPI_PL`)

To trigger the **`UPI_PL` flow**, send a `POST` request with `payment_link_id` and customer's `phone_number`. **Do not include `redirect_url`** in the payload.

### Endpoint URLs

| Environment | URL |
| :--- | :--- |
| **Sandbox (UAT)** | `POST https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/payment` |
| **Production** | `POST https://partnerapilayer.payu.in/apilayer/partner/payment-link/payment` |

### Request Headers

```http
Authorization: Bearer <access_token>
Content-Type: application/json
```

### Request Body Parameters

| Parameter | Type | Required | Description | Example |
| :--- | :--- | :--- | :--- | :--- |
| `payment_link_id` | string | **Yes** | Full URL of the PayU payment link | `https://v.payu.in/PAYUMN/abc123` |
| `phone_number` | string | **Yes** | Customer 10-digit mobile number | `919820988398` |
| `redirect_url` | string | **No (Omit)** | **Must be omitted or null** to trigger the UPI Intent flow. | *(omitted)* |

<Callout icon="💡" theme="info">
When `redirect_url` is omitted, PayU evaluates the merchant configuration and returns `upi_intent_url`. Ensure UPI is enabled on the payment link.
</Callout>

### Code Samples

```curl
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/payment' \
--header 'Authorization: Bearer your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
  "payment_link_id": "https://v.payu.in/PAYUMN/abc123",
  "phone_number": "919820988398"
}'
```
```python
import requests

url = "https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/payment"
headers = {
    "Authorization": "Bearer your_access_token_here",
    "Content-Type": "application/json"
}
payload = {
    "payment_link_id": "https://v.payu.in/PAYUMN/abc123",
    "phone_number": "919820988398"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```
```javascript
const response = await fetch('https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/payment', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer your_access_token_here',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    payment_link_id: "https://v.payu.in/PAYUMN/abc123",
    phone_number: "919820988398"
  })
});
const data = await response.json();
console.log(data);
```
```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class InitiateUPIIntentPL {
    public static void main(String[] args) throws Exception {
        String url = "https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/payment";
        String payload = "{\"payment_link_id\":\"https://v.payu.in/PAYUMN/abc123\",\"phone_number\":\"919820988398\"}";

        HttpURLConnection conn = (HttpURLConnection) new URL(url).openConnection();
        conn.setRequestMethod("POST");
        conn.setRequestProperty("Authorization", "Bearer your_access_token_here");
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setDoOutput(true);

        try (OutputStream os = conn.getOutputStream()) {
            os.write(payload.getBytes(StandardCharsets.UTF_8));
        }

        BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String line;
        StringBuilder sb = new StringBuilder();
        while ((line = br.readLine()) != null) sb.append(line);
        System.out.println(sb.toString());
    }
}
```

### Response Schema

```json
{
  "order_ref_id": "28408067218883788",
  "upi_intent_url": "upi://pay?pa=payu@axisbank&pn=PayU&am=250.00&tr=28408067218883788&cu=INR",
  "expiry_time": 1735689900
}
```

| Field | Type | Description |
| :--- | :--- | :--- |
| `order_ref_id` | string | PayU unique order reference identifier |
| `upi_intent_url` | string | Deep-link URI to trigger installed UPI applications on the customer's device |
| `expiry_time` | integer | Intent link expiration Unix timestamp |

***

## Step 4: Launch UPI App on Customer Device

Pass the `upi_intent_url` to the customer's mobile device to trigger UPI apps:

### Android (Intent Invocation)
```kotlin
val intentUri = Uri.parse(upiIntentUrl)
val upiIntent = Intent(Intent.ACTION_VIEW, intentUri)
val chooser = Intent.createChooser(upiIntent, "Pay with UPI")
if (upiIntent.resolveActivity(packageManager) != null) {
    startActivityForResult(chooser, UPI_PAYMENT_REQUEST_CODE)
}
```

### iOS (Custom URL Scheme)
```swift
if let url = URL(string: upiIntentUrl) {
    if UIApplication.shared.canOpenURL(url) {
        UIApplication.shared.open(url, options: [:], completionHandler: nil)
    }
}
```

***

## Step 5: Verify Transaction Status

Always perform server-to-server payment verification before fulfilling orders or services.

### Endpoint URLs

| Environment | URL |
| :--- | :--- |
| **Sandbox (UAT)** | `GET https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/verifyPayment?order_ref_id=<ORDER_REF_ID>&payment_link_id=<PAYMENT_LINK_URL>` |
| **Production** | `GET https://partnerapilayer.payu.in/apilayer/partner/payment-link/verifyPayment?order_ref_id=<ORDER_REF_ID>&payment_link_id=<PAYMENT_LINK_URL>` |

### Sample Request

```bash
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/verifyPayment?order_ref_id=28408067218883788&payment_link_id=https://v.payu.in/PAYUMN/abc123' \
--header 'Authorization: Bearer your_access_token_here'
```

### Sample Response (`UPI_PL`)

```json
{
  "order_ref_id": "28408067218883788",
  "payment_link_id": "https://v.payu.in/PAYUMN/abc123",
  "order_status": "success",
  "payments": [
    {
      "payment_id": "403993715531980001",
      "status": "success",
      "method": "UPI",
      "transaction_type": "UPI_PL",
      "pg_error_message": null
    }
  ]
}
```

***

## Webhook Configuration

Ensure your partner webhook endpoint is listening for asynchronous notifications:

```sql
INSERT INTO partner_merchant_params (
  partner_uuid,
  merchant_id,
  key,
  value,
  is_active
) VALUES (
  '11ee-0e7e-5403fde2-9523-0a696b110fde',
  '8739528',
  'partner_payment_link_webhook_url',
  'https://partner.example.com/webhook/upi-pl',
  true
);
```

***

## Troubleshooting & FAQ

| Error / Issue | Probable Cause | Action |
| :--- | :--- | :--- |
| `Link does not support UPI` | Merchant configuration on payment link does not permit UPI. | Merchant must reconfigure the link or use Hosted Checkout (`NON_UPI_PL`). |
| `Payment link expired` | The link has passed `expiry_time`. | Customer cannot pay. A new link must be created. |
| `Payment link already used` | Link has already been marked as paid. | Cannot be reused. |
| `Invalid phone number` | Phone number formatting error. | Pass digits only (between 5 and 16 characters). |
