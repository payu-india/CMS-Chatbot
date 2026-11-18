---
title: Net Banking TPV
excerpt: What the Merchant Hosted source says about net-banking TPV, and what it does not
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Net Banking TPV — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Net banking TPV for Merchant Hosted Checkout. The source page only links out. Account number and IFSC are mentioned, without a parameter table. See the link.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">
  The Net Banking TPV page in the current folder has no body. It links to the Net Banking TPV guide outside this folder.
</Callout>

# Net Banking TPV

Third-party validation is not specified in this folder. The current page is a redirect to [Net Banking integration for TPV](https://docs.payu.in/docs/net-banking-integration-for-tpv/).

## What This Folder States

The overview's net-banking paragraph says merchants should always send the customer account number and the customer IFSC. The net-banking parameter table does not have those fields.

The EFTNET row of the same overview table says `api_version` `"6"` must be passed for NEFT/RTGS, and that merchants should always send the customer account number and IFSC. That row uses `pg=NB` and `bankcode=EFTAXTPV`. The EFTNET prose on the same page says `pg=NEFTRTGS`.

<!-- VALIDATION NEEDED: Account number and IFSC are attached to "Net Banking" in one paragraph and to EFTNET in the table, with two different pg values for EFTNET. This page does not decide which flow those fields belong to. -->

<!-- DOCUMENTATION GAP: No TPV parameter names, endpoint sample, or callback are in the Merchant Hosted folder. Use the linked TPV guide. Do not invent field names. -->

## Post the Payment Request

<!-- DOCUMENTATION GAP: No TPV request is in this folder. -->

## Handle the Callback

<!-- DOCUMENTATION GAP: No TPV callback is in this folder. -->

## Verify the Payment Server-Side

<!-- DOCUMENTATION GAP: No TPV-specific verify sample is in this folder. The shared verify call is Verify Payment. -->

<Verify_Payment_Tabs />

## Test Credentials

<!-- DOCUMENTATION GAP: No TPV test account number, IFSC, or OTP is in this folder. The net-banking test login (payu / payu / 123456) is for the net-banking page, not labeled as TPV. -->

## Related Resources

<Cards columns={2}>
  <Card title="Net Banking TPV guide" icon="fa-arrow-up-right-from-square" href="https://docs.payu.in/docs/net-banking-integration-for-tpv/">
    The document the current TPV page links to.
  </Card>
  <Card title="Net Banking" icon="fa-building-columns" href="./net-banking">
    The test net-banking post, which does not include account number or IFSC.
  </Card>
  <Card title="EFTNET" icon="fa-money-bill-transfer" href="./eftnet">
    The other place the overview mentions account number and IFSC.
  </Card>
</Cards>
