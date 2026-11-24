---
title: Quick Start — Checkout Plus
excerpt: Open the Checkout Plus modal on a test page with the UAT Bolt script
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Quick Start — Checkout Plus | PayU Developer Docs
  description: >-
    Load the PayU Checkout Plus UAT Bolt script, call bolt.launch() with a test
    transaction, and then read SUCCESS, FAILED, or CANCEL in the responseHandler.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">

Use the UAT Bolt script and your test key. Do not use live credentials on a test page.

</Callout>

## What You'll Build

A page that loads the UAT Bolt script and opens the PayU modal when the customer clicks the payment control.

## Step 1: Get Your Test Credentials

<!-- NEW CONTENT: The Checkout Plus pages say to pass your test key. They do not describe Dashboard navigation. This block points at the shared key-and-salt guides. -->

<KeySaltReference />

## Step 2: Generate the Hash

`hash` is a mandatory field on `bolt.launch()`. The integration page says it is there to prevent tampering and links to [Encryption of Request](https://docs.payu.in/docs/generate-hash-merchant-hosted).

<!-- DOCUMENTATION GAP: No hash formula and no hash code sample are published in the Checkout Plus pages. Do not add a formula until the docs team confirms whether Checkout Plus uses the merchant-hosted formula or the PayU Hosted Checkout formula. -->

## Step 3: Load the Bolt Script and Launch the Modal

| Environment | Script |
| --- | --- |
| Test | `https://jssdk-uat.payu.in/bolt/bolt.min.js` |

Put the viewport meta tag and the UAT script in the page header, then call `bolt.launch()` from the payment click. This sample follows the published request. It uses the UAT script, and it uses `Your Test Key` where the parameter table says to pass your test key. The full published sample, including every optional field, is on [Build the Integration](./integration-guide/build-integration).

<Accordion title="Minimal launch sample" icon="fa-code">

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://jssdk-uat.payu.in/bolt/bolt.min.js"></script>
```

```javascript
var data = {
  key: 'Your Test Key',
  hash: hash,
  txnid: txnid,
  amount: '1',
  firstname: 'surbhi',
  email: 'text@example.com',
  phone: '1234567890',
  productinfo: 'BOLT',
  surl: 'http://thirdparty.com/testresponse.php',
  furl: 'http://thirdparty.com/testresponse.php'
};

var handlers = {
  responseHandler: function (BOLT) {
    if (BOLT.response.txnStatus == "SUCCESS") {
      console.log('Your payment has been successful');
    }
    if (BOLT.response.txnStatus == "FAILED") {
      console.log('Payment failed. Please try again.');
    }
    if (BOLT.response.txnStatus == "CANCEL") {
      console.log('Payment failed. Please try again.');
    }
  },
  catchException: function (BOLT) {
    console.log('Payment failed. Please try again.');
  }
};

bolt.launch(data, handlers);
```

</Accordion>

<!-- VALIDATION NEEDED: The parameter table describes amount as an integer in paise (299.35 is sent as 29935). This sample, taken from the published data object, sends amount as '1'. The published response sample shows amount 10.00. Do not pick a unit until the docs team confirms it. -->

<Callout icon="📘" theme="info">

The published demo is at [https://www.payu.in/integrationlab/checkoutplus](https://www.payu.in/integrationlab/checkoutplus).

</Callout>

<!-- DOCUMENTATION GAP: No test card number, test VPA, or test OTP is documented in the Checkout Plus pages. -->

## Step 4: Handle responseHandler and catchException

`responseHandler` runs when the transaction completes. The sample branches on `BOLT.response.txnStatus`:

| txnStatus in the sample | What the sample does |
| --- | --- |
| `SUCCESS` | Logs that the payment was successful |
| `FAILED` | Logs a retry message |
| `CANCEL` | Logs a retry message |

`catchException` runs for an exception and, in the sample, logs a retry message.

<!-- VALIDATION NEEDED: The response parameter table uses status with success, failure, and pending. The handler sample uses txnStatus with SUCCESS, FAILED, and CANCEL. The published response body shows status: success and does not show txnStatus. -->

## Step 5: Verify the Payment Server-Side

The API page says to confirm the transaction with the [Verify Payment API](https://docs.payu.in/reference/verify_payment_api).

| Item | Value documented for Checkout Plus |
| --- | --- |
| Command | `verify_payment` |
| Endpoint | `POST https://info.payu.in/merchant/postservice.php?form=2` |
| Post-service hash | `sha512(key\|command\|var1\|SALT)` |

<!-- DOCUMENTATION GAP: The Checkout Plus pages do not include a Verify Payment cURL sample, var1 format, or response body. Use the linked Verify Payment API reference for the request contract. Do not reconstruct it here. -->

## Next Steps

<Cards columns={2}>
  <Card title="Build the Integration" icon="fa-code" href="./integration-guide/build-integration">
    Full parameter tables, optional modal controls, and the response field list.
  </Card>
  <Card title="Test the Integration" icon="fa-flask" href="./integration-guide/test-integration">
    UAT script URL and the SUCCESS, FAILED, and CANCEL handler cases.
  </Card>
</Cards>
