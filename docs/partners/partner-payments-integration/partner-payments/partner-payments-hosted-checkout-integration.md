---
title: Partner Payments Hosted Checkout Integration
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
---
title: "Partner Payments — Hosted Checkout Integration"
excerpt: "Integrate PayU's hosted checkout for partner payments with OAuth authentication, supporting cards, UPI, net banking, and wallets."
category: "65dd9cf7bc5a4a001d4e160d"
---

# Partner Payments — Hosted Checkout Integration

## Introduction

Partner Payments Hosted Checkout enables partners to redirect customers to PayU's secure, PCI-compliant payment gateway where they can complete payments using multiple payment methods—all without handling sensitive card data or building custom payment forms.

Unlike Payment Links (which create shareable URLs for remote payments), Partner Payments Hosted Checkout is designed for **direct integration** into your platform's checkout flow. When a customer initiates checkout on your website or app, you create a payment session via the Partner Payments API and immediately redirect them to PayU's hosted checkout page.

**Key Benefits:**

- **Multi-method payment support** — Cards, UPI, net banking, wallets in a single integration
- **PCI-DSS compliance** — PayU handles all card data; you never touch sensitive information
- **Proven conversion** — Optimized checkout UI tested across millions of transactions
- **Zero maintenance** — PayU manages payment method updates, bank integrations, and compliance
- **Brand consistency** — Customizable checkout page with your merchant branding

This integration is ideal for:
- **E-commerce platforms** managing payments for multiple merchants
- **Subscription services** requiring recurring payment collection
- **B2B platforms** enabling business-to-business transactions
- **Marketplaces** facilitating buyer-seller payments

---

## How It Works

The Partner Payments Hosted Checkout flow follows these steps:

1. **OAuth Authentication** — Obtain an access token with scopes: `create_payment_links`, `partner_payment_links`, `partner_payments`

2. **Initiate Payment** — POST a payment request to the Partner Payments API with transaction details, callback URLs (`surl`, `furl`, `curl`), and a computed hash

3. **Receive Redirect URL** — PayU returns a `redirectUri` pointing to the hosted checkout page

4. **Redirect Customer** — Immediately redirect the customer to the `redirectUri` in their browser

5. **Customer Completes Payment** — Customer selects a payment method on PayU's hosted page, authenticates, and completes the transaction

6. **Customer Redirected Back** — PayU redirects the customer to your success/failure/cancel URL based on payment outcome

7. **Receive Webhook** — PayU sends payment status notification to your configured partner webhook URL

8. **Verify Payment** — Call the Verify Payment API to confirm final transaction status

---

## Prerequisites

Before you begin, ensure you have:

<Note>
**Required OAuth Scopes:**
- `create_payment_links`
- `partner_payment_links`
- `partner_payments`
</Note>

- **Partner OAuth Application** registered with PayU with the above scopes enabled
- **OAuth Credentials:** `client_id` and `client_secret`
- **Merchant Credentials:** `merchant_id` (PayU merchant ID) and `reseller_id` (partner UUID)
- **Callback URLs Ready:**
  - `surl` — Success redirect URL (where PayU sends customers after successful payment)
  - `furl` — Failure redirect URL (where PayU sends customers after failed payment)
  - `curl` — Cancel redirect URL (where PayU sends customers if they cancel payment)
- **Partner Webhook URLs** configured in PayU's system (`partner_webhook_success`, `partner_webhook_failure`, `partner_webhook_cancelled`)
- **Test Environment Access** to `https://test-partnerapilayer.payu.in`

<Warning>
**Important:** All hash computations for partner payments use your OAuth `client_secret`, NOT the merchant salt used in direct merchant integrations.
</Warning>

---

## Step 1: Generate OAuth Access Token

Partner Payments API requires OAuth 2.0 Bearer token authentication.

### Step 1.1: Request Authorization Code

Obtain an authorization code with the required scopes:

**Endpoint:** `POST https://uat-partner.payu.in/api/v1/merchants/auth_code`

**Request:**

