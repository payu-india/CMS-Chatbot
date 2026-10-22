---
title: Collect Payment API - CB Export
deprecated: false
hidden: true
icon: far fa-arrow-down-up-across-line
metadata:
  robots: index
---
You can collect payments from overseas buyers in their own currency, using local wallets and international cards on PayU Hosted Checkout, with PayU's \_payment API. This section provides the request and response parameters used in Step 1 of [Cross-Border Exports Integration](doc:cross-border-exports-integration). You can get the sample request and response when using the "Try It" experience. For the complete integration steps, refer to [Cross-Border Exports Integration](doc:cross-border-exports-integration).

<Cards_PayU_Labs />

<br />

<Callout icon="📘" theme="info">
  ### **Note**

  - Use the **key and salt of the MID for the transaction currency**. Each currency has its own MID.
  - Send the amount in the **foreign currency**. PayU doesn't convert INR at checkout.
  - The exact hash formula is confirmed by the PayU integration team at onboarding.
</Callout>

**Environment**

|                            |                                   |
| :------------------------- | :-------------------------------- |
| **Test Environment**       | `https://test.payu.in/_payment`   |
| **Production Environment** | `https://secure.payu.in/_payment` |

## Request parameters

### Mandatory parameters

| **Parameter**         | **Type** | **Description**                                                                                                                                                                         |
| :-------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `key`                 | `string` | Merchant key of the MID for the transaction currency. Each currency has a separate key. For example, `YOUR_SGD_MID_KEY`                                                                 |
| `txnid`               | `string` | Unique transaction ID you generate. Alphanumeric, maximum 25 characters, unique across all your transactions. A reused `txnid` is treated as a duplicate. For example, `EXP20261022001` |
| `amount`              | `string` | Amount in the foreign currency, with no currency symbol. Convert INR to FCY before calling PayU. For example, `161.29`                                                                  |
| `transactionCurrency` | `string` | ISO 4217 code of the amount. Must match the currency of the MID key. Mandatory for exports. For example, `SGD`                                                                          |
| `productinfo`         | `string` | Description of the actual product or service. Avoid generic labels. For example, `Online Course`                                                                                        |
| `firstname`           | `string` | Buyer's first name. Used as the remitter name for settlement; missing values cause settlement to fail. For example, `Wei Ling`                                                          |
| `email`               | `string` | Buyer's email address. For example, `weiling@example.com`                                                                                                                               |
| `phone`               | `string` | Buyer's phone number with country code. For example, `+6591234567`                                                                                                                      |
| `address1`            | `string` | Buyer's billing address line 1. Used as the remitter address for settlement. Mandatory for exports. For example, `10 Anson Road`                                                        |
| `city`                | `string` | Buyer's city. For example, `Singapore`                                                                                                                                                  |
| `zipcode`             | `string` | Buyer's postal or ZIP code. For example, `079903`                                                                                                                                       |
| `country`             | `string` | Buyer's country as an ISO alpha-2 code. Must not be `IN`. For example, `SG`                                                                                                             |
| `surl`                | `string` | HTTPS URL for the success redirect. For example, `<redacted URL>`                                                                                                                       |
| `furl`                | `string` | HTTPS URL for the failure or cancellation redirect. For example, `<redacted URL>`                                                                                                       |
| `hash`                | `string` | SHA-512 hash of the request, generated on your server. See [Generate the hash](doc:cross-border-exports-integration).                                                                   |

### Conditional parameters

| **Parameter** | **Type** | **Description**                                                                                                                                                                                  |
| :------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `udf1`        | `string` | RBI purpose code. Required for service exports. Confirm the code for your service category with the PayU onboarding team. For example, `P1007` (online education) or `P1004` (software services) |
| `udf2`        | `string` | Service utilization country. Required when `udf1` is a service-export purpose code. For example, `SG`                                                                                            |
| `udf5`        | `string` | Invoice ID. Required when your purpose code needs an invoice reference. For example, `INV-2026-0001`                                                                                             |
| `api_version` | `string` | API version that allows `transactionCurrency`. For example, `22`                                                                                                                                 |

{/* REVIEW: Confirm api_version=22 for merchants (Confluence: transactionCurrency is accepted only on api_version 22 or 23). Confirm when udf5 is required. */}

### Supported currencies and wallets

| **MID currency** | **Wallets**                                        |
| :--------------- | :------------------------------------------------- |
| `SGD`            | GrabPay Singapore, international cards             |
| `MYR`            | Touch 'n Go, GrabPay Malaysia, international cards |

{/* REVIEW: Confirm whether THB and IDR are supported; the source doc lists them as accepted transactionCurrency values but not in the supported wallets table. */}

### Hash formula

```text
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|transactionCurrency|SALT)
```

<Callout icon="❗️" theme="error">
  ### **Important**

  The hash formula shown is for `api_version=22`. Confirm the formula with the PayU integration team at onboarding, and don't use the domestic formula without confirming it applies.
