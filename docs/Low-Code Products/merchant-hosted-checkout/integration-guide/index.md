---
title: Integration Guide
excerpt: Build, test, and take Merchant Hosted Checkout live
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Merchant Hosted Checkout Integration Guide | PayU Developer Docs
  description: >-
    Build, test, and go live with PayU Merchant Hosted Checkout. Method pages for cards, net banking, wallets, UPI Collect, PayPal, and Pluxee.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Integration Guide

<!-- NEW CONTENT: Landing page added so ReadMe lists this folder. A folder with no index.md is omitted from the sidebar, which hid Build the Integration, Test, and Go-Live. -->

This section is the build path for Merchant Hosted Checkout: post a payment for each method, test it, then switch to production.

<Cards columns={2}>
  <Card title="Build the Integration" icon="fa-code" href="./build-integration">
    Endpoints, hash, and one page per method: cards, net banking, wallets, UPI Collect, PayPal, and Pluxee.
  </Card>
  <Card title="Test Your Integration" icon="fa-flask" href="./test-integration">
    Test key and salt, and the test values published for each method.
  </Card>
  <Card title="Go-Live Checklist" icon="fa-list-check" href="./go-live-checklist">
    Production key, salt, and the production _payment endpoint.
  </Card>
</Cards>
