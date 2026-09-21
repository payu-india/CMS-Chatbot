---
title: 'Hosted Checkout with UPI TPV - Partner Payments '
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
Partner Payments Hosted Checkout with UPI TPV combines the convenience of PayU's multi-payment hosted gateway with the security of UPI Third-Party Verification (TPV). This integration enables you to collect payments through PayU's hosted checkout page while ensuring that UPI payments originate from a specific verified bank account, meeting regulatory compliance and fraud prevention requirements.

Unlike standard Hosted Checkout (which accepts UPI payments from any account) or standalone UPI TPV (which is S2S-only), this hybrid integration allows customers to:

1. Be redirected to PayU's hosted checkout page
2. Choose from multiple payment methods (cards, UPI, net banking, wallets)
3. If UPI is selected, have their account validated against the beneficiary details you provided
4. Complete payment only if the UPI account matches the authorized beneficiary account

**Key Benefits:**

- **Multi-method payment support** — Cards, UPI (with TPV), net banking, wallets in one integration
- **UPI account validation** — Ensures UPI payments come from the authorized beneficiary account
- **PCI-DSS compliance** — PayU handles all card data; you never touch sensitive information
- **Regulatory compliance** — Meets KYC, anti-money laundering, and beneficiary verification requirements
- **Fraud prevention** — Prevents UPI payments from unauthorized accounts
- **Zero maintenance** — PayU manages payment methods, bank integrations, and TPV validation
- **Flexible fallback** — Customers can use cards/net banking/wallets if UPI account doesn't match

**This integration is ideal for:**

- **Loan repayment platforms** requiring EMI collections from borrower's registered account
- **NBFC/Lending platforms** with regulatory beneficiary verification requirements
- **Vendor payment portals** ensuring payments from verified business accounts
- **Insurance premium collection** requiring account validation
- **Government payment portals** with strict compliance needs
- **Multi-tenant platforms** serving compliance-heavy industries

***

## How It Works

The Partner Payments Hosted Checkout with UPI TPV flow follows these steps:

1. **OAuth Authentication** — Obtain an access token with scopes: `create_payment_links`, `partner_payment_links`, `partner_payments`

2. **Initiate Payment with Beneficiary Details** — POST a payment request with:
   - Standard hosted checkout parameters (transaction details, callback URLs)
   - Beneficiary account details (`beneficiarydetail` JSON string)
   - Optional: S2S flow parameters if you want UPI-only TPV enforcement
   - Computed hash (beneficiarydetail is NOT included in hash)

3. **Receive Redirect URL** — PayU returns a `redirectUri` pointing to the hosted checkout page

4. **Redirect Customer** — Customer is redirected to PayU's hosted checkout in their browser

5. **Customer Selects Payment Method** on hosted page:
   - **If Cards/Net Banking/Wallets selected:** Standard payment flow (no TPV validation)
   - **If UPI selected:** PayU validates customer's UPI account against beneficiary details

6. **UPI TPV Validation** (when UPI is selected):
   - PayU internally sets `bankcode=INTTPV` and `api_version=6`
   - Customer's UPI account is matched against the beneficiary details you provided
   - If account matches: Payment proceeds
   - If account mismatch: Payment is rejected with validation error

7. **Customer Redirected Back** — PayU redirects to your success/failure/cancel URL based on outcome

8. **Receive Webhook** — PayU sends payment status notification to your configured partner webhook URL
   - For successful UPI TPV payments: `bankcode: "INTTPV"` is included

9. **Verify Payment** — Call Verify Payment API to confirm final transaction status

***

## Prerequisites

Before you begin, ensure you have:

- **Partner OAuth Application** registered with PayU with the above scopes enabled
- **OAuth Credentials:** `client_id` and `client_secret`
- **Merchant Credentials:** `merchant_id` (PayU merchant ID) and `reseller_id` (partner UUID)
- **UPI TPV Feature Enabled** — Your account must be enabled for UPI TPV transactions (contact PayU support)
- **Beneficiary Account Details** for each transaction:
  - IFSC code
  - Account number
  - Account holder name
- **Callback URLs Ready:**
  - `surl` — Success redirect URL
  - `furl` — Failure redirect URL
  - `curl` — Cancel redirect URL
- **Partner Webhook URLs** configured in PayU's system (`partner_webhook_success`, `partner_webhook_failure`, `partner_webhook_cancelled`)
- **Test Environment Access** to `https://test-partnerapilayer.payu.in`

