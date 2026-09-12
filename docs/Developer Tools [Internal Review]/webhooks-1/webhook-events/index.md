---
title: Webhook Events and Payloads
deprecated: false
hidden: true
metadata:
  robots: index
---
You can accept customer payments using PayU products. By subscribing to payments webhook events you can get notified about payment state changes. Know more about <Anchor target="_blank" href="https://docs.payu.in/docs/manage-webhooks-using-dashboard">managing webhooks using the dashboard</Anchor>.

## List of Webhook Events

The table below lists the available webhook events.

| Product             | **Event Name** | Product | **Description**                                            |
| :------------------ | -------------- | ------- | :--------------------------------------------------------- |
| **Payment Gateway** | `Successful`   |         | Triggered when a payment is successful.                    |
| **Payment Gateway** | `Failed`       |         | Triggered when a payment is failed.                        |
| **Refunds**         | `Refund`       |         | Triggered when a payment refund is successful and failure. |
| **Disputes**        | `Dispute`      |         | Triggered when a dispute is raised for a payment.          |

## Sample Payloads

The following are the sample payloads for webhook events.

<Callout icon="📘" theme="info">
  ### Payload Format

  The payment successful and failure payloads are in the Form POST URL Encoded format:

  ` application/x-www-form-urlencode`
</Callout>

### Payment Gateway

Given below are the sample webhook event payloads of different payment products.

#### Cards

