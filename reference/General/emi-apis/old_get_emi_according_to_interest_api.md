---
title: '[OLD]Get EMI According to Interest API'
excerpt: ''
api:
  file: emi-apis-8.json
  operationId: GetEMIAccordingtoInterest
deprecated: false
hidden: true
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
The **Get EMI Amount According to Interest** API (**getEmiAmountAccordingToInterest** API) is used to get the EMI interest bank rates for all the enabled EMIs.

<GENERALAPIsEnvironment />

<details><summary>Sample request</summary>

```
curl -X POST "https://test.payu.in/merchant/postservice?form=2"-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d"key=JP***g&command=getEmiAmountAccordingToInterest&var1=20000&hash=3b16384427372f658244a106258790df9ed601e3c1dcd1f43d08f7e616bfe907f095947491baa3ec8629d33b3903e8b1e0a1872aa009c5f5c34b06466311dc95&hash="
```

 </details>

 <details><summary>Sample response</summary>

```plaintext
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
    "EMIA6": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 16666.67,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 16666.67,
      "card_type": "credit card",
      "emi_value": 17453.03,
      "emi_interest_paid": 4718.17,
      "tenure": "06 months"
    },
    "EMIA9": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 11111.11,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 11111.11,
      "card_type": "credit card",
      "emi_value": 11864.93,
      "emi_interest_paid": 6784.37,
      "tenure": "09 months"
    },
    "EMIA12": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 8333.33,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 8333.33,
      "card_type": "credit card",
      "emi_value": 9073.09,
      "emi_interest_paid": 8877.03,
      "tenure": "12 months"
    }
  },
  "15": {
    "EMI": {
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
    "EMI6": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 16666.67,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 16666.67,
      "card_type": "credit card",
      "emi_value": 17453.03,
      "emi_interest_paid": 4718.17,
      "tenure": "06 months"
    },
    "EMI9": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 11111.11,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 11111.11,
      "card_type": "credit card",
      "emi_value": 11864.93,
      "emi_interest_paid": 6784.37,
      "tenure": "09 months"
    },
    "EMI12": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 8333.33,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 8333.33,
      "card_type": "credit card",
      "emi_value": 9073.09,
      "emi_interest_paid": 8877.03,
      "tenure": "12 months"
    }
  },
  "20": {
    "EMI03": {
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
    "EMI06": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 16666.67,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 16666.67,
      "card_type": "credit card",
      "emi_value": 17453.03,
      "emi_interest_paid": 4718.17,
      "tenure": "06 months"
    },
    "EMI012": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 8333.33,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 8333.33,
      "card_type": "credit card",
      "emi_value": 9073.09,
      "emi_interest_paid": 8877.03,
      "tenure": "12 months"
    },
    "EMI018": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 5555.56,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 5555.56,
      "card_type": "credit card",
      "emi_value": 6285.64,
      "emi_interest_paid": 13141.57,
      "tenure": "18 months"
    },
    "EMI024": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 4166.67,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 4166.67,
      "card_type": "credit card",
      "emi_value": 4896.31,
      "emi_interest_paid": 17511.47,
      "tenure": "24 months"
    }
  },
  "21": {
    "EMIIC18": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 5555.56,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15.99,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 5555.56,
      "card_type": "credit card",
      "emi_value": 6285.17,
      "emi_interest_paid": 13133.06,
      "tenure": "18 months"
    },
    "EMIIC24": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 4166.67,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15.99,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 4166.67,
      "card_type": "credit card",
      "emi_value": 4895.83,
      "emi_interest_paid": 17500,
      "tenure": "24 months"
    }
  },
  "54": {
    "EMIAMEX3": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 33333.33,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 14,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 33333.33,
      "card_type": "credit card",
      "emi_value": 34114.12,
      "emi_interest_paid": 2342.35,
      "tenure": "03 months"
    },
    "EMIAMEX6": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 16666.67,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 14,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 16666.67,
      "card_type": "credit card",
      "emi_value": 17353.8,
      "emi_interest_paid": 4122.8,
      "tenure": "06 months"
    },
    "EMIAMEX9": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 11111.11,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 14,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 11111.11,
      "card_type": "credit card",
      "emi_value": 11769.28,
      "emi_interest_paid": 5923.53,
      "tenure": "09 months"
    }
  },
  "ONEC": {
    "ONEC03": {
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
    "ONEC06": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 16666.67,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 16666.67,
      "card_type": "credit card",
      "emi_value": 17453.03,
      "emi_interest_paid": 4718.17,
      "tenure": "06 months"
    },
    "ONEC09": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 11111.11,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 11111.11,
      "card_type": "credit card",
      "emi_value": 11864.93,
      "emi_interest_paid": 6784.37,
      "tenure": "09 months"
    },
    "ONEC12": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 8333.33,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 8333.33,
      "card_type": "credit card",
      "emi_value": 9073.09,
      "emi_interest_paid": 8877.03,
      "tenure": "12 months"
    },
    "ONEC18": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 5555.56,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 5555.56,
      "card_type": "credit card",
      "emi_value": 6285.64,
      "emi_interest_paid": 13141.57,
      "tenure": "18 months"
    },
    "ONEC24": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 4166.67,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 4166.67,
      "card_type": "credit card",
      "emi_value": 4896.31,
      "emi_interest_paid": 17511.47,
      "tenure": "24 months"
    }
  },
  "BOB": {
    "BOBCC03": {
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
    "BOBCC06": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 16666.67,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 16666.67,
      "card_type": "credit card",
      "emi_value": 17453.03,
      "emi_interest_paid": 4718.17,
      "tenure": "06 months"
    },
    "BOBCC09": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 11111.11,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 11111.11,
      "card_type": "credit card",
      "emi_value": 11864.93,
      "emi_interest_paid": 6784.37,
      "tenure": "09 months"
    },
    "BOBCC12": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 8333.33,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 8333.33,
      "card_type": "credit card",
      "emi_value": 9073.09,
      "emi_interest_paid": 8877.03,
      "tenure": "12 months"
    },
    "BOBCC18": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 5555.56,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 5555.56,
      "card_type": "credit card",
      "emi_value": 6285.64,
      "emi_interest_paid": 13141.57,
      "tenure": "18 months"
    },
    "BOBCC36": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 2777.78,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 2777.78,
      "card_type": "credit card",
      "emi_value": 3515.7,
      "emi_interest_paid": 26565.32,
      "tenure": "36 months"
    }
  },
  "SCB": {
    "EMISCB3": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 33333.33,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 11.88,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 33333.33,
      "card_type": "credit card",
      "emi_value": 33995.5,
      "emi_interest_paid": 1986.5,
      "tenure": "03 months"
    },
    "EMISCB6": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 16666.67,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 14,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 16666.67,
      "card_type": "credit card",
      "emi_value": 17353.8,
      "emi_interest_paid": 4122.8,
      "tenure": "06 months"
    },
    "EMISCB9": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 11111.11,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 11111.11,
      "card_type": "credit card",
      "emi_value": 11817.06,
      "emi_interest_paid": 6353.5,
      "tenure": "09 months"
    },
    "EMISCB12": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 8333.33,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 8333.33,
      "card_type": "credit card",
      "emi_value": 9025.83,
      "emi_interest_paid": 8309.97,
      "tenure": "12 months"
    },
    "EMISCB24": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 4166.67,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 4166.67,
      "card_type": "credit card",
      "emi_value": 4848.66,
      "emi_interest_paid": 16367.96,
      "tenure": "24 months"
    }
  },
  "YES": {
    "EMIY03": {
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
    "EMIY09": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 11111.11,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 11111.11,
      "card_type": "credit card",
      "emi_value": 11864.93,
      "emi_interest_paid": 6784.37,
      "tenure": "09 months"
    },
    "EMIY12": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 8333.33,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 8333.33,
      "card_type": "credit card",
      "emi_value": 9073.09,
      "emi_interest_paid": 8877.03,
      "tenure": "12 months"
    },
    "EMIY18": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 5555.56,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 5555.56,
      "card_type": "credit card",
      "emi_value": 6285.64,
      "emi_interest_paid": 13141.57,
      "tenure": "18 months"
    }
  },
  "INDUS": {
    "EMIIND3": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 33333.33,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 14,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 33333.33,
      "card_type": "credit card",
      "emi_value": 34114.12,
      "emi_interest_paid": 2342.35,
      "tenure": "03 months"
    },
    "EMIIND6": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 16666.67,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 14,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 16666.67,
      "card_type": "credit card",
      "emi_value": 17353.8,
      "emi_interest_paid": 4122.8,
      "tenure": "06 months"
    },
    "EMIIND9": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 11111.11,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 11111.11,
      "card_type": "credit card",
      "emi_value": 11817.06,
      "emi_interest_paid": 6353.5,
      "tenure": "09 months"
    },
    "EMIIND12": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 8333.33,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 8333.33,
      "card_type": "credit card",
      "emi_value": 9025.83,
      "emi_interest_paid": 8309.97,
      "tenure": "12 months"
    },
    "EMIIND18": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 5555.56,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 5555.56,
      "card_type": "credit card",
      "emi_value": 6238.48,
      "emi_interest_paid": 12292.62,
      "tenure": "18 months"
    },
    "EMIIND24": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 4166.67,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 4166.67,
      "card_type": "credit card",
      "emi_value": 4848.66,
      "emi_interest_paid": 16367.96,
      "tenure": "24 months"
    },
    "EMIIND36": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 2777.78,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 2777.78,
      "card_type": "credit card",
      "emi_value": 3466.53,
      "emi_interest_paid": 24795.18,
      "tenure": "36 months"
    }
  },
  "SBI": {
    "SBI03": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 33333.33,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16.5,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 33333.33,
      "card_type": "credit card",
      "emi_value": 34254.17,
      "emi_interest_paid": 2762.52,
      "tenure": "03 months"
    },
    "SBI06": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 16666.67,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 16666.67,
      "card_type": "credit card",
      "emi_value": 17403.38,
      "emi_interest_paid": 4420.29,
      "tenure": "06 months"
    },
    "SBI09": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 11111.11,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 11111.11,
      "card_type": "credit card",
      "emi_value": 11817.06,
      "emi_interest_paid": 6353.5,
      "tenure": "09 months"
    },
    "SBI12": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 8333.33,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 8333.33,
      "card_type": "credit card",
      "emi_value": 9025.83,
      "emi_interest_paid": 8309.97,
      "tenure": "12 months"
    },
    "SBI24": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 4166.67,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15.75,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 4166.67,
      "card_type": "credit card",
      "emi_value": 4884.37,
      "emi_interest_paid": 17224.98,
      "tenure": "24 months"
    }
  },
  "HSBC": {
    "EMIHS03": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 33333.33,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 33333.33,
      "card_type": "credit card",
      "emi_value": 34170.12,
      "emi_interest_paid": 2510.35,
      "tenure": "03 months"
    },
    "EMIHS06": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 16666.67,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 16666.67,
      "card_type": "credit card",
      "emi_value": 17403.38,
      "emi_interest_paid": 4420.29,
      "tenure": "06 months"
    },
    "EMIHS09": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 11111.11,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 11111.11,
      "card_type": "credit card",
      "emi_value": 11817.06,
      "emi_interest_paid": 6353.5,
      "tenure": "09 months"
    },
    "EMIHS12": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 8333.33,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 8333.33,
      "card_type": "credit card",
      "emi_value": 9025.83,
      "emi_interest_paid": 8309.97,
      "tenure": "12 months"
    },
    "EMIHS18": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 5555.56,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 5555.56,
      "card_type": "credit card",
      "emi_value": 6238.48,
      "emi_interest_paid": 12292.62,
      "tenure": "18 months"
    },
    "EMIHS24": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 4166.67,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 4166.67,
      "card_type": "credit card",
      "emi_value": 4848.66,
      "emi_interest_paid": 16367.96,
      "tenure": "24 months"
    }
  },
  "KOTAK": {
    "EMIK18": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 5555.56,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 5555.56,
      "card_type": "credit card",
      "emi_value": 6285.64,
      "emi_interest_paid": 13141.57,
      "tenure": "18 months"
    },
    "EMIK24": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 4166.67,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 16,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 4166.67,
      "card_type": "credit card",
      "emi_value": 4896.31,
      "emi_interest_paid": 17511.47,
      "tenure": "24 months"
    }
  },
  "RBL": {
    "EMIRBL3": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 33333.33,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 13,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 33333.33,
      "card_type": "credit card",
      "emi_value": 34058.15,
      "emi_interest_paid": 2174.45,
      "tenure": "03 months"
    },
    "EMIRBL9": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 11111.11,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 11111.11,
      "card_type": "credit card",
      "emi_value": 11817.06,
      "emi_interest_paid": 6353.5,
      "tenure": "09 months"
    },
    "EMIRBL24": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 4166.67,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 4166.67,
      "card_type": "credit card",
      "emi_value": 4848.66,
      "emi_interest_paid": 16367.96,
      "tenure": "24 months"
    }
  },
  "FEDED": {
    "FEDED03": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 33333.33,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 33333.33,
      "card_type": "debit card",
      "emi_value": 34170.12,
      "emi_interest_paid": 2510.35,
      "tenure": "03 months"
    },
    "FEDED06": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 16666.67,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 16666.67,
      "card_type": "debit card",
      "emi_value": 17403.38,
      "emi_interest_paid": 4420.29,
      "tenure": "06 months"
    },
    "FEDED09": {
      "transactionAmount": 100000,
      "paybackAmount": 0,
      "loanAmount": 100000,
      "emiAmount": 11111.11,
      "additionalCost": "0.00",
      "emiMdrNote": null,
      "emiBankInterest": 15,
      "bankRate": null,
      "bankCharge": 0,
      "amount": 11111.11,
      "card_type": "debit card",
      "emi_value": 11817.06,
      "emi_interest_paid": 6353.5,
      "tenure": "09 months"
    }
  }
}
```

 </details>

 <details><summary>Response parameters</summary>

