---
title: Classic S2S 3DS2 Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
Integrate card payments using PayU's Classic Server-to-Server (S2S) flow with full 3D Secure 2.0 support. This integration handles all authentication redirects internally while your server maintains control over the payment flow.

<Callout icon="📘" theme="info">
  **Prerequisites:**

  - Merchant account enabled for S2S flow (`txn_s2s_flow = 1`)
  - Valid PayU merchant key and salt
  - Payment gateway (PG) enabled for card payments on your account
  - PCI DSS compliance or tokenization setup
</Callout>

## Step 1: Start Integration

### Step 1.1: Prepare the Request Parameters

<Accordion title="Step 1.1: Prepare the Request Parameters" icon="fa-table">
  Before making the payment request, prepare all required parameters:

#### Mandatory Parameters

support. This integration handles all authentication redirects internally while your server maintains control over the payment flow.

<Callout icon="📘" theme="info">
  **Prerequisites:**

  - Merchant account enabled for S2S flow (`txn_s2s_flow = 1`)
  - Valid PayU merchant key and salt
  - Payment gateway (PG) enabled for card payments on your account
  - PCI DSS compliance or tokenization setup


</Callout>


  This integration handles all authentication redirects internally while your server maintains control over the payment flow.

  <Callout icon="📘" theme="info">
    **Prerequisites:**

    - Merchant account enabled for S2S flow (`txn_s2s_flow = 1`)
    - Valid PayU merchant key and salt
    - Payment gateway (PG) enabled for card payments on your account
    - PCI DSS compliance or tokenization setup
  </Callout>

  ## Step 1: Start Integration

    ### Step 1.1: Prepare the Request Parameters and Post Request

<Tabs>
<Tab title="Request Parameters">
    Before making the payment request, prepare all required parameters:

    #### Mandatory Parameters

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
      <td>key</td>
      <td>String. Merchant key (posted).</td>
      <td>OgAFEC</td>
    </tr>
    <tr>
      <td>txnid</td>
      <td>String. Unique merchant transaction ID.</td>
      <td>xriK2cGsCl</td>
    </tr>
    <tr>
      <td>amount</td>
      <td>Decimal/String. Transaction amount.</td>
      <td>1 or 1.00</td>
    </tr>
    <tr>
      <td>productinfo</td>
      <td>String. Product description.</td>
      <td>Product_info</td>
    </tr>
    <tr>
      <td>firstname</td>
      <td>String. Customer first name.</td>
      <td>PayU</td>
    </tr>
    <tr>
      <td>email</td>
      <td>String. Customer email address.</td>
      <td>test@example.com</td>
    </tr>
    <tr>
      <td>phone</td>
      <td>String. Customer phone number.</td>
      <td>1234567890</td>
    </tr>
    <tr>
      <td>surl</td>
      <td>String. Merchant success redirect URL (postback).</td>
      <td>https://admin.payu.in/test_response</td>
    </tr>
    <tr>
      <td>furl</td>
      <td>String. Merchant failure redirect URL (postback).</td>
      <td>https://admin.payu.in/test_response</td>
    </tr>
    <tr>
      <td>hash</td>
      <td>String. SHA512 hash for request validation. Computed as: SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||Salt)</td>
      <td>f6e733f1e8e95e2b...</td>
    </tr>
    <tr>
      <td>pg</td>
      <td>String. Payment gateway code (PG type).</td>
      <td>CC</td>
    </tr>
    <tr>
      <td>bankcode</td>
      <td>String. Bank/payment method code.</td>
      <td>CC</td>
    </tr>
    <tr>
      <td>ccnum</td>
      <td>String. Card number.</td>
      <td>XXXXXXXXXXXX1036</td>
    </tr>
    <tr>
      <td>ccname</td>
      <td>String. Cardholder name.</td>
      <td>Test User</td>
    </tr>
    <tr>
      <td>ccvv</td>
      <td>String. Card CVV.</td>
      <td>XXX</td>
    </tr>
    <tr>
      <td>ccexpmon</td>
      <td>String. Card expiry month (MM).</td>
      <td>05</td>
    </tr>
    <tr>
      <td>ccexpyr</td>
      <td>String. Card expiry year (YYYY).</td>
      <td>2026</td>
    </tr>
    <tr>
      <td>txn_s2s_flow</td>
      <td>Integer. Flag to enable S2S flow.</td>
      <td>1</td>
    </tr>
  </tbody>
