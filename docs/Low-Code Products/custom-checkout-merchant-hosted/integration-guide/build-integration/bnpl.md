---
title: BNPL
excerpt: Where Merchant Hosted BNPL is documented, and what this folder does not contain
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: BNPL — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Buy Now Pay Later on Merchant Hosted Checkout. This folder links the BNPL flows and does not include pg, bankcode, or request parameters. Read the links.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# BNPL

Buy Now Pay Later lets the customer spread the payment over a short period instead of paying the full amount at checkout. The current BNPL page says you can collect it with Merchant Hosted Checkout and then links elsewhere. It has no parameters.

## Flows the Source Points To

<Cards columns={2}>
  <Card title="PayU Hosted BNPL workflow" icon="fa-diagram-project" href="https://docs.payu.in/docs/bnpl-workflow-payu-hosted-checkout">
    Linked from the BNPL page.
  </Card>
  <Card title="Merchant Hosted BNPL workflow" icon="fa-diagram-project" href="https://docs.payu.in/docs/general-flow-bnpl-integration-with-merchant-hosted">
    Linked from the BNPL page.
  </Card>
  <Card title="BNPL Link and Pay" icon="fa-link" href="https://docs.payu.in/docs/collect-payments-with-bnpl-using-link-and-pay">
    Linked from the BNPL page.
  </Card>
</Cards>

Postman collection linked from the page: [Merchant Hosted Checkout BNPL](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/folder/lt115hb/bnpl-integration).

## Post the Payment Request

<!-- DOCUMENTATION GAP: The overview says pg and bankcode vary by BNPL provider and does not list the values. No request sample is in this folder. -->

## Handle the Callback

<!-- DOCUMENTATION GAP: No BNPL callback sample is in this folder. -->

## Verify the Payment Server-Side

<!-- DOCUMENTATION GAP: No BNPL-specific verify sample is in this folder. -->

<Verify_Payment_Tabs />

## Test Credentials

<!-- DOCUMENTATION GAP: No BNPL test credentials are in the Merchant Hosted test page or the BNPL page. -->

## Related Resources

<Cards columns={2}>
  <Card title="BNPL introduction" icon="fa-book" href="https://docs.payu.in/docs/payu-bnpl-integration-introduction">
    The integration page the overview links for BNPL.
  </Card>
  <Card title="APIs" icon="fa-rectangle-api" href="../../merchant-hosted-checkout-apis">
    Shared _payment and verify calls. No BNPL command is named in this folder.
  </Card>
</Cards>
