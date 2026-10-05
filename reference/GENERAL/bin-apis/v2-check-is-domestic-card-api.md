---
title: Check is Domestic Card API
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: Check is Domestic Card API
deprecated: false
hidden: false
metadata:
  title: Check is Domestic Card API
  description: Fast evaluation of card BIN nationality (domestic vs international), issuing bank, card type, and category.
  robots: index
---

The **Check is Domestic Card** API allows merchants to verify whether a given card Bank Identification Number (BIN) belongs to a domestic Indian financial institution or an international issuer. This information enables merchants to route payments effectively and adjust processing fees or authentication paths.

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
| `is_domestic` | Boolean | Mandatory | Flag instructing the engine to evaluate domestic card status. Set to `true`. | `true` |

---

## Request Body Parameters

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `bin` | `String` The first 6 or 8 digits of the card number (BIN). | `462273` |

---

## Sample Request

```bash
curl --location '<redacted URL>' \
--header 'Content-Type: application/json' \
--header 'Date: Tue, 17 Jun 2025 06:48:55 GMT' \
--header 'Authorization: hmac username="<YOUR_MERCHANT_KEY>", algorithm="sha512", headers="date", signature="<YOUR_SIGNATURE>"' \
--data '{
  "bin": "462273"
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
    "bin": "462273"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

```php
<?php
$url = "<redacted URL>";

$payload = json_encode([
    "bin" => "462273"
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
        
        String payload = "{\"bin\": \"462273\"}";
        
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
  bin: "462273"
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
| `isDomestic` | String | `Y` if domestic Indian card; `N` if international card. | `Y` |
| `issuingBank` | String | Identified card issuing bank code (e.g. `SCB`, `HDFC`, `ICICI`, or `UNKNOWN`). | `SCB` |
| `cardType` | String | Card network brand: `VISA`, `MAST`, `AMEX`, `RUPAY`, `DINER`. | `VISA` |
| `cardCategory` | String | Card instrument category: `CC` (Credit Card) or `DC` (Debit Card). | `CC` |

---

## Sample Responses

### Domestic Card
```json
{
  "isDomestic": "Y",
  "issuingBank": "SCB",
  "cardType": "VISA",
  "cardCategory": "CC"
}
```

### International Card
```json
{
  "isDomestic": "N",
  "issuingBank": "UNKNOWN",
  "cardType": "Unknown",
  "cardCategory": "CC"
}
```
