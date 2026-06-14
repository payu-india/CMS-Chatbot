---
title: UPI and Net Banking TPV integration
excerpt: >-
  Integrate UPI and Net Banking Third Party Validation payments with PayU using
  beneficiary account details, TPV bank codes, and hash generation.
deprecated: false
hidden: true
metadata:
  robots: index
---
# UPI and Net Banking TPV integration

Use Third Party Validation (TPV) with UPI or Net Banking to verify the customer's underlying bank account before completing a payment.

Third Party Validation (TPV) reduces risk by validating the bank account used for a transaction. TPV is mandatory under SEBI requirements for BFSI merchants such as stockbrokers and mutual funds.

## Test credentials

### UPI

| Field | Test value |
| --- | --- |
| `beneficiarydetail` | `{"beneficiaryAccountNumber":"1111111111","ifscCode":"111111189HSBB001"}` |
| `vpa` | `kk@okaxis` or `9999999999@upi` |

### Net Banking

| Field | Test value |
| --- | --- |
| `beneficiarydetail` | `{"beneficiaryAccountNumber":"123456789012345","ifscCode":"KTKB0000046"}` |

## UPI TPV integration

Use Merchant Hosted or S2S seamless integration for UPI TPV.

<Callout icon="circle-info" theme="info">
For UPI TPV, the transaction amount must be greater than `100`.
</Callout>

### 1. Validate the VPA

Validate the customer's VPA before initiating the UPI TPV collect transaction.

### 2. Initiate the UPI TPV payment

Initiate the transaction with the customer's bank account details by using the Collect Payment (`_payment`) API.

```text title="UPI TPV request fields"
key: ISgdHG
txnid: 7378d239f3a9d065cb48
api_version: 6
amount: 200
email:
phone: 1234567890
productinfo: Product Info
surl:
furl:
pg: UPI
bankcode: UPITPV
hash: 45c113cd47f427599002ac58194ef00b1b4ed23c325c72c97bccf73a51035e636c6d089fde2bc25f6dbfba10bd8c04ad9e1348707168814fe7e533b343f07807
beneficiarydetail: {"beneficiaryAccountNumber":"1111111111","ifscCode":"111111189HSBB001"}
vpa: kk@okaxis
```

Generate the UPI TPV hash with this sequence:

```text
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT
```

Expected response:

```text
[mihpayid] => 403993715533342518
[mode] => UPI
[status] => success
[unmappedstatus] => captured
[key] => ISgdHG
[txnid] => 7378d239f3a9d065cb48
[amount] => 200.00
[discount] => 0.00
[net_amount_debit] => 200
[addedon] => 2025-02-11 17:25:52
[productinfo] => Product Info
[firstname] =>
[email] =>
[phone] => 1234567890
[udf1] =>
[udf2] =>
[udf3] =>
[udf4] =>
[udf5] =>
[hash] => 5b22c4192d64bb96a73730c89c265fe6e4d1613e60b8d89cb12f20cd4fc9970fbdb93e2b05ca5e62f3aa3ef36c9a49603704edcf7b14f2ea346d26b212af6709
[field1] => kk@okaxis
[field2] => 1739274956306
[field3] => kk@okaxis
[field4] => KUNAL KUKREJA
[field5] => HDFG9W332GP1XLWQ5V9ERUEZUE2TKJQ3QCTS
[field6] => State Bank of India!1111111111!SBIN0011111!+917985392981
[field7] => APPROVED OR COMPLETED SUCCESSFULLY|00
[field8] =>
[field9] => SUCCESS|Completed Using Verify API
[payment_source] => payu
[pa_name] => PayU
[PG_TYPE] => UPI-PG
[bank_ref_num] => 869637478153
[bankcode] => UPITPV
[error] => E000
[error_Message] => No Error
[splitInfo] => {"splitStatus":"splitNotReceived","splitSegments":[]}
```

## Net Banking TPV integration

Use seamless or S2S integration for Net Banking TPV.

### 1. Prepare beneficiary account details

Collect the account numbers and matching IFSC codes that must be sent for TPV. You can send up to five account details in the `beneficiarydetail` parameter.

