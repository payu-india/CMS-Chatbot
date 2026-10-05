---
title: S2S Eligible BINs API
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: S2S Eligible BINs API
deprecated: false
hidden: false
metadata:
  title: S2S Eligible BINs API
  description: Lightweight, low-latency Server-to-Server API for card BIN lookup, issuing bank identification, and ATM PIN eligibility.
  robots: index
---

The **S2S Eligible BINs** API is a lightweight, low-latency endpoint specifically optimized for Server-to-Server (S2S) merchant integrations. It rapidly validates card BINs, identifies the issuing bank, confirms card category (Credit/Debit), and returns ATM PIN authentication support.

HTTP Method: **POST**

**Environment**

| Environment | URL |
| :--- | :--- |
| **Test Environment** | `<redacted URL>` |
| **Production Environment** | `<redacted URL>` |

## Request Headers

<V2_payment_header_params />

| Header | Type | Description |
| :--- | :--- | :--- |
| `Content-Type` | String | Must be `application/json`. |
| `Date` | String | Current GMT timestamp (e.g. `Tue, 17 Jun 2025 06:48:55 GMT`). |
| `Authorization` | String | Standard PayU HMAC authorization header. |

---

## Query Parameters

| Parameter | Type | Required | Description | Example |
| :--- | :--- | :--- | :--- | :--- |
| `s2s` | String | Optional | Flag activating the streamlined S2S response payload. | `s2s` |

---

## Request Body Parameters



---

## Sample Request

```bash
curl --location '<redacted URL>' \
--header 'Content-Type: application/json' \
--header 'Date: Tue, 17 Jun 2025 06:48:55 GMT' \
--header 'Authorization: hmac username="<YOUR_MERCHANT_KEY>", algorithm="sha512", headers="date", signature="<YOUR_SIGNATURE>"' \
--data '{
    "bin": "512345"
}'
```
```python
import requests

url = "<redacted URL>"

headers = {
    "Content-Type": "application/json",
    "Date": "Tue, 17 Jun 2025 06:48:55 GMT",
    "Authorization": "hmac username=\"<YOUR_MERCHANT_KEY>\", algorithm=\"sha512\", headers=\"date\", signature=\"<YOUR_SIGNATURE>\""
}

payload = {
    "bin": "512345"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```
```php
<?php
$url = "<redacted URL>";

$payload = json_encode([
    "bin" => "512345"
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
        
        String payload = "{\"bin\": \"512345\"}";
        
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("<redacted URL>"))
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
const url = "<redacted URL>";

const payload = {
  bin: "512345"
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
| `message` | String | Status description of the query execution. | `Success` |
| `status` | Number | Execution outcome flag: `1` for success, `0` for failure. | `1` |
| `result.bin` | String | Queried card BIN digits. | `512345` |
| `result.issuing_bank` | String | PayU bank identifier for the issuing institution. | `HDFC` |
| `result.category` | String | Card instrument category: `creditcard` or `debitcard`. | `creditcard` |
| `result.card_type` | String | Card scheme network (`MAST`, `VISA`, `RUPAY`, `AMEX`). | `MAST` |
| `result.is_domestic` | Boolean | `true` if domestic Indian card; `false` if international. | `true` |
| `result.is_atmpin_card` | Number | `1` if the card supports 2-Factor ATM PIN authentication; `0` otherwise. | `1` |

---

## Sample Response

```json
{
  "message": "Success",
  "status": 1,
  "result": {
    "bin": "512345",
    "issuing_bank": "HDFC",
    "category": "creditcard",
    "card_type": "MAST",
    "is_domestic": true,
    "is_atmpin_card": 1
  }
}
```
## Next Steps

1. **Detect Card Type & Sub-Type**:
   - Use the returned `category` (`creditcard` vs `debitcard`) and `card_type` (Visa, Mastercard, RuPay) to automatically select the matching card icon and form validations.
2. **Route ATM PIN vs OTP Flow**:
   - Check `is_atmpin_card`; if eligible and supported, offer debit cardholders the choice to authenticate via 2-factor OTP or ATM PIN.
3. **Submit Payment Request**:
   - Forward the card details directly to the **[Cards v2 Payment API](ref:_payment-v2-merchant-hosted-cards)**.
