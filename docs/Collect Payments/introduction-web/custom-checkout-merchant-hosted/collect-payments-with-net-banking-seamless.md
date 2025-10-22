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

**The Net Banking with Merchant Hosted Checkout integration involves the following steps:**

<Cards columns={3}>
  <Card title="1. Initiate the Payment to PayU" href="https://docs.payu.in/docs/collect-payments-with-net-banking-seamless#step-1-initiate-the-payment-to-payu" target="_blank">
    Initiate the payment to PayU with pg=NEFT and bankcode=\<based on bank>

    <br />
  </Card>

  <Card title="2. Check response from PayU" href="https://docs.payu.in/docs/collect-payments-with-net-banking-seamless#step-2-check-response-from-payu">
    Check the response from PayU

    <br />
  </Card>

  <Card title="3. Verify the payment" href="https://docs.payu.in/docs/collect-payments-with-net-banking-seamless#step-3-verify-the-payment">
    Verify the payment using verify\_payment and monitor using webhooks
  </Card>

  <br />
</Cards>

<RegisterMerchantPrerequiste />

## Step 1: Initiate the payment to PayU

<Accordion title="Post request syntax & composition" icon="fa-code">
  Post Request Syntax & Composition for Net Banking

  ```html
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

  <Callout icon="📘" theme="info">
    Note: The above HTML code block is for Merchant Checkout integration on the Net Banking call for the test environment.
  </Callout>
</Accordion>

<Accordion title="Request parameters" icon="fa-code">
  The pg and bankcode parameters vary for the NetBanking payment mode in the **Collect Payment** API (**\_payment** API).

  **Environment**

  |                            |                                                                         |
  | :------------------------- | :---------------------------------------------------------------------- |
  | **Test Environment**       | \<[https://test.payu.in/\_payment>](https://test.payu.in/_payment>)     |
  | **Production Environment** | \<[https://secure.payu.in/\_payment>](https://secure.payu.in/_payment>) |

  <Callout icon="📘" theme="info">
    **Reference**: For the Try-IT experience, refer to <Anchor label="Collect Payment API - Merchant Hosted Checkout" target="_blank" href="https://docs.payu.in/reference/_payment_merchant_hosted">Collect Payment API - Merchant Hosted Checkout</Anchor> under API Reference.
  </Callout>

  | Parameter                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                              | Example                           |
  | :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------- |
  | key <code>mandatory</code>         | `String` Merchant key provided by PayU during onboarding.                                                                                                                                                                                                                                                                                                                                                                                                | JP\*\*\*g                         |
  | txnId <code>mandatory</code>       | `String` The transaction ID is a reference number for a specific order that is generated by the merchant.                                                                                                                                                                                                                                                                                                                                                | ypl938459435                      |
  | amount <code>mandatory</code>      | `String` The payment amount for the transaction.                                                                                                                                                                                                                                                                                                                                                                                                         | 10.00                             |
  | productinfo <code>mandatory</code> | `String` A brief description of the product.                                                                                                                                                                                                                                                                                                                                                                                                             | iPhone                            |
  | firstname <code>mandatory</code>   | `String` The first name of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                 | Ashish                            |
  | email <code>mandatory</code>       | `String` The email address of the customer.                                                                                                                                                                                                                                                                                                                                                                                                              | [abc@payu.in](mailto:abc@payu.in) |
  | phone <code>mandatory</code>       | `String` The phone number of the customer.                                                                                                                                                                                                                                                                                                                                                                                                               |                                   |
  | pg <code>mandatory</code>          | `String` This parameter defined the payment gateway. For NetBanking, pg=NB.                                                                                                                                                                                                                                                                                                                                                                              | TESTPG                            |
  | bankcode <code>mandatory</code>    | `String` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. For the list of bank codes that can be used with the **bankcode** parameter, refer to [Net Banking Codes](doc:net-banking-codes) .- *Reference*\*: For the test Net Banking credentials, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) . | TESTPGNB                          |
  | furl <code>mandatory</code>        | `String` The success URL, which is the page PayU will redirect to if the transaction is successful.                                                                                                                                                                                                                                                                                                                                                      |                                   |
  | surl <code>mandatory</code>        | `String` The Failure URL, which is the page PayU will redirect to if the transaction is failed.                                                                                                                                                                                                                                                                                                                                                          |                                   |
  | hash <code>mandatory</code>        | `String` It is the hash calculated by the merchant. The hash calculation logic is:&#xA;`sha512(key\\|txnid\\|amount\\|productinfo\\|firstname\\|email\\|udf1\\|udf2\\|udf3\\|udf4\\|udf5\\|\\|\\|\\|\\|\\|SALT)`                                                                                                                                                                                                                                         |                                   |
  | address1 <code>optional</code>     | `String` The first line of the billing address.- *For Fraud Detection*\*: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.                                                                                                                                                                                                                          |                                   |
  | address2 <code>optional</code>     | `String` The second line of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                         |                                   |
  | city <code>optional</code>         | `String` The city where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                            |                                   |
  | state <code>optional</code>        | `String` The state where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                           |                                   |
  | country <code>optional</code>      | `String` The country where your customer resides.                                                                                                                                                                                                                                                                                                                                                                                                        |                                   |
  | zipcode <code>optional</code>      | `String` Billing address zip code is mandatory for the cardless EMI option.&#xA;`Character Limit`-20                                                                                                                                                                                                                                                                                                                                                     |                                   |
  | udf1 <code>optional</code>         | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.                                                                                                                                                                                                                                                      |                                   |
  | udf2 <code>optional</code>         | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.                                                                                                                                                                                                                                                      |                                   |
  | udf3 <code>optional</code>         | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.                                                                                                                                                                                                                                                                                                                                          |                                   |
  | udf4 <code>optional</code>         | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.                                                                                                                                                                                                                                                                                                                                          |                                   |
  | udf5 <code>optional</code>         | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.                                                                                                                                                                                                                                                                                                                                          |                                   |

  <HashingRequestParameters />
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X \
   POST "https://test.payu.in/_payment" -H \
   "accept: application/json" -H \
   "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=ewP8oRopzdHEtC&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=TESTPG&bankcode=TESTPGNB&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"
  ```
  ```javascript
  /**
   * PayU Payment Request using Fetch API
   * 
   * IMPORTANT: This should only be executed server-side, never in the browser,
   * as it contains sensitive payment information.
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
      'accept': 'application/json',
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: formData
  };

  // Execute the request
  fetch(url, requestOptions)
    .then(response => {
      console.log('Status Code:', response.status);
      return response.text(); // or response.json() if you're sure it returns JSON
    })
    .then(data => {
      console.log('Response:', data);
    })
    .catch(error => {
      console.error('Error:', error);
    });

  ```
  ```python
  import urllib.request
  import urllib.parse

  url = "https://test.payu.in/_payment"

  headers = {
      "accept": "application/json",
      "Content-Type": "application/x-www-form-urlencoded"
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
      "hash": "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"
  }

  data = urllib.parse.urlencode(payload).encode('utf-8')
  req = urllib.request.Request(url, data=data, headers=headers, method="POST")

  try:
      with urllib.request.urlopen(req) as response:
          response_body = response.read().decode('utf-8')
          print("Status Code:", response.getcode())
          print("Response:")
          print(response_body)
  except urllib.error.HTTPError as e:
      print("Error:", e.code, e.reason)
      print(e.read().decode('utf-8'))

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
</Accordion>

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
      [discount] => 0.00
      [net_amount_debit] => 10
      [addedon] => 2021-09-06 13:27:08
      [productinfo] => iPhone
      [firstname] => Ashish
      [lastname] => 
      [address1] => 
      [address2] => 
      [city] => 
      [state] => 
      [country] => 
      [zipcode] => 
      [email] => test@gmail.com
      [phone] => 9876543210
      [udf1] => 
      [udf2] => 
      [udf3] => 
      [udf4] => 
      [udf5] => 
      [udf6] => 
      [udf7] => 
      [udf8] => 
      [udf9] => 
      [udf10] => 
      [hash] => 1be7e6e97ab1ea9034b9a107e7cf9718308aa9637b4dbbd1a3343c91b0da02b34a40d00ac7267ebe81c20ea1129b931371c555d565bc6e11f470c3d2cf69b5a3
      [field1] => 
      [field2] => 
      [field3] => 
      [field4] => 
      [field5] => 
      [field6] => 
      [field7] => 
      [field8] => 
      [field9] => Transaction Completed Successfully
      [payment_source] => payu
      [PG_TYPE] => NB-PG
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

You can check whether the Net Banking server is up and running using the **getNetBankingStatus** API. If the Net Banking server is down for a bank, you can inform your customers that the Net Banking server is down. For more information on the **getNetBankingStatus** API, refer to getNetBankingStatus.

## Recommended integrations for Net Banking

* **Recurring Payments**: Enable recurring payments or subscriptions for wallets. For more information, refer to [Recurring Payments Integration](doc:introduction-recurring-payments-integration).
* **Offers**: Configure offers for cards on Dashboard and then collect payments with offers. For more information, refer to [Create a No-Cost EMI Offer](doc:create-a-no-cost-emi-offer) and [Create a SKU-Based Offer](doc:create-a-sku-based-offer).
