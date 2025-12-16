---
title: SI Mandate - Cards CB Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
This integration guide walks you through implementing Standing Instruction (SI) mandate registration for recurring card payments using PayU's Server-to-Server (S2S) integration with PACB (Payment Aggregator Cross Border) flow.

## Prerequisites

Before starting the integration, ensure you have:

* Active PayU merchant account with PACB enabled
* Merchant Key and Salt from PayU dashboard
* Test environment access for development

## Step 1: Post the Request

Before implementing, familiarize yourself with the required parameters. 

### Key Parameters for Mandate Registration

* **Mandatory Parameters**: key, txnid, amount, productinfo, firstname, email, phone, surl, furl, hash, pg, bankcode, card details (ccnum, ccvv, ccname, ccexpmon, ccexpyr), si, si_details, api_version, udf1-udf5
* **S2S Flow Parameters**: txn_s2s_flow, s2s_client_ip, s2s_device_info
* **SI Details**: JSON object containing billing cycle, amounts, and dates

Construct the request payload with all required parameters. Ensure `si_details` is properly formatted as a JSON string.

### Request Payload Structure

```json
{
  "key": "JPM7Fg",
  "txnid": "payuTestMandate12345",
  "amount": "100.00",
  "productinfo": "Subscription Plan",
  "firstname": "Ashish",
  "email": "test@payu.in",
  "phone": "9988776655",
  "surl": "https://example.com/success",
  "furl": "https://example.com/failure",
  "pg": "CC",
  "bankcode": "CC",
  "ccnum": "5506900480000008",
  "ccname": "Test User",
  "ccvv": "123",
  "ccexpmon": "09",
  "ccexpyr": "2026",
  "api_version": "7",
  "si": "1",
  "si_details": "{\"billingAmount\":\"200.00\",\"billingCurrency\":\"INR\",\"billingCycle\":\"ADHOC\",\"billingInterval\":1,\"paymentStartDate\":\"2025-06-05\",\"paymentEndDate\":\"2025-12-01\",\"siTokenRequestor\":\"2\"}",
  "udf1": "AELPR****E",
  "udf2": "",
  "udf3": "02-02-1980",
  "udf4": "XYZ Pvt. Ltd.",
  "udf5": "098450845",
  "txn_s2s_flow": "4",
  "s2s_client_ip": "10.200.12.12",
  "s2s_device_info": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0",
  "hash": "generated_hash_value"

```

***

### Sample Request

Send a POST request to PayU's API endpoint with the payload.

### PHP Example

```php
<?php
$url = 'https://test.payu.in/_payment';

$data = [
    'key' => 'JPM7Fg',
    'txnid' => 'payuTestMandate12345',
    'amount' => '100.00',
    'productinfo' => 'Subscription Plan',
    'firstname' => 'Ashish',
    'email' => 'test@payu.in',
    'phone' => '9988776655',
    'surl' => 'https://example.com/success',
    'furl' => 'https://example.com/failure',
    'pg' => 'CC',
    'bankcode' => 'CC',
    'ccnum' => '5506900480000008',
    'ccname' => 'Test User',
    'ccvv' => '123',
    'ccexpmon' => '09',
    'ccexpyr' => '2026',
    'api_version' => '7',
    'si' => '1',
    'si_details' => json_encode([
        'billingAmount' => '200.00',
        'billingCurrency' => 'INR',
        'billingCycle' => 'ADHOC',
        'billingInterval' => 1,
        'paymentStartDate' => '2025-06-05',
        'paymentEndDate' => '2025-12-01',
        'siTokenRequestor' => '2'
    ]),
    'udf1' => 'AELPR****E',
    'udf2' => '',
    'udf3' => '02-02-1980',
    'udf4' => 'XYZ Pvt. Ltd.',
    'udf5' => '098450845',
    'txn_s2s_flow' => '4',
    's2s_client_ip' => $_SERVER['REMOTE_ADDR'],
    's2s_device_info' => $_SERVER['HTTP_USER_AGENT'],
    'hash' => $hash // Generated hash from Step 2
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/x-www-form-urlencoded'
]);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

// Handle response
if ($httpCode == 200) {
    $responseData = json_decode($response, true);
    // Process the response
} else {
    // Handle error
}
?>
```

### Python Example

```python
import requests
import json

url = 'https://test.payu.in/_payment'

payload = {
    'key': 'JPM7Fg',
    'txnid': 'payuTestMandate12345',
    'amount': '100.00',
    'productinfo': 'Subscription Plan',
    'firstname': 'Ashish',
    'email': 'test@payu.in',
    'phone': '9988776655',
    'surl': 'https://example.com/success',
    'furl': 'https://example.com/failure',
    'pg': 'CC',
    'bankcode': 'CC',
    'ccnum': '5506900480000008',
    'ccname': 'Test User',
    'ccvv': '123',
    'ccexpmon': '09',
    'ccexpyr': '2026',
    'api_version': '7',
    'si': '1',
    'si_details': json.dumps({
        'billingAmount': '200.00',
        'billingCurrency': 'INR',
        'billingCycle': 'ADHOC',
        'billingInterval': 1,
        'paymentStartDate': '2025-06-05',
        'paymentEndDate': '2025-12-01',
        'siTokenRequestor': '2'
    }),
    'udf1': 'AELPR****E',
    'udf2': '',
    'udf3': '02-02-1980',
    'udf4': 'XYZ Pvt. Ltd.',
    'udf5': '098450845',
    'txn_s2s_flow': '4',
    's2s_client_ip': '10.200.12.12',
    's2s_device_info': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0',
    'hash': hash_value  # Generated hash from Step 2
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.post(url, data=payload, headers=headers)

if response.status_code == 200:
    response_data = response.json()
    # Process the response
else:
    # Handle error
    print(f"Error: {response.status_code}")
```

