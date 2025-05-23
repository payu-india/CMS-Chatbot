---
title: Merchant Hosted Checkout
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Custom Checkout Integration
  description: >-
    Learn how to process credit/debit card, UPI, EMI or any other payments on
    your website using PayU's Merchant Hosted Checkout API. This approach
    eliminates redirection to PayU's payment page, enhancing transaction
    security and efficiency.
  keywords:
    - Merchant Hosted Checkout
    - ' Custom Hosted Checkout'
    - ' Merchant Hosted Checkout Prerequisites'
  robots: index
next:
  description: ''
---
This guide provides a comprehensive overview of integrating PayU’s Merchant Hosted Checkout solution for collecting payments on your website or application. This guide is designed for developers with varying levels of experience, from those new to payment gateways to seasoned API integrators.

## What is Merchant Hosted Checkout or Custom Checkout?

PayU’s Merchant Hosted Checkout allows you to create a custom payment experience on your website while leveraging PayU’s secure payment processing infrastructure. This approach gives you greater control over the look and feel of your checkout flow, while still benefiting from PayU’s robust security and compliance features. With merchant hosted checkout, you collect the payment details on your website and then securely transmit them to PayU for processing.

### Key Benefits

* **Customizable UI**: Design a checkout flow that seamlessly integrates with your brand. 
* **Direct Customer Relationship**: Maintain control over the customer experience from start to finish. 
* **Flexible Integration**: Integrate with a wide range of payment methods, including cards, net banking, wallets, UPI, and more.

> 👍 Note:
>
> Merchant Hosted Checkout is a specific PayU product with defined features. It’s distinct from simply hosting payment elements on your website. This guide specifically covers the PayU’s Merchant Hosted Checkout product and its associated APIs.

## Workflow and Experience

The following process diagram illustrates the Merchant Hosted Checkout workflow:

<Image align="center" className="border" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/08/Merchant_Hosted_Flow-2048x989.png" />

1. It operates through a form post-call directly from the customer’s browser, sending their payment data into the PayU’s systems.
2. A payment process initiated from your e-commerce website travels through PayU’s secured environment before reaching the card ACS or a bank’s Net Banking page.
3. After the transaction is completed in the bank’s website environment, the customer is redirected to your website.

### Customer Experience

**Step 1:** The customer completes shopping at your website and initiates a transaction with saved card (for example, VISA) credentials.

**Step 2:** The customer enters the CVV and proceeds to complete the payment.

<Image align="center" className="border" border={true} width="300px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/05/MicrosoftTeams-image-1.png" />

**Step 3:** After the credentials are entered, and the payment flow is launched, the user is navigated through a secured PayU environment that reflects the transaction ID.

**Step 4:** The flow takes the user to the login ACS page of the bank, where the user needs to complete the transaction by using the OTP sent by the bank to the registered mobile number.

<Image align="center" className="border" border={true} width="300px" src="https://files.readme.io/1764f1a919d1e2a65ea7af0227bbb1b649c85cfde4cdbc4b435be8e6fb722fd3-merchant_hosted_acs_page.png" />

**Step 5:** Customer is shown the status (failed/successful) on your website based on the transaction status from PayU.

## Prerequisites and Setup

Before you begin the integration process, ensure you have the following: 

* **PayU Merchant Account**: You need a valid PayU merchant account. If you don’t have one, register for a test account to start integrating and testing. Later, register for a production account. 
* **API Credentials (Key and Salt)**: Obtain your API key and salt from the PayU Dashboard. The key identifies your merchant account, and the salt is used to generate secure hashes for API requests and responses. 
* **Test Credentials**: Use your test key and salt during development and testing. These credentials allow you to simulate transactions without processing real payments. You can access the test Key or Salt as described in Generate Merchant Key and Salt on PayU Dashboard. 
* **Production Credentials**: Once your integration is complete, replace the test credentials with your production key and salt. These credentials will be used for live transactions. You can generate the live merchant key and salt by logging in to the PayU Dashboard and switching to Live Mode on the menu. Navigate to Payment Gateway → Web Integration → Key Salt Details. 
* **Secure Hosting (HTTPS)**: Your website must be hosted on a secure server with HTTPS enabled to protect sensitive payment data. 
* **PCI DSS Compliance**: If you are storing, processing, or transmitting cardholder data, you must comply with the Payment Card Industry Data Security Standard (PCI DSS). This might involve filling the “Self-Assessment Questionnaire A-EP and Attestation of Compliance” form from PCI. If you are using Merchant Hosted Checkout, you will collect card details on your own website and therefore you must be PCI-DSS compliant. 
* **Webhooks Implementation**: Set up webhooks to receive real-time updates on transaction statuses. Webhooks allow PayU to notify your server about successful payments, failures, and other important events. Confirmed the transaction status on the Server-side, if the callback fail. Use Webhooks for hearing callbacks. For more information, refer to Verify Payment API and Webhooks.

