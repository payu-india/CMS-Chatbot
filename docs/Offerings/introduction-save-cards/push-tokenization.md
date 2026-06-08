---
title: Push Tokenization
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## What is Push Tokenization?

A faster way to share payment credentials between merchants & banks. Using Push Tokenization, tokens will be created at the issuer bank level and linked to their existing accounts with various e-commerce apps/ websites

RBI released the circular in December 2023 which said that the banks cardholder should be able to tokenize the card on multiple merchants from a a single bank platform either mobile or internet banking.

- Eliminate the duplication of tokenization process at each app/website, making payments simpler and faster
- Increase transaction security, resulting in reduced card-data-related frauds

## PayU solution

PayU provides both network tokens and issuer tokens for its merchants for push provisioning feature:

- **Network Tokens**: Network tokens are virtual payment cards created by the payment schemes (VISA, Mastercard, Rupay, Diners), and they replace the original card in the digital space. This allows for several network tokens to be created per card, and they function in the same way as the original card when storing and transacting with them.  
- **Issuer Tokens**: Issuer tokens are virtual payment cards created by the card-issuing bank, and they replace the original card in the digital space. However, these tokens are not understood by the network schemes.

## How it works

```mermaid
%%{init: {
  "theme": "base",
  "flowchart": {
    "htmlLabels": true,
    "curve": "basis",
    "padding": 28,
    "nodeSpacing": 55,
    "rankSpacing": 65,
    "diagramPadding": 20
  },
  "themeVariables": {
    "fontFamily": "Arial, Helvetica, sans-serif",
    "fontSize": "20px",
    "background": "#FFFFFF",
    "primaryColor": "#A6C307",
    "primaryTextColor": "#002843",
    "primaryBorderColor": "#002843",
    "secondaryColor": "#F4F9E0",
    "lineColor": "#002843",
    "textColor": "#002843",
    "clusterBkg": "#FAFCF4",
    "clusterBorder": "#D8E8A8",
    "edgeLabelBackground": "#FFFFFF"
  }
}}%%
flowchart TB
    subgraph R1[" "]
        direction LR
        A[Customer opens bank app] --> B[Manage cards] --> C[Save card with merchant] --> D[Select merchants]
    end

    subgraph R2[" "]
        direction LR
        E[Provide consent] --> F{Phone number verified?} --> G[PayU provisions card token] --> H{Provisioning complete?}
    end

    subgraph R3[" "]
        direction LR
        I[Show failure message]
        J[Show success message]
    end

    subgraph R4[" "]
        direction LR
        Done([Finished])
    end

    D --> E
    F -->|Yes| G
    F -->|No| Done
    H -->|No| I
    H -->|Yes| J
    I --> Done
    J --> Done

    classDef bankStep fill:#A6C307,stroke:#002843,color:#002843,stroke-width:2px
    classDef payuStep fill:#002843,stroke:#002843,color:#FFFFFF,stroke-width:2px
    classDef decision fill:#F4F9E0,stroke:#002843,color:#002843,stroke-width:2px
    classDef outcome fill:#E8F0C4,stroke:#8AA205,color:#002843,stroke-width:2px
    classDef endNode fill:#002843,stroke:#002843,color:#FFFFFF,stroke-width:2px

    class A,B,C,D,E bankStep
    class G payuStep
    class F,H decision
    class I,J outcome
    class Done endNode

```

## Benefits

#### Customer

- Customer can create card token at the bank level for multiple merchants instead of creating card tokens at individual merchant level.
- Frictionless card payment experience
- Enjoy enhanced security – no card data related theft.

### Banks

- Banks get a plug and play platform without any heavy technology investment.
- Helps in incentivising transactions via card across merchants.
- Drive adoption and activation of cards through partners.

### Merchants

- Improved payment experience for customers which reduces drop-offs, increases conversion rates and boosts card spends.
- A new way to acquire/reactivate customers when they enable their cards for online purchase.

## Supported card networks

- Visa
- Mastercard
- Rupay
- Diners

## Workflow

### Using PayU for tokenization

Changes expected are:

1. Integrate with **Account Discovery** API.  For more information, refer to [Account Discovery API](ref:account-discovery-api) .

> 📘 Step 1  is mandatory
>
> This is the mandatory step before creating tokens. When a cardholder select merchants at banks platform for push provisioning,  mobile number, email id of the cardholder associated with the card will be passed from bank to PayU for further validating with the merchant if customer profile exists or not

2. If customer profile is not present at your end against the mobile number or email ID, tokens will not be created.<br />OR<br />If customer profile exists, PayU will create the tokens.
3. In the **Get Payment Details** API, PayU has added an identifier `push_token=1 `which indicates the token created belongs to push tokenization flow. For more information, refer [Get Payment Details (Cryptogram) API](ref:get_payment_details_cryptogram).

### Using Other Aggregator for Tokenization

1. Register your PayU endpoint in your Onboarding form for the schemes.
2. Integrate account discovery API (similar to the [Account Discovery API](ref:account-discovery-api) from PayU) where you will send user ID corresponding to the mobile number received for push tokenization.
3. Post that PayU will relay the information to their <Glossary>Token Requestor</Glossary> and send response to the you after the token is created.

<br />