```text Credit Card (Amex) - Successful
mihpayid=613345778913016188
mode=CC
status=success
key=DSHd23
txnid=051fd7ecb5ff50818b80
amount=10.00
addedon=2026-09-04 14:11:23
productinfo=Product Info
firstname=Payu-Admin
lastname=
address1=
address2=
city=
state=
country=
zipcode=
email=test@example.com
phone=1234567890
udf1=
udf2=
udf3=
udf4=
udf5=
udf6=
udf7=
udf8=
udf9=
udf10=
card_token=
card_no=XXXXXXXXXXXX0005
field0=
field1=
field2=022849
field3=
field4=613345778913016188auth
field5=
field6=02
field7=AUTHPOSITIVE
field8=APPROVED
field9=Transaction is Successful
payment_source=payu
cardToken=
authenticationMethod=
PG_TYPE=CC-PG
error=E000
error_Message=No Error
issuing_bank=AMEX
card_type=AMEX
net_amount_debit=10
discount=0.00
offer_key=
offer_availed=
splitInfo={"splitStatus":"splitNotReceived","splitSegments":[]}
unmappedstatus=captured
hash=8080e275e4c306198489ff98528378bf0b168d0ed4bd3d3f46fdcea0119605682614b466aa3749fa65fb4313c59e6afd09ae7979e2c2844ec29a8123ab8892ca
bank_ref_no=328811022849
bank_ref_num=328811022849
bankcode=AMEX
surl=https://test.payu.in/admin/test_response
curl=https://test.payu.in/admin/test_response
furl=https://test.payu.in/admin/test_response
card_hash=eb06389e68f5158a712299c6e742f5da8a75a5c141b87c9fdfddfc9a56e16825
pa_name=PayU
authRefNo=1x5lRYlkHkADlc2eDSJ5obDmex=
```
```text Debit Card - Successful
mihpayid=613345778913028520
mode=DC
status=success
key=DSHd23
txnid=50d3a03c624676709cd
amount=10.00
addedon=2026-09-07 09:33:21
productinfo=Product Info
firstname=Payu-Admin
lastname=
address1=
address2=
city=
state=
country=
zipcode=
email=test@example.com
phone=1234567890
udf1=
udf2=
udf3=
udf4=
udf5=
udf6=
udf7=
udf8=
udf9=
udf10=
card_token=
card_no=XXXXXXXXXXXX9999
field0=
field1=349811814884
field2=322797
field3=10.00
field4=
field5=00
field6=05
field7=AUTHPOSITIVE
field8=AUTHORIZED
field9=Transaction is Successful
payment_source=payu
cardToken=
authenticationMethod=
PG_TYPE=DC-PG
error=E000
error_Message=No Error
issuing_bank=KOTAK
card_type=VISA
net_amount_debit=10
discount=0.00
offer_key=
offer_availed=
splitInfo={"splitStatus":"splitNotReceived","splitSegments":[]}
unmappedstatus=captured
hash=bf7ffc615a5c3ed89420d9dc295c4aa67e35be66930f00dd387d24f59525efd2ddd2978afeef4b2e02c7528b027f119333186be0976d859f28238790a4232729
bank_ref_no=224560489731950270
bank_ref_num=224560489731950270
bankcode=VISA
surl=https://test.payu.in/admin/test_response
curl=https://test.payu.in/admin/test_response
furl=https://test.payu.in/admin/test_response
card_hash=5d9fd133ba5ecd0a0311c3463495667ac5caaac1e403bf917ace7b24a5ef50c6
pa_name=PayU
```
```text Failed
mihpayid=27553387529
&mode=CC
&status=failure
&key=1LtbLt
&txnid=adanilounge-fef018ea-dd58-4af9-bce2-9d1920a93421-1
&amount=2.00
&addedon=2026-03-04+14%3A47%3A38
&productinfo=Description+not+provided
&firstname=CARDHOLDERXXXXXXXXNAME
&lastname=CARDHOLDERXXXXXXXXNAME
&address1=
&address2=
&city=
&state=
&country=
&zipcode=
&email=name%40mail.com
&phone=##########
&udf1=fef018eadd584af9bce29d1920a93421
&udf2=loungeone
&udf3=loungeone
&udf4=fef018eadd584af9bce29d1920a93421
&udf5=0
&udf6=
&udf7=
&udf8=
&udf9=
&udf10=
&card_token=
&card_no=XXXXXXXXXXXX6509
&field0=
&field1=7726158727156987305915
&field2=
&field3=
&field4=
&field5=93
&field6=05
&field7=AUTHNEGATIVE
&field8=93+%7C+Transaction+cannot+be+completed%3B+violation+of+law+%7C+Transaction+cannot+be+completed%3B+violation+of+law
&field9=Transaction+declined+due+to+card+not+enabled+for+online+transactions+or+user+%2F+Bank+Defined+Restrictions
&payment_source=payuS2S
&cardToken=
&authenticaticationMethod=
&PG_TYPE=CC-PG
&error=E325
&error_Message=Bank+denied+transaction+on+the+card.
&net_amount_debit=0
&discount=0.00
&offer_key=
&offer_availed=
&unmappedstatus=failed
&hash=eded314a21cc033d3c9d620006492b76a430bef7f0d661313a6ed9f5717fa7dca8c6ec885cba8ecfdf95396fce3a5ef1a55e42c4b9f0fc8fcab0767e80130eeb
&bank_ref_no=7726158727156987305915
&bank_ref_num=7726158727156987305915
&bankcode=CC
&surl=https%3A%2F%2Fapi.juspay.in%2Fv2%2Fpay%2Fresponse%2Fadanilounge%2FmozmFhdZrfsT69TfhWB
&curl=https%3A%2F%2Fapi.juspay.in%2Fv2%2Fpay%2Fresponse%2Fadanilounge%2FmozmFhdZrfsT69TfhWB
&furl=https%3A%2F%2Fapi.juspay.in%2Fv2%2Fpay%2Fresponse%2Fadanilounge%2FmozmFhdZrfsT69TfhWB
&threeDSVersion=2.2.0
```

#### NetBanking

