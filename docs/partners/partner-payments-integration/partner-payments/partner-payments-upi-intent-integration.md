---
title: Partner Payments UPI Intent Integration
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
Partner Payment UPI Intent enables partners to initiate UPI payments through a server-to-server (S2S) flow that directly invokes UPI apps on the customer's mobile device. Unlike hosted checkout flows that redirect customers to a web page, UPI Intent provides a seamless, native mobile payment experience.

When you initiate a UPI Intent payment, PayU returns an `intentURIData` string that contains pre-filled UPI payment details. Your mobile application uses this data to launch the customer's preferred UPI app (Google Pay, PhonePe, BHIM, Paytm, etc.) with transaction details already populated. The customer simply authenticates using their UPI PIN, and the payment is complete.

**Key Benefits:**

- **Native mobile experience** — Payments happen within UPI apps customers already trust
- **Faster checkout** — No form filling, no card details entry
- **Higher success rates** — Reduced friction leads to better conversion
- **Real-time confirmation** — Instant payment status updates via webhooks

This integration is ideal for:

- **Mobile-first applications** with high UPI payment volume
- **Quick checkout flows** for ride-hailing, food delivery, e-commerce apps
- **In-app purchases** requiring seamless payment experiences
- **QR code alternatives** for merchant-initiated UPI flows

***

## How It Works

The Partner Payment UPI Intent flow follows these steps:

1. **OAuth Authentication** — Obtain an access token with scope: `hub_session`

2. **Initiate UPI Intent Payment** — POST a payment request with `txn_s2s_flow=4` and customer device details (`s2s_client_ip`, `s2s_device_info`)

3. **Receive intentURIData** — PayU returns a UPI deep link string with pre-filled payment parameters

4. **Invoke UPI App** — Use the intentURIData to launch the customer's UPI app on their mobile device

5. **Customer Authenticates** — Customer enters their UPI PIN in the UPI app to authorize payment

6. **Receive Webhook** — PayU sends payment status notification to your configured webhook URL

7. **Verify Payment** — Call the Verify Payment API to confirm final transaction status

***

## Prerequisites

Before you begin, ensure you have:

- **Partner OAuth Application** registered with PayU with the above scopes enabled
- **OAuth Credentials:** `client_id` and `client_secret`
- **Merchant Credentials:** `merchant_id` (PayU merchant ID) and `reseller_id` (partner UUID)
- **S2S Flow Enabled** — Your account must be enabled for `txn_s2s_flow=4` (contact PayU if not enabled)
- **Partner Webhook URLs** configured (`partner_webhook_success`, `partner_webhook_failure`, `partner_webhook_cancelled`)
- **Ability to Capture:**
  - Customer IP address (`s2s_client_ip`)
  - Device user-agent string (`s2s_device_info`)
- **Test Environment Access** to `https://test-partnerapilayer.payu.in`

<Warning>
**Critical Requirements for UPI Intent:**
- `txn_s2s_flow` MUST be set to `"4"`
- `s2s_client_ip` and `s2s_device_info` are **mandatory** when txn_s2s_flow=4
- All hash computations use OAuth `client_secret` (NOT merchant salt)
</Warning>

***

## Step 1: Generate OAuth Access Token

Partner Payments API requires a 3-step OAuth 2.0 authentication flow to obtain the final Bearer token.

<Warning>
**Important Differences from Direct Merchant Integration:**
- Partner Payments uses a **3-step OAuth flow** (reseller password grant → merchant auth code → final token)
- First token uses `scope=hub_session`, merchant auth code uses `scopes=create_payment_links partner_payment_links partner_payments`
- Content-Type is `application/x-www-form-urlencoded` (not `application/json`)
- Authorization code request requires the reseller's initial access token
</Warning>

### Step 1.1: Obtain Initial Access Token (Reseller Password Grant)

The first step obtains an access token using your reseller credentials with the `hub_session` scope.

**Endpoint:** `POST https://uat-accounts.payu.in/oauth/token`

**Headers:**

```
Content-Type: application/x-www-form-urlencoded
```

**Request:**

```bash
curl --location 'https://uat-accounts.payu.in/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=your_client_id' \
--data-urlencode 'client_secret=your_client_secret' \
--data-urlencode 'grant_type=password' \
--data-urlencode 'username=your_reseller_username' \
--data-urlencode 'password=your_reseller_password' \
--data-urlencode 'scope=hub_session'
```

