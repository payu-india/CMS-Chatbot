---
title: Validate VPA API
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Validate VPA** API enables merchants to verify whether a customer's UPI Virtual Payment Address (VPA / UPI ID) is active and valid with the National Payments Corporation of India (NPCI) and issuing bank handle. It also verifies if the VPA is eligible for UPI Auto-Pay recurring mandates.

HTTP Method: **GET**

**Environment**

| Environment                | URL              |
| :------------------------- | :--------------- |
| **Test Environment**       | `<redacted URL>` |
| **Production Environment** | `<redacted URL>` |

## Request Headers

<V2_payment_header_params />

| Header          | Type   | Description                                                                                                               |
| :-------------- | :----- | :------------------------------------------------------------------------------------------------------------------------ |
| `Date`          | String | Current GMT timestamp (e.g. `Tue, 17 Jun 2025 06:48:55 GMT`).                                                             |
| `Authorization` | String | Standard PayU HMAC authorization header (`hmac username="<KEY>", algorithm="sha512", headers="date", signature="<SIG>"`). |

***

## Query Parameters

**Mandatory parameters**

| Parameter | Description                                                    | Example          |
| :-------- | :------------------------------------------------------------- | :--------------- |
| `vpa`     | `String` The UPI Virtual Payment Address (UPI ID) to validate. | `customer@oksbi` |

**Optional parameters**

| Parameter        | Description                                                                                                              | Example |
| :--------------- | :----------------------------------------------------------------------------------------------------------------------- | :------ |
| `isAutoVPAValid` | `Boolean` Pass `true` to check whether the VPA supports UPI Auto-Pay recurring mandate registration. Default is `false`. | `true`  |

***

## Sample Request

```bash
curl --location '<redacted URL>' \
--header 'Date: Tue, 17 Jun 2025 06:48:55 GMT' \
--header 'Authorization: hmac username="<YOUR_MERCHANT_KEY>", algorithm="sha512", headers="date", signature="<YOUR_SIGNATURE>"'
```
```python
import requests

url = "<redacted URL>"
params = {
    "vpa": "customer@oksbi",
    "isAutoVPAValid": "true"
}

headers = {
    "Date": "Tue, 17 Jun 2025 06:48:55 GMT",
    "Authorization": "hmac username=\"<YOUR_MERCHANT_KEY>\", algorithm=\"sha512\", headers=\"date\", signature=\"<YOUR_SIGNATURE>\""
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```
```php
<?php
$url = "<redacted URL>";

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Date: Tue, 17 Jun 2025 06:48:55 GMT",
    "Authorization: hmac username=\"<YOUR_MERCHANT_KEY>\", algorithm=\"sha512\", headers=\"date\", signature=\"<YOUR_SIGNATURE>\""
]);

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
        
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("<redacted URL>"))
            .header("Date", "Tue, 17 Jun 2025 06:48:55 GMT")
            .header("Authorization", "hmac username=\"<YOUR_MERCHANT_KEY>\", algorithm=\"sha512\", headers=\"date\", signature=\"<YOUR_SIGNATURE>\"")
            .GET()
            .build();
        
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
    }
}
```
```javascript
const url = "<redacted URL>";

const options = {
  method: "GET",
  headers: {
    "Date": "Tue, 17 Jun 2025 06:48:55 GMT",
    "Authorization": "hmac username=\"<YOUR_MERCHANT_KEY>\", algorithm=\"sha512\", headers=\"date\", signature=\"<YOUR_SIGNATURE>\""
  }
};

fetch(url, options)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

***

## Response Parameters

| Parameter                  | Type    | Description                                                                      | Example          |
| :------------------------- | :------ | :------------------------------------------------------------------------------- | :--------------- |
| `message`                  | String  | Outcome message describing the validation result.                                | `Success`        |
| `status`                   | Number  | Outcome flag: `1` for successful validation call, `0` for failed.                | `1`              |
| `result.isValidVpa`        | Boolean | `true` if the VPA is registered with NPCI and capable of accepting payments.     | `true`           |
| `result.payerAccountName`  | String  | Registered account holder name associated with the VPA (as returned by the PSP). | `AARAV SHARMA`   |
| `result.vpa`               | String  | Canonical VPA validated.                                                         | `customer@oksbi` |
| `result.isAutoPayVPAValid` | Boolean | `true` if this VPA is eligible for UPI Auto-Pay recurring mandates.              | `true`           |

***

## Sample Responses

### Valid VPA

```json
{
  "message": "Success",
  "status": 1,
  "result": {
    "isValidVpa": true,
    "payerAccountName": "AARAV SHARMA",
    "vpa": "customer@oksbi",
    "isAutoPayVPAValid": true
  }
}
```

### Invalid VPA

```json
{
  "message": "Invalid VPA",
  "status": 0,
  "result": {
    "isValidVpa": false,
    "payerAccountName": null,
    "vpa": "invalidvpa@handle",
    "isAutoPayVPAValid": false
  }
}
```

## Next Steps

Once you have verified that the customer's VPA is valid and active (`isVPAValid: 1`), proceed with the following steps depending on your checkout flow:

1. **Initiate UPI Collect Payment**:
   Pass the validated VPA in the `additionalInfo.vpa` parameter of the [Collect Payment (v2/payment) API](ref:_payment_v2_merchant_hosted_upi) with `"txnS2sFlow": "4"`. This triggers a payment collect request directly to the customer's UPI mobile application.

2. **Handle Invalid or Inactive VPAs**:
   If the API returns `isVPAValid: 0`:
   - Prompt the customer on your checkout UI to re-check their handle or enter an alternate VPA.
   - Display a fallback option to pay via **UPI Intent / QR code** or other available payment methods (Cards, Net Banking).

3. **Verify Auto-Pay / Recurring Eligibility (Optional)**:
   If your integration supports recurring subscriptions or UPI AutoPay, check the `isAutoVPAValid` attribute in the response before initiating mandate registration requests.

4. **Poll or Verify Payment Status**:
   After triggering the collect request, listen for PayU's server-to-server webhook callback on your configured `callBackActions.successAction` / `failureAction` URLs, or poll transaction status using the [Verify Payment API](ref:v2_verify_payment_api).
