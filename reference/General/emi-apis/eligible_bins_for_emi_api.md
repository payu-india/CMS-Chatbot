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

![EMI Eligible BINs Flow](https://files.readme.io/2eaac64-emi_eligible_bins_flow.png)

You can post a request using any of the following methods:

* **Request without Bank Selection**: This is submitting API without bank name in var3 field.
* **Request with Bank Selection**: This is submitting API with bank name in var3 field so that you will get the details for the specified bank.

## Environment

| Environment            | URL                                                                                                  |
| :--------------------- | :--------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/merchant/postservice?form=2](https://test.payu.in/merchant/postservice?form=2) |
| Production Environment | [https://info.payu.in/merchant/postservice?form=2](https://info.payu.in/merchant/postservice?form=2) |

## Sample request

```bash
curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
-H "accept: application/json" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "key=JP***g&command=eligibleBinsForEMI&var1=Bin&var2=512345&hash=3c923a16606d07f12aa984487626abbc0981f540131f8bb0d24b6322c362089bbd4114d710129ce54128691956775352ac53e7d7943392959d37275c934245f2"
```

## Sample response

**Success Scenario**

On successful processing from PayU, the response is similar to the following:

```json
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

```json
{
    "status": 1,
    "msg": "Details fetched successfully",
    "details": {
        "isEligible": 0
    } 
}
```

## Response parameters

| **Parameter** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | **Example**                                            |
| :------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------- |
| status        | This parameter returns the status of web service call. The status can be any of the following:<ul><li>0 - If web service call failed.</li><li>1 - If web service call succeeded</li></ul>                                                                                                                                                                                                                                                                                                     |                                                        |
| msg           | This parameter returns whether the EMI details were fetched successfully or not found.                                                                                                                                                                                                                                                                                                                                                                                                        | Details fetched successfully                           |
| details       | The details of the EMI offer is displayed in a JSON format and it contains the following fields:<ul><li>**isEligible** - This parameter can be any of the following values:<ul><li>0 - If EMI offers are not available for the given card BIN.</li><li>1 - If EMI offers are available for the given card BIN.</li></ul></li><li>**bank** - The name of bank that corresponds to the given card BIN</li><li>**minAmount** - The minimum amount for which the EMI offer is available</li></ul> | `{"isEligible": 1, "bank": "AXIS", "minAmount": 2500}` |

## Request parameters

### Example values

Use the following sample values while trying out the API:

* `var1`: Bin or NET
* `var2` (first 6/8/9 digits of the card):
  * **AXIS EMI**: 4453-3410-6587-6437
  * **ICICI EMI**: 4808-5578-4874-1463