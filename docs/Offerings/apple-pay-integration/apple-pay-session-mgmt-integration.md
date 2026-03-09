---
title: Apple Pay - Merchant Hosted with Session Management Integration
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
This section provides a comprehensive guide for integrating Apple Pay Seamless Flow with session management.

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

<Accordion title="Sample response" icon="fa-reply">
  ```json
  "{"statusMessage":null,"statusCode":null,"epochTimestamp":1764929571691,"expiresAt":1764933171691,"merchantSessionIdentifier":"SSH3552B208B665452DAF7A7739458184B5_916523AAED1343F5BC5815E12BEE9250AFFDC1A17C46B0DE5A943F0F94927C24","nonce":"e5b3d507","merchantIdentifier":"D862D24F557AE4DF8BE42CAEE0915227377AA9FD2FBE7F9A098BB1306EA15622","domainName":"api.payu.in","displayName":"Test Merchant 180012","signature":"308006092a864886f70d010702a0803080020101310d300b0609608648016503040201308006092a864886f70d0107010000a080308203e43082038ba003020102020859d8a1bcaaf4e3cd300a06082a8648ce3d040302307a312e302c06035504030c254170706c65204170706c69636174696f6e20496e746567726174696f6e204341202d20473331263024060355040b0c1d4170706c652043657274696669636174696f6e20417574686f7269747931133011060355040a0c0a4170706c6520496e632e310b3009060355040613025553301e170d3231303432303139333730305a170d3236303431393139333635395a30623128302606035504030c1f6563632d736d702d62726f6b65722d7369676e5f5543342d53414e44424f5831143012060355040b0c0b694f532053797374656d7331133011060355040a0c0a4170706c6520496e632e310b30090603550406130255533059301306072a8648ce3d020106082a8648ce3d030107034200048230fdabc39cf75e202c50d99b4512e637e2a901dd6cb3e0b1cd4b526798f8cf4ebde81a25a8c21e4c33ddce8e2a96c2f6afa1930345c4e87a4426ce951b1295a38202113082020d300c0603551d130101ff04023000301f0603551d2304183016801423f249c44f93e4ef27e6c4f6286c3fa2bbfd2e4b304506082b0601050507010104393037303506082b060105050730018629687474703a2f2f6f6373702e6170706c652e636f6d2f6f63737030342d6170706c65616963613330323082011d0603551d2004820114308201103082010c06092a864886f7636405013081fe3081c306082b060105050702023081b60c81b352656c69616e6365206f6e207468697320636572746966696361746520627920616e7920706172747920617373756d657320616363657074616e6365206f6620746865207468656e206170706c696361626c65207374616e64617264207465726d7320616e6420636f6e646974696f6e73206f66207573652c20636572746966696361746520706f6c69637920616e642063657274696669636174696f6e2070726163746963652073746174656d656e74732e303606082b06010505070201162a687474703a2f2f7777772e6170706c652e636f6d2f6365727469666963617465617574686f726974792f30340603551d1f042d302b3029a027a0258623687474703a2f2f63726c2e6170706c652e636f6d2f6170706c6561696361332e63726c301d0603551d0e041604140224300b9aeeed463197a4a65a299e4271821c45300e0603551d0f0101ff040403020780300f06092a864886f76364061d04020500300a06082a8648ce3d0403020347003044022074a1b324db4249430dd3274c5074c4808d9a1f480e3a85c5c1362566325fbca3022069369053abf50b5a52f9f6004dc58aad6c50a7d608683790e0a73ad01e4ad981308202ee30820275a0030201020208496d2fbf3a98da97300a06082a8648ce3d0403023067311b301906035504030c124170706c6520526f6f74204341202d20473331263024060355040b0c1d4170706c652043657274696669636174696f6e20417574686f7269747931133011060355040a0c0a4170706c6520496e632e310b3009060355040613025553301e170d3134303530363233343633305a170d3239303530363233343633305a307a312e302c06035504030c254170706c65204170706c69636174696f6e20496e746567726174696f6e204341202d20473331263024060355040b0c1d4170706c652043657274696669636174696f6e20417574686f7269747931133011060355040a0c0a4170706c6520496e632e310b30090603550406130255533059301306072a8648ce3d020106082a8648ce3d03010703420004f017118419d76485d51a5e25810776e880a2efde7bae4de08dfc4b93e13356d5665b35ae22d097760d224e7bba08fd7617ce88cb76bb6670bec8e82984ff5445a381f73081f4304606082b06010505070101043a3038303606082b06010505073001862a687474703a2f2f6f6373702e6170706c652e636f6d2f6f63737030342d6170706c65726f6f7463616733301d0603551d0e0416041423f249c44f93e4ef27e6c4f6286c3fa2bbfd2e4b300f0603551d130101ff040530030101ff301f0603551d23041830168014bbb0dea15833889aa48a99debebdebafdacb24ab30370603551d1f0430302e302ca02aa0288626687474703a2f2f63726c2e6170706c652e636f6d2f6170706c65726f6f74636167332e63726c300e0603551d0f0101ff0404030201063010060a2a864886f7636406020e04020500300a06082a8648ce3d040302036700306402303acf7283511699b186fb35c356ca62bff417edd90f754da28ebef19c815e42b789f898f79b599f98d5410d8f9de9c2fe0230322dd54421b0a305776c5df3383b9067fd177c2c216d964fc6726982126f54f87a7d1b99cb9b0989216106990f09921d00003182018730820183020101308186307a312e302c06035504030c254170706c65204170706c69636174696f6e20496e746567726174696f6e204341202d20473331263024060355040b0c1d4170706c652043657274696669636174696f6e20417574686f7269747931133011060355040a0c0a4170706c6520496e632e310b3009060355040613025553020859d8a1bcaaf4e3cd300b0609608648016503040201a08193301806092a864886f70d010903310b06092a864886f70d010701301c06092a864886f70d010905310f170d3235313230353130313235315a302806092a864886f70d010934311b3019300b0609608648016503040201a10a06082a8648ce3d040302302f06092a864886f70d01090431220420165f0c6a1f054d36ee3ca6d31dd3b832274c4dac948ef09786fa881b378fc280300a06082a8648ce3d0403020446304402200767e7382304ff161cea67201af176592e7e10feb8f2ce4fd180d10c51dc893b02203dee78e49104d3ab340e25edb893cb846542bf1f9431c09fd57d6726bb796be7000000000000","operationalAnalyticsIdentifier":"Test Merchant 180012:D862D24F557AE4DF8BE42CAEE0915227377AA9FD2FBE7F9A098BB1306EA15622","retries":0,"pspId":"13904BBF0C62E35A2A6FA715075EE113BE3B9EE8265332B11313D49287304602"}"
  ```
