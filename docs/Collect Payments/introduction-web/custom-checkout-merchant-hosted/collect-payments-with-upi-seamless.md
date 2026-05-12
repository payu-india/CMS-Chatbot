---
title: UPI Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Collect Payments with UPI - Merchant Hosted Checkout
  description: >-
    Learn how to seamlessly collect payments through UPI transactions using
    PayU's Merchant Hosted Checkout integration. Discover the steps to validate
    the customer's Virtual Payment Address (VPA), initiate payments, and verify
    the payment status.
  robots: index
next:
  description: ''
---
<NPCI_Mandate />

<br />

PayU allows you to collect payments using UPI handles. For the list of UPI providers supported, refer to [UPI Handles](https://docs.payu.in/docs/doc:upi-handles).

<br />

<Callout icon="👍" theme="okay">
  Experience the end-to-end **Merchant Hosted Checkout** > **UPI** flow and instantly generate the complete code for seamless, zero-coding integration into your website.

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
                              font-weight: bold; /* Added this line */
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

                          <button onclick="window.open('https://payu.in/integrationlab/seamless/sm-upiflow', '_blank')" 
                                  class="tooltip-btn" 
                                  data-tooltip="Click here to see the Merchant Hosted Checkout >  UPI end-to-end integration and instantly generate the complete code needed for a zero-coding setup on your website.">
                              Experience the flow and get the code
                          </button>
  `}</HTMLBlock>
</Callout>

**Steps to Integrate:**

<Cards>
  <Card title="1. Validate the UPI handle" href="https://docs.payu.in/docs/collect-payments-with-upi-seamless#step-1-valiadate-the-upi-handle">
    Validate the card type using the Validae VPA API
  </Card>

  <Card title="2. Initiate the Payment to PayU" href="https://docs.payu.in/docs/collect-payments-with-upi-seamless#step-2-initiate-the-payment-to-payu">
    Initiate the payment to PayU with pg=UPI and bankcode=UPI
  </Card>

  <Card title="3. Check response from PayU" href="https://docs.payu.in/docs/collect-payments-with-upi-seamless#step-3-check-response-from-payu">
    Check the response from PayU
  </Card>

  <Card title="4. Verify the payment" href="#step-4-verify-the-payment">
    Verify the payment using verify\_payment and monitor using webhooks
  </Card>
</Cards>

<RegisterMerchantPrerequiste />

<Callout icon="📮" theme="default">
  **Postman Collection**: Access the **Merchant Hosted Checkout > UPI APIs Postman Collection** from the following location:

  [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/folder/394lrbp/upi-integration](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/folder/394lrbp/upi-integration)
</Callout>

<Callout icon="⚠️" theme="warning">
  **Important UPI Integration Changes as per NPCI Mandate on UPI Collect Disablement**:

  * **Seamless Form Post Users**: Merchants using Seamless Form Post flow must migrate to `txn_s2s_flow` (UPI Intent S2S), as Intent is **not supported** in the seamless form post flow for Android and Desktop web. For migration guidance, refer to [UPI Intent S2S Integration](doc:upi-intent-server-to-server).

  * **For Android Apps**: Merchants must implement the Smart Intent implementation. Refer to [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow) or use [PayU Android SDKs](doc:explore-android-sdks) which have Smart Intent built-in.

  * **For iOS Apps**: Merchants can implement the specific deeplink and continue using the UPI Collect flow as is.

  * **For Web**: Merchants must use the deeplink created via [UPI Intent S2S Integration](doc:upi-intent-server-to-server) to generate a QR code of the deeplink, instead of the UPI Collect flow.
</Callout>

## Step 1: Validate the UPI handle

You can validate your customer's Virtual Payment Address (VPA) using the <Anchor label="Validate VPA Handle" target="_blank" href="https://docs.payu.in/reference/validate_vpa_api">Validate VPA Handle</Anchor> API before initiating the transaction.

<GENERALAPIsEnvironment />

<Accordion title="Sample request" icon="fa-code">
  <Validate_VPA />
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  **Success scenario**

  if successfully validated:

  ````plaintext
  {
     "status":"SUCCESS",
     "vpa":"9999999999@upi",
     "isVPAValid":1,
     "isAutoPayVPAValid":1,
     "isAutoPayBankValid":"NA",
     "payerAccountName":"ABC"
  }
  > 📘 Notes:
  >
  > * The **payerAccountName** parameter can be empty or NA or will have a payer name based on the value given by the bank.
  > * If both **isVPAValid** and **isAutoPayVPAValid** is 1, you must initiate payment for Recurring Payments.
  > * Ignore the **isAutoPayBankValid** parameter in the response.

  **Failure scenarios**

  * If invalid VPA, the response is similar to the following:

  ```plaintext
  {
   "status":"SUCCESS","vpa":"abc@upi","isVPAValid":0,"payerAccountName":"NA"
  }  
  ````

  * Invalid VPA but handle supporting SI (Autopay):

  ```plaintext
  {
   "status":"SUCCESS","vpa":"abc@upi","isVPAValid":0,"isAutoPayVPAValid":1,"isAutoPayBankValid":"NA","payerAccountName":"NA"
  }
  ```

  * Customer valid but handle not supporting SI (Autopay):

  ```plaintext
  {
    "status":"SUCCESS","vpa":"xyz@freecharge","isVPAValid":1,"isAutoPayVPAValid":0,"isAutoPayBankValid":"NA","payerAccountName":"XYZ"
  }
  ```

  * Neither customer valid nor handle supporting Autopay:

  ```plaintext
  {
    "status":"SUCCESS","vpa":"xyz@freecharge","isVPAValid":0,"isAutoPayVPAValid":0,"isAutoPayBankValid":"NA","payerAccountName":"NA"
  }
  ```
</Accordion>

<Accordion title="Sample VPA validation code" icon="fa-code">
  ```javascript
      	// JavaScript example for VPA validation before payment submission
      // This should be run on your server, not client-side

      async function validateVpa(vpa) {
          try {
              // Get hash from server endpoint
              const hashResponse = await fetch('/generate-vpa-hash', {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/json' },
                  body: JSON.stringify({ vpa })
              });
              const { hash } = await hashResponse.json();
              
              // Validate VPA with PayU
              const response = await fetch('https://test.payu.in/merchant/postservice?form=2', {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                  body: new URLSearchParams({
                      key: 'YOUR_MERCHANT_KEY',
                      command: 'validateVPA',
                      var1: vpa, // VPA to validate
                      hash: hash
                  })
              });
              
              const result = await response.json();
              
              // Sample response:
              // {"status":1,"msg":"VPA is valid","isVPAValid":1,"isUPIBarredBank":0}
              // OR
              // {"status":0,"msg":"VPA is invalid","isVPAValid":0}
              
              return {
                  isValid: result.isVPAValid === 1,
                  message: result.msg
              };
          } catch (error) {
              console.error('VPA validation error:', error);
              return { isValid: false, message: 'Validation service error' };
          }
      }

  ```
  ```curl
  # Once you have the hash, make the API call

  curl -X POST "https://test.payu.in/merchant/postservice?form=2"       -H "Content-Type: application/x-www-form-urlencoded"       -d "key=YOUR_MERCHANT_KEY"       -d "command=validateVPA"       -d "var1=customer@upi"       -d "hash=$HASH"

  ```
</Accordion>

## Step 2: Initiate the payment to PayU

<Accordion title="Post request syntax & composition" icon="fa-code">
  Post Request Syntax & Composition for UPI

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
  <input type="hidden" name="pg" value="UPI" />
  <input type="hidden" name="bankcode" value="UPI" />
  <input type="hidden" name="vpa" value="test123@okhdfcbank" />
  <input type="hidden" name="surl" value="your own success url" />
  <input type="hidden" name="furl" value="your own failure url" />
  <input type="hidden" name="phone" value="9988776655" />
  <input type="hidden" name="hash" value="eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972" />
  <input type="submit" value="submit"> </form>
  </body>
  </html>
  ```

  > 📘 Note
  >
  > The above HTML code block is for Merchant Checkout integration on the UPI call for the test environment.
</Accordion>

<Accordion title="Request parameters" icon="fa-table">
  #### Request parameters

  The following parameters vary for the UPI payment mode in the **Collect Payment** API (**\_payment** API).

  **Environment**

  |                            |                                                                         |
  | :------------------------- | :---------------------------------------------------------------------- |
  | **Test Environment**       | \<[https://test.payu.in/\_payment>](https://test.payu.in/_payment>)     |
  | **Production Environment** | \<[https://secure.payu.in/\_payment>](https://secure.payu.in/_payment>) |

  > 📘 Reference:
  >
  > For the **Try It** experience and response, refer to [Collect Payment API - Merchant Hosted Checkout](https://docs.payu.in/reference/_payment_merchant_hosted) under API Reference.

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
                                                                                                      <td>key <code>mandatory</code></td>
                                                                                                      <td><code>String</code> Merchant key provided by PayU during onboarding.</td>
                                                                                                      <td>JPg***r</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>txnid <code>mandatory</code></td>
                                                                                                      <td><code>String</code> The transaction ID is a reference number for a specific order that is generated by the merchant.</td>
                                                                                                      <td>ypl938459435</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>amount <code>mandatory</code></td>
                                                                                                      <td><code>String</code> The payment amount for the transaction.</td>
                                                                                                      <td>10.00</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>productinfo <code>mandatory</code></td>
                                                                                                      <td><code>String</code> A brief description of the product.</td>
                                                                                                      <td>iPhone</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>firstname <code>mandatory</code></td>
                                                                                                      <td><code>String</code> The first name of the customer.</td>
                                                                                                      <td>Ashish</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>email <code>mandatory</code></td>
                                                                                                      <td><code>String</code> The email address of the customer.</td>
                                                                                                      <td>abc@payu.in</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>phone <code>mandatory</code></td>
                                                                                                      <td><code>String</code> The phone number of the customer.</td>
                                                                                                      <td>9988776655</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>pg <code>mandatory</code></td>
                                                                                                      <td><code>String</code> It defines the payment category that the merchant wants the customer to see by default on the PayU's payment page. This field must contain the value as "UPI" for UPI transactions.</td>
                                                                                                      <td>UPI</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>bankcode <code>mandatory</code></td>
                                                                                                      <td><code>String</code> Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. For a detailed list of bank codes, please contact the PayU Support.</td>
                                                                                                      <td>UPI</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>vpa <code>mandatory</code></td>
                                                                                                      <td><code>String</code> The VPA of the customer. For the list of bank name part of the handles, refer to <a href="https://docs.payu.in/docs/doc:upi-handles">UPI Handles</a>. <br><strong>Reference</strong>: For the list of test card numbers for EMI, refer to <a href="https://docs.payu.in/docs/test-cards-upi-id-and-wallets">Test Cards, UPI ID and Wallets</a></td>
                                                                                                      <td>test123@okhdfcbank</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>furl <code>mandatory</code></td>
                                                                                                      <td><code>String</code> The success URL, which is the page PayU will redirect to if the transaction is successful.</td>
                                                                                                      <td>https://example.com/success</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>surl <code>mandatory</code></td>
                                                                                                      <td><code>String</code> The Failure URL, which is the page PayU will redirect to if the transaction is failed.</td>
                                                                                                      <td>https://example.com/failure</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>hash <code>mandatory</code></td>
                                                                                                      <td><code>String</code> It is the hash calculated by the merchant. The hash calculation logic is:<br><code>sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)</code></td>
                                                                                                      <td>eabec285da28fd...</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>address1 <code>optional</code></td>
                                                                                                      <td><code>String</code> The first line of the billing address.<br><strong>For Fraud Detection</strong>: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.</td>
                                                                                                      <td>123 Main Street</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>address2 <code>optional</code></td>
                                                                                                      <td><code>String</code> The second line of the billing address.</td>
                                                                                                      <td>Apt 4B</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>city <code>optional</code></td>
                                                                                                      <td><code>String</code> The city where your customer resides as part of the billing address.</td>
                                                                                                      <td>New Delhi</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>state <code>optional</code></td>
                                                                                                      <td><code>String</code> The state where your customer resides as part of the billing address.</td>
                                                                                                      <td>Delhi</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>country <code>optional</code></td>
                                                                                                      <td><code>String</code> The country where your customer resides.</td>
                                                                                                      <td>India</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>zipcode <code>optional</code></td>
                                                                                                      <td><code>String</code> Billing address zip code is mandatory for the cardless EMI option.<br><code>Character Limit</code>: 20</td>
                                                                                                      <td>110001</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>udf1 <code>optional</code></td>
                                                                                                      <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.</td>
                                                                                                      <td>Custom Data 1</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>udf2 <code>optional</code></td>
                                                                                                      <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.</td>
                                                                                                      <td>Custom Data 2</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>udf3 <code>optional</code></td>
                                                                                                      <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td>
                                                                                                      <td>Custom Data 3</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>udf4 <code>optional</code></td>
                                                                                                      <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td>
                                                                                                      <td>Custom Data 4</td>
                                                                                                    </tr>
                                                                                                    <tr>
                                                                                                      <td>udf5 <code>optional</code></td>
                                                                                                      <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td>
                                                                                                      <td>Custom Data 5</td>
                                                                                                    </tr>
                                                                                                  </tbody>
                                                                                                </table>
  `}</HTMLBlock>

  <Accordion title="Understanding Hashing and sample code" icon="fa-code">
    <HashingRequestParameters />

    #### Hashing Sample Code

    <HashingSample />
  </Accordion>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
      curl -X      POST "https://test.payu.in/_payment" -H      "accept: application/json" -H      "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=xdB9G7qYpfqszo&amount=10&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=UPI&bankcode=UPI&vpa=VPA-anything@payu&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb"
  ```
  ```python
  import requests

  url = "https://test.payu.in/_payment"

  headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
  }

  data = {
    "key": "JP***g",
    "txnid": "xdB9G7qYpfqszo",
    "amount": "10",
    "firstname": "PayU User",
    "email": "test@gmail.com",
    "phone": "9876543210",
    "productinfo": "iPhone",
    "pg": "UPI",
    "bankcode": "UPI",
    "vpa": "VPA-anything@payu",
    "surl": "https://apiplayground-response.herokuapp.com/",
    "furl": "https://apiplayground-response.herokuapp.com/",
    "hash": "649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb"
  }

  response = requests.post(url, headers=headers, data=data)
  print(response.status_code)
  print(response.text)
  ```
  ```perl
  use strict;
  use warnings;
  use LWP::UserAgent;
  use HTTP::Request::Common qw(POST);

  my $url = "https://test.payu.in/_payment";

  my $ua = LWP::UserAgent->new();

  my $response = $ua->request(POST $url,
      'Accept' => 'application/json',
      'Content-Type' => 'application/x-www-form-urlencoded',
      Content => [
          key => 'JP***g',
          txnid => 'xdB9G7qYpfqszo',
          amount => '10',
          firstname => 'PayU User',
          email => 'test@gmail.com',
          phone => '9876543210',
          productinfo => 'iPhone',
          pg => 'UPI',
          bankcode => 'UPI',
          vpa => 'VPA-anything@payu',
          surl => 'https://apiplayground-response.herokuapp.com/',
          furl => 'https://apiplayground-response.herokuapp.com/',
          hash => '649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb'
      ]
  );

  print "Status: " . $response->code . "\n";
  print "Response: " . $response->content . "\n";
  ```
  ```java
  import java.io.IOException;
  import java.net.URI;
  import java.net.URLEncoder;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;
  import java.nio.charset.StandardCharsets;
  import java.util.HashMap;
  import java.util.Map;
  import java.util.stream.Collectors;

  public class PayURequest {
      public static void main(String[] args) throws IOException, InterruptedException {
          String url = "https://test.payu.in/_payment";
          
          Map<String, String> parameters = new HashMap<>();
          parameters.put("key", "JP***g");
          parameters.put("txnid", "xdB9G7qYpfqszo");
          parameters.put("amount", "10");
          parameters.put("firstname", "PayU User");
          parameters.put("email", "test@gmail.com");
          parameters.put("phone", "9876543210");
          parameters.put("productinfo", "iPhone");
          parameters.put("pg", "UPI");
          parameters.put("bankcode", "UPI");
          parameters.put("vpa", "VPA-anything@payu");
          parameters.put("surl", "https://apiplayground-response.herokuapp.com/");
          parameters.put("furl", "https://apiplayground-response.herokuapp.com/");
          parameters.put("hash", "649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb");
          
          String formData = parameters.entrySet()
                  .stream()
                  .map(entry -> URLEncoder.encode(entry.getKey(), StandardCharsets.UTF_8) + "=" + 
                               URLEncoder.encode(entry.getValue(), StandardCharsets.UTF_8))
                  .collect(Collectors.joining("&"));
          
          HttpClient client = HttpClient.newHttpClient();
          HttpRequest request = HttpRequest.newBuilder()
                  .uri(URI.create(url))
                  .header("Accept", "application/json")
                  .header("Content-Type", "application/x-www-form-urlencoded")
                  .POST(HttpRequest.BodyPublishers.ofString(formData))
                  .build();
          
          HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
          
          System.out.println("Status Code: " + response.statusCode());
          System.out.println("Response: " + response.body());
      }
  }
  ```
  ```javascript
  const url = 'https://test.payu.in/merchant/postservice?form=2';

  const data = new URLSearchParams({
  key: 'JP***g',
  command: 'validateVPA',
  var1: '9999999999@upi',
  hash: '75bb573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472fff9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e'
  });

  const response = await fetch(url, {
  method: 'POST',
  headers: {
   'Accept': 'application/json',
   'Content-Type': 'application/x-www-form-urlencoded'
  },
  body: data.toString()
  });

  const result = await response.json();
  console.log(result);
  ```
</Accordion>

## Step 3: Check response from PayU

<ReverseHashing />

### Hash validation logic for payment response (Reverse Hashing)

While sending the response, PayU takes the exact same parameters that were sent in the request (in reverse order) to calculate the hash and returns it to you. You must verify the hash and then mark a transaction as a success or failure. This is to make sure the transaction has not tampered within the response.

The order of the parameters is similar to the following code block:

```
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