> 🚧 Remember
>
> If you are using only the UPI and Wallet payment modes with Merchant Hosted checkout, ensure that your website is secure.

* **Understanding of concepts and technical bandwidth**: You must have an understanding of the following concepts and take care of the technical bandwidth:
  * workflows
  * various payment processes
  * website designing fundamentals
  * Usability (UX) management principles necessary to build the complete online payments infrastructure on your website.
  * Sufficient technical bandwidth dedicated to managing the end-to-end web checkout processes in-house consistently.

## Authentication

PayU uses a hashing mechanism to ensure the security and integrity of API requests and responses. Hashing involves creating a unique, fixed-size string (the hash) from a variable-length input using a cryptographic algorithm. This hash acts as a digital signature, verifying that the data has not been tampered with during transmission. 

### Key Concepts

* **Key**: Your unique merchant identifier provided by PayU. 
* **Salt**: A secret key known only to you and PayU, used to generate the hash. 
* **Hash Algorithm**: PayU typically uses the SHA-512 algorithm for hashing. 

### Hashing Process

1. **Construct the Plaintext String**: Create a string by concatenating the required parameters in a specific order, separated by the ‘|’ character. The order of parameters is crucial for generating the correct hash. 
2. **Append the Salt**: Add your PayU salt to the end of the plaintext string. 
3. **Calculate the SHA-512 Hash**: Use a SHA-512 hashing function to generate the hash of the resulting string. 

#### Sample Code

```
import hashlib 
 
def generate_hash(key, txnid, amount, productinfo, firstname, email, salt): 
    """Generates the SHA-512 hash for PayU API requests.""" 
    plaintext = f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}||||||||||{salt}" 
    hash_object = hashlib.sha512(plaintext.encode()) 
    hash_value = hash_object.hexdigest() 
    return hash_value 
 
# Example Usage 
key = "YOUR_MERCHANT_KEY" 
txnid = "YOUR_TRANSACTION_ID" 
amount = "100.00" 
productinfo = "Product Description" 
firstname = "John" 
email = "john@example.com" 
salt = "YOUR_MERCHANT_SALT" 
 
hash_value = generate_hash(key, txnid, amount, productinfo, firstname, email, salt) 
print(f"Generated Hash: {hash_value}") 
```

#### Hash Verification

When PayU sends a response to your server, it includes a hash value calculated using the same process. You must verify this hash to ensure that the response has not been tampered with during transit. Recreate the hash on your server using the response parameters and your salt. If the generated hash matches the hash received from PayU, the response is valid.

## Integration Steps

With Merchant Hosted Checkout, you are responsible for collecting payment details from the customer on your website. Ensure that you follow security best practices to protect sensitive data. 

**Best Practices:** 

* **Use Secure Input Fields**: Implement secure input fields for collecting card details, such as those provided by a PCI DSS compliant payment gateway. 
* **Encrypt Data in Transit**: Always transmit payment data over HTTPS using TLS encryption. 
* **Tokenization**: Consider using tokenization to replace sensitive card details with a non-sensitive token. This reduces the risk of data breaches and simplifies PCI DSS compliance. For more information on Save Cards API integration, refer to PayU Save Cards API Integration docs. 
* **Avoid Storing Sensitive Data**: Do not store sensitive card details (CVV, full card number) on your servers. If you need to store card information for recurring payments, use PayU’s Save Cards feature or a PCI DSS compliant tokenization service.

### Post request syntax & composition