```text Success
mihpayid=613345778913000865
mode=NB
status=success
key=DSHd23
txnid=C250626525054aaqasa123
amount=10.00
addedon=2026-09-02 21:52:08
productinfo=FLT
firstname=UserT
lastname=
address1=
address2=
city=
state=
country=
zipcode=
email=test@test.com
phone=9876543210
udf1=udf1
udf2=udf2
udf3=udf3
udf4=udf4
udf5=udf5
udf6=
udf7=
udf8=
udf9=
udf10=
card_token=
card_no=
field0=
field1=
field2=
field3=
field4=
field5=
field6=
field7=
field8=
field9=Transaction Completed Successfully
payment_source=payu
cardToken=
authenticationMethod=
PG_TYPE=NB-PG
error=E000
error_Message=No Error
net_amount_debit=21.8
discount=0.00
offer_key=
offer_availed=
additionalCharges=11.80
splitInfo={"splitStatus":"splitNotReceived","splitSegments":[]}
unmappedstatus=captured
hash=d29de8fb3184bcc7a8481f8cde080049f56b0c20b54555aea9897a32ba23a3757d6e45f2859ceebe2974584f4f62442d9d2f03b87479c5312df42460fd281582
bank_ref_no=3bf3f58e-c7a3-4567-88e2-55d7c3d64318
bank_ref_num=3bf3f58e-c7a3-4567-88e2-55d7c3d64318
bankcode=TESTPGNB
surl=https://bijliftt.com/WegrowMobTest/WeGrowService.svc/eNachRegistrationcallback
curl=https://test.payu.in/admin/test_response
furl=https://test.payu.in/admin/test_response
pa_name=PayU
```
```text Failure
mihpayid=613345778913000865
mode=NB
status=failure
key=DSHd23
txnid=C250626525054aaqasa123
amount=10.00
addedon=2026-09-02 21:52:08
productinfo=FLT
firstname=UserT
lastname=
address1=
address2=
city=
state=
country=
zipcode=
email=test@test.com
phone=9876543210
udf1=udf1
udf2=udf2
udf3=udf3
udf4=udf4
udf5=udf5
udf6=
udf7=
udf8=
udf9=
udf10=
card_token=
card_no=
field0=
field1=
field2=
field3=
field4=
field5=
field6=
field7=
field8=
field9=Transaction+declined
payment_source=payu
cardToken=
authenticationMethod=
PG_TYPE=NB-PG
error=E000
error_Message=Bank+denied
net_amount_debit=21.8
discount=0.00
offer_key=
offer_availed=
additionalCharges=11.80
splitInfo={"splitStatus":"splitNotReceived","splitSegments":[]}
unmappedstatus=captured
hash=d29de8fb3184bcc7a8481f8cde080049f56b0c20b54555aea9897a32ba23a3757d6e45f2859ceebe2974584f4f62442d9d2f03b87479c5312df42460fd281582
bank_ref_no=3bf3f58e-c7a3-4567-88e2-55d7c3d64318
bank_ref_num=3bf3f58e-c7a3-4567-88e2-55d7c3d64318
bankcode=TESTPGNB
surl=https://bijliftt.com/WegrowMobTest/WeGrowService.svc/eNachRegistrationcallback
curl=https://test.payu.in/admin/test_response
furl=https://test.payu.in/admin/test_response
pa_name=PayU
```

#### Payments Event Payload Parameter Description

<Callout icon="📘" theme="info">
  ### **Webhook amount field:**&#x20;

  The `amount` field in the webhook payload reflects the **original transaction amount** passed in the payment request — it does not include convenience fees or MDR charges added by the merchant. If you have configured convenience fees, the `net_amount_debit` field (where available) reflects the actual amount debited from the customer's account. Always use `amount` for reconciliation against your order value and `net_amount_debit` for the customer-side amount.
</Callout>