When you send multiple accounts, separate values with `|` and keep the account number and IFSC values in the same order.

```json title="Multiple beneficiary details example"
{
  "beneficiaryAccountNumber": "002001600674|00000031957292212|00000035955239352|00000035955239352",
  "ifscCode": "KTKB0000046|KTKB0000023|KTKB0000035|KTKB0000035"
}
```

### 2. Initiate the Net Banking TPV payment

Initiate the transaction with the customer's bank account details by using the Collect Payment (`_payment`) API.

```text title="Net Banking TPV request fields"
key: ISgdHG
txnid: 0f7c3287b1ef167dd96e
api_version: 6
amount: 1000
email:
phone: 1234567890
productinfo: Product Info
surl:
furl:
udf1:
udf2:
udf3:
udf4:
udf5:
hash: 58935e68838406dc1c35f5a89b69dee4ab033f332a08712d85564fec7f0c7623ea123fb4fb11f01092f08ef7dee83df8878a73bf4ecd87889d6299b83c1356f8
pg: NB
bankcode: AXNBTPV
beneficiarydetail: {"beneficiaryAccountNumber":"123456789012345","ifscCode":"KTKB0000046"}
```

<Callout icon="circle-info" theme="info">
The TPV `bankcode` value varies by bank. Use the TPV bank code assigned for the customer's selected bank.
</Callout>

Generate the Net Banking TPV hash with this sequence:

```text
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT
```

Expected response:

```text
[mihpayid] => 403993715533343271
[mode] => NB
[status] => success
[unmappedstatus] => captured
[key] => ISgdHG
[txnid] => 0f7c3287b1ef167dd96e
[amount] => 1000.00
[discount] => 0.00
[net_amount_debit] => 1000
[addedon] => 2025-02-11 18:28:38
[productinfo] => Product Info
[firstname] =>
[email] =>
[phone] => 1234567890
[udf1] =>
[udf2] =>
[udf3] =>
[udf4] =>
[udf5] =>
[hash] => d50929316d1a7497f392251090f873ccf6957a5147462dd58e6b964e729e5163f4a6ee28506e554f12b776f602693aed83b3fd7fb9050f37492c5386165780e6
[field1] =>
[field2] =>
[field3] =>
[field4] =>
[field5] =>
[field6] =>
[field7] =>
[field8] =>
[field9] => Transaction Completed Successfully
[payment_source] => payu
[pa_name] => PayU
[PG_TYPE] => NB-PG
[bank_ref_num] => 870bdc23-1b1a-41c9-87cd-db25665c1490
[bankcode] => AXNBTPV
[error] => E000
[error_Message] => No Error
[splitInfo] => {"splitStatus":"invalidSplitReceived","splitSegments":[]}
```

## Required parameters

| Parameter | UPI TPV | Net Banking TPV | Description |
| --- | --- | --- | --- |
| `key` | Required | Required | Merchant key provided by PayU. |
| `txnid` | Required | Required | Unique transaction ID. |
| `api_version` | Required | Required | Use `6` for the request examples on this page. |
| `amount` | Required | Required | Transaction amount. UPI TPV amount must be greater than `100`. |
| `productinfo` | Required | Required | Product or service description. |
| `firstname` | Required for hash sequence | Required for hash sequence | Customer first name. Include an empty value in the hash sequence if not passed. |
| `email` | Required for hash sequence | Required for hash sequence | Customer email. Include an empty value in the hash sequence if not passed. |
| `phone` | Required | Required | Customer phone number. |
| `surl` | Required | Required | Success URL. |
| `furl` | Required | Required | Failure URL. |
| `pg` | Required | Required | Use `UPI` for UPI TPV and `NB` for Net Banking TPV. |
| `bankcode` | Required | Required | Use `UPITPV` for UPI TPV. For Net Banking TPV, use the bank-specific TPV code, such as `AXNBTPV`. |
| `beneficiarydetail` | Required | Required | JSON object containing `beneficiaryAccountNumber` and `ifscCode`. |
| `vpa` | Required | Not applicable | Customer VPA for UPI TPV. |
| `hash` | Required | Required | Hash generated from the documented hash sequence. |

## Troubleshooting

