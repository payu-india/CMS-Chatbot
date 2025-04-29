---
title: Get TDR API
excerpt: ''
api:
  file: general-33.json
  operationId: get_TDR
deprecated: false
hidden: false
metadata:
  title: Get TDR API
  description: >-
    The Get TDR API retrieves the Transaction Discount Rate (TDR) value of a
    transaction with PayU by providing the PayU ID of the transaction as input.
    The output includes the TDR value, with a sample request and response
    provided in the document.
  keywords:
    - Get Transaction Discount Rate API
    - Get TDR API
    - get_TDR command
    - get_TDR API Command
  robots: index
next:
  description: ''
---
The Get TDR API (**get_TDR** API) is used to get the Transaction Discount Rate (TDR) value of a transaction with PayU. It is a simple API for which you need to provide the PayU ID of the transaction as input and the TDR value is returned in the output, var1 is Payu id (mihpayid) of the transaction.

<GENERALAPIsEnvironment />

<details><summary>Sample request</summary>

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2"-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d"key=JP***g&command=get_TDR&var1=403993715521891555&hash=a0cf2d4ed3fb551388bd9e078f7ace8fb565d3240e06735cfc83330bb604b0f97a26a31160f1987af4ba5f78e126f400826a62d71337395e6e127b28a62b860d"
```

</details>

<details>  <summary>Sample response</summary>

**Success scenario**

```
{
      "status": 1,
      "msg": "Transaction Fetched Successfully",
      "TDR_details": {
            "TDR": 0
      }
}
```

**Failure scenario**

- If mihpayid is not found

```
{
      "status": 0,
      "msg": "Invalid PayU ID"
}
```

</details>

## Request parameters

<details>  <summary>Reference information for request parameters</summary>

<KeyHashForGeneralParametersDescription />

</details>

**Sample values**

Use the following sample values while trying out the API:

- `var1` (Payu ID/mihpayid): 403993715521891555