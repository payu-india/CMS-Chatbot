---
title: Getting Issuing Bank Down BINs API
excerpt: ''
api:
  file: bin-info-10.json
  operationId: GetIssuingBankDownBINs
deprecated: false
hidden: false
metadata:
  title: Getting Issuing Bank Down Bins
  description: >-
    The Getting Issuing Bank Down Bins API retrieves card BINs for banks
    experiencing downtime, with the ability to specify a specific bank or
    retrieve all banks in JSON format.
  keywords:
    - gettingIssuingBankDownBins API Command
    - Issuing Bank Down BINs API
    - Check issuing bank status API
    - Issuing bank downtime API
    - Bank outage verification API
    - API Command gettingIssuingBankDownBins
  robots: index
next:
  description: ''
---
The **Getting Issuing Bank Down Bins** API (**gettingIssuingBankDownBins**)  is used to retrieve the card BINs for all the banks that are observing either full downtime or partial downtime at an instance.

<GENERALAPIsEnvironment />

<details><summary>Sample request</summary>

```
curl -X POST "https://test.payu.in/merchant/postservice?form=2
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d

"key=JP***g&command=getIssuingBankDownBins&var1=ALLBD&var2=1&hash=efc4452469091d4d6061fcf6bce45c8116675972a89ddcba6bdd27dce613ca6e48e703e3ba7f6015ef128eda60ed61a3307795c5dd7e284a7691f0c6dc3812a8"
```

</details>

<details><summary>Sample response</summary>

```
[
      {
            "issuing_bank": "ALLBD",
            "status": 2,
            "title": "ALLAHABAD BANK",
            "bins_arr": [
                  "421337",
                  "608219",
                  "608218",
                  "608171",
                  "608102",
                  "607352",
                  "607137",
                  "607038",
                  "607091",
                  "607016",
                  "607117",
                  "430450",
                  "652204"
            ]
      }
]
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

<details><summary>Reference information for request parameters</summary>

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Reference",
    "0-0": "key",
    "0-1": "For more information on how to generate the Key and Salt, refer to any of the following:  \n  \n\\- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  \n  \n- **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)",
    "1-0": "hash",
    "1-1": "Hash logic for this API is:  \n`sha512(key\\|command\\|var1\\|salt) sha512\n`"
  },
  "cols": 2,
  "rows": 2,
  "align": [
    "left",
    "left"
  ]
}
[/block]


</details>

Use the following sample values while trying out the API:

**Example values**:

- `var1`: Pass "default" to get the downtime status of all banks or pass the bank codes (ex-AXISB) to get the downtime status of a specific bank.