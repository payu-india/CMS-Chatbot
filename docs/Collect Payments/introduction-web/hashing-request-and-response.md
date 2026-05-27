---
title: Generate Hash
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Generate Hash for Server-to-Server integration
  description: >-
    The page you are referring to is about generating hash for Server-to-Server
    integration. The page provides information on how to generate a hash value
    for a payment request using the SHA-512 hash function that belongs to the
    SHA-2 family of cryptographic functions. The hash is used to protect
    transactions against a “man-in-the-middle-attack” 1.
  robots: index
next:
  description: ''
---
A hash is an encrypted value (checksum) that is sent by you in a payment request and reverted by PayU in the payment response. The hash is used to protect transactions against a “man-in-the-middle-attack.”

> 📘 **Hashing logic for Web Integration and SDK is different**:&#x20;
>
> For the hashing logic in Android SDK or iOS SKD, refer to [Generate Dynamic Hash](doc:ioscheckoutpro-generate-hash).

## Hash Generation Logic for Basic Payment Request

PayU uses the SHA-512 hash function that belongs to the SHA-2 family of cryptographic functions to generate hash values.

To generate hash for a payment request in general:

1. **Collect Transaction Data**: Gather the required transaction details, including: 

- <Glossary>key</Glossary>: Your merchant key (Test or Production key).
- txnid: Unique transaction ID 
- amount: Transaction amount 
- productinfo: Product information 
- firstname: Customer's first name 
- email: Customer's email ID 
- <Glossary>Salt</Glossary>: Your Salt (Test or Production)

