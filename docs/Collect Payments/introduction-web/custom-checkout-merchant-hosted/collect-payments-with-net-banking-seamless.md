---
title: Net Banking Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
---
title: Net Banking Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Collect payments using Net Banking with Merchant Hosted Checkout integration as described in this section. After collecting the details from the customer, make the transaction request with the payment details to PayU.

<Callout icon="👍" theme="okay">
  ###

  Experience the end-to-end **Merchant Hosted Checkout** > **Net Banking** flow and instantly generate the complete code for seamless, zero-coding integration into your website. <br />

  <HTMLBlock>{`
                  <style>
                  .tooltip-btn {
                      position: relative;
                      background-color: #4CAF50;
                      color: white;
                      padding: 10px 20px;
                      border: none;
                      border-radius: 5px;
                      cursor: pointer;
                      font-weight: bold;
                  }
                  .tooltip-btn:hover::after {
                      content: attr(data-tooltip);
                      position: absolute;
                      bottom: 125%;
                      left: 50%;
                      transform: translateX(-50%);
                      background-color: #333;
                      color: white;
                      padding: 5px 10px;
                      border-radius: 4px;
                      white-space: nowrap;
                      font-size: 12px;
                      z-index: 1;
                  }
                  </style>
                  <button onclick="window.open('https://payu.in/integrationlab/seamless/sm-nb-status', '_blank')"
                          class="tooltip-btn"
                          data-tooltip="Click here to see the Merchant Hosted Checkout > Net Banking end-to-end integration and instantly generate the complete code needed for a zero-coding setup on your website.">
                      Experience the flow and get the code
                  </button>
  `}</HTMLBlock>
</Callout>

<br />

## Steps to Integrate

Below are the integration steps:

<Cards>
  <Card title="1. Initiate the Payment to PayU" href="https://docs.payu.in/docs/collect-payments-with-net-banking-seamless#step-1-initiate-the-payment-to-payu">
    Initiate the payment to PayU with pg=NEFT and bankcode=\<based on bank>
  </Card>

  <Card title="2. Check the Response" href="https://docs.payu.in/docs/collect-payments-with-net-banking-seamless#step-2-check-response-from-payu">
    Check the response from PayU
  </Card>

  <Card title="3. Verify the Payment" href="https://docs.payu.in/docs/collect-payments-with-net-banking-seamless#step-3-verify-the-payment">
    Verify the payment using verify\_payment and monitor using webhooks
  </Card>
</Cards>

<RegisterMerchantPrerequiste />

<Callout icon="📮" theme="default">
  ###

  **Postman Collection**: Access the **Merchant Hosted Checkout >. Net Banking Postman Collection** from the following location:

  [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/folder/6uqfq01/net-banking-integration](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/folder/6uqfq01/net-banking-integration)
</Callout>

## Step 1: Initiate the payment to PayU

