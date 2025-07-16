---
title: Integration Steps
deprecated: false
hidden: false
metadata:
  robots: index
---
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

## Best Practices

* **Use Secure Input Fields**: Implement secure input fields for collecting card details, such as those provided by a PCI DSS compliant payment gateway. 
* **Encrypt Data in Transit**: Always transmit payment data over HTTPS using TLS encryption. 
* **Tokenization**: Consider using tokenization to replace sensitive card details with a non-sensitive token. This reduces the risk of data breaches and simplifies PCI DSS compliance. For more information on Save Cards API integration, refer to PayU Save Cards API Integration docs. 
* **Avoid Storing Sensitive Data**: Do not store sensitive card details (CVV, full card number) on your servers. If you need to store card information for recurring payments, use PayU’s Save Cards feature or a PCI DSS compliant tokenization service.