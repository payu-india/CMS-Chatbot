---
title: Testing and Go Live - Partner Integration
deprecated: false
hidden: false
metadata:
  robots: index
---
This section includes the Testing and Go Live checklist for Partner Integration onboarding and collect payment after onboarding.

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

Follow these steps to test the complete merchant onboarding flow:

### 1. Setup Test Credentials

**Prerequisites:**
- Partner Client ID and Client Secret (test environment)
- Access to partner dashboard (test mode)
- Postman or API testing tool

> Contact PayU Partner Support to obtain your test environment client credentials.

### 2. Test OAuth Authentication

**API:** [Get Token API](ref:get_token_partner_integration)

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

**API:** [Create Merchant API](ref:createmerchant)

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

**Common Test Scenarios:**
- Valid merchant creation
- Duplicate PAN validation
- Invalid business entity handling
- Missing required fields

---

### 4. Test KYC Document Upload Flow

**APIs:**
- [Fetch Required Documents API](ref:fetchrequireddocs)
- [Upload KYC Document API](ref:uploadkycdocument)
- [Show KYC Document API](ref:showkycdocument)
- [Delete KYC Document API](ref:deletekycdocument)

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

> 📘 Reference
>
> For document categories and types, refer to [Document Categories and Types](ref:document-categories-and-types)

---

### 5. Test Bank Details Addition

**API:** [Update Merchant - Bank Details](ref:updatemerchant_bankdetails)

**Test Steps:**
1. Add bank account details
2. Verify penny drop validation (if enabled)
3. Update existing bank details
4. Test IFSC code validation

**Test Bank Details:**
```json
{
  "account_number": "1234567890123456",
  "ifsc_code": "SBIN0001234",
  "account_holder_name": "Test Merchant Name",
  "account_type": "current"
}
```

**Validation Points:**
- Bank details saved successfully
- IFSC code validated
- Account holder name matches merchant name
- Penny drop verification completed (if applicable)

---

### 6. Test E-Sign/Agreement Flow

**API:** [Generate Agreement for E-Sign](ref:generateagreementforesign)

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

---

### 7. Test Merchant Status Tracking

**API:** [Get Merchant Details](ref:getmerchant)

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

---

### 8. Test Webhook Integration

**API:** [Partner Webhook](ref:partner-webhook)

**Test Steps:**
1. Configure webhook endpoint in partner dashboard
2. Implement webhook receiver endpoint
3. Test webhook signature verification
4. Test idempotency handling
5. Test retry mechanism

**Webhook Events to Test:**
- `merchant.created`
- `merchant.kyc_submitted`
- `merchant.approved`
- `merchant.rejected`
- `merchant.live`

**Validation Points:**
- Webhook received within SLA
- Signature verified successfully
- Duplicate webhooks handled (idempotency)
- Retry logic working for failures
- Status polling as fallback

**Sample Webhook Handler:**
```javascript
app.post('/webhooks/payu-partner', (req, res) => {
  // Verify signature
  const signature = req.headers['x-payu-signature'];
  const isValid = verifyWebhookSignature(req.body, signature, WEBHOOK_SECRET);
  
  if (!isValid) {
    return res.status(401).send('Invalid signature');
  }
  
  // Process webhook (idempotent handling)
  const eventId = req.body.event_id;
  if (!isEventProcessed(eventId)) {
    processWebhookEvent(req.body);
    markEventAsProcessed(eventId);
  }
  
  // Always return 200 OK quickly
  res.status(200).send('OK');
});
```

> 📘 Reference
>
> For webhook implementation details and troubleshooting, refer to [Get Real-time Merchant Status using Webhooks](ref:get-real-time-merchant-status-using-webhooks)

---

## Testing Partner Payment Integration

Follow these steps to test payment collection through Partner APIs:

### 1. Setup Payment Test Credentials

**Prerequisites:**
- Test Merchant Key and Salt (from onboarded merchant)
- Partner access token (OAuth)
- Test payment cards/methods

> 📘 Test Payment Credentials
>
> Refer to Test Cards, UPI IDs and Wallets documentation for test payment methods.

