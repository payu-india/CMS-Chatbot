---
title: ' Issuing Bank Status API'
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Get Issuing Bank Status** API (**getIssuingBankStatus**) is used to help you handle the credit card or debit card issuing bank downtime.

**Environment**

|            |                                                                                      |
| :--------- | :----------------------------------------------------------------------------------- |
| Production | [https://info.payu.in/issuing-bank/v1/bin](https://info.payu.in/issuing-bank/v1/bin) |
| Test       | [https://test.payu.in/issuing-bank/v1/bin](https://test.payu.in/issuing-bank/v1/bin) |

# Request header

<V2_payment_header_params />

## Query parameters

**Mandatory parameters**

| Parameter | Description                                                                                             | Example  |
| :-------- | :------------------------------------------------------------------------------------------------------ | :------- |
| `bin`     | `String` The first 6 digits of the card number (Bank Identification Number) to get issuing bank status. | `512345` |

**Optional parameters**

| Parameter             | Description                                                                | Example |
| :-------------------- | :------------------------------------------------------------------------- | :------ |
| `issuing_bank_status` | `Boolean` Flag to include issuing bank status information in the response. | `true`  |

## Request body

**Mandatory parameters**

| Parameter | Description                                                              | Example  |
| :-------- | :----------------------------------------------------------------------- | :------- |
| `bin`     | `String` The first six digits of card (card BIN) must be specified here. | `512345` |

## Sample request

```
curl --location 'https://info.payu.in/issuing-bank/v1/bin/?bin=512345&issuing_bank_status=true' \
--header 'Content-Type: application/json' \
--header 'date: {{date}}' \
--header 'Authorization: {{authorization}}' \
--data '{
    "bin": "512345"
  }'
```

The `--data` flag implies a **POST** request. Note that `bin` appears in **both the query string and the request body** — this is preserved exactly as in the original cURL. The `{{date}}` and `{{authorization}}` placeholders follow a template/collection variable style (e.g., Postman) and are kept as-is for you to substitute.

```python
import requests
import json

url = "https://info.payu.in/issuing-bank/v1/bin/"

params = {
    "bin": "512345",
    "issuing_bank_status": "true"
}

headers = {
    "Content-Type": "application/json",
    "date": "{{date}}",
    "Authorization": "{{authorization}}"
}

payload = {
    "bin": "512345"
}

response = requests.post(url, headers=headers, params=params, data=json.dumps(payload))

print("Status Code:", response.status_code)
print("Response:", response.text)
```
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        using HttpClient client = new HttpClient();

        client.DefaultRequestHeaders.Add("date", "{{date}}");
        client.DefaultRequestHeaders.Add("Authorization", "{{authorization}}");

        string requestUrl = "https://info.payu.in/issuing-bank/v1/bin/?bin=512345&issuing_bank_status=true";

        string jsonBody = "{\"bin\":\"512345\"}";
        StringContent content = new StringContent(jsonBody, Encoding.UTF8, "application/json");

        HttpResponseMessage response = await client.PostAsync(requestUrl, content);

        Console.WriteLine("Status Code: " + (int)response.StatusCode);
        Console.WriteLine("Response: " + await response.Content.ReadAsStringAsync());
    }
}
```
```javascript
const url = "https://info.payu.in/issuing-bank/v1/bin/?bin=512345&issuing_bank_status=true";

const headers = {
  "Content-Type": "application/json",
  "date": "{{date}}",
  "Authorization": "{{authorization}}"
};

const body = JSON.stringify({
  bin: "512345"
});

const response = await fetch(url, {
  method: "POST",
  headers: headers,
  body: body
});

console.log("Status Code:", response.status);
console.log("Response:", await response.text());
```
```java
import java.io.OutputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class Main {
    public static void main(String[] args) throws Exception {
        URL url = new URL("https://info.payu.in/issuing-bank/v1/bin/?bin=512345&issuing_bank_status=true");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();

        conn.setRequestMethod("POST");
        conn.setDoOutput(true);
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setRequestProperty("date", "{{date}}");
        conn.setRequestProperty("Authorization", "{{authorization}}");

        String jsonBody = "{\"bin\":\"512345\"}";
        try (OutputStream os = conn.getOutputStream()) {
            os.write(jsonBody.getBytes("UTF-8"));
        }

        int statusCode = conn.getResponseCode();
        BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        StringBuilder response = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            response.append(line);
        }
        br.close();

        System.out.println("Status Code: " + statusCode);
        System.out.println("Response: " + response.toString());
    }
}
```
```php
<?php

