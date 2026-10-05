---
title: Delete a Saved Card API
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: Delete a Saved Card API
deprecated: false
hidden: false
metadata:
  robots: index
---

This v2 API is used to delete an existing card stored on PayU Vault.

HTTP Method: **DELETE**

**Environment**

|            |                                                                                        |
| :--------- | :------------------------------------------------------------------------------------- |
| Test       | [https://apitest.payu.in/storecard/card/v1](https://apitest.payu.in/storecard/card/v1) |
| Production | [https://info.payu.in/storecard/card/v1](https://info.payu.in/storecard/card/v1)       |

## Request parameters

<HeaderAuthentication />

### Query parameters
**Mandatory**
| Parameter                       | Description                                                                                | Example              |
| ------------------------------- | ------------------------------------------------------------------------------------------ | -------------------- |
| userCredential<br />`mandatory` | `String` User authentication credential in the format `username:userid`.                   | testuser:testuser123 |
| cardToken<br />`mandatory`      | `String` Card token of the saved card.                                                     |                      |
**Optional**

| Parameter                       | Description                                                                                | Example              |
| ------------------------------- | ------------------------------------------------------------------------------------------ | -------------------- |
| networkToken<br />`optional`    | `String` Network issuer token.                                                             |                      |
| issuerToken  <br />`optional`   | `String` Issuer token.                                                                     |                      |
| bankType <br />`optional`       | `String` The bank type of card. It can be any of the following: Credit, Debit, or Prepaid. | Credit               |
---
## Sample Request
```curl
curl --location --request DELETE '<redacted URL>' \
--header 'Date: Mon, 05 Oct 2026 08:30:00 GMT' \
--header 'Authorization: hmac username="merchant_key", algorithm="sha512", headers="date", signature="<SIGNATURE>"'
```
```python
import requests

url = "<redacted URL>"
params = {
    "userCredential": "sms:user12345",
    "cardToken": "29850879bf39848ca078727b8e1a95165a41cea1"
}
headers = {
    "Date": "Mon, 05 Oct 2026 08:30:00 GMT",
    "Authorization": 'hmac username="merchant_key", algorithm="sha512", headers="date", signature="<SIGNATURE>"'
}

response = requests.delete(url, headers=headers, params=params)
print(response.json())
```
```php
<?php
$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => '<redacted URL>',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_CUSTOMREQUEST => 'DELETE',
  CURLOPT_HTTPHEADER => [
    'Date: Mon, 05 Oct 2026 08:30:00 GMT',
    'Authorization: hmac username="merchant_key", algorithm="sha512", headers="date", signature="<SIGNATURE>"'
  ],
]);

$response = curl_exec($curl);
curl_close($curl);
echo $response;
```
```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class DeleteCard {
    public static void main(String[] args) throws Exception {
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("<redacted URL>"))
            .header("Date", "Mon, 05 Oct 2026 08:30:00 GMT")
            .header("Authorization", "hmac username=\"merchant_key\", algorithm=\"sha512\", headers=\"date\", signature=\"<SIGNATURE>\"")
            .DELETE()
            .build();

        HttpClient client = HttpClient.newHttpClient();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
    }
}
```
```javascript
const axios = require('axios');

const config = {
  method: 'delete',
  url: '<redacted URL>',
  headers: { 
    'Date': 'Mon, 05 Oct 2026 08:30:00 GMT',
    'Authorization': 'hmac username="merchant_key", algorithm="sha512", headers="date", signature="<SIGNATURE>"'
  }
};

axios(config)
  .then(response => console.log(JSON.stringify(response.data)))
  .catch(error => console.error(error));
```
## Response Parameters

| Parameter | Type | Description |
| :--- | :--- | :--- |
| **status** | Integer | Status flag: `1` (Success) or `0` (Failure). |
| **message** | String | Descriptive outcome message (e.g. `"Card deleted successfully"`). |

### Sample Response (Success)

```json
{
  "status": 1,
  "message": "Card deleted successfully"
}
```

### Sample Response (Failure)

```json
{
  "status": 0,
  "message": "cardToken is invalid"
}
```

---

## Next Steps

1. **Update Local Customer Profile**:
   - On receiving `status: 1`, remove the corresponding card token and masked PAN reference from your customer database.
2. **Refresh Stored Payment Instruments UI**:
   - Refresh the customer's payment options using the **[Get User Cards API](./v2_get_user_cards_api.md)** or **[Get Payment Instrument API](./v2-get-payment-instrument-api.md)**.
3. **Handle Edge Cases**:
   - If the API returns `status: 0` (`cardToken is invalid`), ensure that the card is marked deleted or purged locally.
