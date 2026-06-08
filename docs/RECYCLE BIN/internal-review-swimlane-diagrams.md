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

<br />