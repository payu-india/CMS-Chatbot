---
title: Testing and Go Live - OAuth Flow Partner Integration
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
This checklist covers everything you need to test and validate the Co-Branded OAuth flow before going live.

## Postman Collection

<Callout icon="📘" theme="success">
  Accelerate your integration workflow with our Postman collection for OAuth Integration. Click the Download Postman Collection button below to download and get started.

  <HTMLBlock>{`
                  <style>
                  .tooltip-btn {
                      position: relative;
                      background-color: #4CAF50;
                      color: white;
                      padding: 10px 20px;
                      border: none;
                      border-radius: 5px;
                      cursor: pointer;
                      font-weight: bold;
                  }
                  .tooltip-btn:hover::after {
                      content: attr(data-tooltip);
                      position: absolute;
                      bottom: 125%;
                      left: 50%;
                      transform: translateX(-50%);
                      background-color: #333;
                      color: white;
                      padding: 5px 10px;
                      border-radius: 4px;
                      white-space: nowrap;
                      font-size: 12px;
                      z-index: 1;
                  }
                  </style>

                  <button onclick="window.open('https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/collection/3ztf96f/payu-oauth2-collection', '_blank')"
                          class="tooltip-btn"
                          data-tooltip="Click to download the Postman collection and explore OAuth APIs.">
                      Access Postman Collection
                  </button>
  `}</HTMLBlock>
</Callout>

***

## Test Environment

Use the following test environment endpoints for OAuth Integration:

| Resource                         | Test Environment URL                                                                                 | Production Environment URL                                                                      |
| -------------------------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Authorization Page               | `https://uat-onepayuonboarding.payu.in/app/account/signup&reseller_id={Reseller UUID}&state={state}` | `https://onboarding.payu.in/app/account/signup?reseller_id={reseller_id}&state={session state}` |
| Validate Auth Code               | `https://testdashboard.payu.in/oauth/validate-auth-code`                                             | `https://dashboard.payu.in/oauth/validate-auth-code`                                            |
| Get Merchant Credentials         | `https://testdashboard.payu.in/oauth/get-merchant-credentials`                                       | `https://dashboard.payu.in/oauth/get-merchant-credentials`                                      |
| Payment APIs (Partner API Layer) | `https://test-partnerapilayer.payu.in/apilayer/partner/payments`                                     | `https://partnerapilayer.payu.in/apilayer/partner/payments`                                     |

***

## Testing OAuth Integration

Follow these steps to test the complete OAuth onboarding flow:

