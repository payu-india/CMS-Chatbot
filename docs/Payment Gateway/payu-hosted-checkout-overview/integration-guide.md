---
title: Integration Guide
deprecated: false
hidden: false
metadata:
  robots: index
---
Follow these steps to integrate the PayU Hosted Checkout on your website.

<Callout icon="👍" theme="okay">
  **Payment Flow**

  Before you start integrating, it’s important to understand how PayU Hosted Checkout payment flow and customer journey works.
</Callout>

<HoverCardGrid
  columns={2}
  items={[
    {
      title: "",
      text: (
        <div style={{ color: "#000", padding: "8px" }}>
          <div style={{ display: "flex", alignItems: "center", gap: "8px", marginBottom: "6px" }}>
            <i className="fa fa-code" style={{ color: "#00b386", fontSize: "18px" }} />
            <h4 style={{ margin: 0, fontWeight: "600" }}>
              1. Build Integration
            </h4>
          </div>

          <p style={{ margin: 0 }}>
            <a href="/docs/prebuilt-checkout-payu-hosted">
              Follow these steps to build your test integration for PayU Hosted Checkout.
            </a>
          </p>
        </div>
      ),
    },
    {
      title: "",
      text: (
        <div style={{ color: "#000", padding: "8px" }}>
          <div style={{ display: "flex", alignItems: "center", gap: "8px", marginBottom: "6px" }}>
            <i className="fa fa-flask" style={{ color: "#00b386", fontSize: "18px" }} />
            <h4 style={{ margin: 0, fontWeight: "600" }}>
              2. Test Integration
            </h4>
          </div>

          <p style={{ margin: 0 }}>
            <a href="/docs/prebuilt-checkout-payu-hosted">
              Test your integration in the sandbox before going live.
            </a>
          </p>
        </div>
      ),
    },
    {
      title: "",
      text: (
        <div style={{ color: "#000", padding: "8px" }}>
          <div style={{ display: "flex", alignItems: "center", gap: "8px", marginBottom: "6px" }}>
            <i className="fa fa-check-circle" style={{ color: "#00b386", fontSize: "18px" }} />
            <h4 style={{ margin: 0, fontWeight: "600" }}>
              3. Production Checklist
            </h4>
          </div>

          <p style={{ margin: 0 }}>
            <a href="/docs/prebuilt-checkout-payu-hosted">
              Follow this checklist to ensure your integration is ready before going live.
            </a>
          </p>
        </div>
      ),
    },
  ]}
/>

## What You Are Building

In this step, you are:

* Creating a **payment request** on your backend
* Securing it using a **hash**
* Sending the user to  the **PayU Hosted Checkout** to complete the payment

This is the core of the integration. Everything else builds on top of this.

## Prerequisites

Go through the <Anchor label="prerequisites" target="_blank" href="https://docs.payu.in/v3.0_pg-web-checkout-restcng-new/docs/payu-hosted-checkout-quick-start#prerequisites">prerequisites</Anchor> before you proceed with the integration.

## 1. Build Integration

Perform the following steps to build your integration:

### Step 1.1 Prepare Payment Request Parameters

You need to collect and structure the required payment details before initiating a transaction.

These include the following parameters:

<Accordion title="Parameters and Description" icon="fa-sliders">
  Lorem ipsum dolor sit amet, **consectetur adipiscing elit.** Ut enim
  ad minim veniam, quis nostrud exercitation ullamco. Excepteur sint
  occaecat cupidatat non proident!
</Accordion>
