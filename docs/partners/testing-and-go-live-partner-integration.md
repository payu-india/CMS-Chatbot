---
title: Testing and Go Live - Partner Integration
deprecated: false
hidden: false
metadata:
  robots: index
---
This section includes the Testing and Go Live checklist for Partner Integration onboarding and collect payment after onboarding.

## Test environment

| Resource                       | URL                                        |
| ------------------------------ | ------------------------------------------ |
| Authentication (Get Token API) | `https://uat-accounts.payu.in/oauth/token` |
| Onboarding APIs                | `https://uat-partner.payu.in`              |
| Collect Payment                | `https://test.payu.in`                     |

## Postman collection

<Callout icon="📘" theme="success">
  Accelerate your integration workflow with our Postman collection for Partner Integration. Click the Download Postman Collection button below to download and get started.

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
                      font-weight: bold; /* Added this line */
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

                  <button onclick="window.open('https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/collection/8fpyicz/partners-merchant-onboarding-apis', '_blank')" 
                          class="tooltip-btn" 
                          data-tooltip="Click to download the Postman collection and explore APIs.">
                      Access Postman Collection
                  </button>
  `}</HTMLBlock>


</Callout>



## Test Environment

Use the following test environment endpoints for Partner Integration:

| Resource | Test Environment URL | Production Environment URL |
|----------|---------------------|---------------------------|
| OAuth/Authentication | `https://uat-accounts.payu.in/oauth/token` | `https://accounts.payu.in/oauth/token` |
| Partner Onboarding APIs | `https://uat-partner.payu.in` | `https://partner.payu.in` |
| Payment APIs (Hosted Checkout) | `https://test.payu.in/_payment` | `https://secure.payu.in/_payment` |
| Payment Postservice | `https://test.payu.in/merchant/postservice.php` | `https://info.payu.in/merchant/postservice.php` |

> **Note:** All Partner API endpoints use UAT environment URLs with `uat-` prefix for testing.

---

## Testing Partner Onboarding Integration

### 1. Setup Test Credentials

**Prerequisites:**
- Partner Client ID and Client Secret (test environment)
- Access to partner dashboard (test mode)
- Postman or API testing tool

> Contact PayU Partner Support to obtain your test environment client credentials.

### 2. Test OAuth Authentication

**API Reference:** Get Token API

**Test Steps:**
1. Generate access token using test client ID and secret
2. Verify token expiration (default: 3600 seconds)
3. Test token refresh mechanism
4. Validate error handling for invalid credentials

**Expected Results:**
- Access token received successfully
- Token type is `Bearer`
- Refresh token received for renewal

### 3. Test Merchant Creation

**API Reference:** Create Merchant API

**Test Steps:**
1. Create a new merchant with valid test data
2. Use dummy PAN: `AAAPA1234A` (test PAN)
3. Use test mobile number: `9999999999`
4. Use test email: `test.merchant@example.com`

**Validation Points:**
- Merchant UUID generated
- Merchant ID (MID) created
- Merchant status is `created` or `pending_kyc`
- Response includes next steps

### 4. Test KYC Document Upload Flow

**APIs Used:**
- Fetch Required Documents API
- Upload KYC Document API
- Show KYC Document API
- Delete KYC Document API

**Test Steps:**
1. Fetch required documents for merchant
2. Upload each required document
3. Verify document upload status
4. Test document retrieval
5. Test document deletion (if needed)

**Document Upload Testing:**
- Upload PAN card
- Upload address proof
- Upload bank proof (cancelled cheque/statement)
- Upload authorization letter (if applicable)
- Upload business proof/certificate

**Validation Points:**
- Document format validation (PDF, JPG, PNG)
- File size limits (max 5MB per document)
- Document status tracking
- Error handling for invalid formats

### 5. Test Bank Details Addition

**API Reference:** Add/Update Bank Details API

**Test Steps:**
1. Add bank account details
2. Verify penny drop validation (if enabled)
3. Update existing bank details
4. Test IFSC code validation

**Validation Points:**
- Bank details saved successfully
- IFSC code validated
- Account holder name matches merchant name
- Penny drop verification completed (if applicable)

### 6. Test E-Sign/Agreement Flow

**APIs Used:**
- Generate Agreement for E-Sign API
- Send OTP to Signatory API
- E-Sign Merchant Agreement API

**Test Steps:**
1. Generate merchant agreement document
2. Send OTP to signatory email
3. Verify OTP and complete e-sign
4. Confirm signed agreement status

**Validation Points:**
- Agreement PDF generated
- OTP sent to signatory
- E-sign completed successfully
- Agreement status updated to `signed`

### 7. Test Merchant Status Tracking

**API Reference:** Get Merchant Details API

**Test Steps:**
1. Retrieve merchant details after each step
2. Monitor merchant status transitions
3. Track KYC completion percentage
4. Identify pending requirements

