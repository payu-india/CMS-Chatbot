---
title: '[Internal Review] Swimlane Diagrams'
deprecated: false
hidden: true
metadata:
  robots: index
---
## PayU Hosted Checkout

Original workflow image: [https://docs.payu.in/docs/prebuilt-checkout-payu-hosted](https://docs.payu.in/docs/prebuilt-checkout-payu-hosted "https://docs.payu.in/docs/prebuilt-checkout-payu-hosted")

```mermaid
%%{init: {
  "theme": "base",
  "sequence": {
    "mirrorActors": false,
    "rightAngles": true,
    "messageAlign": "left",
    "fontSize": 12,
    "actorFontSize": 12,
    "noteFontSize": 11,
    "actorMargin": 95,
    "width": 175,
    "boxMargin": 10,
    "messageMargin": 38,
    "diagramMarginX": 60,
    "diagramMarginY": 18
  },
  "themeVariables": {
    "fontFamily": "Arial, Helvetica, sans-serif",
    "fontSize": "12px",
    "background": "#FFFFFF",
    "primaryColor": "#A6C307",
    "primaryTextColor": "#002843",
    "primaryBorderColor": "#002843",
    "secondaryColor": "#F4F9E0",
    "lineColor": "#002843",
    "textColor": "#002843",
    "actorBkg": "#A6C307",
    "actorBorder": "#002843",
    "actorTextColor": "#002843",
    "actorLineColor": "#002843",
    "signalColor": "#002843",
    "signalTextColor": "#002843",
    "labelBoxBkgColor": "#F4F9E0",
    "labelBoxBorderColor": "#A6C307",
    "noteBkgColor": "#F4F9E0",
    "noteTextColor": "#002843",
    "noteBorderColor": "#A6C307",
    "activationBkgColor": "#E8F0C4",
    "activationBorderColor": "#002843"
  }
}}%%
sequenceDiagram
    box Merchant Website
        participant Merchant
    end
    box PayU Checkout
        participant PayU
    end
    box Bank Website
        participant Bank
    end

    Note over Merchant: 1. Customer selects item(s)

    Merchant->>Merchant: 2. Click Pay Now
    Merchant->>PayU: Redirect to PayU

    Note over PayU: Customer fills payment details

    PayU->>Bank: 3. Send payment details

    Bank->>Bank: Verify payment
    Bank-->>PayU: 4. Success or failure

    PayU-->>Merchant: 5. Redirect with status

    Note over Merchant: Show success or failure page

```

## Merchant Hosted

Original: [https://docs.payu.in/docs/custom-checkout-merchant-hosted](https://docs.payu.in/docs/custom-checkout-merchant-hosted "https://docs.payu.in/docs/custom-checkout-merchant-hosted")

```mermaid
%%{init: {
  "theme": "base",
  "sequence": {
    "mirrorActors": false,
    "rightAngles": true,
    "messageAlign": "left",
    "fontSize": 11,
    "actorFontSize": 11,
    "noteFontSize": 10,
    "actorMargin": 115,
    "width": 200,
    "boxMargin": 12,
    "messageMargin": 42,
    "diagramMarginX": 70,
    "diagramMarginY": 20
  },
  "themeVariables": {
    "fontFamily": "Arial, Helvetica, sans-serif",
    "fontSize": "11px",
    "background": "#FFFFFF",
    "primaryColor": "#A6C307",
    "primaryTextColor": "#002843",
    "primaryBorderColor": "#002843",
    "actorBkg": "#A6C307",
    "actorBorder": "#002843",
    "actorTextColor": "#002843",
    "signalColor": "#002843",
    "noteBkgColor": "#F4F9E0",
    "noteTextColor": "#002843",
    "noteBorderColor": "#A6C307",
    "activationBkgColor": "#E8F0C4",
    "activationBorderColor": "#002843"
  }
}}%%
sequenceDiagram
    box Merchant
        participant Merchant
    end
    box PayU
        participant PayU
    end
    box Bank
        participant Bank
    end

    Note over Merchant: 1. Select item(s)
    Note over Merchant: Fill payment details

    Merchant->>PayU: 2. Send details and redirect
    Note over Merchant,PayU: PayU provides redirect URL

    PayU->>Bank: 3. Send to bank

    Bank->>Bank: Verify payment
    Bank-->>PayU: 4. Success/failure

    PayU-->>Merchant: 5. Return status

    Note over Merchant: Success/failure page

```

## Refunds

Original: [https://docs.payu.in/docs/introduction-refunds](https://docs.payu.in/update/docs/introduction-refunds "https://docs.payu.in/update/docs/introduction-refunds")

```mermaid
%%{init: {
  "theme": "base",
  "sequence": {
    "mirrorActors": false,
    "rightAngles": true,
    "messageAlign": "left",
    "fontSize": 12,
    "actorFontSize": 12,
    "noteFontSize": 11,
    "actorMargin": 90,
    "width": 170,
    "boxMargin": 10,
    "messageMargin": 38,
    "diagramMarginX": 60,
    "diagramMarginY": 18
  },
  "themeVariables": {
    "fontFamily": "Arial, Helvetica, sans-serif",
    "fontSize": "12px",
    "background": "#FFFFFF",
    "primaryColor": "#A6C307",
    "primaryTextColor": "#002843",
    "primaryBorderColor": "#002843",
    "secondaryColor": "#F4F9E0",
    "lineColor": "#002843",
    "textColor": "#002843",
    "actorBkg": "#A6C307",
    "actorBorder": "#002843",
    "actorTextColor": "#002843",
    "actorLineColor": "#002843",
    "signalColor": "#002843",
    "signalTextColor": "#002843",
    "labelBoxBkgColor": "#F4F9E0",
    "labelBoxBorderColor": "#A6C307",
    "noteBkgColor": "#F4F9E0",
    "noteTextColor": "#002843",
    "noteBorderColor": "#A6C307",
    "activationBkgColor": "#E8F0C4",
    "activationBorderColor": "#002843"
  }
}}%%
sequenceDiagram
    box Merchant
        participant Merchant
    end
    box PayU
        participant PayU
    end
    box Bank
        participant Bank
    end

    Merchant->>PayU: cancel_refund_transaction
    Note over PayU: Queued

    PayU->>PayU: Debit settlement funds
    PayU->>Bank: Refund initiated

    Note over Bank: Bank API call
    Note over Bank: Up to 3 retries

    Bank->>Bank: Process refund

    alt API success
        Bank-->>PayU: Success
        PayU-->>Merchant: Update ARN
    else API failure
        Bank-->>PayU: Failure
        PayU->>PayU: Send offline to bank
        Note over PayU,Bank: 5th attempt<br/>TAT 5-7 days
        alt Manual success
            PayU-->>Merchant: Update ARN
        else Manual failure
            PayU-->>Merchant: Failure status
            Merchant->>Merchant: Re-initiate refund
        end
    end

    loop Poll status
        Merchant->>PayU: check_action_status_txn_id
        PayU-->>Merchant: Status response
    end

```

## Chargeback

[ Original: https://docs.payu.in/docs/chargeback](https://docs.payu.in/docs/chargeback "https://docs.payu.in/docs/chargeback")

```mermaid
%%{init: {
  "theme": "base",
  "sequence": {
    "mirrorActors": false,
    "rightAngles": true,
    "messageAlign": "left",
    "fontSize": 10,
    "actorFontSize": 10,
    "noteFontSize": 10,
    "actorMargin": 72,
    "width": 145,
    "boxMargin": 8,
    "messageMargin": 34,
    "diagramMarginX": 50,
    "diagramMarginY": 16
  },
  "themeVariables": {
    "fontFamily": "Arial, Helvetica, sans-serif",
    "fontSize": "10px",
    "background": "#FFFFFF",
    "primaryColor": "#A6C307",
    "primaryTextColor": "#002843",
    "actorBkg": "#A6C307",
    "actorBorder": "#002843",
    "signalColor": "#002843",
    "noteBkgColor": "#F4F9E0",
    "noteTextColor": "#002843",
    "noteBorderColor": "#A6C307"
  }
}}%%
sequenceDiagram
    participant Holder as Card Holder
    participant Issuer as Issuing Bank
    participant Network as Card Network
    participant Acquirer as Acquiring Bank
    box PayU
        participant PayU
    end
    participant Merchant

    Holder->>Issuer: 1. Dispute transaction
    Issuer->>Network: 2. Raise chargeback
    Network->>Acquirer: 3. Route chargeback
    Acquirer->>PayU: 4. Notify PayU
    PayU->>Merchant: 5. Chargeback alert
    Note over Merchant: 6. Merchant responds

```

## Apple Pay

Original: [https://docs.payu.in/docs/apple-pay-integration](https://docs.payu.in/update/docs/apple-pay-integration "https://docs.payu.in/update/docs/apple-pay-integration")

```mermaid
%%{init: {
  "theme": "base",
  "sequence": {
    "mirrorActors": false,
    "rightAngles": true,
    "messageAlign": "left",
    "fontSize": 10,
    "actorFontSize": 10,
    "noteFontSize": 10,
    "actorMargin": 68,
    "width": 140,
    "boxMargin": 8,
    "messageMargin": 32,
    "diagramMarginX": 45,
    "diagramMarginY": 16
  },
  "themeVariables": {
    "fontFamily": "Arial, Helvetica, sans-serif",
    "fontSize": "10px",
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
    "edgeLabelBackground": "#FFFFFF",
    "actorBkg": "#A6C307",
    "actorBorder": "#002843",
    "actorTextColor": "#002843",
    "actorLineColor": "#002843",
    "signalColor": "#002843",
    "signalTextColor": "#002843",
    "labelBoxBkgColor": "#F4F9E0",
    "labelBoxBorderColor": "#A6C307",
    "labelTextColor": "#002843",
    "noteBkgColor": "#F4F9E0",
    "noteTextColor": "#002843",
    "noteBorderColor": "#A6C307",
    "activationBkgColor": "#E8F0C4",
    "activationBorderColor": "#002843"
  }
}}%%
sequenceDiagram
    participant User
    box Merchant Site
        participant Merchant as Merchant Checkout
    end
    box PayU
        participant PayU
    end
    participant Apple as Apple Pay
    participant Bank as Acquiring Bank

    User->>Merchant: Select Apple Pay
    Note over Merchant: Device check<br/>Compatible - continue<br/>Not compatible - fallback

    Merchant->>User: Display Apple Pay sheet
    Merchant->>PayU: Create merchant session
    PayU->>Apple: Request merchant session
    Apple-->>PayU: Return signed session
    PayU-->>Merchant: Provide session to frontend

    User->>Apple: Select device token card
    Apple-->>User: Authorize with Face ID or Touch ID

    PayU->>Bank: Submit authorization
    Note over PayU,Bank: Tokenized card rails via Apple Pay

    Bank-->>PayU: Approved or declined
    PayU-->>Merchant: Payment result
    Merchant-->>User: Show success or failure

    Note over User,Merchant: Fallback if not compatible<br/>Show other payment methods
```

## TPV Workflow

Original:[https://docs.payu.in/update/docs/introduction-to-payu-tpv](https://docs.payu.in/update/docs/introduction-to-payu-tpv "https://docs.payu.in/update/docs/introduction-to-payu-tpv")

```mermaid
%%{init: {
  "theme": "base",
  "sequence": {
    "mirrorActors": false,
    "rightAngles": true,
    "messageAlign": "left",
    "fontSize": 11,
    "actorFontSize": 11,
    "noteFontSize": 10,
    "actorMargin": 90,
    "width": 165,
    "boxMargin": 10,
    "messageMargin": 38,
    "diagramMarginX": 55,
    "diagramMarginY": 18
  },
  "themeVariables": {
    "fontFamily": "Arial, Helvetica, sans-serif",
    "fontSize": "11px",
    "background": "#FFFFFF",
    "primaryColor": "#A6C307",
    "primaryTextColor": "#002843",
    "actorBkg": "#A6C307",
    "actorBorder": "#002843",
    "signalColor": "#002843",
    "noteBkgColor": "#F4F9E0",
    "noteTextColor": "#002843",
    "noteBorderColor": "#A6C307"
  }
}}%%
sequenceDiagram
    participant Customer
    box Merchant
        participant Merchant
    end
    box PayU
        participant PayU
    end
    participant Bank

    Customer->>Merchant: 1. TPV transaction request

    Merchant->>PayU: 2. Send TPV request
    Note over Merchant,PayU: bankcode, pg, account number

    PayU-->>Merchant: 3. Return redirect URL
    Note over PayU: Includes account number

    Merchant->>Customer: 4. Redirect to bank page

    Customer->>Bank: 5. Login and authorize
    Note over Bank: Verify requested account number

    Bank-->>PayU: 6. Return to PayU success URL

    PayU-->>Merchant: 7. Redirect to merchant success URL

    Merchant-->>Customer: 8. Order confirmation page

```

## Split Settlements Flow

Mermaid swimlane diagrams for [Split Settlements](https://docs.payu.in/docs/split-settlments), based on the aggregator/marketplace docs.

### Payment, split, and settlement

Covers collect payment, split during or after transaction, and fund release to child merchants.

```mermaid
%%{init: {
  "theme": "base",
  "sequence": {
    "mirrorActors": false,
    "rightAngles": true,
    "messageAlign": "left",
    "fontSize": 10,
    "actorFontSize": 10,
    "noteFontSize": 10,
    "actorMargin": 72,
    "width": 145,
    "boxMargin": 8,
    "messageMargin": 34,
    "diagramMarginX": 45,
    "diagramMarginY": 16
  },
  "themeVariables": {
    "fontFamily": "Arial, Helvetica, sans-serif",
    "fontSize": "10px",
    "background": "#FFFFFF",
    "primaryColor": "#A6C307",
    "primaryTextColor": "#002843",
    "primaryBorderColor": "#002843",
    "secondaryColor": "#F4F9E0",
    "lineColor": "#002843",
    "textColor": "#002843",
    "actorBkg": "#A6C307",
    "actorBorder": "#002843",
    "actorTextColor": "#002843",
    "signalColor": "#002843",
    "noteBkgColor": "#F4F9E0",
    "noteTextColor": "#002843",
    "noteBorderColor": "#A6C307",
    "activationBkgColor": "#E8F0C4",
    "activationBorderColor": "#002843"
  }
}}%%
sequenceDiagram
    participant Customer
    box Aggregator
        participant Parent as Aggregator Merchant
    end
    box PayU
        participant PayU
    end
    participant Bank
    participant Child as Child Merchant

    Customer->>Parent: 1. Checkout and pay

    Parent->>PayU: 2. Collect payment API
    Note over Parent,PayU: During txn - include splitRequest<br/>After txn - use payment_split later

    PayU->>Bank: 3. Process payment
    Bank-->>PayU: 4. Payment success

    opt Split after transaction
        Parent->>PayU: payment_split API
    end

    PayU->>PayU: 5. Create sub-transactions
    Note over PayU: Split by amount or percentage<br/>aggregatorCharges and amountToBeSettled

    PayU-->>Parent: 6. Success with splitInfo
    Parent-->>Customer: 7. Order confirmation

    Parent->>PayU: 8. Release Settlement API
    PayU-->>Child: 9. Credit child merchant
    PayU-->>Parent: 10. Credit aggregator commission
```

### Child merchant onboarding

One-time setup before split payments. See [Onboarding Child Merchants Workflow](https://docs.payu.in/docs/introduction-split-settlements).

```mermaid
%%{init: {
  "theme": "base",
  "sequence": {
    "mirrorActors": false,
    "rightAngles": true,
    "messageAlign": "left",
    "fontSize": 11,
    "actorFontSize": 11,
    "noteFontSize": 10,
    "actorMargin": 90,
    "width": 165,
    "boxMargin": 10,
    "messageMargin": 38,
    "diagramMarginX": 55,
    "diagramMarginY": 18
  },
  "themeVariables": {
    "fontFamily": "Arial, Helvetica, sans-serif",
    "fontSize": "11px",
    "background": "#FFFFFF",
    "primaryColor": "#A6C307",
    "primaryTextColor": "#002843",
    "primaryBorderColor": "#002843",
    "actorBkg": "#A6C307",
    "actorBorder": "#002843",
    "actorTextColor": "#002843",
    "signalColor": "#002843",
    "noteBkgColor": "#F4F9E0",
    "noteTextColor": "#002843",
    "noteBorderColor": "#A6C307"
  }
}}%%
sequenceDiagram
    box Aggregator
        participant Parent as Aggregator Merchant
    end
    box PayU Hub
        participant Hub as Accounts Hub
    end
    box PayU Onboarding
        participant Onboarding
    end
    participant Child as Child Merchant

    Note over Parent: Activate Split Settlements on dashboard

    Parent->>Hub: 1. Get Client Token API
    Note over Hub: scope refer_child_merchant
    Hub-->>Parent: Access token

    Parent->>Onboarding: 2. Create Child Merchant API
    Onboarding-->>Parent: Child MID and UUID

    Parent->>Onboarding: 3. Update bank details
    Onboarding-->>Child: Child merchant active

    Note over Parent,Child: Fetch child details via dashboard or APIs
```

<br />

## Cross-Border Payments Import Flow

Mermaid swimlane diagrams for [Cross-Border Payments – Import](https://docs.payu.in/docs/introduction-cross-border-payments-import), based on the payment journey, integration, settlement, and on-hold sections.

### Payment and cross-border settlement

End-to-end flow from Indian customer payment to overseas merchant settlement via AD-1 bank (T+2/T+3).

```mermaid
%%{init: {
  "theme": "base",
  "sequence": {
    "mirrorActors": false,
    "rightAngles": true,
    "messageAlign": "left",
    "fontSize": 10,
    "actorFontSize": 10,
    "noteFontSize": 10,
    "actorMargin": 58,
    "width": 130,
    "boxMargin": 8,
    "messageMargin": 30,
    "diagramMarginX": 40,
    "diagramMarginY": 14
  },
  "themeVariables": {
    "fontFamily": "Arial, Helvetica, sans-serif",
    "fontSize": "10px",
    "background": "#FFFFFF",
    "primaryColor": "#A6C307",
    "primaryTextColor": "#002843",
    "primaryBorderColor": "#002843",
    "secondaryColor": "#F4F9E0",
    "lineColor": "#002843",
    "textColor": "#002843",
    "actorBkg": "#A6C307",
    "actorBorder": "#002843",
    "actorTextColor": "#002843",
    "signalColor": "#002843",
    "noteBkgColor": "#F4F9E0",
    "noteTextColor": "#002843",
    "noteBorderColor": "#A6C307",
    "activationBkgColor": "#E8F0C4",
    "activationBorderColor": "#002843"
  }
}}%%
sequenceDiagram
    participant Customer
    box Merchant Site
        participant Merchant as Overseas Merchant
    end
    box PayU
        participant PayU
    end
    participant Acquirer as Acquirer Bank
    participant AD1 as AD-1 Bank

    Customer->>Merchant: 1. Checkout on merchant site

    Merchant->>PayU: 2. Collect payment API
    Note over Merchant,PayU: Mandatory buyer name and zipcode<br/>Invoice ID in udf5

    alt PayU Hosted Checkout
        PayU->>Customer: 3. Show payment page
    else Merchant Hosted Checkout
        Merchant->>Customer: 3. Collect payment on site
    end

    Customer->>PayU: 4. Pay via Cards NetBanking UPI or NEFT
    PayU->>Acquirer: 5. Process payment
    Acquirer-->>PayU: 6. Payment success

    PayU-->>Merchant: 7. Transaction success
    Merchant-->>Customer: 8. Order confirmation

    Note over Acquirer,PayU: Funds to PayU nodal pool account

    Merchant->>PayU: 9. Upload invoice or AWB
    Note over Merchant,PayU: Invoice Upload API or UDF Update

    PayU->>AD1: 10. Settlement instruction via SFTP
    AD1->>Merchant: 11. SWIFT to offshore account
    Note over AD1,Merchant: Native currency T+2 or T+3

    AD1-->>PayU: 12. Response file and UTR
    PayU-->>Merchant: 13. Settlement details
```

### LRS customer journey (PayU Hosted)

For travel and education under the Liberalised Remittance Scheme. See [Customer Journey - PayU Hosted Checkout with LRS](https://docs.payu.in/docs/customer-journey-payu-hosted-checkout-with-lrs-integration).

```mermaid
%%{init: {
  "theme": "base",
  "sequence": {
    "mirrorActors": false,
    "rightAngles": true,
    "messageAlign": "left",
    "fontSize": 10,
    "actorFontSize": 10,
    "noteFontSize": 10,
    "actorMargin": 72,
    "width": 145,
    "boxMargin": 8,
    "messageMargin": 32,
    "diagramMarginX": 45,
    "diagramMarginY": 16
  },
  "themeVariables": {
    "fontFamily": "Arial, Helvetica, sans-serif",
    "fontSize": "10px",
    "background": "#FFFFFF",
    "primaryColor": "#A6C307",
    "primaryTextColor": "#002843",
    "primaryBorderColor": "#002843",
    "secondaryColor": "#F4F9E0",
    "lineColor": "#002843",
    "textColor": "#002843",
    "actorBkg": "#A6C307",
    "actorBorder": "#002843",
    "actorTextColor": "#002843",
    "signalColor": "#002843",
    "noteBkgColor": "#F4F9E0",
    "noteTextColor": "#002843",
    "noteBorderColor": "#A6C307"
  }
}}%%
sequenceDiagram
    participant Customer
    box Merchant Site
        participant Merchant as Overseas Merchant
    end
    box PayU
        participant PayU
    end

    Customer->>Merchant: 1. Select products and checkout
    Merchant->>PayU: 2. Payment request with lrs_service_type
    PayU->>Customer: 3. PayU Hosted Checkout page

    Customer->>PayU: 4. Select Individual Buyer
    Note over Customer,PayU: PAN DOB pincode and LRS declaration

    Customer->>PayU: 5. TCS declaration if applicable
    Note over PayU: Tax based on lrs_service_type<br/>PayU remits TCS via AD-1 bank

    Customer->>PayU: 6. Complete payment
    PayU-->>Merchant: 7. Payment result
    Merchant-->>Customer: 8. Order confirmation
```

### On-hold settlement resolution

When AD-1 bank requires additional information before releasing outward settlement. See [On-Hold Settlements](https://docs.payu.in/docs/on-hold-settlements-cross-border-payments).

```mermaid
%%{init: {
  "theme": "base",
  "sequence": {
    "mirrorActors": false,
    "rightAngles": true,
    "messageAlign": "left",
    "fontSize": 10,
    "actorFontSize": 10,
    "noteFontSize": 10,
    "actorMargin": 80,
    "width": 150,
    "boxMargin": 8,
    "messageMargin": 34,
    "diagramMarginX": 45,
    "diagramMarginY": 16
  },
  "themeVariables": {
    "fontFamily": "Arial, Helvetica, sans-serif",
    "fontSize": "10px",
    "background": "#FFFFFF",
    "primaryColor": "#A6C307",
    "primaryTextColor": "#002843",
    "primaryBorderColor": "#002843",
    "secondaryColor": "#F4F9E0",
    "lineColor": "#002843",
    "textColor": "#002843",
    "actorBkg": "#A6C307",
    "actorBorder": "#002843",
    "actorTextColor": "#002843",
    "signalColor": "#002843",
    "noteBkgColor": "#F4F9E0",
    "noteTextColor": "#002843",
    "noteBorderColor": "#A6C307"
  }
}}%%
sequenceDiagram
    box Merchant Site
        participant Merchant as Overseas Merchant
    end
    box PayU
        participant PayU
    end
    participant AD1 as AD-1 Bank

    PayU->>AD1: 1. Settlement instruction
    AD1-->>PayU: 2. Needs Response - on hold
    PayU-->>Merchant: 3. On-hold status notification

    alt Missing invoice or buyer details
        Merchant->>PayU: 4. UDF Update or Invoice Upload API
        Note over Merchant,PayU: Dashboard On-hold tab also available
        PayU->>AD1: 5. Resubmit compliance data
        AD1-->>PayU: 6. Settled with UTR
        PayU-->>Merchant: 7. Settlement complete
    else AML or sanction match
        AD1-->>PayU: Rejected by Bank
        PayU-->>Merchant: Refund required
        Merchant->>PayU: Initiate refund
    end
```

## Recommendation Engine Flow

Mermaid swimlane diagrams for [Recommendation Engine](https://docs.payu.in/docs/recommendation-engine), based on the intro, customer journey, and Fetch API sections.

### Checkout personalization flow

How RE personalizes payment instruments on PayU Hosted Checkout or via the Fetch API for merchant-hosted checkout.

```mermaid
%%{init: {
  "theme": "base",
  "sequence": {
    "mirrorActors": false,
    "rightAngles": true,
    "messageAlign": "left",
    "fontSize": 10,
    "actorFontSize": 10,
    "noteFontSize": 10,
    "actorMargin": 58,
    "width": 130,
    "boxMargin": 8,
    "messageMargin": 30,
    "diagramMarginX": 40,
    "diagramMarginY": 14
  },
  "themeVariables": {
    "fontFamily": "Arial, Helvetica, sans-serif",
    "fontSize": "10px",
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
    "edgeLabelBackground": "#FFFFFF",
    "actorBkg": "#A6C307",
    "actorBorder": "#002843",
    "actorTextColor": "#002843",
    "actorLineColor": "#002843",
    "signalColor": "#002843",
    "signalTextColor": "#002843",
    "labelBoxBkgColor": "#F4F9E0",
    "labelBoxBorderColor": "#A6C307",
    "labelTextColor": "#002843",
    "noteBkgColor": "#F4F9E0",
    "noteTextColor": "#002843",
    "noteBorderColor": "#A6C307",
    "activationBkgColor": "#E8F0C4",
    "activationBorderColor": "#002843"
  }
}}%%
sequenceDiagram
    participant Customer
    box Merchant Site
        participant Merchant
    end
    box PayU
        participant PayU
        participant RE as Recommendation Engine
    end
    participant PG as Payment Gateway

    Note over Merchant: Activate RE via PayU Key Account Manager (KAM)

    Customer->>Merchant: 1. Proceed to checkout

    alt PayU Hosted Checkout
        Merchant->>PayU: 2. Payment request
        PayU->>RE: 3. Evaluate recommendations
    else Merchant Hosted with Fetch API
        Merchant->>PayU: 2. Fetch RE API
        PayU->>RE: 3. Evaluate recommendations
        RE-->>PayU: Ranked paymentOptions
        PayU-->>Merchant: savedPaymentOptions response
        Merchant->>Customer: 4. Show personalized checkout
    end

    Note over RE,PayU: User history and merchant goal<br/>Transaction amount and category

    RE-->>PayU: 4. Ranked L1 and L2 options
    PayU->>Customer: 5. Display prioritized payment page

    Customer->>PayU: 6. Select recommended payment mode
    PayU->>PG: 7. Process payment
    PG-->>PayU: 8. Payment result

    PayU-->>Merchant: 9. Transaction status
    Merchant-->>Customer: 10. Order confirmation
```

### User scenarios and merchant goals

How RE adapts recommendations based on customer type and the merchant-selected optimization goal.

```mermaid
%%{init: {
  "theme": "base",
  "sequence": {
    "mirrorActors": false,
    "rightAngles": true,
    "messageAlign": "left",
    "fontSize": 10,
    "actorFontSize": 10,
    "noteFontSize": 10,
    "actorMargin": 72,
    "width": 145,
    "boxMargin": 8,
    "messageMargin": 32,
    "diagramMarginX": 45,
    "diagramMarginY": 16
  },
  "themeVariables": {
    "fontFamily": "Arial, Helvetica, sans-serif",
    "fontSize": "10px",
    "background": "#FFFFFF",
    "primaryColor": "#A6C307",
    "primaryTextColor": "#002843",
    "primaryBorderColor": "#002843",
    "secondaryColor": "#F4F9E0",
    "lineColor": "#002843",
    "textColor": "#002843",
    "actorBkg": "#A6C307",
    "actorBorder": "#002843",
    "actorTextColor": "#002843",
    "signalColor": "#002843",
    "noteBkgColor": "#F4F9E0",
    "noteTextColor": "#002843",
    "noteBorderColor": "#A6C307"
  }
}}%%
sequenceDiagram
    participant Customer
    box PayU
        participant RE as Recommendation Engine
    end

    alt Repeat user with saved data
        Customer->>RE: Logged in with consented instruments
        Note over Customer,RE: Saved cards UPI and wallets shown first
    else Repeat user without saved data
        Customer->>RE: Known user no stored instruments
        Note over Customer,RE: Recommendations from history and goal
    else First-time user
        Customer->>RE: New user at checkout
        Note over Customer,RE: Goal and contextual data only
    end

    alt Goal Success Rate
        RE->>Customer: Prioritize highest SRT instruments
        Note over RE: Example Airtel Money on L1 and L2
    else Goal Processing Cost
        RE->>Customer: Prioritize lowest cost modes
        Note over RE: Example UPI over wallets on L1
    else Goal Affordability
        RE->>Customer: Prioritize EMI and BNPL options
        Note over RE: Affordability on L1 and L2 screens
    end
```

### Fetch Recommendation Engine API

Server-to-server flow for merchants building a custom checkout UI. See [Fetch Recommendation Engine API](https://docs.payu.in/docs/fetch-recommendation-engine-api).

```mermaid
%%{init: {
  "theme": "base",
  "sequence": {
    "mirrorActors": false,
    "rightAngles": true,
    "messageAlign": "left",
    "fontSize": 10,
    "actorFontSize": 10,
    "noteFontSize": 10,
    "actorMargin": 80,
    "width": 150,
    "boxMargin": 8,
    "messageMargin": 34,
    "diagramMarginX": 45,
    "diagramMarginY": 16
  },
  "themeVariables": {
    "fontFamily": "Arial, Helvetica, sans-serif",
    "fontSize": "10px",
    "background": "#FFFFFF",
    "primaryColor": "#A6C307",
    "primaryTextColor": "#002843",
    "primaryBorderColor": "#002843",
    "secondaryColor": "#F4F9E0",
    "lineColor": "#002843",
    "textColor": "#002843",
    "actorBkg": "#A6C307",
    "actorBorder": "#002843",
    "actorTextColor": "#002843",
    "signalColor": "#002843",
    "noteBkgColor": "#F4F9E0",
    "noteTextColor": "#002843",
    "noteBorderColor": "#A6C307"
  }
}}%%
sequenceDiagram
    box Merchant Site
        participant Merchant
    end
    box PayU
        participant PayU
        participant RE as Recommendation Engine
    end

    Merchant->>PayU: 1. POST recommendation/v1/fetch
    Note over Merchant,PayU: HMAC auth with Date and Digest headers

    Note over Merchant,PayU: amount and userToken mandatory<br/>phone txnId mode ibiboCode optional

    PayU->>RE: 2. Score payment instruments
    RE-->>PayU: 3. Ranked options by merchant goal

    PayU-->>Merchant: 4. paymentOptions and savedPaymentOptions
    Note over Merchant: Render L1 and L2 checkout UI
```