```bash
curl --location 'https://uat-partner.payu.in/api/v1/merchants/auth_code' \
--header 'Content-Type: application/json' \
--data '{
  "client_id": "your_client_id",
  "client_secret": "your_client_secret",
  "grant_type": "password",
  "username": "your_merchant_username",
  "password": "your_merchant_password",
  "scope": "create_payment_links partner_payment_links partner_payments"
}'
```

**Response:**

```json
{
  "code": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expires_in": 300
}
```

### Step 1.2: Exchange Authorization Code for Access Token

**Endpoint:** `POST https://uat-accounts.payu.in/oauth/token`

**Request:**

```bash
curl --location 'https://uat-accounts.payu.in/oauth/token' \
--header 'Content-Type: application/json' \
--data '{
  "client_id": "your_client_id",
  "client_secret": "your_client_secret",
  "grant_type": "authorization_code",
  "code": "auth_code_from_previous_step",
  "redirect_uri": "https://yoursite.com/oauth/callback"
}'
```

**Response:**

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "create_payment_links partner_payment_links partner_payments"
}
```

<Info>
**Token Refresh:** OAuth tokens expire after ~1 hour. Implement automatic token refresh logic to avoid integration disruptions.
</Info>

---

## Step 2: Initiate Hosted Checkout Payment

### Step 2.1: Prepare Request Parameters

**Endpoint URLs:**

| Environment | URL |
|-------------|-----|
| Test | `https://test-partnerapilayer.payu.in/apilayer/partner/payments` |
| Production | `https://api.payu.in/partner/payments` |

**HTTP Method:** `POST`

**Headers:**

```
Authorization: Bearer <your_access_token>
Content-Type: application/json
```

**Request Body Parameters:**

#### Mandatory Parameters

<table>
  <thead>
    <tr>
      <th style="text-align:left">Parameter</th>
      <th style="text-align:left">Type &amp; Description</th>
      <th style="text-align:left">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>txnid</td>
      <td><strong>String</strong><br>Unique transaction ID generated by the partner.</td>
      <td>PPHOST20240315001</td>
    </tr>
    <tr>
      <td>amount</td>
      <td><strong>String</strong><br>Transaction amount in decimal format.</td>
      <td>1500.00</td>
    </tr>
    <tr>
      <td>productinfo</td>
      <td><strong>String</strong><br>Product or service description.</td>
      <td>Premium Subscription - Monthly</td>
    </tr>
    <tr>
      <td>phone</td>
      <td><strong>String</strong><br>Customer phone number with country code (10 digits).</td>
      <td>919876543210</td>
    </tr>
    <tr>
      <td>merchant_id</td>
      <td><strong>Integer</strong><br>PayU merchant ID.</td>
      <td>8739528</td>
    </tr>
    <tr>
      <td>reseller_id</td>
      <td><strong>String</strong><br>Partner or reseller UUID.</td>
      <td>11ee-0e7e-5403fde2-9523-0a696b110fde</td>
    </tr>
    <tr>
      <td>surl</td>
      <td><strong>String</strong><br>Success callback URL. Customer is redirected here after successful payment.</td>
      <td>https://yourplatform.com/payment/success</td>
    </tr>
    <tr>
      <td>furl</td>
      <td><strong>String</strong><br>Failure callback URL. Customer is redirected here after failed payment.</td>
      <td>https://yourplatform.com/payment/failure</td>
    </tr>
    <tr>
      <td>curl</td>
      <td><strong>String</strong><br>Cancel callback URL. Customer is redirected here when payment is cancelled.</td>
      <td>https://yourplatform.com/payment/cancel</td>
    </tr>
    <tr>
      <td>hash</td>
      <td><strong>String</strong><br>SHA-512 hash (lowercase hex) used to authenticate the request. Computed as:
      merchant_id|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||client_secret</td>
      <td>—</td>
    </tr>
  </tbody>
</table>

#### Optional Parameters

