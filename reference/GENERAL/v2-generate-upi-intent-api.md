---
title: Generate UPI Intent API
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: Generate UPI Intent API
deprecated: false
hidden: false
metadata:
  title: Generate UPI Intent API
  description: Generate server-side UPI payment intent URIs and QR code links for deep linking to UPI applications.
  robots: index
---

The **Generate UPI Intent** API enables merchants to create UPI payment intents dynamically on the server. This allows mobile applications to invoke installed UPI apps (Google Pay, PhonePe, Paytm, BHIM, Cred) via deep linking, or web applications to display dynamic payment QR codes for scanning.

HTTP Method: **POST**

**Environment**

| Environment | URL |
| :--- | :--- |
| **Test Environment** | `<redacted URL>` |
| **Production Environment** | `https://info.payu.in/v1/intent` |

## Request Headers

<V2_payment_header_params />

| Header | Type | Description |
| :--- | :--- | :--- |
| `Content-Type` | String | Must be `application/json`. |
| `Date` | String | Current GMT timestamp (e.g. `Tue, 17 Jun 2025 06:48:55 GMT`). |
| `Authorization` | String | Standard PayU HMAC authorization header. |

---

## Request Body Parameters

**Mandatory parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `transactionId` | `String` Unique merchant transaction identifier (`txnId`). Must be unique for every payment request. | `TXN_UPI_9829f68` |
| `transactionAmount` | `String` Amount to be paid by the customer, formatted with two decimal places (`XX.XX`). | `190.00` |
| `expiryTime` | `String` Intent validity window in seconds. After this duration, the intent expires. | `600` |

**Optional parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `refUrl` | `String` Reference URL for the transaction or merchant application callback. | `<redacted URL>` |
| `category` | `String` Merchant Category Code (MCC) identifier for reporting purposes. | `5411` |

---

## Sample Request

```bash
curl --location 'https://info.payu.in/v1/intent' \
--header 'Content-Type: application/json' \
--header 'Date: Tue, 17 Jun 2025 06:48:55 GMT' \
--header 'Authorization: hmac username="<YOUR_MERCHANT_KEY>", algorithm="sha512", headers="date", signature="<YOUR_SIGNATURE>"' \
--data '{
    "transactionId": "TXN_UPI_9829f68",
    "transactionAmount": "190.00",
    "expiryTime": "600",
    "refUrl": "<redacted URL>",
    "category": "5411"
}'
```
```python
import requests
import json

url = "https://info.payu.in/v1/intent"

headers = {
    "Content-Type": "application/json",
    "Date": "Tue, 17 Jun 2025 06:48:55 GMT",
    "Authorization": "hmac username=\"<YOUR_MERCHANT_KEY>\", algorithm=\"sha512\", headers=\"date\", signature=\"<YOUR_SIGNATURE>\""
}

payload = {
    "transactionId": "TXN_UPI_9829f68",
    "transactionAmount": "190.00",
    "expiryTime": "600",
    "refUrl": "<redacted URL>",
    "category": "5411"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```
```php
<?php
$url = "https://info.payu.in/v1/intent";

$payload = json_encode([
    "transactionId" => "TXN_UPI_9829f68",
    "transactionAmount" => "190.00",
    "expiryTime" => "600",
    "refUrl" => "<redacted URL>",
    "category" => "5411"
]);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Content-Type: application/json",
    "Date: Tue, 17 Jun 2025 06:48:55 GMT",
    "Authorization: hmac username=\"<YOUR_MERCHANT_KEY>\", algorithm=\"sha512\", headers=\"date\", signature=\"<YOUR_SIGNATURE>\""
]);
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```
```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class PayURequest {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();
        
        String payload = "{\"transactionId\": \"TXN_UPI_9829f68\", \"transactionAmount\": \"190.00\", \"expiryTime\": \"600\", \"refUrl\": \"<redacted URL>", \"category\": \"5411\"}";
        
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://info.payu.in/v1/intent"))
            .header("Content-Type", "application/json")
            .header("Date", "Tue, 17 Jun 2025 06:48:55 GMT")
            .header("Authorization", "hmac username=\"<YOUR_MERCHANT_KEY>\", algorithm=\"sha512\", headers=\"date\", signature=\"<YOUR_SIGNATURE>\"")
            .POST(HttpRequest.BodyPublishers.ofString(payload))
            .build();
        
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
    }
}
```

```javascript
const url = "https://info.payu.in/v1/intent";

const payload = {
  transactionId: "TXN_UPI_9829f68",
  transactionAmount: "190.00",
  expiryTime: "600",
  refUrl: "<redacted URL>",
  category: "5411"
};

const options = {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "Date": "Tue, 17 Jun 2025 06:48:55 GMT",
    "Authorization": "hmac username=\"<YOUR_MERCHANT_KEY>\", algorithm=\"sha512\", headers=\"date\", signature=\"<YOUR_SIGNATURE>\""
  },
  body: JSON.stringify(payload)
};

fetch(url, options)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

## Response Parameters

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `message` | String | Status description of the API call. | `Success` |
| `status` | Number | Outcome flag: `1` for success, `0` for failure. | `1` |
| `result.intentId` | String | Standard `upi://pay` URI string formatted for deep linking. | `upi://pay?pa=payumoney@hdfcbank&...` |
| `result.intentUri` | String | Direct URI compatible with Android and iOS native intent handlers. | `upi://pay?pa=payumoney@hdfcbank&...` |
| `result.intentUrl` | String | Web-hosted checkout URL for customer browser display. | `https://secure.payu.in/omni?id=000b` |
| `result.intentUrlWithQR` | String | Web URL rendering a dynamic QR code for desktop/mobile scanning. | `https://secure.payu.in/omni?id=000b` |
| `result.transactionId` | String | Merchant transaction identifier confirmed by the engine. | `TXN_UPI_9829f68` |
| `result.expiryTime` | Number | Validity duration in seconds. | `600` |

---

## Sample Response

```json
{
  "message": "Success",
  "status": 1,
  "result": {
    "intentId": "upi://pay?pa=payumoney@hdfcbank&pn=MerchantEnterprise&tr=TXN_UPI_9829f68&am=190.00&cu=INR&mc=5411&tn=Order%20Payment",
    "intentUri": "upi://pay?pa=payumoney@hdfcbank&pn=MerchantEnterprise&tr=TXN_UPI_9829f68&am=190.00&cu=INR&mc=5411&tn=Order%20Payment",
    "intentUrl": "https://secure.payu.in/omni?id=000b",
    "intentUrlWithQR": "https://secure.payu.in/omni?id=000b",
    "transactionId": "TXN_UPI_9829f68",
    "expiryTime": 600
  }
}
```
