---
title: EMI Options for Get EMI According to Interest API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The following codes are used to indicate the issuer or bank name in the response of the Get EMI According to Interest API. For example, **7** is displayed for Axis Bank in the following response for Credit Card BIN:

```
{
      "7": {
            "EMIA3": {
                  "transactionAmount": 20000,
                  "paybackAmount": 0,
                  "loanAmount": 20000,
                  "emiAmount": 6666.67,
                  "additionalCost": "0.00",
                  "emiMdrNote": null,
                  "emiBankInterest": 13,
                  "bankRate": null,
                  "bankCharge": 0,
                  "amount": 6666.67,
                  "card_type": "credit card",
                  "emi_value": 6811.63,
                  "emi_interest_paid": 434.89,
                  "tenure": "03 months"
            },
            "EMIA6": {
                  "transactionAmount": 20000,
                  "paybackAmount": 0,
                  "loanAmount": 20000,
                  "emiAmount": 3333.33,
                  "additionalCost": "0.00",
                  "emiMdrNote": null,
                  "emiBankInterest": 13,
                  "bankRate": null,
                  "bankCharge": 0,
                  "amount": 3333.33,
                  "card_type": "credit card",
                  "emi_value": 3460.86,
                  "emi_interest_paid": 765.14,
                  "tenure": "06 months"
            },
            "EMIA9": {
                  "transactionAmount": 20000,
                  "paybackAmount": 0,
                  "loanAmount": 20000,
                  "emiAmount": 2222.22,
                  "additionalCost": "0.00",
                  "emiMdrNote": null,
                  "emiBankInterest": 14,
                  "bankRate": null,
                  "bankCharge": 0,
                  "amount": 2222.22,
                  "card_type": "credit card",
                  "emi_value": 2353.86,
                  "emi_interest_paid": 1184.71,
                  "tenure": "09 months"
            },
            "EMIA12": {
                  "transactionAmount": 20000,
                  "paybackAmount": 0,
                  "loanAmount": 20000,
                  "emiAmount": 1666.67,
                  "additionalCost": "0.00",
                  "emiMdrNote": null,
                  "emiBankInterest": 14,
                  "bankRate": null,
                  "bankCharge": 0,
                  "amount": 1666.67,
                  "card_type": "credit card",
                  "emi_value": 1795.74,
                  "emi_interest_paid": 1548.91,
                  "tenure": "12 months"
            }
      },
      "AXISD": {
            "AXISD03": {
                  "transactionAmount": 20000,
                  "paybackAmount": 0,
                  "loanAmount": 20000,
                  "emiAmount": 6666.67,
                  "additionalCost": "0.00",
                  "emiMdrNote": null,
                  "emiBankInterest": 14,
                  "bankRate": null,
                  "bankCharge": 0,
                  "amount": 6666.67,
                  "card_type": "debit card",
                  "emi_value": 6822.82,
                  "emi_interest_paid": 468.47,
                  "tenure": "03 months"
            },
            "AXISD06": {
                  "transactionAmount": 20000,
                  "paybackAmount": 0,
                  "loanAmount": 20000,
                  "emiAmount": 3333.33,
                  "additionalCost": "0.00",
                  "emiMdrNote": null,
                  "emiBankInterest": 14,
                  "bankRate": null,
                  "bankCharge": 0,
                  "amount": 3333.33,
                  "card_type": "debit card",
                  "emi_value": 3470.76,
                  "emi_interest_paid": 824.56,
                  "tenure": "06 months"
            },
            "AXISD09": {
                  "transactionAmount": 20000,
                  "paybackAmount": 0,
                  "loanAmount": 20000,
                  "emiAmount": 2222.22,
                  "additionalCost": "0.00",
                  "emiMdrNote": null,
                  "emiBankInterest": 16,
                  "bankRate": null,
                  "bankCharge": 0,
                  "amount": 2222.22,
                  "card_type": "debit card",
                  "emi_value": 2372.99,
                  "emi_interest_paid": 1356.87,
                  "tenure": "09 months"
            },
            "AXISD12": {
                  "transactionAmount": 20000,
                  "paybackAmount": 0,
                  "loanAmount": 20000,
                  "emiAmount": 1666.67,
                  "additionalCost": "0.00",
                  "emiMdrNote": null,
                  "emiBankInterest": 16,
                  "bankRate": null,
                  "bankCharge": 0,
                  "amount": 1666.67,
                  "card_type": "debit card",
                  "emi_value": 1814.62,
                  "emi_interest_paid": 1775.41,
                  "tenure": "12 months"
            }
      }
}
```

## Debit Card EMI

| Issuer Name         | Code   |
| ------------------- | ------ |
| Axis Bank           | AXISD  |
| Bank of Baroda      | BOBD   |
| Federal Bank        | FEDED  |
| HDFC Bank           | HDFCDC |
| ICICI Bank          | ICICID |
| Kotak Bank          | KOTAKD |
| State Bank of India | SBID   |

## Credit Card EMI

| Issuer Name             | Code   |
| ----------------------- | ------ |
| Amex                    | 54     |
| AUSF Bank               | AUSF   |
| Axis Bank               | 7      |
| Bank of Baroda          | BOB    |
| Canara Bank             | CANARA |
| CITI bank               | 20     |
| DBS Bank                | DBS    |
| Federal Bank            | FDRL   |
| HDFC Bank               | 15     |
| HSBC Bank               | HSBC   |
| ICICI Bank              | 21     |
| IDBI Bank               | IDBI   |
| IDFC Bank               | IDFC   |
| Indusind Bank           | INDUS  |
| Kotak Bank              | KOTAK  |
| One Card                | ONEC   |
| RBL Bank                | RBL    |
| Standard Chartered Bank | STANC  |
| State Bank of India     | SBI    |
| Yes Bank                | YES    |

## Cardless EMI

| Issuer Name   | Code      |
| ------------- | --------- |
| Axio          | AXIO      |
| Bajaj Finance | BAJFIN    |
| HDFC Bank     | HDFC\_CL  |
| Homecredit    | HMECDT    |
| ICICI Bank    | ICICI\_CL |
| Kreditbee     | KREDITBEE |
| Zest Money    | ZESTMON   |
| Kotak Bank    | KOTAKC    |