```python
import requests

url = "https://uat-accounts.payu.in/oauth/token"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

payload = {
    "client_id": "your_client_id",
    "client_secret": "your_client_secret",
    "grant_type": "password",
    "username": "your_reseller_username",
    "password": "your_reseller_password",
    "scope": "hub_session"
}

response = requests.post(url, headers=headers, data=payload)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")

# Extract access token for Step 1.2
if response.status_code == 200:
    initial_access_token = response.json()["access_token"]
    print(f"
Initial Access Token: {initial_access_token}")
```

```java
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;

public class Step1_ObtainInitialToken {
    public static void main(String[] args) throws Exception {
        String url = "https://uat-accounts.payu.in/oauth/token";
        
        // Build form-encoded body
        String formBody = "client_id=" + URLEncoder.encode("your_client_id", StandardCharsets.UTF_8) +
                         "&client_secret=" + URLEncoder.encode("your_client_secret", StandardCharsets.UTF_8) +
                         "&grant_type=password" +
                         "&username=" + URLEncoder.encode("your_reseller_username", StandardCharsets.UTF_8) +
                         "&password=" + URLEncoder.encode("your_reseller_password", StandardCharsets.UTF_8) +
                         "&scope=hub_session";
        
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(formBody))
            .build();
        
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        
        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response: " + response.body());
        
        // Extract access_token (use a JSON library like Gson in production)
        if (response.statusCode() == 200) {
            String responseBody = response.body();
            String accessToken = responseBody.split("\"access_token\":\"")[1].split("\"")[0];
            System.out.println("
Initial Access Token: " + accessToken);
        }
    }
}
```

```php
<?php
$url = "https://uat-accounts.payu.in/oauth/token";

$headers = array(
    "Content-Type: application/x-www-form-urlencoded"
);

$payload = http_build_query(array(
    "client_id" => "your_client_id",
    "client_secret" => "your_client_secret",
    "grant_type" => "password",
    "username" => "your_reseller_username",
    "password" => "your_reseller_password",
    "scope" => "hub_session"
));

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
$statusCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

if (curl_errno($ch)) {
    echo "Error: " . curl_error($ch);
} else {
    echo "Status Code: " . $statusCode . "
";
    echo "Response: " . $response . "
";
    
    // Extract access token for Step 1.2
    if ($statusCode == 200) {
        $responseData = json_decode($response, true);
        $initialAccessToken = $responseData["access_token"];
        echo "
Initial Access Token: " . $initialAccessToken;
    }
}

curl_close($ch);
?>
```

**Response:**

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "hub_session"
}
```

<Info>
**Note:** Save the `access_token` from this response. You'll need it in Step 1.2 to request the merchant authorization code.
</Info>

### Step 1.2: Request Merchant Authorization Code

Use the access token from Step 1.1 to request an authorization code for the specific merchant.

**Endpoint:** `POST https://uat-partner.payu.in/api/v1/merchants/auth_code`

**Headers:**

```
Authorization: Bearer <access_token_from_step_1.1>
Content-Type: application/x-www-form-urlencoded
```

**Request:**

```bash
curl --location 'https://uat-partner.payu.in/api/v1/merchants/auth_code' \
--header 'Authorization: Bearer access_token_from_step_1.1' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'merchant_id=8739528' \
--data-urlencode 'reseller_uuid=11ee-0e7e-5403fde2-9523-0a696b110fde' \
--data-urlencode 'redirect_uri=https://uat-partner.payu.in' \
--data-urlencode 'scopes=create_payment_links partner_payment_links partner_payments'
```

```python
import requests

url = "https://uat-partner.payu.in/api/v1/merchants/auth_code"

headers = {
    "Authorization": f"Bearer {initial_access_token}",  # From Step 1.1
    "Content-Type": "application/x-www-form-urlencoded"
}

payload = {
    "merchant_id": "8739528",
    "reseller_uuid": "11ee-0e7e-5403fde2-9523-0a696b110fde",
    "redirect_uri": "https://uat-partner.payu.in",
    "scopes": "create_payment_links partner_payment_links partner_payments"
}

response = requests.post(url, headers=headers, data=payload)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")

# Extract authorization code for Step 1.3
if response.status_code == 200:
    authorization_code = response.json()["code"]
    print(f"
Authorization Code: {authorization_code}")
```

