---
title: Aggregator or Marketplace Settlement Solution
excerpt: >-
  This section describes the aggregator model and the steps for the technical
  integration process between your website and PayU Marketplace APIs to enable
  split settlements between you and your sub-sellers.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
PayU Aggregator APIs are organized around REST, each API is a server-to-server call from your server to our server and it is designed to have predictable resource-oriented URLs and PayU uses HTTP response codes to indicate API errors. For more information on HTTP response codes, refer to [Error Codes](ref:error-codes).

PayU supports cross-platform resource sharing so that you can interact securely with PayU Split Settlements APIs from a client-side web application. PayU responds with a JSON object in all the responses.

## Understanding Split Settlements terms

The terms involved in the Split Settlements API are:

- The marketplace owners are referred to as the **aggregator merchant**.
- The individual providers or sub-sellers of that marketplace are referred to as the **child Merchants**.
- The fee that the parent Merchant can optionally apply per sub-merchant transaction is referred to as **aggregatorCharges**.
- The amount that will be settled to a given child Merchants is referred to as **amountToBeSettled**.

## Split Settlements characteristics

The characteristics of Split Settlements are:

- Customers make a single payment to the aggregator
- Separate accounts for aggregator’s sellers will be created to which money will be settled.
- Settlement of a single transaction can be done across multiple sellers
- Aggregator’s commission is settled to the Aggregator’s account.
- PayUMoney takes care of Nodal Registrations, Settlements and Regulatory
- Requirements of sub-sellers.

## Payment workflow

1. PayU creates sub-transactions based on these amounts for the sellers.
2. Every transaction/order can be split into any number of sub-transactions (depending on the sellers involved).
3. These sub-transactions are settled to the corresponding seller’s account.
4. Marketplace’s commission is settled to the marketplace’s account after deducting PAYU TDR

The following flow diagram explains how the customer makes the payment and how the process flows:

```mermaid
%%{init: {
  "theme": "base",
  "flowchart": {
    "curve": "stepAfter",
    "padding": 16,
    "nodeSpacing": 36,
    "rankSpacing": 48,
    "diagramPadding": 16,
    "htmlLabels": true,
    "useMaxWidth": false
  },
  "themeVariables": {
    "fontFamily": "Arial, Helvetica, sans-serif",
    "fontSize": "11px",
    "background": "#FFFFFF",
    "primaryColor": "#A6C307",
    "primaryTextColor": "#002843",
    "primaryBorderColor": "#002843",
    "secondaryColor": "#F4F9E0",
    "secondaryTextColor": "#002843",
    "secondaryBorderColor": "#A6C307",
    "tertiaryColor": "#002843",
    "tertiaryTextColor": "#FFFFFF",
    "lineColor": "#002843",
    "textColor": "#002843",
    "mainBkg": "#A6C307",
    "clusterBkg": "#FAFCF4",
    "clusterBorder": "#D8E8A8",
    "edgeLabelBackground": "#FFFFFF"
  }
}}%%
flowchart TB
    classDef payu fill:#A6C307,stroke:#002843,stroke-width:1px,color:#002843,font-size:11px
    classDef bank fill:#F4F9E0,stroke:#002843,stroke-width:1px,color:#002843,font-size:11px
    classDef actor fill:#E8F0C4,stroke:#002843,stroke-width:1px,color:#002843,font-size:11px

    C(["Customer"]):::actor
    N1["The money is debited from the<br/>customer's bank account and is sent<br/>to the PayU nodal account."]:::payu
    N2["The marketplace provides seller<br/>&amp; order breakup info to PayU."]:::payu
    N3["The marketplace selectively instructs<br/>PayU to settle the funds to its sellers."]:::payu
    SB["Seller B's<br/>bank account"]:::bank
    MC["Marketplace's commissions<br/>settled to its bank account"]:::bank
    SA["Seller A's<br/>bank account"]:::bank

    C -->|"Customer makes payment"| N1
    N1 -->|"Marketplace creates sub-transactions"| N2
    N2 -->|"Marketplace releases sub-transactions"| N3
    N3 --> SB
    N3 --> MC
    N3 --> SA
```

<br />
