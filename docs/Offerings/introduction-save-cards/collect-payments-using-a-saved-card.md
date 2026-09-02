---
title: Collect Payments using a Tokenized Card
excerpt: >-
  When your customer has an account on your shopping website, they may store
  their card details to use when they revisit your website (repeat payment).
deprecated: false
hidden: false
metadata:
  title: Collect Payments using a Saved Card
  description: >-
    Find out how to collect payments using a saved card on PayU India. This
    guide shows you how to use the Merchant Hosted Checkout integration to offer
    a seamless and secure payment experience to your customers.
  keywords:
    - Collect payments using saved cards
    - Collect payments with saved cards on PayU
    - Process transactions using saved cards
    - Payment with saved card
    - Payment using saved card
    - Payment using tokenised cards
    - Collect payment with tokenised cards
  robots: index
next:
  description: ''
---
PayU offers you API to tokenize the card details and retrieves them using the Store Card APIs. For example, the stored cards are displayed when your customer performs checkout and lands on the payment page, similar to the following screenshot where they need to enter only the CVV:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/11/save_card_checkout-1024x817.jpeg)

This section explains the procedure for getting a customer’s card details and using a tokenized card to initiate payment.

***

For all the scenarios mentioned in this section you must follow the

1. **Get the tokenized card details**:  Get the customer’s card details your merchant key and customer’s registered mail ID to PayU using the **get_user_details** API. For more information, refer to <Anchor target="_blank" href="ref:get_user_cards_api_model3">Get User Cards API - Model 3</Anchor> API  under API Reference.

