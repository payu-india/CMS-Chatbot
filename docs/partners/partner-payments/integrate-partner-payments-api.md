---
title: Integrate Partner Payments API
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
This section describes how to integrate PayU's Partner Payments API to enable payment acceptance on behalf of your merchants. The integration covers OAuth token generation, payment initiation, webhook configuration, and payment verification.

## Prerequisites

Before you begin, ensure you have:

<Note>
✅ Active PayU Partner account registered as a reseller  
✅ Partner OAuth credentials: `client_id` and `client_secret` issued by PayU  
✅ Reseller credentials: `username` and `password` for OAuth password grant  
✅ Merchant linked to your partner account with valid `merchant_id`  
✅ Partner `reseller_uuid` (also called `partner_uuid`)  
✅ OAuth scopes enabled: `create_payment_links`, `partner_payment_links`, `partner_payments`  
✅ Database access to configure webhook tables (if using webhooks)
</Note>

***

<Cards columns="3">
  <Card title="1. Generate OAuth Access Token" href="#step-1-generate-oauth-access-token">
    Complete the three-step OAuth flow to obtain a bearer token with `partner_payments` scope:

    1. Call the **password grant endpoint** with reseller credentials to get an initial access token
    2. Use that token to **request an authorization code** for your merchant
    3. **Exchange the authorization code** for the final access token

    Store this token securely and reuse it until expiration (typically **3600 seconds**)

    **What you need:** Partner `client_id`, `client_secret`, reseller username & password, `merchant_id`, `reseller_uuid`

    ✅ **Checkpoint:** JSON response with `access_token`, `token_type: "Bearer"`, and `expires_in: 3600`


  </Card>

  <Card title="2. Initiate Payment" href="#step-2-initiate-payment">
    Prepare and POST your payment request to the `/partner/payments` endpoint:

    1. Assemble the payload with required parameters: `txnid`, `amount`, `productinfo`, `phone`
    2. Compute the **SHA-512 payment hash** using the formula:
       `merchant_id|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||client_secret`
       _(note the six consecutive pipes before&#x20;_`client_secret`_)_
    3. For **UPI Intent S2S**, include `txn_s2s_flow=4`, `s2s_client_ip`, and `s2s_device_info`
    4. POST with header: `Authorization: Bearer <token>`

    **What you need:** Final access token, transaction details, `merchant_id`, `reseller_id`, `client_secret`

    ✅ **Checkpoint:** `200` response with `metaData.txnStatus` and either `result.intentURIData` (S2S) or `redirectUri` (redirect flow)


  </Card>

  <Card title="3. Configure and Receive Webhooks" href="#step-3-configure-and-receive-webhooks">
    Set up partner webhook routing and verify incoming payloads:

    1. Insert a row into `partner_webhook_urls` with your `partner_uuid`, webhook URLs for success/failure/cancelled/default, and set `is_payment_webhook_enabled=true`
    2. Optionally insert into `partner_merchant_params` with `key=disable_core_payment_webhook_url` and `value='1'` to prevent fallback to merchant core webhooks
    3. On receipt, extract all fields from the payload `Map<String,String>`
    4. Verify webhook hash via reverse formula (SHA-512):
       `client_secret|status|||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|merchant_id`
    5. Compare digest **case-insensitively** with the `hash` field in the payload

    **What you need:** DB access to `partner_webhook_urls` & `partner_merchant_params` tables, partner webhook endpoint URLs

    ✅ **Checkpoint:** Webhook endpoint receives POST requests with complete transaction data and hash verification returns `true`


  </Card>

  <Card title="4. Verify the Payment" href="#step-4-verify-the-payment">
    Confirm the final transaction status via the verify payment API:

    1. Generate the verify hash using SHA-512 on:
       `merchant_id|verify_payment|txnid|client_secret`
    2. Call `POST /partner/verifyPayment` with header `Authorization: Bearer <token>`
    3. Pass `txnid`, `merchant_id`, `reseller_id`, and the computed `hash` in the request body
    4. Parse the response to extract `txnStatus`, `mihpayid` (PayU payment ID), and other transaction details
    5. **Reconcile** the verified status against webhook data received in the previous step

    **What you need:** `txnid`, `merchant_id`, `reseller_id`, `client_secret`, final access token

    ✅ **Checkpoint:** Verified transaction status (`success`/`failure`/`pending`) returned with `mihpayid` for reconciliation


  </Card>
</Cards>

***

## Step 1: Generate OAuth Access Token

Partner Payments API uses OAuth 2.0 authentication. You must complete a three-step token generation flow to obtain an access token with the `partner_payments` scope.

### Step 1.1: Password Grant (Get Initial Token)

Call the OAuth token endpoint using password grant type with your reseller credentials.

**Endpoint:** `POST /oauth/token`

**Environment URLs:**

| Environment | URL                                        |
| ----------- | ------------------------------------------ |
| Test        | `https://uat-accounts.payu.in/oauth/token` |
| Production  | `https://accounts.payu.in/oauth/token`     |

**Request Headers:**

```
Content-Type: application/x-www-form-urlencoded
```

**Request Parameters (form-urlencoded):**

<table>
  <thead>
    <tr>
      <th align="left">Parameter</th>
      <th align="left">Type &amp; Description</th>
      <th align="left">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>client_id</td>
      <td><strong>String</strong><br>OAuth client ID issued by PayU to the partner.</td>
      <td>abc123clientid</td>
    </tr>
    <tr>
      <td>client_secret</td>
      <td><strong>String</strong><br>OAuth client secret issued by PayU to the partner.</td>
      <td>s3cr3t_v4lue_xyz</td>
    </tr>
    <tr>
      <td>grant_type</td>
      <td><strong>String</strong><br>Must be <code>password</code> for this step.</td>
      <td>password</td>
    </tr>
    <tr>
      <td>username</td>
      <td><strong>String</strong><br>Reseller username.</td>
      <td>reseller_user</td>
    </tr>
    <tr>
      <td>password</td>
      <td><strong>String</strong><br>Reseller password.</td>
      <td>P@ssw0rd!</td>
    </tr>
    <tr>
      <td>scope</td>
      <td><strong>String</strong><br>Must be <code>hub_session</code> for initial token.</td>
      <td>hub_session</td>
    </tr>
  </tbody>
</table>

**Sample Request:**

```bash
curl --location 'https://uat-accounts.payu.in/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=YOUR_CLIENT_ID' \
--data-urlencode 'client_secret=YOUR_CLIENT_SECRET' \
--data-urlencode 'grant_type=password' \
--data-urlencode 'username=YOUR_RESELLER_USERNAME' \
--data-urlencode 'password=YOUR_RESELLER_PASSWORD' \
--data-urlencode 'scope=hub_session'
```

**Sample Response:**

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "hub_session"
}
```

<Note>
**Important:** Store the `access_token` value. You'll use this token in Step 1.2 to request an authorization code.
</Note>

***

### Step 1.2: Request Authorization Code for Merchant

Use the access token from Step 1.1 to obtain an authorization code for your specific merchant.

**Endpoint:** `POST /api/v1/merchants/auth_code`

**Environment URLs:**

| Environment | URL                                                      |
| ----------- | -------------------------------------------------------- |
| Test        | `https://uat-partner.payu.in/api/v1/merchants/auth_code` |
| Production  | `https://partner.payu.in/api/v1/merchants/auth_code`     |

