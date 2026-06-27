---
title: Test the Integration
deprecated: false
hidden: true
metadata:
  title: Test the Integration - Onboarding Chid Merchants for Split Settlements
  robots: index
---
This section describes how to test the API integration for onboarding chid merchants for Split Settlements.

<Callout icon="📘" theme="info">
  ### Note:

  Always test thoroughly in the sandbox environment before moving to production. Ensure all edge cases and error scenarios are covered for a robust integration.
</Callout>

## Prerequisites for Testing

Before testing PayU Split Settlements API integration, ensure that:

- **Hub Registration for OAuth2 Service**:
  - Register your client service on PayU's Hub with required details
  - **Scope**: Must include `refer_child_merchant`
  - **Grant Type**: `client_credentials`
  - **Client Type**: `External`
- **API Credentials Access**:
  - Obtain **Client ID** and **Client Secret** for OAuth2 authentication
  - Access **test merchant key** and **salt** from your PayU dashboard
  - For credential details, refer to [Access Test Key and Salt](https://docs.payu.in/docs/generate-test-merchant-key-and-salt)
- **Test Environment Setup**:
  - Use test endpoint: `https://uat-onepayuonboarding.payu.in/api/v3/`
  - Ensure Split Settlement feature is enabled on your parent merchant account
- **KYC Compliance**:
  - Complete KYC requirements for parent merchant account
  - Prepare test KYC documents for child merchant onboarding

## Step 1: Generate Access Token

- Use the **Get Client Token API** to obtain authentication token
- **Test Endpoint**: `https://uat-onepayuonboarding.payu.in/api/v3/get-client-token`
- **Sample Request**:

```bash
curl --location 'https://uat-onepayuonboarding.payu.in/api/v3/get-client-token' \
--header 'Content-Type: application/json' \
--data-raw '{
  "client_id": "your_test_client_id",
  "client_secret": "your_test_client_secret",
  "scope": "refer_child_merchant"
}'
```

- **Expected Response**: Should return access token for subsequent API calls

## Step 2: Create Child Merchant

- Use the **Create Child Merchant API** to onboard a test sub-merchant
- **Test Endpoint**: `https://uat-onepayuonboarding.payu.in/api/v3/product_accounts`
- **Test with Sample Data**:

```json
{
  "product_account": {
    "product": "PayUBiz",
    "name": "Test Child Merchant",
    "email": "testchild@payu.in", 
    "mobile": "9000000000",
    "aggregator_parent_mid": "your_test_parent_mid",
    "merchant_type": "aggregator",
    "pancard_number": "ABCDE1234F",
    "pancard_name": "Test Child Merchant",
    "business_entity_id": 14,
    "business_category_id": 16,
    "business_sub_category_id": 128,
    "monthly_expected_volume": "50000",
    "business_name": "Test Business Pvt Ltd"
  }
}
```

## Step 3: Update Bank Details

- Add bank account information for the created child merchant
- **Test Bank Details**:

```json
{
  "product_account": {
    "bank_detail": {
      "bank_account_number": "1234567890",
      "ifsc_code": "SBIN0010650",
      "holder_name": "Test Child Merchant"
    }
  }
}
```

## Step 4: Verify Child Merchant Creation

- Check if the child merchant is successfully created and activated
- Note the assigned **MID (Merchant ID)** for the child merchant
- Verify the status shows "Profile Completion in progress" or "Active"

## Step 5: Test Payment with Split Settlement

- Create a test transaction that includes split settlement parameters
- **Sample Split Settlement Data**:

```json
{
  "split_info": {
    "sub_merchants": [
      {
        "child_merchant_id": "created_child_mid",
        "amount_to_be_settled": "800.00",
        "commission": "50.00",
        "suborder_id": "sub_order_001"
      }
    ]
  }
}
```

## Step 6: Process Test Settlement

- Use the **Release Settlement API** to process settlements for completed transactions
- **Test Endpoint**: `POST /release_settlement`
- **Sample Request**:

```json
{
  "merchant_id": "your_parent_merchant_id",
  "transaction_id": "test_transaction_id",
  "amount": "800.00",
  "currency": "INR",
  "sub_account_id": "child_merchant_id"
}
```

## Step 7: Verify Settlement Reconciliation

- Use the **Settlement Reconciliation API** to fetch settlement details
- **Test Endpoint**: `GET /settlement_reconciliation`
- **Sample Request**:

```json
{
  "merchant_id": "your_merchant_id",
  "start_date": "2024-01-01",
  "end_date": "2024-01-31"
}
```

***

## Test Data and Credentials

### Authentication test data

- **Client ID**: Use test client ID from PayU Hub registration
- **Client Secret**: Use test client secret from PayU Hub
- **Access Token**: Generated from Step 1

### Child merchant test data:

- **Name**: "Test Child Merchant"
- **Email**: "[testchild@payu.in](mailto:testchild@payu.in)"
- **Mobile**: "9000000000"
- **PAN**: "ABCDE1234F" (Test PAN number)
- **Bank Account**: "1234567890"
- **IFSC**: "SBIN0010650"

### Transaction test data

- **Test Amount**: ₹1000.00
- **Split Amount**: ₹800.00 (to child merchant)
- **Commission**: ₹50.00 (platform fee)
- **Remaining**: ₹150.00 (taxes/other charges)

## Key Testing Scenarios

### 1. Successful Integration Flow

- Token generation successful
- Child merchant creation successful
- Bank details updated successfully
- Split payment processed correctly
- Settlement released successfully

### 2. Error Handling Scenarios

- Invalid credentials (401 Unauthorized)
- Duplicate child merchant creation
- Invalid PAN or bank details
- Insufficient funds for settlement
- Expired access token

### 3. Validation Scenarios

- Verify split amounts total correctly
- Validate child merchant receives correct settlement amount
- Check commission deduction is accurate
- Ensure settlement timing is as expected

### 4. API Response Validation

- Success responses return status 200/201
- Error responses provide meaningful error codes
- Settlement reconciliation shows correct transaction data
- All required fields are present in responses

### 5. Integration Security Testing

- Hash verification for API requests
- Token expiration handling
- API rate limiting compliance
- Secure transmission of sensitive data

## Expected Results Verification

1. **Child Merchant Status**: Should show "Active" or "Profile Completion in progress"
2. **Settlement Status**: Should show "Completed" for successful settlements
3. **Amount Reconciliation**: Split amounts should match defined rules
4. **API Responses**: All APIs should return proper JSON responses with correct status codes

## Troubleshooting Common Issues

- **Token Issues**: Regenerate access token if receiving 401 errors
- **Bank Validation**: Ensure bank holder name matches PAN card name
- **Settlement Delays**: Check if all KYC requirements are completed
- **API Limits**: Monitor API rate limits and implement proper retry logic

## Quick Start Checklist

- [ ] Register OAuth2 client with PayU Hub
- [ ] Obtain test credentials (Client ID, Secret, Merchant Key, Salt)
- [ ] Generate access token
- [ ] Create test child merchant
- [ ] Update bank details
- [ ] Process test transaction with split
- [ ] Verify settlement release
- [ ] Check reconciliation data
- [ ] Test error scenarios
- [ ] Validate security measures

<br />
