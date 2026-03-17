---
title: Native OTP Flow for BNPL
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  title: ''
  description: ''
  keywords:
    - Native OTP Flow BNPL Integration
    - BNPL Native OTP Flow Integration with PayU
    - PayU Seamless BNPL integration Native OTP Flow
    - >-
      Buy Now Pay Later Integration with Merchant Hosted Checkout Native OTP
      Flow
    - BNPL API Integration Pay Later Services with PayU
    - Merchant Hosted BNPL Merchant Integration
    - Flexible Payment Options Merchant Hosted Checkout Integration
  robots: index
---
---
title: Native OTP Flow for BNPL
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - Native OTP Flow BNPL Integration
    - BNPL Native OTP Flow Integration with PayU
    - PayU Seamless BNPL integration Native OTP Flow
    - >-
      Buy Now Pay Later Integration with Merchant Hosted Checkout Native OTP
      Flow
    - BNPL API Integration Pay Later Services with PayU
    - Merchant Hosted BNPL Merchant Integration
    - Flexible Payment Options Merchant Hosted Checkout Integration
  robots: index
next:
  description: ''
---

This section describes what is Native OTP flow with benefits and how to implement Native OTP flow when collecting payments using <Glossary>BNPL</Glossary>.

**Steps to integrate**

<Cards columns={3}>
  <Card title="1. Check the BNPL Eligibility" href="https://docs.payu.in/docs/payu-hosted-checkout-integration-with-offers#step-1-check-the-bnpl-eligibility">
    Verify customer eligibility for Buy Now Pay Later options using PayU hosted checkout
  </Card>

  <Card title="2. Initiate the Payment" href="https://docs.payu.in/docs/payu-hosted-checkout-integration-with-offers#step-2-initiate-the-payment">
    Start the payment process using PayU hosted checkout integration with offers
  </Card>

  <Card title="3. Check the Response from PayU" href="https://docs.payu.in/docs/payu-hosted-checkout-integration-with-offers#step-3-check-the-response-from-payu">
    Handle and process the response received from PayU after payment initiation
  </Card>

  <Card title="4. Submit the OTP" href="https://docs.payu.in/docs/payu-hosted-checkout-integration-with-offers#step-4-submit-the-otp">
    Submit and validate OTP for authentication in the BNPL payment flow
  </Card>

  <Card title="5. Verify the Payment" href="https://docs.payu.in/docs/payu-hosted-checkout-integration-with-offers#step-5-verify-the-payment">
    Confirm the payment status and ensure successful transaction completion

    <br />
  </Card>
</Cards>

## What is Native OTP flow

In general, the transaction OTP is captured on Bank pages through multiple hops. With Native OTP Flow, it will be triggered and captured on merchants or the PayU Payment page. The customer stays on the merchant’s (or PayU’s) website/app and completes the Card authentication process of entering OTP on the merchant’s (or PayU) website itself, rather than redirecting the user to a 3d-secure page to complete the transaction. This reduces hops, points of failure, or drops in the checkout process hence faster completion of transactions, better experience, and improved success rate so preferred over OTP on Bank’s Page.