**Request Headers:**

```
Authorization: Bearer <ACCESS_TOKEN_FROM_STEP_1>
Content-Type: application/x-www-form-urlencoded
```

**Request Parameters (form-urlencoded):**

| Parameter       | Type & Description                                                  | Example                                                     |
| --------------- | ------------------------------------------------------------------- | ----------------------------------------------------------- |
| `merchant_id`   | integer — PayU merchant ID for whom payment will be initiated       | 8739528                                                     |
| `reseller_uuid` | string — Your partner/reseller UUID                                 | 11ee-0e7e-5403fde2-9523-0a696b110fde                        |
| `redirect_uri`  | string — OAuth redirect URI (typically your partner dashboard URL)  | [https://uat-partner.payu.in](https://uat-partner.payu.in)  |
| `scopes`        | string — Space-separated OAuth scopes required for Partner Payments | create_payment_links partner_payment_links partner_payments |

**Sample Request:**

```bash
curl --location 'https://uat-partner.payu.in/api/v1/merchants/auth_code' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'merchant_id=8739528' \
--data-urlencode 'reseller_uuid=11ee-0e7e-5403fde2-9523-0a696b110fde' \
--data-urlencode 'redirect_uri=https://uat-partner.payu.in' \
--data-urlencode 'scopes=create_payment_links partner_payment_links partner_payments'
```

**Sample Response:**

```json
{
  "data": {
    "id": "1340444",
    "type": "authorization-codes",
    "attributes": {
      "code": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
      "redirect-uri": "https://uat-partner.payu.in"
    }
  }
}
```

<Note>
**Important:** Extract the `attributes.code` value from the response. This is the authorization code you'll exchange in Step 1.3.
</Note>

***

### Step 1.3: Exchange Authorization Code for Final Access Token

Exchange the authorization code for the final access token with `partner_payments` scope.

**Endpoint:** `POST /oauth/token`

**Environment URLs:**

| Environment | URL                                        |
| ----------- | ------------------------------------------ |
| Test        | `https://uat-accounts.payu.in/oauth/token` |
| Production  | `https://accounts.payu.in/oauth/token`     |

**Request Headers:**

```
Content-Type: application/x-www-form-urlencoded
```

**Request Parameters (form-urlencoded):**

| Parameter       | Type & Description                          | Example                                                    |
| --------------- | ------------------------------------------- | ---------------------------------------------------------- |
| `client_id`     | string — Your OAuth client ID               | YOUR_CLIENT_ID                                             |
| `client_secret` | string — Your OAuth client secret           | YOUR_CLIENT_SECRET                                         |
| `grant_type`    | string — Must be `authorization_code`       | authorization_code                                         |
| `code`          | string — Authorization code from Step 1.2   | a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6                           |
| `redirect_uri`  | string — Same redirect URI used in Step 1.2 | [https://uat-partner.payu.in](https://uat-partner.payu.in) |

**Sample Request:**

```bash
curl --location 'https://uat-accounts.payu.in/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=YOUR_CLIENT_ID' \
--data-urlencode 'client_secret=YOUR_CLIENT_SECRET' \
--data-urlencode 'grant_type=authorization_code' \
--data-urlencode 'code=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6' \
--data-urlencode 'redirect_uri=https://uat-partner.payu.in'
```

**Sample Response:**

```json
{
  "access_token": "039e0d1d70f467f946e2d73bd43868df856cfaa352ea54591a76bfc4a08d3487",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

<Success>
**Success!** The `access_token` in this response is your **final access token**. Use this token in the `Authorization: Bearer` header for all Partner Payments API calls (`/partner/payments`, `/partner/verifyPayment`).
</Success>

<Warning>
**Token Expiry:** Access tokens typically expire after 3600 seconds (1 hour). When you receive a `401 Unauthorized` response, regenerate the token by repeating all three steps.
</Warning>

***

## Step 2: Initiate Payment

Now that you have the final OAuth access token, you can initiate payments on behalf of your merchant.

### Step 2.1: Prepare the Request Parameters

Collect the required payment details and partner identifiers:

**Mandatory Parameters:**

<table>
<thead>
<tr>
<th align="left">Parameter</th>
<th align="left">Type &amp; Description</th>
<th align="left">Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>txnid</code></td>
<td>string — Unique transaction ID generated by partner</td>
<td>28408067218883788</td>
</tr>
<tr>
<td><code>amount</code></td>
<td>string — Transaction amount</td>
<td>518.02</td>
</tr>
<tr>
<td><code>productinfo</code></td>
<td>string — Product description</td>
<td>Payment for service</td>
</tr>
<tr>
<td><code>phone</code></td>
<td>string — Customer phone number (10 digits)</td>
<td>919820988398</td>
</tr>
<tr>
<td><code>merchant_id</code></td>
<td>integer — PayU merchant ID</td>
<td>8739528</td>
</tr>
<tr>
<td><code>reseller_id</code></td>
<td>string — Partner/reseller UUID</td>
<td>11ee-0e7e-5403fde2-9523-0a696b110fde</td>
</tr>
<tr>
<td><code>hash</code></td>
<td>string — SHA-512 hash computed using payment request formula</td>
<td>(computed hash value)</td>
</tr>
</tbody>
</table>

**Optional Parameters (Recommended):**

- `firstname`, `lastname`, `email` — Customer details
- `udf1` through `udf5` — Custom fields for partner-specific data
- `surl`, `furl`, `curl` — Redirect URLs for success/failure/cancel (required for redirect flows)

**UPI Intent S2S Parameters (Mandatory when&#x20;**`txn_s2s_flow=4`**):**

| Parameter         | Type & Description                                           | Example                                  |
| :---------------- | :----------------------------------------------------------- | :--------------------------------------- |
| `txn_s2s_flow`    | string — Set to "4" for UPI Intent S2S                       | 4                                        |
| `s2s_client_ip`   | string — Customer IP address (mandatory when txn_s2s_flow=4) | 157.240.22.9                             |
| `s2s_device_info` | string — Device user-agent (mandatory when txn_s2s_flow=4)   | Mozilla/5.0 (iPhone) AppleWebKit/602.4.6 |

<Warning>
**Critical:** When `txn_s2s_flow` is set to `"4"`, the fields `s2s_client_ip` and `s2s_device_info` become **mandatory**. Omitting them will result in an error: *"s2s_client_ip or s2s_device_info mandatory"*.
</Warning>

***

### Step 2.2: Generate Payment Request Hash

Compute the SHA-512 hash using this exact formula:

```
merchant_id|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||client_secret
```

<Warning>
**Important Hash Notes:**
- There are **six consecutive pipe characters** (`||||||`) between `udf5` and `client_secret`
- Use your OAuth `client_secret`, **not** the merchant salt
- For empty fields (e.g., `firstname`, `email`, `udf1`), use empty strings (resulting in consecutive pipes)
- Compute SHA-512 and convert to **lowercase hexadecimal**
</Warning>

**Hash Generation Example (Java):**

```java
import java.security.MessageDigest;

public class PartnerPaymentHash {
    public static String generateHash(
        int merchantId, String txnid, String amount, String productinfo,
        String firstname, String email, String udf1, String udf2, String udf3,
        String udf4, String udf5, String clientSecret
    ) throws Exception {
        
        String hashString = merchantId + "|" + txnid + "|" + amount + "|" + productinfo + "|" +
                           getOrEmpty(firstname) + "|" + getOrEmpty(email) + "|" +
                           getOrEmpty(udf1) + "|" + getOrEmpty(udf2) + "|" + getOrEmpty(udf3) + "|" +
                           getOrEmpty(udf4) + "|" + getOrEmpty(udf5) + "||||||" + clientSecret;
        
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] digest = md.digest(hashString.getBytes("UTF-8"));
        
        StringBuilder hex = new StringBuilder();
        for (byte b : digest) {
            String h = Integer.toHexString(0xFF & b);
            if (h.length() == 1) hex.append("0");
            hex.append(h);
        }
        return hex.toString();
    }
    
    private static String getOrEmpty(String value) {
        return (value == null || value.isEmpty()) ? "" : value;
    }
}
```

***

### Step 2.3: POST the Payment Request

Call the Partner Payments endpoint with the computed hash and all required parameters.

**Endpoint:** `POST /partner/payments`

**Environment URLs:**

| Environment | URL                                                              |
| ----------- | ---------------------------------------------------------------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer/partner/payments` |
| Production  | `https://api.payu.in/partner/payments`                           |

**Request Headers:**

```
Authorization: Bearer <FINAL_ACCESS_TOKEN>
Content-Type: application/json
```

**Sample Request (UPI Intent S2S):**

```bash
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/payments' \
--header 'Authorization: Bearer 039e0d1d70f467f946e2d73bd43868df856cfaa352ea54591a76bfc4a08d3487' \
--header 'Content-Type: application/json' \
--data '{
  "txnid": "28471834809170981",
  "amount": "518.02",
  "productinfo": "28471834809170981",
  "firstname": "",
  "email": "",
  "phone": "919820988398",
  "merchant_id": 8739528,
  "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
  "udf1": "",
  "udf2": "1370625260",
  "udf3": "r-hway-LDnTRBuFK8STTTeTEc2SuD",
  "udf4": "",
  "udf5": "whatsapp",
  "txn_s2s_flow": "4",
  "s2s_client_ip": "157.240.22.9",
  "s2s_device_info": "Mozilla/5.0 (iPhone) AppleWebKit/602.4.6",
  "hash": "COMPUTED_HASH_VALUE_HERE"
}'
```

> **Note:** Replace `COMPUTED_HASH_VALUE_HERE` with the actual SHA-512 hash you computed in Step 2.2.

***

### Step 2.4: Handle Payment Response

The response structure varies based on the payment flow type.

**UPI Intent S2S Response (txn_s2s_flow=4):**

```json
{
  "metaData": {
    "message": null,
    "referenceId": "7a3060b7462bd2ce6d025c9997220e01",
    "statusCode": null,
    "txnId": "28471834809170981",
    "txnStatus": "pending",
    "unmappedStatus": "pending"
  },
  "result": {
    "paymentId": "30478359671",
    "merchantName": "HathwayCableAndDatacomLimited",
    "merchantVpa": "hathway.payu@indus",
    "amount": "518.02",
    "intentURIData": "pa=hathway.payu@indus&pn=HATHWAY...&tr=30478359671&tid=PPPL304...&am=518.02&cu=INR&tn=UPIIntent",
    "acsTemplate": "PGh0bWw+PGhlYWQ+...",
    "otpPostUrl": "https://secure.payu.in/ResponseHandler.php"
  }
}
```

**Key Fields:**

- `result.intentURIData` — UPI intent string to invoke customer's UPI app
- `result.acsTemplate` — Base64-encoded HTML template for rendering UPI intent link
- `result.paymentId` — PayU payment ID (same as `mihpayid` in webhooks)
- `metaData.txnStatus` — Initial transaction status (typically `"pending"`)

**Redirect Flow Response:**

```json
{
  "redirectUri": "https://secure.payu.in/_payment?mihpayid=403993715521855092&..."
}
```

**Key Fields:**

- `redirectUri` — URL to redirect customer for completing payment on PayU hosted page

<Note>
After initiating the payment, PayU will send a webhook to your configured partner webhook URL once the customer completes or cancels the payment. See Step 3 for webhook configuration and verification.
</Note>

***

## Step 3: Configure and Receive Webhooks

Webhooks enable real-time payment status updates from PayU to your partner backend. Configuration requires database entries.

### Step 3.1: Database Configuration (partner_webhook_urls)

Insert a row into the `partner_webhook_urls` table to configure where PayU should send payment webhooks.

**Required Table Schema:**

| Column                       | Type    | Description                                                     |
| ---------------------------- | ------- | --------------------------------------------------------------- |
| `partner_uuid`               | string  | Your partner/reseller UUID                                      |
| `merchant_id`                | integer | Specific merchant ID, or `NULL` for partner-level configuration |
| `partner_webhook_success`    | string  | URL to receive successful payment webhooks                      |
| `partner_webhook_failure`    | string  | URL to receive failed payment webhooks                          |
| `partner_webhook_cancelled`  | string  | URL to receive cancelled payment webhooks                       |
| `partner_webhook_default`    | string  | Default/fallback webhook URL                                    |
| `partner_name`               | string  | Partner display name                                            |
| `is_payment_webhook_enabled` | boolean | Must be `true` to enable webhooks                               |
| `is_json_payment_payload`    | boolean | `true` for JSON payload, `false` for form-encoded               |

**Example INSERT Statement:**

```sql
INSERT INTO partner_webhook_urls (
  partner_uuid,
  merchant_id,
  partner_webhook_success,
  partner_webhook_failure,
  partner_webhook_cancelled,
  partner_webhook_default,
  partner_name,
  is_payment_webhook_enabled,
  is_json_payment_payload
) VALUES (
  '11ee-0e7e-5403fde2-9523-0a696b110fde',
  NULL,
  'https://partner.example.com/webhook/payment/success',
  'https://partner.example.com/webhook/payment/failure',
  'https://partner.example.com/webhook/payment/cancelled',
  'https://partner.example.com/webhook/payment/default',
  'WhatsApp Partner',
  true,
  false
);
```

<Info>
**Partner-Level vs. Merchant-Level:**
- Set `merchant_id = NULL` for partner-level configuration (applies to all merchants under this partner)
- Set specific `merchant_id` value for merchant-specific webhook URLs
- PayU looks up merchant-level first, then falls back to partner-level
</Info>

***

### Step 3.2: Database Configuration (partner_merchant_params)

Optionally disable fallback to merchant core webhook URLs by inserting a configuration parameter.

**Example INSERT Statement:**

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
  'disable_core_payment_webhook_url',
  '1',
  true
);
```

<Info>
**Fallback Behavior:**
- Without this parameter: If no partner webhook URL is found, PayU falls back to merchant's core webhook URLs (`PAYMENT_SUCCESS_URL`, `PAYMENT_FAILURE_URL`)
- With `disable_core_payment_webhook_url = '1'`: PayU will **only** send to partner webhook URLs and will not fall back to merchant core URLs
</Info>

***

### Step 3.3: Receive Webhook Payload

After payment completion, PayU sends a `POST` request to your configured webhook URL with the following payload structure:

**Sample Webhook Payload:**

```json
{
  "key": "7o583a",
  "txnid": "28471834809170981",
  "mihpayid": "30478359671",
  "status": "success",
  "unmappedstatus": "captured",
  "mode": "UPI",
  "bankcode": "INTENT",
  "amount": "518.02",
  "productinfo": "28471834809170981",
  "firstname": "",
  "email": "",
  "phone": "919820988398",
  "udf1": "",
  "udf2": "1370625260",
  "udf3": "r-hway-LDnTRBuFK8STTTeTEc2SuD",
  "udf4": "",
  "udf5": "whatsapp",
  "merchant_id": "8739528",
  "error": "E000",
  "error_Message": "No Error",
  "hash": "WEBHOOK_HASH_VALUE"
}
```

**Key Fields:**

- `mihpayid` — PayU payment ID (matches `paymentId` from payment response)
- `status` — Payment status (`success`, `failure`, `pending`, `userCancelled`)
- `unmappedstatus` — Internal PayU status (`captured`, `failed`, `initiated`)
- `txnid` — Transaction ID (matches your original request)
- `hash` — SHA-512 hash for webhook verification (see Step 3.4)

***

### Step 3.4: Verify Webhook Hash (Reverse Hash)

**Always verify** the webhook hash to ensure authenticity. Use the **reverse hash formula**:

```
client_secret|status|||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|merchant_id
```

<Warning>
**Reverse Hash Notes:**
- There are **five consecutive pipe characters** (`|||||`) between `status` and `udf5`
- The field order is **reversed** compared to the payment request hash
- Use your OAuth `client_secret`, **not** the merchant salt
- **Do not** include a trailing pipe after `merchant_id`
- Compute SHA-512 and compare **case-insensitively** with the `hash` field in the webhook payload
</Warning>

**Webhook Verification Code (Java):**

```java
import java.security.MessageDigest;
import java.util.Map;