> 📘
>
> **Reference**: For more information on getting key and salt, refer to [Generate Test Merchant Key and Salt](doc:generate-merchant-key-and-salt-copy#) or [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-copy#).

2. **Create a Hash String**: Concatenate the collected data in the following format: 
   `sha512(key|txnid|amount|productinfo|firstname|email|||||||||||SALT)` 
3. **Generate Hash**: Use the SHA512 encryption algorithm to generate a hash of the concatenated string. 

> 📘
>
> **Hash logic for \_payment API Version 19**: The following hash logic must be used for \_payment API with **api\_version=19**:
> `key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|user_token|offer_key|offer_auto_apply|cart_details|extra_charges|phone`

### Example Hash Generation

Suppose the transaction data is: 

- key: gtKFFx 
- txnid: 123456789 
- amount: 10.00 
- productinfo: Test Product 
- firstname: John 
- email: [john@example.com](mailto:john@example.com) 
- Salt: \<Salt>

The concatenated string would be: 

`JP***g|123456789|10.00|Test Product|John|john@example.com|||||||||||| <Salt>` 

> 📘 Important Notes:
>
> - Ensure that the hash is generated using the SHA512 encryption algorithm. 
> - The hash should be generated on the server-side to prevent tampering. 
> - The hash should be verified on the PayU server to ensure the authenticity of the transaction data. 
> - Salt is a susceptible information. **Do not** pass Salt in the payment request. 
> - PayU recommends you to use **Merchant Salt (Version 2)**. To know more about generating salt, that is **Merchant Salt (Version 2)**, see [Access Production Key and Salt](doc:generate-merchant-key-and-salt-copy#).

> 🚧 Salt Security
>
> Salt is a susceptible information. **Do not** pass Salt in the payment request. To know more about generating salt, see [Generate Merchant Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-copy#).

For more information on the parameters (and their descriptions) listed in the above hash logic, refer to any of the following based on the merchant hosted integration you are integrating:

- [Net Banking](https://docs.payu.in/reference/_payment_merchant_hosted_netbanking)
- [Cards](https://docs.payu.in/reference/_payment_merchant_hosted_cards)
- [UPI](https://docs.payu.in/reference/_payment_merchant_hosted_upi)
- [Wallets](https://docs.payu.in/reference/_payment_merchant_hosted_wallets)
- [EMI](https://docs.payu.in/reference/_payment_merchant_hosted_emi)
- [BNPL](https://docs.payu.in/reference/_payment_merchant_hosted_bnpl)

### Sample code for generating hash

<HashingSample />

<br />

> 📘 Reference:
>
> You can use the Hash API of the PayU node SDK on Github to perform hashing. Refer to the [PayU node SDK Readme](https://github.com/payu-india/payu-sdk-node/blob/main/README.md), download and install the PayU node SDK from the [PayU node SDK Github location](https://github.com/payu-india/payu-sdk-node).

### Hashing scenarios for payment request

Here, we will discuss some payment request scenarios and see how hash calculation varies for each of them:

- **Scenario 1**: When all the udf parameters (udf1-udf5) are posted by the merchant, hash is calculated as:

```
sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|SALT)
```

- **Scenario 2**: If only some of the udf parameters are posted . For example, if udf2 and udf4 are posted and udf1, udf3, udf5 are not, hash is calculated as:

```
sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|\|udf2\|\|udf4\|\|\|\|\|\|\|SALT)
```

- **Scenario 3**: If none of the udf parameters (udf1-udf5) are posted, hash is calculated as:

```
sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|\|\|\|\|\|\|\|\|\|\|SALT)
```

> 📘
>
> **Delimiters when UDF parameters are not passed**: Ensure that you include the delimiters (pipe symbol: **|**) if you don't pass the UDF parameters, so you need to ensure that 5 delimiters are included if UDF parameters are not passed. There are 15 delimiters in total.

<details>
  <summary>Tips for Hashing</summary>

- In the **test environment** (payu.test.in), PayU displays the error message and the correct action required to resolve the error.
- However, in the **live environment**, to retain the confidentiality of the business information, PayU displays only an error message and drops the transaction.
- It has been observed that a majority of the hash mismatch errors result from an incorrect key insert by the merchant’s developers while generating the hash value. For instance:

| Inserting Merchant ID (MID) instead of Merchant Key                   | sha512(4**1**1112345110001 Shopping I Vinay I [vinay@test.com](mailto:vinay@test.com) I &#x33;**\*\*\*\***&#x73;**\***&#x6B;**\*\*\*\***&#x68;**\***&#x6A;)                   |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inserting SALT instead of Merchant Key & Merchant ID in place of SALT | sha512(&#x33;**\*\*\*\***&#x73;**\***&#x6B;**\*\*\*\***&#x68;**\***[j112345110001Shopping1Vinaylvinay@test.com](mailto:j112345110001Shopping1Vinaylvinay@test.com) \|4**1**1) |

In these cases, while PayU will compile the hash value with the right positioning of the merchant key and salt in the string, it will be different from the one posted by the merchant for apparent reasons, leading to a mismatch.

- PayU advises **against sending the salt value as part of the payment request package**, as it severely compromises the security of the transaction. Because, with access to the salt, a malicious actor executing a _man-in-the-middle_ (MITM) attack can easily alter the details, regenerate the hash value, and can pass the same through the authentication filters in the PayU’s servers.

</details>

## Hash Validation Logic for Payment Response (Reverse Hashing)

While sending the response, PayU takes the exact same parameters that were sent in the request (in reverse order) to calculate the hash and returns it to you. You must verify the hash and then mark a transaction as a success or failure. This is to make sure the transaction has not tampered within the response.

<Reverse_Hash_Types />

### Integration Security

After receiving a response from PayU, you must calculate the hash again and validate it against the hash that you sent in the request to ensure the transaction is secure. PayU recommends implementing the transaction details APIs and **webhook**/**callbac**k as an extra security measure. You can find more information on this process in the [Transaction Detail APIs](ref:transaction-detail-apis) and [Webhooks](doc:webhooks).

You need to ensure that sensitive information related to the integration is not part of the payment request to PayU. The details including — but are not limited to — the following are considered sensitive information:

- salt value
- plain text hash string

Along with the request, the sensitive information should not be a part of any merchant-level URL. The following are considered sources for the merchant-level URL:

- The last web address accessed by a browser before loading PayU’s checkout page.
- URLs shared as part of payment request to PayU in the parameters: surl, furl, curl, nurl, and termUrl.
- Notification URLs configured with the merchant account.
- Invoice Completion URLs configured with the merchant account.

> 📘 Note:
>
> It is important to compare the parameters sent by PayU in the response with the ones you sent in the request to make sure none of them have been changed. You should verify specific parameters such as the transaction ID and amount. PayU is not responsible for any security breaches or losses resulting from your failure to implement the necessary security measures.

<br />
