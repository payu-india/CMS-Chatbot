---
title: EFTNET (NEFT/RTGS)
excerpt: What the Merchant Hosted source says about NEFT and RTGS, and where it conflicts
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: EFTNET — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    NEFT and RTGS on Merchant Hosted Checkout. The source page only links out. The overview gives two different pg values for the same method. Confirm pg first.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">
  The EFTNET page in the current folder has no body. It links to the EFTNET seamless guide. The overview contradicts itself on `pg` and `bankcode`.
</Callout>

# EFTNET (NEFT/RTGS)

There is no request, response, or test credential for EFTNET in this folder.

## What the Overview Says

| Source | pg | bankcode | Other |
| --- | --- | --- | --- |
| Overview prose | `NEFTRTGS` | Based on the bank or institution | |
| Overview table | `NB` | `EFTAXTPV` | `api_version` `"6"`. Always send the customer account number and IFSC |

<!-- VALIDATION NEEDED: Those two rows are the same page. Do not pick NEFTRTGS or NB, and do not pick EFTAXTPV or a bank-specific code, until PayU confirms. The linked guide is the canonical page today: https://docs.payu.in/docs/collect-payments-with-eftnet-neftrtgs-seamless/ -->

<!-- DOCUMENTATION GAP: No EFTNET parameter table or callback is in the Merchant Hosted folder. A spec file exists at reference/eft-neft-payu.json. This page does not read operations out of that file. -->

## Post the Payment Request

<!-- DOCUMENTATION GAP: No EFTNET request sample is in this folder. -->

## Handle the Callback

<!-- DOCUMENTATION GAP: No EFTNET callback sample is in this folder. -->

## Verify the Payment Server-Side

<!-- DOCUMENTATION GAP: No EFTNET-specific verify sample is in this folder. -->

<Verify_Payment_Tabs />

## Test Credentials

<!-- DOCUMENTATION GAP: No NEFT or RTGS test account is in the Merchant Hosted test page. -->

## Related Resources

<Cards columns={2}>
  <Card title="EFTNET seamless guide" icon="fa-arrow-up-right-from-square" href="https://docs.payu.in/docs/collect-payments-with-eftnet-neftrtgs-seamless/">
    The document the current EFTNET page links to.
  </Card>
  <Card title="Net Banking TPV" icon="fa-building-columns" href="./net-banking-tpv">
    The other page that mentions account number and IFSC.
  </Card>
</Cards>
