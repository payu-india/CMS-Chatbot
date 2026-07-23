---
title: SKU-Based Offer using Merchant Hosted Checkout
deprecated: false
hidden: false
metadata:
  title: SKU-Based Offer using Merchant Hosted Checkout - Offers Integration
  keywords:
    - Integrate an SKU-Based Offer with Merchant Hosted Checkout
    - Integrate Merchant Hosted Checkout with Cashback Offer
    - Integrate Cashback Offer with Seamless Integration
    - SKU-Based Offer with Seamless Integration
    - Integrating SKU-Based Offers with Merchant Hosted Checkout
    - Stock Keeping Units-based Offer Integration with Merchant Hosted Checkout
    - Stock Keeping Units-based Offer Integration with Seamless Integration
  robots: index
---
<br />

After you create a SKU-based offer on PayU Dashboard, you can start collecting payments for products with SKU-based offer.  For more information on creating a SKU-based offer, refer to [Create a SKU-Based Offer](doc:create-a-sku-based-offer).

<Callout icon="📘" theme="info">
  **Note**: For payment journey of instant discount offers using Merchant Hosted Checkout, refer to [Instant Discount or Cashback using Merchant Hosted Checkout](doc:instant-discount-or-cashback-offers-integration-using-merchant-hosted-checkout).
</Callout>

