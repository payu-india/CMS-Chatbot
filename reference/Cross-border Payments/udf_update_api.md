---
title: UDF Update API
deprecated: false
hidden: false
metadata:
  robots: index
---
The UDF Update API allows you to update User Defined Fields (UDF1-UDF7 and additional UDFs if enabled) for a completed transaction.

## Use Cases

* Update customer-related metadata after transaction completion
* Add invoice or order details to transaction records
* Store additional business-specific information against transactions

<Callout icon="📘" theme="info">
  **Note:** To update udf6 and udf7, the additional UDFs` merchant parameter must be enabled for your MID. To enable additional UDFs, contact your PayU Key Account Manager or <Anchor label="PayU Support" target="_blank" href="https://help.payu.in">PayU Support</Anchor>.
</Callout>

## Environment

| Environment | URL                                                       |
| ----------- | --------------------------------------------------------- |
| Test        | `https://pp1info.payu.in/merchant/postservice.php?form=2` |
| Production  | `https://info.payu.in/merchant/postservice.php?form=2`    |

## Request Parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key<br />`mandatory`
      </td>

      <td>
        `String`<br />Merchant key provided by PayU.
      </td>

      <td>
        `smsplus`
      </td>
    </tr>

    <tr>
      <td>
        hash<br />`mandatory`
      </td>

      <td>
        `String`<br />SHA512 hash for request verification.
      </td>

      <td>
        `17285990acb0dc4e64c23e7097575a39dc4fdb6d8162ea8d8c1b40a06c055c7fc6f2c6f25864010ced75417b249a576b54c17c805a4f1a4d8f5657878334f25b`
      </td>
    </tr>

    <tr>
      <td>
        command<br />`mandatory`
      </td>

      <td>
        `String`<br />API command identifier. Must be `udf_update`.
      </td>

      <td>
        `udf_update`
      </td>
    </tr>

    <tr>
      <td>
        var1<br />`mandatory`
      </td>

      <td>
        `String`<br />Transaction ID (txnid) of the transaction to update.
      </td>

      <td>
        `my_order_642`
      </td>
    </tr>

    <tr>
      <td>
        var2<br />`optional`
      </td>

      <td>
        `String`<br />New value for UDF1. Contains the buyer's PAN. <br />For UPI recurring, format is "Buyer's PAN||Buyer's DOB". Character limit: 255.
      </td>

      <td>
        AAAPZ1234C  
        For UPI: `AAAPZ1234C||22-08-1972`
      </td>
    </tr>

    <tr>
      <td>
        var4<br />`optional`
      </td>

      <td>
        `String`<br />New value for UDF3.This parameter must contains the Buyer's DOB. <br />For UPI recurring, format is "InvoiceID||MerchantName". Character limit: 255.
      </td>

      <td>
        22-08-1972  
        For UPI: `inv435345|Ashish`
      </td>
    </tr>

    <tr>
      <td>
        var5<br />`optional`
      </td>

      <td>
        `String`<br />New value for UDF2.
      </td>

      <td>
        ``
      </td>
    </tr>

    <tr>
      <td>
        var6<br />`optional`
      </td>

      <td>
        `String`<br />New value for UDF5.
      </td>

      <td>
        `udf5value`
      </td>
    </tr>

    <tr>
      <td>
        var7<br />`optional`
      </td>

      <td>
        `String`<br />New value for UDF6.
      </td>

      <td>
        `fweew`
      </td>
    </tr>

    <tr>
      <td>
        var8<br />`optional`
      </td>

      <td>
        `String`<br />New value for UDF7. This must include the IEC (Importer-Exporter Code).
      </td>

      <td>
        `0100000029`
      </td>
    </tr>
  </tbody>
</Table>

## Hash Generation

The hash is generated using the following formula:

```
hash = sha512(key|command|var1|salt)
```

## Sample Request

