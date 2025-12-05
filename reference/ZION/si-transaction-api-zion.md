---
title: SI Transaction API - Zion
deprecated: false
hidden: true
metadata:
  robots: index
---
Use the **SI Transaction** API to execute recurring transactions with parallel sequencing support for UPI AutoPay.

## Environment

| Environment | URL |
|-------------|-----|
| Test | `https://test.payu.in/merchant/postservice?form=2` |
| Production | `https://info.payu.in/merchant/postservice?form=2` |

## Request Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| command<br/>`mandatory` | `String`<br/>The API command name. | `si_transaction` |
| key<br/>`mandatory` | `String`<br/>Your merchant key provided by PayU. | `JP***g` |
| hash<br/>`mandatory` | `String`<br/>The hash value generated using the hash logic. | `jbUS07Og8BToVZ` |
| var1<br/>`mandatory` | `JSON String`<br/>JSON object containing the transaction details. | See below |

### var1 Object Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| authpayuid<br/>`mandatory` | `String`<br/>The authorization PayU ID received during mandate creation. | `6611192557` |
| txnid<br/>`mandatory` | `String`<br/>Unique transaction ID for this execution. | `REC15113506209` |
| amount<br/>`mandatory` | `String`<br/>The amount to be debited. | `3` |
| phone<br/>`mandatory` | `String`<br/>Customer's phone number. | `9999999999` |
| email<br/>`mandatory` | `String`<br/>Customer's email address. | `abc@email.com` |
| invoiceDisplayNumber<br/>`optional` | `String`<br/>Invoice number to display to the customer. | `2345678910` |
| mandateSeqNo<br/>`optional` | `Integer`<br/>Sequence number for parallel processing. Valid range: 2 to 11000. | `3` |
| udf2<br/>`optional` | `String`<br/>User-defined field 2. | ` ` |
| udf3<br/>`optional` | `String`<br/>User-defined field 3. | ` ` |
| udf4<br/>`optional` | `String`<br/>User-defined field 4. | ` ` |
| udf5<br/>`optional` | `String`<br/>User-defined field 5. | ` ` |

## Sample Request

```bash
curl --location 'https://test.payu.in/merchant/postservice?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=JP***g' \
--data-urlencode 'command=si_transaction' \
--data-urlencode 'var1={"authpayuid":"6611192557","invoiceDisplayNumber":"2345678910","amount":"3","txnid":"REC15113506209","phone":"9999999999","email":"abc@email.com","udf2":"","udf3":"","udf4":"","udf5":"","mandateSeqNo":3}' \
--data-urlencode 'hash=jbUS07Og8BToVZ'
```

```python
import requests

url = "https://test.payu.in/merchant/postservice?form=2"

payload = {
    "key": "JP***g",
    "command": "si_transaction",
    "var1": '{"authpayuid":"6611192557","invoiceDisplayNumber":"2345678910","amount":"3","txnid":"REC15113506209","phone":"9999999999","email":"abc@email.com","udf2":"","udf3":"","udf4":"","udf5":"","mandateSeqNo":3}',
    "hash": "jbUS07Og8BToVZ"
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
            new KeyValuePair<string, string>("key", "JP***g"),
            new KeyValuePair<string, string>("command", "si_transaction"),
            new KeyValuePair<string, string>("var1", "{\"authpayuid\":\"6611192557\",\"invoiceDisplayNumber\":\"2345678910\",\"amount\":\"3\",\"txnid\":\"REC15113506209\",\"phone\":\"9999999999\",\"email\":\"abc@email.com\",\"udf2\":\"\",\"udf3\":\"\",\"udf4\":\"\",\"udf5\":\"\",\"mandateSeqNo\":3}"),
            new KeyValuePair<string, string>("hash", "jbUS07Og8BToVZ")
        });
        
        var response = await client.PostAsync("https://test.payu.in/merchant/postservice?form=2", content);
        var result = await response.Content.ReadAsStringAsync();
        Console.WriteLine(result);
    }
}
```

