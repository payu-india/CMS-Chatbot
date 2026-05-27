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

## Hash Generation Logic for General Command-based APIs

> 📘 Notes
>
> - **Test endpoint:** `https://test.payu.in/merchant/postservice` (typically with `?form=2` for JSON responses).
> - For most command-based postservice APIs, PayU uses `sha512(key|command|var1|salt)`. Regenerate the hash whenever request parameters change. See [REST API Format](docs/API basics/rest-api-format.md) and [API Authentication and Security](/docs/api-authentication-and-security).


| API | command | Hash logic |
| --- | --- | --- |
| [Verify Payment API](ref:verify_payment_api) | `verify_payment` | Hash formula: `sha512(key\|command\|var1\|salt)` |
| [Get Transaction Details API](ref:get_transaction_details_api) | `get_Transaction_Details` | Hash logic for this API is: `sha512(key\|command\|var1\|salt)` sha512 |
| [Get Transaction Info API](ref:get_transaction_info_api) | `get_transaction_info` | The string used for calculating the hash is in the following format: `sha512(key\|command\|var1\|salt)` sha512 |
| [Get TDR API](ref:get_tdr_api) | `get_TDR` | Hash formula: `sha512(key\|command\|var1\|salt)` |
| [Refund Transaction API](ref:refund_transaction_api) | `cancel_refund<br/>_transaction` | Calculated using the sha512 algorithm with the format: `sha512(key\|command\|var1\|salt)` |
| [Get All Refunds from Transaction ID](ref:get_all_refunds_from_transaction_ids_api) | `getAllRefunds<br/>FromTxnIds` | Calculated using the sha512 algorithm with the format: `sha512(key\|command\|var1\|salt)` |
| [Check Action Status with PayU ID](ref:check_action_status_api_with_payu_id) | `check_action_status` | Hash logic for this API is: `sha512(key\|command\|var1\|salt)` sha512 |
| [Check Refund Status with Request ID API](ref:check_action_status_api_with_request_id) | `check_action_status<br/>_txnid` | Calculated using the sha512 algorithm with the format: `sha512(key\|command\|var1\|salt)` |
| [Check is Domestic API](ref:check_is_domestic_api) | `check_isDomestic` | Hash logic: `sha512(key\|command\|var1\|salt)` |
| [Get BIN Info API](ref:get_bin_info_api) | `getBinInfo` | Hash logic for this API is: `sha512(key\|command\|var1\|salt)` sha512 |
| [Get EMI Amount according to Interest API](ref:get_emi_according_to_interest_api) | `getEmiAmountAccording<br/>ToInterest` | Hash logic for this API is: `sha512(key\|command\|var1\|salt)` sha512 |
| [Get Issuing Bank Status API](ref:get_issuing_bank_status_api) | `getIssuing<br/>BankStatus` | Hash logic for this API is: `sha512(key\|command\|var1\|salt)` sha512 |
| [Get Issuing Bank Down BINs API](ref:get_issuing_bank_down_bins_api) | `getIssuing<br/>BankDownBins` | Hash formula: `sha512(key\|command\|var1\|salt)` |
| [Get Net Banking Status API](ref:get_net_banking_status_api) | `getNetbankingStatus` | Hash formula: `sha512(key\|command\|var1\|salt)` |
| [Get Checkout Details API](ref:get_checkout_details) | `get_checkout<br/>_details` | `hash = sha512(key\|command\|var1\|SALT)` |
| [Get Checkout Details – NTB Seamless Journey](ref:get-checkout-details-ntb-seamless-journey) | `get_checkout_details` | `sha512(key\|command\|var1\|salt)` (see sample request hash field) |
| [Check Offer Status API](ref:check-offer-status-api) | `check_offer_status` | For command-based General APIs: `sha512(key\|command\|var1\|salt)` — sha512 is the encryption method used |
| [Fetch Balance API (Sodexo)](ref:fetch-balance-api-sodexo) | `check_balance` | `sha512(key\|command\|var1\|salt)` sha512 |
| [Fetch Balance API (Open Loop Wallet)](ref:fetch-balance-api) | `check_balance` | `sha512(key\|command\|var1\|salt)` sha512 |
| [Release Settlement API](ref:release_settlement_api) | `release_settlement` | The format of the hash is: `key\|command\|var1\|salt` (Where var1 is your mihpayuid) |
| [Get Settlement Detail API (Cross-Border)](ref:get-settlement-detail-api-cross-border-payments) | `get_settlement_details` | Postservice sample uses `hash` with `command=get_settlement_details`; for General APIs use `sha512(key\|command\|var1\|salt)`. Treasury endpoint uses separate HMAC authorization — see API reference. |
| [UDF Update API](ref:udf_update_api) | `udf_update` | `hash = sha512(key\|command\|var1\|salt)` |
| [Recurring Payment Transaction API](ref:recurring_payment_api) | `si_transaction` | Hash logic for this API is: `sha512(key\|command\|var1\|salt)` sha512 |
| [SI Transaction API](ref:si-transaction-api-parallel-sequencing) | `si_transaction` | Hash logic for this API is: `sha512(key\|command\|var1\|salt)` sha512 |
| [Recurring Payment Transaction API – PACB](ref:recurring-payment-transaction-api-pacb) | `si_transaction` | SHA512 hash: `sha512(key\|command\|var1\|salt)` |
| [Pre-Debit Notification API](ref:pre_debit_notification_api) | `pre_debit_SI` | Hash formula: `sha512(key\|command\|var1\|salt)` |
| [Validate VPA API](ref:validate_vpa_api) | `validateVPA` | Hash logic for this API is: `sha512(key\|command\|var1\|salt)` sha512 |
| [Check the Mandate Status](ref:check-the-mandate-status) | `check_mandate_status` | `hash = sha512(key\|command\|var1\|SALT)` |
| [Check Net Banking Mandate Status API](ref:net_banking_mandate_status_api) | `NB_mandate_status` | `hash = sha512(key\|command\|var1\|SALT)` |
| [Cancel Recurring Payment (Cards)](ref:cancel-the-recurring-payment-for-cards) | `mandate_revoke` | `hash = sha512(key\|command\|var1\|SALT)` |
| [Cancel Recurring Payment (Net Banking)](ref:cancel-the-recurring-payment-for-net-banking) | `mandate_revoke` | `hash = sha512(key\|command\|var1\|SALT)` |
| [Cancel Recurring Payment (UPI)](ref:cancel-the-recurring-payment-for-upi) | `upi_mandate_revoke` | 512 SHA hash strings generated by encrypting request parameters (use subscription API hash pattern: `hash = sha512(key\|command\|var1\|SALT)`) |
| [Get User Cards API (Model 2)](ref:get_user_cards_api) | `get_user_cards` | The hash is calculated using the following logic: `sha512 (key\|command\|var1\|salt)` sha512 |
| [Get User Cards API – Model 3](ref:get_user_cards_api_model3) | `get_payment_instrument` | The hash is calculated using the following logic: `sha512 (key\|command\|var1\|salt)` sha512 |
| [Tokenize a Card API](ref:save_card_api) | `save_payment<br/>_instrument` | Hash logic for this API is: `sha512(key\|command\|var1\|salt)` sha512 |
| [Edit a Saved Card API](ref:edit_saved_card_api) | `edit_payment_instrument` | Hash logic for this API is: `sha512(key\|command\|var1\|salt)` sha512 |
| [Collect Payments – Save Card](ref:collect-payments-save-card) | `get_user_cards` | The hash is calculated using the following logic: `sha512 (key\|command\|var1\|salt)` sha512 |
| [Get Split Info API](ref:get_split_info_api) | `get_split_info` | `sha512(key\|command\|payuId\|salt)` sha512 |
| [Split After Transaction API](ref:split_after<br/>_transaction_api) | `payment_split` | The format of the hash is: `sha512(key\|command\|var1\|salt)` (Where var1 contains the fields as described in the var1 description) |
| [Refund Status API for Split Payments](ref:refund-status-api-for-split-payments) | `aggregator_check<br/>_action_status<br/>_txnid` | `sha512(key\|command\|var1\|salt)` — sha512 is the encryption method used here |
| [Cancel Omnichannel Transaction API](ref:cancel-omnichannel-transaction-api-1) | `cancel_omni_payment` | The string used for calculating the hash is mentioned below: `sha512(key\|command\|var1\|salt)` |