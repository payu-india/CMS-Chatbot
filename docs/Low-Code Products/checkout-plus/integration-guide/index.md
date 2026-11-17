---
title: Integrate Checkout Plus
excerpt: Where to build, test, and take Checkout Plus live
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Integrate Checkout Plus | PayU Developer Docs
  description: >-
    Start the Checkout Plus website integration. Build the Bolt launch call, test
    with the UAT script, and switch to the production script when you go live.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

Checkout Plus on a website is one path: load Bolt, call `bolt.launch()`, and handle the result. There is no separate build per payment method.

## The Integration Path

<Cards columns={2}>
  <Card title="Website" icon="fa-window-restore" href="./build-integration">
    Add the Bolt script and call bolt.launch() from your payment button.
  </Card>
  <Card title="In-app WebView or Chrome Custom Tab" icon="fa-mobile" href="../../payu-hosted-checkout-1/payu-hosted-checkout-webview-integration">
    Not recommended for Checkout Plus. Use redirection-based PayU Hosted Checkout.
  </Card>
</Cards>

<Callout icon="⚠️" theme="warn">

The Checkout Plus integrate page says this integration is not recommended for app browsers such as WebView or Chrome Custom Tabs.

</Callout>

## Before You Start

<Accordion title="PayU Hosted Checkout is required" icon="fa-layer-group">

Checkout Plus is only available for PayU Hosted Checkout. The API page lists that hosted integration as the prerequisite.

</Accordion>

<Accordion title="Bolt script URL" icon="fa-code">

Test: `https://jssdk-uat.payu.in/bolt/bolt.min.js`

Production: `https://jssdk.payu.in/bolt/bolt.min.js`

</Accordion>

<Accordion title="Hash" icon="fa-shield-halved">

`hash` is mandatory on the launch data object.

<!-- DOCUMENTATION GAP: The formula is not in the Checkout Plus pages. See How Checkout Plus Works. -->

</Accordion>

<Accordion title="surl and furl" icon="fa-link">

Both are mandatory. `surl` receives the final response on success. `furl` receives it on failure.

</Accordion>

<Accordion title="Verify Payment" icon="fa-circle-check">

The API page names `verify_payment` so you can reconcile the transaction with PayU. The launch sample does not call it. Call it from your server before you fulfil the order.

</Accordion>

## In This Section

<Cards columns={2}>
  <Card title="Build the Integration" icon="fa-code" href="./build-integration">
    Script tag, parameters, bolt.launch(), and response fields.
  </Card>
  <Card title="Test the Integration" icon="fa-flask" href="./test-integration">
    UAT script and handler scenarios.
  </Card>
  <Card title="Go-Live Checklist" icon="fa-rocket" href="./go-live-checklist">
    Switch the Bolt script to production and review the open gaps.
  </Card>
</Cards>
