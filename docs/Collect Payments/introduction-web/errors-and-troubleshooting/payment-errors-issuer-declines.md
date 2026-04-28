---
title: Issuer decline errors
excerpt: Issuer decline error codes and card-network response codes categorized from the PayU repo.
deprecated: false
hidden: true
metadata:
  title: Issuer decline errors
  description: Issuer decline error codes and card-network response codes categorized from the PayU repo.
  robots: index
next:
  description: ''
---

These rows are categorized from existing PayU repository error-code and troubleshooting documentation for **Issuer Decline Error Codes**.

Use this page with [Payment Failed or Declined](doc:payment-failed-declined) for debugging guidance and retry handling.

<!-- PAYU_REPO_PRODUCT_PAYMENT_ERRORS_PAYMENT_ERRORS_ISSUER_DECLINES_BEGIN -->

## Error reference

Rows categorized: **55**.

| Source doc | Error code / type | Error message / response indicator | Description | Recommended fix |
| --- | --- | --- | --- | --- |
| Issuer Decline Error Codes | E000 / response 0 | No Error | Approved or completed successfully | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E1625 / response 78 | Card not enabled for Ecomm transactions, either the card is newly issued or has not been used for any online transaction during last 12 months | Invalid/nonexistent account specified (general) | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E1626 / response 62 | Restricted card | Restricted card | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E1629 / response 70 | Transaction declined due to technical failure at bank end | Contact Card Issuer | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E1642 / response 57 | Transaction not permitted to cardholder | Transaction not permitted to issuer/cardholder | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E1656 / response 95 | Reconcile Error | Reconcile Error | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E1903 / response 6 | Authorization failed at Bank | Payment could not be authorised | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E207 / response 12 | Bank denied transaction on the card. | Invalid transaction | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E2102 / response 30 | Transaction not approved | Format error | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E224 / response 39 | Virtual Account Number Mismatch | No credit account | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E305 / response 15 | The transaction failed due to invalid or absent card number. | Invalid issuer | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E307 / response 5 | Transaction declined with do not honor | Do not honor | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E308 / response 20 | Transaction Failed at bank end. | Invalid response | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E312 / response 63 | Bank denied transaction on the card. | Security violation | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E324 / response 34 | Transaction was declined by the issuing bank due to suspected fraudulent activities | Suspected Fraud, Retain Card | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E325 / response 36 | Transaction declined due to card not enabled for online transactions or user / Bank Defined Restrictions | Restricted Card, Retain Card | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E337 / response 60 | Transaction declined by the issuer | Contact Card Acquirer | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E341 / response 3 | Transaction failed due to invalid merchant | Invalid Merchant | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E345 / response 19 | Transaction declined due to technical failure | Re-enter Transaction | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E348 / response 1 | Transaction declined by the issuer | Refer to card issuer | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E4346 / response 56 | Transaction failed due to no card details from customer's bank | No Card Record | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E4519 / response 86 | Refund failed due to insufficient amount | Cannot verify PIN | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E706 / response 51 | The account against which the payment was made has insufficient funds. | Insufficient funds/over credit limit / Not sufficient funds | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E707 / response 52 | Transaction failed due to invalid Primary Account Number. (Primary Account Number or PAN is the number that is embossed and/or encoded on a plastic card that identifies the issuer and the particular cardholder account.) | No Checking Account | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E710 / response 55 | Transaction failed due to invalid PIN | Invalid PIN | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E715 / response 13 | Invalid amount sent to the bank | Invalid amount | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E717 / response 46 | Transaction declined as bank reported account to be closed | Closed account | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9202 / response 10 | Partial Amount Approved | Partial Amount Approved | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9203 / response 11 | Approved VIP (not used) | Approved VIP (not used) | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9204 / response 16 | Approved Update Track 3 (not used) | Approved Update Track 3 (not used) | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9205 / response 17 | Customer Cancellation | Customer Cancellation | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9206 / response 18 | Customer Dispute | Customer Dispute | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9207 / response 21 | No Action Taken | No Action Taken | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9208 / response 22 | Suspected Malfunction | Suspected Malfunction | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9209 / response 23 | Unacceptable Transaction Fee | Unacceptable Transaction Fee | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9210 / response 24 | File Update not Supported by receiver | File Update not Supported by receiver | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9212 / response 26 | Duplicate File Update Record | Duplicate File Update Record | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9213 / response 27 | File Update Field Edit Error | File Update Field Edit Error | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9214 / response 28 | File Update File Locked Out | File Update File Locked Out | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9215 / response 29 | File Update not Successful | File Update not Successful | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9216 / response 32 | Completed Partially | Completed Partially | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9217 / response 38 | Allowable PIN Tries Exceeded | Allowable PIN Tries Exceeded | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9218 / response 40 | Requested Function not Supported | Requested Function not Supported | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9219 / response 66 | Card Acceptor Call Acquirer Security | Card Acceptor Call Acquirer Security | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9221 / response 69 | Mobile number record not found / mis-match | Mobile number record not found / mis-match | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9222 / response 77 | Approved (ANZ only) | Approved (ANZ only) | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9223 / response 81 | Cryptographic Error | Cryptographic Error | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9224 / response 87 | No Envelope Inserted | No Envelope Inserted | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9225 / response 88 | Unable to Dispense | Unable to Dispense | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9229 / response 97 | Reconciliation Totals Reset | Reconciliation Totals Reset | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9230 / response 98 | Exceeds Cash Limit | Exceeds Cash Limit | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9231 / response 99 | Reserved for National Use | Reserved for National Use | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9252 / response 42 | The customer's card issuer has declined the transaction as the account type selected is not valid for this credit card number | No Universal Account | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9253 / response 64 | Amount Incorrect / Mismatch | Original Amount Incorrect | Verify final status, then ask the customer to contact the issuer or use another payment method. |
| Issuer Decline Error Codes | E9254 / response 91 | Authorization Platform or Switch / Issuer system inoperative or Not Supported | Issuer or Switch is Inoperative | Verify final status, then ask the customer to contact the issuer or use another payment method. |

<!-- PAYU_REPO_PRODUCT_PAYMENT_ERRORS_PAYMENT_ERRORS_ISSUER_DECLINES_END -->
