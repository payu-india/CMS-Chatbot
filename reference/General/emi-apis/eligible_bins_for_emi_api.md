---
title: Eligible BINs for EMI API v1.0
excerpt: ''
api:
  file: emi-apis-10.json
  operationId: EligibleBINsforEMI
deprecated: false
hidden: false
metadata:
  title: Eligible BINs for EMI API
  description: >-
    The Eligible BINs for EMI API version 1.0 provides information on the
    issuing bank of a card bin and the minimum eligible amount for EMI
    transactions. It can be used with or without specifying a bank name.
  keywords:
    - eligibleBinsForEMI API Command
    - Check EMI eligibility API version 1.0
    - ' EMI Eligibility Check API v1.0'
    - API Command eligibleBinsForEMI
  robots: index
next:
  description: ''
---
The Eligible BINs for EMI API (**eligibleBinsForEMI**) version 1.0 is used only when the merchant needs the EMI feature of PayU. If you are managing card details on your website, this API can tell the issuing bank of the card bin. It also provides the minimum eligible amount for a particular bank.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2eaac64-emi_eligible_bins_flow.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


You can post a request using any of the following methods:

- **Request without Bank Selection**: This is submitting API without bank name in var3 field.
- **Request with Bank Selection**: : This is submitting API with bank name in var3 field so that you will get the details for the specified bank.

<GENERALAPIsEnvironment />

<details><summary>Sample request</summary>

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2"-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d"key=JP***g&command=eligibleBinsForEMI&var1=Bin&var2=512345&hash=3c923a16606d07f12aa984487626abbc0981f540131f8bb0d24b6322c362089bbd4114d710129ce54128691956775352ac53e7d7943392959d37275c934245f2"
```

</details>

<details>  <summary>Sample response</summary>

**Success Scenario**

On successful processing from PayU, the response is similar to the following:

```plaintext
{
      "status": 1,
      "msg": "Details fetched successfully",
      "details": {
            "isEligible": 1,
            "bank": "AXIS",
            "minAmount": 2500
      }
}

```

**Failure scenario**

If eligibility is not found:

```
Array 
(
    [status] => 1
    [msg] => Details fetched successfully
    [details] => Array
(
[isEligible] => 0
) )
```

</details>

<details><summary>Response parameters</summary>

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "status",
    "0-1": "This parameter returns the status of web service call. The status can be any of the following:  \n_ 0 - If web service call failed.  \n_ 1 - If web service call succeeded",
    "0-2": "",
    "1-0": "msg",
    "1-1": "This parameter returns whether the EMI details were fetched successfully or not found.",
    "1-2": "Details fetched successfully",
    "2-0": "details",
    "2-1": "The details of the EMI offer is displayed in a JSON format and it contains the following fields:  \n\\_ **isEligible** - This paraAny of the following values are  \n  \n- 0 - If EMI offers are not available for the given card BIN.\n- 1 - If EMI offers are available for the given card BIN.  \n  \\_ **bank** - The name of bank that corresponds to the given card BIN  \n  \\* **minAmount** - The minimum amount for which the EMI offer is available",
    "2-2": "{  \n\"isEligible\": 1,  \n\"bank\": \"AXIS\",  \n\"minAmount\": 2500  \n}\\*\\*\\*\\*"
  },
  "cols": 3,
  "rows": 3,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


</details>

## Request parameters

<details>/summary>Reference information</summary>

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

- `var1`: Bin or NET
- `var2`(first 6/8/9 digits of the card): 
  - **AXIS EMI**: 4453-3410-6587-6437
  - **ICICI EMI**: 4808-5578-4874-1463