$url = "https://info.payu.in/issuing-bank/v1/bin/?bin=512345&issuing_bank_status=true";

$headers = [
    "Content-Type: application/json",
    "date: {{date}}",
    "Authorization: {{authorization}}"
];

$body = json_encode([
    "bin" => "512345"
]);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
$statusCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo "Status Code: " . $statusCode . "\n";
echo "Response: " . $response . "\n";
```

## Response parameters

The response parameters for a bank code passed in **var1**, it returns a response for the specified bank alone with the parameters as explained in the following table. If the **default** value is passed in **var1**, it returns a array of all the banks in a JSON array format and each JSON has the list of fields similar to the parameter list:

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>message</td>
      <td><code>String</code> Response message indicating the status of the API call.</td>
      <td>Success</td>
    </tr>
    <tr>
      <td>status</td>
      <td><code>Integer</code> Overall status code of the API response.</td>
      <td>1</td>
    </tr>
    <tr>
      <td>result</td>
      <td><code>Object</code> Contains detailed information about the BIN and issuing bank details. For more information, refer to <a href="#result-object-fields-description"> result object fields description</a></td>
      <td>Refer to <a href="#result-object-fields-description">result object fields description</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

### result object fields description

Sample object

```
 {
        "status": 0,
        "category": "creditcard",
        "bin": "512345",
        "is_domestic": false,
        "card_type": "MAST",
        "issuing_bank": "UNKNOWN",
        "otp_on_fly": false,
        "issuing_bank_status": 1,
        "is_atmpin_card": 1,
        "oobEligible": false
}
```

Fields description

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Field</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>status</td>
      <td><code>Integer</code> Status code specific to the BIN lookup result.</td>
      <td>0</td>
    </tr>
    <tr>
      <td>category</td>
      <td><code>String</code> Category of the card (e.g., creditcard, debitcard).</td>
      <td>creditcard</td>
    </tr>
    <tr>
      <td>bin</td>
      <td><code>String</code> The Bank Identification Number (first 6 digits of the card).</td>
      <td>512345</td>
    </tr>
    <tr>
      <td>is_domestic</td>
      <td><code>Boolean</code> Indicates whether the card is domestic (true) or international (false).</td>
      <td>false</td>
    </tr>
    <tr>
      <td>card_type</td>
      <td><code>String</code> Type of card network (MAST, VISA, AMEX, etc.).</td>
      <td>MAST</td>
    </tr>
    <tr>
      <td>issuing_bank</td>
      <td><code>String</code> Name of the issuing bank or "UNKNOWN" if not identified.</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <td>otp_on_fly</td>
      <td><code>Boolean</code> Indicates if the card supports OTP on the fly authentication.</td>
      <td>false</td>
    </tr>
    <tr>
      <td>issuing_bank_status</td>
      <td><code>Integer</code> Status code for the issuing bank information.</td>
      <td>1</td>
    </tr>
    <tr>
      <td>is_atmpin_card</td>
      <td><code>Integer</code> Indicates if the card supports ATM PIN authentication (1 = yes, 0 = no).</td>
      <td>1</td>
    </tr>
    <tr>
      <td>oobEligible</td>
      <td><code>Boolean</code> Indicates if the card is eligible for out-of-band authentication.</td>
      <td>false</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Sample response

```
{
    "message": "Success",
    "status": 1,
    "result": {
        "status": 0,
        "category": "creditcard",
        "bin": "512345",
        "is_domestic": false,
        "card_type": "MAST",
        "issuing_bank": "UNKNOWN",
        "otp_on_fly": false,
        "issuing_bank_status": 1,
        "is_atmpin_card": 1,
        "oobEligible": false
    }
```
## Next Steps

1. **Proactive Downtime Warnings**:
   - If `issuing_bank_status` is `0` (DOWN), display a warning banner on your checkout form alerting the shopper that their issuing bank is facing degradation.
2. **Suggest Alternative Payment Methods**:
   - Recommend using UPI, Net Banking, or a different card to prevent transaction drop-offs and improve checkout conversion rates.
3. **Proceed with Payment**:
   - If the bank is active (`1`), seamlessly proceed with the **[Cards v2 Payment API](ref:_payment-v2-merchant-hosted-cards)**.
}
