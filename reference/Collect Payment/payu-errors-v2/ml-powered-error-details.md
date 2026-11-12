---
title: ML-Powered Error Details
deprecated: false
hidden: true
metadata:
  robots: index
---
Issuing banks, card networks and payment gateways report transaction failures in widely varying formats, and a single failure reason may be returned as many different raw messages. PayU applies a machine learning model to each raw failure response and maps it to a single standard error code, accompanied by a message for the end customer and a detailed explanation for the merchant.

When a transaction fails, PayU includes an `error_details` object in the transaction response. This object contains:

* A standard PayU error code
* A message intended for the end customer
* A detailed technical message intended for the merchant
* The raw error returned by the gateway

The `error_details` object is returned **in addition to** the existing response fields. PayU continues to return `field9` and `error_Message`, so existing integrations require no changes.

On PayU Hosted Checkout, PayU displays `userMessage` on the failure screen automatically.

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
  ### **Note:**

  The reason for failure depends upon the error codes provided by different banks and hence the detailing of error reasons may differ from one transaction to another.
</Callout>

***

## Cards

This section contains error codes associated with cards.

### **Sample Response**

The following sample illustrates the `error_details` object for a failed domestic card transaction:

<Tabs>
  <Tab title="Response Payload">
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


  </Tab>

  <Tab title="Parameter Description">
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

    ### `newErrorCode` Object Parameters

    <Tabs>
      <Tab title="Category (first digit)">
        | Digit | Category                 | Description                                                                                              | Recommended action                                                                          |
        | ----- | ------------------------ | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
        | 1     | Customer error           | The customer entered incorrect details, cancelled the payment, or did not complete it.                   | Request the customer to verify their details and retry.                                     |
        | 2     | Internal technical error | A technical issue within PayU systems.                                                                   | Retry the transaction. If the issue persists, contact PayU support.                         |
        | 3     | External technical error | A technical issue at the bank, card network or another partner.                                          | Retry the transaction, or request the customer to use an alternative payment method.        |
        | 4     | Configuration error      | The merchant account or integration is not configured for this payment.                                  | Contact your PayU account manager or PayU support.                                          |
        | 5     | Business decline         | The transaction was declined for a business reason, such as insufficient funds or a limit being reached. | Request the customer to use an alternative payment method or contact their bank.            |
        | 6     | Risk decline             | The transaction was declined by the bank or by risk checks for security reasons.                         | Do not retry with the same card. Request the customer to use an alternative payment method. |
        | 0     | Unclassified             | The failure could not be categorised.                                                                    | Retry the transaction. If the issue persists, contact PayU support.                         |
      </Tab>

      <Tab title="Source (second digit)">
        | Digit | Source      | Point of failure                    |
        | ----- | ----------- | ----------------------------------- |
        | 1     | Issuer      | The customer's bank                 |
        | 2     | Network     | The card network or payment scheme  |
        | 3     | Merchant    | The merchant account or integration |
        | 4     | Customer    | The customer's action or input      |
        | 5     | PayU        | PayU systems                        |
        | 0     | Unspecified | The source could not be determined  |
      </Tab>
    </Tabs>

    **Format:** `EN` + Category (first digit) + Source (second digit) + Message number (variable length).<br />For example: `EN311`, `EN3126`, `EN30505`.

    #### Examples

    | Code   | Interpretation                                                          |
    | ------ | ----------------------------------------------------------------------- |
    | EN3126 | External technical error (3) at the customer's bank (1), message 26     |
    | EN6145 | Risk decline (6) by the customer's bank (1), message 45                 |
    | EN4312 | Configuration error (4) in the merchant's configuration (3), message 12 |
    | EN1408 | Customer error (1) arising from customer input (4), message 8           |
  </Tab>

  <Tab title="New Tab">
    >
  </Tab>
</Tabs>

<Callout icon="📘" theme="info">
  ### **Recommendations**

  * **Analytics and reporting:** Group failures by `newErrorCode`, or by its category and source digits, rather than parsing the free-text value in `field9`.
  * **Triage:** Use the category digit to determine the next action. For example, category 6 (Risk decline) indicates that the transaction must not be retried with the same card, and category 4 (Configuration error) indicates that you should contact your PayU account manager.
  * **Custom failure pages:** Display only `userMessage` to end customers. Do not display `merchantMessage` or `pgError`.
  * **Message updates:** PayU updates error messages periodically to address new error scenarios across the ecosystem. Ensure that any logic built on this data accommodates such updates.
</Callout>

### User Error Messages by Payment Mode

The following lists set out the `userMessage` values that PayU returns to end customers for each payment mode.

<Accordion title="Domestic Cards">
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


</Accordion>

### Other Payment Modes

<Callout icon="📘" theme="info">
  ### **Under development**

  Error lists for International Cards, Net Banking, UPI, Wallets, EMI and BNPL are under development. PayU will publish a list for each payment mode in this section as it becomes available. In the interim, please refer to the [Standard Error Codes](#standard-error-codes) for these payment modes.
</Callout>