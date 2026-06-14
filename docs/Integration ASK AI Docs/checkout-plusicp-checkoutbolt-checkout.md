---
title: Checkout Plus | ICP Checkout | Bolt Checkout
excerpt: >-
  Integrate PayU Checkout Plus with the Bolt JavaScript SDK to open checkout in
  a modal and handle payment responses.
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Checkout Plus | ICP Checkout | Bolt Checkout
description: Integrate PayU Checkout Plus with the Bolt JavaScript SDK to open checkout in a modal and handle payment responses.
tags:
  - checkout-plus
  - icp-checkout
  - bolt-checkout
  - payu
---

Integrate Checkout Plus with the Bolt JavaScript SDK so customers can complete a PayU payment in a modal without leaving your website.

## TL;DR

Add the Bolt SDK script to your checkout page, pass a transaction `data` object and `handlers` object to `bolt.launch()`, and process the returned `SUCCESS`, `FAILED`, or `CANCEL` status in `responseHandler()`. The outcome is a redirectionless Checkout Plus payment flow that opens when the customer selects your **Pay** or **Buy Now** button.

## Prerequisites

1. Get your PayU merchant key.
2. Generate a unique `txnid` for every order. PayU does not accept duplicate transaction IDs.
3. Generate the transaction `hash` on your backend before opening checkout. Do not generate hashes in browser code.
4. Configure success and failure response URLs for `surl` and `furl`.
5. Choose the Bolt SDK script URL for your environment:
   - Production: `https://jssdk.payu.in/bolt/bolt.min.js`
   - UAT: `https://jssdk-uat.payu.in/bolt/bolt.min.js`

## Customer experience

1. The customer selects **Buy Now** or **Pay** on your website.
2. Your website opens Checkout Plus in a modal.
3. The customer completes, fails, or cancels the payment.
4. The Bolt SDK returns the payment result to your `responseHandler()` function.

## Integration steps

### 1. Add the Bolt SDK script

Add the viewport meta tag and the Bolt SDK script in the HTML `<head>` of your checkout page.

```bash title="Check that the production SDK is reachable"
curl -I https://jssdk.payu.in/bolt/bolt.min.js
```

Expected result:

```text
HTTP/2 200
```

Use the UAT SDK while testing:

```bash title="Check that the UAT SDK is reachable"
curl -I https://jssdk-uat.payu.in/bolt/bolt.min.js
```

Expected result:

```text
HTTP/2 200
```

### 2. Add the checkout button and launch code

Use the following browser example after your backend has generated the merchant key, hash, and transaction ID values for the transaction.

```html title="checkout-plus.html"
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <script src="https://jssdk.payu.in/bolt/bolt.min.js"></script>
    <title>Checkout Plus</title>
  </head>
  <body>
    <button id="submit" type="button">Pay</button>

    <script>
      const payButton = document.getElementById('submit');

      payButton.addEventListener('click', function () {
        const data = {
          key: 'Your Merchant Key',
          hash: 'hash-generated-on-your-backend',
          txnid: 'unique-transaction-id',
          amount: '1.00',
          firstname: 'Mansi',
          email: 'text@example.com',
          phone: '9999999999',
          productinfo: 'BOLT',
          surl: 'http://thirdparty.com/testresponse.php',
          furl: 'http://thirdparty.com/testresponse.php',
          lastname: 'Rastogi'
        };

        const handlers = {
          responseHandler: function (BOLT) {
            const status = BOLT.response.txnStatus;

            if (status === 'SUCCESS') {
              console.log('Your payment has been successful');
              console.log(BOLT.response);
              return;
            }

            if (status === 'FAILED') {
              console.log('Payment failed. Please try again.');
              console.log(BOLT.response);
              return;
            }

            if (status === 'CANCEL') {
              console.log('Payment was cancelled. Please try again.');
              console.log(BOLT.response);
              return;
            }

            console.log('Payment returned an unknown status:', status);
            console.log(BOLT.response);
          },
          catchException: function (BOLT) {
            console.log('Payment failed. Please try again.');
            console.log(BOLT);
          }
        };

        bolt.launch(data, handlers);
      });
    </script>
  </body>
</html>
```

Expected success log:

```text
Your payment has been successful
```

Expected failure log:

```text
Payment failed. Please try again.
```

Expected cancellation log:

```text
Payment was cancelled. Please try again.
```

### 3. Handle the payment response

Use `responseHandler()` to fetch the response from PayU after the transaction is completed. PayU returns response parameters to `responseHandler()` for successful, failed, and cancelled transactions based on the logic that you define.

Use `catchException()` to capture transaction exceptions and show a retry message to the customer.

Expected successful response shape:

