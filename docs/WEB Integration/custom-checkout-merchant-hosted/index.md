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

> 👍 Before you Begin:
>
> * PayU strongly recommends you test your integration using the test merchant Key or Salt. To create a test merchant account, refer to [Register for a Merchant Account on Dashboard](doc:register-for-a-merchant-account-on-dashboard). After you create a test merchant account, you can access the test Key or Salt as described in [Generate Merchant Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard).
> * Later, register for a production account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

### Key Benefits

* **Customizable UI**: Design a checkout flow that seamlessly integrates with your brand. 
* **Direct Customer Relationship**: Maintain control over the customer experience from start to finish. 
* **Flexible Integration**: Integrate with a wide range of payment methods, including cards, net banking, wallets, UPI, and more.

<br />

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