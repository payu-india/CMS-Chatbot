---
title: Get Issuing Bank Status API
excerpt: Issuing Bank Status
api:
  file: health-check-7.json
  operationId: IssuingBankStatus
deprecated: false
hidden: false
metadata:
  title: Get Issuing Bank Status API
  description: >-
    The **Get Issuing Bank Status** API (**getIssuingBankStatus**) helps handle
    credit or debit card issuing bank downtime by providing information on the
    status of the bank.
  keywords:
    - getIssuingBankStatus API Command
    - Issuing Bank of Credit Card Status API
    - ' Issuing Bank of Debit Card Status API'
    - Check issuing bank health that issued credit card API
    - Check issuing bank health that issued debit card API
    - Health check of card issuing bank API
    - Health check of credit card issuing bank API
    - Health check of debit card issuing bank API
    - API Command getIssuingBankStatus
  robots: index
next:
  description: ''
---
The **Get Issuing Bank Status** API (**getIssuingBankStatus**) is used to help you handle the credit card or debit card issuing bank downtime.

<GENERALAPIsEnvironment />

<details><summary>Sample request</summary>

```
curl -X POST "https://test.payu.in/merchant/postservice?form=2
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
"key=J****g&command=getIssuingBankStatus&var1=512345&hash=190908741314524c922d9587298eb64a076d058c085c66229f5acfeac4fb8a11dcd41f3f566cdb2e14a12f486a598a4e56943a2390c258384add9aeed1885e9d"
```

 </details>

 <details><summary>Sample response</summary>

**Success scenario**

```plaintext
{
      "issuing_bank": "HDFC",
      "up_status": "1"
}
```

- up_status parameter with the value as 0 signifies that the particular Bank option is down at the moment.
- up_status parameter with the value as 1 signifies that the particular Bank Banking option is up at the moment.

**Failure scenario**

If issuing bank data is not available for the BIN:

```
{             
 "msg":"No information available",
"status":0
}
```

 </details>

 <details><summary>Response parameters</summary>

The response parameters for a bank code passed in **var1**, it returns a response for the specified bank alone with the parameters as explained in the following table. If the **default** value is passed in **var1**, it returns a array of all the banks in a JSON array format and each JSON has the list of fields similar to the parameter list:

[block:parameters]
{
  "data": {
    "h-0": "**Parameter/JSON Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "ibibo\\_code",
    "0-1": "This parameter contains the bank code for which the Net Banking status is displayed.",
    "0-2": "AXIB",
    "1-0": "title",
    "1-1": "This parameter contains the bank name and service.",
    "1-2": "AXIS Bank NetBanking",
    "2-0": "up\\_status",
    "2-1": "This parameter contains the status of the NetBanking service and can be any of the following:  \n  \n- 0 - signifies that the particular Bank option is down at the moment\n- 1 - signifies that the particular Banking option is up at the moment",
    "2-2": "1",
    "3-0": "mode",
    "3-1": "This parameter contains the mode of payment for which the status is displayed.",
    "3-2": "NB"
  },
  "cols": 3,
  "rows": 4,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


</details>

## Request parameters

 <details><summary>Reference information</summary>

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Reference",
    "0-0": "key",
    "0-1": "For more information on how to generate the Key and Salt, refer to any of the following:  \n  \n\\- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  \n  \n- **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)",
    "1-0": "hash",
    "1-1": "Hash logic for this API is:  \n`sha512(key\\|command\\|var1\\|salt) sha512\n`",
    "2-0": "var1",
    "2-1": "For JSON fields description, refer to [Additional Info for General APIs](ref:addl-info-general-apis)"
  },
  "cols": 2,
  "rows": 3,
  "align": [
    "left",
    "left"
  ]
}
[/block]


 </details>

Use the following sample values while trying out the API:

**Example values**:

- `var1`(first 6 digit of the card): First six digits of any card (ex- 512345)