```bash
curl --location 'https://info.payu.in/merchant/postservice.php?form=2' \
--header 'Content-Type: application/json' \
--form 'key="smsplus"' \
--form 'hash="17285990acb0dc4e64c23e7097575a39dc4fdb6d8162ea8d8c1b40a06c055c7fc6f2c6f25864010ced75417b249a576b54c17c805a4f1a4d8f5657878334f25b"' \
--form 'command="udf_update"' \
--form 'var1="my_order_642"' \
--form 'var2="AAAPZ1234C"' \
--form 'var4="22-08-1972"' \
--form 'var5=""' \
--form 'var6="udf5value"' \
--form 'var7="fweew"' \
--form 'var8="0100000029"'
```
```python
import requests

url = "https://info.payu.in/merchant/postservice.php?form=2"

headers = {
    'date': 'Sat, 13 Sep 2025 12:04:53 GMT',
    'digest': 'TqXFCKZWbnYkBUP4/rBv1Fd3e+OVScQBZDav2mXSMw4=',
    'authorization': 'hmac username="PRiQvJ", algorithm="sha512", headers="date", signature="65178bc488a7cd9cc631b722c6f37f439cd3ac9f2c9c018b30d9338d7a3d1fc6c518a316ad7d67becc2834473ecf125c730522ad04e62618b04a22e16acee33a"',
    'Content-Type': 'application/json'
}

data = {
    'key': 'smsplus',
    'hash': '17285990acb0dc4e64c23e7097575a39dc4fdb6d8162ea8d8c1b40a06c055c7fc6f2c6f25864010ced75417b249a576b54c17c805a4f1a4d8f5657878334f25b',
    'command': 'udf_update',
    'var1': 'my_order_642',
    'var2': 'AAAPZ1234C',
    'var4': '22-08-1972',
    'var5': '',
    'var6': 'udf5value',
    'var7': 'fweew',
    'var8': '0100000029'
}

try:
    response = requests.post(url, headers=headers, data=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        var client = new HttpClient();
        var url = "https://info.payu.in/merchant/postservice.php?form=2";
        
        var formData = new List<KeyValuePair<string, string>>
        {
            new KeyValuePair<string, string>("key", "smsplus"),
            new KeyValuePair<string, string>("hash", "17285990acb0dc4e64c23e7097575a39dc4fdb6d8162ea8d8c1b40a06c055c7fc6f2c6f25864010ced75417b249a576b54c17c805a4f1a4d8f5657878334f25b"),
            new KeyValuePair<string, string>("command", "udf_update"),
            new KeyValuePair<string, string>("var1", "my_order_642"),
            new KeyValuePair<string, string>("var2", "AAAPZ1234C"),
            new KeyValuePair<string, string>("var4", "22-08-1972"),
            new KeyValuePair<string, string>("var5", ""),
            new KeyValuePair<string, string>("var6", "udf5value"),
            new KeyValuePair<string, string>("var7", "fweew"),
            new KeyValuePair<string, string>("var8", "0100000029")
        };

        var formContent = new FormUrlEncodedContent(formData);
        
        client.DefaultRequestHeaders.Add("date", "Sat, 13 Sep 2025 12:04:53 GMT");
        client.DefaultRequestHeaders.Add("digest", "TqXFCKZWbnYkBUP4/rBv1Fd3e+OVScQBZDav2mXSMw4=");
        client.DefaultRequestHeaders.Add("authorization", "hmac username=\"PRiQvJ\", algorithm=\"sha512\", headers=\"date\", signature=\"65178bc488a7cd9cc631b722c6f37f439cd3ac9f2c9c018b30d9338d7a3d1fc6c518a316ad7d67becc2834473ecf125c730522ad04e62618b04a22e16acee33a\"");

        try
        {
            var response = await client.PostAsync(url, formContent);
            var responseContent = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response: {responseContent}");
        }
        catch (HttpRequestException e)
        {
            Console.WriteLine($"Request failed: {e.Message}");
        }
        finally
        {
            client.Dispose();
        }
    }
}
```
```javascript
async function updateUdf() {
    const url = "https://info.payu.in/merchant/postservice.php?form=2";
    
    const formData = new FormData();
    formData.append('key', 'smsplus');
    formData.append('hash', '17285990acb0dc4e64c23e7097575a39dc4fdb6d8162ea8d8c1b40a06c055c7fc6f2c6f25864010ced75417b249a576b54c17c805a4f1a4d8f5657878334f25b');
    formData.append('command', 'udf_update');
    formData.append('var1', 'my_order_642');
    formData.append('var2', 'AAAPZ1234C');
    formData.append('var4', '22-08-1972');
    formData.append('var5', '');
    formData.append('var6', 'udf5value');
    formData.append('var7', 'fweew');
    formData.append('var8', '0100000029');

    const headers = {
        'date': 'Sat, 13 Sep 2025 12:04:53 GMT',
        'digest': 'TqXFCKZWbnYkBUP4/rBv1Fd3e+OVScQBZDav2mXSMw4=',
        'authorization': 'hmac username="PRiQvJ", algorithm="sha512", headers="date", signature="65178bc488a7cd9cc631b722c6f37f439cd3ac9f2c9c018b30d9338d7a3d1fc6c518a316ad7d67becc2834473ecf125c730522ad04e62618b04a22e16acee33a"'
    };

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: headers,
            body: formData
        });
        
        const responseText = await response.text();
        console.log(`Status Code: ${response.status}`);
        console.log(`Response: ${responseText}`);
    } catch (error) {
        console.error(`Request failed: ${error.message}`);
    }
}

updateUdf();
```
```java
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;

public class PayUUdfUpdate {
    public static void main(String[] args) {
        try {
            URL url = new URL("https://info.payu.in/merchant/postservice.php?form=2");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            
            connection.setRequestMethod("POST");
            connection.setRequestProperty("date", "Sat, 13 Sep 2025 12:04:53 GMT");
            connection.setRequestProperty("digest", "TqXFCKZWbnYkBUP4/rBv1Fd3e+OVScQBZDav2mXSMw4=");
            connection.setRequestProperty("authorization", "hmac username=\"PRiQvJ\", algorithm=\"sha512\", headers=\"date\", signature=\"65178bc488a7cd9cc631b722c6f37f439cd3ac9f2c9c018b30d9338d7a3d1fc6c518a316ad7d67becc2834473ecf125c730522ad04e62618b04a22e16acee33a\"");
            connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
            connection.setDoOutput(true);
            
            String formData = "key=smsplus" +
                "&hash=17285990acb0dc4e64c23e7097575a39dc4fdb6d8162ea8d8c1b40a06c055c7fc6f2c6f25864010ced75417b249a576b54c17c805a4f1a4d8f5657878334f25b" +
                "&command=udf_update" +
                "&var1=my_order_642" +
                "&var2=AAAPZ1234C" +
                "&var4=22-08-1972" +
                "&var5=" +
                "&var6=udf5value" +
                "&var7=fweew" +
                "&var8=0100000029";
            
            try (DataOutputStream outputStream = new DataOutputStream(connection.getOutputStream())) {
                outputStream.write(formData.getBytes(StandardCharsets.UTF_8));
            }
            
            int responseCode = connection.getResponseCode();
            System.out.println("Status Code: " + responseCode);
            
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(
                    responseCode >= 200 && responseCode < 300 ? 
                    connection.getInputStream() : connection.getErrorStream()))) {
                
                StringBuilder response = new StringBuilder();
                String line;
                while ((line = reader.readLine()) != null) {
                    response.append(line).append("\n");
                }
                System.out.println("Response: " + response.toString());
            }
            
        } catch (Exception e) {
            System.err.println("Request failed: " + e.getMessage());
        }
    }
}
```
```php
<?php
$url = "https://info.payu.in/merchant/postservice.php?form=2";

$data = [
    'key' => 'smsplus',
    'hash' => '17285990acb0dc4e64c23e7097575a39dc4fdb6d8162ea8d8c1b40a06c055c7fc6f2c6f25864010ced75417b249a576b54c17c805a4f1a4d8f5657878334f25b',
    'command' => 'udf_update',
    'var1' => 'my_order_642',
    'var2' => 'AAAPZ1234C',
    'var4' => '22-08-1972',
    'var5' => '',
    'var6' => 'udf5value',
    'var7' => 'fweew',
    'var8' => '0100000029'
];

$headers = [
    'date: Sat, 13 Sep 2025 12:04:53 GMT',
    'digest: TqXFCKZWbnYkBUP4/rBv1Fd3e+OVScQBZDav2mXSMw4=',
    'authorization: hmac username="PRiQvJ", algorithm="sha512", headers="date", signature="65178bc488a7cd9cc631b722c6f37f439cd3ac9f2c9c018b30d9338d7a3d1fc6c518a316ad7d67becc2834473ecf125c730522ad04e62618b04a22e16acee33a"',
    'Content-Type: application/x-www-form-urlencoded'
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

if (curl_errno($ch)) {
    echo "Request failed: " . curl_error($ch);
} else {
    echo "Status Code: " . $httpCode . "\n";
    echo "Response: " . $response . "\n";
}

curl_close($ch);
?>
```

