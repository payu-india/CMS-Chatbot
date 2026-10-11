---
api:
  file: cards-si-api.yaml
  operationId: post_authorizetransaction-php
hidden: true
---
After the customer completes OTP authentication in [Step 1](doc:cards-si-step1-payment-authentication), the merchant receives a `bankData` JSON in the OTP submission response. This step passes that `bankData` augmented with `siTokenDetails` (network token details) — as `authentication_info` to the `AuthorizeTransaction` API to complete authorization and register the mandate.

<Callout icon="👍" theme="okay">
  ### **On Success**

  The response contains `IsStandingInstructionSet: "1"` confirming the mandate is registered. Save the `mihpayid` from the `result` object — this is the `authPayuId` you will use in all subsequent [Pre-Debit and Recurring Payments](doc:cards-si-pre-debit-recurring) calls.
</Callout>

<Callout icon="📘" theme="info">
  ### **Saved Card Flow**

  `siTokenDetails` is **optional** when authentication was done via PayU for a saved card (Flow 2 in Step 1).
</Callout>

***

## Environments

| Environment | URL                                               |
| :---------- | :------------------------------------------------ |
| Test        | `https://test.payu.in/AuthorizeTransaction.php`   |
| Production  | `https://secure.payu.in/AuthorizeTransaction.php` |

***

## Sample Request

<Tabs>
  <Tab title="Request Payload">
    ```curl
    curl --location 'https://test.payu.in/AuthorizeTransaction.php' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'key=vqpS7W' \
    --data-urlencode 'txnid=Txn080720261125' \
    --data-urlencode 'amount=100.00' \
    --data-urlencode 'hash=e7929823f663946bf9f54a68567901da847e505555e187412cf21a3d8e8fd18b6db1904442f62a07f77e74237398bcbf689353903415bb89d42c2ef0117fff88' \
    --data-urlencode 'authentication_info={"referenceId":"4e0d4a1b8f093f9bb03ed6e5605071b62ce39a9d136698d703862953a0106c24","cres":"eyJtZXNzYWdlVHlwZSI6IkNSZXMi...","additionalInfo":{"authUdf1":"","authUdf2":"","authUdf3":"","authUdf4":"","authUdf5":"","authUdf6":"","authUdf7":"","authUdf8":"","authUdf9":"","authUdf10":""},"siTokenDetails":{"token_exp_yr":"2029","token_exp_mon":"10","token_value":"6755390289370426","card_name":"test","tavv":"ADcBA4ZHFQAgJRImEjklAAAAAAE=","par":"PN07d26452cf9a1696e2744f470377ec48d5","last4digits":"2656"}}' \
    --data-urlencode 'si=1' \
    --data-urlencode 'si_details={"billingAmount":"200.00","billingCurrency":"INR","billingCycle":"ADHOC","billingInterval":1,"paymentStartDate":"2026-07-08","paymentEndDate":"2099-01-01"}'
    ```
  </Tab>

  <Tab title="Parameter Description">
    | Parameter                                | Description                                                                                                                                                                                                                                            |
    | :--------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `key` <br /> `mandatory`                 | `String` The merchant key generated from the PayU dashboard. For more information, refer to [Check your API Key and Salt](doc:check-api-key-and-salt). For example `vqpS7W`                                                                            |
    | `txnid` <br /> `mandatory`               | `String` The same transaction ID used in the `_payment` request (Step 1). For example `Txn080720261125`                                                                                                                                                |
    | `amount` <br /> `mandatory`              | `String` The same amount used in the `_payment` request. For example `100.00`                                                                                                                                                                          |
    | `hash` <br /> `mandatory`                | `String` SHA-512 hash for request integrity. Formula: <br /> `SHA512(key\|txnid\|amount\|authentication_info\|SALT)` <br /> **Important**: Use the exact serialised `authentication_info` JSON string (not the parsed object) when computing the hash. |
    | `authentication_info` <br /> `mandatory` | `JSON Object` The `bankData` JSON received after OTP submission, with `siTokenDetails` added. Must be serialised to a JSON string when submitted as a form field. See parameter breakdown below.                                                       |
    | `si` <br /> `mandatory`                  | `String` The value should be `1` to flag this as a Standing Instruction mandate creation transaction.                                                                                                                                                  |
    | `si_details` <br /> `mandatory`          | `JSON Object` Mandate billing parameters. Use the exact same values submitted in the Step 1 `_payment` request. For more information, refer to [SI Parameter JSON Details](ref:si-parameter-json-details).                                             |
  </Tab>
</Tabs>

### `authentication_info` Object Payload

<Tabs>
  <Tab title="Request Payload">
    The `authentication_info` field is the `bankData` JSON from the OTP response, with `siTokenDetails` added. The complete structure is as follows:

    ```json
    {
      "referenceId": "4e0d4a1b8f093f9bb03ed6e5605071b62ce39a9d136698d703862953a0106c24",
      "cres": "eyJtZXNzYWdlVHlwZSI6IkNSZXMiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMi4wIn0=",
      "additionalInfo": {
        "authUdf1": "",
        "authUdf2": "",
        "authUdf3": "",
        "authUdf4": "",
        "authUdf5": "",
        "authUdf6": "",
        "authUdf7": "",
        "authUdf8": "",
        "authUdf9": "",
        "authUdf10": ""
      },
      "siTokenDetails": {
        "token_exp_yr": "2029",
        "token_exp_mon": "10",
        "token_value": "6755390289370426",
        "card_name": "test",
        "tavv": "ADcBA4ZHFQAgJRImEjklAAAAAAE=",
        "par": "PN07d26452cf9a1696e2744f470377ec48d5",
        "last4digits": "2656"
      }
    }
    ```
  </Tab>

  <Tab title="Parameter Description">
    | Field                                             | Description                                                                                                                                                                     |
    | :------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | `referenceId` <br /> `mandatory`                  | `String` PayU reference ID from the `_payment` authentication response (`metaData.referenceId`). For example `4e0d4a1b8f093f9bb03ed6e5605071b62ce39a9d136698d703862953a0106c24` |
    | `cres` <br /> `mandatory`                         | `String` Base64-encoded 3DS CRes (Challenge Response) message returned by the ACS after OTP submission.                                                                         |
    | `additionalInfo` <br /> `mandatory`               | `JSON Object` User-defined authentication fields (`authUdf1` through `authUdf10`). Pass as empty strings if not used.                                                           |
    | `siTokenDetails.token_exp_yr` <br /> `mandatory`  | `String` Network token expiry year (4 digits). For example `2029`                                                                                                               |
    | `siTokenDetails.token_exp_mon` <br /> `mandatory` | `String` Network token expiry month (2 digits). For example `10`                                                                                                                |
    | `siTokenDetails.token_value` <br /> `mandatory`   | `String` The network token value returned after successful tokenisation. For example `6755390289370426`.                                                                        |
    | `siTokenDetails.card_name` <br /> `mandatory`     | `String` Cardholder name associated with the token. For example `test`.                                                                                                         |
    | `siTokenDetails.tavv` <br /> `mandatory`          | `String` Token Authentication Verification Value (cryptogram) from the network/scheme. For example `ADcBA4ZHFQAgJRImEjklAAAAAAE`.                                               |
    | `siTokenDetails.par` <br /> `mandatory`           | `String` Payment Account Reference assigned by the network. For example `PN07d26452cf9a1696e2744f470377ec48d5`.                                                                 |
    | `siTokenDetails.last4digits` <br /> `mandatory`   | `String` Last 4 digits of the tokenised card. For example `2656`.                                                                                                               |
  </Tab>
</Tabs>
