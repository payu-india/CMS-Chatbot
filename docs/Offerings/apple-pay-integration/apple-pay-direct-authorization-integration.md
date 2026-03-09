---
title: Apple Pay - Direct Authorization Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
This section provides a comprehensive guide for integrating Apple Pay Seamless Flow with PayU's Server-to-Server (S2S) Direct Authorization using `txn_s2s_flow=3`. This approach enables direct authorization of pre-authenticated Apple Pay transactions through server-to-server communication.

## Understanding S2S Direct Authorization Flow

### Key Characteristics of txn_s2s_flow=3

* **Direct Authorization**: Process pre-authenticated transactions
* **3DS Support**: Handle 3DS/3DS2 authentication data
* **Server-to-Server**: No browser redirects required
* **Real-time Response**: Immediate authorization results

### Flow Sequence

1. Merchant receives Apple Pay token with authentication data
2. Extract 3DS authentication information from Apple Pay token
3. Prepare Direct Authorization request with `txn_s2s_flow=3`
4. Send authorization request to PayU
5. Receive base64-encoded response
6. Decode and verify response hash
7. Process authorization result

## Step 1: Initiate Payment Session

Initiate the payment session similar to the following cURL request:

```curl
curl --location 'https://secure.payu.in/seamless/Session' \
--header 'Content-Type: application/json' \
--header 'mid: 2' \
--data '{
    "validationUrl": "https://apple-pay-gateway.apple.com/paymentservices/paymentSession",
    "txnid": "06fb0aa23eaeb32772e18"
  }'
```

## Step 2: Authorize Transaction

To initiate an Apple Pay payment, post the payment parameters to PayU's transaction endpoint.

