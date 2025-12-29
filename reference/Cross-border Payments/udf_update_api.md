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

## Request Header Parameters

| Parameter                      | Description                                                                     | Example                                                                               |
| ------------------------------ | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| date<br />`mandatory`          | `String`<br />Current date in RFC 2616 format (UTC).                            | `Sat, 13 Sep 2025 12:04:53 GMT`                                                       |
| digest<br />`mandatory`        | `String`<br />Base64 encoded SHA256 digest of the request body.                 | `TqXFCKZWbnYkBUP4/rBv1Fd3e+OVScQBZDav2mXSMw4=`                                        |
| authorization<br />`mandatory` | `String`<br />HMAC SHA512 authorization header containing merchant credentials. | `hmac username="PRiQvJ", algorithm="sha512", headers="date", signature="<signature>"` |
| Content-Type<br />`mandatory`  | `String`<br />Content type of the request.                                      | `application/json`                                                                    |

## Request Body Parameters

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
        `String`<br />New value for UDF7.
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
--header 'date: Sat, 13 Sep 2025 12:04:53 GMT' \
--header 'digest: TqXFCKZWbnYkBUP4/rBv1Fd3e+OVScQBZDav2mXSMw4=' \
--header 'authorization: hmac username="PRiQvJ", algorithm="sha512", headers="date", signature="65178bc488a7cd9cc631b722c6f37f439cd3ac9f2c9c018b30d9338d7a3d1fc6c518a316ad7d67becc2834473ecf125c730522ad04e62618b04a22e16acee33a"' \
--header 'Content-Type: application/json' \
--form 'key="smsplus"' \
--form 'hash="17285990acb0dc4e64c23e7097575a39dc4fdb6d8162ea8d8c1b40a06c055c7fc6f2c6f25864010ced75417b249a576b54c17c805a4f1a4d8f5657878334f25b"' \
--form 'command="udf_update"' \
--form 'var1="c82847d52a146dca3830"' \
--form 'var2="updatedudf2_again"' \
--form 'var3="fsdfdsfd"' \
--form 'var4="fdsfdsfdsfds"' \
--form 'var5="fdsfsdf"' \
--form 'var7="fweew"'
```
```python
import requests

url = "https://info.payu.in/merchant/postservice.php?form=2"

headers = {
    "date": "Sat, 13 Sep 2025 12:04:53 GMT",
    "digest": "TqXFCKZWbnYkBUP4/rBv1Fd3e+OVScQBZDav2mXSMw4=",
    "authorization": 'hmac username="PRiQvJ", algorithm="sha512", headers="date", signature="65178bc488a7cd9cc631b722c6f37f439cd3ac9f2c9c018b30d9338d7a3d1fc6c518a316ad7d67becc2834473ecf125c730522ad04e62618b04a22e16acee33a"',
    "Content-Type": "application/json"
}

data = {
    "key": "smsplus",
    "hash": "17285990acb0dc4e64c23e7097575a39dc4fdb6d8162ea8d8c1b40a06c055c7fc6f2c6f25864010ced75417b249a576b54c17c805a4f1a4d8f5657878334f25b",
    "command": "udf_update",
    "var1": "c82847d52a146dca3830",
    "var2": "updatedudf2_again",
    "var3": "fsdfdsfd",
    "var4": "fdsfdsfdsfds",
    "var5": "fdsfsdf",
    "var7": "fweew"
}

response = requests.post(url, headers=headers, data=data)
print(response.json())
```
```csharp
using System;
using System.Net.Http;
using System.Threading.Tasks;
using System.Collections.Generic;

class Program
{
    static async Task Main()
    {
        using (HttpClient client = new HttpClient())
        {
            client.DefaultRequestHeaders.Add("date", "Sat, 13 Sep 2025 12:04:53 GMT");
            client.DefaultRequestHeaders.Add("digest", "TqXFCKZWbnYkBUP4/rBv1Fd3e+OVScQBZDav2mXSMw4=");
            client.DefaultRequestHeaders.Add("authorization", "hmac username=\"PRiQvJ\", algorithm=\"sha512\", headers=\"date\", signature=\"65178bc488a7cd9cc631b722c6f37f439cd3ac9f2c9c018b30d9338d7a3d1fc6c518a316ad7d67becc2834473ecf125c730522ad04e62618b04a22e16acee33a\"");

            var formData = new FormUrlEncodedContent(new[]
            {
                new KeyValuePair<string, string>("key", "smsplus"),
                new KeyValuePair<string, string>("hash", "17285990acb0dc4e64c23e7097575a39dc4fdb6d8162ea8d8c1b40a06c055c7fc6f2c6f25864010ced75417b249a576b54c17c805a4f1a4d8f5657878334f25b"),
                new KeyValuePair<string, string>("command", "udf_update"),
                new KeyValuePair<string, string>("var1", "c82847d52a146dca3830"),
                new KeyValuePair<string, string>("var2", "updatedudf2_again"),
                new KeyValuePair<string, string>("var3", "fsdfdsfd"),
                new KeyValuePair<string, string>("var4", "fdsfdsfdsfds"),
                new KeyValuePair<string, string>("var5", "fdsfsdf"),
                new KeyValuePair<string, string>("var7", "fweew")
            });

            string url = "https://info.payu.in/merchant/postservice.php?form=2";
            HttpResponseMessage response = await client.PostAsync(url, formData);
            string responseBody = await response.Content.ReadAsStringAsync();
            Console.WriteLine(responseBody);
        }
    }
}
```
```javascript
const updateUdf = async () => {
    const url = 'https://info.payu.in/merchant/postservice.php?form=2';

    const formData = new FormData();
    formData.append('key', 'smsplus');
    formData.append('hash', '17285990acb0dc4e64c23e7097575a39dc4fdb6d8162ea8d8c1b40a06c055c7fc6f2c6f25864010ced75417b249a576b54c17c805a4f1a4d8f5657878334f25b');
    formData.append('command', 'udf_update');
    formData.append('var1', 'c82847d52a146dca3830');
    formData.append('var2', 'updatedudf2_again');
    formData.append('var3', 'fsdfdsfd');
    formData.append('var4', 'fdsfdsfdsfds');
    formData.append('var5', 'fdsfsdf');
    formData.append('var7', 'fweew');

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'date': 'Sat, 13 Sep 2025 12:04:53 GMT',
            'digest': 'TqXFCKZWbnYkBUP4/rBv1Fd3e+OVScQBZDav2mXSMw4=',
            'authorization': 'hmac username="PRiQvJ", algorithm="sha512", headers="date", signature="65178bc488a7cd9cc631b722c6f37f439cd3ac9f2c9c018b30d9338d7a3d1fc6c518a316ad7d67becc2834473ecf125c730522ad04e62618b04a22e16acee33a"'
        },
        body: formData
    });

    const data = await response.json();
    console.log(data);
};

