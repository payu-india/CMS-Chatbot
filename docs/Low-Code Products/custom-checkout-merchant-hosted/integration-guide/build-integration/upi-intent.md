---
title: UPI Intent
excerpt: What the Merchant Hosted source says about UPI Intent, and what it does not
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: UPI Intent — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    UPI Intent for Merchant Hosted Checkout. The source page is a link to UPI
    Intent S2S. bankcode INTENT is named. The request table is not in this folder.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">
  The NPCI note on the Merchant Hosted overview and on UPI Collect says seamless form post must move to UPI Intent S2S. Android must implement Smart Intent. Web must turn the Intent deeplink into a QR instead of using UPI Collect. iOS can keep Collect with a deeplink.
</Callout>

# UPI Intent

The UPI Intent page in the current Merchant Hosted folder has no body. It redirects to the UPI Intent server-to-server guide: [UPI Intent S2S](https://docs.payu.in/docs/upi-intent-server-to-server).

## What This Folder States

| Item | What the Merchant Hosted overview says |
| --- | --- |
| `bankcode` | `INTENT` |
| `txn_s2s_flow` | `2` or `4`, in the NPCI callout. Not in a parameter table |

<!-- DOCUMENTATION GAP: Endpoint, mandatory parameters, deeplink or QR steps, and callback fields for UPI Intent are not in this folder. Do not reconstruct them from the S2S guide inside this page. Follow the linked UPI Intent S2S document. -->

## Post the Payment Request

<!-- DOCUMENTATION GAP: No UPI Intent request sample exists in the Merchant Hosted source folder. -->

## Handle the Callback

<!-- DOCUMENTATION GAP: No UPI Intent callback sample exists in the Merchant Hosted source folder. -->

## Verify the Payment Server-Side

The other method pages verify with Verify Payment and webhooks. There is no Intent-specific verify sample here.

<Verify_Payment_Tabs />

## Test Credentials

The test page says the UPI intent flow is not available in test mode. No Intent test values are listed in this folder.

## Related Resources

<Cards columns={2}>
  <Card title="UPI Intent S2S" icon="fa-arrow-up-right-from-square" href="https://docs.payu.in/docs/upi-intent-server-to-server">
    The document the current UPI Intent page links to.
  </Card>
  <Card title="UPI Collect" icon="fa-mobile-screen" href="./upi-collect">
    VPA validation and the Collect request that the NPCI note restricts.
  </Card>
</Cards>
