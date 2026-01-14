---
title: Single Transfer Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Single Transfer Integration
  description: >-
    Integrate PayU's Single Transfer Payouts seamlessly with our comprehensive
    API guide. Learn how to automate and manage your business payouts securely
    and efficiently. Explore the step-by-step process for integrating PayU's
    payout solutions to enhance your financial operations.
  keywords:
    - PayU Payouts integration
    - Single transfer payouts
    - Automate payouts with PayU
    - Secure payouts Integration with PayU
    - Real-time payouts API
    - Business payouts with PayU
    - Integrate PayU payouts
    - ' Salary Payouts integration with PayU Payouts API'
    - Amount Disbursements with Payouts API
  robots: index
next:
  description: ''
---
---
title: Single Transfer Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Single Transfer Integration
  description: >-
    Integrate PayU's Single Transfer Payouts seamlessly with our comprehensive
    API guide. Learn how to automate and manage your business payouts securely
    and efficiently. Explore the step-by-step process for integrating PayU's
    payout solutions to enhance your financial operations.
  keywords:
    - PayU Payouts integration
    - Single transfer payouts
    - Automate payouts with PayU
    - Secure payouts Integration with PayU
    - Real-time payouts API
    - Business payouts with PayU
    - Integrate PayU payouts
    - ' Salary Payouts integration with PayU Payouts API'
    - Amount Disbursements with Payouts API
  robots: index
next:
  description: ''
---
Single Transfer Integration with Payouts allows you to make instant payments to a beneficiary through the APIs using different payment modes as illustrated in the following figure:

<Image border={false} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Frame-5-1024x304.png" />


## Step 1. Generate authentication token

Payouts Integration begins with access token generation. You should have an Access Token for authentication while accessing Payouts Endpoints. Without authentication, payouts core APIs can’t be accessed.

For this purpose, PayU provides two methods to generate the authentication token as follows:

1. [Generate Token using Merchant's Credentials API](ref:generate-token-using-merchants-credentials-api)
2. [Generate Token using Private Client ID](ref:generate-token-using-private-client-id)

> 📘 Note:
>
> The authentication tokens have a TTL (Time To Live) and are required to be refreshed after a fixed interval of time. A Refresh Token API can be requested to obtain a renewed access token. For more information on this, refer to [Refresh Token API - Payouts](ref:refresh-token-api-payouts)

***

## Step 2. Get account details

The **getAccountDetail** API returns complete account details of the merchant’s Payouts account.

**Environment**

|                        |                                                                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://uatoneapi.payu.in/payout/merchant/getAccountDetail](https://uatoneapi.payu.in/payout/merchant/getAccountDetail>)       |
| Production Environment | [https://payout.payumoney.com/payout/merchant/getAccountDetail](https://payout.payumoney.com/payout/merchant/getAccountDetail>) |

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X GET "https://test.payumoney.com/payout/merchant/getAccountDetail" \
    -H "cache-control: no-cache" \
    -H "content-type: application/x-www-form-urlencoded" \
    -H "authorization: bearer aab9dc927c4a68af7eb95ef694f0b48bb731c5a1a7111786d6658d774db14188" \
    -H "payoutMerchantId: 1111123"
  ```
  ```python
  import requests

  url = "https://test.payumoney.com/payout/merchant/getAccountDetail"

  headers = {
      "cache-control": "no-cache",
      "content-type": "application/x-www-form-urlencoded",
      "authorization": "bearer aab9dc927c4a68af7eb95ef694f0b48bb731c5a1a7111786d6658d774db14188",
      "payoutMerchantId": "1111123"
  }

  response = requests.get(url, headers=headers)

  print("Status Code:", response.status_code)
  print("Response:", response.json())
  ```
  ```java
  import java.io.IOException;
  import java.net.URI;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;

  public class GetAccountDetail {
      public static void main(String[] args) throws IOException, InterruptedException {
          String url = "https://test.payumoney.com/payout/merchant/getAccountDetail";
          
          HttpClient client = HttpClient.newHttpClient();
          
          HttpRequest request = HttpRequest.newBuilder()
              .uri(URI.create(url))
              .header("cache-control", "no-cache")
              .header("content-type", "application/x-www-form-urlencoded")
              .header("authorization", "bearer aab9dc927c4a68af7eb95ef694f0b48bb731c5a1a7111786d6658d774db14188")
              .header("payoutMerchantId", "1111123")
              .GET()
              .build();
          
          HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
          
          System.out.println("Status Code: " + response.statusCode());
          System.out.println("Response: " + response.body());
      }
  }
  ```
  ```php
  <?php

  $url = "https://test.payumoney.com/payout/merchant/getAccountDetail";

  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      'cache-control: no-cache',
      'content-type: application/x-www-form-urlencoded',
      'authorization: bearer aab9dc927c4a68af7eb95ef694f0b48bb731c5a1a7111786d6658d774db14188',
      'payoutMerchantId: 1111123'
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

  my $url = "https://test.payumoney.com/payout/merchant/getAccountDetail";

  my $ua = LWP::UserAgent->new;
  $ua->timeout(30);

  my $req = HTTP::Request->new('GET', $url);
  $req->header('cache-control'    => 'no-cache');
  $req->header('content-type'     => 'application/x-www-form-urlencoded');
  $req->header('authorization'    => 'bearer aab9dc927c4a68af7eb95ef694f0b48bb731c5a1a7111786d6658d774db14188');
  $req->header('payoutMerchantId' => '1111123');

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
  "status": 0,
  "msg": null,
  "code": null,
  "data": {
  "payoutMerchantId": 1111123,
  "uuid": "11e8-5a8f-05faaaa4-84a5-020d245326e4",
  "virtualAccountNumber": "PAYUIN1111123",
  "transferableAmount": 0,
  "balance": 94003,
  "lowBalance": false,
  "ifsc": "YESB0CMSNOC",
  "type": "current",
  "clientId": "6f8bb4951e030d4d7349e64a144a534778673585f86039617c167166e9154f7e",
  "transitAccountNumber": null
  }
  }
  ```
</Accordion>

## Step 3. Initiate single transfer

Request for initiation of a single transfer to the beneficiary using Initiate Single Transfer API. For Try IT experience, refer to [Initiate Transfer API](ref:initiate-transfer-api).

You can transfer through various payment modes described in [Initiate Transfer API](ref:initiate-transfer-api):

* IMPS, NEFT or RTGS Payment Request
* UPI Payment Request
* Phone Payment Request
* MasterCard Payment Request
* VISA Card Payment Request
* Credit Card Payment Request
**Environment**

|                            |                                                                                            |
| -------------------------- | ------------------------------------------------------------------------------------------ |
| **Test Environment**       | [https://uatoneapi.payu.in/payout/v2/payment](https://uatoneapi.payu.in/payout/v2/payment) |
| **Production Environment** | [https://payout.payumoney.com/payout/payment](https://payout.payumoney.com/payout/payment) |

<Accordion title="Sample request" icon="fa-code">
  **IMPS, NEFT or RTGS Payment Request**

  ```curl
  curl -X POST "https://uatoneapi.payu.in/payout/v2/payment" \
    -H "authorization: Bearer <your_access_token>" \
    -H "content-type: application/json" \
    -H "payoutMerchantId: 1111123" \
    -d '[
      {
        "beneficiaryAccountNumber": "51234567890",
        "beneficiaryIfscCode": "HDFC0001234",
        "beneficiaryName": "Payu",
        "beneficiaryEmail": "payu@payu.in",
        "beneficiaryMobile": "9876473627",
        "purpose": "Payment from Company",
        "amount": 1234.12,
        "batchId": "1",
        "merchantRefId": "123asdfad3",
        "paymentType": "IMPS",
        "retry": false
      }
    ]'
  ```
  ```python
  import requests
  import json

  url = "https://uatoneapi.payu.in/payout/v2/payment"

  headers = {
      "authorization": "Bearer <your_access_token>",
      "content-type": "application/json",
      "payoutMerchantId": "1111123"
  }

  payload = [
      {
          "beneficiaryAccountNumber": "51234567890",
          "beneficiaryIfscCode": "HDFC0001234",
          "beneficiaryName": "Payu",
          "beneficiaryEmail": "payu@payu.in",
          "beneficiaryMobile": "9876473627",
          "purpose": "Payment from Company",
          "amount": 1234.12,
          "batchId": "1",
          "merchantRefId": "123asdfad3",
          "paymentType": "IMPS",
          "retry": False
      }
  ]

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

  public class InitiateIMPSTransfer {
      public static void main(String[] args) throws IOException, InterruptedException {
          String url = "https://uatoneapi.payu.in/payout/v2/payment";
          
          String jsonPayload = """
              [
                  {
                      "beneficiaryAccountNumber": "51234567890",
                      "beneficiaryIfscCode": "HDFC0001234",
                      "beneficiaryName": "Payu",
                      "beneficiaryEmail": "payu@payu.in",
                      "beneficiaryMobile": "9876473627",
                      "purpose": "Payment from Company",
                      "amount": 1234.12,
                      "batchId": "1",
                      "merchantRefId": "123asdfad3",
                      "paymentType": "IMPS",
                      "retry": false
                  }
              ]
              """;
          
          HttpClient client = HttpClient.newHttpClient();
          
          HttpRequest request = HttpRequest.newBuilder()
              .uri(URI.create(url))
              .header("authorization", "Bearer <your_access_token>")
              .header("content-type", "application/json")
              .header("payoutMerchantId", "1111123")
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

  $url = "https://uatoneapi.payu.in/payout/v2/payment";

  $payload = array(
      array(
          'beneficiaryAccountNumber' => '51234567890',
          'beneficiaryIfscCode' => 'HDFC0001234',
          'beneficiaryName' => 'Payu',
          'beneficiaryEmail' => 'payu@payu.in',
          'beneficiaryMobile' => '9876473627',
          'purpose' => 'Payment from Company',
          'amount' => 1234.12,
          'batchId' => '1',
          'merchantRefId' => '123asdfad3',
          'paymentType' => 'IMPS',
          'retry' => false
      )
  );

  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      'authorization: Bearer <your_access_token>',
      'content-type: application/json',
      'payoutMerchantId: 1111123'
  ));

  $response = curl_exec($ch);
  $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
  curl_close($ch);

  echo "Status Code: " . $httpCode . "\n";
  echo "Response: " . $response . "\n";
  ?>
  ```
  ```perl
  #!/usr/bin/perl
  use strict;
  use warnings;
  use LWP::UserAgent;
  use HTTP::Request;
  use JSON;

  my $url = "https://uatoneapi.payu.in/payout/v2/payment";

  my $payload = [
      {
          beneficiaryAccountNumber => '51234567890',
          beneficiaryIfscCode      => 'HDFC0001234',
          beneficiaryName          => 'Payu',
          beneficiaryEmail         => 'payu@payu.in',
          beneficiaryMobile        => '9876473627',
          purpose                  => 'Payment from Company',
          amount                   => 1234.12,
          batchId                  => '1',
          merchantRefId            => '123asdfad3',
          paymentType              => 'IMPS',
          retry                    => JSON::false
      }
  ];

  my $json_payload = encode_json($payload);

  my $ua = LWP::UserAgent->new;
  my $req = HTTP::Request->new('POST', $url);
  $req->header('authorization'    => 'Bearer <your_access_token>');
  $req->header('content-type'     => 'application/json');
  $req->header('payoutMerchantId' => '1111123');
  $req->content($json_payload);

  my $response = $ua->request($req);

  print "Status Code: " . $response->code . "\n";
  print "Response: " . $response->decoded_content . "\n";
  ```

  **UPI Payment Request**

  ```curl
  curl -X POST "https://uatoneapi.payu.in/payout/v2/payment" \
    -H "authorization: Bearer <your_access_token>" \
    -H "content-type: application/json" \
    -H "payoutMerchantId: 1111123" \
    -d '[
      {
        "beneficiaryName": "Payu",
        "beneficiaryEmail": "payu@payu.in",
        "beneficiaryMobile": "9876473627",
        "purpose": "Payment from Company",
        "amount": 1234.12,
        "batchId": "1",
        "merchantRefId": "123",
        "paymentType": "UPI",
        "vpa": "ankush.pokarana@ybl",
        "retry": false
      }
    ]'
  ```
  ```python
  import requests
  import json

  url = "https://uatoneapi.payu.in/payout/v2/payment"

  headers = {
      "authorization": "Bearer <your_access_token>",
      "content-type": "application/json",
      "payoutMerchantId": "1111123"
  }

  payload = [
      {
          "beneficiaryName": "Payu",
          "beneficiaryEmail": "payu@payu.in",
          "beneficiaryMobile": "9876473627",
          "purpose": "Payment from Company",
          "amount": 1234.12,
          "batchId": "1",
          "merchantRefId": "123",
          "paymentType": "UPI",
          "vpa": "ankush.pokarana@ybl",
          "retry": False
      }
  ]

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

  public class InitiateUPITransfer {
      public static void main(String[] args) throws IOException, InterruptedException {
          String url = "https://uatoneapi.payu.in/payout/v2/payment";
          
          String jsonPayload = """
              [
                  {
                      "beneficiaryName": "Payu",
                      "beneficiaryEmail": "payu@payu.in",
                      "beneficiaryMobile": "9876473627",
                      "purpose": "Payment from Company",
                      "amount": 1234.12,
                      "batchId": "1",
                      "merchantRefId": "123",
                      "paymentType": "UPI",
                      "vpa": "ankush.pokarana@ybl",
                      "retry": false
                  }
              ]
              """;
          
          HttpClient client = HttpClient.newHttpClient();
          
          HttpRequest request = HttpRequest.newBuilder()
              .uri(URI.create(url))
              .header("authorization", "Bearer <your_access_token>")
              .header("content-type", "application/json")
              .header("payoutMerchantId", "1111123")
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

  $url = "https://uatoneapi.payu.in/payout/v2/payment";

  $payload = array(
      array(
          'beneficiaryName' => 'Payu',
          'beneficiaryEmail' => 'payu@payu.in',
          'beneficiaryMobile' => '9876473627',
          'purpose' => 'Payment from Company',
          'amount' => 1234.12,
          'batchId' => '1',
          'merchantRefId' => '123',
          'paymentType' => 'UPI',
          'vpa' => 'ankush.pokarana@ybl',
          'retry' => false
      )
  );

  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      'authorization: Bearer <your_access_token>',
      'content-type: application/json',
      'payoutMerchantId: 1111123'
  ));

  $response = curl_exec($ch);
  $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
  curl_close($ch);

  echo "Status Code: " . $httpCode . "\n";
  echo "Response: " . $response . "\n";
  ?>
  ```
  ```perl
  #!/usr/bin/perl
  use strict;
  use warnings;
  use LWP::UserAgent;
  use HTTP::Request;
  use JSON;

  my $url = "https://uatoneapi.payu.in/payout/v2/payment";

  my $payload = [
      {
          beneficiaryName   => 'Payu',
          beneficiaryEmail  => 'payu@payu.in',
          beneficiaryMobile => '9876473627',
          purpose           => 'Payment from Company',
          amount            => 1234.12,
          batchId           => '1',
          merchantRefId     => '123',
          paymentType       => 'UPI',
          vpa               => 'ankush.pokarana@ybl',
          retry             => JSON::false
      }
  ];

  my $json_payload = encode_json($payload);

  my $ua = LWP::UserAgent->new;
  my $req = HTTP::Request->new('POST', $url);
  $req->header('authorization'    => 'Bearer <your_access_token>');
  $req->header('content-type'     => 'application/json');
  $req->header('payoutMerchantId' => '1111123');
  $req->content($json_payload);

  my $response = $ua->request($req);

  print "Status Code: " . $response->code . "\n";
  print "Response: " . $response->decoded_content . "\n";
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-code">
**Success response**

  ```plaintext
  {
   "status": 0,
   "msg": "Requests are in process. Will send response of individual request on webhooks set by you",
   "code": null,
   "data": []
   }
  ```

  **Failure response**

  ```plaintext
  {
   "status": 1,
   "msg": null,
   "code": null,
   "data": [
             {
              "batchId": "1",
              "merchantRefId": "111",
              "error": "beneficiary account number can not be empty. ",
              "code": [1004]
             }
           ]
   }
  ```