<Accordion title="Post request syntax & composition" icon="fa-code">
  Add the `Submit` button on your web page using the below checkout code.<br />

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
  <input type="hidden" name="hash" value="eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972" />
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
  const url = 'https://test.payu.in/_payment';
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
  const requestOptions = {
    method: 'POST',
    headers: { accept: 'application/json', 'Content-Type': 'application/x-www-form-urlencoded' },
    body: formData,
  };
  fetch(url, requestOptions)
    .then((response) => { console.log('Status Code:', response.status); return response.text(); })
    .then((data) => { console.log('Response:', data); })
    .catch((error) => { console.error('Error:', error); });
  ```
  ```python
  import urllib.request
  import urllib.parse

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
  req = urllib.request.Request(url, data=data, headers=headers, method="POST")
  with urllib.request.urlopen(req) as response:
    body = response.read().decode("utf-8")
    print("Status Code:", response.getcode())
    print("Response:", body)
  ```
  ```php
  <?php
  $url = "https://test.payu.in/_payment";
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
  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postData));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      'Accept: application/json',
      'Content-Type: application/x-www-form-urlencoded'
  ));
  $response = curl_exec($ch);
  $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
  curl_close($ch);
  echo "HTTP Status Code: " . $httpCode . "\n";
  echo "Response: " . $response . "\n";
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
              String url = "https://test.payu.in/_payment";
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
              StringJoiner sj = new StringJoiner("&");
              for (Map.Entry<String, String> entry : params.entrySet())
                  sj.add(URLEncoder.encode(entry.getKey(), "UTF-8") + "=" + URLEncoder.encode(entry.getValue(), "UTF-8"));
              byte[] postData = sj.toString().getBytes(StandardCharsets.UTF_8);
              URL apiUrl = new URL(url);
              HttpURLConnection conn = (HttpURLConnection) apiUrl.openConnection();
              conn.setRequestMethod("POST");
              conn.setRequestProperty("accept", "application/json");
              conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
              conn.setDoOutput(true);
              try (DataOutputStream dos = new DataOutputStream(conn.getOutputStream())) { dos.write(postData); }
              int responseCode = conn.getResponseCode();
              try (BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8))) {
                  StringBuilder response = new StringBuilder();
                  String responseLine;
                  while ((responseLine = br.readLine()) != null) response.append(responseLine.trim());
                  System.out.println("Status Code: " + responseCode);
                  System.out.println("Response: " + response.toString());
              }
          } catch (Exception e) { e.printStackTrace(); }
      }
  }
  ```

  <Callout icon="📘" theme="info">
    **Note:** The above codes are for testing the Merchant Hosted Checkout integration with net banking as a payment method.
  </Callout>
</Accordion>

<PaymentAPIEnvironment />

The pg and bankcode parameters vary for the NetBanking payment mode in the **Collect Payment** API (**\_payment** API).

<Tabs>
  <Tab title="Request Parameters">

**Mandatory Parameters**

<table>
<thead>
<tr><th>Parameter</th><th>Description</th><th>Example</th></tr>
</thead>
<tbody>
<tr><td><Glossary>key</Glossary></td><td><code>String</code> Merchant key provided by PayU during onboarding.</td><td>JP***g</td></tr>
<tr><td><Glossary>txnid</Glossary></td><td><code>String</code> The transaction ID is a reference number for a specific order that is generated by the merchant.</td><td>ypl938459435</td></tr>
<tr><td>amount</td><td><code>String</code> The payment amount for the transaction.</td><td>10.00</td></tr>
<tr><td><Glossary>productinfo</Glossary></td><td><code>String</code> A brief description of the product.</td><td>iPhone</td></tr>
<tr><td>firstname</td><td><code>String</code> The first name of the customer.</td><td>Ashish</td></tr>
<tr><td>email</td><td><code>String</code> The email address of the customer.</td><td>abc@payu.in</td></tr>
<tr><td>phone</td><td><code>String</code> The phone number of the customer.</td><td>9876543210</td></tr>
<tr><td><Glossary>pg</Glossary></td><td><code>String</code> This parameter defined the payment gateway. For NetBanking, pg=<Glossary>NB</Glossary>.</td><td>TESTPG</td></tr>
<tr><td><Glossary>bankcode</Glossary></td><td><code>String</code> Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. For the list of bank codes, refer to <a href="https://docs.payu.in/docs/net-banking-codes">Net Banking Codes</a>. For test Net Banking credentials, refer to <a href="https://docs.payu.in/docs/test-cards-upi-id-and-wallets">Test Cards, UPI ID and Wallets</a>.</td><td>TESTPGNB</td></tr>
<tr><td><Glossary>furl</Glossary></td><td><code>String</code> The success URL, which is the page PayU will redirect to if the transaction is successful.</td><td>https://merchant.com/success</td></tr>
<tr><td><Glossary>surl</Glossary></td><td><code>String</code> The Failure URL, which is the page PayU will redirect to if the transaction is failed.</td><td>https://merchant.com/failure</td></tr>
<tr><td><Glossary>hash</Glossary></td><td><code>String</code> It is the hash calculated by the merchant. The hash calculation logic is: <Glossary>SHA-512</Glossary>(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|<Glossary>Salt</Glossary>)</td><td>calculated_hash_value</td></tr>
</tbody>
</table>

**Optional Parameters**

<table>
<thead>
<tr><th>Parameter</th><th>Description</th><th>Example</th></tr>
</thead>
<tbody>
<tr><td>address1</td><td><code>String</code> The first line of the billing address. For <Glossary>Fraud Detection</Glossary>: This information is helpful when it comes to issues related to fraud detection and chargebacks.</td><td>123 Main Street</td></tr>
<tr><td>address2</td><td><code>String</code> The second line of the billing address.</td><td>Apt 456</td></tr>
<tr><td>city</td><td><code>String</code> The city where your customer resides as part of the billing address.</td><td>Mumbai</td></tr>
<tr><td>state</td><td><code>String</code> The state where your customer resides as part of the billing address.</td><td>Maharashtra</td></tr>
<tr><td>country</td><td><code>String</code> The country where your customer resides.</td><td>India</td></tr>
<tr><td>zipcode</td><td><code>String</code> Billing address zip code is mandatory for the cardless <Glossary>EMI</Glossary> option. <code>Character Limit</code>: 20</td><td>400001</td></tr>
<tr><td>udf1</td><td><code>String</code> <Glossary>User Defined Field</Glossary>s (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.</td><td>custom_value_1</td></tr>
<tr><td>udf2</td><td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.</td><td>custom_value_2</td></tr>
<tr><td>udf3</td><td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td><td>custom_value_3</td></tr>
<tr><td>udf4</td><td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td><td>custom_value_4</td></tr>
<tr><td>udf5</td><td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td><td>custom_value_5</td></tr>
</tbody>
</table>

  <Accordion title="Understanding Hashing and sample code" icon="fa-code">
    <HashingRequestParameters />

    #### Hashing Sample Code

    <HashingSample />
  </Accordion>

  </Tab>

  <Tab title="Sample Request">

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
const url = 'https://test.payu.in/_payment';
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
fetch(url, { method: 'POST', headers: { accept: 'application/json', 'Content-Type': 'application/x-www-form-urlencoded' }, body: formData })
  .then(r => { console.log('Status:', r.status); return r.text(); })
  .then(d => console.log('Response:', d))
  .catch(e => console.error('Error:', e));
```
```python
import urllib.request
import urllib.parse
url = "https://test.payu.in/_payment"
payload = {
    "key": "JP***g", "txnid": "ewP8oRopzdHEtC", "amount": "10.00",
    "firstname": "Ashish", "email": "test@gmail.com", "phone": "9876543210",
    "productinfo": "iPhone", "pg": "TESTPG", "bankcode": "TESTPGNB",
    "surl": "https://apiplayground-response.herokuapp.com/",
    "furl": "https://apiplayground-response.herokuapp.com/",
    "hash": "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"
}
data = urllib.parse.urlencode(payload).encode("utf-8")
req = urllib.request.Request(url, data=data, headers={"accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}, method="POST")
with urllib.request.urlopen(req) as response:
    print("Status Code:", response.getcode())
    print("Response:", response.read().decode("utf-8"))
```
```php
<?php
$url = "https://test.payu.in/_payment";
$postData = array(
    'key' => 'JP***g', 'txnid' => 'ewP8oRopzdHEtC', 'amount' => '10.00',
    'firstname' => 'Ashish', 'email' => 'test@gmail.com', 'phone' => '9876543210',
    'productinfo' => 'iPhone', 'pg' => 'TESTPG', 'bankcode' => 'TESTPGNB',
    'surl' => 'https://apiplayground-response.herokuapp.com/',
    'furl' => 'https://apiplayground-response.herokuapp.com/',
    'hash' => 'bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319'
);
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postData));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Accept: application/json', 'Content-Type: application/x-www-form-urlencoded'));
$response = curl_exec($ch);
echo "HTTP Status: " . curl_getinfo($ch, CURLINFO_HTTP_CODE) . "\n";
echo "Response: " . $response . "\n";
curl_close($ch);
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
    public static void main(String[] args) throws Exception {
        String url = "https://test.payu.in/_payment";
        Map<String, String> params = new HashMap<>();
        params.put("key","JP***g"); params.put("txnid","ewP8oRopzdHEtC"); params.put("amount","10.00");
        params.put("firstname","Ashish"); params.put("email","test@gmail.com"); params.put("phone","9876543210");
        params.put("productinfo","iPhone"); params.put("pg","TESTPG"); params.put("bankcode","TESTPGNB");
        params.put("surl","https://apiplayground-response.herokuapp.com/");
        params.put("furl","https://apiplayground-response.herokuapp.com/");
        params.put("hash","bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319");
        StringJoiner sj = new StringJoiner("&");
        for (Map.Entry<String,String> e : params.entrySet())
            sj.add(URLEncoder.encode(e.getKey(),"UTF-8")+"="+URLEncoder.encode(e.getValue(),"UTF-8"));
        byte[] postData = sj.toString().getBytes(StandardCharsets.UTF_8);
        HttpURLConnection conn = (HttpURLConnection) new URL(url).openConnection();
        conn.setRequestMethod("POST");
        conn.setRequestProperty("accept","application/json");
        conn.setRequestProperty("Content-Type","application/x-www-form-urlencoded");
        conn.setDoOutput(true);
        try (DataOutputStream dos = new DataOutputStream(conn.getOutputStream())) { dos.write(postData); }
        int code = conn.getResponseCode();
        try (BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream(),StandardCharsets.UTF_8))) {
            StringBuilder sb = new StringBuilder(); String line;
            while ((line = br.readLine()) != null) sb.append(line);
            System.out.println("Status: " + code); System.out.println("Response: " + sb);
        }
    }
}
```

  </Tab>
