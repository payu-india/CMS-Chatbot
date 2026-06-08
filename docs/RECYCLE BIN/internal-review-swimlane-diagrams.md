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
box Merchant
    participant Merchant as Merchant Checkout

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
