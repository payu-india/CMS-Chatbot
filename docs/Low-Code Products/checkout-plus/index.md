---
title: Checkout Plus
excerpt: Open a PayU payment modal on your website with the Bolt JavaScript SDK
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Checkout Plus | PayU Developer Docs
  description: >-
    PayU Checkout Plus opens a payment modal on your site through the Bolt
    JavaScript SDK. One call covers cards, UPI, net banking, wallets, EMI, and BNPL.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Banner
  isInline={true}
  message="Integration effort: a Bolt script and bolt.launch() on your site. PayU serves the payment modal."
  color="#FF6B00"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

Checkout Plus keeps the customer on your website while they pay. The payment page opens as a modal, served from PayU, so the customer does not enter card data on your page. PayU Checkout Plus is only available for [PayU Hosted Checkout](../payu-hosted-checkout-1).

![Checkout Plus modal](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/09/image2-1024x585.jpg)

## What Can I Build with Checkout Plus?

<Accordion title="Keep the customer on your page" icon="fa-window-restore">

The modal opens on your site. The customer stays in the context of your website for the payment, instead of leaving for a separate payment page.

</Accordion>

<Accordion title="Accept the payment methods PayU shows in the modal" icon="fa-credit-card">

One `bolt.launch()` call covers the methods listed for Checkout Plus: Credit Card, Debit Card, Net Banking, UPI, Wallet, EMI, and BNPL. PayU renders those methods inside the modal. You do not build a separate flow per method.

</Accordion>

<Accordion title="Let the customer retry without leaving the payment" icon="fa-rotate-right">

If a payment fails at the bank or on the 3-D Secure page, the customer can land back on the Checkout Plus payment form and continue the current order, instead of starting the whole checkout again.

</Accordion>

<Accordion title="Add a short JavaScript integration" icon="fa-code">

You add the Bolt script and call `bolt.launch()` when the customer chooses to pay. Later changes to the payment experience are made in the PayU modal.

</Accordion>

<Accordion title="Show offers and basic branding" icon="fa-palette">

The current overview says you can align UI colours and your logo with your brand, and create offers in the PayU Dashboard so the customer sees applicable offers on the checkout page.

<!-- DOCUMENTATION GAP: No dashboard path, parameter, or sample is documented for logo, colour, or offer setup in the Checkout Plus source pages. -->

</Accordion>

## Is Checkout Plus Right for Me?

| I want to… | Works? |
| --- | --- |
| Take payment in a modal while the customer stays on my page | Yes |
| Cover cards, UPI, net banking, wallets, EMI, and BNPL in one call | Yes |
| Keep card entry off my page | Yes. The modal is served from PayU. |
| Use Checkout Plus without PayU Hosted Checkout | No. Checkout Plus is only available for PayU Hosted Checkout. |
| Open checkout inside an in-app WebView or Chrome Custom Tab | Not recommended. Use redirection-based [PayU Hosted Checkout](../payu-hosted-checkout-1). |

<Callout icon="📘" theme="info">

