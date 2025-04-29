---
title: Get Payment Details (Cryptogram)
excerpt: ''
api:
  file: storecard-8.json
  operationId: get_payment_details
deprecated: false
hidden: false
metadata:
  title: Get Payment Details (Cryptogram)
  description: >-
    Learn how to use the PayU Get Payment Details (Cryptogram) API to retrieve
    secure payment details, including cryptograms and token information. This
    guide provides detailed instructions, request parameters, and sample
    responses for efficient card management.
  keywords:
    - Get Payment Details API
    - ' cryptogram'
    - ' card details retrieval'
    - ' secure card payment details'
    - ' get payment details of tokenized card'
    - ' card management'
    - ' retrieve saved card payment details'
  robots: index
next:
  description: ''
---
This API is used to get the payment details of an existing card stored on PayU Vault so that you can use it with third-party tokenization. The payment details include the cryptogram, PAR, card number, card token, issuer token details and network token details as listed in the [Response Parameters table](#response-parameters) of this section.

HTTP Method: **POST**

<GENERALAPIsEnvironment />

<details><summary>Sample response</summary>

**Successful Scenario**

```plaintext
{
    "status": "1",
    "msg": "Instrument details",
    "details": {
        "one_click_status": "",
        "one_click_flow": "",
        "card_type": "VISA",
        "network_token": {
            "token_exp_yr": "2025",
            "token_value": "464XXX7450050615",
            "token_exp_mon": "01"
        },
        "trid": "400600",
        "card_mode": "",
        "token_refernce_id": "4776af84a5079512934417214171fd01",
        "card_no": "XXXXXXXXXXXX0615",
        "card_PAR": "V0010013021031409361532",
        "one_click_card_alias": "",
        "card_token": "60ac10XXX09d1965b7dae2",
        "card_name": "",
        "cryptogram": "/wAAAAoAtd1XnhwAmbHTgkUAAAA="
    }
}
```

**Failure Scenario**

```plaintext
{
"status": 0,
"msg": card not found
}
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
    "0-1": "The status of the response can be any of the following:  \n_ 1: Success  \n_. 2: Failure",
    "0-2": "1",
    "1-0": "msg",
    "1-1": "The description of the response whether the card details were stored successfully or not stored.",
    "1-2": "Instrument details",
    "2-0": "card details",
    "2-1": "(Array format) | The details are sent by PayU in Array format for the successful response. The next table describes the details in the Array format.",
    "2-2": ""
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

<details><summary>Reference info for request parameters</summary>

<KeyHashForGeneralParametersDescription />

</details>