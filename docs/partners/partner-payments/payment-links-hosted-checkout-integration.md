---
title: Payment Links Hosted Checkout Integration
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
Payment Links Hosted Checkout enables partners to create secure, shareable payment links that redirect customers to PayU's hosted checkout page. Customers can complete payments using multiple payment methods including credit/debit cards, UPI, net banking, and wallets—all within PayU's PCI-compliant checkout interface.

Unlike UPI Intent flows that directly invoke UPI apps, hosted checkout payment links provide a complete payment gateway experience through a web-based interface, making them ideal for:

- **E-commerce checkout** — Send payment links via email or SMS after order confirmation
- **Invoice payments** — Share payment links for bill settlements
- **Remote/contactless payments** — Enable customers to pay without physical interaction
- **Request money scenarios** — Collect payments from customers who don't have your payment integration

This guide covers the complete integration flow using **OAuth 2.0 authentication** and the PayU Partner Payments API.

***

## How It Works

The Payment Links Hosted Checkout flow follows these steps:

1. **OAuth Authentication** — Obtain an access token using your OAuth client credentials with required scopes (`create_payment_links`, `partner_payment_links`, `partner_payments`)

2. **Create Payment Link** — POST a payment request to the Partner Payments API with transaction details, callback URLs, and a computed hash

3. **Receive redirectUri** — PayU returns a hosted checkout URL (`https://secure.payu.in/_payment?...`)

4. **Share Link** — Send the redirectUri to your customer via SMS, WhatsApp, email, or any other channel

5. **Customer Completes Payment** — Customer opens the link, selects a payment method on PayU's hosted page, and completes the transaction

6. **Receive Webhook** — PayU sends a payment notification to your configured partner webhook URL with transaction status and details

7. **Verify Payment** — Call the Verify Payment API to confirm the final transaction status and reconcile

***

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
- **Partner Webhook URLs** configured in PayU's system (`partner_webhook_success`, `partner_webhook_failure`, `partner_webhook_cancelled`)
- **Test Environment Access** to `https://test-partnerapilayer.payu.in`

<Warning>
**Important:** All hash computations for partner payments use your OAuth `client_secret`, NOT the merchant salt used in direct merchant integrations.
</Warning>

***

## Step 1: Generate OAuth Access Token

Partner Payments API requires OAuth 2.0 Bearer token authentication. Follow this two-step process to obtain your access token.

### Step 1.1: Request Authorization Code

First, obtain an authorization code using the password grant type with your merchant credentials:

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

Use the authorization code to obtain your final access token:

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
**Access Token Validity:** OAuth tokens typically expire after 1 hour. Implement token refresh logic to handle expiration gracefully.
</Info>

***

## Step 2: Create Payment Link

### Step 2.1: Prepare Request Parameters

**Endpoint URLs:**

| Environment | URL                                                              |
| ----------- | ---------------------------------------------------------------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer/partner/payments` |
| Production  | `https://api.payu.in/partner/payments`                           |

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
      <td>TXNPL20240315001</td>
    </tr>
    <tr>
      <td>amount</td>
      <td><strong>String</strong><br>Transaction amount in decimal format.</td>
      <td>500.00</td>
    </tr>
    <tr>
      <td>productinfo</td>
      <td><strong>String</strong><br>Product or service description.</td>
      <td>Payment for Order #12345</td>
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
      <td><strong>String</strong><br>Success callback URL redirected to after a successful payment.</td>
      <td>https://yoursite.com/payment/success</td>
    </tr>
    <tr>
      <td>furl</td>
      <td><strong>String</strong><br>Failure callback URL redirected to after a failed payment.</td>
      <td>https://yoursite.com/payment/failure</td>
    </tr>
    <tr>
      <td>curl</td>
      <td><strong>String</strong><br>Cancel callback URL redirected to when a payment is cancelled.</td>
      <td>https://yoursite.com/payment/cancel</td>
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
      <td>John</td>
    </tr>
    <tr>
      <td>lastname</td>
      <td><strong>String</strong><br>Customer's last name.</td>
      <td>Doe</td>
    </tr>
    <tr>
      <td>email</td>
      <td><strong>String</strong><br>Customer's email address.</td>
      <td>john.doe@example.com</td>
    </tr>
    <tr>
      <td>udf1</td>
      <td><strong>String</strong><br>User-defined field 1 for storing custom data.</td>
      <td>—</td>
    </tr>
    <tr>
      <td>udf2</td>
      <td><strong>String</strong><br>User-defined field 2 for storing custom data.</td>
      <td>—</td>
    </tr>
    <tr>
      <td>udf3</td>
      <td><strong>String</strong><br>User-defined field 3 for storing custom data.</td>
      <td>—</td>
    </tr>
    <tr>
      <td>udf4</td>
      <td><strong>String</strong><br>User-defined field 4 for storing custom data.</td>
      <td>—</td>
    </tr>
    <tr>
      <td>udf5</td>
      <td><strong>String</strong><br>User-defined field 5, often used for partner or channel ID.</td>
      <td>—</td>
    </tr>
  </tbody>