public class PartnerWebhookVerifier {
    public static boolean verifyWebhookHash(Map<String,String> payload, String clientSecret) 
        throws Exception {
        
        StringBuilder hashString = new StringBuilder();
        hashString.append(clientSecret).append("|");
        hashString.append(payload.get("status")).append("|||||");
        hashString.append(getOrEmpty(payload,"udf5")).append("|");
        hashString.append(getOrEmpty(payload,"udf4")).append("|");
        hashString.append(getOrEmpty(payload,"udf3")).append("|");
        hashString.append(getOrEmpty(payload,"udf2")).append("|");
        hashString.append(getOrEmpty(payload,"udf1")).append("|");
        hashString.append(getOrEmpty(payload,"email")).append("|");
        hashString.append(getOrEmpty(payload,"firstname")).append("|");
        hashString.append(getOrEmpty(payload,"productinfo")).append("|");
        hashString.append(getOrEmpty(payload,"amount")).append("|");
        hashString.append(getOrEmpty(payload,"txnid")).append("|");
        hashString.append(getOrEmpty(payload,"merchant_id"));
        
        String expectedHash = sha512Hex(hashString.toString());
        return expectedHash.equalsIgnoreCase(payload.get("hash"));
    }
    
    private static String getOrEmpty(Map<String,String> map, String key) {
        return map.getOrDefault(key,"");
    }
    
