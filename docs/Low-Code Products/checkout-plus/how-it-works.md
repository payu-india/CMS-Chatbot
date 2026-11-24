---
title: How Checkout Plus Works
excerpt: How the Bolt modal, launch call, and payment result fit together
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: How Checkout Plus Works | PayU Developer Docs
  description: >-
    See how PayU Checkout Plus opens a Bolt payment modal on your page, which
    script URLs to load, and how a UPI payment moves from Buy Now to the result.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

## Architecture Overview

Your page loads the Bolt script from PayU. When the customer pays, the page calls `bolt.launch(data, handlers)`. PayU opens the payment modal on top of your page and collects the payment there. The Checkout Plus API page says this modal presents the same `_payment` collect flow as [PayU Hosted Checkout](../payu-hosted-checkout-1).

When the attempt finishes, Bolt calls `responseHandler`. If the SDK hits an exception, it calls `catchException`.

<!-- DOCUMENTATION GAP: The source does not include a sequence diagram, and it does not say whether the browser also navigates to surl or furl after responseHandler runs. The customer journey says the success or failure page depends on surl and furl. -->

## Endpoints

| Environment | URL | Role |
| --- | --- | --- |
| Test | `https://jssdk-uat.payu.in/bolt/bolt.min.js` | Bolt script while you test |
| Production | `https://jssdk.payu.in/bolt/bolt.min.js` | Bolt script for live traffic |
| Post-service | `POST https://info.payu.in/merchant/postservice.php?form=2` | `verify_payment`, `check_action_status`, and `get_transaction_info` |

<!-- DOCUMENTATION GAP: Test and production _payment URLs are not written in the Checkout Plus pages. The API page says they are the same as PayU Hosted Checkout. Link the hosted collect-payment reference instead of copying URLs from another guide: https://docs.payu.in/reference/_payment_payu_hosted_checkout -->

## Key Parameters

`bolt.launch()` takes the transaction fields in its first argument. These are the fields the integration page documents. Full tables are on [Build the Integration](./integration-guide/build-integration).

| Parameter | Required in source | What the source says it is for |
| --- | --- | --- |
| `key` | Mandatory | Merchant key |
| `hash` | Mandatory | Tamper check. Formula is not stated on these pages. |
| `txnid` | Mandatory | Your order reference. PayU does not accept a duplicate transaction ID. |
| `amount` | Mandatory | Transaction amount. The unit is inconsistent in source. See Build the Integration. |
| `firstname` | Mandatory | Customer first name |
| `email` | Mandatory | Customer email |
| `phone` | Mandatory | Customer phone |
| `productinfo` | Mandatory | Short product description |
| `surl` | Mandatory | URL for the final response when the transaction succeeds |
| `furl` | Mandatory | URL for the final response when the transaction fails |
| `pg` | Optional | Payment category to display. Source says the default is `CC`. |
| `bankcode` | Optional | Bank code for the payment option. No value list is published here. |
| `drop_category` | Optional | Hide one or more payment options. Sample: `creditcard\|debitcard` |
| `enforce_paymethod` | Optional | Limit modes, schemes, or net-banking banks. Sample: `creditcard\|debitcard\|HDFB\|AXIB` |
| `custom_note` | Optional | Note shown for the transaction |
| `note_category` | Optional | Which categories see `custom_note`. Source example: `CC, NB` |
| `display_lang` | Not in the parameter table | Sample data object sets `display_lang` to `Hindi`. |

<!-- DOCUMENTATION GAP: No allowed-value list is published for pg, bankcode, or display_lang. The sample sets pg to CC. enforce_paymethod and drop_category examples are the strings above, not a complete code list. -->

## Hash Generation

### Request Hash