</Callout>

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl -X POST "https://test.payu.in/_payment" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    --data-urlencode "key=YOUR_SGD_MID_KEY" \
    --data-urlencode "txnid=EXP20261022001" \
    --data-urlencode "amount=161.29" \
    --data-urlencode "transactionCurrency=SGD" \
    --data-urlencode "api_version=22" \
    --data-urlencode "productinfo=Online Course" \
    --data-urlencode "firstname=Wei Ling" \
    --data-urlencode "email=weiling@example.com" \
    --data-urlencode "phone=+6591234567" \
    --data-urlencode "address1=10 Anson Road" \
    --data-urlencode "city=Singapore" \
    --data-urlencode "zipcode=079903" \
    --data-urlencode "country=SG" \
    --data-urlencode "udf1=P1007" \
    --data-urlencode "udf2=SG" \
    --data-urlencode "udf5=INV-2026-0001" \
    --data-urlencode "surl=<redacted URL>" \
    --data-urlencode "furl=<redacted URL>" \
    --data-urlencode "hash=YOUR_GENERATED_HASH"
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  PayU posts the response to your `surl` or `furl` as form fields. The values below are illustrative.

  ### Success

  ```text
  mihpayid=403993715531234567
  status=success
  key=YOUR_SGD_MID_KEY
  txnid=EXP20261022001
  amount=161.29
  net_amount_debit=161.29
  transactionCurrency=SGD
  productinfo=Online Course
  firstname=Wei Ling
  email=weiling@example.com
  phone=+6591234567
  udf1=P1007
  udf2=SG
  udf5=INV-2026-0001
  error=E000
  error_Message=No Error
  hash=RESPONSE_HASH
  ```

  ### Failure (buyer abandoned the wallet page)

  ```text
  mihpayid=403993715531234568
  status=failure
  key=YOUR_SGD_MID_KEY
  txnid=EXP20261022002
  amount=161.29
  transactionCurrency=SGD
  error=ERROR_CODE
  error_Message=ERROR_MESSAGE
  hash=RESPONSE_HASH
  ```


</Accordion>

<Accordion title="Response parameters" icon="fa-list">
  | **Parameter**         | **Description**                                                             |
  | :-------------------- | :-------------------------------------------------------------------------- |
  | `mihpayid`            | `string` PayU's unique transaction reference.                               |
  | `status`              | `string` Payment status: `success` or `failure`.                            |
  | `txnid`               | `string` Your transaction ID from the request.                              |
  | `amount`              | `string` Amount in the foreign currency, as sent in the request.            |
  | `net_amount_debit`    | `string` Amount debited from the buyer.                                     |
  | `transactionCurrency` | `string` ISO 4217 currency code of the transaction.                         |
  | `udf1`–`udf5`         | `string` The user-defined fields you sent, returned unchanged.              |
  | `error`               | `string` Error code, populated on failure.                                  |
  | `error_Message`       | `string` Error description, populated on failure.                           |
  | `hash`                | `string` Response hash. Verify it on your server before updating the order. |

  Verify the response hash with the same MID's salt:

  ```text
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  {/* REVIEW: Confirm the reverse hash formula for api_version 22. */}
</Accordion>

<Accordion title="Webhook notification" icon="fa-bell">
  PayU sends an HTTP POST to your registered webhook URL when the final payment result is available.

  | **Parameter**         | **Description**                                                |
  | :-------------------- | :------------------------------------------------------------- |
  | `txnid`               | `string` Your transaction ID. Use it as the deduplication key. |
  | `status`              | `string` `success` or `failure`.                               |
  | `mihpayid`            | `string` PayU's transaction reference.                         |
  | `amount`              | `string` Transaction amount in the foreign currency.           |
  | `net_amount_debit`    | `string` Amount debited from the buyer.                        |
  | `transactionCurrency` | `string` ISO 4217 currency code.                               |
  | `error_code`          | `string` Error code, populated on failure.                     |
  | `error_message`       | `string` Error description, populated on failure.              |

  Return HTTP `200` quickly. PayU retries on a non-200 response or a timeout, so process notifications idempotently.
</Accordion>

<Callout icon="🚧" theme="warn">
  ### Error Handling

  - A mismatch between the MID key and `transactionCurrency` makes the payment fail.
  - Missing `firstname`, `address1`, `zipcode` or `country`, or a `country` of `IN`, causes settlement to be rejected even if the payment succeeded.
  - If the webhook doesn't arrive, use the [Verify Payment API](ref:verify-payment-api) with the `txnid` or `mihpayid`. For error codes, refer to [Error Codes](ref:error-codes).
</Callout>

<Accordion title="Values to be used in Test environment" icon="fa-flask">
  - **Payment URL:** `https://test.payu.in/_payment`
  - **Key and salt:** the test key and salt for each currency MID, shared by PayU at onboarding.
  - **Buyer country:** any supported non-Indian country code, for example `SG` or `MY`.

{/* REVIEW: Add test wallet credentials or simulator details for GrabPay and Touch 'n Go. */}

</Accordion>
