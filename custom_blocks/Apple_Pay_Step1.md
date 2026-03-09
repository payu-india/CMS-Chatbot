---
name: Apple_Pay_Step1
---
## Step 1: Initiate the payment to PayU

To initiate an Apple Pay payment, post the payment parameters to PayU's transaction endpoint.

| Environment | URL                                                                                                |
| :---------- | :------------------------------------------------------------------------------------------------- |
| Production  | [https://secure.payu.in/AuthorizeTransaction.php](https://secure.payu.in/AuthorizeTransaction.php) |

<Accordion title="Request parameters" icon="fa-table">
  \| Parameter                             | Description                                                                                                                                                                     | Example                                                                                                                       |   |   |
  \| :------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------- |
  \| key<br />`mandatory`                  | `String` - This parameter contains the merchant key provided by PayU during onboarding.                                                                                         | JP\*\*\*g                                                                                                                     |\
  \| txnid<br />`mandatory`                | `String` - This parameter contains a unique transaction ID. You can generate this ID or use the PayU API to generate it. The maximum length of this parameter is 25 characters. | txn\_applepay\_001                                                                                                            |\
  \| amount<br />`mandatory`               | `String` - This parameter contains the payment amount.                                                                                                                          | 100.00                                                                                                                        |\
  \| authentication\_info<br />`mandatory` | `String` - This parameter contains the authentication info as described in the (Authentication Info)\[#authentication-info] below this table.                                   | iPhone Case                                                                                                                   |\
  \| firstname<br />`mandatory`            | `String` - This parameter contains the first name of the customer.                                                                                                              | John                                                                                                                          |\
  \| email<br />`mandatory`                | `String` - This parameter contains the email address of the customer.                                                                                                           | [john@example.com](mailto:john@example.com)                                                                                   |\
  \| phone<br />`mandatory`                | `String` - This parameter contains the phone number of the customer.                                                                                                            | 9876543210                                                                                                                    |\
  \| pg<br />`mandatory`                   | `String` - This parameter specifies the payment category. For Apple Pay integration, the value must be `APPLEPAY`.                                                              | APPLEPAY     |
  \| bankcode<br />`mandatory`             | `String` - This parameter specifies the payment option. For Apple Pay integration, the value must be CCAP                                                                       | CCAP    |\
  \| address1<br />`mandatory`                 | `String` - This parameter must contain the address details of the customer.                                                     |                                                                  |\
  \| city<br />`mandatory`                 | `String` - This parameter must contain the city of tof the customer address.                                                     |                                                                  |\
  \| state<br />`mandatory`                 | `String` - This parameter must contain the state of tof the customer address.                                                     |                                                                  |\
  \| country<br />`mandatory`                 | `String` - This parameter must contain the country of tof the customer address.                                                     |                                                                  |\
  \| hash<br />`mandatory`                 | `String` - This parameter contains the hash value calculated using SHA-512 algorithm. Hash logic ensures the integrity of the transaction data.                                 | Refer to [Hashing sample code](https://docs.payu.in/docs/apple-pay-integration-merchant-hosted-checkout#/hashing-sample-code) |   |   |
  \| udf1<br />`optional`                  | `String` - This parameter must contain the Apple transaction identifier. Maximum length is 255 characters.                                                               |                                                                                                                               |\
  \| udf2<br />`optional`                  | `String` - This parameter must contain the value as MAST:credit. Maximum length is 255 characters.                                                               |                                                                                                                               |

  ### Authentication Info

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