</table>

<Warning>
**Important Notes:**
- **NO** `txn_s2s_flow` parameter — this is for UPI Intent S2S flows only
- **NO** `s2s_client_ip` or `s2s_device_info` — not required for hosted checkout redirect flows
- `surl`, `furl`, and `curl` are **mandatory** for redirect-based payment links
</Warning>

### Step 2.2: Generate Payment Request Hash

The payment request hash authenticates your API call. Compute it using SHA-512 with this exact sequence:

**Hash Formula:**

```
merchant_id|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||client_secret
```

<Warning>
**Critical Hash Rules:**
- There are **six consecutive pipes** (`||||||`) between `udf5` and `client_secret`
- Use your OAuth **client_secret** (NOT merchant salt)
- Use empty strings for any missing optional fields (which results in consecutive pipes)
- Compute SHA-512 and output as **lowercase hexadecimal**
- Do NOT add a trailing pipe after `client_secret`
</Warning>

**Sample Hash Generation Code:**

**Python:**

```python
import hashlib

def generate_payment_hash(merchant_id, txnid, amount, productinfo, firstname, email, udf1, udf2, udf3, udf4, udf5, client_secret):
    # Build hash string with exact pipe sequence
    hash_string = f"{merchant_id}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{client_secret}"
    
    # Compute SHA-512 and return lowercase hex
    return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()

# Example usage
payment_hash = generate_payment_hash(
    merchant_id=8739528,
    txnid="TXNPL20240315001",
    amount="500.00",
    productinfo="Payment for Order #12345",
    firstname="John",
    email="john.doe@example.com",
    udf1="",
    udf2="",
    udf3="",
    udf4="",
    udf5="partner_channel_001",
    client_secret="your_client_secret_here"
)

print(f"Payment Hash: {payment_hash}")
```

**Java:**

```java
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class PaymentHashGenerator {
    public static String generatePaymentHash(
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
    
    public static void main(String[] args) throws NoSuchAlgorithmException {
        String hash = generatePaymentHash(
            8739528,
            "TXNPL20240315001",
            "500.00",
            "Payment for Order #12345",
            "John",
            "john.doe@example.com",
            "",
            "",
            "",
            "",
            "partner_channel_001",
            "your_client_secret_here"
        );
        
        System.out.println("Payment Hash: " + hash);
    }
}
```

**PHP:**

```php
<?php
function generatePaymentHash($merchantId, $txnid, $amount, $productinfo, 
                             $firstname, $email, $udf1, $udf2, $udf3, 
                             $udf4, $udf5, $clientSecret) {
    
    $hashString = $merchantId . "|" . $txnid . "|" . $amount . "|" . 
                  $productinfo . "|" . $firstname . "|" . $email . "|" .
                  $udf1 . "|" . $udf2 . "|" . $udf3 . "|" . $udf4 . "|" . 
                  $udf5 . "||||||" . $clientSecret;
    
    return hash('sha512', $hashString);
}

// Example usage
$paymentHash = generatePaymentHash(
    8739528,
    "TXNPL20240315001",
    "500.00",
    "Payment for Order #12345",
    "John",
    "john.doe@example.com",
    "",
    "",
    "",
    "",
    "partner_channel_001",
    "your_client_secret_here"
);

echo "Payment Hash: " . $paymentHash;
?>
```

### Step 2.3: POST the Payment Request

**Sample Request (cURL):**