Post Request Syntax & Composition for Net Banking

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
<input type="hidden" name="pg" value="TESTPG" />
<input type="hidden" name="bankcode" value="TESTPGNB" />
<input type="hidden" name="surl" value="your own success url" />
<input type="hidden" name="furl" value="your own failure url" />
<input type="hidden" name="phone" value="9988776655” />
<input type="hidden" name="hash" value="eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972" />
<input type="submit" value="submit"> </form>
</body>
</html>
```

> 📘 Note
>
> The above HTML code block is for Merchant Checkout integration on the Net Banking call for the test environment.

### Step 1: Post Request to PayU

The following parameters vary for the NetBanking payment mode in the **Collect Payment** API (**\_payment** API).

**Environment**

|                            |                                                                         |
| :------------------------- | :---------------------------------------------------------------------- |
| **Test Environment**       | \<[https://test.payu.in/\_payment>](https://test.payu.in/_payment>)     |
| **Production Environment** | \<[https://secure.payu.in/\_payment>](https://secure.payu.in/_payment>) |

> 📘 Reference:
>
> For the complete list of parameters and response, refer to [Collect Payment API - Merchant Hosted Checkout](doc:_payment_merchant_hosted) under API Reference.

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
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        <Glossary>key</Glossary>
        `mandatory`
      </td>

      <td>
        `String`Merchant key provided by PayU during onboarding.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        <Glossary>txnid</Glossary>\
        `mandatory`
      </td>

      <td>
        `String`The transaction ID is a reference number for a specific order that is generated by the merchant.
      </td>

      <td>

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
        email\
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
        phone\
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
        pg\
        `mandatory`
      </td>

      <td>
        `String` The pg parameter determines which payment tabs will be displayed on the PayU page. For more information, refer to [Supported Payment Methods with additional details of integration](#supported-payment-methods-details-for-api-integration).
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
        `String` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option’s bank code value in it. For the list of bank codes that can be used with the **bankcode** parameter, refer to [Bank and Card Codes for Integration](doc:bank-and-card-codes-for-integration).
      </td>

      <td>
        AMEX
      </td>
    </tr>

    <tr>
      <td>
        ccnum\
        `mandatory for cards`
      </td>

      <td>
        `String` Use 13-19 digit card number for credit/debit cards (15 digits for AMEX, 13-19 for Maestro) and validate with LUHN algorithm. Refer to  [Card Number Formats](doc:card-number-formats) and display error message on invalid input.
      </td>

      <td>
        5123456789012346
      </td>
    </tr>

    <tr>
      <td>
        ccname  `mandatory for cards`
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
        ccvv\
        `mandatory for cards`
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
        ccexpmon  `mandatory for cards`
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
        ccexpyr\
        `mandatory for cards`
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
        beneficiarydetail\
        `mandatory for NetBanking and EFTNEFT`
      </td>

      <td>
        `String`This is a JSON format text and there should be key named beneficiaryAccountNumber with account number as value and ifscCode with customer IFSC code as value.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        vpa\
        `mandatory for UPI`
      </td>

      <td>
        `String` The VPA of the customer. For the list of bank name part of the handles, refer to [UPI Handles](doc:upi-handles)  . **Reference**: For the list of test card numbers for EMI, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets)
      </td>

      <td>
        test\@payu
      </td>
    </tr>

    <tr>
      <td>
        furl\
        `mandatory`
      </td>

      <td>
        `String`The success URL, which is the page PayU will redirect to if the transaction is successful.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        surl\
        `mandatory`
      </td>

      <td>
        `String`The Failure URL, which is the page PayU will redirect to if the transaction is failed.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        hash\
        `mandatory`
      </td>

      <td>
        `String`It is the hash calculated by the merchant. The hash calculation logic is:\
        `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\||\||\||SALT)`
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        api\_version\
        `optional`
      </td>

      <td>
        `String`The api\_version is conditional. You must pass “6” for NEFT/RTGS.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        address1\
        `optional`
      </td>

      <td>
        `String` The first line of the billing address.

        * *For Fraud Detection*\*: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        address2\
        `optional`
      </td>

      <td>
        `String` The second line of the billing address.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        city\
        `optional`
      </td>

      <td>
        `String` The city where your customer resides as part of the billing address.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        state\
        `optional`
      </td>

      <td>
        `String` The state where your customer resides as part of the billing address,
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        country\
        `optional`
      </td>

      <td>
        `String` The country where your customer resides.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        zipcode\
        `optional`
      </td>

      <td>
        `String` Billing address zip code is mandatory for the cardless EMI option.\
        `Character Limit`-20
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf1\
        `optional`
      </td>

      <td>
        `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf2\
        `optional`
      </td>

      <td>
        `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf3\
        `optional`
      </td>

      <td>
        `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf4\
        `optional`
      </td>

      <td>
        `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf5\
        `optional`
      </td>

      <td>
        `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

<HashingRequestParameters />

### Sample request

