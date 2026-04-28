---
title: Error Codes and Messages
excerpt: >-
  PayU payment error codes, messages, developer-friendly descriptions, possible
  causes, and fixes.
deprecated: false
hidden: true
metadata:
  description: PayU payment error codes, messages, causes, and recommended fixes.
  robots: index
---
Use this table to map PayU response fields to the action your integration should take.

For the complete reference, see [Error Codes](ref:error-codes). For transaction-stage diagnostics, see [Transaction Stages - Error References on Field7 & Field8](ref:transaction-stages-error-references-field7-field8).

<SearchableTable
  headers={[
    'Error Code/Type',
    'Error Message as Returned by PayU',
    'Description',
    'Possible cause',
    'Recommended fix'
  ]}
  rows={[
    ['E000','No Error','Transaction completed successfully.','Payment was authorized and captured successfully.','Mark the order as paid only after validating response hash and matching txnid, amount, and status.'],
    ['E700','Validation of secure hash failed','PayU could not validate the request hash.','Wrong hash sequence, wrong salt, missing delimiters, value mismatch, environment key/salt mismatch.','Recreate the hash server-side using the exact posted values and correct salt. See Generate Hash (PayU Hosted).'],
    ['SECURE_HASH_FAILURE','Validation of secure hash failed','Security validation failed.','Request was tampered with or hash was generated from normalized values that differ from submitted values.','Log the raw hash string server-side and compare it with the posted request. Never send salt to frontend.'],
    ['E1101','Transaction failed due to invalid params shared by the merchant','PayU rejected the transaction request because one or more parameters are invalid.','Invalid amount, txnid, productinfo, surl, furl, pg, bankcode, or unsupported combination of fields.','Validate request payload before submitting to PayU. Confirm mandatory fields for your integration type.'],
    ['E4156 / E4373','VALIDATION ERROR','Generic validation failure.','Missing or malformed parameter, invalid field length, invalid enum, unsupported value.','Compare request with API reference and check raw request logs.'],
    ['Missing parameter','One or more mandatory parameters are missing','Required fields were not sent.','Frontend did not pass data to backend, backend omitted empty fields, or request content type is incorrect.','Send all mandatory fields and include empty UDF delimiters in the hash string.'],
    ['Invalid amount','Invalid amount / Please enter valid amount','Amount is missing or not accepted.','Amount is blank, zero, negative, contains commas, has unsupported decimal precision, or differs between hash and request.','Send amount as a decimal string, for example 10.00, and use the exact same value in hash generation.'],
    ['Duplicate txnid','Duplicate Transaction ID / THE REQUEST IS DUPLICATE','The transaction ID was already used.','Retrying a new payment attempt with the same txnid, or reusing order ID as transaction ID without uniqueness.','Generate a unique txnid for every new payment attempt. Use Transaction Detail APIs for status checks instead of re-posting the same transaction.'],
    ['E4150','Transaction declined due to duplicate request','PayU or bank detected a duplicate request.','Same transaction submitted multiple times in a short window.','Disable double-submit on frontend and enforce idempotency on backend.'],
    ['E1201','You are not authorized to do this transaction.','Merchant is not authorized for requested service.','Payment mode, route, S2S flow, currency, or feature not enabled for merchant.','Confirm merchant configuration in Dashboard or with PayU Integration Team.'],
    ['E1631','Merchant Validation Failed','Merchant-level validation failed.','Invalid merchant key, inactive merchant, invalid bank MID/terminal, or disabled configuration.','Verify key/salt, environment, MID status, and payment mode enablement.'],
    ['E1621','Merchant does not have access to S2S flow','S2S flow is not enabled for the merchant.','Attempting S2S APIs without enablement.','Request S2S enablement and confirm production/test credentials.'],
    ['E1622','S2S flow not enabled on selected payment gateway','Selected payment gateway does not support enabled S2S route.','Wrong pg/bankcode or payment mode not configured for S2S.','Use an enabled payment method or update gateway configuration.'],
    ['E1615','txn_s2s_flow missing parameter','Required S2S parameter is missing.','S2S request missing flow-specific parameter.','Add the required S2S parameters from the S2S integration guide.'],
    ['E907 / E1620','Wrong payment method selected','Payment method does not match enforced method.','User selected a different mode than configured, or request has wrong pg/bankcode.','Pass the correct payment method parameters and validate frontend payment selection.'],
    ['E908','International cards not allowed','Card is not allowed for this merchant/payment route.','International card attempted while international card processing is disabled.','Enable international cards if required or show a clear customer message.'],
    ['E306','Card authentication failure','Card authentication could not be completed.','Invalid OTP, expired OTP, 3DS issue, user abandoned authentication.','Ask customer to retry; if repeated, use another card or payment method.'],
    ['E300','Card failed 3D authentication as 3 D Secure signatures did not match','3DS authentication failed.','Incorrect OTP/password or issuer authentication issue.','Let customer retry authentication or use another card.'],
    ['E1000','3-D secure authentication failed.','3DS authentication failed.','User failed challenge, challenge timed out, issuer unavailable.','Retry with the same payment method only after confirming final transaction status.'],
    ['E317','Payer could not be authenticated','Customer authentication failed.','Issuer/ACS could not authenticate payer.','Show retry option and alternate payment methods.'],
    ['E1670','Card authentication failed at the bank due to invalid CVV','Card security code validation failed.','Wrong CVV/CVC entered by customer.','Ask customer to re-enter card details or use another card.'],
    ['E348','Transaction declined by the issuer','Issuer declined the payment.','Issuer risk rules, card limits, insufficient funds, card disabled for online payments.','Show issuer-decline message and suggest another payment method.'],
    ['E307','Transaction declined with do not honor','Issuer declined without a specific reason.','Issuer risk, card restrictions, transaction pattern, bank policy.','Ask customer to contact issuer or use a different payment method.'],
    ['E500','Bank failed to authenticate the customer','Bank could not authenticate the customer.','Bank authentication page failed, user abandoned OTP, issuer timeout.','Ask customer to retry after verifying final status.'],
    ['E308','Transaction Failed at bank end.','Bank reported a failed transaction.','Bank declined or could not process the payment.','Treat as failed unless later webhook/status check confirms success.'],
    ['E227','Transaction is Pending','Final status is not yet available.','Bank/PSP processing is delayed, corporate banking approval pending, or callback not received.','Do not mark failed immediately. Poll Transaction Detail APIs and listen for webhooks.'],
    ['E507','Transaction Expired','Customer did not complete the payment in time.','Checkout session, bank page, OTP, or UPI collect expired.','Create a new payment attempt with a new txnid.'],
    ['E231','Transaction was marked as dropped','Payment flow was abandoned or dropped.','User closed browser, redirect failed, or no bank response.','Verify final status before retrying. If not successful, create a new attempt.'],
    ['E408','Transaction failed. Page expired due to no user input.','Checkout or bank page timed out.','Customer took too long or abandoned payment.','Ask customer to retry with a new transaction.'],
    ['E1206','Transaction interrupted by pressing back button','Customer interrupted the redirect flow.','Customer used browser back button or closed page.','Treat as failed/dropped only after status verification.'],
    ['E4292','PSP TIME-OUT','PSP did not respond in time.','PSP/UPI app/bank timeout.','Keep order pending and reconcile through status API/webhook before retry.'],
    ['E4177','REMITTER BANK NOT AVAILABLE','Customer bank was unavailable.','Bank downtime or connectivity issue.','Suggest alternate bank/payment method.'],
    ['E1654','Route to merchant unavailable','PayU could not route the transaction.','Gateway route unavailable or misconfigured.','Retry later or contact PayU if persistent for the same route.'],
    ['E4526','Record not found against given parameters','Status/refund/verification lookup did not find a matching transaction.','Wrong txnid, wrong mihpayid, wrong key, environment mismatch.','Confirm identifiers and environment before retrying lookup.'],
    ['E1500','Retry not allowed','Retry is not permitted for this transaction.','Payment network or PayU state does not allow retry on same request.','Create a new payment attempt with a new txnid after confirming final status.'],
    ['Webhook delivery 4xx','HTTP/2 405, 401 Unauthorized, 403 Forbidden, 404 Not Found','Merchant endpoint rejected PayU webhook.','Wrong URL, unsupported method, authentication rule, WAF/firewall, route not deployed.','Accept PayU POST requests, allow PayU IPs, and support form-encoded payloads.'],
    ['Webhook delivery 5xx','500 Internal Server Error, 502, 503, 504','Merchant endpoint failed while processing webhook.','Handler exception, timeout, dependency outage, database failure.','Make webhook processing idempotent, fast, and queue-backed. Return 2xx after durable receipt.'],
    ['E4530','Mandate request failed as start date is less than current date','SI/mandate start date is invalid.','startDate is in the past or timezone conversion changed date.','Send a valid future/current mandate start date as per API requirements.'],
    ['E4531','Mandate request failed as end date is less than start date','SI/mandate end date is invalid.','End date is before start date.','Validate mandate date range before creating mandate.'],
    ['E4112','Transaction failed as mandate and transaction amount is different','Debit amount does not match mandate rules.','Debit exceeds fixed mandate amount or does not follow billing rule.','Align debit amount with mandate amount and billing rule.'],
    ['E4105','Transaction failed due to recurring sequence mismatch','Recurring sequence is invalid.','Wrong sequence number or parallel debit issue.','Use the correct recurring sequence and avoid concurrent debits for the same mandate.'],
    ['E4271','Mandate request declined by the customer','Customer declined the mandate.','Customer rejected UPI Autopay/SI approval.','Ask customer to create a new mandate.'],
    ['E4272','Transaction declined due to timeout at Issuer/Acquirer end','Mandate authentication timed out.','Issuer/acquirer did not respond.','Keep status pending until verified; retry mandate setup if final status is failed.'],
    ['E4278','Transaction failed as mandate setup failed from customer bank','Mandate setup failed at customer bank.','Bank rejected mandate or account does not support it.','Ask customer to use another account/payment method.'],
    ['E4682','Recurrence Payment is in progress','Recurring debit is already being processed.','Duplicate or parallel recurring request.','Do not retry immediately. Wait for final status or webhook.'],
    ['E4683','Recurrence Payment is already completed','Recurring debit was already completed.','Duplicate debit request for the same cycle.','Treat as duplicate and reconcile existing debit.']
  ]}
  placeholder="Search errors"
/>
