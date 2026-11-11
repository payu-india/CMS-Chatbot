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

#### **Field Error code structure**

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

***

<SearchableRichTable
  headersJson='["Errors", "Error_message/Message", "Error Description", "Title"]'
  placeholder="Search error codes..."
  maxHeight="600px"
>
  <tr>
    <td><code>E1620</code></td>
    <td>Payment Method Enforced and wrong method selected</td>
    <td>WRONG_PAYMENT_METHOD_SELECTED</td>
    <td>WRONG_PAYMENT_METHOD_SELECTED</td>
  </tr>
  <tr>
    <td><code>E907</code></td>
    <td>Wrong payment method selected.</td>
    <td>WRONG_PAYMENT_METHOD</td>
    <td>WRONG_PAYMENT_METHOD</td>
  </tr>
  <tr>
    <td><code>E4318</code></td>
    <td>WITHDRAWAL STOPPED OWING TO LUNACY OF ACCOUNT HOLD</td>
    <td>WITHDRAWAL STOPPED OWING TO LUNACY OF ACCOUNT HOLD</td>
    <td>WITHDRAWAL_STOPPED_OWING_TO_LUNACY_OF_ACCOUNT_HOLD</td>
  </tr>
  <tr>
    <td><code>E4317</code></td>
    <td>WITHDRAWAL STOPPED OWING TO INSOLVENCY OF ACCOUNT</td>
    <td>WITHDRAWAL STOPPED OWING TO INSOLVENCY OF ACCOUNT</td>
    <td>WITHDRAWAL_STOPPED_OWING_TO_INSOLVENCY_OF_ACCOUNT</td>
  </tr>
  <tr>
    <td><code>E4316</code></td>
    <td>WITHDRAWAL STOPPED OWING TO DEATH OF ACCOUNT HOLDER</td>
    <td>WITHDRAWAL STOPPED OWING TO DEATH OF ACCOUNT HOLDER</td>
    <td>WITHDRAWAL_STOPPED_OWING_TO_DEATH_OF_ACCOUNT_HOLDER</td>
  </tr>
  <tr>
    <td><code>E4684</code></td>
    <td>VPA is not available for transaction</td>
    <td>VPA is not available for transaction</td>
    <td>VPA_Is_Not_Available_For_Transaction</td>
  </tr>
  <tr>
    <td><code>E4685</code></td>
    <td>VPA is available for transaction</td>
    <td>VPA is available for transaction</td>
    <td>VPA_Is_Available_For_Transaction</td>
  </tr>
  <tr>
    <td><code>E224</code></td>
    <td>Virtual Account Number Mismatch</td>
    <td>VIRTUAL_ACCOUNT_NUMBER_MISMATCH</td>
    <td>VIRTUAL_ACCOUNT_NUMBER_MISMATCH</td>
  </tr>
  <tr>
    <td><code>E1649</code></td>
    <td>VIP Approval</td>
    <td>VIP_APPROVAL</td>
    <td>VIP_APPROVAL</td>
  </tr>
  <tr>
    <td><code>E4251</code></td>
    <td>VERSION/TAGS SENT NOT SUPPORTED BY PSP/BANK</td>
    <td>VERSION/TAGS SENT NOT SUPPORTED BY PSP/BANK</td>
    <td>VERSION_TAGS_SENT_NOT_SUPPORTED_BY_PSP_BANK</td>
  </tr>
  <tr>
    <td><code>E4530</code></td>
    <td>Mandate request failed as start date is less than current date</td>
    <td>Validity start date should not be less than current date</td>
    <td>Validity_Start_Date_Should_Not_Be_Less_Than_Current_Date</td>
  </tr>
  <tr>
    <td><code>E4531</code></td>
    <td>Mandate request failed as end date is less than start date</td>
    <td>Validity end date should not be less than validity start date</td>
    <td>Validity_End_Date_Should_Not_Be_Less_Than_Validity_Start_Date</td>
  </tr>
  <tr>
    <td><code>E4156</code></td>
    <td>VALIDATION ERROR</td>
    <td>VALIDATION ERROR</td>
    <td>VALIDATION_ERROR</td>
  </tr>
  <tr>
    <td><code>E4373</code></td>
    <td>VALIDATION ERROR</td>
    <td>VALIDATION ERROR</td>
    <td>VALIDATION_ERROR_1</td>
  </tr>
  <tr>
    <td><code>E4221</code></td>
    <td>VAE FAILED</td>
    <td>VAE FAILED</td>
    <td>VAE_FAILED</td>
  </tr>
  <tr>
    <td><code>E705</code></td>
    <td>Bank declined to process the transaction due to user permissions set for the card.</td>
    <td>USER_PROFILE_SETTINGS_ERROR</td>
    <td>USER_PROFILE_SETTINGS_ERROR</td>
  </tr>
  <tr>
    <td><code>E4255</code></td>
    <td>URL VERSION MISMATCHED (NEG ACK FOR RESPAUTH. ERROR CODE U18 IN FINAL RESPPAY.)</td>
    <td>URL VERSION MISMATCHED (NEG ACK FOR RESPAUTH. ERROR CODE U18 IN</td>
    <td>URL_VERSION_MISMATCHED_NEG_ACK_FOR_RESPAUTH__ERROR_CODE_U18_IN_FINAL_RESPPAY</td>
  </tr>
  <tr>
    <td><code>E500</code></td>
    <td>Bank failed to authenticate the customer</td>
    <td>UNKNOWN_ERROR_PG</td>
    <td>UNKNOWN_ERROR_PG</td>
  </tr>
  <tr>
    <td><code>E908</code></td>
    <td>International cards not allowed</td>
    <td>UNKNOWN_BINS_NO_ACTIVE_PG_ASSIGNED</td>
    <td>UNKNOWN_BINS_NO_ACTIVE_PG_ASSIGNED</td>
  </tr>
  <tr>
    <td><code>E1634</code></td>
    <td>Unique Constraint failure from the bank</td>
    <td>UNIQUE_CONSTRAINT_FAILURE</td>
    <td>UNIQUE_CONSTRAINT_FAILURE</td>
  </tr>
  <tr>
    <td><code>E9209</code></td>
    <td>Unacceptable Transaction Fee</td>
    <td>Unacceptable Transaction Fee</td>
    <td>UNACCEPTABLE_TRANSACTION_FEE</td>
  </tr>
  <tr>
    <td><code>E1608</code></td>
    <td>Unable to process the request.</td>
    <td>UNABLE_TO_PROCESS</td>
    <td>UNABLE_TO_PROCESS</td>
  </tr>
  <tr>
    <td><code>E4385</code></td>
    <td>UNABLE TO PROCESS REVERSAL</td>
    <td>UNABLE TO PROCESS REVERSAL</td>
    <td>UNABLE_TO_PROCESS_REVERSAL</td>
  </tr>
  <tr>
    <td><code>E4041</code></td>
    <td>Transaction failed due to internal exception at server/cbs end at customer&#x27;s bank</td>
    <td>UNABLE TO PROCESS DUE TO INTERNAL EXCEPTION AT SERVER/CBS/ETC ON</td>
    <td>UNABLE_TO_PROCESS_DUE_TO_INTERNAL_EXCEPTION_AT_SERVER_CBS_ETC_ON_REMITTER_SIDE</td>
  </tr>
  <tr>
    <td><code>E4259</code></td>
    <td>Transaction failed due to internal exception at server/cbs end at acquirer&#x27;s bank</td>
    <td>UNABLE TO PROCESS DUE TO INTERNAL EXCEPTION AT SERVER/CBS/ETC ON</td>
    <td>UNABLE_TO_PROCESS_DUE_TO_INTERNAL_EXCEPTION_AT_SERVER_CBS_ETC_ON_BENEFICIARY_TD_SIDE</td>
  </tr>
  <tr>
    <td><code>E4044</code></td>
    <td>Transaction failed due to credit processing issue in pool account of the acquriing bank</td>
    <td>UNABLE TO PROCESS CREDIT FROM BANK&#x27;S POOL/BGL ACCOUNT</td>
    <td>UNABLE_TO_PROCESS_CREDIT_FROM_BANK_S_POOL_BGL_ACCOUNT</td>
  </tr>
  <tr>
    <td><code>E4045</code></td>
    <td>Transaction failed due to debit processing issue in pool account of the customer bank</td>
    <td>UNABLE TO PROCESS CREDIT FROM BANK&#x27;S POOL/BGL ACCOUNT</td>
    <td>UNABLE_TO_PROCESS_DEBIT_IN_BANK_S_POOL_BGL_ACCOUNT</td>
  </tr>
  <tr>
    <td><code>E4102</code></td>
    <td>Transaction failed due to customer not notified of the transaction</td>
    <td>Unable to Notify the Customer</td>
    <td>Unable_To_Notify_The_Customer</td>
  </tr>
  <tr>
    <td><code>E9211</code></td>
    <td>Unable to Locate Record on File</td>
    <td>Unable to Locate Record on File</td>
    <td>UNABLE_TO_LOCATE_RECORD_ON_FILE</td>
  </tr>
  <tr>
    <td><code>E9225</code></td>
    <td>Unable to Dispense</td>
    <td>Unable to Dispense</td>
    <td>UNABLE_TO_DISPENSE</td>
  </tr>
  <tr>
    <td><code>E9240</code></td>
    <td>Unable to Authorise</td>
    <td>Unable to Authorise</td>
    <td>UNABLE_TO_AUTHORISE</td>
  </tr>
  <tr>
    <td><code>E4114</code></td>
    <td>Transaction failed as umn details doesn&#x27;t exist at customer&#x27;s end</td>
    <td>UMN DOES NOT EXIST (PAYER)</td>
    <td>UMN_DOES_NOT_EXIST_PAYER</td>
  </tr>
  <tr>
    <td><code>E4128</code></td>
    <td>Transaction failed as umn details doesn&#x27;t exist at acquiring bank&#x27;s end</td>
    <td>UMN DOES NOT EXIST (PAYEE)</td>
    <td>UMN_DOES_NOT_EXIST_PAYEE</td>
  </tr>
  <tr>
    <td><code>E4227</code></td>
    <td>UIDAI FAILURE</td>
    <td>UIDAI FAILURE</td>
    <td>UIDAI_FAILURE</td>
  </tr>
  <tr>
    <td><code>E2101</code></td>
    <td>Transaction could not be processed because offer is not applicable.</td>
    <td>TXN_FAILURE_FOR * INVALID_OFFER</td>
    <td>TXN_FAILURE_FOR_INVALID_OFFER</td>
  </tr>
  <tr>
    <td><code>E2201</code></td>
    <td>splitRequest param sent for non-aggregator merchant</td>
    <td>TXN_FAILED_AGGREGATOR * TXN_NOT_ALLOWED</td>
    <td>TXN_FAILED_AGGREGATOR_TXN_NOT_ALLOWED</td>
  </tr>
  <tr>
    <td><code>E2202</code></td>
    <td>Invalid split provided in transaction request.</td>
    <td>TXN_FAILED_AGGREGATOR * INVALID_SPLIT_PROVIDED</td>
    <td>TXN_FAILED_AGGREGATOR_INVALID_SPLIT_PROVIDED</td>
  </tr>
  <tr>
    <td><code>E1101</code></td>
    <td>Transaction failed due to invalid params shared by the merchant</td>
    <td>TXN_DETAIL_INVALID * REDIRECTING_TO_MERCHANT</td>
    <td>TXN_DETAIL_INVALID_REDIRECTING_TO_MERCHANT</td>
  </tr>
  <tr>
    <td><code>E4112</code></td>
    <td>Transaction failed as mandate and transaction amount is different</td>
    <td>TXN AMOUNT DIFFERS FROM MANDATE AMOUNT</td>
    <td>TXN_AMOUNT_DIFFERS_FROM_MANDATE_AMOUNT</td>
  </tr>
  <tr>
    <td><code>E9234</code></td>
    <td>TVR validation failed by Issuer</td>
    <td>TVR validation failed by Issuer</td>
    <td>TVR_VALIDATION_FAILED_BY_ISSUER</td>
  </tr>
  <tr>
    <td><code>E227</code></td>
    <td>Transaction is Pending</td>
    <td>TRANSACTION_PENDING</td>
    <td>TRANSACTION_PENDING</td>
  </tr>
  <tr>
    <td><code>E306</code></td>
    <td>Card authentication failure</td>
    <td>TRANSACTION_INVALID_PG</td>
    <td>TRANSACTION_INVALID_PG</td>
  </tr>
  <tr>
    <td><code>E229</code></td>
    <td>Transaction declined as no prior EMI transaction exists here</td>
    <td>TRANSACTION_INVALID * EMI_BASE_ID</td>
    <td>TRANSACTION_INVALID_EMI_BASE_ID</td>
  </tr>
  <tr>
    <td><code>E308</code></td>
    <td>Transaction Failed at bank end.</td>
    <td>TRANSACTION_FAILED</td>
    <td>TRANSACTION_FAILED</td>
  </tr>
  <tr>
    <td><code>E507</code></td>
    <td>Transaction Expired</td>
    <td>TRANSACTION_EXPIRED</td>
    <td>TRANSACTION_EXPIRED</td>
  </tr>
  <tr>
    <td><code>E231</code></td>
    <td>Transaction was marked as dropped</td>
    <td>TRANSACTION_DROPPED</td>
    <td>TRANSACTION_DROPPED</td>
  </tr>
  <tr>
    <td><code>E408</code></td>
    <td>Transaction failed. Page expired due to no user input.</td>
    <td>TRANSACTION_BOUNCED</td>
    <td>TRANSACTION_BOUNCED</td>
  </tr>
  <tr>
    <td><code>E345</code></td>
    <td>Transaction declined due to technical failure</td>
    <td>Transaction rejected</td>
    <td>TECHNICAL_FAILURE</td>
  </tr>
  <tr>
    <td><code>E4374</code></td>
    <td>Transaction not allowed on VPA by customer application</td>
    <td>TRANSACTION NOT PERMITTED TO VPA by the PSP</td>
    <td>TRANSACTION_NOT_PERMITTED_TO_VPA_By_The_PSP</td>
  </tr>
  <tr>
    <td><code>E4010</code></td>
    <td>Transaction not allowed on/from the account</td>
    <td>TRANSACTION NOT PERMITTED TO THE ACCOUNT</td>
    <td>TRANSACTION_NOT_PERMITTED_TO_THE_ACCOUNT</td>
  </tr>
  <tr>
    <td><code>E1642</code></td>
    <td>Transaction not permitted to cardholder</td>
    <td>Transaction not permitted to issuer/cardholder</td>
    <td>CARD_NOT_PERMITTED</td>
  </tr>
  <tr>
    <td><code>E4375</code></td>
    <td>TRANSACTION NOT PERMITTED TO DEVICE</td>
    <td>TRANSACTION NOT PERMITTED TO DEVICE</td>
    <td>TRANSACTION_NOT_PERMITTED_TO_DEVICE</td>
  </tr>
  <tr>
    <td><code>E4348</code></td>
    <td>TRANSACTION NOT PERMITTED TO CARDHOLDER (REMITTER)</td>
    <td>Transaction not permitted to cardholder</td>
    <td>TRANSACTION_NOT_PERMITTED_TO_CARDHOLDER_REMITTER</td>
  </tr>
  <tr>
    <td><code>E4146</code></td>
    <td>Transaction not allowed from overdraft account</td>
    <td>TRANSACTION NOT PERMITTED FOR THIS A/C TYPE (OD)</td>
    <td>TRANSACTION_NOT_PERMITTED_FOR_THIS_A_C_TYPE_OD</td>
  </tr>
  <tr>
    <td><code>E4931</code></td>
    <td>Transaction is in `value` state</td>
    <td>Transaction is in `value` state</td>
    <td>Transaction_Is_In_Value_State</td>
  </tr>
  <tr>
    <td><code>E4188</code></td>
    <td>TRANSACTION IS ALREADY BEEN FAILED</td>
    <td>TRANSACTION IS ALREADY BEEN FAILED</td>
    <td>TRANSACTION_IS_ALREADY_BEEN_FAILED</td>
  </tr>
  <tr>
    <td><code>E4197</code></td>
    <td>Transaction failed as original transaction details not found during status check</td>
    <td>TRANSACTION ID IS NOT PRESENT</td>
    <td>TRANSACTION_ID_IS_NOT_PRESENT</td>
  </tr>
  <tr>
    <td><code>E4155</code></td>
    <td>TRANSACTION ID IS MISMATCHED VALIDATION ERROR</td>
    <td>TRANSACTION ID IS MISMATCHED VALIDATION ERROR</td>
    <td>TRANSACTION_ID_IS_MISMATCHED_VALIDATION_ERROR</td>
  </tr>
  <tr>
    <td><code>E4369</code></td>
    <td>Transaction declined as count of transactions increased as set by customer&#x27;s bank</td>
    <td>TRANSACTION FREQUENCY LIMIT EXCEEDED AS SET BY REMITTING MEMBER</td>
    <td>TRANSACTION_FREQUENCY_LIMIT_EXCEEDED_AS_SET_BY_REMITTING_MEMBER_BD</td>
  </tr>
  <tr>
    <td><code>E1655</code></td>
    <td>Transaction could not be completed due to violation of law</td>
    <td>TRANSACTION CANNOT BE COMPLETED. COMPLIANCE VIOLATION (REMITTER)</td>
    <td>DECLINING_DUE_TO_VOILATION_OF_LAW</td>
  </tr>
  <tr>
    <td><code>E217</code></td>
    <td>This error comes when Bank does some changes in the terminal/plug-in profile of the merchant. If merchant receives this error Bank should generate new resource file and forward the same to the merchant.</td>
    <td>TRANPORTAL_ID_ERROR</td>
    <td>TRANPORTAL_ID_ERROR</td>
  </tr>
  <tr>
    <td><code>E1911</code></td>
    <td>User entered wrong VPA too many times</td>
    <td>TOO_MANY_WRONG_VPA</td>
    <td>TOO_MANY_WRONG_VPA</td>
  </tr>
  <tr>
    <td><code>E9226</code></td>
    <td>TID not present on host</td>
    <td>TID not present on host</td>
    <td>TID_NOT_PRESENT_ON_HOST</td>
  </tr>
  <tr>
    <td><code>E4516</code></td>
    <td>Refund failed as original transaction details not valid</td>
    <td>This transaction is already processed (&quot;ICICI&quot;, Online duplicate</td>
    <td>This_Transaction_Is_Already_Processed_ICICI_Online_Duplicate_Transaction</td>
  </tr>
  <tr>
    <td><code>E4119</code></td>
    <td>Revoke is not allowed for this mandate</td>
    <td>THIS MANDATE IS NON REVOKEABLE BD</td>
    <td>THIS_MANDATE_IS_NON_REVOKEABLE_BD</td>
  </tr>
  <tr>
    <td><code>E4150</code></td>
    <td>Transaction declined due to duplicate request</td>
    <td>THE REQUEST IS DUPLICATE</td>
    <td>THE_REQUEST_IS_DUPLICATE</td>
  </tr>
  <tr>
    <td><code>E223</code></td>
    <td>Transaction not approved</td>
    <td>The order has been rejected by Decision Manager</td>
    <td>TRANSACTION_REJECTED_BY_CHECKER</td>
  </tr>
  <tr>
    <td><code>E338</code></td>
    <td>Transaction denied because one or more risk rules failed</td>
    <td>The customer matched the Denied Parties List</td>
    <td>RISK_RULE_FAILED</td>
  </tr>
  <tr>
    <td><code>E335</code></td>
    <td>Transaction failed due to incomplete authentication process</td>
    <td>The cardholder is enrolled in Payer Authentication. Please authe</td>
    <td>AUTHENTICATION_INCOMPLETE</td>
  </tr>
  <tr>
    <td><code>E2405</code></td>
    <td>Sorry, you are not eligible for the selected tenure. Please select another tenure</td>
    <td>TENURE_NOT_FOUND</td>
    <td>TENURE_NOT_FOUND</td>
  </tr>
  <tr>
    <td><code>E4157</code></td>
    <td>SYSTEM EXCEPTION</td>
    <td>SYSTEM EXCEPTION</td>
    <td>SYSTEM_EXCEPTION</td>
  </tr>
  <tr>
    <td><code>E4004</code></td>
    <td>SUSPECTED FRAUD, DECLINE/TRANSACTIONS DECLINED BASED ON RISKSCORE BY REMITTER</td>
    <td>SUSPECTED_FRAUD_DECLINE_TRANSACTIONS_DECLINED_BASED_ON_RISKSCORE_BY_REMITTER</td>
    <td>SUSPECTED_FRAUD_DECLINE_TRANSACTIONS_DECLINED_BASED_ON_RISKSCORE_BY_REMITTER</td>
  </tr>
  <tr>
    <td><code>E9208</code></td>
    <td>Suspected Malfunction</td>
    <td>Suspected Malfunction</td>
    <td>SUSPECTED_MALFUNCTION</td>
  </tr>
  <tr>
    <td><code>E4378</code></td>
    <td>Transaction declined due to risk score by beneficiary bank</td>
    <td>SUSPECTED FRAUD, DECLINE / TRANSACTIONS DECLINED BASED ON RISK S</td>
    <td>SUSPECTED_FRAUD_DECLINE_TRANSACTIONS_DECLINED_BASED_ON_RISK_SCORE_BY_BD_BENEFICIARY</td>
  </tr>
  <tr>
    <td><code>E1611</code></td>
    <td>UserCancelled as the Transaction was left orphan during sure_pay</td>
    <td>SURE_PAY_USER_CANCELLED</td>
    <td>SURE_PAY_USER_CANCELLED</td>
  </tr>
  <tr>
    <td><code>E1613</code></td>
    <td>SurePay usercancelled</td>
    <td>SURE_PAY_PROCESSED</td>
    <td>SURE_PAY_PROCESSED</td>
  </tr>
  <tr>
    <td><code>E1657</code></td>
    <td>Surcharge amount not permitted</td>
    <td>SURCHARGE_AMOUNT_NOT_PERMITTED</td>
    <td>SURCHARGE_AMOUNT_NOT_PERMITTED</td>
  </tr>
  <tr>
    <td><code>E000</code></td>
    <td>No Error</td>
    <td>Successful transaction</td>
    <td>NO_ERROR</td>
  </tr>
  <tr>
    <td><code>E1631</code></td>
    <td>Merchant Validation Failed</td>
    <td>Sorry! Transaction could not be processed as the limit of your m</td>
    <td>MERCHANT_VALIDATION_FAILED</td>
  </tr>
  <tr>
    <td><code>E1630</code></td>
    <td>Invalid Bank ME Code</td>
    <td>Sorry! Transaction could not be processed as limit is exhausted</td>
    <td>INVALID_BANK_ME_CODE</td>
  </tr>
  <tr>
    <td><code>E4520</code></td>
    <td>Refund failed as online refund not enabled on merchant</td>
    <td>Sorry you canNULLt initiate refund request</td>
    <td>Sorry_You_Cant_Initiate_Refund_Request</td>
  </tr>
  <tr>
    <td><code>E337</code></td>
    <td>Transaction declined by the issuer</td>
    <td>Soft Decline - The authorization request was approved by the iss</td>
    <td>NOT_CAPTURED</td>
  </tr>
  <tr>
    <td><code>E4025</code></td>
    <td>SIGNATURE MISMATCH</td>
    <td>SIGNATURE MISMATCH</td>
    <td>SIGNATURE_MISMATCH</td>
  </tr>
  <tr>
    <td><code>E4024</code></td>
    <td>SIGNATURE ERROR</td>
    <td>SIGNATURE ERROR</td>
    <td>SIGNATURE_ERROR</td>
  </tr>
  <tr>
    <td><code>E4093</code></td>
    <td>SHARETOPAYEE=Y FOR PAYER INITIATED IF PURPOSE=01</td>
    <td>SHARETOPAYEE=Y FOR PAYER INITIATED IF PURPOSE=01</td>
    <td>SHARETOPAYEE_Y_FOR_PAYER_INITIATED_IF_PURPOSE_01</td>
  </tr>
  <tr>
    <td><code>E1658</code></td>
    <td>Service not available</td>
    <td>SERVICE_NOT_AVAILABLE</td>
    <td>SERVICE_NOT_AVAILABLE</td>
  </tr>
  <tr>
    <td><code>E1201</code></td>
    <td>You are not authorized to do this transaction.</td>
    <td>SERVICE_AUTHORIZATION_ERROR</td>
    <td>SERVICE_AUTHORIZATION_ERROR</td>
  </tr>
  <tr>
    <td><code>E4147</code></td>
    <td>Transaction failed as customer is not active on UPI</td>
    <td>Service disable on UPI/ Customer is not active</td>
    <td>Service_Disable_On_UPI__Customer_is_Not_Active</td>
  </tr>
  <tr>
    <td><code>E4105</code></td>
    <td>Transaction failed due to recurring sequence mismatch</td>
    <td>SEQNUM MISMATCH (PAYER PSP)</td>
    <td>SEQNUM_MISMATCH_PAYER_PSP</td>
  </tr>
  <tr>
    <td><code>E1633</code></td>
    <td>Separate Authentication Failed</td>
    <td>SEPARATE_AUTHENTICATION_FAILED</td>
    <td>SEPARATE_AUTHENTICATION_FAILED</td>
  </tr>
  <tr>
    <td><code>E1663</code></td>
    <td>Failure received in send OTP API call</td>
    <td>SEND_OTP_API_FAILURE</td>
    <td>SEND_OTP_API_FAILURE</td>
  </tr>
  <tr>
    <td><code>E1670</code></td>
    <td>Card authentication failed at the bank due to invalid CVV (or CVC or Card Security Code)</td>
    <td>Security violation</td>
    <td>ISSUER_RISK_RULE_FAILED</td>
  </tr>
  <tr>
    <td><code>E700</code></td>
    <td>Validation of secure hash failed</td>
    <td>SECURE_HASH_FAILURE</td>
    <td>SECURE_HASH_FAILURE</td>
  </tr>
  <tr>
    <td><code>E300</code></td>
    <td>Card failed 3D authentication as 3 D Secure signatures did not match</td>
    <td>SECURE_3D_PASSWORD_ERROR</td>
    <td>SECURE_3D_PASSWORD_ERROR</td>
  </tr>
  <tr>
    <td><code>E1000</code></td>
    <td>3-D secure authentication failed.</td>
    <td>SECURE_3D_AUTHENTICATION_ERROR_S3A</td>
    <td>SECURE_3D_AUTHENTICATION_ERROR_S3A</td>
  </tr>
  <tr>
    <td><code>E317</code></td>
    <td>Payer could not be authenticated</td>
    <td>SECURE_3D_AUTHENTICATION_ERROR</td>
    <td>SECURE_3D_AUTHENTICATION_ERROR</td>
  </tr>
  <tr>
    <td><code>E1662</code></td>
    <td>ATM PIN monthly limit exceeded for this card. Please retry using OTP or any other payment option.</td>
    <td>SBI_DI_MONTHLY_CARD_LIMIT_EXCEEDED</td>
    <td>SBI_DI_MONTHLY_CARD_LIMIT_EXCEEDED</td>
  </tr>
  <tr>
    <td><code>E1661</code></td>
    <td>ATM PIN daily limit exceeded for this card. Please retry using OTP or any other payment option.</td>
    <td>SBI_DI_DAILY_CARD_LIMIT_EXCEEDED</td>
    <td>SBI_DI_DAILY_CARD_LIMIT_EXCEEDED</td>
  </tr>
  <tr>
    <td><code>E1664</code></td>
    <td>Card blocked by the issuer. Please contact the bank to get it enabled for online transactions.</td>
    <td>SBI_DI_BLOCKED_CARD</td>
    <td>SBI_DI_BLOCKED_CARD</td>
  </tr>
  <tr>
    <td><code>E1615</code></td>
    <td>txn_s2s_flow missing parameter</td>
    <td>S2S_PARAMETER_MISSING</td>
    <td>S2S_PARAMETER_MISSING</td>
  </tr>
  <tr>
    <td><code>E1622</code></td>
    <td>S2S flow not enabled on selected payment gateway</td>
    <td>S2S_NOT_ENABLED_PAYMENTGATEWAY</td>
    <td>S2S_NOT_ENABLED_PAYMENTGATEWAY</td>
  </tr>
  <tr>
    <td><code>E1621</code></td>
    <td>Merchant does not have access to S2S flow</td>
    <td>S2S_NOT_ENABLED_MERCHANT</td>
    <td>S2S_NOT_ENABLED_MERCHANT</td>
  </tr>
  <tr>
    <td><code>E199</code></td>
    <td>Rreq not received from the Network Scheme</td>
    <td>RREQ_NOT_RECEIVED</td>
    <td>RREQ_NOT_RECEIVED</td>
  </tr>
  <tr>
    <td><code>E1654</code></td>
    <td>Route to merchant unavailable</td>
    <td>ROUTE_UNAVAILABLE</td>
    <td>ROUTE_UNAVAILABLE</td>
  </tr>
  <tr>
    <td><code>E4034</code></td>
    <td>REVOKE MANDATE AFTER THE REMITTER UNBLOCKED THE AMOUNT</td>
    <td>REVOKE MANDATE AFTER THE REMITTER UNBLOCKED THE AMOUNT</td>
    <td>REVOKE_MANDATE_AFTER_THE_REMITTER_UNBLOCKED_THE_AMOUNT</td>
  </tr>
  <tr>
    <td><code>E4183</code></td>
    <td>REVERTED</td>
    <td>REVERTED</td>
    <td>REVERTED</td>
  </tr>
  <tr>
    <td><code>E4186</code></td>
    <td>REVERSAL HAS BEEN SENT</td>
    <td>REVERSAL HAS BEEN SENT</td>
    <td>REVERSAL_HAS_BEEN_SENT</td>
  </tr>
  <tr>
    <td><code>E1500</code></td>
    <td>Retry not allowed</td>
    <td>RETRY_NOT_ALLOWED</td>
    <td>RETRY_NOT_ALLOWED</td>
  </tr>
  <tr>
    <td><code>E1626</code></td>
    <td>Restricted card</td>
    <td>RESTRICTED CARD, DECLINE (REMITTER)</td>
    <td>RESTRICTED_CARD_TYPE</td>
  </tr>
  <tr>
    <td><code>E4268</code></td>
    <td>Response ValQR TimeOut</td>
    <td>Response ValQR TimeOut</td>
    <td>Response_ValQR_TimeOut</td>
  </tr>
  <tr>
    <td><code>E9220</code></td>
    <td>Response Received Too Late</td>
    <td>Response Received Too Late</td>
    <td>RESPONSE_RECEIVED_TOO_LATE</td>
  </tr>
  <tr>
    <td><code>E4187</code></td>
    <td>RESPONSE IS ALREADY BEEN SENT</td>
    <td>RESPONSE IS ALREADY BEEN SENT</td>
    <td>RESPONSE_IS_ALREADY_BEEN_SENT</td>
  </tr>
  <tr>
    <td><code>E4184</code></td>
    <td>RESPONSE IS ALREADY BEEN RECEIVED</td>
    <td>RESPONSE IS ALREADY BEEN RECEIVED</td>
    <td>RESPONSE_IS_ALREADY_BEEN_RECEIVED</td>
  </tr>
  <tr>
    <td><code>E4267</code></td>
    <td>Response Activation TimeOut</td>
    <td>Response Activation TimeOut</td>
    <td>Response_Activation_TimeOut</td>
  </tr>
  <tr>
    <td><code>E4279</code></td>
    <td>Transaction declined due to timeout at customer&#x27;s bank</td>
    <td>RESPMANDATE TIMEOUT AT REMITTER END</td>
    <td>RESPMANDATE_TIMEOUT_AT_REMITTER_END</td>
  </tr>
  <tr>
    <td><code>E4278</code></td>
    <td>Transaction failed as mandate setup failed from customer&#x27;s bank</td>
    <td>RESPMANDATE DECLINED BY REMITTER BANK</td>
    <td>RESPMANDATE_DECLINED_BY_REMITTER_BANK</td>
  </tr>
  <tr>
    <td><code>E4283</code></td>
    <td>RESPMANDATE ACK NOT RECEIVED FROM PAYER</td>
    <td>RESPMANDATE ACK NOT RECEIVED FROM PAYER</td>
    <td>RESPMANDATE_ACK_NOT_RECEIVED_FROM_PAYER</td>
  </tr>
  <tr>
    <td><code>E4272</code></td>
    <td>Transaction declined due to timeout at Issuer/Acquirer end</td>
    <td>RESPAUTHMANDATE TIMEOUT</td>
    <td>RESPAUTHMANDATE_TIMEOUT</td>
  </tr>
  <tr>
    <td><code>E4275</code></td>
    <td>RESPAUTHMANDATE NEGATIVE ACK SENT FROM UPI TO PSP</td>
    <td>RESPAUTHMANDATE NEGATIVE ACK SENT FROM UPI TO PSP</td>
    <td>RESPAUTHMANDATE_NEGATIVE_ACK_SENT_FROM_UPI_TO_PSP</td>
  </tr>
  <tr>
    <td><code>E4273</code></td>
    <td>Transaction failed due to mandate request expired</td>
    <td>RESPAUTHMANDATE EXPIRED</td>
    <td>RESPAUTHMANDATE_EXPIRED</td>
  </tr>
  <tr>
    <td><code>E4271</code></td>
    <td>Mandate request declined by the customer</td>
    <td>RESPAUTHMANDATE DECLINED BY PSP</td>
    <td>RESPAUTHMANDATE_DECLINED_BY_PSP</td>
  </tr>
  <tr>
    <td><code>E215</code></td>
    <td>Unknown Error</td>
    <td>RESERVED_USAGE_ERROR</td>
    <td>RESERVED_USAGE_ERROR</td>
  </tr>
  <tr>
    <td><code>E9231</code></td>
    <td>Reserved for National Use</td>
    <td>Reserved for National Use</td>
    <td>RESERVED_FOR_NATIONAL_USE</td>
  </tr>
  <tr>
    <td><code>E4342</code></td>
    <td>REQUESTED FUNCTION NOT SUPPORTED (REMITTER)</td>
    <td>REQUESTED FUNCTION NOT SUPPORTED (REMITTER)</td>
    <td>REQUESTED_FUNCTION_NOT_SUPPORTED_REMITTER</td>
  </tr>
  <tr>
    <td><code>E4343</code></td>
    <td>REQUESTED FUNCTION NOT SUPPORTED (BENEFICIARY)</td>
    <td>REQUESTED FUNCTION NOT SUPPORTED (BENEFICIARY)</td>
    <td>REQUESTED_FUNCTION_NOT_SUPPORTED_BENEFICIARY</td>
  </tr>
  <tr>
    <td><code>E9218</code></td>
    <td>Requested Function not Supported</td>
    <td>Requested Function not Supported</td>
    <td>REQUESTED_FUNCTION_NOT_SUPPORTED</td>
  </tr>
  <tr>
    <td><code>E4200</code></td>
    <td>REQUEST REFUND IS NOT FOUND</td>
    <td>REQUEST REFUND IS NOT FOUND</td>
    <td>REQUEST_REFUND_IS_NOT_FOUND</td>
  </tr>
  <tr>
    <td><code>E4605</code></td>
    <td>Request Processed Successfully</td>
    <td>Request Processed Successfully</td>
    <td>Request_Processed_Successfully</td>
  </tr>
  <tr>
    <td><code>E4198</code></td>
    <td>REQUEST MESSAGE ID IS NOT PRESENT</td>
    <td>REQUEST MESSAGE ID IS NOT PRESENT</td>
    <td>REQUEST_MESSAGE_ID_IS_NOT_PRESENT</td>
  </tr>
  <tr>
    <td><code>E4153</code></td>
    <td>REQUEST IS NOT FOUND</td>
    <td>REQUEST IS NOT FOUND</td>
    <td>REQUEST_IS_NOT_FOUND</td>
  </tr>
  <tr>
    <td><code>E4185</code></td>
    <td>REQUEST IS ALREADY BEEN SENT</td>
    <td>REQUEST IS ALREADY BEEN SENT</td>
    <td>REQUEST_IS_ALREADY_BEEN_SENT</td>
  </tr>
  <tr>
    <td><code>E4608</code></td>
    <td>Request has been timed out</td>
    <td>Request has been timed out</td>
    <td>Request_Has_Been_Timed_Out</td>
  </tr>
  <tr>
    <td><code>E4517</code></td>
    <td>Offline Refund request already raised</td>
    <td>Request has already been initiated for this transaction (&quot;ICICI&quot;</td>
    <td>Request_Has_Already_Been_Initiated_For_This_Transaction_ICICI_Offline_Duplicate_Transaction</td>
  </tr>
  <tr>
    <td><code>E4140</code></td>
    <td>Transaction declined by the bank</td>
    <td>Request Decline by the bank</td>
    <td>Request_Decline_By_The_Bank</td>
  </tr>
  <tr>
    <td><code>E4196</code></td>
    <td>REQUEST DEBIT IS NOT FOUND</td>
    <td>REQUEST DEBIT IS NOT FOUND</td>
    <td>REQUEST_DEBIT_IS_NOT_FOUND</td>
  </tr>
  <tr>
    <td><code>E4195</code></td>
    <td>REQUEST CREDIT IS NOT FOUND</td>
    <td>REQUEST CREDIT IS NOT FOUND</td>
    <td>REQUEST_CREDIT_IS_NOT_FOUND</td>
  </tr>
  <tr>
    <td><code>E4170</code></td>
    <td>REQUEST AUTHORISATION IS NOT FOUND</td>
    <td>REQUEST AUTHORISATION IS NOT FOUND</td>
    <td>REQUEST_AUTHORISATION_IS_NOT_FOUND</td>
  </tr>
  <tr>
    <td><code>E4167</code></td>
    <td>Transaction failed as authorisation acknowledgement not received</td>
    <td>REQUEST AUTHORISATION ACKNOWLEDGEMENT IS NOT</td>
    <td>REQUEST_AUTHORISATION_ACKNOWLEDGEMENT_IS_NOT</td>
  </tr>
  <tr>
    <td><code>E4284</code></td>
    <td>REQMANDATECONFIRMATION ACK NOT RECEIVED FROM PAYER</td>
    <td>REQMANDATECONFIRMATION ACK NOT RECEIVED FROM PAYER</td>
    <td>REQMANDATECONFIRMATION_ACK_NOT_RECEIVED_FROM_PAYER</td>
  </tr>
  <tr>
    <td><code>E4280</code></td>
    <td>REQMANDATE NEGATIVE ACK RECEIVED FROM REMITTER</td>
    <td>REQMANDATE NEGATIVE ACK RECEIVED FROM REMITTER</td>
    <td>REQMANDATE_NEGATIVE_ACK_RECEIVED_FROM_REMITTER</td>
  </tr>
  <tr>
    <td><code>E4277</code></td>
    <td>REQMANDATE ACK NOT RECEIVED FROM REMITTER BANK</td>
    <td>REQMANDATE ACK NOT RECEIVED FROM REMITTER BANK</td>
    <td>REQMANDATE_ACK_NOT_RECEIVED_FROM_REMITTER_BANK</td>
  </tr>
  <tr>
    <td><code>E4274</code></td>
    <td>REQAUTHMANDATE NEGATIVE ACK RECEIVED FROM PSP</td>
    <td>REQAUTHMANDATE NEGATIVE ACK RECEIVED FROM PSP</td>
    <td>REQAUTHMANDATE_NEGATIVE_ACK_RECEIVED_FROM_PSP</td>
  </tr>
  <tr>
    <td><code>E4363</code></td>
    <td>Transaction declined due to customer&#x27;s account blocked or frozen</td>
    <td>REMITTING ACCOUNT BLOCKED/FROZEN</td>
    <td>REMITTING_ACCOUNT_BLOCKED_FROZEN</td>
  </tr>
  <tr>
    <td><code>E4294</code></td>
    <td>Transaction declined due to timeout at Issuer/Customer&#x27;s end</td>
    <td>REMITTER/ISSUER UNAVAILABLE (TIMEOUT)</td>
    <td>REMITTER_ISSUER_UNAVAILABLE_TIMEOUT</td>
  </tr>
  <tr>
    <td><code>E4357</code></td>
    <td>Transaction failed due to customer&#x27;s bank CBS offline</td>
    <td>REMITTER CBS OFFLINE</td>
    <td>REMITTER_CBS_OFFLINE</td>
  </tr>
  <tr>
    <td><code>E4258</code></td>
    <td>REMITTER BANK,VERSION/TAGS SENT NOT SUPPORTED BY BANK</td>
    <td>REMITTER BANK,VERSION/TAGS SENT NOT SUPPORTED BY BANK</td>
    <td>REMITTER_BANK_VERSION_TAGS_SENT_NOT_SUPPORTED_BY_BANK</td>
  </tr>
  <tr>
    <td><code>E4256</code></td>
    <td>REMITTER BANK,REQUEST &amp; RESPONSE HEADER VERSION MISMATCH</td>
    <td>REMITTER BANK,REQUEST &amp; RESPONSE HEADER VERSION MISMATCH</td>
    <td>REMITTER_BANK_REQUEST_RESPONSE_HEADER_VERSION_MISMATCH</td>
  </tr>
  <tr>
    <td><code>E4257</code></td>
    <td>REMITTER BANK,HEADER OR URL VERSION MISMATCHED</td>
    <td>REMITTER BANK,HEADER OR URL VERSION MISMATCHED</td>
    <td>REMITTER_BANK_HEADER_OR_URL_VERSION_MISMATCHED</td>
  </tr>
  <tr>
    <td><code>E4290</code></td>
    <td>Mandate not supported by customer&#x27;s bank</td>
    <td>REMITTER BANK NOT REGISTERED (MANDATE)</td>
    <td>REMITTER_BANK_NOT_REGISTERED_MANDATE</td>
  </tr>
  <tr>
    <td><code>E4177</code></td>
    <td>Debit failed due to technical issue at customer&#x27;s bank</td>
    <td>REMITTER BANK NOT AVAILABLE</td>
    <td>REMITTER_BANK_NOT_AVAILABLE</td>
  </tr>
  <tr>
    <td><code>E4096</code></td>
    <td>REMITTER BANK DOES NOT SUPPORT VERSION MANDATE 2.1</td>
    <td>REMITTER BANK DOES NOT SUPPORT VERSION MANDATE 2.1</td>
    <td>REMITTER_BANK_DOES_NOT_SUPPORT_VERSION_MANDATE_2_1</td>
  </tr>
  <tr>
    <td><code>E4265</code></td>
    <td>REMITTER BANK DOES NOT SUPPORT VERSION</td>
    <td>REMITTER BANK DOES NOT SUPPORT VERSION</td>
    <td>REMITTER_BANK_DOES_NOT_SUPPORT_VERSION</td>
  </tr>
  <tr>
    <td><code>E4009</code></td>
    <td>Transaction failed due to mobile number linked to account is changed</td>
    <td>REGISTERED MOBILE NUMBER LINKED TO THE ACCOUNT HAS BEEN CHANGED/</td>
    <td>REGISTERED_MOBILE_NUMBER_LINKED_TO_THE_ACCOUNT_HAS_BEEN_CHANGED_REMOVED</td>
  </tr>
  <tr>
    <td><code>E348</code></td>
    <td>Transaction declined by the issuer</td>
    <td>Refer to card issuer</td>
    <td>ISSUER_DECLINED</td>
  </tr>
  <tr>
    <td><code>E4649</code></td>
    <td>Ref Url is not valid or proper format. e.g. [http://www.yyy.zzz](http://www.yyy.zzz)</td>
    <td>Ref Url is not valid or proper format. e.g. [http://www.yyy.zzz](http://www.yyy.zzz)</td>
    <td>Ref_Url_Is_Not_Valid_Or_Proper_Format</td>
  </tr>
  <tr>
    <td><code>E1206</code></td>
    <td>Transaction interrupted by pressing back button</td>
    <td>REDIRECTED_BY_BACK_BUTTON</td>
    <td>REDIRECTED_BY_BACK_BUTTON</td>
  </tr>
  <tr>
    <td><code>E4682</code></td>
    <td>Recurrence Payment is in progress</td>
    <td>Recurrence Payment is in progress</td>
    <td>Recurrence_Payment_Is_In_Progress</td>
  </tr>
  <tr>
    <td><code>E4683</code></td>
    <td>Recurrence Payment is already completed</td>
    <td>Recurrence Payment is already completed</td>
    <td>Recurrence_Payment_Is_Already_Completed</td>
  </tr>
  <tr>
    <td><code>E4091</code></td>
    <td>RECURRENCE PATTERN IS ALWAYS ONETIME IF PURPOSE=01</td>
    <td>RECURRENCE PATTERN IS ALWAYS ONETIME IF PURPOSE=01</td>
    <td>RECURRENCE_PATTERN_IS_ALWAYS_ONETIME_IF_PURPOSE_01</td>
  </tr>
  <tr>
    <td><code>E4063</code></td>
    <td>RECURRENCE PATTERN AS WELL AS FOR PAYER INITIATED</td>
    <td>RECURRENCE PATTERN AS WELL AS FOR PAYER INITIATED</td>
    <td>RECURRENCE_PATTERN_AS_WELL_AS_FOR_PAYER_INITIATED</td>
  </tr>
  <tr>
    <td><code>E4106</code></td>
    <td>Transaction failed due to recurrence pattern, value and amount rule mismatch</td>
    <td>RECURRENCE PATTERN AND VALUE MISMATCH (PAYER)</td>
    <td>RECURRENCE_PATTERN_AND_VALUE_MISMATCH_PAYER</td>
  </tr>
  <tr>
    <td><code>E4526</code></td>
    <td>Transaction not found in status check</td>
    <td>Record not found against given parameters</td>
    <td>Record_Not_Found_Against_Given_Parameters</td>
  </tr>
  <tr>
    <td><code>E9229</code></td>
    <td>Reconciliation Totals Reset</td>
    <td>Reconciliation Totals Reset</td>
    <td>RECONCILIATION_TOTALS_RESET</td>
  </tr>
  <tr>
    <td><code>E1656</code></td>
    <td>Reconcile Error</td>
    <td>RECONCILE_ERROR</td>
    <td>RECONCILE_ERROR</td>
  </tr>
  <tr>
    <td><code>E4168</code></td>
    <td>Transaction declined by the customer</td>
    <td>RECEIVED REQUEST AUTHORISATION IS DECLINED</td>
    <td>RECEIVED_REQUEST_AUTHORISATION_IS_DECLINED</td>
  </tr>
  <tr>
    <td><code>E4219</code></td>
    <td>RECEIVED LATE RESPONSE</td>
    <td>RECEIVED LATE RESPONSE</td>
    <td>RECEIVED_LATE_RESPONSE</td>
  </tr>
  <tr>
    <td><code>E4381</code></td>
    <td>RECEIVED LATE RESPONSE</td>
    <td>RECEIVED LATE RESPONSE</td>
    <td>RECEIVED_LATE_RESPONSE_1</td>
  </tr>
  <tr>
    <td><code>E704</code></td>
    <td>Authorization request declined by the bank due to an internal error</td>
    <td>RECEIPT_NUMBER_ERROR</td>
    <td>RECEIPT_NUMBER_ERROR</td>
  </tr>
  <tr>
    <td><code>E4301</code></td>
    <td>Transaction failed as revoke should be allowed for recurring mandate</td>
    <td>Purpose Code=14, Revocable= N ( Revokable tag must always be Y f</td>
    <td>Purpose_Code_14_Revocable_N_Revokable_Tag_Must_Always_Be_Y_For_For_SI__Recurring_Mandate_REMITTER</td>
  </tr>
  <tr>
    <td><code>E4107</code></td>
    <td>Transaction failed as blocking of funds not allowed for recurring mandate</td>
    <td>Purpose code=14, Block fund = Y ( Block Fund must be N always fo</td>
    <td>Purpose_Code_14_Block_Fund_Y_Block_Fund_Must_Be_N_Always_For_SI_Recurring_Mandate_PAYER</td>
  </tr>
  <tr>
    <td><code>E4292</code></td>
    <td>Transaction declined due to timeout at Issuer&#x27;s end</td>
    <td>PSP TIME-OUT</td>
    <td>PSP_TIME_OUT</td>
  </tr>
  <tr>
    <td><code>E4202</code></td>
    <td>PSP REQUEST PAY DEBIT ACKNOWLEDGEMENT NOT RECEIVED</td>
    <td>PSP REQUEST PAY DEBIT ACKNOWLEDGEMENT NOT RECEIVED</td>
    <td>PSP_REQUEST_PAY_DEBIT_ACKNOWLEDGEMENT_NOT_RECEIVED</td>
  </tr>
  <tr>
    <td><code>E4175</code></td>
    <td>PSP REQUEST CREDIT PAY ACKNOWLEDGEMENT IS NOT RECEIVED</td>
    <td>PSP REQUEST CREDIT PAY ACKNOWLEDGEMENT IS NOT RECEIVED</td>
    <td>PSP_REQUEST_CREDIT_PAY_ACKNOWLEDGEMENT_IS_NOT_RECEIVED</td>
  </tr>
  <tr>
    <td><code>E4201</code></td>
    <td>PSP ORGID NOT FOUND</td>
    <td>PSP ORGID NOT FOUND</td>
    <td>PSP_ORGID_NOT_FOUND</td>
  </tr>
  <tr>
    <td><code>E4249</code></td>
    <td>PSP NOT SUPPORTED BY UPI</td>
    <td>PSP NOT SUPPORTED BY UPI</td>
    <td>PSP_NOT_SUPPORTED_BY_UPI</td>
  </tr>
  <tr>
    <td><code>E4658</code></td>
    <td>PSP not found or configured</td>
    <td>PSP not found or configured</td>
    <td>PSP_Not_Found_Or_Configured</td>
  </tr>
  <tr>
    <td><code>E4166</code></td>
    <td>Transaction failed as handle used is not registered</td>
    <td>PSP IS NOT REGISTERED</td>
    <td>PSP_IS_NOT_REGISTERED_NEW</td>
  </tr>
  <tr>
    <td><code>E800</code></td>
    <td>Transaction failed due to error at the merchant&#x27;s end</td>
    <td>PREFERED_GATEWAY_NOT_SET</td>
    <td>PREFERED_GATEWAY_NOT_SET</td>
  </tr>
  <tr>
    <td><code>E4527</code></td>
    <td>Refund failed due to invalid amount</td>
    <td>Please enter valid refund amount</td>
    <td>Please_Enter_Valid_Refund_Amount</td>
  </tr>
  <tr>
    <td><code>E9244</code></td>
    <td>PIN required</td>
    <td>PIN required</td>
    <td>PIN_REQUIRED</td>
  </tr>
  <tr>
    <td><code>E4298</code></td>
    <td>PIN Cred Block is missing (txns &gt; 2000)</td>
    <td>PIN Cred Block is missing (txns &gt; 2000)</td>
    <td>PIN_Cred_Block_Is_Missing_txns__2000</td>
  </tr>
  <tr>
    <td><code>E4299</code></td>
    <td>PIN Cred Block is missing (txns \&lt; 2000 and Seq No = 1)</td>
    <td>PIN Cred Block is missing (txns \&lt; 2000 and Seq No = 1)</td>
    <td>PIN_Cred_Block_Is_Missing_txns__2000_And_Seq_No_1</td>
  </tr>
  <tr>
    <td><code>E310</code></td>
    <td>Card has been classified as lost and has been blocked.</td>
    <td>Pick Up Card</td>
    <td>LOST_CARD</td>
  </tr>
  <tr>
    <td><code>E1907</code></td>
    <td>We are unable to fetch status of transaction right now. Check with merchant for order confirmation</td>
    <td>PHONE_PE_VERIFY_ERROR</td>
    <td>PHONE_PE_VERIFY_ERROR</td>
  </tr>
  <tr>
    <td><code>E1905</code></td>
    <td>Transaction could not be processed due to some internal error</td>
    <td>PHONE_PE_JS_EXCEPTION</td>
    <td>PHONE_PE_JS_EXCEPTION</td>
  </tr>
  <tr>
    <td><code>E1906</code></td>
    <td>Error while initiating payment with PhonePe!</td>
    <td>PHONE_PE_INITIATE_ERROR</td>
    <td>PHONE_PE_INITIATE_ERROR</td>
  </tr>
  <tr>
    <td><code>E1203</code></td>
    <td>You have exceeded your third party funds transfer limit for the day.You cannot transfer any more funds.</td>
    <td>PER TRANSACTION LIMIT EXCEEDED AS SET BY REMITTING MEMBER</td>
    <td>LIMIT_EXCEED</td>
  </tr>
  <tr>
    <td><code>E330</code></td>
    <td>Validation Failure at PG End</td>
    <td>PAYMENT_GATEWAY_VALIDATION_FAILURE</td>
    <td>PAYMENT_GATEWAY_VALIDATION_FAILURE</td>
  </tr>
  <tr>
    <td><code>E4103</code></td>
    <td>Payment validity expired</td>
    <td>Payment validity expired</td>
    <td>Payment_Validity_Expired</td>
  </tr>
  <tr>
    <td><code>E4315</code></td>
    <td>PAYMENT STOPPED BY COURT ORDER</td>
    <td>PAYMENT STOPPED BY COURT ORDER</td>
    <td>PAYMENT_STOPPED_BY_COURT_ORDER</td>
  </tr>
  <tr>
    <td><code>E4326</code></td>
    <td>PAYMENT STOPPED BY ATTACHMENT ORDER BD</td>
    <td>PAYMENT STOPPED BY ATTACHMENT ORDER BD</td>
    <td>PAYMENT_STOPPED_BY_ATTACHMENT_ORDER_BD</td>
  </tr>
  <tr>
    <td><code>E1903</code></td>
    <td>Authorization failed at Bank</td>
    <td>Payment could not be authorised</td>
    <td>AUTHORIZATION_FAILED_BY_BANK</td>
  </tr>
  <tr>
    <td><code>E4030</code></td>
    <td>PAYER/PAYEE.INFO.IDENTITY.TYPE MUST BE PRESENT MINLENGTH 1 MAXLENGTH 20</td>
    <td>PAYER/PAYEE.INFO.IDENTITY.TYPE MUST BE PRESENT MINLENGTH 1 MAXLE</td>
    <td>PAYER_PAYEE_INFO_IDENTITY_TYPE_MUST_BE_PRESENT_MINLENGTH_1_MAXLENGTH_20</td>
  </tr>
  <tr>
    <td><code>E4028</code></td>
    <td>PAYER/PAYEE.INFO MUST BE PRESENT</td>
    <td>PAYER/PAYEE.INFO MUST BE PRESENT</td>
    <td>PAYER_PAYEE_INFO_MUST_BE_PRESENT</td>
  </tr>
  <tr>
    <td><code>E4017</code></td>
    <td>PAYER/PAYEE.DEVICE MUST BE PRESENT</td>
    <td>PAYER/PAYEE.DEVICE MUST BE PRESENT</td>
    <td>PAYER_PAYEE_DEVICE_MUST_BE_PRESENT</td>
  </tr>
  <tr>
    <td><code>E4018</code></td>
    <td>PAYER/PAYEE. DEVICE.TAGS MUST BE PRESENT PAYER/PAYEE.TAG.DEVICE .NAME/VALUE MUST BE PRESENT</td>
    <td>PAYER/PAYEE. DEVICE.TAGS MUST BE PRESENT PAYER/PAYEE.TAG.DEVICE.</td>
    <td>PAYER_PAYEE__DEVICE_TAGS_MUST_BE_PRESENT_PAYER_PAYEE_TAG_DEVICE_NAME_VALUE_MUST_BE_PRESENT</td>
  </tr>
  <tr>
    <td><code>E4254</code></td>
    <td>PAYER/PAYEE PSP,VERSION/TAGS NOT SUPPORTED BY PSP/BANK</td>
    <td>PAYER/PAYEE PSP,VERSION/TAGS NOT SUPPORTED BY PSP/BANK</td>
    <td>PAYER_PAYEE_PSP_VERSION_TAGS_NOT_SUPPORTED_BY_PSP_BANK</td>
  </tr>
  <tr>
    <td><code>E4253</code></td>
    <td>PAYER/PAYEE PSP,REQUEST &amp; RESPONSE HEADER VERSION MISMATCH</td>
    <td>PAYER/PAYEE PSP,REQUEST &amp; RESPONSE HEADER VERSION MISMATCH</td>
    <td>PAYER_PAYEE_PSP_REQUEST_RESPONSE_HEADER_VERSION_MISMATCH</td>
  </tr>
  <tr>
    <td><code>E4252</code></td>
    <td>PAYER/PAYEE PSP,HEADER OR URL VERSION MISMATCHED</td>
    <td>PAYER/PAYEE PSP,HEADER OR URL VERSION MISMATCHED</td>
    <td>PAYER_PAYEE_PSP_HEADER_OR_URL_VERSION_MISMATCHED</td>
  </tr>
  <tr>
    <td><code>E4032</code></td>
    <td>PAYER/PAYEE .INFO.RATING WHITELISTED MUST BE PRESENT MINLENGTH 1 MAXLENGTH 5</td>
    <td>PAYER/PAYEE .INFO.RATING WHITELISTED MUST BE PRESENT MINLENGTH 1</td>
    <td>PAYER_PAYEE_INFO_RATING_WHITELISTED_MUST_BE_PRESENT_MINLENGTH_1_MAXLENGTH_5</td>
  </tr>
  <tr>
    <td><code>E4031</code></td>
    <td>PAYER/PAYEE .INFO.IDENTITY VERIFIEDNAME MUST BE PRESENT ALPHANUMERIC MINLENGTH 1 MAXLENGTH 99</td>
    <td>PAYER/PAYEE .INFO.IDENTITY VERIFIEDNAME MUST BE PRESENT ALPHANUM</td>
    <td>PAYER_PAYEE_INFO_IDENTITY_UERIFIEDNAME_MUST_BE_PRESENT_ALPHANUMERIC_MINLENGTH_1_MAXLENGTH_99</td>
  </tr>
  <tr>
    <td><code>E4029</code></td>
    <td>PAYER/PAYEE .INFO.IDENTITY MUST BE PRESENT</td>
    <td>PAYER/PAYEE .INFO.IDENTITY MUST BE PRESENT</td>
    <td>PAYER_PAYEE_INFO_IDENTITY_MUST_BE_PRESENT</td>
  </tr>
  <tr>
    <td><code>E4136</code></td>
    <td>PAYER.TYPE MUST BE PRESENT/VALID</td>
    <td>PAYER.TYPE MUST BE PRESENT/VALID</td>
    <td>PAYER_TYPE_MUST_BE_PRESENT_VALID</td>
  </tr>
  <tr>
    <td><code>E4135</code></td>
    <td>PAYER.SEQNUM NUMERIC MINLENGTH 1 MAXLENGTH 3</td>
    <td>PAYER.SEQNUM NUMERIC MINLENGTH 1 MAXLENGTH 3</td>
    <td>PAYER_SEQNUM_NUMERIC_MINLENGTH_1_MAXLENGTH_3</td>
  </tr>
  <tr>
    <td><code>E4134</code></td>
    <td>PAYER.NAME ALPHANUMERIC MINLENGTH 1 MAXLENGTH 99</td>
    <td>PAYER.NAME ALPHANUMERIC MINLENGTH 1 MAXLENGTH 99</td>
    <td>PAYER_NAME_ALPHANUMERIC_MINLENGTH_1_MAXLENGTH_99</td>
  </tr>
  <tr>
    <td><code>E4026</code></td>
    <td>PAYER.INFO MUST BE PRESENT</td>
    <td>PAYER.INFO MUST BE PRESENT</td>
    <td>PAYER_INFO_MUST_BE_PRESENT</td>
  </tr>
  <tr>
    <td><code>E4137</code></td>
    <td>PAYER.CODE NUMERIC OF LENGTH 4</td>
    <td>PAYER.CODE NUMERIC OF LENGTH 4</td>
    <td>PAYER_CODE_NUMERIC_OF_LENGTH_4</td>
  </tr>
  <tr>
    <td><code>E4133</code></td>
    <td>PAYER.ADDR MUST BE VALID VPA MAXLENGTH 255</td>
    <td>PAYER.ADDR MUST BE VALID VPA MAXLENGTH 255</td>
    <td>PAYER_ADDR_MUST_BE_VALID_VPA_MAXLENGTH_255</td>
  </tr>
  <tr>
    <td><code>E4117</code></td>
    <td>Transaction failed as payer details are not correct in mandate</td>
    <td>PAYER VPA IS INCORRECT (PAYER)</td>
    <td>PAYER_VPA_IS_INCORRECT_PAYER</td>
  </tr>
  <tr>
    <td><code>E4288</code></td>
    <td>PAYER PSP NOT REGISTERED</td>
    <td>PAYER PSP NOT REGISTERED</td>
    <td>PAYER_PSP_NOT_REGISTERED</td>
  </tr>
  <tr>
    <td><code>E4285</code></td>
    <td>PAYER PSP NOT AVAILABLE</td>
    <td>PAYER PSP NOT AVAILABLE</td>
    <td>PAYER_PSP_NOT_AVAILABLE</td>
  </tr>
  <tr>
    <td><code>E4264</code></td>
    <td>PAYER PSP DOES NOT SUPPORTS VERSION</td>
    <td>PAYER PSP DOES NOT SUPPORTS VERSION</td>
    <td>PAYER_PSP_DOES_NOT_SUPPORTS_VERSION</td>
  </tr>
  <tr>
    <td><code>E4094</code></td>
    <td>PAYER PSP DOES NOT SUPPORT VERSION MANDATE 2.1</td>
    <td>PAYER PSP DOES NOT SUPPORT VERSION MANDATE 2.1</td>
    <td>PAYER_PSP_DOES_NOT_SUPPORT_VERSION_MANDATE_2_1</td>
  </tr>
  <tr>
    <td><code>E4295</code></td>
    <td>Transaction failed as vpa is not valid/expired</td>
    <td>PAYER PROFILE DOES NOT EXIST (DE REGISTRATION/VPA REMOVED/UPDATE</td>
    <td>EXPIRED_VIRTUAL_ADDRESS</td>
  </tr>
  <tr>
    <td><code>E4132</code></td>
    <td>PAYER NOT PRESENT</td>
    <td>PAYER NOT PRESENT</td>
    <td>PAYER_NOT_PRESENT</td>
  </tr>
  <tr>
    <td><code>E4120</code></td>
    <td>Modification not allowed by merchant for payer initiated mandate</td>
    <td>PAYER INITIATED MANDATE CANNOT BE MODIFIED BY PAYEE</td>
    <td>PAYER_INITIATED_MANDATE_CANNOT_BE_MODIFIED_BY_PAYEE</td>
  </tr>
  <tr>
    <td><code>E4210</code></td>
    <td>PAYER INFO DIFFERS FROM ORIGINAL REQUEST</td>
    <td>PAYER INFO DIFFERS FROM ORIGINAL REQUEST</td>
    <td>PAYER_INFO_DIFFERS_FROM_ORIGINAL_REQUEST</td>
  </tr>
  <tr>
    <td><code>E4211</code></td>
    <td>PAYER INFO DIFFERS FROM ORIGINAL REQUEST</td>
    <td>PAYER INFO DIFFERS FROM ORIGINAL REQUEST</td>
    <td>PAYER_INFO_DIFFERS_FROM_ORIGINAL_REQUEST_1</td>
  </tr>
  <tr>
    <td><code>E4050</code></td>
    <td>PAYER AND PAYEE TOTAL AMOUNT NOT MATCHING</td>
    <td>PAYER AND PAYEE TOTAL AMOUNT NOT MATCHING</td>
    <td>PAYER_AND_PAYEE_TOTAL_AMOUNT_NOT_MATCHING</td>
  </tr>
  <tr>
    <td><code>E4138</code></td>
    <td>Transaction failed as payer and payee account cannot be same</td>
    <td>PAYER AND PAYEE ACCOUNT SHOULD NOT BE EQUAL</td>
    <td>PAYER_AND_PAYEE_ACCOUNT_SHOULD_NOT_BE_EQUAL</td>
  </tr>
  <tr>
    <td><code>E4052</code></td>
    <td>PAYER AMOUNT SHOULD BE GREATER THAN TOTAL PAYEE AMOUNT</td>
    <td>PAYER AMOUNT SHOULD BE GREATER THAN TOTAL PAYEE AMOUNT</td>
    <td>PAYER_AMOUNT_SHOULD_BE_GREATER_THAN_TOTAL_PAYEE_AMOUNT</td>
  </tr>
  <tr>
    <td><code>E4222</code></td>
    <td>PAYER ACCOUNT MISMATCH</td>
    <td>PAYER ACCOUNT MISMATCH</td>
    <td>PAYER_ACCOUNT_MISMATCH</td>
  </tr>
  <tr>
    <td><code>E4125</code></td>
    <td>Transaction declined as customer account has changed</td>
    <td>PAYER ACCOUNT HAS CHANGED (PAYER)</td>
    <td>PAYER_ACCOUNT_HAS_CHANGED_PAYER</td>
  </tr>
  <tr>
    <td><code>E4048</code></td>
    <td>PAYER &amp; PAYEE TOTAL AMOUNT NOT MATCHING</td>
    <td>PAYER &amp; PAYEE TOTAL AMOUNT NOT MATCHING</td>
    <td>PAYER_PAYEE_TOTAL_AMOUNT_NOT_MATCHING</td>
  </tr>
  <tr>
    <td><code>E4006</code></td>
    <td>PAYEES NOT PRESENT</td>
    <td>PAYEES NOT PRESENT</td>
    <td>PAYEES_NOT_PRESENT</td>
  </tr>
  <tr>
    <td><code>E4008</code></td>
    <td>PAYEE.ADDR MUST BE VALID VPA MAXLENGTH 255</td>
    <td>PAYEE.ADDR MUST BE VALID VPA MAXLENGTH 255</td>
    <td>PAYEE_ADDR_MUST_BE_UALID_UPA_MAXLENGTH_255</td>
  </tr>
  <tr>
    <td><code>E4325</code></td>
    <td>Transaction declined as merchant vpa is not correct</td>
    <td>PAYEE VPA IS INCORRECT (REMITTER)</td>
    <td>PAYEE_VPA_IS_INCORRECT_REMITTER</td>
  </tr>
  <tr>
    <td><code>E4113</code></td>
    <td>Transaction failed as payee details are not correct in mandate</td>
    <td>PAYEE VPA IS INCORRECT (PAYER)</td>
    <td>PAYEE_VPA_IS_INCORRECT_PAYER</td>
  </tr>
  <tr>
    <td><code>E4242</code></td>
    <td>PAYEE VPA AADHAAR OR IIN VPA IS DISABLED</td>
    <td>PAYEE VPA AADHAAR OR IIN VPA IS DISABLED</td>
    <td>PAYEE_VPA_AADHAAR_OR_IIN_VPA_IS_DISABLED</td>
  </tr>
  <tr>
    <td><code>E4244</code></td>
    <td>PAYEE VPA AADHAAR OR IIN VPA IS DISABLED</td>
    <td>PAYEE VPA AADHAAR OR IIN VPA IS DISABLED</td>
    <td>PAYEE_VPA_AADHAAR_OR_IIN_VPA_IS_DISABLED_1</td>
  </tr>
  <tr>
    <td><code>E4289</code></td>
    <td>PAYEE PSP NOT REGISTERED</td>
    <td>PAYEE PSP NOT REGISTERED</td>
    <td>PAYEE_PSP_NOT_REGISTERED</td>
  </tr>
  <tr>
    <td><code>E4286</code></td>
    <td>PAYEE PSP NOT AVAILABLE</td>
    <td>PAYEE PSP NOT AVAILABLE</td>
    <td>PAYEE_PSP_NOT_AVAILABLE</td>
  </tr>
  <tr>
    <td><code>E4095</code></td>
    <td>PAYEE PSP DOES NOT SUPPORT VERSION MANDATE 2.1</td>
    <td>PAYEE PSP DOES NOT SUPPORT VERSION MANDATE 2.1</td>
    <td>PAYEE_PSP_DOES_NOT_SUPPORT_VERSION_MANDATE_2_1</td>
  </tr>
  <tr>
    <td><code>E4038</code></td>
    <td>PAYEE PSP DOES NOT SUPPORT VERSION 2</td>
    <td>PAYEE PSP DOES NOT SUPPORT VERSION 2</td>
    <td>PAYEE_PSP_DOES_NOT_SUPPORT_VERSION_2</td>
  </tr>
  <tr>
    <td><code>E4007</code></td>
    <td>PAYEE NOT PRESENT</td>
    <td>PAYEE NOT PRESENT</td>
    <td>PAYEE_NOT_PRESENT</td>
  </tr>
  <tr>
    <td><code>E4143</code></td>
    <td>Transaction failed as merchant is reported SPAM by the customer</td>
    <td>PAYEE IS REPORTED AS SPAM UNDER RULE 1</td>
    <td>PAYEE_IS_REPORTED_AS_SPAM_UNDER_RULE_1</td>
  </tr>
  <tr>
    <td><code>E4130</code></td>
    <td>Modification not allowed by payer for merchant initiated mandate</td>
    <td>PAYEE INITIATED MANDATE CANNOT BE MODIFIED BY PAYER</td>
    <td>PAYEE_INITIATED_MANDATE_CANNOT_BE_MODIFIED_BY_PAYER</td>
  </tr>
  <tr>
    <td><code>E4047</code></td>
    <td>PAYEE AMOUNTCUR IS INVALID</td>
    <td>PAYEE AMOUNTCUR IS INVALID</td>
    <td>PAYEE_AMOUNTCUR_IS_INVALID</td>
  </tr>
  <tr>
    <td><code>E4206</code></td>
    <td>PAYEE AMOUNT DIFFERS FROM ORIGINAL REQUEST</td>
    <td>PAYEE AMOUNT DIFFERS FROM ORIGINAL REQUEST</td>
    <td>PAYEE_AMOUNT_DIFFERS_FROM_ORIGINAL_REQUEST</td>
  </tr>
  <tr>
    <td><code>E4207</code></td>
    <td>PAYEE AMOUNT DIFFERS FROM ORIGINAL REQUEST</td>
    <td>PAYEE AMOUNT DIFFERS FROM ORIGINAL REQUEST</td>
    <td>PAYEE_AMOUNT_DIFFERS_FROM_ORIGINAL_REQUEST_1</td>
  </tr>
  <tr>
    <td><code>E4046</code></td>
    <td>PAYEE AMOUNT CUR MUST BE CONSISTENT</td>
    <td>PAYEE AMOUNT CUR MUST BE CONSISTENT</td>
    <td>PAYEE_AMOUNT_CUR_MUST_BE_CONSISTENT</td>
  </tr>
  <tr>
    <td><code>E4208</code></td>
    <td>PAYEE ADDRESS DIFFERS FROM ORIGINAL REQUEST</td>
    <td>PAYEE ADDRESS DIFFERS FROM ORIGINAL REQUEST</td>
    <td>PAYEE_ADDRESS_DIFFERS_FROM_ORIGINAL_REQUEST</td>
  </tr>
  <tr>
    <td><code>E4209</code></td>
    <td>PAYEE ADDRESS DIFFERS FROM ORIGINAL REQUEST</td>
    <td>PAYEE ADDRESS DIFFERS FROM ORIGINAL REQUEST</td>
    <td>PAYEE_ADDRESS_DIFFERS_FROM_ORIGINAL_REQUEST_1</td>
  </tr>
  <tr>
    <td><code>E4223</code></td>
    <td>PAYEE ACCOUNT MISMATCH</td>
    <td>PAYEE ACCOUNT MISMATCH</td>
    <td>PAYEE_ACCOUNT_MISMATCH</td>
  </tr>
  <tr>
    <td><code>E326</code></td>
    <td>Authentication failed due to invalid password.</td>
    <td>PASSWORD_ERROR</td>
    <td>PASSWORD_ERROR</td>
  </tr>
  <tr>
    <td><code>E4003</code></td>
    <td>PARTIAL REVERSAL</td>
    <td>PARTIAL REVERSAL</td>
    <td>PARTIAL_REVERSAL</td>
  </tr>
  <tr>
    <td><code>E4141</code></td>
    <td>Transaction failed as partial debit request timeout at customer&#x27;s bank</td>
    <td>PARTIAL DEBIT REVERSAL TIMEOUT</td>
    <td>PARTIAL_DEBIT_REVERSAL_TIMEOUT</td>
  </tr>
  <tr>
    <td><code>E1648</code></td>
    <td>Partial Approval</td>
    <td>Partial amount was approved</td>
    <td>PARTIAL_APPROVAL</td>
  </tr>
  <tr>
    <td><code>E9202</code></td>
    <td>Partial Amount Approved</td>
    <td>Partial Amount Approved</td>
    <td>PARTIAL_AMOUNT_APPROVED</td>
  </tr>
  <tr>
    <td><code>E1606</code></td>
    <td>Transaction failed due to user pressing refresh button.</td>
    <td>PAGE_REFRESHED_BY_USER</td>
    <td>PAGE_REFRESHED_BY_USER</td>
  </tr>
  <tr>
    <td><code>E1610</code></td>
    <td>Transaction failed. Page expired due to no user input.</td>
    <td>PAGE_EXPIRED</td>
    <td>PAGE_EXPIRED</td>
  </tr>
  <tr>
    <td><code>E9246</code></td>
    <td>Over Daily Limit</td>
    <td>Over Daily Limit</td>
    <td>OVER_DAILY_LIMIT</td>
  </tr>
  <tr>
    <td><code>E2404</code></td>
    <td>OTP Validation Failed</td>
    <td>OTP_VALIDATION_FAILED</td>
    <td>OTP_VALIDATION_FAILED</td>
  </tr>
  <tr>
    <td><code>E1604</code></td>
    <td>Transaction failed due to incorrect user action.</td>
    <td>OTP_MAX_RESEND_ATTEMPT</td>
    <td>OTP_MAX_RESEND_ATTEMPT</td>
  </tr>
  <tr>
    <td><code>E1601</code></td>
    <td>Customer Authentication failed due to incorrect OTP.</td>
    <td>OTP_MAX_LIMIT_EXCEEDED</td>
    <td>OTP_MAX_LIMIT_EXCEEDED</td>
  </tr>
  <tr>
    <td><code>E4388</code></td>
    <td>OTP TRANSACTION LIMIT EXCEEDED</td>
    <td>OTP TRANSACTION LIMIT EXCEEDED</td>
    <td>OTP_TRANSACTION_LIMIT_EXCEEDED</td>
  </tr>
  <tr>
    <td><code>E4387</code></td>
    <td>OTP EXPIRED</td>
    <td>OTP EXPIRED</td>
    <td>OTP_EXPIRED</td>
  </tr>
  <tr>
    <td><code>E4263</code></td>
    <td>OTHER BANK/PSP IS NOT SUPPORTED IN 2 VERSION</td>
    <td>OTHER BANK/PSP IS NOT SUPPORTED IN 2 VERSION</td>
    <td>OTHER_BANK_PSP_IS_NOT_SUPPORTED_IN_2_VERSION</td>
  </tr>
  <tr>
    <td><code>E4282</code></td>
    <td>ORIGINAL REQMANDATE NOT FOUND</td>
    <td>ORIGINAL REQMANDATE NOT FOUND</td>
    <td>ORIGINAL_REQMANDATE_NOT_FOUND</td>
  </tr>
  <tr>
    <td><code>E4276</code></td>
    <td>ORIGINAL REQAUTHMANDATE NOT FOUND</td>
    <td>ORIGINAL REQAUTHMANDATE NOT FOUND</td>
    <td>ORIGINAL_REQAUTHMANDATE_NOT_FOUND</td>
  </tr>
  <tr>
    <td><code>E9253</code></td>
    <td>Amount Incorrect / Mismatch</td>
    <td>Original Amount Incorrect</td>
    <td>AMOUNT_INCORRECT_MISMATCH</td>
  </tr>
  <tr>
    <td><code>E1668</code></td>
    <td>Failing as no gateway found for One Click transaction</td>
    <td>ONE_CLICK_PG * SELECTION_FAILED</td>
    <td>ONE_CLICK_PG_SELECTION_FAILED</td>
  </tr>
  <tr>
    <td><code>E1667</code></td>
    <td>Failing as One Click only option was used and data validation checks failed</td>
    <td>ONE_CLICK_DATA * VALIDATION_FAILED</td>
    <td>ONE_CLICK_DATA_VALIDATION_FAILED</td>
  </tr>
  <tr>
    <td><code>E1666</code></td>
    <td>Failing as One Click only option was used and transaction failed in authentication</td>
    <td>ONE_CLICK_AUTHENTICATION * FAILED</td>
    <td>ONE_CLICK_AUTHENTICATION_FAILED</td>
  </tr>
  <tr>
    <td><code>E4049</code></td>
    <td>ONE OR MORE PAYEE AMOUNT IS MISSING</td>
    <td>ONE OR MORE PAYEE AMOUNT IS MISSING</td>
    <td>ONE_OR_MORE_PAYEE_AMOUNT_IS_MISSING</td>
  </tr>
  <tr>
    <td><code>E9250</code></td>
    <td>Offline Approved</td>
    <td>Offline Approved</td>
    <td>OFFLINE_APPROVED</td>
  </tr>
  <tr>
    <td><code>E1800</code></td>
    <td>The transaction cannot be processed as discount given exceeds the allowed limit. If money is debited from your account then it will be auto refunded. Please try again</td>
    <td>OFFER_AMOUNT_EXCEEDED * DURING_TRANSACTION</td>
    <td>OFFER_AMOUNT_EXCEEDED_DURING_TRANSACTION</td>
  </tr>
  <tr>
    <td><code>E1303</code></td>
    <td>Transaction declined due to technical failure</td>
    <td>OBJECT_CREATION_FAILED</td>
    <td>OBJECT_CREATION_FAILED</td>
  </tr>
  <tr>
    <td><code>E4205</code></td>
    <td>NUMBER OF PAYEES DIFFERS FROM ORIGINAL REQUEST</td>
    <td>NUMBER OF PAYEES DIFFERS FROM ORIGINAL REQUEST</td>
    <td>NUMBER_OF_PAYEES_DIFFERS_FROM_ORIGINAL_REQUEST</td>
  </tr>
  <tr>
    <td><code>E4312</code></td>
    <td>Transaction failed as number of mandates allowed exceeded</td>
    <td>NUMBER OF MANDATES ALLOWED ON THIS ACCOUNT HAS EXCEEDED ISSUER&#x27;S</td>
    <td>NUMBER_OF_MANDATES_ALLOWED_ON_THIS_ACCOUNT_HAS_EXCEEDED_ISSUER_S_LIMIT_BD_OPTIONAL_AS_PER_BANKS_POLICY</td>
  </tr>
  <tr>
    <td><code>E4247</code></td>
    <td>NULL ACK RECEIVED BY UPI FOR META TRANSACTION</td>
    <td>NULL ACK RECEIVED BY UPI FOR META TRANSACTION</td>
    <td>NULL_ACK_RECEIVED_BY_UPI_FOR_META_TRANSACTION</td>
  </tr>
  <tr>
    <td><code>E1618</code></td>
    <td>No form post variables found [S2S Flow]</td>
    <td>NO_FORM_POST * VARS_S2SFLOW</td>
    <td>NO_FORM_POST_VARS_S2SFLOW</td>
  </tr>
  <tr>
    <td><code>E803</code></td>
    <td>Payment gateway seems to be down at this moment.</td>
    <td>NO_ELIGIBLE_PG</td>
    <td>NO_ELIGIBLE_PG</td>
  </tr>
  <tr>
    <td><code>E222</code></td>
    <td>Debit account number is not received in transaction response</td>
    <td>NO_DEBIT_ACCOUNT * NUMBER</td>
    <td>NO_DEBIT_ACCOUNT_NUMBER</td>
  </tr>
  <tr>
    <td><code>E221</code></td>
    <td>Bank reference number is not received in transaction response</td>
    <td>NO_BANK_REFERENCE * NUMBER</td>
    <td>NO_BANK_REFERENCE_NUMBER</td>
  </tr>
  <tr>
    <td><code>E1624</code></td>
    <td>No Active Authentication Option Eligible</td>
    <td>NO_ACTIVE_PAYMENT * ELIGIBLE</td>
    <td>NO_ACTIVE_PAYMENT_ELIGIBLE</td>
  </tr>
  <tr>
    <td><code>E2402</code></td>
    <td>The customer does not have an active credit line to book a consumer loan</td>
    <td>NO_ACTIVE_CREDIT_LINE * WITH_THE_CUSTOMER</td>
    <td>NO_ACTIVE_CREDIT_LINE_WITH_THE_CUSTOMER</td>
  </tr>
  <tr>
    <td><code>E1650</code></td>
    <td>No action taken</td>
    <td>NO_ACTION_TAKEN</td>
    <td>NO_ACTION_TAKEN</td>
  </tr>
  <tr>
    <td><code>E342</code></td>
    <td>Transaction not initiated</td>
    <td>NOT_INITIATED</td>
    <td>NOT_INITIATED</td>
  </tr>
  <tr>
    <td><code>E1609</code></td>
    <td>Transaction declined due to the registered mobile number being international. It should be a domestic number to process the transaction.</td>
    <td>NOT_DOMESTIC_NUMBER</td>
    <td>NOT_DOMESTIC_NUMBER</td>
  </tr>
  <tr>
    <td><code>E343</code></td>
    <td>Transaction not approved</td>
    <td>NOT_APPROVED</td>
    <td>NOT_APPROVED</td>
  </tr>
  <tr>
    <td><code>E347</code></td>
    <td>Transaction failed because of non whitelisted domain</td>
    <td>NON_WHITELISTED_DOMAIN</td>
    <td>NON_WHITELISTED_DOMAIN</td>
  </tr>
  <tr>
    <td><code>E1616</code></td>
    <td>Non-seamless not allowed in S2S Flow</td>
    <td>NONSEAMLESS_NOT * ALLOWED_S2SFLOW</td>
    <td>NONSEAMLESS_NOT_ALLOWED_S2SFLOW</td>
  </tr>
  <tr>
    <td><code>E9252</code></td>
    <td>The customer&#x27;s card issuer has declined the transaction as the account type selected is not valid for this credit card number.</td>
    <td>No Universal Account</td>
    <td>NO_UNIVERSAL_ACCOUNT</td>
  </tr>
  <tr>
    <td><code>E4176</code></td>
    <td>Transaction failed as no response received from merchant/customer</td>
    <td>NO RESPONSE FROM PSP</td>
    <td>NO_RESPONSE_FROM_PSP</td>
  </tr>
  <tr>
    <td><code>E4522</code></td>
    <td>Refund failed due to no response from Customer&#x27;s bank</td>
    <td>No response from Beneficiary Bank</td>
    <td>No_Response_From_Beneficiary_Bank</td>
  </tr>
  <tr>
    <td><code>E4101</code></td>
    <td>Transaction failed due to technical issue at Issuer/Acquirer end</td>
    <td>NO ORIGINAL REQUEST FOUND DURING DEBIT/CREDIT BD</td>
    <td>NO_ORIGINAL_REQUEST_FOUND_DURING_DEBIT_CREDIT_BD</td>
  </tr>
  <tr>
    <td><code>E4680</code></td>
    <td>No Mandate data found to Modify</td>
    <td>No Mandate data found to Modify</td>
    <td>No_Mandate_Data_Found_To_Modify</td>
  </tr>
  <tr>
    <td><code>E4356</code></td>
    <td>NO FINANCIAL ADDRESS RECORD FOUND</td>
    <td>NO FINANCIAL ADDRESS RECORD FOUND</td>
    <td>NO_FINANCIAL_ADDRESS_RECORD_FOUND</td>
  </tr>
  <tr>
    <td><code>E9224</code></td>
    <td>No Envelope Inserted</td>
    <td>No Envelope Inserted</td>
    <td>NO_ENVELOPE_INSERTED</td>
  </tr>
  <tr>
    <td><code>E4346</code></td>
    <td>Transaction failed due to no card details from customer&#x27;s bank</td>
    <td>NO CARD RECORD (REMITTER)</td>
    <td>NO_CARD_RECORD_REMITTER</td>
  </tr>
  <tr>
    <td><code>E4347</code></td>
    <td>Transaction failed due to no card details from acquirer&#x27;s bank</td>
    <td>NO CARD RECORD (BENEFICIARY)</td>
    <td>NO_CARD_RECORD_BENEFICIARY</td>
  </tr>
  <tr>
    <td><code>E4533</code></td>
    <td>No active mandates found</td>
    <td>No Approved Mandates are available</td>
    <td>No_Approved_Mandates_Are_Available</td>
  </tr>
  <tr>
    <td><code>E4002</code></td>
    <td>NO ACTION TAKEN (FULL REVERSAL)</td>
    <td>NO ACTION TAKEN (FULL REVERSAL)</td>
    <td>NO_ACTION_TAKEN_FULL_REVERSAL</td>
  </tr>
  <tr>
    <td><code>E9207</code></td>
    <td>No Action Taken</td>
    <td>No Action Taken</td>
    <td>NO_ACTION_TAKEN_</td>
  </tr>
  <tr>
    <td><code>E211</code></td>
    <td>The Bank servers are unreachable over the network</td>
    <td>NETWORK_ERROR</td>
    <td>NETWORK_ERROR</td>
  </tr>
  <tr>
    <td><code>E801</code></td>
    <td>Netbanking option was temporarily not available so set as bounced.</td>
    <td>NETBANKING_GATEWAY * DOWN</td>
    <td>NETBANKING_GATEWAY_DOWN</td>
  </tr>
  <tr>
    <td><code>E1204</code></td>
    <td>Transaction Failed at bank end.</td>
    <td>NETBANKING_AUTHENTICATION * ERROR</td>
    <td>NETBANKING_AUTHENTICATION_ERROR</td>
  </tr>
  <tr>
    <td><code>E4152</code></td>
    <td>Transaction failed due to debit limit on customer exceeded</td>
    <td>NET DEBIT CAP IS EXCEEDED</td>
    <td>NET_DEBIT_CAP_IS_EXCEEDED</td>
  </tr>
  <tr>
    <td><code>E4248</code></td>
    <td>NEGATIVE ACK RECEIVED BY UPI FOR META TRANSACTION</td>
    <td>NEGATIVE ACK RECEIVED BY UPI FOR META TRANSACTION</td>
    <td>NEGATIVE_ACK_RECEIVED_BY_UPI_FOR_META_TRANSACTION</td>
  </tr>
  <tr>
    <td><code>E4314</code></td>
    <td>Transaction failed as debit not allowed</td>
    <td>NATURE OF DEBIT NOT ALLOWED IN ACCOUNT TYPE</td>
    <td>NATURE_OF_DEBIT_NOT_ALLOWED_IN_ACCOUNT_TYPE</td>
  </tr>
  <tr>
    <td><code>E4525</code></td>
    <td>Multiple transactions found in status check</td>
    <td>Multiple transactions against given parameter</td>
    <td>Multiple_Transactions_Against_Given_Parameter</td>
  </tr>
  <tr>
    <td><code>E4005</code></td>
    <td>Transaction failed due to MPIN not set by customer</td>
    <td>MPIN NOT SET BY CUSTOMER</td>
    <td>MPIN_NOT_SET_BY_CUSTOMER</td>
  </tr>
  <tr>
    <td><code>E4051</code></td>
    <td>MORE THAN ONE PAYEE AMOUNT IS MISSING</td>
    <td>MORE THAN ONE PAYEE AMOUNT IS MISSING</td>
    <td>MORE_THAN_ONE_PAYEE_AMOUNT_IS_MISSING</td>
  </tr>
  <tr>
    <td><code>E4012</code></td>
    <td>MOBILE NUMBER REGISTERED WITH MULTIPLE CUSTOMER IDS</td>
    <td>MOBILE NUMBER REGISTERED WITH MULTIPLE CUSTOMER IDS</td>
    <td>MOBILE_NUMBER_REGISTERED_WITH_MULTIPLE_CUSTOMER_IDS</td>
  </tr>
  <tr>
    <td><code>E9221</code></td>
    <td>Mobile number record not found / mis-match</td>
    <td>Mobile number record not found / mis-match</td>
    <td>MOBILE_NUMBER_RECORD_NOT_FOUND</td>
  </tr>
  <tr>
    <td><code>E4224</code></td>
    <td>MOBILE BANKING REGISTRATION FORMAT NOT SUPPORTED BY THE ISSUER BANK</td>
    <td>MOBILE BANKING REGISTRATION FORMAT NOT SUPPORTED BY THE ISSUER B</td>
    <td>MOBILE_BANKING_REGISTRATION_FORMAT_NOT_SUPPORTED_BY_THE_ISSUER_BANK</td>
  </tr>
  <tr>
    <td><code>E1700</code></td>
    <td>Term URL is missing in the request</td>
    <td>MISSING_TERM_URL</td>
    <td>MISSING_TERM_URL</td>
  </tr>
  <tr>
    <td><code>E1644</code></td>
    <td>Empty Otp Received</td>
    <td>MISSING_OTP</td>
    <td>MISSING_OTP</td>
  </tr>
  <tr>
    <td><code>E226</code></td>
    <td>Security Signature missing or mismatched</td>
    <td>MISSING_MISMATCHED_SIGNATURE</td>
    <td>MISSING_MISMATCHED_SIGNATURE</td>
  </tr>
  <tr>
    <td><code>E1651</code></td>
    <td>Mismatch in retrieval reference number</td>
    <td>MISMATCH_RETRIEVAL_REFERENCE_NUMBER</td>
    <td>MISMATCH_RETRIEVAL_REFERENCE_NUMBER</td>
  </tr>
  <tr>
    <td><code>E4011</code></td>
    <td>MISMATCH IN PAYMENT DETAILS</td>
    <td>MISMATCH IN PAYMENT DETAILS</td>
    <td>MISMATCH_IN_PAYMENT_DETAILS</td>
  </tr>
  <tr>
    <td><code>E4204</code></td>
    <td>MESSAGE INTEGRITY FAILED DUE TO ORGID MISMATCH</td>
    <td>MESSAGE INTEGRITY FAILED DUE TO ORGID MISMATCH</td>
    <td>MESSAGE_INTEGRITY_FAILED_DUE_TO_ORGID_MISMATCH</td>
  </tr>
  <tr>
    <td><code>E346</code></td>
    <td>Merchant Not Eligible for this transaction</td>
    <td>MERCHANT_NOT_ELIGIBLE</td>
    <td>MERCHANT_NOT_ELIGIBLE</td>
  </tr>
  <tr>
    <td><code>E4666</code></td>
    <td>Merchant Account details not found or configured</td>
    <td>Merchant_Account_Details * Not_Found_Or_Configured</td>
    <td>Merchant_Account_Details_Not_Found_Or_Configured</td>
  </tr>
  <tr>
    <td><code>E4512</code></td>
    <td>Transaction details not present at bank&#x27;s end</td>
    <td>Merchant TranId is not available</td>
    <td>Merchant_TranId_Is_Not_Available</td>
  </tr>
  <tr>
    <td><code>E4333</code></td>
    <td>MERCHANT NOT REACHABLE (ACQURIER)</td>
    <td>MERCHANT NOT REACHABLE (ACQURIER)</td>
    <td>MERCHANT_NOT_REACHABLE_ACQURIER</td>
  </tr>
  <tr>
    <td><code>EA09</code></td>
    <td>Alt ID Provisioning Failed</td>
    <td>Merchant not onboarded, please contact PayU Support</td>
    <td>ALT_ID_PROV_MERCHANT</td>
  </tr>
  <tr>
    <td><code>E4365</code></td>
    <td>Transaction declined due to merchant error</td>
    <td>MERCHANT ERROR (PAYEE PSP)</td>
    <td>MERCHANT_ERROR_PAYEE_PSP</td>
  </tr>
  <tr>
    <td><code>E9237</code></td>
    <td>Merchant Daily Limit Exceeded</td>
    <td>Merchant Daily Limit Exceeded</td>
    <td>MERCHANT_DAILY_LIMIT_EXCEEDED</td>
  </tr>
  <tr>
    <td><code>E4220</code></td>
    <td>MERCHANT CREDIT NOT SUPPORTED IN IMPS</td>
    <td>MERCHANT CREDIT NOT SUPPORTED IN IMPS</td>
    <td>MERCHANT_CREDIT_NOT_SUPPORTED_IN_IMPS</td>
  </tr>
  <tr>
    <td><code>E4225</code></td>
    <td>Transaction failed as merchant is blocked</td>
    <td>MERCHANT BLOCKED</td>
    <td>MERCHANT_BLOCKED</td>
  </tr>
  <tr>
    <td><code>E1643</code></td>
    <td>Mecode Not Permitted</td>
    <td>MECODE_NOT_PERMITTED</td>
    <td>MECODE_NOT_PERMITTED</td>
  </tr>
  <tr>
    <td><code>E1669</code></td>
    <td>MCP lookup details tampered</td>
    <td>MCP_LOOKUP_DETAILS_TAMPERED</td>
    <td>MCP_LOOKUP_DETAILS_TAMPERED</td>
  </tr>
  <tr>
    <td><code>E2406</code></td>
    <td>You have entered incorrect otp too many times, Please try again</td>
    <td>MAXIMUM_OTP_LIMIT_REACHED</td>
    <td>MAXIMUM_OTP_LIMIT_REACHED</td>
  </tr>
  <tr>
    <td><code>E9242</code></td>
    <td>Maximum refund credit reached</td>
    <td>Maximum refund credit reached</td>
    <td>MAXIMUM_REFUND_CREDIT_REACHED</td>
  </tr>
  <tr>
    <td><code>E9241</code></td>
    <td>Maximum off-line refund reached</td>
    <td>Maximum off-line refund reached</td>
    <td>MAXIMUM_OFFLINE_REFUND_REACHED</td>
  </tr>
  <tr>
    <td><code>E9243</code></td>
    <td>Maximum number refund credits</td>
    <td>Maximum number refund credits</td>
    <td>MAXIMUM_NUMBER_REFUND_CREDITS</td>
  </tr>
  <tr>
    <td><code>E4104</code></td>
    <td>MAXIMUM BALANCE EXCEEDED AS SET BY BENEFICIARY BANK</td>
    <td>MAXIMUM BALANCE EXCEEDED AS SET BY BENEFICIARY BANK</td>
    <td>MAXIMUM_BALANCE_EXCEEDED_AS_SET_BY_BENEFICIARY_BANK</td>
  </tr>
  <tr>
    <td><code>E1640</code></td>
    <td>Offus Master Card Not Approved Transaction</td>
    <td>MASTER_CARD_NOT_APPROVED</td>
    <td>MASTER_CARD_NOT_APPROVED</td>
  </tr>
  <tr>
    <td><code>E1641</code></td>
    <td>Cancellation not allowed for offus master card</td>
    <td>MASTER_CARD_CANCELLATION_NOT_ALLOWED</td>
    <td>MASTER_CARD_CANCELLATION_NOT_ALLOWED</td>
  </tr>
  <tr>
    <td><code>E4065</code></td>
    <td>MANDATE.VALIDITY.START MUST BE PRESENT, DATE FORMAT</td>
    <td>MANDATE.VALIDITY.START MUST BE PRESENT, DATE FORMAT</td>
    <td>MANDATE_VALIDITY_START_MUST_BE_PRESENT_DATE_FORMAT</td>
  </tr>
  <tr>
    <td><code>E4099</code></td>
    <td>MANDATE.VALIDITY.START DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE.VALIDITY.START DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE_VALIDITY_START_DIFFERS_FROM_ORIGINAL_REQUEST</td>
  </tr>
  <tr>
    <td><code>E4066</code></td>
    <td>MANDATE.VALIDITY.END MUST BE PRESENT, DATE FORMAT DDMMYYYY, END DATE MUST BE GREATER THAN TODAY&#x27;S DATE</td>
    <td>MANDATE.VALIDITY.END MUST BE PRESENT, DATE FORMAT DDMMYYYY, END</td>
    <td>MANDATE_VALIDITY_END_MUST_BE_PRESENT_DATE_FORMAT_DDMMYYYY_END_DATE_MUST_BE_GREATER_THAN_TODAYS_DATE</td>
  </tr>
  <tr>
    <td><code>E4100</code></td>
    <td>MANDATE.VALIDITY.END DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE.VALIDITY.END DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE_VALIDITY_END_DIFFERS_FROM_ORIGINAL_REQUEST</td>
  </tr>
  <tr>
    <td><code>E4064</code></td>
    <td>MANDATE.VALIDITY MUST BE PRESENT</td>
    <td>MANDATE.VALIDITY MUST BE PRESENT</td>
    <td>MANDATE_VALIDITY_MUST_BE_PRESENT</td>
  </tr>
  <tr>
    <td><code>E4098</code></td>
    <td>MANDATE.VALIDITY DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE.VALIDITY DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE_VALIDITY_DIFFERS_FROM_ORIGINAL_REQUEST</td>
  </tr>
  <tr>
    <td><code>E4056</code></td>
    <td>MANDATE.UMN SHOULD NOT BE PRESENT FOR PAYEE INITIATED</td>
    <td>MANDATE.UMN SHOULD NOT BE PRESENT FOR PAYEE INITIATED</td>
    <td>MANDATE_UMN_SHOULD_NOT_BE_PRESENT_FOR_PAYEE_INITIATED</td>
  </tr>
  <tr>
    <td><code>E4060</code></td>
    <td>MANDATE.UMN MUST BE PRESENT, LENGTH 32</td>
    <td>MANDATE.UMN MUST BE PRESENT, LENGTH 32</td>
    <td>MANDATE_UMN_MUST_BE_PRESENT_Length_32</td>
  </tr>
  <tr>
    <td><code>E4059</code></td>
    <td>MANDATE.UMN MUST BE PRESENT</td>
    <td>MANDATE.UMN MUST BE PRESENT</td>
    <td>MANDATE_UMN_MUST_BE_PRESENT_1</td>
  </tr>
  <tr>
    <td><code>E4081</code></td>
    <td>MANDATE.UMN DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE.UMN DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE_UMN_DIFFERS_FROM_ORIGINAL_REQUEST</td>
  </tr>
  <tr>
    <td><code>E4075</code></td>
    <td>MANDATE.UMN CANNOT BE GENERATED BY PAYEE</td>
    <td>MANDATE.UMN CANNOT BE GENERATED BY PAYEE</td>
    <td>MANDATE_UMN_CANNOT_BE_GENERATED_BY_PAYEE</td>
  </tr>
  <tr>
    <td><code>E4086</code></td>
    <td>MANDATE.TYPE DIFFERS FROM ORIGINAL REQUEST,MANDATE.AMOUNT DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE.TYPE DIFFERS FROM ORIGINAL REQUEST,MANDATE.AMOUNT DIFFER</td>
    <td>MANDATE_TYPE_DIFFERS_FROM_ORIGINAL_REQUEST_MANDATE_AMOUNT_DIFFERS_FROM_ORIGINAL_REQUEST</td>
  </tr>
  <tr>
    <td><code>E4057</code></td>
    <td>MANDATE.TXNID MUST BE PRESENT, MUST BE 35 CHARACTERS OF ALPHANUMERIC</td>
    <td>MANDATE.TXNID MUST BE PRESENT, MUST BE 35 CHARACTERS OF ALPHANUM</td>
    <td>MANDATE_TXNID_MUST_BE_PRESENT_MUST_BE_35_CHARACTERS_OF_ALPHANUMERIC</td>
  </tr>
  <tr>
    <td><code>E4080</code></td>
    <td>MANDATE.TXNID DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE.TXNID DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE_TXNID_DIFFERS_FROM_ORIGINAL_REQUEST</td>
  </tr>
  <tr>
    <td><code>E4058</code></td>
    <td>MANDATE.TXNID AND TXN.ID MUST BE SAME</td>
    <td>MANDATE.TXNID AND TXN.ID MUST BE SAME</td>
    <td>MANDATE_TXNID_AND_TXN_ID_MUST_BE_SAME</td>
  </tr>
  <tr>
    <td><code>E4061</code></td>
    <td>MANDATE.TS MUST BE PRESENT AND SHOULD BE IN ISO_ZONE</td>
    <td>MANDATE.TS MUST BE PRESENT AND SHOULD BE IN ISO_ZONE</td>
    <td>MANDATE_TS_MUST_BE_PRESENT_AND_SHOULD_BE_IN_ISO_ZONE</td>
  </tr>
  <tr>
    <td><code>E4084</code></td>
    <td>MANDATE.SHARETOPAYEE DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE.SHARETOPAYEE DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE_SHARETOPAYEE_DIFFERS_FROM_ORIGINAL_REQUEST</td>
  </tr>
  <tr>
    <td><code>E4062</code></td>
    <td>MANDATE.REVOKEABLE MUST BE PRESENT</td>
    <td>MANDATE.REVOKEABLE MUST BE PRESENT</td>
    <td>MANDATE_REVOKEABLE_MUST_BE_PRESENT</td>
  </tr>
  <tr>
    <td><code>E4072</code></td>
    <td>MANDATE.RECURRENCE.RULE NOT APPLICABLE FOR MANDATE.RECURRENCE.PATTERN ONETIME/DAILY/WEEKLY/FORTNIGHTLY/MONTHLY /BIMONTHLY/QUARTERLY/HALFYEARLY /YEARLY/ASPRESENTED</td>
    <td>MANDATE.RECURRENCE.RULE NOT APPLICABLE FOR MANDATE.RECURRENCE.PA</td>
    <td>MANDATE_RECURRENCE_RULE_NOT_APPLICABLE_FOR_MANDATE_RECURRENCE_PATTERN_ONETIME_DAILY_WEEKLY_FORTNIGHTLY_MONTHLY_BIMONTHLY_QUARTERLY_HALFYEARLY_YEARLY_ASPRESENTED</td>
  </tr>
  <tr>
    <td><code>E4070</code></td>
    <td>MANDATE.RECURRENCE.RULE MUST BE PRESENT,MANDATE.RECURRENCE.RULE.TYPE MUST BE AFTER OR ON OR BEFORE</td>
    <td>MANDATE.RECURRENCE.RULE MUST BE PRESENT,MANDATE.RECURRENCE.RULE.</td>
    <td>MANDATE_RECURRENCE_RULE_MUST_BE_PRESENT_MANDATE_RECURRENCE_RULE_TYPE_MUST_BE_AFTER_OR_ON_OR_BEFORE</td>
  </tr>
  <tr>
    <td><code>E4071</code></td>
    <td>MANDATE.RECURRENCE.RULE MUST BE PRESENT,MANDATE.RECURRENCE.RULE.VALUE IN BETWEEN 1 TO 7 ONLY WHEN MANDATE.RECURRENCE.PATTERN IS WEEKLY</td>
    <td>MANDATE.RECURRENCE.RULE MUST BE PRESENT,MANDATE.RECURRENCE.RULE.</td>
    <td>MANDATE_RECURRENCE_RULE_MUST_BE_PRESENT_MANDATE_RECURRENCE_RULE_VALUE_IN_BETWEEN_1_TO_7_ONLY_WHEN_MANDATE_RECURRENCE_PATTERN_IS_WEEKLY</td>
  </tr>
  <tr>
    <td><code>E4087</code></td>
    <td>MANDATE.RECURRENCE.PATTERN DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE.RECURRENCE.PATTERN DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE_RECURRENCE_PATTERN_DIFFERS_FROM_ORIGINAL_REQUEST</td>
  </tr>
  <tr>
    <td><code>E4327</code></td>
    <td>MANDATE.RECURRENCE RULE TAG SHOULD NOT BE PRESENTREMITTER BANK NOT CERTIFIED FOR 2.7</td>
    <td>MANDATE.RECURRENCE RULE TAG SHOULD NOT BE PRESENTREMITTER BANK N</td>
    <td>MANDATE_RECURRENCE_RULE_TAG_SHOULD_NOT_BE_PRESENTREMITTER_BANK_NOT_CERTIFIED_FOR_2_7</td>
  </tr>
  <tr>
    <td><code>E4328</code></td>
    <td>MANDATE.RECURRENCE RULE TAG SHOULD NOT BE PRESENTBENEFICIARY BANK NOT CERTIFIED FOR 2.7</td>
    <td>MANDATE.RECURRENCE RULE TAG SHOULD NOT BE PRESENTBENEFICIARY BAN</td>
    <td>MANDATE_RECURRENCE_RULE_TAG_SHOULD_NOT_BE_PRESENTBENEFICIARY_BANK_NOT_CERTIFIED_FOR_2_7</td>
  </tr>
  <tr>
    <td><code>E4069</code></td>
    <td>MANDATE.RECURRENCE MUST BE PRESENT,MANDATE.RECURRENCE.PATTERN MUST BE ONETIME OR DAILYOR WEEKLY</td>
    <td>MANDATE.RECURRENCE MUST BE PRESENT,MANDATE.RECURRENCE.PATTERN MU</td>
    <td>MANDATE_RECURRENCE_MUST_BE_PRESENT_MANDATE_RECURRENCE_PATTERN_MUST_BE_ONETIME_OR_DAILYOR_WEEKLY</td>
  </tr>
  <tr>
    <td><code>E4079</code></td>
    <td>MANDATE.NAME DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE.NAME DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE_NAME_DIFFERS_FROM_ORIGINAL_REQUEST</td>
  </tr>
  <tr>
    <td><code>E4054</code></td>
    <td>MANDATE.NAME ALPHANUMERIC; MINLENGTH 1 , MAXLENGTH 99</td>
    <td>MANDATE.NAME ALPHANUMERIC; MINLENGTH 1 , MAXLENGTH 99</td>
    <td>MANDATE_NAME_ALPHANUMERIC_MINLENGTH_1_MAXLENGTH_99</td>
  </tr>
  <tr>
    <td><code>E4085</code></td>
    <td>MANDATE.BLOCKFUND DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE.BLOCKFUND DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE_BLOCKFUND_DIFFERS_FROM_ORIGINAL_REQUEST</td>
  </tr>
  <tr>
    <td><code>E4068</code></td>
    <td>MANDATE.AMOUNT.RULE MUST BE PRESENT, RULE MUST BE EXACT/MAX</td>
    <td>MANDATE.AMOUNT.RULE MUST BE PRESENT, RULE MUST BE EXACT/MAX</td>
    <td>MANDATE_AMOUNT_RULE_MUST_BE_PRESENT_RULE_MUST_BE_EXACT_MAX</td>
  </tr>
  <tr>
    <td><code>E4067</code></td>
    <td>MANDATE.AMOUNT MUST BE PRESENT, VALUE AND RULE SHOULD NOT BE EMPTY</td>
    <td>MANDATE.AMOUNT MUST BE PRESENT, VALUE AND RULE SHOULD NOT BE EMP</td>
    <td>MANDATE_AMOUNT_MUST_BE_PRESENT_VALUE_AND_RULE_SHOULD_NOT_BE_EMPTY</td>
  </tr>
  <tr>
    <td><code>E4090</code></td>
    <td>MANDATE.AMOUNT CAN ONLY BE UPDATED IF PURPOSE=01</td>
    <td>MANDATE.AMOUNT CAN ONLY BE UPDATED IF PURPOSE=01</td>
    <td>MANDATE_AMOUNT_CAN_ONLY_BE_UPDATED_IF_PURPOSE_01</td>
  </tr>
  <tr>
    <td><code>E4679</code></td>
    <td>Modification request already initiated</td>
    <td>Mandate Update Request already initiated for Same UMN</td>
    <td>Mandate_Update_Request_Already_Initiated_For_Same_UMN</td>
  </tr>
  <tr>
    <td><code>E4055</code></td>
    <td>MANDATE UMN MUST BE PRESENT</td>
    <td>MANDATE UMN MUST BE PRESENT</td>
    <td>MANDATE_UMN_MUST_BE_PRESENT</td>
  </tr>
  <tr>
    <td><code>E4082</code></td>
    <td>MANDATE TS DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE TS DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE_TS_DIFFERS_FROM_ORIGINAL_REQUEST</td>
  </tr>
  <tr>
    <td><code>E4078</code></td>
    <td>MANDATE TAG DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE TAG DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE_TAG_DIFFERS_FROM_ORIGINAL_REQUEST</td>
  </tr>
  <tr>
    <td><code>E4309</code></td>
    <td>Transaction failed as mandate signature is tampered</td>
    <td>MANDATE SIGNATURE IS TAMPERED OR CORRUPT (REMITTER)</td>
    <td>MANDATE_SIGNATURE_IS_TAMPERED_OR_CORRUPT_REMITTER</td>
  </tr>
  <tr>
    <td><code>E4083</code></td>
    <td>MANDATE REVOKEABLE DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE REVOKEABLE DIFFERS FROM ORIGINAL REQUEST</td>
    <td>MANDATE_REVOKEABLE_DIFFERS_FROM_ORIGINAL_REQUEST</td>
  </tr>
  <tr>
    <td><code>E4532</code></td>
    <td>Mandate request not created</td>
    <td>Mandate request not created</td>
    <td>Mandate_Request_Not_Created</td>
  </tr>
  <tr>
    <td><code>E4115</code></td>
    <td>Transaction failed as mandate request limit is breached</td>
    <td>MANDATE REQUEST LIMIT HAS BREACHED</td>
    <td>MANDATE_REQUEST_LIMIT_HAS_BREACHED</td>
  </tr>
  <tr>
    <td><code>E4077</code></td>
    <td>MANDATE REQUEST IS DECLINED BY MERCHANT (PAYEE)</td>
    <td>MANDATE REQUEST IS DECLINED BY MERCHANT (PAYEE)</td>
    <td>MANDATE_REQUEST_IS_DECLINED_BY_MERCHANT_PAYEE</td>
  </tr>
  <tr>
    <td><code>E4607</code></td>
    <td>Mandate Request Approved</td>
    <td>Mandate Request Approved</td>
    <td>Mandate_Request_Approved</td>
  </tr>
  <tr>
    <td><code>E4313</code></td>
    <td>MANDATE REGISTRATION NOT ALLOWED FOR CC PF PPF ACT (BANK&#x27;S POLICY)</td>
    <td>MANDATE REGISTRATION NOT ALLOWED FOR CC PF PPF ACT (BANKNULLS PO</td>
    <td>MANDATE_REGISTRATION_NOT_ALLOWED_FOR_CC_PF_PPF_ACT_BANKS_POLICY</td>
  </tr>
  <tr>
    <td><code>E4329</code></td>
    <td>MANDATE RECURRENCE RULE TAG SHOULD NOT BE PRESENTPAYER PSP NOT CERTIFIED FOR 2.7</td>
    <td>MANDATE RECURRENCE RULE TAG SHOULD NOT BE PRESENTPAYER PSP NOT C</td>
    <td>MANDATE_RECURRENCE_RULE_TAG_SHOULD_NOT_BE_PRESENTPAYER_PSP_NOT_CERTIFIED_FOR_2_7</td>
  </tr>
  <tr>
    <td><code>E4330</code></td>
    <td>MANDATE RECURRENCE RULE TAG SHOULD NOT BE PRESENT PAYEE PSP NOT CERTIFIED FOR 2.7</td>
    <td>MANDATE RECURRENCE RULE TAG SHOULD NOT BE PRESENT PAYEE PSP NOT</td>
    <td>MANDATE_RECURRENCE_RULE_TAG_SHOULD_NOT_BE_PRESENT_PAYEE_PSP_NOT_CERTIFIED_FOR_2_7</td>
  </tr>
  <tr>
    <td><code>E4073</code></td>
    <td>MANDATE RECURRENCE PATTERN.BLOCK=N IS ALLOWED ONLY IF THE PURPOSE CODE=14</td>
    <td>MANDATE RECURRENCE PATTERN.BLOCK=N IS ALLOWED ONLY IF THE PURPOS</td>
    <td>MANDATE_RECURRENCE_PATTERN_BLOCK_N_IS_ALLOWED_ONLY_IF_THE_PURPOSE_CODE_14</td>
  </tr>
  <tr>
    <td><code>E4074</code></td>
    <td>MANDATE RECURRENCE PATTERN. REVOKABLE=Y, ONLY Y IS ALLOWED IF THE PURPOSE CODE=14</td>
    <td>MANDATE RECURRENCE PATTERN. REVOKABLE=Y, ONLY Y IS ALLOWED IF TH</td>
    <td>MANDATE_RECURRENCE_PATTERN__REVOKABLE_Y_ONLY_Y_IS_ALLOWED_IF_THE_PURPOSE_CODE_14</td>
  </tr>
  <tr>
    <td><code>E4053</code></td>
    <td>Transaction failed due to mandate not present</td>
    <td>MANDATE NOT PRESENT</td>
    <td>MANDATE_NOT_PRESENT</td>
  </tr>
  <tr>
    <td><code>E4124</code></td>
    <td>Modification request declined by the customer</td>
    <td>MANDATE MODIFY REQUEST IS DECLINED (PAYER)</td>
    <td>MANDATE_MODIFY_REQUEST_IS_DECLINED_PAYER</td>
  </tr>
  <tr>
    <td><code>E4131</code></td>
    <td>Modification request declined by merchant</td>
    <td>MANDATE MODIFICATION DECLINED BY MERCHANT</td>
    <td>MANDATE_MODIFICATION_DECLINED_BY_MERCHANT</td>
  </tr>
  <tr>
    <td><code>E4108</code></td>
    <td>Transaction failed as mandate is paused by the user</td>
    <td>MANDATE IS PAUSED BY USER</td>
    <td>MANDATE_IS_PAUSED_BY_USER</td>
  </tr>
  <tr>
    <td><code>E4109</code></td>
    <td>Transaction failed as mandate is already honoured</td>
    <td>MANDATE IS ALREADY HONOURED</td>
    <td>MANDATE_IS_ALREADY_HONOURED_1</td>
  </tr>
  <tr>
    <td><code>E4111</code></td>
    <td>Transaction failed as mandate is expired</td>
    <td>MANDATE HAS EXPIRED</td>
    <td>MANDATE_HAS_EXPIRED</td>
  </tr>
  <tr>
    <td><code>E4110</code></td>
    <td>Transaction failed as mandate is revoked by the user</td>
    <td>MANDATE HAS BEEN REVOKED</td>
    <td>MANDATE_HAS_BEEN_REVOKED</td>
  </tr>
  <tr>
    <td><code>E4127</code></td>
    <td>Transaction declined as payee is a non-merchant</td>
    <td>MANDATE DECLINED AS PAYEE IS NON-MERCHANT (PAYER)</td>
    <td>MANDATE_DECLINED_AS_PAYEE_IS_NON_MERCHANT_PAYER</td>
  </tr>
  <tr>
    <td><code>E4116</code></td>
    <td>Transaction failed as mandate amount is higher than allowed by customer&#x27;s application</td>
    <td>MANDATE DEBIT IS BEYOND PSP SPECIFIED AMOUNT CAP</td>
    <td>MANDATE_DEBIT_IS_BEYOND_PSP_SPECIFIED_AMOUNT_CAP</td>
  </tr>
  <tr>
    <td><code>E4121</code></td>
    <td>Transaction failed as mandate is not allowed to be created on this merchant</td>
    <td>MANDATE CANNOT BE CREATED ON THIS VPA (PAYER)</td>
    <td>MANDATE_CANNOT_BE_CREATED_ON_THIS_VPA_PAYER</td>
  </tr>
  <tr>
    <td><code>E4535</code></td>
    <td>Transaction failed due to amount mismatch error</td>
    <td>Mandate amounts mis-matched</td>
    <td>Mandate_Amounts_Mis_matched</td>
  </tr>
  <tr>
    <td><code>E4293</code></td>
    <td>Transaction declined as mandate amount limit exceeded</td>
    <td>MANDATE AMOUNT CAP IS EXCEEDED</td>
    <td>MANDATE_AMOUNT_CAP_IS_EXCEEDED</td>
  </tr>
  <tr>
    <td><code>E806</code></td>
    <td>You have opted out of Lazypay service</td>
    <td>LP_USER_OPTED_OUT</td>
    <td>LP_USER_OPTED_OUT</td>
  </tr>
  <tr>
    <td><code>E807</code></td>
    <td>Sorry! You are currently not registered for LazyPay</td>
    <td>LP_USER_INELIGIBLE</td>
    <td>LP_USER_INELIGIBLE</td>
  </tr>
  <tr>
    <td><code>E805</code></td>
    <td>Your Lazypay account is blocked</td>
    <td>LP_USER_BLOCKED</td>
    <td>LP_USER_BLOCKED</td>
  </tr>
  <tr>
    <td><code>E4001</code></td>
    <td>ISSUER NOT LIVE ON UPI</td>
    <td>Low confidence</td>
    <td>ISSUER_NOT_LIVE_ON_UPI</td>
  </tr>
  <tr>
    <td><code>E4359</code></td>
    <td>Transaction failed due to lost or stolen card from customer&#x27;s bank</td>
    <td>LOST OR STOLEN CARD (REMITTER)</td>
    <td>LOST_OR_STOLEN_CARD_REMITTER</td>
  </tr>
  <tr>
    <td><code>E4360</code></td>
    <td>Transaction failed due to lost or stolen card from acquirer&#x27;s bank</td>
    <td>LOST OR STOLEN CARD (BENEFICIARY)</td>
    <td>LOST_OR_STOLEN_CARD_BENEFICIARY</td>
  </tr>
  <tr>
    <td><code>E1505</code></td>
    <td>You don&#x27;t have sufficient credit limit to complete this transaction.</td>
    <td>LOAN_AMOUNT_GREATER * THAN_ELIGIBLITY</td>
    <td>LOAN_AMOUNT_GREATER_THAN_ELIGIBLITY</td>
  </tr>
  <tr>
    <td><code>E2408</code></td>
    <td>Link and Pay not Eligible</td>
    <td>LINK_AND_PAY_NOT_ELIGIBLE</td>
    <td>LINK_AND_PAY_NOT_ELIGIBLE</td>
  </tr>
  <tr>
    <td><code>E4389</code></td>
    <td>LIMIT EXCEEDED FOR REMITTING BANK/ISSUING BANK</td>
    <td>LIMIT EXCEEDED FOR REMITTING BANK/ISSUING BANK</td>
    <td>LIMIT_EXCEEDED_FOR_REMITTING_BANK_ISSUING_BANK</td>
  </tr>
  <tr>
    <td><code>E2503</code></td>
    <td>Late otp submission on Headless</td>
    <td>LATE_OTP_SUBMISSSION * ON_HEADLESS</td>
    <td>LATE_OTP_SUBMISSSION_ON_HEADLESS</td>
  </tr>
  <tr>
    <td><code>E4158</code></td>
    <td>Transaction failed due to timeout at acquirer&#x27;s end</td>
    <td>Issuer unavailable or switch inoperative</td>
    <td>REQAUTH_TIME_OUT_FOR_PAY</td>
  </tr>
  <tr>
    <td><code>E9254</code></td>
    <td>Authorization Platform or Switch / Issuer system inoperative or Not Supported</td>
    <td>Issuer or Switch is Inoperative</td>
    <td>BANK_NOT_SUPPORTED_BY_SWITCH</td>
  </tr>
  <tr>
    <td><code>E9254</code></td>
    <td>ACQUIRER/BENEFICIARY UNAVAILABLE(TIMEOUT)</td>
    <td>ACQUIRER_BENEFICIARY_UNAVAILABLE_TIMEOUT</td>
    <td></td>
  </tr>
  <tr>
    <td><code>E714</code></td>
    <td>Card authentication failed due to invalid ZIP code</td>
    <td>INVALID_ZIP</td>
    <td>INVALID_ZIP</td>
  </tr>
  <tr>
    <td><code>E1020</code></td>
    <td>Transaction ID you&#x27;ve generated isn&#x27;t valid</td>
    <td>INVALID_TRANSACTION_ID</td>
    <td>INVALID_TRANSACTION_ID</td>
  </tr>
  <tr>
    <td><code>E1603</code></td>
    <td>Transaction failed. Mobile number not registered for the given card.</td>
    <td>INVALID_PHONE_NO</td>
    <td>INVALID_PHONE_NO</td>
  </tr>
  <tr>
    <td><code>E1646</code></td>
    <td>Invalid PayU ID</td>
    <td>INVALID_PAYU_ID</td>
    <td>INVALID_PAYU_ID</td>
  </tr>
  <tr>
    <td><code>E707</code></td>
    <td>Transaction failed due to invalid Primary Account Number. (Primary Account Number or PAN is the number that is embossed and/or encoded on a plastic card that identifies the issuer and the particular cardholder account.)</td>
    <td>INVALID_PAN</td>
    <td>INVALID_PAN</td>
  </tr>
  <tr>
    <td><code>E340</code></td>
    <td>Transaction failed due to invalid OTP</td>
    <td>INVALID_OTP</td>
    <td>INVALID_OTP</td>
  </tr>
  <tr>
    <td><code>E1665</code></td>
    <td>Incorrect request received for one click transaction</td>
    <td>INVALID_ONE_CLICK * REQUEST_RECEIVED</td>
    <td>INVALID_ONE_CLICK_REQUEST_RECEIVED</td>
  </tr>
  <tr>
    <td><code>E339</code></td>
    <td>Transaction failed due to invalid mobile number</td>
    <td>INVALID_MOBILE_NUMBER</td>
    <td>INVALID_MOBILE_NUMBER</td>
  </tr>
  <tr>
    <td><code>E1501</code></td>
    <td>Transaction amount is less than the minimum amount accepted by issuing bank for processing EMI.</td>
    <td>INVALID_MIN_AMOUNT_EMI</td>
    <td>INVALID_MIN_AMOUNT_EMI</td>
  </tr>
  <tr>
    <td><code>E1637</code></td>
    <td>Merchant Type Not Supported</td>
    <td>INVALID_MERCHANT_TYPE</td>
    <td>INVALID_MERCHANT_TYPE</td>
  </tr>
  <tr>
    <td><code>E1647</code></td>
    <td>Invalid Merchant Key</td>
    <td>INVALID_MERCHANT_KEY</td>
    <td>INVALID_MERCHANT_KEY</td>
  </tr>
  <tr>
    <td><code>E2409</code></td>
    <td>Transaction amount is more than the maximum amount accepted by issuing bank for processing EMI.</td>
    <td>INVALID_MAX_AMOUNT_EMI</td>
    <td>INVALID_MAX_AMOUNT_EMI</td>
  </tr>
  <tr>
    <td><code>E327</code></td>
    <td>Authentication failed to due invalid login</td>
    <td>INVALID_LOGIN</td>
    <td>INVALID_LOGIN</td>
  </tr>
  <tr>
    <td><code>E2407</code></td>
    <td>Missing User details</td>
    <td>INVALID_LINK_AND_PAY * REQUEST_RECEIVED</td>
    <td>INVALID_LINK_AND_PAY_REQUEST_RECEIVED</td>
  </tr>
  <tr>
    <td><code>E332</code></td>
    <td>Card authentication failed due to invalid FAX number</td>
    <td>INVALID_FAX</td>
    <td>INVALID_FAX</td>
  </tr>
  <tr>
    <td><code>E323</code></td>
    <td>Card authentication failed due to invalid card expiry date.</td>
    <td>INVALID_EXPIRY_DATE</td>
    <td>INVALID_EXPIRY_DATE</td>
  </tr>
  <tr>
    <td><code>E910</code></td>
    <td>EMI is not supported on this card</td>
    <td>INVALID_EMI_CARD_BIN</td>
    <td>INVALID_EMI_CARD_BIN</td>
  </tr>
  <tr>
    <td><code>E331</code></td>
    <td>Card authentication failed due to invalid email id</td>
    <td>INVALID_EMAIL_ID</td>
    <td>INVALID_EMAIL_ID</td>
  </tr>
  <tr>
    <td><code>E2081</code></td>
    <td>Invalid Device Id</td>
    <td>INVALID_DEVICE_ID</td>
    <td>INVALID_DEVICE_ID</td>
  </tr>
  <tr>
    <td><code>E333</code></td>
    <td>Card authentication failed due to invalid contact/phone details</td>
    <td>INVALID_CONTACT</td>
    <td>INVALID_CONTACT</td>
  </tr>
  <tr>
    <td><code>E709</code></td>
    <td>Transaction failed due to invalid credit card name</td>
    <td>INVALID_CARD_NAME</td>
    <td>INVALID_CARD_NAME</td>
  </tr>
  <tr>
    <td><code>E1702</code></td>
    <td>Invalid Action</td>
    <td>INVALID_ACTION</td>
    <td>INVALID_ACTION</td>
  </tr>
  <tr>
    <td><code>E1625</code></td>
    <td>Card not enabled for Ecomm transactions, either the card is newly issued or has not been used for any online transaction during last 12 months</td>
    <td>Invalid/nonexistent account specified (general)</td>
    <td>CARD_NOT_ENABLED_FOR_ECOMM_TXN</td>
  </tr>
  <tr>
    <td><code>E4148</code></td>
    <td>INVALID/INCORRECT ATM PIN</td>
    <td>INVALID/INCORRECT ATM PIN</td>
    <td>INVALID_INCORRECT_ATM_PIN</td>
  </tr>
  <tr>
    <td><code>E4042</code></td>
    <td>Invalid verification token</td>
    <td>Invalid verification token</td>
    <td>Invalid_Verification_Token</td>
  </tr>
  <tr>
    <td><code>E207</code></td>
    <td>Bank denied transaction on the card.</td>
    <td>Invalid transaction</td>
    <td>INVALID_TRANSACTION</td>
  </tr>
  <tr>
    <td><code>E4521</code></td>
    <td>Transaction failed due to invalid MCC details</td>
    <td>Invalid Terminal Id</td>
    <td>Invalid_Terminal_Id</td>
  </tr>
  <tr>
    <td><code>E2110</code></td>
    <td>Unable to process the request.</td>
    <td>Invalid Response From Up Streaming Server</td>
    <td>INVALID_REQUEST_FROM_PG_TO_DOWNSTREAM</td>
  </tr>
  <tr>
    <td><code>E4367</code></td>
    <td>INVALID RESPONSE CODE</td>
    <td>INVALID RESPONSE CODE</td>
    <td>INVALID_RESPONSE_CODE</td>
  </tr>
  <tr>
    <td><code>E710</code></td>
    <td>Transaction failed due to invalid PIN</td>
    <td>Invalid PIN</td>
    <td>INVALID_PIN</td>
  </tr>
  <tr>
    <td><code>E4386</code></td>
    <td>INVALID OTP</td>
    <td>INVALID OTP</td>
    <td>INVALID_OTP_1</td>
  </tr>
  <tr>
    <td><code>E4371</code></td>
    <td>Transaction declined due to invalid merchant details</td>
    <td>INVALID MERCHANT (PAYEE PSP)</td>
    <td>INVALID_MERCHANT_PAYEE_PSP</td>
  </tr>
  <tr>
    <td><code>E4332</code></td>
    <td>INVALID MERCHANT (ACQURIER)</td>
    <td>INVALID MERCHANT (ACQURIER)</td>
    <td>INVALID_MERCHANT_ACQURIER</td>
  </tr>
  <tr>
    <td><code>E341</code></td>
    <td>Transaction failed due to invalid merchant</td>
    <td>Invalid Merchant</td>
    <td>INVALID_MERCHANT</td>
  </tr>
  <tr>
    <td><code>E305</code></td>
    <td>The transaction failed due to invalid or absent card number.</td>
    <td>Invalid issuer</td>
    <td>CARD_NUMBER_INVALID</td>
  </tr>
  <tr>
    <td><code>E1632</code></td>
    <td>Transaction declined due to either incorrect cvv/expiry or card validation failure</td>
    <td>Invalid card number</td>
    <td>CARD_VALIDATION_FAILED</td>
  </tr>
  <tr>
    <td><code>E4368</code></td>
    <td>INVALID BENEFICIARY CREDENTIALS</td>
    <td>INVALID BENEFICIARY CREDENTIALS</td>
    <td>INVALID_BENEFICIARY_CREDENTIALS</td>
  </tr>
  <tr>
    <td><code>E4336</code></td>
    <td>INVALID AMOUNT (REMITTER)</td>
    <td>INVALID AMOUNT (REMITTER)</td>
    <td>INVALID_AMOUNT_REMITTER</td>
  </tr>
  <tr>
    <td><code>E4337</code></td>
    <td>INVALID AMOUNT (BENEFICIARY)</td>
    <td>INVALID AMOUNT (BENEFICIARY)</td>
    <td>INVALID_AMOUNT_BENEFICIARY</td>
  </tr>
  <tr>
    <td><code>E715</code></td>
    <td>Invalid amount sent to the bank</td>
    <td>Invalid amount</td>
    <td>INVALID_AMOUNT</td>
  </tr>
  <tr>
    <td><code>E903</code></td>
    <td>International cards are not accepted</td>
    <td>INTERNATIONAL_CARD * NOT_ALLOWED</td>
    <td>INTERNATIONAL_CARD_NOT_ALLOWED</td>
  </tr>
  <tr>
    <td><code>E4040</code></td>
    <td>International Service not activated/disabled</td>
    <td>International Service not activated/disabled</td>
    <td>International_Service_Not_Activated_disabled</td>
  </tr>
  <tr>
    <td><code>E9239</code></td>
    <td>International Acceptance not enabled</td>
    <td>International Acceptance not enabled</td>
    <td>INTERNATIONAL_ACCEPTANCE_NOT_ENABLED</td>
  </tr>
  <tr>
    <td><code>E1617</code></td>
    <td>Internal server Error [S2S FLow]</td>
    <td>INTERNAL_SERVER * ERROR_S2SFLOW</td>
    <td>INTERNAL_SERVER_ERROR_S2SFLOW</td>
  </tr>
  <tr>
    <td><code>E1901</code></td>
    <td>Customer chose Collect over Intent</td>
    <td>INTENT_SDK_FALLBACK</td>
    <td>INTENT_SDK_FALLBACK</td>
  </tr>
  <tr>
    <td><code>E1900</code></td>
    <td>Unable to open intent, switched to collect</td>
    <td>INTENT_OPENING_FAILED</td>
    <td>INTENT_OPENING_FAILED</td>
  </tr>
  <tr>
    <td><code>E1208</code></td>
    <td>Transaction failed because the customer does not have the necessary funds or he has given a wrong expiry date.</td>
    <td>INSUFFICIENT_FUNDS * INCORRECT_EXPIRY</td>
    <td>INSUFFICIENT_FUNDS_INCORRECT_EXPIRY</td>
  </tr>
  <tr>
    <td><code>E713</code></td>
    <td>The account against which the payment was made has insufficient funds,or, card authentication failed due to invalid card expiry date</td>
    <td>INSUFFICIENT_FUNDS * EXPIRY_INVALID</td>
    <td>INSUFFICIENT_FUNDS_EXPIRY_INVALID</td>
  </tr>
  <tr>
    <td><code>E719</code></td>
    <td>Transaction failed due to card authentication failure and/or insufficient funds</td>
    <td>INSUFFICIENT_FUNDS * AUTHENTICATION_FAILURE</td>
    <td>INSUFFICIENT_FUNDS_AUTHENTICATION_FAILURE</td>
  </tr>
  <tr>
    <td><code>E706</code></td>
    <td>The account against which the payment was made has insufficient funds.</td>
    <td>Insufficient funds/over credit limit / Not sufficient funds</td>
    <td>INSUFFICIENT_FUNDS</td>
  </tr>
  <tr>
    <td><code>E4390</code></td>
    <td>INCORRECT OTP</td>
    <td>INCORRECT OTP</td>
    <td>INCORRECT_OTP</td>
  </tr>
  <tr>
    <td><code>E1502</code></td>
    <td>Incorrect request for SI, CC received in drop_category.</td>
    <td>INCOMPLETE_SI_REQUEST</td>
    <td>INCOMPLETE_SI_REQUEST</td>
  </tr>
  <tr>
    <td><code>E219</code></td>
    <td>Error at the Bank Server end</td>
    <td>INCOMPLETE_BANK_RESPONSE</td>
    <td>INCOMPLETE_BANK_RESPONSE</td>
  </tr>
  <tr>
    <td><code>E4391</code></td>
    <td>Transaction failed due to customer&#x27;s account being inactive or dormant</td>
    <td>INACTIVE OR DORMANT ACCOUNT (REMITTER)</td>
    <td>INACTIVE_OR_DORMANT_ACCOUNT_REMITTER</td>
  </tr>
  <tr>
    <td><code>E4392</code></td>
    <td>Transaction failed due to acquirer&#x27; account being inactive or dormant</td>
    <td>INACTIVE OR DORMANT ACCOUNT (BENEFICIARY)</td>
    <td>INACTIVE_OR_DORMANT_ACCOUNT_BENEFICIARY</td>
  </tr>
  <tr>
    <td><code>E4191</code></td>
    <td>IMPS TRANSACTION IS ALREADY BEEN PROCESSED</td>
    <td>IMPS TRANSACTION IS ALREADY BEEN PROCESSED</td>
    <td>IMPS_TRANSACTION_IS_ALREADY_BEEN_PROCESSED</td>
  </tr>
  <tr>
    <td><code>E4189</code></td>
    <td>IMPS PROCESSING FAILED IN UPI</td>
    <td>IMPS PROCESSING FAILED IN UPI</td>
    <td>IMPS_PROCESSING_FAILED_IN_UPI</td>
  </tr>
  <tr>
    <td><code>E4190</code></td>
    <td>IMPS IS SIGNED OFF</td>
    <td>IMPS IS SIGNED OFF</td>
    <td>IMPS_IS_SIGNED_OFF</td>
  </tr>
  <tr>
    <td><code>E4192</code></td>
    <td>IMPS IS DECLINED</td>
    <td>IMPS IS DECLINED</td>
    <td>IMPS_IS_DECLINED</td>
  </tr>
  <tr>
    <td><code>E4159</code></td>
    <td>ILLEGAL OPERATION</td>
    <td>ILLEGAL OPERATION</td>
    <td>ILLEGAL_OPERATION</td>
  </tr>
  <tr>
    <td><code>E4199</code></td>
    <td>IFSC IS NOT PRESENT</td>
    <td>IFSC IS NOT PRESENT</td>
    <td>IFSC_IS_NOT_PRESENT</td>
  </tr>
  <tr>
    <td><code>E1639</code></td>
    <td>Host down</td>
    <td>HOST_DOWN</td>
    <td>HOST_DOWN</td>
  </tr>
  <tr>
    <td><code>E2502</code></td>
    <td>Payu unable to parse ACS page for native</td>
    <td>HEADLESS_ELEMENT_MISSING</td>
    <td>HEADLESS_ELEMENT_MISSING</td>
  </tr>
  <tr>
    <td><code>E4250</code></td>
    <td>HEADER &amp; URL VERSION IS MISMATCHED</td>
    <td>HEADER &amp; URL VERSION IS MISMATCHED</td>
    <td>HEADER_URL_VERSION_IS_MISMATCHED</td>
  </tr>
  <tr>
    <td><code>E4076</code></td>
    <td>GLOBAL ADDRESS NOT SUPPORTED IN MANDATE</td>
    <td>GLOBAL ADDRESS NOT SUPPORTED IN MANDATE</td>
    <td>GLOBAL_ADDRESS_NOT_SUPPORTED_IN_MANDATE</td>
  </tr>
  <tr>
    <td><code>E4933</code></td>
    <td>NPCI General error</td>
    <td>GENERAL ERROR</td>
    <td>NPCI_ERROR</td>
  </tr>
  <tr>
    <td><code>E4382</code></td>
    <td>FUNCTIONALITY NOT YET AVAILABLE FOR MERCHANT THROUGH THE ACQUIRING BANK</td>
    <td>FUNCTIONALITY NOT YET AVAILABLE FOR MERCHANT THROUGH THE ACQUIRI</td>
    <td>FUNCTIONALITY_NOT_YET_AVAILABLE_FOR_MERCHANT_THROUGH_THE_ACQUIRING_BANK</td>
  </tr>
  <tr>
    <td><code>E4383</code></td>
    <td>FUNCTIONALITY NOT YET AVAILABLE FOR CUSTOMER THROUGH THE PAYEE PSP</td>
    <td>FUNCTIONALITY NOT YET AVAILABLE FOR CUSTOMER THROUGH THE PAYEE P</td>
    <td>FUNCTIONALITY_NOT_YET_AVAILABLE_FOR_CUSTOMER_THROUGH_THE_PAYEE_PSP</td>
  </tr>
  <tr>
    <td><code>E4022</code></td>
    <td>Transaction failed due to freeze period for the first time customer</td>
    <td>FREEZE PERIOD FOR FIRST TIME USER</td>
    <td>FREEZE_PERIOD_FOR_FIRST_TIME_USER</td>
  </tr>
  <tr>
    <td><code>E4154</code></td>
    <td>FORMATION IS NOT PROPER</td>
    <td>FORMATION IS NOT PROPER</td>
    <td>FORMATION_IS_NOT_PROPER</td>
  </tr>
  <tr>
    <td><code>E4338</code></td>
    <td>FORMAT ERROR (INVALID FORMAT) (REMITTER)</td>
    <td>FORMAT ERROR (INVALID FORMAT) (REMITTER)</td>
    <td>FORMAT_ERROR_INVALID_FORMAT_REMITTER</td>
  </tr>
  <tr>
    <td><code>E4339</code></td>
    <td>FORMAT ERROR (INVALID FORMAT) (BENEFICIARY)</td>
    <td>FORMAT ERROR (INVALID FORMAT) (BENEFICIARY)</td>
    <td>FORMAT_ERROR_INVALID_FORMAT_BENEFICIARY</td>
  </tr>
  <tr>
    <td><code>E2102</code></td>
    <td>Transaction not approved</td>
    <td>Format error</td>
    <td>TXN_FAILURE</td>
  </tr>
  <tr>
    <td><code>E4194</code></td>
    <td>FORM PROCESSING HAS BEEN FAILED IN UPI</td>
    <td>FORM PROCESSING HAS BEEN FAILED IN UPI</td>
    <td>FORM_PROCESSING_HAS_BEEN_FAILED_IN_UPI</td>
  </tr>
  <tr>
    <td><code>E4193</code></td>
    <td>FORM HAS BEEN SIGNED OFF</td>
    <td>FORM HAS BEEN SIGNED OFF</td>
    <td>FORM_HAS_BEEN_SIGNED_OFF</td>
  </tr>
  <tr>
    <td><code>E4269</code></td>
    <td>FOREX Error in ValQR</td>
    <td>FOREX Error in ValQR</td>
    <td>FOREX_Error_In_ValQR</td>
  </tr>
  <tr>
    <td><code>E9245</code></td>
    <td>Force Post</td>
    <td>Force Post</td>
    <td>FORCE_POST</td>
  </tr>
  <tr>
    <td><code>E4021</code></td>
    <td>Transaction failed due to first transaction limit exceeded by the customer</td>
    <td>FIRST TRANSACTION LIMIT EXCEEDED</td>
    <td>FIRST_TRANSACTION_LIMIT_EXCEEDED</td>
  </tr>
  <tr>
    <td><code>E9210</code></td>
    <td>File Update not Supported by receiver</td>
    <td>File Update not Supported by receiver</td>
    <td>FILE_UPDATE_NOT_SUPPORTED_BY_RECEIVER</td>
  </tr>
  <tr>
    <td><code>E9215</code></td>
    <td>File Update not Successful</td>
    <td>File Update not Successful</td>
    <td>FILE_UPDATE_NOT_SUCCESSFUL</td>
  </tr>
  <tr>
    <td><code>E9214</code></td>
    <td>File Update File Locked Out</td>
    <td>File Update File Locked Out</td>
    <td>FILE_UPDATE_FILE_LOCKED_OUT</td>
  </tr>
  <tr>
    <td><code>E9213</code></td>
    <td>File Update Field Edit Error</td>
    <td>File Update Field Edit Error</td>
    <td>FILE_UPDATE_FIELD_EDIT_ERROR</td>
  </tr>
  <tr>
    <td><code>E4888</code></td>
    <td>FAILURE</td>
    <td>FAILURE</td>
    <td>FAILURE_3</td>
  </tr>
  <tr>
    <td><code>E4890</code></td>
    <td>FAILURE</td>
    <td>FAILURE</td>
    <td>FAILURE_5</td>
  </tr>
  <tr>
    <td><code>E4891</code></td>
    <td>FAILURE</td>
    <td>FAILURE</td>
    <td>FAILURE_6</td>
  </tr>
  <tr>
    <td><code>E4892</code></td>
    <td>FAILURE</td>
    <td>FAILURE</td>
    <td>FAILURE_7</td>
  </tr>
  <tr>
    <td><code>E4897</code></td>
    <td>FAILURE</td>
    <td>FAILURE</td>
    <td>FAILURE_11</td>
  </tr>
  <tr>
    <td><code>E4900</code></td>
    <td>FAILURE</td>
    <td>FAILURE</td>
    <td>FAILURE_13</td>
  </tr>
  <tr>
    <td><code>E4903</code></td>
    <td>FAILURE</td>
    <td>FAILURE</td>
    <td>FAILURE_16</td>
  </tr>
  <tr>
    <td><code>E4904</code></td>
    <td>FAILURE</td>
    <td>FAILURE</td>
    <td>FAILURE_17</td>
  </tr>
  <tr>
    <td><code>E4907</code></td>
    <td>FAILURE</td>
    <td>FAILURE</td>
    <td>FAILURE_19</td>
  </tr>
  <tr>
    <td><code>E4909</code></td>
    <td>FAILURE</td>
    <td>FAILURE</td>
    <td>FAILURE_21</td>
  </tr>
  <tr>
    <td><code>E4910</code></td>
    <td>FAILURE</td>
    <td>FAILURE</td>
    <td>FAILURE_22</td>
  </tr>
  <tr>
    <td><code>E4803</code></td>
    <td>Transaction failed at bank end</td>
    <td>Failed</td>
    <td>Failed</td>
  </tr>
  <tr>
    <td><code>E1202</code></td>
    <td>Third Party Funds Transfer facility and Secure Access not enabled.</td>
    <td>FACILITY_UNAVAILABLE</td>
    <td>FACILITY_UNAVAILABLE</td>
  </tr>
  <tr>
    <td><code>E336</code></td>
    <td>Transaction failed due to incorrect card expiry date and/or insufficient funds</td>
    <td>EXPIRY_DATE_LOW_FUNDS</td>
    <td>EXPIRY_DATE_LOW_FUNDS</td>
  </tr>
  <tr>
    <td><code>E311</code></td>
    <td>Transaction declined due to invalid expiry details or the card is expired</td>
    <td>Expired card</td>
    <td>EXPIRED_CARD</td>
  </tr>
  <tr>
    <td><code>E4122</code></td>
    <td>Transaction failed as execution day and execution rule mismatch</td>
    <td>EXECUTION DAY AND EXECUTION RULE MISMATCH (PAYER)</td>
    <td>EXECUTION_DAY_AND_EXECUTION_RULE_MISMATCH_PAYER</td>
  </tr>
  <tr>
    <td><code>E4536</code></td>
    <td>Transaction failed as execution amount is higher than mandate created amount</td>
    <td>Execution amount exceeded to Mandate approved amount</td>
    <td>Execution_Amount_Exceeded_To_Mandate_Approved_Amount</td>
  </tr>
  <tr>
    <td><code>E909</code></td>
    <td>Transaction amount exceeds the withdrawal limit of the user account</td>
    <td>Exceeds withdrawal amount limit(s) / Withdrawal amount limit exc</td>
    <td>TRANSACTION_MAX_LIMIT_EXCEEDED</td>
  </tr>
  <tr>
    <td><code>E9230</code></td>
    <td>Exceeds Cash Limit</td>
    <td>Exceeds Cash Limit</td>
    <td>EXCEEDS_CASH_LIMIT</td>
  </tr>
  <tr>
    <td><code>E1645</code></td>
    <td>Transaction failed during authentication</td>
    <td>ERROR_OCCURRED_IN * ENROLLMENT_VALIDATION</td>
    <td>ERROR_OCCURRED_IN_ENROLLMENT_VALIDATION</td>
  </tr>
  <tr>
    <td><code>E209</code></td>
    <td>No Bank response</td>
    <td>Error: The request was received, but a service did not finish ru</td>
    <td>NO_BANK_RESPONSE</td>
  </tr>
  <tr>
    <td><code>E210</code></td>
    <td>Authentication failure or there is a delay in processing the transaction.</td>
    <td>Error - The request was received, but there was a timeout at the</td>
    <td>COMMUNICATION_ERROR</td>
  </tr>
  <tr>
    <td><code>E208</code></td>
    <td>Error at the Bank Server end</td>
    <td>Error - The request was received but there was a server timeout.</td>
    <td>BANK_SERVER_ERROR</td>
  </tr>
  <tr>
    <td><code>E309</code></td>
    <td>Bank denied transaction on the card.</td>
    <td>Error - General system failure</td>
    <td>GENERAL_SYSTEM_ERROR_PG</td>
  </tr>
  <tr>
    <td><code>E1909</code></td>
    <td>Error while processing enstage request</td>
    <td>ENSTAGE_PROCESSING_ERROR</td>
    <td>ENSTAGE_PROCESSING_ERROR</td>
  </tr>
  <tr>
    <td><code>E1908</code></td>
    <td>BIN not supported for pureS2S</td>
    <td>ENSTAGE_BIN_NOT * ELIGIBLE_PURES2S</td>
    <td>ENSTAGE_BIN_NOT_ELIGIBLE_PURES2S</td>
  </tr>
  <tr>
    <td><code>E4178</code></td>
    <td>Transaction failed due to technical error at customer&#x27;s application</td>
    <td>ENCRYPTION ERROR</td>
    <td>ADDRESS_RESOLUTION_IS_FAILED</td>
  </tr>
  <tr>
    <td><code>E303</code></td>
    <td>Payer could not be authenticated</td>
    <td>Encountered a Payer Authentication problem. Payer could not be a</td>
    <td>AUTHENTICATION_ERROR</td>
  </tr>
  <tr>
    <td><code>E1301</code></td>
    <td>EMI not applicable for this transactions.</td>
    <td>EMI_NOT_APPLICABLE</td>
    <td>EMI_NOT_APPLICABLE</td>
  </tr>
  <tr>
    <td><code>E9236</code></td>
    <td>E-commerce Decline</td>
    <td>E-commerce Decline</td>
    <td>ECOMMERCE_DECLINE</td>
  </tr>
  <tr>
    <td><code>E1300</code></td>
    <td>Customer has pressed the refresh key during the payment process.</td>
    <td>DUPLICATE_SESSION_ID</td>
    <td>DUPLICATE_SESSION_ID</td>
  </tr>
  <tr>
    <td><code>E344</code></td>
    <td>Transaction Failed</td>
    <td>DUPLICATE_CONTACT</td>
    <td>DUPLICATE_CONTACT</td>
  </tr>
  <tr>
    <td><code>E504</code></td>
    <td>The transaction has been identified as duplicate transaction.</td>
    <td>Duplicate Transaction</td>
    <td>DUPLICATE_TRANSACTION</td>
  </tr>
  <tr>
    <td><code>E4020</code></td>
    <td>DUPLICATE RRN FOUND IN THE TRANSACTION. (REMITTER)</td>
    <td>DUPLICATE RRN FOUND IN THE TRANSACTION. (REMITTER)</td>
    <td>DUPLICATE_RRN_FOUND_IN_THE_TRANSACTION__REMITTER</td>
  </tr>
  <tr>
    <td><code>E4019</code></td>
    <td>DUPLICATE RRN FOUND IN THE TRANSACTION. (BENEFICIARY)</td>
    <td>DUPLICATE RRN FOUND IN THE TRANSACTION. (BENEFICIARY)</td>
    <td>DUPLICATE_RRN_FOUND_IN_THE_TRANSACTION__BENEFICIARY</td>
  </tr>
  <tr>
    <td><code>E4319</code></td>
    <td>DUPLICATE MANDATE REQUEST FOR SAME ITEM</td>
    <td>DUPLICATE MANDATE REQUEST FOR SAME ITEM</td>
    <td>DUPLICATE_MANDATE_REQUEST_FOR_SAME_ITEM</td>
  </tr>
  <tr>
    <td><code>E4118</code></td>
    <td>Transaction failed due to duplicate mandate request</td>
    <td>DUPLICATE MANDATE REQUEST BD</td>
    <td>DUPLICATE_MANDATE_REQUEST_BD</td>
  </tr>
  <tr>
    <td><code>E9212</code></td>
    <td>Duplicate File Update Record</td>
    <td>Duplicate File Update Record</td>
    <td>DUPLICATE_FILE_UPDATE_RECORD</td>
  </tr>
  <tr>
    <td><code>E4033</code></td>
    <td>DUPLICATE BLOCKFUND FOR MANDATE REQUEST</td>
    <td>DUPLICATE BLOCKFUND FOR MANDATE REQUEST</td>
    <td>DUPLICATE_BLOCKFUND_FOR_MANDATE_REQUEST</td>
  </tr>
  <tr>
    <td><code>E307</code></td>
    <td>Transaction declined with do not honor</td>
    <td>Do not honor</td>
    <td>DO_NOT_HONOUR</td>
  </tr>
  <tr>
    <td><code>E307</code></td>
    <td>Risk Service denied transaction</td>
    <td>Risk Service denied transaction - DO_NOT_HONOUR</td>
    <td></td>
  </tr>
  <tr>
    <td><code>E804</code></td>
    <td>Payment gateway seems to be down at this moment.</td>
    <td>DISABLE_PG_NOT_AVAILABLE_HANDLING</td>
    <td>DISABLE_PG_NOT_AVAILABLE_HANDLING</td>
  </tr>
  <tr>
    <td><code>E4212</code></td>
    <td>DEVICE REGISTRATION FAILED IN UPI</td>
    <td>DEVICE REGISTRATION FAILED IN UPI</td>
    <td>DEVICE_REGISTRATION_FAILED_IN_UPI</td>
  </tr>
  <tr>
    <td><code>E225</code></td>
    <td>Transaction in Progress</td>
    <td>Destination cannot be found for routing / Unable to route transa</td>
    <td>TRANSACTION_IN_PROGRESS</td>
  </tr>
  <tr>
    <td><code>DEFAULT</code></td>
    <td>Bank was unable to authenticate.</td>
    <td>DEFAULT_VALUE</td>
    <td>DEFAULT_VALUE</td>
  </tr>
  <tr>
    <td><code>E712</code></td>
    <td>The transaction could not be processed due to incomplete data provided at the users end.</td>
    <td>Declined - The request is missing one or more fields</td>
    <td>INCOMPLETE_DATA</td>
  </tr>
  <tr>
    <td><code>E2100</code></td>
    <td>Invalid Request received for processing.</td>
    <td>Declined - One or more fields in the request contains invalid da</td>
    <td>INVALID_DATA_RECEIVED_IN_REQUEST</td>
  </tr>
  <tr>
    <td><code>E1638</code></td>
    <td>Transaction Already Reversed</td>
    <td>Decline - The transaction has already been settled or reversed.</td>
    <td>TRANSACTION_REVERSED</td>
  </tr>
  <tr>
    <td><code>E1701</code></td>
    <td>Invalid Payment ID</td>
    <td>Decline - The request ID is invalid.</td>
    <td>INVALID_PAYMENT_ID</td>
  </tr>
  <tr>
    <td><code>E1623</code></td>
    <td>Customer Authentication failed due to incorrect ATM PIN.</td>
    <td>Decline - The Pinless Debit card&#x27;s use frequency or maximum amou</td>
    <td>ATM_MAX_LIMIT_EXCEEDED</td>
  </tr>
  <tr>
    <td><code>E329</code></td>
    <td>Transaction declined by the issuer</td>
    <td>Decline - The issuing bank has questions about the request. You</td>
    <td>ISSUER_DECLINED_LOW_FUNDS</td>
  </tr>
  <tr>
    <td><code>E902</code></td>
    <td>Invalid Card Number</td>
    <td>Decline - The card type is not accepted by the payment processor</td>
    <td>INVALID_CARD_TYPE</td>
  </tr>
  <tr>
    <td><code>E1628</code></td>
    <td>Daily limit exceeded</td>
    <td>Decline - The card has reached the credit limit</td>
    <td>LIMIT_EXCEEDED</td>
  </tr>
  <tr>
    <td><code>E1653</code></td>
    <td>Card Issuer Unavailable</td>
    <td>Decline - Issuing bank unavailable</td>
    <td>ISSUER_UNAVAILABLE</td>
  </tr>
  <tr>
    <td><code>E312</code></td>
    <td>Bank denied transaction on the card.</td>
    <td>Decline - General decline of the card. No other information prov</td>
    <td>BANK_DENIED</td>
  </tr>
  <tr>
    <td><code>E2111</code></td>
    <td>Transaction failed due to technical issue at Issuer/Acquirer end</td>
    <td>Decline - General decline by the processor.</td>
    <td>GENERAL_DECLINE_BY_PROCESSOR</td>
  </tr>
  <tr>
    <td><code>E1400</code></td>
    <td>Invalid data received from bank.</td>
    <td>Decline - card verification number (CVN) did not match</td>
    <td>INVALID_DATA_NEW</td>
  </tr>
  <tr>
    <td><code>E4182</code></td>
    <td>Transaction failed as debit reversal failed in the customer&#x27;s account</td>
    <td>DEBIT REVERT HAS BEEN FAILED</td>
    <td>DEBIT_REVERT_HAS_BEEN_FAILED</td>
  </tr>
  <tr>
    <td><code>E4142</code></td>
    <td>Debit failed due to timeout at customer&#x27;s bank</td>
    <td>DEBIT REVERSAL TIMEOUT(REVERSAL)</td>
    <td>DEBIT_REVERSAL_TIMEOUT_REVERSAL</td>
  </tr>
  <tr>
    <td><code>E4179</code></td>
    <td>Transaction failed as debit failed from the customer&#x27;s account</td>
    <td>DEBIT HAS BEEN FAILED</td>
    <td>DEBIT_HAS_BEEN_FAILED</td>
  </tr>
  <tr>
    <td><code>E4035</code></td>
    <td>DEBIT AMOUNT IS NOT BLOCKED FOR THE CUSTOMER</td>
    <td>DEBIT AMOUNT IS NOT BLOCKED FOR THE CUSTOMER</td>
    <td>DEBIT_AMOUNT_IS_NOT_BLOCKED_FOR_THE_CUSTOMER</td>
  </tr>
  <tr>
    <td><code>E4036</code></td>
    <td>DEBIT AMOUNT GREATER THAN BLOCKED AMOUNT</td>
    <td>DEBIT AMOUNT GREATER THAN BLOCKED AMOUNT</td>
    <td>DEBIT_AMOUNT_GREATER_THAN_BLOCKED_AMOUNT</td>
  </tr>
  <tr>
    <td><code>E4213</code></td>
    <td>DATA TAG SHOULD CONTAIN 4 PARTS DURING DEVICE REGISTRATION</td>
    <td>DATA TAG SHOULD CONTAIN 4 PARTS DURING DEVICE REGISTRATION</td>
    <td>DATA_TAG_SHOULD_CONTAIN_4_PARTS_DURING_DEVICE_REGISTRATION</td>
  </tr>
  <tr>
    <td><code>E1627</code></td>
    <td>Daily limit for wrong ATM PIN attempts reached</td>
    <td>DAILY_ATM_MAX_LIMIT_EXCEEDED</td>
    <td>DAILY_ATM_MAX_LIMIT_EXCEEDED</td>
  </tr>
  <tr>
    <td><code>E9235</code></td>
    <td>CVR validation failed by Issuer</td>
    <td>CVR validation failed by Issuer</td>
    <td>CVR_VALIDATION_FAILED_BY_ISSUER</td>
  </tr>
  <tr>
    <td><code>E206</code></td>
    <td>Transaction failed as the bank servers are blocked for end of the day processing. Consequently, its servers are temporarily closed to any authentication requests.</td>
    <td>CUTOFF_ERROR</td>
    <td>CUTOFF_ERROR</td>
  </tr>
  <tr>
    <td><code>E4352</code></td>
    <td>Transaction failed due to CBS cut-off at customer&#x27;s bank</td>
    <td>CUT-OFF IS IN PROCESS (REMITTER)</td>
    <td>CUT_OFF_IS_IN_PROCESS_REMITTER</td>
  </tr>
  <tr>
    <td><code>E4353</code></td>
    <td>Transaction failed due to CBS cut-off at acquirer&#x27;s end</td>
    <td>CUT-OFF IS IN PROCESS (BENEFICIARY)</td>
    <td>CUT_OFF_IS_IN_PROCESS_BENEFICIARY</td>
  </tr>
  <tr>
    <td><code>E9227</code></td>
    <td>Cut-off in Progress</td>
    <td>Cut-off in Progress</td>
    <td>CUTOFF_IN_PROGRESS</td>
  </tr>
  <tr>
    <td><code>E2401</code></td>
    <td>The customer is not eligible for this transaction</td>
    <td>CUSTOMER_NOT_ELIGIBLE * FOR_THIS_TRANSACTION</td>
    <td>CUSTOMER_NOT_ELIGIBLE_FOR_THIS_TRANSACTION</td>
  </tr>
  <tr>
    <td><code>E2403</code></td>
    <td>Customer KYC is pending at Issuer&#x27;s end</td>
    <td>CUSTOMER_KYC_PENDING</td>
    <td>CUSTOMER_KYC_PENDING</td>
  </tr>
  <tr>
    <td><code>E9206</code></td>
    <td>Customer Dispute</td>
    <td>Customer Dispute</td>
    <td>CUSTOMER_DISPUTE</td>
  </tr>
  <tr>
    <td><code>E9205</code></td>
    <td>Customer Cancellation</td>
    <td>Customer Cancellation</td>
    <td>CUSTOMER_CANCELLATION</td>
  </tr>
  <tr>
    <td><code>E205</code></td>
    <td>Error at the Bank Server end</td>
    <td>CURL_ERROR_ENROLLED</td>
    <td>CURL_ERROR_ENROLLED</td>
  </tr>
  <tr>
    <td><code>E214</code></td>
    <td>The Bank servers are unreachable over the network</td>
    <td>CURL_CALL_FAILURE</td>
    <td>CURL_CALL_FAILURE</td>
  </tr>
  <tr>
    <td><code>E9223</code></td>
    <td>Cryptographic Error</td>
    <td>Cryptographic Error</td>
    <td>CRYPTOGRAPHIC_ERROR</td>
  </tr>
  <tr>
    <td><code>EX311</code></td>
    <td>Transaction Failed</td>
    <td>CROSS_BORDER * IMPORT_ERROR</td>
    <td>CROSS_BORDER_IMPORT_ERROR</td>
  </tr>
  <tr>
    <td><code>E4214</code></td>
    <td>CREDS BLOCK SHOULD CONTAIN CORRECT ELEMENTS DURING DEVICE REGISTRATION</td>
    <td>CREDS BLOCK SHOULD CONTAIN CORRECT ELEMENTS DURING DEVICE REGIST</td>
    <td>CREDS_BLOCK_SHOULD_CONTAIN_CORRECT_ELEMENTS_DURING_DEVICE_REGISTRATION</td>
  </tr>
  <tr>
    <td><code>E4181</code></td>
    <td>Transaction failed as credit reversal failed from the acquirer&#x27;s account</td>
    <td>CREDIT REVERT HAS BEEN FAILED</td>
    <td>CREDIT_REVERT_HAS_BEEN_FAILED</td>
  </tr>
  <tr>
    <td><code>E4180</code></td>
    <td>Credit failed due to technical issue at acquirer&#x27;s bank</td>
    <td>CREDIT HAS BEEN FAILED</td>
    <td>CREDIT_HAS_BEEN_FAILED</td>
  </tr>
  <tr>
    <td><code>E4160</code></td>
    <td>CREDENTIALS IS NOT PRESENT</td>
    <td>CREDENTIALS IS NOT PRESENT</td>
    <td>CREDENTIALS_IS_NOT_PRESENT</td>
  </tr>
  <tr>
    <td><code>E4016</code></td>
    <td>Transaction failed due to currency not supported</td>
    <td>Country/ Currency not supported</td>
    <td>Country__Currency_Not_Supported</td>
  </tr>
  <tr>
    <td><code>E1629</code></td>
    <td>Transaction declined due to technical failure at bank end</td>
    <td>Contact Card Issuer</td>
    <td>BANK_TECHNICAL_FAILURE</td>
  </tr>
  <tr>
    <td><code>E4015</code></td>
    <td>COMPLIANCE ERROR CODE FOR ISSUER BD</td>
    <td>COMPLIANCE ERROR CODE FOR ISSUER BD</td>
    <td>COMPLIANCE_ERROR_CODE_FOR_ISSUER_BD</td>
  </tr>
  <tr>
    <td><code>E9232</code></td>
    <td>Compliance error code for issuer</td>
    <td>Compliance error code for issuer</td>
    <td>COMPLIANCE_ERROR_CODE_FOR_ISSUER</td>
  </tr>
  <tr>
    <td><code>E4014</code></td>
    <td>COMPLIANCE ERROR CODE FOR ACQUIRER</td>
    <td>COMPLIANCE ERROR CODE FOR ACQUIRER</td>
    <td>COMPLIANCE_ERROR_CODE_FOR_ACQUIRER</td>
  </tr>
  <tr>
    <td><code>E9216</code></td>
    <td>Completed Partially</td>
    <td>Completed Partially</td>
    <td>COMPLETED_PARTIALLY</td>
  </tr>
  <tr>
    <td><code>E1902</code></td>
    <td>VPA is blank.Either validations have failed or merchant has not passed VPA</td>
    <td>COLLECT_EMPTY_VPA</td>
    <td>COLLECT_EMPTY_VPA</td>
  </tr>
  <tr>
    <td><code>E4149</code></td>
    <td>Transaction request declined as merchant is blocked by the customer</td>
    <td>COLLECT REQUEST IS DECLINED AS REQUESTOR IS BLOCKED BY CUSTOMER</td>
    <td>COLLECT_REQUEST_IS_DECLINED_AS_REQUESTOR_IS_BLOCKED_BY_CUSTOMER</td>
  </tr>
  <tr>
    <td><code>E4218</code></td>
    <td>Transaction failed due to collect request expired</td>
    <td>COLLECT EXPIRED</td>
    <td>COLLECT_EXPIRED</td>
  </tr>
  <tr>
    <td><code>E4511</code></td>
    <td>Transaction declined due to collect by date less that current date</td>
    <td>Collect By date should be greater than or equal to Current date</td>
    <td>Collect_By_Date_Should_Be_Greater_Than_Or_Equal_To_Current_Date</td>
  </tr>
  <tr>
    <td><code>E4174</code></td>
    <td>CM URL IS NOT FOUND</td>
    <td>CM URL IS NOT FOUND</td>
    <td>CM_URL_IS_NOT_FOUND</td>
  </tr>
  <tr>
    <td><code>E4172</code></td>
    <td>CM REQUEST TIMEOUT</td>
    <td>CM REQUEST TIMEOUT</td>
    <td>CM_REQUEST_TIMEOUT</td>
  </tr>
  <tr>
    <td><code>E4171</code></td>
    <td>CM REQUEST IS DECLINED</td>
    <td>CM REQUEST IS DECLINED</td>
    <td>CM_REQUEST_IS_DECLINED</td>
  </tr>
  <tr>
    <td><code>E4173</code></td>
    <td>CM REQUEST ACKNOWLEDGEMENT IS NOT RECEIVED</td>
    <td>CM REQUEST ACKNOWLEDGEMENT IS NOT RECEIVED</td>
    <td>CM_REQUEST_ACKNOWLEDGEMENT_IS_NOT_RECEIVED</td>
  </tr>
  <tr>
    <td><code>E717</code></td>
    <td>Transaction declined as bank reported account to be closed</td>
    <td>Closed account</td>
    <td>INVALID_ACCOUNT_NUMBER</td>
  </tr>
  <tr>
    <td><code>E213</code></td>
    <td>Card authentication failure</td>
    <td>CHECKSUM_FAILURE</td>
    <td>CHECKSUM_FAILURE</td>
  </tr>
  <tr>
    <td><code>E4164</code></td>
    <td>CHECKSUM FAILED</td>
    <td>CHECKSUM FAILED</td>
    <td>CHECKSUM_FAILED</td>
  </tr>
  <tr>
    <td><code>E601</code></td>
    <td>Challan Generation Failed</td>
    <td>CHALLAN_PAYMENT * TRANSACTION_FAILED</td>
    <td>CHALLAN_PAYMENT_TRANSACTION_FAILED</td>
  </tr>
  <tr>
    <td><code>E4023</code></td>
    <td>CERTIFICATE NOT FOUND</td>
    <td>CERTIFICATE NOT FOUND</td>
    <td>CERTIFICATE_NOT_FOUND</td>
  </tr>
  <tr>
    <td><code>E802</code></td>
    <td>Issuing Bank was temporarily not available so set as bounced.</td>
    <td>CC_DC_ISSUING_BANK_DOWN</td>
    <td>CC_DC_ISSUING_BANK_DOWN</td>
  </tr>
  <tr>
    <td><code>E1619</code></td>
    <td>Category or ibibo code not recieved</td>
    <td>CATEGORY_IBIBO_NOT_RCVD_S2SFLOW</td>
    <td>CATEGORY_IBIBO_NOT_RCVD_S2SFLOW</td>
  </tr>
  <tr>
    <td><code>E9249</code></td>
    <td>Cash back exceeds daily limit</td>
    <td>Cash back exceeds daily limit</td>
    <td>CASH_BACK_EXCEEDS_DAILY_LIMIT</td>
  </tr>
  <tr>
    <td><code>E9238</code></td>
    <td>Card Re-use Limit Exceeded</td>
    <td>Card Re-use Limit Exceeded</td>
    <td>CARD_REUSE_LIMIT_EXCEEDED</td>
  </tr>
  <tr>
    <td><code>E9247</code></td>
    <td>Card Not Supported</td>
    <td>Card Not Supported</td>
    <td>CARD_NOT_SUPPORTED</td>
  </tr>
  <tr>
    <td><code>E9219</code></td>
    <td>Card Acceptor Call Acquirer Security</td>
    <td>Card Acceptor Call Acquirer Security</td>
    <td>CARD_ACCEPTOR_CALL_ACQUIRER_SECURITY</td>
  </tr>
  <tr>
    <td><code>E4519</code></td>
    <td>Refund failed due to insufficient amount</td>
    <td>Cannot verify PIN</td>
    <td>Insufficient_Amount</td>
  </tr>
  <tr>
    <td><code>E4930</code></td>
    <td>Refund cannot be processed</td>
    <td>Cannot process Refund</td>
    <td>Cannot_Process_Refund</td>
  </tr>
  <tr>
    <td><code>E1605</code></td>
    <td>Transaction failed due to customer pressing cancel button.</td>
    <td>CANCEL_BUTTON_PRESSED_BY_USER</td>
    <td>CANCEL_BUTTON_PRESSED_BY_USER</td>
  </tr>
  <tr>
    <td><code>E9248</code></td>
    <td>Transaction is decline by issuing bank</td>
    <td>CAF status = 0 or 9</td>
    <td>CAF_STATUS</td>
  </tr>
  <tr>
    <td><code>E1635</code></td>
    <td>Broker failure received from bank</td>
    <td>BROKER_FAILURE</td>
    <td>BROKER_FAILURE</td>
  </tr>
  <tr>
    <td><code>E201</code></td>
    <td>The transaction failed due to invalid or absent card number.</td>
    <td>BRAND_INVALID</td>
    <td>BRAND_INVALID</td>
  </tr>
  <tr>
    <td><code>E1210</code></td>
    <td>Credit card used in Debit Card PG.</td>
    <td>BLOCK_CREDIT_CARDS</td>
    <td>BLOCK_CREDIT_CARDS</td>
  </tr>
  <tr>
    <td><code>E4089</code></td>
    <td>BLOCKFUND=Y IS ALLOWED FOR CREATE/UPDATE AND BLOCKFUND=N IS ALLOWED FOR REVOKE</td>
    <td>BLOCKFUND=Y IS ALLOWED FOR CREATE/UPDATE AND BLOCKFUND=N IS ALLO</td>
    <td>BLOCKFUND_Y_IS_ALLOWED_FOR_CREATE_UPDATE_AND_BLOCKFUND_N_IS_ALLOWED_FOR_REVOKE</td>
  </tr>
  <tr>
    <td><code>E4088</code></td>
    <td>BLOCKFUND IS ALLOWED ONLY IF THE PURPOSE=01</td>
    <td>BLOCKFUND IS ALLOWED ONLY IF THE PURPOSE=01</td>
    <td>BLOCKFUND_IS_ALLOWED_ONLY_IF_THE_PURPOSE_01</td>
  </tr>
  <tr>
    <td><code>E1660</code></td>
    <td>MCP Lookup api failed after sending S2S response</td>
    <td>BLAZE_MCP_LOOKUP_ERROR</td>
    <td>BLAZE_MCP_LOOKUP_ERROR</td>
  </tr>
  <tr>
    <td><code>E1659</code></td>
    <td>Error while connecting with blaze net encryption utility</td>
    <td>BLAZE_ENCRYPTION_ERROR</td>
    <td>BLAZE_ENCRYPTION_ERROR</td>
  </tr>
  <tr>
    <td><code>E4935</code></td>
    <td>Cryptogram missing</td>
    <td>Blank or null card token crypto</td>
    <td>CRYPTOGRAM_MISSING</td>
  </tr>
  <tr>
    <td><code>E4934</code></td>
    <td>Invalid BIN</td>
    <td>Bin Not Found</td>
    <td>INVALID_BIN</td>
  </tr>
  <tr>
    <td><code>E4262</code></td>
    <td>BENIFICIARY BANK,VERSION/TAGS SENT NOT SUPPORTED BY BANK</td>
    <td>BENIFICIARY BANK,VERSION/TAGS SENT NOT SUPPORTED BY BANK</td>
    <td>BENIFICIARY_BANK_VERSION_TAGS_SENT_NOT_SUPPORTED_BY_BANK</td>
  </tr>
  <tr>
    <td><code>E4260</code></td>
    <td>BENIFICIARY BANK,REQUEST &amp; RESPONSE HEADER VERSION MISMATCH</td>
    <td>BENIFICIARY BANK,REQUEST &amp; RESPONSE HEADER VERSION MISMATCH</td>
    <td>BENIFICIARY_BANK_REQUEST_RESPONSE_HEADER_VERSION_MISMATCH</td>
  </tr>
  <tr>
    <td><code>E4261</code></td>
    <td>BENIFICIARY BANK,HEADER OR URL VERSION MISMATCHED</td>
    <td>BENIFICIARY BANK,HEADER OR URL VERSION MISMATCHED</td>
    <td>BENIFICIARY_BANK_HEADER_OR_URL_VERSION_MISMATCHED</td>
  </tr>
  <tr>
    <td><code>E4097</code></td>
    <td>BENIFICIARY BANK DOES NOT SUPPORTS VERSION MANDATE 2.1</td>
    <td>BENIFICIARY BANK DOES NOT SUPPORTS VERSION MANDATE 2.1</td>
    <td>BENIFICIARY_BANK_DOES_NOT_SUPPORTS_VERSION_MANDATE_2_1</td>
  </tr>
  <tr>
    <td><code>E4358</code></td>
    <td>Transaction failed due to acquirers bank CBS offline</td>
    <td>BENEFICIARY CBS OFFLINE</td>
    <td>BENEFICIARY_CBS_OFFLINE</td>
  </tr>
  <tr>
    <td><code>E4291</code></td>
    <td>Mandate not supported by acquirer&#x27;s bank</td>
    <td>BENEFICIARY BANK NOT REGISTERED (MANDATE)</td>
    <td>BENEFICIARY_BANK_NOT_REGISTERED_MANDATE</td>
  </tr>
  <tr>
    <td><code>E4364</code></td>
    <td>Transaction declined due to acquirer&#x27;s account blocked or frozen</td>
    <td>BENEFICIARY ACCOUNT BLOCKED/FROZEN</td>
    <td>BENEFICIARY_ACCOUNT_BLOCKED_FROZEN</td>
  </tr>
  <tr>
    <td><code>E4027</code></td>
    <td>BANKS HSM IS DOWN(REMITTER)</td>
    <td>BANKS HSM IS DOWN(REMITTER)</td>
    <td>BANKS_HSM_IS_DOWN_REMITTER</td>
  </tr>
  <tr>
    <td><code>E4384</code></td>
    <td>BANKS AS BENEFICIARY NOT LIVE ON PARTICULAR TXN TYPE</td>
    <td>BANKS AS BENEFICIARY NOT LIVE ON PARTICULAR TXN TYPE</td>
    <td>BANKS_AS_BENEFICIARY_NOT_LIVE_ON_PARTICULAR_TXN_TYPE</td>
  </tr>
  <tr>
    <td><code>E4039</code></td>
    <td>BANK/PSP IS NOT SUPPORTING VERSION 2</td>
    <td>BANK/PSP IS NOT SUPPORTING VERSION 2</td>
    <td>BANK_PSP_IS_NOT_SUPPORTING_VERSION_2</td>
  </tr>
  <tr>
    <td><code>E4281</code></td>
    <td>BANK TD RESPMANDATE NEGATIVE ACK SENT FROM UPI TO REMITTER BANK</td>
    <td>BANK TD RESPMANDATE NEGATIVE ACK SENT FROM UPI TO REMITTER BANK</td>
    <td>BANK_TD_RESPMANDATE_NEGATIVE_ACK_SENT_FROM_UPI_TO_REMITTER_BANK</td>
  </tr>
  <tr>
    <td><code>E9251</code></td>
    <td>Bank Settlement Limit Exceeded</td>
    <td>Bank Settlement Limit Exceeded</td>
    <td>BANK_SETTLEMENT_LIMIT_EXCEEDED</td>
  </tr>
  <tr>
    <td><code>E9251</code></td>
    <td>PAYER PSP THROTTLE DECLINE</td>
    <td>ADDRESS_RESOLUTION_IS_FAILED</td>
    <td></td>
  </tr>
  <tr>
    <td><code>E9252</code></td>
    <td>PSP REQUEST META ACKNOWLEDGEMENT NOT RECEIVED</td>
    <td>ADDRESS_RESOLUTION_IS_FAILED</td>
    <td></td>
  </tr>
  <tr>
    <td><code>E1607</code></td>
    <td>Transaction failed due to user pressing back button.</td>
    <td>BACK_BUTTON_PRESSED</td>
    <td>BACK_BUTTON_PRESSED</td>
  </tr>
  <tr>
    <td><code>E1703</code></td>
    <td>Auth Data mismatch</td>
    <td>AUTH_DATA_MISMATCH</td>
    <td>AUTH_DATA_MISMATCH</td>
  </tr>
  <tr>
    <td><code>E1001</code></td>
    <td>Bank network is unavailable at the moment.</td>
    <td>AUTHENTICATION_SERVICE_UNAVAILABLE_ASU</td>
    <td>AUTHENTICATION_SERVICE_UNAVAILABLE_ASU</td>
  </tr>
  <tr>
    <td><code>E334</code></td>
    <td>Authentication service not available</td>
    <td>AUTHENTICATION_SERVICE_UNAVAILABLE</td>
    <td>AUTHENTICATION_SERVICE_UNAVAILABLE</td>
  </tr>
  <tr>
    <td><code>E1003</code></td>
    <td>Card not enabled for Ecomm transactions, either the card is newly issued or has not been used for any online transaction during last 12 months</td>
    <td>AUTHENTICATION_NOT_ATTEMPTED</td>
    <td>AUTHENTICATION_NOT_ATTEMPTED</td>
  </tr>
  <tr>
    <td><code>E914</code></td>
    <td>Transaction failed by Acquirer due to invalid request</td>
    <td>AUTHENTICATION_INVALID_REQUEST_ERROR</td>
    <td>AUTHENTICATION_INVALID_REQUEST_ERROR</td>
  </tr>
  <tr>
    <td><code>E1910</code></td>
    <td>Authentication failed or invalid PaRes received</td>
    <td>AUTHENTICATION_INVALID_PARES</td>
    <td>AUTHENTICATION_INVALID_PARES</td>
  </tr>
  <tr>
    <td><code>E916</code></td>
    <td>Transaction failed due to invalid merchant config at Acquirer</td>
    <td>AUTHENTICATION_INVALID_MERCHANT_CONFIG</td>
    <td>AUTHENTICATION_INVALID_MERCHANT_CONFIG</td>
  </tr>
  <tr>
    <td><code>E915</code></td>
    <td>Transaction failed by Acquirer due to invalid request data</td>
    <td>AUTHENTICATION_INVALID_DATA_ERROR</td>
    <td>AUTHENTICATION_INVALID_DATA_ERROR</td>
  </tr>
  <tr>
    <td><code>E917</code></td>
    <td>Transaction failed due to card authentication failure</td>
    <td>AUTHENTICATION_FAILURE</td>
    <td>AUTHENTICATION_FAILURE</td>
  </tr>
  <tr>
    <td><code>E232</code></td>
    <td>Payer could not be authenticated</td>
    <td>AUTHENTICATION_ATTEMPTS</td>
    <td>AUTHENTICATION_ATTEMPTS</td>
  </tr>
  <tr>
    <td><code>E1002</code></td>
    <td>Authentication was attempted but was not available at banks end</td>
    <td>AUTHENTICATION_ATTEMPTED</td>
    <td>AUTHENTICATION_ATTEMPTED</td>
  </tr>
  <tr>
    <td><code>E600</code></td>
    <td>Bank denied transaction on the card.</td>
    <td>Authentication declined by issuer</td>
    <td>PAYU_API_ERROR</td>
  </tr>
  <tr>
    <td><code>E1602</code></td>
    <td>Transaction failed. Page expired due to no user input.</td>
    <td>ATM_PIN_PAGE_EXPIRED</td>
    <td>OTP_PAGE_EXPIRED</td>
  </tr>
  <tr>
    <td><code>E9233</code></td>
    <td>ARQC validation failed by Issuer</td>
    <td>ARQC validation failed by Issuer</td>
    <td>ARQC_VALIDATION_FAILED_BY_ISSUER</td>
  </tr>
  <tr>
    <td><code>E9203</code></td>
    <td>Approved VIP (not used)</td>
    <td>Approved VIP (not used)</td>
    <td>APPROVED_VIP</td>
  </tr>
  <tr>
    <td><code>E9204</code></td>
    <td>Approved Update Track 3 (not used)</td>
    <td>Approved Update Track 3 (not used)</td>
    <td>APPROVED_TRACK</td>
  </tr>
  <tr>
    <td><code>E9222</code></td>
    <td>Approved (ANZ only)</td>
    <td>Approved (ANZ only)</td>
    <td>APPROVED_ANZ_ONLY</td>
  </tr>
  <tr>
    <td><code>E220</code></td>
    <td>Amount or transaction doesnt match</td>
    <td>AMOUNT_TRANSACTION_MISMATCH</td>
    <td>AMOUNT_TRANSACTION_MISMATCH</td>
  </tr>
  <tr>
    <td><code>E4092</code></td>
    <td>AMOUNT RULE SHOULD BE ALWAYS MAX IF PURPOSE=01</td>
    <td>AMOUNT RULE SHOULD BE ALWAYS MAX IF PURPOSE=01</td>
    <td>AMOUNT_RULE_SHOULD_BE_ALWAYS_MAX_IF_PURPOSE_01</td>
  </tr>
  <tr>
    <td><code>E4161</code></td>
    <td>AMOUNT OR CURRENCY MISMATCH</td>
    <td>AMOUNT OR CURRENCY MISMATCH</td>
    <td>AMOUNT_OR_CURRENCY_MISMATCH</td>
  </tr>
  <tr>
    <td><code>E4151</code></td>
    <td>Transaction failed due to amount limit on merchant exceeded</td>
    <td>AMOUNT CAP IS EXCEEDED</td>
    <td>AMOUNT_CAP_IS_EXCEEDED</td>
  </tr>
  <tr>
    <td><code>EA08</code></td>
    <td>Alt ID Provisioning Failed</td>
    <td>Alt ID Provisioning Failed due to incorrect Card Details</td>
    <td>ALT_ID_PROV</td>
  </tr>
  <tr>
    <td><code>E9217</code></td>
    <td>Allowable PIN Tries Exceeded</td>
    <td>Allowable PIN Tries Exceeded</td>
    <td>ALLOWABLE_PIN_TRIES_EXCEEDED</td>
  </tr>
  <tr>
    <td><code>E708</code></td>
    <td>Card authentication failed as user exceeded maximum number of permitted retries for PIN.</td>
    <td>Allowable number of PIN tries exceeded</td>
    <td>PIN_RETRIES_EXCEEDED</td>
  </tr>
  <tr>
    <td><code>E4037</code></td>
    <td>Transaction failed due to funds blocked for mandate in customer&#x27;s account</td>
    <td>ADEQUATE FUNDS NOT AVAILABLE IN THE ACCOUNT BECAUSE FUNDS HAVE B</td>
    <td>ADEQUATE_FUNDS_NOT_AVAILABLE_IN_THE_ACCOUNT_BECAUSE_FUNDS_HAVE_BEEN_BD_BLOCKED_FOR_MANDATE</td>
  </tr>
  <tr>
    <td><code>E304</code></td>
    <td>The address needs to match with the records of card issuing bank</td>
    <td>ADDRESS_INVALID</td>
    <td>ADDRESS_INVALID</td>
  </tr>
  <tr>
    <td><code>E4013</code></td>
    <td>Transaction failed due to beneficiary timeout</td>
    <td>ACQUIRER/BENEFICIARY UNAVAILABLE(TIMEOUT)</td>
    <td>ACQUIRER_BENEFICIARY_UNAVAILABLE_TIMEOUT</td>
  </tr>
  <tr>
    <td><code>E4232</code></td>
    <td>ACCTYPE IS NOT SUPPORTED (OD)</td>
    <td>ACCTYPE IS NOT SUPPORTED (OD)</td>
    <td>ACCTYPE_IS_NOT_SUPPORTED_OD</td>
  </tr>
  <tr>
    <td><code>E4340</code></td>
    <td>Transaction failed due to account details not found at customer&#x27;s bank</td>
    <td>ACCOUNT DOES NOT EXIST (REMITTER)</td>
    <td>ACCOUNT_DOES_NOT_EXIST_REMITTER</td>
  </tr>
  <tr>
    <td><code>E4341</code></td>
    <td>Transaction failed due to account details not found at acquirer&#x27;s bank</td>
    <td>ACCOUNT DOES NOT EXIST (BENEFICIARY)</td>
    <td>ACCOUNT_DOES_NOT_EXIST_BENEFICIARY</td>
  </tr>
  <tr>
    <td><code>E324</code></td>
    <td>Transaction was declined by the issuing bank due to suspected fraudulent activities</td>
    <td>Suspected Fraud, Retain Card</td>
    <td>CARD_FRAUD_SUSPECTED</td>
  </tr>
  <tr>
    <td><code>E325</code></td>
    <td>Transaction declined due to card not enabled for online transactions or user / Bank Defined Restrictions</td>
    <td>Restricted Card, Retain Card</td>
    <td>RESTRICTED_CARD</td>
  </tr>
  <tr>
    <td><code>E313</code></td>
    <td>Card authentication failed at the bank due to invalid CVV (or CVC or Card Security Code)</td>
    <td>Negative online CAM, dCVV, iCVV, CVV, or CAVV results or Offlin</td>
    <td>CVC_FAILURE</td>
  </tr>
  <tr>
    <td><code>E1652</code></td>
    <td>Card blocked</td>
    <td></td>
    <td>CARD_BLOCKED</td>
  </tr>
  <tr>
    <td><code>E502</code></td>
    <td>Transaction cancelled by customer</td>
    <td></td>
    <td>TRANSACTION_ABORTED</td>
  </tr>
  <tr>
    <td><code>E228</code></td>
    <td>Transaction is Deferred</td>
    <td></td>
    <td>TRANSACTION_DEFERRED</td>
  </tr>
  <tr>
    <td><code>E501</code></td>
    <td>Bank was unable to authenticate.</td>
    <td></td>
    <td>DEFAULT_ERROR</td>
  </tr>
  <tr>
    <td><code>E905</code></td>
    <td>Transaction declined</td>
    <td></td>
    <td>USER_DECLINED</td>
  </tr>
  <tr>
    <td><code>E314</code></td>
    <td>The address needs to match with the records of card issuing bank</td>
    <td></td>
    <td>ADDRESS_FAILURE</td>
  </tr>
  <tr>
    <td><code>E216</code></td>
    <td>Submitting multiple transactions in a single file is an efficient way to upload credit card and electronic check transaction data from enterprise applications or other file-based systems. Error occurred during batch processing of the cards.</td>
    <td></td>
    <td>BATCH_ERROR</td>
  </tr>
  <tr>
    <td><code>E316</code></td>
    <td>Bank failed to authenticate the customer due to 3D Secure Authentication decline</td>
    <td></td>
    <td>SECURE_3D_NOT_ENROLLED</td>
  </tr>
  <tr>
    <td><code>E1636</code></td>
    <td>Transaction time out</td>
    <td></td>
    <td>TRANSACTION_TIMEOUT</td>
  </tr>
  <tr>
    <td><code>E1302</code></td>
    <td>Bank failed to authenticate the customer due to 3D Secure Enrollment decline</td>
    <td></td>
    <td>NOT_ENROLLED_FAILURE</td>
  </tr>
  <tr>
    <td><code>E202</code></td>
    <td>Card authentication failure</td>
    <td></td>
    <td>TRANSACTION_INVALID</td>
  </tr>
  <tr>
    <td><code>EX000</code></td>
    <td></td>
    <td>GRAND_TOTAL</td>
    <td></td>
  </tr>
  <tr>
    <td><code>EX001</code></td>
    <td>No MySQL DSN Supplied</td>
    <td>MYSQL_DSN_ERROR</td>
    <td>No MySQL DSN Supplied</td>
  </tr>
  <tr>
    <td><code>EX002</code></td>
    <td>Default db not mentioned</td>
    <td>MYSQL_DEFAULT_DB_UKNOWN</td>
    <td>Default db not mentioned</td>
  </tr>
  <tr>
    <td><code>EX003</code></td>
    <td>MySQL DSN not configured for ?</td>
    <td>MYSQL_DSN_NOT_CONFIGURED</td>
    <td>MySQL DSN not configured for ?</td>
  </tr>
  <tr>
    <td><code>EX004</code></td>
    <td>MySQL DSN not configured for ?</td>
    <td>MYSQL_DSNKEY_NOT_CONFIGURED</td>
    <td>MySQL DSN not configured for ?</td>
  </tr>
  <tr>
    <td><code>EX005</code></td>
    <td>Data is empty</td>
    <td>MYSQL_DATA_EMPTY</td>
    <td>Data is empty</td>
  </tr>
  <tr>
    <td><code>EX006</code></td>
    <td>where clause is empty</td>
    <td>MYSQL_WHERE_CLAUSE_EMPTY</td>
    <td>where clause is empty</td>
  </tr>
  <tr>
    <td><code>EX007</code></td>
    <td>Table name is empty</td>
    <td>MYSQL_TABLENAME_EMPTY</td>
    <td>Table name is empty</td>
  </tr>
  <tr>
    <td><code>EX008</code></td>
    <td>Insufficient dataTypes given.</td>
    <td>MYSQL_DATATYPE_INSUFFICIENT</td>
    <td>Insufficient dataTypes given.</td>
  </tr>
  <tr>
    <td><code>EX009</code></td>
    <td>DataTypes provided but whereParamTypes not provided</td>
    <td>MYSQL_WHEREPARAMTYPE_EMPTY</td>
    <td>DataTypes provided but whereParamTypes not provided</td>
  </tr>
  <tr>
    <td><code>EX010</code></td>
    <td>Insufficent whereParamTypes provided</td>
    <td>MYSQL_WHEREPARAMTYPE_INSUFFICIENT</td>
    <td>Insufficent whereParamTypes provided</td>
  </tr>
  <tr>
    <td><code>EX011</code></td>
    <td>CSRF happened</td>
    <td>CSRF_OCCURRED</td>
    <td>CSRF happened</td>
  </tr>
  <tr>
    <td><code>EX012</code></td>
    <td>Key is Null</td>
    <td>NULL_KEY</td>
    <td>Key is Null</td>
  </tr>
  <tr>
    <td><code>EX013</code></td>
    <td>Insufficient Input</td>
    <td>INSUFFICIENT_INPUT</td>
    <td>Insufficient Input</td>
  </tr>
  <tr>
    <td><code>EX014</code></td>
    <td>Merchant Param: Key not supplied</td>
    <td>MERCHANT_PARAM_KEY_EMPTY</td>
    <td>Merchant Param: Key not supplied</td>
  </tr>
  <tr>
    <td><code>EX015</code></td>
    <td>Merchant payment type insufficient parameters</td>
    <td>MERCHANT_PAYMENT_TYPE_INSUFFICIENT</td>
    <td>Merchant payment type insufficient parameters</td>
  </tr>
  <tr>
    <td><code>EX016</code></td>
    <td>Merchant gateway insufficient parameters</td>
    <td>MERCHANT_GATEWAY_INSUFFICIENT_PARAMS</td>
    <td>Merchant gateway insufficient parameters</td>
  </tr>
  <tr>
    <td><code>EX017</code></td>
    <td>Payment gateway id not assigned to merchant payment type</td>
    <td>PG_UNASSIGNED_TO_MERCHANT_PAYMENT_TYPE</td>
    <td>Payment gateway id not assigned to merchant payment type</td>
  </tr>
  <tr>
    <td><code>EX018</code></td>
    <td>Invalid Payment Gateway Identifier</td>
    <td>INVALID_PAYMENTGATEWAY_INDENTIFIER</td>
    <td>Invalid Payment Gateway Identifier</td>
  </tr>
  <tr>
    <td><code>EX019</code></td>
    <td>Unable to obtain lock for transaction</td>
    <td>UNABLE_TO_LOCK</td>
    <td>Unable to obtain lock for transaction</td>
  </tr>
  <tr>
    <td><code>EX020</code></td>
    <td>Inconsistent Transaction Status in database</td>
    <td>INCONSISTENCY_IN_TRANSACTION_STATUS</td>
    <td>Inconsistent Transaction Status in database</td>
  </tr>
  <tr>
    <td><code>EX021</code></td>
    <td>The risk_category for this merchant hasn</td>
    <td>RISK_CATEGORY_MISSING</td>
    <td>The risk_category for this merchant hasn</td>
  </tr>
  <tr>
    <td><code>EX022</code></td>
    <td>PayuId not attached to Transaction Class ?</td>
    <td>PAYUID_MISSING</td>
    <td>PayuId not attached to Transaction Class ?</td>
  </tr>
  <tr>
    <td><code>EX023</code></td>
    <td>Verifier hash mismatch</td>
    <td>VERIFIER_MISMATCH</td>
    <td>Verifier hash mismatch</td>
  </tr>
  <tr>
    <td><code>EX024</code></td>
    <td>Empty lockid in transaction::unlock</td>
    <td>LOCKID_EMPTY</td>
    <td>Empty lockid in transaction::unlock</td>
  </tr>
  <tr>
    <td><code>EX025</code></td>
    <td>Merchant not found</td>
    <td>MERCHANT_NOT_FOUND</td>
    <td>Merchant not found</td>
  </tr>
  <tr>
    <td><code>EX026</code></td>
    <td>Transaction could not be reinitiated due to empty base transaction or invalid status</td>
    <td>TRANSACTION_REINITIATION_PROBLEM</td>
    <td>Transaction could not be reinitiated due to empty base transaction or invalid status</td>
  </tr>
  <tr>
    <td><code>EX027</code></td>
    <td>Empty previous transaction id</td>
    <td>TRANSACTIONID_EMPTY</td>
    <td>Empty previous transaction id</td>
  </tr>
  <tr>
    <td><code>EX028</code></td>
    <td>Invalid Attempt</td>
    <td>INVALID_ATTEMPT</td>
    <td>Invalid Attempt</td>
  </tr>
  <tr>
    <td><code>EX029</code></td>
    <td>Invalid User Identifier</td>
    <td>INVALID_USER_IDENTIFIER</td>
    <td>Invalid User Identifier</td>
  </tr>
  <tr>
    <td><code>EX030</code></td>
    <td>Invalid Vendor Identifier</td>
    <td>INVALID_VENDOR_IDENTIFIER</td>
    <td>Invalid Vendor Identifier</td>
  </tr>
  <tr>
    <td><code>EX031</code></td>
    <td>Cancel Error: Invalid File or no data</td>
    <td>CANCEL_ERROR_INVALID_FILE</td>
    <td>Cancel Error: Invalid File or no data</td>
  </tr>
  <tr>
    <td><code>EX032</code></td>
    <td>Cancel Error: Mandatory column missing. Mandatory columns are:  ? </td>
    <td>CANCEL_ERROR_MANDATORY_COLUMN</td>
    <td>Cancel Error: Mandatory column missing. Mandatory columns are:  ? </td>
  </tr>
  <tr>
    <td><code>EX033</code></td>
    <td>Refund Error: Invalid File or no data ?</td>
    <td>REFUND_ERROR_INVALID_FILE</td>
    <td>Refund Error: Invalid File or no data ?</td>
  </tr>
  <tr>
    <td><code>EX034</code></td>
    <td>Refund Error: Mandatory column missing. Mandatory columns are:  ? </td>
    <td>REFUND_ERROR_MANDATORY_COLUMN</td>
    <td>Refund Error: Mandatory column missing. Mandatory columns are:  ? </td>
  </tr>
  <tr>
    <td><code>EX035</code></td>
    <td>Capture Error: Invalid File or no data</td>
    <td>CAPTURE_ERROR_INVALID_FILE</td>
    <td>Capture Error: Invalid File or no data</td>
  </tr>
  <tr>
    <td><code>EX036</code></td>
    <td>Captured Error: Mandatory column missing. Mandatory columns are:  ? </td>
    <td>CAPTURE_ERROR_MANDATORY_COLUMN</td>
    <td>Captured Error: Mandatory column missing. Mandatory columns are:  ? </td>
  </tr>
  <tr>
    <td><code>EX037</code></td>
    <td>Reconciliation Error: Invalid File or no data</td>
    <td>RECONCILIATION_ERROR_INVALID_FILE</td>
    <td>Reconciliation Error: Invalid File or no data</td>
  </tr>
  <tr>
    <td><code>EX038</code></td>
    <td>Reconciliation Error: Mandatory column missing. Mandatory columns are:  ? </td>
    <td>RECONCILIATION_ERROR_MANDATORY_COLUMN</td>
    <td>Reconciliation Error: Mandatory column missing. Mandatory columns are:  ? </td>
  </tr>
  <tr>
    <td><code>EX039</code></td>
    <td>Recon: Transaction not set</td>
    <td>RECON_TRANSACTION_UNSET</td>
    <td>Recon: Transaction not set</td>
  </tr>
  <tr>
    <td><code>EX040</code></td>
    <td>?</td>
    <td>NO_PRIVILEGE</td>
    <td>?</td>
  </tr>
  <tr>
    <td><code>EX041</code></td>
    <td>The requested file does not exist or you do not have priviledge to access it</td>
    <td>FILE_DO_NOT_EXIST_OR_NO_PRIVILEGE</td>
    <td>The requested file does not exist or you do not have priviledge to access it</td>
  </tr>
  <tr>
    <td><code>EX042</code></td>
    <td>Invalid Invoice ID</td>
    <td>INVOICE_INVALID</td>
    <td>Invalid Invoice ID</td>
  </tr>
  <tr>
    <td><code>EX043</code></td>
    <td>Problem reading data from ? : ?</td>
    <td>PROBLEM_READING_DATA_SENTROPI_URL</td>
    <td>Problem reading data from ? : ?</td>
  </tr>
  <tr>
    <td><code>EX044</code></td>
    <td>pExcelReader: Invalid type ?</td>
    <td>PEXCELREADER_INVALID_TYPE</td>
    <td>pExcelReader: Invalid type ?</td>
  </tr>
  <tr>
    <td><code>EX045</code></td>
    <td>pExcelReader: File ? not readable</td>
    <td>PEXCELREADER_FILE_NOT_READABLE</td>
    <td>pExcelReader: File ? not readable</td>
  </tr>
  <tr>
    <td><code>EX046</code></td>
    <td>XLSXReader : File not readable Filepath : ( ? ) Error : ( ? )</td>
    <td>XLSXREADER_FILE_NOT_READABLE</td>
    <td>XLSXReader : File not readable Filepath : ( ? ) Error : ( ? )</td>
  </tr>
  <tr>
    <td><code>EX047</code></td>
    <td>ODSReader :  File not readable Filepath : ( ? ) Error : ( ? )</td>
    <td>ODSREADER_FILE_NOT_READABLE</td>
    <td>ODSReader :  File not readable Filepath : ( ? ) Error : ( ? )</td>
  </tr>
  <tr>
    <td><code>EX048</code></td>
    <td>CSVReader :  File not readable Filepath : ( ? ) Error : ( ? )</td>
    <td>CSVREADER_FILE_NOT_READABLE</td>
    <td>CSVReader :  File not readable Filepath : ( ? ) Error : ( ? )</td>
  </tr>
  <tr>
    <td><code>EX049</code></td>
    <td>All edit keys must have an associated value</td>
    <td>EDIT_KEY_UNASSOCIATED_VALUE</td>
    <td>All edit keys must have an associated value</td>
  </tr>
  <tr>
    <td><code>EX050</code></td>
    <td>No data found for this form. Edit form is unavailable</td>
    <td>EDIT_FORM_UNAVAILABLE</td>
    <td>No data found for this form. Edit form is unavailable</td>
  </tr>
  <tr>
    <td><code>EX051</code></td>
    <td>All edit keys must be part of edit fields</td>
    <td>EDIT_KEY_PART_OF_EDIT_FIELDS</td>
    <td>All edit keys must be part of edit fields</td>
  </tr>
  <tr>
    <td><code>EX052</code></td>
    <td>TransactionID not found in Pg Response</td>
    <td>TRANSACTIONID_NOT_FOUND_PG_RESPONSE</td>
    <td>TransactionID not found in Pg Response</td>
  </tr>
  <tr>
    <td><code>EX053</code></td>
    <td>Invalid Transaction ID in gateway response</td>
    <td>TRANSACTIONID_INVALID_GATEWAY_RESPONSE</td>
    <td>Invalid Transaction ID in gateway response</td>
  </tr>
  <tr>
    <td><code>EX054</code></td>
    <td>Base merchant id not posted from the paisa request for payuId ?</td>
    <td>BASE_MERCHANT_ID_MISSING</td>
    <td>Base merchant id not posted from the paisa request for payuId ?</td>
  </tr>
  <tr>
    <td><code>EX055</code></td>
    <td>Base payu id not posted from the paisa request for payuId ?</td>
    <td>BASE_PAYU_ID_MISSING</td>
    <td>Base payu id not posted from the paisa request for payuId ?</td>
  </tr>
  <tr>
    <td><code>EX056</code></td>
    <td>Invalid Paisa Merchant Id</td>
    <td>INVALID_PAISA_MERCHANT</td>
    <td>Invalid Paisa Merchant Id</td>
  </tr>
  <tr>
    <td><code>EX057</code></td>
    <td>Not Implemented</td>
    <td>NOT_IMPLEMENTED</td>
    <td>Not Implemented</td>
  </tr>
  <tr>
    <td><code>EX058</code></td>
    <td>Object can not be saved to database. Identifiers not set</td>
    <td>OBJECT_UNSAVED_IDENTIFIER_UNSET</td>
    <td>Object can not be saved to database. Identifiers not set</td>
  </tr>
  <tr>
    <td><code>EX059</code></td>
    <td>Object can not be saved to database. Table name not mentioned</td>
    <td>OBJECT_UNSAVED_TABLENAME_MISSING</td>
    <td>Object can not be saved to database. Table name not mentioned</td>
  </tr>
  <tr>
    <td><code>EX060</code></td>
    <td>Object can not be saved to database. Identifier value missing</td>
    <td>OBJECT_UNSAVED_IDENTIFIER_MISSING</td>
    <td>Object can not be saved to database. Identifier value missing</td>
  </tr>
  <tr>
    <td><code>EX061</code></td>
    <td>Protocol Mismatch</td>
    <td>PROTOCOL_MISSMATCH</td>
    <td>Protocol Mismatch</td>
  </tr>
  <tr>
    <td><code>EX062</code></td>
    <td>Add Payment Call to payu_paisa_addpayment_url failed</td>
    <td>PAYU_PAISA_ADDPAYMENT_URL_FAILED</td>
    <td>Add Payment Call to payu_paisa_addpayment_url failed</td>
  </tr>
  <tr>
    <td><code>EX063</code></td>
    <td>Invalid Transaction State: Transaction in IN PROGRESS state in cancel.php</td>
    <td>INVALID_TRANSACTION_STATE</td>
    <td>Invalid Transaction State: Transaction in IN PROGRESS state in cancel.php</td>
  </tr>
  <tr>
    <td><code>EX064</code></td>
    <td>Missing forward action</td>
    <td>MISSING_FORWARD_ACTION</td>
    <td>Missing forward action</td>
  </tr>
  <tr>
    <td><code>EX065</code></td>
    <td>Invalid forward - App ? not available</td>
    <td>APPS_APPNAME_UNAVAILABLE</td>
    <td>Invalid forward - App ? not available</td>
  </tr>
  <tr>
    <td><code>EX066</code></td>
    <td>Action must extend PayuAction</td>
    <td>ACTION_MUST_EXTEND_PAYUACTION</td>
    <td>Action must extend PayuAction</td>
  </tr>
  <tr>
    <td><code>EX067</code></td>
    <td>Unable to reload action: ?</td>
    <td>UNABLE_TO_RELOAD_ACTION</td>
    <td>Unable to reload action: ?</td>
  </tr>
  <tr>
    <td><code>EX068</code></td>
    <td>No fields specified in adminViewer</td>
    <td>MISSING_ADMINVIEWER_FIELDS</td>
    <td>No fields specified in adminViewer</td>
  </tr>
  <tr>
    <td><code>EX069</code></td>
    <td>The request parameter must be set</td>
    <td>REQUEST_PARAM_UNSET</td>
    <td>The request parameter must be set</td>
  </tr>
  <tr>
    <td><code>EX070</code></td>
    <td>The ? request parameter must be set</td>
    <td>HTTPREQUEST_PARAM_UNSET</td>
    <td>The ? request parameter must be set</td>
  </tr>
  <tr>
    <td><code>EX071</code></td>
    <td>Problem Building WURFL Repository: ?</td>
    <td>WURFL_REPOSITORY_PROBLEM</td>
    <td>Problem Building WURFL Repository: ?</td>
  </tr>
  <tr>
    <td><code>EX072</code></td>
    <td>There is no device with ID [?] in the loaded WURFL Data</td>
    <td>DEVICE_MISSING_IN_WURFL_DATA</td>
    <td>There is no device with ID [?] in the loaded WURFL Data</td>
  </tr>
  <tr>
    <td><code>EX073</code></td>
    <td>WriteRow failed: Unknown Result</td>
    <td>WRITE_ROW_FAILED</td>
    <td>WriteRow failed: Unknown Result</td>
  </tr>
  <tr>
    <td><code>EX074</code></td>
    <td>WriteFormattedRow failed: unknown result</td>
    <td>WRITE_FORMATTED_ROW_FAILED</td>
    <td>WriteFormattedRow failed: unknown result</td>
  </tr>
  <tr>
    <td><code>EX075</code></td>
    <td>OpenExcel failed: unknown result</td>
    <td>OPENEXCEL_FAILED</td>
    <td>OpenExcel failed: unknown result</td>
  </tr>
  <tr>
    <td><code>EX076</code></td>
    <td>SaveFile failed: unknown result</td>
    <td>SAVEFILE_FAILED</td>
    <td>SaveFile failed: unknown result</td>
  </tr>
  <tr>
    <td><code>EX077</code></td>
    <td>Write N Rows failed: unknown result</td>
    <td>WRITE_N_ROW_FAILED</td>
    <td>Write N Rows failed: unknown result</td>
  </tr>
  <tr>
    <td><code>EX078</code></td>
    <td>WriteFormattedNRows failed: unknown result</td>
    <td>WRITE_N_FORMATTED_ROW_FAILED</td>
    <td>WriteFormattedNRows failed: unknown result</td>
  </tr>
  <tr>
    <td><code>EX079</code></td>
    <td>Message : ?. Error Code : ?</td>
    <td>DB_EXCEPTION_ERROR_OTHERS</td>
    <td>Message : ?. Error Code : ?</td>
  </tr>
  <tr>
    <td><code>EX080</code></td>
    <td>Could not open remote file: ?</td>
    <td>REMOTE_FILE_OPEN_FAILED</td>
    <td>Could not open remote file: ?</td>
  </tr>
  <tr>
    <td><code>EX081</code></td>
    <td>Could not open local file: ?</td>
    <td>LOCAL_FILE_OPEN_FAILED</td>
    <td>Could not open local file: ?</td>
  </tr>
  <tr>
    <td><code>EX082</code></td>
    <td>Could not send data from file: ?</td>
    <td>DATA_SENDIG_FAILED</td>
    <td>Could not send data from file: ?</td>
  </tr>
  <tr>
    <td><code>EX083</code></td>
    <td>Parameter Passed : ?</td>
    <td>BLANK</td>
    <td>Parameter Passed : ?</td>
  </tr>
  <tr>
    <td><code>EX084</code></td>
    <td>Return URI not received</td>
    <td>URI_NOT_RECEIVED</td>
    <td>Return URI not received</td>
  </tr>
  <tr>
    <td><code>EX085</code></td>
    <td>Verifier payu Id not received</td>
    <td>VERIFIER_PAYUID_NOT_RECEIVED</td>
    <td>Verifier payu Id not received</td>
  </tr>
  <tr>
    <td><code>EX086</code></td>
    <td>Card bin is not present</td>
    <td>CARD_BIN_NOT_PRESENT</td>
    <td>Card bin is not present</td>
  </tr>
  <tr>
    <td><code>EX087</code></td>
    <td>Transaction failed due to incorrectly calculated hash parameter. ?</td>
    <td>CHECKSUM_FAILED</td>
    <td>Transaction failed due to incorrectly calculated hash parameter. ?</td>
  </tr>
  <tr>
    <td><code>EX088</code></td>
    <td>Merchant registration limit exceeded in 1 hour</td>
    <td>MERCHANT_REGISTRATION_LIMIT_EXCEEDED</td>
    <td>Merchant registration limit exceeded in 1 hour</td>
  </tr>
  <tr>
    <td><code>EX089</code></td>
    <td>Token mismatch</td>
    <td>TOKEN_MISMATCH</td>
    <td>Token mismatch</td>
  </tr>
  <tr>
    <td><code>EX090</code></td>
    <td>Payu id or token missing</td>
    <td>PAYUID_MISSING_TOKEN_MISS</td>
    <td>Payu id or token missing</td>
  </tr>
  <tr>
    <td><code>EX091</code></td>
    <td>Invalid Request ?</td>
    <td>INVALID_PAGE_REQUESTED</td>
    <td>Invalid Request ?</td>
  </tr>
  <tr>
    <td><code>EX092</code></td>
    <td>Upload Error: Invalid File or no data</td>
    <td>UPLOAD_ERROR</td>
    <td>Upload Error: Invalid File or no data</td>
  </tr>
  <tr>
    <td><code>EX093</code></td>
    <td>Reporting Error: Invalid File or no data</td>
    <td>REPORTING_ERROR_INVALID_FILE</td>
    <td>Reporting Error: Invalid File or no data</td>
  </tr>
  <tr>
    <td><code>EX094</code></td>
    <td>Vendor details not saved</td>
    <td>VENDOR_DETAILS_NOT_SAVED</td>
    <td>Vendor details not saved</td>
  </tr>
  <tr>
    <td><code>EX095</code></td>
    <td>The value must be an integer (not 0) signifying the number of days ? ?</td>
    <td>NON_INTEGER_ERROR</td>
    <td>The value must be an integer (not 0) signifying the number of days ? ?</td>
  </tr>
  <tr>
    <td><code>EX096</code></td>
    <td>Reconciliation Error: Undefined actions requested. Defined actions are :  ?  Change  ?  action(s) to appropriate actions.</td>
    <td>RECONCILIATION_ERROR_UNDEFINED_ACTION</td>
    <td>Reconciliation Error: Undefined actions requested. Defined actions are :  ?  Change  ?  action(s) to appropriate actions.</td>
  </tr>
  <tr>
    <td><code>EX097</code></td>
    <td>Invalid Merchant Identifier</td>
    <td>INVALID_MERCHANT_IDENTIFIER</td>
    <td>Invalid Merchant Identifier</td>
  </tr>
  <tr>
    <td><code>EX098</code></td>
    <td>Insufficient parameters for pt key addition</td>
    <td>INSUFFICIENT_PARAM_PT_KEY_ADDITION</td>
    <td>Insufficient parameters for pt key addition</td>
  </tr>
  <tr>
    <td><code>EX099</code></td>
    <td>Insufficient parameters for pt key deletion</td>
    <td>INSUFFICIENT_PARAM_PT_KEY_DELETION</td>
    <td>Insufficient parameters for pt key deletion</td>
  </tr>
  <tr>
    <td><code>EX100</code></td>
    <td>Insufficient parameters for pt key update</td>
    <td>INSUFFICIENT_PARAM_PT_KEY_UPDATE</td>
    <td>Insufficient parameters for pt key update</td>
  </tr>
  <tr>
    <td><code>EX101</code></td>
    <td>Remove pg key - Invalid merchant id</td>
    <td>INVALID_MERCHANT_ID</td>
    <td>Remove pg key - Invalid merchant id</td>
  </tr>
  <tr>
    <td><code>EX102</code></td>
    <td>Insufficient Input for pg keys</td>
    <td>INSUFFICIENT_INPUT_FOR_PG_KEYS</td>
    <td>Insufficient Input for pg keys</td>
  </tr>
  <tr>
    <td><code>EX103</code></td>
    <td>Mapped status and unmapped status of payu id ? didnt match</td>
    <td>MAPPED_UNMAPPED_STATUS</td>
    <td>Mapped status and unmapped status of payu id ? didnt match</td>
  </tr>
  <tr>
    <td><code>EX104</code></td>
    <td>Reporting Error: Mandatory column missing. Mandatory columns are:  ? </td>
    <td>REPORTING_ERROR_MANDATORY_COL_MISSING</td>
    <td>Reporting Error: Mandatory column missing. Mandatory columns are:  ? </td>
  </tr>
  <tr>
    <td><code>EX105</code></td>
    <td>Upload Error: Mandatory column missing. Mandatory columns are:  ? </td>
    <td>UPLOAD_ERROR_MANDATORY_COL_MISSING</td>
    <td>Upload Error: Mandatory column missing. Mandatory columns are:  ? </td>
  </tr>
  <tr>
    <td><code>EX106</code></td>
    <td>Refund Reference Number Upload Error: Invalid File or no data</td>
    <td>REFUND_UPLOAD_ERROR_INVLALID_FILE</td>
    <td>Refund Reference Number Upload Error: Invalid File or no data</td>
  </tr>
  <tr>
    <td><code>EX107</code></td>
    <td>Refund Reference Number Upload Error: Mandatory column missing. Mandatory columns are:  ? </td>
    <td>REFUND_UPLOAD_ERROR_MANDATORY_COL_MISS</td>
    <td>Refund Reference Number Upload Error: Mandatory column missing. Mandatory columns are:  ? </td>
  </tr>
  <tr>
    <td><code>EX108</code></td>
    <td>This txnid has been used previously or was successfully captured. ?</td>
    <td>DUPLICATE_ORDER_ID</td>
    <td>This txnid has been used previously or was successfully captured. ?</td>
  </tr>
  <tr>
    <td><code>EX109</code></td>
    <td>Wallet Mode Override for ?</td>
    <td>WALLET_MODE_OVERRIDE</td>
    <td>Wallet Mode Override for ?</td>
  </tr>
  <tr>
    <td><code>EX110</code></td>
    <td>Error! File upload for ? ? failed</td>
    <td>FILE_UPLOAD_FAILURE</td>
    <td>Error! File upload for ? ? failed</td>
  </tr>
  <tr>
    <td><code>EX111</code></td>
    <td>Incorrect additional charge posted in paisa response for p1 ?</td>
    <td>INCORRECT_ADDITIONAL_CHARGE</td>
    <td>Incorrect additional charge posted in paisa response for p1 ?</td>
  </tr>
  <tr>
    <td><code>EX112</code></td>
    <td>Invalid request for payuid: ? : addedon: ? : updatedon: ? ?</td>
    <td>INVALID_REQUEST_FOR_PAYUID</td>
    <td>Invalid request for payuid: ? : addedon: ? : updatedon: ? ?</td>
  </tr>
  <tr>
    <td><code>EX113</code></td>
    <td>Invalid Transaction</td>
    <td>ACCESS_TOKEN_MISMATCH</td>
    <td>Invalid Transaction</td>
  </tr>
  <tr>
    <td><code>EX114</code></td>
    <td>Merchant key missing in Request</td>
    <td>MERCHANT_KEY_MISSING</td>
    <td>Merchant key missing in Request</td>
  </tr>
  <tr>
    <td><code>EX115</code></td>
    <td>The key ? value which you are using in the transaction request - is currently inactive. ?</td>
    <td>PAYMENTFLOW_INACTIVE_MERCHANT</td>
    <td>The key ? value which you are using in the transaction request - is currently inactive. ?</td>
  </tr>
  <tr>
    <td><code>EX116</code></td>
    <td>Expired transaction.</td>
    <td>PAYMENTFLOW_EXPIRED_TRANSACTION</td>
    <td>Expired transaction.</td>
  </tr>
  <tr>
    <td><code>EX117</code></td>
    <td>Invalid amount</td>
    <td>INVALID_AMOUNT</td>
    <td>Invalid amount</td>
  </tr>
  <tr>
    <td><code>EX118</code></td>
    <td>Invalid Transaction.</td>
    <td>PAYMENTFLOW_INVALID_TRANSACTION</td>
    <td>Invalid Transaction.</td>
  </tr>
  <tr>
    <td><code>EX119</code></td>
    <td>Card details invalid.</td>
    <td>CARD_DETAILS_INVALID</td>
    <td>Card details invalid.</td>
  </tr>
  <tr>
    <td><code>EX120</code></td>
    <td>Invalid additional amount</td>
    <td>INVALID_ADDITIONAL_AMOUNT</td>
    <td>Invalid additional amount</td>
  </tr>
  <tr>
    <td><code>EX121</code></td>
    <td>No edit keys specified. Edit form is unavailable.</td>
    <td>NO_EDIT_KEY_EDIT_FORM_UNAVAILABLE</td>
    <td>No edit keys specified. Edit form is unavailable.</td>
  </tr>
  <tr>
    <td><code>EX122</code></td>
    <td>Error: Invalid File or no data</td>
    <td>ERROR_INVALID_FILE</td>
    <td>Error: Invalid File or no data</td>
  </tr>
  <tr>
    <td><code>EX123</code></td>
    <td>Mandatory parameter payuId missing.</td>
    <td>MANDATORY_PARAMETER_PAYUID_MISSING</td>
    <td>Mandatory parameter payuId missing.</td>
  </tr>
  <tr>
    <td><code>EX124</code></td>
    <td>One or more mandatory parameters are missing in the transaction request. ?</td>
    <td>MANDATORY_PARAMETER_TXNID_MISSING</td>
    <td>One or more mandatory parameters are missing in the transaction request. ?</td>
  </tr>
  <tr>
    <td><code>EX125</code></td>
    <td>Transaction Expired, payuid: ?  base txn Id: ? uniqueness: ? , ?</td>
    <td>PAYMENT_FLOW_EXCEP_TRANSACTION_EXPIRED</td>
    <td>Transaction Expired, payuid: ?  base txn Id: ? uniqueness: ? , ?</td>
  </tr>
  <tr>
    <td><code>EX126</code></td>
    <td>Invalid Data</td>
    <td>PAYMENTFLOW_INVALID_DATA</td>
    <td>Invalid Data</td>
  </tr>
  <tr>
    <td><code>EX127</code></td>
    <td>Invalid check card is credit</td>
    <td>INVALID_CHECK_CARD_IS_CREDIT</td>
    <td>Invalid check card is credit</td>
  </tr>
  <tr>
    <td><code>EX128</code></td>
    <td>This Invoice has expired</td>
    <td>INVOICE_EXPIRED</td>
    <td>This Invoice has expired</td>
  </tr>
  <tr>
    <td><code>EX129</code></td>
    <td>Invalid set user request</td>
    <td>INVALID_SET_USER_REQUEST</td>
    <td>Invalid set user request</td>
  </tr>
  <tr>
    <td><code>EX130</code></td>
    <td>Error: Mandatory column missing. Mandatory columns are:  ? </td>
    <td>ERROR_MANDATORY_FILE_MISSING</td>
    <td>Error: Mandatory column missing. Mandatory columns are:  ? </td>
  </tr>
  <tr>
    <td><code>EX131</code></td>
    <td>Switcher Failure - No active gateway set for merchant transaction id: ?.</td>
    <td>NO_ACTIVE_PG_FOUND</td>
    <td>Switcher Failure - No active gateway set for merchant transaction id: ?.</td>
  </tr>
  <tr>
    <td><code>EX132</code></td>
    <td>SS-ratio based Switcher failure - No eligible gateway returned for transaction id: ?.</td>
    <td>SS_RATIO_BASED_SWITCHER_FAILURE</td>
    <td>SS-ratio based Switcher failure - No eligible gateway returned for transaction id: ?.</td>
  </tr>
  <tr>
    <td><code>EX133</code></td>
    <td>Invalid discount amount</td>
    <td>INVALID_DISCOUNT</td>
    <td>Invalid discount amount</td>
  </tr>
  <tr>
    <td><code>EX134</code></td>
    <td>Recon: All Ibibo Code not set</td>
    <td>RECON_ALL_IBIBO_CODE_UNSET</td>
    <td>Recon: All Ibibo Code not set</td>
  </tr>
  <tr>
    <td><code>EX135</code></td>
    <td>Number of elements in a row should be equal to column count</td>
    <td>MYSQL_ROW_COLUMN_COUNT_MISMATCH</td>
    <td>Number of elements in a row should be equal to column count</td>
  </tr>
  <tr>
    <td><code>EX136</code></td>
    <td>Message sending failed. Message Content : ?; Mobile Number : ?; App : ? .  \n Response received : ?</td>
    <td>MESSAGE_SENDING_FAILED</td>
    <td>Message sending failed. Message Content : ?; Mobile Number : ?; App : ? .  \n Response received : ?</td>
  </tr>
  <tr>
    <td><code>EX137</code></td>
    <td>Recon: Card bin map not set</td>
    <td>RECON_CARDBIN_PGS_UNSET</td>
    <td>Recon: Card bin map not set</td>
  </tr>
  <tr>
    <td><code>EX138</code></td>
    <td>Fatal Error Handler Counter</td>
    <td>FATAL_ERROR_HANDLER</td>
    <td>Fatal Error Handler Counter</td>
  </tr>
  <tr>
    <td><code>EX139</code></td>
    <td>Recon: Email Template not set</td>
    <td>RECON_EMAIL_TEMPLATE_UNSET</td>
    <td>Recon: Email Template not set</td>
  </tr>
  <tr>
    <td><code>EX140</code></td>
    <td>Profiling error. ProfilerName: ?, AppName: ?, Event: ?, Message: ?</td>
    <td>PROFILING_ERROR</td>
    <td>Profiling error. ProfilerName: ?, AppName: ?, Event: ?, Message: ?</td>
  </tr>
  <tr>
    <td><code>EX141</code></td>
    <td>Mandrill ERROR : ?</td>
    <td>MANDRILL_ERROR</td>
    <td>Mandrill ERROR : ?</td>
  </tr>
  <tr>
    <td><code>EX142</code></td>
    <td>Message : ?. Error Code : ?</td>
    <td>DB_EXCEPTION_ERROR_MASTER</td>
    <td>Message : ?. Error Code : ?</td>
  </tr>
  <tr>
    <td><code>EX143</code></td>
    <td>Message : ?. Error Code : ?</td>
    <td>DB_EXCEPTION_ERROR_SLAVE</td>
    <td>Message : ?. Error Code : ?</td>
  </tr>
  <tr>
    <td><code>EX144</code></td>
    <td>Message : ?. Error Code : ?</td>
    <td>DB_EXCEPTION_ERROR_CONCURRENCY</td>
    <td>Message : ?. Error Code : ?</td>
  </tr>
  <tr>
    <td><code>EX145</code></td>
    <td>Redirection loop for key : ?</td>
    <td>EXCEPTION_REDIRECTION</td>
    <td>Redirection loop for key : ?</td>
  </tr>
  <tr>
    <td><code>EX146</code></td>
    <td>? table details are missing in lib/utility/RiskConstants.php</td>
    <td>INVALID_TABLENAME</td>
    <td>? table details are missing in lib/utility/RiskConstants.php</td>
  </tr>
  <tr>
    <td><code>EX147</code></td>
    <td>You seem to be using an incorrect key or salt value. ?</td>
    <td>INCORRECT_MERCHANT_KEY</td>
    <td>You seem to be using an incorrect key or salt value. ?</td>
  </tr>
  <tr>
    <td><code>EX148</code></td>
    <td>Invalid Request: ? Unable to parse URL.</td>
    <td>INVALID_URL</td>
    <td>Invalid Request: ? Unable to parse URL.</td>
  </tr>
  <tr>
    <td><code>EX149</code></td>
    <td>Maximum retry attempts for this txnid has been exceeded.</td>
    <td>RETRY_EXHAUSTED</td>
    <td>Maximum retry attempts for this txnid has been exceeded.</td>
  </tr>
  <tr>
    <td><code>EX150</code></td>
    <td>Invalid subvention amount</td>
    <td>INVALID_SUBVENTION_AMOUNT</td>
    <td>Invalid subvention amount</td>
  </tr>
  <tr>
    <td><code>EX151</code></td>
    <td></td>
    <td>SFTP_CONNECTION_FAILED</td>
    <td></td>
  </tr>
  <tr>
    <td><code>EX151</code></td>
    <td>Invalid subvention</td>
    <td>INVALID_SUBVENTION</td>
    <td>Invalid subvention</td>
  </tr>
  <tr>
    <td><code>EX152</code></td>
    <td>No form post variables found [S2S Flow]</td>
    <td>NO_FORM_POST_VARS_S2SFLOW</td>
    <td>No form post variables found [S2S Flow]</td>
  </tr>
  <tr>
    <td><code>EX153</code></td>
    <td>Category or ibibo code not recieved</td>
    <td>CATEGORY_IBIBO_NOT_RCVD_S2SFLOW</td>
    <td>Category or ibibo code not recieved</td>
  </tr>
  <tr>
    <td><code>EX154</code></td>
    <td>Payment Method Enforced and wrong method selected</td>
    <td>WRONG_PAYMENT_METHOD_SELECTED</td>
    <td>Payment Method Enforced and wrong method selected</td>
  </tr>
  <tr>
    <td><code>EX155</code></td>
    <td>NB option is down</td>
    <td>NB_OPTIION_DOWN</td>
    <td>NB option is down</td>
  </tr>
  <tr>
    <td><code>EX156</code></td>
    <td>Issuing Bank is down</td>
    <td>ISSUING_BANK_DOWN</td>
    <td>Issuing Bank is down</td>
  </tr>
  <tr>
    <td><code>EX157</code></td>
    <td></td>
    <td>INVALID_CHECK_ALLOWED_BANKS_DC_IN_SI</td>
    <td></td>
  </tr>
  <tr>
    <td><code>EX158</code></td>
    <td>Merchant Integration Exception occurred</td>
    <td>MERCHANT_INTEGRATION_EXCEPTION_CODE</td>
    <td>Merchant Integration Exception occurred</td>
  </tr>
  <tr>
    <td><code>EX159</code></td>
    <td></td>
    <td>UNABLE_TO_DECRYPT_TRANSACTION</td>
    <td></td>
  </tr>
  <tr>
    <td><code>EX160</code></td>
    <td>Zipped file generation exception occurred</td>
    <td>PASSWORD_PROTECT_FILE_GENERATION_FAILED</td>
    <td>Zipped file generation exception occurred</td>
  </tr>
  <tr>
    <td><code>EX200</code></td>
    <td>Something went wrong</td>
    <td>V2_API_CURL_EXCEPTION</td>
    <td>Something went wrong</td>
  </tr>
  <tr>
    <td><code>EX201</code></td>
    <td>Merchant key used for HMAC auth is different from merchant key in data</td>
    <td>V2_API_MERCHANT_KEY_MISMATCH</td>
    <td>Merchant key used for HMAC auth is different from merchant key in data</td>
  </tr>
  <tr>
    <td><code>EX210</code></td>
    <td>This link has expired</td>
    <td>INTENT_LINK_EXPIRED</td>
    <td>This link has expired</td>
  </tr>
  <tr>
    <td><code>EX211</code></td>
    <td>Link already used</td>
    <td>INTENT_LINK_USED</td>
    <td>Link already used</td>
  </tr>
  <tr>
    <td><code>EX212</code></td>
    <td></td>
    <td>INVOICE_GMV_LIMIT_REACHED</td>
    <td></td>
  </tr>
  <tr>
    <td><code>EX213</code></td>
    <td>Duplicate Callback. Please try after sometime</td>
    <td>DUPLICATE_CALLBACK</td>
    <td>Duplicate Callback. Please try after sometime</td>
  </tr>
  <tr>
    <td><code>EX214</code></td>
    <td>Retry limit exhausted. Please ask your merchant to send you a new link.</td>
    <td>INTENT_LINK_USE_EXHAUSTED</td>
    <td>Retry limit exhausted. Please ask your merchant to send you a new link.</td>
  </tr>
  <tr>
    <td><code>EX215</code></td>
    <td>Invalid response from curl</td>
    <td>INVALID_CURL_RESPONSE</td>
    <td>Invalid response from curl</td>
  </tr>
  <tr>
    <td><code>EX216</code></td>
    <td></td>
    <td>REQUEST_LIMIT_REACHED</td>
    <td></td>
  </tr>
  <tr>
    <td><code>EX217</code></td>
    <td>Invalid First Name</td>
    <td>INVALID_FIRST_NAME_EXCEPTION</td>
    <td>Invalid First Name</td>
  </tr>
  <tr>
    <td><code>EX218</code></td>
    <td>Invalid Last Name</td>
    <td>INVALID_LAST_NAME_EXCEPTION</td>
    <td>Invalid Last Name</td>
  </tr>
  <tr>
    <td><code>EX219</code></td>
    <td>Invalid Email</td>
    <td>INVALID_EMAIL_EXCEPTION</td>
    <td>Invalid Email</td>
  </tr>
  <tr>
    <td><code>EX220</code></td>
    <td>Invalid phone number</td>
    <td>INVALID_PHONE_EXCEPTION</td>
    <td>Invalid phone number</td>
  </tr>
  <tr>
    <td><code>EX221</code></td>
    <td>Invalid ZipCode</td>
    <td>INVALID_ZIPCODE_EXCEPTION</td>
    <td>Invalid ZipCode</td>
  </tr>
  <tr>
    <td><code>EX222</code></td>
    <td>Invalid Product Info</td>
    <td>INVALID_PRODUCT_INFO_EXCEPTION</td>
    <td>Invalid Product Info</td>
  </tr>
  <tr>
    <td><code>EX223</code></td>
    <td>Incomplete Onboarding</td>
    <td>INCOMPLETE_ONBOARDING</td>
    <td>Incomplete Onboarding</td>
  </tr>
  <tr>
    <td><code>EX224</code></td>
    <td>Transactions initiation not allowed on aggregator-child merchant.</td>
    <td>AGGREGATOR_CHILD_MERCHANT_KEY</td>
    <td>Transactions initiation not allowed on aggregator-child merchant.</td>
  </tr>
  <tr>
    <td><code>EX225</code></td>
    <td></td>
    <td>INVALID_EXPIRY_TIME</td>
    <td></td>
  </tr>
  <tr>
    <td><code>EX226</code></td>
    <td></td>
    <td>PIH_ERROR</td>
    <td></td>
  </tr>
  <tr>
    <td><code>EX227</code></td>
    <td>This currency is not supported on your account. Please reach out to your KAM for activation</td>
    <td>INACTIVE_CURRENCY_FOR_SINGLE_MID</td>
    <td>This currency is not supported on your account. Please reach out to your KAM for activation</td>
  </tr>
  <tr>
    <td><code>EX300</code></td>
    <td></td>
    <td>MISMATCH_CART_AMOUNT_AND_TRANSACTION_AMOUNT</td>
    <td></td>
  </tr>
  <tr>
    <td><code>EX301</code></td>
    <td></td>
    <td>INCOMPLETE_SKU_DETAILS</td>
    <td></td>
  </tr>
  <tr>
    <td><code>EX302</code></td>
    <td></td>
    <td>MISMATCH_CART_ITEMS_AND_SKU_QUANTITY_SUM</td>
    <td></td>
  </tr>
  <tr>
    <td><code>EX303</code></td>
    <td></td>
    <td>MISMATCH_CART_AMOUNT_AND_PER_SKU_SUM</td>
    <td></td>
  </tr>
  <tr>
    <td><code>EX304</code></td>
    <td></td>
    <td>MULTIPLE_SAME_SKU_ID_IN_SINGLE_CART</td>
    <td></td>
  </tr>
  <tr>
    <td><code>EX305</code></td>
    <td>Invalid additional percentage</td>
    <td>INVALID_ADDITIONAL_PERCENTAGE</td>
    <td>Invalid additional percentage</td>
  </tr>
  <tr>
    <td><code>EX306</code></td>
    <td>Transaction amount convenience fee GST is incorrect, Please try again.</td>
    <td>INVALID_ADDITIONAL_GST</td>
    <td>Transaction amount convenience fee GST is incorrect, Please try again.</td>
  </tr>
  <tr>
    <td><code>EX306</code></td>
    <td>Invalid Webhook Url</td>
    <td>INVALID_WEBHOOK_URL</td>
    <td>Invalid Webhook Url</td>
  </tr>
  <tr>
    <td><code>EX306</code></td>
    <td>Wrong Api version selected for split txn</td>
    <td>API_VERSION_INCORRECT_SPLIT_TXN</td>
    <td>Wrong Api version selected for split txn</td>
  </tr>
  <tr>
    <td><code>EX307</code></td>
    <td>Sent convenience fee over transaction amount is high. Please check &amp; try again</td>
    <td>HIGH_CONV_FEE</td>
    <td>Sent convenience fee over transaction amount is high. Please check &amp; try again</td>
  </tr>
  <tr>
    <td><code>EX307</code></td>
    <td>One or more mandatory parameters are missing in the transaction request for split txn</td>
    <td>MANDATORY_PARAMS_MISSING_SPLIT_TXN</td>
    <td>One or more mandatory parameters are missing in the transaction request for split txn</td>
  </tr>
  <tr>
    <td><code>EX401</code></td>
    <td></td>
    <td>REDIS_DSN_ERROR</td>
    <td></td>
  </tr>
  <tr>
    <td><code>EX401</code></td>
    <td></td>
    <td>REDIS_DSNKEY_NOT_CONFIGURED</td>
    <td></td>
  </tr>
  <tr>
    <td><code>EX402</code></td>
    <td>Invalid Partner Param</td>
    <td>INVALID_PARTNER_PARAM</td>
    <td>Invalid Partner Param</td>
  </tr>
  <tr>
    <td><code>EX403</code></td>
    <td>Invalid UDF Param</td>
    <td>INVALID_UDF_PARAM</td>
    <td>Invalid UDF Param</td>
  </tr>
  <tr>
    <td><code>EX404</code></td>
    <td>Invalid Buyer Type Business</td>
    <td>INVALID_BUYER_TYPE_BUSINESS</td>
    <td>Invalid Buyer Type Business</td>
  </tr>
  <tr>
    <td><code>EX405</code></td>
    <td>Invalid More Info Param</td>
    <td>INVALID_MORE_INFO_PARAM</td>
    <td>Invalid More Info Param</td>
  </tr>
  <tr>
    <td><code>EX406</code></td>
    <td>Invalid PAN or DOB Details</td>
    <td>INVALID_PAN_DOB_DETAILS</td>
    <td>Invalid PAN or DOB Details</td>
  </tr>
  <tr>
    <td><code>EX407</code></td>
    <td>Invalid TCS Amount</td>
    <td>INVALID_TCS_AMOUNT</td>
    <td>Invalid TCS Amount</td>
  </tr>
  <tr>
    <td><code>EX408</code></td>
    <td>Insufficient TCS amount passed based on lrs service type</td>
    <td>INSUFFICIENT_TCS_AMOUNT</td>
    <td>Insufficient TCS amount passed based on lrs service type</td>
  </tr>
  <tr>
    <td><code>EX409</code></td>
    <td>Invalid value for pacb_lrs_declaration_individual</td>
    <td>INVALID_PACB_LRS_DECLARATION_INDIVIDUAL</td>
    <td>Invalid value for pacb_lrs_declaration_individual</td>
  </tr>
  <tr>
    <td><code>EX410</code></td>
    <td>Invalid Lrs Service Type</td>
    <td>INVALID_LRS_SERVICE_TYPE</td>
    <td>Invalid Lrs Service Type</td>
  </tr>
  <tr>
    <td><code>EX411</code></td>
    <td></td>
    <td>INVALID_PRICING_RESPONSE</td>
    <td></td>
  </tr>
  <tr>
    <td><code>EX412</code></td>
    <td>The IBIBO codes sent in request are wrong or not active for your merchant account.</td>
    <td>INVALID_ENFORCE_PAYMETHOD</td>
    <td>The IBIBO codes sent in request are wrong or not active for your merchant account.</td>
  </tr>
</SearchableRichTable>