**Expected Status Flow:**
1. `created` - Initial merchant creation
2. `pending_kyc` - KYC documents pending
3. `kyc_submitted` - Documents uploaded
4. `under_review` - PayU team reviewing
5. `approved` - Merchant activated
6. `live` - Ready for transactions

**Validation Points:**
- Status transitions correctly
- Pending actions clearly identified
- Error messages are actionable
- Completion percentage accurate

### 8. Test Webhook Integration

**API Reference:** Partner Webhook

**Test Steps:**
1. Configure webhook endpoint in partner dashboard
2. Implement webhook receiver endpoint
3. Test webhook signature verification
4. Test idempotency handling
5. Test retry mechanism

**Webhook Events to Test:**
- merchant.created
- merchant.kyc_submitted
- merchant.approved
- merchant.rejected
- merchant.live

**Validation Points:**
- Webhook received within SLA
- Signature verified successfully
- Duplicate webhooks handled (idempotency)
- Retry logic working for failures
- Status polling as fallback

---

## Testing Partner Payment Integration

### 1. Setup Payment Test Credentials

**Prerequisites:**
- Test Merchant Key and Salt (from onboarded merchant)
- Partner access token (OAuth)
- Test payment cards/methods

> Refer to Test Cards, UPI IDs and Wallets documentation for test payment methods.

### 2. Test Payment Flow - Hosted Checkout

**API Reference:** Hosted Checkout API - Partner Integration

**Test Steps:**

**Step 1:** Generate Access Token using OAuth

**Step 2:** Create Payment Request with mandatory parameters

**Step 3:** Generate hash using the formula:
```
hash = sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
```

**Validation Points:**
- Hash generated correctly
- All mandatory parameters included
- Payment page loads successfully
- Merchant branding displayed (if configured)

### 3. Test Payment Methods

**Credit/Debit Cards**
- Test Card: `5123456789012346` (MasterCard)
- CVV: `123`
- Expiry: Any future date
- OTP: `123456`

**Test Scenarios:**
- Successful card payment
- Insufficient funds
- Invalid CVV
- Invalid OTP
- 3D Secure authentication

**Net Banking**
- Test Banks: ICICI, HDFC, Axis (test mode)

**Test Scenarios:**
- Successful net banking payment
- Payment cancellation
- Bank timeout handling
- Redirect flow validation

**UPI**
- Test VPA: `success@payu`

**Test Scenarios:**
- UPI Collect successful
- UPI Intent successful
- Payment timeout
- User declined payment

**Wallets**
- Test Wallets: PayTM, PhonePe, Google Pay (test mode)

### 4. Test Payment Response Handling

**Test Steps:**
1. Handle success callback (SURL)
2. Handle failure callback (FURL)
3. Verify response parameters
4. Validate reverse hash

**Validation Points:**
- SURL called on success
- FURL called on failure
- Reverse hash validated
- Transaction details match request
- Payment status is accurate

### 5. Test Transaction Verification

**API Reference:** Verify Payment API

**Test Steps:**
1. Verify transaction status after payment
2. Handle cases where callback fails
3. Test with different transaction IDs
4. Validate response parameters

**Validation Points:**
- Transaction status matches actual payment
- Amount matches request
- Merchant verification successful
- Error handling for invalid txnid

### 6. Test Refund Flow

**APIs Used:**
- Refund Transaction API - Partner
- Refund Status API - Partner

**Test Scenarios:**
1. Full refund
2. Partial refund
3. Check refund status
4. Verify refund in merchant dashboard
5. Test multiple partial refunds

**Validation Points:**
- Refund initiated successfully
- Refund status updated correctly
- Refund amount within allowed limits
- Error handling for invalid requests
- Notification sent to customer (if configured)

---

## End-to-End Testing Scenarios

### Scenario 1: New Merchant Onboarding + First Payment
1. Create merchant via API
2. Upload all KYC documents
3. Complete e-sign
4. Wait for approval (or use test auto-approve)
5. Receive merchant credentials
6. Make first payment transaction
7. Verify payment success
8. Initiate test refund

### Scenario 2: Bulk Merchant Onboarding
1. Create multiple merchants (5-10)
2. Upload documents for all
3. Track status via webhooks
4. Handle any rejections
5. Test parallel processing

### Scenario 3: Error Handling
1. Test with invalid data
2. Test network timeouts
3. Test webhook delivery failures
4. Test payment failures
5. Test refund rejections

---

## Go-Live Checklist

### Partner Onboarding - Go-Live Checklist

**Legal Agreements**
- [ ] Partner Reseller Agreement signed
- [ ] Data Processing Addendum in place
- [ ] Terms of Service accepted

**Production Credentials**
- [ ] Production Client ID obtained
- [ ] Production Client Secret obtained
- [ ] Production reseller token generated
- [ ] Credentials securely stored (environment variables/secrets manager)

**Onboarding Flow Testing**
- [ ] Full onboarding flow tested end-to-end
- [ ] All KYC document types uploaded successfully
- [ ] Bank verification completed
- [ ] E-sign flow tested and verified
- [ ] Merchant status transitions validated
- [ ] Error handling implemented