### Node.js Example

```javascript
const axios = require('axios');
const qs = require('querystring');

const url = 'https://test.payu.in/_payment';

const payload = {
    key: 'JPM7Fg',
    txnid: 'payuTestMandate12345',
    amount: '100.00',
    productinfo: 'Subscription Plan',
    firstname: 'Ashish',
    email: 'test@payu.in',
    phone: '9988776655',
    surl: 'https://example.com/success',
    furl: 'https://example.com/failure',
    pg: 'CC',
    bankcode: 'CC',
    ccnum: '5506900480000008',
    ccname: 'Test User',
    ccvv: '123',
    ccexpmon: '09',
    ccexpyr: '2026',
    api_version: '7',
    si: '1',
    si_details: JSON.stringify({
        billingAmount: '200.00',
        billingCurrency: 'INR',
        billingCycle: 'ADHOC',
        billingInterval: 1,
        paymentStartDate: '2025-06-05',
        paymentEndDate: '2025-12-01',
        siTokenRequestor: '2'
    }),
    udf1: 'AELPR****E',
    udf2: '',
    udf3: '02-02-1980',
    udf4: 'XYZ Pvt. Ltd.',
    udf5: '098450845',
    txn_s2s_flow: '4',
    s2s_client_ip: '10.200.12.12',
    s2s_device_info: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0',
    hash: hash  // Generated hash from Step 2
};

axios.post(url, qs.stringify(payload), {
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
})
.then(response => {
    console.log('Response:', response.data);
    // Process the response
})
.catch(error => {
    console.error('Error:', error);
    // Handle error
});
```

***

## Step 2: Check the Response from PayU

The API returns a JSON response. For S2S4 flow, you'll receive an OTP enrollment response if the card requires OTP authentication.

### Successful Response Structure

```json
{
  "metaData": {
    "message": null,
    "referenceId": "5a3e7cb9884e003dce1f28f965478a9a12fb9244fc15be91b0b3de48763a12e7",
    "statusCode": null,
    "txnId": "payuTestMandate12345",
    "txnStatus": "Enrolled",
    "unmappedStatus": "pending",
    "resendOtp": {
      "isSupported": true,
      "attemptsLeft": 2
    },
    "submitOtp": {
      "attemptsLeft": 3
    }
  },
  "result": {
    "otpPostUrl": "https://test.payu.in/ResponseHandler.php",
    "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0i..."
  },
  "binData": {
    "pureS2SSupported": true,
    "issuingBank": "AXIS",
    "category": "creditcard",
    "cardType": "MAST",
    "isDomestic": true
  }
}
```

### Response Handling Logic

1. **Check Transaction Status**: Verify `metaData.txnStatus` and `metaData.unmappedStatus`
2. **OTP Handling**: If `txnStatus` is "Enrolled", handle OTP flow using `result.acsTemplate` or `result.otpPostUrl`
3. **Store Mandate Details**: On successful registration, store `mihpayid` and mandate details for future recurring payments
4. **Error Handling**: Check for error codes and handle accordingly

For detailed response handling, refer to [S2S Response Handling](doc:s2s-response-handling).

***

## Step 3: Configure Webhooks

Configure webhooks to receive real-time transaction status updates. PayU will send POST requests to your webhook URL.

### Webhook Payload Example

```text
status=success&mihpayid=403993715525316543&txnid=payuTestMandate12345&amount=100.00&productinfo=Subscription Plan&firstname=Ashish&email=test@payu.in&phone=9988776655&hash=generated_hash&payment_source=sist&cardToken=stored_token_value
```

### Webhook Validation

Always validate the webhook hash before processing:

```php
function validateWebhookHash($response, $salt) {
    $hashString = '';
    $hashSequence = "status|mihpayid|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||||||";
    $hashVarsSeq = explode('|', $hashSequence);
    
    foreach($hashVarsSeq as $hashVar) {
        $hashString .= isset($response[$hashVar]) ? $response[$hashVar] : '';
        $hashString .= '|';
    }
    $hashString .= $salt;
    
    $calculatedHash = strtolower(hash('sha512', $hashString));
    $receivedHash = strtolower($response['hash']);
    
    return $calculatedHash === $receivedHash;
}
```

For detailed webhook handling, refer to [S2S Webhook Handling](doc:s2s-webhook-handling).

***

## Step 4: Verify Mandate Registration

After successful registration, verify the mandate status:

1. **Check Response Parameters**:
   * `status` should be "success"
   * `payment_source` should be "sist"
   * `cardToken` should be present
   * `mihpayid` should be returned

2. **Store Mandate Details**:
   * Save `mihpayid` for future recurring payments
   * Store `cardToken` if tokenization is enabled
   * Save mandate expiry dates from `si_details`

3. **Test Recurring Payment**:
   * Use the stored `mihpayid` to initiate a recurring payment
   * Verify the payment processes successfully

***

## Troubleshooting

### Common Issues

1. **Hash Mismatch**: Verify hash generation formula and ensure all parameters are included
2. **Invalid si_details**: Ensure JSON is properly formatted and URL-encoded
3. **Missing Parameters**: Verify all mandatory parameters are included
4. **OTP Issues**: Check OTP handling flow and bank redirects
5. **Webhook Not Received**: Verify webhook URL is accessible and properly configured

### Debug Tips

1. **Log all requests**: Log request payloads (excluding sensitive data)
2. **Verify parameters**: Double-check all parameter values
3. **Check response**: Review complete API responses
4. **Test incrementally**: Test each step separately

<br />
