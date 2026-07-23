---
title: APIs used for Payouts Integration
deprecated: false
hidden: false
metadata:
  title: APIs used for Payouts Integration
  robots: index
---
PayU offers Payouts as a product for businesses to make instant payments to their customers. The Payouts APIs are categorized based on the following capabilities:

### Authentication for Payouts

| API name                                                                                              | Description                                                                                 |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| [Generate Token using Merchant's Credentials API](ref:generate-token-using-merchants-credentials-api) | Generates an authentication token using the merchant's username and password.               |
| [Generate Token using Private Client ID](ref:generate-token-using-private-client-id)                  | Generates an authentication token using the merchant's private client ID and client secret. |
| [Refresh Token API - Payouts](ref:refresh-token-api-payouts)                                          | Refreshes the validity of an existing authentication token.                                 |
| [IP Check for Payouts](ref:ip-check-for-payouts)                                                      | Adds an IP allowlist check as an additional security measure for Payouts requests.          |

### Initiation and Tracking

| API name                                                                 | Description                                                                             |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| [Get Account Details API - Payouts](ref:get-account-details-api-payouts) | Retrieves complete details of the merchant's Payouts account.                           |
| [Initiate Transfer API](ref:initiate-transfer-api)                       | Initiates or schedules a transfer to a beneficiary's bank account, VPA, or credit card. |
| [Check Transfer Status API](ref:check-transfer-status-api)               | Retrieves the status of transfers initiated by the merchant.                            |
| [Cancel Transfer API](ref:cancel-transfer-api)                           | Cancels a transfer that is in the queued or scheduled state.                            |
| [Disable Queued Payouts API](ref:disable-queued-payouts-api)             | Marks queued transactions as failed when the merchant account has insufficient balance. |

### Verification and Validation

| API name                                              | Description                                                                                     |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| [Get IFSC Details API](ref:get-ifsc-details-api)      | Retrieves bank details for a specified IFSC code.                                               |
| [Verify Account or Penny Test API](ref:verifyaccount) | Verifies a beneficiary bank account through a penny test and returns the account holder's name. |
| [Validate VPA - Payouts](ref:validatevpa)             | Checks whether a customer's VPA exists before a UPI transfer is initiated.                      |

### Smart Send APIs

| API name                                                     | Description                                                                                               |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| [Create Smart Send Link API](ref:create-smart-send-link-api) | Creates and sends a Smart Send link when the beneficiary's bank account details or VPA are unavailable.   |
| [Smart Send Details API](ref:smart_send_details_api)         | Retrieves the details of a Smart Send transaction using the payout merchant ID and merchant reference ID. |
| [Extend Expiry Date API](ref:extend-expiry-date-api)         | Extends the expiry date of an unexpired Smart Send link with a pending transaction.                       |
| [Cancel Smart Send API](ref:cancel-smartsend-api)            | Cancels a Smart Send payment link.                                                                        |
| [Smart Send Error Codes](ref:smart-send-error-codes)         | Lists the error codes and descriptions returned by the Smart Send APIs.                                   |

### Bulk Smart Send

| API name                                             | Description                                                              |
| ---------------------------------------------------- | ------------------------------------------------------------------------ |
| [Bulk File Upload API](ref:bulk-upload-api)          | Uploads a CSV, XLSX, or XLS file containing Smart Send transfer details. |
| [Bulk Process File API](ref:bulk-process-file-api)   | Processes an uploaded file containing Smart Send transfer details.       |
| [Bulk Upload Status API](ref:bulk-upload-status-api) | Retrieves the processing status of an uploaded bulk transfer file.       |

### Beneficiary Management

| API name                                                                     | Description                                                            |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [View Beneficiary Details API](ref:view-beneficiary-details-api)             | Retrieves beneficiaries registered under the merchant account.         |
| [Create or Register Beneficiary API](ref:create-or-register-beneficiary-api) | Registers a beneficiary under the merchant account for use in payouts. |

You can also configure Payout Webhooks to receive notification on various events such as **Transfer Success Webhook**, **Transfer Failed Webhook**, **Scheduled Downtime Webhook**, etc. Refer to [Payouts Webhooks](doc:payouts-webhooks) to learn more about Payout Webhooks.

### Before you Begin

- PayU strongly recommends you test your integration using the test credentials. For more information refer to [Test Credentials](doc:test-credentials-for-payouts).
- Before you use the above-listed APIs, you need to understand the Payouts integration and configure the PayU Dashboard. For more information, refer to the following documentation:
  - [Introduction to Payouts](doc:introduction-to-payouts)
  - [Payouts Dashboard](doc:payouts-dashboard)

<br />
