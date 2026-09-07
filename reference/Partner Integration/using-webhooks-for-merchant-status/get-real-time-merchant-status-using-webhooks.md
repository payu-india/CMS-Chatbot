---
title: Get Real-Time Merchant Status using Webhooks
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Partners can refer many merchants as they want, and every merchant has their own onboarding journey with PayU. To get the real-time merchant status update, resellers can integrate with PayU with their webhooks, where PayU will notify the reseller about the merchant onboarding status in real-time.

**Note**: Partners need to contact PayU or their Key Account Manager to enable the real-time merchant status service.

### Configure Webhooks

To configure webhooks:

1. If real-time merchant status service is enabled for Partner, PayU will hit the partner webhook URL. It will be a POST request which will consist of an authorization header and request payload. For more information on registering webhooks for real-time merchant status, refer to [Register Webhooks API to Get Real-Time Merchant Status](ref:register-webhooks-api-to-get-real-time-merchant-status).

### Validate the Webhook Signature

* Each Webhook payload will have a HMAC signature in the Authorization header.
* HMAC will be generated using the SHA-256 function using request payload passed to webhook URL, and a **client_secret** of partner application will be used as secret key to sign it and get a hashed string. This hashed string will be passed in the Authorization header.

**The formula for HMAC:**

```plaintext
OpenSSL::HMAC.hexdigest("SHA256", client_secret, payload.sort.join)
```

**Sample HMAC:**

```plaintext
"d59e5be387204e8c37bc8f46306f5013197b2f9d082ec859da1b09f9bc703036"
```

When the following payload is sent:

```json
{
  "previous_status": "Pending",
  "current_status": "Success",
  "change_timestamp": 18548123746,
  "mid": 123456,
  "merchant_uuid": "123-abcd-5678-gcjsa",
  "event_name": "Document status update",
  "error": "NA",
  "remarks": "NA"
}
```

`payload.sort.join` returns the following:

```plaintext
"change_timestamp18548123746current_statusSuccesserrorNAevent_nameDocument status updatemerchant_uuid123-abcd-5678-gcjsamid123456previous_statusPendingremarksNA"
```

1. Partner needs to verify this hashed string on its end before consuming the webhook’s data.
2. Partner needs to return an empty response with status 200 on receiving webhooks.
3. PayU will retry five times, waiting exponentially till it gets the **200** response from the partner. After which, it will be considered failed. Wait time after each retry will be 3, 9, 27, 81 and 243 seconds, respectively.

## Merchant onboarding event reference

The workbook defines 12 webhook event rows or dynamic event patterns. The event-specific examples and field notes in this section are sourced from the **Webhook Events** and **Payload Field Reference** sheets.

| #  | Event name or pattern                | Category          | Trigger action                                                   |
| :- | :----------------------------------- | :---------------- | :--------------------------------------------------------------- |
| 1  | Settlement Status Update             | Standard          | `update` (`settlement_status` change)                            |
| 2  | Nodal Status Update                  | Standard          | `update_bank_detail`                                             |
| 3  | Bank Verification Status Update      | Standard          | `update_bank_detail`                                             |
| 4  | Website Status Update                | Standard          | `update_merchant_account_status` (`status_type = WEBSITE`)       |
| 5  | Document Status Update               | Standard          | `update_merchant_account_status` (`status_type = KYC_DOCUMENTS`) |
| 6  | Agreement Status Update              | Standard          | `update_merchant_account_status` (`status_type = Agreement`)     |
| 7  | Aadhar Verification Status Update    | KYC               | `create_kyc` / `update_kyc` (`kyc_type = aadhaar_kyc`)           |
| 8  | Video KYC Verification Status Update | KYC               | `create_kyc` / `update_kyc` (`kyc_type = video_kyc`)             |
| 9  | `{DocumentCategory} Doc Created`     | Dynamic document  | `create_kyc_doc`                                                 |
| 10 | `{DocumentCategory} Status Update`   | Dynamic document  | `update_kyc_doc`                                                 |
| 11 | `{DocumentCategory} Doc Deleted`     | Dynamic document  | `delete_kyc_doc`                                                 |
| 12 | `merchant_credentials_issued`        | Credential issued | Merchant credentials generated and issued                        |

