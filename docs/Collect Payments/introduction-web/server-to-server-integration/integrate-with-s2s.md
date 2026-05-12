---
title: General Integration
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The Server-to-Server integration is performed at the server level, that is, your server (merchant server) and PayU server. The transaction is initiated from your server; hence redirection hop is eliminated. Since the details are captured on your page, customers gain confidence and enhance the checkout experience.

<Callout icon="📘" theme="info">
  **Note**: You must be **PCI-DSS** certified to use Server-to-Server integration. For more information on PCI-DSS certification, contact your Account Manager at PayU.
</Callout>

<br />

<Callout icon="👍" theme="okay">
  Experience the end-to-end **Merchant Hosted Checkout** > **Cards** flow and instantly generate the complete code for seamless, zero-coding integration into your website.

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

<Accordion title="Integration security" icon="fa-code">
  After receiving a response from PayU, you must calculate the hash again and validate it against the hash that you sent in the request to ensure the transaction is secure. PayU recommends implementing the transaction details APIs and **webhook**/**callbac**k as an extra security measure. You can find more information on this process in the [Transaction Detail APIs](ref:transaction-detail-apis) and [Webhooks](doc:webhooks) documentation.

  You need to ensure that sensitive information related to the integration is not part of the payment request to PayU. The details including — but are not limited to — the following are considered sensitive information:

  * <Glossary>Salt</Glossary> value
  * plain text hash string

  Along with the request, the sensitive information should not be a part of any merchant-level URL. The following are considered sources for the merchant-level URL:

  * The last web address accessed by a browser before loading PayU's checkout page.
  * URLs shared as part of payment request to PayU in the parameters: surl, furl, curl, nurl, and termUrl.
  * Notification URLs configured with the merchant account.
  * Invoice Completion URLs configured with the merchant account.

  <Callout icon="📘" theme="info">
    **Note**: It is important to compare the parameters sent by PayU in the response with the ones you sent in the request to make sure none of them have been changed. You should verify specific parameters such as the transaction ID and amount. PayU is not responsible for any security breaches or losses resulting from your failure to implement the necessary security measures.
  </Callout>

  ***
</Accordion>

**Steps to integrate**

<Cards columns={2}>
  <Card title="1. Post the parameters to PayU" href="https://docs.payu.in/docs/integrate-with-s2s#step-1-post-the-parameters-to-payu">
    Post the transaction parameters to PayU server to initiate the payment process
  </Card>

  <Card title="2. Check response from PayU" href="https://docs.payu.in/docs/integrate-with-s2s#step-2-check-response-from-payu">
    Check and process the response received from PayU after payment processing
  </Card>

  <Card title="3. Verify the payment" href="https://docs.payu.in/docs/integrate-with-s2s#step-3-verify-the-payment">
    Verify the payment using verify\_payment and monitor using webhooks
  </Card>
</Cards>

## Step 1: Post the parameters to PayU

The first request from you to PayU with the required transaction mandatory/ optional parameters. This needs to be a server-to-server Curl call request. For the sample request and response,  refer to  [Collect Payment - General Integration](ref:_payment_s2s_classic_integration) .

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
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String`Merchant key provided by PayU during onboarding.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          txnid
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String`The transaction ID is a reference number for a specific order that is generated by the merchant.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          amount  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String`The payment amount for the transaction.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          productinfo  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String`A brief description of the product.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          firstname  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` The first name of the customer.
        </td>

        <td style={{ textAlign: "left" }}>
          Ashish
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          email
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String`The email address of the customer.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          phone
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String`The phone number of the customer.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          pg
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` The pg parameter determines which payment tabs will be displayed on the PayU page. For cards, 'CC' will be the value.
        </td>

        <td style={{ textAlign: "left" }}>
          CC
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          bankcode `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. For more information, refer to <a href="card-type-codes-and-supported-banks-for-cards" target="_blank"> Card Type Codes and Supported Banks for Cards</a>.
        </td>

        <td style={{ textAlign: "left" }}>
          AMEX
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          ccnum
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` Use 13-19 digit card number for credit/debit cards (15 digits for AMEX, 13-19 for Maestro) and validate with LUHN algorithm. Refer to  <a href="card-number-formats" target="_blank"> Card Number Formats</a> and display error message on invalid input.
        </td>

        <td style={{ textAlign: "left" }}>
          5123456789012346
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          ccname  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter must contain the name on card – as entered by the customer for the transaction.
        </td>

        <td style={{ textAlign: "left" }}>
          Ashish Kumar
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          ccvv
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` Use 3-digit CVV number for credit/debit cards and 4-digit security code (4DBC/CID) for AMEX cards. Validate with BIN API.
        </td>

        <td style={{ textAlign: "left" }}>
          123
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          ccexpmon  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter must contain the card's expiry month – as entered by the user for the transaction. It must always be in 2 digits or in MM format. For months 1-9, this parameter must be appended with 0 – like 01, 02…09. For months 10-12, this parameter must not be appended – It should be 10,11 and 12 respectively.
        </td>

        <td style={{ textAlign: "left" }}>
          10
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          ccexpyr
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter must contain the card's expiry year – as entered by the customer for the transaction. It must be of four digits.
        </td>

        <td style={{ textAlign: "left" }}>
          2021
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          furl
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String`The success URL, which is the page PayU will redirect to if the transaction is successful.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          surl
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String`The Failure URL, which is the page PayU will redirect to if the transaction is failed.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          hash
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String`It is the hash calculated by the merchant. The hash calculation logic is:
          `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)`
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          txn\_s2s\_flow
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String`This parameter must be passed with the value as:

          * **4**for Legacy Decoupled flow.
          * **3** for Direct Authorization.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          address1
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` The first line of the billing address.

          * *For Fraud Detection*\*: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          address2
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` The second line of the billing address.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          city
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` The city where your customer resides as part of the billing address.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          state
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` The state where your customer resides as part of the billing address,
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          country
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` The country where your customer resides.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          zipcode
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` Billing address zip code is mandatory for the cardless EMI option.
          `Character Limit`-20
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          udf1
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          udf2
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          udf3
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          udf4
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          udf5
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>
    </tbody>
  </Table>

  <HashingRequestParameters />
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/_payment
  -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d

  "key=JP***g&txnid=tJA4IWme0jIsDw&amount=10.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cc&bankcode=cc&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=5123456789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=&txn_s2s_flow=4&hash=36b4ab309154a9cbc0a0b9829c086a196cb2edd758b1e918cf7f20fbc1f596f17cc4ba5682eee32317365c99e8b461692595328eea7bb9c6e689bc4b923abe81"
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
      "txnid": "tJA4IWme0jIsDw",
      "amount": "10.00",
      "firstname": "PayU User",
      "email": "test@gmail.com",
      "phone": "9876543210",
      "productinfo": "iPhone",
      "pg": "cc",
      "bankcode": "cc",
      "surl": "https://apiplayground-response.herokuapp.com/",
      "furl": "https://apiplayground-response.herokuapp.com/",
      "ccnum": "5123456789012346",
      "ccexpmon": "05",
      "ccexpyr": "2022",
      "ccvv": "123",
      "ccname": "",
      "txn_s2s_flow": "4",
      "hash": "36b4ab309154a9cbc0a0b9829c086a196cb2edd758b1e918cf7f20fbc1f596f17cc4ba5682eee32317365c99e8b461692595328eea7bb9c6e689bc4b923abe81"
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

  public class PayUCreditCardS2SPayment {
      public static void main(String[] args) throws IOException, InterruptedException {
          String url = "https://test.payu.in/_payment";
          
          Map<String, String> formData = new LinkedHashMap<>();
          formData.put("key", "JP***g");
          formData.put("txnid", "tJA4IWme0jIsDw");
          formData.put("amount", "10.00");
          formData.put("firstname", "PayU User");
          formData.put("email", "test@gmail.com");
          formData.put("phone", "9876543210");
          formData.put("productinfo", "iPhone");
          formData.put("pg", "cc");
          formData.put("bankcode", "cc");
          formData.put("surl", "https://apiplayground-response.herokuapp.com/");
          formData.put("furl", "https://apiplayground-response.herokuapp.com/");
          formData.put("ccnum", "5123456789012346");
          formData.put("ccexpmon", "05");
          formData.put("ccexpyr", "2022");
          formData.put("ccvv", "123");
          formData.put("ccname", "");
          formData.put("txn_s2s_flow", "4");
          formData.put("hash", "36b4ab309154a9cbc0a0b9829c086a196cb2edd758b1e918cf7f20fbc1f596f17cc4ba5682eee32317365c99e8b461692595328eea7bb9c6e689bc4b923abe81");
          
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
      'txnid' => 'tJA4IWme0jIsDw',
      'amount' => '10.00',
      'firstname' => 'PayU User',
      'email' => 'test@gmail.com',
      'phone' => '9876543210',
      'productinfo' => 'iPhone',
      'pg' => 'cc',
      'bankcode' => 'cc',
      'surl' => 'https://apiplayground-response.herokuapp.com/',
      'furl' => 'https://apiplayground-response.herokuapp.com/',
      'ccnum' => '5123456789012346',
      'ccexpmon' => '05',
      'ccexpyr' => '2022',
      'ccvv' => '123',
      'ccname' => '',
      'txn_s2s_flow' => '4',
      'hash' => '36b4ab309154a9cbc0a0b9829c086a196cb2edd758b1e918cf7f20fbc1f596f17cc4ba5682eee32317365c99e8b461692595328eea7bb9c6e689bc4b923abe81'
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
      'key'          => 'JP***g',
      'txnid'        => 'tJA4IWme0jIsDw',
      'amount'       => '10.00',
      'firstname'    => 'PayU User',
      'email'        => 'test@gmail.com',
      'phone'        => '9876543210',
      'productinfo'  => 'iPhone',
      'pg'           => 'cc',
      'bankcode'     => 'cc',
      'surl'         => 'https://apiplayground-response.herokuapp.com/',
      'furl'         => 'https://apiplayground-response.herokuapp.com/',
      'ccnum'        => '5123456789012346',
      'ccexpmon'     => '05',
      'ccexpyr'      => '2022',
      'ccvv'         => '123',
      'ccname'       => '',
      'txn_s2s_flow' => '4',
      'hash'         => '36b4ab309154a9cbc0a0b9829c086a196cb2edd758b1e918cf7f20fbc1f596f17cc4ba5682eee32317365c99e8b461692595328eea7bb9c6e689bc4b923abe81'
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

## Step 2: Check response from PayU

<Accordion title="Sample response" icon="fa-code">
  ```
  {
    "metaData": {
      "message": null,
      "referenceId": "2710cd2a20e08a006034861feea27f084a425e94920df9b1856eb6e90793067b",
      "statusCode": "E000",
      "txnId": "payuTestTransaction2909041",
      "unmappedStatus": "captured"
    },
    "result": {
      "mihpayid": "412345678912362515",
      "mode": "CC",
      "status": "success",
      "key": "J****g",
      "txnid": "payuTestTransaction2909041",
      "amount": "100",
      "addedon": "2020-06-09 16:54:26",
      "productinfo": "Product Info",
      "firstname": "Postman",
      "lastname": "",
      "address1": "",
      "address2": "",
      "city": "",
      "state": "",
      "country": "",
      "zipcode": "",
      "email": "test@payu.in",
      "phone": "9123456781",
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
      "card_no": "XXXXXXXXXXXX2346",
      "field0": "",
      "field1": "",
      "field2": "",
      "field3": "",
      "field4": "",
      "field5": "NW9WYkV0dzJCclpsMWNRbzg0VVk=",
      "field6": "02",
      "field7": "AUTHPOSITIVE",
      "field8": "",
      "field9": "Successful Transaction",
      "payment_source": "payuPureS2SAuth",
      "PG_TYPE": "CC-PG",
      "error": "E000",
      "error_Message": "Success",
      "unmappedstatus": "captured",
      "hash": "df540d8fc8265e9382415993e468cfe0884574ddc617b96053082195752e11e4405888bb96030e749be780805dcf8499241a3c51fb26f978cdb6d328cda2a138",
      "bank_ref_num": "",
      "bankcode": "CC"
    }
  }
  Next Steps
  ```
</Accordion>

<Accordion title="Response Parameters" icon="fa-code">
  <Callout icon="📘" theme="info">
    **Note**: The response contains a combination of the following JSON objects (**metaData**, **result**, and binData) based on the use case used in S2S, and the fields in each of them are described in the following tables.
  </Callout>

  Collect the response in the  [Collect Payment API - Server-to-Server](ref:_payment_s2s_classic_integration)  under API Reference. The response for the S2S payment request is not similar to Merchant Hosted or PayU Hosted Checkout. For description of response parameters,  refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).
</Accordion>

## Step 3. Verify the payment

<Verify_Payment_Tabs />