<Accordion title="Parameters and Description" icon="fa-table">
  | Parameters               | Description                                                                                                                                                                                                                                                     |
  | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | mihpayid                 | Unique transaction ID assigned by PayU for each transaction. Use for inquiry or refund.                                                                                                                                                                         |
  | key                      | Merchant key identifying the merchant's PayU account; same as in the transaction request.                                                                                                                                                                       |
  | txnid                    | Transaction ID (Order ID) that was sent by the merchant in the transaction request.                                                                                                                                                                             |
  | amount                   | Original payment amount sent in the transaction request by the merchant.                                                                                                                                                                                        |
  | productinfo              | Product description sent in the transaction request.                                                                                                                                                                                                            |
  | firstname                | Customer first name as sent in the transaction request.                                                                                                                                                                                                         |
  | lastname                 | Customer last name as sent in the transaction request.                                                                                                                                                                                                          |
  | email                    | Customer email as sent in the transaction request.                                                                                                                                                                                                              |
  | phone                    | Customer phone number as sent in the transaction request.                                                                                                                                                                                                       |
  | address1                 | Customer address line 1 (from request).                                                                                                                                                                                                                         |
  | address2                 | Customer address line 2 (from request).                                                                                                                                                                                                                         |
  | city                     | Customer city (from request).                                                                                                                                                                                                                                   |
  | state                    | Customer state (from request).                                                                                                                                                                                                                                  |
  | country                  | Customer country (from request).                                                                                                                                                                                                                                |
  | zipcode                  | Customer zip/postal code (from request).                                                                                                                                                                                                                        |
  | udf1 – udf10             | User-defined fields (udf1–udf5 documented; udf6–udf10 in response). Same values as sent in the transaction request. Character limit 255 for udf1–udf5.                                                                                                          |
  | hash                     | Hash calculated by PayU. Merchant must verify it before marking the transaction success/failure to ensure integrity. See [Response Handling](doc:using-payu-hash-verification-tool).                                                                            |
  | status                   | Outcome of the transaction: `success`, `failure`, or `pending`. Treat only `success` as successful.                                                                                                                                                             |
  | error                    | Error code indicating the reason for failure (e.g. E500). Failure reasons vary by bank.                                                                                                                                                                         |
  | error_Message            | Human-readable error message. Refer to [Error Codes](ref:error-codes) for the list.                                                                                                                                                                             |
  | PG_TYPE                  | Payment gateway type used for the transaction (e.g. `CC-PG` for credit card, `DC-PG` for debit card, `UPI-PG`, `CASH-PG`, `EMI-PG`, `BNPL-PG`, `QR-PG`).                                                                                                        |
  | bank_ref_num             | For successful transactions, the bank reference number generated by the bank.                                                                                                                                                                                   |
  | bank_ref_no              | Same as bank_ref_num; alternate parameter name for bank reference number.                                                                                                                                                                                       |
  | unmappedstatus           | Transaction status in PayU’s internal system; can include intermediate states. Values include: dropped, bounced, captured, auth, failed, usercancelled, pending. See [Payment State Explanations](ref:payment-state-explanations).                              |
  | surl                     | Success URL – URL on which PayU redirects when the transaction is successful.                                                                                                                                                                                   |
  | furl                     | Failure URL – URL on which PayU redirects when the transaction fails.                                                                                                                                                                                           |
  | curl                     | Cancel URL – URL used when the user cancels (character limit 50 in request).                                                                                                                                                                                    |
  | addedon                  | Date and time when the transaction was recorded (e.g. `2026-02-27 14:24:42`).                                                                                                                                                                                   |
  | discount                 | Discount amount applied (e.g. `0.00`).                                                                                                                                                                                                                          |
  | net_amount_debit         | Net amount debited from the customer.                                                                                                                                                                                                                           |
  | additionalCharges        | Additional charges applied (e.g. convenience fee).                                                                                                                                                                                                              |
  | payment_source           | Source of the payment (e.g. `payu`).                                                                                                                                                                                                                            |
  | pa_name                  | Name of the payment aggregator through which the transaction was routed (e.g. PayU, RazorPay). Shown when using Maximiser / other aggregators.                                                                                                                  |
  | offer_key                | Key of the offer applied, if any.                                                                                                                                                                                                                               |
  | offer_availed            | Indicates whether an offer was availed.                                                                                                                                                                                                                         |
  | authenticaticationMethod | Authentication method used (e.g. 3DS). Note: name may appear with typo in payload.                                                                                                                                                                              |
  | field0 – field9          | Gateway- or flow-specific fields. Content varies by payment mode and outcome (e.g. bank reference, RRN, auth result, status message). For cards, field7/field8/field9 often carry auth result or message (e.g. AUCNEGATIVE, UNKNOWN, Message Received Invalid). |
</Accordion>

#### Payment State Explanations

The following table provides description for each status of the transaction. You must map the order status using the payment state specified in the **Status** column of the following table. As Test environment (Sandbox) is a replica of the Production environment, you can push the code in production by just replacing account credentials and URL.

<Accordion title="Status and Description" icon="far fa-table">
  <Payment_State_Explanation />
</Accordion>

### Refund Successful

<Callout icon="📘" theme="info">
  ### **Note:**

  The Refund and Dispute payloads are in the following format:

  - **Method:** POST
  - **Content type:** application/json
</Callout>