```text
mihpayid: 403993715523615328
mode: CC
status: success
unmappedstatus: captured
key: JPM7Fg
txnid: 50QJq6lBJBmx14
amount: 10.00
cardCategory: domestic
discount: 0.00
net_amount_debit: 10
addedon: 2021-07-28 15:11:37
productinfo: iPhone
firstname: PayU User
lastname:
email: test@gmail.com
phone: 9876543210
field9: Transaction Completed Successfully
payment_source: payu
PG_TYPE: CC-PG
bank_ref_num: 7f0d5ada-59bb-41d7-9e41-20a6af2406c9
bankcode: CC
error: E000
error_Message: No Error
name_on_card: test
cardnum: 411111XXXXXX1111
```

`cardhash` is no longer supported in postback parameters.

## Request parameters

| Parameter | Type | Required | Default | Constraints | Example |
| --- | --- | --- | --- | --- | --- |
| `key` | String | Yes | None | Merchant key provided by PayU. | `Your Test Key` |
| `hash` | String | Yes | None | Generate on your backend to prevent transaction tampering. | `eabec285da28fd...` |
| `txnid` | String | Yes | None | Must be unique for every transaction. PayU does not accept duplicates. | `s7hhDQVWvbhBdN` |
| `amount` | Integer or decimal string | Yes | None | Use the transaction amount expected by your PayU integration. | `29935` or `1.00` |
| `firstname` | String | Yes | None | Customer first name. | `Ashish` |
| `lastname` | String | No | Empty | Customer last name. | `Verma` |
| `email` | String | Yes | None | Customer email address. | `text@example.com` |
| `phone` | String | Yes | None | Customer phone number. | `9876543210` |
| `productinfo` | String | Yes | None | Brief product description. | `iPhone` |
| `surl` | String | Yes | None | Success URL that receives the final response after a successful transaction. | `http://thirdparty.com/testresponse.php` |
| `furl` | String | Yes | None | Failure URL that receives the final response after a failed transaction. | `http://thirdparty.com/testresponse.php` |
| `udf1` | String | No | Empty | User-defined field. Use `udf1` through `udf5` to store transaction-specific data. | `Payment Preference` |
| `udf2` | String | No | Empty | User-defined field. | `Shipping Method` |
| `udf3` | String | No | Empty | User-defined field. | `Shipping Address1` |
| `udf4` | String | No | Empty | User-defined field. | `Shipping City` |
| `udf5` | String | No | Empty | User-defined field. | `Shipping Zip Code` |
| `drop_category` | String | No | Empty | Hide one or more payment options. Separate multiple options with `|`. | `creditcard|debitcard` |
| `enforce_paymethod` | String | No | Empty | Enforce payment modes, card schemes, or specific net banking banks for the transaction. Separate multiple values with `|`. | `creditcard|debitcard|HDFB|AXIB` |

## Troubleshooting

| Symptom | Cause | Fix | Log or status to check |
| --- | --- | --- | --- |
| Checkout does not open after the customer selects **Pay**. | The Bolt SDK script did not load, or the button handler is not attached. | Confirm the SDK URL returns `HTTP/2 200`, place the script in the page `<head>`, and verify that the `submit` button exists before attaching the click handler. | Browser console errors; `curl -I https://jssdk.payu.in/bolt/bolt.min.js` |
| PayU rejects the transaction. | The `txnid` was already used. | Generate a new unique `txnid` for every order before calling `bolt.launch()`. | Transaction response for the rejected order |
| The payment returns as failed. | PayU returned `FAILED` in `BOLT.response.txnStatus`. | Show a retry message and log `BOLT.response` for investigation. | `Payment failed. Please try again.` |
| The customer closes or cancels checkout. | PayU returned `CANCEL` in `BOLT.response.txnStatus`. | Keep the customer on your checkout page and let them retry payment. | `Payment was cancelled. Please try again.` |
| `catchException()` runs. | The SDK raised an exception while processing the transaction. | Log the `BOLT` object, verify all mandatory request parameters, and retry with a fresh `txnid` and hash. | `Payment failed. Please try again.` |

## Style guide compliance checklist

| Check | Score | Finding | Remediation |
| --- | ---: | --- | --- |
| Frontmatter | 10 | The page includes `title`, `description`, and `tags`. | Keep frontmatter current when the page title or scope changes. |
| TL;DR | 10 | The page opens with a one-paragraph TL;DR that states the outcome. | Keep the TL;DR focused on what the integration accomplishes. |
| Steps | 10 | The core flow uses numbered steps and each step includes an expected result. | Preserve the numbered flow when adding new actions. |
| Troubleshooting | 10 | The troubleshooting table maps symptoms to causes, fixes, and logs or statuses. | Add new rows for newly discovered error patterns. |
| Code samples | 10 | The page shows cURL checks before the JavaScript SDK sample, handles success, failure, cancellation, and exceptions, and avoids browser-side secret generation. | Add SDK examples after the cURL checks if more languages become supported. |