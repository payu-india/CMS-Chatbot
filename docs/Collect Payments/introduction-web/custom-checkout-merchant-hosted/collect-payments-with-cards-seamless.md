---
title: Cards Integration
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
PayU supports the following debit cards and credit cards:

* American Express (AMEX)
* Visa
* Mastercard
* Diners
* Rupay

<Callout icon="📘" theme="info">
  **Notes**: 

  * PayU accepts domestic and international transactions, but international transactions need to be enabled by writing to PayU Integration Team (<Anchor label="integration@pay.in" target="_blank" href="mailto:integration@pay.in">integration@pay.in</Anchor>).
  * If you are storing or transmitting cardholder data, you must fill the “<Anchor label="Self-Assessment Questionnaire A-EP and Attestation of Compliance" target="_blank" href="https://www.pcisecuritystandards.org/documents/PCI-DSS-v3_2-SAQ-A_EP-rev1_1.pdf">Self-Assessment Questionnaire A-EP and Attestation of Compliance</Anchor>” form. For more information on Save Cards API integration, refer to PayU Save Cards API Integration docs.
</Callout>

<Callout icon="👍" theme="okay">
  Experience the end-to-end **Merchant Hosted Checkout** > **Net Banking** flow and instantly generate the complete code for seamless, zero-coding integration into your website.

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

                            <button onclick="window.open('https://payu.in/integrationlab/seamless/sm-nb-status', '_blank')" 
                                    class="tooltip-btn" 
                                    data-tooltip="Click here to see the Merchant Hosted Checkout > Net Banking end-to-end integration and instantly generate the complete code needed for a zero-coding setup on your website.">
                                Experience the flow and get the code
                            </button>
  `}</HTMLBlock>
</Callout>

<RegisterMerchantPrerequiste />

## Steps to Integrate

<Cards>
  <Card title="1. Validate the card type" href="https://docs.payu.in/docs/collect-payments-with-cards-seamless#step-1-validate-the-card-type">
    Validate the card type using the card BIN API>
  </Card>

  <Card title="2. Initiate the Payment to PayU" href="https://docs.payu.in/docs/collect-payments-with-cards-seamless#step-2-initiate-the-payment-to-payu">
    Initiate the payment to PayU with pg=CC and bankcode=CC
  </Card>

  <Card title="3. Check response from PayU" href="https://docs.payu.in/docs/collect-payments-with-cards-seamless#step-3-check-response-from-payu">
    Check the response from PayU
  </Card>

  <Card title="4. Verify the payment" href="https://docs.payu.in/docs/collect-payments-with-cards-seamless#step-4-verify-the-payment">
    Verify the payment using verify\_payment and monitor using webhooks
  </Card>
</Cards>

### Handling Transactions

<Cards>
  <Card title="Guest Checkout Transactions" href="#handling-guest-checkout-transactions" target="_blank">
    For handling Guest Checkout transaction, you need to include additional parameter based on the Guest Checkout flow.
  </Card>

  <Card title="3DS Secure 2.0 Transactions" href="#handling-3ds-secure-20-transaction" target="_blank">
    For handling 3DS Secure 2.0 transaction, you need to include threeDS2RequestData as an additional parameter to \_payment.
  </Card>
</Cards>

<Callout icon="📘" theme="info">
  **Postman Collection**

  <Postman_collection />
</Callout>

## Step 1: Validate the card type

When customers use debit cards or credit cards on your website, you can validate the card type with the first six digits. Use the **getBinInfo** API (known as BIN API) to validate the type of card. For more information, refer to  <Anchor label="BIN APIs" target="_blank" href="https://docs.payu.in/reference/get_bin_info_api">BIN APIs</Anchor>.

| Environment            | URL                                                                                                  |
| :--------------------- | :--------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/merchant/postservice?form=2](https://test.payu.in/merchant/postservice?form=2) |
| Production Environment | [https://info.payu.in/merchant/postservice?form=2](https://info.payu.in/merchant/postservice?form=2) |

<Accordion title="Sample request" icon="fa-code">
  ## For Single Card

  The following values are specified in the var1, var2, and var5 for this scenario:

  * var1 = 1
  * var2 = 512345
  * var5 = 1

  ```cURL
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g" \
  -d "command=getBinInfo" \
  -d "var1=2" \
  -d "var2=512345" \
  -d "var3=" \
  -d "var4=" \
  -d "var5=1" \
  -d "hash={{hash_value}}"
  ```

  ### Hashing Logic

  <KeyHashForGeneralParametersDescription />
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  ### Success Scenario

  ```php
  $response = array(
    'status' => 1,
    'data'   => array(
        'bins_data' => array(
            'issuing_bank' => 'HDFC',
            'bin'           => '512345',
            'category'      => 'creditcard',
            'card_type'     => 'MAST',
            'is_domestic'   => 1,
        ),
    ),
  );
  ```
</Accordion>

## Step 2: Initiate the payment to PayU

<Accordion title="Post Request Syntax & Composition" icon="fa-code">
  Post Request Syntax & Composition for Cards

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
  <input type="hidden" name="pg" value="CC" />
  <input type="hidden" name="bankcode" value="MAST" />
  <input type="hidden" name="ccnum" value="5123456789012346" />
  <input type="hidden" name="ccname" value="Ashish Kumar" />
  <input type="hidden" name="ccvv" value="123" />
  <input type="hidden" name="ccexpmon" value="12" />
  <input type="hidden" name="ccexpyr" value="2021" />
  <input type="hidden" name="surl" value="your own success url" />
  <input type="hidden" name="furl" value="your own failure url" />
  <input type="hidden" name="phone" value="9988776655" />
  <input type="hidden" name="hash" value="eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972" />
  <input type="submit" value="submit"> </form>
  </body>
  </html>
  ```

  <Callout icon="📘" theme="info">
    **Note**: The above code block is for Merchant Checkout integration on the credit card call for the test environment.
  </Callout>
</Accordion>