</Accordion>


## Step 4. Check transfer status

Fetch the status of the transfer by posting the merchant’s reference ID as a parameter using the Check Transfer Status API. For more information on Payouts statuses, refer to [Payouts Lifecycle](doc:payouts-lifecycle). For Try-It experience for Check Transfer Status API, refer to [Check Transfer Status API](https://docs.payu.in/reference/check-transfer-status-api/).
**Environment**

|                            |                                                                                                                              |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Test Environment**       | [https://uatoneapi.payu.in/payout/payment/listTransactions](https://uatoneapi.payu.in/payout/payment/listTransactions)       |
| **Production Environment** | [https://payout.payumoney.com/payout/payment/listTransactions](https://payout.payumoney.com/payout/payment/listTransactions) |

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X POST "https://test.payumoney.com/payout/payment/listTransactions" \
    -H "authorization: Bearer 2678f236346281e6029e3430da1a721af29bb3546d6acbc27e6aadd7fca72605" \
    -H "cache-control: no-cache" \
    -H "content-type: application/x-www-form-urlencoded" \
    -H "payoutmerchantid: 1111122" \
    -d "transferStatus=QUEUED&from=01%2F01%2F2019&to=01%2F01%2F2019&page=1&pageSize=100&merchantRefId=&batchId=1"
  ```
  ```python
  import requests

  url = "https://test.payumoney.com/payout/payment/listTransactions"

  headers = {
      "authorization": "Bearer 2678f236346281e6029e3430da1a721af29bb3546d6acbc27e6aadd7fca72605",
      "cache-control": "no-cache",
      "content-type": "application/x-www-form-urlencoded",
      "payoutmerchantid": "1111122"
  }

  data = {
      "transferStatus": "QUEUED",
      "from": "01/01/2019",
      "to": "01/01/2019",
      "page": "1",
      "pageSize": "100",
      "merchantRefId": "",
      "batchId": "1"
  }

  response = requests.post(url, headers=headers, data=data)

  print("Status Code:", response.status_code)
  print("Response:", response.json())
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

  public class CheckTransferStatus {
      public static void main(String[] args) throws IOException, InterruptedException {
          String url = "https://test.payumoney.com/payout/payment/listTransactions";
          
          Map<String, String> params = new HashMap<>();
          params.put("transferStatus", "QUEUED");
          params.put("from", "01/01/2019");
          params.put("to", "01/01/2019");
          params.put("page", "1");
          params.put("pageSize", "100");
          params.put("merchantRefId", "");
          params.put("batchId", "1");
          
          String formData = params.entrySet().stream()
              .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "=" 
                      + URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
              .collect(Collectors.joining("&"));
          
          HttpClient client = HttpClient.newHttpClient();
          
          HttpRequest request = HttpRequest.newBuilder()
              .uri(URI.create(url))
              .header("authorization", "Bearer 2678f236346281e6029e3430da1a721af29bb3546d6acbc27e6aadd7fca72605")
              .header("cache-control", "no-cache")
              .header("content-type", "application/x-www-form-urlencoded")
              .header("payoutmerchantid", "1111122")
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

  $url = "https://test.payumoney.com/payout/payment/listTransactions";

  $data = array(
      'transferStatus' => 'QUEUED',
      'from' => '01/01/2019',
      'to' => '01/01/2019',
      'page' => '1',
      'pageSize' => '100',
      'merchantRefId' => '',
      'batchId' => '1'
  );

  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      'authorization: Bearer 2678f236346281e6029e3430da1a721af29bb3546d6acbc27e6aadd7fca72605',
      'cache-control: no-cache',
      'content-type: application/x-www-form-urlencoded',
      'payoutmerchantid: 1111122'
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
  use JSON;

  my $url = "https://test.payumoney.com/payout/payment/listTransactions";

  my %data = (
      transferStatus => 'QUEUED',
      from           => '01/01/2019',
      to             => '01/01/2019',
      page           => '1',
      pageSize       => '100',
      merchantRefId  => '',
      batchId        => '1'
  );

  my $ua = LWP::UserAgent->new;
  $ua->timeout(30);

  my $req = HTTP::Request->new('POST', $url);
  $req->header('authorization'    => 'Bearer 2678f236346281e6029e3430da1a721af29bb3546d6acbc27e6aadd7fca72605');
  $req->header('cache-control'    => 'no-cache');
  $req->header('content-type'     => 'application/x-www-form-urlencoded');
  $req->header('payoutmerchantid' => '1111122');

  # Build form data
  my $content = join('&', map { "$_=" . uri_escape($data{$_}) } keys %data);
  $req->content($content);

  use URI::Escape;

  my $response = $ua->request($req);

  if ($response->is_success) {
      print "Status Code: " . $response->code . "\n";
      print "Response: " . $response->decoded_content . "\n";
      
      my $json_response = decode_json($response->decoded_content);
      use Data::Dumper;
      print Dumper($json_response);
  } else {
      print "Error: " . $response->status_line . "\n";
  }
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-code">
```
  {
      "status": 0,
      "msg": null,
      "code": null,
      "data": {
          "payoutMerchantId": null,
          "noOfPages": 1,
          "totalElements": 1,
          "currentPage": 0,
          "totalAmount": 0.0,
          "succesTxn": 0,
          "pendingTxn": 0,
          "transactionDetails": [
              {
                  "txnId": 71870,
                  "batchId": "smartSendBatch",
                  "merchantRefId": "0101010031",
                  "purpose": "Payout",
                  "amount": 1.0,
                  "txnStatus": "FAILED",
                  "txnSubStatus": null,
                  "txnSource": "SMART_SEND",
                  "txnDate": "2022-08-22T05:56:13.000+0000",
                  "scheduledTxnDate": "2022-08-22T05:56:13.000+0000",
                  "payuTransactionRefNo": "PAYOUT1661147773462lrSLcvHSc1K",
                  "beneficiaryName": "Customer",
                  "beneficiaryCardNo": null,
                  "msg": "Internal Error while validating vpa account",
                  "responseCode": null,
                  "transferType": "UPI",
                  "bankTransactionRefNo": null,
                  "nameWithBank": null,
                  "lastStatusUpdateDate": "2022-08-22T05:56:15.000+0000",
                  "succeedOn": null,
                  "fee": null,
                  "tax": null,
                  "txnStatusDescription": "Internal Error while validating vpa account",
                  "custom1": null,
                  "custom2": null,
                  "custom3": null,
                  "nameMatch": null
              }
          ]
      }
  }
  ```

  The status of a particular transaction has to be determined only from the field **txnStatus** in the**transactionDetails** JSON against the **merchantRefId**.

  On receiving the following JSON Response in the **Check Transfer Status** API, the transaction status is not determined and has to considered as **unidentified** or **Pending** by merchant.

  ```
  {
      "status": 0,
      "msg": null,
      "code": null,
      "data": {
          "payoutMerchantId": null,
          "noOfPages": 0,
          "totalElements": 0,
          "currentPage": 0,
          "totalAmount": 0.0,
          "succesTxn": 0,
          "pendingTxn": 0,
          "transactionDetails": []
      }
  }
  ```
</Accordion>


## Step 5. Integrate with webhooks

You can integrate with webhooks to track the status of your payment. For more information, refer to the [Payouts Webhooks](doc:payouts-webhooks).
