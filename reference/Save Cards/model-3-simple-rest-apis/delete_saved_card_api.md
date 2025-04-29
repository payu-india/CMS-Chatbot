---
title: Delete a Saved Card API
excerpt: ''
api:
  file: storecard-2.json
  operationId: delete_payment_instrument
deprecated: false
hidden: false
metadata:
  title: Delete Saved Card API
  description: >-
    Learn how to use the PayU Delete Saved Card API to securely remove stored
    card details. This guide provides detailed instructions, request parameters,
    and sample responses for efficient card management."
  keywords:
    - Delete Saved Card API
    - ' saved card removal'
    - ' delete secure card'
    - ' delete tokenized cards'
    - ' card management'
    - ' delete saved card details'
  robots: index
next:
  description: ''
---
This API is used to delete an existing card stored on PayU Vault.

HTTP Method: **POST**

<GENERALAPIsEnvironment />

<details><summary>Sample Response</summary>

- On successful deletion

```plaintext
{
        status: 1,
        msg: "My_card card deleted successfully",
}
```

- On failure of deletion

```plaintext
{
"status": 0,
"msg": card not found
}
```

</details>

<details> <summary>Response parameters</summary>

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "status",
    "0-1": "The status of the response can be any of the following:  \n   -** 1**: Success  \n  \n- **0**: Failure",
    "0-2": "1",
    "1-0": "msg",
    "1-1": "The description of the response whether the card details were deleted successfully or not deleted.",
    "1-2": "My\\_card deleted successfully"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


</details>

## Request Parameters

<details> <summary>Reference info for request parameters</summary>

<KeyHashForGeneralParametersDescription />

</details>