    private static String sha512Hex(String input) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] digest = md.digest(input.getBytes("UTF-8"));
        StringBuilder hex = new StringBuilder();
        for(byte b : digest) {
            String h = Integer.toHexString(0xFF & b);
            if(h.length() == 1) hex.append("0");
            hex.append(h);
        }
        return hex.toString();
    }
}
```

<Success>
**Best Practice:** Only trust webhook data **after** successful hash verification. If hash verification fails, log the event and discard the payload.
</Success>

***

## Step 4: Verify the Payment

After receiving the webhook, call the Verify Payment API to confirm the final transaction status.

### Step 4.1: Generate Verify Payment Hash

Compute the SHA-512 hash using this formula:

```
merchant_id|verify_payment|txnid|client_secret
```

**Example:**

```
8739528|verify_payment|28471834809170981|YOUR_CLIENT_SECRET
```

Compute SHA-512 hex digest of the above string.

***

### Step 4.2: Call Verify Payment API

**Endpoint:** `POST /partner/verifyPayment`

**Environment URLs:**

| Environment | URL                                                                   |
| ----------- | --------------------------------------------------------------------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment` |
| Production  | `https://api.payu.in/partner/verifyPayment`                           |

**Request Headers:**

```
Authorization: Bearer <FINAL_ACCESS_TOKEN>
Content-Type: application/json
```

