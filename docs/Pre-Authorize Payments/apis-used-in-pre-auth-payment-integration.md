---
title: APIs used in Pre-Auth Payment Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
This page provides a quick reference for all endpoints and commands across the Auth and Capture lifecycle.

***

## 1. Authorize, Capture, or Cancel Payment

| Operation                                         | HTTP Method | Endpoint         | Primary Command / Flag                                          | Hash Formula                                                                                              |
| :------------------------------------------------ | :---------- | :--------------- | :-------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| **Pre-Authorize Payment** (PayU Hosted)           | `POST`      | `<redacted URL>` | `_payment` with `pre_authorize=1`                               | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|SALT)` |
| **Pre-Authorize Payment** (Merchant Hosted Cards) | `POST`      | `<redacted URL>` | `_payment` (`pg=CC/DC`, `pre_authorize=1`)                      | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|SALT)` |
| **Pre-Authorize S2S Decoupled**                   | `POST`      | `<redacted URL>` | `_payment` (`txn_s2s_flow=4`, `auth_only=2`, `pre_authorize=1`) | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|SALT)` |
| **Capture Pre-Authorized Payment**                | `POST`      | `<redacted URL>` | `command="capture_transaction"`                                 | `sha512(key\|command\|var1\|salt)`                                                                        |
| **Cancel Pre-Authorized Payment**                 | `POST`      | `<redacted URL>` | `command="cancel_transaction"`                                  | `sha512(key\|command\|var1\|salt)`                                                                        |

***

## 2. Verify Payment & Track Action Status

| Operation                 | HTTP Method | Endpoint         | Primary Command                 | Description                                                                                                                             |
| :------------------------ | :---------- | :--------------- | :------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------- |
| **Verify Payment Status** | `POST`      | `<redacted URL>` | `command="verify_payment"`      | Checks current transaction state; `unmappedstatus=auth` indicates active hold, and `unmappedstatus=captured` indicates settled payment. |
| **Check Action Status**   | `POST`      | `<redacted URL>` | `command="check_action_status"` | Checks the processing status of queued capture or cancel requests using `request_id`.                                                   |

***

## 3. UPI One-Time Mandate & Reserve Pay APIs

| Operation            | HTTP Method | Endpoint         | Primary Command / Flags                                    | Description                                                  |
| :------------------- | :---------- | :--------------- | :--------------------------------------------------------- | :----------------------------------------------------------- |
| **UPI Intent OTM**   | `POST`      | `<redacted URL>` | `pg="UPI"`, `bankcode="INTENT"`, `pre_authorize=1`         | Returns `intentURIData` to launch UPI apps.                  |
| **UPI Collect OTM**  | `POST`      | `<redacted URL>` | `pg="UPI"`, `bankcode="UPI"`, `vpa="...", pre_authorize=1` | Sends mandate push notification to customer VPA.             |
| **Validate VPA API** | `POST`      | `<redacted URL>` | `command="validateVpa"`                                    | Validates customer VPA before initiating UPI Collect.        |
| **UPI Reserve Pay**  | `POST`      | `<redacted URL>` | UPI OTM with `siDetails` up to 90 days                     | Enables extended 90-day hold with multiple partial captures. |