<Accordion title="Request Parameters" icon="fa-table">
  Post the following parameters for the card payment to PayU using the Merchant Hosted integration.

  **Environment**

  |                            |                                                                         |
  | :------------------------- | :---------------------------------------------------------------------- |
  | **Test Environment**       | \<[https://test.payu.in/\_payment>](https://test.payu.in/_payment>)     |
  | **Production Environment** | \<[https://secure.payu.in/\_payment>](https://secure.payu.in/_payment>) |

  <Callout icon="📘" theme="info">
    **Reference**: For the **Try It** experience and response, refer to <Anchor label="Collect Payment API - Merchant Hosted Checkout" target="_blank" href="https://docs.payu.in/reference/_payment_merchant_hosted">Collect Payment API - Merchant Hosted Checkout</Anchor> under API Reference.
  </Callout>

  <Table align={["left","left","left"]}>
    <thead>
      <tr>
        <th>
          Parameter
        </th>

        <th>
          Description
        </th>

        <th>
           Example
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          key
          `mandatory`
        </td>

        <td>
          `String `Merchant key provided by PayU during onboarding.
        </td>

        <td>
          JP\*\*\*g
        </td>
      </tr>

      <tr>
        <td>
          txnid
          `mandatory`
        </td>

        <td>
          `String `The transaction ID is a reference number for a specific order that is generated by the merchant.
        </td>

        <td>
          ashdfu72634
        </td>
      </tr>

      <tr>
        <td>
          amount  `mandatory`
        </td>

        <td>
          `String`The payment amount for the transaction.
        </td>

        <td>
           
        </td>
      </tr>

      <tr>
        <td>
          productinfo  `mandatory`
        </td>

        <td>
          `String`A brief description of the product.
        </td>

        <td>
           
        </td>
      </tr>

      <tr>
        <td>
          firstname  `mandatory`
        </td>

        <td>
          `String` The first name of the customer.
        </td>

        <td>
          Ashish
        </td>
      </tr>

      <tr>
        <td>
          email
          `mandatory`
        </td>

        <td>
          `String`The email address of the customer.
        </td>

        <td>
           
        </td>
      </tr>

      <tr>
        <td>
          phone
          `mandatory`
        </td>

        <td>
          `String`The phone number of the customer.
        </td>

        <td>
           
        </td>
      </tr>

      <tr>
        <td>
          pg
          `mandatory`
        </td>

        <td>
          `String` The pg parameter determines which payment tabs will be displayed on the PayU page. For cards, 'CC' will be the value.
        </td>

        <td>
          CC
        </td>
      </tr>

      <tr>
        <td>
          bankcode `mandatory`
        </td>

        <td>
          `String` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option’s bank code value in it. For more information, refer to [Card Type Codes and Supported Banks for Cards](doc:card-type-codes-and-supported-banks-for-cards)

          .
        </td>

        <td>
          AMEX
        </td>
      </tr>

      <tr>
        <td>
          ccnum
          `mandatory`
        </td>

        <td>
          `String` Use 13-19 digit card number for credit/debit cards (15 digits for AMEX, 13-19 for Maestro) and validate with LUHN algorithm. Refer to

          [Card Number Formats](doc:card-number-formats)

          and display error message on invalid input.
        </td>

        <td>
          5123456789012346
        </td>
      </tr>

      <tr>
        <td>
          ccname  `mandatory`
        </td>

        <td>
          `String` This parameter must contain the name on card – as entered by the customer for the transaction.
        </td>

        <td>
          Ashish Kumar
        </td>
      </tr>

      <tr>
        <td>
          ccvv
          `mandatory`
        </td>

        <td>
          `String` Use 3-digit CVV number for credit/debit cards and 4-digit security code (4DBC/CID) for AMEX cards. Validate with BIN API.
        </td>

        <td>
          123
        </td>
      </tr>

      <tr>
        <td>
          ccexpmon  `mandatory`
        </td>

        <td>
          `String` This parameter must contain the card’s expiry month – as entered by the user for the transaction. It must always be in 2 digits or in MM format. For months 1-9, this parameter must be appended with 0 – like 01, 02…09. For months 10-12, this parameter must not be appended – It should be 10,11 and 12 respectively.
        </td>

        <td>
          10
        </td>
      </tr>

      <tr>
        <td>
          ccexpyr
          `mandatory`
        </td>

        <td>
          `String` This parameter must contain the card’s expiry year – as entered by the customer for the transaction. It must be of four digits.
        </td>

        <td>
          2021
        </td>
      </tr>

      <tr>
        <td>
          furl
          `mandatory`
        </td>

        <td>
          `String`The failure URL, which is the page PayU will redirect to if the transaction is failure.
        </td>

        <td />
      </tr>

      <tr>
        <td>
          surl
          `mandatory`
        </td>

        <td>
          `String`The success URL, which is the page PayU will redirect to if the transaction is successful.
        </td>

        <td />
      </tr>

      <tr>
        <td>
          hash
          `mandatory`
        </td>

        <td>
          `String`It is the hash calculated by the merchant. The hash calculation logic is:
          `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)`
        </td>

        <td />
      </tr>

      <tr>
        <td>
          address1
          `optional`
        </td>

        <td>
          `String` The first line of the billing address.

          * *For Fraud Detection*\*: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.
        </td>

        <td />
      </tr>

      <tr>
        <td>
          address2
          `optional`
        </td>

        <td>
          `String` The second line of the billing address.
        </td>

        <td />
      </tr>

      <tr>
        <td>
          city
          `optional`
        </td>

        <td>
          `String` The city where your customer resides as part of the billing address.
        </td>

        <td />
      </tr>

      <tr>
        <td>
          state
          `optional`
        </td>

        <td>
          `String` The state where your customer resides as part of the billing address,
        </td>

        <td />
      </tr>

      <tr>
        <td>
          country
          `optional`
        </td>

        <td>
          `String` The country where your customer resides.
        </td>

        <td />
      </tr>

      <tr>
        <td>
          zipcode
          `optional`
        </td>

        <td>
          `String` Billing address zip code is mandatory for the cardless EMI option.
          `Character Limit`-20
        </td>

        <td />
      </tr>

      <tr>
        <td>
          udf1
          `optional`
        </td>

        <td>
          `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.
        </td>

        <td />
      </tr>

      <tr>
        <td>
          udf2
          `optional`
        </td>

        <td>
          `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.
        </td>

        <td />
      </tr>

      <tr>
        <td>
          udf3
          `optional`
        </td>

        <td>
          `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.
        </td>

        <td />
      </tr>

      <tr>
        <td>
          udf4
          `optional`
        </td>

        <td>
          `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.
        </td>

        <td />
      </tr>

      <tr>
        <td>
          udf5
          `optional`
        </td>

        <td>
          `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.
        </td>

        <td />
      </tr>
    </tbody>
  </Table>

  <Accordion title="Understanding Hashing and sample code" icon="fa-code">
    <HashingRequestParameters />

    #### Hashing Sample Code

    <HashingSample />
  </Accordion>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
  # IMPORTANT: This is a server-side call, never execute this client-side
  # Replace placeholders with actual values
  # In production: Use environment variables for sensitive values

  curl -X POST "https://test.payu.in/_payment" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=YOUR_MERCHANT_KEY" \
    -d "txnid=TXN_12345" \
    -d "amount=1000.00" \
    -d "productinfo=Product+Description" \
    -d "firstname=Customer+Name" \
    -d "email=customer@example.com" \
    -d "phone=9988776655" \
    -d "pg=CC" \
    -d "bankcode=CC" \
    -d "ccnum=CARD_NUMBER" \
    -d "ccexpmon=MM" \
    -d "ccexpyr=YY" \
    -d "ccvv=CVV" \
    -d "ccname=NAME_ON_CARD" \
    -d "surl=https://yourwebsite.com/success" \
    -d "furl=https://yourwebsite.com/failure" \
    -d "hash=HASH_GENERATED_ON_SERVER"
  ```
  ```python
  import urllib.request
  import urllib.parse
  import json
  import os
  from typing import Dict, Any

  def process_payment(payment_data: Dict[str, Any]) -> Dict[str, Any]:
      """
      Process payment using PayU's Merchant Hosted Checkout
      
      IMPORTANT: This is a server-side function. Never expose card details to client-side code.
      This handles sensitive card data and requires PCI DSS compliance.
      
      Args:
          payment_data: Dictionary containing payment information
          
      Returns:
          Dictionary with response from PayU API
      """
      # API endpoint - Use different URLs for test/production environments
      url = "https://test.payu.in/_payment"  # Test URL
      # url = "https://secure.payu.in/_payment"  # Production URL
      
      # Prepare the form data with proper URL encoding
      # In production: Get merchant_key and hash from secure environment variables
      payload = {
          "key": "YOUR_MERCHANT_KEY",           # Replace with actual merchant key
          "txnid": "TXN_12345",                 # Generate unique transaction ID
          "amount": "1000.00",                  # Amount to be charged
          "productinfo": "Product Description", # Description of product/service
          "firstname": "Customer Name",         # Customer's first name
          "email": "customer@example.com",      # Customer's email
          "phone": "9988776655",                # Customer's phone number
          "pg": "CC",                           # Payment gateway (CC for credit card)
          "bankcode": "CC",                     # Bank code (CC for credit card)
          
          # SENSITIVE DATA - Handle with care according to PCI DSS requirements
          "ccnum": "CARD_NUMBER",               # Credit card number
          "ccexpmon": "MM",                     # Expiry month (2 digits)
          "ccexpyr": "YY",                      # Expiry year (2 digits)
          "ccvv": "CVV",                        # Card verification value
          "ccname": "NAME_ON_CARD",             # Name on the card
          
          # Success and failure URLs
          "surl": "https://yourwebsite.com/success",  # Success callback URL
          "furl": "https://yourwebsite.com/failure",  # Failure callback URL
          
          # Hash is generated on server using specific algorithm provided by PayU
          # See PayU documentation for the exact hash generation logic
          "hash": "HASH_GENERATED_ON_SERVER",   # Security hash
      }
      
      # Convert dictionary to URL-encoded form data
      data = urllib.parse.urlencode(payload).encode('utf-8')
      
      # Set headers
      headers = {
          "Content-Type": "application/x-www-form-urlencoded"
      }
      
      # Create a request object
      req = urllib.request.Request(url, data=data, headers=headers, method="POST")
      
      try:
          # Send the request and get the response
          with urllib.request.urlopen(req) as response:
              response_data = response.read().decode('utf-8')
              
              # In production, implement proper response handling and logging
              # (but never log full card details)
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
              "response": "An error occurred during the payment process"
          }

  # Example usage:
  # payment_result = process_payment(payment_data)
  # print(f"Status: {payment_result['status_code']}")
  # Process the response appropriately

  ```
  ```php
  <?php
  /**
   * Process payment using PayU's Merchant Hosted Checkout
   * 
   * IMPORTANT: This is a server-side function. Never expose card details to client-side code.
   * This handles sensitive card data and requires PCI DSS compliance.
   * 
   * @param array $paymentData Payment information
   * @return array Response from PayU API
   */
  function processPayment($paymentData = []) {
      // API endpoint - Use different URLs for test/production environments
      $url = "https://test.payu.in/_payment"; // Test URL
      // $url = "https://secure.payu.in/_payment"; // Production URL
      
      // Prepare the form data
      // In production: Get merchant_key and hash from secure environment variables
      $payload = [
          "key" => "YOUR_MERCHANT_KEY",           // Replace with actual merchant key
          "txnid" => "TXN_12345",                 // Generate unique transaction ID
          "amount" => "1000.00",                  // Amount to be charged
          "productinfo" => "Product Description", // Description of product/service
          "firstname" => "Customer Name",         // Customer's first name
          "email" => "customer@example.com",      // Customer's email
          "phone" => "9988776655",                // Customer's phone number
          "pg" => "CC",                           // Payment gateway (CC for credit card)
          "bankcode" => "CC",                     // Bank code (CC for credit card)
          
          // SENSITIVE DATA - Handle with care according to PCI DSS requirements
          "ccnum" => "CARD_NUMBER",               // Credit card number
          "ccexpmon" => "MM",                     // Expiry month (2 digits)
          "ccexpyr" => "YY",                      // Expiry year (2 digits)
          "ccvv" => "CVV",                        // Card verification value
          "ccname" => "NAME_ON_CARD",             // Name on the card
          
          // Success and failure URLs
          "surl" => "https://yourwebsite.com/success", // Success callback URL
          "furl" => "https://yourwebsite.com/failure", // Failure callback URL
          
          // Hash is generated on server using specific algorithm provided by PayU
          // See PayU documentation for the exact hash generation logic
          "hash" => "HASH_GENERATED_ON_SERVER",   // Security hash
      ];
      
      // Initialize cURL session
      $ch = curl_init($url);
      
      // Set cURL options
      curl_setopt($ch, CURLOPT_POST, true);
      curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
      curl_setopt($ch, CURLOPT_HTTPHEADER, [
          "Content-Type: application/x-www-form-urlencoded"
      ]);
      
      // For additional security in production
      curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true);
      curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);
      
      // Execute the request
      $response = curl_exec($ch);
      $status_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
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
      
      // In production, implement proper response handling and logging
      // (but never log full card details)
      return [
          "status_code" => $status_code,
          "response" => $response
      ];
  }

  // Example usage:
  // $paymentResult = processPayment($paymentData);
  // echo "Status: " . $paymentResult["status_code"];
  // Process the response appropriately
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
   * PayU Payment Processor for Merchant Hosted Checkout
   * 
   * IMPORTANT: This is a server-side implementation. Never expose card details to client-side code.
   * This handles sensitive card data and requires PCI DSS compliance.
   */
  public class PayUPaymentProcessor {
      
      // API endpoints - Use different URLs for test/production environments
      private static final String TEST_URL = "https://test.payu.in/_payment";
      private static final String PROD_URL = "https://secure.payu.in/_payment";
      
      /**
       * Process payment using PayU Merchant Hosted Checkout
       * 
       * @return PaymentResponse containing status and response data
       */
      public PaymentResponse processPayment() {
          try {
              // Use test URL (change to PROD_URL in production)
              URL url = new URL(TEST_URL);
              
              // Prepare form parameters
              // In production: Get merchant_key and hash from secure environment variables
              Map<String, String> params = new HashMap<>();
              params.put("key", "YOUR_MERCHANT_KEY");           // Replace with actual merchant key
              params.put("txnid", "TXN_12345");                 // Generate unique transaction ID
              params.put("amount", "1000.00");                  // Amount to be charged
              params.put("productinfo", "Product Description"); // Description of product/service
              params.put("firstname", "Customer Name");         // Customer's first name
              params.put("email", "customer@example.com");      // Customer's email
              params.put("phone", "9988776655");                // Customer's phone number
              params.put("pg", "CC");                           // Payment gateway (CC for credit card)
              params.put("bankcode", "CC");                     // Bank code (CC for credit card)
              
              // SENSITIVE DATA - Handle with care according to PCI DSS requirements
              params.put("ccnum", "CARD_NUMBER");               // Credit card number
              params.put("ccexpmon", "MM");                     // Expiry month (2 digits)
              params.put("ccexpyr", "YY");                      // Expiry year (2 digits)
              params.put("ccvv", "CVV");                        // Card verification value
              params.put("ccname", "NAME_ON_CARD");             // Name on the card
              
              // Success and failure URLs
              params.put("surl", "https://yourwebsite.com/success"); // Success callback URL
              params.put("furl", "https://yourwebsite.com/failure"); // Failure callback URL
              
              // Hash is generated on server using specific algorithm provided by PayU
              // See PayU documentation for the exact hash generation logic
              params.put("hash", "HASH_GENERATED_ON_SERVER");   // Security hash
              
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
              
              // In production, implement proper response handling and logging
              // (but never log full card details)
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
      
      // Example usage:
      public static void main(String[] args) {
          PayUPaymentProcessor processor = new PayUPaymentProcessor();
          PaymentResponse result = processor.processPayment();
          
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

  namespace PayUIntegration
  {
      /// <summary>
      /// PayU Payment Processor for Merchant Hosted Checkout
      /// 
      /// IMPORTANT: This is a server-side implementation. Never expose card details to client-side code.
      /// This handles sensitive card data and requires PCI DSS compliance.
      /// </summary>
      public class PayUPaymentProcessor
      {
          // API endpoints - Use different URLs for test/production environments
          private const string TestUrl = "https://test.payu.in/_payment";
          private const string ProdUrl = "https://secure.payu.in/_payment";
          
          /// <summary>
          /// Process payment using PayU Merchant Hosted Checkout
          /// </summary>
          /// <returns>PaymentResponse containing status and response data</returns>
          public async Task<PaymentResponse> ProcessPaymentAsync()
          {
              try
              {
                  // Use test URL (change to ProdUrl in production)
                  string url = TestUrl;
                  
                  // Prepare form parameters
                  // In production: Get merchant_key and hash from secure environment variables
                  var formData = new Dictionary<string, string>
                  {
                      { "key", "YOUR_MERCHANT_KEY" },           // Replace with actual merchant key
                      { "txnid", "TXN_12345" },                 // Generate unique transaction ID
                      { "amount", "1000.00" },                  // Amount to be charged
                      { "productinfo", "Product Description" }, // Description of product/service
                      { "firstname", "Customer Name" },         // Customer's first name
                      { "email", "customer@example.com" },      // Customer's email
                      { "phone", "9988776655" },                // Customer's phone number
                      { "pg", "CC" },                           // Payment gateway (CC for credit card)
                      { "bankcode", "CC" },                     // Bank code (CC for credit card)
                      
                      // SENSITIVE DATA - Handle with care according to PCI DSS requirements
                      { "ccnum", "CARD_NUMBER" },               // Credit card number
                      { "ccexpmon", "MM" },                     // Expiry month (2 digits)
                      { "ccexpyr", "YY" },                      // Expiry year (2 digits)
                      { "ccvv", "CVV" },                        // Card verification value
                      { "ccname", "NAME_ON_CARD" },             // Name on the card
                      
                      // Success and failure URLs
                      { "surl", "https://yourwebsite.com/success" }, // Success callback URL
                      { "furl", "https://yourwebsite.com/failure" }, // Failure callback URL
                      
                      // Hash is generated on server using specific algorithm provided by PayU
                      // See PayU documentation for the exact hash generation logic
                      { "hash", "HASH_GENERATED_ON_SERVER" }    // Security hash
                  };
                  
                  // Create HttpClient with timeout
                  using (var httpClient = new HttpClient())
                  {
                      httpClient.Timeout = TimeSpan.FromSeconds(30);
                      
                      // Convert form data to content
                      var content = new FormUrlEncodedContent(formData);
                      
                      // Send POST request
                      var response = await httpClient.PostAsync(url, content);
                      
                      // Get response content
                      var responseContent = await response.Content.ReadAsStringAsync();
                      
                      // In production, implement proper response handling and logging
                      // (but never log full card details)
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
      
      // Example usage:
      public class Program
      {
          public static async Task Main(string[] args)
          {
              var processor = new PayUPaymentProcessor();
              var result = await processor.ProcessPaymentAsync();
              
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

#### Sample request for saved card

<Accordion title="Sample request for saved card" icon="fa-code">
  <Accordion title="Request parameters" icon="fa-info-table">
    <HTMLBlock>{`
                                                                                                                                                                                                                                  <Table>
                                                                                                                                                                                                                                    <thead>
                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <th>
                                                                                                                                                                                                                                          Parameter
                                                                                                                                                                                                                                        </th>

                                                                                                                                                                                                                                        <th>
                                                                                                                                                                                                                                          Description
                                                                                                                                                                                                                                        </th>

                                                                                                                                                                                                                                        <th>
                                                                                                                                                                                                                                          Example
                                                                                                                                                                                                                                        </th>
                                                                                                                                                                                                                                      </tr>
                                                                                                                                                                                                                                    </thead>

                                                                                                                                                                                                                                    <tbody>
                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          key
                                                                                                                                                                                                                                          <br/><code>mandatory</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>String</code> The merchant key is a unique identifier for a merchant account in PayU's database.
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          Your Test Key
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          api_version
                                                                                                                                                                                                                                          <br/><code>optional</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>String</code> The API version for this API.
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          1
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          txnid
                                                                                                                                                                                                                                          <br/><code>mandatory</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>String</code> The transaction ID is a reference number for a specific order that is generated by the merchant. It is used to track the order and must be unique. PayU's system will not accept duplicate transaction IDs.
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          s7hhDQVWvbhBdN
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          amount
                                                                                                                                                                                                                                          <br/><code>mandatory</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>String</code> This field should contain the payment amount for the transaction. If you want to use the cardless EMI option, the amount must be at least Rs. 8000
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          10.00
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          productinfo
                                                                                                                                                                                                                                          <br/><code>mandatory</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>String</code> It should be a string containing a brief description of the product.\`\`\`

                                                                                                                                                                                                                                          Character Limit-100
                                                                                                                                                                                                                                          \`\`\`
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          iPhone
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          firstname
                                                                                                                                                                                                                                          <br/><code>mandatory</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>String</code> The first name of the customer.\`\`\`

                                                                                                                                                                                                                                          Character Limit-60
                                                                                                                                                                                                                                          \`\`\`
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          Ashish
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          email
                                                                                                                                                                                                                                          <br/><code>mandatory</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>String</code> The email of the customer.\`\`\`

                                                                                                                                                                                                                                          Character Limit-50
                                                                                                                                                                                                                                          \`\`\`
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          [test@gmail.com](mailto:test@gmail.com)
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          phone
                                                                                                                                                                                                                                          <br/><code>mandatory</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>String</code> The phone number of the customer.  

                                                                                                                                                                                                                                          * \*Note\*\*: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          9876543210
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          lastname
                                                                                                                                                                                                                                          <br/><code>mandatory</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>String</code> The last name of the customer.\`\`\`

                                                                                                                                                                                                                                          Character Limit-60
                                                                                                                                                                                                                                          \`\`\`
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          Verma
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          address1
                                                                                                                                                                                                                                          <br/><code>optional</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>String</code> The first line of the billing address.\`\`\`

                                                                                                                                                                                                                                          Character Limit-100
                                                                                                                                                                                                                                          \`\`\`
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          address2
                                                                                                                                                                                                                                          <br/><code>optional</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>String</code> The second line of the billing address.<code>Character Limit-100</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          34 Saikripa-Estate, Tilak Nagar
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          city
                                                                                                                                                                                                                                          <br/><code>optional</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>String</code> The city where your customer resides as part of the billing address.
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          Mumbai
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          state
                                                                                                                                                                                                                                          <br/><code>optional</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>String</code> The state where your customer resides as part of the billing address,
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          Maharashtra
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          country
                                                                                                                                                                                                                                          <br/><code>optional</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>String</code> The country where your customer resides.<code>Character Limit-50</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          India
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          zipcode
                                                                                                                                                                                                                                          <br/><code>optional</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>String</code> Billing address zip code is mandatory for the cardless EMI option.\`\`\`

                                                                                                                                                                                                                                          Character Limit-20
                                                                                                                                                                                                                                          \`\`\`
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          400004
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          surl
                                                                                                                                                                                                                                          <br/><code>mandatory</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>String</code> The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          furl
                                                                                                                                                                                                                                          <br/><code>mandatory</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>String</code> The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          hash
                                                                                                                                                                                                                                          <br/><code>mandatory</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>String</code> It is used to avoid the possibility of transaction tampering. For more information on hash generation process, refer to [Generate Hash](doc:generate-hash-merchant-hosted).
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>eabec285da28fd 0e3054d41a4d24fe 9f7599c9d0b6664 6f7a9984303fd612 4044b6206daf831 e9a8bda28a6200d 318293a13d6c193 109b60bd4b4f8b09 c90972</code>
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <Glossary>pg</Glossary>
                                                                                                                                                                                                                                          <br/><code>mandatory</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>String</code> The pg parameter determines which payment tabs will be displayed. Here, use 'CC' as the value.
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          CC
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <Glossary>bankcode</Glossary>
                                                                                                                                                                                                                                          <br/><code>mandatory</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>String</code> Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. 
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          AMEX
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          udf1 - udf5
                                                                                                                                                                                                                                          <br/><code>optional</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.
                                                                                                                                                                                                                                          <code>Character Limit-255</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          Payment Preference, Shipping Method, Shipping Address1, Shipping City, Shipping Zip Code, etc.
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          ccnum
                                                                                                                                                                                                                                          <br/><code>optional</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>varchar</code> This parameter must contain the 13 to 19-digit card number for credit or debit cards in general. 
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          512***6789012346
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          ccname
                                                                                                                                                                                                                                          <br/><code>optional</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>varchar</code> It is the customer's name on card.
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          Ashish
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          ccvv
                                                                                                                                                                                                                                          <br/><code>optional</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>varchar</code> This parameter must contain the CVV number of the card – as entered by the customer for the transaction.
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          123
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          ccexpmon
                                                                                                                                                                                                                                          <br/><code>mandatory</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>integer</code> This parameter must contain the network token expiry month.
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          10
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          ccexpyr
                                                                                                                                                                                                                                          <br/><code>mandatory</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>integer</code> This parameter must contain the network token expiry year.
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          2022
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          store_card_token
                                                                                                                                                                                                                                          <br/><code>mandatory</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>varchar</code> This must include the Network token generated at your end.
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          1234 4567 2456 3566
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          storecard_token_type
                                                                                                                                                                                                                                          <br/><code>mandatory</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>integer</code> This parameter is used to specify the store card token type. For this scenario, you must include 1.
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          1
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>

                                                                                                                                                                                                                                      <tr>
                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          additional_info
                                                                                                                                                                                                                                          <br/><code>mandatory</code>
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          <code>varchar</code> This parameter will contain the additional information in the following JSON format:
                                                                                                                                                                                                                                          {"last4Digits": "1234", "<Glossary>TAVV</Glossary>": "ABCDEFGH","<Glossary>trid</Glossary>":"1234567890", "<Glossary>tokenRefNo</Glossary>":"abcde123456"}  
                                                                                                                                                                                                                                        </td>

                                                                                                                                                                                                                                        <td>
                                                                                                                                                                                                                                          {"last4Digits": "1234", "tavv": "ABCDEFGH","trid":"1234567890", "tokenRefNo":"abcde123456"}
                                                                                                                                                                                                                                        </td>
                                                                                                                                                                                                                                      </tr>
                                                                                                                                                                                                                                    </tbody>
                                                                                                                                                                                                                                  </Table>
    `}</HTMLBlock>
  </Accordion>

  <Accordion title="Collect Payment with Saved Card" icon="fa-code">
    ```curl
    curl -X POST "https://test.payu.in/_payment" \
      -H "accept: application/json" \
      -H "Content-Type: application/x-www-form-urlencoded" \
      -d "key=YourMerchantKey" \
      -d "txnid=NT_TXN_1234567890" \
      -d "amount=250.00" \
      -d "productinfo=Premium Subscription Plan" \
      -d "firstname=John" \
      -d "lastname=Doe" \
      -d "email=john.doe@example.com" \
      -d "phone=9876543210" \
      -d "surl=https://yourwebsite.com/payment/success" \
      -d "furl=https://yourwebsite.com/payment/failure" \
      -d "pg=CC" \
      -d "bankcode=VISA" \
      -d "ccexpmon=12" \
      -d "ccexpyr=2025" \
      -d "ccname=John Doe" \
      -d "store_card_token=4111111111111111" \
      -d "storecard_token_type=1" \
      -d "additional_info={\"last4Digits\":\"1111\",\"TAVV\":\"ABCD1234EFGH5678\",\"trid\":\"987654321012345\",\"tokenRefNo\":\"TKN_REF_12345678\"}" \
      -d "api_version=1" \
      -d "address1=123 Business District" \
      -d "address2=Tech Park Avenue" \
      -d "city=Bangalore" \
      -d "state=Karnataka" \
      -d "country=India" \
      -d "zipcode=560001" \
      -d "udf1=Premium_Plan" \
      -d "udf2=Monthly_Billing" \
      -d "udf3=Customer_ID_789" \
      -d "udf4=" \
      -d "udf5=" \
      -d "hash=b5c6d8e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9"

    ```

    <br />
  </Accordion>
</Accordion>

## Step 3: Check response from PayU

<ReverseHashing />

<Accordion title="Sample response (parsed)" icon="fa-code">
  * Success scenario

  ```
  Array
  (
      [mihpayid] => 403993715524069222
      [mode] => CC
      [status] => success
      [unmappedstatus] => captured
      [key] => JF***g
      [txnid] => EaE4ZO3vU4iPsp
      [amount] => 10.00
      [cardCategory] => domestic
      [discount] => 0.00
      [net_amount_debit] => 10
      [addedon] => 2021-09-08 19:37:19
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
      [hash] => ed99957adb08fea56c907b88e8d158a79c3562c67f96c298461509826f77a7ae9e88b2a176b3234c25f50bcd451271728719656f3bb59c13a52bebabc468615a
      [field1] => 0608273386032718000015
      [field2] => 986987
      [field3] => 10.00
      [field4] => 403993715524069222
      [field5] => 100
      [field6] => 02
      [field7] => AUTHPOSITIVE
      [field8] => 
      [field9] => Transaction is Successful
      [payment_source] => payu
      [PG_TYPE] => CC-PG
      [bank_ref_num] => 0608273386032718000015
      [bankcode] => CC
      [error] => E000
      [error_Message] => No Error
      [name_on_card] => payu
      [cardnum] => 512345XXXXXX2346
  )
  ```

  * Failure scenario

  ```
  Array
  (
      [mihpayid] => 20869277619
      [mode] => CC
      [status] => failure
      [unmappedstatus] => failed
      [key] => L43t1c
      [txnid] => 26ba7cd6a67b0a010542
      [amount] => 1.00
      [cardCategory] => domestic
      [discount] => 0.00
      [net_amount_debit] => 0.00
      [addedon] => 2024-09-05 17:46:10
      [productinfo] => Product Info
      [firstname] => Payu-Admin
      [lastname] => 
      [address1] => 
      [address2] => 
      [city] => 
      [state] => 
      [country] => 
      [zipcode] => 
      [email] => test@example.com
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
      [hash] => ac7720e4bc33e5494bec6d37302e522171175a987f9d47286bfd29e8a7fc794f56433fcacf0bc120db781c4dc1d05a4857d71e83f00f6ed6aa9c97a1938b9467
      [field1] => 
      [field2] => 
      [field3] => 
      [field4] => 
      [field5] => 05
      [field6] => 
      [field7] => AUTHNEGATIVE
      [field8] => 
      [field9] => Authorization failed at Bank
      [payment_source] => payu
      [pa_name] => PayU
      [PG_TYPE] => CC-PG
      [bank_ref_num] => 2409052690
      [bankcode] => AMEX
      [error] => E1903
      [error_Message] => Authorization failed at Bank
      [cardnum] => XXXXXXXXXXXX2003
      [cardhash] => This field is no longer supported in postback params.
  )
  ```

  <br />
</Accordion>

## Step 4: Verify the Payment

<Verify_Payment_Tabs />

## Handling Guest Checkout Transactions

Guest Checkout is a valuable feature that can provided be enabled for your e-commerce websites. It allows your customers to make purchases without the need to sign in or create a user account. This streamlined process benefits one-time or occasional shoppers, as it eliminates the registration step, leading to faster transactions and enhanced customer satisfaction.

<Callout icon="📘" theme="info">
  **Enable Guest Checkout**: To enable this feature, contact your PayU Key Account Manager or PayU Integration Support.
</Callout>

As per RBI compliances, acquirers are also not allowed to store card details after a stipulated timeline. As per recommendations from RBI end, Guest checkout transactions won’t be allowed post 31st Oct. 2023. Guest checkout PAN should be replaced with some alternative number for transaction processing. As per the new regulations on guest checkout, where we have to tokenise plain card numbers. This token is called Alternative ID or Alt ID.

There are three scenarios with Alternative ID:

<Image align="center" width="900px" src="https://files.readme.io/f84108124634526cf547dac1d59ff3272600f8cfd26f486baba8425033ddf5c8-Guest-checkout-alt-id-implementation-methods.png" />

<Accordion title="Scenario 1: Provision & processes guest transaction with PayU" icon="fa-code">
  No changes required in the **\_payment** request used to collect payments.
</Accordion>

<Accordion title="Scenario 2: Provision Alt ID outside PayU and use PayU to Process Transaction" icon="fa-code">
  #### Request parameters

  Along with the parameters listed in the <Anchor label="Collect Payment API - Cards (Merchant Hosted Checkout)" target="_blank" href="https://docs.payu.in/reference/_payment_merchant_hosted_cards">Collect Payment API - Cards (Merchant Hosted Checkout)</Anchor>, you have to pass alt ID as a variable and pass TAVV (Cryptogram), last four digits and **par** parameter as part of **additional\_info** JSON. There is no change in the response and it remains the same.

  <Callout icon="📘" theme="info">
    **Note**: The **par** parameter is optional as part of **additional\_info** JSON.
  </Callout>

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
                                                                                                                      <td>JP***g</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>txnid <code>mandatory</code></td>
                                                                                                                      <td><code>String</code> The transaction ID is a reference number for a specific</br> order that is generated by the merchant.</td>
                                                                                                                      <td>ashdfu72634</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>amount <code>mandatory</code></td>
                                                                                                                      <td><code>String</code> The payment amount for the transaction.</td>
                                                                                                                      <td></td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>productinfo <code>mandatory</code></td>
                                                                                                                      <td><code>String</code> A brief description of the product.</td>
                                                                                                                      <td></td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>firstname <code>mandatory</code></td>
                                                                                                                      <td><code>String</code> The first name of the customer.</td>
                                                                                                                      <td>Ashish</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>email <code>mandatory</code></td>
                                                                                                                      <td><code>String</code> The email address of the customer.</td>
                                                                                                                      <td></td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>phone <code>mandatory</code></td>
                                                                                                                      <td><code>String</code> The phone number of the customer.</td>
                                                                                                                      <td></td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>pg <code>mandatory</code></td>
                                                                                                                      <td><code>String</code> The pg parameter determines which payment tabs will</br> be displayed on the PayU page. For cards, 'CC' will be the value.</td>
                                                                                                                      <td>CC</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>bankcode <code>mandatory</code></td>
                                                                                                                      <td><code>String</code> Each payment option is identified with a unique bank code</br> at PayU. The merchant must post this parameter with the corresponding payment option's</br> bank code value in it. For more information, refer to Card Type Codes and Supported Banks for Cards.</td>
                                                                                                                      <td>AMEX</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>ccname <code>mandatory</code></td>
                                                                                                                      <td><code>String</code> This parameter must contain the name on card – as entered by the customer for the transaction.</td>
                                                                                                                      <td>Ashish Kumar</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>ccvv <code>mandatory</code></td>
                                                                                                                      <td><code>String</code> Use 3-digit CVV number for credit/debit cards and 4-digit security code (4DBC/CID) for AMEX cards. Validate with BIN API.</td>
                                                                                                                      <td>123</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>ccexpmon <code>mandatory</code></td>
                                                                                                                      <td><code>String</code> This parameter must contain the card's expiry month or Alt ID expiry month for guest checkout – as entered by the user for the transaction. It must always be in 2 digits or in MM format. For months 1-9, this parameter must be appended with 0 – like 01, 02…09. For months 10-12, this parameter must not be appended – It should be 10,11 and 12 respectively. For VISA cards,</br> Plain card's expiry month need to be posted this parameter.</td>
                                                                                                                      <td>10</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>ccexpyr <code>mandatory</code></td>
                                                                                                                      <td><code>String</code> This parameter must contain the card's expiry</br> year or Alt ID expiry year for guest checkout – as entered by the</br> customer for the transaction. It must be of four digits. For VISA cards,</br> Plain card's expiry year need to be posted this parameter.</td>
                                                                                                                      <td>2021</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>alt_id <code>mandatory</code></td>
                                                                                                                      <td><code>String</code> This parameter must contain Alt ID for the guest checkout.</td>
                                                                                                                      <td></td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>furl <code>mandatory</code></td>
                                                                                                                      <td><code>String</code> The success URL, which is the page PayU will redirect to if the transaction is successful.</td>
                                                                                                                      <td></td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>surl <code>mandatory</code></td>
                                                                                                                      <td><code>String</code> The Failure URL, which is the page PayU will redirect to if the transaction is failed.</td>
                                                                                                                      <td></td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>hash <code>mandatory</code></td>
                                                                                                                      <td><code>String</code> It is the hash calculated by the merchant.</br> The hash calculation logic is: </br><code>sha512(key|txnid|amount|productinfo|firstname|</br>email|udf1|udf2|udf3|udf4|udf5||||||SALT)</code></td>
                                                                                                                      <td></td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>additional_info <code>mandatory</code></td>
                                                                                                                      <td><code>JSON</code> The fields which are included in this JSON.</br> For more information, refer to <a href="#additional_info-json-sample-and-field-description">additional_info JSON sample and field description</a>></td>
                                                                                                                      <td></td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>address1 <code>optional</code></td>
                                                                                                                      <td><code>String</code> The first line of the billing address.</br> For Fraud Detection: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.</td>
                                                                                                                      <td></td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>address2 <code>optional</code></td>
                                                                                                                      <td><code>String</code> The second line of the billing address.</td>
                                                                                                                      <td></td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>city <code>optional</code></td>
                                                                                                                      <td><code>String</code> The city where your customer resides as part of the billing address.</td>
                                                                                                                      <td></td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>state <code>optional</code></td>
                                                                                                                      <td><code>String</code> The state where your customer resides as part of the billing address.</td>
                                                                                                                      <td></td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>country <code>optional</code></td>
                                                                                                                      <td><code>String</code> The country where your customer resides.</td>
                                                                                                                      <td></td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>zipcode <code>optional</code></td>
                                                                                                                      <td><code>String</code> Billing address zip code is mandatory for the cardless EMI option. Character Limit-20</td>
                                                                                                                      <td></td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>udf1 <code>optional</code></td>
                                                                                                                      <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.</td>
                                                                                                                      <td></td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>udf2 <code>optional</code></td>
                                                                                                                      <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.</td>
                                                                                                                      <td></td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>udf3 <code>optional</code></td>
                                                                                                                      <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td>
                                                                                                                      <td></td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>udf4 <code>optional</code></td>
                                                                                                                      <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td>
                                                                                                                      <td></td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>udf5 <code>optional</code></td>
                                                                                                                      <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td>
                                                                                                                      <td></td>
                                                                                                                    </tr>
                                                                                                                  </tbody>
                                                                                                                </table>
  `}</HTMLBlock>

  <Callout icon="📘" theme="info">
    **Note**: **tokenReferenceid** field is required in the additional\_info parameter if you are provisioning Alt ID outside PayU for Diners card.
  </Callout>

  #### additional\_info JSON sample and field description

  ```
  {  
  "tavv":"AKF/FaM3BPWoAAEWYTiQAAADFA==",  
  "last4Digits":"2346",  
  "par":"799F3ED865F5965CC760A32682BA8A80F19E99ECB3F7F03574C14F5B6C3EB2C1",  
  "tokenReferenceId":"3acdd709-3c4b-4280-a6db-3f02271d09a3"  
  }
  ```

  The description of the fields in the additional\_info JSON.

  | Field            | Description                                                                                                                                                                   |
  | :--------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | trid             | trid is the acronym for Token Requestor ID and it is the identity given by the networks for creating the tokens. You should be able to get the same from your token provider. |
  | tokenReferenceID | The Token Reference ID is generated along with the network token. You should be able to get the same from your token provider.                                                |
  | TAVV             | It is a token authentication verification value given by schemes or interchange. Also, known as cryptogram.                                                                   |

  #### Sample Request

  ```curl
  curl --location 'http://local.secure.payu.in/_payment' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=smsplus' \
  --data-urlencode 'firstname={{firstname}}' \
  --data-urlencode 'email={{email}}' \
  --data-urlencode 'amount={{amount}}' \
  --data-urlencode 'phone=9999999999' \
  --data-urlencode 'productinfo={{productinfo}}' \
  --data-urlencode 'surl=your own success url'  \
  --data-urlencode 'furl=your own failure url'  \
  --data-urlencode 'pg=CC' \
  --data-urlencode 'bankcode=MASTERCARD' \
  --data-urlencode 'alt_id=5123456789012346' \
  --data-urlencode 'additional_info={"tavv":"AKF/FaM3BPWoAAEWYTiQAAADFA==","last4Digits":"2346","par":"799F3ED865F5965CC760A32682BA8A80F19E99ECB3F7F03574C14F5B6C3EB2C1","tokenReferenceId":"3acdd709-3c4b-4280-a6db-3f02271d09a3"}' \
  --data-urlencode 'ccname=Flipkart' \
  --data-urlencode 'ccvv=126' \
  --data-urlencode 'ccexpmon=05' \
  --data-urlencode 'ccexpyr=2024' \
  --data-urlencode 'txnid={{txnid}}' \
  --data-urlencode 'hash={{hash}}' \
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-code">
  > 📘 Notes:
  >
  > The **authRefNo** response parameter contains:
  >
  > * <Glossary>AEVV</Glossary> number for an AMEX card transaction. This is mandatory for AMEX for compliance for token (<Glossary>CoFT</Glossary>) provisioning.
  > * rupayAuthRefId for a Rupay card transaction
  >
  > To enable the  **authRefNo** response parameter in response, contact your PayU Key Account Manager or [PayU Support](https://help.payu.in).

  ```json
  Array
  (
      [mihpayid] => 20869277619
      [mode] => CC
      [status] => failure
      [unmappedstatus] => failed
      [key] => L43t1c
      [txnid] => 26ba7cd6a67b0a010542
      [amount] => 1.00
      [cardCategory] => domestic
      [discount] => 0.00
      [net_amount_debit] => 0.00
      [addedon] => 2024-09-05 17:46:10
      [productinfo] => Product Info
      [firstname] => Payu-Admin
      [lastname] => 
      [address1] => 
      [address2] => 
      [city] => 
      [state] => 
      [country] => 
      [zipcode] => 
      [email] => test@example.com
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
      [hash] => ac7720e4bc33e5494bec6d37302e522171175a987f9d47286bfd29e8a7fc794f56433fcacf0bc120db781c4dc1d05a4857d71e83f00f6ed6aa9c97a1938b9467
      [field1] => 
      [field2] => 
      [field3] => 
      [field4] => 
      [field5] => 05
      [field6] => 
      [field7] => AUTHNEGATIVE
      [field8] => 
      [field9] => Authorization failed at Bank
      [payment_source] => payu
      [pa_name] => PayU
      [PG_TYPE] => CC-PG
      [bank_ref_num] => 2409052690
      [bankcode] => AMEX
      [error] => E1903
      [error_Message] => Authorization failed at Bank
      [cardnum] => XXXXXXXXXXXX2003
      [cardhash] => This field is no longer supported in postback params.
      [authRefNo] => AAAXXXlxAAICQkXXXEAEAAXXXX=
      [corporate_card] => 0
      [cobranded_card] => AMEX_CONSUMER
      [splitInfo] => {"splitStatus":"","splitSegments":[]}
  )
  ```

  <br />
</Accordion>

<Accordion title="Scenario 3: Provision Alt ID from PayU" icon="fa-code">
  The Provision Alt ID API is used to provision Alt ID from PayU, but process transaction outside PayU. For more information, refer to <Anchor label="Provision Alt ID API" target="_blank" href="https://docs.payu.in/reference/provision-alt-id-api">Provision Alt ID API</Anchor>.
</Accordion>

## Handling 3DS Secure 2.0 Transaction

PayU supports 3DS Secure 2.0 transaction with Merchant Hosted Checkout integration. This section provides the information relevant to 3DS Secure 2.0 transaction.

<Accordion title="Request Parameters for 3DS Secure 2.0 Transaction" icon="fa-code">
  You must include the `threeDS2RequestData` parameter along with the regular Collect Payment API for cards.

  <Callout icon="📘" theme="info">
    **Reference**: For the **Try It** experience, refer to  [Collect Payment API - Cards (Merchant Hosted Checkout)](/docs.payu.in/reference/_payment_merchant_hosted_cards),
  </Callout>

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
                                                                                                                      <td>key<br/><code>mandatory</code></td>
                                                                                                                      <td>Merchant key provided by PayU during onboarding. Data type: <code>string</code>.</td>
                                                                                                                      <td>JF****g</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>txnid<br/><code>mandatory</code></td>
                                                                                                                      <td>The transaction ID is a reference number for a specific order that is generated by the merchant. Data type: <code>string</code>.</td>
                                                                                                                      <td>jYhbOYH9o4</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>amount<br/><code>mandatory</code></td>
                                                                                                                      <td>The payment amount for the transaction. Data type: <code>string</code>.</td>
                                                                                                                      <td>10</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>productinfo<br/><code>mandatory</code></td>
                                                                                                                      <td>A brief description of the product. Data type: <code>string</code>.</td>
                                                                                                                      <td>Product_info</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>firstname<br/><code>mandatory</code></td>
                                                                                                                      <td>The first name of the customer. Data type: <code>string</code>.</td>
                                                                                                                      <td>Ashish</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>lastname<br/><code>optional</code></td>
                                                                                                                      <td>The last name of the customer. Data type: <code>string</code>.</td>
                                                                                                                      <td>Test</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>email<br/><code>mandatory</code></td>
                                                                                                                      <td>The email address of the customer. Data type: <code>string</code>.</td>
                                                                                                                      <td>test@example.com</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>phone<br/><code>mandatory</code></td>
                                                                                                                      <td>The phone number of the customer. Data type: <code>string</code>.</td>
                                                                                                                      <td>9876543210</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>pg<br/><code>mandatory</code></td>
                                                                                                                      <td>The pg parameter determines which payment tabs will be displayed on the PayU page. For cards, 'CC' will be the value. Data type: <code>string</code>.</td>
                                                                                                                      <td>CC</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>bankcode<br/><code>mandatory</code></td>
                                                                                                                      <td>Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. Data type: <code>string</code>.</td>
                                                                                                                      <td>CC</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>ccnum<br/><code>mandatory</code></td>
                                                                                                                      <td>Use 13-19 digit card number for credit/debit cards (15 digits for AMEX, 13-19 for Maestro) and validate with LUHN algorithm. Data type: <code>string</code>.</td>
                                                                                                                      <td>4012000000002004</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>ccname<br/><code>mandatory</code></td>
                                                                                                                      <td>This parameter must contain the name on card – as entered by the customer for the transaction. Data type: <code>string</code>.</td>
                                                                                                                      <td>Test User</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>ccvv<br/><code>mandatory</code></td>
                                                                                                                      <td>Use 3-digit CVV number for credit/debit cards and 4-digit security code (4DBC/CID) for AMEX cards. Validate with BIN API. Data type: <code>string</code>.</td>
                                                                                                                      <td>123</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>ccexpmon<br/><code>mandatory</code></td>
                                                                                                                      <td>This parameter must contain the card's expiry month – as entered by the user for the transaction. It must always be in 2 digits or in MM format. For months 1-9, this parameter must be appended with 0 – like 01, 02…09. For months 10-12, this parameter must not be appended – It should be 10,11 and 12 respectively. Data type: <code>string</code>.</td>
                                                                                                                      <td>06</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>ccexpyr<br/><code>mandatory</code></td>
                                                                                                                      <td>This parameter must contain the card's expiry year – as entered by the customer for the transaction. It must be of four digits. Data type: <code>string</code>.</td>
                                                                                                                      <td>2024</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>surl<br/><code>mandatory</code></td>
                                                                                                                      <td>The success URL, which is the page PayU will redirect to if the transaction is successful. Data type: <code>string</code>.</td>
                                                                                                                      <td>http://pp30admin.payu.in/</br>test_response</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>furl<br/><code>mandatory</code></td>
                                                                                                                      <td>The failure URL, which is the page PayU will redirect to if the transaction is failed. Data type: <code>string</code>.</td>
                                                                                                                      <td>http://pp30admin.payu.in/</br>test_response</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>hash<br/><code>mandatory</code></td>
                                                                                                                      <td>It is the hash calculated by the merchant. The hash calculation logic is: sha512(key|txnid|amount|productinfo|firstname|email</br>|udf1|udf2|udf3|udf4|udf5||||||SALT). Data type: <code>string</code>.</td>
                                                                                                                      <td>e5b286a9c8545038de9</br>d4e4ee4d8a2fd02</br>e821015aff7e0323</br>807ba174997d8643f9</br>aa174981385e3e4dfe60</br>b918650806ccb97b3e8e3</br>471e1985ecadefd0184</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>txn_s2s_flow<br/><code>optional</code></td>
                                                                                                                      <td>Server-to-server transaction flow parameter that indicates the type of transaction processing flow to be used. Data type: <code>string</code>.</td>
                                                                                                                      <td>4</td>
                                                                                                                    </tr>
                                                                                                                    <tr>
                                                                                                                      <td>threeDS2RequestData<br/><code>optional</code></td>
                                                                                                                      <td>JSON object containing 3DS2 authentication data including browser information, user agent, screen dimensions, timezone, and other parameters required for 3D Secure 2.0 authentication. Data type: <code>object</code>.</td>
                                                                                                                      <td>Refer to #threeds2requestdata-json-format</td>
                                                                                                                    </tr>
                                                                                                                  </tbody>
                                                                                                                </table>
  `}</HTMLBlock>

  #### threeDS2RequestData JSON format

  in the following JSON format for 3DS Secure 2.0 support for cards:

  ```json
   "browserInfo": {
          "userAgent": "Mozilla\/5.0 (X11 Linux x86_64) AppleWebKit\/537.36 (KHTML, like Gecko) HeadlessChrome\/93.0.4577.0 Safari\/537.36",
          "acceptHeader": "*\/*",
          "language": "en-US",
          "colorDepth": "24",
          "screenHeight": "600",
          "screenWidth": "800",
          "timeZone": "-300",
          "javaEnabled": true,
          "ip": "10.248.2.71"
      }
  ```

  #### 3DS Secure 2.0 browserDetails JSON Fields Description

  | **Field**    | **Description**                                                                             | **Example**      |
  | ------------ | ------------------------------------------------------------------------------------------- | ---------------- |
  | userAgent    | This field must include user agent of the device browser.                                   |                  |
  | acceptHeader | This field contains the format of the header.                                               | application/json |
  | language     | This field contains the language for the 3D Secure Challenge.                               | en-US            |
  | colorDepth   | This field contains the color depth of the screen.                                          | 24               |
  | screenHeight | This field contains the screen height of the device displaying the 3D Secure Challenge.     | 640              |
  | screenWidth  | This field contains the screen width of the device displaying the 3D Secure Challenge.      | 480              |
  | javaEnabled  | This field contains whether Java is enabled for the device. It can be any of the following: | true             |
  | timeZone     | This field contains the time zone code where the payment is accepted.                       | 273              |
  | ip           | This should include the IP address of the device from which the browser is accessed.        | 10.248.2.71      |
</Accordion>

<Accordion title="Sample cURL Request with 3DS Secure 2.0" icon="fa-code">
  The sample cURL request with 3DS Secure 2.0:

  ```curl
  curl --location 'https://test.payu.in/_payment' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'Cookie: PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e' \
  --data-urlencode 'key=JF****g' \
  --data-urlencode 'firstname=Ashish' \
  --data-urlencode 'email=test@example.com' \
  --data-urlencode 'amount=10' \
  --data-urlencode 'phone= 9876543210' \
  --data-urlencode 'productinfo=Product_info' \
  --data-urlencode 'surl=http://pp30admin.payu.in/test_response' \
  --data-urlencode 'furl=http://pp30admin.payu.in/test_response' \
  --data-urlencode 'pg=CC' \
  --data-urlencode 'bankcode=CC' \
  --data-urlencode 'lastname=Test' \
  --data-urlencode 'ccname=Test User' \
  --data-urlencode 'ccvv=123' \
  --data-urlencode 'ccexpmon=06' \
  --data-urlencode 'ccexpyr=2024' \
  --data-urlencode 'txnid=jYhbOYH9o4' \
  --data-urlencode 'hash=e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184' \
  --data-urlencode 'ccnum=4012000000002004' \
  --data-urlencode 'txn_s2s_flow=4' \
  --data-urlencode 'threeDS2RequestData={
      "browserInfo": {
          "userAgent": "Mozilla\/5.0 (X11 Linux x86_64) AppleWebKit\/537.36 (KHTML, like Gecko) HeadlessChrome\/93.0.4577.0 Safari\/537.36",
          "acceptHeader": "*\/*",
          "language": "en-US",
          "colorDepth": "24",
          "screenHeight": "600",
          "screenWidth": "800",
          "timeZone": "-300",
          "javaEnabled": true,
          "ip": "10.248.2.71"
      }
  }'
  ```
</Accordion>