**Field reference:** `merchantTxnId` (merchant order ID), `mihpayid` (PayU transaction ID), `token` (merchant refund ID), `request_id` (PayU refund ID), `amt` (refund amount), `status` (`success` or `failure`), `action` (`refund`), `key` (merchant key), `bank_ref_num` / `bank_arn` (bank reference).

```json
{
  "additionalValue1": null,
  "bank_arn": null,
  "refund_mode": "Instant Credit through UPI",
  "bank_ref_num": "100142082006",
  "key": "IahMJL",
  "amt": "72.00",
  "remark": null,
  "status": "success",
  "token": "PZT2506150013OR4AN33",
  "mihpayid": " 23907365951 ",
  "request_id": "17265314530",
  "merchantTxnId": "PZT2506150013OR4AN02",
  "additionalValue2": null,
  "action": "refund"
}
```

### Refund ARN Update

**Field reference:** Same refund webhook fields as above; `bank_arn` and `bank_ref_num` contain the updated ARN from the bank.

```json
{
  "additionalValue1":null,
  "bank_arn":308239782136,
  "refund_mode":"Instant Credit through UPI",
  "bank_ref_num":"308239782136",
  "key":"lF76TH",
  "amt":"149.00",
  "remark":null,
  "status":"success",
  "token":"DG0036362",
  "mihpayid":"17025521702",
  "request_id":"11865427756",
  "merchantTxnId":"ORDER_33172661_1679394745",
  "additionalValue2":null,
  "action":"refund"
}
```

### Refund Failure

**Field reference:** Refund failure payload uses the same fields as a successful refund; check `status` (`failure`) and `remark` for the failure reason.

```json
{
  "additionalValue1": null,
  "bank_arn": null,
  "refund_mode": "Instant Credit through UPI",
  "bank_ref_num": "100142082006",
  "key": "IahMJL",
  "amt": "72.00",
  "remark": null,
  "status": "failure",
  "token": "PZT2506150013OR4AN33",
  "mihpayid": " 23907365951 ",
  "request_id": "17265314530",
  "merchantTxnId": "PZT2506150013OR4AN02",
  "additionalValue2": null,
  "action": "refund"
}
```

#### Refunds Payload Parameters

<Accordion title="Parameters and Description" icon="fa-table">
  | Parameter        | Description                                                               | Source Data                      |
  | ---------------- | ------------------------------------------------------------------------- | -------------------------------- |
  | merchantTxnId    | `String` Merchant Sale transaction id `Character Limit: 50`               |                                  |
  | mihpayid         | `String` payuid `Character Limit: max 255 chars`                          | Var1 for refund initiate API     |
  | bank_arn         | `String` Reference number for refund tracking `Character Limit: 45`       |                                  |
  | bank_ref_num     | `String` Bank reference number `Character Limit: 255`                     |                                  |
  | request_id       | `String` Unique refund id generated by payu `Character Limit:  255`       |                                  |
  | token            | `String` Unique refund txn id provided by merchant `Character Limit:  23` | Var2 for refund initiate API     |
  | action           | `String` refund `Character Limit: 32`                                     |                                  |
  | amt              | `String` Refund amount `Character Limit: 65`                              | Var3 for refund initiate API     |
  | status           | `String` Status of the refund `Character Limit: 32`                       | Possible values: success/failure |
  | additionalValue1 | For future scope                                                          |                                  |
  | additionalValue2 |                                                                           |                                  |
  | key              | `String` Merchant key `Character Limit: 20 `                              |                                  |
</Accordion>

### Dispute

**Field reference:** `type` (event category), `event` (dispute event name), `data` (dispute details including transaction and chargeback information).

```json
{
  "type": "payments",
  "event": "dispute",
  "reason_code": "Fraud - Card Present Environment",
  "created_at": "2025-01-15T21:28:25.000+05:30",
  "updated_at": "2025-05-27T22:08:16.000+05:30",
  "mid": "2",
  "cb_id": 1761758,
  "txn_id": "999000000000468",
  "cb_type": "RBI/BO",
  "due_date": "2025-03-31",
  "cb_amount": "1.0",
  "cb_status": "Bank Comm Sent"
}
```

#### Dispute Payload Parameters