| Issue | Likely cause | Fix |
| --- | --- | --- |
| UPI TPV request fails for amount validation | The amount is `100` or lower. | Send a UPI TPV amount greater than `100`. |
| TPV validation fails | `beneficiarydetail` has an incorrect account number or IFSC. | Verify `beneficiaryAccountNumber` and `ifscCode` before initiating the payment. |
| Net Banking TPV request fails for bank code | The `bankcode` does not match the selected bank's TPV code. | Use the TPV bank code assigned for that bank, such as `AXNBTPV` for the sample request. |
| Hash mismatch | The `beneficiarydetail` value used in the hash does not exactly match the request value. | Generate the hash with the exact `beneficiarydetail` string sent in the request. |
| Duplicate transaction rejection | The same `txnid` was reused. | Generate a unique `txnid` for every transaction. |

{/* Legacy malformed source content is hidden below so the page renders reliably. Remove this block after confirming the cleaned content above in production.
**Introduction**

Third Party Validation (TPV) ensures credibility and reduces risk for the businesses by verifying the underlying bank account. Third-Party Verification (TPV) is a mandatory requirement as per Stock Exchange Bureau India (SEBI) mandate for merchants such as stockbrokers and mutual funds operating in the BFSI sector.

Document Reference :-

**UPI Test Credentials:**

• beneficiary details = <br /> {"beneficiaryAccountNumber":"1111111111","ifscCode":"111111189HSBB001"} • VPA = kk\@okaxis Or 9999999999\@upi

**Netbanking Test Credentials:**

• beneficiary details <br /> ={"beneficiaryAccountNumber":"123456789012345","ifscCode":"KTKB0000046"}

**UPI TPV Integration**

• Merchant Hosted or S2S (Seamless) integration has to be done as per the standard kit for  TPV.

(**NOTE**: For UPI TPV transaction amount should be greater than 100)

**Step 1-** Merchant can validate the VPA before initiating UPI TPV collect transaction using Validat for the same, <br />Link:-

**Step 2-** Initiate the transaction request with the customer’s bank account number to the PayU using the Collect Payment (**\_payment**) API.

**Sample Request:**

• key: ISgdHG <br />• txnid: 7378d239f3a9d065cb48 <br />• **api\_version: 6**<br />• amoun<br />• email:

<br />

<br />
*/}

• phone: 1234567890 <br />• productinfo: Product Info <br />• surl: <br />• furl: <br />• **pg: UPI**<br />• **bankcode: UPITPV**<br />• hash: <br /> 45c113cd47f427599002ac58194ef00b1b4ed23c325c72c97bccf73a51035e636c6d089fde2  bc25f6dbfba10bd8c04ad9e1348707168814fe7e533b343f07807 <br />• **beneficiarydetail:&#x20;**<br /> **{"beneficiaryAccountNumber":"1111111111","ifscCode":"111111189HSBB001"}**• vpa: kk\@okaxis

(**NOTE**: The calculation logic for UPI TPV transaction is <br />key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT )

**Response:**

• \[mihpayid] => 403993715533342518 <br />• \[mode] => UPI <br />• \[status] => success <br />• \[unmappedstatus] => captured <br />• \[key] => ISgdHG <br />• \[txnid] => 7378d239f3a9d065cb48 <br />• \[amount] => 200.00 <br />• \[discount] => 0.00 <br />• \[net\_amount\_debit] => 200 <br />• \[addedon] => 2025-02-11 17:25:52 <br />• \[productinfo] => Product Info <br />• \[firstname]<br />• \[email] => <br />• \[phone] => 1234567890 <br />• \[udf1] => <br />• \[udf2] => <br />• \[udf3] => <br />• \[udf4] => <br />• \[udf5] => <br />• \[hash] => <br /> 5b22c4192d64bb96a73730c89c265fe6e4d1613e60b8d89cb12f20cd4fc9970fbdb93e2b05  ca5e62f3aa3ef36c9a49603704edcf7b14f2ea346d26b212af6709 <br />• \[field1] => kk\@okaxis <br />• \[field2] => 1739274956306 <br />• \[field3] => kk\@okaxis <br />• \[field4] => KUNAL KUKREJA <br />• \[field5] => HDFG9W332GP1XLWQ5V9ERUEZUE2TKJQ3QCTS

