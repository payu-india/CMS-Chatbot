---
title: Get User Cards API
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Get User Cards API** fetches all active stored card tokens for a specific customer in PayU Vault, formatted with masked card numbers, card brands, and expiration metadata.

## Endpoint & Environments

| Environment    | Method | URL              |
| :------------- | :----- | :--------------- |
| **Test**       | `GET`  | `<redacted URL>` |
| **Production** | `GET`  | `<redacted URL>` |

***

## Headers

<V2_payment_header_params />

***

## Query Parameters

The table has 2 rows, so here it is in **Markdown format**. Also, noting that no Example column was present in the original, it has been omitted:

**Mandatory parameters**

| Parameter         | Description                                                                                                                                                                         |
| :---------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `userCredentials` | `String` Plaintext identifier representing merchant key and customer ID in format `<merchantKey>:<customerId>` (e.g. `sms:user12345`). URL-encoded in HTTP GET. Max 100 characters. |

**Optional parameters**

| Parameter        | Description                                                                                                |
| :--------------- | :--------------------------------------------------------------------------------------------------------- |
| `getSoftDeleted` | `Integer` Pass `1` to retrieve soft-deleted cards if permitted by merchant vault settings. Default is `0`. |

***

## Response Parameters

The endpoint returns an object with `status`, `msg`, and the `user_cards` array.

The table has 12 rows, so here it is in **HTML format**. Also, noting that no Required or Example columns were present in the original, the table has not been split and those columns have been omitted:

<table>
  <thead>
    <tr>
      <th align="left">Parameter</th>
      <th align="left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>status</code></td>
      <td><code>Integer</code> Status indicator: <code>1</code> (Success) or <code>0</code> (Failure).</td>
    </tr>
    <tr>
      <td><code>msg</code></td>
      <td><code>String</code> Outcome message.</td>
    </tr>
    <tr>
      <td><code>cardToken</code></td>
      <td><code>String</code> Unique token identifier representing the stored card in PayU Vault.</td>
    </tr>
    <tr>
      <td><code>cardNo</code></td>
      <td><code>String</code> Masked card number (e.g. <code>512345XXXXXX2346</code>).</td>
    </tr>
    <tr>
      <td><code>cardName</code></td>
      <td><code>String</code> Cardholder name.</td>
    </tr>
    <tr>
      <td><code>cardType</code></td>
      <td><code>String</code> Card network brand (e.g. <code>MAST</code>, <code>VISA</code>, <code>RUPAY</code>, <code>AMEX</code>).</td>
    </tr>
    <tr>
      <td><code>cardCategory</code></td>
      <td><code>String</code> Card category: <code>CC</code> (Credit Card) or <code>DC</code> (Debit Card).</td>
    </tr>
    <tr>
      <td><code>cardExpiryYear</code></td>
      <td><code>String</code> 4-digit card expiry year.</td>
    </tr>
    <tr>
      <td><code>cardExpiryMonth</code></td>
      <td><code>String</code> 2-digit card expiry month.</td>
    </tr>
    <tr>
      <td><code>isExpired</code></td>
      <td><code>Boolean</code> Indicates whether the card has expired.</td>
    </tr>
    <tr>
      <td><code>networkToken</code></td>
      <td><code>String</code> Network-generated token identifier (returned if network token exists).</td>
    </tr>
    <tr>
      <td><code>issuerToken</code></td>
      <td><code>String</code> Issuer-generated token identifier.</td>
    </tr>
  </tbody>
</table>
### Sample Response (Success)

```json
{
  "status": 1,
  "msg": "Cards fetched successfully",
  "user_cards": [
    {
      "cardToken": "29850879bf39848ca078727b8e1a95165a41cea1",
      "cardNo": "512345XXXXXX2346",
      "cardName": "John Doe",
      "cardType": "MAST",
      "cardCategory": "CC",
      "cardExpiryYear": "2029",
      "cardExpiryMonth": "12",
      "isExpired": false
    }
  ]
}
```

### Sample Response (Failure)

```json
{
  "status": 0,
  "msg": "No cards found for this user"
}
```

***

## Code Samples

### cURL

```bash
curl --location --request GET '<redacted URL>' \
--header 'Date: Mon, 05 Oct 2026 08:30:00 GMT' \
--header 'Authorization: hmac username="merchant_key", algorithm="sha512", headers="date", signature="<SIGNATURE>"'
```

### Python

```python
import requests

url = "<redacted URL>"
params = {
    "userCredentials": "sms:user12345"
}
headers = {
    "Date": "Mon, 05 Oct 2026 08:30:00 GMT",
    "Authorization": 'hmac username="merchant_key", algorithm="sha512", headers="date", signature="<SIGNATURE>"'
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### PHP

```php
<?php
$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => '<redacted URL>',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => [
    'Date: Mon, 05 Oct 2026 08:30:00 GMT',
    'Authorization: hmac username="merchant_key", algorithm="sha512", headers="date", signature="<SIGNATURE>"'
  ],
]);

$response = curl_exec($curl);
curl_close($curl);
echo $response;
```

### Java

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class GetUserCards {
    public static void main(String[] args) throws Exception {
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("<redacted URL>"))
            .header("Date", "Mon, 05 Oct 2026 08:30:00 GMT")
            .header("Authorization", "hmac username=\"merchant_key\", algorithm=\"sha512\", headers=\"date\", signature=\"<SIGNATURE>\"")
            .GET()
            .build();

        HttpClient client = HttpClient.newHttpClient();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
    }
}
```

### Node.js

```javascript
const axios = require('axios');

const config = {
  method: 'get',
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

***

## Next Steps

1. **Populate Checkout UI**:
   - Render the returned list of saved cards with masked PANs and card brand icons.
2. **Execute Saved Card Payment**:
   - Submit the selected `cardToken` and customer CVV to the [Process Transaction with a Saved Card API](./process-transaction-with-a-saved-card.md).
3. **Allow Customer to Remove Card**:
   - Provide a "Delete" button that triggers the [Delete a Saved Card API](./v2_delete-card-api.md).
