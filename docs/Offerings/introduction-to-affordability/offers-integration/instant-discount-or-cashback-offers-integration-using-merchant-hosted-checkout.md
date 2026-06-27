---
title: >-
  Integrate Offers (Instant Discount, Cashback, No Cost, Low-Cost EMI) for
  Merchant Hosted
deprecated: false
hidden: false
metadata:
  title: >-
    Instant Discount or Cashback using Merchant Hosted Checkout - Offers
    Integration
  description: ''
  keywords:
    - Integrate an Instant Discount Offer with Merchant Hosted Checkout
    - Integrate Merchant Hosted Checkout with Cashback Offer
    - Integrate Cashback Offer with Seamless Integration
    - Instant Discount Offer with Seamless Integration
    - Integrating Instant Discount Offers with Merchant Hosted Checkout
    - Integrate an Cashback Offer with Merchant Hosted Checkout
    - Integrate Merchant Hosted Checkout Cashback Offer
    - Integrate a Cashback Offer with Seamless Integration
    - Cashback Offer with Seamless Integration
    - Integrating Cashback Offers with Merchant Hosted Checkout
    - Cash Back Offer Integration
  robots: index
next:
  description: ''
---
With the Merchant Hosted Checkout integration, the entire payment experience can be controlled by merchants and PayU provides APIs to power this checkout experience. This section provides the step-by-step procedure to integrate PayU's Offer Engine with Merchant Hosted Checkout integration, which enables you to display, validate, and apply various offers including instant discounts, cashback, and EMI options throughout your customer's journey.<br />With this integration, you are not limited to showing offers only at checkout—you can surface them anywhere in your app or website where they make sense, whether that's on product pages, cart screens, or a dedicated offer section.

## Customer journey on Merchant Hosted Checkout

The following video walks through the customer journey:

<Embed title="" typeOfEmbed="youtube" url="https://www.youtube.com/watch?v=tRRbSzk9Egg" href="https://www.youtube.com/watch?v=tRRbSzk9Egg" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252FtRRbSzk9Egg%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DtRRbSzk9Egg%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252FtRRbSzk9Egg%252Fhqdefault.jpg%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" providerName="YouTube" providerUrl="https://www.youtube.com/" />

<br />

The steps involved in the customer journey are:

- **Step 1**: Login
  Your customer logs into your app or website. At this point, they're just browsing.

- **Step 2**: Product Selection
  The customer adds products or services to their cart. This is your first opportunity to show relevant offers using the **Fetch Offers** API, potentially influencing their purchase decision before they even reach checkout.

- **Step 3**: Checkout and Offer Discovery
  When the customer lands on your checkout page, you'll call the Fetch Offers API to retrieve all applicable offers for their specific transaction. PayU returns everything you need to display the offer attractively, including the title, description, terms and conditions, applicable payment methods, and the actual discount or cashback value. Think of this API as your offer catalog for this particular transaction.

- **Step 4**: Payment Method Selection and Validation
  After the customer chooses their preferred payment method and enters the required details, you must use the **Validate Offer** API to confirm whether the selected offer will actually apply to this transaction. This validation step is crucial because it prevents customer disappointment at the final stage.

  For EMI-specific flows, there's an additional step. When a customer selects EMI (whether credit card, debit card, or cardless EMI), you'll first call the **Calculate EMI** API. This API returns all available EMI plans along with applicable offers, letting you display complete pricing information upfront. You can call this API not just at checkout but anywhere you want to show EMI options, such as product detail pages. After the customer selects an EMI plan and completes their payment details, you'll then call the **Validate Offer** API to ensure the EMI offer will be honored.

- **Step 5**: Payment Initiation
  You initiate the actual payment using the payment API, passing along the validated offer. The behavior differs based on offer type. For instant discounts, the transaction amount is reduced immediately. For cashback, the full amount is charged but the customer receives credit later.

- **Step 6**: Two-Factor Authentication
  The customer completes their bank's 2FA process on the adjusted amount (reduced amount for instant discount, original amount for cashback).

- **Step 7**: Return to your Site.<br />After successful payment, the customer is redirected back to your app or website.

<Callout icon="👍" theme="okay">
  ###

  **Tip**: You're not limited to showing offers only at checkout. Consider using the **Fetch Offers** API on product pages to highlight "Buy now and get 10% instant discount" messaging, on cart pages to encourage completion, or in a dedicated offers section to drive engagement.
