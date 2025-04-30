---
title: Get EMI Amount according to Interest API
excerpt: ''
api:
  file: emi-apis-11.json
  operationId: GetEMIAccordingtoInterest
deprecated: false
hidden: false
metadata:
  title: ''
  description: >-
    The document describes the Get EMI Amount According to Interest API, which
    is used to retrieve EMI interest bank rates for enabled EMIs. It provides
    sample requests, responses, and response parameters such as transaction
    amount, loan amount, EMI amount, additional costs, bank rate, and more.
  keywords:
    - getEmiAmountAccordingToInterest
    - Get EMI Amount According to Interest
  robots: index
next:
  description: ''
---
# Get EMI Amount According to Interest API

The **Get EMI Amount According to Interest** API (**getEmiAmountAccordingToInterest** API) is used to get the EMI interest bank rates for all the enabled EMIs.

## Sample request

```bash
curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
-H "accept: application/json" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "key=JP***g&command=getEmiAmountAccordingToInterest&var1=20000&hash=3b16384427372f658244a106258790df9ed601e3c1dcd1f43d08f7e616bfe907f095947491baa3ec8629d33b3903e8b1e0a1872aa009c5f5c34b06466311dc95&hash="
```

## Sample response

```json
{
  "7": {
    "EMIA3": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 33333.33,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 33333.33,
      "card_type": "credit card",
      "emi_value": 34226.15,
      "emi_interest_paid": 2678.44,
      "tenure": "03 months"
    },
    /* Additional entries omitted for brevity */
  }
}
```

## Response parameters

The response includes the JSON array and each JSON has the fields as described in the following table:

> 📘 **Reference:**
>
> In the JSON Array of the response of the **Get EMI Amount According to Interest** API, the code displayed for the each issuer (at the beginning of each object). The significance of these codes are described in [EMI Options for Get EMI According to Interest API](ref:emi-options-for-get-emi-according-to-interest-api).

| **Parameter**       | **Description**                                                                                                     | **Example** |
| :------------------ | :------------------------------------------------------------------------------------------------------------------ | :---------- |
| transactionAmount   | The transaction amount that is will be converted into EMI.                                                          | 20000       |
| loanAmount          | The loan amount that needs to be converted as EMI.                                                                  | 20000       |
| emiAmount           | The amount that needs to be converted as EMI.                                                                       | 20000       |
| additionalCost      | The processing fee or additional cost for processing the EMI excluding interest.                                    | 0.00        |
| emiMdrNote          | The EMI Merchant Discount Rate (MDR) note if any for the transaction.                                               | 0.25        |
| bankRate            | The interest rate in percentage for the EMI. This is excluding the processing fee. For example, 12%, 18%, 24%, etc. | 13          |
| bankCharge          | The bank charges for the EMI transaction.                                                                           | 0           |
| amount              | The principal part of the EMI.                                                                                      | 6666.67     |
| card\_type          | The card type used by the customer and can be any of the following:  \* credit card  \* debit card                  | credit card |
| emi\_value          | The amount to be paid per EMI.                                                                                      | 6811.63     |
| emi\_interest\_paid | The total interest paid for all the EMIs.                                                                           | 434.89      |
| tenure              | The tenure for the EMI in months. For example, 3, 6, 12, 24, 36, etc.                                               | 3           |

## Request parameters

### Additional information

Use the following sample values while trying out the API:

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Reference
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key
      </td>

      <td>
        For more information on how to generate the Key and Salt, refer to any of the following:  **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
      </td>
    </tr>

    <tr>
      <td>
        hash
      </td>

      <td>
        Hash logic for this API is:
        `sha512(key\|command\|var1\|salt) sha512 `
        For more information about the hash generation process, refer to [Encryption of Request.](/docs/hashing-request-and-response)
      </td>
    </tr>

    <tr>
      <td>
        var1
      </td>

      <td>
        For JSON fields description, refer to [Additional Info for General APIs](ref:addl-info-general-apis)
      </td>
    </tr>
  </tbody>
</Table>

**Example values**:

* `var1`: Any amount.