Not sure which PayU product fits? Compare the options on [Start Here](https://docs.payu.in/docs/start-here).

</Callout>

## Common Use Cases

<Cards columns={3}>
  <Card title="Stay on the cart or product page" icon="fa-cart-shopping" href="./how-it-works">
    The modal opens on the current page. The customer does not leave your site to pay.
  </Card>
  <Card title="Recover a failed payment in the modal" icon="fa-rotate-right" href="./how-it-works">
    After a bank or 3-D Secure failure, the customer can retry from the Checkout Plus form without starting checkout again.
  </Card>
  <Card title="One website integration" icon="fa-code" href="./integration-guide/build-integration">
    The same Bolt script and bolt.launch() call serve every method enabled for the account.
  </Card>
</Cards>

## What Do I Need to Get Started?

- A PayU merchant account
- PayU Hosted Checkout available on that account. Checkout Plus is only available for PayU Hosted Checkout.
- Your merchant key, and a `hash` value to pass into `bolt.launch()`
- A page that can load the Bolt script
- Values for `surl` and `furl`

<!-- DOCUMENTATION GAP: The Checkout Plus pages do not describe where to copy the test key and salt, and they do not state that surl and furl must be HTTPS. The published sample uses http:// URLs. -->

<!-- NEW CONTENT: Test-key retrieval is included on Quick Start through the KeySaltReference block, which points at the shared key-and-salt guides. -->

## How Do I Integrate Checkout Plus?

<Accordion title="1. Add the Bolt script" icon="fa-circle-1">

Add the viewport meta tag and `bolt.min.js` to the page header. Use the UAT script while testing and the production script when you go live.

</Accordion>

<Accordion title="2. Call bolt.launch()" icon="fa-circle-2">

When the customer pays, pass a data object and a handlers object to `bolt.launch()`. The data object carries the transaction fields. The handlers object carries `responseHandler` and `catchException`.

</Accordion>

<Accordion title="3. Read the result in your handlers" icon="fa-circle-3">

`responseHandler` receives the result. The published sample checks `BOLT.response.txnStatus` for `SUCCESS`, `FAILED`, and `CANCEL`. `catchException` runs when the SDK reports an exception.

</Accordion>

<Accordion title="4. Confirm the payment with Verify Payment" icon="fa-circle-4">

The Checkout Plus API page names the Verify Payment API (`verify_payment`) for reconciliation. The `bolt.launch()` sample itself does not call it.

</Accordion>

<Callout icon="📘" theme="info">

Parameter tables, the launch sample, and the response fields are on [Build the Integration](./integration-guide/build-integration).

</Callout>

<!-- DOCUMENTATION GAP: No request-hash step is documented on the Checkout Plus pages. See How Checkout Plus Works. -->

## Is My Integration Secure?

Card details are entered in the modal PayU serves. The Checkout Plus overview says this keeps you out of PCI-DSS compliance for that collection.

<!-- DOCUMENTATION GAP: The Checkout Plus pages do not say that the hash must be generated on your server, that the salt must stay off the page, or how to verify the hash returned in the response. The hash field links to the merchant-hosted hash guide. -->

## How Does My Customer Pay?

The published customer journey is a UPI example. Labels on your site can differ. The flow of the transaction stays the same.

<Accordion title="1. The customer enters contact details and chooses Buy Now" icon="fa-circle-1">

The customer enters the mobile number and email on your page, then clicks Buy Now. The payment modal opens on the same page.

</Accordion>

<Accordion title="2. The customer pays with UPI inside the modal" icon="fa-circle-2">

The customer selects UPI, chooses an app such as PhonePe, Google Pay, BHIM, or Paytm, enters a UPI ID, and proceeds after the ID is verified. The published example uses PhonePe.

</Accordion>

<Accordion title="3. Checkout Plus waits for approval" icon="fa-circle-3">

The modal stays open while the customer approves the payment.

</Accordion>

<Accordion title="4. The customer sees success or failure" icon="fa-circle-4">

The result is shown on screen. If the payment fails, the customer can choose Retry and return to the payment form. The page shown after success or failure depends on the `surl` and `furl` you sent.

</Accordion>

Screenshots for this UPI example are on [How Checkout Plus Works](./how-it-works).

## Post-Payment Actions

<Cards columns={2}>
  <Card title="Verify Payment" icon="fa-circle-check" href="https://docs.payu.in/reference/verify_payment_api">
    Retrieve transaction status with the merchant transaction ID. Command verify_payment.
  </Card>
  <Card title="Check Action Status" icon="fa-receipt" href="https://docs.payu.in/reference/check_action_status_api_with_payu_id">
    Retrieve the status of capture, refund, and cancellation requests for a PayU ID. Command check_action_status.
  </Card>
</Cards>

<!-- DOCUMENTATION GAP: Settlements, chargebacks, and webhooks are not described in the Checkout Plus source pages. -->

## Use AI to Help You

You can ask an assistant to look up the Bolt setup and the `bolt.launch()` contract from these pages.

<!-- NEW CONTENT: Example prompts below are limited to tasks the Checkout Plus pages describe. -->

<Callout icon="📘" theme="info">

- How do I add the Bolt script for PayU Checkout Plus?
- What fields do I pass to bolt.launch()?
- How do I handle SUCCESS, FAILED, and CANCEL in responseHandler?
- How is Checkout Plus different from a full-page PayU Hosted Checkout redirect?

</Callout>

<Cards columns={2}>
  <Card title="PayU Developer MCP" icon="fa-server" href="doc:payu-devguide-builder-mcp-configuration">
    Search PayU developer docs from your editor.
  </Card>
  <Card title="Integration Lab demo" icon="fa-flask" href="https://www.payu.in/integrationlab/checkoutplus">
    Open the published Checkout Plus demo.
  </Card>
</Cards>

## Next Steps

<Cards columns={2}>
  <Card title="How It Works" icon="fa-diagram-project" href="./how-it-works">
    See the modal flow, the script URLs, and the UPI customer journey.
  </Card>
  <Card title="Quick Start" icon="fa-play" href="./quick-start">
    Load the UAT script and open the modal with bolt.launch().
  </Card>
  <Card title="Build the Integration" icon="fa-code" href="./integration-guide/build-integration">
    Use the full parameter tables, handlers, and response fields.
  </Card>
  <Card title="Checkout Plus APIs" icon="fa-rectangle-api" href="./checkout-plus-apis">
    See Bolt, the hosted collect-payment reference, and the post-payment commands.
  </Card>
</Cards>
