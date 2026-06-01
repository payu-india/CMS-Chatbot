---
title: Credit Card - Merchant Hosted Integration
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
The **pre_authorize** parameter is used to pre-authorize payments using the Merchant Hosted Checkout integration with the **_payment** API. This section describes the step-by-step procedure to integrate pre-authorize payments using credit cards.

<Callout icon="📘" theme="info">
  **Note**: You need to activate the Pre-Authorize Payments before you start using this integration. Contact your PayU Key Account Manager (KAM) to activate Pre-Authorize Payments.
</Callout>

<br />

<Callout icon="👍" theme="okay">
  Experience the end-to-end **Merchant Hosted Checkout** > **Cards** flow and instantly generate the complete code for seamless, zero-coding integration into your website. You need to select **Pre-Auth Payment API** on the left pane after you navigate to the PayU Labs using the following button:

  <br/>

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

                                        <button onclick="window.open('https://payu.in/integrationlab/seamless/cards', '_blank')" 
                                                class="tooltip-btn" 
                                                data-tooltip="Click here to see the Merchant Hosted Checkout > Cards end-to-end integration and instantly generate the complete code needed for a zero-coding setup on your website.">
                                            Experience the flow and get the code
                                        </button>
  `}</HTMLBlock>
</Callout>

<br />

**Steps to integrate**

<Cards columns={2}>
  <Card title="1. Post the Pre-Auth Transaction Request" href="#step-1-post-the-pre-auth-transaction-request">
    Submit the pre-authorization transaction request to PayU for payment hold
  </Card>

  <Card title="2. Check the Response from PayU" href="#step-2-check-the-response-from-payu">
    Handle and process the response received from PayU after pre-auth request submission
  </Card>

  <Card title="3. Capture a Pre-Authorized Payment" href="#step-3-capture-a-pre-authorized-payment">
    Complete the payment capture process for the pre-authorized transaction
  </Card>

  <Card title="4. Check Action Status" href="#step-4-check-action-status">
    Verify the status of the capture action and confirm transaction completion
  </Card>
</Cards>

## Step 1: Post the Pre-Auth transaction request

Post the additional parameters for with the Pre-Authorization using the Merchant Hosted Checkout. For complete list of parameters, refer to [Pre-Authorize Payment](ref:pre_authorize_payment) for the complete list parameters with **Try It** experience.

**Environment**

|                            |                                                                    |
| :------------------------- | :----------------------------------------------------------------- |
| **Test Environment**       | [https://test.payu.in/_payment](https://test.payu.in/_payment)     |
| **Production Environment** | [https://secure.payu.in/_payment](https://secure.payu.in/_payment) |

The **pre_authorize** parameter as specified is used to pre-authorize payments using the Merchant Hosted Checkout integration with the **_payment** API.

<Accordion title="Request parameters" icon="fa-code">
| Parameter | Description | Example |
|---|---|---|
| key<br/><code>mandatory</code> | <code>String</code> Merchant key provided by PayU during onboarding. | JP\*\*\*g |
| txnid<br/><code>mandatory</code> | <code>String</code> The transaction ID is a reference number for a specific order that is generated by the merchant. | sdlkfj394ru3495 |
| amount<br/><code>mandatory</code> | <code>String</code> The payment amount for the transaction. | 10.00 |
| productinfo<br/><code>mandatory</code> | <code>String</code> A brief description of the product. | iPhone |
| firstname<br/><code>mandatory</code> | <code>String</code> The first name of the customer. | Ashish |
| email<br/><code>mandatory</code> | <code>String</code> The email address of the customer. | ashish@abccorp.com |
| phone<br/><code>mandatory</code> | <code>String</code> The phone number of the customer. | |
| pg<br/><code>mandatory</code> | <code>String</code> The pg parameter determines which payment tabs will be displayed on the PayU page. For credit cards, 'CC' will be the value. | CC |
| bankcode<br/><code>mandatory</code> | <code>String</code> Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. For more information, refer to Card Type Codes and Supported Banks for Cards. | AMEX |
| ccnum<br/><code>mandatory</code> | <code>String</code> Use 13-19 digit card number for credit/debit cards (15 digits for AMEX, 13-19 for Maestro) and validate with LUHN algorithm. Refer to Card Number Formats and display error message on invalid input. | 5123456789012346 |
| ccname<br/><code>mandatory</code> | <code>String</code> This parameter must contain the name on card – as entered by the customer for the transaction. | Ashish Kumar |
| ccvv<br/><code>mandatory</code> | <code>String</code> Use 3-digit CVV number for credit/debit cards and 4-digit security code (4DBC/CID) for AMEX cards. Validate with BIN API. | 123 |
| ccexpmon<br/><code>mandatory</code> | <code>String</code> This parameter must contain the card's expiry month – as entered by the user for the transaction. It must always be in 2 digits or in MM format. For months 1-9, this parameter must be appended with 0 – like 01, 02…09. For months 10-12, this parameter must not be appended – It should be 10, 11 and 12 respectively. | 10 |
| ccexpyr<br/><code>mandatory</code> | <code>String</code> This parameter must contain the card's expiry year – as entered by the customer for the transaction. It must be of four digits. | 2021 |
| furl<br/><code>mandatory</code> | <code>String</code> The success URL, which is the page PayU will redirect to if the transaction is successful. | |
| surl<br/><code>mandatory</code> | <code>String</code> The Failure URL, which is the page PayU will redirect to if the transaction is failed. | |
| pre_authorize<br/><code>mandatory for Pre-Auth</code> | This parameter is set to **1** to pre-authorize payment using PayU Hosted Checkout. | |
| hash<br/><code>mandatory</code> | <code>String</code> It is the hash calculated by the merchant. The hash calculation logic is: <code>sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)</code> | |
| address1<br/><code>optional</code> | <code>String</code> The first line of the billing address. **For Fraud Detection**: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information. | |
| address2<br/><code>optional</code> | <code>String</code> The second line of the billing address. | |
| city<br/><code>optional</code> | <code>String</code> The city where your customer resides as part of the billing address. | |
| state<br/><code>optional</code> | <code>String</code> The state where your customer resides as part of the billing address. | |
| country<br/><code>optional</code> | <code>String</code> The country where your customer resides. | |
| zipcode<br/><code>optional</code> | <code>String</code> Billing address zip code is mandatory for the cardless EMI option. <code>Character Limit</code>: 20. | |
| udf1<br/><code>optional</code> | <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5. | |
| udf2<br/><code>optional</code> | <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5. | |
| udf3<br/><code>optional</code> | <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. | |
| udf4<br/><code>optional</code> | <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. | |
| udf5<br/><code>optional</code> | <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. | |

</Accordion>

<HashingRequestParameters />

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --request POST      --url 'https://test.payu.in/_payment?form=2'      --header 'Content-Type: application/x-www-form-urlencoded'      --header 'accept: text/plain'      --data key=JPM7Fg      --data pg=CC      --data bankcode=CC      --data pre_authorize=1      --data surl=https://test-payment-middleware.payu.in/simulatorResponse      --data furl=https://test-payment-middleware.payu.in/simulatorResponse      --data txnid=ypskjfdaaksdjfh      --data amount=10000      --data productinfo=iPhone      --data firstname=Ashish      --data email=ashish@gmail.com      --data phone=9889XXXXXX      --data ccnum=512*******012346      --data ccname=Ashish      --data ccexpmon=11      --data ccexpyr=2025      --data ccvv=123      --data hash=d99f230c19d781016fa64c57f976d0ec8ff3761fe5d9d6448933cf46d7177db6fb7b370e551e39dd37f2045a2a761f9065f8462838bbaad22963c083c84f9ced
  ```
  ```python
  import requests

  url = "https://test.payu.in/_payment?form=2"

  headers = {
      "accept": "text/plain",
      "Content-Type": "application/x-www-form-urlencoded"
  }

  data = {
      "key": "JPM7Fg",
      "pg": "CC",
      "bankcode": "CC",
      "pre_authorize": "1",
      "surl": "https://test-payment-middleware.payu.in/simulatorResponse",
      "furl": "https://test-payment-middleware.payu.in/simulatorResponse",
      "txnid": "ypskjfdaaksdjfh",
      "amount": "10000",
      "productinfo": "iPhone",
      "firstname": "Ashish",
      "email": "ashish@gmail.com",
      "phone": "9889XXXXXX",
      "ccnum": "512*******012346",
      "ccname": "Ashish",
      "ccexpmon": "11",
      "ccexpyr": "2025",
      "ccvv": "123",
      "hash": "d99f230c19d781016fa64c57f976d0ec8ff3761fe5d9d6448933cf46d7177db6fb7b370e551e39dd37f2045a2a761f9065f8462838bbaad22963c083c84f9ced"
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

  public class PayUPreAuthorizePayment {
      public static void main(String[] args) throws IOException, InterruptedException {
          String url = "https://test.payu.in/_payment?form=2";
          
          Map<String, String> formData = new LinkedHashMap<>();
          formData.put("key", "JPM7Fg");
          formData.put("pg", "CC");
          formData.put("bankcode", "CC");
          formData.put("pre_authorize", "1");
          formData.put("surl", "https://test-payment-middleware.payu.in/simulatorResponse");
          formData.put("furl", "https://test-payment-middleware.payu.in/simulatorResponse");
          formData.put("txnid", "ypskjfdaaksdjfh");
          formData.put("amount", "10000");
          formData.put("productinfo", "iPhone");
          formData.put("firstname", "Ashish");
          formData.put("email", "ashish@gmail.com");
          formData.put("phone", "9889XXXXXX");
          formData.put("ccnum", "512*******012346");
          formData.put("ccname", "Ashish");
          formData.put("ccexpmon", "11");
          formData.put("ccexpyr", "2025");
          formData.put("ccvv", "123");
          formData.put("hash", "d99f230c19d781016fa64c57f976d0ec8ff3761fe5d9d6448933cf46d7177db6fb7b370e551e39dd37f2045a2a761f9065f8462838bbaad22963c083c84f9ced");
          
          String formBody = formData.entrySet()
              .stream()
              .map(entry -> URLEncoder.encode(entry.getKey(), StandardCharsets.UTF_8) + "=" + 
                            URLEncoder.encode(entry.getValue(), StandardCharsets.UTF_8))
              .collect(Collectors.joining("&"));
          
          HttpClient client = HttpClient.newHttpClient();
          
          HttpRequest request = HttpRequest.newBuilder()
              .uri(URI.create(url))
              .header("accept", "text/plain")
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

  $url = "https://test.payu.in/_payment?form=2";

  $data = array(
      'key' => 'JPM7Fg',
      'pg' => 'CC',
      'bankcode' => 'CC',
      'pre_authorize' => '1',
      'surl' => 'https://test-payment-middleware.payu.in/simulatorResponse',
      'furl' => 'https://test-payment-middleware.payu.in/simulatorResponse',
      'txnid' => 'ypskjfdaaksdjfh',
      'amount' => '10000',
      'productinfo' => 'iPhone',
      'firstname' => 'Ashish',
      'email' => 'ashish@gmail.com',
      'phone' => '9889XXXXXX',
      'ccnum' => '512*******012346',
      'ccname' => 'Ashish',
      'ccexpmon' => '11',
      'ccexpyr' => '2025',
      'ccvv' => '123',
      'hash' => 'd99f230c19d781016fa64c57f976d0ec8ff3761fe5d9d6448933cf46d7177db6fb7b370e551e39dd37f2045a2a761f9065f8462838bbaad22963c083c84f9ced'
  );

  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      'accept: text/plain',
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

  my $url = "https://test.payu.in/_payment?form=2";

  my $ua = LWP::UserAgent->new;
  $ua->timeout(30);

  my %data = (
      'key'           => 'JPM7Fg',
      'pg'            => 'CC',
      'bankcode'      => 'CC',
      'pre_authorize' => '1',
      'surl'          => 'https://test-payment-middleware.payu.in/simulatorResponse',
      'furl'          => 'https://test-payment-middleware.payu.in/simulatorResponse',
      'txnid'         => 'ypskjfdaaksdjfh',
      'amount'        => '10000',
      'productinfo'   => 'iPhone',
      'firstname'     => 'Ashish',
      'email'         => 'ashish@gmail.com',
      'phone'         => '9889XXXXXX',
      'ccnum'         => '512*******012346',
      'ccname'        => 'Ashish',
      'ccexpmon'      => '11',
      'ccexpyr'       => '2025',
      'ccvv'          => '123',
      'hash'          => 'd99f230c19d781016fa64c57f976d0ec8ff3761fe5d9d6448933cf46d7177db6fb7b370e551e39dd37f2045a2a761f9065f8462838bbaad22963c083c84f9ced'
  );

  my $response = $ua->request(POST $url,
      Content_Type => 'application/x-www-form-urlencoded',
      Accept       => 'text/plain',
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
  The formatted sample response body is similar to the following, and you need to look for the following parameters:

  * PG\_TYPE: CC PG
  * bankcode: CC
  * **unamappedstatus: auth**

  ```
    {
    "mihpayid": "403993715531065775",
    "mode": "CC",
    "status": "success",
    "unmappedstatus": "captured",
    "key": "JPM7Fg",
    "txnid": "ypskjfdaaksdjfh",
    "amount": "10000.00",
    "cardCategory": "domestic",
    "discount": "0.00",
    "net_amount_debit": "10000",
    "addedon": "2024-02-26 07:20:56",
    "productinfo": "iPhone",
    "firstname": "Ashish",
    "lastname": "",
    "address1": "",
    "address2": "",
    "city": "",
    "state": "",
    "country": "",
    "zipcode": "",
    "email": "ashish@gmail.com",
    "phone": "9889843845",
    "udf1": "",
    "udf2": "",
    "udf3": "",
    "udf4": "",
    "udf5": "",
    "udf6": "",
    "udf7": "",
    "udf8": "",
    "udf9": "",
    "udf10": "",
    "hash": "00f188fdda2d60d418b147e7dce3a6ead172cf760a95a4df09b763f7627c01d867127e022de97841f1fe41cecb420b12b482fd8b68aaf66476b840bdfe82ca3c",
    "field1": "261005309469848160",
    "field2": "724760",
    "field3": "10000.00",
    "field4": "",
    "field5": "00",
    "field6": "02",
    "field7": "AUTHPOSITIVE",
    "field8": "AUTHORIZED",
    "field9": "Transaction is Successful",
    "payment_source": "payu",
    "PG_TYPE": "CC-PG",
    "bank_ref_num": "261005309469848160",
    "bankcode": "CC",
    "error": "E000",
    "error_Message": "No Error",
    "cardnum": "XXXXXXXXXXXX2346",
    "cardhash": "This field is no longer supported in postback params.",
    "splitInfo": "{"splitStatus":"splitNotReceived","splitSegments":[]}"
  }
  ```
</Accordion>

## Step 3: Capture a Pre-authorized payment

To capture a pre-authorized payment, use the following command. After the API command is successful, the transaction would be captured and settled to you.

**Environment**

| Environment            | URL                                                                                                  |
| :--------------------- | :--------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/merchant/postservice?form=2](https://test.payu.in/merchant/postservice?form=2) |
| Production Environment | [https://info.payu.in/merchant/postservice?form=2](https://info.payu.in/merchant/postservice?form=2) |

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
  ```plaintext
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
  **Notes**:

  * The **unamappedstatus** to **auth** can be checked using thje <Anchor label="Verify Payment API" target="_blank" href="ref:verify_payment_api">Verify Payment API</Anchor> and in callback response in the Transaction callback.
  * To check the status of the Auth Request and then Capture Request sent, use the **check_action_status** API. For more information,  refer to  <Anchor label="Check Refund Status API with Request ID" target="_blank" href="ref:check_action_status_api_with_request_id">Check Refund Status API with Request ID</Anchor>.
  * If you want to cancel or refund a pre-authorized payment, refer to [Cancel a Pre-Authorized Payment](doc:cancel-a-pre-authorized-payment).
</Callout>

<Callout icon="👍" theme="okay">
  **Reference**: For cancelling pre-auth payments, refer to <Anchor label="Cancel a Pre-Authorized Transaction API" target="_blank" href="ref:cancel-a-pre-authorized-transaction">Cancel a Pre-Authorized Transaction API</Anchor>.
</Callout>