---
title: Accept Payments with the PayU Go SDK
deprecated: false
hidden: true
metadata:
  robots: index
---
The PayU Go SDK enables you to integrate PayU's Payment Gateway into applications built with Go (Golang). Instead of handling low-level API requests, request signing, and response parsing manually, you can use the SDK to interact with PayU APIs through a simple and consistent interface.

## PayU Go Web SDK

Download the <Anchor target="_blank" href="https://github.com/payu-india/web-sdk-go/archive/refs/heads/main.zip">PayU Go</Anchor> sample app and go through the below folder structure.

| **File** | **Content** |
| -------- | ----------- |
|          |             |
|          |             |

***

## Prerequisites

Go through these prerequisites and dependencies before starting the integration.

***

## Integration Steps

<Callout icon="✋" theme="info">
  ### **Payment Flow**

  Before you start integrating, it’s important to understand how payment flow works in <Anchor target="_blank" href="https://docs.payu.in/v3.0_pg-web-checkout-restcng-new/docs/payu-payment-gateway-workflow">PayU Payment Gateway</Anchor>.
</Callout>

Follow these steps to integrate PayU Go SDK and accept payments.

<HoverCardGrid
  columns={3}
  items={[
    {
      title: '1. Build Integration',
      href: 'https://docs.payu.in/v3.0_pg-web-checkout-restcng-new/docs/integration-guide2#1-build-integration',
      icon: 'fa-code',
      target: '_self',
      text: 'Build your test integration for PayU Go SDK.',
    },
    {
      title: '2. Test Integration',
      href: 'https://docs.payu.in/docs/integration-guide2#2-test-integration',
      icon: 'fa-flask',
      target: '_self',
      text: 'Validate your PayU Go SDK integration by testing transactions in the sandbox environment.',
    },
    {
      title: '3. Production Checklist',
      href: 'https://docs.payu.in/docs/integration-guide2#3-go-live-checklist',
      icon: 'fa-check-circle',
      target: '_self',
      text: 'Follow this checklist to ensure your integration is ready before going live.',
    },
  ]}
/>

## 1. Build Integration

Below are the steps to build the integration:
