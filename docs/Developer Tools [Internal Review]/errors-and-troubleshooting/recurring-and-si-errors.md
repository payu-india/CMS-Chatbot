---
title: Recurring and SI Errors
excerpt: >-
  Troubleshoot PayU Standing Instruction, UPI Autopay, mandate, and recurring
  debit errors.
deprecated: false
hidden: true
metadata:
  robots: index
---
Recurring and Standing Instruction (SI) errors happen during mandate registration, mandate modification, pre-debit processing, or recurring debit execution.

## Common Recurring and SI Errors

These are some of the common recurring and SI errors.

<Accordion title="Errors and Fixes" icon="far fa-wrench-simple">
  <AdvancedTable
    data={[
      {
        'error_code': '`E4530`',
        'what_it_means': 'SI/mandate start date is invalid.',
        'recommended_fix': 'Send a valid future/current mandate start date as per API requirements.'
      },
      {
        'error_code': '`E4531`',
        'what_it_means': 'SI/mandate end date is invalid.',
        'recommended_fix': 'Validate mandate date range before creating mandate.'
      },
      {
        'error_code': '`E4112`',
        'what_it_means': 'Debit amount does not match mandate rules.',
        'recommended_fix': 'Align debit amount with mandate amount and billing rule.'
      },
      {
        'error_code': '`E4105`',
        'what_it_means': 'Recurring sequence is invalid.',
        'recommended_fix': 'Use the correct recurring sequence and avoid concurrent debits for the same mandate.'
      },
      {
        'error_code': '`E4271`',
        'what_it_means': 'Customer declined the mandate.',
        'recommended_fix': 'Ask customer to create a new mandate.'
      },
      {
        'error_code': '`E4272`',
        'what_it_means': 'Mandate authentication timed out.',
        'recommended_fix': 'Keep status pending until verified; retry mandate setup if final status is failed.'
      },
      {
        'error_code': '`E4278`',
        'what_it_means': 'Mandate setup failed at customer bank.',
        'recommended_fix': 'Ask customer to use another account/payment method.'
      },
      {
        'error_code': '`E4682`',
        'what_it_means': 'Recurring debit is already being processed.',
        'recommended_fix': 'Do not retry immediately. Wait for final status or webhook.'
      },
      {
        'error_code': '`E4683`',
        'what_it_means': 'Recurring debit was already completed.',
        'recommended_fix': 'Treat as duplicate and reconcile existing debit.'
      }
    ]}
  />
</Accordion>

## When these Errors Occur

<Accordion title="Error Causes" icon="far fa-list-timeline">
  Recurring/SI failures commonly appear when:

  - A customer rejects the mandate in the bank or UPI app.
  - Mandate dates are invalid.
  - Debit amount does not match the mandate rule.
  - Multiple recurring debits are sent for the same cycle.
  - Issuer, PSP, or customer bank times out during mandate authentication.
</Accordion>

## Troubleshooting

Now that we know the error causes, let's see how how to troubleshoot.

<Accordion title="Troubleshooting Steps" icon="far fa-arrow-down-1-9">
  1. Identify whether the failure happened during mandate setup, mandate modification, or debit execution.
  2. Check `authpayuid` or `authPayuId`, `requestId`, `debitDate`, `amount`, billing rule, and billing cycle.
  3. Confirm mandate start and end dates in the expected timezone.
  4. Confirm the debit amount follows the approved mandate rule.
  5. Do not send parallel debits for the same mandate cycle.
  6. Treat `in progress` responses as pending until the final webhook/status is available.
  7. For customer-declined mandates, ask the customer to create a new mandate.
</Accordion>

<Callout icon="📘" theme="info">
  ### **Common Mistake:**

  Reusing the same recurring request while the first debit is still in progress can create duplicate or sequence-mismatch errors.
</Callout>

# Recurring, SI, and Mandate Errors

These are some of the common recurring and SI errors.

### Authentication 3DS Errors

<Accordion title="Errors and Fixes" icon="far fa-wrench-simple">
  <AdvancedTable
    data={[
      {
        'error_code': '`3DS_CHALLENGE_POSITIVE`',
        'what_it_means': 'Challenge successful - Occurs when the Access Control Server returns a successful authentication response after the customer completes the challenge step.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`3DS_METHOD_ERROR`',
        'what_it_means': '3DS2 Method failure - Signifies a technical failure during the 3DS2 method process. This could be due to incorrect configuration, communication errors with the directory server, or invalid parameters.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`AUCERROR`',
        'what_it_means': 'Authentication error - Occurs when there is a technical error during the authentication call, such as OTP submission failure, timeout, or request issues.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`AUCINVALID`',
        'what_it_means': 'Authentication internal failure - Indicates that the authentication process completed but failed due to an internal system error such as parsing issues or service failure.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`AUTHPOSITIVE`',
        'what_it_means': 'Authorization successful - Indicates that both authentication and authorization were successful. The payment is approved and funds are reserved.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`VERERROR`',
        'what_it_means': 'Verification error - Occurs when a technical issue prevents successful verification with the bank or wallet, such as API errors or network issues.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`VERPOSITIVE`',
        'what_it_means': 'Verification success - Occurs when a verification call confirms that the transaction was successful. Typically used when reconciling or validating transaction status.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`Unauthorised person digital sign received on agreement`',
        'what_it_means': 'Unauthorised person digital sign received on agreement - Re-upload service agreement with Authorised person digital sign.',
        'recommended_fix': 'Re-upload service agreement with Authorised person digital sign.'
      },
      {
        'error_code': '`3DS_CHALLENGE_ERROR`',
        'what_it_means': 'When received authentication No response from ACS on our TermURL - Occurs when PayU does not receive any response from the ACS at the termination URL after the challenge was initiated. This could be due to timeout, network issues, or the customer closing the browser during authentica...',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`3DS_CHALLENGE_POSITIVE`',
        'what_it_means': 'When received authentication response from ACS on our TermURL - Occurs when the Access Control Server (ACS) returns a positive authentication response to PayU\'s termination URL after the cardholder successfully completes the challenge (e.g., enters correct OTP or completes biometr...',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`3DS_METHOD_ERROR`',
        'what_it_means': 'When 3DS2 Method Failure - Signifies a technical failure during the 3DS2 method process. This could be due to incorrect 3DS configurations, communication errors with the Directory Server, or invalid 3DS parameters being passed.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`AUCERROR`',
        'what_it_means': 'When there is an error is authentication call (ex. Submit otp) - Occurs when there\'s a technical error during an authentication action, such as when submitting an OTP. This could be due to invalid OTP format, transmission errors, or timeout issues in the authentication service.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`AUTHERROR`',
        'what_it_means': 'When there is an error is authentication call (ex. Submit otp) - Indicates a technical error occurred during the authorization process. This could be due to gateway timeouts, network issues with the issuing bank, or internal processing errors in the authorization service.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`AUTHNEGATIVE`',
        'what_it_means': 'Authentication was successful but subsequent authorization call failed. - Occurs when cardholder authentication succeeds, but the subsequent authorization request to the issuing bank is declined. This could be due to insufficient funds, spending limits, or other bank-side restrictions.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`AUTHPOSITIVE`',
        'what_it_means': 'Authentication with subsequent authorization call was successful. - Indicates that both the authentication (3DS) and subsequent authorization (payment approval) processes were successful. The payment has been approved by the issuing bank and funds have been reserved for the transaction.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`VERERROR`',
        'what_it_means': 'Technical error with the verification call - Occurs when a technical error prevents PayU from successfully making or processing a verification call to the bank/wallet. This could be due to API errors, network issues, or invalid parameters in the verification req...',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      }
    ]}
  />
</Accordion>

### Mandate Recurring Errors