## Response Parameters

| Parameter      | Description                                                          | Example                                |
| -------------- | -------------------------------------------------------------------- | -------------------------------------- |
| transaction_id | `String`<br />Transaction ID that was updated.                       | `c82847d52a146dca3830`                 |
| status         | `String`<br />Status message indicating success or failure.          | `UDF values updated`                   |
| udf1           | `String`<br />Updated value of UDF1.                                 | `updatedudf2_again`                    |
| udf2           | `String`<br />Updated value of UDF2.                                 | `fsdfdsfd`                             |
| udf3           | `String`<br />Updated value of UDF3.                                 | `fdsfdsfdsfds`                         |
| udf4           | `String`<br />Updated value of UDF4.                                 | `fdsfsdf`                              |
| udf5           | `String`<br />Updated value of UDF5.                                 | ``                                     |
| udf6           | `String`<br />Updated value of UDF6 (if AdditionalNoOfUDFs enabled). | `fweew`                                |
| udf7           | `String`<br />Updated value of UDF7 (if AdditionalNoOfUDFs enabled). | `dfweewd`                              |
| msg            | `String`<br />Error message returned on failure.                     | `Update not allowed on provided Field` |

## Sample Responses

### Success Response

When UDF values are updated successfully:

```json
{
    "transaction_id": "c82847d52a146dca3830",
    "udf5": "",
    "udf3": "22-08-1972",
    "udf4": "XYZ Pvt. Ltd.",
    "udf1": "AAAPZ1234C",
    "udf2": "fsdfdsfd",
    "status": "UDF values updated",
    "udf7": "0100000029"
}
```

### Failure scenarios

#### Update Not Allowed

When attempting to update a field that is not permitted:

```json
{
    "status": "0",
    "msg": "Update not allowed on provided Field"
}
```

#### No Data Found

When the transaction ID does not exist:

```json
{
    "status": "0",
    "msg": "No Data Found for txnid: 3424"
}
```

#### Merchant Inactive

When the merchant is not authorized:

```json
{
    "msg": "Merchant is not authorized to use PayU API",
    "status": 0
}
```

## Important Notes

1. **AdditionalNoOfUDFs Parameter**: To update UDF6 and beyond, ensure the `AdditionalNoOfUDFs` merchant parameter is enabled for your MID. Contact PayU support to enable this feature.

2. **Standard UDF Updates**: UDF1-UDF5 can be updated without any additional configuration.

3. **Field Restrictions**: Some fields may be restricted from updates based on your merchant configuration. If you receive "Update not allowed on provided Field" error, contact PayU support.

4. **Transaction Existence**: Ensure the transaction ID (var1) exists in the system before attempting to update UDF values.