</Tabs>

## Step 2: Check response from PayU

<ReverseHashing />

<Accordion title="Sample response (parsed)" icon="fa-code">
  ```
  Array
  (
      [mihpayid] => 403993715524045752
      [mode] => NB
      [status] => success
      [unmappedstatus] => captured
      [key] => JPM7Fg
      [txnid] => ewP8oRopzdHEtC
      [amount] => 10.00
      [net_amount_debit] => 10
      [productinfo] => iPhone
      [firstname] => Ashish
      [email] => test@gmail.com
      [phone] => 9876543210
      [bank_ref_num] => 87d3b2a1-5a60-4169-8692-649f61923b3d
      [bankcode] => TESTPGNB
      [error] => E000
      [error_Message] => No Error
  )
  ```
</Accordion>

## Step 3: Verify the payment

<Verify_Payment_Tabs />

## Check Net Banking health

You can check whether the Net Banking server is up and running using the **getNetBankingStatus** API. For more information, refer to [Get Net Banking Status API.](ref:get_net_banking_status_api)

## Recommended integrations for Net Banking

- **Recurring Payments**: Enable recurring payments or subscriptions for wallets. For more information, refer to [Recurring Payments Integration](doc:introduction-recurring-payments-integration).
- **Offers**: Configure offers for cards on Dashboard and then collect payments with offers. For more information, refer to [Create a No-Cost EMI Offer](doc:create-a-no-cost-emi-offer) and [Create a SKU-Based Offer](doc:create-a-sku-based-offer).

<br />