<Accordion title="Sample Response" icon="fa-code">
  ```
      Array
      (
          [mihpayid] => 403993715523409521
          [mode] => UPI
          [status] => success
          [unmappedstatus] => captured
          [key] => JPM7Fg
          [txnid] => 5jJ9xRceXX1ydT
          [amount] => 10.00
          [discount] => 0.00
          [net_amount_debit] => 1000
          [addedon] => 2021-07-02 15:03:50
          [productinfo] => iPhone
          [firstname] => PayU User
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
          [hash] => 716f92a6452adadba68d133ba7f5ca3f3403f03f554e3ef850911f3e6727ee73402b249054170ad276c8b55ca12368a5e27cc69ffb0642ef6403dae9a5708794
          [field1] => vpa-anything@payu
          [field2] => 5jJ9xRceXX1ydT
          [field3] => 
          [field4] => PayU User
          [field5] => AXIhh4ExnaJ9dKiJvPxsewHwxMMmT3ba7UY
          [field6] => 
          [field7] => Transaction completed successfully
          [field8] => 
          [field9] => Transaction completed successfully
          [payment_source] => payu
          [PG_TYPE] => UPI-PG
          [bank_ref_num] => 5jJ9xRceXX1ydT
          [bankcode] => UPI
          [error] => E000
          [error_Message] => No Error
      )
  ```
</Accordion>

## Step 4: Verify the payment

<Verify_Payment_Tabs />

## Recommended integrations for UPI

* **Recurring Payments**: Enable recurring payments or subscriptions for wallets. For more information, refer to [Recurring Payments Integration](https://docs.payu.in/docs/introduction-recurring-payments-integration).
  * **Offers**: Configure offers for cards on Dashboard and then collect payments with offers. For more information, refer to [Offers Dashboard](https://docs.payu.in/docs/offers-dashboard) and [Offers Integration APIs](https://docs.payu.in/docs/offers-integration)