---

### 2. Test Payment Flow - Hosted Checkout

**API:** [Hosted Checkout API - Partner Integration](ref:hosted-checkout-api-partner-integration)

**Test Steps:**

#### Step 1: Generate Access Token
Use [Validate Auth Code and Client API](ref:validate-auth-code-and-client) to get partner access token

#### Step 2: Create Payment Request
Send payment request with mandatory parameters

#### Step 3: Hash Generation
Test hash generation using the formula:
```
hash = sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
```

**Validation Points:**
- Hash generated correctly
- All mandatory parameters included
- Payment page loads successfully
- Merchant branding displayed (if configured)

---

### 3. Test Payment Methods

Test transactions with each payment method:

#### Credit/Debit Cards
**Test Card:** `5123456789012346` (MasterCard)
- CVV: `123`
- Expiry: Any future date
- OTP: `123456`

**Test Scenarios:**
- Successful card payment
- Insufficient funds
- Invalid CVV
- Invalid OTP
- 3D Secure authentication

#### Net Banking
**Test Banks:**
- ICICI Bank (Test Mode)
- HDFC Bank (Test Mode)
- Axis Bank (Test Mode)

**Test Scenarios:**
- Successful net banking payment
- Payment cancellation
- Bank timeout handling
- Redirect flow validation

#### UPI
**Test VPA:** `success@payu`

**Test Scenarios:**
- UPI Collect successful
- UPI Intent successful
- Payment timeout
- User declined payment

**API:** [UPI S2S Integration for Partners](ref:upi-s2s-partner-integration-api)

#### Wallets
**Test Wallets:**
- PayTM (test mode)
- PhonePe (test mode)
- Google Pay (test mode)

---

### 4. Test Payment Response Handling

**Test Steps:**
1. Handle success callback (SURL)
2. Handle failure callback (FURL)
3. Verify response parameters
4. Validate reverse hash

**Success Response Validation:**
```php
// Reverse hash verification
$reverseHash = hash('sha512', 
  $SALT.'|'.$status.'|||||||||||'.$email.'|'.$firstname.'|'
  .$productinfo.'|'.$amount.'|'.$txnid.'|'.$key
);

if ($reverseHash == $receivedHash) {
  // Response is valid
}
```

**Validation Points:**
- SURL called on success
- FURL called on failure
- Reverse hash validated
- Transaction details match request
- Payment status is accurate

---

### 5. Test Transaction Verification

**API:** Verify Payment API

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

---

### 6. Test Refund Flow

**APIs:**
- [Refund Transaction API - Partner](ref:refund-transaction-api-partner-integration)
- [Refund Status API - Partner](ref:refund-status-api-partner-integration)

**Test Scenarios:**

#### Full Refund
```json
{
  "merchantKey": "MERCHANT_KEY",
  "paymentId": "PAYU_PAYMENT_ID",
  "refundAmount": "100.00",
  "token": "PARTNER_TOKEN"
}
```

#### Partial Refund
```json
{
  "merchantKey": "MERCHANT_KEY",
  "paymentId": "PAYU_PAYMENT_ID",
  "refundAmount": "50.00",
  "token": "PARTNER_TOKEN"
}
```

**Test Steps:**
1. Initiate full refund
2. Initiate partial refund
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

## Additional API Testing

### CKYC Verification Flow

**APIs:**
- [Send CKYC OTP](ref:sendckycotp)
- [Verify CKYC OTP](ref:verifyckycotp)
- [Fetch CKYC Data](ref:fetchckycdata)

**Test Steps:**
1. Send OTP to mobile number
2. Verify OTP
3. Fetch CKYC data
4. Validate fetched information

### DigiLocker Integration

**API:** [Generate DigiLocker Link](ref:generatedigilockerlink)

**Test Steps:**
1. Generate DigiLocker authorization link
2. Complete DigiLocker authentication
3. Verify document fetch
4. Validate document details

### Business Members & Signatory

