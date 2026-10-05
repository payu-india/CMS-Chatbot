---
title: Get BIN Info API
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: Get BIN Info API
deprecated: false
hidden: false
metadata:
  title: Get BIN Info API
  description: Retrieve card BIN metadata including issuing bank, card type, category, ATM PIN capabilities, zero-redirect, and Standing Instruction (SI) support.
  robots: index
---

The **Get BIN Info** API provides detailed metadata for a given card Bank Identification Number (BIN). Merchants can inspect card capabilities such as ATM PIN authentication, OTP-on-the-fly support, Zero-Redirect eligibility, and Standing Instruction (e-Mandate / Recurring) support.

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

## Request Body Parameters

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `bin` | `String` The first 6 or 8 digits of the card number to query. | `512345` |

---

## Sample Request

```curl
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
| `status` | Number | Outcome flag: `1` for success, `0` for failure. | `1` |
| `data.bins_data.issuing_bank` | String | PayU bank identifier for the issuing bank. | `HDFC` |
| `data.bins_data.bin` | String | The queried BIN digits. | `512345` |
| `data.bins_data.category` | String | Card category: `creditcard` or `debitcard`. | `creditcard` |
| `data.bins_data.card_type` | String | Card brand network: `MAST`, `VISA`, `AMEX`, `RUPAY`, `DINR`. | `MAST` |
| `data.bins_data.is_domestic` | Number | `1` for domestic Indian cards; `0` for international cards. | `1` |
| `data.bins_data.is_atmpin_card` | Number | `1` if ATM PIN authentication is supported; `0` otherwise. | `1` |
| `data.bins_data.is_otp_on_the_fly` | Number | `1` if the issuing bank supports OTP-on-the-fly; `0` otherwise. | `1` |
| `data.bins_data.is_zero_redirect_supported` | Number | `1` if Zero-Redirect checkout is supported; `0` otherwise. | `1` |
| `data.bins_data.is_si_supported` | Number | `1` if Standing Instructions (e-Mandate / Recurring) are supported; `0` otherwise. | `0` |

---

## Sample Response

```json
{
  "message": "Success",
  "status": 1,
  "data": {
    "bins_data": {
      "bin": "512345",
      "issuing_bank": "HDFC",
      "category": "creditcard",
      "card_type": "MAST",
      "is_domestic": 1,
      "is_atmpin_card": 1,
      "is_otp_on_the_fly": 1,
      "is_zero_redirect_supported": 1,
      "is_si_supported": 0
    }
  }
}
```
## Next Steps

1. **Configure Transaction Capabilities**:
   - Check if the card BIN supports recurring payments / standing instructions (SI), Zero-Redirect flows, or ATM PIN authentication.
2. **Optimize Payment Payload**:
   - Set relevant flags in the `additionalInfo` object of your payment request based on the capabilities confirmed for this card BIN.
3. **Proceed to Card Processing**:
   - Route the payment through the **[Cards v2 Payment API](ref:_payment-v2-merchant-hosted-cards)**.