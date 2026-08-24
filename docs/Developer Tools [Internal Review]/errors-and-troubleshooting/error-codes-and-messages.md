---
title: Error Codes and Messages
excerpt: >-
  PayU payment error codes, messages, developer-friendly descriptions, possible
  causes, and fixes.
deprecated: false
hidden: true
metadata:
  robots: index
---
Use this table to map PayU response fields to the action your integration should take.

For the complete reference, see [Error Codes](ref:error-codes). For transaction-stage diagnostics, see [Transaction Stages - Error References on Field7 & Field8](ref:transaction-stages-error-references-field7-field8).

<AdvancedTable
  data={[
    {
      'error_code_type': 'E000',
      'error_message_as_returned_by_payu': 'No Error',
      'description': 'Transaction completed successfully.',
      'possible_cause': 'Payment was authorized and captured successfully.',
      'recommended_fix': 'Mark the order as paid only after validating response hash and matching txnid, amount, and status.'
    },
    {
      'error_code_type': 'E700',
      'error_message_as_returned_by_payu': 'Validation of secure hash failed',
      'description': 'PayU could not validate the request hash.',
      'possible_cause': 'Wrong hash sequence, wrong salt, missing delimiters, value mismatch, environment key/salt mismatch.',
      'recommended_fix': 'Recreate the hash server-side using the exact posted values and correct salt. See Generate Hash (PayU Hosted).'
    },
    {
      'error_code_type': 'SECURE_HASH_FAILURE',
      'error_message_as_returned_by_payu': 'Validation of secure hash failed',
      'description': 'Security validation failed.',
      'possible_cause': 'Request was tampered with or hash was generated from normalized values that differ from submitted values.',
      'recommended_fix': 'Log the raw hash string server-side and compare it with the posted request. Never send salt to frontend.'
    },
    {
      'error_code_type': 'E1101',
      'error_message_as_returned_by_payu': 'Transaction failed due to invalid params shared by the merchant',
      'description': 'PayU rejected the transaction request because one or more parameters are invalid.',
      'possible_cause': 'Invalid amount, txnid, productinfo, surl, furl, pg, bankcode, or unsupported combination of fields.',
      'recommended_fix': 'Validate request payload before submitting to PayU. Confirm mandatory fields for your integration type.'
    },
    {
      'error_code_type': 'E4156 / E4373',
      'error_message_as_returned_by_payu': 'VALIDATION ERROR',
      'description': 'Generic validation failure.',
      'possible_cause': 'Missing or malformed parameter, invalid field length, invalid enum, unsupported value.',
      'recommended_fix': 'Compare request with API reference and check raw request logs.'
    },
    {
      'error_code_type': 'Missing parameter',
      'error_message_as_returned_by_payu': 'One or more mandatory parameters are missing',
      'description': 'Required fields were not sent.',
      'possible_cause': 'Frontend did not pass data to backend, backend omitted empty fields, or request content type is incorrect.',
      'recommended_fix': 'Send all mandatory fields and include empty UDF delimiters in the hash string.'
    },
    {
      'error_code_type': 'Invalid amount',
      'error_message_as_returned_by_payu': 'Invalid amount / Please enter valid amount',
      'description': 'Amount is missing or not accepted.',
      'possible_cause': 'Amount is blank, zero, negative, contains commas, has unsupported decimal precision, or differs between hash and request.',
      'recommended_fix': 'Send amount as a decimal string, for example 10.00, and use the exact same value in hash generation.'
    },
    {
      'error_code_type': 'Duplicate txnid',
      'error_message_as_returned_by_payu': 'Duplicate Transaction ID / THE REQUEST IS DUPLICATE',
      'description': 'The transaction ID was already used.',
      'possible_cause': 'Retrying a new payment attempt with the same txnid, or reusing order ID as transaction ID without uniqueness.',
      'recommended_fix': 'Generate a unique txnid for every new payment attempt. Use Transaction Detail APIs for status checks instead of re-posting the same transaction.'
    },
    {
      'error_code_type': 'E4150',
      'error_message_as_returned_by_payu': 'Transaction declined due to duplicate request',
      'description': 'PayU or bank detected a duplicate request.',
      'possible_cause': 'Same transaction submitted multiple times in a short window.',
      'recommended_fix': 'Disable double-submit on frontend and enforce idempotency on backend.'
    },
    {
      'error_code_type': 'E1201',
      'error_message_as_returned_by_payu': 'You are not authorized to do this transaction.',
      'description': 'Merchant is not authorized for requested service.',
      'possible_cause': 'Payment mode, route, S2S flow, currency, or feature not enabled for merchant.',
      'recommended_fix': 'Confirm merchant configuration in Dashboard or with PayU Integration Team.'
    },
    {
      'error_code_type': 'E1631',
      'error_message_as_returned_by_payu': 'Merchant Validation Failed',
      'description': 'Merchant-level validation failed.',
      'possible_cause': 'Invalid merchant key, inactive merchant, invalid bank MID/terminal, or disabled configuration.',
      'recommended_fix': 'Verify key/salt, environment, MID status, and payment mode enablement.'
    },
    {
      'error_code_type': 'E1621',
      'error_message_as_returned_by_payu': 'Merchant does not have access to S2S flow',
      'description': 'S2S flow is not enabled for the merchant.',
      'possible_cause': 'Attempting S2S APIs without enablement.',
      'recommended_fix': 'Request S2S enablement and confirm production/test credentials.'
    },
    {
      'error_code_type': 'E1622',
      'error_message_as_returned_by_payu': 'S2S flow not enabled on selected payment gateway',
      'description': 'Selected payment gateway does not support enabled S2S route.',
      'possible_cause': 'Wrong pg/bankcode or payment mode not configured for S2S.',
      'recommended_fix': 'Use an enabled payment method or update gateway configuration.'
    },
    {
      'error_code_type': 'E1615',
      'error_message_as_returned_by_payu': 'txn_s2s_flow missing parameter',
      'description': 'Required S2S parameter is missing.',
      'possible_cause': 'S2S request missing flow-specific parameter.',
      'recommended_fix': 'Add the required S2S parameters from the S2S integration guide.'
    },
    {
      'error_code_type': 'E907 / E1620',
      'error_message_as_returned_by_payu': 'Wrong payment method selected',
      'description': 'Payment method does not match enforced method.',
      'possible_cause': 'User selected a different mode than configured, or request has wrong pg/bankcode.',
      'recommended_fix': 'Pass the correct payment method parameters and validate frontend payment selection.'
    },
    {
      'error_code_type': 'E908',
      'error_message_as_returned_by_payu': 'International cards not allowed',
      'description': 'Card is not allowed for this merchant/payment route.',
      'possible_cause': 'International card attempted while international card processing is disabled.',
      'recommended_fix': 'Enable international cards if required or show a clear customer message.'
    },
    {
      'error_code_type': 'E306',
      'error_message_as_returned_by_payu': 'Card authentication failure',
      'description': 'Card authentication could not be completed.',
      'possible_cause': 'Invalid OTP, expired OTP, 3DS issue, user abandoned authentication.',
      'recommended_fix': 'Ask customer to retry; if repeated, use another card or payment method.'
    },
    {
      'error_code_type': 'E300',
      'error_message_as_returned_by_payu': 'Card failed 3D authentication as 3 D Secure signatures did not match',
      'description': '3DS authentication failed.',
      'possible_cause': 'Incorrect OTP/password or issuer authentication issue.',
      'recommended_fix': 'Let customer retry authentication or use another card.'
    },
    {
      'error_code_type': 'E1000',
      'error_message_as_returned_by_payu': '3-D secure authentication failed.',
      'description': '3DS authentication failed.',
      'possible_cause': 'User failed challenge, challenge timed out, issuer unavailable.',
      'recommended_fix': 'Retry with the same payment method only after confirming final transaction status.'
    },
    {
      'error_code_type': 'E317',
      'error_message_as_returned_by_payu': 'Payer could not be authenticated',
      'description': 'Customer authentication failed.',
      'possible_cause': 'Issuer/ACS could not authenticate payer.',
      'recommended_fix': 'Show retry option and alternate payment methods.'
    },
    {
      'error_code_type': 'E1670',
      'error_message_as_returned_by_payu': 'Card authentication failed at the bank due to invalid CVV',
      'description': 'Card security code validation failed.',
      'possible_cause': 'Wrong CVV/CVC entered by customer.',
      'recommended_fix': 'Ask customer to re-enter card details or use another card.'
    },
    {
      'error_code_type': 'E348',
      'error_message_as_returned_by_payu': 'Transaction declined by the issuer',
      'description': 'Issuer declined the payment.',
      'possible_cause': 'Issuer risk rules, card limits, insufficient funds, card disabled for online payments.',
      'recommended_fix': 'Show issuer-decline message and suggest another payment method.'
    },
    {
      'error_code_type': 'E307',
      'error_message_as_returned_by_payu': 'Transaction declined with do not honor',
      'description': 'Issuer declined without a specific reason.',
      'possible_cause': 'Issuer risk, card restrictions, transaction pattern, bank policy.',
      'recommended_fix': 'Ask customer to contact issuer or use a different payment method.'
    },
    {
      'error_code_type': 'E500',
      'error_message_as_returned_by_payu': 'Bank failed to authenticate the customer',
      'description': 'Bank could not authenticate the customer.',
      'possible_cause': 'Bank authentication page failed, user abandoned OTP, issuer timeout.',
      'recommended_fix': 'Ask customer to retry after verifying final status.'
    },
    {
      'error_code_type': 'E308',
      'error_message_as_returned_by_payu': 'Transaction Failed at bank end.',
      'description': 'Bank reported a failed transaction.',
      'possible_cause': 'Bank declined or could not process the payment.',
      'recommended_fix': 'Treat as failed unless later webhook/status check confirms success.'
    },
    {
      'error_code_type': 'E227',
      'error_message_as_returned_by_payu': 'Transaction is Pending',
      'description': 'Final status is not yet available.',
      'possible_cause': 'Bank/PSP processing is delayed, corporate banking approval pending, or callback not received.',
      'recommended_fix': 'Do not mark failed immediately. Poll Transaction Detail APIs and listen for webhooks.'
    },
    {
      'error_code_type': 'E507',
      'error_message_as_returned_by_payu': 'Transaction Expired',
      'description': 'Customer did not complete the payment in time.',
      'possible_cause': 'Checkout session, bank page, OTP, or UPI collect expired.',
      'recommended_fix': 'Create a new payment attempt with a new txnid.'
    },
    {
      'error_code_type': 'E231',
      'error_message_as_returned_by_payu': 'Transaction was marked as dropped',
      'description': 'Payment flow was abandoned or dropped.',
      'possible_cause': 'User closed browser, redirect failed, or no bank response.',
      'recommended_fix': 'Verify final status before retrying. If not successful, create a new attempt.'
    },
    {
      'error_code_type': 'E408',
      'error_message_as_returned_by_payu': 'Transaction failed. Page expired due to no user input.',
      'description': 'Checkout or bank page timed out.',
      'possible_cause': 'Customer took too long or abandoned payment.',
      'recommended_fix': 'Ask customer to retry with a new transaction.'
    },
    {
      'error_code_type': 'E1206',
      'error_message_as_returned_by_payu': 'Transaction interrupted by pressing back button',
      'description': 'Customer interrupted the redirect flow.',
      'possible_cause': 'Customer used browser back button or closed page.',
      'recommended_fix': 'Treat as failed/dropped only after status verification.'
    },
    {
      'error_code_type': 'E4292',
      'error_message_as_returned_by_payu': 'PSP TIME-OUT',
      'description': 'PSP did not respond in time.',
      'possible_cause': 'PSP/UPI app/bank timeout.',
      'recommended_fix': 'Keep order pending and reconcile through status API/webhook before retry.'
    },
    {
      'error_code_type': 'E4177',
      'error_message_as_returned_by_payu': 'REMITTER BANK NOT AVAILABLE',
      'description': 'Customer bank was unavailable.',
      'possible_cause': 'Bank downtime or connectivity issue.',
      'recommended_fix': 'Suggest alternate bank/payment method.'
    },
    {
      'error_code_type': 'E1654',
      'error_message_as_returned_by_payu': 'Route to merchant unavailable',
      'description': 'PayU could not route the transaction.',
      'possible_cause': 'Gateway route unavailable or misconfigured.',
      'recommended_fix': 'Retry later or contact PayU if persistent for the same route.'
    },
    {
      'error_code_type': 'E4526',
      'error_message_as_returned_by_payu': 'Record not found against given parameters',
      'description': 'Status/refund/verification lookup did not find a matching transaction.',
      'possible_cause': 'Wrong txnid, wrong mihpayid, wrong key, environment mismatch.',
      'recommended_fix': 'Confirm identifiers and environment before retrying lookup.'
    },
    {
      'error_code_type': 'E1500',
      'error_message_as_returned_by_payu': 'Retry not allowed',
      'description': 'Retry is not permitted for this transaction.',
      'possible_cause': 'Payment network or PayU state does not allow retry on same request.',
      'recommended_fix': 'Create a new payment attempt with a new txnid after confirming final status.'
    },
    {
      'error_code_type': 'Webhook delivery 4xx',
      'error_message_as_returned_by_payu': 'HTTP/2 405, 401 Unauthorized, 403 Forbidden, 404 Not Found',
      'description': 'Merchant endpoint rejected PayU webhook.',
      'possible_cause': 'Wrong URL, unsupported method, authentication rule, WAF/firewall, route not deployed.',
      'recommended_fix': 'Accept PayU POST requests, allow PayU IPs, and support form-encoded payloads.'
    },
    {
      'error_code_type': 'Webhook delivery 5xx',
      'error_message_as_returned_by_payu': '500 Internal Server Error, 502, 503, 504',
      'description': 'Merchant endpoint failed while processing webhook.',
      'possible_cause': 'Handler exception, timeout, dependency outage, database failure.',
      'recommended_fix': 'Make webhook processing idempotent, fast, and queue-backed. Return 2xx after durable receipt.'
    },
    {
      'error_code_type': 'E4530',
      'error_message_as_returned_by_payu': 'Mandate request failed as start date is less than current date',
      'description': 'SI/mandate start date is invalid.',
      'possible_cause': 'startDate is in the past or timezone conversion changed date.',
      'recommended_fix': 'Send a valid future/current mandate start date as per API requirements.'
    },
    {
      'error_code_type': 'E4531',
      'error_message_as_returned_by_payu': 'Mandate request failed as end date is less than start date',
      'description': 'SI/mandate end date is invalid.',
      'possible_cause': 'End date is before start date.',
      'recommended_fix': 'Validate mandate date range before creating mandate.'
    },
    {
      'error_code_type': 'E4112',
      'error_message_as_returned_by_payu': 'Transaction failed as mandate and transaction amount is different',
      'description': 'Debit amount does not match mandate rules.',
      'possible_cause': 'Debit exceeds fixed mandate amount or does not follow billing rule.',
      'recommended_fix': 'Align debit amount with mandate amount and billing rule.'
    },
    {
      'error_code_type': 'E4105',
      'error_message_as_returned_by_payu': 'Transaction failed due to recurring sequence mismatch',
      'description': 'Recurring sequence is invalid.',
      'possible_cause': 'Wrong sequence number or parallel debit issue.',
      'recommended_fix': 'Use the correct recurring sequence and avoid concurrent debits for the same mandate.'
    },
    {
      'error_code_type': 'E4271',
      'error_message_as_returned_by_payu': 'Mandate request declined by the customer',
      'description': 'Customer declined the mandate.',
      'possible_cause': 'Customer rejected UPI Autopay/SI approval.',
      'recommended_fix': 'Ask customer to create a new mandate.'
    },
    {
      'error_code_type': 'E4272',
      'error_message_as_returned_by_payu': 'Transaction declined due to timeout at Issuer/Acquirer end',
      'description': 'Mandate authentication timed out.',
      'possible_cause': 'Issuer/acquirer did not respond.',
      'recommended_fix': 'Keep status pending until verified; retry mandate setup if final status is failed.'
    },
    {
      'error_code_type': 'E4278',
      'error_message_as_returned_by_payu': 'Transaction failed as mandate setup failed from customer bank',
      'description': 'Mandate setup failed at customer bank.',
      'possible_cause': 'Bank rejected mandate or account does not support it.',
      'recommended_fix': 'Ask customer to use another account/payment method.'
    },
    {
      'error_code_type': 'E4682',
      'error_message_as_returned_by_payu': 'Recurrence Payment is in progress',
      'description': 'Recurring debit is already being processed.',
      'possible_cause': 'Duplicate or parallel recurring request.',
      'recommended_fix': 'Do not retry immediately. Wait for final status or webhook.'
    },
    {
      'error_code_type': 'E4683',
      'error_message_as_returned_by_payu': 'Recurrence Payment is already completed',
      'description': 'Recurring debit was already completed.',
      'possible_cause': 'Duplicate debit request for the same cycle.',
      'recommended_fix': 'Treat as duplicate and reconcile existing debit.'
    }
  ]}
/>
