---
title: Quick Start Server-to-Server Integration
deprecated: false
hidden: false
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
Get up and running with PayU Server-to-Server (S2S) payments in three steps.

### Environment

| Environment        | Base URL         | Transaction Endpoint |
| :----------------- | :--------------- | :------------------- |
| **Test / Sandbox** | `<redacted URL>` | `<redacted URL>`     |
| **Production**     | `<redacted URL>` | `<redacted URL>`     |


## 1. Generate SHA-512 Request Hash

Every payment request sent to `/_payment` requires a cryptographically secure SHA-512 signature.

### Hash Formula

$$\text{hash} = \text{SHA-512}(\text{key} \mid \text{txnid} \mid \text{amount} \mid \text{productinfo} \mid \text{firstname} \mid \text{email} \mid \text{udf1} \mid \text{udf2} \mid \text{udf3} \mid \text{udf4} \mid \text{udf5} \mid \mid \mid \mid \mid \mid \text{SALT})$$

* Concatenate the values using pipe (`|`) delimiters.
* If user defined fields (`udf1` through `udf5`) are not used, pass empty strings, but keep the pipe delimiters intact (`...|email|||||||||||SALT`).

***

## 2. Verify Reverse Response Hash

When PayU posts payment status back to your `surl`, `furl`, or webhook endpoint, compute and verify the reverse hash:

$$\text{reverseHash} = \text{SHA-512}(\text{SALT} \mid \text{status} \mid \mid \mid \mid \mid \mid \text{udf5} \mid \text{udf4} \mid \text{udf3} \mid \text{udf2} \mid \text{udf1} \mid \text{email} \mid \text{firstname} \mid \text{productinfo} \mid \text{amount} \mid \text{txnid} \mid \text{key})$$

* If `received_hash !== calculated_hash`, discard the response and flag the transaction for investigation.

***

## 3. IP Whitelisting

Whitelist PayU outgoing notification IP addresses on your firewall and reverse proxy:

* `180.179.174.1`
* `180.179.174.2`