**APIs:**
- [Add Signatory Details](ref:addsignatorydetails)
- [Submit Business Members](ref:submitbusinessmembers)
- [List Business Members](ref:list_business_members_api)

**Test Steps:**
1. Add signatory details
2. Add business members/KMP
3. List all business members
4. Verify details are correct

---

## End-to-End Testing Scenarios

Test the complete integration flow from merchant onboarding to payment collection:

### Scenario 1: New Merchant Onboarding + First Payment
1. Create merchant via [Create Merchant API](ref:createmerchant)
2. Upload all KYC documents via [Upload KYC Document API](ref:uploadkycdocument)
3. Complete e-sign via [Generate Agreement for E-Sign](ref:generateagreementforesign)
4. Wait for approval (or use test auto-approve)
5. Receive merchant credentials via [Get Merchant Details](ref:getmerchant)
6. Make first payment transaction via [Hosted Checkout API](ref:hosted-checkout-api-partner-integration)
7. Verify payment success
8. Initiate test refund via [Refund Transaction API](ref:refund-transaction-api-partner-integration)

### Scenario 2: Bulk Merchant Onboarding
1. Create multiple merchants (5-10)
2. Upload documents for all
3. Track status via [Partner Webhook](ref:partner-webhook)
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

Use this checklist before moving to production:

### Partner Onboarding - Go-Live Checklist

- [ ] **Legal Agreements**
  - [ ] Partner Reseller Agreement signed
  - [ ] Data Processing Addendum in place
  - [ ] Terms of Service accepted

- [ ] **Production Credentials**
  - [ ] Production Client ID obtained
  - [ ] Production Client Secret obtained
  - [ ] Production reseller token generated
  - [ ] Credentials securely stored (environment variables/secrets manager)

- [ ] **Onboarding Flow Testing**
  - [ ] Full onboarding flow tested end-to-end
  - [ ] All KYC document types uploaded successfully
  - [ ] Bank verification completed
  - [ ] E-sign flow tested and verified
  - [ ] Merchant status transitions validated
  - [ ] Error handling implemented

- [ ] **Webhook Integration**
  - [ ] Production webhook endpoint configured
  - [ ] Webhook signature verification implemented
  - [ ] Returns **200 OK** within 5 seconds
  - [ ] Idempotent webhook handling verified
  - [ ] Retry logic implemented
  - [ ] Dead letter queue for failed webhooks
  - [ ] Status polling fallback mechanism

- [ ] **API Integration Best Practices**
  - [ ] All API endpoints use production URLs
  - [ ] OAuth token refresh implemented via [Refresh Token API](ref:refresh-token-partner-integration)
  - [ ] Rate limiting handled (429 responses)
  - [ ] Timeout handling (30 second default)
  - [ ] Retry logic with exponential backoff
  - [ ] Error logging and monitoring

- [ ] **Data Security & Compliance**
  - [ ] PII handling compliant (minimize storage)
  - [ ] Encryption at rest for sensitive data
  - [ ] Encryption in transit (HTTPS only)
  - [ ] No plain text storage of PAN/bank details
  - [ ] GDPR/data privacy compliance
  - [ ] Consent captured at CKYC/DigiLocker/VKYC steps
  - [ ] Data retention policy implemented

- [ ] **Monitoring & Logging**
  - [ ] API request/response logging
  - [ ] Error tracking system integrated
  - [ ] Performance monitoring setup
  - [ ] Alert notifications configured
  - [ ] Dashboard for merchant status tracking

---

### Partner Payment Integration - Go-Live Checklist

- [ ] **Production Setup**
  - [ ] Production merchant keys obtained
  - [ ] Production salt obtained
  - [ ] Test environment code removed
  - [ ] Production URLs configured
  - [ ] Hash generation using production salt

- [ ] **Payment Flow Testing**
  - [ ] All payment methods tested
  - [ ] Hash generation verified
  - [ ] Reverse hash validation implemented
  - [ ] Success/failure callbacks working
  - [ ] Transaction verification integrated