<Accordion title="Parameters and Description" icon="fa-table">
  | Field       | Description                                                                                                                                                                                                      |
  | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | type        | Type of transaction  and merchant must include the value as **payments** only.                                                                                                                                   |
  | event       | Event type and the merchant must the include the value as **dispute** only.                                                                                                                                      |
  | reason_code | Reason for the chargeback. For the list of reason codes, refer to [Reason codes for chargebacks](https://docs.payu.in/docs/webhooks-for-chargeback#reason-codes-for-chargebacks).                                |
  | created_at  | Timestamp when the chargeback was created                                                                                                                                                                        |
  | updated_at  | Timestamp when the chargeback was last updated                                                                                                                                                                   |
  | mid         | PayU Merchant ID                                                                                                                                                                                                 |
  | cb_id       | Chargeback ID                                                                                                                                                                                                    |
  | txn_id      | This is the PayU transaction ID that is associated with the chargeback.                                                                                                                                          |
  | cb_type     | Type of chargeback (for example, "RBI/BO", that is, Reserve Bank of India/Banking Operations)                                                                                                                    |
  | due_date    | Due date for the chargeback resolution                                                                                                                                                                           |
  | cb_amount   | Amount involved in the chargeback                                                                                                                                                                                |
  | cb_status   | Current status of the chargeback. For the possible chargeback status values, refer to [cb_status field values description](https://docs.payu.in/docs/webhooks-for-chargeback#cb_status-field-values-description) |
</Accordion>

#### cb_status Parameter Values

<Accordion title="Parameters and Description" icon="fa-table">
  The `cb_status` or chargeback status field can have the following values:<br />

  | Chargeback Status            | Description                                                                                                                                                                                                                                                                                                            |
  | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | New                          | It indicates that a new chargeback has been initiated by the customer basis the chargeback reason.                                                                                                                                                                                                                     |
  | Pending Response             | It indicates that the chargeback is awaiting merchant response, that is, to accept, partially accept or decline with evidence.                                                                                                                                                                                         |
  | Pending Doc Review           | It indicates that merchant has submitted their response, and the response are being reviewed by the PayU Chargeback team.                                                                                                                                                                                              |
  | Submitted to Bank            | It indicates that the PayU Chargeback team has completed their review and forwarded the evidence to the bank for representment.                                                                                                                                                                                        |
  | Insufficient Document        | It indicates that the PayU Chargeback team has reviewed the evidence documents and is requesting the merchant for additional documents for representment or the correct document based on the Chargeback team's comment.                                                                                               |
  | Closed Customer Favour       | It indicates that that the chargeback has been closed in the customer's favour. The merchant will lose the chargeback amount to the customer.                                                                                                                                                                          |
  | Closed in Merchant Favour    | It indicates that the chargeback has been closed in the merchant's favour. The chargeback amount will be reversed back to the merchant account.                                                                                                                                                                        |
  | Closed under Fraud Liability | It indicates that the chargeback has been closed since the transaction has been identified as fraudulent. Moreover, PayU will cover the chargeback amount under the fraud liability program so the chargeback amount will be reversed back to the merchant account or will not be debited from the merchant's account. |
</Accordion>

<Callout icon="📘" theme="info">
  ### **Webhook Logs**

  You can now view the webhook logs on your dashboard by navigating to:

  Dashboard -> Developers -> Webhook logs

  Ensure that your webhook URL is captures and handles the posted response payload. Additionally, you may use the <Anchor target="_blank" href="https://docs.payu.in/reference/transaction-callback-api">Transaction Callback API</Anchor> to manually test the response payload:
</Callout>

## IP Addresses

All our webhook requests originate from a set of IP addresses. If your server-handing webhook requests is behind a firewall, you should whitelist the following set of IP addresses to ensure that requests are successful:

| **Environment**        | **DC IPs**                                                             | **DR IPs**                                                              |
| :--------------------- | :--------------------------------------------------------------------- | :---------------------------------------------------------------------- |
| Test Environment       | <ul><li>180.179.174.1</li> <li>3.6.73.183</li> <li>3.6.83.44</li></ul> | NA                                                                      |
| Production Environment | <ul><li>3.7.89.1</li> <li>3.7.89.2</li> <li>3.7.89.3</li></ul>         | <ul><li>52.140.8.88</li> <li>52.140.8.89</li> <li>52.140.8.64</li></ul> |
