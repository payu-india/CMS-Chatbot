---
title: Page Structure (DO NOT PUBLISH)
deprecated: false
hidden: true
metadata:
  robots: index
---
## Step 1: Initiate the payment to PayU

<Accordion title="My Accordion Title" icon="fa-info-circle">
  Add the `Submit` button on your web page using the below checkout code.

```html
<html>
  <body>
  <form action='https://test.payu.in/_payment' method='post'>
  <input type="hidden" name="key" value="JP***g" />
  <input type="hidden" name="txnid" value="t6svtqtjRdl34W" />
  <input type="hidden" name="productinfo" value="iPhone" />
  <input type="hidden" name="amount" value="10" />
  <input type="hidden" name="email" value="test@gmail.com" />
  <input type="hidden" name="firstname" value="Ashish" />
  <input type="hidden" name="lastname" value="Kumar" />
  <input type="hidden" name="pg" value="TESTPG" />
  <input type="hidden" name="bankcode" value="TESTPGNB" />
  <input type="hidden" name="surl" value="your own success url" />
  <input type="hidden" name="furl" value="your own failure url" />
  <input type="hidden" name="phone" value="9988776655" />
  <input type="hidden" name="hash" value="eabec285da28fd0e3054d41a 4d24fe9f7599c9d0b6 6646f7a9984303fd6124044 b6206daf831e9a8bda28 a6200d318293a 13d6c193109b60bd 4b4f8b09c90972" />
  <input type="submit" value="submit"> </form>
  </body>
  </html>
```
```curl
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g" \
  -d "txnid=ewP8oRopzdHEtC" \
  -d "amount=10.00" \
  -d "firstname=Ashish" \
  -d "email=test@gmail.com" \
  -d "phone=9876543210" \
  -d "productinfo=iPhone" \
  -d "pg=TESTPG" \
  -d "bankcode=TESTPGNB" \
  -d "surl=https://apiplayground-response.herokuapp.com/" \
  -d "furl=https://apiplayground-response.herokuapp.com/" \
  -d "hash={{hash_value}}"
```
```javascript
/**
  * PayU Payment Request using Fetch API
  *
  * IMPORTANT: This should only be executed server-side, never in the browser, as it contains sensitive payment information.
  */
    
  // Payment endpoint
  const url = 'https://test.payu.in/_payment';

  // Form data parameters    
  const formData = new URLSearchParams();
  formData.append('key', 'JP***g');
  formData.append('txnid', 'ewP8oRopzdHEtC');
  formData.append('amount', '10.00');
  formData.append('firstname', 'Ashish');
  formData.append('email', 'test@gmail.com');
  formData.append('phone', '9876543210');
  formData.append('productinfo', 'iPhone');
  formData.append('pg', 'TESTPG');
  formData.append('bankcode', 'TESTPGNB');
  formData.append('surl', 'https://apiplayground-response.herokuapp.com/');
  formData.append('furl', 'https://apiplayground-response.herokuapp.com/');
  formData.append('hash', 'bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319');

  // Request options    
  const requestOptions = {
  method: 'POST',
  headers: {
    accept: 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
  },
  body: formData,
  };

  // Execute the request    
  fetch(url, requestOptions)
  .then((response) => {
    console.log('Status Code:', response.status);
    return response.text();
  })
  .then((data) => {
    console.log('Response:', data);
  })
  .catch((error) => {
    console.error('Error:', error);
  });
```
```python
import urllib.error
  import urllib.parse
  import urllib.request

  url = "https://test.payu.in/_payment"

  headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
  }

  payload = {
    "key": "JP***g",
    "txnid": "ewP8oRopzdHEtC",
    "amount": "10.00",
    "firstname": "Ashish",
    "email": "test@gmail.com",
    "phone": "9876543210",
    "productinfo": "iPhone",
    "pg": "TESTPG",
    "bankcode": "TESTPGNB",
    "surl": "https://apiplayground-response.herokuapp.com/",
    "furl": "https://apiplayground-response.herokuapp.com/",
    "hash": "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319",
  }

    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers=headers,
        method="POST",
    )

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode("utf-8")
            print("Status Code:", response.getcode())
            print("Response:")
            print(response_body)
            return body
    except urllib.error.HTTPError as e:
        print("Error:", e.code, e.reason)
        print(e.read().decode("utf-8"))
```
```php
<?php
  // PayU Payment Gateway API Request

  // Set the API endpoint
  $url = "https://test.payu.in/_payment";

  // Prepare the form data
  $postData = array(
      'key' => 'JP***g',
      'txnid' => 'ewP8oRopzdHEtC',
      'amount' => '10.00',
      'firstname' => 'Ashish',
      'email' => 'test@gmail.com',
      'phone' => '9876543210',
      'productinfo' => 'iPhone',
      'pg' => 'TESTPG',
      'bankcode' => 'TESTPGNB',
      'surl' => 'https://apiplayground-response.herokuapp.com/',
      'furl' => 'https://apiplayground-response.herokuapp.com/',
      'hash' => 'bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319'
  );

  // Initialize cURL session
  $ch = curl_init();

  // Set cURL options
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postData));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      'Accept: application/json',
      'Content-Type: application/x-www-form-urlencoded'
  ));

  // Optional: Disable SSL verification for testing (not recommended for production)
  // curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
  // curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);

  // Execute the request
  $response = curl_exec($ch);

  // Check for cURL errors
  if (curl_errno($ch)) {
      echo 'cURL Error: ' . curl_error($ch);
  } else {
      // Get HTTP status code
      $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
      echo "HTTP Status Code: " . $httpCode . "\n";
      echo "Response: " . $response . "\n";
  }

  // Close cURL session
  curl_close($ch);

  // Optional: Parse JSON response if needed
  $responseData = json_decode($response, true);
  if ($responseData !== null) {
      echo "Parsed Response:\n";
      print_r($responseData);
  }
  ?>
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

  public class PayUPaymentRequest {

      public static void main(String[] args) {
          try {
              // API endpoint
              String url = "https://test.payu.in/_payment";

              // Form parameters
              Map<String, String> params = new HashMap<>();
              params.put("key", "JP***g");
              params.put("txnid", "ewP8oRopzdHEtC");
              params.put("amount", "10.00");
              params.put("firstname", "Ashish");
              params.put("email", "test@gmail.com");
              params.put("phone", "9876543210");
              params.put("productinfo", "iPhone");
              params.put("pg", "TESTPG");
              params.put("bankcode", "TESTPGNB");
              params.put("surl", "https://apiplayground-response.herokuapp.com/");
              params.put("furl", "https://apiplayground-response.herokuapp.com/");
              params.put("hash", "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319");

              // Convert parameters to URL encoded form data
              StringJoiner sj = new StringJoiner("&");
              for (Map.Entry<String, String> entry : params.entrySet()) {
                  sj.add(URLEncoder.encode(entry.getKey(), "UTF-8") + "="
                       + URLEncoder.encode(entry.getValue(), "UTF-8"));
              }
              byte[] postData = sj.toString().getBytes(StandardCharsets.UTF_8);

              // Create connection
              URL apiUrl = new URL(url);
              HttpURLConnection conn = (HttpURLConnection) apiUrl.openConnection();
              conn.setRequestMethod("POST");
              conn.setRequestProperty("accept", "application/json");
              conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
              conn.setRequestProperty("Content-Length", String.valueOf(postData.length));
              conn.setDoOutput(true);

              // Send request
              try (DataOutputStream dos = new DataOutputStream(conn.getOutputStream())) {
                  dos.write(postData);
              }

              // Read response
              int responseCode = conn.getResponseCode();
              try (BufferedReader br = new BufferedReader(
                      new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8))) {
                  StringBuilder response = new StringBuilder();
                  String responseLine;
                  while ((responseLine = br.readLine()) != null) {
                      response.append(responseLine.trim());
                  }

                  System.out.println("Status Code: " + responseCode);
                  System.out.println("Response: " + response.toString());
              }

          } catch (Exception e) {
              e.printStackTrace();
          }
      }
  }
```

<br />

</Accordion>

 
