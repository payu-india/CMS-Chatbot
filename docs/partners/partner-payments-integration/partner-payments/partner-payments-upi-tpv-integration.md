---
title: Partner Payments UPI TPV Integration
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
Partner Payments UPI TPV (Third-Party Verification) enables partners to initiate UPI payments with beneficiary account validation. Unlike standard UPI Intent, TPV ensures that the payment is made from a specific verified bank account by validating the customer's UPI account against the beneficiary details you provide.

This is critical for regulatory compliance scenarios where you need to ensure funds originate from an authorized account, such as loan repayments where the borrower must pay from their registered account, or vendor payments where the vendor must use their verified business account.

**Key Benefits:**

- **Account validation** — Ensures payment comes from the authorized beneficiary account
- **Regulatory compliance** — Meets KYC and anti-money laundering requirements
- **Fraud prevention** — Prevents payments from unauthorized accounts
- **Audit trail** — Complete record of which account was used for payment
- **Secure S2S flow** — Direct UPI app invocation with account verification

This integration is ideal for:

- **Loan repayments** — EMI collections from borrower's registered account
- **Vendor payments** — Ensure payments come from vendor's verified business account
- **Refund collections** — Collect refunds to the original payment account
- **Compliance-heavy industries** — NBFC, lending, insurance, government payments

***

## How It Works

The Partner Payments UPI TPV flow follows these steps:

1. **OAuth Authentication** — Obtain an access token with scope: `hub_session`

2. **Initiate UPI TPV Payment** — POST a payment request with:
   - `txn_s2s_flow=4` (enables UPI S2S flow)
   - Beneficiary account details (`beneficiarydetail` with IFSC, account number, account holder name)
   - Customer device details (`s2s_client_ip`, `s2s_device_info`)
   - Computed hash

3. **Receive intentURIData** — PayU returns a UPI deep link string and sets `bankcode=INTTPV`, `api_version=6` internally

4. **Invoke UPI App** — Customer's UPI app opens with pre-filled payment details

5. **Account Validation** — PayU validates the customer's UPI account against beneficiary details provided

6. **Customer Authenticates** — If account matches, customer enters UPI PIN; if mismatch, payment is rejected

7. **Receive Webhook** — PayU sends payment status notification with `bankcode=INTTPV`

8. **Verify Payment** — Call Verify Payment API to confirm final transaction status

***

## Prerequisites

Before you begin, ensure you have:

- **Partner OAuth Application** registered with PayU with the above scopes enabled
- **OAuth Credentials:** `client_id` and `client_secret`
- **Merchant Credentials:** `merchant_id` (PayU merchant ID) and `reseller_id` (partner UUID)
- **UPI TPV Enabled** — Your account must be enabled for UPI TPV transactions (contact PayU)
- **S2S Flow Enabled** — Support for `txn_s2s_flow=4`
- **Partner Webhook URLs** configured (`partner_webhook_success`, `partner_webhook_failure`, `partner_webhook_cancelled`)
- **Beneficiary Account Details:**
  - IFSC code
  - Account number
  - Account holder name
- **Ability to Capture:**
  - Customer IP address (`s2s_client_ip`)
  - Device user-agent string (`s2s_device_info`)
- **Test Environment Access** to `https://test-partnerapilayer.payu.in`

