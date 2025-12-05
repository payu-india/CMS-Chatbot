---
title: Pre-Debit SI API - Zion
deprecated: false
hidden: false
metadata:
  robots: index
---
Use the Pre-Debit SI API to send pre-debit notifications for upcoming recurring debits with parallel sequencing support.

## Environment

| Environment | URL |
|-------------|-----|
| Test | `https://test.info.payu.in/merchant/postservice.php?form=2` |
| Production | `https://info.payu.in/merchant/postservice.php?form=2` |

## Request Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| key<br/>`mandatory` | `String`<br/>Your merchant key provided by PayU. | `JP***g` |
| command<br/>`mandatory` | `String`<br/>The API command name. | `pre_debit_SI` |
| hash<br/>`mandatory` | `String`<br/>The hash value generated using the hash logic. | `abc0ada2e12` |
| var1<br/>`mandatory` | `JSON String`<br/>JSON object containing the pre-debit details. | [var1 Object Parameters Description](var1-object-parameters-description) |

### var1 Object Parameters Description

| Parameter | Description | Example |
|-----------|-------------|---------|
| authpayuid<br/>`mandatory` | `String`<br/>The authorization PayU ID received during mandate creation. | `999000000000826` |
| requestid<br/>`mandatory` | `String`<br/>Unique request ID for tracking the pre-debit request. | `RCS0123459PD` |
| debitdate<br/>`mandatory` | `String`<br/>The date when the debit will occur in YYYY-MM-DD format. | `2024-11-22` |
| amount<br/>`mandatory` | `String`<br/>The amount to be debited. | `125` |
| invoiceDisplayNumber<br/>`optional` | `String`<br/>Invoice number to display to the customer. | `12345678910` |
| mandateSeqNo<br/>`optional` | `Integer`<br/>Sequence number for parallel processing. Valid range: 2 to 11000. | `2` |

## Sample Request

```bash
curl --location 'https://test.info.payu.in/merchant/postservice.php?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'command=pre_debit_SI' \
--data-urlencode 'var1={"authpayuid":"999000000000826","requestid":"RCS0123459PD","debitdate":"2024-11-22","amount":"125","invoiceDisplayNumber":"12345678910","mandateSeqNo":2}' \
--data-urlencode 'key=JP***g' \
--data-urlencode 'hash=abc0ada2e12'
```

```python
import requests

url = "https://test.info.payu.in/merchant/postservice.php?form=2"

payload = {
    "command": "pre_debit_SI",
    "var1": '{"authpayuid":"999000000000826","requestid":"RCS0123459PD","debitdate":"2024-11-22","amount":"125","invoiceDisplayNumber":"12345678910","mandateSeqNo":2}',
    "key": "JP***g",
    "hash": "abc0ada2e12"
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(url, data=payload, headers=headers)
print(response.json())
```

```csharp
using System;
using System.Net.Http;
using System.Collections.Generic;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        using var client = new HttpClient();
        
        var content = new FormUrlEncodedContent(new[]
        {
            new KeyValuePair<string, string>("command", "pre_debit_SI"),
            new KeyValuePair<string, string>("var1", "{\"authpayuid\":\"999000000000826\",\"requestid\":\"RCS0123459PD\",\"debitdate\":\"2024-11-22\",\"amount\":\"125\",\"invoiceDisplayNumber\":\"12345678910\",\"mandateSeqNo\":2}"),
            new KeyValuePair<string, string>("key", "JP***g"),
            new KeyValuePair<string, string>("hash", "abc0ada2e12")
        });
        
        var response = await client.PostAsync("https://test.info.payu.in/merchant/postservice.php?form=2", content);
        var result = await response.Content.ReadAsStringAsync();
        Console.WriteLine(result);
    }
}
```

```javascript
const sendPreDebitRequest = async () => {
    const url = "https://test.info.payu.in/merchant/postservice.php?form=2";
    
    const params = new URLSearchParams();
    params.append("command", "pre_debit_SI");
    params.append("var1", JSON.stringify({
        authpayuid: "999000000000826",
        requestid: "RCS0123459PD",
        debitdate: "2024-11-22",
        amount: "125",
        invoiceDisplayNumber: "12345678910",
        mandateSeqNo: 2
    }));
    params.append("key", "JP***g");
    params.append("hash", "abc0ada2e12");
    
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: params
    });
    
    const data = await response.json();
    console.log(data);
};

sendPreDebitRequest();
```

```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class PreDebitSI {
    public static void main(String[] args) throws Exception {
        String url = "https://test.info.payu.in/merchant/postservice.php?form=2";
        
        String params = "command=pre_debit_SI" +
            "&var1=" + URLEncoder.encode("{\"authpayuid\":\"999000000000826\",\"requestid\":\"RCS0123459PD\",\"debitdate\":\"2024-11-22\",\"amount\":\"125\",\"invoiceDisplayNumber\":\"12345678910\",\"mandateSeqNo\":2}", StandardCharsets.UTF_8) +
            "&key=JP***g" +
            "&hash=abc0ada2e12";
        
        HttpURLConnection conn = (HttpURLConnection) new URL(url).openConnection();
        conn.setRequestMethod("POST");
        conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
        conn.setDoOutput(true);
        
        try (OutputStream os = conn.getOutputStream()) {
            os.write(params.getBytes(StandardCharsets.UTF_8));
        }
        
        try (BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()))) {
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        }
    }
}
```

```php
<?php
$url = "https://test.info.payu.in/merchant/postservice.php?form=2";

$data = array(
    "command" => "pre_debit_SI",
    "var1" => json_encode(array(
        "authpayuid" => "999000000000826",
        "requestid" => "RCS0123459PD",
        "debitdate" => "2024-11-22",
        "amount" => "125",
        "invoiceDisplayNumber" => "12345678910",
        "mandateSeqNo" => 2
    )),
    "key" => "JP***g",
    "hash" => "abc0ada2e12"
);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array("Content-Type: application/x-www-form-urlencoded"));

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```

## Response Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| status | `String`<br/>Status of the request. `1` indicates success, `0` or error code indicates failure. | `1` |
| action | `String`<br/>The action performed. | `MANDATE_PRE_DEBIT` |
| message | `String`<br/>Description of the response status. | `Request Processed Successfully` |

## Sample Responses

### Success Response

```json
{
    "status": "1",
    "action": "MANDATE_PRE_DEBIT",
    "message": "Request Processed Successfully"
}
```

### Error Responses

| Scenario | Response |
|----------|----------|
| Invalid mandateSeqNo | `{"status":"0","message":"Invalid value for mandateSeqNo","action":"MANDATE_PRE_DEBIT"}` |
| Pre-debit already sent for sequence | `{"status":"E9254","action":"MANDATE_PRE_DEBIT","message":"Predebit notification already sent for the mandate sequence no. 2"}` |
| Execution already exists for sequence | `{"status":"E9256","action":"MANDATE_PRE_DEBIT","message":"Execution already sent for the mandate sequence no.:2"}` |
| Debit date exceeds 30 days | `{"status":"E9260","action":"MANDATE_PRE_DEBIT","message":"Predebit notification can only be sent for a maximum 30 days in advance."}` |
| Pre-debit sent for past sequence | `{"status":"E9263","action":"MANDATE_PRE_DEBIT","message":"Predebit for calculated sequence sent during incorrect period"}` |
