---
title: EMI Calculator API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: EMI Calculator API version 2.0
  description: >-
    This document provides information on an API that can be used to display EMI
    plans and offers on checkout pages or product pages, allowing merchants to
    fetch EMI amounts, rates of interest, and total amounts to be paid across
    eligible banks.
  keywords:
    - EMI calculator API version 2.0
    - Calculate EMI API 2.0
    - ' EMI interest rate calculation API'
    - ' Loan EMI calculator API'
    - Get EMI According to Interest API version 2.0
  robots: index
next:
  description: ''
---
You can use this API to display the EMI plans along with all offers on the checkout page. This API may also be used to display the EMI plans on Product Page or any other screen the merchant may deem fit. You can use it for the following:

- Fetch EMI plans: You can use this API to fetch EMI Amounts, rate of interest, total amount to be paid across eligible banks.
- Fetch EMI plans for a particular bank
- Fetch EMI plan for a particular bank & tenure
- Fetch EMI plans with best offers applicable
- Fetch EMI plans with one offer applied
- Fetch EMI plans with SKU based offers

**Environment**

|                            |                                           |
| -------------------------- | ----------------------------------------- |
| **Test Environment**       | <https://apitest.payu.in/calculateEmi/v2> |
| **Production Environment** | <https://api.payu.in/calculateEmi/v2>     |

## Header parameters

| Parameter             | Example          |
| --------------------- | ---------------- |
| accept                | application/json |
| content-type          | application/json |
| x-credential-username | OADt8R           |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "amount  \n`mandatory`",
    "0-1": "This parameter must include the principal amount that needs to be converted into EMI.",
    "1-0": "additional_charges  \n`optional`",
    "1-1": "This parameter must include the convenience fee if the merchant wants to collect.",
    "2-0": "offer_key  \n`optional`",
    "2-1": "This parameter must contain the offer key for the transaction-level offer.",
    "3-0": "autoApplyOffer  \n`optional`",
    "3-1": "This parameter must be set to **true** if the merchant wants to apply best offer when no transaction offer keys specified.",
    "4-0": "skus  \n`optional`",
    "4-1": "This parameter must include the SKU data.",
    "5-0": "skus.skuAmount  \nmandatory",
    "5-1": "This parameter must contain the amount per SKU.",
    "6-0": "skus.quantity  \nmandatory",
    "6-1": "This parameter must contain the SKU quantity.",
    "7-0": "skus.skuName  \nmandatory",
    "7-1": "This parameter must contain the name of SKU.",
    "8-0": "skus.offerKeys  \n`optional`",
    "8-1": "This parameter must contain the offer key for SKU.",
    "9-0": "skus.autoApplyOffer",
    "9-1": "This parameter must be set to **true** if the merchant wants to apply best offer when no SKU offer keys specified..",
    "10-0": "bankCodes  \n`optional`",
    "10-1": "This parameter must contain the bank codes for filtering.",
    "11-0": "emiCodes  \n`optional`",
    "11-1": "This parameter must contain the EMI  bankcodes for filtering.",
    "12-0": "disableOverrideNceConfig  \n`optional`",
    "12-1": "This parameter must be set to **true ** PayU will not consider NCE through merchant parameters for the merchant."
  },
  "cols": 2,
  "rows": 13,
  "align": [
    null,
    null
  ]
}
[/block]


## Sample request

```curl
curl --location --request POST 'https://apitest.payu.in/calculateEmi/v2' \
--header 'x-credential-username: smsplus' \
--header 'Content-Type: application/json' \
--data-raw '{
    "txnAmount": 10000,
    "additionalCharges": 0,
    "offerKeys": null,
    "autoApplyOffer": true,
    "bankCodes":null,
    "emiCodes":null,
    "disableOverrideNceConfig": true,
    "skus": [
        {
            "skuId": "Product1",
            "skuAmount": 8000,
            "quantity": 1,
            "offerKeys": null,
            "autoApplyOffer": false
        },
        {
            "skuId": "Product2",
            "skuAmount": 1000,
            "quantity": 2,
            "offerKeys": null,
            "autoApplyOffer": false
        }
    ]
}'

```