<Accordion title="Errors and Fixes" icon="far fa-wrench-simple">
  <AdvancedTable
    data={[
      {
        'error_code': '`E4510`',
        'what_it_means': 'Mandatory Param Missing for Token txn store_card_token',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4510`',
        'what_it_means': 'Mandatory Param Missing for Token txn user_credentials',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4510`',
        'what_it_means': 'Mandatory Param Missing for Token txn ccexpyr',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4510`',
        'what_it_means': 'Mandatory Param Missing trmerchantid',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4510`',
        'what_it_means': 'Mandatory Param Missing for Token txn ccexpmon',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4510`',
        'what_it_means': 'Mandatory Param Missing last4digits',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4510`',
        'what_it_means': 'Mandatory Param Missing for AltId txn last4digits',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4510`',
        'what_it_means': 'Mandatory Param Missing tavv',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4512`',
        'what_it_means': 'Transaction details not present at bank\'s end - Merchant TranId is not available',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4530`',
        'what_it_means': 'Mandate request failed as start date is less than current date - Validity start date should not be less than current date',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4531`',
        'what_it_means': 'Mandate request failed as end date is less than start date - Validity end date should not be less than validity start date',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4532`',
        'what_it_means': 'Mandate request not created',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4533`',
        'what_it_means': 'No active mandates found - No Approved Mandates are available',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4535`',
        'what_it_means': 'Transaction failed due to amount mismatch error - Mandate amounts mis-matched',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4536`',
        'what_it_means': 'Transaction failed as execution amount is higher than mandate created amount - Execution amount exceeded to Mandate approved amount',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4607`',
        'what_it_means': 'Mandate Request Approved',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4679`',
        'what_it_means': 'Modification request already initiated - Mandate Update Request already initiated for Same UMN',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4680`',
        'what_it_means': 'No Mandate data found to Modify',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4682`',
        'what_it_means': 'Recurrence Payment is in progress',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4683`',
        'what_it_means': 'Recurrence Payment is already completed',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      }
    ]}
  />
</Accordion>

### UPI Errors

<Accordion title="Errors and Fixes" icon="far fa-wrench-simple">
  <AdvancedTable
    data={[
      {
        'error_code': '`E4006`',
        'what_it_means': 'PAYEES NOT PRESENT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4007`',
        'what_it_means': 'PAYEE NOT PRESENT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4017`',
        'what_it_means': 'PAYER/PAYEE.DEVICE MUST BE PRESENT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4018`',
        'what_it_means': 'PAYER/PAYEE. DEVICE.TAGS MUST BE PRESENT PAYER/PAYEE.TAG.DEVICE .NAME/VALUE MUST BE PRESENT - PAYER/PAYEE. DEVICE.TAGS MUST BE PRESENT PAYER/PAYEE.TAG.DEVICE.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4026`',
        'what_it_means': 'PAYER.INFO MUST BE PRESENT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4028`',
        'what_it_means': 'PAYER/PAYEE.INFO MUST BE PRESENT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4029`',
        'what_it_means': 'PAYER/PAYEE .INFO.IDENTITY MUST BE PRESENT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4030`',
        'what_it_means': 'PAYER/PAYEE.INFO.IDENTITY.TYPE MUST BE PRESENT MINLENGTH 1 MAXLENGTH 20 - PAYER/PAYEE.INFO.IDENTITY.TYPE MUST BE PRESENT MINLENGTH 1 MAXLE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4031`',
        'what_it_means': 'PAYER/PAYEE .INFO.IDENTITY VERIFIEDNAME MUST BE PRESENT ALPHANUMERIC MINLENGTH 1 MAXLENGTH 99 - PAYER/PAYEE .INFO.IDENTITY VERIFIEDNAME MUST BE PRESENT ALPHANUM',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4032`',
        'what_it_means': 'PAYER/PAYEE .INFO.RATING WHITELISTED MUST BE PRESENT MINLENGTH 1 MAXLENGTH 5 - PAYER/PAYEE .INFO.RATING WHITELISTED MUST BE PRESENT MINLENGTH 1',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4033`',
        'what_it_means': 'DUPLICATE BLOCKFUND FOR MANDATE REQUEST',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4034`',
        'what_it_means': 'REVOKE MANDATE AFTER THE REMITTER UNBLOCKED THE AMOUNT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4035`',
        'what_it_means': 'DEBIT AMOUNT IS NOT BLOCKED FOR THE CUSTOMER',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4036`',
        'what_it_means': 'DEBIT AMOUNT GREATER THAN BLOCKED AMOUNT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4037`',
        'what_it_means': 'Transaction failed due to funds blocked for mandate in customer\'s account - ADEQUATE FUNDS NOT AVAILABLE IN THE ACCOUNT BECAUSE FUNDS HAVE B',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4038`',
        'what_it_means': 'PAYEE PSP DOES NOT SUPPORT VERSION 2',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4039`',
        'what_it_means': 'BANK/PSP IS NOT SUPPORTING VERSION 2',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4041`',
        'what_it_means': 'Transaction failed due to internal exception at server/cbs end at customer\'s bank - UNABLE TO PROCESS DUE TO INTERNAL EXCEPTION AT SERVER/CBS/ETC ON',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4046`',
        'what_it_means': 'PAYEE AMOUNT CUR MUST BE CONSISTENT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4049`',
        'what_it_means': 'ONE OR MORE PAYEE AMOUNT IS MISSING',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4051`',
        'what_it_means': 'MORE THAN ONE PAYEE AMOUNT IS MISSING',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4053`',
        'what_it_means': 'Transaction failed due to mandate not present - MANDATE NOT PRESENT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4054`',
        'what_it_means': 'MANDATE.NAME ALPHANUMERIC; MINLENGTH 1 , MAXLENGTH 99',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4055`',
        'what_it_means': 'MANDATE UMN MUST BE PRESENT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4056`',
        'what_it_means': 'MANDATE.UMN SHOULD NOT BE PRESENT FOR PAYEE INITIATED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4058`',
        'what_it_means': 'MANDATE.TXNID AND TXN.ID MUST BE SAME',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4059`',
        'what_it_means': 'MANDATE.UMN MUST BE PRESENT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4060`',
        'what_it_means': 'MANDATE.UMN MUST BE PRESENT, LENGTH 32',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4061`',
        'what_it_means': 'MANDATE.TS MUST BE PRESENT AND SHOULD BE IN ISO_ZONE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4062`',
        'what_it_means': 'MANDATE.REVOKEABLE MUST BE PRESENT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4063`',
        'what_it_means': 'RECURRENCE PATTERN AS WELL AS FOR PAYER INITIATED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4064`',
        'what_it_means': 'MANDATE.VALIDITY MUST BE PRESENT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4065`',
        'what_it_means': 'MANDATE.VALIDITY.START MUST BE PRESENT, DATE FORMAT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4066`',
        'what_it_means': 'MANDATE.VALIDITY.END MUST BE PRESENT, DATE FORMAT DDMMYYYY, END DATE MUST BE GREATER THAN TODAY\'S DATE - MANDATE.VALIDITY.END MUST BE PRESENT, DATE FORMAT DDMMYYYY, END',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4067`',
        'what_it_means': 'MANDATE.AMOUNT MUST BE PRESENT, VALUE AND RULE SHOULD NOT BE EMPTY - MANDATE.AMOUNT MUST BE PRESENT, VALUE AND RULE SHOULD NOT BE EMP',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4068`',
        'what_it_means': 'MANDATE.AMOUNT.RULE MUST BE PRESENT, RULE MUST BE EXACT/MAX',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4069`',
        'what_it_means': 'MANDATE.RECURRENCE MUST BE PRESENT,MANDATE.RECURRENCE.PATTERN MUST BE ONETIME OR DAILYOR WEEKLY - MANDATE.RECURRENCE MUST BE PRESENT,MANDATE.RECURRENCE.PATTERN MU',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4070`',
        'what_it_means': 'MANDATE.RECURRENCE.RULE MUST BE PRESENT,MANDATE.RECURRENCE.RULE.TYPE MUST BE AFTER OR ON OR BEFORE - MANDATE.RECURRENCE.RULE MUST BE PRESENT,MANDATE.RECURRENCE.RULE.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4071`',
        'what_it_means': 'MANDATE.RECURRENCE.RULE MUST BE PRESENT,MANDATE.RECURRENCE.RULE.VALUE IN BETWEEN 1 TO 7 ONLY WHEN MANDATE.RECURRENCE.PATTERN IS WEEKLY - MANDATE.RECURRENCE.RULE MUST BE PRESENT,MANDATE.RECURRENCE.RULE.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4072`',
        'what_it_means': 'MANDATE.RECURRENCE.RULE NOT APPLICABLE FOR MANDATE.RECURRENCE.PATTERN ONETIME/DAILY/WEEKLY/FORTNIGHTLY/MONTHLY /BIMONTHLY/QUARTERLY/HALFYEARLY /YEARLY/ASPRESENTED - MANDATE.RECURRENCE.RULE NOT APPLICABLE FOR MANDATE.RECURRENCE.PA',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4073`',
        'what_it_means': 'MANDATE RECURRENCE PATTERN.BLOCK=N IS ALLOWED ONLY IF THE PURPOSE CODE=14 - MANDATE RECURRENCE PATTERN.BLOCK=N IS ALLOWED ONLY IF THE PURPOS',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4074`',
        'what_it_means': 'MANDATE RECURRENCE PATTERN. REVOKABLE=Y, ONLY Y IS ALLOWED IF THE PURPOSE CODE=14 - MANDATE RECURRENCE PATTERN. REVOKABLE=Y, ONLY Y IS ALLOWED IF TH',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4075`',
        'what_it_means': 'MANDATE.UMN CANNOT BE GENERATED BY PAYEE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4076`',
        'what_it_means': 'GLOBAL ADDRESS NOT SUPPORTED IN MANDATE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4077`',
        'what_it_means': 'MANDATE REQUEST IS DECLINED BY MERCHANT (PAYEE)',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4078`',
        'what_it_means': 'MANDATE TAG DIFFERS FROM ORIGINAL REQUEST',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4079`',
        'what_it_means': 'MANDATE.NAME DIFFERS FROM ORIGINAL REQUEST',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4080`',
        'what_it_means': 'MANDATE.TXNID DIFFERS FROM ORIGINAL REQUEST',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4081`',
        'what_it_means': 'MANDATE.UMN DIFFERS FROM ORIGINAL REQUEST',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4082`',
        'what_it_means': 'MANDATE TS DIFFERS FROM ORIGINAL REQUEST',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4083`',
        'what_it_means': 'MANDATE REVOKEABLE DIFFERS FROM ORIGINAL REQUEST',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4084`',
        'what_it_means': 'MANDATE.SHARETOPAYEE DIFFERS FROM ORIGINAL REQUEST',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4085`',
        'what_it_means': 'MANDATE.BLOCKFUND DIFFERS FROM ORIGINAL REQUEST',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4086`',
        'what_it_means': 'MANDATE.TYPE DIFFERS FROM ORIGINAL REQUEST,MANDATE.AMOUNT DIFFERS FROM ORIGINAL REQUEST - MANDATE.TYPE DIFFERS FROM ORIGINAL REQUEST,MANDATE.AMOUNT DIFFER',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4087`',
        'what_it_means': 'MANDATE.RECURRENCE.PATTERN DIFFERS FROM ORIGINAL REQUEST',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4090`',
        'what_it_means': 'MANDATE.AMOUNT CAN ONLY BE UPDATED IF PURPOSE=01',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4091`',
        'what_it_means': 'RECURRENCE PATTERN IS ALWAYS ONETIME IF PURPOSE=01',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4094`',
        'what_it_means': 'PAYER PSP DOES NOT SUPPORT VERSION MANDATE 2.1',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4095`',
        'what_it_means': 'PAYEE PSP DOES NOT SUPPORT VERSION MANDATE 2.1',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4096`',
        'what_it_means': 'REMITTER BANK DOES NOT SUPPORT VERSION MANDATE 2.1',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4097`',
        'what_it_means': 'BENIFICIARY BANK DOES NOT SUPPORTS VERSION MANDATE 2.1',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4098`',
        'what_it_means': 'MANDATE.VALIDITY DIFFERS FROM ORIGINAL REQUEST',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4099`',
        'what_it_means': 'MANDATE.VALIDITY.START DIFFERS FROM ORIGINAL REQUEST',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4100`',
        'what_it_means': 'MANDATE.VALIDITY.END DIFFERS FROM ORIGINAL REQUEST',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4101`',
        'what_it_means': 'Transaction failed due to technical issue at Issuer/Acquirer end - NO ORIGINAL REQUEST FOUND DURING DEBIT/CREDIT BD',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4105`',
        'what_it_means': 'Transaction failed due to recurring sequence mismatch - SEQNUM MISMATCH (PAYER PSP)',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4106`',
        'what_it_means': 'Transaction failed due to recurrence pattern, value and amount rule mismatch - RECURRENCE PATTERN AND VALUE MISMATCH (PAYER)',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4108`',
        'what_it_means': 'Transaction failed as mandate is paused by the user - MANDATE IS PAUSED BY USER',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4109`',
        'what_it_means': 'Transaction failed as mandate is already honoured - MANDATE IS ALREADY HONOURED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4110`',
        'what_it_means': 'Transaction failed as mandate is revoked by the user - MANDATE HAS BEEN REVOKED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4111`',
        'what_it_means': 'Transaction failed as mandate is expired - MANDATE HAS EXPIRED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4112`',
        'what_it_means': 'Transaction failed as mandate and transaction amount is different - TXN AMOUNT DIFFERS FROM MANDATE AMOUNT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4113`',
        'what_it_means': 'Transaction failed as payee details are not correct in mandate - PAYEE VPA IS INCORRECT (PAYER)',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4114`',
        'what_it_means': 'Transaction failed as umn details doesn\'t exist at customer\'s end - UMN DOES NOT EXIST (PAYER)',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4115`',
        'what_it_means': 'Transaction failed as mandate request limit is breached - MANDATE REQUEST LIMIT HAS BREACHED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4116`',
        'what_it_means': 'Transaction failed as mandate amount is higher than allowed by customer\'s application - MANDATE DEBIT IS BEYOND PSP SPECIFIED AMOUNT CAP',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4117`',
        'what_it_means': 'Transaction failed as payer details are not correct in mandate - PAYER VPA IS INCORRECT (PAYER)',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4118`',
        'what_it_means': 'Transaction failed due to duplicate mandate request - DUPLICATE MANDATE REQUEST BD',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4119`',
        'what_it_means': 'Revoke is not allowed for this mandate - THIS MANDATE IS NON REVOKEABLE BD',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4120`',
        'what_it_means': 'Modification not allowed by merchant for payer initiated mandate - PAYER INITIATED MANDATE CANNOT BE MODIFIED BY PAYEE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4121`',
        'what_it_means': 'Transaction failed as mandate is not allowed to be created on this merchant - MANDATE CANNOT BE CREATED ON THIS VPA (PAYER)',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4124`',
        'what_it_means': 'Modification request declined by the customer - MANDATE MODIFY REQUEST IS DECLINED (PAYER)',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4127`',
        'what_it_means': 'Transaction declined as payee is a non-merchant - MANDATE DECLINED AS PAYEE IS NON-MERCHANT (PAYER)',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4128`',
        'what_it_means': 'Transaction failed as umn details doesn\'t exist at acquiring bank\'s end - UMN DOES NOT EXIST (PAYEE)',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4130`',
        'what_it_means': 'Modification not allowed by payer for merchant initiated mandate - PAYEE INITIATED MANDATE CANNOT BE MODIFIED BY PAYER',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4131`',
        'what_it_means': 'Modification request declined by merchant - MANDATE MODIFICATION DECLINED BY MERCHANT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4132`',
        'what_it_means': 'PAYER NOT PRESENT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4135`',
        'what_it_means': 'PAYER.SEQNUM NUMERIC MINLENGTH 1 MAXLENGTH 3',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4136`',
        'what_it_means': 'PAYER.TYPE MUST BE PRESENT/VALID',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4141`',
        'what_it_means': 'Transaction failed as partial debit request timeout at customer\'s bank - PARTIAL DEBIT REVERSAL TIMEOUT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4142`',
        'what_it_means': 'Debit failed due to timeout at customer\'s bank - DEBIT REVERSAL TIMEOUT(REVERSAL)',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4152`',
        'what_it_means': 'Transaction failed due to debit limit on customer exceeded - NET DEBIT CAP IS EXCEEDED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4158`',
        'what_it_means': 'AUTHNEGATIVE - 96 \| System malfunction \| We encountered a problem with Rupay processor: Session expired for this transaction',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4158`',
        'what_it_means': 'AUTHNEGATIVE - 96 \| System malfunction \| We encountered a problem with Rupay processor: PREVIOUSLY AUTHORIZED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4158`',
        'what_it_means': 'AUTHNEGATIVE - 96 \| Session expired for this transaction',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4160`',
        'what_it_means': 'CREDENTIALS IS NOT PRESENT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4177`',
        'what_it_means': 'Debit failed due to technical issue at customer\'s bank - REMITTER BANK NOT AVAILABLE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4179`',
        'what_it_means': 'Transaction failed as debit failed from the customer\'s account - DEBIT HAS BEEN FAILED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4182`',
        'what_it_means': 'Transaction failed as debit reversal failed in the customer\'s account - DEBIT REVERT HAS BEEN FAILED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4189`',
        'what_it_means': 'IMPS PROCESSING FAILED IN UPI',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4194`',
        'what_it_means': 'FORM PROCESSING HAS BEEN FAILED IN UPI',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4196`',
        'what_it_means': 'REQUEST DEBIT IS NOT FOUND',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4197`',
        'what_it_means': 'Transaction failed as original transaction details not found during status check - TRANSACTION ID IS NOT PRESENT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4198`',
        'what_it_means': 'REQUEST MESSAGE ID IS NOT PRESENT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4199`',
        'what_it_means': 'IFSC IS NOT PRESENT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4202`',
        'what_it_means': 'PSP REQUEST PAY DEBIT ACKNOWLEDGEMENT NOT RECEIVED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4250`',
        'what_it_means': 'HEADER & URL VERSION IS MISMATCHED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4251`',
        'what_it_means': 'VERSION/TAGS SENT NOT SUPPORTED BY PSP/BANK',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4252`',
        'what_it_means': 'PAYER/PAYEE PSP,HEADER OR URL VERSION MISMATCHED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4253`',
        'what_it_means': 'PAYER/PAYEE PSP,REQUEST & RESPONSE HEADER VERSION MISMATCH',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4254`',
        'what_it_means': 'PAYER/PAYEE PSP,VERSION/TAGS NOT SUPPORTED BY PSP/BANK',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4255`',
        'what_it_means': 'URL VERSION MISMATCHED (NEG ACK FOR RESPAUTH. ERROR CODE U18 IN FINAL RESPPAY.) - URL VERSION MISMATCHED (NEG ACK FOR RESPAUTH. ERROR CODE U18 IN',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4256`',
        'what_it_means': 'REMITTER BANK,REQUEST & RESPONSE HEADER VERSION MISMATCH',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4257`',
        'what_it_means': 'REMITTER BANK,HEADER OR URL VERSION MISMATCHED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4258`',
        'what_it_means': 'REMITTER BANK,VERSION/TAGS SENT NOT SUPPORTED BY BANK',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4259`',
        'what_it_means': 'Transaction failed due to internal exception at server/cbs end at acquirer\'s bank - UNABLE TO PROCESS DUE TO INTERNAL EXCEPTION AT SERVER/CBS/ETC ON',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4260`',
        'what_it_means': 'BENIFICIARY BANK,REQUEST & RESPONSE HEADER VERSION MISMATCH',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4261`',
        'what_it_means': 'BENIFICIARY BANK,HEADER OR URL VERSION MISMATCHED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4262`',
        'what_it_means': 'BENIFICIARY BANK,VERSION/TAGS SENT NOT SUPPORTED BY BANK',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4263`',
        'what_it_means': 'OTHER BANK/PSP IS NOT SUPPORTED IN 2 VERSION',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4264`',
        'what_it_means': 'PAYER PSP DOES NOT SUPPORTS VERSION',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4265`',
        'what_it_means': 'REMITTER BANK DOES NOT SUPPORT VERSION',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4271`',
        'what_it_means': 'Mandate request declined by the customer - RESPAUTHMANDATE DECLINED BY PSP',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4272`',
        'what_it_means': 'Transaction declined due to timeout at Issuer/Acquirer end - RESPAUTHMANDATE TIMEOUT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4273`',
        'what_it_means': 'Transaction failed due to mandate request expired - RESPAUTHMANDATE EXPIRED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4274`',
        'what_it_means': 'REQAUTHMANDATE NEGATIVE ACK RECEIVED FROM PSP',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4275`',
        'what_it_means': 'RESPAUTHMANDATE NEGATIVE ACK SENT FROM UPI TO PSP',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4276`',
        'what_it_means': 'ORIGINAL REQAUTHMANDATE NOT FOUND',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4277`',
        'what_it_means': 'REQMANDATE ACK NOT RECEIVED FROM REMITTER BANK',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4278`',
        'what_it_means': 'Transaction failed as mandate setup failed from customer\'s bank - RESPMANDATE DECLINED BY REMITTER BANK',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4279`',
        'what_it_means': 'Transaction declined due to timeout at customer\'s bank - RESPMANDATE TIMEOUT AT REMITTER END',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4280`',
        'what_it_means': 'REQMANDATE NEGATIVE ACK RECEIVED FROM REMITTER',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4281`',
        'what_it_means': 'BANK TD RESPMANDATE NEGATIVE ACK SENT FROM UPI TO REMITTER BANK',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4282`',
        'what_it_means': 'ORIGINAL REQMANDATE NOT FOUND',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4283`',
        'what_it_means': 'RESPMANDATE ACK NOT RECEIVED FROM PAYER',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4284`',
        'what_it_means': 'REQMANDATECONFIRMATION ACK NOT RECEIVED FROM PAYER',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4290`',
        'what_it_means': 'Mandate not supported by customer\'s bank - REMITTER BANK NOT REGISTERED (MANDATE)',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4291`',
        'what_it_means': 'Mandate not supported by acquirer\'s bank - BENEFICIARY BANK NOT REGISTERED (MANDATE)',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4293`',
        'what_it_means': 'Transaction declined as mandate amount limit exceeded - MANDATE AMOUNT CAP IS EXCEEDED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4298`',
        'what_it_means': 'PIN Cred Block is missing (txns > 2000)',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4299`',
        'what_it_means': 'PIN Cred Block is missing (txns \< 2000 and Seq No = 1)',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4301`',
        'what_it_means': 'Transaction failed as revoke should be allowed for recurring mandate - Purpose Code=14, Revocable= N ( Revokable tag must always be Y f',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4313`',
        'what_it_means': 'MANDATE REGISTRATION NOT ALLOWED FOR CC PF PPF ACT (BANK\'S POLICY) - MANDATE REGISTRATION NOT ALLOWED FOR CC PF PPF ACT (BANKNULLS PO',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4319`',
        'what_it_means': 'DUPLICATE MANDATE REQUEST FOR SAME ITEM',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4327`',
        'what_it_means': 'MANDATE.RECURRENCE RULE TAG SHOULD NOT BE PRESENTREMITTER BANK NOT CERTIFIED FOR 2.7 - MANDATE.RECURRENCE RULE TAG SHOULD NOT BE PRESENTREMITTER BANK N',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4328`',
        'what_it_means': 'MANDATE.RECURRENCE RULE TAG SHOULD NOT BE PRESENTBENEFICIARY BANK NOT CERTIFIED FOR 2.7 - MANDATE.RECURRENCE RULE TAG SHOULD NOT BE PRESENTBENEFICIARY BAN',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4329`',
        'what_it_means': 'MANDATE RECURRENCE RULE TAG SHOULD NOT BE PRESENTPAYER PSP NOT CERTIFIED FOR 2.7 - MANDATE RECURRENCE RULE TAG SHOULD NOT BE PRESENTPAYER PSP NOT C',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4330`',
        'what_it_means': 'MANDATE RECURRENCE RULE TAG SHOULD NOT BE PRESENT PAYEE PSP NOT CERTIFIED FOR 2.7 - MANDATE RECURRENCE RULE TAG SHOULD NOT BE PRESENT PAYEE PSP NOT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4932`',
        'what_it_means': 'Get_cryptogram_failure - Mandatory Param Missing for Token txn store_card_token',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E4935`',
        'what_it_means': 'Cryptogram missing - Blank or null card token crypto',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E1611 - The transaction cannot be processed as discount given exceeds the allowed limit. If money is debited from your account then it will be auto refunded. Please try again',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4031 - PAYER/PAYEE .INFO.IDENTITY VERIFIEDNAME MUST BE PRESENT ALPHANUMERIC MINLENGTH 1 MAXLENGTH 99',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4037 - Transaction failed due to funds blocked for mandate in customer\'s account',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4106 - Transaction failed due to recurrence pattern, value and amount rule mismatch',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4108 - Transaction failed as mandate is paused by the user',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4109 - Transaction failed as mandate is already honoured',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4110 - Transaction failed as mandate is revoked by the user',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4111 - Transaction failed as mandate is expired',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4114 - Transaction failed as umn details does not exist at customer\'s end',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4115 - Transaction failed as mandate request limit is breached',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4116 - Transaction failed as mandate amount is higher than allowed by customer\'s application',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4118 - Transaction failed due to duplicate mandate request',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4121 - Transaction failed as mandate is not allowed to be created on this merchant',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4142 - Debit failed due to timeout at customer\'s bank',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4152 - Transaction failed due to debit limit on customer exceeded',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4177 - Debit failed due to technical issue at customer\'s bank',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4179 - Transaction failed as debit failed from the customer\'s account',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4263 - OTHER BANK/PSP IS NOT SUPPORTED IN 2 VERSION',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4271 - Mandate request declined by the customer',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4273 - Transaction failed due to mandate request expired',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4278 - Transaction failed as mandate setup failed from customer\'s bank',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4283 - RESPMANDATE ACK NOT RECEIVED FROM PAYER',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4284 - REQMANDATECONFIRMATION ACK NOT RECEIVED FROM PAYER',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4293 - Transaction declined as mandate amount limit exceeded',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4299 - PIN Cred Block is missing (txns \< 2000 and Seq No = 1)',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4313 - MANDATE REGISTRATION NOT ALLOWED FOR CC PF PPF ACT (BANK\'S POLICY)',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4314 - Transaction failed as debit not allowed',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4319 - DUPLICATE MANDATE REQUEST FOR SAME ITEM',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E4803 - Transaction failed as amount should always be positive',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPI`',
        'what_it_means': 'E507 - Credit card used in Debit Card PG.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPICC`',
        'what_it_means': 'E4142 - Debit failed due to timeout at customer\'s bank',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPICC`',
        'what_it_means': 'E4152 - Transaction failed due to debit limit on customer exceeded',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPICC`',
        'what_it_means': 'E4177 - Debit failed due to technical issue at customer\'s bank',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPICC`',
        'what_it_means': 'E4179 - Transaction failed as debit failed from the customer\'s account',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPICC`',
        'what_it_means': 'E4803 - Transaction failed as amount should always be positive',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPIPPI`',
        'what_it_means': 'E4152 - Transaction failed due to debit limit on customer exceeded',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`UPIPPI`',
        'what_it_means': 'E4803 - Transaction failed as amount should always be positive',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      }
    ]}
  />
</Accordion>

### Card Token Errors

<Accordion title="Errors and Fixes" icon="far fa-wrench-simple">
  <AdvancedTable
    data={[
      {
        'error_code': '`ALT_ID_PROV_ERROR`',
        'what_it_means': 'Alt Provisioning API Failure - Occurs when the alternative ID generation API encounters a technical failure. This typically happens due to network issues, system unavailability, or invalid request parameters. The system cannot generate token or alt...',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`ALT_ID_PROV_NEGATIVE`',
        'what_it_means': 'Alt Provisioning Failure - Indicates that while the API itself worked correctly, the attempt to provision an alternative ID was unsuccessful. This may be due to invalid card details, issuer restrictions, or the card being ineligible for tokeniz...',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EA08`',
        'what_it_means': 'Alt ID Provisioning Failed - Alt ID Provisioning Failed due to incorrect Card Details',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EA081`',
        'what_it_means': 'ALT_ID_PROV_ERROR - EA081\|The network token provision request contained data that could not be verified',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EA081`',
        'what_it_means': 'ALT_ID_PROV_ERROR - EA081\|One or more fields in the request are either missing or does not have correct value.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EA081`',
        'what_it_means': 'ALT_ID_PROV_ERROR - EA081\|Invalid / Missing Field :: card expiry',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EA09`',
        'what_it_means': 'Alt ID Provisioning Failed - Merchant not onboarded, please contact PayU Support',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`ALT_ID_PROV_ERROR`',
        'what_it_means': 'Alt Provisioning API Failure - Occurs when the alternative ID generation API encounters a technical failure. This typically happens due to network issues, system unavailability, or invalid request parameters. The system cannot generate token/altern...',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      }
    ]}
  />
</Accordion>

### Transaction Flow Errors

<Accordion title="Errors and Fixes" icon="far fa-wrench-simple">
  <AdvancedTable
    data={[
      {
        'error_code': '`AUTOREFUND`',
        'what_it_means': 'Auto refund triggered - Indicates that the transaction was automatically refunded due to predefined system conditions such as duplicate payment, timeout, or missing confirmation.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`REDIRECT`',
        'what_it_means': 'Redirect initiated to bank or merchant - Indicates that either a redirect URL is provided to the merchant in seamless flow, or the customer is redirected to the bank or wallet page in non-seamless flow. This is a transitional state in the payment journey.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`REDIRECT`',
        'what_it_means': 'S2S redirect initiated - Occurs when a server-to-server interim response is sent to the merchant or customer, indicating that a redirect is required to complete the payment flow. This is a transitional state.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`TXNPENDING`',
        'what_it_means': 'Pending corporate approval - Applicable for corporate banking flows where the maker has initiated the transaction but it is pending approval from the checker before processing.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`TXNPOSITIVE`',
        'what_it_means': 'Successful bank callback - Indicates that the bank or wallet has sent a successful callback confirming that the payment was completed and funds were debited from the customer account.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`INTNEGATIVE`',
        'what_it_means': 'When wrong IBIBO code is used - Indicates that an incorrect IBIBO code (internal payment method identifier) was used in the transaction request. This usually happens when there\'s a mismatch between the payment method selected and the code sent in th...',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`REDIRECT`',
        'what_it_means': 'For seamless link to redirect posted to merchant For non seamless users the user was redirected to the bank page - A status indicating that either: 1) In seamless integration, a redirect URL has been generated and provided to the merchant to forward to the customer, or 2) In non-seamless integration, the customer has been automati...',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`REDIRECT`',
        'what_it_means': 'Whenever PayU S2S interim response sent to Merchant or Customer - Occurs when a server-to-server (S2S) interim response is sent from PayU to either the merchant system or customer browser, indicating that the flow requires a redirect to complete the payment process. This is a transi...',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`TXNERROR`',
        'what_it_means': 'Callback not received or technical error \ - Null Response received',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`TXNPOSITIVE`',
        'what_it_means': 'Callback received from the bank - Positive identification - Indicates that the bank or wallet provider has sent a positive callback to PayU confirming that the payment was successful. The funds have been debited from the customer\'s account and the transaction has been approved...',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      }
    ]}
  />
</Accordion>

### System Errors

<Accordion title="Errors and Fixes" icon="far fa-wrench-simple">
  <AdvancedTable
    data={[
      {
        'error_code': '`EX017`',
        'what_it_means': 'Payment gateway id not assigned to merchant payment type - PG_UNASSIGNED_TO_MERCHANT_PAYMENT_TYPE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX020`',
        'what_it_means': 'Inconsistent Transaction Status in database - INCONSISTENCY_IN_TRANSACTION_STATUS',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX021`',
        'what_it_means': 'The risk_category for this merchant hasn - RISK_CATEGORY_MISSING',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX022`',
        'what_it_means': 'PayuId not attached to Transaction Class ? - PAYUID_MISSING',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX027`',
        'what_it_means': 'Empty previous transaction id - TRANSACTIONID_EMPTY',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX032`',
        'what_it_means': 'Cancel Error: Mandatory column missing. Mandatory columns are: \ ? \ - CANCEL_ERROR_MANDATORY_COLUMN',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX034`',
        'what_it_means': 'Refund Error: Mandatory column missing. Mandatory columns are: \ ? \ - REFUND_ERROR_MANDATORY_COLUMN',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX036`',
        'what_it_means': 'Captured Error: Mandatory column missing. Mandatory columns are: \ ? \ - CAPTURE_ERROR_MANDATORY_COLUMN',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX038`',
        'what_it_means': 'Reconciliation Error: Mandatory column missing. Mandatory columns are: \ ? \ - RECONCILIATION_ERROR_MANDATORY_COLUMN',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX042`',
        'what_it_means': 'Invalid Invoice ID - INVOICE_INVALID',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX054`',
        'what_it_means': 'Base merchant id not posted from the paisa request for payuId ? - BASE_MERCHANT_ID_MISSING',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX055`',
        'what_it_means': 'Base payu id not posted from the paisa request for payuId ? - BASE_PAYU_ID_MISSING',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX059`',
        'what_it_means': 'Object can not be saved to database. Table name not mentioned - OBJECT_UNSAVED_TABLENAME_MISSING',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX060`',
        'what_it_means': 'Object can not be saved to database. Identifier value missing - OBJECT_UNSAVED_IDENTIFIER_MISSING',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX064`',
        'what_it_means': 'Missing forward action - MISSING_FORWARD_ACTION',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX068`',
        'what_it_means': 'No fields specified in adminViewer - MISSING_ADMINVIEWER_FIELDS',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX070`',
        'what_it_means': 'The ? request parameter must be set - HTTPREQUEST_PARAM_UNSET',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX071`',
        'what_it_means': 'Problem Building WURFL Repository: ? - WURFL_REPOSITORY_PROBLEM',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX072`',
        'what_it_means': 'There is no device with ID [?] in the loaded WURFL Data - DEVICE_MISSING_IN_WURFL_DATA',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX086`',
        'what_it_means': 'Card bin is not present - CARD_BIN_NOT_PRESENT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX090`',
        'what_it_means': 'Payu id or token missing - PAYUID_MISSING_TOKEN_MISS',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX104`',
        'what_it_means': 'Reporting Error: Mandatory column missing. Mandatory columns are: \ ? \ - REPORTING_ERROR_MANDATORY_COL_MISSING',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX105`',
        'what_it_means': 'Upload Error: Mandatory column missing. Mandatory columns are: \ ? \ - UPLOAD_ERROR_MANDATORY_COL_MISSING',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX107`',
        'what_it_means': 'Refund Reference Number Upload Error: Mandatory column missing. Mandatory columns are: \ ? \ - REFUND_UPLOAD_ERROR_MANDATORY_COL_MISS',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX108`',
        'what_it_means': 'This \ txnid\ has been used previously or was successfully captured. ? - DUPLICATE_ORDER_ID',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX114`',
        'what_it_means': 'Merchant key missing in Request - MERCHANT_KEY_MISSING',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX115`',
        'what_it_means': 'The \ key\ ? value which you are using in the transaction request - is currently inactive. ? - PAYMENTFLOW_INACTIVE_MERCHANT',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX123`',
        'what_it_means': 'Mandatory parameter payuId missing. - MANDATORY_PARAMETER_PAYUID_MISSING',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX124`',
        'what_it_means': 'One or more mandatory parameters are missing in the transaction request. ? - MANDATORY_PARAMETER_TXNID_MISSING',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX128`',
        'what_it_means': 'This Invoice has expired - INVOICE_EXPIRED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX130`',
        'what_it_means': 'Error: Mandatory column missing. Mandatory columns are: \ ? \ - ERROR_MANDATORY_FILE_MISSING',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX146`',
        'what_it_means': '? table details are missing in lib/utility/RiskConstants.php - INVALID_TABLENAME',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX147`',
        'what_it_means': 'You seem to be using an incorrect \ key\ or \ salt\ value. ? - INCORRECT_MERCHANT_KEY',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX157`',
        'what_it_means': 'INVALID_CHECK_ALLOWED_BANKS_DC_IN_SI',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX212`',
        'what_it_means': 'INVOICE_GMV_LIMIT_REACHED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX227`',
        'what_it_means': 'This currency is not supported on your account. Please reach out to your KAM for activation - INACTIVE_CURRENCY_FOR_SINGLE_MID',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX304`',
        'what_it_means': 'MULTIPLE_SAME_SKU_ID_IN_SINGLE_CART',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX306`',
        'what_it_means': 'Wrong Api version selected for split txn - API_VERSION_INCORRECT_SPLIT_TXN',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX307`',
        'what_it_means': 'One or more mandatory parameters are missing in the transaction request for split txn - MANDATORY_PARAMS_MISSING_SPLIT_TXN',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`EX404`',
        'what_it_means': 'Invalid Buyer Type Business - INVALID_BUYER_TYPE_BUSINESS',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      }
    ]}
  />
</Accordion>

### General Errors

<Accordion title="Errors and Fixes" icon="far fa-wrench-simple">
  <AdvancedTable
    data={[
      {
        'error_code': '`E2416`',
        'what_it_means': 'One or more parameters is missing in the API.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E2418`',
        'what_it_means': 'Transaction cannot Processed. Previous bill is overdue',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`89`',
        'what_it_means': 'E9226 - TID_NOT_ PRESENT_ON_HOST',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': '3DS_CHALLENGE_POSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': '3DS_CHALLENGE_POSITIVE - Marking transaction as dropped - CSW',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': '3DS_CHALLENGE_POSITIVE - UNKNOWN_ERROR',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': '3DS_METHOD_POSITIVE - No Error',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': '3DS_METHOD_POSITIVE - 61 \| Exceeds withdrawal amount limit(s) / Withdrawal amount limit exc \| Decline - The card has reached the credit limit.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': '3DS_METHOD_POSITIVE - AUTHORIZED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': '3DS_METHOD_POSITIVE - UNKNOWN_ERROR',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': '3DS_METHOD_POSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': '3DS_METHOD_POSITIVE - Marking transaction as dropped - CSW',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'ACS_REDIRECT - Json processing',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'ALT_ID_PROV_ERROR - EA081\|The network token provision request contained data that could not be verified',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUCNEGATIVE - Session timed out',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUCNEGATIVE - Element missing',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUCPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUTHERROR - Cancel api failed with response decision as DECLINED and reason code',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUTHERROR - Cancel api failed with response decision as and reason code',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUTHNEGATIVE - Warning: 490 Missing or Invalid Merchant Category Code',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUTHNEGATIVE - 10024 \| duplicate request, another txn already processing with same details',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUTHPOSITIVE - AUTHORIZED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUTHPOSITIVE - 00 \| Function performed error-free',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUTHPOSITIVE - NO_ERROR',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUTHPOSITIVE - 00 \| success',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUTHPOSITIVE - No Error',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUTHPOSITIVE - 0 \| No Error',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUTHPOSITIVE - 00',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUTHPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUTHPOSITIVE - 0 \| Transaction Completed',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUTHPOSITIVE - 00 \| Successful approval/completion or that V.I.P. PIN verification is valid',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUTHPOSITIVE - 00 \|',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUTHPOSITIVE - 00 \| Approved or completed successfully',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUTHPOSITIVE - AUTHENTICATION_SUCCESSFUL \| 100',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUTHPOSITIVE - 0 \|',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUTHPOSITIVE - APPROVED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUTHPOSITIVE - Transaction successful',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'AUTHPOSITIVE - AUTHORISED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'EVPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E000`',
        'what_it_means': 'EVPOSITIVE - 00 \| Approved or completed successfully',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1003`',
        'what_it_means': '3DS_METHOD_POSITIVE - AUTHENTICATION_FAILED\|Encountered a Payer Authentication problem. Payer could not be authenticated. \| CONSUMER_AUTHENTICATION_FAILED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1101`',
        'what_it_means': 'Mandatory Param Missing for Token txn ccexpmon',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1101`',
        'what_it_means': 'Mandatory Param Missing tavv',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1101`',
        'what_it_means': 'Mandatory Param Missing for Token txn store_card_token',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1101`',
        'what_it_means': 'Mandatory Param Missing for Token txn user_credentials',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1101`',
        'what_it_means': 'AUTHNEGATIVE - 10024 \| duplicate request, another txn already processing with same details',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1101`',
        'what_it_means': 'AUTHPOSITIVE - No Error',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1202`',
        'what_it_means': 'EVPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1205`',
        'what_it_means': '3DS_METHOD_POSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1205`',
        'what_it_means': 'AUCPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1205`',
        'what_it_means': 'EVPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1206`',
        'what_it_means': 'N:ACCU200:User Pressed cancel button',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1206`',
        'what_it_means': '3DS_CHALLENGE_POSITIVE - Marking transaction as dropped - CSW',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1206`',
        'what_it_means': '3DS_METHOD_POSITIVE - Marking transaction as dropped - CSW',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1206`',
        'what_it_means': '3DS_METHOD_POSITIVE - Blc\|0 \| Blc\|SUCCESS',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1206`',
        'what_it_means': '3DS_METHOD_POSITIVE - UNKNOWN_ERROR',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1206`',
        'what_it_means': '3DS_METHOD_POSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1206`',
        'what_it_means': '3DS_METHOD_POSITIVE - Cancel api failed with response decision as and reason code',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1206`',
        'what_it_means': 'AUCPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1206`',
        'what_it_means': 'AUCPOSITIVE - Marking transaction as dropped - CSW',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1206`',
        'what_it_means': 'AUTHNEGATIVE - Cancel api failed with response decision as and reason code',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1206`',
        'what_it_means': 'EVPOSITIVE - GW00201 \| Transaction not found',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1206`',
        'what_it_means': 'EVPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1206`',
        'what_it_means': 'EVPOSITIVE - Marking transaction as dropped - CS',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1206`',
        'what_it_means': 'EVPOSITIVE - Marking transaction as dropped - CSW',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1206`',
        'what_it_means': 'EVPOSITIVE - 0 \| OTP Generated Successfully',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1206`',
        'what_it_means': 'EVPOSITIVE - 62 \| Restricted card',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1206`',
        'what_it_means': 'EVPOSITIVE - 0 \|',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1206`',
        'what_it_means': 'REDIRECT - N:-50822:Processing error while provisioning Guest Checkout Token',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1206`',
        'what_it_means': 'REDIRECT - N:ACCU200:User Pressed cancel button',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1206`',
        'what_it_means': 'Transaction interrupted by pressing back button - REDIRECTED_BY_BACK_BUTTON',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1206`',
        'what_it_means': 'VERERROR - Verification \| failed \| Key encData not present',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1210`',
        'what_it_means': 'Credit card used in Debit Card PG. - BLOCK_CREDIT_CARDS',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1300`',
        'what_it_means': 'Customer has pressed the refresh key during the payment process. - DUPLICATE_SESSION_ID',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1302`',
        'what_it_means': '3DS_METHOD_POSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1302`',
        'what_it_means': '3DS_METHOD_POSITIVE - NOT_ENROLLED_FAILURE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1303`',
        'what_it_means': 'AUCPOSITIVE - AUTHENTICATION_SUCCESSFUL \| 100',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1303`',
        'what_it_means': 'EVPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1501`',
        'what_it_means': 'Transaction amount is less than the minimum amount accepted by issuing bank for processing EMI. - INVALID_MIN_AMOUNT_EMI',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1502`',
        'what_it_means': 'Incorrect request for SI, CC received in drop_category. - INCOMPLETE_SI_REQUEST',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1601`',
        'what_it_means': '3DS_METHOD_POSITIVE - UNKNOWN_ERROR',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1601`',
        'what_it_means': '3DS_METHOD_POSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1602`',
        'what_it_means': '3DS_METHOD_POSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1602`',
        'what_it_means': '3DS_METHOD_POSITIVE - UNKNOWN_ERROR',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1602`',
        'what_it_means': '3DS_METHOD_POSITIVE - 000 \| Blc\|SUCCESS',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1602`',
        'what_it_means': '3DS_METHOD_POSITIVE - Invalid Otp',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1602`',
        'what_it_means': 'EVPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1602`',
        'what_it_means': 'EVPOSITIVE - UNKNOWN_ERROR',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1605`',
        'what_it_means': 'Transaction failed due to customer pressing cancel button. - CANCEL_BUTTON_PRESSED_BY_USER',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1606`',
        'what_it_means': 'Transaction failed due to user pressing refresh button. - PAGE_REFRESHED_BY_USER',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1607`',
        'what_it_means': 'Transaction failed due to user pressing back button. - BACK_BUTTON_PRESSED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1608`',
        'what_it_means': '3DS_METHOD_POSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1608`',
        'what_it_means': 'AUCNEGATIVE - Page parsing Failure',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1611`',
        'what_it_means': '3DS_METHOD_POSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1611`',
        'what_it_means': '3DS_METHOD_POSITIVE - UNKNOWN_ERROR',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1611`',
        'what_it_means': 'AUTHNEGATIVE - Cancel api failed with response decision as and reason code',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1611`',
        'what_it_means': 'EVPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1611`',
        'what_it_means': 'EVPOSITIVE - GW00201 \| Transaction not found',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1615`',
        'what_it_means': 'txn_s2s_flow missing parameter - S2S_PARAMETER_MISSING',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1623`',
        'what_it_means': 'Customer Authentication failed due to incorrect ATM PIN. - Decline - The Pinless Debit card\'s use frequency or maximum amou',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1626`',
        'what_it_means': 'AUTHNEGATIVE - 15062 \| you are using restricted card',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1626`',
        'what_it_means': 'AUTHNEGATIVE - 62 \| Restricted card (for example, in Country Exclusion table)',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1642`',
        'what_it_means': 'AUTHNEGATIVE - 58 \| Transaction not permitted to acquirer/terminal \| Decline - Inactive card or card not authorized for card-not-present transactions.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1642`',
        'what_it_means': 'AUTHNEGATIVE - 57 \| Transaction not permitted to issuer/cardholder \| Decline - Inactive card or card not authorized for card-not-present transactions.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1642`',
        'what_it_means': 'EVPOSITIVE - 57 \| Transaction not permitted to issuer/cardholder',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1644`',
        'what_it_means': 'Empty Otp Received - MISSING_OTP',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1661`',
        'what_it_means': 'ATM PIN daily limit exceeded for this card. Please retry using OTP or any other payment option. - SBI_DI_DAILY_CARD_LIMIT_EXCEEDED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1662`',
        'what_it_means': 'ATM PIN monthly limit exceeded for this card. Please retry using OTP or any other payment option. - SBI_DI_MONTHLY_CARD_LIMIT_EXCEEDED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1700`',
        'what_it_means': 'Term URL is missing in the request - MISSING_TERM_URL',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1703`',
        'what_it_means': 'User Pressed cancel button',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1703`',
        'what_it_means': 'Processing error while provisioning Guest Checkout Token',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1703`',
        'what_it_means': 'Session expired for this transaction',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1703`',
        'what_it_means': 'Error while Processing FIRSTDATA payment',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1703`',
        'what_it_means': 'ACS_REDIRECT - User Pressed cancel button',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1703`',
        'what_it_means': 'ACS_REDIRECT - Session expired for this transaction',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1703`',
        'what_it_means': 'ACS_REDIRECT - Processing error while provisioning Guest Checkout Token',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1703`',
        'what_it_means': 'AUCNEGATIVE - Processing error while provisioning Guest Checkout Token',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1703`',
        'what_it_means': 'AUTHNEGATIVE - Blc\|204 \| Internal Server Error\|domestic/International CardFlag or credit/debit card flag not avalible for pan.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1703`',
        'what_it_means': 'AUTHNEGATIVE - 10004 \| domestic/International CardFlag or credit/debit card flag not avalible for pan.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1703`',
        'what_it_means': 'AUTHNEGATIVE - Blc\|102 \| Blc\|currency parameter is missing or invalid',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1703`',
        'what_it_means': 'AUTHNEGATIVE - Blc\|204 \| Error occured while preparing Auth Request Rounding necessary',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1703`',
        'what_it_means': 'AUTHNEGATIVE - Blc\|102 \| Blc\|cardNo parameter is missing',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1703`',
        'what_it_means': 'REDIRECT - User Pressed cancel button',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1703`',
        'what_it_means': 'REDIRECT - Processing error while provisioning Guest Checkout Token',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1703`',
        'what_it_means': 'REDIRECT - Session expired for this transaction',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1703`',
        'what_it_means': 'REDIRECT - Error while Processing FIRSTDATA payment',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1903`',
        'what_it_means': '3DS_METHOD_POSITIVE - AUTHORIZATION_FAILED_BY_BANK',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1903`',
        'what_it_means': 'AUTHNEGATIVE - FSS00003 \| Only Debit Card Allowed',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1903`',
        'what_it_means': 'AUTHNEGATIVE - 50822 \| Processing error while provisioning Guest Checkout Token',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1903`',
        'what_it_means': 'AUTHNEGATIVE - GW00159 \| Missing card number',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1903`',
        'what_it_means': 'AUTHNEGATIVE - 002 \| Invalid or missing token cryptogram',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1903`',
        'what_it_means': 'AUTHNEGATIVE - Warning: 490 Missing or Invalid Merchant Category Code',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1903`',
        'what_it_means': 'AUTHPOSITIVE - AUTHORIZED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E1909`',
        'what_it_means': 'Error while processing enstage request - ENSTAGE_PROCESSING_ERROR',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E202`',
        'what_it_means': '3DS_METHOD_POSITIVE - AUTHENTICATION_FAILED \| Cardholder did not complete authentication \| Transaction Error',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E202`',
        'what_it_means': 'AUTHNEGATIVE - INVALID_REQUEST \| Missing parameter. Transaction source must be INTERNET or MERCHANT for payments using a scheme token.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E202`',
        'what_it_means': 'VERERROR - Verification \| failed \| Key encData not present',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E204`',
        'what_it_means': '3DS_METHOD_NEGATIVE - Blc\|102 \| Blc\|currency parameter is missing or invalid',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E205`',
        'what_it_means': 'AUTHNEGATIVE - 12001 \| Duplicate transmission',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E205`',
        'what_it_means': 'EVERROR - 50021 \| kindly provide token authentication value if your passing Y in ext10.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E207`',
        'what_it_means': 'AUCNEGATIVE - AUTHENTICATION_MODE_MISSING \| AuthenticationMode not received, please reachout to PayU Support.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E207`',
        'what_it_means': 'AUCNEGATIVE - 50822 \| Processing error while provisioning Guest Checkout Token',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E207`',
        'what_it_means': 'AUCNEGATIVE - SERVER_FAILED \| Cannot ensure consistent access to data. Please try again later.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E207`',
        'what_it_means': 'AUCNEGATIVE - 301 \| threeDSServerTransID',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E207`',
        'what_it_means': 'AUCNEGATIVE - 301 \| dsTransID',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E207`',
        'what_it_means': 'AUTHNEGATIVE - 12 \| Invalid transaction \| Decline - Inactive card or card not authorized for card-not-present transactions.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E210`',
        'what_it_means': 'Authentication failure or there is a delay in processing the transaction. - Error - The request was received, but there was a timeout at the',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E2100`',
        'what_it_means': 'Invalid Request received for processing. - Declined - One or more fields in the request contains invalid da',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E2101`',
        'what_it_means': 'EVPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E214`',
        'what_it_means': '3DS_METHOD_POSITIVE - CURL_CALL_FAILURE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E222`',
        'what_it_means': 'Debit account number is not received in transaction response - NO_DEBIT_ACCOUNT * NUMBER',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E223`',
        'what_it_means': 'Transaction not approved - The order has been rejected by Decision Manager',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'N:-50822:Processing error while provisioning Guest Checkout Token',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'N:ACCU200:User Pressed cancel button',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'N:96:Session expired for this transaction',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': '3DS_CHALLENGE_POSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': '3DS_CHALLENGE_POSITIVE - Marking transaction as dropped - CSW',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': '3DS_CHALLENGE_POSITIVE - UNKNOWN_ERROR',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': '3DS_METHOD_POSITIVE - Marking transaction as dropped - CSW',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': '3DS_METHOD_POSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': '3DS_METHOD_POSITIVE - Invalid Otp',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': '3DS_METHOD_POSITIVE - UNKNOWN_ERROR',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': '3DS_METHOD_POSITIVE - Marking transaction as dropped - CS',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'AUCNEGATIVE - 50822 \| Processing error while provisioning Guest Checkout Token',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'AUCNEGATIVE - Session timed out',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'AUCPOSITIVE - Invalid Otp',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'AUCPOSITIVE - Marking transaction as dropped - CS',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'AUCPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'AUCPOSITIVE - UNKNOWN_ERROR',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'AUTHERROR - Cancel api failed with response decision as and reason code',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'AUTHNEGATIVE - 10024 \| duplicate request, another txn already processing with same details',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'AUTHNEGATIVE - Cancel api failed with response decision as and reason code',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'AUTHPOSITIVE - No Error',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'AUTHPOSITIVE - Transaction successful',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'EVPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'EVPOSITIVE - 0 \|',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'EVPOSITIVE - Marking transaction as dropped - CS',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'EVPOSITIVE - GW00201 \| Transaction not found',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'EVPOSITIVE - 0 \| OTP Generated Successfully',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'EVPOSITIVE - GW00555 \| UNKNOWN',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'EVPOSITIVE - Marking transaction as dropped - CSW',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'EVPOSITIVE - K \| UNKNOWN',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'EVPOSITIVE - GW00462 \| Invalid Tranportal Password.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'EVPOSITIVE - 62 \| Restricted card',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'EVPOSITIVE - UNKNOWN_ERROR',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'EVPOSITIVE - CM900000 \| UNKNOWN',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'REDIRECT - N:-50822:Processing error while provisioning Guest Checkout Token',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'REDIRECT - N:ACCU200:User Pressed cancel button',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E231`',
        'what_it_means': 'VERERROR - Verification \| failed \| Key encData not present',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E232`',
        'what_it_means': '3DS_METHOD_POSITIVE - AUTHENTICATION_ATTEMPTS',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E2407`',
        'what_it_means': 'Missing User details - INVALID_LINK_AND_PAY * REQUEST_RECEIVED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E2409`',
        'what_it_means': 'Transaction amount is more than the maximum amount accepted by issuing bank for processing EMI. - INVALID_MAX_AMOUNT_EMI',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E2502`',
        'what_it_means': 'ACS_REDIRECT - Element missing',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E2502`',
        'what_it_means': 'AUCNEGATIVE - Element missing',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E2502`',
        'what_it_means': 'Payu unable to parse ACS page for native - HEADLESS_ELEMENT_MISSING',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E2503`',
        'what_it_means': '3DS_METHOD_POSITIVE - Session timed out',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E2503`',
        'what_it_means': 'AUCNEGATIVE - Session timed out',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E2503`',
        'what_it_means': 'Late otp submission on Headless - LATE_OTP_SUBMISSSION * ON_HEADLESS',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E303`',
        'what_it_means': 'AUCNEGATIVE - 50822 \| Processing error while provisioning Guest Checkout Token',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E307`',
        'what_it_means': 'EVPOSITIVE - 05 \| Do not honor',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E308`',
        'what_it_means': '3DS_METHOD_POSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E308`',
        'what_it_means': 'EVPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E308`',
        'what_it_means': 'VERERROR - Verification \| failed \| Key encData not present',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E310`',
        'what_it_means': 'Card has been classified as lost and has been blocked. - Pick Up Card',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E312`',
        'what_it_means': 'AUTHERROR - Cancel api failed with response decision as DECLINED and reason code',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E312`',
        'what_it_means': 'AUTHERROR - Cancel api failed with response decision as and reason code',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E312`',
        'what_it_means': 'AUTHNEGATIVE - Cancel api failed with response decision as and reason code',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E317`',
        'what_it_means': '3DS_METHOD_POSITIVE - Card authentication failed',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E330`',
        'what_it_means': 'AUTHNEGATIVE - 15001 \| Some parameters are missing. Please check / contact the merchant',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E330`',
        'what_it_means': 'AUTHNEGATIVE - 15001 \| missing parameter',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E330`',
        'what_it_means': 'EVERROR - 15001 \| Some parameters are missing. Please contact merchant',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E335`',
        'what_it_means': 'AUCNEGATIVE - 987 \| Declined by DS - Transaction is excluded from Attempts Processing',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E335`',
        'what_it_means': 'AUCNEGATIVE - 201 \| A message element required as defined in Table A.1 is missing from the message.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E335`',
        'what_it_means': 'AUCNEGATIVE - 201 \| Required element missing',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E335`',
        'what_it_means': 'AUCNEGATIVE - 403 \| Transient System Failure',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E335`',
        'what_it_means': 'AUCNEGATIVE - Blc\|202 \| Blc\|Invalid threeDSServerTransID, not found in transaction',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E335`',
        'what_it_means': 'AUCNEGATIVE - E0914 \| key not present,key not present',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E335`',
        'what_it_means': 'AUCNEGATIVE - Blc\|202 \| Blc\|SERVER_FAILED::Cannot ensure consistent access to data. Please try again later.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E335`',
        'what_it_means': 'AUTHNEGATIVE - 15096 \| system error/ PREVIOUSLY AUTHORIZED /PREVIOUSLY DECLINED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E335`',
        'what_it_means': 'AUTHNEGATIVE - 15096 \| SYSTEM ERROR or PREVIOUSLY AUTHORIZED or PREVIOUSLY DECLINED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E335`',
        'what_it_means': 'EVERROR - 15096 \| SYSTEM ERROR or PREVIOUSLY AUTHORIZED or PREVIOUSLY DECLINED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E340`',
        'what_it_means': '3DS_METHOD_POSITIVE - Invalid Otp',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E500`',
        'what_it_means': '3DS_METHOD_POSITIVE - Message Received Invalid',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E500`',
        'what_it_means': 'AUCNEGATIVE - Required element missing',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E500`',
        'what_it_means': 'AUCNEGATIVE - Transient system failure',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E500`',
        'what_it_means': 'AUCNEGATIVE - Message Version Number received is not valid for the receiving component.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E500`',
        'what_it_means': 'AUCNEGATIVE - Transient System Failure',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E500`',
        'what_it_means': 'AUCNEGATIVE - Transient system failure.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E500`',
        'what_it_means': 'AUCNEGATIVE - Missing card record.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E500`',
        'what_it_means': 'AUTHNEGATIVE - FSS00003 \| FSS00003-Only Debit Card Allowed.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E500`',
        'what_it_means': 'AUTHNEGATIVE - NPCI01 \| NPCI01 - Missing Parameter tranCtx',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E500`',
        'what_it_means': 'AUTHNEGATIVE - Invalid / Missing Field :: tokenReferenceId \| UNKNOWN',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E500`',
        'what_it_means': 'EVPOSITIVE - UNKNOWN',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E501`',
        'what_it_means': 'PG filtering based on Card SI PGs',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E501`',
        'what_it_means': '3DS_CHALLENGE_POSITIVE - Marking transaction as dropped - CSW',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E501`',
        'what_it_means': '3DS_CHALLENGE_POSITIVE - UNKNOWN_ERROR',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E501`',
        'what_it_means': '3DS_METHOD_POSITIVE - Marking transaction as dropped - CSW',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E501`',
        'what_it_means': '3DS_METHOD_POSITIVE - UNKNOWN_ERROR',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E501`',
        'what_it_means': '3DS_METHOD_POSITIVE - AUTHENTICATION_FAILED\|UNKNOWN_ERROR',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E501`',
        'what_it_means': '3DS_METHOD_POSITIVE - googlepay',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E501`',
        'what_it_means': '3DS_METHOD_POSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E501`',
        'what_it_means': 'AUCPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E501`',
        'what_it_means': 'AUCPOSITIVE - UNKNOWN_ERROR',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E501`',
        'what_it_means': 'AUTHPOSITIVE - 0 \|',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E501`',
        'what_it_means': 'EVPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E501`',
        'what_it_means': 'EVPOSITIVE - 72 \| UNKNOWN_ERROR',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E502`',
        'what_it_means': '3DS_METHOD_POSITIVE - UNKNOWN_ERROR',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E502`',
        'what_it_means': '3DS_METHOD_POSITIVE - 000 \| Blc\|SUCCESS',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E502`',
        'what_it_means': '3DS_METHOD_POSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E502`',
        'what_it_means': 'AUTHNEGATIVE - OTPCAN \| User Pressed Cancel Button',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E502`',
        'what_it_means': 'EVPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E502`',
        'what_it_means': 'EVPOSITIVE - UNKNOWN_ERROR',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E502`',
        'what_it_means': 'EVPOSITIVE - 000 \| Blc\|SUCCESS',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E502`',
        'what_it_means': 'EVPOSITIVE - 0 \| OTP Generated Successfully',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E503`',
        'what_it_means': '3DS_METHOD_POSITIVE - UNKNOWN_ERROR',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E503`',
        'what_it_means': 'AUCPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E503`',
        'what_it_means': 'AUCPOSITIVE - Invalid Otp',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E503`',
        'what_it_means': 'EVPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E504`',
        'what_it_means': 'AUTHNEGATIVE - 94 \| Duplicate Transmission',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E706`',
        'what_it_means': '3DS_METHOD_POSITIVE - 51 \| Insufficient funds/over credit limit / Not sufficient funds',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E706`',
        'what_it_means': 'EVPOSITIVE - 51 \| Insufficient funds/over credit limit / Not sufficient funds',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E710`',
        'what_it_means': 'AUTHNEGATIVE - 55 \| Invalid PIN \| Decline - Inactive card or card not authorized for card-not-present transactions.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E712`',
        'what_it_means': 'The transaction could not be processed due to incomplete data provided at the users end. - Declined - The request is missing one or more fields',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E715`',
        'what_it_means': 'AUTHNEGATIVE - 13 \| Invalid amount \| Invalid amt or Currency conversion field overflow',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E715`',
        'what_it_means': 'AUTHNEGATIVE - 13 \| Invalid amount (currency conversion field overflow) or amount exceeds maximum for card program',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E715`',
        'what_it_means': 'EVPOSITIVE - 13 \| Invalid amount',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E717`',
        'what_it_means': 'AUTHNEGATIVE - 46 \| Closed account \| Decline - Inactive card or card not authorized for card-not-present transactions.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E720`',
        'what_it_means': 'EVPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E800`',
        'what_it_means': 'Transaction failed due to error at the merchant\'s end - PREFERED_GATEWAY_NOT_SET',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E802`',
        'what_it_means': 'EVPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E803`',
        'what_it_means': 'PG filtering based on Pre Auth Allowed PGs for merchant',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E803`',
        'what_it_means': 'PG filtering based on Card SI PGs',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E803`',
        'what_it_means': '3DS_METHOD_POSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E803`',
        'what_it_means': 'PG_NOT_ACTIVATED - No Active PG found for Prepaid Card',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E804`',
        'what_it_means': 'PG filtering based on Card SI PGs',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E804`',
        'what_it_means': '3DS_METHOD_POSITIVE - Disable pg down time handling on UI so marked as bounced.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E804`',
        'what_it_means': '3DS_METHOD_POSITIVE - FILTERED_FOR_MCP',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E804`',
        'what_it_means': '3DS_METHOD_POSITIVE - REMOVED_HEADLESS_PGS',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E908`',
        'what_it_means': 'International cards not allowed - UNKNOWN_BINS_NO_ACTIVE_PG_ASSIGNED',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E909`',
        'what_it_means': '3DS_METHOD_POSITIVE - 61 \| Exceeds withdrawal amount limit(s) / Withdrawal amount limit exc',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E909`',
        'what_it_means': 'EVPOSITIVE - 65 \| Exceeds withdrawal count limit / Withdrawal count limit exceeded',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E909`',
        'what_it_means': 'EVPOSITIVE - 61 \| Exceeds withdrawal amount limit(s) / Withdrawal amount limit exc',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E9226`',
        'what_it_means': 'AUTHNEGATIVE - 89 \| TID not present on host',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E9226`',
        'what_it_means': 'TID not present on host',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`SSER001`',
        'what_it_means': 'EVPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`failed`',
        'what_it_means': '3DS_METHOD_POSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`failed`',
        'what_it_means': 'AUCPOSITIVE',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E310 / response 4`',
        'what_it_means': 'Card has been classified as lost and has been blocked. - Pick Up Card',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E9226 / response 89`',
        'what_it_means': 'TID not present on host',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`Entity ( Individual/proprietor/Pvt ltd etc ) written mismatch with the provided documents`',
        'what_it_means': 'Entity ( Individual/proprietor/Pvt ltd etc ) written mismatch with the provided documents - Re-upload correct document as per your Business Entity.',
        'recommended_fix': 'Re-upload correct document as per your Business Entity.'
      },
      {
        'error_code': '`Entity ( Individual/proprietor/Pvt ltd etc ) written mismatch with the provided documents`',
        'what_it_means': 'Entity ( Individual/proprietor/Pvt ltd etc ) written mismatch with the provided documents - Re-upload the correct document as per the business Entity.',
        'recommended_fix': 'Re-upload the correct document as per the business Entity.'
      },
      {
        'error_code': '`E-sign blocked`',
        'what_it_means': 'Verification incomplete - Complete pending steps',
        'recommended_fix': 'Complete pending steps'
      },
      {
        'error_code': '`File too large`',
        'what_it_means': '> 5 MB - Compress',
        'recommended_fix': 'Compress'
      },
      {
        'error_code': '`-`',
        'what_it_means': 'Capture Request Queued',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`-`',
        'what_it_means': 'Requests limit reached',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`-`',
        'what_it_means': 'Transaction not exists',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`100`',
        'what_it_means': '100 - Capture Request Queued',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`101`',
        'what_it_means': '101',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`102`',
        'what_it_means': '102 - Capture Request Queued',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`106`',
        'what_it_means': '106 - Token already exists.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`108`',
        'what_it_means': '108',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`109`',
        'what_it_means': '109 - Capture failed',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`109`',
        'what_it_means': '109 - Request is already logged',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`111`',
        'what_it_means': '111 - Invalid transaction status',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`116`',
        'what_it_means': '116 - Transaction Not Found',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`120`',
        'what_it_means': '120 - Transaction lock could not be obtained.',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`301`',
        'what_it_means': '301 - Capture already successful for this transaction',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`303`',
        'what_it_means': '303 - Amount greater than maximum capturable amount',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`304`',
        'what_it_means': '304 - Amount less than allowed',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`305`',
        'what_it_means': '305 - Amount more than allowed',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`306`',
        'what_it_means': '306 - Invalid amount tolerance configuration',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`E2015`',
        'what_it_means': 'PG Params are missing. Please contact sales support - Mastercard, Rupay & Visa IDs are missing for the merchant',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`124`',
        'what_it_means': 'Input Data missing - 124',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`236`',
        'what_it_means': 'Refund not possible on this transaction - 236',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`261`',
        'what_it_means': 'Error while processing request - 261',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`262`',
        'what_it_means': 'Error while processing request - 262',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`264`',
        'what_it_means': 'Error while processing request - 264',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      },
      {
        'error_code': '`265`',
        'what_it_means': 'Error while processing request - 265',
        'recommended_fix': 'Validate mandate/SI dates, amount, sequence, and customer approval state; reconcile through webhook or status API before retrying.'
      }
    ]}
  />
</Accordion>

### SDK Integration Errors

<Accordion title="Errors and Fixes" icon="far fa-wrench-simple">
  <AdvancedTable
    data={[
      {
        'error_code': '`SDK error`',
        'what_it_means': 'MERCHANT_INFO_NOT_PRESENT - Enable txn-s2s_flow on the MID.',
        'recommended_fix': 'Enable txn-s2s_flow on the MID.'
      },
      {
        'error_code': '`SDK error`',
        'what_it_means': 'verify your server OR Something went wrong, please verify with your server. - Native OTP feature is not supported in UAT; comment native-otp-assist for UAT.',
        'recommended_fix': 'Native OTP feature is not supported in UAT; comment native-otp-assist for UAT.'
      }
    ]}
  />
</Accordion>
