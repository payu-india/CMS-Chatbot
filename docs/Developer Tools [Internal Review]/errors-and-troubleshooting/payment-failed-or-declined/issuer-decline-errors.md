---
title: Issuer Decline Errors
excerpt: Go through issuer decline error codes and card-network response codes.
deprecated: false
hidden: true
metadata:
  robots: index
---
These are the issuer decline error codes and card-network response codes, along with their descriptions, and recommended fix.

Refer to the Payment Failed or Declined page for debugging guidance and retry handling.

<Accordion title="" icon="fa-info-circle">
  <AdvancedTable
    data={[
      {
        'bank_code': '`No Error`',
        'description': 'Approved or completed successfully',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Card not enabled for Ecomm transactions, either the card is newly issued or has not been used for any online transaction during last 12 months`',
        'description': 'Invalid/nonexistent account specified (general)',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Restricted card`',
        'description': 'Restricted card',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Transaction declined due to technical failure at bank end`',
        'description': 'Contact Card Issuer',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Transaction not permitted to cardholder`',
        'description': 'Transaction not permitted to issuer/cardholder',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Reconcile Error`',
        'description': 'Reconcile Error',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Authorization failed at Bank`',
        'description': 'Payment could not be authorised',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Bank denied transaction on the card.`',
        'description': 'Invalid transaction',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Transaction not approved`',
        'description': 'Format error',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Virtual Account Number Mismatch`',
        'description': 'No credit account',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`The transaction failed due to invalid or absent card number.`',
        'description': 'Invalid issuer',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Transaction declined with do not honor`',
        'description': 'Do not honor',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Transaction Failed at bank end.`',
        'description': 'Invalid response',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Bank denied transaction on the card.`',
        'description': 'Security violation',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Transaction was declined by the issuing bank due to suspected fraudulent activities`',
        'description': 'Suspected Fraud, Retain Card',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Transaction declined due to card not enabled for online transactions or user / Bank Defined Restrictions`',
        'description': 'Restricted Card, Retain Card',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Transaction declined by the issuer`',
        'description': 'Contact Card Acquirer',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Transaction failed due to invalid merchant`',
        'description': 'Invalid Merchant',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Transaction declined due to technical failure`',
        'description': 'Re-enter Transaction',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Transaction declined by the issuer`',
        'description': 'Refer to card issuer',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Transaction failed due to no card details from customer\'s bank`',
        'description': 'No Card Record',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Refund failed due to insufficient amount`',
        'description': 'Cannot verify PIN',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`The account against which the payment was made has insufficient funds.`',
        'description': 'Insufficient funds/over credit limit / Not sufficient funds',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Transaction failed due to invalid Primary Account Number. (Primary Account Number or PAN is the number that is embossed and/or encoded on a plastic card that identifies the issuer and the particular cardholder account.)`',
        'description': 'No Checking Account',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Transaction failed due to invalid PIN`',
        'description': 'Invalid PIN',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Invalid amount sent to the bank`',
        'description': 'Invalid amount',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Transaction declined as bank reported account to be closed`',
        'description': 'Closed account',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Partial Amount Approved`',
        'description': 'Partial Amount Approved',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Approved VIP (not used)`',
        'description': 'Approved VIP (not used)',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Approved Update Track 3 (not used)`',
        'description': 'Approved Update Track 3 (not used)',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Customer Cancellation`',
        'description': 'Customer Cancellation',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Customer Dispute`',
        'description': 'Customer Dispute',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`No Action Taken`',
        'description': 'No Action Taken',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Suspected Malfunction`',
        'description': 'Suspected Malfunction',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Unacceptable Transaction Fee`',
        'description': 'Unacceptable Transaction Fee',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`File Update not Supported by receiver`',
        'description': 'File Update not Supported by receiver',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Duplicate File Update Record`',
        'description': 'Duplicate File Update Record',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`File Update Field Edit Error`',
        'description': 'File Update Field Edit Error',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`File Update File Locked Out`',
        'description': 'File Update File Locked Out',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`File Update not Successful`',
        'description': 'File Update not Successful',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Completed Partially`',
        'description': 'Completed Partially',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Allowable PIN Tries Exceeded`',
        'description': 'Allowable PIN Tries Exceeded',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Requested Function not Supported`',
        'description': 'Requested Function not Supported',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Card Acceptor Call Acquirer Security`',
        'description': 'Card Acceptor Call Acquirer Security',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Mobile number record not found / mis-match`',
        'description': 'Mobile number record not found / mis-match',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Approved (ANZ only)`',
        'description': 'Approved (ANZ only)',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Cryptographic Error`',
        'description': 'Cryptographic Error',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`No Envelope Inserted`',
        'description': 'No Envelope Inserted',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Unable to Dispense`',
        'description': 'Unable to Dispense',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Reconciliation Totals Reset`',
        'description': 'Reconciliation Totals Reset',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Exceeds Cash Limit`',
        'description': 'Exceeds Cash Limit',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Reserved for National Use`',
        'description': 'Reserved for National Use',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`The customer\'s card issuer has declined the transaction as the account type selected is not valid for this credit card number`',
        'description': 'No Universal Account',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Amount Incorrect / Mismatch`',
        'description': 'Original Amount Incorrect',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      },
      {
        'bank_code': '`Authorization Platform or Switch / Issuer system inoperative or Not Supported`',
        'description': 'Issuer or Switch is Inoperative',
        'recommended_fix': 'Verify final status, then ask the customer to contact the issuer or use another payment method.'
      }
    ]}
  />
</Accordion>