</table>


### Generate Hash

<Accordion title="Generate Hash" icon="fa-info-circle">
  Generate a SHA512 hash to secure your payment request:

  **Hash Formula:**

  ```
  hash = SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
  ```

  **Rules:**

  - Use empty strings for UDF fields if not used (shown as `||||||` above)
  - Compute hash server-side only (never expose salt to frontend)
  - Output must be lowercase hexadecimal

  <HashingSample />
</Accordion>
</Tab>
<Tab title="Sample Request">
  ```bash
  curl --location 'https://test.payu.in/_payment' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=OgAFEC' \
  --data-urlencode 'firstname=PayU' \
  --data-urlencode 'email=test@example.com' \
  --data-urlencode 'amount=1' \
  --data-urlencode 'phone=1234567890' \
  --data-urlencode 'productinfo=Product_info' \
  --data-urlencode 'surl=https://yourdomain.com/success' \
  --data-urlencode 'furl=https://yourdomain.com/failure' \
  --data-urlencode 'pg=CC' \
  --data-urlencode 'bankcode=CC' \
  --data-urlencode 'ccnum=XXXXXXXXXXXX1036' \
  --data-urlencode 'ccname=Test User' \
  --data-urlencode 'ccvv=XXX' \
  --data-urlencode 'ccexpmon=05' \
  --data-urlencode 'ccexpyr=2026' \
  --data-urlencode 'txnid=xriK2cGsCl' \
  --data-urlencode 'hash=f6e733f1e8e95e2bff40953c00a5beaa4f2755ddcbb995c532f82720fcd6658c01b521e58ec3e2308589731b22ad71dc778f7ab381a0a57819556abb1220d484' \
  --data-urlencode 'txn_s2s_flow=1'
  ```
  ```python
  import requests

  url = "https://test.payu.in/_payment"

  headers = {
      "Content-Type": "application/x-www-form-urlencoded"
  }

  payload = {
      "key": "OgAFEC",
      "firstname": "PayU",
      "email": "test@example.com",
      "amount": "1",
      "phone": "1234567890",
      "productinfo": "Product_info",
      "surl": "https://yourdomain.com/success",
      "furl": "https://yourdomain.com/failure",
      "pg": "CC",
      "bankcode": "CC",
      "ccnum": "XXXXXXXXXXXX1036",
      "ccname": "Test User",
      "ccvv": "XXX",
      "ccexpmon": "05",
      "ccexpyr": "2026",
      "txnid": "xriK2cGsCl",
      "hash": "f6e733f1e8e95e2bff40953c00a5beaa4f2755ddcbb995c532f82720fcd6658c01b521e58ec3e2308589731b22ad71dc778f7ab381a0a57819556abb1220d484",
      "txn_s2s_flow": "1"
  }

  response = requests.post(url, headers=headers, data=payload)

  print(f"Status Code: {response.status_code}")
  print(f"Response Body:\n{response.text}")
  ```
  ```php
  <?php

  $url = "https://test.payu.in/_payment";

  $payload = [
      "key" => "OgAFEC",
      "firstname" => "PayU",
      "email" => "test@example.com",
      "amount" => "1",
      "phone" => "1234567890",
      "productinfo" => "Product_info",
      "surl" => "https://yourdomain.com/success",
      "furl" => "https://yourdomain.com/failure",
      "pg" => "CC",
      "bankcode" => "CC",
      "ccnum" => "XXXXXXXXXXXX1036",
      "ccname" => "Test User",
      "ccvv" => "XXX",
      "ccexpmon" => "05",
      "ccexpyr" => "2026",
      "txnid" => "xriK2cGsCl",
      "hash" => "f6e733f1e8e95e2bff40953c00a5beaa4f2755ddcbb995c532f82720fcd6658c01b521e58ec3e2308589731b22ad71dc778f7ab381a0a57819556abb1220d484",
      "txn_s2s_flow" => "1"
  ];

  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
  curl_setopt($ch, CURLOPT_HTTPHEADER, ["Content-Type: application/x-www-form-urlencoded"]);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

  $response = curl_exec($ch);
  $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);

  curl_close($ch);

  echo "HTTP Status: $http_code\n";
  echo "Response:\n$response\n";

  ?>
  ```
  ```java
  import java.io.IOException;
  import java.net.URI;
  import java.net.URLEncoder;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;
  import java.nio.charset.StandardCharsets;
  import java.util.LinkedHashMap;
  import java.util.Map;
  import java.util.StringJoiner;

  public class PayUClassicS2S {
      public static void main(String[] args) throws IOException, InterruptedException {
          String url = "https://test.payu.in/_payment";

          Map<String, String> payload = new LinkedHashMap<>();
          payload.put("key", "OgAFEC");
          payload.put("firstname", "PayU");
          payload.put("email", "test@example.com");
          payload.put("amount", "1");
          payload.put("phone", "1234567890");
          payload.put("productinfo", "Product_info");
          payload.put("surl", "https://yourdomain.com/success");
          payload.put("furl", "https://yourdomain.com/failure");
          payload.put("pg", "CC");
          payload.put("bankcode", "CC");
          payload.put("ccnum", "XXXXXXXXXXXX1036");
          payload.put("ccname", "Test User");
          payload.put("ccvv", "XXX");
          payload.put("ccexpmon", "05");
          payload.put("ccexpyr", "2026");
          payload.put("txnid", "xriK2cGsCl");
          payload.put("hash", "f6e733f1e8e95e2bff40953c00a5beaa4f2755ddcbb995c532f82720fcd6658c01b521e58ec3e2308589731b22ad71dc778f7ab381a0a57819556abb1220d484");
          payload.put("txn_s2s_flow", "1");

          StringJoiner body = new StringJoiner("&");
          for (Map.Entry<String, String> entry : payload.entrySet()) {
              body.add(URLEncoder.encode(entry.getKey(), StandardCharsets.UTF_8) + "=" + 
                       URLEncoder.encode(entry.getValue(), StandardCharsets.UTF_8));
          }

          HttpClient client = HttpClient.newHttpClient();
          HttpRequest request = HttpRequest.newBuilder()
                  .uri(URI.create(url))
                  .header("Content-Type", "application/x-www-form-urlencoded")
                  .POST(HttpRequest.BodyPublishers.ofString(body.toString()))
                  .build();

          HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

          System.out.println("Status Code: " + response.statusCode());
          System.out.println("Response Body:\n" + response.body());
      }
  }
  ```