- [ ] **Payment Security**
  - [ ] No sensitive data logged
  - [ ] Hash generated server-side only
  - [ ] Salt never exposed to client
  - [ ] HTTPS enforced on all endpoints
  - [ ] XSS and CSRF protection implemented

- [ ] **Response Handling**
  - [ ] Success URL (SURL) configured
  - [ ] Failure URL (FURL) configured
  - [ ] Response validation implemented
  - [ ] Database transaction recording
  - [ ] Customer notification system

- [ ] **Refund Implementation**
  - [ ] Refund API integrated
  - [ ] Refund status tracking
  - [ ] Full refund tested
  - [ ] Partial refund tested
  - [ ] Refund limits validated
  - [ ] Customer refund notifications

- [ ] **Error Handling**
  - [ ] Payment timeout handling
  - [ ] Network error handling
  - [ ] Invalid response handling
  - [ ] Duplicate transaction prevention
  - [ ] User-friendly error messages

- [ ] **Compliance & Reconciliation**
  - [ ] Transaction reconciliation process
  - [ ] Settlement tracking
  - [ ] Tax compliance (GST/TDS)
  - [ ] Dispute handling process
  - [ ] Chargeback monitoring

- [ ] **Testing Completed**
  - [ ] End-to-end testing in production (small amounts)
  - [ ] All payment methods verified
  - [ ] All currencies tested (if multi-currency)
  - [ ] Peak load testing
  - [ ] Fallback mechanisms tested

---

## Production URLs Reference

Once all testing is complete and checklist items are verified, update all endpoints to production:

| Resource | Production URL |
|----------|---------------|
| OAuth/Authentication | `https://accounts.payu.in/oauth/token` |
| Partner Onboarding APIs | `https://partner.payu.in` |
| Payment (Hosted Checkout) | `https://secure.payu.in/_payment` |
| Payment Postservice | `https://info.payu.in/merchant/postservice.php` |
| Verify Payment | `https://info.payu.in/merchant/postservice?form=2` |

---

## Support & Resources

### Documentation
- [Partner Integration API Introduction](ref:partner-integration-api-introduction)
- Partner API Reference
- Payment API Reference
- Test Cards and Payment Methods

### Tools
- **Postman Collection:** Import from PayU Postman workspace
- **Hash Generation Tool:** Available in PayU Dashboard
- **Webhook Testing:** Use tools like ngrok for local testing

### Support Channels
- Partner Support Email: partner-support@payu.in
- Technical Support: tech-support@payu.in
- Dashboard: Partner Dashboard

---

## Common Issues & Troubleshooting

### Issue 1: OAuth Token Expired
**Solution:** Implement token refresh logic using [Refresh Token API](ref:refresh-token-partner-integration)

### Issue 2: Webhook Not Received
**Solution:** 
- Verify endpoint is publicly accessible
- Check firewall rules
- Implement status polling as fallback
- Refer to [KYC Errors and Solutions](ref:kyc-errors-and-solutions) for common issues

### Issue 3: Hash Mismatch
**Solution:**
- Verify parameter order
- Check salt is correct
- Ensure no extra spaces
- Use UTF-8 encoding

### Issue 4: Payment Callback Not Triggered
**Solution:**
- Verify SURL/FURL are publicly accessible
- Implement Verify Payment API as fallback
- Check server logs for errors

### Issue 5: KYC Document Upload Failures
**Solution:**
- Verify document format (PDF, JPG, PNG)
- Check file size (max 5MB)
- Ensure correct document category and type from [Document Categories and Types](ref:document-categories-and-types)
- Review error messages from [Upload KYC Document API](ref:uploadkycdocument)

---

> 🚧 Important
>
> Always test thoroughly in the test environment before going live. Start with small transaction amounts in production to verify the integration.

> 📘 Best Practice
>
> Implement comprehensive logging and monitoring to quickly identify and resolve issues in production.

---

**Last Updated:** August 27, 2026
```

**✅ Copy the entire code snippet above!**

This updated version includes proper cross-references to all relevant Partner Integration API reference pages using the `ref:` syntax. Save it as `testing_go_live_partner.md`! 🎯