```java
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;

public class Step2_RequestAuthCode {
    public static void main(String[] args) throws Exception {
        String url = "https://uat-partner.payu.in/api/v1/merchants/auth_code";
        String initialAccessToken = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."; // From Step 1.1
        
        // Build form-encoded body
        String formBody = "merchant_id=8739528" +
                         "&reseller_uuid=" + URLEncoder.encode("11ee-0e7e-5403fde2-9523-0a696b110fde", StandardCharsets.UTF_8) +
                         "&redirect_uri=" + URLEncoder.encode("https://uat-partner.payu.in", StandardCharsets.UTF_8) +
                         "&scopes=" + URLEncoder.encode("create_payment_links partner_payment_links partner_payments", StandardCharsets.UTF_8);
        
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Authorization", "Bearer " + initialAccessToken)
            .header("Content-Type", "application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(formBody))
            .build();
        
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        
        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response: " + response.body());
        
        // Extract authorization code
        if (response.statusCode() == 200) {
            String responseBody = response.body();
            String authCode = responseBody.split("\"code\":\"")[1].split("\"")[0];
            System.out.println("
Authorization Code: " + authCode);
        }
    }
}
```

```php
<?php
$url = "https://uat-partner.payu.in/api/v1/merchants/auth_code";
$initialAccessToken = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."; // From Step 1.1

$headers = array(
    "Authorization: Bearer " . $initialAccessToken,
    "Content-Type: application/x-www-form-urlencoded"
);

$payload = http_build_query(array(
    "merchant_id" => "8739528",
    "reseller_uuid" => "11ee-0e7e-5403fde2-9523-0a696b110fde",
    "redirect_uri" => "https://uat-partner.payu.in",
    "scopes" => "create_payment_links partner_payment_links partner_payments"
));

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
$statusCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

if (curl_errno($ch)) {
    echo "Error: " . curl_error($ch);
} else {
    echo "Status Code: " . $statusCode . "
";
    echo "Response: " . $response . "
";
    
    // Extract authorization code for Step 1.3
    if ($statusCode == 200) {
        $responseData = json_decode($response, true);
        $authorizationCode = $responseData["code"];
        echo "
Authorization Code: " . $authorizationCode;
    }
}

curl_close($ch);
?>
```

**Response:**

```json
{
  "code": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expires_in": 300
}
```

<Warning>
**Critical Scope Parameter:**
The `scopes` parameter must include all three scopes for Partner Payments:
- `create_payment_links` — Create payment links
- `partner_payment_links` — Manage partner payment links
- `partner_payments` — **Required for payment initiation and verification APIs**

Format: `scopes=create_payment_links partner_payment_links partner_payments` (space-separated, no commas)
</Warning>

### Step 1.3: Exchange Authorization Code for Final Access Token

Exchange the authorization code from Step 1.2 for the final access token you'll use for all Partner Payments API calls.

**Endpoint:** `POST https://uat-accounts.payu.in/oauth/token`

**Headers:**

```
Content-Type: application/x-www-form-urlencoded
```

**Request:**

```bash
curl --location 'https://uat-accounts.payu.in/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=your_client_id' \
--data-urlencode 'client_secret=your_client_secret' \
--data-urlencode 'grant_type=authorization_code' \
--data-urlencode 'code=authorization_code_from_step_1.2' \
--data-urlencode 'redirect_uri=https://uat-partner.payu.in'
```

```python
import requests

url = "https://uat-accounts.payu.in/oauth/token"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

payload = {
    "client_id": "your_client_id",
    "client_secret": "your_client_secret",
    "grant_type": "authorization_code",
    "code": authorization_code,  # From Step 1.2
    "redirect_uri": "https://uat-partner.payu.in"
}

response = requests.post(url, headers=headers, data=payload)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")

# Extract final access token
if response.status_code == 200:
    final_access_token = response.json()["access_token"]
    print(f"
✅ Final Access Token (use for all API calls): {final_access_token}")
```

```java
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;

public class Step3_ExchangeForFinalToken {
    public static void main(String[] args) throws Exception {
        String url = "https://uat-accounts.payu.in/oauth/token";
        String authorizationCode = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."; // From Step 1.2
        
        // Build form-encoded body
        String formBody = "client_id=" + URLEncoder.encode("your_client_id", StandardCharsets.UTF_8) +
                         "&client_secret=" + URLEncoder.encode("your_client_secret", StandardCharsets.UTF_8) +
                         "&grant_type=authorization_code" +
                         "&code=" + URLEncoder.encode(authorizationCode, StandardCharsets.UTF_8) +
                         "&redirect_uri=" + URLEncoder.encode("https://uat-partner.payu.in", StandardCharsets.UTF_8);
        
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(formBody))
            .build();
        
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        
        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response: " + response.body());
        
        // Extract final access token
        if (response.statusCode() == 200) {
            String responseBody = response.body();
            String finalAccessToken = responseBody.split("\"access_token\":\"")[1].split("\"")[0];
            System.out.println("
✅ Final Access Token: " + finalAccessToken);
        }
    }
}
```

