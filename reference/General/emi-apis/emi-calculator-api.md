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

* Fetch EMI plans: You can use this API to fetch EMI Amounts, rate of interest, total amount to be paid across eligible banks.
* Fetch EMI plans for a particular bank
* Fetch EMI plan for a particular bank & tenure
* Fetch EMI plans with best offers applicable
* Fetch EMI plans with one offer applied
* Fetch EMI plans with SKU based offers

## Environment

| Environment                | URL                                                                                |
| -------------------------- | ---------------------------------------------------------------------------------- |
| **Test Environment**       | [https://apitest.payu.in/calculateEmi/v2](https://apitest.payu.in/calculateEmi/v2) |
| **Production Environment** | [https://api.payu.in/calculateEmi/v2](https://api.payu.in/calculateEmi/v2)         |

## Header parameters

| Parameter             | Example          |
| --------------------- | ---------------- |
| accept                | application/json |
| content-type          | application/json |
| x-credential-username | OADt8R           |

## Request parameters

| Parameter                                           | Description                                                                                                                |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| txnAmount<br /><code>mandatory</code>               | This parameter must include the principal amount that needs to be converted into EMI.                                      |
| additional_charges<br /><code>optional</code>       | This parameter must include the convenience fee if the merchant wants to collect.                                          |
| offerKeys<br /><code>optional</code>                | This parameter must contain the offer key for the transaction-level offer.                                                 |
| autoApplyOffer<br /><code>optional</code>           | This parameter must be set to **true** if the merchant wants to apply best offer when no transaction offer keys specified. |
| skus<br /><code>optional</code>                     | This parameter must include the SKU data.                                                                                  |
| skus.skuAmount<br /><code>mandatory</code>          | This parameter must contain the amount per SKU.                                                                            |
| skus.quantity<br /><code>mandatory</code>           | This parameter must contain the SKU quantity.                                                                              |
| skus.skuId<br /><code>mandatory</code>              | This parameter must contain the name of SKU.                                                                               |
| skus.offerKeys<br /><code>optional</code>           | This parameter must contain the offer key for SKU.                                                                         |
| skus.autoApplyOffer                                 | This parameter must be set to **true** if the merchant wants to apply best offer when no SKU offer keys specified.         |
| bankCodes<br /><code>optional</code>                | This parameter must contain the bank codes for filtering.                                                                  |
| emiCodes<br /><code>optional</code>                 | This parameter must contain the EMI bankcodes for filtering.                                                               |
| disableOverrideNceConfig<br /><code>optional</code> | This parameter must be set to **true** PayU will not consider NCE through merchant parameters for the merchant.            |

## Sample request

```bash
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

| Field                | Description                                                                                                                                                                                                                                              | Example  |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------- |
| message              | Response message indicating success or failure of the API call.                                                                                                                                                                                          | Success  |
| status               | Status code indicating the result of the API call (1 for success, 0 for failure).                                                                                                                                                                        | 1        |
| result               | The result is in JSON format with an array of EMI options. For example, EMI6, EMI12, EMI18, etc. For more information, refer to <a href="https://docs.payu.in/reference/emi-calculator-api#emi-json-fields-description">EMI JSON fields description</a>. | 10000.0  |
| nceDiscount.total    | In NCE (No-Cost EMI), total non-cash equivalent discount amount.                                                                                                                                                                                         | 1266.78  |
| nceDiscount.instant  | In NCE (No-Cost EMI), instant non-cash equivalent discount applied.                                                                                                                                                                                      | 1266.78  |
| nceDiscount.cashback | In NCE (No-Cost EMI), cashback from non-cash equivalent discount.                                                                                                                                                                                        | 0.0      |
| sku                  | SKU details in a JSON format. For more information, refer to <a href="https://docs.payu.in/reference/emi-calculator-api#sku-json-fields-description">sku JSON fields description</a>.                                                                    | Product1 |
| totalPayableAmount   | Total amount payable after discounts and EMI.                                                                                                                                                                                                            | 10000.0  |
| nceDiscountAmount    | Total non-cash equivalent discount amount applied.                                                                                                                                                                                                       | 1266.78  |
| revisedPrincipal     | Revised principal loan amount.                                                                                                                                                                                                                           | 10000.0  |
| subventionAmount     | Subvention amount considered for the transaction.                                                                                                                                                                                                        | 10000.0  |
| gstSubvention        | Indicates if GST is included in subvention.                                                                                                                                                                                                              | true     |
| nceViaConfig         | Indicates if NCE discount is via configuration.                                                                                                                                                                                                          | true     |
| bankCode             | Bank code of the bank providing EMI. For more information, refer to <a href="https://docs.payu.in/docs/emi-codes">EMI Codes</a>.                                                                                                                         | YESB     |
| emi_value            | EMI value calculated.                                                                                                                                                                                                                                    | 555.55   |
| emi_interest_paid    | Total interest paid over the EMI tenure.                                                                                                                                                                                                                 | 1266.78  |

### EMI JSON fields description

| Field                  | Description                                                         | Example     |
| :--------------------- | :------------------------------------------------------------------ | :---------- |
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
| :--------------------- | :------------------------------------------------- | :------- |
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

### General

```json
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
            }
        }
    }
}
```

### With Instant Discount + NCE Discount (Single SKU)

```json
{
    "message": "Success",
    "status": 1,
    "result": {
        "IDBI": {
            "IDBI30": {
                "transactionAmount": 40000.0,
                "payBackAmount": 0.0,
                "emiAmount": 1333.33,
                "additionalCost": "0.0",
                "emiMdrNote": 0.0,
                "emiBankInterest": 13.0,
                "bankRate": 0.0,
                "bankCharge": 0.0,
                "amount": 1333.33,
                "cardType": "credit card",
                "tenure": "30 months",
                "loanAmount": 40000.0,
                "offerDiscount": {
                    "total": 0.0,
                    "instant": 0.0,
                    "cashback": 0.0
                },
                "nceDiscount": {
                    "total": 0.0,
                    "instant": 0.0,
                    "cashback": 0.0
                },
                "sku": [
                    {
                        "skuId": "111",
                        "amountPerSku": 40000.0,
                        "amount": 40000.0,
                        "quantity": 1,
                        "offerKeys": [
                            "NceBaseSku@zzy2kJgYsEkE",
                            "InstantEmi@DcLwZ5zV8og0"
                        ],
                        "emiAmount": 1300.0,
                        "emiBankInterest": 13.0,
                        "emiValue": 1300.0,
                        "emiInterestPaid": 5854.96,
                        "offerDiscount": {
                            "total": 1000.0,
                            "instant": 1000.0,
                            "cashback": 0.0
                        },
                        "nceDiscount": {
                            "total": 5854.96,
                            "instant": 5854.96,
                            "cashback": 0.0
                        },
                        "totalPayableAmount": 39000.0,
                        "nceDiscountAmount": 5854.96,
                        "subventionAmount": 39000.0,
                        "revisedPrincipal": 39000.0,
                        "additionalCharge": 0.0,
                        "lceDiscount": {
                            "total": 0.0,
                            "instant": 0.0,
                            "cashback": 0.0
                        }
                    }
                ],
                "totalPayableAmount": 39000.0,
                "nceDiscountAmount": 5854.96,
                "revisedPrincipal": 39000.0,
                "subventionAmount": 39000.0,
                "gstSubvention": false,
                "bankCode": "IDBI",
                "lceDiscount": {
                    "total": 0.0,
                    "instant": 0.0,
                    "cashback": 0.0
                },
                "notification": {
                    "tncLink": null,
                    "tncText": null
                },
                "emi_value": 1300.0,
                "emi_interest_paid": 5854.96
            },
            "IDBI09": {
                "transactionAmount": 40000.0,
                "payBackAmount": 0.0,
                "emiAmount": 4444.44,
                "additionalCost": "0.0",
                "emiMdrNote": 0.0,
                "emiBankInterest": 13.0,
                "bankRate": 0.0,
                "bankCharge": 0.0,
                "amount": 4444.44,
                "cardType": "credit card",
                "tenure": "09 months",
                "loanAmount": 40000.0,
                "offerDiscount": {
                    "total": 0.0,
                    "instant": 0.0,
                    "cashback": 0.0
                },
                "nceDiscount": {
                    "total": 0.0,
                    "instant": 0.0,
                    "cashback": 0.0
                },
                "sku": [
                    {
                        "skuId": "111",
                        "amountPerSku": 40000.0,
                        "amount": 40000.0,
                        "quantity": 1,
                        "offerKeys": [
                            "NceBaseSku@zzy2kJgYsEkE",
                            "InstantEmi@DcLwZ5zV8og0"
                        ],
                        "emiAmount": 4333.33,
                        "emiBankInterest": 13.0,
                        "emiValue": 4333.33,
                        "emiInterestPaid": 2031.24,
                        "offerDiscount": {
                            "total": 1000.0,
                            "instant": 1000.0,
                            "cashback": 0.0
                        },
                        "nceDiscount": {
                            "total": 2031.24,
                            "instant": 2031.24,
                            "cashback": 0.0
                        },
                        "totalPayableAmount": 38999.97,
                        "nceDiscountAmount": 2031.24,
                        "subventionAmount": 39000.0,
                        "revisedPrincipal": 39000.0,
                        "additionalCharge": 0.0,
                        "lceDiscount": {
                            "total": 0.0,
                            "instant": 0.0,
                            "cashback": 0.0
                        }
                    }
                ],
                "totalPayableAmount": 39000.0,
                "nceDiscountAmount": 2031.24,
                "revisedPrincipal": 39000.0,
                "subventionAmount": 39000.0,
                "gstSubvention": false,
                "bankCode": "IDBI",
                "lceDiscount": {
                    "total": 0.0,
                    "instant": 0.0,
                    "cashback": 0.0
                },
                "notification": {
                    "tncLink": null,
                    "tncText": null
                },
                "emi_value": 4333.33,
                "emi_interest_paid": 2031.24
            },
            "IDBI18": {
                "transactionAmount": 40000.0,
                "payBackAmount": 0.0,
                "emiAmount": 2222.22,
                "additionalCost": "0.0",
                "emiMdrNote": 0.0,
                "emiBankInterest": 13.0,
                "bankRate": 0.0,
                "bankCharge": 0.0,
                "amount": 2222.22,
                "cardType": "credit card",
                "tenure": "18 months",
                "loanAmount": 40000.0,
                "offerDiscount": {
                    "total": 0.0,
                    "instant": 0.0,
                    "cashback": 0.0
                },
                "nceDiscount": {
                    "total": 0.0,
                    "instant": 0.0,
                    "cashback": 0.0
                },
                "sku": [
                    {
                        "skuId": "111",
                        "amountPerSku": 40000.0,
                        "amount": 40000.0,
                        "quantity": 1,
                        "offerKeys": [
                            "NceBaseSku@zzy2kJgYsEkE",
                            "InstantEmi@DcLwZ5zV8og0"
                        ],
                        "emiAmount": 2166.67,
                        "emiBankInterest": 13.0,
                        "emiValue": 2166.67,
                        "emiInterestPaid": 3739.6,
                        "offerDiscount": {
                            "total": 1000.0,
                            "instant": 1000.0,
                            "cashback": 0.0
                        },
                        "nceDiscount": {
                            "total": 3739.6,
                            "instant": 3739.6,
                            "cashback": 0.0
                        },
                        "totalPayableAmount": 39000.06,
                        "nceDiscountAmount": 3739.6,
                        "subventionAmount": 39000.0,
                        "revisedPrincipal": 39000.0,
                        "additionalCharge": 0.0,
                        "lceDiscount": {
                            "total": 0.0,
                            "instant": 0.0,
                            "cashback": 0.0
                        }
                    }
                ],
                "totalPayableAmount": 39000.0,
                "nceDiscountAmount": 3739.6,
                "revisedPrincipal": 39000.0,
                "subventionAmount": 39000.0,
                "gstSubvention": false,
                "bankCode": "IDBI",
                "lceDiscount": {
                    "total": 0.0,
                    "instant": 0.0,
                    "cashback": 0.0
                },
                "notification": {
                    "tncLink": null,
                    "tncText": null
                },
                "emi_value": 2166.67,
                "emi_interest_paid": 3739.6
            }
        }
    }
}
```

### With Instant Discount + NCE Discount (Multi SKU)

```json
{
    "message": "Success",
    "status": 1,
    "result": {
        "IDBI": {
            "IDBI18": {
                "transactionAmount": 40000.0,
                "payBackAmount": 0.0,
                "emiAmount": 2222.22,
                "additionalCost": "0.0",
                "emiMdrNote": 0.0,
                "emiBankInterest": 13.0,
                "bankRate": 0.0,
                "bankCharge": 0.0,
                "amount": 2222.22,
                "cardType": "credit card",
                "tenure": "18 months",
                "loanAmount": 40000.0,
                "offerDiscount": {
                    "total": 0.0,
                    "instant": 0.0,
                    "cashback": 0.0
                },
                "nceDiscount": {
                    "total": 0.0,
                    "instant": 0.0,
                    "cashback": 0.0
                },
                "sku": [
                    {
                        "skuId": "111",
                        "amountPerSku": 20000.0,
                        "amount": 20000.0,
                        "quantity": 1,
                        "offerKeys": [
                            "NceBaseSku@zzy2kJgYsEkE",
                            "InstantEmi@DcLwZ5zV8og0"
                        ],
                        "emiAmount": 1055.56,
                        "emiBankInterest": 13.0,
                        "emiValue": 1055.56,
                        "emiInterestPaid": 1821.86,
                        "offerDiscount": {
                            "total": 1000.0,
                            "instant": 1000.0,
                            "cashback": 0.0
                        },
                        "nceDiscount": {
                            "total": 1821.86,
                            "instant": 1821.86,
                            "cashback": 0.0
                        },
                        "totalPayableAmount": 19000.079999999998,
                        "nceDiscountAmount": 1821.86,
                        "subventionAmount": 19000.0,
                        "revisedPrincipal": 19000.0,
                        "additionalCharge": 0.0,
                        "lceDiscount": {
                            "total": 0.0,
                            "instant": 0.0,
                            "cashback": 0.0
                        }
                    },
                    {
                        "skuId": "222",
                        "amountPerSku": 20000.0,
                        "amount": 20000.0,
                        "quantity": 1,
                        "offerKeys": [
                            "NceBaseSku@zzy2kJgYsEkE",
                            "InstantEmi@DcLwZ5zV8og0"
                        ],
                        "emiAmount": 1055.56,
                        "emiBankInterest": 13.0,
                        "emiValue": 1055.56,
                        "emiInterestPaid": 1821.86,
                        "offerDiscount": {
                            "total": 1000.0,
                            "instant": 1000.0,
                            "cashback": 0.0
                        },
                        "nceDiscount": {
                            "total": 1821.86,
                            "instant": 1821.86,
                            "cashback": 0.0
                        },
                        "totalPayableAmount": 19000.079999999998,
                        "nceDiscountAmount": 1821.86,
                        "subventionAmount": 19000.0,
                        "revisedPrincipal": 19000.0,
                        "additionalCharge": 0.0,
                        "lceDiscount": {
                            "total": 0.0,
                            "instant": 0.0,
                            "cashback": 0.0
                        }
                    }
                ],
                "totalPayableAmount": 38000.0,
                "nceDiscountAmount": 3643.72,
                "revisedPrincipal": 38000.0,
                "subventionAmount": 38000.0,
                "gstSubvention": false,
                "bankCode": "IDBI",
                "lceDiscount": {
                    "total": 0.0,
                    "instant": 0.0,
                    "cashback": 0.0
                },
                "notification": {
                    "tncLink": null,
                    "tncText": null
                },
                "emi_value": 2111.12,
                "emi_interest_paid": 3643.72
            },
            "IDBI06": {
                "transactionAmount": 40000.0,
                "payBackAmount": 0.0,
                "emiAmount": 6666.67,
                "additionalCost": "0.0",
                "emiMdrNote": 0.0,
                "emiBankInterest": 13.0,
                "bankRate": 0.0,
                "bankCharge": 0.0,
                "amount": 6666.67,
                "cardType": "credit card",
                "tenure": "06 months",
                "loanAmount": 40000.0,
                "offerDiscount": {
                    "total": 0.0,
                    "instant": 0.0,
                    "cashback": 0.0
                },
                "nceDiscount": {
                    "total": 0.0,
                    "instant": 0.0,
                    "cashback": 0.0
                },
                "sku": [
                    {
                        "skuId": "111",
                        "amountPerSku": 20000.0,
                        "amount": 20000.0,
                        "quantity": 1,
                        "offerKeys": [
                            "NceBaseSku@zzy2kJgYsEkE",
                            "InstantEmi@DcLwZ5zV8og0"
                        ],
                        "emiAmount": 3166.67,
                        "emiBankInterest": 13.0,
                        "emiValue": 3166.67,
                        "emiInterestPaid": 700.1,
                        "offerDiscount": {
                            "total": 1000.0,
                            "instant": 1000.0,
                            "cashback": 0.0
                        },
                        "nceDiscount": {
                            "total": 700.1,
                            "instant": 700.1,
                            "cashback": 0.0
                        },
                        "totalPayableAmount": 19000.02,
                        "nceDiscountAmount": 700.1,
                        "subventionAmount": 19000.0,
                        "revisedPrincipal": 19000.0,
                        "additionalCharge": 0.0,
                        "lceDiscount": {
                            "total": 0.0,
                            "instant": 0.0,
                            "cashback": 0.0
                        }
                    },
                    {
                        "skuId": "222",
                        "amountPerSku": 20000.0,
                        "amount": 20000.0,
                        "quantity": 1,
                        "offerKeys": [
                            "NceBaseSku@zzy2kJgYsEkE",
                            "InstantEmi@DcLwZ5zV8og0"
                        ],
                        "emiAmount": 3166.67,
                        "emiBankInterest": 13.0,
                        "emiValue": 3166.67,
                        "emiInterestPaid": 700.1,
                        "offerDiscount": {
                            "total": 1000.0,
                            "instant": 1000.0,
                            "cashback": 0.0
                        },
                        "nceDiscount": {
                            "total": 700.1,
                            "instant": 700.1,
                            "cashback": 0.0
                        },
                        "totalPayableAmount": 19000.02,
                        "nceDiscountAmount": 700.1,
                        "subventionAmount": 19000.0,
                        "revisedPrincipal": 19000.0,
                        "additionalCharge": 0.0,
                        "lceDiscount": {
                            "total": 0.0,
                            "instant": 0.0,
                            "cashback": 0.0
                        }
                    }
                ],
                "totalPayableAmount": 38000.0,
                "nceDiscountAmount": 1400.2,
                "revisedPrincipal": 38000.0,
                "subventionAmount": 38000.0,
                "gstSubvention": false,
                "bankCode": "IDBI",
                "lceDiscount": {
                    "total": 0.0,
                    "instant": 0.0,
                    "cashback": 0.0
                },
                "notification": {
                    "tncLink": null,
                    "tncText": null
                },
                "emi_value": 6333.34,
                "emi_interest_paid": 1400.2
            }
        }
    }
}
```

<br />