```javascript
const executeTransaction = async () => {
    const url = "https://test.payu.in/merchant/postservice?form=2";
    
    const params = new URLSearchParams();
    params.append("key", "JP***g");
    params.append("command", "si_transaction");
    params.append("var1", JSON.stringify({
        authpayuid: "6611192557",
        invoiceDisplayNumber: "2345678910",
        amount: "3",
        txnid: "REC15113506209",
        phone: "9999999999",
        email: "abc@email.com",
        udf2: "",
        udf3: "",
        udf4: "",
        udf5: "",
        mandateSeqNo: 3
    }));
    params.append("hash", "jbUS07Og8BToVZ");
    
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

executeTransaction();
```

```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class SITransaction {
    public static void main(String[] args) throws Exception {
        String url = "https://test.payu.in/merchant/postservice?form=2";
        
        String params = "key=JP***g" +
            "&command=si_transaction" +
            "&var1=" + URLEncoder.encode("{\"authpayuid\":\"6611192557\",\"invoiceDisplayNumber\":\"2345678910\",\"amount\":\"3\",\"txnid\":\"REC15113506209\",\"phone\":\"9999999999\",\"email\":\"abc@email.com\",\"udf2\":\"\",\"udf3\":\"\",\"udf4\":\"\",\"udf5\":\"\",\"mandateSeqNo\":3}", StandardCharsets.UTF_8) +
            "&hash=jbUS07Og8BToVZ";
        
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
$url = "https://test.payu.in/merchant/postservice?form=2";

$data = array(
    "key" => "JP***g",
    "command" => "si_transaction",
    "var1" => json_encode(array(
        "authpayuid" => "6611192557",
        "invoiceDisplayNumber" => "2345678910",
        "amount" => "3",
        "txnid" => "REC15113506209",
        "phone" => "9999999999",
        "email" => "abc@email.com",
        "udf2" => "",
        "udf3" => "",
        "udf4" => "",
        "udf5" => "",
        "mandateSeqNo" => 3
    )),
    "hash" => "jbUS07Og8BToVZ"
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
| status | `Integer`<br/>Status of the request. `1` indicates success. | `1` |
| message | `String`<br/>Description of the response status. | `Transaction Processed successfully` |
| details | `Object`<br/>Object containing transaction details keyed by transaction reference. | See below |

### Details Object Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| authpayuid | `String`<br/>The authorization PayU ID for the mandate. | `999000000000826` |
| transactionid | `String`<br/>The transaction ID for this execution. | `SITXN03` |
| amount | `String`<br/>The amount debited. | `125.00` |
| payuid | `String`<br/>PayU's unique identifier for this transaction. | `999000000000828` |
| status | `String`<br/>Current status of the transaction. | `in progress` |
| field9 | `String`<br/>Transaction status code and message. | `92\|Transaction Initiated` |
| user_credentials | `String`<br/>User credentials if applicable. | ` ` |
| card_token | `String`<br/>Card token if applicable. | ` ` |
| udf1 | `String`<br/>User-defined field 1 value. | `null` |
| udf2 | `String`<br/>User-defined field 2 value. | ` ` |
| udf3 | `String`<br/>User-defined field 3 value. | ` ` |
| udf4 | `String`<br/>User-defined field 4 value. | `Executed` |
| udf5 | `String`<br/>User-defined field 5 value. | `999000000000826` |
| phone | `String`<br/>Customer phone number. | ` ` |
| email | `String`<br/>Customer email address. | ` ` |

## Sample Success Response

```json
{
    "status": 1,
    "message": "Transaction Processed successfully",
    "details": {
        "CLPOP-VNQKTR_2": {
            "authpayuid": "999000000000826",
            "transactionid": "SITXN03",
            "amount": "125.00",
            "user_credentials": "",
            "card_token": "",
            "payuid": "999000000000828",
            "status": "in progress",
            "udf1": null,
            "field9": "92|Transaction Initiated",
            "udf2": "",
            "udf3": "",
            "udf4": "Executed",
            "udf5": "999000000000826",
            "phone": "",
            "email": ""
        }
    }
}
```
