---
title: Payment Links Integration using Hosted Checkout
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU Partner Payments **Payment Links via Hosted Checkout (**`NON_UPI_PL`**)** allows partners and resellers to fulfill standard merchant payment links through PayU's multi-instrument Hosted Payment Page (HPP).

This flow is suitable when customers want the flexibility to pay across multiple payment instruments—including **Credit Cards, Debit Cards, Net Banking, EMI, Wallets, and UPI**—or when customer transactions are initiated from desktop or mobile web browsers.

By passing a valid `redirect_url` in the initiation request, PayU provides a secure `hpp_url`. The partner redirects the customer's browser to this URL to complete authentication, and PayU returns the user to the specified callback URL once the transaction concludes.

**Key Benefits:**

- **Multi-Instrument Payment Support:** Supports Cards, Net Banking, Wallets, EMI, and UPI in a single integration.
- **PCI-DSS Compliant:** No card data touches partner servers; full cardholder data environment is hosted by PayU.
- **Custom Callback Redirection:** Directs the customer back to your portal or mobile web view upon completion.
- **Reseller Managed Integration:** Execute and track payments for all linked merchants with a single OAuth access token.

***

## How It Works

```mermaid
sequenceDiagram
    autonumber
    actor Customer
    participant Partner as Partner App / Web
    participant PayU as PayU Partner API Layer
    participant Bank as Bank / Payment Gateway

    Partner->>PayU: 1. Request Bearer Token (grant_type=client_credentials)
    PayU-->>Partner: Returns access_token (scope: partner_payment_links)
    Partner->>PayU: 2. GET /payment-link/metadata?payment_link=<URL>
    PayU-->>Partner: Returns link metadata (amount, status, expiry)
    Partner->>PayU: 3. POST /payment-link/payment (payment_link_id, phone_number, redirect_url)
    PayU-->>Partner: Returns hpp_url & order_ref_id
    Partner->>Customer: 4. Redirect browser to hpp_url
    Customer->>PayU: 5. Select payment method (Cards/NB/UPI/Wallets)
    PayU->>Bank: 6. 3DS / OTP Authentication
    Bank-->>PayU: Payment authorized
    PayU-->>Customer: 7. Redirect customer back to partner redirect_url
    PayU->>Partner: 8. Send Server Webhook Notification
    Partner->>PayU: 9. GET /payment-link/verifyPayment?order_ref_id=<ID>&payment_link_id=<URL>
    PayU-->>Partner: Returns final transaction status (NON_UPI_PL)
```

***

## Prerequisites

Before integrating the `NON_UPI_PL` flow, ensure that:

1. **Partner Registration:** You have an active reseller account with a valid `reseller_uuid`.
2. **Merchant Linking:** The target merchant is linked to your reseller account.
3. **OAuth Scopes:** Your OAuth application has the `partner_payment_links` scope enabled.
4. **Allowed Redirect Domains:** The domain of the `redirect_url` provided in your payment request must be **pre-allowlisted** in PayU’s system.
5. **Eligibility Rules:**
   - Link status must be `PENDING`.
   - Link must not have custom attributes or partial payments enabled.
   - Transaction amount must be greater than zero.
6. **Webhook Configuration:** Configure `partner_payment_link_webhook_url` in `partner_merchant_params` to receive asynchronous callbacks.

***

## Step 1: Generate Access Token

Obtain an OAuth Bearer token using the `client_credentials` grant type.

### Endpoint URLs

| Environment       | URL                                             |
| :---------------- | :---------------------------------------------- |
| **Sandbox (UAT)** | `POST https://uat-accounts.payu.in/oauth/token` |
| **Production**    | `POST https://accounts.payu.in/oauth/token`     |

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

Verify that the payment link is valid, in `PENDING` state, and retrieve the amount.

### Endpoint URLs

| Environment       | URL                                                                                                               |
| :---------------- | :---------------------------------------------------------------------------------------------------------------- |
| **Sandbox (UAT)** | `GET https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/metadata?payment_link=<PAYMENT_LINK_URL>` |
| **Production**    | `GET https://partnerapilayer.payu.in/apilayer/partner/payment-link/metadata?payment_link=<PAYMENT_LINK_URL>`      |

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
  "amount": 1250.0,
  "currency": "INR",
  "description": "Annual Subscription Renewal",
  "payment_link_id": "https://v.payu.in/PAYUMN/abc123",
  "payment_link_status": "PENDING",
  "expiry_time": 1735689600
}
```

***

## Step 3: Initiate Hosted Checkout Payment (`NON_UPI_PL`)

To initiate the `NON_UPI_PL`**&#x20;hosted checkout flow**, send a `POST` request with `payment_link_id`, `phone_number`, and your pre-registered `redirect_url`.

### Endpoint URLs

| Environment       | URL                                                                               |
| :---------------- | :-------------------------------------------------------------------------------- |
| **Sandbox (UAT)** | `POST https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/payment` |
| **Production**    | `POST https://partnerapilayer.payu.in/apilayer/partner/payment-link/payment`      |

### Request Headers

```http
Authorization: Bearer <access_token>
Content-Type: application/json
```

### Request Body Parameters

