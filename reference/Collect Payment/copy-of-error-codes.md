---
title: Error Codes V2
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU's error handling operates at two complementary levels. The standard error codes and `error_message` fields provide a baseline view of why a transaction failed. In addition, PayU applies a machine learning model to raw gateway failure responses and returns an `error_details` object alongside the standard fields — giving you a standardised error code, a curated customer message, and a detailed merchant explanation, without any changes to your existing integration.

Keep the following in mind when handling payment responses:

* The **PayU Error Code** column in the error code tables corresponds to the value returned in the **error** parameter of the payment response.
* The **error_message / message** column corresponds to the value returned in the **error_message / message** parameter of the payment response.

<Callout icon="📘" theme="info">
  ### **Note:**

  The reason for failure depends upon the error codes provided by different banks and hence the detailing of error reasons may differ from one transaction to another.
</Callout>

<Callout icon="❗️" theme="error">
  ### **Transaction Stages Error handling:**

  For error references during various transaction stages in Net Banking, Cards and Wallets, refer to [Transaction Stages - Error References on Field7 & Field8](#transaction-stages-error-references-field7-field8).
</Callout>

<Callout icon="📘" theme="info">
  ### **Reference:**

  Refer to the [Cards](https://docs.payu.in/reference/error-codes#cards) section for AuthN and AuthZ errors.
</Callout>

***

## Consolidated List Of Error Codes

Below is the consolidated list of all error codes.

<SearchableTableRemote
  tableKey="https://raw.githubusercontent.com/palgunams21/payu-docs-assets/refs/heads/main/data/payment-error-codes.json"
  placeholder="Search"
  maxHeight="500px"
/>

***

## Other Error Codes

<SearchableTableRemote
  tableKey="https://raw.githubusercontent.com/palgunams21/payu-docs-assets/refs/heads/main/data/other-error-codes.json"
  placeholder="Search"
  maxHeight="500px"
/>

***

## Cards

This section contains error codes associated with cards.

### Error References on Field7 and Field8

The PayU error mappings documentation page provides a reference guide for various error codes in the PayU payment system. The page includes:

* [Field Error code structure](#field-error-code-structure): Explains how error codes are formatted and what different components mean
* **Field7 Error Code Mapping** — Contains error codes like ALT_ID_PROV_ERROR, 3DS_METHOD_POSITIVE, etc., with their descriptions, platform layers, and API layers for the following payment modes:
  * [Field7 for Card payments](#field7-for-card-payments)
  * [Field 7 for Net Banking/Wallet payments](#netbanking-and-wallets)

> :blue_book: **Standard error codes vs Field 7 error codes**
>
> The Field7 error codes documented in this section are part of PayU's comprehensive error handling system. These codes provide detailed transaction state information that complements the standard [Error Codes](#standard-error-codes) used across PayU's payment platform.
>
> While standard error codes (e.g. E501, E502, etc.) indicate specific failure reasons, Field7 values track the transaction state and provide visibility into exactly where in the payment flow an error or status change occurred. For complete error handling, developers should check both:
>
> 1. **Field7 Values**: To determine the transaction state and processing stage
> 2. **Error Codes**: To identify specific failure reasons when applicable
>
> For integration purposes, always implement error handling that accounts for both these complementary systems to provide the best user experience and troubleshooting capabilities.

### Field Error code structure

To understand the error codes, you need to read the Error Code Object sent in the Response structure or stored in the database.

1. **Field7 – Execution Leg**: This field is used to understand at which execution stage (or leg) the transaction got declined. It is essentially a forward leg or process leg of an API that identifies the point of transaction failure. Refer to following sub-sections for understanding this field values:
   * [Field7 for Card payments](#field7-for-card-payments)
   * [Field 7 for Net Banking/Wallet payments](#netbanking-and-wallets)
2. **Field8 – Bank or Wallet's Reason**: This field captures the actual reason for the transaction failure as provided by the bank. It gives direct feedback or error information from the bank's end.
3. **Field9 – PayU's Error Translation**: This field contains the PayU-translated version of the error recorded in Field8. It provides a simplified and standardized interpretation of the error for easier understanding and debugging.
4. **Error Code**: Represents PayU's error code mapped to the specific issue. It acts as a unique identifier for the error.
5. **Error Message**: This contains PayU's error interpretation, which elaborates on or describes the error in a user-friendly manner to assist in troubleshooting.

### Issuer Decline Error Codes

The following table helps you identify specific reasons for payment failures and provides standardized error codes and messages. This will facilitate troubleshooting and help you communicate with your customers when transactions are declined.

<SearchableTableRemote
  tableKey="https://raw.githubusercontent.com/palgunams21/payu-docs-assets/refs/heads/main/data/issuer-decline-error-codes.json"
  placeholder="Search"
  maxHeight="500px"
/>

### Field7 for Card payments

<SearchableTableRemote
  tableKey="https://raw.githubusercontent.com/palgunams21/payu-docs-assets/refs/heads/main/data/field7-card-payments.json"
  placeholder="Search"
  maxHeight="500px"
/>

### AuthN Errors

<SearchableTableRemote
  tableKey="https://raw.githubusercontent.com/palgunams21/payu-docs-assets/refs/heads/main/data/auth-n-error-codes.json"
  placeholder="Search"
  maxHeight="500px"
/>

<Callout icon="⬇️" theme="default">
  ### **Download Template**

  [Download AuthN Errors in the CSV Template](https://github.com/palgunams21/payu-docs-assets/releases/download/AuthN-AuthZ-errors/AuthN_error_list.csv)
</Callout>

### AuthZ Errors

<SearchableTableRemote
  tableKey="https://raw.githubusercontent.com/palgunams21/payu-docs-assets/refs/heads/main/data/auth-z-error-codes.json"
  placeholder="Search"
  maxHeight="500px"
/>

<Callout icon="⬇️" theme="default">
  ### **Download Template**

  [Download AuthZ Errors in the CSV Template](https://github.com/palgunams21/payu-docs-assets/releases/download/AuthN-AuthZ-errors/AuthZ_error_list.csv)
</Callout>

### Alt ID Errors

<SearchableTableRemote
  tableKey="https://raw.githubusercontent.com/palgunams21/payu-docs-assets/refs/heads/main/data/alt-id-error-codes.json"
  placeholder="Search"
  maxHeight="500px"
/>

### ML-Powered Error Details

Issuing banks, card networks and payment gateways report transaction failures in widely varying formats, and a single failure reason may be returned as many different raw messages. PayU applies a machine learning model to each raw failure response and maps it to a single standard error code, accompanied by a message for the end customer and a detailed explanation for the merchant.

When a transaction fails, PayU includes an `error_details` object in the transaction response. This object contains:

* A standard PayU error code
* A message intended for the end customer
* A detailed technical message intended for the merchant
* The raw error returned by the gateway

The `error_details` object is returned **in addition to** the existing response fields. PayU continues to return `field9` and `error_Message`, so existing integrations require no changes.

On PayU Hosted Checkout, PayU displays `userMessage` on the failure screen automatically.

<Callout icon="📘" theme="info">
  ### **Availability**

  ML-powered error codes are currently available for **Domestic Cards**. Support for other payment modes is under development. Until a payment mode is made available, please continue to refer to the [Standard Error Codes](#standard-error-codes) for that mode.
</Callout>

| Payment mode        | Status            |
| ------------------- | ----------------- |
| Domestic Cards      | Available         |
| International Cards | Under development |
| Net Banking         | Under development |
| UPI                 | Under development |
| Wallets             | Under development |
| EMI                 | Under development |
| BNPL                | Under development |

<Callout icon="📘" theme="info">
  ### **Note**

  Every failure response contains a complete `error_details` object. Where PayU is unable to classify an error, the response contains a generic `userMessage`, with `newErrorCode` set to `NA` and the category set to `Unknown`. No additional fallback logic is required in your integration.
</Callout>

#### **Sample Response**

The following sample illustrates the `error_details` object for a failed domestic card transaction:

```json
"error_details": {
  "step": "authorisationFailure",
  "source": "Risk decline",
  "responsibility": "Issuer",
  "userMessage": "Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours.",
  "merchantMessage": "The bank declined the authorization because they suspected fraudulent activity. Please ask the customer to contact their bank or try a different payment method.",
  "newErrorCode": "EN613",
  "optional": {
    "pgError": "05 | Do not honor",
    "issuerErrorCode": "",
    "apiLayer": ""
  }
}
```

#### **Field Reference**

The following table describes each field in the `error_details` object and its intended audience:

| Field                      | Description                                                                                                                | Audience         |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `userMessage`              | Curated message for the end customer. PayU Hosted Checkout displays this message on the failure screen.                    | **End customer** |
| `merchantMessage`          | Detailed technical explanation of the failure, with a recommended action, for analysis and support purposes.               | Merchant         |
| `newErrorCode`             | Standard PayU error code (EN…). Set to `NA` where the error could not be classified.                                       | Merchant         |
| `source`                   | Failure category, for example, Risk decline or Business decline. Set to `Unknown` where the error could not be classified. | Merchant         |
| `responsibility`           | Party at which the failure occurred, for example, Issuer.                                                                  | Merchant         |
| `step`                     | Payment stage at which the failure occurred.                                                                               | Merchant         |
| `optional.pgError`         | Raw response code and description returned by the gateway or acquirer.                                                     | Merchant         |
| `optional.issuerErrorCode` | Error code returned by the issuer, where available.                                                                        | Merchant         |
| `optional.apiLayer`        | Layer at which the failure was raised. Set to `Unknown` where the error could not be classified.                           | Merchant         |

> **Important:** Only `userMessage` is intended for end customers. All other fields are intended for merchant use only and must not be displayed to customers.

#### **Error Code Reference**

Every failed payment response includes a `newErrorCode`, for example, `EN3126`.

**Format:** `EN` + Category (first digit) + Source (second digit) + Message number (variable length).<br />For example: `EN311`, `EN3126`, `EN30505`.

#### Category (first digit)

| Digit | Category                 | Description                                                                                              | Recommended action                                                                          |
| ----- | ------------------------ | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| 1     | Customer error           | The customer entered incorrect details, cancelled the payment, or did not complete it.                   | Request the customer to verify their details and retry.                                     |
| 2     | Internal technical error | A technical issue within PayU systems.                                                                   | Retry the transaction. If the issue persists, contact PayU support.                         |
| 3     | External technical error | A technical issue at the bank, card network or another partner.                                          | Retry the transaction, or request the customer to use an alternative payment method.        |
| 4     | Configuration error      | The merchant account or integration is not configured for this payment.                                  | Contact your PayU account manager or PayU support.                                          |
| 5     | Business decline         | The transaction was declined for a business reason, such as insufficient funds or a limit being reached. | Request the customer to use an alternative payment method or contact their bank.            |
| 6     | Risk decline             | The transaction was declined by the bank or by risk checks for security reasons.                         | Do not retry with the same card. Request the customer to use an alternative payment method. |
| 0     | Unclassified             | The failure could not be categorised.                                                                    | Retry the transaction. If the issue persists, contact PayU support.                         |

#### Source (second digit)

| Digit | Source      | Point of failure                    |
| ----- | ----------- | ----------------------------------- |
| 1     | Issuer      | The customer's bank                 |
| 2     | Network     | The card network or payment scheme  |
| 3     | Merchant    | The merchant account or integration |
| 4     | Customer    | The customer's action or input      |
| 5     | PayU        | PayU systems                        |
| 0     | Unspecified | The source could not be determined  |

#### Examples

| Code   | Interpretation                                                          |
| ------ | ----------------------------------------------------------------------- |
| EN3126 | External technical error (3) at the customer's bank (1), message 26     |
| EN6145 | Risk decline (6) by the customer's bank (1), message 45                 |
| EN4312 | Configuration error (4) in the merchant's configuration (3), message 12 |
| EN1408 | Customer error (1) arising from customer input (4), message 8           |

<Callout icon="📘" theme="info">
  ### **Recommendations**

  * **Analytics and reporting:** Group failures by `newErrorCode`, or by its category and source digits, rather than parsing the free-text value in `field9`.
  * **Triage:** Use the category digit to determine the next action. For example, category 6 (Risk decline) indicates that the transaction must not be retried with the same card, and category 4 (Configuration error) indicates that you should contact your PayU account manager.
  * **Custom failure pages:** Display only `userMessage` to end customers. Do not display `merchantMessage` or `pgError`.
  * **Message updates:** PayU updates error messages periodically to address new error scenarios across the ecosystem. Ensure that any logic built on this data accommodates such updates.
</Callout>

### Error Lists by Payment Mode

The following lists set out the `userMessage` values that PayU returns to end customers for each payment mode.

#### Domestic Cards

| Status | User message                                                                                                                                                         |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| failed | E-Commerce is not enabled for this card. Please enable E-commerce on your bank app and retry the transaction.                                                        |
| failed | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP                                                                                  |
| failed | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours.                            |
| failed | Payment could not be processed. Please try again or use a different payment method.                                                                                  |
| failed | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours.                   |
| failed | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours.                           |
| failed | Payment could not be completed. Please try again later or use a different payment method.                                                                            |
| failed | A technical error occurred. Please try again or use a different payment method.                                                                                      |
| failed | Payment failed. Please try again later or use a different payment method.                                                                                            |
| failed | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours.                                                   |
| failed | Session timed out error, Please retry or use another paymode. If money is debited it will be refunded within 48 hours.                                               |
| failed | We couldn't verify your payment. Please try again.                                                                                                                   |
| failed | Payment declined by bank. Please contact your bank or try another card.                                                                                              |
| failed | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours.                             |
| failed | The card details entered were incorrect. Please re-enter correct card details and try again.                                                                         |
| failed | Transaction failed as the card has expired please use another paymode. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | This card is not supported on this merchant, please use another card or another paymode.                                                                             |
| failed | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours.        |
| failed | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode.                                                |
| failed | Wrong Expiry date/CVV entered, please recheck and try again.                                                                                                         |
| failed | Transaction failed due to bank server error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours.                           |
| failed | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode.                                                                  |
| failed | No account found for this card. You can retry on another paymode. If money is debited it will be refunded within 48 hours.                                           |
| failed | Transaction Failed due to insufficient fund in your account. Kindly use another card or another payment mode.                                                        |
| failed | This card is currently not supported by your card network. Please use another paymode. If money is debited it will be refunded within 48 hours.                      |
| failed | This payment was already processed. If charged twice, money will be refunded within 48 hours.                                                                        |
| failed | E-Commerce not enable for this card. Please enable E-commerce on your bank app and retry the transaction.                                                            |
| failed | Wrong Expiry date/CVV entered, please recheck and try again                                                                                                          |
| failed | Payment failed due to a technical issue. Please try again or use a different payment method.                                                                         |
| failed | Transaction Succesful                                                                                                                                                |
| failed | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 - 72 hours.                      |
| failed | The card used cannot be saved currently due to bank's rules. Please retry or use another paymode. If money is debited it will be refunded within 48 hours.           |
| failed | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP.                                                                                 |
| failed | Transaction has been cancelled by the user, Please retry or use another paymode. If money is debited it will be refunded within 48 hours.                            |
| failed | Payment verification failed. Please try again.                                                                                                                       |
| failed | Transaction declined due to Wrong CVV or expiry. Please retry with correct card details or use another paymode.                                                      |
| failed | Transaction failed due to technical issues. Please retry or use another paymode. If money is debited it will be refunded within 48 hours.                            |
| failed | Transaction failed due to some technical issues. Please retry or use another paymode. If money is debited it will be refunded within 48 hours.                       |
| failed | Transaction timed out at the Payment Gateway, please retry.                                                                                                          |
| failed | No account found for this card. Please contact your issuer. You can retry on another paymode. If money is debited it will be refunded within 48 - 72 hours.          |
| failed | Transaction failed due to technical issues. Please retry or use another paymode. If money is debited it will be refunded within 48 - 72 hours                        |

#### Other Payment Modes

<Callout icon="📘" theme="info">
  ### **Under development**

  Error lists for International Cards, Net Banking, UPI, Wallets, EMI and BNPL are under development. PayU will publish a list for each payment mode in this section as it becomes available. In the interim, please refer to the [Standard Error Codes](#standard-error-codes) for these payment modes.
</Callout>

***

## NetBanking and Wallets Error Codes

The following are the errors associated with NetBanking and wallets along with their reasons and descriptions.

<SearchableTableRemote
  tableKey="https://raw.githubusercontent.com/palgunams21/payu-docs-assets/refs/heads/main/data/netbanking-wallets.json"
  placeholder="Search"
  maxHeight="500px"
/>

## UPI Error Codes

<SearchableTableRemote
  tableKey="https://raw.githubusercontent.com/palgunams21/payu-docs-assets/refs/heads/main/data/upi-error-codes.json"
  placeholder="Search"
  maxHeight="500px"
/>

## Subscription Error Codes

These are the errors you may get during mandate registration, along with their descriptions and recommended actions.

<Accordion title="Errors and Recommended Fix" icon="⚠️">
  <Table>
    <thead>
      <tr>
        <th>
          **Errors (Error Code)**
        </th>

        <th>
          **Error Message**
        </th>

        <th>
          **Error Description**
        </th>

        <th>
          **Recommended Fix**
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          **E756**
        </td>

        <td>
          Tokenization failed before debit could be initiated
        </td>

        <td>
          This error occurs when tokenization fails or the card/token BIN is not supported for subscriptions.<br /><br />**Note:**

          1. You should enable the required flag on your MID to receive this error. Raise request to the support team to enable the flag.
          2. This failure scenario does not apply to the Direct Auth flow.
        </td>

        <td>
          Retry using a new card.
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>