The `hash` field is mandatory. The integration page points hash generation to [Encryption of Request](https://docs.payu.in/docs/generate-hash-merchant-hosted). The API page says the hash on `_payment` is the same family as PayU Hosted Checkout unless the Checkout Plus guide specifies additional fields. The Checkout Plus guide does not list additional hash fields.

<!-- DOCUMENTATION GAP: The request hash formula and field order are not stated in the Checkout Plus product pages. Do not copy a formula from custom_blocks/PayUCheckoutPlusWizard.mdx until the docs team confirms it. No language samples are included here for that reason. -->

<!-- VALIDATION NEEDED: Integrate Checkout Plus links to the merchant-hosted hash guide. The API page says the _payment hash matches PayU Hosted Checkout unless Checkout Plus adds fields. Those two statements are not reconciled in source. -->

### Response Hash Verification

The response includes a `hash` field. The integration page says it is used like the request hash and links to [Generate Hash](https://docs.payu.in/docs/generate-hash-merchant-hosted).

<!-- DOCUMENTATION GAP: No reverse-hash formula is stated in the Checkout Plus product pages. Do not copy a reverse formula from the Checkout Plus wizard until the docs team confirms it. -->

## Payment Flow — Step by Step

<Accordion title="1. The page loads the Bolt script" icon="fa-circle-1">

The header includes the viewport meta tag and either the UAT or the production `bolt.min.js` URL.

</Accordion>

<Accordion title="2. The customer chooses to pay" icon="fa-circle-2">

Your page handles the click. The published sample binds that click to `#submit`.

</Accordion>

<Accordion title="3. The page calls bolt.launch()" icon="fa-circle-3">

The first argument is the transaction data. The second argument is the handlers object with `responseHandler` and `catchException`.

</Accordion>

<Accordion title="4. The customer pays inside the PayU modal" icon="fa-circle-4">

PayU collects the payment in the modal. The customer does not type card data into your page.

</Accordion>

<Accordion title="5. A bank or 3-D Secure failure can return to the modal form" icon="fa-circle-5">

The overview says the customer can land back on the Checkout Plus payment form and continue the current order, without starting checkout again.

</Accordion>

<Accordion title="6. Bolt calls responseHandler or catchException" icon="fa-circle-6">

The sample treats `txnStatus` of `SUCCESS`, `FAILED`, and `CANCEL` in `responseHandler`. Exceptions go to `catchException`.

</Accordion>

<Accordion title="7. Confirm the result with Verify Payment" icon="fa-circle-7">

The API page names `verify_payment` to retrieve status by your transaction ID. The launch sample does not show this call.

<!-- DOCUMENTATION GAP: No Verify Payment request sample is included in the Checkout Plus pages. -->

</Accordion>

## What the Customer Sees

### Sample UPI journey

This is the published Checkout Plus walkthrough for a UPI payment. Button names on your site can differ. The transaction flow stays broadly the same.

**Step 1.** The customer enters the mobile number and email for their account and clicks Buy Now.

<Image src="https://files.readme.io/dba2a2d-getobject.jpeg" align="center" />

The payment modal opens on the same page.

<Image src="https://files.readme.io/3e1fe55-getobject_1.jpeg" align="center" />

**Step 2.** The customer selects UPI and an app such as PhonePe, Google Pay, BHIM, or Paytm, enters the UPI ID, and clicks Proceed once the ID is verified. The published example uses PhonePe.

<Image src="https://files.readme.io/a1b98cd-getobject_2.jpeg" align="center" />

**Step 3.** The modal waits for the customer to approve the payment.

<Image src="https://files.readme.io/3652db8-getobject_3.jpeg" align="center" />

The screen then shows success or failure. On failure, Retry starts again from step 1 of this journey.

<Callout icon="⚠️" theme="warn">

The page shown for a successful or failed transaction depends on the `surl` and `furl` in the transaction request.

</Callout>

<!-- DOCUMENTATION GAP: Customer steps for cards, net banking, wallets, EMI, and BNPL are not documented. This section is the UPI sample only. -->

## PCI-DSS Scope

The modal is served from PayU servers. The overview says you do not have to take on PCI-DSS compliance for collecting payment details on your site.

<!-- DOCUMENTATION GAP: No SAQ type is stated in the Checkout Plus pages. -->

## When to Use Checkout Plus vs PayU Hosted Checkout

| Situation | Use |
| --- | --- |
| The customer should pay in a modal on your page | Checkout Plus |
| The customer should be redirected to a PayU page, including inside an app WebView | [PayU Hosted Checkout](../payu-hosted-checkout-1) |
| You want Checkout Plus without PayU Hosted Checkout | Not available. Checkout Plus is only available for PayU Hosted Checkout. |

The integrate page says Checkout Plus is not recommended for app browsers such as WebView or Chrome Custom Tabs.

## Key Concepts

<Accordion title="Bolt SDK" icon="fa-code">

The script at `bolt.min.js`. Test and production use different hosts. See Endpoints above.

</Accordion>

<Accordion title="bolt.launch(data, handlers)" icon="fa-window-restore">

Opens the modal. `data` is the transaction object. `handlers` contains `responseHandler` and `catchException`.

</Accordion>

<Accordion title="responseHandler" icon="fa-reply">

Called when the transaction completes, fails, or is canceled. The sample reads `BOLT.response.txnStatus`.

</Accordion>

<Accordion title="catchException" icon="fa-triangle-exclamation">

Called when the SDK captures an exception. The page does not list exception types.

</Accordion>

<Accordion title="txnStatus" icon="fa-flag">

Values checked in the sample: `SUCCESS`, `FAILED`, `CANCEL`.

<!-- VALIDATION NEEDED: The response parameter table and the sample response body use status (success, failure, pending), not txnStatus. The sample response body does not contain txnStatus. -->

</Accordion>

<Accordion title="surl and furl" icon="fa-link">

Mandatory URLs. `surl` is where PayU sends the final response on success. `furl` is where PayU sends it on failure. The customer journey says the result page depends on these URLs.

</Accordion>

<Accordion title="mihpayid" icon="fa-hashtag">

PayU's reference for the transaction. The response description says to use it to identify a transaction for a refund.

</Accordion>