```curl
curl -X \
 POST "https://test.payu.in/_payment" -H \
 "accept: application/json" -H \
 "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=ewP8oRopzdHEtC&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=TESTPG&bankcode=TESTPGNB&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"
```
```javascript
/**
 * PayU Payment Request using Fetch API
 * 
 * IMPORTANT: This should only be executed server-side, never in the browser,
 * as it contains sensitive payment information.
 */

// Payment endpoint
const url = 'https://test.payu.in/_payment';

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
  })
  .catch(error => {
    console.error('Error:', error);
  });

```
```python
import urllib.request
import urllib.parse

url = "https://test.payu.in/_payment"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

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
    "hash": "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"
}

data = urllib.parse.urlencode(payload).encode('utf-8')
req = urllib.request.Request(url, data=data, headers=headers, method="POST")

try:
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode('utf-8')
        print("Status Code:", response.getcode())
        print("Response:")
        print(response_body)
except urllib.error.HTTPError as e:
    print("Error:", e.code, e.reason)
    print(e.read().decode('utf-8'))

```
```php
import urllib.request
import urllib.parse

url = "https://test.payu.in/_payment"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

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
    "hash": "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"
}

data = urllib.parse.urlencode(payload).encode('utf-8')
req = urllib.request.Request(url, data=data, headers=headers, method="POST")

try:
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode('utf-8')
        print("Status Code:", response.getcode())
        print("Response:")
        print(response_body)
except urllib.error.HTTPError as e:
    print("Error:", e.code, e.reason)
    print(e.read().decode('utf-8'))

```
```java
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;
import java.util.StringJoiner;

public class PayUPaymentRequest {
    
    public static void main(String[] args) {
        try {
            // API endpoint
            String url = "https://test.payu.in/_payment";
            
            // Form parameters
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
            params.put("hash", "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319");
            
            // Convert parameters to URL encoded form data
            StringJoiner sj = new StringJoiner("&");
            for (Map.Entry<String, String> entry : params.entrySet()) {
                sj.add(URLEncoder.encode(entry.getKey(), "UTF-8") + "="
                     + URLEncoder.encode(entry.getValue(), "UTF-8"));
            }
            byte[] postData = sj.toString().getBytes(StandardCharsets.UTF_8);
            
            // Create connection
            URL apiUrl = new URL(url);
            HttpURLConnection conn = (HttpURLConnection) apiUrl.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("accept", "application/json");
            conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
            conn.setRequestProperty("Content-Length", String.valueOf(postData.length));
            conn.setDoOutput(true);
            
            // Send request
            try (DataOutputStream dos = new DataOutputStream(conn.getOutputStream())) {
                dos.write(postData);
            }
            
            // Read response
            int responseCode = conn.getResponseCode();
            try (BufferedReader br = new BufferedReader(
                    new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8))) {
                StringBuilder response = new StringBuilder();
                String responseLine;
                while ((responseLine = br.readLine()) != null) {
                    response.append(responseLine.trim());
                }
                
                System.out.println("Status Code: " + responseCode);
                System.out.println("Response: " + response.toString());
            }
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

```

### Step 2: Handling the response from PayU

<ReverseHashing />

> 📘 Important Considerations:
>
> * **Verify the Hash**: Always verify the hash received in the response to ensure the integrity of the data. 
> * **Check the Transaction Status**: Use the status parameter to determine the outcome of the transaction. 
> * **success**: The payment was successful. 
> * **failure**: The payment failed. 
> * **pending**: The transaction is still being processed. 
> * **Handle Pending Transactions**: Implement a mechanism to handle pending transactions. Use webhooks or the Verify Payment API to check the final status of the transaction. 
> * **Display Confirmation**: Display a clear confirmation message to the customer, indicating whether the payment was successful or not.

#### Sample response (parsed)

```
Array
(
    [mihpayid] => 403993715524045752
    [mode] => NB
    [status] => success
    [unmappedstatus] => captured
    [key] => JPM7Fg
    [txnid] => ewP8oRopzdHEtC
    [amount] => 10.00
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2021-09-06 13:27:08
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
    [hash] => 1be7e6e97ab1ea9034b9a107e7cf9718308aa9637b4dbbd1a3343c91b0da02b34a40d00ac7267ebe81c20ea1129b931371c555d565bc6e11f470c3d2cf69b5a3
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
    [PG_TYPE] => NB-PG
    [bank_ref_num] => 87d3b2a1-5a60-4169-8692-649f61923b3d
    [bankcode] => TESTPGNB
    [error] => E000
    [error_Message] => No Error
)
```

### Step 3: Verify the payment

