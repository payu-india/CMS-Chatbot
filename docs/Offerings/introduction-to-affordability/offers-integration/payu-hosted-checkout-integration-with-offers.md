---
title: Integrate with PayU Hosted Checkout
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Integrate with PayU Hosted Checkout for Offers
  description: ''
  keywords:
    - Integrate an Offer with PayU Hosted Checkout
    - Integrate an PayU Hosted Checkout with Offer
    - Integrate an Offer with Non-Seamless Integration
    - Offer with Non-Seamless Integration
  robots: index
next:
  description: ''
---
With the PayU Hosted Checkout integration, the entire payment experience is controlled by PayU. The following sections describe how to use the PayU Hosted Integration to collect payments with various types of offers:

- [Instant Discount or Cashback Offer](#instant-discount-or-cashback-offer)
- [SKU-Based Offer](#sku-based-offer)

<Callout icon="👍" theme="okay">
  ###

  Experience the end-to-end **Instant Discount/Cashback or SKU-Based Offer** flow and instantly generate the complete code for seamless, zero-coding integration into your website.

    

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

                <button onclick="window.open('https://payu.in/integrationlab/bankoffer', '_blank')" 
                        class="tooltip-btn" 
                        data-tooltip="Automatically generate code including hashing for your eCommerce website to integrate Offers - PayU Hosted Checkout with zero coding knowledge.">
                     Experience the flow and get the code
                </button>
  `}</HTMLBlock>
</Callout>

<br />

<Accordion title="General customer journey" icon="fa-route">
  1. Customer clicks **Pay** on your mobile application or website.
  2. Customer is redirected to the PayU Hosted Checkout page.

     The PayU Hosted Checkout page on Desktop is similar to the following screenshot. In case offer keys have been passed by the merchant, the same would be filtered and displayed to the customer.
  3. Customer is shown the applicable offers on the checkout page for that transaction.
  4. Customer will have an option to apply the offer. If the offer is applicable on a specific payment option, the customer will be redirected to the specific payment option.

  The PayU Hosted Checkout page for specify payment option on Mobile.

  5. Alternatively, the customer can choose the payment option. If only an offer is applicable for that payment option, the offer will be automatically applied.
  6. For Instant Discount, the amount is reduced after the offer is applied, whereas, in the case of cashback, the amount will not be reduced after the offer is applied.
  7. Customer completes the 2FA payment on the adjusted amount.
  8. Customer is redirected back to the merchant mobile application or website.
</Accordion>

## Instant Discount or Cashback

With the PayU Hosted Checkout integration, the entire payment experience is controlled by PayU. This section describes how to use the PayU Hosted Integration to collect payments with offers.

<Accordion title="Customer journey on PayU Hosted Checkout" icon="fa-credit-card">
  1. Customer clicks **Pay** on your mobile application or website.
  2. Customer is redirected to the PayU Hosted Checkout page.

     The PayU Hosted Checkout page on Desktop is similar to the following screenshot. In case offer keys have been passed by the merchant, the same would be filtered and displayed to the customer.

  The PayU Hosted Checkout page on Mobile

  3. Customer is shown the applicable offers on the checkout page for that transaction.
  4. Customer will have the option to apply the offer. If the offer is applicable to a specific payment option, the customer will be redirected to the specific payment option.

  <img align="center" src="https://files.readme.io/725ae934c0f2c2d875989729a29e2c38c7d8f6984b68f03bc0044f09562c37d0-instant_discount_offer_integration.png" width="300" alt="Instant Discount based offer sample" />

  The PayU Hosted Checkout page for specific payment option on Mobile is similar to the following screenshot:

  5. Alternatively, the customer can choose the payment option. If only an offer is applicable for that payment option, the offer will be automatically applied.
  6. For Instant Discount, the amount is reduced after the offer is applied, whereas, in the case of cashback, the amount will not be reduced after the offer is applied.
  7. Customer completes the 2FA payment on the adjusted amount.
  8. Customer is redirected back to the merchant's mobile application or website.
</Accordion>

### Integration steps

To integrate offers using PayU Hosted Checkout integration:

<Callout icon="📘" theme="info">
  ###

  **Reference**: For the PayU Hosted Checkout flow, refer to [PayU Hosted Checkout](doc:prebuilt-checkout-payu-hosted).
</Callout>

1. Make the payment request to PayU:

   You need to send an additional parameter (**user token)**, **api\_version** as 14, and hash as described in the following table. This user token would be used to identify the customer for applying velocity rules.

<Accordion title="Request parameters" icon="fa-database">
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
          api\_version
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          The API version of the \_payment API must be specified as **14**.
        </td>

        <td style={{ textAlign: "left" }}>
          14
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          user\_token
          `mandatory for UPI, NB, Wallet`
        </td>

        <td style={{ textAlign: "left" }}>
          The use for this param is to allow the offer engine to apply velocity rules at a user level.

          * **Card Based Offers (CC, DC, EMI)**: In case of card payment mode offers, if this parameter is passed the velocity rules would be applied on this token, if not passed the same would be applied on the card number.
          * **UPI, NB, Wallet**: It is mandatory for UPI, NB, and Wallet payment modes. If not passed the validation rules would not apply.
        </td>

        <td style={{ textAlign: "left" }}></td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          hash
          for UPI, NB, Wallet
        </td>

        <td style={{ textAlign: "left" }}>
          It is used to avoid the possibility of transaction tampering.

          * *Note*\*: The following order must be used for hashing:
            `key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|offer_key|offer_auto_apply|SALT`
            For more information on hash generation process, refer to [Generate Hash](doc:generate-hash-payu-hosted) .
        </td>

        <td style={{ textAlign: "left" }}></td>
      </tr>
    </tbody>
  </Table>
</Accordion>

<Accordion title="Sample request" icon="fa-server">
  ```curl
  curl --location 'https://test.payu.in/_payment' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'Cookie: PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e' \
  --data-urlencode 'key=JF****g' \
  --data-urlencode 'txnid=jYhbOYH9o4' \
  --data-urlencode 'amount=10' \
  --data-urlencode 'productinfo=Product_info' \
  --data-urlencode 'firstname=Ashish' \
  --data-urlencode 'lastname=Test' \
  --data-urlencode 'email=test@example.com' \
  --data-urlencode 'phone=9876543210' \
  --data-urlencode 'furl=http://pp30admin.payu.in/test_response' \
  --data-urlencode 'surl=http://pp30admin.payu.in/test_response' \
  --data-urlencode 'hash=e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184' \
  --data-urlencode 'api_version=14' \
  --data-urlencode 'user_token=8789'

  ```
  ```javascript
  // Using Fetch API with URLSearchParams
  const url = "https://test.payu.in/_payment";

  // Define form data
  const formData = new URLSearchParams({
      'key': 'JF****g',
      'txnid': 'jYhbOYH9o4',
      'amount': '10',
      'productinfo': 'Product_info',
      'firstname': 'Ashish',
      'lastname': 'Test',
      'email': 'test@example.com',
      'phone': '9876543210',
      'furl': 'http://pp30admin.payu.in/test_response',
      'surl': 'http://pp30admin.payu.in/test_response',
      'hash': 'e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184',
      'api_version': '14',
      'user_token': '8789'
  });

  // Make the request
  fetch(url, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'Cookie': 'PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e'
      },
      body: formData
  })
  .then(response => {
      console.log('Status:', response.status);
      return response.text();
  })
  .then(data => {
      console.log('Response:', data);
  })
  .catch(error => {
      console.error('Error:', error);
  });

  ```
  ```python
  import requests

  # Define the URL
  url = "https://test.payu.in/_payment"

  # Define headers
  headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': 'PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e'
  }

  # Define form data
  data = {
      'key': 'JF****g',
      'txnid': 'jYhbOYH9o4',
      'amount': '10',
      'productinfo': 'Product_info',
      'firstname': 'Ashish',
      'lastname': 'Test',
      'email': 'test@example.com',
      'phone': '9876543210',
      'furl': 'http://pp30admin.payu.in/test_response',
      'surl': 'http://pp30admin.payu.in/test_response',
      'hash': 'e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184',
      'api_version': '14',
      'user_token': '8789'
  }

  # Make the request
  try:
      response = requests.post(url, headers=headers, data=data)
      print("Status Code:", response.status_code)
      print("Response:", response.text)
  except requests.exceptions.RequestException as e:
      print("Error:", e)

  ```
  ```java
  import java.io.*;
  import java.net.HttpURLConnection;
  import java.net.URL;
  import java.net.URLEncoder;
  import java.nio.charset.StandardCharsets;
  import java.util.HashMap;
  import java.util.Map;
  import java.util.StringJoiner;

  public class PayUSimpleRequest {
      public static void main(String[] args) throws IOException {
          String url = "https://test.payu.in/_payment";

          // Prepare form data
          Map<String, String> parameters = new HashMap<>();
          parameters.put("key", "JF****g");
          parameters.put("txnid", "jYhbOYH9o4");
          parameters.put("amount", "10");
          parameters.put("productinfo", "Product_info");
          parameters.put("firstname", "Ashish");
          parameters.put("lastname", "Test");
          parameters.put("email", "test@example.com");
          parameters.put("phone", "9876543210");
          parameters.put("furl", "http://pp30admin.payu.in/test_response");
          parameters.put("surl", "http://pp30admin.payu.in/test_response");
          parameters.put("hash", "e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184");
          parameters.put("api_version", "14");
          parameters.put("user_token", "8789");

          // Build URL-encoded string
          StringJoiner sj = new StringJoiner("&");
          for (Map.Entry<String, String> entry : parameters.entrySet()) {
              sj.add(URLEncoder.encode(entry.getKey(), StandardCharsets.UTF_8) + "=" +
                     URLEncoder.encode(entry.getValue(), StandardCharsets.UTF_8));
          }
          byte[] postData = sj.toString().getBytes(StandardCharsets.UTF_8);

          // Create connection
          URL obj = new URL(url);
          HttpURLConnection connection = (HttpURLConnection) obj.openConnection();
          
          // Set request method and headers
          connection.setRequestMethod("POST");
          connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
          connection.setRequestProperty("Cookie", "PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e");
          connection.setRequestProperty("Content-Length", String.valueOf(postData.length));
          connection.setDoOutput(true);

          // Send request
          try (DataOutputStream wr = new DataOutputStream(connection.getOutputStream())) {
              wr.write(postData);
          }

          // Read response
          int responseCode = connection.getResponseCode();
          
          InputStream inputStream = responseCode >= 200 && responseCode < 300 
              ? connection.getInputStream() 
              : connection.getErrorStream();
              
          BufferedReader in = new BufferedReader(new InputStreamReader(inputStream));
          String inputLine;
          StringBuilder response = new StringBuilder();

          while ((inputLine = in.readLine()) != null) {
              response.append(inputLine).append("\n");
          }
          in.close();

          System.out.println("Response Code: " + responseCode);
          System.out.println("Response: " + response.toString());
      }
  }

  ```
  ```php
  <?php
  // Define the URL
  $url = "https://test.payu.in/_payment";

  // Prepare form data
  $postData = array(
      'key' => 'JF****g',
      'txnid' => 'jYhbOYH9o4',
      'amount' => '10',
      'productinfo' => 'Product_info',
      'firstname' => 'Ashish',
      'lastname' => 'Test',
      'email' => 'test@example.com',
      'phone' => '9876543210',
      'furl' => 'http://pp30admin.payu.in/test_response',
      'surl' => 'http://pp30admin.payu.in/test_response',
      'hash' => 'e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184',
      'api_version' => '14',
      'user_token' => '8789'
  );

  // Initialize cURL
  $ch = curl_init();

  // Set cURL options
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postData));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
  curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      'Content-Type: application/x-www-form-urlencoded',
      'Cookie: PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e'
  ));

  // Execute request
  $response = curl_exec($ch);
  $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

  // Check for errors
  if (curl_errno($ch)) {
      echo 'cURL error: ' . curl_error($ch) . "\n";
  } else {
      echo "HTTP Code: " . $httpCode . "\n";
      echo "Response: " . $response . "\n";
  }

  // Close cURL
  curl_close($ch);
  ?>

  ```
  ```csharp
  using System;
  using System.Collections.Generic;
  using System.Net.Http;
  using System.Threading.Tasks;

  class Program
  {
      static async Task Main(string[] args)
      {
          var client = new HttpClient();
          var url = "https://test.payu.in/_payment";

          // Prepare form data
          var formData = new List<KeyValuePair<string, string>>
          {
              new KeyValuePair<string, string>("key", "JF****g"),
              new KeyValuePair<string, string>("txnid", "jYhbOYH9o4"),
              new KeyValuePair<string, string>("amount", "10"),
              new KeyValuePair<string, string>("productinfo", "Product_info"),
              new KeyValuePair<string, string>("firstname", "Ashish"),
              new KeyValuePair<string, string>("lastname", "Test"),
              new KeyValuePair<string, string>("email", "test@example.com"),
              new KeyValuePair<string, string>("phone", "9876543210"),
              new KeyValuePair<string, string>("furl", "http://pp30admin.payu.in/test_response"),
              new KeyValuePair<string, string>("surl", "http://pp30admin.payu.in/test_response"),
              new KeyValuePair<string, string>("hash", "e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184"),
              new KeyValuePair<string, string>("api_version", "14"),
              new KeyValuePair<string, string>("user_token", "8789")
          };

          var formContent = new FormUrlEncodedContent(formData);

          // Set headers
          client.DefaultRequestHeaders.Add("Cookie", "PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e");

          try
          {
              var response = await client.PostAsync(url, formContent);
              var responseContent = await response.Content.ReadAsStringAsync();
              
              Console.WriteLine($"Status Code: {response.StatusCode}");
              Console.WriteLine($"Response: {responseContent}");
          }
          catch (Exception ex)
          {
              Console.WriteLine($"Error: {ex.Message}");
          }
          finally
          {
              client.Dispose();
          }
      }
  }

  ```

  <br />
</Accordion>

2. Check the response from PayU.

   You need to understand the following parameters to handle the payment response as the net amount debit may be different from the amount sent by you in the request.

<Accordion title="Response parameters" icon="fa-database">
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

          * instant
          * cashback
        </td>

        <td style={{ textAlign: "left" }}>
          instant
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>

3. Verify the payment.

   Similar to the payment response, the same parameters can be handled as part of the **verify\_payment** API. For more information, refer to [Verify Payment API](ref:verify_payment_api),

<Accordion title="Response parameters from verify_payment API" icon="fa-database">
  The following response parameters are partial list which are relevant for SKU-based offers.

  | **Parameter**       | **Description**                                                                                                                                                                                  | **Example** |
  | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
  | transaction\_amount | This parameter contains the total transaction amount before discount.                                                                                                                            | 50000.00    |
  | net\_amount\_debit  | This parameter contains the actual amount deducted from the customer’s payment instrument. In case of Instant discount this amount would be lesser than the amount passed by you in the request. | 47500.00    |
  | discount            | This parameter contains the offer value provided to the user. This value will specify the offer amount for both Instant discount and Cashback offers.                                            | 2500.00     |

  For the sample request and response from PayU, refer to [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout).
</Accordion>

4. If you want to refund the payment to customer. refer to [Refund APIs](ref:refund-apis).

PayU would refund the exact amount passed by you in the Refund request. For more information, refer to [Refunds for Offers](doc:refunds-for-offers). 

<Callout icon="📘" theme="info">
  ###

  **Note**: You can enable the **Enforce Offer** flag by requesting your PayU Key Account Manager. If you enable the **Enforce Offer** flag, all the offers passed are visible to the customer and the customer chooses an offer that they wish to apply.
</Callout>

## SKU-Based offer

After you create an SKU-based offer on PayU Dashboard, you can start collecting payments for products with an SKU-based offer.

This section describes the customer workflow with an SKU-based offer on the PayU Payment page when redirected from your website for payment and request parameters for the **\_payment** API to collect payments with an SKU-Based Offer.

<Callout icon="📘" theme="info">
  ###

  **Note**: For payment journey of instant discount offers using Redirection Flow or PayU Hosted Checkout, refer to [Integrate with PayU Hosted Checkout](doc:payu-hosted-checkout-integration-with-offers).
</Callout>

### Customer journey

<Accordion title="Customer journey" icon="fa-times-circle">
  After your customer selects the items from your website (for example, mobile online shopping), the customer is redirected to the PayU page for payment and involves the following steps:

  1. Select **Offers** at the top-right corner.

  All the offers for the products in the shopping cart (if any) are listed.

  <img align="center" src="https://files.readme.io/b1984bec41045b6b8368526afddf38613f865973af4b191c67db448533ff3447-sku_based_offer_sample_step1a.png" width="300" alt="SKU based offer journey step 1" />

  2. Select the **Product Offers** tab.

     The **Product Offers** tab is displayed on the *Offer & Discount* page.

  <img align="center" src="https://files.readme.io/125790b4a8e0c940e5d749db3da58b0fba2a8221162a8743bd79c36e737db3f7-sku_based_offer_sample_step2.png" width="300" alt="SKU based offer journey Offers tab" />

  3. Apply an offer using the **Use Offer** button for the offer you wish to apply.

     The *Offer Applied!* pop-up page is displayed.

  <img align="center" src="https://files.readme.io/0b8210a58d2e248f80943709b73cb961eb1f19a9b28b56e4af59d241b881375b-sku_based_offer_sample_step3.png" width="300" alt="SKU based offer journey Offers Applied page" />

  4. Click **Thanks.**

     The page to collect your credit card details is displayed.

  <img align="center" src="https://files.readme.io/2d8c8c5c9f3e505055d787f8a22ce3d43ed3c8335d43ca7da44a95c330a3e328-sku_based_offer_sample_step4.png" width="300" alt="SKU based offer journey Offers Card Payment page" />

  5. Click **Proceed** to make payment and then enter the OTP sent by bank to your mobile to complete the purchase.
  6. Close this page to return back to the merchant website.
</Accordion>

### Integration steps

#### Step 1: Post request parameters

<Accordion title="Request parameters" icon="fa-database">
  **Additional request parameters for SKU-Based Offer**

  The following request parameters are posted along with request parameters posted for a PayU Hosted Checkout transaction. For the checkout flow and list of request parameters required for the Offer integration, refer to  [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout).

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
          cart\_details
          `mandatory for SKU`
        </td>

        <td>
          `JSON Object `The card details is specified in this parameter in a JSON format.
          **Note**: If given null, no cart will be created for the transaction.
        </td>
      </tr>

      <tr>
        <td>
          cart\_details.amount
          `mandatory`
        </td>

        <td>
          `String` The amount for the SKU-based offer.
        </td>
      </tr>

      <tr>
        <td>
          cart\_details.surcharges
          `conditional`
        </td>

        <td>
          `String` Total txn amount is now increased, but the cart\_details.amount is lesser, to handle the difference, the additional amount added by the merchant should be passed in surcharges field
        </td>
      </tr>

      <tr>
        <td>
          cart\_details.pre\_discount
          `conditional`
        </td>

        <td>
          * String\_ If there are any pre discount given by merchant on their checkout page. Total txn amount is now reduced, but the cart\_details.amount is higher, to handle the difference, the discount given by the merchant should be passed in pre\_discount field
        </td>
      </tr>

      <tr>
        <td>
          cart\_details.items
          `mandatory`
        </td>

        <td>
          * String\_ The number of the items for the SKU-based offer.
        </td>
      </tr>

      <tr>
        <td>
          cart\_details.sku\_details
          `mandatory`
        </td>

        <td>
          * JSON Object\_ The SKU details is specified in this parameter in a JSON format.
        </td>
      </tr>

      <tr>
        <td>
          cart\_details.sku\_details.sku\_id
          `mandatory`
        </td>

        <td>
          * String\_ This parameter contains the unique identifier for SKU.
          * *Note*\*: The Product ID in the Excel file as described in the[Create a SKU-Based Offer](doc:create-a-sku-based-offer) section and the **skuId** request parameter used in the Merchant Hosted Checkout Integration for SKU-based offer have the same function, Hence, after you create Product IDs on Dashboard, use them as values for the skuId parameter.
        </td>
      </tr>

      <tr>
        <td>
          sku\_details.sku\_name
          `mandatory`
        </td>

        <td>
          `String`  This parameter contains the SKU name.
        </td>
      </tr>

      <tr>
        <td>
          sku\_details.quantity
          `mandatory`
        </td>

        <td>
          `String`  The parameter must contain the quantity of SKU added in cart.
        </td>
      </tr>

      <tr>
        <td>
          sku\_details.amount\_per\_sku
          `mandatory`
        </td>

        <td>
          `String`  The parameter must contain the per SKU amount.
        </td>
      </tr>

      <tr>
        <td>
          sku\_details.offer\_key
          `mandatory`
        </td>

        <td>
          `String` This parameter must contain the Offer Key(s) which can be used for this transaction. |
        </td>
      </tr>

      <tr>
        <td>
          sku\_details.offer\_auto\_apply
          `mandatory`
        </td>

        <td>
          `String` This parameter contains the flag for when to enable auto application of best offer on this SKU.
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>

<Accordion title="Sample request" icon="fa-server">
  ```curl
  curl --location 'https://test.payu.in/_payment' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'Cookie: PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e' \
  --data-urlencode 'key=JF****g' \
  --data-urlencode 'txnid=jYhbOYH9o4' \
  --data-urlencode 'amount=10' \
  --data-urlencode 'productinfo=Product_info' \
  --data-urlencode 'firstname=Ashish' \
  --data-urlencode 'lastname=Test' \
  --data-urlencode 'email=test@example.com' \
  --data-urlencode 'phone=9876543210' \
  --data-urlencode 'furl=http://pp30admin.payu.in/test_response' \
  --data-urlencode 'surl=http://pp30admin.payu.in/test_response' \
  --data-urlencode 'api_version=19' \
  --data-urlencode 'hash=e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184' \
  --data-urlencode 'cart_details={
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
  }'
  ```
  ```javascript
  async function makePayURequest() {
      const url = "https://test.payu.in/_payment";

```
  // Define cart details object
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

  // Define form data
  const formData = new URLSearchParams({
      'key': 'JF****g',
      'txnid': 'jYhbOYH9o4',
      'amount': '10',
      'productinfo': 'Product_info',
      'firstname': 'Ashish',
      'lastname': 'Test',
      'email': 'test@example.com',
      'phone': '9876543210',
      'furl': 'http://pp30admin.payu.in/test_response',
      'surl': 'http://pp30admin.payu.in/test_response',
      'api_version': '19',
      'hash': 'e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184',
      'cart_details': JSON.stringify(cartDetails)
  });

  try {
      console.log('Making request to:', url);
      console.log('Cart details:', cartDetails);
      
      const response = await fetch(url, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/x-www-form-urlencoded',
              'Cookie': 'PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e'
          },
          body: formData
      });

      console.log('Response status:', response.status);
      console.log('Response headers:', response.headers);

      // Check if response is successful
      if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}, statusText: ${response.statusText}`);
      }

      const data = await response.text();
      console.log('Success! Response data:', data);
      
      return {
          success: true,
          status: response.status,
          data: data
      };

  } catch (error) {
      console.error('Request failed:', error);
      
      return {
          success: false,
          error: error.message
      };
  }
