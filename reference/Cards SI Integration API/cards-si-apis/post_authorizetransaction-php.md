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

## Sample Response

<Tabs>
  <Tab title="Response Payload">
    A successful response includes `IsStandingInstructionSet: "1"` in the `result` object, confirming mandate registration.

    ```json
    {
        "metaData": {
          "message": "No Error",
          "referenceId": "4e0d4a1b8f093f9bb03ed6e5605071b62ce39a9d136698d703862953a0106c24",
          "statusCode": "E000",
          "txnId": "Txn080720261125",
          "unmappedStatus": "success",
          "submitOtp": {
            "status": "success"
          }
        },
        "result": {
          "mihpayid": "403993715537854394",
          "mode": "CC",
          "status": "success",
          "key": "vqpS7W",
          "txnid": "Txn080720261125",
          "amount": "100.00",
          "addedon": "2026-07-08 11:26:39",
          "productinfo": "iPhone",
          "firstname": "Test User",
          "card_no": "XXXXXXXXXXXX1258",
          "error": "E000",
          "error_Message": "No Error",
          "issuing_bank": "YES",
          "card_type": "VISA",
          "AcqTID": "PAYUPAYMENTCYBS",
          "AcqName": "AxisCYBER",
          "AuthCode": "506907",
          "net_amount_debit": "100",
          "bank_ref_no": "295522556067763300",
          "bankcode": "CC",
          "PG_TYPE": "CC-PG",
          "IsStandingInstructionSet": "1",
          "payment_source": "sist",
          "hash": "5d7a542fcd45146b9bfb..."
        }
      }
    ```
  </Tab>

  <Tab title="Parameter Description">
    | Parameter                         | Description                                                                                                                                          |
    | :-------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `metaData.message`                | `string` Human-readable status message from the authentication layer. `No Error` on success.                                                         |
    | `metaData.referenceId`            | `string` PayU reference ID echoed from the request. Use this to correlate the response with the original `_payment` call.                            |
    | `metaData.statusCode`             | `string` Authentication status code. `E000` indicates success.                                                                                       |
    | `metaData.txnId`                  | `string` Merchant transaction ID echoed from the request.                                                                                            |
    | `metaData.unmappedStatus`         | `string` Raw authentication status string. `success` on mandate registration.                                                                        |
    | `metaData.submitOtp.status`       | `string` Status of the OTP submission step. `success` confirms the ACS challenge was completed.                                                      |
    | `result.mihpayid`                 | `string` PayU's unique transaction identifier. **Save this as&#x20;**`authPayuId` — required for all subsequent pre-debit and recurring debit calls. |
    | `result.mode`                     | `string` Payment mode used. `CC` = Credit Card, `DC` = Debit Card.                                                                                   |
    | `result.status`                   | `string` Overall transaction status. `success` = mandate registered.                                                                                 |
    | `result.key`                      | `string` Merchant key echoed from the request.                                                                                                       |
    | `result.txnid`                    | `string` Merchant transaction ID echoed from the request.                                                                                            |
    | `result.amount`                   | `string` Transaction amount echoed from the request.                                                                                                 |
    | `result.addedon`                  | `string` Timestamp when the transaction was created on PayU (IST, `YYYY-MM-DD HH:MM:SS`).                                                            |
    | `result.productinfo`              | `string` Product description echoed from the `_payment` request.                                                                                     |
    | `result.firstname`                | `string` Customer first name echoed from the `_payment` request.                                                                                     |
    | `result.card_no`                  | `string` Masked card number. All digits except the last 4 are replaced with `X`.                                                                     |
    | `result.error`                    | `string` Error code. `E000` = no error.                                                                                                              |
    | `result.error_Message`            | `string` Human-readable error description. `No Error` on success.                                                                                    |
    | `result.issuing_bank`             | `string` Short code of the card-issuing bank.                                                                                                        |
    | `result.card_type`                | `string` Card network. Possible values: `VISA`, `MAST`, `AMEX`, `DINR`.                                                                              |
    | `result.AcqTID`                   | `string` Acquirer Terminal ID assigned by PayU.                                                                                                      |
    | `result.AcqName`                  | `string` Acquirer name used to process the transaction.                                                                                              |
    | `result.AuthCode`                 | `string` Authorization code returned by the issuing bank.                                                                                            |
    | `result.net_amount_debit`         | `string` Net amount debited from the customer's card after any adjustments.                                                                          |
    | `result.bank_ref_no`              | `string` Bank reference number for the transaction. Use for reconciliation.                                                                          |
    | `result.bankcode`                 | `string` Payment instrument code. `CC` = Credit Card, `DC` = Debit Card.                                                                             |
    | `result.PG_TYPE`                  | `string` Payment gateway type used to process the transaction.                                                                                       |
    | `result.IsStandingInstructionSet` | `string` Mandate registration confirmation. `1` = mandate successfully registered at the bank.                                                       |
    | `result.payment_source`           | `string` Identifies the payment source type. `sist` confirms the transaction is flagged as a Standing Instruction.                                   |
    | `result.hash`                     | `string` Response hash for integrity verification. Validate this on your server before accepting the response.                                       |

    <Callout icon="📘" theme="info">
      ### **Verify Mandate Registration**

      Check all four conditions in the response to confirm the mandate was successfully registered:

      | Parameter                  | Expected Value      | Description                                    |
      | :------------------------- | :------------------ | :--------------------------------------------- |
      | `status`                   | `success`           | Transaction was successful                     |
      | `payment_source`           | `sist`              | Card marked correctly for Standing Instruction |
      | `IsStandingInstructionSet` | `1`                 | Mandate registered at the bank                 |
      | `mihpayid`                 | Any non-empty value | PayU transaction acknowledgment                |

      If any of these conditions is not met, the mandate has **not** been registered. Do not proceed to recurring debits.
    </Callout>
  </Tab>
</Tabs>