<table>
  <thead>
    <tr>
      <th style="text-align:left">Parameter</th>
      <th style="text-align:left">Type &amp; Description</th>
      <th style="text-align:left">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>firstname</td>
      <td><strong>String</strong><br>Customer's first name.</td>
      <td>Priya</td>
    </tr>
    <tr>
      <td>lastname</td>
      <td><strong>String</strong><br>Customer's last name.</td>
      <td>Sharma</td>
    </tr>
    <tr>
      <td>email</td>
      <td><strong>String</strong><br>Customer's email address.</td>
      <td>priya.sharma@example.com</td>
    </tr>
    <tr>
      <td>udf1</td>
      <td><strong>String</strong><br>User-defined field 1 for storing custom data.</td>
      <td>subscription_plan_premium</td>
    </tr>
    <tr>
      <td>udf2</td>
      <td><strong>String</strong><br>User-defined field 2 for storing custom data.</td>
      <td>monthly_billing</td>
    </tr>
    <tr>
      <td>udf3</td>
      <td><strong>String</strong><br>User-defined field 3 for storing custom data.</td>
      <td>customer_segment_B</td>
    </tr>
    <tr>
      <td>udf4</td>
      <td><strong>String</strong><br>User-defined field 4 for storing custom data.</td>
      <td>campaign_spring2024</td>
    </tr>
    <tr>
      <td>udf5</td>
      <td><strong>String</strong><br>User-defined field 5, often used for partner or channel ID.</td>
      <td>partner_web_checkout</td>
    </tr>
  </tbody>
</table>

<Warning>
**Hosted Checkout-Specific Notes:**
- **NO** `txn_s2s_flow` parameter — This is for UPI Intent S2S flows only
- **NO** `s2s_client_ip` or `s2s_device_info` — Not required for redirect-based flows
- `surl`, `furl`, and `curl` are **mandatory** — These URLs receive the customer after payment completion
- The `redirectUri` in the response is NOT shareable — It should be used for immediate redirect only
</Warning>

### Step 2.2: Generate Payment Request Hash

The payment request hash authenticates your API call using SHA-512.

**Hash Formula:**

```
merchant_id|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||client_secret
```

<Warning>
**Critical Hash Rules:**
- There are **six consecutive pipes** (`||||||`) between `udf5` and `client_secret`
- Use your OAuth **client_secret** (NOT merchant salt)
- Use empty strings for any missing optional fields (results in consecutive pipes)
- Compute SHA-512 and output as **lowercase hexadecimal**
- Do NOT add a trailing pipe after `client_secret`
</Warning>

**Sample Hash Generation Code:**

**Python:**

```python
import hashlib

def generate_payment_hash(merchant_id, txnid, amount, productinfo, firstname, email, udf1, udf2, udf3, udf4, udf5, client_secret):
    hash_string = f"{merchant_id}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{client_secret}"
    return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()

# Example usage
payment_hash = generate_payment_hash(
    merchant_id=8739528,
    txnid="PPHOST20240315001",
    amount="1500.00",
    productinfo="Premium Subscription - Monthly",
    firstname="Priya",
    email="priya.sharma@example.com",
    udf1="subscription_plan_premium",
    udf2="monthly_billing",
    udf3="",
    udf4="",
    udf5="partner_web_checkout",
    client_secret="your_client_secret_here"
)

print(f"Payment Hash: {payment_hash}")
```

**Java:**

```java
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class HostedCheckoutHashGenerator {
    public static String generateHash(
        int merchantId, String txnid, String amount, String productinfo,
        String firstname, String email, String udf1, String udf2, 
        String udf3, String udf4, String udf5, String clientSecret
    ) throws NoSuchAlgorithmException {
        
        String hashString = merchantId + "|" + txnid + "|" + amount + "|" + 
                          productinfo + "|" + firstname + "|" + email + "|" +
                          udf1 + "|" + udf2 + "|" + udf3 + "|" + udf4 + "|" + 
                          udf5 + "||||||" + clientSecret;
        
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] hashBytes = md.digest(hashString.getBytes());
        
        StringBuilder hexString = new StringBuilder();
        for (byte b : hashBytes) {
            String hex = Integer.toHexString(0xff & b);
            if (hex.length() == 1) hexString.append('0');
            hexString.append(hex);
        }
        
        return hexString.toString();
    }
}
```

