---
title: '[Internal Review] Swimlane Diagrams'
deprecated: false
hidden: false
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

<br />