| Environment | URL                                                                                                |
| :---------- | :------------------------------------------------------------------------------------------------- |
| Production  | [https://secure.payu.in/AuthorizeTransaction.php](https://secure.payu.in/AuthorizeTransaction.php) |

<Accordion title="Request parameters" icon="fa-table">
  Here is the corrected markdown table without the commenting, so it will display properly:

  | Parameter                             | Description                                                                                                                                                                     | Example                                                                                                                       |
  | :------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------- |
  | key<br />`mandatory`                  | `String` - This parameter contains the merchant key provided by PayU during onboarding.                                                                                         | JP\*\*\*g                                                                                                                     |
  | txnid<br />`mandatory`                | `String` - This parameter contains a unique transaction ID. You can generate this ID or use the PayU API to generate it. The maximum length of this parameter is 25 characters. | txn\_applepay\_001                                                                                                            |
  | amount<br />`mandatory`               | `String` - This parameter contains the payment amount.                                                                                                                          | 100.00                                                                                                                        |
  | authentication\_info<br />`mandatory` | `String` - This parameter contains the authentication info as described in the (Authentication Info)\[#authentication-info] below this table.                                   | iPhone Case                                                                                                                   |
  | firstname<br />`mandatory`            | `String` - This parameter contains the first name of the customer.                                                                                                              | John                                                                                                                          |
  | email<br />`mandatory`                | `String` - This parameter contains the email address of the customer.                                                                                                           | [john@example.com](mailto:john@example.com)                                                                                   |
  | phone<br />`mandatory`                | `String` - This parameter contains the phone number of the customer.                                                                                                            | 9876543210                                                                                                                    |
  | pg<br />`mandatory`                   | `String` - This parameter specifies the payment category. For Apple Pay integration, the value must be `APPLEPAY`.                                                              | APPLEPAY                                                                                                                      |
  | bankcode<br />`mandatory`             | `String` - This parameter specifies the payment option. For Apple Pay integration, the value must be CCAP                                                                       | CCAP                                                                                                                          |
  | address1<br />`mandatory`             | `String` - This parameter must contain the address details of the customer.                                                                                                     |                                                                                                                               |
  | city<br />`mandatory`                 | `String` - This parameter must contain the city of the customer address.                                                                                                        |                                                                                                                               |
  | state<br />`mandatory`                | `String` - This parameter must contain the state of the customer address.                                                                                                       |                                                                                                                               |
  | country<br />`mandatory`              | `String` - This parameter must contain the country of the customer address.                                                                                                     |                                                                                                                               |
  | hash<br />`mandatory`                 | `String` - This parameter contains the hash value calculated using SHA-512 algorithm. Hash logic ensures the integrity of the transaction data.                                 | Refer to [Hashing sample code](https://docs.payu.in/docs/apple-pay-integration-merchant-hosted-checkout#/hashing-sample-code) |
  | udf1<br />`optional`                  | `String` - This parameter must contain the Apple transaction identifier. Maximum length is 255 characters.                                                                      |                                                                                                                               |
  | udf2<br />`optional`                  | `String` - This parameter must contain the value as MAST:credit. Maximum length is 255 characters.                                                                              |                                                                                                                               |

  ### Authentication Info

  <Accordion title="Authentication info for Apple Pay" icon="fa-code">
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

| Field | Description |
|-------|------|-------------|
| `data`| **Encrypted payment data** (Base64). Symmetrically encrypted payload containing tokenized card and cryptogram data. Decryption key is derived using the merchant’s private key and `header.ephemeralPublicKey` (ECDH). Must be decrypted by the merchant/processor to obtain the payment token used for authorization. |
| `signature` | **PKCS#7 detached signature** (Base64). Contains Apple’s certificate chain and a signature over the payload. Used to verify that the token was issued by a valid Apple Pay environment and was not tampered with. |
| `header` | **Key agreement and transaction metadata.** Supplies the ephemeral public key for decryption and the transaction ID. |
| `version` | **Token format version.** Value `EC_v1` indicates EC-based key agreement and this encrypted structure. Determines how to parse and decrypt the token. |
| `header.publicKeyHash` | **Merchant certificate public key hash** (Base64, SHA-256). Identifies the merchant’s Apple Pay certificate used for this token. Used to select the correct private key for decryption and to verify the token was intended for this merchant. |
| `header.ephemeralPublicKey` | **Ephemeral EC P-256 public key** (Base64). Generated per transaction by the device. The merchant combines this with their private key (ECDH) to derive the symmetric key that decrypts `paymentData.data`. |
| `header.transactionId` | **Unique transaction identifier** (e.g. hex). Ties this token to a single transaction. Must match top-level `transactionIdentifier`; use for idempotency and audit. |

### paymentMethod JSON object 

| Field  | Description |
|-------|------|-------------|
| `displayName` | **User-facing label** for the card (e.g. “Visa 7013”). Often “Network” + last 4 digits. Safe for receipts and UI; must not be used as PAN or for authorization. |
| `network`| **Card scheme/network** (e.g. `Visa`, `MasterCard`, `AMEX`). Used for routing and scheme-specific handling. |
| `type` | **Product type** of the card: e.g. `credit`, `debit`, `prepaid`. Used for routing, compliance, and UX. |
                                                                |
  </Accordion>

  <Accordion title="Understanding Hashing and sample code" icon="fa-code">
    <HashingRequestParameters />

    #### Hashing Sample Code

    <HashingSample />
  </Accordion>
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

## Step 3: Check Response from PayU

The Direct Authorization API returns a **base64-encoded** response that needs to be decoded:

```json
{
  "status": "success",
  "result": {
    "mihpayid": "403993715527623137",
    "mode": "APPLEPAY",
    "status": "success",
    "key": "your_merchant_key",
    "txnid": "APPLEPAY_DA_1703845200_a1b2c3d4", 
    "amount": "100.00",
    "addedon": "2023-12-29 10:30:00",
    "productinfo": "Apple Pay Direct Authorization",
    "firstname": "John",
    "lastname": "",
    "email": "john@example.com",
    "phone": "9876543210",
    "udf1": "",
    "udf2": "",
    "udf3": "",
    "udf4": "",
    "udf5": "",
    "card_no": "XXXXXXXXXXXX1111",
    "card_token": "token_value",
    "net_amount_debit": "100.00",
    "discount": "0.00",
    "unmappedstatus": "captured",
    "payment_source": "dirAuthS2S",
    "PG_TYPE": "APPLEPAY-PG",
    "error": "No Error",
    "error_Message": "",
    "bank_ref_no": "AP123456789",
    "bankcode": "CCAP",
    "card_hash": "hash_value",
    "hash": "response_hash"
  }
}
```

## Step 4: Verify the Payment

<Verify_Payment_Tabs />