**PHP:**

```php
<?php
function generateHostedCheckoutHash($merchantId, $txnid, $amount, $productinfo, 
                                    $firstname, $email, $udf1, $udf2, $udf3, 
                                    $udf4, $udf5, $clientSecret) {
    
    $hashString = $merchantId . "|" . $txnid . "|" . $amount . "|" . 
                  $productinfo . "|" . $firstname . "|" . $email . "|" .
                  $udf1 . "|" . $udf2 . "|" . $udf3 . "|" . $udf4 . "|" . 
                  $udf5 . "||||||" . $clientSecret;
    
    return hash('sha512', $hashString);
}

// Example
$hash = generateHostedCheckoutHash(
    8739528,
    "PPHOST20240315001",
    "1500.00",
    "Premium Subscription - Monthly",
    "Priya",
    "priya.sharma@example.com",
    "subscription_plan_premium",
    "monthly_billing",
    "",
    "",
    "partner_web_checkout",
    "your_client_secret_here"
);

echo "Payment Hash: " . $hash;
?>
```

### Step 2.3: POST the Payment Request

**Sample Request (cURL):**

```bash
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/payments' \
--header 'Authorization: Bearer your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
  "txnid": "PPHOST20240315001",
  "amount": "1500.00",
  "productinfo": "Premium Subscription - Monthly",
  "firstname": "Priya",
  "email": "priya.sharma@example.com",
  "phone": "919876543210",
  "merchant_id": 8739528,
  "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
  "surl": "https://yourplatform.com/payment/success",
  "furl": "https://yourplatform.com/payment/failure",
  "curl": "https://yourplatform.com/payment/cancel",
  "udf1": "subscription_plan_premium",
  "udf2": "monthly_billing",
  "udf5": "partner_web_checkout",
  "hash": "computed_sha512_hash_here"
}'
```

**Sample Request (Python):**

```python
import requests
import json

url = "https://test-partnerapilayer.payu.in/apilayer/partner/payments"

headers = {
    'Authorization': 'Bearer your_access_token_here',
    'Content-Type': 'application/json'
}

payload = {
    "txnid": "PPHOST20240315001",
    "amount": "1500.00",
    "productinfo": "Premium Subscription - Monthly",
    "firstname": "Priya",
    "email": "priya.sharma@example.com",
    "phone": "919876543210",
    "merchant_id": 8739528,
    "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
    "surl": "https://yourplatform.com/payment/success",
    "furl": "https://yourplatform.com/payment/failure",
    "curl": "https://yourplatform.com/payment/cancel",
    "udf1": "subscription_plan_premium",
    "udf2": "monthly_billing",
    "udf5": "partner_web_checkout",
    "hash": "computed_sha512_hash_here"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
```

