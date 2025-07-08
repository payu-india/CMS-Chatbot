---
title: 1. API Integration to Onboard Merchants
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU Split Settlements allows marketplace platforms to split payment transactions among multiple child merchants (sub-sellers) involved in an order. This integration guide walks you through the complete process of onboarding child merchants and implementing split settlements.

## Prerequisites

Before integrating Split Settlements, ensure you have:

1. **Parent Merchant Account**: A verified PayU merchant account that will act as the platform/aggregator
2. **API Credentials**: Your `key` and `salt` from the PayU dashboard
3. **Marketplace Setup**: Business model allowing multiple sellers on your platform
4. **KYC Documentation**: Required documents for child merchant verification

### Getting Your API Credentials

1. Log into your [PayU Dashboard](https://test.payu.in/merchant/dashboard)
2. Navigate to **Account & Settings** → **API Configuration**
3. Copy your `Key` and `Salt` values
4. Note your Merchant ID for reference

## Step 1: Onboard Child Merchants

Child merchant onboarding is a multi-step process that ensures compliance and security.

### Register Child Merchant

Use the Child Merchant Registration API to create new sub-merchant accounts:

**Endpoint**: `POST /api/v1/createChildMerchant`

**Request Parameters**:

| Parameter      | Type   | Required | Description                                           |
| -------------- | ------ | -------- | ----------------------------------------------------- |
| `merchantName` | String | Yes      | Legal name of the child merchant                      |
| `email`        | String | Yes      | Valid email address for login                         |
| `mobile`       | String | Yes      | 10-digit mobile number                                |
| `businessType` | String | Yes      | Type of business (Individual/Partnership/LLP/Pvt Ltd) |
| `tradeName`    | String | Yes      | Business trade name (must match bank account)         |
| `category`     | String | Yes      | Business category code                                |
| `subcategory`  | String | Yes      | Business subcategory code                             |

**Sample Request (cURL)**:

```bash
curl -X POST "https://test.payu.in/api/v1/createChildMerchant" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_CLIENT_TOKEN" \
-d '{
  "merchantName": "ABC Electronics Store",
  "email": "merchant@abcelectronics.com",
  "mobile": "9876543210",
  "businessType": "Pvt Ltd",
  "tradeName": "ABC Electronics",
  "category": "1001",
  "subcategory": "1001001"
}'
```

**Sample Response**:

```json
{
  "status": "success",
  "message": "Child merchant created successfully",
  "data": {
    "childMerchantId": "CM_ABC_123456",
    "merchantName": "ABC Electronics Store",
    "email": "merchant@abcelectronics.com",
    "status": "pending_activation",
    "createdAt": "2024-01-15T10:30:00Z"
  }
}
```

### Activate Child Merchant Account

After registration, the child merchant must activate their account:

1. **Email Notification**: Child merchant receives activation email
2. **Dashboard Login**: Visit `https://onboarding.payu.in/app/account/signin`
3. **Account Activation**: Click "Activate Account" in the dashboard
4. **Password Setup**: Create a secure password for the account

#### 1.3 Complete KYC Verification

Child merchants must complete Know Your Customer (KYC) verification:

**Required Documents**:

* Business registration certificate
* PAN card of business/individual
* Bank account verification (cancelled cheque/bank statement)
* Address proof
* ID proof of authorized signatory

**KYC Process**:

1. Login to PayU dashboard
2. Navigate to **Account Settings** → **KYC Documents**
3. Upload required documents
4. Submit for verification
5. Wait for PayU approval (typically 1-3 business days)

**Important**: Trade name must exactly match the bank account holder name.

## Step 2: Implement Split Settlements

Once child merchants are onboarded and verified, implement split settlements in your payment flow.

### Add Payment Splits

Use the Payment Splits API to define how transaction amounts should be distributed:

**Endpoint**: `POST /api/v1/addPaymentSplits`

**Request Parameters**:

| Parameter                     | Type    | Required | Description                    |
| ----------------------------- | ------- | -------- | ------------------------------ |
| `txnid`                       | String  | Yes      | Unique transaction ID          |
| `amount`                      | Decimal | Yes      | Total transaction amount       |
| `splits`                      | Array   | Yes      | Array of split details         |
| `splits.childMerchantId`      | String  | Yes      | Child merchant identifier      |
| `splits.amountToBeSettled`    | Decimal | Yes      | Amount for this child merchant |
| `splits.aggregatorCommission` | Decimal | No       | Platform commission amount     |
| `splits.suborderId`           | String  | Yes      | Unique sub-order identifier    |

**Sample Request (Python)**:

```python
import requests
import hashlib
import json

def add_payment_splits(txnid, total_amount, splits_data):
    url = "https://test.payu.in/api/v1/addPaymentSplits"
    
    payload = {
        "txnid": txnid,
        "amount": total_amount,
        "splits": splits_data
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_auth_token()}"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Example usage
splits = [
    {
        "childMerchantId": "CM_ABC_123456",
        "amountToBeSettled": 800.00,
        "aggregatorCommission": 50.00,
        "suborderId": "SUB_001"
    },
    {
        "childMerchantId": "CM_XYZ_789012",
        "amountToBeSettled": 1200.00,
        "aggregatorCommission": 75.00,
        "suborderId": "SUB_002"
    }
]

result = add_payment_splits("TXN_20240115_001", 2000.00, splits)
print(json.dumps(result, indent=2))
```

**Sample Response**:

```json
{
  "status": "success",
  "message": "Payment splits added successfully",
  "data": {
    "txnid": "TXN_20240115_001",
    "totalAmount": 2000.00,
    "splitsCount": 2,
    "splits": [
      {
        "childMerchantId": "CM_ABC_123456",
        "amountToBeSettled": 800.00,
        "aggregatorCommission": 50.00,
        "suborderId": "SUB_001",
        "status": "pending_settlement"
      },
      {
        "childMerchantId": "CM_XYZ_789012",
        "amountToBeSettled": 1200.00,
        "aggregatorCommission": 75.00,
        "suborderId": "SUB_002",
        "status": "pending_settlement"
      }
    ]
  }
}
```

### Integration with Payment Flow

Integrate split settlements with your existing payment process:

**HTML Form Example**:

```html
<form action="https://test.payu.in/_payment" method="post" name="payuForm">
    <input type="hidden" name="key" value="YOUR_MERCHANT_KEY" />
    <input type="hidden" name="txnid" value="TXN_20240115_001" />
    <input type="hidden" name="amount" value="2000.00" />
    <input type="hidden" name="productinfo" value="Multi-seller Order" />
    <input type="hidden" name="firstname" value="John" />
    <input type="hidden" name="email" value="john@example.com" />
    <input type="hidden" name="phone" value="9876543210" />
    <input type="hidden" name="surl" value="https://yoursite.com/payment/success" />
    <input type="hidden" name="furl" value="https://yoursite.com/payment/failure" />
    <input type="hidden" name="hash" value="CALCULATED_HASH" />
    
    <!-- Split Settlement specific parameters -->
    <input type="hidden" name="split_payments" value="1" />
    <input type="hidden" name="sub_merchant_id" value="CM_ABC_123456,CM_XYZ_789012" />
    
    <input type="submit" value="Pay Now" />
</form>
```

### Handle Settlement and Reconciliation

### Settlement Reconciliation API

Use the Settlement Reconciliation API to track and verify settlements:

**Endpoint**: `GET /api/v1/getSettlementDetails`

**Request Parameters**:

| Parameter         | Type   | Required | Description              |
| ----------------- | ------ | -------- | ------------------------ |
| `txnid`           | String | Yes      | Transaction ID to query  |
| `settlementDate`  | Date   | No       | Specific settlement date |
| `childMerchantId` | String | No       | Filter by child merchant |

**Sample Request (Java)**:

```java
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URI;

public class SettlementReconciliation {
    
    public String getSettlementDetails(String txnid) {
        try {
            HttpClient client = HttpClient.newHttpClient();
            
            String url = "https://test.payu.in/api/v1/getSettlementDetails?txnid=" + txnid;
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("Authorization", "Bearer " + getAuthToken())
                .GET()
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            return response.body();
            
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
```

### Webhook Notifications

Set up webhooks to receive real-time settlement notifications:

**Webhook Endpoint Configuration**:

1. Navigate to **Dashboard** → **Settings** → **Webhooks**
2. Add your webhook URL: `https://yoursite.com/webhooks/settlement`
3. Select events: `settlement.completed`, `settlement.failed`

**Sample Webhook Handler (PHP)**:

```php
<?php
function handleSettlementWebhook() {
    $payload = file_get_contents('php://input');
    $data = json_decode($payload, true);
    
    // Verify webhook signature
    $signature = $_SERVER['HTTP_X_PAYU_SIGNATURE'];
    if (!verifyWebhookSignature($payload, $signature)) {
        http_response_code(401);
        exit('Unauthorized');
    }
    
    switch ($data['event']) {
        case 'settlement.completed':
            handleSettlementCompleted($data);
            break;
        case 'settlement.failed':
            handleSettlementFailed($data);
            break;
    }
    
    http_response_code(200);
    echo 'OK';
}

function handleSettlementCompleted($data) {
    $txnid = $data['txnid'];
    $childMerchantId = $data['childMerchantId'];
    $settledAmount = $data['settledAmount'];
    
    // Update your database
    updateSettlementStatus($txnid, $childMerchantId, 'completed', $settledAmount);
    
    // Notify child merchant
    notifyChildMerchant($childMerchantId, $settledAmount);
}
?>
```

## Additional Resources

* [Split Settlements API Reference](https://docs.payu.in/docs/split-settlments)
* [Settlement Reconciliation Guide](https://docs.payu.in/reference/settlement-reconciliation-api)
* [KYC Requirements](https://docs.payu.in/docs/kyc-requirements)
* [Error Codes Reference](https://docs.payu.in/docs/error-codes)