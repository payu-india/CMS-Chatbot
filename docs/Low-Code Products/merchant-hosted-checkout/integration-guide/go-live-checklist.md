---
title: Go-Live Checklist
excerpt: >-
  Switch Merchant Hosted Checkout from test credentials to the production key,
  salt, and endpoint.
deprecated: false
hidden: true
metadata:
  title: Merchant Hosted Checkout Go-live Checklist
  description: >-
    Go live with PayU Merchant Hosted Checkout: production key and salt from
    Key Salt Details, and the secure.payu.in/_payment endpoint.
  keywords:
    - payu merchant hosted go live
    - payu production key salt
    - payu secure.payu.in _payment
  robots: index
next:
  description: Explore related information and resources.
---
<Banner
  isInline={true}
  message="Integration effort: Developer required"
  color="#FFC107"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
 />

Work through this checklist before you accept live payments.<br />

Before you start, complete the previous two stages:

<Cards columns="2">
  <Card title="Build Integration" href="./build-integration" icon="fa-code">
    Request parameters, hash, form POST, reverse hash, and Verify Payment.
  </Card>
  <Card title="Test Integration" href="./test-integration" icon="fa-flask">
    Test values for the methods you enabled.
  </Card>
</Cards>

***

## 1. Switch to Production Credentials

<Accordion title="Replace Test Credentials With Live Credentials" icon="fa-user-lock">
  - [x] Log in to the PayU Dashboard and switch to Live Mode.
  - [x] Open **Payment Gateway → Web Integration → Key Salt Details**.
  - [x] Copy the production key and salt.
  - [x] Replace the test key and test salt in the integration code.

  <Callout icon="⚠️" theme="warn">
    ### **Important:**

    The salt is a secret. Do not put it in the browser.
  </Callout>
</Accordion>

***

## 2. Switch to the Production Endpoint

<Accordion title="Update the Payment Form Action URL" icon="fa-link">
  - [x] Point the form at `https://secure.payu.in/_payment`.
  - [x] Keep `method="post"`.
  - [x] Remove `https://test.payu.in/_payment` from the live code.

  | Environment | URL |
  | --- | --- |
  | Test | `https://test.payu.in/_payment` |
  | **Production** | `https://secure.payu.in/_payment` |
</Accordion>

***

## 3. Security Checklist

<Accordion title="Verify All Security Requirements" icon="fa-shield-halved">
  - [x] Hash is generated on the server.
  - [x] The salt is not in frontend code.
  - [x] The site and the callback URLs use HTTPS.
  - [x] The reverse hash is checked on every callback.
  - [x] CVV and the full card number are not stored.
  - [x] If you collect card data, PCI-DSS SAQ A-EP is completed.
</Accordion>

***

## 4. Configure Webhooks

<Accordion title="Set Up Server-To-Server Payment Notifications" icon="fa-plug">
  The production checklist says to confirm the transaction on the server if the callback fails, and to use webhooks to hear callbacks.

  - [x] Webhooks are enabled for production.
  - [x] You still call Verify Payment.

  <!-- DOCUMENTATION GAP: This folder does not give the Dashboard click-path or the HTTP status your endpoint should return. See https://docs.payu.in/docs/webhooks -->
</Accordion>

***

## 5. Production Readiness Verification

<Accordion title="Functional Verification" icon="fa-clipboard-check">
  - [x] Required checkout fields are collected and validated.
  - [x] The PayU response is verified.
  - [x] The reverse hash is checked.
  - [x] Each method you will enable has been tested. Advantage Club has no sandbox in the source.
</Accordion>

<Accordion title="Order Management Verification" icon="fa-list-check">
  - [x] `txnid` is unique for each attempt.
  - [x] You confirm status with Verify Payment before you fulfil the order.

  <!-- DOCUMENTATION GAP: Storing txnid before the post, and comparing the response amount, are not specified in this folder. -->
</Accordion>

***

## 6. Final Sign-off

The legacy checklist says to monitor transactions in the first days after go-live.

<Callout icon="✅" theme="okay">
  ### **After Going Live:**

  Watch the first live transactions and confirm callbacks are processed.
</Callout>

If you run into issues, see [Errors and Troubleshooting](../errors-and-troubleshooting).
