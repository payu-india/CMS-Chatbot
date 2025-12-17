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

```curl
curl --location --request POST 'https://test.payu.in/_payment' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=JPM7Fg' \
--data-urlencode 'txnid=payuTestMandate12345' \
--data-urlencode 'amount=100.00' \
--data-urlencode 'firstname=Ashish' \
--data-urlencode 'email=test@payu.in' \
--data-urlencode 'phone=9988776655' \
--data-urlencode 'productinfo=Subscription Plan' \
--data-urlencode 'surl=https://test.payu.in/admin/test_response' \
--data-urlencode 'furl=https://test.payu.in/admin/test_response' \
--data-urlencode 'pg=CC' \
--data-urlencode 'bankcode=CC' \
--data-urlencode 'ccnum=5506900480000008' \
--data-urlencode 'ccname=Test User' \
--data-urlencode 'ccvv=123' \
--data-urlencode 'ccexpmon=09' \
--data-urlencode 'ccexpyr=2026' \
--data-urlencode 'api_version=7' \
--data-urlencode 'si=1' \
--data-urlencode 'si_details={"billingAmount":"200.00","billingCurrency":"INR","billingCycle":"ADHOC","billingInterval":1,"paymentStartDate":"2025-06-05","paymentEndDate":"2025-12-01","siTokenRequestor":"2"}' \
--data-urlencode 'udf1=AELPR****E' \
--data-urlencode 'udf2=' \
--data-urlencode 'udf3=02-02-1980' \
--data-urlencode 'udf4=XYZ Pvt. Ltd.' \
--data-urlencode 'udf5=098450845' \
--data-urlencode 'txn_s2s_flow=4' \
--data-urlencode 's2s_client_ip=10.200.12.12' \
--data-urlencode 's2s_device_info=Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0' \
--data-urlencode 'hash=YOUR_CALCULATED_HASH'
```
```python
import requests

url = "https://test.payu.in/_payment"

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'key': 'JPM7Fg',
    'txnid': 'payuTestMandate12345',
    'amount': '100.00',
    'firstname': 'Ashish',
    'email': 'test@payu.in',
    'phone': '9988776655',
    'productinfo': 'Subscription Plan',
    'surl': 'https://test.payu.in/admin/test_response',
    'furl': 'https://test.payu.in/admin/test_response',
    'pg': 'CC',
    'bankcode': 'CC',
    'ccnum': '5506900480000008',
    'ccname': 'Test User',
    'ccvv': '123',
    'ccexpmon': '09',
    'ccexpyr': '2026',
    'api_version': '7',
    'si': '1',
    'si_details': '{"billingAmount":"200.00","billingCurrency":"INR","billingCycle":"ADHOC","billingInterval":1,"paymentStartDate":"2025-06-05","paymentEndDate":"2025-12-01","siTokenRequestor":"2"}',
    'udf1': 'AELPR****E',
    'udf2': '',
    'udf3': '02-02-1980',
    'udf4': 'XYZ Pvt. Ltd.',
    'udf5': '098450845',
    'txn_s2s_flow': '4',
    's2s_client_ip': '10.200.12.12',
    's2s_device_info': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0',
    'hash': 'YOUR_CALCULATED_HASH'
}

try:
    response = requests.post(url, headers=headers, data=data)
    print("Status Code:", response.status_code)
    print("Response:", response.text)
except requests.exceptions.RequestException as e:
    print("Error:", e)
```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        string url = "https://test.payu.in/_payment";
        
        using HttpClient client = new HttpClient();
        
        List<KeyValuePair<string, string>> postData = new List<KeyValuePair<string, string>>()
        {
            new KeyValuePair<string, string>("key", "JPM7Fg"),
            new KeyValuePair<string, string>("txnid", "payuTestMandate12345"),
            new KeyValuePair<string, string>("amount", "100.00"),
            new KeyValuePair<string, string>("firstname", "Ashish"),
            new KeyValuePair<string, string>("email", "test@payu.in"),
            new KeyValuePair<string, string>("phone", "9988776655"),
            new KeyValuePair<string, string>("productinfo", "Subscription Plan"),
            new KeyValuePair<string, string>("surl", "https://test.payu.in/admin/test_response"),
            new KeyValuePair<string, string>("furl", "https://test.payu.in/admin/test_response"),
            new KeyValuePair<string, string>("pg", "CC"),
            new KeyValuePair<string, string>("bankcode", "CC"),
            new KeyValuePair<string, string>("ccnum", "5506900480000008"),
            new KeyValuePair<string, string>("ccname", "Test User"),
            new KeyValuePair<string, string>("ccvv", "123"),
            new KeyValuePair<string, string>("ccexpmon", "09"),
            new KeyValuePair<string, string>("ccexpyr", "2026"),
            new KeyValuePair<string, string>("api_version", "7"),
            new KeyValuePair<string, string>("si", "1"),
            new KeyValuePair<string, string>("si_details", "{\"billingAmount\":\"200.00\",\"billingCurrency\":\"INR\",\"billingCycle\":\"ADHOC\",\"billingInterval\":1,\"paymentStartDate\":\"2025-06-05\",\"paymentEndDate\":\"2025-12-01\",\"siTokenRequestor\":\"2\"}"),
            new KeyValuePair<string, string>("udf1", "AELPR****E"),
            new KeyValuePair<string, string>("udf2", ""),
            new KeyValuePair<string, string>("udf3", "02-02-1980"),
            new KeyValuePair<string, string>("udf4", "XYZ Pvt. Ltd."),
            new KeyValuePair<string, string>("udf5", "098450845"),
            new KeyValuePair<string, string>("txn_s2s_flow", "4"),
            new KeyValuePair<string, string>("s2s_client_ip", "10.200.12.12"),
            new KeyValuePair<string, string>("s2s_device_info", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0"),
            new KeyValuePair<string, string>("hash", "YOUR_CALCULATED_HASH")
        };
        
        FormUrlEncodedContent content = new FormUrlEncodedContent(postData);
        
        try
        {
            HttpResponseMessage response = await client.PostAsync(url, content);
            string responseBody = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine($"Status Code: {(int)response.StatusCode}");
            Console.WriteLine($"Response: {responseBody}");
        }
        catch (HttpRequestException e)
        {
            Console.WriteLine($"Error: {e.Message}");
        }
    }
}
```
```javascript
async function makePayment() {
    const url = "https://test.payu.in/_payment";
    
    const formData = new URLSearchParams();
    formData.append('key', 'JPM7Fg');
    formData.append('txnid', 'payuTestMandate12345');
    formData.append('amount', '100.00');
    formData.append('firstname', 'Ashish');
    formData.append('email', 'test@payu.in');
    formData.append('phone', '9988776655');
    formData.append('productinfo', 'Subscription Plan');
    formData.append('surl', 'https://test.payu.in/admin/test_response');
    formData.append('furl', 'https://test.payu.in/admin/test_response');
    formData.append('pg', 'CC');
    formData.append('bankcode', 'CC');
    formData.append('ccnum', '5506900480000008');
    formData.append('ccname', 'Test User');
    formData.append('ccvv', '123');
    formData.append('ccexpmon', '09');
    formData.append('ccexpyr', '2026');
    formData.append('api_version', '7');
    formData.append('si', '1');
    formData.append('si_details', '{"billingAmount":"200.00","billingCurrency":"INR","billingCycle":"ADHOC","billingInterval":1,"paymentStartDate":"2025-06-05","paymentEndDate":"2025-12-01","siTokenRequestor":"2"}');
    formData.append('udf1', 'AELPR****E');
    formData.append('udf2', '');
    formData.append('udf3', '02-02-1980');
    formData.append('udf4', 'XYZ Pvt. Ltd.');
    formData.append('udf5', '098450845');
    formData.append('txn_s2s_flow', '4');
    formData.append('s2s_client_ip', '10.200.12.12');
    formData.append('s2s_device_info', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0');
    formData.append('hash', 'YOUR_CALCULATED_HASH');
    
    const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: formData
    };
    
    try {
        const response = await fetch(url, requestOptions);
        const responseText = await response.text();
        
        console.log('Status Code:', response.status);
        console.log('Response:', responseText);
    } catch (error) {
        console.error('Error:', error);
    }
}