updateUdf();
```
```java
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;
import java.util.StringJoiner;

public class UdfUpdate {
    public static void main(String[] args) throws Exception {
        String url = "https://info.payu.in/merchant/postservice.php?form=2";

        URL obj = new URL(url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();
        con.setRequestMethod("POST");
        con.setRequestProperty("date", "Sat, 13 Sep 2025 12:04:53 GMT");
        con.setRequestProperty("digest", "TqXFCKZWbnYkBUP4/rBv1Fd3e+OVScQBZDav2mXSMw4=");
        con.setRequestProperty("authorization", "hmac username=\"PRiQvJ\", algorithm=\"sha512\", headers=\"date\", signature=\"65178bc488a7cd9cc631b722c6f37f439cd3ac9f2c9c018b30d9338d7a3d1fc6c518a316ad7d67becc2834473ecf125c730522ad04e62618b04a22e16acee33a\"");
        con.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");

        Map<String, String> params = new HashMap<>();
        params.put("key", "smsplus");
        params.put("hash", "17285990acb0dc4e64c23e7097575a39dc4fdb6d8162ea8d8c1b40a06c055c7fc6f2c6f25864010ced75417b249a576b54c17c805a4f1a4d8f5657878334f25b");
        params.put("command", "udf_update");
        params.put("var1", "c82847d52a146dca3830");
        params.put("var2", "updatedudf2_again");
        params.put("var3", "fsdfdsfd");
        params.put("var4", "fdsfdsfdsfds");
        params.put("var5", "fdsfsdf");
        params.put("var7", "fweew");

        StringJoiner sj = new StringJoiner("&");
        for (Map.Entry<String, String> entry : params.entrySet()) {
            sj.add(URLEncoder.encode(entry.getKey(), "UTF-8") + "=" + URLEncoder.encode(entry.getValue(), "UTF-8"));
        }

        con.setDoOutput(true);
        try (DataOutputStream wr = new DataOutputStream(con.getOutputStream())) {
            wr.writeBytes(sj.toString());
        }

        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuilder response = new StringBuilder();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        System.out.println(response.toString());
    }
}
```
```php
<?php
$curl = curl_init();

$postFields = [
    'key' => 'smsplus',
    'hash' => '17285990acb0dc4e64c23e7097575a39dc4fdb6d8162ea8d8c1b40a06c055c7fc6f2c6f25864010ced75417b249a576b54c17c805a4f1a4d8f5657878334f25b',
    'command' => 'udf_update',
    'var1' => 'c82847d52a146dca3830',
    'var2' => 'updatedudf2_again',
    'var3' => 'fsdfdsfd',
    'var4' => 'fdsfdsfdsfds',
    'var5' => 'fdsfsdf',
    'var7' => 'fweew'
];

curl_setopt_array($curl, [
    CURLOPT_URL => 'https://info.payu.in/merchant/postservice.php?form=2',
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => $postFields,
    CURLOPT_HTTPHEADER => [
        'date: Sat, 13 Sep 2025 12:04:53 GMT',
        'digest: TqXFCKZWbnYkBUP4/rBv1Fd3e+OVScQBZDav2mXSMw4=',
        'authorization: hmac username="PRiQvJ", algorithm="sha512", headers="date", signature="65178bc488a7cd9cc631b722c6f37f439cd3ac9f2c9c018b30d9338d7a3d1fc6c518a316ad7d67becc2834473ecf125c730522ad04e62618b04a22e16acee33a"',
        'Content-Type: application/json'
    ],
]);

$response = curl_exec($curl);
curl_close($curl);

echo $response;
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
    "udf3": "fdsfdsfdsfds",
    "udf4": "fdsfsdf",
    "udf1": "updatedudf2_again",
    "udf2": "fsdfdsfd",
    "status": "UDF values updated",
    "udf7": "fweew"
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
