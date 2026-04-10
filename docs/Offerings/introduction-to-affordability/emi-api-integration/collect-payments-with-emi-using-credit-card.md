---
title: Credit Card - Merchant Hosted Checkout Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Credit Card Integration - Merchant Hosted Checkout - EMI
  description: ''
  keywords:
    - Seamless Credit Card EMI Integration PayU
    - PayU Credit Card EMI Integration
    - Merchant Hosted EMI Integration Credit Card
  robots: index
next:
  description: ''
---
When your customer wants to opt for the EMI option with credit cards, you can use EMI APIs to check the customer’s eligibility and get the EMI amount, interest, processing fee, or No-Cost EMI and tenure. If the customer is eligible, you can post the transaction with EMI conversion.

<Callout icon="📘" theme="info">
  **Notes**:

  * You can create EMI offers using the PayU Dashboard and use them for collecting payments as described in this procedure. For more information, refer to [Create a No-Cost EMI Offer](doc:create-a-no-cost-emi-offer)
  * For Server-to-Server integration, CC-EMI works on **txn_s2s_flow=1, 2,** or **4**, whereas, DC-EMI only works on **txn_s2s_flow=1**. The same **base64Decoder** logic will be used to decode the encrypted **acsTemplate** (in case of txn_s2s_flow=4) and post_data (in case of txn_s2s_flow=1 or 2).
  * You can handle Guest Checkout transactions for EMI integration. For more information, refer to[ Cards Integration > Handling Guest Checkout Transactions](doc:collect-payments-with-cards-seamless#handling-guest-checkout-transactions).
</Callout>

<Callout icon="🚧" theme="warn">
  **Test Environment Limitation for Tokens (Saved Cards)**: PayU does not support network tokens or issuer tokens in Test Environment, so you cannot try using API Reference for network tokens or issuer tokens.
</Callout>

**Steps to integrate**

<Cards columns={2}>
  <Card title="1. Check the Card EMI Eligibility" href="#step-1-check-the-card-emi-eligibility">
    Verify if the customer's card is eligible for EMI payments before proceeding

    <br />
  </Card>

  <Card title="2. Calculate the EMI Interest" href="#step-2-calculate-the-emi-interest">
    Calculate the EMI interest rates and monthly installment amounts for the transaction

    <br />
  </Card>

  <Card title="3. Initiate the Payment" href="#step-3-initiate-the-payment">
    Start the payment process with EMI configuration in Android Checkout Pro

    <br />
  </Card>

  <Card title="4. Check the PayU Response" href="#step-4-check-the-payu-response">
    Handle and process the response received from PayU after payment initiation

    <br />
  </Card>

  <Card title="5. Verify the Payment" href="#step-5-verify-the-payment">
    Verify the payment status and ensure successful EMI transaction completion
  </Card>

  <br />
</Cards>

<Callout icon="📮" theme="default">
  **Postman Collection**: Download the **Merchant Hosted Checkout > Credit Card EMI** Postman Collection from the following location:

  [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/folder/vaqlmg8/integrate-with-credit-card](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/folder/vaqlmg8/integrate-with-credit-card)
</Callout>

## Step 1: Check the card EMI eligibility

After collecting the customer’s card and the amount to be paid, check the EMI eligibility based on the card BIN from the customer’s credit card number using the **eligibleBINsforEMI** API. For more information on how to use **eligibleBINsforEMI** API, refer to [Eligible BINs for EMI API v1.0](ref:eligiblebinsforemi).

## Step 2: Calculate the EMI interest

Use the **getEmiAmountAccordingToInterest** API to calculate the EMI interest. For more information, refer to [Get EMI According to Interest API](ref:get_emi_according_to_interest_api)

## Step 3: Initiate the payment

When your customer has an account on your shopping website, they may store their card details to use when they visit/revisit your website. They can use a following options to initiate the payment with EMI:

* [Using complete card details](doc:collect-payments-with-emi-using-credit-card#using-complete-card-details)
* [Using network tokens](doc:collect-payments-with-emi-using-credit-card#using-network-tokens)
* [Using issuer tokens](doc:collect-payments-with-emi-using-credit-card#using-issuer-tokens)
* [Using card tokenized with PayU](doc:collect-payments-with-emi-using-credit-card#using-card-tokenized-with-payu)
* [Using card on a decoupled flow with network token or other partner tokenization](doc:collect-payments-with-emi-using-credit-card#using-card-on-a-decoupled-flow-with-network-token-or-other-partner-tokenization)
* [Using card on a decoupled flow with PayU tokenization](doc:collect-payments-with-emi-using-credit-card#using-card-on-a-decoupled-flow-with-payu-tokenization)

**Environment**

| Test       | [https://test.payu.in/_payment](https://test.payu.in/_payment)     |
| ---------- | ------------------------------------------------------------------ |
| Production | [https://secure.payu.in/_payment](https://secure.payu.in/_payment) |

### Using complete card details

<Accordion title="Additional request parameters" icon="fa-database">
  Post the following parameters for cards. For complete list of parameters, refer to <Anchor label="Collect Payment API - EMI" target="_blank" href="ref:_payment_merchant_hosted_emi">Collect Payment API - EMI</Anchor> for the complete list parameters with **Try It** experience.

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

        <td style={{ textAlign: "left" }}>
          JP\*\*\*\*g
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          txnid
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String `The transaction ID is a reference number for a specific order that is generated by the merchant.
        </td>

        <td style={{ textAlign: "left" }}>
          kjsdho834580
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          amount  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String`The payment amount for the transaction.
        </td>

        <td style={{ textAlign: "left" }}>
          10.00
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          productinfo  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String`A brief description of the product.
        </td>

        <td style={{ textAlign: "left" }}>
          iPhone
        </td>
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
          `String` It defines the payment category that the merchant wants the customer to see by default on the PayU’s payment page. In this integration, "EMI" must be specified.
        </td>

        <td style={{ textAlign: "left" }}>
          EMI
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          bankcode `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` Post this parameter to identify payment options with unique bank codes and use getEmiAmountAccordingToInterest API to check for EMI code for corresponding tenure. For the list of EMI codes, refer to

          [EMI Codes](doc:emi-codes)

          .
        </td>

        <td style={{ textAlign: "left" }}>
          EMI03
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          ccnum
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` Use 13-19 digit card number for credit/debit cards (15 digits for AMEX, 13-19 for Maestro) and validate with LUHN algorithm. Refer to

          [Card Number Formats](https://docs.payu.in/docs/card-number-formats)

          and display error message on invalid input.
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
          `String` This parameter must contain the card’s expiry month – as entered by the user for the transaction. It must always be in 2 digits or in MM format. For months 1-9, this parameter must be appended with 0 – like 01, 02…09. For months 10-12, this parameter must not be appended – It should be 10,11 and 12 respectively.
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
          `String` This parameter must contain the card’s expiry year – as entered by the customer for the transaction. It must be of four digits.
        </td>

        <td style={{ textAlign: "left" }}>
          2021
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          threeDS2RequestData
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          `JSON` This parameter must contain the following information in JSON format. For more information, refer to

          [Handling 3DS Secure 2.0 Transaction](https://docs.payu.in/docs/collect-payments-with-cards-seamless#/handling-guest-checkout-transactions)

          .
        </td>

        <td style={{ textAlign: "left" }} />
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
</Accordion>

<HashingRequestParameters />

### Sample request

<Accordion title="Sample request" icon="fa-server">
  ```curl
  curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=H6mUfE0ccAY94j&amount=20000.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=EMI&bankcode=EMIA3&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=5123456789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=&hash=782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36"
  ```
  ```javascript
  /**
   * PayU Credit Card EMI Payment Integration using Fetch API
   * 
   * IMPORTANT: This should only be executed server-side (e.g., in Node.js), never in the browser,
   * as it contains sensitive payment information.
   */

  // Payment endpoint
  const url = 'https://test.payu.in/_payment';

  // Form data parameters
  const formData = new URLSearchParams();
  formData.append('key', 'JP***g');                // Your merchant key
  formData.append('txnid', 'H6mUfE0ccAY94j');     // Unique transaction ID
  formData.append('amount', '20000.00');          // Payment amount
  formData.append('firstname', 'Ashish');         // Customer's name
  formData.append('email', 'test@gmail.com');     // Customer's email
  formData.append('phone', '9876543210');         // Customer's phone
  formData.append('productinfo', 'iPhone');       // Product information
  formData.append('pg', 'EMI');                   // Payment gateway (EMI)
  formData.append('bankcode', 'EMIA3');           // Bank code (Axis Bank EMI)
  formData.append('surl', 'https://apiplayground-response.herokuapp.com/'); // Success URL
  formData.append('furl', 'https://apiplayground-response.herokuapp.com/'); // Failure URL
  // Card details - SENSITIVE DATA
  formData.append('ccnum', '5123456789012346');   // Card number
  formData.append('ccexpmon', '05');              // Expiry month
  formData.append('ccexpyr', '2022');             // Expiry year 
  formData.append('ccvv', '123');                 // CVV
  formData.append('ccname', '');                  // Cardholder name
  // Security hash
  formData.append('hash', '782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36');

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
      // Process payment response here, which may include EMI options
    })
    .catch(error => {
      console.error('Error:', error);
    });

  ```
  ```python
  import urllib.request
  import urllib.parse
  import json
  from typing import Dict, Any

  def process_credit_card_emi_payment() -> Dict[str, Any]:
      """
      Process credit card EMI payment using PayU's Merchant Hosted Checkout
      
      IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
      
      Returns:
          Dictionary with response from PayU API
      """
      # API endpoint
      url = "https://test.payu.in/_payment"
      
      # Prepare the form data
      payload = {
          "key": "JP***g",                   # Your merchant key
          "txnid": "H6mUfE0ccAY94j",         # Unique transaction ID
          "amount": "20000.00",              # Payment amount
          "firstname": "Ashish",             # Customer's name
          "email": "test@gmail.com",         # Customer's email
          "phone": "9876543210",             # Customer's phone
          "productinfo": "iPhone",           # Product information
          "pg": "EMI",                       # Payment gateway (EMI)
          "bankcode": "EMIA3",               # Bank code (Axis Bank EMI)
          "surl": "https://apiplayground-response.herokuapp.com/", # Success URL
          "furl": "https://apiplayground-response.herokuapp.com/", # Failure URL
          # Card details - SENSITIVE DATA
          "ccnum": "5123456789012346",       # Card number
          "ccexpmon": "05",                  # Expiry month
          "ccexpyr": "2022",                 # Expiry year
          "ccvv": "123",                     # CVV
          "ccname": "",                      # Cardholder name
          # Security hash
          "hash": "782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36"
      }
      
      # Convert dictionary to URL-encoded form data
      data = urllib.parse.urlencode(payload).encode('utf-8')
      
      # Set headers
      headers = {
          "accept": "application/json",
          "Content-Type": "application/x-www-form-urlencoded"
      }
      
      # Create a request object
      req = urllib.request.Request(url, data=data, headers=headers, method="POST")
      
      try:
          # Send the request and get the response
          with urllib.request.urlopen(req) as response:
              response_data = response.read().decode('utf-8')
              
              # Process and return response
              return {
                  "status_code": response.getcode(),
                  "response": response_data
              }
              
      except urllib.error.HTTPError as e:
          # Handle HTTP errors
          error_data = e.read().decode('utf-8')
          return {
              "status_code": e.code,
              "error": e.reason,
              "response": error_data
          }
          
      except Exception as e:
          # Handle other exceptions
          return {
              "status_code": 500,
              "error": str(e),
              "response": "An error occurred during payment processing"
          }

  # Example usage
  if __name__ == "__main__":
      result = process_credit_card_emi_payment()
      print(f"Status Code: {result['status_code']}")
      if 'error' in result:
          print(f"Error: {result['error']}")
      print(f"Response: {result['response']}")

  ```
  ```php
  <?php
  /**
   * Process credit card EMI payment using PayU's Merchant Hosted Checkout
   * 
   * IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
   * 
   * @return array Response from PayU API
   */
  function processCreditCardEmiPayment() {
      // API endpoint
      $url = "https://test.payu.in/_payment";
      
      // Prepare the form data
      $payload = [
          "key" => "JP***g",                    // Your merchant key
          "txnid" => "H6mUfE0ccAY94j",          // Unique transaction ID
          "amount" => "20000.00",               // Payment amount
          "firstname" => "Ashish",              // Customer's name
          "email" => "test@gmail.com",          // Customer's email
          "phone" => "9876543210",              // Customer's phone
          "productinfo" => "iPhone",            // Product information
          "pg" => "EMI",                        // Payment gateway (EMI)
          "bankcode" => "EMIA3",                // Bank code (Axis Bank EMI)
          "surl" => "https://apiplayground-response.herokuapp.com/", // Success URL
          "furl" => "https://apiplayground-response.herokuapp.com/", // Failure URL
          // Card details - SENSITIVE DATA
          "ccnum" => "5123456789012346",        // Card number
          "ccexpmon" => "05",                   // Expiry month
          "ccexpyr" => "2022",                  // Expiry year
          "ccvv" => "123",                      // CVV
          "ccname" => "",                       // Cardholder name
          // Security hash
          "hash" => "782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36"
      ];
      
      // Initialize cURL session
      $ch = curl_init($url);
      
      // Set cURL options
      curl_setopt($ch, CURLOPT_POST, true);
      curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
      curl_setopt($ch, CURLOPT_HTTPHEADER, [
          "accept: application/json",
          "Content-Type: application/x-www-form-urlencoded"
      ]);
      
      // For additional security in production
      curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true);
      curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);
      
      // Execute the request
      $response = curl_exec($ch);
      $statusCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
      $error = curl_error($ch);
      $errno = curl_errno($ch);
      
      // Close cURL session
      curl_close($ch);
      
      // Handle response
      if ($errno) {
          return [
              "status_code" => 500,
              "error" => $error,
              "response" => "cURL Error: " . $error
          ];
      }
      
      return [
          "status_code" => $statusCode,
          "response" => $response
      ];
  }

  // Example usage
  $result = processCreditCardEmiPayment();
  echo "Status Code: " . $result["status_code"] . "\n";
  if (isset($result["error"])) {
      echo "Error: " . $result["error"] . "\n";
  }
  echo "Response: " . $result["response"] . "\n";
  ?>

  ```
  ```java
  import java.io.BufferedReader;
  import java.io.DataOutputStream;
  import java.io.IOException;
  import java.io.InputStreamReader;
  import java.net.HttpURLConnection;
  import java.net.URL;
  import java.net.URLEncoder;
  import java.nio.charset.StandardCharsets;
  import java.util.HashMap;
  import java.util.Map;
  import java.util.StringJoiner;

  /**
   * PayU Credit Card EMI Payment Processor for Merchant Hosted Checkout
   * 
   * IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
   */
  public class PayUCreditCardEmiPaymentProcessor {
      
      // API endpoint
      private static final String PAYU_TEST_URL = "https://test.payu.in/_payment";
      
      /**
       * Process credit card EMI payment through PayU
       * @return PaymentResponse containing status and response data
       */
      public PaymentResponse processCreditCardEmiPayment() {
          try {
              // Initialize URL
              URL url = new URL(PAYU_TEST_URL);
              
              // Prepare form parameters
              Map<String, String> params = new HashMap<>();
              params.put("key", "JP***g");                    // Your merchant key
              params.put("txnid", "H6mUfE0ccAY94j");          // Unique transaction ID
              params.put("amount", "20000.00");               // Payment amount
              params.put("firstname", "Ashish");              // Customer's name
              params.put("email", "test@gmail.com");          // Customer's email
              params.put("phone", "9876543210");              // Customer's phone
              params.put("productinfo", "iPhone");            // Product information
              params.put("pg", "EMI");                        // Payment gateway (EMI)
              params.put("bankcode", "EMIA3");                // Bank code (Axis Bank EMI)
              params.put("surl", "https://apiplayground-response.herokuapp.com/"); // Success URL
              params.put("furl", "https://apiplayground-response.herokuapp.com/"); // Failure URL
              // Card details - SENSITIVE DATA
              params.put("ccnum", "5123456789012346");        // Card number
              params.put("ccexpmon", "05");                   // Expiry month
              params.put("ccexpyr", "2022");                  // Expiry year
              params.put("ccvv", "123");                      // CVV
              params.put("ccname", "");                       // Cardholder name
              // Security hash
              params.put("hash", "782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36");
              
              // Convert parameters to URL-encoded form data
              StringJoiner formData = new StringJoiner("&");
              for (Map.Entry<String, String> entry : params.entrySet()) {
                  formData.add(URLEncoder.encode(entry.getKey(), "UTF-8") + "=" + 
                               URLEncoder.encode(entry.getValue(), "UTF-8"));
              }
              byte[] postData = formData.toString().getBytes(StandardCharsets.UTF_8);
              
              // Configure connection
              HttpURLConnection conn = (HttpURLConnection) url.openConnection();
              conn.setRequestMethod("POST");
              conn.setRequestProperty("accept", "application/json");
              conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
              conn.setRequestProperty("Content-Length", String.valueOf(postData.length));
              conn.setDoOutput(true);
              conn.setConnectTimeout(5000);
              conn.setReadTimeout(15000);
              
              // Send request
              try (DataOutputStream dos = new DataOutputStream(conn.getOutputStream())) {
                  dos.write(postData);
                  dos.flush();
              }
              
              // Get response
              int responseCode = conn.getResponseCode();
              
              // Read response data
              StringBuilder response = new StringBuilder();
              try (BufferedReader reader = new BufferedReader(
                      new InputStreamReader(
                          responseCode >= 400 ? conn.getErrorStream() : conn.getInputStream(), 
                          StandardCharsets.UTF_8))) {
                          
                  String line;
                  while ((line = reader.readLine()) != null) {
                      response.append(line);
                  }
              }
              
              return new PaymentResponse(responseCode, response.toString(), null);
              
          } catch (IOException e) {
              // Handle exception
              return new PaymentResponse(500, null, "Error: " + e.getMessage());
          }
      }
      
      /**
       * Payment response wrapper class
       */
      public static class PaymentResponse {
          private final int statusCode;
          private final String response;
          private final String error;
          
          public PaymentResponse(int statusCode, String response, String error) {
              this.statusCode = statusCode;
              this.response = response;
              this.error = error;
          }
          
          public int getStatusCode() {
              return statusCode;
          }
          
          public String getResponse() {
              return response;
          }
          
          public String getError() {
              return error;
          }
          
          public boolean isSuccess() {
              return statusCode >= 200 && statusCode < 300;
          }
      }
      
      // Example usage
      public static void main(String[] args) {
          PayUCreditCardEmiPaymentProcessor processor = new PayUCreditCardEmiPaymentProcessor();
          PaymentResponse result = processor.processCreditCardEmiPayment();
          
          System.out.println("Status Code: " + result.getStatusCode());
          if (result.isSuccess()) {
              System.out.println("Response: " + result.getResponse());
          } else {
              System.out.println("Error: " + result.getError());
          }
      }
  }

  ```
  ```csharp
  using System;
  using System.Collections.Generic;
  using System.Net.Http;
  using System.Threading.Tasks;
  using System.Text;

  namespace PayUCreditCardEmiIntegration
  {
      /// <summary>
      /// PayU Credit Card EMI Payment Processor for Merchant Hosted Checkout
      /// 
      /// IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
      /// </summary>
      public class PayUCreditCardEmiPaymentProcessor
      {
          // API endpoint
          private const string PayuTestUrl = "https://test.payu.in/_payment";
          
          /// <summary>
          /// Process credit card EMI payment through PayU
          /// </summary>
          /// <returns>PaymentResponse containing status and response data</returns>
          public async Task<PaymentResponse> ProcessCreditCardEmiPaymentAsync()
          {
              try
              {
                  // Prepare form parameters
                  var formData = new Dictionary<string, string>
                  {
                      { "key", "JP***g" },                     // Your merchant key
                      { "txnid", "H6mUfE0ccAY94j" },           // Unique transaction ID
                      { "amount", "20000.00" },                // Payment amount
                      { "firstname", "Ashish" },               // Customer's name
                      { "email", "test@gmail.com" },           // Customer's email
                      { "phone", "9876543210" },               // Customer's phone
                      { "productinfo", "iPhone" },             // Product information
                      { "pg", "EMI" },                         // Payment gateway (EMI)
                      { "bankcode", "EMIA3" },                 // Bank code (Axis Bank EMI)
                      { "surl", "https://apiplayground-response.herokuapp.com/" }, // Success URL
                      { "furl", "https://apiplayground-response.herokuapp.com/" }, // Failure URL
                      // Card details - SENSITIVE DATA
                      { "ccnum", "5123456789012346" },         // Card number
                      { "ccexpmon", "05" },                    // Expiry month
                      { "ccexpyr", "2022" },                   // Expiry year
                      { "ccvv", "123" },                       // CVV
                      { "ccname", "" },                        // Cardholder name
                      // Security hash
                      { "hash", "782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36" }
                  };
                  
                  // Create HttpClient with timeout
                  using (var httpClient = new HttpClient())
                  {
                      httpClient.Timeout = TimeSpan.FromSeconds(30);
                      
                      // Convert form data to content
                      var content = new FormUrlEncodedContent(formData);
                      
                      // Add headers
                      content.Headers.ContentType = new System.Net.Http.Headers.MediaTypeHeaderValue("application/x-www-form-urlencoded");
                      httpClient.DefaultRequestHeaders.Add("accept", "application/json");
                      
                      // Send POST request
                      var response = await httpClient.PostAsync(PayuTestUrl, content);
                      
                      // Get response content
                      var responseContent = await response.Content.ReadAsStringAsync();
                      
                      return new PaymentResponse(
                          (int)response.StatusCode,
                          responseContent,
                          null
                      );
                  }
              }
              catch (Exception ex)
              {
                  // Handle exception
                  return new PaymentResponse(
                      500,
                      null,
                      $"Error: {ex.Message}"
                  );
              }
          }
          
          /// <summary>
          /// Payment response wrapper class
          /// </summary>
          public class PaymentResponse
          {
              public int StatusCode { get; }
              public string Response { get; }
              public string Error { get; }
              
              public PaymentResponse(int statusCode, string response, string error)
              {
                  StatusCode = statusCode;
                  Response = response;
                  Error = error;
              }
              
              public bool IsSuccess => StatusCode >= 200 && StatusCode < 300;
          }
      }
      
      // Example usage
      class Program
      {
          static async Task Main(string[] args)
          {
              var processor = new PayUCreditCardEmiPaymentProcessor();
              var result = await processor.ProcessCreditCardEmiPaymentAsync();
              
              Console.WriteLine($"Status Code: {result.StatusCode}");
              if (result.IsSuccess)
              {
                  Console.WriteLine($"Response: {result.Response}");
              }
              else
              {
                  Console.WriteLine($"Error: {result.Error}");
              }
          }
      }
  }

  ```
</Accordion>

### Using network tokens

#### Applicable scenarios

* Merchant has the card token, TAVV(Cryptogram), and the last four digits of the card
* The token could be created by the merchant or through another partner

> 📘 Note:
>
> This scenario is applicable if you are PCI compliant and got the network token and TAVV from any other aggregator or schemes and then sending the card transaction request in the form of authentication.

<Accordion title="Additional request parameters" icon="fa-database">
  Along the parameters listed in the [Collect Payment API - Merchant Hosted Checkout](ref:_payment_merchant_hosted_emi), include the following additional request parameters in your collect payment request with PayU. Check the response when you try enter the values in API Reference.

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
          **Value**
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td style={{ textAlign: "left" }}>
          ccvv
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter must contain the CVV number of the card – as entered by the customer for the transaction.  Note: If your customer is returning to your website to shop, you must fetch all the customer's stored cards from PayU, collect the CVV for the card the customer will be using to make payment and then post the CVV number to PayU.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          ccexpmon
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter must contain the network token expiry month.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          ccexpyr
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String`This parameter must contain the network token expiry year.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          store\_card\_token  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String`This must include the Network token generated at your end.
        </td>

        <td style={{ textAlign: "left" }}>
          1234 4567 2456 3566
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          storecard\_token\_type  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String`This parameter is used to specify the store card token type. For this scenario, you must include 1.
        </td>

        <td style={{ textAlign: "left" }}>
          1
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          additional\_info  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String`This parameter will contain the additional information in the following JSON format:  \{“last4Digits”: “1234”, “tavv”: “ABCDEFGH”,”trid”:”1234567890”, “tokenRefNo”:”abcde123456”}  Where:
        </td>

        <td style={{ textAlign: "left" }}>
          \{“last4Digits”: “1234”, “tavv”: “ABCDEFGH”,”trid”:”1234567890”, “tokenRefNo”:”abcde123456”}
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>

### Using issuer tokens

This scenario is applicable if you wanted to collect payments using issuer tokens.

#### Applicable scenarios

* Merchant has the card token, trMerchantId, tokenReferenceId, and the last four digits of the card
* The token could be created by the issuer

> 📘 Note:
>
> This scenario is applicable if you are PCI compliant and got the issuer token, **trMerchantId**, and **tokenReferenceId** and then sending the card transaction request in the form of authentication.

<Accordion title="Additional request parameters" icon="fa-database">
  Along the parameters listed in the [Collect Payment API - Merchant Hosted Checkout](ref:_payment_merchant_hosted_emi)., include the following additional request parameters in your collect payment request with PayU. Check the response when you try enter the values in API Reference.

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
          **Value**
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td style={{ textAlign: "left" }}>
          ccvv
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter must contain the CVV number of the card – as entered by the customer for the transaction.  Note: If your customer is returning to your website to shop, you must fetch all the customer’s stored cards from PayU, collect the CVV for the card the customer will be using to make payment and then post the CVV number to PayU.
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
          `String` This parameter must contain the network token expiry month.
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
          `String` This parameter must contain the network token expiry year.
        </td>

        <td style={{ textAlign: "left" }}>
          2022
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          store\_card\_token  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This must include the issuer token generated at your end.
        </td>

        <td style={{ textAlign: "left" }}>
          1234 4567 2456 3566
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          storecard\_token\_type  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter is used to specify the store card token type. For this scenario, you must include **2**.
        </td>

        <td style={{ textAlign: "left" }}>
          2
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          additional\_info  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `JSON` This parameter will contain the additional information in the following JSON format:  \{“trMerchantId”:”INBANPAYUWIBPAY011″,”tokenReferenceId”:”02ac786d-0081-4b1a-a2a6-b0755a83964c”,”tokenBank”:”HDFC”,”last4Digits”:”8179″}  Where:   **trMerchantId** is the Token Requestor Merchant ID.  **tokenReferenceId** (Token Reference ID) is generated specifically for card tokens.  **tokenBank** is the issuing token bank name. For example, “HDFC” can be sent in the request for Diners cards.  **last4Digits** must contain the last four digits of the card.
        </td>

        <td style={{ textAlign: "left" }}>
          \{“trMerchantId”:”INBANPAYUWIBPAY011″,”tokenReferenceId”:”02ac786d-0081-4b1a-a2a6-b0755a83964c”,”tokenBank”:”HDFC”,”last4Digits”:”8179″}
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>

### Using card tokenized with PayU

If the merchant has tokenized the card with PayU and needs to process the transaction using PayU token only.

#### Applicable scenarios

* Merchant has created the token using PayU as the partner

> 📘 Note:
>
> This scenario is applicable if any PCI or Non-PCI complied merchant sends the PayU token in a request for fulfilment purposes.

<Accordion title="Additional request parameters" icon="fa-database">
  Along the parameters listed in the <Anchor label="Collect Payment API - Merchant Hosted Checkout" target="_blank" href="ref:_payment_merchant_hosted">Collect Payment API - Merchant Hosted Checkout</Anchor>. include the following additional request parameters in your collect payment request with PayU. Check the response when you try enter the values in API Reference.

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
          ccvv
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter must contain the CVV number of the card – as entered by the customer for the transaction.  Note: If your customer is returning to your website to shop, you must fetch all the customer’s stored cards from PayU, collect the CVV for the card the customer will use to make payment, and then post the CVV number to PayU.
        </td>

        <td style={{ textAlign: "left" }}>
          123
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          storecard\_token\_type
        </td>

        <td style={{ textAlign: "left" }}>
          `String`This parameter is used to specify the store card token type. For this scenario, you must include **0**.
        </td>

        <td style={{ textAlign: "left" }}>
          0
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          user\_credentials  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter must contain the user credentials.
        </td>

        <td style={{ textAlign: "left" }}>
          a:b
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          store\_card\_token
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This must include the token generated by PayU for the card.
        </td>

        <td style={{ textAlign: "left" }}>
          1234 4567 2456 3566
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>

### Using card on a decoupled flow with network token or other partner tokenization

#### Applicable scenario

This scenario is applicable where you are on a decoupled flow. This is where you are using the PayU for either authentication or authorization only while using tokens created by the network or some other partner.

**Decoupled flow**: You are sending the authentication request to PayU and if the merchant wishes to send the authorization request eventually or to other aggregators.

<Accordion title="Additional request parameters" icon="fa-database">
  Along the parameters listed in the [Collect Payment API - Merchant Hosted Checkout](ref:_payment_merchant_hosted_emi), include the following additional request parameters in your collect payment request with PayU. Check the response when you try enter the values in API Reference.

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
          **Value**
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td style={{ textAlign: "left" }}>
          store\_card\_token  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This must include the network token available with the merchant.
        </td>

        <td style={{ textAlign: "left" }}>
          1234 4567 2456 3566
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          storecard\_token\_type  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `Integer` This parameter is used to specify any of the following store card token type, that is, tokenization partner.   **0** – PayU token  **1** – Network token  **2** – Issuer token   \*

          * Note\*\*: For this scenario, you must include**1**.
        </td>

        <td style={{ textAlign: "left" }}>
          1
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          additional\_info  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `JSON` This parameter will contain the additional information in the following JSON format that PayU would fetch TAVV/Cryptogram internally.  \{ “last4Digits”: “1234”, “tavv”: “ABCDEFGH”}  Where:   **trid** (Token Requestor ID) is the identity given by the networks for creating the tokens. You should be able to get the same from your token provider.  **tokenRefNo** (Token Reference Number) is generated along with the network token. . You should be able to get the same from your token provider.  **TAVV** is a 20-byte Base64-encoded binary value that is used with tokens.

          * *Notes*\*:    The last 4 digits of cards is mandatory for all transactions.    Some payment gateways require the Token Requester ID (trid) and Token Reference Number (tokenRefNo) to be passed for processing the transaction. Not passing these values will restrict the number of payment gateways available for processing the transaction.   Token Requester ID (trid) and Token Reference Number (tokenRefNo) are mandatory for Diners token transactions.
        </td>

        <td style={{ textAlign: "left" }}>
          \{ “last4Digits”: “1234”, “tavv”: “ABCDEFGH” }
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>

### Using card on a decoupled flow with PayU tokenization

#### Applicable scenario

This scenario is the application on a decoupled flow using the PayU for either authentication or authorization only with tokens created in partnership with PayU.

**Direct Authorisation Flow**: When you have done the authentication from some other aggregator and authorization request is coming to PayU.

<Accordion title="Additional request parameters" icon="fa-database">
  Along the parameters listed in the [Collect Payment API - Merchant Hosted Checkout](ref:_payment_merchant_hosted_emi), include the following additional request parameters in your collect payment request with PayU. Check the response when you try enter the values in API Reference.

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
          **Value**
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td style={{ textAlign: "left" }}>
          ccvv
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          varchar This parameter must contain the CVV number of the card – as entered by the customer for the transaction.

          * *Note*\*: If your customer is returning to your website to shop, you must fetch all the customer’s stored cards from PayU, collect the CVV for the card the customer will be using to make payment and then post the CVV number to PayU.
        </td>

        <td style={{ textAlign: "left" }}>
          123
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          store\_card\_token  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          varchar This must include the token generated by PayU for the card.
        </td>

        <td style={{ textAlign: "left" }}>
          1234 4567 2456 3566
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          storecard\_token\_type  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          integer This parameter is used to specify any of the following store card token type, that is, tokenization partner.   **0** – PayU token  **1** – Network token  **2** – Issuer token

          * *Note*\*: For this scenario, you must include**0**.
        </td>

        <td style={{ textAlign: "left" }}>
          0
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          additional\_info  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          JSON This parameter will contain the additional information in the following JSON format that PayU would fetch TAVV/Cryptogram internally.  \{“last4Digits”: “1234”, “tavv”: “ABCDEFGH”,”trid”:”1234567890”, “tokenRefNo”:”abcde123456”}  Where:   **trid** (Token Requestor ID) is the identity given by the networks for creating the tokens. You should be able to get the same from your token provider.  **tokenRefNo** (Token Reference Number) is generated along with the network token. . You should be able to get the same from your token provider.  **TAVV** is a 20-byte Base64-encoded binary value that is used with tokens.

          * *Notes*\*:    The last 4 digits of cards is mandatory for all transactions.    Some payment gateways require the Token Requester ID (trid) and Token Reference Number (tokenRefNo) to be passed for processing the transaction. Not passing these values will restrict the number of payment gateways available for processing the transaction.   Token Requester ID (trid) and Token Reference Number (tokenRefNo) are mandatory for Diners token transactions.
        </td>

        <td style={{ textAlign: "left" }}>
          \{“last4Digits”: “1234”, “tavv”: “ABCDEFGH”,”trid”:”1234567890”, “tokenRefNo”:”abcde123456”}
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>

## Step 4: Check the PayU response

<ReverseHashing />

### Sample response

You need to look for the following parameters in the response:

* **PG_TYPE**
* **bankcode**

<Accordion title="Sample response" icon="fa-reply">
  The formatted sample response from PayU is similar to the following:

  ```
  Array
  (
      [mihpayid] => 403993715523602563
      [status] => success
      [unmappedstatus] => captured
      [key] => JP***g
      [txnid] => v2tWbbdUOuacK9
      [amount] => 20000.00
      [discount] => 0.00
      [net_amount_debit] => 20000.00
      [addedon] => 2021-07-27 11:14:44
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
      [phone] => 1234567890
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
      [hash] => 10f8ead10cdf5f9b7bf9046987de046d63d62d6679dded9d5da8145f459066943570eec4aa184494ae77f99a8bcd55452af3c4eff0d7a7d3ba809c97b7c73045
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
      [PG_TYPE] => EMI-PG
      [bank_ref_num] => 3d7cc4a4-00c8-4705-a0e7-5708d2c2bb75
      [bankcode]=> EMIA3
      [error] => E000
      [error_Message] => No Error
      [name_on_card] => payu
      [cardnum] =>512345XXXXXX2346
  )
  ```
</Accordion>

## Step 5: Verify the payment

<Verify_Payment_Tabs />