</Tab>
</Tabs>

### Step 1.2: Response Handling & Hash Verification

<Accordion title="Success Response Example" icon="fa-code">
  **Success Scenario**

  ```json
  {
    "result": {
      "post_uri": "https://test.payu.in/874eba1f31115d4204be9a414909ad71f0131fad60129801badf5c659cb6c47f/threeDSecure/method",
      "post_data": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0Ij4uLi48L2Zvcm0+PC9ib2R5PjwvaHRtbD4="
    },
    "status": "success",
    "error": null,
    "message": null
  }
  ```

  **Failure Scenario:**

  ```json
  {
    "status": "failure",
    "error": "E214",
    "message": "The Bank servers are unreachable over the network"
  }
  ```
</Accordion>

<Accordion title="Response Verification Using Reverse Hashing" icon="fa-code">
  When you receive the final transaction response at your `surl` or `furl`, verify the response hash:

  **Reverse Hash Formula:**

  ```
  reverse_hash = SHA512(salt|status|||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  **Verification Steps:**

  1. Extract all response parameters
  2. Compute reverse hash using the formula above
  3. Compare computed hash with the `hash` field in the response
  4. **Match required:** Only trust the response if hashes match (case-sensitive comparison)

  > **Security Note:** Always perform hash verification server-side. Never trust transaction status without validating the hash.
</Accordion>

### Step 1.5: Verify the Payment

<Verify_Payment_Tabs />

***

## Step 2: Test Integration

### Step 2.1: Pre-Payment Validation

<Accordion title="Pre-Payment Validation" icon="fa-info-circle">
  **Verify Merchant Credentials:**

  - Confirm your `key` and `salt` are correct
  - Check that `txn_s2s_flow` flag is enabled on your account

  2. **Validate Hash Generation:**
     - Test hash generation with known values
     - Compare with expected output
     - Ensure lowercase hexadecimal output

  3. **Check Endpoint Accessibility:**
     - Verify your server can reach `https://test.payu.in/_payment`
     - Confirm TLS/SSL compatibility

  4. **Test surl/furl URLs:**
     - Ensure your success and failure URLs are publicly accessible
     - Test POST data reception at these endpoints