</Callout>

## Integration steps

To integrate offers using Merchant Hosted Checkout integration:

<Callout icon="❗️" theme="error">
  ###

  **Prerequisites**: Before starting, ensure you're familiar with the standard Merchant Hosted Checkout workflow. If you haven't implemented basic checkout yet, refer to the Merchant Hosted Checkout documentation first. For the Merchant Hosted Checkout workflow, refer [Merchant Hosted Checkout](doc:custom-checkout-merchant-hosted)
</Callout>

### Step 1: Fetch Offers

The first step is to retrieve offers using the **Fetch Offers** API, which you can call at multiple points in your user journey. This API returns a comprehensive list of offers applicable to the transaction context you provide.

**Where to implement this**: checkout page (essential), product detail pages (recommended for conversion), cart page (recommended), or a dedicated offers page (optional but valuable for discovery). For complete API specifications and request parameters, refer to [Fetch Offers API](ref:fetch-offers-api).

### Step 2: Calculate EMI plans with offers

If your checkout supports EMI as a payment option, there is a specialized API you need to integrate before the validation step. The Calculate EMI API is specifically designed for EMI transactions and serves a different purpose than the Fetch Offers API you used in [Step 1](#step-1-fetch-offers).

When a customer selects EMI as their payment method, whether through credit card, debit card, or cardless EMI, they need to see the available EMI plans along with any applicable offers before making their final decision. The **Calculate EMI** API returns the complete EMI breakdown including tenure options, monthly installment amounts, interest rates, and any EMI-specific offers that can be applied. For complete API specification and request parameters, refer to [EMI Calculator API](https://docs.payu.in/reference/emi-calculator-api).

### Step 3: Validate Offer

Use the **Validate Offer** API to validate if the offer will be applied on this transaction or not. For more information, refer to [Validate Offer API](ref:validate-offer-api).

### Step 4: Make Payment

Make the payment request using the **\_payment** API using the following additional parameters for Offers. For more information on the complete list of parameters to be posted, refer to  <Anchor target="_blank" href="ref:_payment_merchant_hosted">Collect Payment API - Merchant Hosted Checkout</Anchor>

<Accordion title="Request Parameters" icon="fa-table">
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
          `String` Merchant key provided by PayU during onboarding.
        </td>

        <td style={{ textAlign: "left" }}>
          vqpS7W
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          txnid
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` The transaction ID is a reference number for a specific order that is generated by the merchant. Must be unique for each transaction.
        </td>

        <td style={{ textAlign: "left" }}>
          Txn\_050220260127
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          amount
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` The payment amount for the transaction.
        </td>

        <td style={{ textAlign: "left" }}>
          500
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          productinfo
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` A brief description of the product or service.
        </td>

        <td style={{ textAlign: "left" }}>
          iPhone
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          firstname
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` The first name of the customer.
        </td>

        <td style={{ textAlign: "left" }}>
          Test User
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          email
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` The email address of the customer.
        </td>

        <td style={{ textAlign: "left" }}>
          [test@gmail.com](mailto:test@gmail.com)
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          phone
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` The phone number of the customer.
        </td>

        <td style={{ textAlign: "left" }}>
          9876543210
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          surl
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` The success URL, which is the page PayU will redirect to if the transaction is successful.
        </td>

        <td style={{ textAlign: "left" }}>
          [https://test.payu.in/admin/test\_response](https://test.payu.in/admin/test_response)
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          furl
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` The failure URL, which is the page PayU will redirect to if the transaction fails.
        </td>

        <td style={{ textAlign: "left" }}>
          [https://test.payu.in/admin/test\_response](https://test.payu.in/admin/test_response)
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          hash
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` Hash calculated for transaction security. For offers, use the following order:
          `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|offer_key|offer_auto_apply|SALT)`

          **Note**: If any of the keys is null/not configured, the `|` character must still be concatenated.
        </td>

        <td style={{ textAlign: "left" }}>
          3f1b738fe8485e21d2b...
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          pg
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` The pg parameter determines which payment type will be used. For more information, refer to <a href="https://docs.payu.in/docs/bank-and-card-codes-for-integration">Bank and Card Codes for Integration</a>.
        </td>

        <td style={{ textAlign: "left" }}>
          CC
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          bankcode
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` Each payment option is identified with a unique bank code at PayU. For more information, refer to <a href="https://docs.payu.in/docs/bank-and-card-codes-for-integration">Bank and Card Codes for Integration</a>.
        </td>

        <td style={{ textAlign: "left" }}>
          CC
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          offer\_key
          `mandatory for Offers`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` The offer key identifier to apply a specific offer to the transaction. Use the Fetch Offer API to fetch the list offers and corresponding offer key as described in <a href="#step-1-fetch-offers">Step 1: Fetch Offers</a>.
        </td>

        <td style={{ textAlign: "left" }}>
          flat150Off\@03q62aqtF34n
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          offer\_auto\_apply
          `mandatory for Offers`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` Set to `true` to automatically apply the best available offer. If set to `false`, only the specified `offer_key` will be applied.
        </td>

        <td style={{ textAlign: "left" }}>
          true
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          api\_version
          `mandatory for offers`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` The API version of the `_payment` API. Must be `14` or later for offers integration.
        </td>

        <td style={{ textAlign: "left" }}>
          14
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          user\_token
          `mandatory for UPI/NB/Wallet`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` Used by the offer engine to apply velocity rules at a user level. Format: `merchant_key:unique_user_identifier`.

          * **Card Based Offers (CC, DC, EMI)**: If this parameter is passed, velocity rules are applied on this token; if not passed, the same is applied on the card number.
          * **UPI, NB, Wallet**: Mandatory for these payment modes. If not passed, validation rules will not apply.
        </td>

        <td style={{ textAlign: "left" }}>
          vqpS7W:test123
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>

<Callout icon="📘" theme="info">
  ### Notes:

  - The following order must be used for hashing:
    `key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|offer_key|offer_auto_apply|SALT`
    For more information on hash generation process, refer to [Hashing Request and Response](ref:generate-hash-merchant-hosted).
  - If any of the keys is null/not configured, "|" character must be concatenated.
  - The above hash logic is for \_payment API version 10 or later
</Callout>

<Accordion title="Sample Request" icon="fa-code">
  **Sample Request with cart\_details JSON object**

  ```curl
  curl --location 'https://test.payu.in/_payment' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'Cookie: PHPSESSID=iafp415uqvlrr9k7l7u7t9sqg1; USERTXNINFO=696f17aec44136.43043592' \
  --data-urlencode 'key=vqpS7W' \
  --data-urlencode 'txnid=Txn_050220260127' \
  --data-urlencode 'amount=500' \
  --data-urlencode 'productinfo=iPhone' \
  --data-urlencode 'firstname=Test User' \
  --data-urlencode 'email=test@gmail.com' \
  --data-urlencode 'phone=9876543210' \
  --data-urlencode 'surl=https://test.payu.in/admin/test_response' \
  --data-urlencode 'furl=https://test.payu.in/admin/test_response' \
  --data-urlencode 'hash=3f1b738fe8485e21d2b2087d4bfbfff5357de76f234d932d31c9073e17353bf80eadef62cb287f449f590323f31a3928a2234e328c8a334a5c15a7a2f381a3f1' \
  --data-urlencode 'offer_key=flat150Off@03q62aqtF34n' \
  --data-urlencode 'offer_auto_apply=true' \
  --data-urlencode 'api_version=14' \
  --data-urlencode 'user_token=vqpS7W:test123' \
  --data-urlencode 'pg=CC' \
  --data-urlencode 'bankcode=CC' \
  --data-urlencode 'ccnum=5123456789012346' \
  --data-urlencode 'ccname=Test' \
  --data-urlencode 'ccvv=123' \
  --data-urlencode 'ccexpmon=05' \
  --data-urlencode 'ccexpyr=2026'
  ```
  ```javascript
  async function makePayUPayment() {
      const url = "https://test.payu.in/_payment";
      
      const formData = new URLSearchParams();
      formData.append('key', 'vqpS7W');
      formData.append('txnid', 'Txn_050220260127');
      formData.append('amount', '500');
      formData.append('productinfo', 'iPhone');
      formData.append('firstname', 'Test User');
      formData.append('email', 'test@gmail.com');
      formData.append('phone', '9876543210');
      formData.append('surl', 'https://test.payu.in/admin/test_response');
      formData.append('furl', 'https://test.payu.in/admin/test_response');
      formData.append('hash', '3f1b738fe8485e21d2b2087d4bfbfff5357de76f234d932d31c9073e17353bf80eadef62cb287f449f590323f31a3928a2234e328c8a334a5c15a7a2f381a3f1');
      formData.append('offer_key', 'flat150Off@03q62aqtF34n');
      formData.append('offer_auto_apply', 'true');
      formData.append('api_version', '14');
      formData.append('user_token', 'vqpS7W:test123');
      formData.append('pg', 'CC');
      formData.append('bankcode', 'CC');
      formData.append('ccnum', '5123456789012346');
      formData.append('ccname', 'Test');
      formData.append('ccvv', '123');
      formData.append('ccexpmon', '05');
      formData.append('ccexpyr', '2026');
      
      try {
          const response = await fetch(url, {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/x-www-form-urlencoded'
              },
              body: formData
          });
          
          const responseText = await response.text();
          console.log(`Status Code: ${response.status}`);
          console.log(`Response: ${responseText}`);
          return response;
      } catch (error) {
          console.error(`Error occurred: ${error.message}`);
          return null;
      }
  }

  makePayUPayment();
  ```
  ```python
  import requests

  def make_payu_payment():
      url = "https://test.payu.in/_payment"
      
      data = {
          'key': 'vqpS7W',
          'txnid': 'Txn_050220260127',
          'amount': '500',
          'productinfo': 'iPhone',
          'firstname': 'Test User',
          'email': 'test@gmail.com',
          'phone': '9876543210',
          'surl': 'https://test.payu.in/admin/test_response',
          'furl': 'https://test.payu.in/admin/test_response',
          'hash': '3f1b738fe8485e21d2b2087d4bfbfff5357de76f234d932d31c9073e17353bf80eadef62cb287f449f590323f31a3928a2234e328c8a334a5c15a7a2f381a3f1',
          'offer_key': 'flat150Off@03q62aqtF34n',
          'offer_auto_apply': 'true',
          'api_version': '14',
          'user_token': 'vqpS7W:test123',
          'pg': 'CC',
          'bankcode': 'CC',
          'ccnum': '5123456789012346',
          'ccname': 'Test',
          'ccvv': '123',
          'ccexpmon': '05',
          'ccexpyr': '2026'
      }
      
      headers = {
          'Content-Type': 'application/x-www-form-urlencoded'
      }
      
      try:
          response = requests.post(url, data=data, headers=headers)
          print(f"Status Code: {response.status_code}")
          print(f"Response: {response.text}")
          return response
      except requests.exceptions.RequestException as e:
          print(f"Error occurred: {e}")
          return None

  make_payu_payment()
  ```
  ```php
  <?php

  function makePayUPayment() {
      $url = "https://test.payu.in/_payment";
      
      $data = array(
          'key' => 'vqpS7W',
          'txnid' => 'Txn_050220260127',
          'amount' => '500',
          'productinfo' => 'iPhone',
          'firstname' => 'Test User',
          'email' => 'test@gmail.com',
          'phone' => '9876543210',
          'surl' => 'https://test.payu.in/admin/test_response',
          'furl' => 'https://test.payu.in/admin/test_response',
          'hash' => '3f1b738fe8485e21d2b2087d4bfbfff5357de76f234d932d31c9073e17353bf80eadef62cb287f449f590323f31a3928a2234e328c8a334a5c15a7a2f381a3f1',
          'offer_key' => 'flat150Off@03q62aqtF34n',
          'offer_auto_apply' => 'true',
          'api_version' => '14',
          'user_token' => 'vqpS7W:test123',
          'pg' => 'CC',
          'bankcode' => 'CC',
          'ccnum' => '5123456789012346',
          'ccname' => 'Test',
          'ccvv' => '123',
          'ccexpmon' => '05',
          'ccexpyr' => '2026'
      );
      
      $ch = curl_init();
      
      curl_setopt($ch, CURLOPT_URL, $url);
      curl_setopt($ch, CURLOPT_POST, true);
      curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
      curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
      curl_setopt($ch, CURLOPT_HTTPHEADER, array(
          'Content-Type: application/x-www-form-urlencoded'
      ));
      
      $response = curl_exec($ch);
      
      if (curl_errno($ch)) {
          echo 'Error occurred: ' . curl_error($ch) . PHP_EOL;
          curl_close($ch);
          return false;
      }
      
      $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
      
      echo "Status Code: " . $httpCode . PHP_EOL;
      echo "Response: " . $response . PHP_EOL;
      
      curl_close($ch);
      return $response;
  }

  makePayUPayment();
  ?>
  ```
  ```java
  import java.io.*;
  import java.net.*;
  import java.nio.charset.StandardCharsets;
  import java.util.*;

  public class PayUPayment {
      
      public static void main(String[] args) {
          try {
              makePayUPayment();
          } catch (Exception e) {
              System.err.println("Error occurred: " + e.getMessage());
              e.printStackTrace();
          }
      }
      
      public static void makePayUPayment() throws Exception {
          String url = "https://test.payu.in/_payment";
          
          Map<String, String> parameters = new LinkedHashMap<>();
          parameters.put("key", "vqpS7W");
          parameters.put("txnid", "Txn_050220260127");
          parameters.put("amount", "500");
          parameters.put("productinfo", "iPhone");
          parameters.put("firstname", "Test User");
          parameters.put("email", "test@gmail.com");
          parameters.put("phone", "9876543210");
          parameters.put("surl", "https://test.payu.in/admin/test_response");
          parameters.put("furl", "https://test.payu.in/admin/test_response");
          parameters.put("hash", "3f1b738fe8485e21d2b2087d4bfbfff5357de76f234d932d31c9073e17353bf80eadef62cb287f449f590323f31a3928a2234e328c8a334a5c15a7a2f381a3f1");
          parameters.put("offer_key", "flat150Off@03q62aqtF34n");
          parameters.put("offer_auto_apply", "true");
          parameters.put("api_version", "14");
          parameters.put("user_token", "vqpS7W:test123");
          parameters.put("pg", "CC");
          parameters.put("bankcode", "CC");
          parameters.put("ccnum", "5123456789012346");
          parameters.put("ccname", "Test");
          parameters.put("ccvv", "123");
          parameters.put("ccexpmon", "05");
          parameters.put("ccexpyr", "2026");
          
          URL obj = new URL(url);
          HttpURLConnection connection = (HttpURLConnection) obj.openConnection();
          connection.setRequestMethod("POST");
          connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
          connection.setDoOutput(true);
          
          StringBuilder formData = new StringBuilder();
          for (Map.Entry<String, String> entry : parameters.entrySet()) {
              if (formData.length() > 0) formData.append("&");
              formData.append(URLEncoder.encode(entry.getKey(), StandardCharsets.UTF_8.toString()));
              formData.append("=");
              formData.append(URLEncoder.encode(entry.getValue(), StandardCharsets.UTF_8.toString()));
          }
          
          try (DataOutputStream wr = new DataOutputStream(connection.getOutputStream())) {
              wr.writeBytes(formData.toString());
              wr.flush();
          }
          
          int responseCode = connection.getResponseCode();
          System.out.println("Status Code: " + responseCode);
          
          BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
          String inputLine;
          StringBuilder response = new StringBuilder();
          while ((inputLine = in.readLine()) != null) {
              response.append(inputLine);
          }
          in.close();
          
          System.out.println("Response: " + response.toString());
      }
  }
  ```
  ```csharp
  using System;
  using System.Collections.Generic;
  using System.Net.Http;
  using System.Threading.Tasks;

  class Program
  {
      private static readonly HttpClient client = new HttpClient();

      static async Task Main(string[] args)
      {
          await MakePayUPayment();
      }

      static async Task MakePayUPayment()
      {
          string url = "https://test.payu.in/_payment";
          
          var formParams = new List<KeyValuePair<string, string>>
          {
              new KeyValuePair<string, string>("key", "vqpS7W"),
              new KeyValuePair<string, string>("txnid", "Txn_050220260127"),
              new KeyValuePair<string, string>("amount", "500"),
              new KeyValuePair<string, string>("productinfo", "iPhone"),
              new KeyValuePair<string, string>("firstname", "Test User"),
              new KeyValuePair<string, string>("email", "test@gmail.com"),
              new KeyValuePair<string, string>("phone", "9876543210"),
              new KeyValuePair<string, string>("surl", "https://test.payu.in/admin/test_response"),
              new KeyValuePair<string, string>("furl", "https://test.payu.in/admin/test_response"),
              new KeyValuePair<string, string>("hash", "3f1b738fe8485e21d2b2087d4bfbfff5357de76f234d932d31c9073e17353bf80eadef62cb287f449f590323f31a3928a2234e328c8a334a5c15a7a2f381a3f1"),
              new KeyValuePair<string, string>("offer_key", "flat150Off@03q62aqtF34n"),
              new KeyValuePair<string, string>("offer_auto_apply", "true"),
              new KeyValuePair<string, string>("api_version", "14"),
              new KeyValuePair<string, string>("user_token", "vqpS7W:test123"),
              new KeyValuePair<string, string>("pg", "CC"),
              new KeyValuePair<string, string>("bankcode", "CC"),
              new KeyValuePair<string, string>("ccnum", "5123456789012346"),
              new KeyValuePair<string, string>("ccname", "Test"),
              new KeyValuePair<string, string>("ccvv", "123"),
              new KeyValuePair<string, string>("ccexpmon", "05"),
              new KeyValuePair<string, string>("ccexpyr", "2026")
          };

          var formContent = new FormUrlEncodedContent(formParams);
          
          try
          {
              HttpResponseMessage response = await client.PostAsync(url, formContent);
              string responseBody = await response.Content.ReadAsStringAsync();
              
              Console.WriteLine($"Status Code: {response.StatusCode}");
              Console.WriteLine($"Response: {responseBody}");
          }
          catch (HttpRequestException e)
          {
              Console.WriteLine($"Error occurred: {e.Message}");
          }
      }
  }
  ```
</Accordion>

### Step 5: Check the response from PayU

Check the following response parameters (for Offers) from PayU to handle the payment response, as the net amount debit may be different from the amount sent by you in the request.

<Accordion title="Response Parameters specific to Offers" icon="fa-reply">
  <Table align={["left","left","left"]}>
    <thead>
      <tr>
        <th style={{ textAlign: "left" }}>
          **Parameter**
        </th>

        <th style={{ textAlign: "left" }}>
          **Description**
        </th>

        <th style={{ textAlign: "left" }}>
          **Example**
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td style={{ textAlign: "left" }}>
          discount
        </td>

        <td style={{ textAlign: "left" }}>
          This will specify the offer value provided to the user.
        </td>

        <td style={{ textAlign: "left" }}>
          10.00
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          net\_amount\_debit
        </td>

        <td style={{ textAlign: "left" }}>
          This will specify the actual amount deducted from the customer’s payment instrument. In case of Instant discount this amount would be lesser than the amount passed by you in the request.
        </td>

        <td style={{ textAlign: "left" }}>
          100.00
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          offer
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter is used to post the offer key.
        </td>

        <td style={{ textAlign: "left" }}>
          newoffer1\@5686
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          offer\_type
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter is used to post any of the following offer\_type:
           - instant

          * cashback
        </td>

        <td style={{ textAlign: "left" }}>
          instant
        </td>
      </tr>
    </tbody>
  </Table>

  For a sample response, refer to the [Additional Info for Payment APIs](ref:addl_info-payment-apis).
</Accordion>

### Step 6: Verify the payment

Similar to the payment response, same params can be handled as part of the **Verify Payment** API or webhooks. For more information, For more information, refer to following tabs.

| Parameter           | Description                                                                                                                                                                                      | **Example** |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| transaction\_amount | This parameter contains the total transaction amount before discount.                                                                                                                            | 50000.00    |
| net\_amount\_debit  | This parameter contains the actual amount deducted from the customer’s payment instrument. In case of Instant discount this amount would be lesser than the amount passed by you in the request. | 47500.00    |
| discount            | This parameter contains the offer value provided to the user. This value will specify the offer amount for both Instant discount and Cashback offers.                                            | 2500.00     |

<Verify_Payment_Tabs />

<br />

PayU would refund the exact amount passed by you in the Refund request. For more information, refer to [Refunds for Offers](doc:refunds-for-offers)

<Callout icon="📘" theme="info">
  ###

  **Note**: You can enable the **Enforce Offer** flag by requesting your PayU Key Account Manager. If you enable the **Enforce Offer** flag, the best offer out of the all the offers passed will be applied for the customer.
</Callout>

<br />