**Sample Request (Java):**

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class InitiateHostedCheckout {
    public static void main(String[] args) throws Exception {
        String url = "https://test-partnerapilayer.payu.in/apilayer/partner/payments";
        
        String payload = "{\"txnid\":\"PPHOST20240315001\",\"amount\":\"1500.00\",\"productinfo\":\"Premium Subscription - Monthly\",\"firstname\":\"Priya\",\"email\":\"priya.sharma@example.com\",\"phone\":\"919876543210\",\"merchant_id\":8739528,\"reseller_id\":\"11ee-0e7e-5403fde2-9523-0a696b110fde\",\"surl\":\"https://yourplatform.com/payment/success\",\"furl\":\"https://yourplatform.com/payment/failure\",\"curl\":\"https://yourplatform.com/payment/cancel\",\"udf1\":\"subscription_plan_premium\",\"udf2\":\"monthly_billing\",\"udf5\":\"partner_web_checkout\",\"hash\":\"computed_sha512_hash_here\"}";
        
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Authorization", "Bearer your_access_token_here")
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(payload))
            .build();
        
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        
        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```

**Sample Request (PHP):**

```php
<?php
$url = "https://test-partnerapilayer.payu.in/apilayer/partner/payments";

$headers = array(
    'Authorization: Bearer your_access_token_here',
    'Content-Type: application/json'
);

$payload = json_encode(array(
    "txnid" => "PPHOST20240315001",
    "amount" => "1500.00",
    "productinfo" => "Premium Subscription - Monthly",
    "firstname" => "Priya",
    "email" => "priya.sharma@example.com",
    "phone" => "919876543210",
    "merchant_id" => 8739528,
    "reseller_id" => "11ee-0e7e-5403fde2-9523-0a696b110fde",
    "surl" => "https://yourplatform.com/payment/success",
    "furl" => "https://yourplatform.com/payment/failure",
    "curl" => "https://yourplatform.com/payment/cancel",
    "udf1" => "subscription_plan_premium",
    "udf2" => "monthly_billing",
    "udf5" => "partner_web_checkout",
    "hash" => "computed_sha512_hash_here"
));

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
$statusCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

curl_close($ch);

echo "Status Code: " . $statusCode . "\n";
echo "Response: " . $response;
?>
```

### Step 2.4: Handle Payment Response & Redirect Customer

**Success Response:**

```json
{
  "redirectUri": "https://secure.payu.in/_payment?mihpayid=403993715521899234&amount=1500.00&txnid=PPHOST20240315001&key=JPM7Fg&productinfo=Premium+Subscription+-+Monthly&phone=919876543210&firstname=Priya&email=priya.sharma%40example.com&surl=https%3A%2F%2Fyourplatform.com%2Fpayment%2Fsuccess&furl=https%3A%2F%2Fyourplatform.com%2Fpayment%2Ffailure&curl=https%3A%2F%2Fyourplatform.com%2Fpayment%2Fcancel&hash=..."
}
```

**Key Response Field:**

- **redirectUri** — The PayU hosted checkout URL. **Immediately redirect the customer to this URL.**

**Redirect Implementation:**

**Server-side redirect (recommended):**

```python
# Python Flask example
from flask import redirect

@app.route('/checkout', methods=['POST'])
def initiate_checkout():
    # Create payment via Partner API (steps above)
    response = requests.post(payu_url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        redirect_uri = response.json().get('redirectUri')
        return redirect(redirect_uri, code=302)
    else:
        return "Payment initiation failed", 500
```

```php
// PHP redirect
<?php
// Create payment via Partner API
$response = json_decode($apiResponse, true);

if ($response['redirectUri']) {
    header("Location: " . $response['redirectUri']);
    exit();
}
?>
```

**Client-side redirect (JavaScript):**

```javascript
// After receiving API response
fetch('/api/create-payment', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(paymentData)
})
.then(response => response.json())
.then(data => {
    if (data.redirectUri) {
        // Redirect customer to PayU checkout
        window.location.href = data.redirectUri;
    }
});
```

**Customer Experience on Hosted Checkout:**

Once redirected to `redirectUri`, the customer will:

1. **See PayU's hosted checkout page** with:
   - Your merchant branding (logo, colors)
   - Transaction summary (amount, product description)
   - Available payment methods

2. **Select a payment method:**
   - **Credit/Debit Cards** (Visa, Mastercard, Amex, Rupay)
   - **UPI** (Intent or Collect flow)
   - **Net Banking** (50+ banks)
   - **Wallets** (PayU Money, PhonePe, Paytm, etc.)

3. **Complete authentication:**
   - Card: CVV + OTP (3D Secure)
   - UPI: PIN authentication
   - Net Banking: Bank credentials
   - Wallet: Wallet PIN/OTP

4. **Receive outcome:**
   - **Success** → Redirected to `surl`
   - **Failure** → Redirected to `furl`
   - **Cancel** → Redirected to `curl`

<Info>
**Callback URL Best Practices:**
- Always use HTTPS for surl/furl/curl endpoints
- Display clear success/failure messages on callback pages
- Extract transaction details from callback parameters (PayU POSTs data to these URLs)
- Do NOT rely solely on callback parameters — always verify using webhooks and Verify Payment API
</Info>

---

## Step 3: Receive Payment Notification

### Step 3.1: Partner Webhook

After the customer completes payment, PayU sends a webhook notification to your configured partner webhook URL.

**Webhook Configuration:**

Ensure these URLs are configured:
- `partner_webhook_success` — Called on successful payment
- `partner_webhook_failure` — Called on failed payment
- `partner_webhook_cancelled` — Called when payment is cancelled

**Sample Success Webhook Payload:**

```json
{
  "key": "JPM7Fg",
  "txnid": "PPHOST20240315001",
  "mihpayid": "403993715521899234",
  "status": "success",
  "unmappedstatus": "captured",
  "mode": "CC",
  "bankcode": "VISA",
  "amount": "1500.00",
  "productinfo": "Premium Subscription - Monthly",
  "firstname": "Priya",
  "email": "priya.sharma@example.com",
  "phone": "919876543210",
  "udf1": "subscription_plan_premium",
  "udf2": "monthly_billing",
  "udf3": "",
  "udf4": "",
  "udf5": "partner_web_checkout",
  "merchant_id": "8739528",
  "error": "No Error",
  "error_Message": "No Error",
  "hash": "webhook_hash_from_payu"
}
```

**Sample Failure Webhook Payload:**

```json
{
  "key": "JPM7Fg",
  "txnid": "PPHOST20240315001",
  "mihpayid": "403993715521899241",
  "status": "failure",
  "unmappedstatus": "failed",
  "mode": "NB",
  "bankcode": "ICIC",
  "amount": "1500.00",
  "productinfo": "Premium Subscription - Monthly",
  "firstname": "Priya",
  "email": "priya.sharma@example.com",
  "phone": "919876543210",
  "udf1": "subscription_plan_premium",
  "udf2": "monthly_billing",
  "udf3": "",
  "udf4": "",
  "udf5": "partner_web_checkout",
  "merchant_id": "8739528",
  "error": "E000",
  "error_Message": "Payment declined by bank",
  "hash": "webhook_hash_from_payu"
}
```

### Step 3.2: Verify Webhook Hash

**Always verify the webhook hash before processing.**

**Reverse Hash Formula:**

```
client_secret|status|||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|merchant_id
```

<Warning>
**Critical Verification Rules:**
- There are **five consecutive pipes** (`|||||`) between `status` and `udf5`
- Use OAuth **client_secret** (NOT merchant salt)
- Do NOT add a trailing pipe after `merchant_id`
- Compute SHA-512 and compare as **case-insensitive**
- **Reject webhook if hash doesn't match**
</Warning>

**Sample Verification Code:**

**Python:**

```python
import hashlib

def verify_webhook_hash(webhook_payload, client_secret):
    status = webhook_payload.get('status', '')
    udf5 = webhook_payload.get('udf5', '')
    udf4 = webhook_payload.get('udf4', '')
    udf3 = webhook_payload.get('udf3', '')
    udf2 = webhook_payload.get('udf2', '')
    udf1 = webhook_payload.get('udf1', '')
    email = webhook_payload.get('email', '')
    firstname = webhook_payload.get('firstname', '')
    productinfo = webhook_payload.get('productinfo', '')
    amount = webhook_payload.get('amount', '')
    txnid = webhook_payload.get('txnid', '')
    merchant_id = webhook_payload.get('merchant_id', '')
    received_hash = webhook_payload.get('hash', '')
    
    hash_string = f"{client_secret}|{status}|||||{udf5}|{udf4}|{udf3}|{udf2}|{udf1}|{email}|{firstname}|{productinfo}|{amount}|{txnid}|{merchant_id}"
    
    computed_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
    
    return computed_hash.lower() == received_hash.lower()

# Example
is_valid = verify_webhook_hash(webhook_data, "your_client_secret")

if is_valid:
    print("✅ Webhook verified — safe to process")
else:
    print("❌ Invalid webhook hash — reject")
```

**Java:**

```java
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class WebhookVerifier {
    public static boolean verifyHash(
        String status, String udf5, String udf4, String udf3, String udf2, String udf1,
        String email, String firstname, String productinfo, String amount,
        String txnid, String merchantId, String receivedHash, String clientSecret
    ) throws NoSuchAlgorithmException {
        
        String hashString = clientSecret + "|" + status + "|||||" + 
                          udf5 + "|" + udf4 + "|" + udf3 + "|" + udf2 + "|" + udf1 + "|" +
                          email + "|" + firstname + "|" + productinfo + "|" + 
                          amount + "|" + txnid + "|" + merchantId;
        
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] hashBytes = md.digest(hashString.getBytes());
        
        StringBuilder hexString = new StringBuilder();
        for (byte b : hashBytes) {
            String hex = Integer.toHexString(0xff & b);
            if (hex.length() == 1) hexString.append('0');
            hexString.append(hex);
        }
        
        return hexString.toString().equalsIgnoreCase(receivedHash);
    }
}
```

### Step 3.3: Process Webhook

**Python Flask Webhook Handler:**

```python
from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/partner/webhook/success', methods=['POST'])
def handle_success_webhook():
    webhook_data = request.json
    
    # Verify hash
    if not verify_webhook_hash(webhook_data, "your_client_secret"):
        return jsonify({"error": "Invalid hash"}), 400
    
    # Extract details
    txnid = webhook_data.get('txnid')
    mihpayid = webhook_data.get('mihpayid')
    status = webhook_data.get('status')
    mode = webhook_data.get('mode')
    amount = webhook_data.get('amount')
    
    # Update database
    # db.update_payment_status(txnid=txnid, mihpayid=mihpayid, status=status)
    
    print(f"✅ Payment Success: {txnid} | PayU ID: {mihpayid} | Mode: {mode} | Amount: ₹{amount}")
    
    # Respond with 200 OK
    return jsonify({"message": "Webhook received"}), 200