Verify the transaction details using the Verification APIs. For more information, refer to \[Verify Payment API]\(ref: verify\_payment\_api) under API Reference.

> 📘 Tip
>
> The transaction ID that you posted in Step 1 with PayU must be used here.

## Payment Methods

Merchant Hosted Checkout supports a wide range of payment methods: 

* **Credit Cards and Debit Cards**: Visa, Mastercard, American Express, etc. 
* **Net Banking**: Collect payments through EFTNET (NEFT/RTGS) transactions using PayU’s Merchant Hosted Checkout integration. Merchants should always send both customer account no and customer IFSC Code in Request. For NEFT/RTGS TPV, the flow will work for txn\_s2s\_flow = 1 or txn\_s2s\_flow = 4 as is. EFTAXTPV must be used as bankcode for NEFT/RTGS. The api\_version “6” must be passed for this parameter for NEFT/RTGS. 
* **Wallets**: Integrate with popular wallets like Paytm, PhonePe, and others. 
* **UPI**: Collect payments via UPI using the customer’s UPI ID. 
* **EMI (Equated Monthly Installments)**: Offer customers the option to pay in installments. 
* **BNPL (Buy Now, Pay Later)**: Integrate with BNPL providers to allow customers to spread payments over time. 
* **PayPal**: Facilitate international payments through PayPal. If you’re using the PayU Hosted Checkout or Merchant Hosted integration, you need to activate PayPal from PayU Dashboard. 
* **Pluxee Card**: Integrate with Pluxee (formerly Sodexo) meal cards. For Sodexo payment option mode or PG is MC and Ibibo\_code or bankcodeis SODEXO. In case customer provides the consent to save the card details with merchant on their check-out page: Merchant should pass save\_sodexo\_card parameter value as 1 when initiating the transaction using \_payment API. Merchants are recommended to use the check\_balance API for checking the Sodexo card balance. 
* **QR Code**: Enable payments via QR codes. 

> 📘 Note:
>
> For each payment method, you may need to pass specific parameters in the \_payment API request. Refer to the PayU documentation for each payment method for details. For all the supported wallets, refer to Wallet Codes to understand exact value which needs to be passed against bankcode parameter. 

### Supported Payment Methods: Details for API Integration

The following table summarizes the supported payment methods for PayU’s Merchant Hosted Checkout, along with the corresponding bankcode and pg values required in the \_payment API request. It also includes other relevant details and considerations for each payment method. 

| Payment Method       | pg     | bankcode                 | Additional Details                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------- | ------ | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Credit/Debit Cards   | CC     | N/A                      | No bankcode is needed for card payments. Card details (ccnum, ccname, ccexpmon, ccexpyr, ccvv) must be collected securely on your website. Ensure PCI DSS compliance if collecting card details directly. Implement 3D Secure for enhanced security.                                                                                                                                                                                  |
| Net Banking          | NB     | Varies (Bank-Specific)   | Refer to the PayU documentation for a complete list of bank codes. Each bank has a unique code. Collect customer's net banking credentials securely. If you are using Merchant Hosted Checkout, you will collect card details on your own website and therefore you must be PCI-DSS compliant. Always use HTTPS to encrypt data transmitted between your website and the customer's browser, as well as between your server and PayU. |
| Wallets              | CASH   | Varies (Wallet-Specific) | Refer to the PayU documentation for a complete list of wallet codes. Examples: PAYTM, PHONEPE, AMAZONPAY. The bankcode value should correspond to the specific wallet the customer chooses. Ensure you display the available wallet options to the customer clearly.                                                                                                                                                                  |
| UPI                  | UPI    | N/A                      | UPI payments require the customer to enter their UPI ID or scan a QR code. The pg value depends on whether its collect or intent flow. If its UPI collect, the customer will need to manually authorize the payment from the UPI app and no bankcode is required for UPI.                                                                                                                                                             |
| EMI                  | CC     | N/A                      | EMI is usually processed through credit cards. The pg value is CC. You may need to pass additional parameters related to the EMI plan, such as the number of months and the interest rate. The availability of EMI options depends on the card issuing bank and PayU's agreements. For more information, refer to [EMI](doc:emi-api-integration).                                                                                     |
| BNPL                 | Varies | Varies                   | The pg and bankcode values depend on the specific BNPL provider. Refer to the PayU documentation for the correct values for each provider. Integration requirements vary depending on the provider. For more information, refer to [BNPL Integration](doc:payu-bnpl-integration-introduction).                                                                                                                                        |
| PayPal               | PAYPAL | N/A                      | Activate PayPal from the PayU Dashboard before integrating. No bankcode is required for PayPal. Settlements are typically processed in INR. You're using the PayU Hosted Checkout or Merchant Hosted integration, you need to activate PayPal from PayU Dashboard.                                                                                                                                                                    |
| Pluxee Card (Sodexo) | MC     | SODEXO                   | Use the SODEXO bankcode. The pg value is MC. Merchants are recommended to use the check\_balance API for checking the Sodexo card balance.                                                                                                                                                                                                                                                                                            |
| EFTNET (NEFT/RTGS)   | NB     | EFTAXTPV                 | The api\_version "6" must be passed for this parameter for NEFT/RTGS. Merchants should always send both customer account no and customer IFSC Code in Request.                                                                                                                                                                                                                                                                        |
| QR Code              | UPI    | N/A                      | The QR code format should be as per Bharat QR specifications.                                                                                                                                                                                                                                                                                                                                                                         |