**Webhook Integration**
- [ ] Production webhook endpoint configured
- [ ] Webhook signature verification implemented
- [ ] Returns 200 OK within 5 seconds
- [ ] Idempotent webhook handling verified
- [ ] Retry logic implemented
- [ ] Dead letter queue for failed webhooks
- [ ] Status polling fallback mechanism

**API Integration Best Practices**
- [ ] All API endpoints use production URLs
- [ ] OAuth token refresh implemented
- [ ] Rate limiting handled (429 responses)
- [ ] Timeout handling (30 second default)
- [ ] Retry logic with exponential backoff
- [ ] Error logging and monitoring

**Data Security & Compliance**
- [ ] PII handling compliant (minimize storage)
- [ ] Encryption at rest for sensitive data
- [ ] Encryption in transit (HTTPS only)
- [ ] No plain text storage of PAN/bank details
- [ ] GDPR/data privacy compliance
- [ ] Consent captured at CKYC/DigiLocker/VKYC steps
- [ ] Data retention policy implemented

**Monitoring & Logging**
- [ ] API request/response logging
- [ ] Error tracking system integrated
- [ ] Performance monitoring setup
- [ ] Alert notifications configured
- [ ] Dashboard for merchant status tracking

---

### Partner Payment Integration - Go-Live Checklist

**Production Setup**
- [ ] Production merchant keys obtained
- [ ] Production salt obtained
- [ ] Test environment code removed
- [ ] Production URLs configured
- [ ] Hash generation using production salt

**Payment Flow Testing**
- [ ] All payment methods tested
- [ ] Hash generation verified
- [ ] Reverse hash validation implemented
- [ ] Success/failure callbacks working
- [ ] Transaction verification integrated

**Payment Security**
- [ ] No sensitive data logged
- [ ] Hash generated server-side only
- [ ] Salt never exposed to client
- [ ] HTTPS enforced on all endpoints
- [ ] XSS and CSRF protection implemented

**Response Handling**
- [ ] Success URL (SURL) configured
- [ ] Failure URL (FURL) configured
- [ ] Response validation implemented
- [ ] Database transaction recording
- [ ] Customer notification system

**Refund Implementation**
- [ ] Refund API integrated
- [ ] Refund status tracking
- [ ] Full refund tested
- [ ] Partial refund tested
- [ ] Refund limits validated
- [ ] Customer refund notifications

**Error Handling**
- [ ] Payment timeout handling
- [ ] Network error handling
- [ ] Invalid response handling
- [ ] Duplicate transaction prevention
- [ ] User-friendly error messages

**Compliance & Reconciliation**
- [ ] Transaction reconciliation process
- [ ] Settlement tracking
- [ ] Tax compliance (GST/TDS)
- [ ] Dispute handling process
- [ ] Chargeback monitoring

**Testing Completed**
- [ ] End-to-end testing in production (small amounts)
- [ ] All payment methods verified
- [ ] All currencies tested (if multi-currency)
- [ ] Peak load testing
- [ ] Fallback mechanisms tested

---

## Reference

| Resource | Production URL |
|----------|---------------|
| OAuth/Authentication | `https://accounts.payu.in/oauth/token` |
| Partner Onboarding APIs | `https://partner.payu.in` |
| Payment (Hosted Checkout) | `https://secure.payu.in/_payment` |
| Payment Postservice | `https://info.payu.in/merchant/postservice.php` |
| Verify Payment | `https://info.payu.in/merchant/postservice?form=2` |

---


## Common Issues & Troubleshooting

**Issue 1: OAuth Token Expired**
- Solution: Implement token refresh logic using refresh_token

**Issue 2: Webhook Not Received**
- Verify endpoint is publicly accessible
- Check firewall rules
- Implement status polling as fallback

**Issue 3: Hash Mismatch**
- Verify parameter order
- Check salt is correct
- Ensure no extra spaces
- Use UTF-8 encoding

**Issue 4: Payment Callback Not Triggered**
- Verify SURL/FURL are publicly accessible
- Implement Verify Payment API as fallback
- Check server logs for errors

---

> **Important:** Always test thoroughly in the Test environment before going live. Start with small transaction amounts in production to verify the integration.

> **Best Practice:** Implement comprehensive logging and monitoring to quickly identify and resolve issues in production.

---


## Go-live checklist

- [ ] Partner Reseller Agreement signed
- [ ] Data Processing Addendum in place
- [ ] Production `resellerToken` obtained
- [ ] Full onboarding flow tested end-to-end
- [ ] Webhook endpoint deployed; **200 OK** within SLA
- [ ] Idempotent webhook handling verified
- [ ] Error handling and retry logic
- [ ] Status polling fallback
- [ ] PII handling compliant (minimize persistent PAN/bank storage)
- [ ] Consent captured at CKYC / DigiLocker / VKYC steps
- [ ] Payment hash generation tested
- [ ] Refund flow tested (full + partial)
- [ ] Production URLs and credentials