```php
<?php
$url = "https://uat-accounts.payu.in/oauth/token";
$authorizationCode = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."; // From Step 1.2

$headers = array(
    "Content-Type: application/x-www-form-urlencoded"
);

$payload = http_build_query(array(
    "client_id" => "your_client_id",
    "client_secret" => "your_client_secret",
    "grant_type" => "authorization_code",
    "code" => $authorizationCode,
    "redirect_uri" => "https://uat-partner.payu.in"
));

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
$statusCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

if (curl_errno($ch)) {
    echo "Error: " . curl_error($ch);
} else {
    echo "Status Code: " . $statusCode . "
";
    echo "Response: " . $response . "
";
    
    // Extract final access token
    if ($statusCode == 200) {
        $responseData = json_decode($response, true);
        $finalAccessToken = $responseData["access_token"];
        echo "
✅ Final Access Token (use for all API calls): " . $finalAccessToken;
    }
}

curl_close($ch);
?>
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

<Success>
**OAuth Flow Complete!** Use the `access_token` from this response as your Bearer token for all Partner Payments API calls:

```
Authorization: Bearer <final_access_token>
```
</Success>

<Info>
**Token Management Best Practices:**
- Store the final access token securely (encrypted database, secure environment variables)
- Monitor token expiry (typically 3600 seconds = 1 hour)
- Implement automatic token refresh before expiry
- Never expose tokens in client-side code or logs
</Info>

## Step 2: Initiate UPI Intent Payment

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

| Parameter       | Type & Description                                                                                                                                                                                                                          | Example                              |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| txnid           | <strong>string</strong> - Unique transaction ID generated by the partner.                                                                                                                                                                   | UPIINT20240315001                    |
| amount          | <strong>string</strong> - Transaction amount in decimal format.                                                                                                                                                                             | 500.00                               |
| productinfo     | <strong>string</strong> - Product or service description.                                                                                                                                                                                   | UPI Payment for Order #12345         |
| phone           | <strong>string</strong> - Customer phone number with country code (10 digits).                                                                                                                                                              | 919876543210                         |
| merchant_id     | <strong>integer</strong> - PayU merchant ID.                                                                                                                                                                                                | 8739528                              |
| reseller_id     | <strong>string</strong> - Partner/reseller UUID.                                                                                                                                                                                            | 11ee-0e7e-5403fde2-9523-0a696b110fde |
| txn_s2s_flow    | <strong>string</strong> - Server-to-server flow identifier. Must be <code>4</code> for UPI Intent.                                                                                                                                          | 4                                    |
| s2s_client_ip   | <strong>string</strong> - Customer's IP address.                                                                                                                                                                                            | 157.240.22.9                         |
| s2s_device_info | <strong>string</strong> - Customer's device user-agent string.                                                                                                                                                                              | Mozilla/5.0 (Linux; Android 10)      |
| hash            | <strong>string</strong> - SHA-512 hash for request authentication, encoded as a lowercase hex string. Computed as SHA-512(merchant_id\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|client_secret) | a3f7c92e1b...                        |

#### Optional Parameters

| Parameter | Type & Description                                                                    | Example                                         |
| --------- | ------------------------------------------------------------------------------------- | ----------------------------------------------- |
| firstname | <strong>string</strong> - Customer's first name.                                      | Rajesh                                          |
| email     | <strong>string</strong> - Customer's email address.                                   | [rajesh@example.com](mailto:rajesh@example.com) |
| udf1      | <strong>string</strong> - User-defined field 1 for custom data.                       | custom_value_1                                  |
| udf2      | <strong>string</strong> - User-defined field 2 for custom data.                       | custom_value_2                                  |
| udf3      | <strong>string</strong> - User-defined field 3 for custom data.                       | custom_value_3                                  |
| udf4      | <strong>string</strong> - User-defined field 4 for custom data.                       | custom_value_4                                  |
| udf5      | <strong>string</strong> - User-defined field 5, often used for partner or channel ID. | partner_channel_001                             |

<Warning>
**UPI Intent-Specific Requirements:**
- `txn_s2s_flow` MUST be set to `"4"` — This activates the UPI Intent S2S flow
- `s2s_client_ip` is **mandatory** — Use the actual customer IP (check `X-Forwarded-For` header if behind a proxy)
- `s2s_device_info` is **mandatory** — Capture the real device user-agent string from the HTTP request
- Do NOT include `surl`, `furl`, `curl` — These redirect URLs are not used in S2S flows
</Warning>

### Step 2.2: Generate Payment Request Hash

**Hash Formula:**

```
merchant_id|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||client_secret
```

<Warning>
**Critical Hash Rules:**
- There are **six consecutive pipes** (`||||||`) between `udf5` and `client_secret`
- Use your OAuth **client_secret** (NOT merchant salt)
- Use empty strings for missing optional fields
- Compute SHA-512 and output as **lowercase hexadecimal**
- Do NOT add a trailing pipe after `client_secret`
</Warning>

**Sample Hash Generation Code:**

**Python:**

```python
import hashlib