```

}

// Call the function
makePayURequest()
.then(result => {
uccess) {
log('Payment request completed successfully');

log('Payment request failed:', result.error);

);

````
```python
import requests
import json

# Define the URL
url = "https://test.payu.in/_payment"

# Define headers
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e'
}

# Define the cart details as a dictionary first, then convert to JSON string
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

# Define form data
data = {
    'key': 'JF****g',
    'txnid': 'jYhbOYH9o4',
    'amount': '10',
    'productinfo': 'Product_info',
    'firstname': 'Ashish',
    'lastname': 'Test',
    'email': 'test@example.com',
    'phone': '9876543210',
    'furl': 'http://pp30admin.payu.in/test_response',
    'surl': 'http://pp30admin.payu.in/test_response',
    'api_version': '19',
    'hash': 'e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184',
    'cart_details': json.dumps(cart_details)
}

# Make the request
response = requests.post(url, headers=headers, data=data)
print("Status Code:", response.status_code)
print("Response:", response.text)

````
```php
<?php
// For Laravel or similar frameworks
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Log;

class PayUService 
{
    private $apiUrl;
    private $timeout;

    public function __construct() 
    {
        $this->apiUrl = config('payu.api_url', 'https://test.payu.in/_payment');
        $this->timeout = config('payu.timeout', 30);
    }

    public function processPayment(array $paymentData, array $cartDetails): array 
    {
        try {
            // Add cart details as JSON
            $formData = array_merge($paymentData, [
                'cart_details' => json_encode($cartDetails, JSON_UNESCAPED_SLASHES)
            ]);

            Log::info('PayU Payment Request', [
                'txnid' => $paymentData['txnid'] ?? 'N/A',
                'amount' => $paymentData['amount'] ?? 'N/A'
            ]);

            // Make HTTP request using Laravel's HTTP client
            $response = Http::timeout($this->timeout)
                ->withHeaders([
                    'Content-Type' => 'application/x-www-form-urlencoded',
                    'Cookie' => 'PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e'
                ])
                ->asForm()
                ->post($this->apiUrl, $formData);

            Log::info('PayU Payment Response', [
                'status' => $response->status(),
                'txnid' => $paymentData['txnid'] ?? 'N/A'
            ]);

            if ($response->successful()) {
                return [
                    'success' => true,
                    'status_code' => $response->status(),
                    'response' => $response->body(),
                    'transaction_id' => $paymentData['txnid'] ?? null
                ];
            } else {
                throw new \Exception("HTTP Error: " . $response->status());
            }

        } catch (\Exception $e) {
            Log::error('PayU Payment Failed', [
                'error' => $e->getMessage(),
                'txnid' => $paymentData['txnid'] ?? 'N/A'
            ]);

            return [
                'success' => false,
                'error' => $e->getMessage(),
                'transaction_id' => $paymentData['txnid'] ?? null
            ];
        }
    }
}

// Usage in Laravel Controller
class PaymentController extends Controller 
{
    protected $payuService;

    public function __construct(PayUService $payuService) 
    {
        $this->payuService = $payuService;
    }

    public function processPayment(Request $request) 
    {
        $paymentData = [
            'key' => 'JF****g',
            'txnid' => 'jYhbOYH9o4',
            'amount' => '10',
            'productinfo' => 'Product_info',
            'firstname' => 'Ashish',
            'lastname' => 'Test',
            'email' => 'test@example.com',
            'phone' => '9876543210',
            'furl' => 'http://pp30admin.payu.in/test_response',
            'surl' => 'http://pp30admin.payu.in/test_response',
            'api_version' => '19',
            'hash' => 'e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184'
        ];

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

        $result = $this->payuService->processPayment($paymentData, $cartDetails);

        return response()->json($result);
    }
}
?>

```
```java
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;
import java.util.StringJoiner;

public class PayURequest {
    public static void main(String[] args) throws IOException {
        String url = "https://test.payu.in/_payment";
        
        // Cart details JSON string
        String cartDetails = "{\n" +
            "  \"amount\": 55000,\n" +
            "  \"items\": 2,\n" +
            "  \"surcharges\": 10,\n" +
            "  \"pre_discount\": 5,\n" +
            "  \"sku_details\": [\n" +
            "    {\n" +
            "      \"sku_id\": \"smartphone234\",\n" +
            "      \"sku_name\": \"Smartphone\",\n" +
            "      \"amount_per_sku\": \"45000\",\n" +
            "      \"quantity\": 1,\n" +
            "      \"offer_key\": null,\n" +
            "      \"offer_auto_apply\": true\n" +
            "    },\n" +
            "    {\n" +
            "      \"sku_id\": \"smartwatch132\",\n" +
            "      \"sku_name\": \"Smartwatch\",\n" +
            "      \"amount_per_sku\": \"10000\",\n" +
            "      \"quantity\": 1,\n" +
            "      \"offer_key\": [\"flat500@2022\"],\n" +
            "      \"offer_auto_apply\": false\n" +
            "    }\n" +
            "  ]\n" +
            "}";

        // Prepare form data
        Map<String, String> parameters = new HashMap<>();
        parameters.put("key", "JF****g");
        parameters.put("txnid", "jYhbOYH9o4");
        parameters.put("amount", "10");
        parameters.put("productinfo", "Product_info");
        parameters.put("firstname", "Ashish");
        parameters.put("lastname", "Test");
        parameters.put("email", "test@example.com");
        parameters.put("phone", "9876543210");
        parameters.put("furl", "http://pp30admin.payu.in/test_response");
        parameters.put("surl", "http://pp30admin.payu.in/test_response");
        parameters.put("api_version", "19");
        parameters.put("hash", "e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184");
        parameters.put("cart_details", cartDetails);

        // Build URL-encoded string
        StringJoiner sj = new StringJoiner("&");
        for (Map.Entry<String, String> entry : parameters.entrySet()) {
            sj.add(URLEncoder.encode(entry.getKey(), StandardCharsets.UTF_8) + "=" +
                   URLEncoder.encode(entry.getValue(), StandardCharsets.UTF_8));
        }
        byte[] postData = sj.toString().getBytes(StandardCharsets.UTF_8);

        // Create connection
        URL obj = new URL(url);
        HttpURLConnection connection = (HttpURLConnection) obj.openConnection();
        
        // Set request method and headers
        connection.setRequestMethod("POST");
        connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
        connection.setRequestProperty("Cookie", "PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e");
        connection.setRequestProperty("Content-Length", String.valueOf(postData.length));
        connection.setDoOutput(true);

        // Send request
        try (DataOutputStream wr = new DataOutputStream(connection.getOutputStream())) {
            wr.write(postData);
        }

        // Read response
        int responseCode = connection.getResponseCode();
        BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
        String inputLine;
        StringBuilder response = new StringBuilder();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        System.out.println("Response Code: " + responseCode);
        System.out.println("Response: " + response.toString());
    }
}

```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