> 📘 Important Notes: 
>
> * Always refer to the official PayU documentation for the most up-to-date information on supported payment methods and their corresponding parameters. 
> * The bankcode values are case-sensitive. 
> * Ensure that the payment methods you intend to support are enabled in your PayU merchant account. 
> * Test your integration thoroughly in the PayU sandbox environment before going live. 
> * For NEFT/RTGS transactions, implement a reconciliation process to track transaction status and match payments with orders.

## Security and testing the Integration

### Security considerations

Security is paramount when handling payment data. Implement the following security measures: 

* **HTTPS**: Always use HTTPS to encrypt data transmitted between your website and the customer’s browser, as well as between your server and PayU. 
* **Data Encryption**: Encrypt sensitive data both in transit and at rest. 
* **Tokenization**: Use tokenization to protect sensitive card details. 
* **Regular Security Audits**: Conduct regular security audits to identify and address potential vulnerabilities. 
* **3D Secure**: Implement 3D Secure (3DS) for card payments to add an extra layer of authentication. PayU supports 3DS Secure 2.0 transaction with Merchant Hosted Checkout integration. 
* **CVV Handling**: Never store the CVV (Card Verification Value). 
* **IP Address Restriction**: Implement IP Address Restriction. 
* **Webhooks Security**: Make sure webhooks are properly configured. 

#### Testing and Go-Live

Before going live, thoroughly test your integration in the PayU sandbox environment. 

### Testing steps

* **Use Test Credentials**: Use your test key and salt to make test transactions. 
* **Simulate Different Scenarios**: Test successful payments, failed payments, and pending transactions. 
* **Verify Webhooks**: Ensure that your webhook implementation is correctly receiving and processing transaction updates. 
* **Test Different Payment Methods**: Test all the payment methods you intend to support in your production environment. 
* **Use Test Data**: Use test credentials for Net Banking: user name: payu. password: payu. OTP: 123456. 

#### Go-Live Checklist

* **Replace Test Credentials**: Replace your test key and salt with your production credentials. 
* **Final Verification**: Perform a final checkout verification to ensure all payment details are collected and processed correctly. 
* **Enable Webhooks**: Ensure that webhooks are enabled and configured to receive transaction updates in your production environment. 
* **Monitor Transactions**: Closely monitor transactions in the first few days after going live to identify and address any issues. 

### Troubleshooting and error handling

* **Incorrect Hash**: Double-check the hash generation logic and ensure that the parameters are in the correct order. 
* **Invalid API Credentials**: Verify that you are using the correct key and salt for the environment (test or production). 
* **Payment Method Not Enabled**: Ensure that the payment method you are trying to use is enabled in your PayU merchant account. 
* **Webhook Issues**: Check your webhook logs to identify any errors in processing transaction updates.

## Check Net Banking health

You can check whether the Net Banking server is up and running using the **getNetBankingStatus** API. If the Net Banking server is down for a bank, you can inform your customers that the Net Banking server is down. For more information on the **getNetBankingStatus** API, refer to getNetBankingStatus.

## Recommended integrations for Net Banking

* **Recurring Payments**: Enable recurring payments or subscriptions for wallets. For more information, refer to [Recurring Payments Integration](doc:introduction-recurring-payments-integration).
* **Offers**: Configure offers for cards on Dashboard and then collect payments with offers. For more information, refer to [Create a No-Cost EMI Offer](doc:create-a-no-cost-emi-offer) and [Create a SKU-Based Offer](doc:create-a-sku-based-offer).