```bash
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/payments' \
--header 'Authorization: Bearer your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
  "txnid": "TXNPL20240315001",
  "amount": "500.00",
  "productinfo": "Payment for Order #12345",
  "firstname": "John",
  "email": "john.doe@example.com",
  "phone": "919876543210",
  "merchant_id": 8739528,
  "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
  "surl": "https://yoursite.com/payment/success",
  "furl": "https://yoursite.com/payment/failure",
  "curl": "https://yoursite.com/payment/cancel",
  "udf5": "partner_channel_001",
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
    "txnid": "TXNPL20240315001",
    "amount": "500.00",
    "productinfo": "Payment for Order #12345",
    "firstname": "John",
    "email": "john.doe@example.com",
    "phone": "919876543210",
    "merchant_id": 8739528,
    "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
    "surl": "https://yoursite.com/payment/success",
    "furl": "https://yoursite.com/payment/failure",
    "curl": "https://yoursite.com/payment/cancel",
    "udf5": "partner_channel_001",
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

public class CreatePaymentLinkHostedCheckout {
    public static void main(String[] args) throws Exception {
        String url = "https://test-partnerapilayer.payu.in/apilayer/partner/payments";
        
        String payload = "{\"txnid\":\"TXNPL20240315001\",\"amount\":\"500.00\",\"productinfo\":\"Payment for Order #12345\",\"firstname\":\"John\",\"email\":\"john.doe@example.com\",\"phone\":\"919876543210\",\"merchant_id\":8739528,\"reseller_id\":\"11ee-0e7e-5403fde2-9523-0a696b110fde\",\"surl\":\"https://yoursite.com/payment/success\",\"furl\":\"https://yoursite.com/payment/failure\",\"curl\":\"https://yoursite.com/payment/cancel\",\"udf5\":\"partner_channel_001\",\"hash\":\"computed_sha512_hash_here\"}";
        
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
    "txnid" => "TXNPL20240315001",
    "amount" => "500.00",
    "productinfo" => "Payment for Order #12345",
    "firstname" => "John",
    "email" => "john.doe@example.com",
    "phone" => "919876543210",
    "merchant_id" => 8739528,
    "reseller_id" => "11ee-0e7e-5403fde2-9523-0a696b110fde",
    "surl" => "https://yoursite.com/payment/success",
    "furl" => "https://yoursite.com/payment/failure",
    "curl" => "https://yoursite.com/payment/cancel",
    "udf5" => "partner_channel_001",
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

### Step 2.4: Handle Payment Response

**Success Response:**

```json
{
  "redirectUri": "https://secure.payu.in/_payment?mihpayid=403993715521855096&amount=500.00&txnid=TXNPL20240315001&key=JPM7Fg&productinfo=Payment+for+Order+%2312345&phone=919876543210&firstname=John&email=john.doe%40example.com&surl=https%3A%2F%2Fyoursite.com%2Fpayment%2Fsuccess&furl=https%3A%2F%2Fyoursite.com%2Fpayment%2Ffailure&curl=https%3A%2F%2Fyoursite.com%2Fpayment%2Fcancel&udf5=partner_channel_001&hash=..."
}
```

**Key Response Field:**

- **redirectUri** — The complete PayU hosted checkout URL. Share this link with your customer via SMS, WhatsApp, email, or any other channel.

**Customer Experience:**

When the customer opens the `redirectUri`:

1. They are taken to PayU's secure hosted checkout page (`secure.payu.in`)
2. The page displays transaction details (amount, product info, merchant name)
3. Customer selects a payment method:
   - Credit/Debit Cards
   - UPI (Intent or Collect)
   - Net Banking
   - Wallets (PayU Money, PhonePe, etc.)
4. Customer completes authentication (OTP, PIN, biometric)
5. PayU processes the payment and redirects the customer to:
   - `surl` (success callback URL) if payment succeeds
   - `furl` (failure callback URL) if payment fails
   - `curl` (cancel callback URL) if customer cancels

<Info>
**Payment Link Sharing Best Practices:**
- Use URL shorteners for SMS to save character count
- Include context in the message (e.g., "Complete your payment for Order #12345: [link]")
- Set expiry time on your server-side to invalidate old payment links
- Track link opens using UTM parameters or custom analytics
</Info>

***

## Step 3: Receive Payment Notification

### Step 3.1: Partner Webhook

PayU sends payment notifications to your configured partner webhook URLs after the customer completes (or cancels) the payment.

**Webhook Configuration:**

Ensure these webhook URLs are configured in PayU's system:

- `partner_webhook_success` — Called on successful payment
- `partner_webhook_failure` — Called on failed payment
- `partner_webhook_cancelled` — Called when payment is cancelled

**Sample Success Webhook Payload:**

```json
{
  "key": "JPM7Fg",
  "txnid": "TXNPL20240315001",
  "mihpayid": "403993715521855096",
  "status": "success",
  "unmappedstatus": "captured",
  "mode": "CC",
  "bankcode": "VISA",
  "amount": "500.00",
  "productinfo": "Payment for Order #12345",
  "firstname": "John",
  "email": "john.doe@example.com",
  "phone": "919876543210",
  "udf1": "",
  "udf2": "",
  "udf3": "",
  "udf4": "",
  "udf5": "partner_channel_001",
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
  "txnid": "TXNPL20240315001",
  "mihpayid": "403993715521855103",
  "status": "failure",
  "unmappedstatus": "failed",
  "mode": "CC",
  "bankcode": "VISA",
  "amount": "500.00",
  "productinfo": "Payment for Order #12345",
  "firstname": "John",
  "email": "john.doe@example.com",
  "phone": "919876543210",
  "udf1": "",
  "udf2": "",
  "udf3": "",
  "udf4": "",
  "udf5": "partner_channel_001",
  "merchant_id": "8739528",
  "error": "E000",
  "error_Message": "Transaction declined by bank",
  "hash": "webhook_hash_from_payu"
}
```

### Step 3.2: Verify Webhook Hash

**Always verify the webhook hash before processing the payment notification.** This ensures the webhook originated from PayU and hasn't been tampered with.

**Reverse Hash Formula:**

```
client_secret|status|||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|merchant_id
```

<Warning>
**Critical Verification Rules:**
- There are **five consecutive pipes** (`|||||`) between `status` and `udf5`
- Use your OAuth **client_secret** (NOT merchant salt)
- Do NOT add a trailing pipe after `merchant_id`
- Compute SHA-512 and compare as **case-insensitive** (lowercase both hashes before comparing)
- **Reject the webhook if the hash doesn't match**
</Warning>

**Sample Webhook Verification Code:**

**Python:**

```python
import hashlib