class Program
{
    static async Task Main(string[] args)
    {
        var client = new HttpClient();
        var url = "https://test.payu.in/_payment";

        // Define cart details
        var cartDetails = new
        {
            amount = 55000,
            items = 2,
            surcharges = 10,
            pre_discount = 5,
            sku_details = new[]
            {
                new
                {
                    sku_id = "smartphone234",
                    sku_name = "Smartphone",
                    amount_per_sku = "45000",
                    quantity = 1,
                    offer_key = (string)null,
                    offer_auto_apply = true
                },
                new
                {
                    sku_id = "smartwatch132",
                    sku_name = "Smartwatch",
                    amount_per_sku = "10000",
                    quantity = 1,
                    offer_key = new[] { "flat500@2022" },
                    offer_auto_apply = false
                }
            }
        };

        // Prepare form data
        var formData = new List<KeyValuePair<string, string>>
        {
            new KeyValuePair<string, string>("key", "JF****g"),
            new KeyValuePair<string, string>("txnid", "jYhbOYH9o4"),
            new KeyValuePair<string, string>("amount", "10"),
            new KeyValuePair<string, string>("productinfo", "Product_info"),
            new KeyValuePair<string, string>("firstname", "Ashish"),
            new KeyValuePair<string, string>("lastname", "Test"),
            new KeyValuePair<string, string>("email", "test@example.com"),
            new KeyValuePair<string, string>("phone", "9876543210"),
            new KeyValuePair<string, string>("furl", "http://pp30admin.payu.in/test_response"),
            new KeyValuePair<string, string>("surl", "http://pp30admin.payu.in/test_response"),
            new KeyValuePair<string, string>("api_version", "19"),
            new KeyValuePair<string, string>("hash", "e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184"),
            new KeyValuePair<string, string>("cart_details", JsonConvert.SerializeObject(cartDetails))
        };

        var formContent = new FormUrlEncodedContent(formData);

        // Set headers
        client.DefaultRequestHeaders.Add("Cookie", "PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e");

        try
        {
            var response = await client.PostAsync(url, formContent);
            var responseContent = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response: {responseContent}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}

```

<br />

#### cart\_details object in sample request

```json
"cart_details": {
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
        "offer_key": [
          "flat500@2022"
        ],
        "offer_auto_apply": false
      }
    ]
  }
```

</Accordion>

#### Step 2: Check the PayU response

<Accordion title="Sample response" icon="fa-terminal">
  **Success scenario**

  The **cart\_details** JSON Object in the response (sample):

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

  **Failure scenarios**

  For a list of error messages for the failure scenarios, refer to [Error Codes for Offers Integration](doc:error-codes-for-offers-integration).
</Accordion>

#### Step 3: Verify Payment

Verify the payment using the **Verify Payment** API. For more information, For API reference, refer to <Anchor target="_blank" href="ref:verify_payment_api">Verify Payment API</Anchor>.