</Accordion>

### Step 2.2: Simulate a Successful Transaction

<Accordion title="Simulate a Successful Transaction" icon="fa-info-circle">
  **General Test Steps:**

  1. Use test merchant credentials (test `key` and `salt`)
  2. Use test card details provided by PayU
  3. Set `amount` to a test value (e.g., 1.00)
  4. Submit payment request to test environment
  5. Complete 3DS authentication using test OTP
  6. Verify successful response at your `surl`
  7. Validate response hash
  8. Check transaction in PayU dashboard
</Accordion>

### Step 2.3: Simulate a Failed Transaction

<Accordion title="Simulate a Failed Transaction" icon="fa-info-circle">
  \> **⚠️ Info Gap:** Test scenarios for failed transactions (insufficient funds, invalid card, declined by issuer) needed. Request test cases from PayU.

  **Test Error Handling:**

  1. Invalid hash — modify hash before sending request
  2. Missing mandatory parameters — omit required fields
  3. Invalid card details — use non-existent card numbers
  4. Network timeout — simulate timeout scenarios
</Accordion>

### Step 2.4: Post-Transaction Verification

<Accordion title=" Post-Transaction Verification" icon="fa-info-circle">
  **1. Check Return URL (surl/furl)**

  - Verify transaction data received at your endpoint
  - Validate all expected fields are present
  - Log complete response for debugging

  **2. Verify S2S Webhook**

  - Confirm webhook delivery (if configured)
  - Validate webhook signature/hash
  - Handle duplicate/retry notifications

  **3. Cross-Verify in Dashboard**

  - Log into PayU Merchant Dashboard
  - Locate transaction by `txnid` or `mihpayid`
  - Confirm status matches your received response
  - Check settlement status
</Accordion>

***

## Step 3: Going Live — Your Final Checklist

### Step 3.1: Update to Production Credentials

<Accordion title="Step 3.1: Update to Production Credentials" icon="fa-info-circle">
  #### Generate Live Keys

  1. Log into PayU Merchant Dashboard
  2. Navigate to **Settings** → **API Keys**
  3. Generate production `key` and `salt`
  4. Securely store credentials (use environment variables or secrets manager)

  #### Update Your Code

  Replace all test credentials with production values:

  ```python
  # Development
  PAYU_KEY = "test_key"
  PAYU_SALT = "test_salt"
  PAYU_URL = "https://test.payu.in/_payment"

  # Production
  PAYU_KEY = "live_key"  # From dashboard
  PAYU_SALT = "live_salt"  # From dashboard
  PAYU_URL = "https://secure.payu.in/_payment"
  ```

  #### Update the Endpoint URLs

  | Environment    | URL                                                                 |
  | -------------- | ------------------------------------------------------------------- |
  | **Test**       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |
  | **Production** | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |
</Accordion>

### Step 3.2: Final Integration Verification

<Accordion title="Step 3.2: Final Integration Verification" icon="fa-info-circle">
  **✅ Conduct a Live Transaction**

  - Process a small-value real transaction (e.g., ₹1)
  - Use a real card (your own test card)
  - Complete full 3DS authentication flow
  - Verify funds are actually debited and credited

  **✅ Verify the S2S Webhook**

  - Confirm production webhook endpoint is configured
  - Test webhook delivery with live transaction
  - Validate webhook hash/signature verification logic

  **✅ Validate the Response Hash**

  - Confirm reverse hash verification is working
  - Test with actual live transaction response
  - Ensure hash mismatch is properly rejected

  **✅ Check surl / furl**

  - Verify production URLs are correct
  - Test both success and failure scenarios
  - Confirm proper customer redirect flow

  **✅ Implement a Reconciliation Plan**

  - Schedule daily reconciliation reports
  - Cross-verify PayU dashboard vs your database
  - Set up alerts for discrepancies
  - Document dispute resolution process
</Accordion>