<Warning>
**Critical Requirements for UPI TPV:**
- `txn_s2s_flow` MUST be set to `"4"`
- `beneficiarydetail` is **mandatory** for TPV (contains IFSC, account number, account holder name)
- `s2s_client_ip` and `s2s_device_info` are **mandatory** when txn_s2s_flow=4
- `beneficiarydetail` is **NOT included in hash calculation**
- All hash computations use OAuth `client_secret` (NOT merchant salt)
- When beneficiarydetail is present with txn_s2s_flow=4, PayU automatically sets `bankcode=INTTPV` and `api_version=6`
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
    print(f"\nInitial Access Token: {initial_access_token}")
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
            System.out.println("\nInitial Access Token: " + accessToken);
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
    echo "Status Code: " . $statusCode . "\n";
    echo "Response: " . $response . "\n";
    
    // Extract access token for Step 1.2
    if ($statusCode == 200) {
        $responseData = json_decode($response, true);
        $initialAccessToken = $responseData["access_token"];
        echo "\nInitial Access Token: " . $initialAccessToken;
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
    print(f"\nAuthorization Code: {authorization_code}")
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
            System.out.println("\nAuthorization Code: " + authCode);
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
    echo "Status Code: " . $statusCode . "\n";
    echo "Response: " . $response . "\n";
    
    // Extract authorization code for Step 1.3
    if ($statusCode == 200) {
        $responseData = json_decode($response, true);
        $authorizationCode = $responseData["code"];
        echo "\nAuthorization Code: " . $authorizationCode;
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
    print(f"\n✅ Final Access Token (use for all API calls): {final_access_token}")
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
            System.out.println("\n✅ Final Access Token: " + finalAccessToken);
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
    echo "Status Code: " . $statusCode . "\n";
    echo "Response: " . $response . "\n";
    
    // Extract final access token
    if ($statusCode == 200) {
        $responseData = json_decode($response, true);
        $finalAccessToken = $responseData["access_token"];
        echo "\n✅ Final Access Token (use for all API calls): " . $finalAccessToken;
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

***

## Step 2: Initiate UPI TPV Payment

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
      <th>Parameter</th>
      <th>Type & Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>txnid</td>
      <td><strong>string</strong> - Unique transaction ID generated by the partner.</td>
      <td>TPVUPI20240315001</td>
    </tr>
    <tr>
      <td>amount</td>
      <td><strong>string</strong> - Transaction amount in decimal format.</td>
      <td>518.02</td>
    </tr>
    <tr>
      <td>productinfo</td>
      <td><strong>string</strong> - Product or service description.</td>
      <td>Loan EMI Payment</td>
    </tr>
    <tr>
      <td>phone</td>
      <td><strong>string</strong> - Customer phone number with country code (10 digits).</td>
      <td>919876543210</td>
    </tr>
    <tr>
      <td>merchant_id</td>
      <td><strong>integer</strong> - PayU merchant ID.</td>
      <td>8739528</td>
    </tr>
    <tr>
      <td>reseller_id</td>
      <td><strong>string</strong> - Partner/reseller UUID.</td>
      <td>11ee-0e7e-5403fde2-9523-0a696b110fde</td>
    </tr>
    <tr>
      <td>txn_s2s_flow</td>
      <td><strong>string</strong> - Server-to-server flow identifier. Must be <code>4</code> for UPI TPV.</td>
      <td>4</td>
    </tr>
    <tr>
      <td>s2s_client_ip</td>
      <td><strong>string</strong> - Customer's IP address.</td>
      <td>157.240.22.9</td>
    </tr>
    <tr>
      <td>s2s_device_info</td>
      <td><strong>string</strong> - Customer's device user-agent string.</td>
      <td>Mozilla/5.0 (iPhone) AppleWebKit/602.4.6</td>
    </tr>
    <tr>
      <td>beneficiarydetail</td>
      <td><strong>string (JSON)</strong> - Beneficiary account details for TPV validation. Must contain: <code>ifscCode</code>, <code>accountNumber</code>, <code>accountHolderName</code></td>
      <td>{"ifscCode":"ICIC0001234","accountNumber":"123456789012","accountHolderName":"Test User"}</td>
    </tr>
    <tr>
      <td>hash</td>
      <td><strong>string</strong> - SHA-512 hash for request authentication, encoded as a lowercase hex string. <strong>Note:</strong> beneficiarydetail is NOT included in hash calculation.</td>
      <td>a3f7c92e1b...</td>
    </tr>
  </tbody>
</table>

#### Optional Parameters

| Parameter | Type & Description                                                                    | Example                                                                      |
| --------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| firstname | <strong>string</strong> - Customer's first name.                                      | Amit                                                                         |
| email     | <strong>string</strong> - Customer's email address.                                   | [amit.kumar@example.com](mailto:amit.kumar@example.com)                      |
| udf1      | <strong>string</strong> - User-defined field 1 for custom data.                       | loan_account_123                                                             |
| udf2      | <strong>string</strong> - User-defined field 2 for custom data.                       | emi_month_06                                                                 |
| udf3      | <strong>string</strong> - User-defined field 3 for custom data.                       | tpv_reference_001                                                            |
| udf4      | <strong>string</strong> - User-defined field 4 for custom data.                       | borrower_id_456                                                              |
| udf5      | <strong>string</strong> - User-defined field 5, often used for partner or channel ID. | partner_tpv_channel                                                          |
| surl      | <strong>string</strong> - Success callback URL (optional for S2S flow).               | [https://yoursite.com/payment/success](https://yoursite.com/payment/success) |
| furl      | <strong>string</strong> - Failure callback URL (optional for S2S flow).               | [https://yoursite.com/payment/failure](https://yoursite.com/payment/failure) |
| curl      | <strong>string</strong> - Cancel callback URL (optional for S2S flow).                | [https://yoursite.com/payment/cancel](https://yoursite.com/payment/cancel)   |

<Warning>
**UPI TPV-Specific Notes:**
- `txn_s2s_flow` MUST be set to `"4"` — This activates the UPI S2S TPV flow
- `beneficiarydetail` is **mandatory** — Contains IFSC, account number, and account holder name in JSON format
- `beneficiarydetail` is **NOT included in hash calculation** — Use the same hash formula as UPI Intent
- When `beneficiarydetail` + `txn_s2s_flow=4` are present, PayU automatically sets:
  - `bankcode = INTTPV`
  - `api_version = 6`
- `s2s_client_ip` and `s2s_device_info` are **mandatory** when txn_s2s_flow=4
- Do NOT send `beneficiarydetail` in the hash string
</Warning>

**Beneficiarydetail Structure:**

```json
{
  "ifscCode": "ICIC0001234",
  "accountNumber": "123456789012",
  "accountHolderName": "Test User"
}
```

Send this as a **JSON string** (not an object) in the `beneficiarydetail` parameter.

### Step 2.2: Generate Payment Request Hash

The payment request hash authenticates your API call using SHA-512. **Important:** The `beneficiarydetail` parameter is NOT included in the hash calculation.

**Hash Formula:**

```
merchant_id|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||client_secret
```

<Warning>
**Critical Hash Rules:**
- There are **six consecutive pipes** (`||||||`) between `udf5` and `client_secret`
- Use your OAuth **client_secret** (NOT merchant salt)
- Use empty strings for any missing optional fields (results in consecutive pipes)
- **DO NOT include `beneficiarydetail` in the hash** — Use the same formula as UPI Intent
- Compute SHA-512 and output as **lowercase hexadecimal**
- Do NOT add a trailing pipe after `client_secret`
</Warning>

**Sample Hash Generation Code:**

**Python:**

```python
import hashlib

def generate_upi_tpv_hash(merchant_id, txnid, amount, productinfo, firstname, email, udf1, udf2, udf3, udf4, udf5, client_secret):
    # Note: beneficiarydetail is NOT included in hash
    hash_string = f"{merchant_id}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{client_secret}"
    return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()

# Example
payment_hash = generate_upi_tpv_hash(
    merchant_id=8739528,
    txnid="TPVUPI20240315001",
    amount="518.02",
    productinfo="Loan EMI Payment",
    firstname="Amit",
    email="amit.kumar@example.com",
    udf1="loan_account_123",
    udf2="emi_month_06",
    udf3="tpv_reference_001",
    udf4="",
    udf5="partner_tpv_channel",
    client_secret="your_client_secret_here"
)

print(f"Payment Hash: {payment_hash}")
```

**Java:**

```java
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class UPITPVHashGenerator {
    public static String generateHash(
        int merchantId, String txnid, String amount, String productinfo,
        String firstname, String email, String udf1, String udf2, 
        String udf3, String udf4, String udf5, String clientSecret
    ) throws NoSuchAlgorithmException {
        
        // Note: beneficiarydetail is NOT included in hash
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
function generateUPITPVHash($merchantId, $txnid, $amount, $productinfo, 
                            $firstname, $email, $udf1, $udf2, $udf3, 
                            $udf4, $udf5, $clientSecret) {
    
    // Note: beneficiarydetail is NOT included in hash
    $hashString = $merchantId . "|" . $txnid . "|" . $amount . "|" . 
                  $productinfo . "|" . $firstname . "|" . $email . "|" .
                  $udf1 . "|" . $udf2 . "|" . $udf3 . "|" . $udf4 . "|" . 
                  $udf5 . "||||||" . $clientSecret;
    
    return hash('sha512', $hashString);
}

$hash = generateUPITPVHash(
    8739528,
    "TPVUPI20240315001",
    "518.02",
    "Loan EMI Payment",
    "Amit",
    "amit.kumar@example.com",
    "loan_account_123",
    "emi_month_06",
    "tpv_reference_001",
    "",
    "partner_tpv_channel",
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
  "txnid": "TPVUPI20240315001",
  "amount": "518.02",
  "productinfo": "Loan EMI Payment",
  "firstname": "Amit",
  "email": "amit.kumar@example.com",
  "phone": "919876543210",
  "merchant_id": 8739528,
  "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
  "txn_s2s_flow": "4",
  "s2s_client_ip": "157.240.22.9",
  "s2s_device_info": "Mozilla/5.0 (iPhone) AppleWebKit/602.4.6",
  "beneficiarydetail": "{\"ifscCode\":\"ICIC0001234\",\"accountNumber\":\"123456789012\",\"accountHolderName\":\"Test User\"}",
  "udf1": "loan_account_123",
  "udf2": "emi_month_06",
  "udf3": "tpv_reference_001",
  "udf5": "partner_tpv_channel",
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

# Beneficiary details as JSON string
beneficiary_detail = json.dumps({
    "ifscCode": "ICIC0001234",
    "accountNumber": "123456789012",
    "accountHolderName": "Test User"
})

payload = {
    "txnid": "TPVUPI20240315001",
    "amount": "518.02",
    "productinfo": "Loan EMI Payment",
    "firstname": "Amit",
    "email": "amit.kumar@example.com",
    "phone": "919876543210",
    "merchant_id": 8739528,
    "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
    "txn_s2s_flow": "4",
    "s2s_client_ip": "157.240.22.9",
    "s2s_device_info": "Mozilla/5.0 (iPhone) AppleWebKit/602.4.6",
    "beneficiarydetail": beneficiary_detail,
    "udf1": "loan_account_123",
    "udf2": "emi_month_06",
    "udf3": "tpv_reference_001",
    "udf5": "partner_tpv_channel",
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

public class CreateUPITPVPayment {
    public static void main(String[] args) throws Exception {
        String url = "https://test-partnerapilayer.payu.in/apilayer/partner/payments";
        
        // Escape the beneficiarydetail JSON properly
        String payload = "{\"txnid\":\"TPVUPI20240315001\",\"amount\":\"518.02\",\"productinfo\":\"Loan EMI Payment\",\"firstname\":\"Amit\",\"email\":\"amit.kumar@example.com\",\"phone\":\"919876543210\",\"merchant_id\":8739528,\"reseller_id\":\"11ee-0e7e-5403fde2-9523-0a696b110fde\",\"txn_s2s_flow\":\"4\",\"s2s_client_ip\":\"157.240.22.9\",\"s2s_device_info\":\"Mozilla/5.0 (iPhone) AppleWebKit/602.4.6\",\"beneficiarydetail\":\"{\\\"ifscCode\\\":\\\"ICIC0001234\\\",\\\"accountNumber\\\":\\\"123456789012\\\",\\\"accountHolderName\\\":\\\"Test User\\\"}\",\"udf1\":\"loan_account_123\",\"udf2\":\"emi_month_06\",\"udf3\":\"tpv_reference_001\",\"udf5\":\"partner_tpv_channel\",\"hash\":\"computed_sha512_hash_here\"}";
        
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

// Beneficiary details as JSON string
$beneficiaryDetail = json_encode(array(
    "ifscCode" => "ICIC0001234",
    "accountNumber" => "123456789012",
    "accountHolderName" => "Test User"
));

$payload = json_encode(array(
    "txnid" => "TPVUPI20240315001",
    "amount" => "518.02",
    "productinfo" => "Loan EMI Payment",
    "firstname" => "Amit",
    "email" => "amit.kumar@example.com",
    "phone" => "919876543210",
    "merchant_id" => 8739528,
    "reseller_id" => "11ee-0e7e-5403fde2-9523-0a696b110fde",
    "txn_s2s_flow" => "4",
    "s2s_client_ip" => "157.240.22.9",
    "s2s_device_info" => "Mozilla/5.0 (iPhone) AppleWebKit/602.4.6",
    "beneficiarydetail" => $beneficiaryDetail,
    "udf1" => "loan_account_123",
    "udf2" => "emi_month_06",
    "udf3" => "tpv_reference_001",
    "udf5" => "partner_tpv_channel",
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
    "message": null,
    "referenceId": "7a3060b7462bd2ce6d025c9997220e01",
    "statusCode": null,
    "txnId": "TPVUPI20240315001",
    "txnStatus": "pending",
    "unmappedStatus": "pending"
  },
  "result": {
    "paymentId": "30478359671",
    "merchantName": "YourMerchantName",
    "merchantVpa": "merchant.payu@indus",
    "amount": "518.02",
    "intentURIData": "pa=merchant.payu@indus&pn=YOUR MERCHANT NAME&tr=30478359671&tid=TPVUPI20240315001&am=518.02&cu=INR&tn=UPIIntent",
    "acsTemplate": null,
    "otpPostUrl": null
  }
}
```

**Key Response Fields:**

| Field                  | Description                                            |
| ---------------------- | ------------------------------------------------------ |
| `metaData.txnStatus`   | Initial status (typically `"pending"` for UPI TPV)     |
| `result.paymentId`     | PayU's internal payment ID (mihpayid)                  |
| `result.merchantVpa`   | Merchant's UPI VPA for this transaction                |
| `result.intentURIData` | **Critical** — UPI deep link string to invoke UPI apps |

<Info>
**TPV Processing:**
- PayU internally sets `bankcode=INTTPV` and `api_version=6`
- The `intentURIData` is used to invoke the customer's UPI app
- During payment, PayU validates the customer's UPI account against the `beneficiarydetail` you provided
- Payment succeeds only if the account details match
</Info>

<Warning>
**⚠️ Info Gap: UPI App Invocation Code**

The PDF does not include platform-specific code for invoking UPI apps. Refer to the Partner Payment UPI Intent documentation or request official samples from PayU for:
- Android Intent URI invocation
- iOS URL scheme handling
- Mobile web fallback mechanisms
</Warning>

***

## Step 3: Receive Payment Notification

### Step 3.1: Partner Webhook

After the customer completes payment (or if account validation fails), PayU sends a webhook notification to your configured partner webhook URL.

**Sample Success Webhook Payload (UPI TPV):**

```json
{
  "key": "JPM7Fg",
  "txnid": "TPVUPI20240315001",
  "mihpayid": "30478359671",
  "status": "success",
  "unmappedstatus": "captured",
  "mode": "UPI",
  "bankcode": "INTTPV",
  "amount": "518.02",
  "productinfo": "Loan EMI Payment",
  "firstname": "Amit",
  "email": "amit.kumar@example.com",
  "phone": "919876543210",
  "udf1": "loan_account_123",
  "udf2": "emi_month_06",
  "udf3": "tpv_reference_001",
  "udf4": "",
  "udf5": "partner_tpv_channel",
  "merchant_id": "8739528",
  "error": "No Error",
  "error_Message": "No Error",
  "hash": "webhook_hash_from_payu"
}
```

**UPI TPV-Specific Fields:**

| Field            | Value for UPI TPV                                                |
| ---------------- | ---------------------------------------------------------------- |
| `mode`           | `"UPI"`                                                          |
| `bankcode`       | `"INTTPV"` (automatically set by PayU)                           |
| `unmappedstatus` | `"captured"` (success) or `"failed"` (failure/validation failed) |

### Step 3.2: Verify Webhook Hash

**Always verify the webhook hash** before processing.

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

def verify_upi_tpv_webhook_hash(webhook_payload, client_secret):
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
is_valid = verify_upi_tpv_webhook_hash(webhook_data, "your_client_secret")

if is_valid:
    print("✅ UPI TPV webhook verified — account validation successful")
else:
    print("❌ Invalid webhook hash — reject")
```

**Java:**

```java
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class UPITPVWebhookVerifier {
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
def handle_upi_tpv_webhook():
    webhook_data = request.json
    
    # Verify hash
    if not verify_upi_tpv_webhook_hash(webhook_data, "your_client_secret"):
        return jsonify({"error": "Invalid hash"}), 400
    
    # Extract details
    txnid = webhook_data.get('txnid')
    mihpayid = webhook_data.get('mihpayid')
    status = webhook_data.get('status')
    bankcode = webhook_data.get('bankcode')
    amount = webhook_data.get('amount')
    
    # Verify it's a TPV transaction
    if bankcode == "INTTPV":
        print(f"✅ UPI TPV Payment: {status} | {txnid} | PayU ID: {mihpayid} | Amount: ₹{amount}")
        print(f"   Account validation successful - payment from verified beneficiary account")
    
    # Update database
    # db.update_payment_status(txnid=txnid, mihpayid=mihpayid, status=status, bankcode=bankcode)
    
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

verify_hash = generate_verify_hash(8739528, "TPVUPI20240315001", "your_client_secret")
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
  "txnid": "TPVUPI20240315001",
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
  "mihpayid": "30478359671",
  "txnid": "TPVUPI20240315001",
  "amount": "518.02",
  "mode": "UPI",
  "bankcode": "INTTPV",
  "productinfo": "Loan EMI Payment",
  "firstname": "Amit",
  "email": "amit.kumar@example.com",
  "phone": "919876543210"
}
```

### Step 4.3: Process Verification Response

**Reconciliation Checklist:**

✅ `mihpayid` matches<br />✅ `txnid` matches<br />✅ `amount` matches<br />✅ `status` is `"success"`<br />✅ `unmappedstatus` is `"captured"`<br />✅ `mode` is `"UPI"`<br />✅ `bankcode` is `"INTTPV"` (confirms TPV transaction)

If all match, the beneficiary account validation was successful and payment is confirmed.

***

## Use Cases

Partner Payments UPI TPV is ideal for:

### Loan Repayments

Ensure EMI payments come from the borrower's registered account. Prevents fraud where someone else tries to pay on behalf of the borrower.

### Vendor Payments

Verify that vendor payments originate from the vendor's verified business account, not personal or third-party accounts.

### Refund Collections

Collect refunds specifically to the account that made the original payment, ensuring compliance with refund regulations.

### Compliance-Heavy Industries

NBFC, lending, insurance, government payments where regulatory compliance requires verified account transactions.

***

## Error Handling

| Error                                         | Cause                                                    | Resolution                                                                                                             |
| --------------------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| <code>s2s_client_ip is mandatory</code>       | Missing customer IP when txn_s2s_flow=4                  | Capture real customer IP from request headers (check <code>X-Forwarded-For</code> if behind proxy)                     |
| <code>s2s_device_info is mandatory</code>     | Missing device user-agent when txn_s2s_flow=4            | Capture device user-agent from HTTP <code>User-Agent</code> header                                                     |
| <code>beneficiarydetail is mandatory</code>   | Missing beneficiary account details for TPV              | Include <code>beneficiarydetail</code> JSON string with ifscCode, accountNumber, accountHolderName                     |
| <code>Invalid beneficiarydetail format</code> | beneficiarydetail JSON is malformed                      | Ensure JSON is properly formatted and contains all three required fields. Send as JSON string, not object              |
| <code>Account validation failed</code>        | Customer's UPI account doesn't match beneficiary details | Payment rejected by PayU. Customer must use the registered account. Inform customer of the required account            |
| <code>Invalid hash</code>                     | Hash computation mismatch                                | Verify NOT including beneficiarydetail in hash. Use client_secret, check 6-pipe sequence, ensure SHA-512 lowercase hex |
| <code>Invalid access token</code>             | OAuth token expired                                      | Refresh OAuth token. Implement auto-refresh logic                                                                      |
| <code>HMAC validation failure</code>          | Webhook hash verification failed                         | Check reverse hash formula (5 pipes after status). Use case-insensitive comparison                                     |

***

## Testing

### Test Environment

**API Base URL:** `https://test-partnerapilayer.payu.in/apilayer/partner`

**OAuth URLs:**

- Auth Code: `https://uat-partner.payu.in/api/v1/merchants/auth_code`
- Access Token: `https://uat-accounts.payu.in/oauth/token`

<Warning>
**⚠️ Info Gap: Test Beneficiary Details**

The PDF does not provide test beneficiary account details for sandbox testing. Request test IFSC codes, account numbers, and account holder names from PayU integration team for UAT testing.
</Warning>

### Test Workflow

1. Generate OAuth access token
2. Create UPI TPV payment with test beneficiary details
3. Verify `intentURIData` is returned
4. Test UPI app invocation (on mobile device)
5. Complete payment using test UPI account matching beneficiary details
6. Verify webhook received with `bankcode=INTTPV`
7. Call Verify Payment API
8. Reconcile all data points

### Validation Checklist

✅ OAuth token generation succeeds<br />✅ Payment API returns `intentURIData`<br />✅ `beneficiarydetail` sent correctly (not in hash)<br />✅ UPI app opens with pre-filled details<br />✅ Account validation succeeds<br />✅ Test payment succeeds<br />✅ Webhook received with `bankcode=INTTPV`<br />✅ Webhook hash verified<br />✅ Verify Payment API confirms TPV status<br />✅ Reconciliation successful

***

## Best Practices

### Beneficiary Data Management

- ✅ Validate IFSC code format before sending (11 characters, alphanumeric)
- ✅ Validate account number (typically 9-18 digits)
- ✅ Match account holder name exactly as per bank records
- ✅ Store beneficiary details securely (encrypted database)
- ✅ Implement beneficiary verification during account linking

### Security

- ✅ Never include `beneficiarydetail` in hash calculation
- ✅ Always verify webhook hash before processing
- ✅ Store `client_secret` securely
- ✅ Use HTTPS for all webhook endpoints
- ✅ Encrypt beneficiary account details in database

### Reliability

- ✅ Implement idempotency using `txnid`
- ✅ Use unique `txnid` per transaction
- ✅ Handle account validation failures gracefully
- ✅ Provide clear error messages to customers
- ✅ Implement retry logic for Verify Payment API

### Customer Experience

- ✅ Clearly communicate which account should be used for payment
- ✅ Show beneficiary account details (last 4 digits) before payment
- ✅ Provide helpful error messages if account doesn't match
- ✅ Explain why TPV is required (compliance/security)
- ✅ Allow customers to update registered account if needed

### Compliance

- ✅ Maintain audit trail of all TPV transactions
- ✅ Store account validation results securely
- ✅ Implement data retention policies per regulations
- ✅ Ensure GDPR/data privacy compliance for beneficiary data

***

## Next Steps

- [Partner Payments Hosted Checkout](#) — Multi-method payment gateway integration
- [Partner Payment UPI Intent Integration](#) — Standard UPI S2S without TPV
- [Verify Payment API Reference](#) — Complete verification documentation
- [Partner Webhook Guide](#) — Advanced webhook patterns

<Success>
**Integration Complete!** You can now accept UPI TPV payments with beneficiary account validation using the Partner Payments API.
</Success>