The response includes the JSON array and each JSON has the fields as described in the following table:

> 📘 Reference:
>
> In the JSON Array of the response of the **Get EMI Amount According to Interest** API, the code displayed for the each issuer (at the beginning of each object). The significance of these codes are described in [EMI Options for Get EMI According to Interest API](ref:emi-options-for-get-emi-according-to-interest-api).

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        transactionAmount
      </td>

      <td>
        The transaction amount that is will be converted into EMI.
      </td>

      <td>
        20000
      </td>
    </tr>

    <tr>
      <td>
        loanAmount
      </td>

      <td>
        The loan amount that needs to be converted as EMI.
      </td>

      <td>
        20000
      </td>
    </tr>

    <tr>
      <td>
        emiAmount
      </td>

      <td>
        The amount that needs to be converted as EMI.
      </td>

      <td>
        20000
      </td>
    </tr>

    <tr>
      <td>
        additionalCost
      </td>

      <td>
        The processing fee or additional cost for processing the EMI excluding interest.
      </td>

      <td>
        0.00
      </td>
    </tr>

    <tr>
      <td>
        emiMdrNote
      </td>

      <td>
        The EMI Merchant Discount Rate (MDR) note if any for the transaction.
      </td>

      <td>
        0.25
      </td>
    </tr>

    <tr>
      <td>
        bankRate
      </td>

      <td>
        The interest rate in percentage for the EMI. This is excluding the processing fee. For example, 12%, 18%, 24%, etc.
      </td>

      <td>
        13
      </td>
    </tr>

    <tr>
      <td>
        bankCharge
      </td>

      <td>
        The bank charges for the EMI transaction.
      </td>

      <td>
        0
      </td>
    </tr>

    <tr>
      <td>
        amount
      </td>

      <td>
        The principal part of the EMI.
      </td>

      <td>
        6666.67
      </td>
    </tr>

    <tr>
      <td>
        card\_type
      </td>

      <td>
        The card type used by the customer and can be any of the following:  

        * credit card   
        * debit card
      </td>

      <td>
        credit card
      </td>
    </tr>

    <tr>
      <td>
        emi\_value
      </td>

      <td>
        The amount to be paid per EMI.
      </td>

      <td>
        6811.63
      </td>
    </tr>

    <tr>
      <td>
        emi\_interest\_paid
      </td>

      <td>
        The total interest paid for all the EMIs.
      </td>

      <td>
        434.89
      </td>
    </tr>

    <tr>
      <td>
        tenure
      </td>

      <td>
        The tenure for the EMI in months. For example, 3, 6, 12, 24, 36, etc.
      </td>

      <td>
        3
      </td>
    </tr>
  </tbody>
</Table>

</details>

## Request parameters

 <details><summary>Additional information</summary>

Use the following sample values while trying out the API:

<Table align={["left","left"]}>
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
        For more information on how to generate the Key and Salt, refer to any of the following:  

        \- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  

        * **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
      </td>
    </tr>

    <tr>
      <td>
        hash
      </td>

      <td>
        Hash logic for this API is:\
        ```
        sha512(key\|command\|var1\|salt) sha512

        ```For more information about the hash generation process, refer to [Encryption of Request.](/docs/hashing-request-and-response)
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

</details>

**Example values**:

* `var1`: Any amount.
