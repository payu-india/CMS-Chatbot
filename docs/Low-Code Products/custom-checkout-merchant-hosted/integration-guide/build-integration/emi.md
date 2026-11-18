---
title: EMI
excerpt: Where Merchant Hosted EMI is documented, and what this folder does not contain
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: EMI — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Merchant Hosted EMI. Check eligibility, then post the EMI conversion. This folder links the card and cardless flows and lists the EMI test cards. See links.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# EMI

When the customer chooses EMI on a card, the source says to use the EMI APIs to check eligibility and to get the EMI amount, interest, processing fee or No-Cost EMI, and the tenure. If the customer is eligible, post the transaction with EMI conversion.

This page does not include that request. The current EMI page only links the flows below.

## Flows the Source Points To

<Cards columns={2}>
  <Card title="Debit card EMI" icon="fa-credit-card" href="https://docs.payu.in/docs/collect-payments-with-emi-using-debit-card">
    Linked from the EMI page as a regular flow.
  </Card>
  <Card title="Credit card EMI" icon="fa-credit-card" href="https://docs.payu.in/docs/collect-payments-with-emi-using-credit-card">
    Linked from the EMI page as a regular flow.
  </Card>
  <Card title="Cardless EMI" icon="fa-mobile-screen" href="https://docs.payu.in/docs/collect-payments-with-cardless-emi-using-merchant-hosted-checkout">
    Linked from the EMI page as a regular flow.
  </Card>
  <Card title="Native OTP" icon="fa-key" href="https://docs.payu.in/docs/native-otp-flow-integration">
    Linked from the EMI page as a separate flow.
  </Card>
</Cards>

Postman collection linked from the page: [Merchant Hosted Checkout EMI](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/folder/twysw5i/emi-integration).

## Post the Payment Request

<!-- DOCUMENTATION GAP: No EMI _payment parameter table is in this folder. -->

<!-- VALIDATION NEEDED: The overview says EMI uses pg CC and bankcode N/A, and that you may need extra plan fields such as months and interest. It does not name those fields. It also links EMI codes, which conflicts with bankcode N/A. Do not invent bankcodes or plan fields here. -->

## Handle the Callback

<!-- DOCUMENTATION GAP: No EMI callback sample is in this folder. -->

## Verify the Payment Server-Side

<!-- DOCUMENTATION GAP: No EMI-specific verify sample is in this folder. -->

<Verify_Payment_Tabs />

## Test Credentials

The test page lists these EMI cards. Expiry is any future date. CVV is `123`. OTP is `111111`. Name is any name. Mobile `9123412345` is mandatory for EMI.

| Card | Number |
| --- | --- |
| Kotak DC EMI | `4706-1378-0509-9594` |
| AXIS DC EMI | `4011-5100-0000-0007` |
| HDFC CC EMI | `4453-3410-65876437` |
| ICICI CC EMI | `4453-3410-65876437` |

<!-- VALIDATION NEEDED: The HDFC CC EMI and ICICI CC EMI rows in the test page use the same card number. Copied as written. -->

## Related Resources

<Cards columns={2}>
  <Card title="EMI codes" icon="fa-list" href="https://docs.payu.in/docs/emi-codes">
    Linked from the Merchant Hosted overview.
  </Card>
  <Card title="Test Your Integration" icon="fa-flask" href="../test-integration">
    The same EMI cards, with the test key and salt.
  </Card>
</Cards>
