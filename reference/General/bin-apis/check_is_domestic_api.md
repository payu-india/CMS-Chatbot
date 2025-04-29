---
title: Check is Domestic API
excerpt: ''
api:
  file: check-is-domestic-api-1.json
  operationId: checkisdomestic
deprecated: false
hidden: false
metadata:
  title: Check is Domestic API
  description: >-
    The document describes the Check is Domestic or Card BIN API, which is used
    to determine if a BIN number is international or domestic, along with other
    card details like issuing bank and card type.
  keywords:
    - check_isDomestic API Command
    - Check is Domestic API
    - Domestic transaction check API
    - Domestic transaction identification API
    - Check domestic payment API
    - Verify domestic transaction API
    - Integrating PayU Check is Domestic API
  robots: index
next:
  description: ''
---
The  ** Check is Domestic** or **Card BIN **API is used to detect whether a particular BIN number is international or domestic. It is also useful to determine: 

- card’s issuing bank
- card type such as, Visa, Master, etc.,
- card category such as Credit/Debit, etc. 
- var1 is bin number which is the first 6 digits of a Credit/Debit card.

<GENERALAPIsEnvironment />

<details><summary>Sample request</summary>

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d

"key=JP***g&command=check_isDomestic&var1=462273&hash=df4ff56008defd9d7f9bf09506061f5c790dbe1d011659d85b88d34323ff49a65181e522eddf3075285c17708566709c803d3b0b0979120804b00f62236062a2"
```

</details>

<details>  <summary>Sample response</summary>

If the card is domestic

```plaintext
{
      "isDomestic": "Y",
      "issuingBank": "SCB",
      "cardType": "VISA",
      "cardCategory": "CC"
}
```

If the card is international

```plaintext
{
      "isDomestic": "N",
      "issuingBank": "UNKNOWN",
      "cardType": "Unknown",
      "cardCategory": "CC"
}
```

</details>

<details><summary>Response parameters description</summary>

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "0-0": "isDomestic",
    "0-1": "Response value can contain any of the following:  \n  \n- **Y** signifies that the particular BIN is domestic.\n- **N** signifies that the particular BIN is International.",
    "1-0": "cardType",
    "1-1": "Response value can contain any of the following:  \n  \n- MAST\n- VISA\n- MAES\n- AMEX\n- DINER\n- Unknown",
    "2-0": "issuingBank",
    "2-1": "The issuing bank of the card used for the transaction.",
    "3-0": "cardCategory",
    "3-1": "Response value can contain any of the following:  \n  \n- **CC** signifies that the particular bin is a credit card BIN \n- **DC** signifies that the particular bin is a debit card BIN"
  },
  "cols": 2,
  "rows": 4,
  "align": [
    null,
    null
  ]
}
[/block]


To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes).

</details>

## Request parameters

<details><summary>Reference information</summary>

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Reference",
    "0-0": "<<glossary:key>>",
    "0-1": "For more information on how to generate the Key and Salt, refer to any of the following:  \n  \n\\- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  \n  \n- **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)",
    "1-0": "<<glossary:hash>>",
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

**Example values**

- `var1` (first six digit of the card): 512345.