if __name__ == '__main__':
    app.run(port=5000)
```

---

## Step 4: Verify Payment

### Step 4.1: Generate Verify Payment Hash

**Hash Formula:**

```
merchant_id|verify_payment|txnid|client_secret
```

**Python:**

```python
import hashlib

def generate_verify_hash(merchant_id, txnid, client_secret):
    hash_string = f"{merchant_id}|verify_payment|{txnid}|{client_secret}"
    return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()

verify_hash = generate_verify_hash(8739528, "PPHOST20240315001", "your_client_secret")
```

### Step 4.2: Call Verify Payment API

**Endpoint:**

| Environment | URL |
|-------------|-----|
| Test | `https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment` |
| Production | `https://api.payu.in/partner/verifyPayment` |

**Request:**

```bash
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment' \
--header 'Authorization: Bearer your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
  "txnid": "PPHOST20240315001",
  "merchant_id": 8739528,
  "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
  "hash": "computed_verify_hash_here"
}'
```

**Response:**

```json
{
  "status": "success",
  "unmappedstatus": "captured",
  "mihpayid": "403993715521899234",
  "txnid": "PPHOST20240315001",
  "amount": "1500.00",
  "mode": "CC",
  "bankcode": "VISA",
  "productinfo": "Premium Subscription - Monthly",
  "firstname": "Priya",
  "email": "priya.sharma@example.com",
  "phone": "919876543210"
}
```

