---
title: Refunds
excerpt: ''
deprecated: false
hidden: false
icon: fab fa-cash-app
metadata:
  title: ''
  description: ''
  keywords:
    - PayU Refunds
    - Transaction Reversal
    - Payment Cancellation
    - Customer Refunds
  robots: index
next:
  description: ''
---
---
title: Refunds
deprecated: false
hidden: false
metadata:
  title: Refunds Integration
  description: >-
    Initiate full or partial refunds via PayU APIs or Dashboard, track status,
    and configure webhooks for refund notifications.
  keywords:
    - PayU Refunds
    - Transaction Reversal
    - Payment Cancellation
    - Customer Refunds
  robots: index
---
Order cancellations are an unfortunate reality for any business. Customers may cancel an order, return part of the order or the full order. Merchants may not have the resources to fulfill the order and must cancel it. Therefore, it is imperative for merchants collecting payment online to refund the payment back to the customers.

> 👍 Before you begin:
>
> Register for a account with PayU before you start integration. Contact your PayU Key Account Manager to enable automatic refunds or instant refunds if required. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

> 📘 **Publish refund policy on your website**: 
PayU recommends publishing the refund policy on your website, including the time taken to refund for failed transactions and the refund process.

## Overview and Workflow

<Accordion title="End-to-end refund flow" icon="fa-diagram-project">
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

  The refunds workflow in PayU typically follows this sequence:

  1. **Customer requests a refund** — A refund begins when the customer cancels an order, returns an item, or did not receive the expected service after being charged.
  2. **Merchant initiates refund request** — Initiate via [PayU Dashboard](doc:refunds-dashboard) or [Refund Transaction API](ref:refund_transaction_api).
  3. **PayU validates refund request** — PayU checks transaction existence, refund conditions, and full or partial amount rules.
  4. **PayU sends refund request to the payment partner** — PayU forwards the request to the bank, card network, wallet, or lender.
  5. **Bank processes the refund** — Funds are returned to the customer's source account.
  6. **Settlement adjustments** — The refund amount is deducted from the merchant settlement balance.
  7. **Customer receives the refund** — Typically **5–21 days** depending on payment method; PayU emails the merchant on completion.
  8. **Poll status** — Use [Check Refund Status APIs](doc:refund-apis-doc) or [Webhooks for Refunds](doc:webhooks-for-refunds) to track progress.

  > 📘 **Automatic retries**: If the refund API call fails at the bank end, the bank retries up to three times automatically. If it still fails, PayU requests the refund manually with the bank.
</Accordion>

<Accordion title="Types of refunds" icon="fa-tags">
  Refunds can be classified into two types:

  * **Partial refund** — The refund amount is less than the payment amount (for example, customer returns one item from a multi-item order).
  * **Full refund** — The refund amount equals the full payment amount (entire order cancelled or returned).

  For step-by-step API integration, refer to [Refund APIs](doc:refund-apis-doc) and [Refund Transaction API](ref:refund_transaction_api).
</Accordion>

<Accordion title="Automatic refund" icon="fa-rotate-left">
  When a customer is making a payment and the transaction was not successful (status is "Pending" or "Dropped"), but the amount was debited due to unforeseen circumstances, the bank sends the amount to PayU. After reconciliation finds the transaction was not successful, PayU automatically initiates the refund to the customer.

  For example, if a customer tries to book a movie ticket and the transaction fails but the amount was debited, PayU initiates the refund automatically after reconciliation.

  > 📘 **Contact PayU Key Account Manager to enable automatic refunds**: If you wish to enable the automatic refund feature, contact your PayU Key Account Manager or [PayU Support](https://help.payu.in).
</Accordion>

<Accordion title="Prerequisites and eligibility" icon="fa-check-circle">
  **When is a customer eligible for a refund?**

  If a customer has been charged for a transaction and did not receive the expected services, they may be eligible for a refund. For example, if the customer was charged for a movie ticket but did not receive the ticket.

  **Prerequisites for initiating a refund**

  * The customer must have made the payment within the allowed time frame or using a supported PayU product.
  * You have the transaction ID, date, and transaction amount.

  Refunds must be sent to the source account used for payment. PayU passes the refund request to the bank or lender through which the payment was made.
</Accordion>

<Accordion title="Refund turnaround time" icon="fa-clock">
  Refunds typically take **5–21 days** to reflect in the customer's bank account. For Net Banking transactions, certain government banks may take longer. PayU communicates the status (successful or failed) over email once the refund request is processed.

  For instant refunds on eligible transactions, refer to [Partner Refunds](doc:partner-refunds).
</Accordion>

<Accordion title="Refund vs chargeback" icon="fa-scale-balanced">
  A **chargeback** is raised by the customer to the issuing bank (for example, fraud, unsatisfactory delivery). A **refund** is initiated by the merchant after the customer requests a refund or a transaction has failed for the customer.

  For chargeback management, refer to the Chargeback section of the PayU Developer Guide.
</Accordion>
## Integration guides

The following sections describe how to initiate, track, and manage refunds with PayU:

* [Refunds Dashboard](doc:refunds-dashboard)
  * [Refund Wallet Dashboard](doc:refund-wallet-dashboard)
* [Refund APIs](doc:refund-apis-doc)
* [Refunds in PayU Products](doc:refunds-in-payu-products)
  * [Refunds for Offers](doc:refunds-for-offers)
  * [Refund APIs for Split Settlements](doc:refund-apis-for-split-settlements)
  * [Partner Refunds](doc:partner-refunds)
  * [Refunds for EMI](doc:refunds-for-emi)
  * [Refunds for BNPL](doc:refunds-for-bnpl)
* [Webhooks for Refunds](doc:webhooks-for-refunds)
* [FAQs for Refunds](doc:faqs-for-refunds)

## APIs used in Refunds integration

| API | Purpose |
| --- | --- |
| [Refund Transaction API](ref:refund_transaction_api) | Initiate a full or partial refund (`cancel_refund_transaction` command) for a captured transaction.|
| [Check Refund Status API with PayU ID](ref:check_action_status_api_with_payu_id) | Poll refund status using the PayU transaction ID (`check_action_status_txn_id`). |
| [Check Refund Status API with Request ID](ref:check_action_status_api_with_request_id) | Poll refund status using the merchant request ID.|
| [Get All Refunds from Transaction IDs](ref:get_all_refunds_from_transaction_ids_api) | Retrieve all refund requests associated with one or more transaction IDs. |
| [Refund Status API for Split Payments](ref:refund-status-api-for-split-payments) | Check refund status for split-payment child transactions. |