<Accordion title="Steps to integrate" icon="fa-code">
  1. [Fetch offers](#step-1-fetch-offers)
  2. [Validate offer](#step-2-validate-offer)
  3. [Payment request](#step-3-payment-request)
  4. [Check the response from PayU](#step-4-check-the-response-fro-payU)
</Accordion>

## Step 1: Fetch offers

<Accordion title="Additional request parameter skusDetail for SKU" icon="fa-code">
  In addition to the request parameters listed in the [Fetch Offers API](ref:fetch-offers-api) section, the **skusDetail** parameter is posted with the following fields are posted in an array:

  <Table>
    <thead>
      <tr>
        <th>
          Field
        </th>

        <th>
          Description
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          skuAmount
          `optional`
        </td>

        <td>
          `String` The price of one/ single unit of SKU is specified in this field.
        </td>
      </tr>

      <tr>
        <td>
          skuId
          `mandatory`
        </td>

        <td>
          `String` The product identifier to select offer is specified in this field.
        </td>
      </tr>

      <tr>
        <td>
          quantity

          `optional`
        </td>

        <td>
          `String` The quantity for the product is specified in this field.\*\*\*\*
        </td>
      </tr>

      <tr>
        <td>
          offerKeys
          `optional`
        </td>

        <td>
          `String` The offer keys to filter at SKU-level is specified in this field.
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>

<Accordion title="skusDetail parameter in sample request" icon="fa-code">
  The sample request posted will include the **skusDetail** parameter similar to the following:

  ```curl
  "skusDetail": [
      {
        "skuAmount": 600,
        "quantity": 3,
        "skuId": "123",
        "offerKeys": null
      }
  ```

  **Sample response**

  ```
  "skusDetail": [
      {
        "skuAmount": 600,
        "quantity": 3,
        "skuId": "123",
        "offerKeys": null
      }
  ```
</Accordion>

## Step 2: Validate Offer

<Accordion title="Additional request parameters" icon="fa-code">
  In addition to the request parameters listed in  [Validate Offer API](ref:validate-offer-api), the **skusDetail** parameter with **skus** in an JSON array is posted, where each **skus** contain the following fields are posted in an array:

  | Field     | Description                                                                                                      |
  | --------- | ---------------------------------------------------------------------------------------------------------------- |
  | autoApply | The flag to specify to automatically apply the offer.                                                            |
  | skuAmount | The price of one/ single unit of SKU is specified in this field.                                                 |
  | offerKeys | The offer keys to filter at SKU-level is specified in this field.                                                |
  | quantity  | The quantity for the product is specified in this field.                                                         |
  | skuId     | The product identifier to select offer is specified in this field. For more information on creating a SKU offer. |
</Accordion>

<Accordion title="skusDetail Object in request" icon="fa-code">
  ```json
    "skusDetail": {
      "skus": [
        {
        "autoApply": false,
          "skuAmount": 1000,
          "offerKeys": [
            "SummerSpecialOffer2021@q1Bh0jsogwqP"
          ],
          "quantity": 1,
          "skuId": "1"
        }
      ]
    }
  ```
</Accordion>

<Accordion title="skusDetail Object in response" icon="fa-code">
  ```json
          "skusDetail": {
              "skusDiscountDetail": {
                  "totalCashbackDiscount": null,
                  "totalInstantDiscount": 100,
                  "totalDiscountedAmount": 900
              },
              "skus": [
                  {
                      "skuId": "1",
                      "quantity": 1,
                      "name": "One Plus",
                      "skuAmount": 1000,
                      "isValid": true,
                      "autoApply": false,
                      "discountDetail": {
                          "offerKey": "SummerSpecialOffer2021@q1Bh0jsogwqP",
                          "offerType": "INSTANT",
                          "discount": 100,
                          "discountedAmount": 900,
                          "discountType": "PERCENTAGE"
                      },
           "offerDetail":{
           "offerId":10005,
           "offerKey":"SummerSpecialOffer2021@q1Bh0jsogwqP",
           "offerType":"INSTANT",
           "title":"SummerSpecialOffer",
           "description":"SummerSpecialOffer discount",
           "validFrom":"2021-07-01 17:02:11",
           "validTo":"2022-08-05 15:53:16",
           "tnc":"abc",
           "tncLink":"abcd",
           "discountType":"ABSOLUTE",
           "offerPercentage":null,
           "maxDiscountPerTxn":100.00,
           "minTxnAmount":10.00,
           "maxTxnAmount":25000.00,
           "status":"ACTIVE",
           "isNce":false,
           "disallowTransactionInvalidOffer": false,
           "isSkuOffer": true,
           "isSubventedOffer": true
        }
  ```
</Accordion>

## Step 3: Payment request

<Accordion title="Additional request parameters for SKU-Based offer" icon="fa-code">
  <Callout icon="📘" theme="info">
    **Reference**: For the checkout flow and list of request parameters required for the Offer integration, refer to [Instant Discount or Cashback using Merchant Hosted Checkout](doc:instant-discount-or-cashback-offers-integration-using-merchant-hosted-checkout).
  </Callout>

  #### cart_details JSON Object Fields Description

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
        amount
        `mandatory`
      </td>

      <td>
        `String` The amount for the SKU-based offer.
      </td>
    </tr>

    <tr>
      <td>
        items
        `mandatory`
      </td>

      <td>
        `String` The number of the items for the SKU-based offer.
      </td>
    </tr>

    <tr>
      <td>
        surcharges
        `conditional`
      </td>

      <td>
        `String` Total txn amount is now increased, but the cart_details.amount is lesser, to handle the difference, the additional amount added by the merchant should be passed in surcharges field
      </td>
    </tr>

    <tr>
      <td>
        pre_discount
        `conditional`
      </td>

      <td>
        `String` If there are any pre discount given by merchant on their checkout page. Total txn amount is now reduced, but the cart_details.amount is higher, to handle the difference, the discount given by the merchant should be passed in pre_discount field
      </td>
    </tr>

    <tr>
      <td>
        sku_details
        `mandatory`
      </td>

      <td>
        `JSON Object` The SKU details is specified in this parameter in a JSON format. Refer to[ sku_details JSON Object Field descriptions](#sku_details-json-object-field-descriptions) (next table).
      </td>
    </tr>

    <tr>
      <td>

      </td>
    </tr>
  </tbody>
</Table>

#### sku_details JSON Object Field descriptions

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        sku_id
        `mandatory`
      </td>

      <td>
        String_ This parameter contains the unique identifier for SKU.

        * _Note_*: The Product ID in the Excel file as described in the[Create a SKU-Based Offer](doc:create-a-sku-based-offer) section and the **skuId** request parameter used in the Merchant Hosted Checkout Integration for SKU-based offer have the same function, Hence, after you create Product IDs on Dashboard, use them as values for the skuId parameter.
      </td>
    </tr>

    <tr>
      <td>
        sku_name
        `mandatory`
      </td>

      <td>
        * String _ This parameter contains the SKU name.
      </td>
    </tr>

    <tr>
      <td>
        sku_details.quantity
        `mandatory`
      </td>

      <td>
        * String _ The parameter must contain the quantity of SKU added in cart.
      </td>
    </tr>

    <tr>
      <td>
        sku_details.amount_per_sku
        `mandatory`
      </td>

      <td>
        * String _ The parameter must contain the per SKU amount.
      </td>
    </tr>

    <tr>
      <td>
        sku_details.offer_key
        `optional`
      </td>

      <td>
        * String_ This parameter must contain the Offer Key(s) which can be used for this transaction. |
      </td>
    </tr>

    <tr>
      <td>
        sku_details.offer_auto_apply
        `optional`
      </td>

      <td>
        * String_This parameter contains the flag for when to enable auto application of best offer on this SKU.
      </td>
    </tr>
  </tbody>
</Table>

  > **Notes**:
  >
  > * The following order must be used for hashing:
  >   `key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|offer_key|offer_auto_apply|SALT`
  >   For more information on hash generation process, refer to [Hashing Request and Response](ref:generate-hash-merchant-hosted).
  > * If any of the keys is null/not configured, "|" character must be concatenated.
  > * The above hash logic is for \_payment API version 10 or later.
</Accordion>

<Accordion title="cart_details Object in sample request" icon="fa-code">
  ```json
  "cart_details": {
      "amount": 55000,
      "items": 2,
      "surcharges":"100",
      "pre_discount":"10"
      "sku_details": [
        {
          "sku_id": "smartphone234",
          "sku_name": "Smartphone",
          "amount_per_sku": "45000",
          "quantity": 1,
          "offer_key": null,
          "offer_auto_apply": true
        },
        {
          "sku_id": "smartwatch132",
          "sku_name": "Smartwatch",
          "amount_per_sku": "10000",
          "quantity": 1,
          "offer_key": [
            "flat500@2022"
          ],
          "offer_auto_apply": false
        }
      ]
    }
  ```
</Accordion>

<Accordion title="Sample Request with **cart_details** JSON object:" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g" \
  -d "txnid=ewP8oRopzdHEtC" \
  -d "amount=10.00" \
  -d "firstname=Ashish" \
  -d "email=test@gmail.com" \
  -d "phone=9876543210" \
  -d "productinfo=iPhone" \
  -d "pg=TESTPG" \
  -d "bankcode=TESTPGNB" \
  -d "surl=https://apiplayground-response.herokuapp.com/" \
  -d "furl=https://apiplayground-response.herokuapp.com/" \
  -d 'cart_details={
    "amount": 55000,
    "items": 2,
    "surcharges": 10,
    "pre_discount": 5,
    "sku_details": [
      {
        "sku_id": "smartphone234",
        "sku_name": "Smartphone",
        "amount_per_sku": "45000",
        "quantity": 1,
        "offer_key": null,
        "offer_auto_apply": true
      },
      {
        "sku_id": "smartwatch132",
        "sku_name": "Smartwatch",
        "amount_per_sku": "10000",
        "quantity": 1,
        "offer_key": ["flat500@2022"],
        "offer_auto_apply": false
      }
    ]
  }' \
  -d "hash=bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"

  ```
  ```javascript
  /**
   * PayU Card Payment with Cart Details using Fetch API
   * 
   * IMPORTANT: This should only be executed server-side (e.g., in Node.js), never in the browser,
   * as it contains sensitive payment information.
   */

  // Payment endpoint
  const url = 'https://test.payu.in/_payment';

  // Cart details object
  const cartDetails = {
    amount: 55000,
    items: 2,
    surcharges: 10,
    pre_discount: 5,
    sku_details: [
      {
        sku_id: "smartphone234",
        sku_name: "Smartphone",
        amount_per_sku: "45000",
        quantity: 1,
        offer_key: null,
        offer_auto_apply: true
      },
      {
        sku_id: "smartwatch132",
        sku_name: "Smartwatch",
        amount_per_sku: "10000",
        quantity: 1,
        offer_key: ["flat500@2022"],
        offer_auto_apply: false
      }
    ]
  };

  // Form data parameters
  const formData = new URLSearchParams();
  formData.append('key', 'JP***g');
  formData.append('txnid', 'ewP8oRopzdHEtC');
  formData.append('amount', '10.00');
  formData.append('firstname', 'Ashish');
  formData.append('email', 'test@gmail.com');
  formData.append('phone', '9876543210');
  formData.append('productinfo', 'iPhone');
  formData.append('pg', 'TESTPG');
  formData.append('bankcode', 'TESTPGNB');
  formData.append('surl', 'https://apiplayground-response.herokuapp.com/');
  formData.append('furl', 'https://apiplayground-response.herokuapp.com/');
  // Add cart details as JSON string
  formData.append('cart_details', JSON.stringify(cartDetails));
  formData.append('hash', 'bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319');

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
      // Process payment response here
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

  def process_card_payment_with_cart_details() -> Dict[str, Any]:
      """
      Process card payment with cart details using PayU's Merchant Hosted Checkout
      
      IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
      
      Returns:
          Dictionary with response from PayU API
      """
      # API endpoint
      url = "https://test.payu.in/_payment"
      
      # Cart details object
      cart_details = {
          "amount": 55000,
          "items": 2,
          "surcharges": 10,
          "pre_discount": 5,
          "sku_details": [
              {
                  "sku_id": "smartphone234",
                  "sku_name": "Smartphone",
                  "amount_per_sku": "45000",
                  "quantity": 1,
                  "offer_key": None,
                  "offer_auto_apply": True
              },
              {
                  "sku_id": "smartwatch132",
                  "sku_name": "Smartwatch",
                  "amount_per_sku": "10000",
                  "quantity": 1,
                  "offer_key": ["flat500@2022"],
                  "offer_auto_apply": False
              }
          ]
      }
      
      # Prepare the form data
      payload = {
          "key": "JP***g",
          "txnid": "ewP8oRopzdHEtC",
          "amount": "10.00",
          "firstname": "Ashish",
          "email": "test@gmail.com",
          "phone": "9876543210",
          "productinfo": "iPhone",
          "pg": "TESTPG",
          "bankcode": "TESTPGNB",
          "surl": "https://apiplayground-response.herokuapp.com/",
          "furl": "https://apiplayground-response.herokuapp.com/",
          # Add cart details as JSON string
          "cart_details": json.dumps(cart_details),
          "hash": "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"
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

  </Accordion>
  # Example usage
  if __name__ == "__main__":
  result = process_card_payment_with_cart_details()
  print(f"Status Code: {result['status_code']}")
  if 'error' in result:
     print(f"Error: {result['error']}")
  print(f"Response: {result['response']}")

  ```
  ```php
  <?php
  /**
   * Process card payment with cart details using PayU's Merchant Hosted Checkout
   * 
   * IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
   * 
   * @return array Response from PayU API
   */
  function processCardPaymentWithCartDetails() {
      // API endpoint
      $url = "https://test.payu.in/_payment";
      
      // Cart details object
      $cartDetails = [
          "amount" => 55000,
          "items" => 2,
          "surcharges" => 10,
          "pre_discount" => 5,
          "sku_details" => [
              [
                  "sku_id" => "smartphone234",
                  "sku_name" => "Smartphone",
                  "amount_per_sku" => "45000",
                  "quantity" => 1,
                  "offer_key" => null,
                  "offer_auto_apply" => true
              ],
              [
                  "sku_id" => "smartwatch132",
                  "sku_name" => "Smartwatch",
                  "amount_per_sku" => "10000",
                  "quantity" => 1,
                  "offer_key" => ["flat500@2022"],
                  "offer_auto_apply" => false
              ]
          ]
      ];
      
      // Prepare the form data
      $payload = [
          "key" => "JP***g",
          "txnid" => "ewP8oRopzdHEtC",
          "amount" => "10.00",
          "firstname" => "Ashish",
          "email" => "test@gmail.com",
          "phone" => "9876543210",
          "productinfo" => "iPhone",
          "pg" => "TESTPG",
          "bankcode" => "TESTPGNB",
          "surl" => "https://apiplayground-response.herokuapp.com/",
          "furl" => "https://apiplayground-response.herokuapp.com/",
          // Add cart details as JSON string
          "cart_details" => json_encode($cartDetails),
          "hash" => "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"
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
  $result = processCardPaymentWithCartDetails();
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

  // For JSON processing
  import javax.json.Json;
  import javax.json.JsonArray;
  import javax.json.JsonArrayBuilder;
  import javax.json.JsonObject;
  import javax.json.JsonObjectBuilder;

  /**
   * PayU Card Payment Processor with Cart Details for Merchant Hosted Checkout
   * 
   * IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
   */
  public class PayUCardPaymentProcessor {
      
      // API endpoint
      private static final String PAYU_TEST_URL = "https://test.payu.in/_payment";
      
      /**
       * Process card payment with cart details through PayU
       * @return PaymentResponse containing status and response data
       */
      public PaymentResponse processCardPaymentWithCartDetails() {
          try {
              // Initialize URL
              URL url = new URL(PAYU_TEST_URL);
              
              // Create cart details JSON
              JsonObjectBuilder cartDetailsBuilder = Json.createObjectBuilder()
                  .add("amount", 55000)
                  .add("items", 2)
                  .add("surcharges", 10)
                  .add("pre_discount", 5);
              
              // Create SKU details array
              JsonArrayBuilder skuDetailsBuilder = Json.createArrayBuilder();
              
              // First SKU item
              JsonObjectBuilder smartphone = Json.createObjectBuilder()
                  .add("sku_id", "smartphone234")
                  .add("sku_name", "Smartphone")
                  .add("amount_per_sku", "45000")
                  .add("quantity", 1)
                  .addNull("offer_key")
                  .add("offer_auto_apply", true);
              
              // Second SKU item
              JsonArrayBuilder offerKeys = Json.createArrayBuilder().add("flat500@2022");
              JsonObjectBuilder smartwatch = Json.createObjectBuilder()
                  .add("sku_id", "smartwatch132")
                  .add("sku_name", "Smartwatch")
                  .add("amount_per_sku", "10000")
                  .add("quantity", 1)
                  .add("offer_key", offerKeys)
                  .add("offer_auto_apply", false);
              
              // Add items to the SKU details array
              skuDetailsBuilder.add(smartphone);
              skuDetailsBuilder.add(smartwatch);
              
              // Finalize cart details JSON
              JsonObject cartDetails = cartDetailsBuilder
                  .add("sku_details", skuDetailsBuilder)
                  .build();
              
              // Prepare form parameters
              Map<String, String> params = new HashMap<>();
              params.put("key", "JP***g");
              params.put("txnid", "ewP8oRopzdHEtC");
              params.put("amount", "10.00");
              params.put("firstname", "Ashish");
              params.put("email", "test@gmail.com");
              params.put("phone", "9876543210");
              params.put("productinfo", "iPhone");
              params.put("pg", "TESTPG");
              params.put("bankcode", "TESTPGNB");
              params.put("surl", "https://apiplayground-response.herokuapp.com/");
              params.put("furl", "https://apiplayground-response.herokuapp.com/");
              // Add cart details as JSON string
              params.put("cart_details", cartDetails.toString());
              params.put("hash", "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319");
              
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
          PayUCardPaymentProcessor processor = new PayUCardPaymentProcessor();
          PaymentResponse result = processor.processCardPaymentWithCartDetails();
          
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
  using System.Text.Json;

  namespace PayUCardIntegration
  {
      /// <summary>
      /// PayU Card Payment Processor with Cart Details for Merchant Hosted Checkout
      /// 
      /// IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
      /// </summary>
      public class PayUCardPaymentProcessor
      {
          // API endpoint
          private const string PayuTestUrl = "https://test.payu.in/_payment";
          
          /// <summary>
          /// Process card payment with cart details through PayU
          /// </summary>
          /// <returns>PaymentResponse containing status and response data</returns>
          public async Task<PaymentResponse> ProcessCardPaymentWithCartDetailsAsync()
          {
              try
              {
                  // Create cart details object
                  var cartDetails = new
                  {
                      amount = 55000,
                      items = 2,
                      surcharges = 10,
                      pre_discount = 5,
                      sku_details = new[]
                      {
                          new {
                              sku_id = "smartphone234",
                              sku_name = "Smartphone",
                              amount_per_sku = "45000",
                              quantity = 1,
                              offer_key = (string)null,
                              offer_auto_apply = true
                          },
                          new {
                              sku_id = "smartwatch132",
                              sku_name = "Smartwatch",
                              amount_per_sku = "10000",
                              quantity = 1,
                              offer_key = new[] { "flat500@2022" },
                              offer_auto_apply = false
                          }
                      }
                  };
                  
                  // Serialize cart details to JSON
                  string cartDetailsJson = JsonSerializer.Serialize(cartDetails);
                  
                  // Prepare form parameters
                  var formData = new Dictionary<string, string>
                  {
                      { "key", "JP***g" },
                      { "txnid", "ewP8oRopzdHEtC" },
                      { "amount", "10.00" },
                      { "firstname", "Ashish" },
                      { "email", "test@gmail.com" },
                      { "phone", "9876543210" },
                      { "productinfo", "iPhone" },
                      { "pg", "TESTPG" },
                      { "bankcode", "TESTPGNB" },
                      { "surl", "https://apiplayground-response.herokuapp.com/" },
                      { "furl", "https://apiplayground-response.herokuapp.com/" },
                      // Add cart details as JSON string
                      { "cart_details", cartDetailsJson },
                      { "hash", "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319" }
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
              var processor = new PayUCardPaymentProcessor();
              var result = await processor.ProcessCardPaymentWithCartDetailsAsync();
              
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

  <br />

  ## Step 4: Check the response from PayU

  You need to look for the skusDetail object in the response. For the complete response, refer to [Merchant Hosted Checkout](doc:custom-checkout-merchant-hosted).

  <Accordion title="Success scenario" icon="fa-code">
    The skusDetail JSON in the following sample response:

    ```
    {"cart_details": {
        "id": "18",
        "payu_id": "999000000000983",
        "total_items": "2",
        "total_cart_amount": "55000",
        "offer_applied": null,
        "offer_availed": null,
        "instant_discount": "1000",
        "cashback_discount": "500",
        "total_discount": "1500",
        "net_cart_amount": "54000",
        "created_at": null,
        "updated_at": null,
        "sku_details": [
          {
            "id": "35",
            "cart_id": "18",
            "payu_id": "999000000000983",
            "mid": "180012",
            "sku_id": "smartphone234",
            "sku_name": "Smartphone",
            "amount_per_sku": "45000.00",
            "quantity": "1",
            "amount_before_discount": "45000",
            "discount": "1000",
            "amount_after_discount": "44000",
            "offer_key": null,
            "offer_status": null,
            "offer_type": null,
            "created_at": null,
            "updated_at": null
          },
          {
            "id": "36",
            "cart_id": "18",
            "payu_id": "999000000000983",
            "mid": "180012",
            "sku_id": "smartwatch132",
            "sku_name": "Smartwatch",
            "amount_per_sku": "10000.00",
            "quantity": "1",
            "amount_before_discount": "10000.00",
            "discount": "500",
            "amount_after_discount": "10000.00",
            "offer_key": null,
            "offer_status": null,
            "offer_type": null,
            "created_at": null,
            "updated_at": null
          }
        ]
      }}
    ```
  </Accordion>

  ## Step 5: Verify the payment

  <p>Upon receiving the response, we recommend performing a reconciliation step to validate all transaction details.\
  You can verify your payments using either of the following methods:</p>

  <br />

  <Tabs>
    <Tab title="1. Verify using Webhooks">
      Configure the webhooks to monitor the status of payments.\
      Webhooks enable a server to communicate with another server by sending an HTTP callback or message.\
      These callbacks are triggered by specific events or instances and operate at the server-to-server (S2S) level.

      👉 For more details, refer to [Webhooks for Payments](https://docs.payu.in/reference/webhooks). <br />
    </Tab>

    <Tab title="2. Verify using Verify Payments API">
      **Environment**

      |                        |                                                                                                              |
      | :--------------------- | :----------------------------------------------------------------------------------------------------------- |
      | Test Environment       | [https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2) |
      | Production Environment | [https://info.payu.in/merchant/postservice.php?form=2](https://info.payu.in/merchant/postservice.php?form=2) |

      > Note: The hash logic for Verify Payment API is:
      > `sha512(key|command|var1|salt)
      > sha512`

      <Accordion title="Sample request" icon="fa-code">
        **Sample Request with cart\_details JSON object**

        ```curl
        curl -X POST "https://test.payu.in/_payment" \
        -H "accept: application/json" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -d "key=JP***g" \
        -d "txnid=ewP8oRopzdHEtC" \
        -d "amount=10.00" \
        -d "firstname=Ashish" \
        -d "email=test@gmail.com" \
        -d "phone=9876543210" \
        -d "productinfo=iPhone" \
        -d "pg=TESTPG" \
        -d "bankcode=TESTPGNB" \
        -d "surl=https://apiplayground-response.herokuapp.com/" \
        -d "furl=https://apiplayground-response.herokuapp.com/" \
        -d 'cart_details={
          "amount": 55000,
          "items": 2,
          "surcharges": 10,
          "pre_discount": 5,
          "sku_details": [
            {
              "sku_id": "smartphone234",
              "sku_name": "Smartphone",
              "amount_per_sku": "45000",
              "quantity": 1,
              "offer_key": null,
              "offer_auto_apply": true
            },
            {
              "sku_id": "smartwatch132",
              "sku_name": "Smartwatch",
              "amount_per_sku": "10000",
              "quantity": 1,
              "offer_key": ["flat500@2022"],
              "offer_auto_apply": false
            }
          ]
        }' \
        -d "hash=bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"

        ```
        ```javascript
        /**
         * PayU Card Payment with Cart Details using Fetch API
         * 
         * IMPORTANT: This should only be executed server-side (e.g., in Node.js), never in the browser,
         * as it contains sensitive payment information.
         */

        // Payment endpoint
        const url = 'https://test.payu.in/_payment';

        // Cart details object
        const cartDetails = {
          amount: 55000,
          items: 2,
          surcharges: 10,
          pre_discount: 5,
          sku_details: [
            {
              sku_id: "smartphone234",
              sku_name: "Smartphone",
              amount_per_sku: "45000",
              quantity: 1,
              offer_key: null,
              offer_auto_apply: true
            },
            {
              sku_id: "smartwatch132",
              sku_name: "Smartwatch",
              amount_per_sku: "10000",
              quantity: 1,
              offer_key: ["flat500@2022"],
              offer_auto_apply: false
            }
          ]
        };

        // Form data parameters
        const formData = new URLSearchParams();
        formData.append('key', 'JP***g');
        formData.append('txnid', 'ewP8oRopzdHEtC');
        formData.append('amount', '10.00');
        formData.append('firstname', 'Ashish');
        formData.append('email', 'test@gmail.com');
        formData.append('phone', '9876543210');
        formData.append('productinfo', 'iPhone');
        formData.append('pg', 'TESTPG');
        formData.append('bankcode', 'TESTPGNB');
        formData.append('surl', 'https://apiplayground-response.herokuapp.com/');
        formData.append('furl', 'https://apiplayground-response.herokuapp.com/');
        // Add cart details as JSON string
        formData.append('cart_details', JSON.stringify(cartDetails));
        formData.append('hash', 'bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319');

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
            // Process payment response here
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

        def process_card_payment_with_cart_details() -> Dict[str, Any]:
            """
            Process card payment with cart details using PayU's Merchant Hosted Checkout
            
            IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
            
            Returns:
                Dictionary with response from PayU API
            """
            # API endpoint
            url = "https://test.payu.in/_payment"
            
            # Cart details object
            cart_details = {
                "amount": 55000,
                "items": 2,
                "surcharges": 10,
                "pre_discount": 5,
                "sku_details": [
                    {
                        "sku_id": "smartphone234",
                        "sku_name": "Smartphone",
                        "amount_per_sku": "45000",
                        "quantity": 1,
                        "offer_key": None,
                        "offer_auto_apply": True
                    },
                    {
                        "sku_id": "smartwatch132",
                        "sku_name": "Smartwatch",
                        "amount_per_sku": "10000",
                        "quantity": 1,
                        "offer_key": ["flat500@2022"],
                        "offer_auto_apply": False
                    }
                ]
            }
            
            # Prepare the form data
            payload = {
                "key": "JP***g",
                "txnid": "ewP8oRopzdHEtC",
                "amount": "10.00",
                "firstname": "Ashish",
                "email": "test@gmail.com",
                "phone": "9876543210",
                "productinfo": "iPhone",
                "pg": "TESTPG",
                "bankcode": "TESTPGNB",
                "surl": "https://apiplayground-response.herokuapp.com/",
                "furl": "https://apiplayground-response.herokuapp.com/",
                # Add cart details as JSON string
                "cart_details": json.dumps(cart_details),
                "hash": "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"
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
            result = process_card_payment_with_cart_details()
            print(f"Status Code: {result['status_code']}")
            if 'error' in result:
                print(f"Error: {result['error']}")
            print(f"Response: {result['response']}")

        ```
        ```php
        <?php
        /**
         * Process card payment with cart details using PayU's Merchant Hosted Checkout
         * 
         * IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
         * 
         * @return array Response from PayU API
         */
        function processCardPaymentWithCartDetails() {
            // API endpoint
            $url = "https://test.payu.in/_payment";
            
            // Cart details object
            $cartDetails = [
                "amount" => 55000,
                "items" => 2,
                "surcharges" => 10,
                "pre_discount" => 5,
                "sku_details" => [
                    [
                        "sku_id" => "smartphone234",
                        "sku_name" => "Smartphone",
                        "amount_per_sku" => "45000",
                        "quantity" => 1,
                        "offer_key" => null,
                        "offer_auto_apply" => true
                    ],
                    [
                        "sku_id" => "smartwatch132",
                        "sku_name" => "Smartwatch",
                        "amount_per_sku" => "10000",
                        "quantity" => 1,
                        "offer_key" => ["flat500@2022"],
                        "offer_auto_apply" => false
                    ]
                ]
            ];
            
            // Prepare the form data
            $payload = [
                "key" => "JP***g",
                "txnid" => "ewP8oRopzdHEtC",
                "amount" => "10.00",
                "firstname" => "Ashish",
                "email" => "test@gmail.com",
                "phone" => "9876543210",
                "productinfo" => "iPhone",
                "pg" => "TESTPG",
                "bankcode" => "TESTPGNB",
                "surl" => "https://apiplayground-response.herokuapp.com/",
                "furl" => "https://apiplayground-response.herokuapp.com/",
                // Add cart details as JSON string
                "cart_details" => json_encode($cartDetails),
                "hash" => "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"
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
        $result = processCardPaymentWithCartDetails();
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

        // For JSON processing
        import javax.json.Json;
        import javax.json.JsonArray;
        import javax.json.JsonArrayBuilder;
        import javax.json.JsonObject;
        import javax.json.JsonObjectBuilder;

        /**
         * PayU Card Payment Processor with Cart Details for Merchant Hosted Checkout
         * 
         * IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
         */
        public class PayUCardPaymentProcessor {
            
            // API endpoint
            private static final String PAYU_TEST_URL = "https://test.payu.in/_payment";
            
            /**
             * Process card payment with cart details through PayU
             * @return PaymentResponse containing status and response data
             */
            public PaymentResponse processCardPaymentWithCartDetails() {
                try {
                    // Initialize URL
                    URL url = new URL(PAYU_TEST_URL);
                    
                    // Create cart details JSON
                    JsonObjectBuilder cartDetailsBuilder = Json.createObjectBuilder()
                        .add("amount", 55000)
                        .add("items", 2)
                        .add("surcharges", 10)
                        .add("pre_discount", 5);
                    
                    // Create SKU details array
                    JsonArrayBuilder skuDetailsBuilder = Json.createArrayBuilder();
                    
                    // First SKU item
                    JsonObjectBuilder smartphone = Json.createObjectBuilder()
                        .add("sku_id", "smartphone234")
                        .add("sku_name", "Smartphone")
                        .add("amount_per_sku", "45000")
                        .add("quantity", 1)
                        .addNull("offer_key")
                        .add("offer_auto_apply", true);
                    
                    // Second SKU item
                    JsonArrayBuilder offerKeys = Json.createArrayBuilder().add("flat500@2022");
                    JsonObjectBuilder smartwatch = Json.createObjectBuilder()
                        .add("sku_id", "smartwatch132")
                        .add("sku_name", "Smartwatch")
                        .add("amount_per_sku", "10000")
                        .add("quantity", 1)
                        .add("offer_key", offerKeys)
                        .add("offer_auto_apply", false);
                    
                    // Add items to the SKU details array
                    skuDetailsBuilder.add(smartphone);
                    skuDetailsBuilder.add(smartwatch);
                    
                    // Finalize cart details JSON
                    JsonObject cartDetails = cartDetailsBuilder
                        .add("sku_details", skuDetailsBuilder)
                        .build();
                    
                    // Prepare form parameters
                    Map<String, String> params = new HashMap<>();
                    params.put("key", "JP***g");
                    params.put("txnid", "ewP8oRopzdHEtC");
                    params.put("amount", "10.00");
                    params.put("firstname", "Ashish");
                    params.put("email", "test@gmail.com");
                    params.put("phone", "9876543210");
                    params.put("productinfo", "iPhone");
                    params.put("pg", "TESTPG");
                    params.put("bankcode", "TESTPGNB");
                    params.put("surl", "https://apiplayground-response.herokuapp.com/");
                    params.put("furl", "https://apiplayground-response.herokuapp.com/");
                    // Add cart details as JSON string
                    params.put("cart_details", cartDetails.toString());
                    params.put("hash", "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319");
                    
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
                PayUCardPaymentProcessor processor = new PayUCardPaymentProcessor();
                PaymentResponse result = processor.processCardPaymentWithCartDetails();
                
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
        using System.Text.Json;

        namespace PayUCardIntegration
        {
            /// <summary>
            /// PayU Card Payment Processor with Cart Details for Merchant Hosted Checkout
            /// 
            /// IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
            /// </summary>
            public class PayUCardPaymentProcessor
            {
                // API endpoint
                private const string PayuTestUrl = "https://test.payu.in/_payment";
                
                /// <summary>
                /// Process card payment with cart details through PayU
                /// </summary>
                /// <returns>PaymentResponse containing status and response data</returns>
                public async Task<PaymentResponse> ProcessCardPaymentWithCartDetailsAsync()
                {
                    try
                    {
                        // Create cart details object
                        var cartDetails = new
                        {
                            amount = 55000,
                            items = 2,
                            surcharges = 10,
                            pre_discount = 5,
                            sku_details = new[]
                            {
                                new {
                                    sku_id = "smartphone234",
                                    sku_name = "Smartphone",
                                    amount_per_sku = "45000",
                                    quantity = 1,
                                    offer_key = (string)null,
                                    offer_auto_apply = true
                                },
                                new {
                                    sku_id = "smartwatch132",
                                    sku_name = "Smartwatch",
                                    amount_per_sku = "10000",
                                    quantity = 1,
                                    offer_key = new[] { "flat500@2022" },
                                    offer_auto_apply = false
                                }
                            }
                        };
                        
                        // Serialize cart details to JSON
                        string cartDetailsJson = JsonSerializer.Serialize(cartDetails);
                        
                        // Prepare form parameters
                        var formData = new Dictionary<string, string>
                        {
                            { "key", "JP***g" },
                            { "txnid", "ewP8oRopzdHEtC" },
                            { "amount", "10.00" },
                            { "firstname", "Ashish" },
                            { "email", "test@gmail.com" },
                            { "phone", "9876543210" },
                            { "productinfo", "iPhone" },
                            { "pg", "TESTPG" },
                            { "bankcode", "TESTPGNB" },
                            { "surl", "https://apiplayground-response.herokuapp.com/" },
                            { "furl", "https://apiplayground-response.herokuapp.com/" },
                            // Add cart details as JSON string
                            { "cart_details", cartDetailsJson },
                            { "hash", "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319" }
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
                    var processor = new PayUCardPaymentProcessor();
                    var result = await processor.ProcessCardPaymentWithCartDetailsAsync();
                    
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

      <Accordion title="Response parameters" icon="fa-list">
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
                status
              </td>

              <td style={{ textAlign: "left" }}>
                This parameter returns the status of web service call. The status can be any of the following:

                * 0 - If web service call failed.
                * 1 - If web service call succeeded
              </td>

              <td style={{ textAlign: "left" }}>
                0
              </td>
            </tr>

            <tr>
              <td style={{ textAlign: "left" }}>
                msg
              </td>

              <td style={{ textAlign: "left" }}>
                This parameter returns the reason string.
              </td>

              <td style={{ textAlign: "left" }}>
                For example, any of the following messages are displayed:

                * Parameter missing
                * Token is empty
                * Amount is empty
                * Transaction not exists
              </td>
            </tr>

            <tr>
              <td style={{ textAlign: "left" }}>
                transaction\_details
              </td>

              <td style={{ textAlign: "left" }}>
                This parameter contains the response in a JSON format. For more information refer to [JSON fields description for transaction\_details parameter ](#json-field-description-for-transaction_details-parameter).
              </td>

              <td style={{ textAlign: "left" }} />
            </tr>

            <tr>
              <td style={{ textAlign: "left" }}>
                request\_id
              </td>

              <td style={{ textAlign: "left" }}>
                PayU Request ID for a request in a Transaction. For example, a transaction can have a refund request.
              </td>

              <td style={{ textAlign: "left" }}>
                7800456
              </td>
            </tr>

            <tr>
              <td style={{ textAlign: "left" }}>
                bank\_ref\_num
              </td>

              <td style={{ textAlign: "left" }}>
                This parameter returns the bank reference number. If the bank provides after a successful action.
              </td>

              <td style={{ textAlign: "left" }}>
                204519474956
              </td>
            </tr>
          </tbody>
        </Table>

        To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes).
      </Accordion>
    </Tab>
  </Tabs>
</Accordion>