<Accordion title="Benefits" icon="fa-code">
  What are the advantages and why should merchants integrate this flow with PayU?

  * Native OTP flow improves Success Rates of card transactions by 3-5% depending upon the source of transactions.
  * It improves the overall user experience since multiple redirections are removed. Also, the customer never leaves the merchant website, which helps in providing a seamless experience. It also reduces drop rates due to users’ fluctuating internet speed issues.
  * PayU supports all major banks – 15+ banks including HDFC, AXIS, ICICI, SBI, KOTAK, RBL, etc. – on this flow for Cards, cardless, CC EMI, DC EMI’s, and BNPLs.

  The flow supports the latest native OTP generation flows through the **Payment** (\_payment\*\*)\*\*API, followed by **Submit OTP** API, to initiate an S2S=4 transaction.

  <Callout icon="📘" theme="info">
    **Note**: If you don’t have BNPL enabled, try requesting using Dashboard. For more information, refer to[ Checkout payment modes](doc:payu-payment-page-customization#configure-checkout-payment-methods-and-settings). If you could not request through Dashboard, contact your PayU Key Account Manager or <Anchor label="PayU Support" target="_blank" href="https://help.payu.in/">PayU Support</Anchor>.
  </Callout>

  **Steps to Integrate**

  1. [Check the BNPL eligibility](#check-the-bnpl-eligibility)
  2. [Initiate the payment](#initiate-the-payment)
  3. [Check the response from PayU](#step-3-check-the-response-from-payu)
  4. [Submit the OTP](#step-4-submit-the-otp)
</Accordion>

## Step 1: Check the BNPL eligibility

Before you can initiate payment with PayU, you can check the eligibility using the **Get EMI Checkout Details** API. For more information, refer to <Anchor label="Get EMI Checkout Details API" target="_blank" href="ref:get-emi-checkout-details-api">Get EMI Checkout Details API</Anchor>.

<Accordion title="Environment" icon="fa-code">
  |                        |                                                                                                                                       |
  | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
  | Test Environment       | \<[https://test.payu.in/info/linkAndPay/get\_emi\_checkout\_details>](https://test.payu.in/info/linkAndPay/get_emi_checkout_details>) |
  | Production Environment | \<[https://info.payu.in/linkAndPay/get\_emi\_checkout\_details>](https://info.payu.in/linkAndPay/get_emi_checkout_details>)           |
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location 'https://test.payu.in/info/linkAndPay/get_emi_checkout_details' \
    --header 'x-credential-username: smsplus' \
    --header 'Content-Type: application/json' \
    --header 'authorization: hmac username="x0i6r2", algorithm="sha512", headers="date", signature="0e0ebc518c085d8ff49058b7c232bfe2e8779e9e9cafd34a4cdf1c11114035eea75b0e404a9b9e152757dbcc4926f78b6f18ba7f6643e2bf687a65942d3bde38"' \
    --header 'date: Mon, 28 Oct 2024 10:34:49 GMT' \
    --data '{
        "amount": 2000000,
        "userCredentials": "aaa:bbb",
        "phone": "9560012582",
        "bankCode": null,
        "payuToken": null
    }'
  ```
  ```python
  import requests
  import json
  from datetime import datetime

  url = "https://test.payu.in/info/linkAndPay/get_emi_checkout_details"

  # Generate date header in RFC 1123 format
  date_header = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

  # HMAC authorization header (replace with your actual signature)
  authorization = 'hmac username="x0i6r2", algorithm="sha512", headers="date", signature="0e0ebc518c085d8ff49058b7c232bfe2e8779e9e9cafd34a4cdf1c11114035eea75b0e404a9b9e152757dbcc4926f78b6f18ba7f6643e2bf687a65942d3bde38"'

  headers = {
      "x-credential-username": "smsplus",
      "Content-Type": "application/json",
      "authorization": authorization,
      "date": date_header
  }

  payload = {
      "amount": 2000000,
      "userCredentials": "aaa:bbb",
      "phone": "9560012582",
      "bankCode": None,
      "payuToken": None
  }

  response = requests.post(url, headers=headers, json=payload)

  print("Status Code:", response.status_code)
  print("Response:", response.json())
  ```
  ```java
  import java.io.IOException;
  import java.net.URI;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;
  import java.time.ZonedDateTime;
  import java.time.format.DateTimeFormatter;
  import java.util.Locale;

  public class BNPLEligibilityCheck {
      public static void main(String[] args) throws IOException, InterruptedException {
          String url = "https://test.payu.in/info/linkAndPay/get_emi_checkout_details";
          
          // Generate date header in RFC 1123 format
          String dateHeader = DateTimeFormatter
              .ofPattern("EEE, dd MMM yyyy HH:mm:ss 'GMT'", Locale.ENGLISH)
              .format(ZonedDateTime.now());
          
          // HMAC authorization header (replace with your actual signature)
          String authorization = "hmac username=\"x0i6r2\", algorithm=\"sha512\", headers=\"date\", signature=\"0e0ebc518c085d8ff49058b7c232bfe2e8779e9e9cafd34a4cdf1c11114035eea75b0e404a9b9e152757dbcc4926f78b6f18ba7f6643e2bf687a65942d3bde38\"";
          
          String jsonPayload = """
              {
                  "amount": 2000000,
                  "userCredentials": "aaa:bbb",
                  "phone": "9560012582",
                  "bankCode": null,
                  "payuToken": null
              }
              """;
          
          HttpClient client = HttpClient.newHttpClient();
          
          HttpRequest request = HttpRequest.newBuilder()
              .uri(URI.create(url))
              .header("x-credential-username", "smsplus")
              .header("Content-Type", "application/json")
              .header("authorization", authorization)
              .header("date", dateHeader)
              .POST(HttpRequest.BodyPublishers.ofString(jsonPayload))
              .build();
          
          HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
          
          System.out.println("Status Code: " + response.statusCode());
          System.out.println("Response: " + response.body());
      }
  }
  ```
  ```php
  <?php

  $url = "https://test.payu.in/info/linkAndPay/get_emi_checkout_details";

  // Generate date header in RFC 1123 format
  $dateHeader = gmdate('D, d M Y H:i:s') . ' GMT';

  // HMAC authorization header (replace with your actual signature)
  $authorization = 'hmac username="x0i6r2", algorithm="sha512", headers="date", signature="0e0ebc518c085d8ff49058b7c232bfe2e8779e9e9cafd34a4cdf1c11114035eea75b0e404a9b9e152757dbcc4926f78b6f18ba7f6643e2bf687a65942d3bde38"';

  $payload = array(
      'amount' => 2000000,
      'userCredentials' => 'aaa:bbb',
      'phone' => '9560012582',
      'bankCode' => null,
      'payuToken' => null
  );

  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      'x-credential-username: smsplus',
      'Content-Type: application/json',
      'authorization: ' . $authorization,
      'date: ' . $dateHeader
  ));

  $response = curl_exec($ch);
  $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
  curl_close($ch);

  echo "Status Code: " . $httpCode . "\n";
  echo "Response: " . $response . "\n";

  $jsonResponse = json_decode($response, true);
  print_r($jsonResponse);
  ?>
  ```
  ```perl
  #!/usr/bin/perl
  use strict;
  use warnings;
  use LWP::UserAgent;
  use HTTP::Request;
  use JSON;
  use POSIX qw(strftime);

  my $url = "https://test.payu.in/info/linkAndPay/get_emi_checkout_details";

  # Generate date header in RFC 1123 format
  my $date_header = strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime());

  # HMAC authorization header (replace with your actual signature)
  my $authorization = 'hmac username="x0i6r2", algorithm="sha512", headers="date", signature="0e0ebc518c085d8ff49058b7c232bfe2e8779e9e9cafd34a4cdf1c11114035eea75b0e404a9b9e152757dbcc4926f78b6f18ba7f6643e2bf687a65942d3bde38"';

  my $payload = {
      amount          => 2000000,
      userCredentials => "aaa:bbb",
      phone           => "9560012582",
      bankCode        => undef,
      payuToken       => undef
  };

  my $json_payload = encode_json($payload);

  my $ua = LWP::UserAgent->new;
  $ua->timeout(30);

  my $req = HTTP::Request->new('POST', $url);
  $req->header('x-credential-username' => 'smsplus');
  $req->header('Content-Type'          => 'application/json');
  $req->header('authorization'         => $authorization);
  $req->header('date'                  => $date_header);
  $req->content($json_payload);

  my $response = $ua->request($req);

  if ($response->is_success) {
      print "Status Code: " . $response->code . "\n";
      print "Response: " . $response->decoded_content . "\n";
  } else {
      print "Error: " . $response->status_line . "\n";
  }
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-code">
  ```
  {
       "bnpl": {
           "all": [
               {
                   "Lazypay": {
                       "status": 1,
                       "kfsLink": https://www.somekfsLink.com, // only if applicable
                       "eligible": true,
                       "customerLinked": true,

                        “PayuToken”: “Token12345”
                   }
               }
           ]
       }
   }
  ```
</Accordion>

## Step 2: Initiate the payment

> 📘 Reference:
>
> For **Try It** experience, refer to <Anchor label="Collect Payment API - BNPL Link & Pay" target="_blank" href="ref:collect-payment-api-bnpl-link-pay">Collect Payment API - BNPL Link & Pay</Anchor> under API Reference.

<PaymentAPIEnvironment />

<Accordion title="Request parameters" icon="fa-code">
  <Table align={["left","left","left"]}>
    <thead>
      <tr>
        <th style={{ textAlign: "left" }}>
          Parameter
        </th>

        <th style={{ textAlign: "left" }}>
          Description
        </th>

        <th style={{ textAlign: "left" }}>
          Example
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td style={{ textAlign: "left" }}>
          key
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> Merchant key provided by PayU during onboarding.
        </td>

        <td style={{ textAlign: "left" }}>
          ypl938459435
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          txnid
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> The transaction ID is a reference number for a specific order that is generated by the merchant.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          amount
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> The payment amount for the transaction.
        </td>

        <td style={{ textAlign: "left" }}>
          10.00
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          productinfo
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> A brief description of the product.
        </td>

        <td style={{ textAlign: "left" }}>
          iPhone
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          firstname
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> The first name of the customer.
        </td>

        <td style={{ textAlign: "left" }}>
          Ashish
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          email
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> The email address of the customer.
        </td>

        <td style={{ textAlign: "left" }}>
          [abc@payu.in](mailto:abc@payu.in)
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          phone
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> The phone number of the customer.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          pg
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> It defines the payment category using the Merchant Hosted Checkout integration. For a BNPL payment, "BNPL" must be specified in the pg parameter.
        </td>

        <td style={{ textAlign: "left" }}>
          BNPL
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          bankcode
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> The merchant must post this parameter with the corresponding payment option's bank code value in it. For the list of bankcodes for BNPL, refer to

          [BNPL Codes](doc:bnpl-codes)

          .
        </td>

        <td style={{ textAlign: "left" }}>
          LAZYPAY
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          furl
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> The success URL, which is the page PayU will redirect to if the transaction is successful.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          surl
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> The Failure URL, which is the page PayU will redirect to if the transaction is failed.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          hash
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> It is the hash calculated by the merchant. The hash calculation logic is:
          <code>sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)</code>
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          address1
          <code>optional</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> The first line of the billing address.

          <em>For Fraud Detection</em>: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          address2
          <code>optional</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> The second line of the billing address.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          city
          <code>optional</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> The city where your customer resides as part of the billing address.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          state
          <code>optional</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> The state where your customer resides as part of the billing address,
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          country
          <code>optional</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> The country where your customer resides.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          zipcode
          <code>optional</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> Billing address zip code is mandatory for the cardless EMI option.
          <code>Character Limit</code>-20
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          udf1
          <code>optional</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          udf2
          <code>optional</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          udf3
          <code>optional</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          udf4
          <code>optional</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          udf5
          <code>optional</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>
    </tbody>
  </Table>

  <HashingRequestParameters />
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/_payment" \
    -H "accept: application/json" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=JP***g" \
    -d "txnid=BNPL123456789" \
    -d "amount=10.00" \
    -d "firstname=Ashish" \
    -d "email=ashish@example.com" \
    -d "phone=9876543210" \
    -d "productinfo=iPhone" \
    -d "pg=BNPL" \
    -d "bankcode=LAZYPAY" \
    -d "surl=https://apiplayground-response.herokuapp.com/" \
    -d "furl=https://apiplayground-response.herokuapp.com/" \
    -d "txn_s2s_flow=4" \
    -d "hash=<<calculated_hash_here>>"
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
      "txnid": "BNPL123456789",
      "amount": "10.00",
      "firstname": "Ashish",
      "email": "ashish@example.com",
      "phone": "9876543210",
      "productinfo": "iPhone",
      "pg": "BNPL",
      "bankcode": "LAZYPAY",
      "surl": "https://apiplayground-response.herokuapp.com/",
      "furl": "https://apiplayground-response.herokuapp.com/",
      "txn_s2s_flow": "4",
      "hash": "<<calculated_hash_here>>"
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
  import java.util.HashMap;
  import java.util.Map;
  import java.util.stream.Collectors;

  public class BNPLPaymentInitiate {
      public static void main(String[] args) throws IOException, InterruptedException {
          String url = "https://test.payu.in/_payment";
          
          Map<String, String> params = new HashMap<>();
          params.put("key", "JP***g");
          params.put("txnid", "BNPL123456789");
          params.put("amount", "10.00");
          params.put("firstname", "Ashish");
          params.put("email", "ashish@example.com");
          params.put("phone", "9876543210");
          params.put("productinfo", "iPhone");
          params.put("pg", "BNPL");
          params.put("bankcode", "LAZYPAY");
          params.put("surl", "https://apiplayground-response.herokuapp.com/");
          params.put("furl", "https://apiplayground-response.herokuapp.com/");
          params.put("txn_s2s_flow", "4");
          params.put("hash", "<<calculated_hash_here>>");
          
          String formData = params.entrySet().stream()
              .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "=" 
                      + URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
              .collect(Collectors.joining("&"));
          
          HttpClient client = HttpClient.newHttpClient();
          
          HttpRequest request = HttpRequest.newBuilder()
              .uri(URI.create(url))
              .header("accept", "application/json")
              .header("Content-Type", "application/x-www-form-urlencoded")
              .POST(HttpRequest.BodyPublishers.ofString(formData))
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
      'txnid' => 'BNPL123456789',
      'amount' => '10.00',
      'firstname' => 'Ashish',
      'email' => 'ashish@example.com',
      'phone' => '9876543210',
      'productinfo' => 'iPhone',
      'pg' => 'BNPL',
      'bankcode' => 'LAZYPAY',
      'surl' => 'https://apiplayground-response.herokuapp.com/',
      'furl' => 'https://apiplayground-response.herokuapp.com/',
      'txn_s2s_flow' => '4',
      'hash' => '<<calculated_hash_here>>'
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

  $response = curl_exec($ch);
  $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
  curl_close($ch);

  echo "Status Code: " . $httpCode . "\n";
  echo "Response: " . $response . "\n";

  $jsonResponse = json_decode($response, true);
  print_r($jsonResponse);
  ?>
  ```
  ```perl
  #!/usr/bin/perl
  use strict;
  use warnings;
  use LWP::UserAgent;
  use HTTP::Request::Common;

  my $url = "https://test.payu.in/_payment";

  my %data = (
      key         => 'JP***g',
      txnid       => 'BNPL123456789',
      amount      => '10.00',
      firstname   => 'Ashish',
      email       => 'ashish@example.com',
      phone       => '9876543210',
      productinfo => 'iPhone',
      pg          => 'BNPL',
      bankcode    => 'LAZYPAY',
      surl        => 'https://apiplayground-response.herokuapp.com/',
      furl        => 'https://apiplayground-response.herokuapp.com/',
      txn_s2s_flow => '4',
      hash        => '<<calculated_hash_here>>'
  );

  my $ua = LWP::UserAgent->new;
  $ua->timeout(30);

  my $response = $ua->post($url, 
      Content_Type => 'application/x-www-form-urlencoded',
      Content => \%data
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

## Step 3: Check the response from PayU

<Accordion title="Sample payment response" icon="fa-code">
  ```plaintext
  { 
    "metaData": { 
      "message": null, 
      "referenceId": "6a037a290af9253a1d300c8ad0b24c94",// mihpayencoded payuid 
      "statusCode": null, 
      "txnId": "5b7d06c6bf7d4dc2d3a8", 
      "txnStatus": "pending", 
      "unmappedStatus": "pending" 
    }, 
    "result": { "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVu 12 dF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vcHA5NHNlY3VyZS5wYXl1LmluL19wYXltZW50X29wdGlvbnM 13 /bWlocGF5aWQ9NzI0MGQ0OTE5NDJiYzg2NmE1ZTZiNDc2ZTNhZTVkODkmcmVzZW5kRWxpZ2liaWxpdHl 14 SZXM9MzU5NGM3M2IxOGY3Y2E5ZTgxNDZmMGJiM2QwYmQ4NDI5ZTVhMjBjMmY2MWQ3NzhiZmQwZmI0YjB 15 kNDMwZWJkMjFhOGQ4ZmYyMGU3Nzc1OGM5MDNhNzFmZTIyZDM5ZDE0OTQxMjcwMzRlZDdkNTA1MjM3Y2I 16 2ZjdiZjgwY2MzMTA3YTAyY2JkMjIyMTdjMTlmNjY2MmVmYWM4ZThmODNkY2E5MDI0NzBhOTgxYmRkMGE 17 wYzAzODQ3ZDU0NmY0MWFkOGYzMDY2YjJjY2M4YTM1OWUwMzAzMjk1M2YzNjExMmQwZTU1MWVjMTliYTc 18 xOTU0ZGZlNzg4ZDE4YTI4YWM3NjA5YmE1M2JkNzc1NDhjZmZiODE4ODIzNDdmYzhiOTczMTU1MDlhZmR 19 mOGEwODk0NDQzY2Y5MWUwYjFmZGU4NDU5NGJlZTZmYzlkMzlkYTg4NGYzMDIxZWIyMjI0NjE4ZTJjN2Y 20 xMTVhMDIwNTcwNTE5ODcyMjBlYzc4NjRlY2M0NGEwMTI0MTdlNDg4MGIxODdlZTFmMTIzNjNhMjVhNGJ 21 lYzYyZDgzMjJlYjFiMTg1MTk1YTcxNDEyNGI1ZGU5NDMwOWE2ZGNlNDJlZjQ0MTQ2NGQzNDYyZTc4MDk 22 2NzBjIiBtZXRob2Q9InBvc3QiPjwvZm9ybT48c2NyaXB0IHR5cGU9J3RleHQvamF2YXNjcmlwdCc+CiA 23 gICAgICAgICAgICAgICAgICAgICAgICAgICB3aW5kb3cub25sb2FkPWZ1bmN0aW9uKCl7CiAgICAgICA 24 gICAgICAgICAgICAgICAgICAgICAgICAgZG9jdW1lbnQuZm9ybXNbJ3BheW1lbnRfcG9zdCddLnN1Ym1 25 pdCgpOwogICAgICAgICAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgICAgICAgICA 26 8L3NjcmlwdD48L2JvZHk+PC9odG1sPg==",// Base64 Encoded HTML 27 "otpPostUrl": "https://test.payu.in/ResponseHandler.php} 
  } 
  ```
</Accordion>

<Accordion title="Handling payment response" icon="fa-code">
  This sub-section describes the components of the payment response received with Native OTP or Zero Redirection flow. It contains the **metaData** and **result** JSON as described in this subsection:

  #### metaData JSON fields description

  | **Field**      | **Description**                                                                                                                                          |
  | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | message        | This field contains any additional message about the transaction.                                                                                        |
  | referenceId    | This field contains the reference ID of the transaction.                                                                                                 |
  | statusCode     | This field contains the status code for the transaction.                                                                                                 |
  | txnId          | This field contains the transaction ID of the transaction that was posted in the request.                                                                |
  | unmappedStatus | This field contains the unmapped status of the transaction. For more information, refer to [Payment State Explanations](ref:payment-state-explanations). |

  #### result JSON fields description

  The **result** JSON contains the **acsTemplate** with base64 encoding.

  <Table>
    <thead>
      <tr>
        <th>
          **Field**
        </th>

        <th>
          **Description**
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          mihpayid
        </td>

        <td>
          It is a unique reference number created for each transaction at PayU’s end. You must note this transaction ID as this will be used as a reference for all the future actions on this transaction like Inquiry or Refund.
        </td>
      </tr>

      <tr>
        <td>
          mode
        </td>

        <td>
          This parameter describes the payment category by which the transaction was completed or attempted by the customer. For the payment categories, refer to

          [Payment Mode Codes](doc:payment-mode-codes)

          .
        </td>
      </tr>

      <tr>
        <td>
          status
        </td>

        <td>
          This parameter gives the status of the transaction as either success, failed or pending.
          Possible values: success, failure, pending
          If the value of the ‘status’ parameter is ’success’, the transaction is successful.
          If the value of ‘status’ is ‘failure’ or ‘pending’, must be treated as a failed transaction only.
        </td>
      </tr>

      <tr>
        <td>
          key
        </td>

        <td>
          This parameter contains the merchant key for the merchant’s account at PayU. It would be the same as the key used while the transaction request is being posted from the merchant’s end to PayU.
        </td>
      </tr>

      <tr>
        <td>
          txnid
        </td>

        <td>
          This parameter would contain the transaction ID value posted by the merchant during the transaction request.
        </td>
      </tr>

      <tr>
        <td>
          amount
        </td>

        <td>
          This parameter would contain the original amount which was sent in the transaction request by the merchant.
        </td>
      </tr>

      <tr>
        <td>
          productinfo
        </td>

        <td>
          This parameter would contain the same value of product information which was sent in the transaction request from the merchant’s end to PayU.
        </td>
      </tr>

      <tr>
        <td>
          firstname
        </td>

        <td>
          This parameter would contain the same value of first name which was sent in the transaction request from the merchant’s end to PayU.
        </td>
      </tr>

      <tr>
        <td>
          lastname
        </td>

        <td>
          This parameter would contain the same value of last name which was sent in the transaction request from the merchant’s end to PayU.
        </td>
      </tr>

      <tr>
        <td>
          email
        </td>

        <td>
          This parameter would contain the same value of email which was sent.
        </td>
      </tr>

      <tr>
        <td>
          phone
        </td>

        <td>
          This parameter would contain the same value of phone which was sent in the transaction request from the merchant’s end to PayU.
        </td>
      </tr>

      <tr>
        <td>
          udf
        </td>

        <td>
          This parameter would contain the same value of udf values that were sent in the transaction request from the merchant’s end to PayU. It ranges from udf1 to udf5.
        </td>
      </tr>

      <tr>
        <td>
          hash
        </td>

        <td>
          PayU calculates the hash using a string of other parameters and returns it to the merchant. The merchant must verify the hash, and only then mark a transaction as success/failure. This is to make sure that the transaction hasn’t been tampered with.
        </td>
      </tr>

      <tr>
        <td>
          error
        </td>

        <td>
          For the failed transactions, this parameter provides the reason for
          failure.

          * *Note*\*: The reason for failure depends upon the error codes provided by different banks and hence the detailing of error reasons may differ from one transaction to another. The merchant can use this parameter to retrieve the reason for failure for a particular transaction.
        </td>
      </tr>

      <tr>
        <td>
          bankcode
        </td>

        <td>
          This parameter contains the code indicating the payment option used for the transaction. For example, in the Debit Card mode, there are different options like Visa Debit Card, Mastercard, Maestro etc. For each option, a unique bank code exists. It would be returned in this bank code parameter. For example, Visa Debit Card – VISA, Master Debit Card – MAST.
        </td>
      </tr>

      <tr>
        <td>
          PG\_TYPE
        </td>

        <td>
          This parameter gives information on the payment gateway used for the transaction. For example, if CC PG was used, it would contain the value CC-PG. Similarly, it would have a unique value for all different types of payment gateways.
        </td>
      </tr>

      <tr>
        <td>
          bank\_ref\_num
        </td>

        <td>
          For each successful transaction – this parameter would contain the bank reference number generated by the bank.
        </td>
      </tr>

      <tr>
        <td>
          unmappedstatus
        </td>

        <td>
          This parameter contains the status of a transaction as per the internal database of PayU. PayU’s system has several intermediate status which are used for tracking various activities internal to the system. For more information, refer to

          [Payment State Explanations](ref:payment-state-explanations)

          .
        </td>
      </tr>
    </tbody>
  </Table>

  <Callout icon="📘" theme="info">
    **Notes**:

    To request OTP on a page, you can utilize the URLs in the response itself. There are two URLs to use:

    * otpPostUrl (Merchant Hosted OTP page)
    * acsTemplate (PayU Hosted OTP page) which acts as a fallback
  </Callout>

  If you are getting a URL in `otpPostUrl`, use `otpPostUrl`, otherwise, you can use `acsTemplate`, which acts as a fallback. In this scenario, use PayU (or WebView or Checkout) OTP page as this is a fallback case.

  Hence, for cases where the above response is not successful, it could either be **Failed** or **Pending**. In the **Pending** state, you can send a fallback URL (as above) which can be shown to the customer.

  #### acsTemplate

  **acsTemplate** is base64 encoded, after decoding we’ll get an HTML like below:

  ```html
  <html> 
     <body> 
        <form name="payment_post" id="payment_post" action="https://test.payu.in/ 
        _payment_options?mihpayid=1983a7cf520b567155ed95ca181e37e3&resendEligibilityRes       =3594c73b18f7ca9e8146f0bb3d0bd8429e5a20c2f61d778bfd0fb4b0d430ebd21a8d8ff20e7775       8c903a71fe22d39d1494127034ed7d505237cb6f7bf80cc3107a02cbd22217c19f6662efac8e8f8       3dca902470a981bdd0a0c03847d546f41ad8f3066b2ccc8a359e03032953f36112d0e551ec19ba7       1954dfe788d18a28ac7609ba53bd77548cffb81882347fc8b97315509afdf8a0894443cf91e0b1f       de84594bee6fc9d39da884f3021eb2224618e2c7f115a02057051987220ec7864ecc44a012417e4      880b187ee1f12363a25a4bec62d8322eb1b185195a714124b5de94309a6dce42ef441464d3462e7 
        809670c" method="post"></form> 
        <script type='text/javascript'> 
           window.onload=function(){ 
               document.forms['payment_post'].submit(); 
           } 
        </script> 
     </body> 
  </html> 
  ```

  On opening the above HTML, you will get a PayU checkout OTP page similar to the following:

  <Image align="center" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/02/word-image-5.png" width="512px" />

  From here, the steps are as in PayU Hosted (non-seamless) or Merchant Hosted or Server-to-Server (seamless) transactions.
</Accordion>

<Accordion title="Handling Failure Response" icon="fa-code">
  This is a situation where the **\_payment** API has a complete failure. Hence, you will be getting ‘failed’ in `txnStatus` and `otpPostUrl` is also not received in the result object.

  ```plaintext
  { 
    "metaData": 
    { 
      "message": "Transaction Failed at bank end.", 
      "referenceId": "ea68a970115a9d87c6ece8d0218e6c2a", 
      "statusCode": "E308", 
      "txnId": "54d2d883f8e4a3fff6ba", 
      "txnStatus": "failed", 
      "unmappedStatus": "failure" 
    }, 
    "result": {} 
  } 
  ```

  ***
</Accordion>

## Step 4: Submit the OTP

After you have collected the OTP from the customer, the reference ID can be found in the Payment API (**_payment**) response. Submit the OTP that is entered by the customer is submitted along with the reference ID using the [Submit OTP API](ref:submit-otp-to-payu).

## Step 5: Verify the payment

<p>Upon receiving the response, we recommend performing a reconciliation step to validate all transaction details.\
You can verify your payments using either of the following methods:</p>

<Verify_Payment_Tabs />

<br />

<br />