def verify_webhook_hash(webhook_payload, client_secret):
    # Extract fields from webhook
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
    
    # Build reverse hash string
    hash_string = f"{client_secret}|{status}|||||{udf5}|{udf4}|{udf3}|{udf2}|{udf1}|{email}|{firstname}|{productinfo}|{amount}|{txnid}|{merchant_id}"
    
    # Compute SHA-512
    computed_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
    
    # Compare (case-insensitive)
    return computed_hash.lower() == received_hash.lower()

# Example usage
webhook_data = {
    "status": "success",
    "udf5": "partner_channel_001",
    "udf4": "",
    "udf3": "",
    "udf2": "",
    "udf1": "",
    "email": "john.doe@example.com",
    "firstname": "John",
    "productinfo": "Payment for Order #12345",
    "amount": "500.00",
    "txnid": "TXNPL20240315001",
    "merchant_id": "8739528",
    "hash": "hash_from_webhook"
}

is_valid = verify_webhook_hash(webhook_data, "your_client_secret_here")

if is_valid:
    print("✅ Webhook hash verified — safe to process")
else:
    print("❌ Invalid webhook hash — reject request")
```

**Java:**

```java
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class WebhookHashVerifier {
    public static boolean verifyWebhookHash(
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
        
        String computedHash = hexString.toString();
        
        return computedHash.equalsIgnoreCase(receivedHash);
    }
    
    public static void main(String[] args) throws NoSuchAlgorithmException {
        boolean isValid = verifyWebhookHash(
            "success",
            "partner_channel_001",
            "",
            "",
            "",
            "",
            "john.doe@example.com",
            "John",
            "Payment for Order #12345",
            "500.00",
            "TXNPL20240315001",
            "8739528",
            "hash_from_webhook",
            "your_client_secret_here"
        );
        
        if (isValid) {
            System.out.println("✅ Webhook hash verified");
        } else {
            System.out.println("❌ Invalid webhook hash");
        }
    }
}
```

### Step 3.3: Process Webhook

After verifying the hash, process the webhook and respond with HTTP 200:

**Python Flask Example:**

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
    
    # Extract transaction details
    txnid = webhook_data.get('txnid')
    mihpayid = webhook_data.get('mihpayid')
    status = webhook_data.get('status')
    amount = webhook_data.get('amount')
    
    # Update your database
    # db.update_transaction(txnid=txnid, mihpayid=mihpayid, status=status)
    
    print(f"✅ Payment Success: {txnid} | PayU ID: {mihpayid} | Amount: {amount}")
    
    # Respond with 200 OK
    return jsonify({"message": "Webhook received"}), 200

if __name__ == '__main__':
    app.run(port=5000)
```

