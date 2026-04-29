---
title: Issuer Decline Errors
excerpt: Go through issuer decline error codes and card-network response codes.
deprecated: false
hidden: true
metadata:
  robots: index
---
These are the issuer decline error codes and card-network response codes, along with their descriptions, and recommended fix.

Refer to the [Payment Failed or Declined](doc:payment-failed-declined) page for debugging guidance and retry handling.

<Accordion title="Errors and Fixes" icon="fa-wrench">
  <SearchableTable
  headers={['Bank Code', 'Description', 'Recommended Fix']}
  columnWidths={['18%', '32%', '50%']}
  rows={[
    ['`No Error`', 'Approved or completed successfully', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Card not enabled for Ecomm transactions, either the card is newly issued or has not been used for any online transaction during last 12 months`', 'Invalid/nonexistent account specified (general)', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Restricted card`', 'Restricted card', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Transaction declined due to technical failure at bank end`', 'Contact Card Issuer', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Transaction not permitted to cardholder`', 'Transaction not permitted to issuer/cardholder', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Reconcile Error`', 'Reconcile Error', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Authorization failed at Bank`', 'Payment could not be authorised', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Bank denied transaction on the card.`', 'Invalid transaction', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Transaction not approved`', 'Format error', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Virtual Account Number Mismatch`', 'No credit account', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`The transaction failed due to invalid or absent card number.`', 'Invalid issuer', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Transaction declined with do not honor`', 'Do not honor', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Transaction Failed at bank end.`', 'Invalid response', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Bank denied transaction on the card.`', 'Security violation', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Transaction was declined by the issuing bank due to suspected fraudulent activities`', 'Suspected Fraud, Retain Card', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Transaction declined due to card not enabled for online transactions or user / Bank Defined Restrictions`', 'Restricted Card, Retain Card', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Transaction declined by the issuer`', 'Contact Card Acquirer', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Transaction failed due to invalid merchant`', 'Invalid Merchant', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Transaction declined due to technical failure`', 'Re-enter Transaction', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Transaction declined by the issuer`', 'Refer to card issuer', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Transaction failed due to no card details from customer\'s bank`', 'No Card Record', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Refund failed due to insufficient amount`', 'Cannot verify PIN', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`The account against which the payment was made has insufficient funds.`', 'Insufficient funds/over credit limit / Not sufficient funds', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Transaction failed due to invalid Primary Account Number. (Primary Account Number or PAN is the number that is embossed and/or encoded on a plastic card that identifies the issuer and the particular cardholder account.)`', 'No Checking Account', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Transaction failed due to invalid PIN`', 'Invalid PIN', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Invalid amount sent to the bank`', 'Invalid amount', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Transaction declined as bank reported account to be closed`', 'Closed account', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Partial Amount Approved`', 'Partial Amount Approved', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Approved VIP (not used)`', 'Approved VIP (not used)', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Approved Update Track 3 (not used)`', 'Approved Update Track 3 (not used)', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Customer Cancellation`', 'Customer Cancellation', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Customer Dispute`', 'Customer Dispute', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`No Action Taken`', 'No Action Taken', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Suspected Malfunction`', 'Suspected Malfunction', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Unacceptable Transaction Fee`', 'Unacceptable Transaction Fee', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`File Update not Supported by receiver`', 'File Update not Supported by receiver', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Duplicate File Update Record`', 'Duplicate File Update Record', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`File Update Field Edit Error`', 'File Update Field Edit Error', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`File Update File Locked Out`', 'File Update File Locked Out', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`File Update not Successful`', 'File Update not Successful', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Completed Partially`', 'Completed Partially', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Allowable PIN Tries Exceeded`', 'Allowable PIN Tries Exceeded', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Requested Function not Supported`', 'Requested Function not Supported', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Card Acceptor Call Acquirer Security`', 'Card Acceptor Call Acquirer Security', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Mobile number record not found / mis-match`', 'Mobile number record not found / mis-match', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Approved (ANZ only)`', 'Approved (ANZ only)', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Cryptographic Error`', 'Cryptographic Error', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`No Envelope Inserted`', 'No Envelope Inserted', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Unable to Dispense`', 'Unable to Dispense', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Reconciliation Totals Reset`', 'Reconciliation Totals Reset', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Exceeds Cash Limit`', 'Exceeds Cash Limit', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Reserved for National Use`', 'Reserved for National Use', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`The customer\'s card issuer has declined the transaction as the account type selected is not valid for this credit card number`', 'No Universal Account', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Amount Incorrect / Mismatch`', 'Original Amount Incorrect', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
    ['`Authorization Platform or Switch / Issuer system inoperative or Not Supported`', 'Issuer or Switch is Inoperative', 'Verify final status, then ask the customer to contact the issuer or use another payment method.'],
  ]}
  placeholder="Search errors..."
  maxHeight="500px"
/>
</Accordion>