<Accordion title="1. Setup Test Credentials" icon="fa-list-check">
  **Prerequisites:**

  - Partner Client ID and Client Secret (test environment)
  - Whitelisted redirect URL (test environment)
  - Access to PayU Partner Portal (test mode)

  > Contact your PayU Key Account Manager (KAM) to:
  >
  > - Enable OAuth onboarding for your partner account
  > - Obtain test environment Client ID and Secret
  > - Whitelist your test redirect URL(s)

  **How to Download Credentials:**

  1. Log in to [PayU Partner Portal](https://test-partner.payu.in) (test environment)
  2. Navigate to **Merchant Integration** → **Partner Integration**
  3. Click **Download Credentials**
  4. Save Client ID and Client Secret securely
</Accordion>

<Accordion title="2. Test Authorization URL Construction" icon="fa-list-check">
  <Accordion title="Step 1: Build Authorization URL" icon="fa-list-check">
    Construct the authorization URL with the required parameters:

    **Test URL Format:**

    ```
    https://uat-onepayuonboarding.payu.in/app/account/signup?reseller_id={Reseller UUID}&state={state}&email=(reseller email ID)
    ```

    **Required Parameters:**

    | Parameter          | Description                                                                                                                                       |
    | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
    | reseller_id        | Contains the reseller UUID. For more information on how to get the UUID, refer to [Download Client Credentials.](doc:download-client-credentials) |
    | state              | Contains encoded session state.                                                                                                                   |
    | email `(optional)` | Contains reseller email ID.                                                                                                                       |

    **Sample Authorization URL:**

    ```
    https://onboarding.payu.in/app/account/signup?reseller_id=66ed-fc3c-512f47ed-ac95-4319452fbd89&state=Uqnr5ge22U
    ```

    **Validation Points:**

    - [ ] `reseller_id` is correctly populated with encoded Merchant ID and email
    - [ ] `state` parameter carries a unique session state value
    - [ ] URL opens the PayU authorization/sign-up page
    - [ ] No browser errors or warnings
  </Accordion>

  <Accordion title="Step 2: URL Encoding Test" icon="fa-list-check">
    Verify URL encoding is correct:

    | Original URL                                       | URL Encoded                                                    |
    | -------------------------------------------------- | -------------------------------------------------------------- |
    | `https://partner.example.com/callback`             | `https%3A%2F%2Fpartner.example.com%2Fcallback`                 |
    | `https://partner.example.com/callback?session=123` | `https%3A%2F%2Fpartner.example.com%2Fcallback%3Fsession%3D123` |
    | `https://partner.example.com/callback?a=1&b=2`     | `https%3A%2F%2Fpartner.example.com%2Fcallback%3Fa%3D1%26b%3D2` |

    <Callout icon="📘" theme="info">
      ### **Tip:** Use online URL encoding tools or programming language built-in functions:

      - JavaScript: `encodeURIComponent(url)`
      - Python: `urllib.parse.quote(url, safe='')`
      - PHP: `urlencode($url)`
      - Java: `URLEncoder.encode(url, "UTF-8")`
    </Callout>
  </Accordion>
</Accordion>

<Accordion title="3. Test Merchant Authorization Flow" icon="fa-list-check">
  <Accordion title="Scenario 1: New Merchant Registration" icon="fa-list-check">
    **Test Steps:**

    1. Click authorization URL
    2. PayU authorization page loads
    3. Click "Create New Account"
    4. Fill merchant registration form:
       - Business name: `Test Business OAuth`
       - Email: `test.oauth.{timestamp}@example.com`
       - Mobile: `9999999999`
       - PAN: `AAAPA1234A` (test PAN)
    5. Complete OTP verification
    6. Grant authorization to partner app
    7. Redirected to partner redirect URL with `auth_code`

    **Validation Points:**

    - [ ] Registration form loads correctly
    - [ ] Mobile OTP received and verified
    - [ ] Email verification completed
    - [ ] Partner branding visible (if configured)
    - [ ] Authorization grant screen displays correctly
    - [ ] Redirect to partner URL successful
    - [ ] `auth_code` present in URL parameters
  </Accordion>

  <Accordion title="Scenario 2: Existing Merchant Login" icon="fa-list-check">
    **Test Steps:**

    1. Click authorization URL
    2. PayU authorization page loads
    3. Login with existing test merchant credentials
    4. Grant authorization to partner app
    5. Redirected to partner redirect URL with `auth_code`

    **Validation Points:**

    - [ ] Login form loads correctly
    - [ ] Authentication successful
    - [ ] Authorization grant screen displays
    - [ ] Partner app details shown correctly
    - [ ] Redirect successful with `auth_code`
  </Accordion>

  <Accordion title="Scenario 3: Already Onboarded Merchant" icon="fa-list-check">
    **Test Steps:**

    1. Click authorization URL with merchant already onboarded through partner
    2. Auto-redirect should occur with `auth_code`

    **Validation Points:**

    - [ ] No additional consent required
    - [ ] Immediate redirect to partner URL
    - [ ] Valid `auth_code` received
  </Accordion>

  <Accordion title="Scenario 4: Merchant Denies Authorization" icon="fa-list-check">
    **Test Steps:**

    1. Click authorization URL
    2. Login as merchant
    3. Click "Deny" or "Cancel" on authorization screen
    4. Redirected to partner URL

    **Validation Points:**

    - [ ] Redirect occurs even on denial
    - [ ] Error parameter in redirect URL (e.g., `?error=access_denied`)
    - [ ] Partner app handles denial gracefully
    - [ ] User-friendly error message displayed
  </Accordion>
</Accordion>

<Accordion title="4. Test Authorization Code Exchange" icon="fa-key">
  **API:** [Validate Auth Code and Client API](/reference/validate_authcode_and_client_api)

  <Accordion title="Step 1: Capture Authorization Code" icon="fa-list-check">
    From the callback URL, extract the `auth_code` parameter:

    **Callback URL Format:**

    ```
    https://onboarding.payu.in/app/account/signup?reseller_id={{reseller_id}}&state={session state}
    ```

    **Example:**

    ```
    https://onboarding.payu.in/app/account/signup?reseller_id=11f1-1078-ee249a86-9fdf-0aad783eb813&state=1513493
    ```

    > **Important:** The `auth_code` is single-use and expires after a short period. Exchange it immediately for merchant credentials.
  </Accordion>

  <Accordion title="Step 2: Exchange Code for Credentials" icon="fa-code">
    Call the Validate Auth Code API immediately after receiving the `auth_code`:

    **Sample Request:**

    ```bash
    curl --location 'https://testdashboard.payu.in/oauth/validate-auth-code' \
    --header 'Content-Type: application/json' \
    --data '{
        "client_id": "ABC123",
        "client_secret": "your_client_secret",
        "auth_code": "XYZ789ABC123"
    }'
    ```

    **Expected Success Response:**

    ```json
    {
        "access_token": "e6ff7e34b704be2b14c8ae3c0e776597df4ae7de9e12d3e4c79781fcbbf2c4bb",
        "token_type": "Bearer",
        "expires_in": 7199,
        "refresh_token": "356fe080daa69438e0c2d3b0a80b3fe4aa3f78b264e6092e95e4429ae59486a7",
        "scope": "credentials_using_oauth create_payment_links read_payment_links update_payment_links delete_payment_links",
        "created_at": 1709198191,
        "user_uuid": "11ed-933c-d307ba06-b71a-0a64ecf8a4cc"
    }
    ```

    **Response Parameters:**

    | Parameter       | Description                                 |
    | --------------- | ------------------------------------------- |
    | `access_token`  | Bearer token to authorize payment API calls |
    | `token_type`    | Always `Bearer`                             |
    | `expires_in`    | Token validity in seconds                   |
    | `refresh_token` | Token used to obtain a new access token     |
    | `scope`         | Permissions granted                         |
    | `created_at`    | Unix timestamp of token creation            |
    | `user_uuid`     | Unique identifier of the onboarded merchant |

    **Validation Points:**

    - [ ] API responds within 2 seconds
    - [ ] `access_token` received and is a valid hex string
    - [ ] `token_type` is `Bearer`
    - [ ] `expires_in` value is present
    - [ ] `user_uuid` received and associated with correct merchant
  </Accordion>

  <Accordion title="Step 3: Test Error Scenarios" icon="fa-shield-check">
    **Invalid Client ID:**

    ```json
    {
        "client_id": "INVALID",
        "client_secret": "your_client_secret",
        "auth_code": "valid_auth_code"
    }
    ```

    **Expected Response:**

    ```json
    {
        "status": 0,
        "msg": "Invalid client credentials"
    }
    ```

    **Invalid Client Secret:**

    ```json
    {
        "client_id": "ABC123",
        "client_secret": "INVALID",
        "auth_code": "valid_auth_code"
    }
    ```

    **Expected Response:**

    ```json
    {
        "status": 0,
        "msg": "Invalid client credentials"
    }
    ```

    **Expired/Invalid Auth Code:**

    ```json
    {
        "client_id": "ABC123",
        "client_secret": "your_client_secret",
        "auth_code": "EXPIRED_OR_INVALID"
    }
    ```

    **Expected Response:**

    ```json
    {
        "status": 0,
        "msg": "Invalid auth code"
    }
    ```

    **Reused Auth Code:**

    ```json
    {
        "client_id": "ABC123",
        "client_secret": "your_client_secret",
        "auth_code": "ALREADY_USED_CODE"
    }
    ```

    **Expected Response:**

    ```json
    {
        "status": 0,
        "msg": "Auth code already used"
    }
    ```

    **Validation Points:**

    - [ ] Invalid credentials rejected with `status: 0`
    - [ ] Expired codes rejected appropriately
    - [ ] Reused codes cannot be exchanged again
    - [ ] Error messages are clear and actionable
    - [ ] No sensitive information leaked in errors
  </Accordion>

  <Accordion title="Step 4: Test Auth Code Expiration" icon="fa-shield-check">
    **Test Steps:**

    1. Generate auth code
    2. Wait for the configured expiry period
    3. Attempt to exchange the expired code
    4. Verify rejection

    **Validation Points:**

    - [ ] Expired codes rejected
    - [ ] Appropriate error message returned
    - [ ] Must generate a new auth code by restarting the OAuth flow
  </Accordion>
</Accordion>

<Accordion title="5. Test Credential Storage and Security" icon="fa-shield-check">
  <Accordion title="Test 1: Secure Storage" icon="fa-shield-check">
    **Validation Points:**

    - [ ] `access_token` stored encrypted in database
    - [ ] `refresh_token` stored encrypted in database
    - [ ] Tokens never logged in plain text
    - [ ] Tokens not exposed in client-side code
    - [ ] Database access controlled and audited
  </Accordion>

  <Accordion title="Test 2: Credential Retrieval" icon="fa-key">
    **Test Steps:**

    1. Store tokens after receiving from the Validate Auth Code API
    2. Associate with partner's internal merchant ID using `user_uuid`
    3. Retrieve access token for payment processing
    4. Decrypt and use as Bearer token in payment API calls

    **Validation Points:**

    - [ ] Tokens retrieved successfully
    - [ ] Decryption works correctly
    - [ ] Associated with correct merchant via `user_uuid`
    - [ ] Audit log created for retrieval
  </Accordion>

  <Accordion title="Test 3: Access Control" icon="fa-shield-check">
    **Test Steps:**

    1. Implement role-based access control
    2. Test admin access to stored tokens
    3. Test non-admin access denied
    4. Test API-level access restrictions

    **Validation Points:**

    - [ ] Only authorized roles can access tokens
    - [ ] Access attempts logged
    - [ ] Failed access attempts trigger alerts
    - [ ] No tokens visible in application logs
  </Accordion>
</Accordion>

<Accordion title="6. Test Get Merchant Credentials API" icon="fa-magnifying-glass">
  **API:** [Get Merchant Credentials API](/reference/get_merchant_credentials_api)

  **Use Case:** Retrieve credentials at a later time if needed

  <Accordion title="Step 1: Basic Retrieval" icon="fa-code">
    ```bash
    curl --location 'https://testdashboard.payu.in/oauth/get-merchant-credentials' \
    --header 'Content-Type: application/json' \
    --data '{
        "client_id": "ABC123",
        "client_secret": "your_client_secret"
    }'
    ```

    **Expected Response:**

    ```json
    {
        "status": 1,
        "msg": "Success",
        "merchant_key": "mK3j2L9p",
        "salt": "sA7x9B2c"
    }
    ```

    **Validation Points:**

    - [ ] Credentials match those received earlier
    - [ ] API responds within 2 seconds
    - [ ] Can be called multiple times
    - [ ] Same credentials returned consistently
  </Accordion>

  <Accordion title="Step 2: Error Scenarios" icon="fa-shield-check">
    **Invalid Client Credentials:**

    ```json
    {
        "client_id": "INVALID",
        "client_secret": "INVALID"
    }
    ```

    **Expected Response:**

    ```json
    {
        "status": 0,
        "msg": "Invalid client credentials"
    }
    ```

    **No Merchant Onboarded:**

    For a valid partner client that hasn't onboarded any merchant via OAuth:

    **Expected Response:**

    ```json
    {
        "status": 0,
        "msg": "No merchant found for this partner"
    }
    ```

    **Validation Points:**

    - [ ] Invalid credentials rejected
    - [ ] Appropriate error messages returned
    - [ ] No sensitive data in error responses
  </Accordion>
</Accordion>

<Accordion title="7. Test Payment Integration with OAuth Credentials" icon="fa-check-circle">
  After receiving merchant credentials via OAuth, test payment collection using the Partner API Layer. Use the `access_token` received from the Validate Auth Code API as the Bearer token.

  <Accordion title="Step 1: Test Hosted Checkout Payment Request" icon="fa-code">
    Submit a payment using the Partner Payments API:

    **Sample Request:**

    ```curl
    curl --location --request POST \
    'https://test-partnerapilayer.payu.in/apilayer/partner/payments' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer <access_token>' \
    --data-raw '{
      "txnid": "nY3tkz3vciHFGTjblyFeycL2Zn1m",
      "amount": 1090.33,
      "productinfo": "whatsapp",
      "firstname": "Manikanta",
      "reseller_id": "83fe-eb64-021844d8-9397-26535b1bf0c2",
      "merchant_id": "8238480",
      "phone": 7036722360,
      "hash": "52f45927e221a16bd5372709516de5110c06c55e0057f8a18a3b9b9f2c2f176870af276274709910f27d7c5df44822777542e3d4b86f29e8304e17fcb373133c",
      "lastname": "CHeruku",
      "email": "manik.cr24@gmail.com",
      "curl": "<YOUR_CANCEL_URL>",
      "furl": "<YOUR_FAILURE_URL>",
      "surl": "<YOUR_SUCCESS_URL>",
      "udf1": "whatsapp"
    }'
    ```

    **Expected Response:**

    ```text
    {
        "redirectUri": "https://apitest.payu.in/public/#/35de666bac018494a06205addba2962cdb8d03ca9c2fa7954807098709f1b6dc"
    }
    ```

    **Validation Points:**

    - [ ] API call succeeds with valid Bearer token
    - [ ] `redirectUri` received in response
    - [ ] Redirect URI opens the PayU payment page
    - [ ] Merchant name displayed correctly on payment page
    - [ ] Test transaction completes successfully
    - [ ] Redirected to success URL (SURL) after payment
  </Accordion>

  <Accordion title="Step 2: Test UPI S2S Payment Request" icon="fa-code">
    For UPI S2S flow, use the same Partner Payments API endpoint with `txn_s2s_flow`:

    **Sample Request:**

    ```curl
    curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/payments' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer 9d2ab8e1b99aa02f6b827af5b5000b277d9cb1cd037acb7cb31436a5b0da4f74' \
    --data-raw '{
        "txnid": "nY3tkz3vciHFGTjblyFeycL2Zn1m",
        "amount": 1090.33,
        "productinfo": "whatsapp",
        "firstname": "Manikanta",
        "reseller_id": "83fe-eb64-021844d8-9397-26535b1bf0c2",
        "merchant_id": 8238480,
        "phone": 7036722360,
        "hash": "5aadceaf6bec9158ccba8ec0dab32debcacbfd50e3587c077fa11107a5be0ac26712fae230522afb8908d068122c02f2d5c733a46c33ace0f66e5cc9d2ae4714",
        "lastname": "CHeruku",
        "email": "manik.cr24@gmail.com",
        "curl": "https://www.google.com",
        "furl": "https://www.google.com",
        "surl": "https://www.youtube.com",
        "txn_s2s_flow": "4",
        "s2s_device_info": "ewew",
        "s2s_client_ip": "ewew"
    }'
    ```

    **Expected Response:**

    ```text
    {
        "metaData": {
            "message": null,
            "referenceId": "024d9afbdbf85bd35b25649ccf983e16ee3d4646c2cdcffada88bd2df371fd43",
            "statusCode": null,
            "txnId": "nY3tkz3vciHFGTjblyFeycL2Zn1m",
            "txnStatus": "pending",
            "unmappedStatus": "pending"
        },
        "result": {
            "paymentId": 403993715529028543,
            "merchantName": "Merchant",
            "merchantVpa": null,
            "amount": "1090.33",
            "intentURIData": "pa=&pn=&tr=403993715529028543&tid=PPPL403993715529028543290523133325&am=1090.33&cu=INR&tn=UPI Transaction for PPPL403993715529028543290523133325",
            "otpPostUrl": "https://test.payu.in/ResponseHandler.php"
        }
    }
    ```

    **Validation Points:**

    - [ ] `txnStatus` is `pending` on initial response
    - [ ] `intentURIData` received for UPI deep link
    - [ ] `otpPostUrl` present for OTP handling
    - [ ] Transaction completes after UPI confirmation
  </Accordion>

  <Accordion title="Step 3: Verify Payment Response" icon="fa-shield-check">
    After payment completes, verify the transaction via PayU's callback:

    **Validation Points:**

    - [ ] SURL/FURL receives POST callback from PayU
    - [ ] `txnid` in callback matches the original request
    - [ ] `amount` in callback matches the original request
    - [ ] `status` field correctly reflects payment outcome (`success`/`failure`)
    - [ ] `mihpayid` (PayU transaction ID) is present
    - [ ] Reverse hash validation passes to confirm authenticity
  </Accordion>
</Accordion>

<Accordion title="8. Test Multiple Merchant Onboarding" icon="fa-list-check">
  Test onboarding multiple merchants through OAuth:

  **Test Steps:**

  1. Onboard Merchant A via OAuth
  2. Store Merchant A's `access_token` and `user_uuid`
  3. Onboard Merchant B via OAuth
  4. Store Merchant B's `access_token` and `user_uuid`
  5. Verify both sets of credentials work independently

  **Validation Points:**

  - [ ] Each merchant has a unique `access_token` and `user_uuid`
  - [ ] Tokens stored separately and correctly associated via `user_uuid`
  - [ ] Payments for Merchant A use Merchant A's Bearer token
  - [ ] Payments for Merchant B use Merchant B's Bearer token
  - [ ] No credential cross-contamination
</Accordion>

<Accordion title="9. Test Error Handling and Edge Cases" icon="fa-shield-check">
  <Accordion title="Scenario 1: Redirect URL Mismatch" icon="fa-times-circle">
    **Test Steps:**

    1. Whitelist URL: `https://partner.example.com/callback`
    2. Use redirect URL: `https://different.example.com/callback`
    3. Attempt authorization

    **Expected Result:**

    - [ ] Authorization blocked
    - [ ] Error message displayed
    - [ ] No auth code generated
  </Accordion>

  <Accordion title="Scenario 2: Missing Parameters" icon="fa-times-circle">
    **Test Steps:**

    1. Build auth URL without `reseller_id`
    2. Build auth URL without `state`
    3. Attempt authorization

    **Expected Result:**

    - [ ] Error message displayed
    - [ ] User not able to proceed
  </Accordion>

  <Accordion title="Scenario 3: Network Timeout" icon="fa-times-circle">
    **Test Steps:**

    1. Simulate slow network during API call
    2. Test timeout handling
    3. Test retry logic

    **Validation Points:**

    - [ ] Timeout handled gracefully
    - [ ] User-friendly error message
    - [ ] Retry mechanism works
    - [ ] No duplicate credential storage
  </Accordion>

  <Accordion title="Scenario 4: Concurrent OAuth Flows" icon="fa-list-check">
    **Test Steps:**

    1. Start OAuth flow for Merchant X
    2. Before completing, start OAuth flow for Merchant Y
    3. Complete both flows

    **Validation Points:**

    - [ ] Both flows complete successfully
    - [ ] Correct credentials stored for each merchant
    - [ ] No session confusion
    - [ ] State management working correctly
  </Accordion>
</Accordion>

***

## End-to-End Testing Scenarios

Test the complete integration flow from OAuth authorization to payment collection:

<Accordion title="Scenario 1: Complete OAuth Flow + First Payment" icon="fa-thumbs-up">
  1. Build and open the authorization URL
  2. Register new test merchant or login with existing credentials
  3. Grant authorization to partner app
  4. Receive auth code in redirect
  5. Exchange auth code for credentials via [Validate Auth Code API](/reference/validate_authcode_and_client_api)
  6. Store `access_token` and `user_uuid` securely
  7. Submit test payment to Partner Payments API using Bearer token
  8. Verify payment success via `redirectUri`
  9. Validate payment callback on SURL

  **Expected Duration:** 3–5 minutes

  **Validation Points:**

  - [ ] All steps complete without errors
  - [ ] `access_token` received and stored
  - [ ] Payment successful with Bearer token auth
  - [ ] Callback received with valid data
</Accordion>

<Accordion title="Scenario 2: OAuth Re-authorization" icon="fa-magnifying-glass">
  1. Complete initial OAuth flow for a merchant
  2. Store credentials
  3. Later, initiate OAuth flow again for same merchant
  4. Verify auto-redirect with new auth code
  5. Exchange new auth code for credentials
  6. Verify `user_uuid` matches previously stored record

  **Validation Points:**

  - [ ] Re-authorization works smoothly
  - [ ] Merchant not asked for consent again
  - [ ] Same `user_uuid` returned
  - [ ] No duplicate merchant records
</Accordion>

<Accordion title="Scenario 3: Bulk Merchant Onboarding via OAuth" icon="fa-list-check">
  1. Prepare list of 10 test merchants
  2. Send OAuth links to each
  3. Track completion status
  4. Store all `access_token` and `user_uuid` values
  5. Test payment for each merchant using their respective Bearer token

  **Validation Points:**

  - [ ] All merchants onboarded successfully
  - [ ] Each has a unique `access_token` and `user_uuid`
  - [ ] Parallel processing works
  - [ ] No credential mix-ups
</Accordion>

<Accordion title="Scenario 4: Error Recovery" icon="fa-times-circle">
  1. Start OAuth flow
  2. Receive auth code
  3. API call fails (simulate network error)
  4. Retry auth code exchange
  5. Verify success on retry

  **Validation Points:**

  - [ ] Retry successful
  - [ ] Auth code still valid within expiry
  - [ ] `access_token` received
  - [ ] No duplicate processing
</Accordion>

***

## Go-Live Checklist

Use this checklist before moving to production:

### OAuth Integration — Go-Live Checklist

- [ ] **Legal Agreements**
  - [ ] Partner Reseller Agreement signed
  - [ ] OAuth integration terms accepted
  - [ ] Data Processing Addendum in place

- [ ] **Production Credentials**
  - [ ] Production Client ID obtained from Partner Portal
  - [ ] Production Client Secret obtained
  - [ ] Production redirect URL(s) whitelisted
  - [ ] Credentials stored securely (secrets manager/vault)
  - [ ] No test credentials in production code

- [ ] **OAuth Configuration**
  - [ ] OAuth scope enabled by PayU KAM for production
  - [ ] Production authorization URL configured: `https://onboarding.payu.in/app/account/signup?reseller_id={reseller_id}&state={session state}`
  - [ ] Production API endpoints configured
  - [ ] Redirect URLs use HTTPS
  - [ ] All redirect URLs whitelisted in Partner Portal

- [ ] **Authorization Flow**
  - [ ] Authorization URL construction tested with correct `reseller_id` and `state` parameters
  - [ ] Merchant login and registration tested
  - [ ] Authorization grant screen tested
  - [ ] Callback handling implemented
  - [ ] Auth code extraction working
  - [ ] `state` parameter used for session binding (recommended for security)

- [ ] **API Integration**
  - [ ] Validate Auth Code API integration complete
  - [ ] Get Merchant Credentials API integration complete (optional)
  - [ ] API error handling implemented
  - [ ] Timeout handling (30 second default)
  - [ ] Retry logic with exponential backoff
  - [ ] Rate limiting handled (429 responses)

- [ ] **Credential Management**
  - [ ] Auth code exchange happens immediately after redirect
  - [ ] `access_token` and `refresh_token` stored securely
  - [ ] Tokens encrypted at rest
  - [ ] Tokens associated with correct merchant via `user_uuid`
  - [ ] Token refresh flow implemented before expiry
  - [ ] No tokens logged in plain text
  - [ ] No tokens exposed to client-side

- [ ] **Payment Integration**
  - [ ] Partner Payments API integration tested with Bearer token auth
  - [ ] Hosted Checkout flow tested end-to-end
  - [ ] UPI S2S flow tested end-to-end (if applicable)
  - [ ] Success callback (SURL) implemented
  - [ ] Failure callback (FURL) implemented
  - [ ] Cancel callback (CURL) implemented
  - [ ] Transaction verification integrated

- [ ] **Security Best Practices**
  - [ ] HTTPS enforced on all endpoints
  - [ ] Redirect URLs validated before use
  - [ ] `state` parameter used to prevent CSRF
  - [ ] Auth codes used only once
  - [ ] Auth code expiry handled
  - [ ] Client secret never exposed to client
  - [ ] XSS protection implemented
  - [ ] SQL injection prevention in place

- [ ] **Error Handling**
  - [ ] Invalid client credentials handled
  - [ ] Expired auth code handled
  - [ ] Used auth code rejection handled
  - [ ] Network errors handled gracefully
  - [ ] User-friendly error messages displayed
  - [ ] Error logging implemented
  - [ ] Alert notifications for critical errors

- [ ] **Data Privacy & Compliance**
  - [ ] GDPR/data privacy compliance verified
  - [ ] User consent captured appropriately
  - [ ] Minimal PII stored
  - [ ] Data retention policy implemented
  - [ ] Right to erasure implemented (if applicable)
  - [ ] Privacy policy updated to mention OAuth

- [ ] **Monitoring & Logging**
  - [ ] OAuth flow events logged
  - [ ] API requests/responses logged (excluding secrets)
  - [ ] Token storage/retrieval audited
  - [ ] Error tracking system integrated
  - [ ] Performance monitoring setup
  - [ ] Alert notifications configured
  - [ ] Dashboard for merchant onboarding status

- [ ] **Testing Completed**
  - [ ] End-to-end OAuth flow tested in production (test merchants)
  - [ ] Multiple merchant onboarding tested
  - [ ] Payment with OAuth Bearer token tested
  - [ ] Error scenarios tested
  - [ ] Edge cases validated
  - [ ] Load testing completed

- [ ] **Documentation**
  - [ ] Internal documentation for OAuth flow
  - [ ] Runbooks for common issues
  - [ ] Escalation procedures defined
  - [ ] Knowledge base updated
  - [ ] Training provided to support team

***

## Production URLs Reference

Once all testing is complete and checklist items are verified, update all endpoints to production:

| Resource                    | Production URL                                                                                  |
| --------------------------- | ----------------------------------------------------------------------------------------------- |
| Authorization Page          | `https://onboarding.payu.in/app/account/signup?reseller_id={reseller_id}&state={session state}` |
| Validate Auth Code          | `https://dashboard.payu.in/oauth/validate-auth-code`                                            |
| Get Merchant Credentials    | `https://dashboard.payu.in/oauth/get-merchant-credentials`                                      |
| Payment (Partner API Layer) | `https://partnerapilayer.payu.in/apilayer/partner/payments`                                     |
| Verify Payment              | `https://info.payu.in/merchant/postservice?form=2`                                              |

***

## Common Issues & Troubleshooting

<Accordion title="Issue 1: Authorization URL Not Loading" icon="fa-times-circle">
  **Symptoms:** Authorization page shows error or doesn't load

  **Possible Causes:**

  - Invalid or missing `reseller_id`
  - Client account not enabled for OAuth
  - `state` parameter malformed or missing
  - OAuth not enabled for partner account

  **Solution:**

  1. Verify `reseller_id` is correctly constructed with encoded Merchant ID and email
  2. Contact PayU KAM to confirm OAuth is enabled
  3. Ensure `state` carries a valid encoded session value
  4. Verify using the test environment URL for testing
</Accordion>

<Accordion title="Issue 2: Redirect URL Mismatch Error" icon="fa-times-circle">
  **Symptoms:** Error message: "Redirect URL not whitelisted"

  **Possible Causes:**

  - Redirect URL not whitelisted in Partner Portal
  - URL encoding mismatch (encoded vs decoded)
  - HTTP vs HTTPS mismatch
  - Trailing slash mismatch

  **Solution:**

  1. Log in to Partner Portal → Settings → OAuth Configuration
  2. Add exact redirect URL to whitelist (including protocol and path)
  3. Ensure URL in authorization request matches exactly
  4. Use HTTPS for all redirect URLs
  5. Be consistent with trailing slashes

  **Examples:**

  ```
  ✅ Correct: https://partner.example.com/callback
  ❌ Wrong: http://partner.example.com/callback (HTTP instead of HTTPS)

  ✅ Correct: https://partner.example.com/callback/
  ❌ Wrong: https://partner.example.com/callback (missing trailing slash if whitelisted with it)
  ```
</Accordion>

<Accordion title="Issue 3: Invalid Auth Code" icon="fa-times-circle">
  **Symptoms:** "Invalid auth code" error when calling Validate Auth Code API

  **Possible Causes:**

  - Auth code already used
  - Auth code expired
  - Incorrect auth code copied from URL
  - Special characters not handled properly

  **Solution:**

  1. Extract auth code immediately from redirect URL
  2. Exchange auth code within the expiry window of receiving it
  3. Use auth code only once
  4. Handle URL decoding properly if auth code contains special characters
  5. Generate new auth code by repeating OAuth flow
</Accordion>

<Accordion title="Issue 4: Merchant Credentials Not Received" icon="fa-times-circle">
  **Symptoms:** API returns success but no `access_token` or `user_uuid`

  **Possible Causes:**

  - Merchant not fully onboarded
  - KYC pending for merchant
  - Merchant account not activated

  **Solution:**

  1. Check merchant status in PayU dashboard
  2. Ensure merchant completed KYC
  3. Wait for merchant approval (if under review)
  4. Contact PayU support if merchant shows as active but tokens not received
</Accordion>

<Accordion title="Issue 5: Payment API Authorization Failure" icon="fa-times-circle">
  **Symptoms:** Partner Payments API returns `401 Unauthorized` or hash mismatch error

  **Possible Causes:**

  - Using an expired or invalid `access_token` as Bearer token
  - Incorrect `Authorization` header format
  - Hash string parameter order incorrect
  - Extra spaces in hash string

  **Solution:**

  1. Verify the `access_token` from OAuth is valid and not expired
  2. Use the format: `Authorization: Bearer <access_token>`
  3. Check hash string parameter order:
     ```
     key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT
     ```
  4. Trim all parameters to remove spaces
  5. Refresh the access token using the `refresh_token` if expired
</Accordion>

<Accordion title="Issue 6: Payment Callback Not Received" icon="fa-times-circle">
  **Symptoms:** Payment completed but SURL/FURL not triggered

  **Possible Causes:**

  - SURL/FURL not publicly accessible
  - Firewall blocking PayU servers
  - Incorrect URL in payment request
  - Server timeout during callback

  **Solution:**

  1. Verify SURL/FURL are publicly accessible (use external tools to test)
  2. Whitelist PayU IP ranges in firewall
  3. Ensure URLs use HTTPS
  4. Check server logs for incoming requests
  5. Implement Verify Payment API as fallback
  6. Return HTTP 200 OK quickly in callback handler
</Accordion>

<Accordion title="Issue 7: Multiple OAuth Sessions Confusion" icon="fa-times-circle">
  **Symptoms:** Wrong merchant credentials stored or retrieved

  **Possible Causes:**

  - Session management issues
  - `state` parameter not used or not validated
  - Concurrent OAuth flows not handled
  - Cache issues

  **Solution:**

  1. Use `state` parameter in authorization URL to bind sessions:
     ```
     https://onboarding.payu.in/app/account/signup?reseller_id={{reseller_id}}&state=SESSION_ID
     ```
  2. Verify `state` parameter in callback matches the original session
  3. Store `access_token` immediately after receiving, keyed to `user_uuid`
  4. Use unique `state` values to track each OAuth flow
  5. Implement proper session management
</Accordion>

<Accordion title="Issue 8: Auth Code Expiry" icon="fa-times-circle">
  **Symptoms:** Auth code rejected even when exchanged quickly

  **Possible Causes:**

  - Auth code expired (short expiry window)
  - Clock skew between servers

  **Solution:**

  1. Exchange auth code immediately after redirect — do not store or delay
  2. Ensure server clocks are synchronized (NTP)
  3. Generate a new auth code by restarting the OAuth flow
</Accordion>

***

## Performance Optimization

<Accordion title="Best Practices" icon="fa-list-check">
  1. **Parallel Processing**
     - Process multiple OAuth flows concurrently
     - Use asynchronous API calls where possible
     - Implement queuing for token storage

  2. **Token Caching**
     - Cache `access_token` securely for its `expires_in` duration
     - Use `refresh_token` to obtain new access tokens without re-authorizing
     - Use Redis or similar for session and token management

  3. **Database Optimization**
     - Index `user_uuid` and `client_id` columns
     - Use connection pooling
     - Optimize token retrieval queries

  4. **API Call Optimization**
     - Implement exponential backoff for retries on the Partner Payments API
     - Set appropriate timeouts (30 seconds recommended)
     - Handle `429 Too Many Requests` with backoff logic

  5. **Monitoring**
     - Track OAuth flow completion rates
     - Monitor API response times
     - Set up alerts for high error rates
     - Track token refresh success rates
</Accordion>

***

## Security Checklist

- [ ] **Transport Security**
  - [ ] All OAuth URLs use HTTPS
  - [ ] TLS 1.2 or higher enforced
  - [ ] Valid SSL certificates installed
  - [ ] HSTS headers configured

- [ ] **Data Protection**
  - [ ] Client secret stored in secrets manager (AWS Secrets Manager, HashiCorp Vault, etc.)
  - [ ] `access_token` and `refresh_token` encrypted at rest (AES-256)
  - [ ] Encryption keys rotated regularly
  - [ ] No tokens in application logs
  - [ ] No tokens in error messages

- [ ] **Access Control**
  - [ ] Role-based access control (RBAC) implemented
  - [ ] API endpoints require authentication
  - [ ] Admin access audited
  - [ ] Principle of least privilege applied

- [ ] **CSRF Protection**
  - [ ] `state` parameter used in OAuth flow
  - [ ] `state` parameter validated in callback
  - [ ] CSRF tokens on all forms
  - [ ] SameSite cookie attribute set

- [ ] **Input Validation**
  - [ ] Auth code validated before use
  - [ ] Client ID and Secret validated
  - [ ] Redirect URL validated against whitelist
  - [ ] All user inputs sanitized

- [ ] **Rate Limiting**
  - [ ] API rate limits implemented
  - [ ] Brute force protection on OAuth endpoints
  - [ ] IP-based rate limiting
  - [ ] Account lockout after multiple failures

- [ ] **Audit Logging**
  - [ ] All OAuth events logged
  - [ ] Token access logged
  - [ ] Failed authentication attempts logged
  - [ ] Logs retained according to policy
  - [ ] Log tampering protection

***

## Support & Escalation

<Accordion title="When to Contact PayU Support" icon="fa-list-check">
  Contact PayU support in these scenarios:

  - OAuth not enabled for your partner account
  - Redirect URL whitelisting issues
  - Merchant tokens not received despite successful OAuth flow
  - Repeated API failures (not related to your implementation)
  - Security concerns or suspected compromise
</Accordion>

<Accordion title="Contact Information" icon="fa-list-check">
  - **Partner Support Email:** [partner-support@payu.in](mailto:partner-support@payu.in)
  - **Technical Support:** Navigate to help.payu.in or send an mail with complete issue details (including mid) to [integration@payu.in](mailto:integration@payu.in)
  - **Key Account Manager:** (provided during onboarding)
</Accordion>

<Accordion title="Information to Provide When Contacting Support" icon="fa-list-check">
  When contacting support, include:

  1. Partner Client ID (never share Client Secret)
  2. Timestamp of issue
  3. Error messages received
  4. API request/response (redact sensitive data such as tokens)
  5. Steps to reproduce
  6. Environment (test/production)
</Accordion>

***

<Callout icon="🚧" theme="warn">
  ### **Important**

  Always test thoroughly in the test environment before going live. Conduct small-scale production testing with a few merchants before full rollout.
</Callout>

<Callout icon="📘" theme="info">
  ### **Best Practice**

  Implement comprehensive logging and monitoring to quickly identify and resolve issues. Set up alerts for high error rates or unusual patterns.
</Callout>

<Callout icon="🔒" theme="default">
  ### **Security Reminder**

  Never share your Client Secret, access tokens, or refresh tokens in logs, error messages, or support tickets. Treat them as passwords.
</Callout>
