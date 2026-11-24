---
title: Checkout Plus APIs
excerpt: Bolt launch surface and the shared PayU APIs Checkout Plus tells you to call
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Checkout Plus APIs | PayU Developer Docs
  description: >-
    Checkout Plus uses bolt.launch() on your website. Payment collection and
    status lookups use PayU Hosted _payment and the shared post-service commands.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

Checkout Plus is the Bolt launch call on your page. Collecting the payment and looking it up afterwards use the shared PayU APIs below. There is no Checkout Plus OpenAPI file in `reference/`.

## Checkout Plus Surface

<Cards columns={2}>
  <Card title="Bolt script" icon="fa-code" href="./integration-guide/build-integration">
    Test: https://jssdk-uat.payu.in/bolt/bolt.min.js. Production: https://jssdk.payu.in/bolt/bolt.min.js.
  </Card>
  <Card title="bolt.launch(data, handlers)" icon="fa-window-restore" href="./integration-guide/build-integration">
    Opens the modal with the transaction data and returns the result to responseHandler or catchException.
  </Card>
  <Card title="PayU Hosted Checkout" icon="fa-layer-group" href="../payu-hosted-checkout-1">
    Prerequisite. Checkout Plus is only available for PayU Hosted Checkout.
  </Card>
</Cards>

## Payment APIs

<Cards columns={2}>
  <Card title="Collect Payment API" icon="fa-credit-card" href="https://docs.payu.in/reference/_payment_payu_hosted_checkout">
    Browser POST to _payment. The Checkout Plus API page says the modal uses the same collect flow as PayU Hosted Checkout.
  </Card>
</Cards>

<!-- DOCUMENTATION GAP: Do not copy Hosted Checkout parameter tables or _payment URLs onto this page. The Checkout Plus source does not list those URLs. -->

## Post-Payment APIs

<Cards columns={2}>
  <Card title="Verify Payment API" icon="fa-circle-check" href="https://docs.payu.in/reference/verify_payment_api">
    Command verify_payment. Retrieves transaction status and details using your transaction ID.
  </Card>
  <Card title="Check Action Status with PayU ID" icon="fa-receipt" href="https://docs.payu.in/reference/check_action_status_api_with_payu_id">
    Command check_action_status. Retrieves the status of capture, refund, and cancellation requests for a PayU ID.
  </Card>
  <Card title="Get Transaction Info API" icon="fa-circle-info" href="https://docs.payu.in/reference/get_transaction_info_api">
    Command get_transaction_info. Retrieves transaction details for an exact transaction time specified in minutes and seconds.
  </Card>
</Cards>

## API Quick Reference

| Use case | Command or call | Description |
| --- | --- | --- |
| Prerequisite hosted checkout | PayU Hosted Checkout | Hosted payment experience that must be available before you add the modal. |
| Open the modal | `bolt.launch(data, handlers)` | Loads Bolt, launches the modal, and returns the result to your page. |
| Collect payment | Browser form `POST` to `_payment` | Collects the payment through PayU Hosted Checkout, which Checkout Plus presents in a modal. |
| Verify a payment | `verify_payment` | Retrieves status and details by your transaction ID. |
| Check an action | `check_action_status` | Status of capture, refund, and cancellation for a PayU ID. |
| Get transaction info | `get_transaction_info` | Transaction details for an exact transaction time, in minutes and seconds. |

Post-service endpoint for the `command` APIs: `POST https://info.payu.in/merchant/postservice.php?form=2`

Post-service hash: `sha512(key|command|var1|SALT)`

<!-- VALIDATION NEEDED: The Checkout Plus API page says the hash on _payment is the same family as PayU Hosted Checkout unless the Checkout Plus guide specifies additional fields. The Checkout Plus guide does not specify additional hash fields, and it links hash generation to the merchant-hosted hash guide. Confirm which formula applies before publishing a request-hash sample. -->