### Standard status payloads

Standard event samples use `previous_status`, `current_status`, `change_timestamp`, an identifier pair (`identifier` and `product_account_uuid` in the ProductAccountConsumer examples below), `event_name`, `error`, and `remarks`. The workbook also documents `mid`/`merchant_uuid` as the alternate identifier pair for AccountConsumer and MerchantConsumer events. Do not add the alternate pair to a payload unless it is present in the source payload for that event.

#### 1. Settlement Status Update

Fired when `settlement_status` changes. Possible `current_status` values are `Risk Hold`, `Thirdparty Hold`, `Active`, `Suspended`, `Risk \u0026 Thirdparty hold`, `NEFT Return`, and `Terminate`.

**Source sample payload:**

```json
{
  "previous_status": "Risk Hold",
  "current_status": "Active",
  "change_timestamp": 1776200038,
  "identifier": "760181268",
  "product_account_uuid": "11f1-3844-76243b60-8aa1-02f4a48620c1",
  "event_name": "Settlement Status Update",
  "error": "NA",
  "remarks": "NA"
}
```

#### 2. Nodal Status Update

Fired alongside Bank Verification Status Update. Both webhooks are sent in the same `bank_detail` update action. Possible `nodal_status` values are `Not Activated`, `Activation In Progress`, and `Activated`.

**Source sample payload:**

```json
{
  "previous_status": "Not Activated",
  "current_status": "Activated",
  "change_timestamp": 1776200038,
  "identifier": "760181268",
  "product_account_uuid": "11f1-3844-76243b60-8aa1-02f4a48620c1",
  "event_name": "Nodal Status Update",
  "error": "NA",
  "remarks": "NA"
}
```

#### 3. Bank Verification Status Update

Fired alongside Nodal Status Update for the same `bank_detail` update action. Possible `bank_verification_status` values are `Pending`, `Success`, `Verification Attempts Exhausted`, and `Failed`.

**Source sample payload:**

```json
{
  "previous_status": "Pending",
  "current_status": "Success",
  "change_timestamp": 1776200038,
  "identifier": "760181268",
  "product_account_uuid": "11f1-3844-76243b60-8aa1-02f4a48620c1",
  "event_name": "Bank Verification Status Update",
  "error": "NA",
  "remarks": "NA"
}
```

#### 4. Website Status Update

Fired by `update_merchant_account_status` when `status_type = WEBSITE`. Possible `website_approval_status` values are `Pending`, `Verification in Process`, `Website Not live`, `Website Incomplete`, `Website Under Construction`, `Website Error`, `Website OK` (terminal approved), and `Not Applicable`.

**Source sample payload:**

```json
{
  "previous_status": "Pending",
  "current_status": "Website OK",
  "change_timestamp": 1776200038,
  "identifier": "760181268",
  "product_account_uuid": "11f1-3844-76243b60-8aa1-02f4a48620c1",
  "event_name": "Website Status Update",
  "error": "NA",
  "remarks": "NA"
}
```

#### 5. Document Status Update

Fired by `update_merchant_account_status` when `status_type = KYC_DOCUMENTS`. Possible aggregate `document_status` values are `Pending`, `Docs Partially Received`, `Docs Received`, `Docs Partially Reuploaded`, `Docs Error`, `Docs Approved`, and `Exceptionally Approved`.

**Source sample payload:**

```json
{
  "previous_status": "Pending",
  "current_status": "Docs Approved",
  "change_timestamp": 1776200038,
  "identifier": "760181268",
  "product_account_uuid": "11f1-3844-76243b60-8aa1-02f4a48620c1",
  "event_name": "Document Status Update",
  "error": "NA",
  "remarks": "NA"
}
```

#### 6. Agreement Status Update

Fired by `update_merchant_account_status` when `status_type = Agreement`. Possible `agreement_status` values are `Not Generated`, `Pending`, `Sent`, `accepted`, `Counter Signed Received`, `Approved`, and `Rejected`.

**Source sample payload:**

```json
{
  "previous_status": "Not Generated",
  "current_status": "Approved",
  "change_timestamp": 1776200038,
  "identifier": "760181268",
  "product_account_uuid": "11f1-3844-76243b60-8aa1-02f4a48620c1",
  "event_name": "Agreement Status Update",
  "error": "NA",
  "remarks": "NA"
}
```