**Request Parameters:**

| Parameter     | Type & Description                                          | Example                              |
| ------------- | ----------------------------------------------------------- | ------------------------------------ |
| `txnid`       | string — Transaction ID to verify                           | 28471834809170981                    |
| `merchant_id` | integer — PayU merchant ID                                  | 8739528                              |
| `reseller_id` | string — Partner/reseller UUID                              | 11ee-0e7e-5403fde2-9523-0a696b110fde |
| `hash`        | string — SHA-512 hash computed using verify payment formula | (computed hash)                      |

**Sample Request:**

```bash
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment' \
--header 'Authorization: Bearer 039e0d1d70f467f946e2d73bd43868df856cfaa352ea54591a76bfc4a08d3487' \
--header 'Content-Type: application/json' \
--data '{
  "txnid": "28471834809170981",
  "merchant_id": 8739528,
  "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
  "hash": "COMPUTED_VERIFY_HASH_HERE"
}'
```

***

### Step 4.3: Process Verification Response

**Sample Response:**

```json
{
  "status": "success",
  "unmappedstatus": "captured",
  "mihpayid": "30478359671",
  "txnid": "28471834809170981",
  "amount": "518.02",
  "mode": "UPI",
  "bankcode": "INTENT",
  "productinfo": "28471834809170981",
  "firstname": "",
  "email": "",
  "phone": "919820988398"
}
```

**Reconciliation Steps:**

1. Compare `mihpayid` from verify response with webhook payload
2. Compare `status` and `unmappedstatus` values
3. Verify `txnid` matches your original transaction ID
4. Check `amount` matches the payment amount
5. If all match, mark the payment as verified in your system

<Success>
**Integration Complete!** You've successfully:
- ✅ Generated OAuth access token
- ✅ Initiated a partner payment
- ✅ Configured and received webhooks
- ✅ Verified the payment status

For UPI TPV integration, see [UPI TPV Integration Guide](doc:upi-tpv-integration).
</Success>

***

## Next Steps

- [UPI TPV Integration](doc:upi-tpv-integration) — Add third-party validation for compliance
- [Testing and Troubleshooting](doc:testing-and-troubleshooting-partner-payments) — Error resolution and test data
- [API Reference: POST /partner/payments](ref:partner-payments-api) — Complete API specification
- [API Reference: POST /partner/verifyPayment](ref:verify-payment-partner-api) — Verification API details
