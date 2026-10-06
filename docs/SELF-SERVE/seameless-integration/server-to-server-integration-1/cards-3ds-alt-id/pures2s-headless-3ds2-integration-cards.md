---
title: PureS2S Headless 3DS2 Integration - Cards
deprecated: false
hidden: true
metadata:
  robots: index
---
Integrate card payments with full control over the OTP user interface using PayU's PureS2S Headless flow. This integration uses a headless browser to handle ACS (Access Control Server) interactions while you collect and submit OTP directly on your own UI.

> **Prerequisites:**
>
> - Merchant account enabled for PureS2S headless flow (`txn_s2s_flow = 2` and `nativeOtpSupportO` flag)
> - Valid PayU merchant key and salt
> - Payment gateway (PG) enabled for card payments
> - PCI DSS compliance for handling card data
> - **Security sign-off required** — PureS2S Headless involves advanced security considerations; confirm with PayU before going live

## Step 1: Start Integration

### Step 1.1: Prepare the Request Parameters

<Accordion title="Step 1.1: Prepare the Request Parameters" icon="fa-list-check">
  PureS2S Headless uses the same core parameters as Classic S2S, with the `txn_s2s_flow` flag set to `2`:

  #### Mandatory Parameters

  | Parameter        | Type & Description                               | Example                                                          |
  | ---------------- | ------------------------------------------------ | ---------------------------------------------------------------- |
  | key              | String. Merchant key.                            | OgAFEC                                                           |
  | txnid            | String. Unique transaction ID.                   | xriK2cGsCl                                                       |
  | amount           | Decimal/String. Transaction amount.              | 1.00                                                             |
  | productinfo      | String. Product description.                     | Product_info                                                     |
  | firstname        | String. Customer first name.                     | PayU                                                             |
  | email            | String. Customer email.                          | [test@example.com](mailto:test@example.com)                      |
  | phone            | String. Customer phone.                          | 1234567890                                                       |
  | surl             | String. Success URL.                             | [https://yourdomain.com/success](https://yourdomain.com/success) |
  | furl             | String. Failure URL.                             | [https://yourdomain.com/failure](https://yourdomain.com/failure) |
  | hash             | String. SHA512 hash.                             | \[computed hash]                                                 |
  | pg               | String. Payment gateway code.                    | CC                                                               |
  | bankcode         | String. Bank code.                               | CC                                                               |
  | ccnum            | String. Card number.                             | XXXXXXXXXXXX1036                                                 |
  | ccname           | String. Cardholder name.                         | Test User                                                        |
  | ccvv             | String. CVV.                                     | XXX                                                              |
  | ccexpmon         | String. Expiry month (MM).                       | 05                                                               |
  | ccexpyr          | String. Expiry year (YYYY).                      | 2026                                                             |
  | **txn_s2s_flow** | **Integer. Enable PureS2S Headless (set to 2).** | **2**                                                            |
</Accordion>

### Step 1.2: Generate Hash

<Accordion title="Step 1.2: Generate Hash" icon="fa-key">
  Hash generation is identical to Classic S2S:

  ```
  hash = SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
  ```

  Refer to the [Classic S2S Integration Guide](page2-classic-s2s-3ds2-integration.md#step-12-generate-hash) for complete hash generation code.
</Accordion>

### Step 1.3: POST the Request to `/_payment`

<Accordion title="Step 1.3: POST the Request" icon="fa-code">
  **Request (cURL):**

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
  --data-urlencode 'hash=[COMPUTED_HASH]' \
  --data-urlencode 'txn_s2s_flow=2'
  ```

  **Python:**

  ```python
  import requests

  url = "https://test.payu.in/_payment"

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
      "hash": "[COMPUTED_HASH]",
      "txn_s2s_flow": "2"
  }

  response = requests.post(url, data=payload)
  print(response.json())
  ```
</Accordion>

### Step 1.4: Handle Headless ACS Response

<Accordion title="Step 1.4: Handle Headless ACS Response" icon="fa-shield-check">
  After posting to `/_payment`, PayU returns a response containing headless-specific fields:

  **Sample Response:**

  ```json
  {
    "result": {
      "post_uri": "https://test.payu.in/ResponseHandler.php",
      "post_data": "cHVyZVMyUw==",
      "referenceId": "96a399f0f585ca5a11de6448cbbdab54",
      "pureS2S": "1",
      "acsTemplate": "PGh0bWw+PGJvZHk+Li4uPC9ib2R5PjwvaHRtbD4="
    },
    "status": "success",
    "error": null,
    "message": null
  }
  ```

  **Key Fields:**

  - `referenceId` — **Save this value**. You'll need it to submit OTP.
  - `post_uri` — The ResponseHandler endpoint where you'll POST the OTP.
  - `pureS2S` — Flag confirming this is a PureS2S flow.
  - `acsTemplate` — Base64-encoded ACS HTML (handled by headless browser internally).

  **Next Step:**<br />PayU's headless browser will internally load the ACS page. The customer will receive an OTP on their registered mobile number. **You must now display an OTP input field on your own UI.**
</Accordion>

### Step 1.5: Submit OTP via ResponseHandler

<Accordion title="Step 1.5: Submit OTP via ResponseHandler" icon="fa-shield-check">
  Once the customer enters the OTP on your UI, submit it to PayU's ResponseHandler:

  **OTP Submission Request:**

  ```bash
  curl --location 'https://test.payu.in/ResponseHandler.php' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'referenceId=96a399f0f585ca5a11de6448cbbdab54' \
  --data-urlencode 'otp=725356'
  ```

  **Python:**

  ```python
  import requests

  otp_url = "https://test.payu.in/ResponseHandler.php"

  otp_payload = {
      "referenceId": "96a399f0f585ca5a11de6448cbbdab54",  # From step 1.4
      "otp": "725356"  # OTP entered by customer
  }

  otp_response = requests.post(otp_url, data=otp_payload)
  print(otp_response.text)
  ```

  **What Happens Internally:**

  1. PayU receives your OTP submission
  2. PayU's headless browser enters the OTP into the ACS page
  3. ACS validates the OTP and returns authentication result (Cres)
  4. PayU processes authentication and calls authorization
  5. Final response is returned to you
</Accordion>

### Step 1.6: Response Handling & Hash Verification

<Accordion title="Step 1.6: Response Handling & Hash Verification" icon="fa-key">
  The ResponseHandler returns a **base64-encoded JSON payload**. Decode it to get transaction details:

  **Sample Encoded Response:**

  ```
  eyJzdGF0dXMiOiJzdWNjZXNzIiwicmVzdWx0Ijp7Im1paHBheWlkIjoiOTk5MDAwMDAwMDAwNDk1IiwidHhuaWQiOiJ4cmlLMmNHc0NsIiwiYW1vdW50IjoiMS4wMCIsImhhc2giOiIuLi4ifX0=
  ```

  **Decoded Response:**

  ```json
  {
    "status": "success",
    "result": {
      "mihpayid": "999000000000495",
      "mode": "CC",
      "status": "success",
      "key": "OgAFEC",
      "txnid": "xriK2cGsCl",
      "amount": "1.00",
      "productinfo": "Product_info",
      "firstname": "PayU",
      "email": "test@example.com",
      "phone": "1234567890",
      "card_no": "XXXXXXXXXXXX1036",
      "bank_ref_no": "251691821342610080",
      "bankcode": "CC",
      "hash": "[response_hash]",
      "net_amount_debit": "1.00",
      "unmappedstatus": "captured",
      "error": "E000",
      "error_Message": "No Error"
    }
  }
  ```

  **Verify Hash:**<br />Use reverse hash verification (same as Classic S2S) to ensure response integrity.
</Accordion>

### Step 1.7: Verify the Payment

<Verify_Payment_Tabs />

***

## Step 2: Test Integration

### Step 2.1: Pre-Payment Validation

<Accordion title="Step 2.1: Pre-Payment Validation" icon="fa-check-circle">
  1. **Verify Merchant Flags:**
     - Confirm `txn_s2s_flow = 2` is set in request
     - Check `nativeOtpSupportO` flag is enabled on your account

  2. **Test OTP Collection UI:**
     - Ensure your OTP input field is working
     - Validate OTP format (typically 6 digits)
     - Test timeout handling (OTP expires after a set time)

  3. **Test referenceId Handling:**
     - Confirm you're storing the `referenceId` from Step 1.4
     - Verify it's correctly passed in Step 1.5
</Accordion>

### Step 2.2: Simulate a Successful Transaction

<Accordion title="Step 2.2: Simulate a Successful Transaction" icon="fa-thumbs-up">
  > **⚠️ Info Gap:** Test OTP values and test card numbers for PureS2S Headless needed. Contact PayU for test data.

  **Test Flow:**

  1. Submit payment request with test credentials
  2. Receive `referenceId` in response
  3. Display OTP input on your UI
  4. Use test OTP (obtain from PayU)
  5. Submit OTP via ResponseHandler
  6. Decode and verify response
  7. Check transaction status in dashboard
</Accordion>

### Step 2.3: Simulate a Failed Transaction

<Accordion title="Step 2.3: Simulate a Failed Transaction" icon="fa-times-circle">
  **Test Error Scenarios:**

  1. **Invalid OTP** — Submit incorrect OTP value
  2. **OTP Timeout** — Wait beyond OTP expiry time before submitting
  3. **Invalid referenceId** — Submit OTP with wrong referenceId
  4. **Multiple OTP Attempts** — Test OTP retry limits
</Accordion>

### Step 2.4: Post-Transaction Verification

<Accordion title="Step 2.4: Post-Transaction Verification" icon="fa-magnifying-glass">
  1. **Decode ResponseHandler Payload:**
     - Ensure base64 decoding works correctly
     - Validate JSON parsing

  2. **Verify Hash:**
     - Compute reverse hash
     - Compare with response hash

  3. **Cross-Verify:**
     - Check transaction in PayU dashboard
     - Confirm status matches decoded response
</Accordion>

***

## Step 3: Going Live — Your Final Checklist

### Step 3.1: Update to Production Credentials

<Accordion title="Step 3.1: Update to Production Credentials" icon="fa-list-check">
  Update endpoints and credentials:

  | Environment    | `/_payment` URL                                                     | ResponseHandler URL                                                                      |
  | -------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
  | **Test**       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     | [https://test.payu.in/ResponseHandler.php](https://test.payu.in/ResponseHandler.php)     |
  | **Production** | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) | [https://secure.payu.in/ResponseHandler.php](https://secure.payu.in/ResponseHandler.php) |
</Accordion>

### Step 3.2: Final Integration Verification

<Accordion title="Step 3.2: Final Integration Verification" icon="fa-magnifying-glass">
  **✅ Security Review:**

  - Confirm PureS2S Headless is approved by PayU security team
  - Validate PCI compliance for card data handling
  - Ensure OTP is never logged or stored

  **✅ Live Transaction Test:**

  - Process a real transaction with small amount
  - Test OTP delivery on real mobile number
  - Verify end-to-end flow including authorization

  **✅ Error Handling:**

  - Test OTP retry mechanism
  - Verify timeout handling
  - Check invalid OTP error messaging

  **✅ Performance:**

  - Monitor ResponseHandler response times
  - Set appropriate timeout values
  - Implement retry logic for network failures
</Accordion>

***

> **⚠️ Security Note:**<br />PureS2S Headless requires additional security review. Contact PayU before deploying to production.

> **📞 Need Help?**
>
> - Technical Support: [support@payu.in](mailto:support@payu.in)
> - Security Review: [security@payu.in](mailto:security@payu.in)
> - Documentation: [https://docs.payu.in](https://docs.payu.in)