### KYC verification payloads

KYC verification samples contain `previous_status`, `current_status`, `product_account_uuid`, `identifier`, `capture_link`, and `event_name`. They do not contain `change_timestamp`, `error`, or `remarks`. For the first-time KYC events, `previous_status` is `null`.

#### 7. Aadhar Verification Status Update

The workbook notes `digilocker_status` values (16 total) including `pending`, `link_generated`, `in_progress`, `document_listed`, `document_pulled`, `approved`, `name_match_failed`, `access_denied`, and `failed`.

**Source sample payload:**

```json
{
  "previous_status": null,
  "current_status": "approved",
  "product_account_uuid": "11f1-3844-76243b60-8aa1-02f4a48620c1",
  "identifier": "760181268",
  "capture_link": null,
  "event_name": "Aadhar Verification Status Update"
}
```

#### 8. Video KYC Verification Status Update

`capture_link` is populated when the status is `link_generated`. The workbook lists `vkyc_status` values as `pending`, `link_generated`, `in_progress`, `review_required`, `approved`, `rejected`, `failed`, and `unable_to_verify`.

**Source sample payload:**

```json
{
  "previous_status": null,
  "current_status": "link_generated",
  "product_account_uuid": "11f1-3844-76243b60-8aa1-02f4a48620c1",
  "identifier": "760181268",
  "capture_link": "https://vcip.vendor.com/session/abc123",
  "event_name": "Video KYC Verification Status Update"
}
```

### Dynamic-document payloads

Dynamic-document events use the standard status field set: `previous_status`, `current_status`, `change_timestamp`, an identifier pair, `event_name`, `error`, and `remarks`. The event name varies by document category. The source samples use `identifier` and `product_account_uuid`.

#### 9. `{DocumentCategory} Doc Created`

The event name follows the pattern `"{DocumentCategory.name} Doc Created"`. Source examples include `PAN Card of Signing Authority Doc Created`, `Bank Account Proof Doc Created`, and `Address Proof of Signing Authority Doc Created`.

**Source sample payload:**

```json
{
  "previous_status": "Pending",
  "current_status": "DOCUMENT_SUBMITTED",
  "change_timestamp": 1776200038,
  "identifier": "760181268",
  "product_account_uuid": "11f1-3844-76243b60-8aa1-02f4a48620c1",
  "event_name": "PAN Card of Signing Authority Doc Created",
  "error": "NA",
  "remarks": "NA"
}
```

#### 10. `{DocumentCategory} Status Update`

The event name follows the pattern `"{DocumentCategory.name} Status Update"`. Possible per-document status values are `Pending`, `DOCUMENT_SUBMITTED`, `Approved`, `Declined`, `DOCUMENT_REUPLOADED`, `DIGITALLY_VERIFIED`, `Counter Signed Received`, `accepted`, and `Deleted`.

**Source sample payload:**

```json
{
  "previous_status": "DOCUMENT_SUBMITTED",
  "current_status": "Approved",
  "change_timestamp": 1776200038,
  "identifier": "760181268",
  "product_account_uuid": "11f1-3844-76243b60-8aa1-02f4a48620c1",
  "event_name": "PAN Card of Signing Authority Status Update",
  "error": "NA",
  "remarks": "Approved by reviewer"
}
```

#### 11. `{DocumentCategory} Doc Deleted`

The event name follows the pattern `"{DocumentCategory.name} Doc Deleted"`.

**Source sample payload:**

```json
{
  "previous_status": "DOCUMENT_SUBMITTED",
  "current_status": "Deleted",
  "change_timestamp": 1776200038,
  "identifier": "760181268",
  "product_account_uuid": "11f1-3844-76243b60-8aa1-02f4a48620c1",
  "event_name": "PAN Card of Signing Authority Doc Deleted",
  "error": "NA",
  "remarks": "NA"
}
```

### Credential-issued payload

#### 12. `merchant_credentials_issued`

This event is fired once when PayU generates and assigns merchant credentials after full onboarding approval. It has a different shape from the other events:

* It does not contain `previous_status` or `current_status`.
* It uses `timestamp`, not `change_timestamp`.
* It carries `mid` and `merchant_uuid`.
* It carries `merchant_key`, `salt_v1`, and `salt_v2`. These are **SENSITIVE** credential fields. Do not log, expose, or use the source sample credentials in an integration.
* Multiple payloads with the same `mid` but a different `timestamp` indicate that credentials were re-issued, such as for salt rotation.

**Source sample payload:**

> The values below reproduce the workbook source sample. Treat `merchant_key`, `salt_v1`, and `salt_v2` as sensitive and do not copy them into code, logs, tickets, screenshots, or client-side applications.

```json
{
  "event_name": "merchant_credentials_issued",
  "mid": "9212200",
  "merchant_uuid": "11f1-21cf-c68ac352-be45-023245796b9b",
  "merchant_key": "Tptlqh",
  "salt_v1": "q5EmFKWfsjSbbBFGGUqSAZWKaVVeKeYO",
  "salt_v2": "q5EmFKWfsjSbbBFGGUqSAZWKaVVeKeYO",
  "timestamp": 1773732652,
  "error": "NA",
  "remarks": "NA"
}
```

### Payload field reference

The following reference consolidates the field descriptions and possible-value notes from the workbook. Presence is event-specific; the samples above are authoritative for the exact fields shown in each event example.

You’re right. I removed the **Present in** column unintentionally while merging the **Type** and **Description / possible values** columns. Here is the corrected table:

| Field                  | Present in                                    | Description / possible values                                                                                                                                              |
| :--------------------- | :-------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `event_name`           | All events                                    | `String` — Human-readable event label. See the event reference above for all possible values.                                                                              |
| `previous_status`      | All events                                    | `String/null` — Status before the change. `null` for first-time KYC events (Aadhaar/Video KYC).                                                                            |
| `current_status`       | All events                                    | `String` — Status after the change. Webhook is only sent when `previous_status != current_status`.                                                                         |
| `change_timestamp`     | Standard events (not KYC verification events) | `Integer` — Unix epoch timestamp (seconds) of the status change.                                                                                                           |
| `mid`                  | AccountConsumer/ MerchantConsumer events       | `String` — Numeric merchant ID. Used in Merchant-based consumer payloads.                                                                                                  |
| `merchant_uuid`        | AccountConsumer/ MerchantConsumer events       | `String` — UUID-format merchant identifier. Used in Merchant-based consumer payloads.                                                                                      |
| `identifier`           | ProductAccountConsumer events                 | `String` — Numeric merchant ID (MID). Used in ProductAccount-based consumer payloads.                                                                                      |
| `product_account_uuid` | ProductAccountConsumer events                 | `String` — UUID-format product account identifier. Used in ProductAccount-based consumer payloads.                                                                         |
| `capture_link`         | Aadhaar KYC/Video KYC events only             | `String/null` — VCIP video call URL. Populated when `vkyc_status = link_generated`. `null` otherwise.                                                                      |
| `error`                | Standard events (not KYC verification events) | `String` — `"NA"` when no error. Contains an error message string when a processing error occurred.                                                                        |
| `remarks`              | Standard events (not KYC verification events) | `String` — `"NA"` when no remarks. Contains reviewer notes or system remarks when present.                                                                                 |
| `merchant_key`         | `merchant_credentials_issued` only            | `String` — PayU merchant key assigned at activation. Used as the public identifier in payment API calls. Treat as sensitive.                                               |
| `salt_v1`              | `merchant_credentials_issued` only            | `String` — Salt v1 for HMAC/SHA1 hash generation for legacy payment APIs. Treat as secret; do not log or expose.                                                           |
| `salt_v2`              | `merchant_credentials_issued` only            | `String` — Salt v2 for SHA256 hash generation for current payment APIs. Treat as secret; do not log or expose.                                                             |
| `timestamp`            | `merchant_credentials_issued` only            | `Integer` — Unix epoch timestamp (seconds) of credential issuance. The field name is `timestamp`, not `change_timestamp`, which is different from standard event payloads. |

> **Note:** For errors or remarks, refer to [KYC Errors and Solutions](ref:kyc-errors-and-solutions).