</Accordion>

## Step 2: Authorize Transaction

To initiate an Apple Pay payment, post the payment parameters to PayU's transaction endpoint.

| Environment | URL                                                                                                |
| :---------- | :------------------------------------------------------------------------------------------------- |
| Production  | [https://secure.payu.in/AuthorizeTransaction.php](https://secure.payu.in/AuthorizeTransaction.php) |

<Accordion title="Request parameters" icon="fa-table">
  | Parameter                             | Description                                                                                                                     | Example                                     |
  | :------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------ |
  | key<br />`mandatory`                  | `String` – Merchant key provided by PayU during onboarding.                                                                     | JP\*\*\*g                                   |
  | txnid<br />`mandatory`                | `String` – Unique transaction ID (max 25 chars). Can be generated by merchant or PayU API.                                      | txn\_applepay\_001                          |
  | amount<br />`mandatory`               | `String` – Payment amount.                                                                                                      | 100.00                                      |
  | authentication\_info<br />`mandatory` | `String` – Authentication info as described in #authentication-info.                                                            | iPhone Case                                 |
  | firstname<br />`mandatory`            | `String` – Customer’s first name.                                                                                               | John                                        |
  | email<br />`mandatory`                | `String` – Customer’s email address.                                                                                            | [john@example.com](mailto:john@example.com) |
  | phone<br />`mandatory`                | `String` – Customer’s phone number.                                                                                             | 9876543210                                  |
  | pg<br />`mandatory`                   | `String` – Payment category. Must be `APPLEPAY` for Apple Pay integration.                                                      | APPLEPAY                                    |
  | bankcode<br />`mandatory`             | `String` – Payment option. Must be `CCAP` for Apple Pay.                                                                        | CCAP                                        |
  | address1<br />`mandatory`             | `String` – Customer address line 1.                                                                                             |                                             |
  | city<br />`mandatory`                 | `String` – Customer city.                                                                                                       |                                             |
  | state<br />`mandatory`                | `String` – Customer state.                                                                                                      |                                             |
  | country<br />`mandatory`              | `String` – Customer country.                                                                                                    |                                             |
  | hash<br />`mandatory`                 | `String` – SHA-512 hash ensuring transaction integrity. Uses the following logic:<br />`sha[key\\|txnid\\|amt\\|info\\|salt]` |                                             |
  | udf1<br />`optional`                  | `String` – Apple transaction identifier (max 255 chars).                                                                        |                                             |
  | udf2<br />`optional`                  | `String` – Should contain the value `MAST:credit` (max 255 chars).                                                              |                                             |
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

  <Callout icon="📘" theme="info">
    **Note**:  You will receive the following JSON on your registered domain from Apple Pay.
  </Callout>

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

  ### paymentData JSON object fields description

  | Field                       | Description                                                                                                                                                                                                                                                                                                            |
  | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `data`                      | **Encrypted payment data** (Base64). Symmetrically encrypted payload containing tokenized card and cryptogram data. Decryption key is derived using the merchant’s private key and `header.ephemeralPublicKey` (ECDH). Must be decrypted by the merchant/processor to obtain the payment token used for authorization. |
  | `signature`                 | **PKCS#7 detached signature** (Base64). Contains Apple’s certificate chain and a signature over the payload. Used to verify that the token was issued by a valid Apple Pay environment and was not tampered with.                                                                                                      |
  | `header`                    | **Key agreement and transaction metadata.** Supplies the ephemeral public key for decryption and the transaction ID.                                                                                                                                                                                                   |
  | `version`                   | **Token format version.** Value `EC_v1` indicates EC-based key agreement and this encrypted structure. Determines how to parse and decrypt the token.                                                                                                                                                                  |
  | `header.publicKeyHash`      | **Merchant certificate public key hash** (Base64, SHA-256). Identifies the merchant’s Apple Pay certificate used for this token. Used to select the correct private key for decryption and to verify the token was intended for this merchant.                                                                         |
  | `header.ephemeralPublicKey` | **Ephemeral EC P-256 public key** (Base64). Generated per transaction by the device. The merchant combines this with their private key (ECDH) to derive the symmetric key that decrypts `paymentData.data`.                                                                                                            |
  | `header.transactionId`      | **Unique transaction identifier** (e.g., hex). Ties this token to a single transaction. Must match top-level `transactionIdentifier`; use for idempotency and audit.                                                                                                                                                   |

  ### paymentMethod JSON object fields description

  | Field         | Description                                                                                                                                                      |
  | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `displayName` | **User-facing label** for the card (e.g., “Visa 7013”). Often “Network” + last 4 digits. Safe for receipts and UI; must not be used as PAN or for authorization. |
  | `network`     | **Card scheme/network** (e.g., `Visa`, `MasterCard`, `AMEX`). Used for routing and scheme‑specific handling.                                                     |
  | `type`        | **Product type** of the card: e.g., `credit`, `debit`, `prepaid`. Used for routing, compliance, and UX.                                                          |
</Accordion>

***

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