<Warning>
**Critical Requirements for Hosted Checkout with UPI TPV:**
- `beneficiarydetail` must be provided as a JSON string
- `beneficiarydetail` is **NOT** included in hash calculation
- When `beneficiarydetail` is present, PayU automatically sets `bankcode=INTTPV` and `api_version=6` for UPI payments
- TPV validation applies ONLY to UPI payments; cards, net banking, and wallets are not validated
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

<Partner_Payment_Auth />

## Step 2: Initiate Hosted Checkout Payment with UPI TPV

### Step 2.1: Prepare Request Parameters

Construct your payment request with transaction details and beneficiary account information.

<Accordion title="Request Parameters" icon="fa-table">
  **Mandatory Parameters**

  | Parameter         | Description                                                                                                                       | Example                                                      |
  | :---------------- | :-------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------- |
  | merchant_id       | PayU merchant ID.                                                                                                                 | 8739528                                                      |
  | reseller_id       | Partner UUID/reseller ID.                                                                                                         | 11ee-0e7e-5403fde2-9523-0a696b110fde                         |
  | txnid             | Unique transaction ID (alphanumeric, max 50 chars).                                                                               | HC_TPV_20240315_001                                          |
  | amount            | Transaction amount (decimal, 2 places).                                                                                           | 1500.00                                                      |
  | productinfo       | Product/service description.                                                                                                      | Loan EMI Payment - March 2024                                |
  | surl              | Success redirect URL (HTTPS).                                                                                                     | [https://yoursite.com/success](https://yoursite.com/success) |
  | furl              | Failure redirect URL (HTTPS).                                                                                                     | [https://yoursite.com/failure](https://yoursite.com/failure) |
  | curl              | Cancel redirect URL (HTTPS).                                                                                                      | [https://yoursite.com/cancel](https://yoursite.com/cancel)   |
  | beneficiarydetail | Beneficiary account details as JSON string. Required for TPV transactions. See the Beneficiary Detail Schema below.               | See below                                                    |
  | hash              | SHA-512 hash computed as: sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|salt) | Computed (see Step 2.2)                                      |

  **Optional Parameters**

  | Parameter | Description                 | Example                                                     |
  | :-------- | :-------------------------- | :---------------------------------------------------------- |
  | firstname | Customer first name.        | Rajesh                                                      |
  | email     | Customer email.             | [rajesh.kumar@example.com](mailto:rajesh.kumar@example.com) |
  | phone     | Customer phone (10 digits). | 9876543210                                                  |
  | udf1      | User-defined field 1.       | session_12345                                               |
  | udf2      | User-defined field 2.       | 1370625260                                                  |
  | udf3      | User-defined field 3.       | loan-ref-ABC123                                             |
  | udf4      | User-defined field 4.       |                                                             |
  | udf5      | User-defined field 5.       | whatsapp                                                    |

  **Beneficiary Detail Schema:**

  The `beneficiarydetail` parameter must be a **JSON string** containing the authorized beneficiary account details:

  ```json
  {
    "ifscCode": "ICIC0001234",
    "accountNumber": "123456789012",
    "accountHolderName": "RAJESH KUMAR"
  }
  ```

  **Mandatory Parameters**

  | Parameter         | Description                                   | Example      |
  | :---------------- | :-------------------------------------------- | :----------- |
  | ifscCode          | 11-character IFSC code of beneficiary's bank. | ICIC0001234  |
  | accountNumber     | Beneficiary's bank account number.            | 123456789012 |
  | accountHolderName | Account holder name (as per bank records).    | RAJESH KUMAR |
</Accordion>

<Warning>
**Critical: Beneficiary Detail Handling**

1. **JSON String Format:** The `beneficiarydetail` value must be a stringified JSON object (escaped quotes for JSON payloads)
2. **NOT Included in Hash:** `beneficiarydetail` is **excluded** from hash calculation
3. **Automatic TPV Activation:** When `beneficiarydetail` is present, PayU internally sets:
   - `bankcode = "INTTPV"`
   - `api_version = "6"`
4. **Account Matching:** During UPI payment, PayU validates the customer's UPI account against these details
5. **Name Matching:** Account holder name must match (case-insensitive, spaces ignored)
</Warning>

**Example Request Body:**

```json
{
  "merchant_id": "8739528",
  "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
  "txnid": "HC_TPV_20240315_001",
  "amount": "1500.00",
  "productinfo": "Loan EMI Payment - March 2024",
  "firstname": "Rajesh",
  "email": "rajesh.kumar@example.com",
  "phone": "9876543210",
  "surl": "https://yoursite.com/success",
  "furl": "https://yoursite.com/failure",
  "curl": "https://yoursite.com/cancel",
  "udf1": "session_12345",
  "udf2": "1370625260",
  "udf3": "loan-ref-ABC123",
  "udf4": "",
  "udf5": "whatsapp",
  "beneficiarydetail": "{\"ifscCode\":\"ICIC0001234\",\"accountNumber\":\"123456789012\",\"accountHolderName\":\"RAJESH KUMAR\"}",
  "hash": "<COMPUTED_HASH>"
}
```

***

### Step 2.2: Generate Payment Request Hash

Compute the SHA-512 hash for request authentication.

<Warning>
**Critical Hash Rules:**
- Use OAuth `client_secret` (NOT merchant salt)
- **Exclude `beneficiarydetail`** from hash calculation
- Six consecutive pipes (`||||||`) between `udf5` and `client_secret`
- Empty fields represented as empty strings between pipes
- Hash must be lowercase hexadecimal (128 characters)
</Warning>

**Hash Formula:**

```
merchant_id|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||client_secret
```

**Step-by-Step Hash Generation:**

1. Concatenate fields with pipe separators (in exact order above)
2. Use empty strings for missing/empty fields (resulting in consecutive pipes)
3. Add six pipes between `udf5` and `client_secret`
4. Compute SHA-512 digest
5. Convert to lowercase hexadecimal

**Example Hash String:**

```
8739528|HC_TPV_20240315_001|1500.00|Loan EMI Payment - March 2024|Rajesh|rajesh.kumar@example.com|session_12345|1370625260|loan-ref-ABC123||whatsapp||||||YOUR_CLIENT_SECRET
```

<Generate_Hash_Partner_Payment />

***

### Step 2.3: POST the Payment Request

Send the payment request to PayU's Partner Payments API.

**Endpoint:**

| Environment | URL                                                              |
| ----------- | ---------------------------------------------------------------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer/partner/payments` |
| Production  | `https://api.payu.in/partner/payments`                           |

**Headers:**

```
Content-Type: application/json
Authorization: Bearer <FINAL_ACCESS_TOKEN>
```

**Sample Request:**

```bash
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/payments' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...' \
--data-raw '{
  "merchant_id": "8739528",
  "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
  "txnid": "HC_TPV_20240315_001",
  "amount": "1500.00",
  "productinfo": "Loan EMI Payment - March 2024",
  "firstname": "Rajesh",
  "email": "rajesh.kumar@example.com",
  "phone": "9876543210",
  "surl": "https://yoursite.com/success",
  "furl": "https://yoursite.com/failure",
  "curl": "https://yoursite.com/cancel",
  "udf1": "session_12345",
  "udf2": "1370625260",
  "udf3": "loan-ref-ABC123",
  "udf4": "",
  "udf5": "whatsapp",
  "beneficiarydetail": "{\"ifscCode\":\"ICIC0001234\",\"accountNumber\":\"123456789012\",\"accountHolderName\":\"RAJESH KUMAR\"}",
  "hash": "a1b2c3d4e5f6789..."
}'
```
```python
import requests
import json

url = "https://test-partnerapilayer.payu.in/apilayer/partner/payments"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {final_access_token}"
}

beneficiary_details = {
    "ifscCode": "ICIC0001234",
    "accountNumber": "123456789012",
    "accountHolderName": "RAJESH KUMAR"
}

payload = {
    "merchant_id": "8739528",
    "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
    "txnid": "HC_TPV_20240315_001",
    "amount": "1500.00",
    "productinfo": "Loan EMI Payment - March 2024",
    "firstname": "Rajesh",
    "email": "rajesh.kumar@example.com",
    "phone": "9876543210",
    "surl": "https://yoursite.com/success",
    "furl": "https://yoursite.com/failure",
    "curl": "https://yoursite.com/cancel",
    "udf1": "session_12345",
    "udf2": "1370625260",
    "udf3": "loan-ref-ABC123",
    "udf4": "",
    "udf5": "whatsapp",
    "beneficiarydetail": json.dumps(beneficiary_details),
    "hash": payment_hash
}

response = requests.post(url, headers=headers, json=payload)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")

if response.status_code == 200:
    redirect_uri = response.json().get("redirectUri")
    print(f"Redirect URI: {redirect_uri}")
```
```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import org.json.JSONObject;

public class InitiateHostedCheckoutTPV {
    public static void main(String[] args) throws Exception {
        String url = "https://test-partnerapilayer.payu.in/apilayer/partner/payments";
        
        JSONObject beneficiaryDetail = new JSONObject();
        beneficiaryDetail.put("ifscCode", "ICIC0001234");
        beneficiaryDetail.put("accountNumber", "123456789012");
        beneficiaryDetail.put("accountHolderName", "RAJESH KUMAR");
        
        JSONObject payload = new JSONObject();
        payload.put("merchant_id", "8739528");
        payload.put("reseller_id", "11ee-0e7e-5403fde2-9523-0a696b110fde");
        payload.put("txnid", "HC_TPV_20240315_001");
        payload.put("amount", "1500.00");
        payload.put("productinfo", "Loan EMI Payment - March 2024");
        payload.put("firstname", "Rajesh");
        payload.put("email", "rajesh.kumar@example.com");
        payload.put("phone", "9876543210");
        payload.put("surl", "https://yoursite.com/success");
        payload.put("furl", "https://yoursite.com/failure");
        payload.put("curl", "https://yoursite.com/cancel");
        payload.put("udf1", "session_12345");
        payload.put("udf2", "1370625260");
        payload.put("udf3", "loan-ref-ABC123");
        payload.put("udf4", "");
        payload.put("udf5", "whatsapp");
        payload.put("beneficiarydetail", beneficiaryDetail.toString());
        payload.put("hash", paymentHash);
        
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .header("Authorization", "Bearer " + finalAccessToken)
            .POST(HttpRequest.BodyPublishers.ofString(payload.toString()))
            .build();
        
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        
        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response: " + response.body());
        
        if (response.statusCode() == 200) {
            JSONObject responseJson = new JSONObject(response.body());
            String redirectUri = responseJson.getString("redirectUri");
            System.out.println("Redirect URI: " + redirectUri);
        }
    }
}
```
```php
<?php
$url = "https://test-partnerapilayer.payu.in/apilayer/partner/payments";

$beneficiaryDetails = array(
    "ifscCode" => "ICIC0001234",
    "accountNumber" => "123456789012",
    "accountHolderName" => "RAJESH KUMAR"
);

$payload = array(
    "merchant_id" => "8739528",
    "reseller_id" => "11ee-0e7e-5403fde2-9523-0a696b110fde",
    "txnid" => "HC_TPV_20240315_001",
    "amount" => "1500.00",
    "productinfo" => "Loan EMI Payment - March 2024",
    "firstname" => "Rajesh",
    "email" => "rajesh.kumar@example.com",
    "phone" => "9876543210",
    "surl" => "https://yoursite.com/success",
    "furl" => "https://yoursite.com/failure",
    "curl" => "https://yoursite.com/cancel",
    "udf1" => "session_12345",
    "udf2" => "1370625260",
    "udf3" => "loan-ref-ABC123",
    "udf4" => "",
    "udf5" => "whatsapp",
    "beneficiarydetail" => json_encode($beneficiaryDetails),
    "hash" => $paymentHash
);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    "Content-Type: application/json",
    "Authorization: Bearer " . $finalAccessToken
));

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";

if ($httpCode == 200) {
    $data = json_decode($response, true);
    $redirectUri = $data['redirectUri'];
    echo "Redirect URI: " . $redirectUri . "\n";
}
?>
```

***

### Step 2.4: Handle Payment Response & Redirect Customer

**Success Response:**

```json
{
  "status": "success",
  "redirectUri": "https://secure.payu.in/_payment?token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "txnid": "HC_TPV_20240315_001",
  "merchant_id": "8739528"
}
```

**Response Fields:**

| Field       | Description                                                   |
| ----------- | ------------------------------------------------------------- |
| status      | Request status (`"success"` or `"failure"`)                   |
| redirectUri | PayU hosted checkout URL (redirect customer here immediately) |
| txnid       | Transaction ID from request                                   |
| merchant_id | Merchant ID from request                                      |

**Next Steps:**

1. **Extract&#x20;**`redirectUri` from the response
2. **Immediately redirect the customer** to this URL in their browser:
   ```javascript
   window.location.href = redirectUri;
   ```
3. Customer lands on PayU's hosted checkout page
4. Customer sees payment method options (cards, UPI, net banking, wallets)
5. **If customer selects UPI:**
   - PayU internally activates TPV mode (`bankcode=INTTPV`, `api_version=6`)
   - Customer completes UPI authentication
   - PayU validates customer's UPI account against `beneficiarydetail`
   - Payment succeeds only if account matches
6. **If customer selects Cards/Net Banking/Wallets:**
   - Standard payment flow (no TPV validation)
   - Payment proceeds normally

<Note>
**TPV Validation Logic:**

When customer selects UPI on the hosted checkout:
- ✅ **Account Match:** Customer's UPI account is linked to the beneficiary account → Payment succeeds
- ❌ **Account Mismatch:** Customer's UPI account differs from beneficiary account → Payment fails with validation error
- ℹ️ **Other Methods:** Cards, net banking, wallets bypass TPV validation (payment proceeds normally)
</Note>

***

## Step 3: Customer Completes Payment on Hosted Checkout

### Hosted Checkout Flow with TPV

1. **Customer lands on PayU's hosted checkout page**
   - Merchant branding displayed (logo, colors)
   - Transaction details shown (amount, product description)
   - Payment method options presented

2. **Customer selects payment method:**

   **Option A: UPI Selected (TPV Validation Applies)**

   - Customer chooses UPI payment
   - PayU presents UPI app selection or VPA entry
   - Customer authenticates with UPI PIN
   - **PayU validates UPI account against beneficiarydetail:**
     - If account matches: Payment succeeds
     - If account mismatch: Error message displayed, payment fails

   **Option B: Card/Net Banking/Wallet Selected (No TPV)**

   - Standard payment authentication
   - 3D Secure OTP for cards
   - Bank login for net banking
   - Wallet PIN/OTP for wallets
   - Payment proceeds without account validation

3. **Payment completion**
   - PayU processes the transaction
   - Transaction status determined (success/failure)

4. **Customer redirect**
   - Success → Redirected to `surl`
   - Failure → Redirected to `furl`
   - Cancel → Redirected to `curl`

***

## Step 4: Receive Callback on Success/Failure/Cancel URL

When PayU redirects the customer to your callback URL, transaction details are appended as **POST parameters**.

### Success URL (surl) Parameters

**Expected POST Parameters:**

| Parameter      | Description         | Example                                                |
| -------------- | ------------------- | ------------------------------------------------------ |
| mihpayid       | PayU transaction ID | `"403993715529111111"`                                 |
| txnid          | Your transaction ID | `"HC_TPV_20240315_001"`                                |
| status         | Transaction status  | `"success"`                                            |
| amount         | Transaction amount  | `"1500.00"`                                            |
| productinfo    | Product description | `"Loan EMI Payment - March 2024"`                      |
| firstname      | Customer first name | `"Rajesh"`                                             |
| email          | Customer email      | `"rajesh.kumar@example.com"`                           |
| phone          | Customer phone      | `"9876543210"`                                         |
| mode           | Payment mode        | `"UPI"` (for TPV), `"CC"` (card), `"NB"` (net banking) |
| bankcode       | Bank code           | `"INTTPV"` (for successful UPI TPV payments)           |
| unmappedstatus | Payment status      | `"captured"` (success), `"failed"`, `"bounced"`        |
| hash           | Response hash       | SHA-512 hash for verification                          |
| udf1-udf5      | User-defined fields | Values from request                                    |

<Note>
**UPI TPV Indicator:**

When a UPI TPV payment succeeds, the callback includes:
- `mode: "UPI"`
- `bankcode: "INTTPV"` — Confirms TPV validation passed
- `unmappedstatus: "captured"` — Payment captured successfully
</Note>

**Sample Success Callback (POST to surl):**

```
mihpayid=403993715529111111
txnid=HC_TPV_20240315_001
status=success
amount=1500.00
productinfo=Loan EMI Payment - March 2024
firstname=Rajesh
email=rajesh.kumar@example.com
phone=9876543210
mode=UPI
bankcode=INTTPV
unmappedstatus=captured
hash=a1b2c3d4e5f6...
udf1=session_12345
udf2=1370625260
udf3=loan-ref-ABC123
udf4=
udf5=whatsapp
```

### Failure URL (furl) Parameters

When payment fails (including UPI TPV account mismatch), customer is redirected to `furl` with:

```
mihpayid=403993715529222222
txnid=HC_TPV_20240315_001
status=failure
amount=1500.00
error=TPV_ACCOUNT_MISMATCH
error_Message=Beneficiary account validation failed
mode=UPI
bankcode=INTTPV
unmappedstatus=bounced
hash=x1y2z3...
```

**Common TPV Failure Reasons:**

| Error Code                     | Description                                              | Resolution                                                                   |
| ------------------------------ | -------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `TPV_ACCOUNT_MISMATCH`         | Customer's UPI account doesn't match beneficiary details | Verify beneficiary account details, ask customer to pay from correct account |
| `TPV_VALIDATION_FAILED`        | Beneficiary details validation error                     | Check IFSC code, account number format                                       |
| `ACCOUNT_HOLDER_NAME_MISMATCH` | Name on UPI account doesn't match `accountHolderName`    | Ensure exact name match (case-insensitive, spaces ignored)                   |

### Cancel URL (curl) Parameters

When customer cancels payment:

```
mihpayid=
txnid=HC_TPV_20240315_001
status=cancel
amount=1500.00
unmappedstatus=userCancelled
```

<Warning>
**Important: Always Verify Response Hash**

Never trust callback parameters without hash verification. Compute the reverse hash and compare with the received `hash` parameter. See [Step 5.2: Verify Webhook Hash](#step-52-verify-webhook-hash) for the formula.
</Warning>

***

## Step 5: Receive and Verify Partner Webhook

PayU sends real-time payment status notifications to your configured partner webhook URLs.

### Step 5.1: Partner Webhook Delivery

**Webhook URLs (configured in PayU system):**

- `partner_webhook_success` — Triggered on successful payment
- `partner_webhook_failure` — Triggered on failed payment
- `partner_webhook_cancelled` — Triggered when customer cancels

**Webhook Payload (POST request):**

```json
{
  "mihpayid": "403993715529111111",
  "txnid": "HC_TPV_20240315_001",
  "status": "success",
  "amount": "1500.00",
  "productinfo": "Loan EMI Payment - March 2024",
  "firstname": "Rajesh",
  "email": "rajesh.kumar@example.com",
  "phone": "9876543210",
  "mode": "UPI",
  "bankcode": "INTTPV",
  "unmappedstatus": "captured",
  "merchant_id": "8739528",
  "udf1": "session_12345",
  "udf2": "1370625260",
  "udf3": "loan-ref-ABC123",
  "udf4": "",
  "udf5": "whatsapp",
  "hash": "a1b2c3d4e5f6...",
  "payment_source": "payu"
}
```

**Key TPV Fields in Webhook:**

| Field          | Value for TPV                                   | Description                    |
| -------------- | ----------------------------------------------- | ------------------------------ |
| mode           | `"UPI"`                                         | Payment method used            |
| bankcode       | `"INTTPV"`                                      | Confirms TPV validation passed |
| unmappedstatus | `"captured"` (success) or `"bounced"` (failure) | Final payment status           |

***

### Step 5.2: Verify Webhook Hash

Always verify the webhook hash before processing payment status.

**Reverse Hash Formula:**

```
client_secret|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|merchant_id
```

**Notes:**

- Five pipes after `status`
- Fields in reverse order compared to request hash
- Use OAuth `client_secret` (same as request hash)

<Verify_Partner_Payment_Webhook_Hash />

## **S**tep 6: Verify Payment Status

Always call the Verify Payment API as the final source of truth for transaction status.

**Endpoint:**

| Environment | URL                                                                   |
| ----------- | --------------------------------------------------------------------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment` |
| Production  | `https://api.payu.in/partner/verifyPayment`                           |

**Headers:**

```
Content-Type: application/json
Authorization: Bearer <FINAL_ACCESS_TOKEN>
```

**Request Body:**

```json
{
  "merchant_id": "8739528",
  "txnid": "HC_TPV_20240315_001"
}
```

**Sample Request:**

```bash
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...' \
--data-raw '{
  "merchant_id": "8739528",
  "txnid": "HC_TPV_20240315_001"
}'
```
```python
import requests

url = "https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {final_access_token}"
}

payload = {
    "merchant_id": "8739528",
    "txnid": "HC_TPV_20240315_001"
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    verify_data = response.json()
    print(f"Payment Status: {verify_data.get('status')}")
    print(f"Bank Code: {verify_data.get('bankcode')}")
    print(f"Amount: {verify_data.get('amount')}")
    print(f"PayU ID: {verify_data.get('mihpayid')}")
    
    if verify_data.get('bankcode') == 'INTTPV':
        print("✅ UPI TPV payment confirmed")
```

**Success Response:**

```json
{
  "status": "success",
  "mihpayid": "403993715529111111",
  "txnid": "HC_TPV_20240315_001",
  "amount": "1500.00",
  "productinfo": "Loan EMI Payment - March 2024",
  "firstname": "Rajesh",
  "email": "rajesh.kumar@example.com",
  "phone": "9876543210",
  "mode": "UPI",
  "bankcode": "INTTPV",
  "unmappedstatus": "captured",
  "payment_source": "payu",
  "merchant_id": "8739528"
}
```

**Response Fields for UPI TPV:**

| Field          | Value               | Description                        |
| -------------- | ------------------- | ---------------------------------- |
| status         | `"success"`         | Payment succeeded                  |
| bankcode       | `"INTTPV"`          | Confirms UPI TPV validation passed |
| mode           | `"UPI"`             | Payment method                     |
| unmappedstatus | `"captured"`        | Payment captured successfully      |
| mihpayid       | PayU transaction ID | Unique PayU reference              |

***

## Testing Hosted Checkout with UPI TPV

### Test Environment Setup

Use UAT credentials and test beneficiary account details provided by PayU.

<Warning>
**Test Data Requirements:**

- Request test beneficiary account details from PayU support for sandbox testing
- Real production accounts cannot be used in UAT
- Test UPI accounts must be pre-configured by PayU to match test beneficiary details
</Warning>

### Test Scenarios

#### Scenario 1: UPI TPV Success (Account Match)

**Test Flow:**

1. Initiate payment with test beneficiary details
2. Redirect customer to hosted checkout
3. Customer selects UPI
4. Customer pays from UPI account linked to test beneficiary account
5. Expected: Payment succeeds, `bankcode=INTTPV` in webhook

**Expected Results:**

- ✅ Webhook received with `status=success`, `bankcode=INTTPV`
- ✅ Verify Payment API confirms `unmappedstatus=captured`
- ✅ Customer redirected to `surl`

***

#### Scenario 2: UPI TPV Failure (Account Mismatch)

**Test Flow:**

1. Initiate payment with test beneficiary details
2. Redirect customer to hosted checkout
3. Customer selects UPI
4. Customer pays from different UPI account (not linked to beneficiary account)
5. Expected: Payment fails with TPV validation error

**Expected Results:**

- ❌ Webhook received with `status=failure`, `error=TPV_ACCOUNT_MISMATCH`
- ❌ Verify Payment API confirms `unmappedstatus=bounced`
- ❌ Customer redirected to `furl`

***

#### Scenario 3: Card Payment (No TPV Validation)

**Test Flow:**

1. Initiate payment with beneficiary details included
2. Redirect customer to hosted checkout
3. Customer selects Credit Card
4. Customer completes card payment
5. Expected: Payment succeeds without TPV validation

**Expected Results:**

- ✅ Webhook received with `status=success`, `mode=CC`, `bankcode` ≠ `INTTPV`
- ✅ TPV validation bypassed for card payments
- ✅ Customer redirected to `surl`

**Test Cards:**

| Card Number      | Expiry  | CVV | Expected Result |
| ---------------- | ------- | --- | --------------- |
| 5123456789012346 | 05/2026 | 123 | Success         |
| 4012001037141112 | 12/2025 | 123 | Success         |
| 6011111111111117 | 06/2027 | 999 | Failure         |

***

#### Scenario 4: Net Banking (No TPV Validation)

**Test Flow:**

1. Initiate payment with beneficiary details
2. Customer selects Net Banking
3. Customer completes net banking authentication
4. Expected: Payment succeeds without TPV validation

**Expected Results:**

- ✅ Webhook received with `status=success`, `mode=NB`
- ✅ TPV validation bypassed for net banking
- ✅ Customer redirected to `surl`

***

## Reconciliation

### Daily Reconciliation Checklist

For each UPI TPV transaction:

- [ ] Match `txnid` between your system, webhook, and Verify Payment API
- [ ] Confirm `mihpayid` (PayU transaction ID) is consistent
- [ ] Verify `amount` matches original request
- [ ] Check `bankcode=INTTPV` for UPI TPV transactions
- [ ] Validate `unmappedstatus=captured` for successful payments
- [ ] Cross-reference with PayU dashboard settlement reports
- [ ] Flag any discrepancies for manual review

### Key Reconciliation Fields

| Field          | Source              | Use                                 |
| -------------- | ------------------- | ----------------------------------- |
| txnid          | Your system         | Primary key for matching            |
| mihpayid       | PayU                | PayU's unique reference             |
| amount         | Request vs response | Amount verification                 |
| bankcode       | Webhook/Verify API  | TPV confirmation (must be `INTTPV`) |
| unmappedstatus | Webhook/Verify API  | Final payment status                |

***

## Common Errors and Troubleshooting

### Error: Invalid hash

**Cause:** Hash mismatch between request and PayU's computed hash

**Resolution:**

1. Verify hash formula (6 pipes between `udf5` and `client_secret`)
2. Ensure `beneficiarydetail` is **NOT** included in hash
3. Use OAuth `client_secret` (not merchant salt)
4. Check for empty fields (use empty strings, not null)
5. Ensure SHA-512 lowercase hexadecimal output

***

### Error: TPV_ACCOUNT_MISMATCH

**Cause:** Customer's UPI account doesn't match beneficiary details

**Resolution:**

1. Verify `beneficiarydetail` IFSC code is correct
2. Check `accountNumber` format (no spaces or special characters)
3. Ensure `accountHolderName` matches exactly (case-insensitive)
4. Ask customer to pay from the registered beneficiary account
5. For testing: Use test beneficiary accounts provided by PayU

***

### Error: Beneficiary detail validation failed

**Cause:** Invalid beneficiary account details format

**Resolution:**

1. Check IFSC code is 11 characters (e.g., `ICIC0001234`)
2. Verify account number is numeric
3. Ensure `beneficiarydetail` is a valid JSON string
4. Confirm account holder name matches bank records
5. Test with PayU-provided test beneficiary data first

***

### Error: UPI TPV feature not enabled

**Cause:** Your merchant account is not enabled for UPI TPV

**Resolution:**

1. Contact PayU support to enable UPI TPV feature
2. Provide your `merchant_id` and `reseller_id`
3. Specify use case and compliance requirements
4. Wait for confirmation before testing

***

### Error: Auth token is not valid

**Cause:** OAuth token expired or invalid

**Resolution:**

1. Regenerate OAuth token (complete 3-step flow)
2. Verify token has required scopes (`partner_payments`)
3. Check token expiry (default: 3600 seconds)
4. Ensure Authorization header format: `Bearer <token>`

***

## Going Live Checklist

Before switching to production:

### Credentials Update

- [ ] Production OAuth `client_id` and `client_secret` obtained
- [ ] Production `merchant_id` and `reseller_id` configured
- [ ] Production endpoints updated in code
- [ ] UPI TPV feature confirmed enabled in production

### Beneficiary Data

- [ ] Real beneficiary account details collection process in place
- [ ] IFSC code validation implemented
- [ ] Account holder name normalization logic added
- [ ] Beneficiary data storage secured (encrypted at rest)

### Testing Complete

- [ ] All test scenarios passed in UAT
- [ ] UPI TPV success and failure flows tested
- [ ] Card/net banking bypass confirmed
- [ ] Webhook hash verification working
- [ ] Verify Payment API integration tested

### Compliance

- [ ] Legal review of TPV usage completed
- [ ] Customer consent for beneficiary validation obtained
- [ ] Privacy policy updated with account validation disclosure
- [ ] Audit trail for TPV transactions in place

### Production Validation

- [ ] Conduct live transaction with small amount
- [ ] Verify production webhook delivery
- [ ] Confirm production Verify Payment API works
- [ ] Check production settlement in PayU dashboard

***

## Related Documentation

- [Partner Payments Overview](doc:partner-payments-overview)
- [Partner Payments UPI Intent Integration](doc:partner-payments-upi-intent-integration)
- [Partner Payments UPI TPV Integration](doc:partner-payments-upi-tpv-integration)
- [Partner Payments Hosted Checkout Integration](doc:partner-payments-hosted-checkout-integration)
- [Testing and Troubleshooting Guide](doc:testing-and-troubleshooting-partner-integration)
- [OAuth Authentication Guide](ref:getting-access-token)
- [Verify Payment API](doc:verify-payment-api)

***

## Support

For UPI TPV feature enablement, test beneficiary accounts, or technical issues, contact PayU Partner Support with:

- Your `reseller_id` (partner UUID)
- Merchant ID(s) involved
- Detailed use case description
- Sample `txnid` and timestamp (for transaction issues)
- Error messages and logs

**Support Channels:**

- Partner Portal: [https://partner.payu.in/support](https://partner.payu.in/support)
- Email: [partner-support@payu.in](mailto:partner-support@payu.in)
