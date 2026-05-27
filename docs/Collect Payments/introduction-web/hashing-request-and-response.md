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

<Cards>
  <Card title="Hash Generation Logic for Basic Payment Request" href="#hash-generation-logic-for-basic-payment-request" icon="fa-rocket">
    Detailed explanation of hash generation logic for _payment request
  </Card>

  <Card title="Hash Validation Logic for Payment Response (Reverse Hashing)API Reference" href="#hash-validation-logic-for-payment-response-reverse-hashing" icon="fa-code">
    Detailed explanation of hash validatio  logic of _payment response
  </Card>

  <Card title="Hash Generation Logic for General Command-based APIs" href="#hash-generation-logic-for-general-command-based-apis" icon="fa-comments">
    Hash Generation logic for General APIs such as Verify Payment, Get Checkout, Split After Payment, etc.
  </Card>
</Cards>

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

## Hash Generation Logic for General Command-based APIs&#x20;

> 📘 Notes
>
> - **Test endpoint:** `https://test.payu.in/merchant/postservice` (typically with `?form=2` for JSON responses).
> - For most command-based postservice APIs, PayU uses `sha512(key|command|var1|salt)`. Regenerate the hash whenever request parameters change. See \[REST API Format]\(docs/API basics/rest-api-format.md) and [API Authentication and Security](https://docs.payu.in/docs/api-authentication-and-security).

Notes

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>API</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>command</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Hash logic</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:verify_payment_api">Verify Payment API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>verify_payment</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|verify_payment|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:get_transaction_details_api">Get Transaction Details API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>get_Transaction_Details</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|get_Transaction_Details|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = start date (<code>YYYY-MM-DD</code>). <em>var2</em> (end date) is required in the request but is not part of the hash string.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:get_transaction_info_api">Get Transaction Info API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>get_transaction_info</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|get_transaction_info|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = start time (<code>YYYY-MM-DD HH:MM:SS</code>). <em>var2</em> (end time) is required in the request but is not part of the hash string.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:get_tdr_api">Get TDR API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>get_TDR</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|get_TDR|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = PayU ID (<code>mihpayid</code>).</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:refund_transaction_api">Refund Transaction API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>cancel_refund_transaction</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|cancel_refund_transaction|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = PayU ID (<code>mihpayid</code>).</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:get_all_refunds_from_transaction_ids_api">Get All Refunds from Transaction ID</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>getAllRefundsFromTxnIds</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|getAllRefundsFromTxnIds|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = merchant transaction ID (<code>txnid</code>).</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:check_action_status_api_with_payu_id">Check Action Status with PayU ID</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>check_action_status</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|check_action_status|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = PayU ID (<code>mihpayid</code>). Set <em>var2</em> = <code>payuid</code> (not included in hash).</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:check_action_status_api_with_request_id">Check Refund Status with Request ID API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>check_action_status_txnid</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|check_action_status_txnid|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = request ID returned from <code>cancel_refund_transaction</code>.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:check_is_domestic_api">Check is Domestic API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>check_isDomestic</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|check_isDomestic|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = card BIN (first 6 digits) or card number.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:get_bin_info_api">Get BIN Info API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>getBinInfo</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|getBinInfo|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:get_emi_according_to_interest_api">Get EMI Amount according to Interest API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>getEmiAmount<br>AccordingTo<br>Interest</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|getEmiAmountAccordingToInterest|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = transaction amount.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:get_issuing_bank_status_api">Get Issuing Bank Status API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>getIssuingBankStatus</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|getIssuingBankStatus|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = card BIN.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:get_issuing_bank_down_bins_api">Get Issuing Bank Down BINs API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>getIssuingBankDownBins</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|getIssuingBankDownBins|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = bank name code or <code>default</code>. <em>var2</em> (<code>0</code> / <code>1</code>) is not part of the hash string.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:get_net_banking_status_api">Get Net Banking Status API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>getNetbankingStatus</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|getNetbankingStatus|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = <code>default</code> (all banks) or a specific net banking bank code.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:get_checkout_details">Get Checkout Details API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>get_checkout_details</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|get_checkout_details|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = JSON string with transaction / eligibility details.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:get-checkout-details-ntb-seamless-journey">Get Checkout Details – NTB Seamless Journey</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>get_checkout_details</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|get_checkout_details|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = JSON string with transaction / eligibility details.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:check-offer-status-api">Check Offer Status API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>check_offer_status</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|check_offer_status|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = offer key. Additional parameters (<em>var2</em>–<em>var8</em>) may be sent but are not part of the standard hash string.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:fetch-balance-api-sodexo">Fetch Balance API (Sodexo)</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>check_balance</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|check_balance|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = JSON with Sodexo source ID.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:fetch-balance-api">Fetch Balance API (Open Loop Wallet)</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>check_balance</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|check_balance|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = customer mobile number.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:release_settlement_api">Release Settlement API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>release_settlement</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|release_settlement|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = PayU ID (<code>mihpayuid</code>).</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:get-settlement-detail-api-cross-border-payments">Get Settlement Detail API (Cross-Border)</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>get_settlement_details</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|get_settlement_details|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = settlement date (<code>YYYY-MM-DD</code>). Some CB deployments also support HMAC authorization on a separate treasury endpoint—refer to the API reference.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:udf_update_api">UDF Update API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>udf_update</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|udf_update|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = JSON with PayU ID and UDF fields to update.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:recurring_payment_api">Recurring Payment Transaction API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>si_transaction</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|si_transaction|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = JSON with recurring debit details (<code>authpayuid</code>, amount, <code>txnid</code>, etc.).</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:si-transaction-api-parallel-sequencing">SI Transaction API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>si_transaction</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|si_transaction|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = JSON with recurring debit details (includes <code>mandateSeqNo</code> for parallel sequencing).</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:recurring-payment-transaction-api-pacb">Recurring Payment Transaction API – PACB</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>si_transaction</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|si_transaction|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = JSON with recurring debit and cross-border UDF details.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:pre_debit_notification_api">Pre-Debit Notification API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>pre_debit_SI</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|pre_debit_SI|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = JSON with mandate and debit notification details.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:validate_vpa_api">Validate VPA API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>validateVPA</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|validateVPA|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = customer VPA (UPI handle).</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:check-the-mandate-status">Check the Mandate Status</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>check_mandate_status</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|check_mandate_status|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = JSON with <code>authPayuId</code>, <code>requestId</code>, amount, and end date.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:net_banking_mandate_status_api">Check Net Banking Mandate Status API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>NB_mandate_status</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|NB_mandate_status|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = JSON with <code>authPayuId</code> and <code>requestId</code>.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:cancel-the-recurring-payment-for-cards">Cancel Recurring Payment (Cards)</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>mandate_revoke</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|mandate_revoke|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = JSON with <code>authPayuId</code> and <code>requestId</code>.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:cancel-the-recurring-payment-for-net-banking">Cancel Recurring Payment (Net Banking)</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>mandate_revoke</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|mandate_revoke|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = JSON with <code>authPayuId</code> and <code>requestId</code>.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:cancel-the-recurring-payment-for-upi">Cancel Recurring Payment (UPI)</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>upi_mandate_<br>revoke</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|upi_mandate_revoke|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = JSON with <code>authPayuId</code> and <code>requestId</code>.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:get_user_cards_api">Get User Cards API (Model 2)</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>get_user_cards</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|get_user_cards|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = <code>&lt;merchantKey&gt;:&lt;userId&gt;</code>.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:get_user_cards_api_model3">Get User Cards API – Model 3</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>get_payment_<br>instrument</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|get_payment_instrument|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = <code>&lt;merchantKey&gt;:&lt;userId&gt;</code>.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:save_card_api">Tokenize a Card API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>save_payment_<br>instrument</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|save_payment_instrument|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = <code>&lt;merchantKey&gt;:&lt;userId&gt;</code>.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:edit_saved_card_api">Edit a Saved Card API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>edit_payment_<br>instrument</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|edit_payment_instrument|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = <code>&lt;merchantKey&gt;:&lt;userId&gt;</code>.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:collect-payments-save-card">Collect Payments – Save Card</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>get_user_cards</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|get_user_cards|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = <code>&lt;merchantKey&gt;:&lt;userId&gt;</code>.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:get_split_info_api">Get Split Info API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>get_split_info</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|get_split_info|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = parent PayU ID (<code>payuId</code>). Hash string uses <code>payuId</code> in place of <code>var1</code> in the pipe sequence.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:split_after_transaction_api">Split After Transaction API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>payment_split</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|payment_split|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = JSON with split type, <code>payuId</code>, and <code>splitInfo</code>.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:refund-status-api-for-split-payments">Refund Status API for Split Payments</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>aggregator_check_<br>action_status_<br>txnid</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|aggregator_check_action<br>_status_txnid|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = transaction ID or PayU ID to check.</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="ref:cancel-omnichannel-transaction-api-1">Cancel Omnichannel Transaction API</a></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>cancel_omni_payment</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>sha512(&lt;Your merchant key&gt;|cancel_omni_payment|&lt;value of var1 parameter&gt;|&lt;Your merchant salt&gt;)</code></p><p><em>var1</em> = PayU ID (<code>mihpayid</code>).</p></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

<br />

<br />