### Step 4.3: Process Verification Response

**Reconciliation Checklist:**

✅ `mihpayid` matches  
✅ `txnid` matches  
✅ `amount` matches  
✅ `status` is `"success"`  
✅ `unmappedstatus` is `"captured"`

If all match, mark transaction as verified.

---

## Use Cases

Partner Payments Hosted Checkout is ideal for:

### E-commerce Platforms
Multi-merchant marketplaces where sellers need to accept payments. Partner handles checkout integration; merchants just onboard.

### Subscription Services
Recurring billing for SaaS, memberships, content subscriptions. Hosted checkout supports saved cards and automated retries.

### B2B Platforms
Business-to-business transactions requiring invoice payments, procurement orders, vendor settlements.

### Event Ticketing
Concert, sports, conference ticket sales with multiple payment methods and high transaction volumes.

---

## Error Handling

<table>
  <thead>
    <tr>
      <th>Error</th>
      <th>Cause</th>
      <th>Resolution</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>Invalid hash</code></td>
      <td>Hash computation mismatch</td>
      <td>Verify using <code>client_secret</code> (not merchant salt), check 6-pipe sequence, ensure SHA-512 lowercase hex</td>
    </tr>
    <tr>
      <td><code>Invalid access token</code></td>
      <td>OAuth token expired or invalid</td>
      <td>Refresh OAuth token. Implement auto-refresh logic</td>
    </tr>
    <tr>
      <td><code>Transaction not found</code></td>
      <td>txnid doesn't exist in PayU</td>
      <td>Verify txnid matches exactly. Check for typos</td>
    </tr>
    <tr>
      <td><code>Missing webhook URL</code></td>
      <td>Partner webhook URLs not configured</td>
      <td>Contact PayU to configure partner_webhook_success, partner_webhook_failure, partner_webhook_cancelled</td>
    </tr>
    <tr>
      <td><code>HMAC validation failure</code></td>
      <td>Webhook hash verification failed</td>
      <td>Check reverse hash formula (5 pipes after status, no trailing pipe). Use case-insensitive comparison</td>
    </tr>
    <tr>
      <td><code>Unauthorized - 401</code></td>
      <td>Missing/invalid Authorization header</td>
      <td>Ensure <code>Authorization: Bearer &lt;token&gt;</code> in all requests</td>
    </tr>
  </tbody>
