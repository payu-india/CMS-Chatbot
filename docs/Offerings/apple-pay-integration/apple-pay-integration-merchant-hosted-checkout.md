---
title: Apple Pay Integration-Merchant Hosted Checkout
deprecated: false
hidden: true
metadata:
  robots: index
---
This section describes step-by-step procedure to integrate Apple Pay as a payment method using Merchant Hosted Checkout integration with two kinds of decryption integration:

* (Merchant-side decryption)[#step-2a-merchant-side-decryption]
* (PayU-side decryption)[#step-2b-payu-side-decryption]

<Callout icon="📘" theme="info">
  **Before you begin**:   Ensure that you have completed the prerequisites before you start the integration. For more information, refer to [Prerequisites and Set up for Apple Pay Integration](doc:prerequisites-and-set-up-for-apple-pay-integration).
</Callout>

<Cards columns={3}>
  <Card title="1. Initiate the payment to PayU" href="https://docs.payu.in/docs/apple-pay-integration#step-1-initiate-the-payment-to-payu">
    Post the required parameters to PayU for Apple Pay integration

    <br />
  </Card>

  <Card title="2. Check response from PayU" href="https://docs.payu.in/docs/apple-pay-integration#step-2-check-response-from-payu">
    Check and handle the response received from PayU after posting parameters

    <br />
  </Card>

  <Card title="3. Verify the payment" href="https://docs.payu.in/docs/apple-pay-integration#step-3-verify-the-payment">
    Verify the payment status and ensure transaction completion
  </Card>
</Cards>

***

## Step 1: Authorize transaction

To initiate an Apple Pay payment, post the payment parameters to PayU's transaction endpoint.

| Environment | URL                                                                                                |
| :---------- | :------------------------------------------------------------------------------------------------- |
| Production  | [https://secure.payu.in/AuthorizeTransaction.php](https://secure.payu.in/AuthorizeTransaction.php) |

<Accordion title="Request parameters" icon="fa-table">
  Here is the corrected markdown table without the commenting, so it will display properly:

  | Parameter                             | Description                                                                                                                                                                                                                                                                                                | Example                                                                                                                       |
  | :------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
  | key<br />`mandatory`                  | `String` - This parameter contains the merchant key provided by PayU during onboarding.                                                                                                                                                                                                                    | JP\*\*\*g                                                                                                                     |
  | txnid<br />`mandatory`                | `String` - This parameter contains a unique transaction ID. You can generate this ID or use the PayU API to generate it. The maximum length of this parameter is 25 characters.                                                                                                                            | txn\_applepay\_001                                                                                                            |
  | amount<br />`mandatory`               | `String` - This parameter contains the payment amount.                                                                                                                                                                                                                                                     | 100.00                                                                                                                        |
  | authentication\_info<br />`mandatory` | `String` - This parameter contains the authentication info based on Merchant-side or PayU-side decryption. For more information, refer to any of the following: <br />    - (Merchant-side decryption)[#step-2a-merchant-side-decryption]<br />    - (PayU-side decryption)[#step-2b-payu-side-decryption] | iPhone Case                                                                                                                   |
  | firstname<br />`mandatory`            | `String` - This parameter contains the first name of the customer.                                                                                                                                                                                                                                         | John                                                                                                                          |
  | email<br />`mandatory`                | `String` - This parameter contains the email address of the customer.                                                                                                                                                                                                                                      | [john@example.com](mailto:john@example.com)                                                                                   |
  | phone<br />`mandatory`                | `String` - This parameter contains the phone number of the customer.                                                                                                                                                                                                                                       | 9876543210                                                                                                                    |
  | pg<br />`mandatory`                   | `String` - This parameter specifies the payment category. For Apple Pay integration, the value must be `APPLEPAY`.                                                                                                                                                                                         | APPLEPAY                                                                                                                      |
  | bankcode<br />`mandatory`             | `String` - This parameter specifies the payment option. For Apple Pay integration, the value must be CCAP                                                                                                                                                                                                  | CCAP                                                                                                                          |
  | address1<br />`mandatory`             | `String` - This parameter must contain the address details of the customer.                                                                                                                                                                                                                                |                                                                                                                               |
  | city<br />`mandatory`                 | `String` - This parameter must contain the city of the customer address.                                                                                                                                                                                                                                   |                                                                                                                               |
  | state<br />`mandatory`                | `String` - This parameter must contain the state of the customer address.                                                                                                                                                                                                                                  |                                                                                                                               |
  | country<br />`mandatory`              | `String` - This parameter must contain the country of the customer address.                                                                                                                                                                                                                                |                                                                                                                               |
  | hash<br />`mandatory`                 | `String` - This parameter contains the hash value calculated using SHA-512 algorithm. Hash logic ensures the integrity of the transaction data.                                                                                                                                                            | Refer to [Hashing sample code](https://docs.payu.in/docs/apple-pay-integration-merchant-hosted-checkout#/hashing-sample-code) |
  | udf1<br />`optional`                  | `String` - This parameter must contain the Apple transaction identifier. Maximum length is 255 characters.                                                                                                                                                                                                 |                                                                                                                               |
  | udf2<br />`optional`                  | `String` - This parameter must contain the value as MAST:credit. Maximum length is 255 characters.                                                                                                                                                                                                         |                                                                                                                               |

  <Accordion title="Understanding Hashing and sample code" icon="fa-code">
    <HashingRequestParameters />

    #### Hashing Sample Code

    <HashingSample />
  </Accordion>
</Accordion>

### Step 2a. Merchant-side Decryption

<Accordion title="Authentication info for Apple Pay" icon="fa-code">
  **Sample Authentication Info**

  ```
  {"applicationPrimaryAccountNumber":"4832086841071751","applicationExpirationDate":"290228","currencyCode":"356","transactionAmount":1000,"deviceManufacturerIdentifier":"040010030273","paymentDataType":"3DSecure","paymentData":{"onlinePaymentCryptogram":"KgAAAAoDK12xsrcAAAAAgTtgE4A=","eciIndicator":"5"}, "paymentMethod":{"displayName":"MasterCard 0049","network":"MasterCard","type":"credit"}}
  ```

  | Field                             | Description                                                                                                                                                                                                                                                                                |
  | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | `applicationPrimaryAccountNumber` | Tokenized Primary Account Number (FPAN). Device-specific token that replaces the real card number (DPAN). Format is card-like (e.g. 16 digits); last 4 may match the real card for display. Must not be stored as a card number; use only for the current transaction and token lifecycle. |
  | `applicationExpirationDate`       | Token expiration date in `YYMM` format (e.g. `290228` = February 28, 2029). Indicates when this payment token expires; distinct from the underlying card’s expiry.                                                                                                                         |
  | `currencyCode`                    | ISO 4217 numeric currency code (e.g. `356` = INR, `840` = USD). Must match the transaction currency.                                                                                                                                                                                       |
  | `transactionAmount`               | Transaction amount in minor units (e.g. paise for INR, cents for USD). Example: `1000` = ₹10.00 or $10.00 depending on `currencyCode`.                                                                                                                                                     |
  | `deviceManufacturerIdentifier`    | Device-specific identifier from the Secure Element. Used for risk, fraud, and token lifecycle (e.g. linking tokens to the same device). Opaque; format is manufacturer-specific.                                                                                                           |
  | `paymentDataType`                 | Type of cryptogram in `paymentData`. Common values: `3DSecure` (e-commerce/CNP), `EMV` (contactless CP), `ECv1` (legacy). Determines which cryptogram field to use and how to validate.                                                                                                    |
  | `paymentData`                     | Cryptogram and 3DS data used to authorize the transaction. Contents depend on `paymentDataType`.                                                                                                                                                                                           |
  | `paymentMethod`                   | Display and card-method metadata (network, type, display name). For UI and routing only; not used as primary authorization data.                                                                                                                                                           |

  #### paymentDat`object (when`paymentDataType`is`3DSecure\`)

  | Field                     | Description                                                                                                                                                                                                                                        |
  | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `onlinePaymentCryptogram` | One-time payment cryptogram (Base64). Generated by the device for this transaction; must be sent to the payment network/processor within its validity window. Used to prove that the transaction was authorized on the device.                     |
  | `eciIndicator`            | E-commerce Indicator (ECI). Indicates 3DS authentication level and liability shift. Common values: `05`/`06` = 3DS authenticated, `07` = 3DS attempted, `01`/`02` = not 3DS. Used by acquirers and schemes for authentication and liability rules. |

  ***

  #### paymentMethod object

  | Field         | Description                                                                                                                                                       |
  | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `displayName` | User-facing label for the card (e.g. “MasterCard 0049”). Often “Network” + last 4 digits. Safe for receipts and UI; must not be used as PAN or for authorization. |
  | `network`     | Card scheme/network (e.g. `MasterCard`, `Visa`, `AMEX`). Used for routing and scheme-specific handling.                                                           |
  | `type`        | Product type of the card: e.g. `credit`, `debit`, `prepaid`. Used for routing, compliance, and UX.                                                                |
</Accordion>

### Step 2b. PayU-side Decryption

<Accordion title="Authentication info for PayU-side Decryption" icon="fa-code">
  **Sample Authentication Info**

  ```json
  {
    "paymentData": {
      "data": "<Base64 encrypted payload>",
      "signature": "<Base64 PKCS#7 signature>",
      "header": {
        "publicKeyHash": "<Base64 SHA-256 hash>",
        "ephemeralPublicKey": "<Base64 EC P-256 public key>",
        "transactionId": "<hex string>"
      },
      "version": "EC_v1"
    },
    "paymentMethod": {
      "displayName": "Visa 7013",
      "network": "Visa",
      "type": "debit"
    },
    "transactionIdentifier": "<hex string>"
  }
  ```

  ### paymentData JSON object fields

  \| Field | Description |
  \|-------|------|-------------|
  \| `data`| **Encrypted payment data** (Base64). Symmetrically encrypted payload containing tokenized card and cryptogram data. Decryption key is derived using the merchant’s private key and `header.ephemeralPublicKey` (ECDH). Must be decrypted by the merchant/processor to obtain the payment token used for authorization. |
  \| `signature` | **PKCS#7 detached signature** (Base64). Contains Apple’s certificate chain and a signature over the payload. Used to verify that the token was issued by a valid Apple Pay environment and was not tampered with. |
  \| `header` | **Key agreement and transaction metadata.** Supplies the ephemeral public key for decryption and the transaction ID. |
  \| `version` | **Token format version.** Value `EC_v1` indicates EC-based key agreement and this encrypted structure. Determines how to parse and decrypt the token. |
  \| `header.publicKeyHash` | **Merchant certificate public key hash** (Base64, SHA-256). Identifies the merchant’s Apple Pay certificate used for this token. Used to select the correct private key for decryption and to verify the token was intended for this merchant. |
  \| `header.ephemeralPublicKey` | **Ephemeral EC P-256 public key** (Base64). Generated per transaction by the device. The merchant combines this with their private key (ECDH) to derive the symmetric key that decrypts `paymentData.data`. |
  \| `header.transactionId` | **Unique transaction identifier** (e.g. hex). Ties this token to a single transaction. Must match top-level `transactionIdentifier`; use for idempotency and audit. |

  ### paymentMethod JSON object

  \| Field  | Description |
  \|-------|------|-------------|
  \| `displayName` | **User-facing label** for the card (e.g. “Visa 7013”). Often “Network” + last 4 digits. Safe for receipts and UI; must not be used as PAN or for authorization. |
  \| `network`| **Card scheme/network** (e.g. `Visa`, `MasterCard`, `AMEX`). Used for routing and scheme-specific handling. |
  \| `type` | **Product type** of the card: e.g. `credit`, `debit`, `prepaid`. Used for routing, compliance, and UX. |
  |
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl --location 'https://secure.payu.in/AuthorizeTransaction.php' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key={{key}}' \
  --data-urlencode 'txnid={{txnid}}' \
  --data-urlencode 'authentication_info={{info}}' \
  --data-urlencode 'hash={{hash1}}' \
  --data-urlencode 'pg=ApplePay' \
  --data-urlencode 'bankcode=CCAP' \
  --data-urlencode 'firstname=John' \
  --data-urlencode 'country=IN' \
  --data-urlencode 'city=Banglore' \
  --data-urlencode 'state=KA' \
  --data-urlencode 'email=abc@gmail.com' \
  --data-urlencode 'address1=street1 area' \
  --data-urlencode 'udf1=appleTransactionIdentifier' \
  --data-urlencode 'udf2=MAST:credit' \
  --data-urlencode 'lastname=Bing' \
  --data-urlencode 'zipcode=45678' \
  --data-urlencode 'phone=9876543210' \
  --data-urlencode 'productinfo=ABC info' \
  --data-urlencode 'amount={{amt}}'
  ```

  <br />
</Accordion>

***

<br />

## Step 2: Check response from PayU

<Accordion title="Hash validation logic for payment response (Reverse Hashing)" icon="fa-shield">
  While sending the response, PayU takes the exact same parameters that were sent in the request (in reverse order) to calculate the hash and returns it to you. You must verify the hash and then mark a transaction as a success or failure. This is to make sure the transaction has not been tampered with in the response.

  The order of the parameters is similar to the following:

  ```
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```
</Accordion>

<Accordion title="Sample response (parsed)" icon="fa-file-code">
  ```php
  Array
  (
      [mihpayid] => 403993715524045752
      [mode] => APPLEPAY
      [status] => success
      [unmappedstatus] => captured
      [key] => JP***g
      [txnid] => txn_applepay_001
      [amount] => 100.00
      [discount] => 0.00
      [net_amount_debit] => 100
      [addedon] => 2024-01-15 10:30:00
      [productinfo] => iPhone Case
      [firstname] => John
      [lastname] => 
      [address1] => 
      [address2] => 
      [city] => 
      [state] => 
      [country] => 
      [zipcode] => 
      [email] => john@example.com
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
      [PG_TYPE] => APPLEPAY-PG
      [bank_ref_num] => 87d3b2a1-5a60-4169-8692-649f61923b3d
      [bankcode] => APPLEPAY
      [error] => E000
      [error_Message] => No Error
  )
  ```
</Accordion>

<Accordion title="Response parameters" icon="fa-table">
  | Parameter                           | Description                                                                                                                                | Example                                     |
  | :---------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------ |
  | mihpayid<br />`mandatory`           | `String` - This parameter contains the unique payment ID generated by PayU for this transaction.                                           | 403993715524045752                          |
  | mode<br />`mandatory`               | `String` - This parameter contains the payment mode used for the transaction. For Apple Pay, this value is `APPLEPAY`.                     | APPLEPAY                                    |
  | status<br />`mandatory`             | `String` - This parameter contains the status of the transaction. Possible values: `success`, `failure`, `pending`.                        | success                                     |
  | unmappedstatus<br />`mandatory`     | `String` - This parameter contains the detailed status of the transaction. Possible values: `captured`, `auth`, `bounced`, `dropped`, etc. | captured                                    |
  | key<br />`mandatory`                | `String` - This parameter contains the merchant key.                                                                                       | JP\*\*\*g                                   |
  | txnid<br />`mandatory`              | `String` - This parameter contains the transaction ID that was sent in the request.                                                        | txn\_applepay\_001                          |
  | amount<br />`mandatory`             | `String` - This parameter contains the transaction amount.                                                                                 | 100.00                                      |
  | discount<br />`optional`            | `String` - This parameter contains the discount amount applied to the transaction.                                                         | 0.00                                        |
  | net\_amount\_debit<br />`mandatory` | `String` - This parameter contains the net amount debited from the customer.                                                               | 100                                         |
  | addedon<br />`mandatory`            | `String` - This parameter contains the date and time when the transaction was added.                                                       | 2024-01-15 10:30:00                         |
  | productinfo<br />`mandatory`        | `String` - This parameter contains the product information sent in the request.                                                            | iPhone Case                                 |
  | firstname<br />`mandatory`          | `String` - This parameter contains the first name of the customer.                                                                         | John                                        |
  | email<br />`mandatory`              | `String` - This parameter contains the email address of the customer.                                                                      | [john@example.com](mailto:john@example.com) |
  | phone<br />`mandatory`              | `String` - This parameter contains the phone number of the customer.                                                                       | 9876543210                                  |
  | hash<br />`mandatory`               | `String` - This parameter contains the hash value returned by PayU. You must validate this hash to ensure the response integrity.          | 1be7e6e97...                                |
  | field9<br />`optional`              | `String` - This parameter contains additional information or error description returned by the bank or payment gateway.                    | Transaction Completed Successfully          |
  | payment\_source<br />`mandatory`    | `String` - This parameter contains the source of the payment.                                                                              | payu                                        |
  | PG\_TYPE<br />`mandatory`           | `String` - This parameter contains the type of payment gateway used. For Apple Pay, this value is `APPLEPAY-PG`.                           | APPLEPAY-PG                                 |
  | bank\_ref\_num<br />`mandatory`     | `String` - This parameter contains the reference number returned by the bank for this transaction.                                         | 87d3b2a1-5a60...                            |
  | bankcode<br />`mandatory`           | `String` - This parameter contains the bank code used for the transaction. For Apple Pay, this value is `APPLEPAY`.                        | APPLEPAY                                    |
  | error<br />`mandatory`              | `String` - This parameter contains the error code. `E000` indicates no error.                                                              | E000                                        |
  | error\_Message<br />`mandatory`     | `String` - This parameter contains the description of the error.                                                                           | No Error                                    |
</Accordion>

***

## Step 3: Verify the payment

<Verify_Payment_Tabs />