def generate_upi_intent_hash(merchant_id, txnid, amount, productinfo, firstname, email, udf1, udf2, udf3, udf4, udf5, client_secret):
    hash_string = f"{merchant_id}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{client_secret}"
    return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()

# Example
payment_hash = generate_upi_intent_hash(
    merchant_id=8739528,
    txnid="UPIINT20240315001",
    amount="500.00",
    productinfo="UPI Payment for Order #12345",
    firstname="Rajesh",
    email="rajesh@example.com",
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

public class UPIIntentHashGenerator {
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
function generateUPIIntentHash($merchantId, $txnid, $amount, $productinfo, 
                               $firstname, $email, $udf1, $udf2, $udf3, 
                               $udf4, $udf5, $clientSecret) {
    
    $hashString = $merchantId . "|" . $txnid . "|" . $amount . "|" . 
                  $productinfo . "|" . $firstname . "|" . $email . "|" .
                  $udf1 . "|" . $udf2 . "|" . $udf3 . "|" . $udf4 . "|" . 
                  $udf5 . "||||||" . $clientSecret;
    
    return hash('sha512', $hashString);
}

$hash = generateUPIIntentHash(
    8739528,
    "UPIINT20240315001",
    "500.00",
    "UPI Payment for Order #12345",
    "Rajesh",
    "rajesh@example.com",
    "",
    "",
    "",
    "",
    "partner_channel_001",
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
  "txnid": "UPIINT20240315001",
  "amount": "500.00",
  "productinfo": "UPI Payment for Order #12345",
  "firstname": "Rajesh",
  "email": "rajesh@example.com",
  "phone": "919876543210",
  "merchant_id": 8739528,
  "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
  "txn_s2s_flow": "4",
  "s2s_client_ip": "157.240.22.9",
  "s2s_device_info": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36",
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
    "txnid": "UPIINT20240315001",
    "amount": "500.00",
    "productinfo": "UPI Payment for Order #12345",
    "firstname": "Rajesh",
    "email": "rajesh@example.com",
    "phone": "919876543210",
    "merchant_id": 8739528,
    "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
    "txn_s2s_flow": "4",
    "s2s_client_ip": "157.240.22.9",
    "s2s_device_info": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36",
    "udf5": "partner_channel_001",
    "hash": "computed_sha512_hash_here"
}

try:
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {str(e)}")
```

**Sample Request (Java):**

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class CreateUPIIntentPayment {
    public static void main(String[] args) throws Exception {
        String url = "https://test-partnerapilayer.payu.in/apilayer/partner/payments";
        
        String payload = "{\"txnid\":\"UPIINT20240315001\",\"amount\":\"500.00\",\"productinfo\":\"UPI Payment for Order #12345\",\"firstname\":\"Rajesh\",\"email\":\"rajesh@example.com\",\"phone\":\"919876543210\",\"merchant_id\":8739528,\"reseller_id\":\"11ee-0e7e-5403fde2-9523-0a696b110fde\",\"txn_s2s_flow\":\"4\",\"s2s_client_ip\":\"157.240.22.9\",\"s2s_device_info\":\"Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36\",\"udf5\":\"partner_channel_001\",\"hash\":\"computed_sha512_hash_here\"}";
        
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
    "txnid" => "UPIINT20240315001",
    "amount" => "500.00",
    "productinfo" => "UPI Payment for Order #12345",
    "firstname" => "Rajesh",
    "email" => "rajesh@example.com",
    "phone" => "919876543210",
    "merchant_id" => 8739528,
    "reseller_id" => "11ee-0e7e-5403fde2-9523-0a696b110fde",
    "txn_s2s_flow" => "4",
    "s2s_client_ip" => "157.240.22.9",
    "s2s_device_info" => "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36",
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
  "metaData": {
    "referenceId": "11ee-0e7e-5403fde2-9523-0a696b110fde",
    "txnId": "UPIINT20240315001",
    "txnStatus": "pending",
    "unmappedStatus": "pending",
    "message": "Transaction initiated successfully",
    "statusCode": "200"
  },
  "result": {
    "paymentId": "30478359672",
    "merchantName": "Your Merchant Name",
    "merchantVpa": "payu@axisbank",
    "amount": "500.00",
    "intentURIData": "pa=payu@axisbank&pn=Your+Merchant+Name&tr=30478359672&tid=UPIINT20240315001&am=500.00&cu=INR&tn=UPIIntent",
    "acsTemplate": null,
    "otpPostUrl": null
  }
}
```

**Key Response Fields:**

| Field                  | Description                                                                       |
| ---------------------- | --------------------------------------------------------------------------------- |
| `metaData.txnStatus`   | Initial status (typically `"pending"` for UPI Intent)                             |
| `result.paymentId`     | PayU's internal payment ID (mihpayid)                                             |
| `result.merchantVpa`   | Merchant's UPI VPA for this transaction                                           |
| `result.intentURIData` | **Critical** — UPI deep link string to invoke UPI apps                            |
| `result.acsTemplate`   | Base64-encoded HTML template (used in some flows, typically null for pure Intent) |
| `result.otpPostUrl`    | OTP submission URL (used in some flows, typically null for pure Intent)           |

<Info>
**Understanding intentURIData:**

The `intentURIData` is a query string containing UPI payment parameters:
- `pa` — Payee address (merchant VPA)
- `pn` — Payee name (merchant name)
- `tr` — Transaction reference (PayU payment ID)
- `tid` — Transaction ID (your txnid)
- `am` — Amount
- `cu` — Currency (INR)
- `tn` — Transaction note

This data is used to construct a UPI deep link that opens the customer's UPI app.
</Info>

**Invoking the UPI App:**

<Warning>
**⚠️ Info Gap: Platform-Specific UPI App Invocation**

The PDF documentation does not include platform-specific code for invoking UPI apps using `intentURIData`. Below is the standard approach, but you should request official code samples from your PayU integration team for production use.
</Warning>

**Android (Intent URI):**

```java
// Construct UPI URI from intentURIData
String intentData = result.getString("intentURIData");
String upiUri = "upi://pay?" + intentData;

// Create Intent
Intent intent = new Intent(Intent.ACTION_VIEW);
intent.setData(Uri.parse(upiUri));

// Check if any UPI app is available
PackageManager packageManager = getPackageManager();
List<ResolveInfo> activities = packageManager.queryIntentActivities(intent, 0);

if (activities.size() > 0) {
    // Launch UPI app
    startActivityForResult(intent, UPI_PAYMENT_REQUEST_CODE);
} else {
    // No UPI app installed
    showError("Please install a UPI app (Google Pay, PhonePe, etc.)");
}
```

**iOS (URL Scheme):**

```swift
// Construct UPI URL from intentURIData
let intentData = result["intentURIData"] as! String
let upiUrlString = "upi://pay?\(intentData)"

if let upiUrl = URL(string: upiUrlString) {
    if UIApplication.shared.canOpenURL(upiUrl) {
        // Launch UPI app
        UIApplication.shared.open(upiUrl, options: [:], completionHandler: nil)
    } else {
        // No UPI app installed
        showError("Please install a UPI app")
    }
}
```

**Web/Mobile Web:**

For mobile web browsers, you can attempt to open the UPI deep link:

```javascript
const intentData = response.result.intentURIData;
const upiUrl = `upi://pay?${intentData}`;

// Attempt to open UPI app
window.location.href = upiUrl;

// Set a timeout to show fallback if app doesn't open
setTimeout(() => {
    // Show QR code or other fallback
}, 3000);
```

<Note>
**Best Practice:** After invoking the UPI app, display a "Waiting for payment confirmation..." screen and listen for the webhook notification to update the payment status in real-time.
</Note>

***

## Step 3: Receive Payment Notification

### Step 3.1: Partner Webhook

After the customer completes (or cancels) the payment in their UPI app, PayU sends a webhook notification to your configured partner webhook URL.

**Webhook Configuration:**

Ensure these URLs are configured in PayU's system:

- `partner_webhook_success` — Called on successful payment
- `partner_webhook_failure` — Called on failed payment
- `partner_webhook_cancelled` — Called when payment is cancelled

**Sample Success Webhook Payload:**

```json
{
  "key": "JPM7Fg",
  "txnid": "UPIINT20240315001",
  "mihpayid": "30478359672",
  "status": "success",
  "unmappedstatus": "captured",
  "mode": "UPI",
  "bankcode": "INTENT",
  "amount": "500.00",
  "productinfo": "UPI Payment for Order #12345",
  "firstname": "Rajesh",
  "email": "rajesh@example.com",
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

**UPI Intent-Specific Fields:**

| Field            | Value for UPI Intent                           |
| ---------------- | ---------------------------------------------- |
| `mode`           | `"UPI"`                                        |
| `bankcode`       | `"INTENT"`                                     |
| `unmappedstatus` | `"captured"` (success) or `"failed"` (failure) |

<Info>
**Note on txnStatus "pending":**

The initial API response shows `txnStatus: "pending"`. The webhook is sent only after the customer completes the UPI authentication. Do NOT rely on polling — always use the webhook for final status updates.
</Info>

### Step 3.2: Verify Webhook Hash

**Always verify the webhook hash** before processing the notification.

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

def verify_upi_intent_webhook_hash(webhook_payload, client_secret):
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
is_valid = verify_upi_intent_webhook_hash(webhook_data, "your_client_secret")

if is_valid:
    print("✅ Webhook verified — UPI Intent payment confirmed")
else:
    print("❌ Invalid webhook hash — reject")
```

**Java:**

```java
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class UPIIntentWebhookVerifier {
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
def handle_upi_intent_webhook():
    webhook_data = request.json
    
    # Verify hash
    if not verify_upi_intent_webhook_hash(webhook_data, "your_client_secret"):
        return jsonify({"error": "Invalid hash"}), 400
    
    # Extract details
    txnid = webhook_data.get('txnid')
    mihpayid = webhook_data.get('mihpayid')
    status = webhook_data.get('status')
    mode = webhook_data.get('mode')
    bankcode = webhook_data.get('bankcode')
    amount = webhook_data.get('amount')
    
    # Update database
    # db.update_payment_status(txnid=txnid, mihpayid=mihpayid, status=status)
    
    print(f"✅ UPI Intent Payment: {status} | {txnid} | PayU ID: {mihpayid} | Mode: {mode}/{bankcode} | Amount: ₹{amount}")
    
    # Respond with 200 OK
    return jsonify({"message": "Webhook received"}), 200

if __name__ == '__main__':
    app.run(port=5000)
```

***

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

verify_hash = generate_verify_hash(8739528, "UPIINT20240315001", "your_client_secret")
```

### Step 4.2: Call Verify Payment API

**Endpoint:**

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
  "txnid": "UPIINT20240315001",
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
    "txnid": "UPIINT20240315001",
    "merchant_id": 8739528,
    "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
    "hash": "computed_verify_hash_here"
}

try:
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {str(e)}")
```

**Response:**

```json
{
  "status": "success",
  "unmappedstatus": "captured",
  "mihpayid": "30478359672",
  "txnid": "UPIINT20240315001",
  "amount": "500.00",
  "mode": "UPI",
  "bankcode": "INTENT",
  "productinfo": "UPI Payment for Order #12345",
  "firstname": "Rajesh",
  "email": "rajesh@example.com",
  "phone": "919876543210"
}
```

### Step 4.3: Process Verification Response

**Reconciliation:**

Compare webhook vs. verify response:

✅ `mihpayid` matches<br />✅ `txnid` matches<br />✅ `amount` matches<br />✅ `status` is `"success"`<br />✅ `unmappedstatus` is `"captured"`<br />✅ `mode` is `"UPI"`<br />✅ `bankcode` is `"INTENT"`

If all match, mark the transaction as confirmed.

***

## Use Cases

Partner Payment UPI Intent is ideal for:

- **Mobile-first apps** — Ride-hailing, food delivery, e-commerce apps
- **Quick checkout** — Minimize steps and friction
- **In-app purchases** — Games, content subscriptions, digital goods
- **Instant payments** — Bills, recharges, peer-to-peer transfers

***

## Error Handling

| Error                                     | Cause                                         | Resolution                                                                                                              |
| ----------------------------------------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| <code>s2s_client_ip is mandatory</code>   | Missing customer IP when txn_s2s_flow=4       | Capture real customer IP from request headers (check <code>X-Forwarded-For</code> if behind proxy). Never use server IP |
| <code>s2s_device_info is mandatory</code> | Missing device user-agent when txn_s2s_flow=4 | Capture device user-agent from HTTP request headers (<code>User-Agent</code>). Never hardcode or leave blank            |
| <code>Invalid hash</code>                 | Hash computation mismatch                     | Verify using <code>client_secret</code>, check 6-pipe sequence, ensure SHA-512 lowercase hex                            |
| <code>Invalid access token</code>         | OAuth token expired                           | Refresh OAuth token. Implement auto-refresh logic before expiry                                                         |
| <code>Transaction not found</code>        | txnid doesn't exist                           | Verify txnid in verify request matches creation request                                                                 |
| <code>HMAC validation failure</code>      | Webhook hash verification failed              | Check reverse hash formula (5 pipes after status). Use case-insensitive comparison                                      |
| UPI app not opening                       | No UPI app installed or deep link issue       | Check if UPI app is installed before invoking. Provide fallback message                                                 |

***

## Testing

### Test Environment

**API Base URL:** `https://test-partnerapilayer.payu.in/apilayer/partner`

**OAuth URLs:**

- Auth Code: `https://uat-partner.payu.in/api/v1/merchants/auth_code`
- Access Token: `https://uat-accounts.payu.in/oauth/token`

<Warning>
**⚠️ Info Gap: Test UPI VPAs**

The PDF does not provide test UPI VPAs or simulator instructions for testing UPI Intent in sandbox. Request test credentials from PayU integration team.
</Warning>

### Test Workflow

1. Generate OAuth access token
2. Initiate UPI Intent payment with `txn_s2s_flow=4`
3. Verify `intentURIData` is returned in response
4. Test UPI app invocation on Android/iOS test devices
5. Complete test payment in UPI app
6. Verify webhook is received
7. Call Verify Payment API
8. Reconcile webhook vs verification response

### Validation Checklist

✅ OAuth token generation succeeds<br />✅ Payment API returns `intentURIData`<br />✅ UPI app opens with pre-filled details<br />✅ Test payment succeeds in UPI app<br />✅ Webhook received within 5-10 seconds<br />✅ Webhook hash verification passes<br />✅ Verify Payment API confirms status<br />✅ Reconciliation successful

***

## Best Practices

### Capturing S2S Parameters

- ✅ **Always capture real customer IP** — Check `X-Forwarded-For`, `X-Real-IP` headers if behind proxy/CDN
- ✅ **Capture accurate user-agent** — Use the actual HTTP `User-Agent` header, never hardcode
- ✅ **Never use server IP** as `s2s_client_ip` — This will cause validation failures

### UPI App Invocation

- ✅ **Check if UPI app is installed** before attempting to open deep link
- ✅ **Provide fallback UI** if no UPI app is installed ("Please install Google Pay or PhonePe")
- ✅ **Show waiting screen** after invoking UPI app with "Completing payment..." message
- ✅ **Handle app-switch timeout** — Update UI if customer doesn't return within 2-3 minutes

### Security

- ✅ **Always verify webhook hash** before updating payment status
- ✅ **Secure client_secret storage** — Never expose in client-side code
- ✅ **Use HTTPS** for all webhook endpoints
- ✅ **Implement rate limiting** on webhook handlers

### Reliability

- ✅ **Implement idempotency** using `txnid` to prevent duplicate processing
- ✅ **Use unique txnid** per transaction — Never reuse
- ✅ **Handle "pending" status gracefully** — Don't show "failed" immediately
- ✅ **Implement webhook retry logic** — PayU retries webhooks, handle duplicates
- ✅ **Always call Verify Payment API** after webhook for final confirmation

### Integration

- ✅ **Implement OAuth token refresh** — Tokens expire after \~1 hour
- ✅ **Log all API requests/responses** for debugging
- ✅ **Monitor webhook latency** — Alert if webhooks delayed beyond expected time
- ✅ **Test on real devices** — Emulators may not handle UPI deep links correctly

***

## Next Steps

- [Payment Links Hosted Checkout](#) — Multi-payment method web-based checkout
- [Partner Payment UPI TPV Integration](#) — UPI Intent with third-party verification
- [Verify Payment API Reference](#) — Complete API documentation
- [Partner Webhook Configuration Guide](#) — Advanced webhook handling

<Success>
**Integration Complete!** You can now process UPI Intent payments with direct app invocation using PayU Partner Payments API.
</Success>
