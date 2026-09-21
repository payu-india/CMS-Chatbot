---
title: Hosted Checkout Integration - Partner Payments
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
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

***

## How It Works

The Partner Payments Hosted Checkout flow follows these steps:

1. **Get the Access token&#x20;**&#x20;— Obtain an access token with scopes: `hub_session`

2. **Initiate Payment** — POST a payment request to the Partner Payments API with transaction details, callback URLs (`surl`, `furl`, `curl`), and a computed hash

3. **Receive Redirect URL** — PayU returns a `redirectUri` pointing to the hosted checkout page

4. **Redirect Customer** — Immediately redirect the customer to the `redirectUri` in their browser

5. **Customer Completes Payment** — Customer selects a payment method on PayU's hosted page, authenticates, and completes the transaction

6. **Customer Redirected Back** — PayU redirects the customer to your success/failure/cancel URL based on payment outcome

7. **Receive Webhook** — PayU sends payment status notification to your configured partner webhook URL

8. **Verify Payment** — Call the Verify Payment API to confirm final transaction status

***

## Prerequisites

Before you begin, ensure you have:

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

<Partner_Payment_Auth />

<br />

## Step 2: Initiate Hosted Checkout Payment

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

For getting access token, refer to [Prequisites](#prequisites).

<Accordion title="Request Body Parameters" icon="fa-table">
  **Mandatory Parameters**

  eckout enables partners to redirect customers to PayU's secure, PCI-compliant payment gateway where they can complete payments using multiple payment methods—all without handling sensitive card data or building custom payment forms.

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

  ***

  ## How It Works

  The Partner Payments Hosted Checkout flow follows these steps:

  1. **Get the Access token&#x20;**&#x20;— Obtain an access token with scopes: `hub_session`

  2. **Initiate Payment** — POST a payment request to the Partner Payments API with transaction details, callback URLs (`surl`, `furl`, `curl`), and a computed hash

  3. **Receive Redirect URL** — PayU returns a `redirectUri` pointing to the hosted checkout page

  4. **Redirect Customer** — Immediately redirect the customer to the `redirectUri` in their browser

  5. **Customer Completes Payment** — Customer selects a payment method on PayU's hosted page, authenticates, and completes the transaction

  6. **Customer Redirected Back** — PayU redirects t

  **Optional Parameters**

  /failure/cancel URL based on payment outcome

  7. **Receive Webhook** — PayU sends payment status notification to your configured partner webhook URL

  8. **Verify Payment** — Call the Verify Payment API to confirm final transaction status

  ***

  ## Prerequisites

  Before you begin, ensure you have:

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

  <Partner_Payment_Auth />

  <br />

  ## Step 2: Initiate Hosted Checkout Payment

  ### Step 2.1: Prepare Request Parameters

  **Endpoint URLs:**

  | Environment | URL                                                              |
  | ----------- | ----------------------------
</Accordion>

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

<Generate_Hash_Partner_Payment />

### Step 2.3: POST the Payment Request

Use the hash created in Step 2.2 here in this step:

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

</Accordion>

### Step 2.4: Handle Payment Response & Redirect Customer

**Success Response:**

```json
{
  "redirectUri": "https://secure.payu.in/_payment?mihpayid=403993715521899234&amount=1500.00&txnid=PPHOST20240315001&key=JPM7Fg&productinfo=Premium+Subscription+-+Monthly&phone=919876543210&firstname=Priya&email=priya.sharma%40example.com&surl=https%3A%2F%2Fyourplatform.com%2Fpayment%2Fsuccess&furl=https%3A%2F%2Fyourplatform.com%2Fpayment%2Ffailure&curl=https%3A%2F%2Fyourplatform.com%2Fpayment%2Fcancel&hash=..."
}
```

<Accordion title="Response Parameters Implementation" icon="fa-info-reply">
  **Key Response Field:**

  \- **redirectUri** — The PayU hosted checkout URL. **Immediately redirect the customer to this URL.**

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
</Accordion>

<Accordion title="Customer Experience on Hosted Checkout" icon="fa-info-circle">
  **:**

  Once redirected to `redirectUri`, the customer will:

  1\. **See PayU's hosted checkout page** with:
  \- Your merchant branding (logo, colors)
  \- Transaction summary (amount, product description)
  \- Available payment methods

  2\. **Select a payment method:**
  \- **Credit/Debit Cards** (Visa, Mastercard, Amex, Rupay)
  \- **UPI** (Intent or Collect flow)
  \- **Net Banking** (50+ banks)
  \- **Wallets** (PayU Money, PhonePe, Paytm, etc.)

  3\. **Complete authentication:**
  \- Card: CVV + OTP (3D Secure)
  \- UPI: PIN authentication
  \- Net Banking: Bank credentials
  \- Wallet: Wallet PIN/OTP

  4\. **Receive outcome:**
  \- **Success** → Redirected to `surl`
  \- **Failure** → Redirected to `furl`
  \- **Cancel** → Redirected to `curl`

    <Info>
    **Callback URL Best Practices:**
    - Always use HTTPS for surl/furl/curl endpoints
    - Display clear success/failure messages on callback pages
    - Extract transaction details from callback parameters (PayU POSTs data to these URLs)
    - Do NOT rely solely on callback parameters — always verify using webhooks and Verify Payment API
    </Info>
</Accordion>

***

## Step 3: Receive Payment Notification

### Step 3.1: Partner Webhook

After the customer completes payment, PayU sends a webhook notification to your configured partner webhook URL.

**Webhook Configuration:**

Ensure these URLs are configured:

\- `partner_webhook_success` — Called on successful payment
\- `partner_webhook_failure` — Called on failed payment
\- `partner_webhook_cancelled` — Called when payment is cancelled

<Callout icon="⚠️" theme="info">
  ### Contact your Account Manager to register for the Webhooks.
</Callout>

<Accordion title="Sample Payload" icon="fa-code">
  **Sample Success Webhook Payload**

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
</Accordion>

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

<Accordion title="Sample Verification Payload" icon="fa-code">
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
</Accordion>

### Step 3.3: Process Webhook

Implement using the following sample python code to handle the webhook:

<Accordion title="Sample Python Flask Webhook Handler" icon="fa-code">
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
</Accordion>

***

## Step 4: Verify Payment

<Verify_Payment_Partner />

### Process Verification Response

**Reconciliation Checklist:**

✅ `mihpayid` matches<br />✅ `txnid` matches<br />✅ `amount` matches<br />✅ `status` is `"success"`<br />✅ `unmappedstatus` is `"captured"`

If all match, mark transaction as verified. </Accordion>

***

## Use Cases

Partner Payments Hosted Checkout is ideal for:

*  **E-commerce Platforms** : Multi-merchant marketplaces where sellers need to accept payments. Partner handles checkout integration; merchants just onboard.

*  **Subscription Services** : Recurring billing for SaaS, memberships, content subscriptions. Hosted checkout supports saved cards and automated retries.

*. **B2B Platforms** : Business-to-business transactions requiring invoice payments, procurement orders, vendor settlements.

* **Event Ticketing** : Concert, sports, conference ticket sales with multiple payment methods and high transaction volumes.

***

## Error Handling

| Error                                | Cause                                | Resolution                                                                                                       |
| ------------------------------------ | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| <code>Invalid hash</code>            | Hash computation mismatch            | Verify using <code>client_secret</code> (not merchant salt), check 6-pipe sequence, ensure SHA-512 lowercase hex |
| <code>Invalid access token</code>    | OAuth token expired or invalid       | Refresh OAuth token. Implement auto-refresh logic                                                                |
| <code>Transaction not found</code>   | txnid doesn't exist in PayU          | Verify txnid matches exactly. Check for typos                                                                    |
| <code>Missing webhook URL</code>     | Partner webhook URLs not configured  | Contact PayU to configure partner_webhook_success, partner_webhook_failure, partner_webhook_cancelled            |
| <code>HMAC validation failure</code> | Webhook hash verification failed     | Check reverse hash formula (5 pipes after status, no trailing pipe). Use case-insensitive comparison             |
| <code>Unauthorized - 401</code>      | Missing/invalid Authorization header | Ensure <code>Authorization: Bearer \<token></code> in all requests                                               |

***

## Testing

### Test Environment

**Base URL:** `https://test-partnerapilayer.payu.in/apilayer/partner`

**OAuth URLs:**

\- Auth Code: `https://uat-partner.payu.in/api/v1/merchants/auth_code`
\- Access Token: `https://uat-accounts.payu.in/oauth/token`

<Accordion title="Test Workflow and Validation Checklist" icon="fa-info-circle">
**Test Workflow**

1\. Generate OAuth access token
2\. Create payment request
3\. Redirect to hosted checkout (test environment)
4\. Complete payment using test card/UPI
5\. Verify redirect to surl/furl
6\. Confirm webhook received
7\. Call Verify Payment API
8\. Reconcile all data points

**Validation Checklist**

✅ OAuth token generation succeeds<br />✅ Payment API returns redirectUri<br />✅ Hosted checkout page loads<br />✅ Test payment succeeds<br />✅ Customer redirected to surl<br />✅ Webhook received within 5 seconds<br />✅ Webhook hash verified<br />✅ Verify Payment API confirms status<br />✅ Reconciliation successful
</Accordion>
***

## Best Practices

### Security

\- ✅ Store `client_secret` securely — Never expose in client-side code
\- ✅ Always verify webhook hash before processing
\- ✅ Use HTTPS for all callback URLs (surl/furl/curl)
\- ✅ Implement rate limiting on webhook endpoints

### Reliability

\- ✅ Implement idempotency using `txnid`
\- ✅ Use unique `txnid` per transaction — Never reuse
\- ✅ Implement retry logic for Verify Payment API
\- ✅ Log all API requests/responses for debugging

### Integration

\- ✅ Implement OAuth token refresh (tokens expire \~1 hour)
\- ✅ Monitor webhook delivery latency
\- ✅ Test both success and failure scenarios
\- ✅ Handle network timeouts gracefully

### Customer Experience

\- ✅ Use descriptive `productinfo` so customers recognize the charge
\- ✅ Include customer name and email (improves checkout experience)
\- ✅ Provide clear success/failure pages on surl/furl
\- ✅ Show payment status in real-time after redirect

***

## Next Steps

\- [Partner Payment UPI Intent Integration](#) — Direct UPI app invocation
\- [Payment Links for Partners Overview](#) — Shareable payment links
\- [Verify Payment API Reference](#) — Complete verification documentation
\- [Partner Webhook Guide](#) — Advanced webhook patterns

<Success>
**Integration Complete!** You can now accept payments through PayU's hosted checkout using the Partner Payments API.
</Success>