<br />

<br />

| •<br />•<br />•<br />•<br />•<br />•<br />•<br />•<br />•<br />•<br />•<br />• | \[field6] => State Bank of India!1111111111!SBIN0011111!+917985392981 \[field7] => APPROVED OR COMPLETED SUCCESSFULLY\|00 <br />\[field8] => <br />\[field9] => SUCCESS\|Completed Using Verify API <br />\[payment\_source] => payu <br />\[pa\_name] => PayU <br />\[PG\_TYPE] => UPI-PG <br />\[bank\_ref\_num] => 869637478153 <br />\[bankcode] => UPITPV <br />\[error] => E000 <br />\[error\_Message] => No Error <br />\[splitInfo] => {"splitStatus":"splitNotReceived","splitSegments":\[]} |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

**Netbanking TPV Integration**

• Seamless or S2S integration has to be done as per the standard kit for TPV.

**Step 1-** Collect a list of account numbers that must be posted along with corresponding IFSC

codes (in the same order as provided in the beneficiaryAccountNumber key)to PayU for TPV as

you can post up to five account details in ‘beneficiary details’ parameter.

For Example :

{"beneficiaryAccountNumber":"002001600674|00000031957292212|00000035955239352|0000

0035955239352", "ifscCode":"KTKB0000046|KTKB0000023|KTKB0000035|KTKB0000035"}

**Step 2-** Initiate the transaction request with the customer’s bank account number to the PayU

using the Collect Payment (**\_payment**) API.

**Sample Request:**

• key: ISgdHG

• txnid: 0f7c3287b1ef167dd96e

• **api\_version: 6**

• amoun

• email:

• phone: 1234567890

• prod

• surl:

• furl:

• udf1:

• udf2:

• udf3:

• udf4:

• udf5:

<br />

<br />

• hash:

58935e68838406dc1c35f5a89b69dee4ab033f332a08712d85564fec7f0c7623ea123fb4fb1

1f01092f08ef7dee83df8878a73bf4ecd87889d6299b83c1356f8

• **pg: NB**

• **bankcode: AXNBTPV**

• beneficiarydetail:

{"beneficiaryAccountNumber":"123456789012345","ifscCode":"KTKB0000046"}

(**NOTE** :

• The TPV bank codes you enter in the bank code parameter varies based on the bank.

all bank codes,

&#x20;.

• The calculation logic for UPI TPV transaction is

key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetai

l|SALT ).

**Response:**

• \[mihpayid] => 403993715533343271

• \[mode] => NB

• \[status] => success

• \[unmappedstatus] => captured

• \[key] => ISgdHG

• \[txnid] => 0f7c3287b1ef167dd96e

• \[amount] => 1000.00

• \[discount] => 0.00

• \[net\_amount\_debit] => 1000

• \[addedon] => 2025-02-11 18:28:38

• \[productinfo] => Product Info

• \[firstname]

• \[email] =>

• \[phone] => 1234567890

• \[udf1] =>

• \[udf2] =>

• \[udf3] =>

• \[udf4] =>

• \[udf5] =>

• \[hash] =>

d50929316d1a7497f392251090f873ccf6957a5147462dd58e6b964e729e5163f4a6ee2850

6e554f12b776f602693aed83b3fd7fb9050f37492c5386165780e6

• \[field1] =>

• \[field2] =>

• \[field3] =>

• \[field4] =>

• \[field5] =>

• \[field6] => <br />• \[field7] => <br />• \[field8] => <br />• \[field9] => Transaction Completed Successfully <br />• \[payment\_source] => payu <br />• \[pa\_name] => PayU <br />• \[PG\_TYPE] => NB-PG <br />• \[bank\_ref\_num] => 870bdc23-1b1a-41c9-87cd-db25665c1490 <br />• \[bankcode] => AXNBTPV <br />• \[error] => E000 <br />• \[error\_Message] => No Error <br />• \[splitInfo] => {"splitStatus":"invalidSplitReceived","splitSegments":\[]}

<br />

<br />