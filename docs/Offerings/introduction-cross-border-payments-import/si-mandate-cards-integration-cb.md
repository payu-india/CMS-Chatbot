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

- Active PayU merchant account with PACB enabled
- Merchant Key and Salt from PayU dashboard
- Test environment access for development

## Step 1: Understand the Request Parameters

Before implementing, familiarize yourself with the required parameters. Refer to the [API Reference](doc:s2s-mandate-registration-cards) for complete parameter details.

### Key Parameters for Mandate Registration

- **Mandatory Parameters**: key, txnid, amount, productinfo, firstname, email, phone, surl, furl, hash, pg, bankcode, card details (ccnum, ccvv, ccname, ccexpmon, ccexpyr), si, si_details, api_version, udf1-udf5
- **S2S Flow Parameters**: txn_s2s_flow, s2s_client_ip, s2s_device_info
- **SI Details**: JSON object containing billing cycle, amounts, and dates

---


## Step 3: Build the Request

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
}
```

---

## Step 4: Send the Request

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

---

## Step 5: Handle the Response

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

---

## Step 6: Process Webhooks

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

---

## Step 7: Verify Mandate Registration

After successful registration, verify the mandate status:

1. **Check Response Parameters**:
   - `status` should be "success"
   - `payment_source` should be "sist"
   - `cardToken` should be present
   - `mihpayid` should be returned

2. **Store Mandate Details**:
   - Save `mihpayid` for future recurring payments
   - Store `cardToken` if tokenization is enabled
   - Save mandate expiry dates from `si_details`

3. **Test Recurring Payment**:
   - Use the stored `mihpayid` to initiate a recurring payment
   - Verify the payment processes successfully

---

## Best Practices

### Security

1. **Never expose sensitive data**: Keep merchant key and salt secure on the server
2. **Validate all inputs**: Sanitize and validate all user inputs before processing
3. **Use HTTPS**: Always use HTTPS for all API communications
4. **Validate webhooks**: Always verify webhook hash before processing
5. **PCI Compliance**: Ensure your infrastructure meets PCI-DSS requirements

### Error Handling

1. **Handle all error codes**: Implement comprehensive error handling
2. **Log errors**: Maintain detailed logs for debugging
3. **Retry logic**: Implement retry logic for transient failures
4. **User feedback**: Provide clear error messages to users

### Performance

1. **Async processing**: Process webhooks asynchronously
2. **Cache responses**: Cache static data where appropriate
3. **Connection pooling**: Use connection pooling for API calls
4. **Timeout handling**: Set appropriate timeouts for API calls

---

## Testing

### Test Environment

Use the test environment for development and testing:

- **Test URL**: `https://test.payu.in/_payment`
- **Test Cards**: Use PayU's test card numbers
- **Test Credentials**: Use test merchant key and salt

### Test Scenarios

1. **Successful Registration**: Test with valid card details
2. **OTP Flow**: Test cards that require OTP authentication
3. **Error Cases**: Test with invalid card details, expired cards, etc.
4. **Webhook Handling**: Verify webhook processing
5. **Edge Cases**: Test with various billing cycles and amounts

### Test Cards

Refer to PayU's test card documentation for available test cards.

---

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

---

## Next Steps

After successful mandate registration:

1. **Process Recurring Payments**: Use the stored mandate to process recurring payments
2. **Monitor Mandates**: Track mandate status and expiry dates
3. **Handle Modifications**: Implement mandate modification and cancellation flows
4. **Update Network Tokens**: Use Update SI API to add network token details if needed

For processing recurring payments, refer to [Cross-Border Recurring Payments](doc:s2s-cross-border-recurring).

---

## Additional Resources

- [API Reference](doc:s2s-mandate-registration-cards)
- [Response Handling](doc:s2s-response-handling)
- [Webhook Handling](doc:s2s-webhook-handling)
- [SI Parameter JSON Details](ref:si-parameter-json-details)
- [Update SI API](ref:update-si-api)

---

## Support

For integration support:

- **Documentation**: [PayU Developer Portal](https://docs.payu.in)
- **Support**: Contact your PayU account manager
- **Status**: Check [PayU Status Page](https://status.payu.in)