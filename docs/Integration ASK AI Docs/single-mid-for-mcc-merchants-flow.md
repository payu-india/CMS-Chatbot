---
title: 'Single MID for MCC Merchants Flow '
deprecated: false
hidden: true
metadata:
  robots: index
---
In this setup, merchants had to maintain multiple MIDs at their end to map each MID with the currency required for payment.

Our Solution:
To address this, we created a flow where merchants can use a single MID at their end for multiple currencies.

Settlement Options:
Option 1: Individual settlements on all MIDs to the same account, with separate payouts provided for different currencies.

Option 2: Everything settled on a single MID with a single payout after converting to INR. Merchants will receive all MID data in the settlement APIs.

Integration Changes
Current hash string:
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT
New hash string with transaction currency:
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||transactionCurrency|S ALT
Post generation of revised hash string, use the SHA-512 logic for hash generation. The hash generation logic stays the same, just that transactionCurrency is added to the hash string before hashing.

3- Pass ‘ap&#x69;_&#x76;ersion' in_ payment API request body Parameter details are as below:

| Parameter                                            | Description                                                                         | Value |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------- | ----- |
| api\_version (Mandatory for multi-currency payments) | Type - String<br />The API version. Must be 22 for all multi-currency transactions. | 22    |

('merc\_hash\_vars\_seq','key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|ud f6|udf7|udf8|udf9|udf10|transactioncurrency',22,1,now(),now());
Array
(
  \[key] => biVbov
  \[txnid] => TXN17774573927586071
  \[amount] => 17000
  \[productinfo] => SingleMidMcf
  \[firstname] => Sunit
  \[email] =>
  \[phone] => 9876543210
  \[surl] =>
  \[furl] =>
  \[lastname] => Kumar
  \[address1] => FIRST FLOOR
  \[address2] => NEW ASHOK NAGAR
  \[city] => Delhi
  \[state] => Delhi
  \[country] => INDIA
  \[zipcode] => 201303
  \[udf1] => Cur-EUR

  \[udf2] => Testing UDF2
  \[udf3] =><br />  \[udf4] =><br />  \[udf5] => Sample\_Invoice\_11
  \[api\_version] => 22
  \[transactionCurrency] => EUR
  \[hash] =>
7a26a84e0525d59e6dc1dcd737ca7cf9fe85a0fdd6ed3849d9949a432516f9c5d7e9f45f59884faf37 aa450032d0cc78d3f4ce189a4d97c360f02fbb5c016e89
)
Key Highlights of the Solution
 •Single MID (Parent/Base MID) for all multi-currency payment initiation
 •Unified integration with one Key & Salt
 •
Currency to be passed dynamically via transactionCurrency parameter  •Internal mapping of Child MIDs (currency-wise) to the Parent MID
 •Flexible options for:
   oSettlement (consolidated or currency-wise)
   oInvoicing (single or currency-wise)
 •Single dashboard for payments, refunds, settlements, and chargebacks

Important Integration Changes (Merchant Side)
1.transactionCurrency must be added to the payment hash string 2.api\_version = 22 is mandatory for all multi-currency transactions 3.Hashing logic remains SHA-512 with the added parameter

Refund & Settlement Behaviour

• Refunds are always initiated using the Parent MID
• If refunds are processed via OD, OD balance must be maintained at the Parent MID• Single consolidated settlement is possible only when settlement cycles are the same  across all Parent & Child MIDs

<br />