</table>

---

## Testing

### Test Environment

**Base URL:** `https://test-partnerapilayer.payu.in/apilayer/partner`

**OAuth URLs:**
- Auth Code: `https://uat-partner.payu.in/api/v1/merchants/auth_code`
- Access Token: `https://uat-accounts.payu.in/oauth/token`

### Test Workflow

1. Generate OAuth access token
2. Create payment request
3. Redirect to hosted checkout (test environment)
4. Complete payment using test card/UPI
5. Verify redirect to surl/furl
6. Confirm webhook received
7. Call Verify Payment API
8. Reconcile all data points

### Validation Checklist

✅ OAuth token generation succeeds  
✅ Payment API returns redirectUri  
✅ Hosted checkout page loads  
✅ Test payment succeeds  
✅ Customer redirected to surl  
✅ Webhook received within 5 seconds  
✅ Webhook hash verified  
✅ Verify Payment API confirms status  
✅ Reconciliation successful

---

## Best Practices

### Security
- ✅ Store `client_secret` securely — Never expose in client-side code
- ✅ Always verify webhook hash before processing
- ✅ Use HTTPS for all callback URLs (surl/furl/curl)
- ✅ Implement rate limiting on webhook endpoints

### Reliability
- ✅ Implement idempotency using `txnid`
- ✅ Use unique `txnid` per transaction — Never reuse
- ✅ Implement retry logic for Verify Payment API
- ✅ Log all API requests/responses for debugging

### Integration
- ✅ Implement OAuth token refresh (tokens expire ~1 hour)
- ✅ Monitor webhook delivery latency
- ✅ Test both success and failure scenarios
- ✅ Handle network timeouts gracefully

### Customer Experience
- ✅ Use descriptive `productinfo` so customers recognize the charge
- ✅ Include customer name and email (improves checkout experience)
- ✅ Provide clear success/failure pages on surl/furl
- ✅ Show payment status in real-time after redirect

---

## Next Steps

- **[Partner Payment UPI Intent Integration](#)** — Direct UPI app invocation
- **[Payment Links for Partners Overview](#)** — Shareable payment links
- **[Verify Payment API Reference](#)** — Complete verification documentation
- **[Partner Webhook Guide](#)** — Advanced webhook patterns

<Success>
**Integration Complete!** You can now accept payments through PayU's hosted checkout using the Partner Payments API.
</Success>

