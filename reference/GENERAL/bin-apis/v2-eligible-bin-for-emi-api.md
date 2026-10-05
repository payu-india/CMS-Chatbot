---
title: Eligible Bin for EMI API
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  title: ''
  description: ''
  robots: index
---
---
title: Eligible BIN for EMI API
deprecated: false
hidden: false
metadata:
  title: Eligible BIN for EMI API
  description: Verify card BIN eligibility for Equated Monthly Installment (EMI) payment options and fetch minimum order transaction thresholds per bank.
  robots: index
---

The **Eligible BIN for EMI** API allows merchants to verify if a customer's credit or debit card BIN is eligible for EMI plans. It also returns the issuing bank identifier and the minimum transaction amount required to qualify for EMI financing.

HTTP Method: **POST**

**Environment**

| Environment | URL |
| :--- | :--- |
| **Test Environment** | `<redacted URL>` |
| **Production Environment** | `<redacted URL>` |

## Request Headers

<V2_payment_header_params />

| Header | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `Content-Type` | String | Must be `application/json`. | `application/json` |
| `Date` | String | Current GMT timestamp (e.g. `Thu, 17 Feb 2025 08:17:59 GMT`). | `Thu, 17 Feb 2025 08:17:59 GMT` |
| `Digest` | String | Base64-encoded SHA-256 hash of the JSON request payload. | `vpGay5D/dmfoDupALPpl...=` |
| `Authorization` | String | HMAC-SHA256 signature calculated over the `Date` and `Digest` headers. | `hmac username="<KEY>", algorithm="hmac-sha256", headers="date digest", signature="..."` |
| `platformId` | String | Static platform identifier for API routing. Pass `1`. | `1` |

---

## Request Body Parameters

Merchants can verify BIN eligibility either with or without pre-specifying the issuing bank:

**Mandatory parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `bintype` | `String` Mode of card identification: pass `bin` for card BIN digits, or `NET` for network token lookup. | `bin` |
| `value` | `String` The first 6, 8, or 9 digits of the card number (or full token if `bintype` is `NET`). | `416104` |

**Conditional parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `amount` | `Number` Transaction order amount. Mandatory when checking eligibility for specific non-bank issuers (e.g., `ONEC` or `BAJFIN`). | `10000.00` |

**Optional parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `bank` | `String` Specific issuing bank code (e.g. `ICICI`, `HDFC`, `AXIS`). If provided, checks eligibility specifically for that institution. | `ICICI` |

---

## Sample Request

```bash
curl --location '<redacted URL>' \
--header 'Content-Type: application/json' \
--header 'platformId: 1' \
--header 'Date: Thu, 17 Feb 2025 08:17:59 GMT' \
--header 'Digest: vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=' \
--header 'Authorization: hmac username="<YOUR_MERCHANT_KEY>", algorithm="hmac-sha256", headers="date digest", signature="zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI="' \
--data '{
    "bintype": "bin",
    "value": "416104",
    "amount": 10000.00,
    "bank": "ICICI"
}'
```
```python
import requests
import json

url = "<redacted URL>"

headers = {
    "Content-Type": "application/json",
    "platformId": "1",
    "Date": "Thu, 17 Feb 2025 08:17:59 GMT",
    "Digest": "YOUR_BASE64_SHA256_DIGEST",
    "Authorization": "hmac username=\"<YOUR_MERCHANT_KEY>\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"YOUR_SIGNATURE\""
}

payload = {
    "bintype": "bin",
    "value": "416104",
    "amount": 10000.00,
    "bank": "ICICI"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```
```php
<?php
$url = "<redacted URL>";

$payload = json_encode([
    "bintype" => "bin",
    "value" => "416104",
    "amount" => 10000.00,
    "bank" => "ICICI"
]);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Content-Type: application/json",
    "platformId: 1",
    "Date: Thu, 17 Feb 2025 08:17:59 GMT",
    "Digest: YOUR_BASE64_SHA256_DIGEST",
    "Authorization: hmac username=\"<YOUR_MERCHANT_KEY>\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"YOUR_SIGNATURE\""
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
        
        String payload = "{\"bintype\": \"bin\", \"value\": \"416104\", \"amount\": 10000.00, \"bank\": \"ICICI\"}";
        
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("<redacted URL>"))
            .header("Content-Type", "application/json")
            .header("platformId", "1")
            .header("Date", "Thu, 17 Feb 2025 08:17:59 GMT")
            .header("Digest", "YOUR_BASE64_SHA256_DIGEST")
            .header("Authorization", "hmac username=\"<YOUR_MERCHANT_KEY>\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"YOUR_SIGNATURE\"")
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
  bintype: "bin",
  value: "416104",
  amount: 10000.00,
  bank: "ICICI"
};

const options = {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "platformId": "1",
    "Date": "Thu, 17 Feb 2025 08:17:59 GMT",
    "Digest": "YOUR_BASE64_SHA256_DIGEST",
    "Authorization": "hmac username=\"<YOUR_MERCHANT_KEY>\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"YOUR_SIGNATURE\""
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
| `message` | String | Description message of the eligibility lookup. | `Details fetched successfully` |
| `status` | Number | Status flag: `1` for success, `0` for failure or ineligible BIN. | `1` |
| `result[].isEligible` | Number | `1` if the card BIN is eligible for EMI financing; `0` if not eligible. | `1` |
| `result[].bank` | String | Issuing bank code associated with the card BIN. | `ICICI` |
| `result[].minAmount` | Number | Minimum order transaction amount required to activate EMI options. | `1500.00` |

---

## Sample Responses

### Eligible BIN Response
```json
{
  "message": "Details fetched successfully",
  "status": 1,
  "result": [
    {
      "isEligible": 1,
      "bank": "ICICI",
      "minAmount": 1500.00
    }
  ]
}
```

### Ineligible BIN Response
```json
{
  "message": "Details fetched successfully",
  "status": 1,
  "result": [
    {
      "isEligible": 0,
      "bank": "ICICI",
      "minAmount": 1500.00
    }
  ]
}
```
## Next Steps

1. **Validate Card for EMI**:
   - As the customer enters the first 6 or 8 digits of their card, call this endpoint to confirm if their card BIN is eligible for EMI plans.
2. **Fetch Detailed EMI Schedules**:
   - Once BIN eligibility is confirmed, query the **[EMI Calculator API](ref:emi-calculator-api.md) using the identified bank code to fetch specific monthly instalments.
3. **Handle Ineligible Cards**:
   - If the card BIN is not eligible, inform the customer and suggest paying via full swipe or switching to a supported issuing bank.