| Parameter         | Type   | Required | Description                                                        | Example                                              |
| :---------------- | :----- | :------- | :----------------------------------------------------------------- | :--------------------------------------------------- |
| `payment_link_id` | string | **Yes**  | Full URL of the PayU payment link                                  | `https://v.payu.in/PAYUMN/abc123`                    |
| `phone_number`    | string | **Yes**  | Customer 10-digit mobile number                                    | `919820988398`                                       |
| `redirect_url`    | string | **Yes**  | Partner callback URL where the customer is redirected post payment | `https://merchant.example.com/payment-link/callback` |

<Warning>
**Allowlisted Redirect URL:**
The domain of `redirect_url` must be pre-approved in PayU configurations. Supplying an unapproved domain results in an error: `redirect_url domain not allowed`.
</Warning>

### Code Samples

```curl
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/payment' \
--header 'Authorization: Bearer your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
  "payment_link_id": "https://v.payu.in/PAYUMN/abc123",
  "phone_number": "919820988398",
  "redirect_url": "https://merchant.example.com/payment-link/callback"
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
    "phone_number": "919820988398",
    "redirect_url": "https://merchant.example.com/payment-link/callback"
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
    phone_number: "919820988398",
    redirect_url: "https://merchant.example.com/payment-link/callback"
  })
});
const data = await response.json();
console.log(data);
```
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        string url = "https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/payment";
        var payload = new
        {
            payment_link_id = "https://v.payu.in/PAYUMN/abc123",
            phone_number = "919820988398",
            redirect_url = "https://merchant.example.com/payment-link/callback"
        };

        var content = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");
        client.DefaultRequestHeaders.Clear();
        client.DefaultRequestHeaders.Add("Authorization", "Bearer your_access_token_here");

        HttpResponseMessage response = await client.PostAsync(url, content);
        string result = await response.Content.ReadAsStringAsync();
        Console.WriteLine(result);
    }
}
```

### Response Schema

```json
{
  "order_ref_id": "28408067218883788",
  "hpp_url": "https://secure.payu.in/_payment?token=8f39a0b1c2d3e4f5",
  "expiry_time": 1735689900
}
```

| Field          | Type    | Description                                                            |
| :------------- | :------ | :--------------------------------------------------------------------- |
| `order_ref_id` | string  | PayU unique order reference identifier                                 |
| `hpp_url`      | string  | PayU Hosted Payment Page checkout URL for customer browser redirection |
| `expiry_time`  | integer | Checkout session validity Unix timestamp                               |

***

## Step 4: Customer Redirection & Payment Completion

1. **Redirect Customer:** Redirect the customer’s browser to the returned `hpp_url`.
2. **Customer Choice:** On the PayU Hosted Page, the customer selects their preferred instrument (Credit/Debit Card, Net Banking, EMI, Wallets, UPI) and completes two-factor authentication (OTP/3DS).
3. **Browser Callback:** Upon transaction finalization, PayU redirects the customer back to your supplied `redirect_url` with transaction parameters.

***

## Step 5: Verify Transaction Status

Always perform server-to-server payment verification before fulfilling orders or services.

### Endpoint URLs

| Environment       | URL                                                                                                                                                   |
| :---------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sandbox (UAT)** | `GET https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/verifyPayment?order_ref_id=<ORDER_REF_ID>&payment_link_id=<PAYMENT_LINK_URL>` |
| **Production**    | `GET https://partnerapilayer.payu.in/apilayer/partner/payment-link/verifyPayment?order_ref_id=<ORDER_REF_ID>&payment_link_id=<PAYMENT_LINK_URL>`      |

### Sample Request

```bash
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/verifyPayment?order_ref_id=28408067218883788&payment_link_id=https://v.payu.in/PAYUMN/abc123' \
--header 'Authorization: Bearer your_access_token_here'
```

### Sample Response (`NON_UPI_PL`)

```json
{
  "order_ref_id": "28408067218883788",
  "payment_link_id": "https://v.payu.in/PAYUMN/abc123",
  "order_status": "success",
  "payments": [
    {
      "payment_id": "403993715531980002",
      "status": "success",
      "method": "CC",
      "transaction_type": "NON_UPI_PL",
      "pg_error_message": null
    }
  ]
}
```

***

## Webhook Configuration

Configure your partner webhook endpoint to receive asynchronous status updates:

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
  'https://partner.example.com/webhook/non-upi-pl',
  true
);
```

***

## Troubleshooting & FAQ

| Error / Issue                     | Probable Cause                                                           | Action                                                                      |
| :-------------------------------- | :----------------------------------------------------------------------- | :-------------------------------------------------------------------------- |
| `redirect_url domain not allowed` | The domain of `redirect_url` is not allowlisted in PayU settings.        | Contact PayU Partner Integration team to allowlist your callback domain.    |
| `Payment link expired`            | The link has passed `expiry_time`.                                       | Customer cannot pay. A new link must be created.                            |
| `Payment link already used`       | Link has already been marked as paid.                                    | Cannot be reused.                                                           |
| `Auth token is not valid`         | Access token missing, expired, or lacking `partner_payment_links` scope. | Regenerate token via OAuth endpoint ensuring `scope=partner_payment_links`. |