2. **Post Payment to PayU and check response**: Make the transaction request with the payment details along with the card nickname to PayU based on the following scenarios of tokenization:

   * [Using zero code change approach](#using-zero-code-change-approach)

   * [Using complete card details](#using-complete-card-details)

   * [Using network tokens](#using-network-tokens)

   * [Using issuer tokens](#using-issuer-tokens)

   * [Using card tokenized with PayU](#using-card-tokenized-with-payu)

   * [Using card on a decoupled flow with network token or other partner tokenization](#using-card-on-a-decoupled-flow-with-network-token-or-other-partner-tokenization)

   * [Using card on a decoupled flow with PayU tokenization](#using-card-on-a-decoupled-flow-with-payu-tokenization)

   <Callout icon="📘" theme="info">
     ### Notes:

     * In addition to the request parameters used for Merchant Hosted Checkout (Seamless integration) payment request, you need to ensure the additional parameters as specified in each scenario specified in this step. For more information on the complete list of parameters, refer to Integrate with Merchant Hosted Checkout.
     * The additional response parameters (if any) are specified for each scenario. For the sample response for a card payment using Merchant Hosted Checkout response, refer to <Anchor target="_blank" href="ref:_payment_merchant_hosted">Collect Payment API - Merchant Hosted Checkout</Anchor>
   </Callout>

3. **Verify the Payment**: Verify the transaction details using the Verification APIs. Post the transaction ID using the **verify_payment** API to verify the payment. For more information, refer to [Verify Payment API](ref:verify_payment_api)

## Using zero code change approach

If the merchant wants PayU to tokenize the card using a zero code change approach (Model 2), use the request parameters as described in this section.

### Applicable Scenarios

* Merchant wants to create tokens without making any integration changes at their end
* Merchant is using PayU as a partner for tokenization

This scenario is applicable if any merchant sends the plain card request to PayU and shares the consent for saving the card details.

For the sample request and response, refer to [Zero Code Change - Model 2](doc:zero-code-change-for-vault-integration-model-2).

## Using complete card details

This scenario is applicable where a customer is providing the complete card number do the transaction (Card number, Expiry, CVV, and name on card) 

### Applicable Scenarios

* It is a guest checkout  
* It is a standard checkout request where there is no need to tokenize the card 

<Callout icon="📘" theme="info">
  Note: Plain card details coming from the merchant, so no changes are applicable in the request & response.
</Callout>

<Accordion title="Request Parameters and Sample Request" icon="far fa-code">
  <Tabs>
    <Tab title="Request Parameters">
      | Parameter                    | Description                                                                                                                                                                                                                    | Example                                                                                                                                                    |
      | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | key<br />`mandatory`         | `String` The merchant key is a unique identifier for a merchant account in PayU's database.                                                                                                                                    | Your Test Key                                                                                                                                              |
      | api_version<br />`optional`  | `String` The API version for this API.                                                                                                                                                                                         | 1                                                                                                                                                          |
      | txnid<br />`mandatory`       | `String` The transaction ID is a reference number for a specific order that is generated by the merchant. It is used to track the order and must be unique. PayU's system will not accept duplicate transaction IDs.           | s7hhDQVWvbhBdN                                                                                                                                             |
      | amount<br />`mandatory`      | `String` This field should contain the payment amount for the transaction. If you want to use the cardless EMI option, the amount must be at least Rs. 8000                                                                    | 10.00                                                                                                                                                      |
      | productinfo<br />`mandatory` | `String` It should be a string containing a brief description of the product.<br />`<br/>Character Limit-100<br/>`                                                                                                             | iPhone                                                                                                                                                     |
      | firstname<br />`mandatory`   | `String` The first name of the customer.<br />`<br/>Character Limit-60<br/>`                                                                                                                                                   | Ashish                                                                                                                                                     |
      | email<br />`mandatory`       | `String` The email of the customer.<br />`<br/>Character Limit-50<br/>`                                                                                                                                                        | [test@gmail.com](mailto:test@gmail.com)                                                                                                                    |
      | phone<br />`mandatory`       | `String` The phone number of the customer.<br /><br />**Note**: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.          | 9876543210                                                                                                                                                 |
      | lastname<br />`mandatory`    | `String` The last name of the customer.<br />`<br/>Character Limit-60<br/>`                                                                                                                                                    | Verma                                                                                                                                                      |
      | address1<br />`optional`     | `String` The first line of the billing address.<br />`<br/>Character Limit-100<br/>`                                                                                                                                           | H.No- 17, Block C, Kalyan Bldg, <br />Khardilkar Road, Mumbai                                                                                              |
      | address2<br />`optional`     | `String` The second line of the billing address.<br />`Character Limit-100`                                                                                                                                                    | 34 Saikripa-Estate, Tilak Nagar                                                                                                                            |
      | city<br />`optional`         | `String` The city where your customer resides as part of the billing address.                                                                                                                                                  | Mumbai                                                                                                                                                     |
      | state<br />`optional`        | `String` The state where your customer resides as part of the billing address.                                                                                                                                                 | Maharashtra                                                                                                                                                |
      | country<br />`optional`      | `String` The country where your customer resides.<br />`Character Limit-50`                                                                                                                                                    | India                                                                                                                                                      |
      | zipcode<br />`optional`      | `String` Billing address zip code is mandatory for the cardless EMI option.<br />`<br/>Character Limit-20<br/>`                                                                                                                | 400004                                                                                                                                                     |
      | surl<br />`mandatory`        | `String` The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.               | [https://apiplayground<br />-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                       |
      | furl<br />`mandatory`        | `String` The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.                   | [https://apiplayground-response.<br />herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                       |
      | hash<br />`mandatory`        | `String` It is used to avoid the possibility of transaction tampering. For more information on hash generation process, refer to Generate Hash.                                                                                | `eabec285da28fd0e3054d41a4d24fe9f`<br />`7599c9d0b66646f7a9984303fd612404`<br />`4b6206daf831e9a8bda28a6200d318293`<br />`a13d6c193109b60bd4b4f8b09c90972` |
      | pg<br />`mandatory`          | `String` The pg parameter determines which payment tabs will be displayed. Here, use 'CC' as the value.                                                                                                                        | CC                                                                                                                                                         |
      | bankcode<br />`mandatory`    | `String` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it.                                               | AMEX                                                                                                                                                       |
      | udf1 - udf5<br />`optional`  | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.<br />`Character Limit-255` | Payment Preference, <br />Shipping Method, <br />Shipping Address1, <br />Shipping City, Shipping Zip Code, etc.                                           |
      | ccnum<br />`optional`        | `varchar` This parameter must contain the 13 to 19-digit card number for credit or debit cards in general.                                                                                                                     | 512\*\*\*6789012346                                                                                                                                        |
      | ccname<br />`optional`       | `varchar` It is the customer's name on card.                                                                                                                                                                                   | Ashish                                                                                                                                                     |
      | ccvv<br />`optional`         | `varchar` This parameter must contain the CVV number of the card – as entered by the customer for the transaction.                                                                                                             | 123                                                                                                                                                        |
      | ccexpmon<br />`mandatory`    | `integer` This parameter must contain the Expiry month that is mentioned under card validity.                                                                                                                                  | 10                                                                                                                                                         |
      | ccexpyr<br />`mandatory`     | `integer` This parameter must contain the Expiry year that is mentioned under card validity.                                                                                                                                   | 2022                                                                                                                                                       |
    </Tab>

    <Tab title="Sample Request">
      ```curl
      curl -X POST "https://test.payu.in/_payment" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -d "key=Your Test Key" \
        -d "api_version=1" \
        -d "txnid=s7hhDQVWvbhBdN" \
        -d "amount=10.00" \
        -d "productinfo=iPhone" \
        -d "firstname=Ashish" \
        -d "lastname=Verma" \
        -d "email=test@gmail.com" \
        -d "phone=9876543210" \
        -d "address1=H.No-17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai" \
        -d "city=Mumbai" \
        -d "state=Maharashtra" \
        -d "country=India" \
        -d "zipcode=400004" \
        -d "surl=https://apiplayground-response.herokuapp.com/" \
        -d "furl=https://apiplayground-response.herokuapp.com/" \
        -d "hash=eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972" \
        -d "pg=CC" \
        -d "bankcode=AMEX" \
        -d "ccnum=5123456789012346" \
        -d "ccname=Ashish" \
        -d "ccvv=123" \
        -d "ccexpmon=10" \
        -d "ccexpyr=2022"
      ```
      ```python
      import requests

      url = "https://test.payu.in/_payment"
      headers = {
          "Content-Type": "application/x-www-form-urlencoded"
      }
      data = {
          "key": "Your Test Key",
          "api_version": "1",
          "txnid": "s7hhDQVWvbhBdN",
          "amount": "10.00",
          "productinfo": "iPhone",
          "firstname": "Ashish",
          "lastname": "Verma",
          "email": "test@gmail.com",
          "phone": "9876543210",
          "address1": "H.No-17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai",
          "city": "Mumbai",
          "state": "Maharashtra",
          "country": "India",
          "zipcode": "400004",
          "surl": "https://apiplayground-response.herokuapp.com/",
          "furl": "https://apiplayground-response.herokuapp.com/",
          "hash": "eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972",
          "pg": "CC",
          "bankcode": "AMEX",
          "ccnum": "5123456789012346",
          "ccname": "Ashish",
          "ccvv": "123",
          "ccexpmon": "10",
          "ccexpyr": "2022"
      }

      try:
          response = requests.post(url, headers=headers, data=data)
          print(f"Status Code: {response.status_code}")
          print(f"Response: {response.text}")
      except requests.exceptions.RequestException as e:
          print(f"Error: {e}")
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
              try
              {
                  string url = "https://test.payu.in/_payment";
                  var formParams = new List<KeyValuePair<string, string>>
                  {
                      new KeyValuePair<string, string>("key", "Your Test Key"),
                      new KeyValuePair<string, string>("api_version", "1"),
                      new KeyValuePair<string, string>("txnid", "s7hhDQVWvbhBdN"),
                      new KeyValuePair<string, string>("amount", "10.00"),
                      new KeyValuePair<string, string>("productinfo", "iPhone"),
                      new KeyValuePair<string, string>("firstname", "Ashish"),
                      new KeyValuePair<string, string>("lastname", "Verma"),
                      new KeyValuePair<string, string>("email", "test@gmail.com"),
                      new KeyValuePair<string, string>("phone", "9876543210"),
                      new KeyValuePair<string, string>("address1", "H.No-17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai"),
                      new KeyValuePair<string, string>("city", "Mumbai"),
                      new KeyValuePair<string, string>("state", "Maharashtra"),
                      new KeyValuePair<string, string>("country", "India"),
                      new KeyValuePair<string, string>("zipcode", "400004"),
                      new KeyValuePair<string, string>("surl", "https://apiplayground-response.herokuapp.com/"),
                      new KeyValuePair<string, string>("furl", "https://apiplayground-response.herokuapp.com/"),
                      new KeyValuePair<string, string>("hash", "eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972"),
                      new KeyValuePair<string, string>("pg", "CC"),
                      new KeyValuePair<string, string>("bankcode", "AMEX"),
                      new KeyValuePair<string, string>("ccnum", "5123456789012346"),
                      new KeyValuePair<string, string>("ccname", "Ashish"),
                      new KeyValuePair<string, string>("ccvv", "123"),
                      new KeyValuePair<string, string>("ccexpmon", "10"),
                      new KeyValuePair<string, string>("ccexpyr", "2022")
                  };

                  var formContent = new FormUrlEncodedContent(formParams);
                  HttpResponseMessage response = await client.PostAsync(url, formContent);
                  string responseContent = await response.Content.ReadAsStringAsync();

                  Console.WriteLine($"Status Code: {response.StatusCode}");
                  Console.WriteLine($"Response: {responseContent}");
              }
              catch (HttpRequestException e)
              {
                  Console.WriteLine($"Error: {e.Message}");
              }
          }
      }
      ```
      ```javascript
      async function completeCardPayment() {
          const url = "https://test.payu.in/_payment";
          const formData = new URLSearchParams();
          formData.append("key", "Your Test Key");
          formData.append("api_version", "1");
          formData.append("txnid", "s7hhDQVWvbhBdN");
          formData.append("amount", "10.00");
          formData.append("productinfo", "iPhone");
          formData.append("firstname", "Ashish");
          formData.append("lastname", "Verma");
          formData.append("email", "test@gmail.com");
          formData.append("phone", "9876543210");
          formData.append("address1", "H.No-17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai");
          formData.append("city", "Mumbai");
          formData.append("state", "Maharashtra");
          formData.append("country", "India");
          formData.append("zipcode", "400004");
          formData.append("surl", "https://apiplayground-response.herokuapp.com/");
          formData.append("furl", "https://apiplayground-response.herokuapp.com/");
          formData.append("hash", "eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972");
          formData.append("pg", "CC");
          formData.append("bankcode", "AMEX");
          formData.append("ccnum", "5123456789012346");
          formData.append("ccname", "Ashish");
          formData.append("ccvv", "123");
          formData.append("ccexpmon", "10");
          formData.append("ccexpyr", "2022");

          try {
              const response = await fetch(url, {
                  method: "POST",
                  headers: { "Content-Type": "application/x-www-form-urlencoded" },
                  body: formData
              });
              const responseText = await response.text();
              console.log(`Status: ${response.status}`);
              console.log(`Response: ${responseText}`);
              return { status: response.status, data: responseText };
          } catch (error) {
              console.error("Error:", error);
              throw error;
          }
      }

      completeCardPayment()
          .then(result => console.log("Success:", result))
          .catch(error => console.error("Failed:", error));
      ```
      ```java
      import java.io.*;
      import java.net.*;
      import java.nio.charset.StandardCharsets;

      public class CompleteCardPayment {
          public static void main(String[] args) {
              try {
                  makePayment();
              } catch (IOException e) {
                  System.err.println("Error: " + e.getMessage());
              }
          }

          public static void makePayment() throws IOException {
              String url = "https://test.payu.in/_payment";
              String formData =
                  "key=" + URLEncoder.encode("Your Test Key", StandardCharsets.UTF_8) +
                  "&api_version=1" +
                  "&txnid=" + URLEncoder.encode("s7hhDQVWvbhBdN", StandardCharsets.UTF_8) +
                  "&amount=10.00" +
                  "&productinfo=" + URLEncoder.encode("iPhone", StandardCharsets.UTF_8) +
                  "&firstname=Ashish&lastname=Verma" +
                  "&email=" + URLEncoder.encode("test@gmail.com", StandardCharsets.UTF_8) +
                  "&phone=9876543210" +
                  "&address1=" + URLEncoder.encode("H.No-17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai", StandardCharsets.UTF_8) +
                  "&city=Mumbai&state=Maharashtra&country=India&zipcode=400004" +
                  "&surl=" + URLEncoder.encode("https://apiplayground-response.herokuapp.com/", StandardCharsets.UTF_8) +
                  "&furl=" + URLEncoder.encode("https://apiplayground-response.herokuapp.com/", StandardCharsets.UTF_8) +
                  "&hash=" + URLEncoder.encode("eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972", StandardCharsets.UTF_8) +
                  "&pg=CC&bankcode=AMEX" +
                  "&ccnum=5123456789012346&ccname=Ashish&ccvv=123&ccexpmon=10&ccexpyr=2022";

              URL urlObj = new URL(url);
              HttpURLConnection connection = (HttpURLConnection) urlObj.openConnection();
              connection.setRequestMethod("POST");
              connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
              connection.setDoOutput(true);

              try (OutputStream os = connection.getOutputStream()) {
                  os.write(formData.getBytes(StandardCharsets.UTF_8));
              }

              int responseCode = connection.getResponseCode();
              System.out.println("Status Code: " + responseCode);

              try (BufferedReader br = new BufferedReader(new InputStreamReader(
                      responseCode >= 200 && responseCode < 300
                          ? connection.getInputStream() : connection.getErrorStream(),
                      StandardCharsets.UTF_8))) {
                  StringBuilder response = new StringBuilder();
                  String line;
                  while ((line = br.readLine()) != null) response.append(line.trim());
                  System.out.println("Response: " + response);
              }
              connection.disconnect();
          }
      }
      ```
      ```php
      <?php
      function completeCardPayment() {
          $url = 'https://test.payu.in/_payment';
          $postData = [
              'key'         => 'Your Test Key',
              'api_version' => '1',
              'txnid'       => 's7hhDQVWvbhBdN',
              'amount'      => '10.00',
              'productinfo' => 'iPhone',
              'firstname'   => 'Ashish',
              'lastname'    => 'Verma',
              'email'       => 'test@gmail.com',
              'phone'       => '9876543210',
              'address1'    => 'H.No-17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai',
              'city'        => 'Mumbai',
              'state'       => 'Maharashtra',
              'country'     => 'India',
              'zipcode'     => '400004',
              'surl'        => 'https://apiplayground-response.herokuapp.com/',
              'furl'        => 'https://apiplayground-response.herokuapp.com/',
              'hash'        => 'eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972',
              'pg'          => 'CC',
              'bankcode'    => 'AMEX',
              'ccnum'       => '5123456789012346',
              'ccname'      => 'Ashish',
              'ccvv'        => '123',
              'ccexpmon'    => '10',
              'ccexpyr'     => '2022'
          ];

          $curl = curl_init();
          curl_setopt_array($curl, [
              CURLOPT_URL            => $url,
              CURLOPT_RETURNTRANSFER => true,
              CURLOPT_POST           => true,
              CURLOPT_POSTFIELDS     => http_build_query($postData),
              CURLOPT_HTTPHEADER     => ['Content-Type: application/x-www-form-urlencoded'],
              CURLOPT_TIMEOUT        => 30,
              CURLOPT_SSL_VERIFYPEER => true,
              CURLOPT_SSL_VERIFYHOST => 2
          ]);

          $response = curl_exec($curl);
          $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
          $error    = curl_error($curl);
          curl_close($curl);

          if ($error) { echo "cURL Error: " . $error . PHP_EOL; return false; }
          echo "Status Code: " . $httpCode . PHP_EOL;
          echo "Response: " . $response . PHP_EOL;
          return ['status_code' => $httpCode, 'response' => $response];
      }

      $result = completeCardPayment();
      ?>
      ```
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Sample response" icon="far fa-reply">
  {
    "mihpayid": "403993715531077182",
    "mode": "CC",
    "status": "success",
    "unmappedstatus": "captured",
    "key": "JPM7Fg",
    "txnid": "ypl938459435dfdfdf",
    "amount": "1000.00",
    "cardCategory": "domestic",
    "discount": "0.00",
    "net_amount_debit": "1000",
    "addedon": "2024-02-27 15:00:42",
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
    "phone": "9876543210",
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
    "hash": "84bbbf0fa3ba2a39942f6c3deab234c4d00bc5b6aceee5cda3c8200d6e1714e19c224d47e24d0c4a9a0cce40eddbae1dc46455c69e5e7d5dd62f6636bfab337c",
    "field1": "896193988312194700",
    "field2": "857712",
    "field3": "1000.00",
    "field4": "",
    "field5": "00",
    "field6": "02",
    "field7": "AUTHPOSITIVE",
    "field8": "AUTHORIZED",
    "field9": "Transaction is Successful",
    "payment_source": "payu",
    "PG_TYPE": "CC-PG",
    "bank_ref_num": "896193988312194700",
    "bankcode": "CC",
    "error": "E000",
    "error_Message": "No Error",
    "cardnum": "XXXXXXXXXXXX2346",
    "cardhash": "This field is no longer supported in postback params.",
    "splitInfo": "{"splitStatus":"splitNotReceived","splitSegments":[]}"
  }
</Accordion>

## Using network tokens

This scenario is applicable if you wanted to collect payments using network tokens.

### Applicable scenarios

* Merchant has the `card token`, `TAVV`(Cryptogram), and the last four digits of the card 
* The token could be created by the merchant or through another partner 

<Callout icon="📘" theme="info">
  ### Note:

  This scenario is applicable if you are PCI compliant and got the network token and `TAVV` from any other aggregator or schemes and then sending the card transaction request in the form of authentication.
</Callout>

<Tabs>
  <Tab title="Request Parameters">
    **Mandatory parameters**

    | Parameter            | Description                                                                                                                                                                                                                                                                                                                                 | Example                                                                                                                            |
    | :------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------- |
    | `key`                | `String` The merchant key is a unique identifier for a merchant account in PayU's database.                                                                                                                                                                                                                                                 | Your Test Key                                                                                                                      |
    | txnid                | `String` The transaction ID is a reference number for a specific order that is generated by the merchant. It is used to track the order and must be unique. PayU's system will not accept duplicate transaction IDs.                                                                                                                        | s7hhDQVWvbhBdN                                                                                                                     |
    | amount               | `String` This field should contain the payment amount for the transaction. If you want to use the cardless EMI option, the amount must be at least Rs. 8000.                                                                                                                                                                                | 10.00                                                                                                                              |
    | productinfo          | `String` It should be a string containing a brief description of the product. Character Limit-100                                                                                                                                                                                                                                           | iPhone                                                                                                                             |
    | firstname            | `String` The first name of the customer. Character Limit-60                                                                                                                                                                                                                                                                                 | Ashish                                                                                                                             |
    | email                | `String` The email of the customer. Character Limit-50                                                                                                                                                                                                                                                                                      | [test@gmail.com](mailto:test@gmail.com)                                                                                            |
    | phone                | `String` The phone number of the customer. **Note**: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information.                                                                                                                                | 9876543210                                                                                                                         |
    | lastname             | `String` The last name of the customer. Character Limit-60                                                                                                                                                                                                                                                                                  | Verma                                                                                                                              |
    | surl                 | `String` The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                            | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                     |
    | furl                 | `String` The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction fails. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                    | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                     |
    | hash                 | `String` It is used to avoid the possibility of transaction tampering. The hash is calculated as: key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\| \| \|\|<Glossary>Salt</Glossary>. For more information on the hash generation process, refer to [Generate Hash](doc:generate-hash-merchant-hosted). | `eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972` |
    | `pg`                 | `String` The pg parameter determines which payment tabs will be displayed. Here, use 'CC' as the value.                                                                                                                                                                                                                                     | CC                                                                                                                                 |
    | `bankcode`           | `String` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it.                                                                                                                                                            | AMEX                                                                                                                               |
    | ccexpmon             | `integer` This parameter must contain the network token expiry month.                                                                                                                                                                                                                                                                       | 10                                                                                                                                 |
    | ccexpyr              | `integer` This parameter must contain the network token expiry year.                                                                                                                                                                                                                                                                        | 2022                                                                                                                               |
    | store_card_token     | `varchar` This must include the Network token generated at your end.                                                                                                                                                                                                                                                                        | 1234 4567 2456 3566                                                                                                                |
    | storecard_token_type | `integer` This parameter is used to specify the store card token type. For this scenario, you must include 1.                                                                                                                                                                                                                               | 1                                                                                                                                  |
    | additional_info      | `varchar` This parameter will contain the additional information in the following JSON format: {"last4Digits": "1234", "TAVV": "ABCDEFGH", "trid": "1234567890", "tokenRefNo": "abcde123456"}                                                                                                                                               | {"last4Digits": "1234", "tavv": "ABCDEFGH", "trid": "1234567890", "tokenRefNo": "abcde123456"}                                     |

    **Optional parameters**

    | Parameter   | Description                                                                                                                                                                                                             | Example                                                                                        |
    | :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------- |
    | api_version | `String` The API version for this API.                                                                                                                                                                                  | 1                                                                                              |
    | address1    | `String` The first line of the billing address. Character Limit-100                                                                                                                                                     | H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai                                        |
    | address2    | `String` The second line of the billing address. Character Limit-100                                                                                                                                                    | 34 Saikripa-Estate, Tilak Nagar                                                                |
    | city        | `String` The city where your customer resides as part of the billing address.                                                                                                                                           | Mumbai                                                                                         |
    | state       | `String` The state where your customer resides as part of the billing address.                                                                                                                                          | Maharashtra                                                                                    |
    | country     | `String` The country where your customer resides. Character Limit-50                                                                                                                                                    | India                                                                                          |
    | zipcode     | `String` Billing address zip code is mandatory for the cardless EMI option. Character Limit-20                                                                                                                          | 400004                                                                                         |
    | udf1 - udf5 | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5. Character Limit-255 | Payment Preference, Shipping Method, Shipping Address1, Shipping City, Shipping Zip Code, etc. |
    | ccnum       | `varchar` This parameter must contain the 13 to 19-digit card number for credit or debit cards in general.                                                                                                              | 512\*\*\*6789012346                                                                            |
    | ccname      | `varchar` It is the customer's name on card.                                                                                                                                                                            | Ashish                                                                                         |
    | ccvv        | `varchar` This parameter must contain the CVV number of the card – as entered by the customer for the transaction.                                                                                                      | 123                                                                                            |
  </Tab>

  <Tab title="Sample Request">
```curl
curl -X POST "https://test.payu.in/_payment" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=Your Test Key" \
  -d "txnid=s7hhDQVWvbhBdN" \
  -d "amount=10.00" \
  -d "productinfo=iPhone" \
  -d "firstname=Ashish" \
  -d "lastname=Verma" \
  -d "email=test@gmail.com" \
  -d "phone=9876543210" \
  -d "surl=https://apiplayground-response.herokuapp.com/" \
  -d "furl=https://apiplayground-response.herokuapp.com/" \
  -d "hash=eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972" \
  -d "pg=CC" \
  -d "bankcode=AMEX" \
  -d "ccexpmon=10" \
  -d "ccexpyr=2022" \
  -d "store_card_token=1234456724563566" \
  -d "storecard_token_type=1" \
  -d "additional_info={\"last4Digits\":\"1234\",\"tavv\":\"ABCDEFGH\",\"trid\":\"1234567890\",\"tokenRefNo\":\"abcde123456\"}" \
  -d "api_version=1" \
  -d "address1=H.No-17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai" \
  -d "address2=34 Saikripa-Estate, Tilak Nagar" \
  -d "city=Mumbai" \
  -d "state=Maharashtra" \
  -d "country=India" \
  -d "zipcode=400004" \
  -d "udf1=Payment Preference" \
  -d "udf2=Shipping Method" \
  -d "udf3=Shipping Address1" \
  -d "udf4=Shipping City" \
  -d "udf5=Shipping Zip Code" \
  -d "ccnum=5123456789012346" \
  -d "ccname=Ashish" \
  -d "ccvv=123"
```
```python
import requests
import json

url = "https://test.payu.in/_payment"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    # Mandatory parameters
    "key": "Your Test Key",
    "txnid": "s7hhDQVWvbhBdN",
    "amount": "10.00",
    "productinfo": "iPhone",
    "firstname": "Ashish",
    "lastname": "Verma",
    "email": "test@gmail.com",
    "phone": "9876543210",
    "surl": "https://apiplayground-response.herokuapp.com/",
    "furl": "https://apiplayground-response.herokuapp.com/",
    "hash": "eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972",
    "pg": "CC",
    "bankcode": "AMEX",
    "ccexpmon": "10",
    "ccexpyr": "2022",
    "store_card_token": "1234456724563566",
    "storecard_token_type": "1",
    "additional_info": json.dumps({
        "last4Digits": "1234",
        "tavv": "ABCDEFGH",
        "trid": "1234567890",
        "tokenRefNo": "abcde123456"
    }),
    # Optional parameters
    "api_version": "1",
    "address1": "H.No-17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai",
    "address2": "34 Saikripa-Estate, Tilak Nagar",
    "city": "Mumbai",
    "state": "Maharashtra",
    "country": "India",
    "zipcode": "400004",
    "udf1": "Payment Preference",
    "udf2": "Shipping Method",
    "udf3": "Shipping Address1",
    "udf4": "Shipping City",
    "udf5": "Shipping Zip Code",
    "ccnum": "5123456789012346",
    "ccname": "Ashish",
    "ccvv": "123"
}

try:
    response = requests.post(url, headers=headers, data=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
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
        try
        {
            string url = "https://test.payu.in/_payment";
            var formParams = new List<KeyValuePair<string, string>>
            {
                // Mandatory parameters
                new KeyValuePair<string, string>("key", "Your Test Key"),
                new KeyValuePair<string, string>("txnid", "s7hhDQVWvbhBdN"),
                new KeyValuePair<string, string>("amount", "10.00"),
                new KeyValuePair<string, string>("productinfo", "iPhone"),
                new KeyValuePair<string, string>("firstname", "Ashish"),
                new KeyValuePair<string, string>("lastname", "Verma"),
                new KeyValuePair<string, string>("email", "test@gmail.com"),
                new KeyValuePair<string, string>("phone", "9876543210"),
                new KeyValuePair<string, string>("surl", "https://apiplayground-response.herokuapp.com/"),
                new KeyValuePair<string, string>("furl", "https://apiplayground-response.herokuapp.com/"),
                new KeyValuePair<string, string>("hash", "eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972"),
                new KeyValuePair<string, string>("pg", "CC"),
                new KeyValuePair<string, string>("bankcode", "AMEX"),
                new KeyValuePair<string, string>("ccexpmon", "10"),
                new KeyValuePair<string, string>("ccexpyr", "2022"),
                new KeyValuePair<string, string>("store_card_token", "1234456724563566"),
                new KeyValuePair<string, string>("storecard_token_type", "1"),
                new KeyValuePair<string, string>("additional_info", "{\"last4Digits\":\"1234\",\"tavv\":\"ABCDEFGH\",\"trid\":\"1234567890\",\"tokenRefNo\":\"abcde123456\"}"),
                // Optional parameters
                new KeyValuePair<string, string>("api_version", "1"),
                new KeyValuePair<string, string>("address1", "H.No-17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai"),
                new KeyValuePair<string, string>("address2", "34 Saikripa-Estate, Tilak Nagar"),
                new KeyValuePair<string, string>("city", "Mumbai"),
                new KeyValuePair<string, string>("state", "Maharashtra"),
                new KeyValuePair<string, string>("country", "India"),
                new KeyValuePair<string, string>("zipcode", "400004"),
                new KeyValuePair<string, string>("udf1", "Payment Preference"),
                new KeyValuePair<string, string>("udf2", "Shipping Method"),
                new KeyValuePair<string, string>("udf3", "Shipping Address1"),
                new KeyValuePair<string, string>("udf4", "Shipping City"),
                new KeyValuePair<string, string>("udf5", "Shipping Zip Code"),
                new KeyValuePair<string, string>("ccnum", "5123456789012346"),
                new KeyValuePair<string, string>("ccname", "Ashish"),
                new KeyValuePair<string, string>("ccvv", "123")
            };

            var formContent = new FormUrlEncodedContent(formParams);
            HttpResponseMessage response = await client.PostAsync(url, formContent);
            string responseContent = await response.Content.ReadAsStringAsync();

            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response: {responseContent}");
        }
        catch (HttpRequestException e)
        {
            Console.WriteLine($"Error: {e.Message}");
        }
    }
}
```
```javascript
async function makePayment() {
    const url = "https://test.payu.in/_payment";
    const formData = new URLSearchParams();
    // Mandatory parameters
    formData.append("key", "Your Test Key");
    formData.append("txnid", "s7hhDQVWvbhBdN");
    formData.append("amount", "10.00");
    formData.append("productinfo", "iPhone");
    formData.append("firstname", "Ashish");
    formData.append("lastname", "Verma");
    formData.append("email", "test@gmail.com");
    formData.append("phone", "9876543210");
    formData.append("surl", "https://apiplayground-response.herokuapp.com/");
    formData.append("furl", "https://apiplayground-response.herokuapp.com/");
    formData.append("hash", "eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972");
    formData.append("pg", "CC");
    formData.append("bankcode", "AMEX");
    formData.append("ccexpmon", "10");
    formData.append("ccexpyr", "2022");
    formData.append("store_card_token", "1234456724563566");
    formData.append("storecard_token_type", "1");
    formData.append("additional_info", JSON.stringify({
        last4Digits: "1234",
        tavv: "ABCDEFGH",
        trid: "1234567890",
        tokenRefNo: "abcde123456"
    }));
    // Optional parameters
    formData.append("api_version", "1");
    formData.append("address1", "H.No-17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai");
    formData.append("address2", "34 Saikripa-Estate, Tilak Nagar");
    formData.append("city", "Mumbai");
    formData.append("state", "Maharashtra");
    formData.append("country", "India");
    formData.append("zipcode", "400004");
    formData.append("udf1", "Payment Preference");
    formData.append("udf2", "Shipping Method");
    formData.append("udf3", "Shipping Address1");
    formData.append("udf4", "Shipping City");
    formData.append("udf5", "Shipping Zip Code");
    formData.append("ccnum", "5123456789012346");
    formData.append("ccname", "Ashish");
    formData.append("ccvv", "123");

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: formData
        });
        const responseText = await response.text();
        console.log(`Status: ${response.status}`);
        console.log(`Response: ${responseText}`);
        return { status: response.status, data: responseText };
    } catch (error) {
        console.error("Error:", error);
        throw error;
    }
}

makePayment()
    .then(result => console.log("Success:", result))
    .catch(error => console.error("Failed:", error));
```
```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class MakePayment {
    public static void main(String[] args) {
        try {
            makePayment();
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }

    public static void makePayment() throws IOException {
        String url = "https://test.payu.in/_payment";
        String additionalInfo = "{\"last4Digits\":\"1234\",\"tavv\":\"ABCDEFGH\",\"trid\":\"1234567890\",\"tokenRefNo\":\"abcde123456\"}";

        // Mandatory parameters
        String formData =
            "key=" + URLEncoder.encode("Your Test Key", StandardCharsets.UTF_8) +
            "&txnid=" + URLEncoder.encode("s7hhDQVWvbhBdN", StandardCharsets.UTF_8) +
            "&amount=10.00" +
            "&productinfo=" + URLEncoder.encode("iPhone", StandardCharsets.UTF_8) +
            "&firstname=Ashish" +
            "&lastname=Verma" +
            "&email=" + URLEncoder.encode("test@gmail.com", StandardCharsets.UTF_8) +
            "&phone=9876543210" +
            "&surl=" + URLEncoder.encode("https://apiplayground-response.herokuapp.com/", StandardCharsets.UTF_8) +
            "&furl=" + URLEncoder.encode("https://apiplayground-response.herokuapp.com/", StandardCharsets.UTF_8) +
            "&hash=" + URLEncoder.encode("eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972", StandardCharsets.UTF_8) +
            "&pg=CC" +
            "&bankcode=AMEX" +
            "&ccexpmon=10" +
            "&ccexpyr=2022" +
            "&store_card_token=1234456724563566" +
            "&storecard_token_type=1" +
            "&additional_info=" + URLEncoder.encode(additionalInfo, StandardCharsets.UTF_8) +
            // Optional parameters
            "&api_version=1" +
            "&address1=" + URLEncoder.encode("H.No-17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai", StandardCharsets.UTF_8) +
            "&address2=" + URLEncoder.encode("34 Saikripa-Estate, Tilak Nagar", StandardCharsets.UTF_8) +
            "&city=Mumbai" +
            "&state=Maharashtra" +
            "&country=India" +
            "&zipcode=400004" +
            "&udf1=" + URLEncoder.encode("Payment Preference", StandardCharsets.UTF_8) +
            "&udf2=" + URLEncoder.encode("Shipping Method", StandardCharsets.UTF_8) +
            "&udf3=" + URLEncoder.encode("Shipping Address1", StandardCharsets.UTF_8) +
            "&udf4=" + URLEncoder.encode("Shipping City", StandardCharsets.UTF_8) +
            "&udf5=" + URLEncoder.encode("Shipping Zip Code", StandardCharsets.UTF_8) +
            "&ccnum=5123456789012346" +
            "&ccname=Ashish" +
            "&ccvv=123";

        URL urlObj = new URL(url);
        HttpURLConnection connection = (HttpURLConnection) urlObj.openConnection();
        connection.setRequestMethod("POST");
        connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
        connection.setDoOutput(true);

        try (OutputStream os = connection.getOutputStream()) {
            os.write(formData.getBytes(StandardCharsets.UTF_8));
        }

        int responseCode = connection.getResponseCode();
        System.out.println("Status Code: " + responseCode);

        try (BufferedReader br = new BufferedReader(new InputStreamReader(
                responseCode >= 200 && responseCode < 300
                    ? connection.getInputStream() : connection.getErrorStream(),
                StandardCharsets.UTF_8))) {
            StringBuilder response = new StringBuilder();
            String line;
            while ((line = br.readLine()) != null) response.append(line.trim());
            System.out.println("Response: " + response);
        }
        connection.disconnect();
    }
}
```
```php
<?php
function makePayment() {
    $url = 'https://test.payu.in/_payment';
    $additionalInfo = json_encode([
        'last4Digits' => '1234',
        'tavv'        => 'ABCDEFGH',
        'trid'        => '1234567890',
        'tokenRefNo'  => 'abcde123456'
    ]);
    $postData = [
        // Mandatory parameters
        'key'                  => 'Your Test Key',
        'txnid'                => 's7hhDQVWvbhBdN',
        'amount'               => '10.00',
        'productinfo'          => 'iPhone',
        'firstname'            => 'Ashish',
        'lastname'             => 'Verma',
        'email'                => 'test@gmail.com',
        'phone'                => '9876543210',
        'surl'                 => 'https://apiplayground-response.herokuapp.com/',
        'furl'                 => 'https://apiplayground-response.herokuapp.com/',
        'hash'                 => 'eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972',
        'pg'                   => 'CC',
        'bankcode'             => 'AMEX',
        'ccexpmon'             => '10',
        'ccexpyr'              => '2022',
        'store_card_token'     => '1234456724563566',
        'storecard_token_type' => '1',
        'additional_info'      => $additionalInfo,
        // Optional parameters
        'api_version'          => '1',
        'address1'             => 'H.No-17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai',
        'address2'             => '34 Saikripa-Estate, Tilak Nagar',
        'city'                 => 'Mumbai',
        'state'                => 'Maharashtra',
        'country'              => 'India',
        'zipcode'              => '400004',
        'udf1'                 => 'Payment Preference',
        'udf2'                 => 'Shipping Method',
        'udf3'                 => 'Shipping Address1',
        'udf4'                 => 'Shipping City',
        'udf5'                 => 'Shipping Zip Code',
        'ccnum'                => '5123456789012346',
        'ccname'               => 'Ashish',
        'ccvv'                 => '123'
    ];

    $curl = curl_init();
    curl_setopt_array($curl, [
        CURLOPT_URL            => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST           => true,
        CURLOPT_POSTFIELDS     => http_build_query($postData),
        CURLOPT_HTTPHEADER     => ['Content-Type: application/x-www-form-urlencoded'],
        CURLOPT_TIMEOUT        => 30,
        CURLOPT_SSL_VERIFYPEER => true,
        CURLOPT_SSL_VERIFYHOST => 2
    ]);

    $response = curl_exec($curl);
    $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
    $error    = curl_error($curl);
    curl_close($curl);

    if ($error) {
        echo "cURL Error: " . $error . PHP_EOL;
        return false;
    }
    echo "Status Code: " . $httpCode . PHP_EOL;
    echo "Response: " . $response . PHP_EOL;
    return ['status_code' => $httpCode, 'response' => $response];
}

$result = makePayment();
?>
```
  </Tab>
</Tabs>

## Using issuer tokens

This scenario is applicable if you wanted to collect payments using issuer tokens.

### Applicable scenarios

* Merchant has the `card token`, `trMerchantId`, `tokenReferenceId`, and the last four digits of the card 
* The token could be created by the issuer

<Callout icon="📘" theme="info">
  ### Note:

  This scenario is applicable if you are PCI compliant and got the `issuer token`, `trMerchantId`, and `tokenReferenceId` and then sending the card transaction request in the form of authentication.
</Callout>

For the sample request and response, refer to <Anchor target="_blank" href="ref:using-issuer-tokens">Using Issuer Tokens</Anchor>.

## Using card tokenized with PayU

If the merchant has tokenized the card with PayU and needs to process the transaction using PayU token only. 

### Applicable scenarios

* Merchant has created the token using PayU  as the partner 

<Callout icon="📘" theme="info">
  ### Note:

  This scenario is applicable if any PCI or Non-PCI complied merchant sends the PayU token in a request for fulfilment purposes.
</Callout>

For the sample request and response, refer to <Anchor target="_blank" href="ref:using-card-tokenized-with-payu">Using Card Tokenized with PayU</Anchor>.

## Using card on a decoupled flow with network token or other partner tokenization

This scenario is applicable where you are on a decoupled flow. This is where you are using the PayU for either authentication or authorization only while using tokens created by the network or some other partner. 

**Decoupled flow**: You are sending the authentication request to PayU and if the merchant wishes to send the authorization request eventually or to other aggregators.

For the sample request and response, refer to <Anchor target="_blank" href="ref:using-card-tokenized-with-payu">Using Card on a Decoupled Flow with Network Token or Other Partner Tokenization</Anchor>.

## Using card on a decoupled flow with PayU tokenization

This scenario is the application on a decoupled flow using the PayU for either authentication or authorization only with tokens created in partnership with PayU.

**Direct Authorisation Flow**: When you have done the authentication from some other aggregator and authorization request is coming to PayU.

For the sample request and response, refer to <Anchor target="_blank" href="ref:using-card-on-a-decoupled-flow-with-payu-tokenization">Using Card on a Decoupled Flow with PayU Tokenization</Anchor>.

<br />
