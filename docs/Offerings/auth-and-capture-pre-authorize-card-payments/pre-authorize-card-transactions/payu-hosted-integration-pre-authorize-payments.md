---
title: PayU Hosted Integration
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
The **pre\_authorize** parameter is used to pre-authorize payments using the PayU Hosted Checkout integration with the **\_payment** API.

<Callout icon="👍" theme="okay">
  ###

  Experience the end-to-end **Pre-Authorize Payments** flow and instantly generate the complete code for seamless, zero-coding integration into your website.

    

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

                  <button onclick="window.open('https://payu.in/integrationlab/preauth', '_blank')" 
                          class="tooltip-btn" 
                          data-tooltip="Automatically generate code including hashing for your eCommerce website to integrate PreAuth - PayU Hosted Checkout with zero coding knowledge.">
                      Experience the flow and get the code
                  </button>
  `}</HTMLBlock>
</Callout>

<br />

<Callout icon="📘" theme="info">
  ###

  **Note**: You need to activate the Pre-Authorize Payments before you start using this integration. Contact your PayU Key Account Manager (KAM) to activate Pre-Authorize Payments.
</Callout>

<Cards columns={2}>
  <Card title="1. Post the Pre-Auth Transaction Request" href="#step-1-post-the-pre-auth-transaction-request">
    Submit pre-authorization payment request to PayU's \_payment API with mandatory parameters including merchant key, transaction details, customer information, and pre\_authorize parameter set to 1

    <br />
  </Card>

  <Card title="2. Check the Response from PayU" href="#step-2-check-the-response-from-payu">
    Validate PayU's response using reverse hash calculation, verify transaction status, unmappedstatus for pre-authorization confirmation, and other key response parameters

    <br />
  </Card>

  <Card title="3. Capture a Pre-Authorized Payment" href="#step-3-capture-a-pre-authorized-payment">
    Use capture\_transaction command with merchant key, hash, and transaction ID to settle pre-authorized payments when ready for final processing

    <br />
  </Card>

  <Card title="4. Check Action Status" href="#step-4-check-action-status">
    Verify and reconcile transaction details using webhooks for real-time monitoring or Verify Payment API to check unmappedstatus and ensure accurate capture processing
  </Card>

  <br />
</Cards>

## Step 1: Post the pre-auth transaction request

The **pre\_authorize** parameter as specified is used to pre-authorize payments using the PayU Hosted Checkout integration with the **\_payment** API. For **Try-It** experience, refer to <Anchor target="_blank" href="ref:pre_authorize_payment">Pre-Authorize Payment</Anchor> for the complete list parameters with **Try It** experience.

**Environment**

|                            |                                                                       |
| :------------------------- | :-------------------------------------------------------------------- |
| **Test Environment**       | [https://test.payu.in/\_payment>](https://test.payu.in/_payment>)     |
| **Production Environment** | [https://secure.payu.in/\_payment>](https://secure.payu.in/_payment>) |

<Accordion title="Request parameters" icon="fa-table">
  <HTMLBlock>{`
              <table>
                <thead>
                  <tr>
                    <th style="text-align: left;">Parameter</th>
                    <th style="text-align: left;">Description</th>
                    <th style="text-align: left;">Example</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>key</td>
                    <td><code>String</code> The merchant key provided by PayU while onboarding.</td>
                    <td>JP***g</td>
                  </tr>
                  <tr>
                    <td>txnid</td>
                    <td><code>String</code> The transaction ID is a reference number for a specific order that is generated by the merchant.</td>
                    <td>ypl938459435</td>
                  </tr>
                  <tr>
                    <td>amount<br><code>mandatory</code></td>
                    <td><code>String</code> The payment amount for the transaction.</td>
                    <td>10.00</td>
                  </tr>
                  <tr>
                    <td>productinfo<br><code>mandatory</code></td>
                    <td><code>String</code> A brief description of the product.</td>
                    <td>iPhone</td>
                  </tr>
                  <tr>
                    <td>firstname<br><code>mandatory</code></td>
                    <td><code>String</code> The first name of the customer.</td>
                    <td>Ashish</td>
                  </tr>
                  <tr>
                    <td>email<br><code>mandatory</code></td>
                    <td><code>String</code> The email address of the customer.</td>
                    <td><a href="mailto:abc@payu.in">abc@payu.in</a></td>
                  </tr>
                  <tr>
                    <td>phone<br><code>mandatory</code></td>
                    <td><code>String</code> The phone number of the customer.</td>
                    <td></td>
                  </tr>
                  <tr>
                    <td>lastname<br><code>optional</code></td>
                    <td><code>String</code> The last name of the customer.</td>
                    <td>Kumar</td>
                  </tr>
                  <tr>
                    <td>surl<br><code>mandatory</code></td>
                    <td><code>String</code> The success URL, which is the page PayU will redirect to if the transaction is successful.</td>
                    <td><a href="https://test-payment-middleware.payu.in/simulatorResponse">https://test-payment-middleware.payu.in/simulatorResponse</a></td>
                  </tr>
                  <tr>
                    <td>furl<br><code>mandatory</code></td>
                    <td><code>String</code> The Failure URL, which is the page PayU will redirect to if the transaction is failed.</td>
                    <td><a href="https://test-payment-middleware.payu.in/simulatorResponse">https://test-payment-middleware.payu.in/simulatorResponse</a></td>
                  </tr>
                  <tr>
                    <td>pre_authorize<br><code>mandatory for Pre-Auth</code></td>
                    <td><code>String</code> This parameter is set to <strong>1</strong> to pre-authorize payment using PayU Hosted Checkout.</td>
                    <td></td>
                  </tr>
                  <tr>
                    <td>hash</td>
                    <td><code>String</code> It is the hash calculated by the merchant.<br><br><strong>Reference:</strong> For detailed information on hashing, refer to <a href="generate-hash-payu-hosted" target="_blank">Generate Hash</a>.</td>
                    <td></td>
                  </tr>
                  <tr>
                    <td>address1<br><code>optional</code></td>
                    <td><code>String</code> The first line of the billing address.<br><br><strong>Fraud Detection:</strong> This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.</td>
                    <td>H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai</td>
                  </tr>
                  <tr>
                    <td>address2<br><code>optional</code></td>
                    <td><code>String</code> The second line of the billing address.</td>
                    <td>34 Saikripa-Estate, Tilak Nagar</td>
                  </tr>
                  <tr>
                    <td>city<br><code>optional</code></td>
                    <td><code>String</code> The city where your customer resides as part of the billing address.</td>
                    <td>Mumbai</td>
                  </tr>
                  <tr>
                    <td>state<br><code>optional</code></td>
                    <td><code>String</code> The state where your customer resides as part of the billing address.</td>
                    <td>Maharashtra</td>
                  </tr>
                  <tr>
                    <td>country<br><code>optional</code></td>
                    <td><code>String</code> The country where your customer resides.</td>
                    <td>India</td>
                  </tr>
                  <tr>
                    <td>zipcode<br><code>optional</code></td>
                    <td><code>String</code> Billing address zip code is mandatory for the cardless EMI option.<br><code>Character Limit: 20</code></td>
                    <td>400004</td>
                  </tr>
                  <tr>
                    <td>enforced_payment<br><code>optional</code></td>
                    <td><code>String</code> This parameter is to customize the payment options for each transaction. You can enforce specific payment modes, cards scheme, and specific banks under Net Banking using this method.</td>
                    <td>creditcard|debitcard</td>
                  </tr>
                  <tr>
                    <td>drop_category<br><code>optional</code></td>
                    <td><code>String</code> This parameter is used if you want to hide one or multiple payment options. For example, if you consider the payment options such as credit card, debit card, and net banking, you can hide the credit card mode of payment.</td>
                    <td>CC</td>
                  </tr>
                  <tr>
                    <td>udf1<br><code>optional</code></td>
                    <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.</td>
                    <td>AELPR****E</td>
                  </tr>
                  <tr>
                    <td>udf2<br><code>optional</code></td>
                    <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.</td>
                    <td></td>
                  </tr>
                  <tr>
                    <td>udf3<br><code>optional</code></td>
                    <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td>
                    <td>02-02-1980</td>
                  </tr>
                  <tr>
                    <td>udf4<br><code>optional</code></td>
                    <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td>
                    <td>XYZ Pvt. Ltd.</td>
                  </tr>
                  <tr>
                    <td>udf5<br><code>optional</code></td>
                    <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td>
                    <td>098450845</td>
                  </tr>
                </tbody>
              </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Hashing" icon="fa-code">
  You must hash the request parameters using the following hash logic:

  ```
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
  ```

  For more information, refer to [Generate Hash](doc:generate-hash-payu-hosted).
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/_payment
  -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
  "key=JP***g&txnid=PQI6MqpYrjEefU&amount=10.00
  &firstname=PayU User&email=test@gmail.com&phone=9876543210
  &productinfo=iPhone&pre_authorize=1&pg=cc&bankcode=CC&surl=
  https://apiplayground-response.herokuapp.com/
  &furl=https://apiplayground-response.herokuapp.com/
  &pre_authorize=1&hash=05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072"
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
      "txnid": "PQI6MqpYrjEefU",
      "amount": "10.00",
      "firstname": "PayU User",
      "email": "test@gmail.com",
      "phone": "9876543210",
      "productinfo": "iPhone",
      "pre_authorize": "1",
      "pg": "cc",
      "bankcode": "CC",
      "surl": "https://apiplayground-response.herokuapp.com/",
      "furl": "https://apiplayground-response.herokuapp.com/",
      "hash": "05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072"
  }

  response = requests.post(url, headers=headers, data=data)

  print("Status Code:", response.status_code)
  print("Response:", response.text)
  ```
  ```java
  import java.io.IOException;
  import java.net.URI;
  import java.net.URLEncoder;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;
  import java.nio.charset.StandardCharsets;
  import java.util.LinkedHashMap;
  import java.util.Map;
  import java.util.stream.Collectors;

  public class PayUHostedPreAuthorizePayment {
      public static void main(String[] args) throws IOException, InterruptedException {
          String url = "https://test.payu.in/_payment";
          
          Map<String, String> formData = new LinkedHashMap<>();
          formData.put("key", "JP***g");
          formData.put("txnid", "PQI6MqpYrjEefU");
          formData.put("amount", "10.00");
          formData.put("firstname", "PayU User");
          formData.put("email", "test@gmail.com");
          formData.put("phone", "9876543210");
          formData.put("productinfo", "iPhone");
          formData.put("pre_authorize", "1");
          formData.put("pg", "cc");
          formData.put("bankcode", "CC");
          formData.put("surl", "https://apiplayground-response.herokuapp.com/");
          formData.put("furl", "https://apiplayground-response.herokuapp.com/");
          formData.put("hash", "05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072");
          
          String formBody = formData.entrySet()
              .stream()
              .map(entry -> URLEncoder.encode(entry.getKey(), StandardCharsets.UTF_8) + "=" + 
                            URLEncoder.encode(entry.getValue(), StandardCharsets.UTF_8))
              .collect(Collectors.joining("&"));
          
          HttpClient client = HttpClient.newHttpClient();
          
          HttpRequest request = HttpRequest.newBuilder()
              .uri(URI.create(url))
              .header("accept", "application/json")
              .header("Content-Type", "application/x-www-form-urlencoded")
              .POST(HttpRequest.BodyPublishers.ofString(formBody))
              .build();
          
          HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
          
          System.out.println("Status Code: " + response.statusCode());
          System.out.println("Response: " + response.body());
      }
  }
  ```
  ```php
  <?php

  $url = "https://test.payu.in/_payment";

  $data = array(
      'key' => 'JP***g',
      'txnid' => 'PQI6MqpYrjEefU',
      'amount' => '10.00',
      'firstname' => 'PayU User',
      'email' => 'test@gmail.com',
      'phone' => '9876543210',
      'productinfo' => 'iPhone',
      'pre_authorize' => '1',
      'pg' => 'cc',
      'bankcode' => 'CC',
      'surl' => 'https://apiplayground-response.herokuapp.com/',
      'furl' => 'https://apiplayground-response.herokuapp.com/',
      'hash' => '05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072'
  );

  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      'accept: application/json',
      'Content-Type: application/x-www-form-urlencoded'
  ));
  curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);

  $response = curl_exec($ch);
  $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
  $error = curl_error($ch);
  curl_close($ch);

  if ($error) {
      echo "cURL Error: " . $error . "\n";
  } else {
      echo "Status Code: " . $httpCode . "\n";
      echo "Response: " . $response . "\n";
  }
  ?>
  ```
  ```perl
  #!/usr/bin/perl
  use strict;
  use warnings;
  use LWP::UserAgent;
  use HTTP::Request::Common qw(POST);

  my $url = "https://test.payu.in/_payment";

  my $ua = LWP::UserAgent->new;
  $ua->timeout(30);

  my %data = (
      'key'           => 'JP***g',
      'txnid'         => 'PQI6MqpYrjEefU',
      'amount'        => '10.00',
      'firstname'     => 'PayU User',
      'email'         => 'test@gmail.com',
      'phone'         => '9876543210',
      'productinfo'   => 'iPhone',
      'pre_authorize' => '1',
      'pg'            => 'cc',
      'bankcode'      => 'CC',
      'surl'          => 'https://apiplayground-response.herokuapp.com/',
      'furl'          => 'https://apiplayground-response.herokuapp.com/',
      'hash'          => '05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072'
  );

  my $response = $ua->request(POST $url,
      Content_Type => 'application/x-www-form-urlencoded',
      Accept       => 'application/json',
      Content      => [%data]
  );

  if ($response->is_success) {
      print "Status Code: " . $response->code . "\n";
      print "Response: " . $response->decoded_content . "\n";
  } else {
      print "Error: " . $response->status_line . "\n";
      print "Response: " . $response->decoded_content . "\n";
  }
  ```
</Accordion>

## Step 2: Check the response from PayU

<ReverseHashing />

<Accordion title="Sample response" icon="fa-code">
  By default, the response in HTML format. The formatted sample response body is similar to the following, and you need to look for the following parameters:

  * PG\_TYPE: CC PG
  * bankcode: CC
  * **unamappedstatus: auth**

  ```
  mihpayid: 403993715523615328
  mode: CC
  status: success
  unmappedstatus: auth
  key: JPM7Fg
  txnid: 50QJq6lBJBmx14
  amount: 10.00
  cardCategory: domestic
  discount: 0.00
  net_amount_debit: 10
  addedon: 2021-07-28 15:11:37
  productinfo: iPhone
  firstname: PayU User
  lastname: 
  address1: 
  address2: 
  city: 
  state: 
  country: 
  zipcode: 
  email: test@gmail.com
  phone: 9876543210
  udf1: 
  udf2: 
  udf3: 
  udf4: 
  udf5: 
  udf6: 
  udf7: 
  udf8: 
  udf9: 
  udf10: 
  hash: afeab9dcf4e43d47f8fbf5a6838d393c70694a58e30ada08e6cb86ac943236c05717c5f5e4872d671fe81d0d9b2d9facd44e9a061ba621aff6f20c4343ea5dfa
  field1: 
  field2: 
  field3: 
  field4: 
  field5: 
  field6: 
  field7: 
  field8: 
  field9: Transaction Completed Successfully
  payment_source: payu
  PG_TYPE: CC-PG
  bank_ref_num: 7f0d5ada-59bb-41d7-9e41-20a6af2406c9
  bankcode: CC
  error: E000
  error_Message: No Error
  name_on_card: test
  cardnum: 411111XXXXXX1111
  cardhash: This field is no longer supported in postback params.

  ```
</Accordion>

## Step 3: Capture a Pre-authorized payment

To capture a pre-authorized payment, use the following command. After the API command is successful, the transaction would be captured and settled to you.

**Environment**

|                        |                                                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| Test Environment       | [https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2) |
| Production Environment | [https://info.payu.in/merchant/postservice.php?form=2](https://info.payu.in/merchant/postservice.php?form=2) |

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location --request POST 'https://info.payu.in/merchant/postservice.php?form=2' \ 
  --header 'Content-Type: application/x-www-form-urlencoded' \ 
  --form 'key="JF***g"' \ 
  --form 'command="capture_transaction"' \ 
  --form 'hash="67411736ab98c59522492a12751a6015c41b87764019f9dc14052690c2c7af9095d31002fc109dcf3596c2f38792d56db6f6207b1989010f2adf51c144fa3019"' \ 
  --form 'var1="15246574846"' \ 
  --form 'var2="authorizeTransaction123"' \ 
  --form 'var3="1"' 
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-code">
  ```json
  { 
      "status": 1, 
      "msg": "Capture Request Queued", 
      "request_id": "Request ID", 
      "bank_ref_num": "Bank Reference Number" 
  } 
  ```
</Accordion>

## Step 4: Check Action Status

<Verify_Payment_Tabs />

<br />

<Callout icon="📘" theme="info">
  ###

  **Notes**:

  - The **unamappedstatus** to **auth** can be checked using the <Anchor target="_blank" href="ref:verify_payment_api">Verify Payment API</Anchor> and in callback response in the Transaction callback.
  - To check the status of the Auth Request and then Capture Request sent, use the **check\_action\_status** API. For more information,  refer to  <Anchor target="_blank" href="ref:check_action_status_api_with_request_id">Check Refund Status API with Request ID</Anchor>.
  - If you want to cancel or refund a pre-authorized payment, refer to [Cancel a Pre-Authorized Payment](doc:cancel-a-pre-authorized-payment).
</Callout>

<Callout icon="👍" theme="okay">
  ###

  **Reference**: For cancelling pre-auth payments, refer to <Anchor target="_blank" href="ref:cancel-a-pre-authorized-transaction">Cancel a Pre-Authorized Transaction API</Anchor>.
</Callout>

<br />