<Warning>
**Important Webhook Handling Rules:**
- Always verify the hash before processing
- Respond with HTTP 200 even if hash verification fails (but don't process the payment)
- Implement idempotency checks using `txnid` to avoid duplicate processing
- Log all webhook payloads for debugging and reconciliation
</Warning>

***

## Step 4: Verify Payment

After receiving the webhook, call the Verify Payment API to confirm the final transaction status. This adds an additional layer of security and ensures you have the most up-to-date payment status.

### Step 4.1: Generate Verify Payment Hash

**Verify Payment Hash Formula:**

```
merchant_id|verify_payment|txnid|client_secret
```

**Sample Code:**

**Python:**

```python
import hashlib

def generate_verify_hash(merchant_id, txnid, client_secret):
    hash_string = f"{merchant_id}|verify_payment|{txnid}|{client_secret}"
    return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()

verify_hash = generate_verify_hash(8739528, "TXNPL20240315001", "your_client_secret")
print(f"Verify Hash: {verify_hash}")
```

**Java:**

```java
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class VerifyHashGenerator {
    public static String generateVerifyHash(int merchantId, String txnid, String clientSecret) 
        throws NoSuchAlgorithmException {
        
        String hashString = merchantId + "|verify_payment|" + txnid + "|" + clientSecret;
        
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

### Step 4.2: Call Verify Payment API

**Endpoint URLs:**

| Environment | URL                                                                   |
| ----------- | --------------------------------------------------------------------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment` |
| Production  | `https://api.payu.in/partner/verifyPayment`                           |

**Request:**

```bash
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment' \
--header 'Authorization: Bearer your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
  "txnid": "TXNPL20240315001",
  "merchant_id": 8739528,
  "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
  "hash": "computed_verify_hash_here"
}'
```

**Python:**

```python
import requests
import json

url = "https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment"

headers = {
    'Authorization': 'Bearer your_access_token_here',
    'Content-Type': 'application/json'
}

payload = {
    "txnid": "TXNPL20240315001",
    "merchant_id": 8739528,
    "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
    "hash": "computed_verify_hash_here"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
```

**Verification Response:**

```json
{
  "status": "success",
  "unmappedstatus": "captured",
  "mihpayid": "403993715521855096",
  "txnid": "TXNPL20240315001",
  "amount": "500.00",
  "mode": "CC",
  "bankcode": "VISA",
  "productinfo": "Payment for Order #12345",
  "firstname": "John",
  "email": "john.doe@example.com",
  "phone": "919876543210"
}
```

### Step 4.3: Process Verification Response

**Reconciliation Checklist:**

Compare the webhook payload with the verification response:

✅ `mihpayid` matches<br />✅ `txnid` matches<br />✅ `amount` matches<br />✅ `status` matches<br />✅ `unmappedstatus` is `captured` (for success)

If all checks pass, mark the transaction as verified and complete in your system.

<Info>
**Best Practice:** Always treat the Verify Payment API response as the source of truth, especially if there's a discrepancy between the webhook and verification response.
</Info>

***

## Use Cases

Payment Links Hosted Checkout is ideal for:

### E-commerce Checkout

Send payment links after order confirmation for customers who prefer not to enter card details directly on your site.

### Invoice Payments

Generate payment links for invoices and share them with customers via email. Track payment status in real-time.

### Remote/Contactless Payments

Enable customers to pay remotely without any physical interaction, ideal for service businesses, donations, and B2B transactions.

### Request Money Scenarios

Send payment requests to individuals or businesses who need to pay you but don't have access to your payment integration.

***

## Error Handling

| Error                                | Cause                                   | Resolution                                                                                                                                                                  |
| ------------------------------------ | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <code>Invalid hash</code>            | Hash computation mismatch               | Verify you're using <code>client_secret</code> (not merchant salt), check pipe sequence (6 pipes between udf5 and client_secret), ensure SHA-512 lowercase hex output       |
| <code>Invalid access token</code>    | OAuth token expired or invalid          | Refresh your OAuth token. Tokens typically expire after 1 hour. Implement automatic refresh logic                                                                           |
| <code>Transaction not found</code>   | txnid doesn't exist in PayU's system    | Verify the txnid in your verify payment request matches the one used during payment creation. Check for typos                                                               |
| <code>Missing webhook URL</code>     | Partner webhook URLs not configured     | Contact PayU integration team to configure <code>partner_webhook_success</code>, <code>partner_webhook_failure</code>, and <code>partner_webhook_cancelled</code> endpoints |
| <code>HMAC validation failure</code> | Webhook hash verification failed        | Check reverse hash formula (5 pipes after status, no trailing pipe). Ensure case-insensitive comparison. Verify you're using client_secret                                  |
| <code>Unauthorized - 401</code>      | Missing or invalid Authorization header | Ensure you're sending <code>Authorization: Bearer &lt;access_token&gt;</code> in all API requests. Verify the token hasn't expired                                          |

***

## Testing

### Test Environment

**Base URL:** `https://test-partnerapilayer.payu.in/apilayer/partner`

**OAuth URLs:**

- Authorization Code: `https://uat-partner.payu.in/api/v1/merchants/auth_code`
- Access Token: `https://uat-accounts.payu.in/oauth/token`

### Test Workflow

1. **Obtain test OAuth credentials** from PayU integration team
2. **Generate access token** using test client_id and client_secret
3. **Create a test payment link** with a test merchant_id
4. **Open the redirectUri** in a browser
5. **Complete payment** using test card details (provided by PayU)
6. **Verify webhook** is received at your test webhook URL
7. **Call Verify Payment API** to confirm final status
8. **Reconcile** webhook vs verify response

### Validation Checklist

✅ OAuth token generation succeeds<br />✅ Payment link creation returns valid redirectUri<br />✅ Hosted checkout page loads correctly<br />✅ Test payment completes successfully<br />✅ Webhook is received within 5 seconds<br />✅ Webhook hash verification passes<br />✅ Verify Payment API returns matching status<br />✅ Reconciliation logic works correctly

<Warning>
**Production Credentials:** Contact PayU for production OAuth URLs and credentials. Never use test credentials in production.
</Warning>

***

## Best Practices

### Security

- ✅ **Store client_secret securely** — Never commit to version control or expose in client-side code
- ✅ **Always verify webhook hash** before processing payment notifications
- ✅ **Use HTTPS** for all webhook endpoints
- ✅ **Implement rate limiting** on webhook endpoints to prevent abuse

### Reliability

- ✅ **Implement idempotency** using txnid to prevent duplicate processing
- ✅ **Use unique txnid per transaction** — Never reuse transaction IDs
- ✅ **Set payment link expiry** on your server to invalidate old links
- ✅ **Implement retry logic** for verify payment API calls

### Integration

- ✅ **Implement token refresh logic** — OAuth tokens expire after \~1 hour
- ✅ **Log all API requests/responses** for debugging and audit trails
- ✅ **Monitor webhook delivery** — Set up alerts if webhooks aren't received within expected timeframes
- ✅ **Test both success and failure scenarios** thoroughly before going live

### Customer Experience

- ✅ **Use descriptive productinfo** so customers recognize the charge
- ✅ **Include customer name and email** even though optional — improves checkout experience
- ✅ **Provide clear surl/furl pages** with next steps after payment
- ✅ **Send payment link with context** (e.g., "Complete payment for Order #12345")

***

## Next Steps

Now that you've integrated Payment Links Hosted Checkout, explore related payment flows:

- **[Partner Payment UPI Intent Integration](#)** — Direct UPI app invocation for instant payments
- **[Payment Links UPI TPV Integration](#)** — Third-party verification for secure beneficiary validation
- **[Verify Payment API Reference](#)** — Detailed API documentation for payment verification
- **[Partner Payments Webhook Guide](#)** — Comprehensive webhook handling patterns

<Success>
**Integration Complete!** You're now ready to create and manage hosted checkout payment links using PayU's Partner Payments API.
</Success>