makePayment();
```
```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class PayUPayment {
    public static void main(String[] args) {
        try {
            String url = "https://test.payu.in/_payment";
            URL obj = new URL(url);
            HttpURLConnection connection = (HttpURLConnection) obj.openConnection();
            
            connection.setRequestMethod("POST");
            connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
            connection.setDoOutput(true);
            
            StringBuilder postData = new StringBuilder();
            postData.append("key=").append(URLEncoder.encode("JPM7Fg", StandardCharsets.UTF_8));
            postData.append("&txnid=").append(URLEncoder.encode("payuTestMandate12345", StandardCharsets.UTF_8));
            postData.append("&amount=").append(URLEncoder.encode("100.00", StandardCharsets.UTF_8));
            postData.append("&firstname=").append(URLEncoder.encode("Ashish", StandardCharsets.UTF_8));
            postData.append("&email=").append(URLEncoder.encode("test@payu.in", StandardCharsets.UTF_8));
            postData.append("&phone=").append(URLEncoder.encode("9988776655", StandardCharsets.UTF_8));
            postData.append("&productinfo=").append(URLEncoder.encode("Subscription Plan", StandardCharsets.UTF_8));
            postData.append("&surl=").append(URLEncoder.encode("https://test.payu.in/admin/test_response", StandardCharsets.UTF_8));
            postData.append("&furl=").append(URLEncoder.encode("https://test.payu.in/admin/test_response", StandardCharsets.UTF_8));
            postData.append("&pg=").append(URLEncoder.encode("CC", StandardCharsets.UTF_8));
            postData.append("&bankcode=").append(URLEncoder.encode("CC", StandardCharsets.UTF_8));
            postData.append("&ccnum=").append(URLEncoder.encode("5506900480000008", StandardCharsets.UTF_8));
            postData.append("&ccname=").append(URLEncoder.encode("Test User", StandardCharsets.UTF_8));
            postData.append("&ccvv=").append(URLEncoder.encode("123", StandardCharsets.UTF_8));
            postData.append("&ccexpmon=").append(URLEncoder.encode("09", StandardCharsets.UTF_8));
            postData.append("&ccexpyr=").append(URLEncoder.encode("2026", StandardCharsets.UTF_8));
            postData.append("&api_version=").append(URLEncoder.encode("7", StandardCharsets.UTF_8));
            postData.append("&si=").append(URLEncoder.encode("1", StandardCharsets.UTF_8));
            postData.append("&si_details=").append(URLEncoder.encode("{\"billingAmount\":\"200.00\",\"billingCurrency\":\"INR\",\"billingCycle\":\"ADHOC\",\"billingInterval\":1,\"paymentStartDate\":\"2025-06-05\",\"paymentEndDate\":\"2025-12-01\",\"siTokenRequestor\":\"2\"}", StandardCharsets.UTF_8));
            postData.append("&udf1=").append(URLEncoder.encode("AELPR****E", StandardCharsets.UTF_8));
            postData.append("&udf2=").append(URLEncoder.encode("", StandardCharsets.UTF_8));
            postData.append("&udf3=").append(URLEncoder.encode("02-02-1980", StandardCharsets.UTF_8));
            postData.append("&udf4=").append(URLEncoder.encode("XYZ Pvt. Ltd.", StandardCharsets.UTF_8));
            postData.append("&udf5=").append(URLEncoder.encode("098450845", StandardCharsets.UTF_8));
            postData.append("&txn_s2s_flow=").append(URLEncoder.encode("4", StandardCharsets.UTF_8));
            postData.append("&s2s_client_ip=").append(URLEncoder.encode("10.200.12.12", StandardCharsets.UTF_8));
            postData.append("&s2s_device_info=").append(URLEncoder.encode("Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0", StandardCharsets.UTF_8));
            postData.append("&hash=").append(URLEncoder.encode("YOUR_CALCULATED_HASH", StandardCharsets.UTF_8));
            
            try (DataOutputStream wr = new DataOutputStream(connection.getOutputStream())) {
                wr.writeBytes(postData.toString());
                wr.flush();
            }
            
            int responseCode = connection.getResponseCode();
            System.out.println("Status Code: " + responseCode);
            
            BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            String inputLine;
            StringBuilder response = new StringBuilder();
            
            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();
            
            System.out.println("Response: " + response.toString());
            
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
```php
<?php
$url = "https://test.payu.in/_payment";

$postData = array(
    'key' => 'JPM7Fg',
    'txnid' => 'payuTestMandate12345',
    'amount' => '100.00',
    'firstname' => 'Ashish',
    'email' => 'test@payu.in',
    'phone' => '9988776655',
    'productinfo' => 'Subscription Plan',
    'surl' => 'https://test.payu.in/admin/test_response',
    'furl' => 'https://test.payu.in/admin/test_response',
    'pg' => 'CC',
    'bankcode' => 'CC',
    'ccnum' => '5506900480000008',
    'ccname' => 'Test User',
    'ccvv' => '123',
    'ccexpmon' => '09',
    'ccexpyr' => '2026',
    'api_version' => '7',
    'si' => '1',
    'si_details' => '{"billingAmount":"200.00","billingCurrency":"INR","billingCycle":"ADHOC","billingInterval":1,"paymentStartDate":"2025-06-05","paymentEndDate":"2025-12-01","siTokenRequestor":"2"}',
    'udf1' => 'AELPR****E',
    'udf2' => '',
    'udf3' => '02-02-1980',
    'udf4' => 'XYZ Pvt. Ltd.',
    'udf5' => '098450845',
    'txn_s2s_flow' => '4',
    's2s_client_ip' => '10.200.12.12',
    's2s_device_info' => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0',
    'hash' => 'YOUR_CALCULATED_HASH'
);

$options = array(
    'http' => array(
        'header' => "Content-type: application/x-www-form-urlencoded\r\n",
        'method' => 'POST',
        'content' => http_build_query($postData)
    )
);

$context = stream_context_create($options);

try {
    $result = file_get_contents($url, false, $context);
    
    if ($result === FALSE) {
        echo "Error: Failed to make request\n";
    } else {
        $http_response_header = $http_response_header ?? [];
        echo "Status: " . (isset($http_response_header[0]) ? $http_response_header[0] : 'Unknown') . "\n";
        echo "Response: " . $result . "\n";
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
?>
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
