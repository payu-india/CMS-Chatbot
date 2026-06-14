---
title: 'Refund: '
deprecated: false
hidden: false
metadata:
  robots: index
---
Refund is the process of reversing funds back to the customer against the sale transaction performed. Merchant initiated the refunds, payment service provider perform pre-processing checks and hit it to the acquirer further acquirer process the refund and credit the funds.

For Test environment use below post action URL.

Test Environment:

In this API call we must pass below mandatory parameters.

• key: Merchant Key
• command : cancel\_refund\_transaction
• var1: Mihpayid
• var2: Unique token id from merchant end
• var3: Amount
• var5: Webhook URL

Hash: Key|command|var1|salt

Please find below merchant curl for the same.

curl --location '[https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2)' \ --header 'Content-Type: application/x-www-form-urlencoded' \\
\--header 'Cookie: PHPSESSID=f5nsq8of7civqt8vj76rb6ad8u;
USERTXNINFO=67a45812ad86e6.64251676' \\
\--data-urlencode 'key=PpyhFu' \\
\--data-urlencode 'command=cancel\_refund\_transaction' \\
\--data-urlencode 'var1=403993715533349791' \\
\--data-urlencode 'var2=081220223' \\
\--data-urlencode 'var3=1000' \\
\--data-urlencode
'hash=b621ae64ed170288cb581f1ce4beca624fc6211c06b763272c5ca5ad17e84e1b1f41259 326881d8416ec9657e39d9db0aae1e077ff7438159389e3600bd34b1c' \\
\--data-urlencode 'var5=[https://webhook.site/1a48cbca-50ae-452e-9248-](https://webhook.site/1a48cbca-50ae-452e-9248-)
f57906b949da'

Response:

Note: On UAT refund status is in Queue only. Refund process will work on Production.

(
\[status] => 1
\[msg] => Refund Request Queued
\[request\_id] => 081220223'
\[bank\_ref\_num] =>
\[mihpayid] => 403993715533349791'
\[error\_code] => 102
)

Check Refund transaction status API:

We can fetch the refund transaction status using request id and mihpayid.

• nt:  • To check the status of refund transaction using PayUID refer document:

• Please refer document for payment state explaination:

Status

Description

• QUEUED

This indicates that the refund is accepted by PayU, but not sent to the downstream banking partner for processing.

• SUCCESS

This indicates that the refund is processed successfully.

• FAILURE

This indicates that refund processing failed. No funds are deducted for such refunds from the merchant’s settlement.

• IN

PROGRESS

This indicates that the refund is raised to the bank for processing.

• REQUESTED

This indicates that the refund is sent to the bank for offline processing. In such cases, it takes upto 5-7 business days for the credit to reflect into the customer’s account.

• PENDING

This indicates that the Overdraft has occurred( Insufficient funds in account ) In such cases, it takes upto 5-7 business days for the credit to reflect into the customer’s account.

Please refer below document for Error codes for refund:

To Get All Refunds for a Transaction ID API (getAllRefundsFromTxnIds) command is used to retrieve the status of all the refund requests fired for a particular Transaction ID:

[https://docs.payu.in/reference/get\_all\_refunds\_from\_transaction\_ids\_api](https://docs.payu.in/reference/get_all_refunds_from_transaction_ids_api "https://docs.payu.in/reference/get_all_refunds_from_transaction_ids_api")