## Response parameters

| Field                | Description                                                                                                                                                                                   | Example  |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| message              | Response message indicating success or failure of the API call.                                                                                                                               | Success  |
| status               | Status code indicating the result of the API call (1 for success, 0 for failure).                                                                                                             | 1        |
| result               | The result is in JSON format with an array of EMI options. For example, EMI6, EMI12, EMI18, etc. For more information, refer to [EMI JSON fields description](#emi-json-fields-description) . | 10000.0  |
| nceDiscount.total    | In NCE (No-Cost EMI), total non-cash equivalent discount amount.                                                                                                                              | 1266.78  |
| nceDiscount.instant  | In NCE (No-Cost EMI), instant non-cash equivalent discount applied.                                                                                                                           | 1266.78  |
| nceDiscount.cashback | In NCE (No-Cost EMI), cashback from non-cash equivalent discount.                                                                                                                             | 0.0      |
| sku                  | SKU details in a JSON format. For more information, refer to [sku JSON fields description](#sku-json-fields-description)                                                                      | Product1 |
| totalPayableAmount   | Total amount payable after discounts and EMI.                                                                                                                                                 | 10000.0  |
| nceDiscountAmount    | Total non-cash equivalent discount amount applied.                                                                                                                                            | 1266.78  |
| revisedPrincipal     | Revised principal loan amount.                                                                                                                                                                | 10000.0  |
| subventionAmount     | Subvention amount considered for the transaction.                                                                                                                                             | 10000.0  |
| gstSubvention        | Indicates if GST is included in subvention.                                                                                                                                                   | true     |
| nceViaConfig         | Indicates if NCE discount is via configuration.                                                                                                                                               | true     |
| bankCode             | Bank code of the bank providing EMI. For more information, refer to [EMI Codes](doc:emi-codes).                                                                                               | YESB     |
| emi_value            | EMI value calculated.                                                                                                                                                                         | 555.55   |
| emi_interest_paid    | Total interest paid over the EMI tenure.                                                                                                                                                      | 1266.78  |

### EMI JSON fields description

| Field                  | Description                                                         | Example     |
| ---------------------- | ------------------------------------------------------------------- | ----------- |
| transactionAmount      | The total transaction amount for which the EMI is calculated.       | 10000.0     |
| payBackAmount          | The amount to be paid back over the EMI tenure, including interest. | 0.0         |
| emiAmount              | The EMI amount to be paid in each installment.                      | 555.56      |
| additionalCost         | Any additional costs apart from the EMI amount.                     | "0.0"       |
| emiMdrNote             | Merchant discount rate note related to EMI.                         | 0.0         |
| emiBankInterest        | Interest rate charged by the bank for the EMI.                      | 15.0        |
| bankRate               | Bank's rate for the EMI calculation.                                | 0.0         |
| bankCharge             | Additional bank charges associated with the EMI.                    | 0.0         |
| amount                 | Amount per EMI installment including any charges.                   | 555.56      |
| cardType               | Type of card used for the transaction.                              | credit card |
| tenure                 | Duration of the EMI plan.                                           | 18 months   |
| loanAmount             | Principal loan amount for EMI.                                      | 10000.0     |
| offerKeys              | Keys associated with any offers applied.                            | null        |
| offerDiscount.total    | Total discount amount provided as part of the offer.                | 0.0         |
| offerDiscount.instant  | Instant discount amount applied.                                    | 0.0         |
| offerDiscount.cashback | Cashback amount provided as part of the offer.                      | 0.0         |

### sku JSON fields description

| Field                  | Description                                        | Example  |
| ---------------------- | -------------------------------------------------- | -------- |
| skuId                  | SKU identifier for the product.                    | Product1 |
| amountPerSku           | Amount per SKU for the product.                    | 8000.0   |
| amount                 | Total amount for the SKUs provided.                | 8000.0   |
| quantity               | Quantity of the SKU.                               | 1        |
| offerKeys              | Keys associated with any offers on SKU.            | null     |
| emiAmount              | EMI amount specific to SKU.                        | 444.44   |
| emiBankInterest        | EMI bank interest for SKU.                         | 15.0     |
| emiValue               | EMI value calculated for SKU.                      | 444.44   |
| emiInterestPaid        | Interest paid for EMI on SKU.                      | 1013.42  |
| offerDiscount.total    | Total offer discount on SKU.                       | 0.0      |
| offerDiscount.instant  | Instant offer discount on SKU.                     | 0.0      |
| offerDiscount.cashback | Cashback offer on SKU.                             | 0.0      |
| nceDiscount.total      | Total non-cash equivalent discount on SKU.         | 1013.42  |
| nceDiscount.instant    | Instant non-cash equivalent discount on SKU.       | 1013.42  |
| nceDiscount.cashback   | Cashback from non-cash equivalent discount on SKU. | 0.0      |
| totalPayableAmount     | Total amount payable for the SKU.                  | 7999.92  |
| nceDiscountAmount      | NCE discount amount applied on SKU.                | 1013.42  |
| subventionAmount       | Subvention amount for SKU.                         | 8000.0   |
| revisedPrincipal       | Revised principal amount for SKU.                  | 8000.0   |
| additionalCharge       | Additional charge applicable to SKU.               | 0.0      |

## Sample response

```
{
    "message": "Success",
    "status": 1,
    "result": {
        "YES": {
            "EMIY18": {
                "transactionAmount": 10000.0,
                "payBackAmount": 0.0,
                "emiAmount": 555.56,
                "additionalCost": "0.0",
                "emiMdrNote": 0.0,
                "emiBankInterest": 15.0,
                "bankRate": 0.0,
                "bankCharge": 0.0,
                "amount": 555.56,
                "cardType": "credit card",
                "tenure": "18 months",
                "loanAmount": 10000.0,
                "offerKeys": null,
                "offerDiscount": {
                    "total": 0.0,
                    "instant": 0.0,
                    "cashback": 0.0
                },
                "nceDiscount": {
                    "total": 1266.78,
                    "instant": 1266.78,
                    "cashback": 0.0
                },
                "sku": [
                    {
                        "skuId": "Product1",
                        "amountPerSku": 8000.0,
                        "amount": 8000.0,
                        "quantity": 1,
                        "offerKeys": null,
                        "emiAmount": 444.44,
                        "emiBankInterest": 15.0,
                        "emiValue": 444.44,
                        "emiInterestPaid": 1013.42,
                        "offerDiscount": {
                            "total": 0.0,
                            "instant": 0.0,
                            "cashback": 0.0
                        },
                        "nceDiscount": {
                            "total": 1013.42,
                            "instant": 1013.42,
                            "cashback": 0.0
                        },
                        "totalPayableAmount": 7999.92,
                        "nceDiscountAmount": 1013.42,
                        "subventionAmount": 8000.0,
                        "revisedPrincipal": 8000.0,
                        "additionalCharge": 0.0
                    },
                    {
                        "skuId": "Product2",
                        "amountPerSku": 1000.0,
                        "amount": 2000.0,
                        "quantity": 2,
                        "offerKeys": null,
                        "emiAmount": 111.11,
                        "emiBankInterest": 15.0,
                        "emiValue": 111.11,
                        "emiInterestPaid": 253.36,
                        "offerDiscount": {
                            "total": 0.0,
                            "instant": 0.0,
                            "cashback": 0.0
                        },
                        "nceDiscount": {
                            "total": 1266.78,
                            "instant": 1266.78,
                            "cashback": 0.0
                        },
                        "totalPayableAmount": 1999.98,
                        "nceDiscountAmount": 253.36,
                        "subventionAmount": 2000.0,
                        "revisedPrincipal": 2000.0,
                        "additionalCharge": 0.0
                    }
                ],
                "totalPayableAmount": 10000.0,
                "nceDiscountAmount": 1266.78,
                "revisedPrincipal": 10000.0,
                "subventionAmount": 10000.0,
                "gstSubvention": true,
                "nceViaConfig": true,
                "bankCode": "YESB",
                "emi_value": 555.55,
                "emi_interest_paid": 1266.78
            },

```