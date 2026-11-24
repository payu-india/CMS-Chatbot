---
title: Build the Integration
excerpt: Add the Bolt script, call bolt.launch(), and handle the payment result
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Build the Checkout Plus Integration | PayU Developer Docs
  description: >-
    Build PayU Checkout Plus with bolt.min.js and bolt.launch(). Includes
    request parameters, modal controls, responseHandler, and the response field list.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">

Checkout Plus is not recommended for app browsers such as WebView or Chrome Custom Tabs. For a redirection checkout, use [PayU Hosted Checkout](../../payu-hosted-checkout-1).

</Callout>

PayU Checkout Plus collects payment in a modal on your site. Add the Bolt script to the page header. When the customer clicks pay, call `bolt.launch()` with the transaction data and your handlers. PayU returns the result to the page.

## Endpoints

| Environment | URL | Role |
| --- | --- | --- |
| Test | `https://jssdk-uat.payu.in/bolt/bolt.min.js` | Bolt script |
| Production | `https://jssdk.payu.in/bolt/bolt.min.js` | Bolt script |
| Post-service | `POST https://info.payu.in/merchant/postservice.php?form=2` | `verify_payment`, `check_action_status`, `get_transaction_info` |

<!-- DOCUMENTATION GAP: _payment test and production URLs are not listed in the Checkout Plus pages. The API page says collection uses the same _payment URLs as PayU Hosted Checkout. See https://docs.payu.in/reference/_payment_payu_hosted_checkout -->

## Load the Bolt SDK

Add this meta tag and script to the HTML header.

<Accordion title="Production script" icon="fa-code">

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://jssdk.payu.in/bolt/bolt.min.js"></script>
```

</Accordion>

<Callout icon="📘" theme="info">

While testing, replace the script URL with `https://jssdk-uat.payu.in/bolt/bolt.min.js`.

</Callout>

## Request Parameters

`bolt.launch()` takes two arguments. The first is the data object. Types below are the types stated on the integration page.

### Mandatory Parameters

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
| `key` | String | Merchant key provided by PayU. Unique identifier for the merchant account. | Your Test Key |
| `hash` | String | Hash used to avoid transaction tampering. The page points to [Encryption of Request](https://docs.payu.in/docs/generate-hash-merchant-hosted). | See the gap below |
| `txnid` | String | Order reference you generate to track an order. It can be used only once. PayU does not accept a duplicate transaction ID. | `s7hhDQVWvbhBdN` |
| `amount` | integer, as described in the parameter table | See the validation note under this table. | `29935` in the table. The launch sample sends `'1'`. |
| `firstname` | String | Customer first name. | Ashish |
| `email` | String | Customer email. | `test@gmail.com` |
| `phone` | String | Customer phone. | `9876543210` |
| `productinfo` | String | Brief product description. | iPhone |
| `surl` | String | URL where PayU redirects the final response if the transaction is successful. | `https://apiplayground-response.herokuapp.com/` |
| `furl` | String | URL where PayU redirects the final response in case of failure. | `https://apiplayground-response.herokuapp.com/` |

<!-- DOCUMENTATION GAP: The hash example in the legacy table is a long hex string, not a formula. The formula and field order are not documented on the Checkout Plus pages. -->

<!-- VALIDATION NEEDED: amount is described as an integer in the currency subunit, such as paise. The table says an actual amount of 299.35 must be sent as 29935. The published launch sample sets amount to '1'. The published response sample shows amount: 10.00. Do not treat either unit as confirmed. -->

### Optional Parameters

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
| `lastname` | String | Customer last name. | Verma |
| `udf1` | String | User-defined field. Up to five fields: `udf1` through `udf5`. | Payment Preference |
| `udf2` | String | User-defined field. | Shipping Method |
| `udf3` | String | User-defined field. | Shipping Address1 |
| `udf4` | String | User-defined field. | Shipping City |
| `udf5` | String | User-defined field. | Shipping Zip Code |
| `pg` | String | Payment category to display. Source says the default is `CC` (Credit Card), and that Checkout Plus supports Net Banking, Credit/Debit Cards, UPI, and Wallet. | Empty in the parameter table. The launch sample sets `CC`. |
| `bankcode` | String | Each payment option has a bank code. Post the code for the option you want. | Empty in the parameter table |
| `codurl` | String | The legacy description says this field must contain the customer's address if Cash on Delivery is chosen. | Empty in the parameter table |
| `drop_category` | String | Hide one or more payment options. | `creditcard\|debitcard` |
| `enforce_paymethod` | String | Customise payment options for this transaction. Enforce payment modes, card schemes, and specific net-banking banks. | `creditcard\|debitcard\|HDFB\|AXIB` |
| `custom_note` | String | A custom note for the transaction. | You will be charged an extra amount of Rs 100 on this transaction |
| `note_category` | String | Which categories show `custom_note`. Source says an example such as `CC, NB` shows the note for Credit Card and Net Banking only. | Empty in the parameter table |
| `display_lang` | Not stated | Present on the published data object only. Not listed in the parameter table. | `Hindi` |

<!-- DOCUMENTATION GAP: Allowed values for pg, bankcode, note_category, and display_lang are not listed. The pg description names Net Banking, cards, UPI, and Wallet, and does not mention EMI or BNPL, which the product overview does list. -->

<!-- VALIDATION NEEDED: The overview lists Credit Card, Debit Card, Net Banking, UPI, Wallet, EMI, and BNPL. The pg description lists Net Banking, Credit/Debit Cards, UPI, and Wallet. The response mode field lists CC, DC, NB, CASH, EMI, CLEMI, and BNPL. -->

## Call bolt.launch()

The second argument is the handlers object: `responseHandler` and `catchException`.

The published sample listens for a click on `#submit`, then calls `bolt.launch(data, handlers)`. The sample variable written against `txnid` is `tnxID`. The parameter name is `txnid`.

<Accordion title="Published launch sample" icon="fa-code">

```javascript
$(document).on('click','#submit',function () {
  var data = { key: 'O85456',
    hash: hash,
    txnid: tnxID,
    amount: '1',
    firstname: 'surbhi',
    email: "text@example.com",
    phone: "1234567890",
    productinfo: 'BOLT',
    surl: 'http://thirdparty.com/testresponse.php',
    furl: 'http://thirdparty.com/testresponse.php',
    lastname: 'soni',
    enforce_paymethod: "creditcard|debitcard|HDFB|AXIB",
    display_lang: "Hindi",
    drop_category: "creditcard|debitcard",
    pg: "CC",
    custom_note: "You will be charged an extra amount of Rs 100 on this transaction"
  };
  var handlers = {responseHandler: function (BOLT) {
    if(BOLT.response.txnStatus == "SUCCESS"){
      console.log('Your payment has been successful');
    }
    if (BOLT.response.txnStatus == "FAILED") {
      console.log('Payment failed. Please try again.');
    }
    if(BOLT.response.txnStatus == "CANCEL"){
      console.log('Payment failed. Please try again.');
    }
  },
  catchException: function (BOLT) {
    console.log('Payment failed. Please try again.');
  }};
  bolt.launch( data , handlers );
});
```

</Accordion>

<Callout icon="📘" theme="info">

`O85456` is the key printed in the published sample. The parameter table tells you to pass your own test key. This page does not document `O85456` as a shared sandbox key.

</Callout>

## Customise the Modal

These optional fields are the only modal controls documented for Checkout Plus.

| Field | What the source says |
| --- | --- |
| `pg` | Payment category to display. Default stated as `CC`. |
| `bankcode` | Bank code of the payment option. No code list is published on this page. |
| `drop_category` | Hide one or more payment options. |
| `enforce_paymethod` | Enforce modes, card schemes, and specific net-banking banks for this transaction. |
| `custom_note` | Custom note for the transaction. |
| `note_category` | Limits `custom_note` to the categories you name. Source cites `CC, NB` for Credit Card and Net Banking. |
| `display_lang` | Set to `Hindi` in the launch sample. No other values and no description are in the parameter table. |

<!-- DOCUMENTATION GAP: Logo, colour, and offer setup are mentioned on the overview and have no fields or dashboard steps here. display_lang has no allowed-value list. -->

## Handle the Response

`responseHandler` fetches the response once the transaction is completed. For a successful, failed, or canceled transaction, the response parameters are returned to `responseHandler` using the logic you define.

### responseHandler statuses

The published handler checks `BOLT.response.txnStatus`:

| txnStatus | Sample behaviour |
| --- | --- |
| `SUCCESS` | Logs that the payment has been successful |
| `FAILED` | Logs `Payment failed. Please try again.` |
| `CANCEL` | Logs `Payment failed. Please try again.` |

<!-- VALIDATION NEEDED: The response field list below uses status, with values success, failure, and pending. It does not list txnStatus. The sample response body uses status: success and does not include txnStatus. -->

### catchException

`catchException` captures the transaction message when an exception occurs. The published function logs `Payment failed. Please try again.`

<!-- DOCUMENTATION GAP: No exception types or error codes are listed for catchException. -->

### Response fields

| Parameter | Description |
| --- | --- |
| `mihpayid` | Unique reference PayU creates for the transaction. Used to identify a transaction for a refund. |
| `mode` | Payment category used. Source values: `CC` (Credit Card), `DC` (Debit Card), `NB` (Net Banking), `CASH` (Cash Card), `EMI`, `CLEMI` (Cardless EMI), `BNPL` (Buy Now Pay Later). |
| `bankcode` | Code of the payment option used. Source examples: Visa Debit Card `VISA`, Master Debit Card `MAST`. |
| `status` | Status to map the order. Source says possible values are `success`, `failure`, or `pending`. It then says: if status is `failure` or `pending`, treat the transaction as failed. |
| `unmappedstatus` | PayU's internal status, including intermediate states. Source values: `dropped`, `bounced`, `captured`, `auth`, `failed`, `usercancelled`, or `pending`. See [Payment State Explanations](ref:payment-state-explanations). |
| `key` | Merchant key. |
| `error` | For a failed transaction, the reason for failure. |
| `error_message` | Error message. The page points to [Error Codes](ref:error-codes). |
| `bank_ref_num` | Bank reference number for a successful transaction. |
| `txnid` | Transaction ID you posted. |
| `amount` | Original amount sent in the request. |
| `productinfo` | Product information sent in the request. |
| `firstname` | First name sent in the request. |
| `lastname` | Last name sent in the request. |
| `email` | Email sent in the request. |
| `phone` | Phone sent in the request. |
| `hash` | Response hash. The page links to [Generate Hash](https://docs.payu.in/docs/generate-hash-merchant-hosted). |
| `PG_TYPE` | Payment gateway used for the transaction. |
| `udf1` | Same `udf1` sent in the request. |
| `udf2` | Same `udf2` sent in the request. |
| `udf3` | Same `udf3` sent in the request. |
| `udf4` | Same `udf4` sent in the request. |
| `udf5` | Same `udf5` sent in the request. |

<!-- VALIDATION NEEDED: The status description says both that pending is a possible status and that pending must be treated as a failed transaction. Confirm which instruction merchants should follow. The sample response uses the key error_Message, while this table uses error_message. -->

### Sample response

This is the published sample.

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
address1:
address2:
city:
state:
country:
zipcode:
email: test@gmail.com
phone: 9876543210
udf1:
udf2:
udf3:
udf4:
udf5:
udf6:
udf7:
udf8:
udf9:
udf10:
hash: afeab9dcf4e43d47f8fbf5a6838d393c70694a58e30ada08e6cb86ac943236c05717c5f5e4872d671fe81d0d9b2d9facd44e9a061ba621aff6f20c4343ea5dfa
field1:
field2:
field3:
field4:
field5:
field6:
field7:
field8:
field9: Transaction Completed Successfully
payment_source: payu
PG_TYPE: CC-PG
bank_ref_num: 7f0d5ada-59bb-41d7-9e41-20a6af2406c9
bankcode: CC
error: E000
error_Message: No Error
name_on_card: test
cardnum: 411111XXXXXX1111
cardhash: This field is no longer supported in postback params.
```

<!-- VALIDATION NEEDED: The sample includes fields that are not in the response table: cardCategory, discount, net_amount_debit, addedon, address1, address2, city, state, country, zipcode, udf6, udf7, udf8, udf9, udf10, field1 through field9, payment_source, name_on_card, cardnum, and cardhash. cardhash is explicitly no longer supported. error is E000 and error_Message is No Error on this success sample. The sample key JPM7Fg is not the key used in the launch sample. -->

### surl and furl

`surl` and `furl` are mandatory on the request. The parameter descriptions say PayU redirects the final response to `surl` on success and to `furl` on failure. The customer journey says the page displayed after success or failure depends on those URLs.

<!-- DOCUMENTATION GAP: The pages do not say whether Bolt redirects the browser to surl or furl, calls responseHandler only, or does both. -->

## Verify the Payment Server-Side

<Accordion title="Verify Payment API" icon="fa-circle-check">

The API page names this call for reconciliation with PayU.

| Item | Documented value |
| --- | --- |
| API | [Verify Payment API](https://docs.payu.in/reference/verify_payment_api) |
| Command | `verify_payment` |
| Endpoint | `POST https://info.payu.in/merchant/postservice.php?form=2` |
| Post-service hash | `sha512(key\|command\|var1\|SALT)` |

<!-- DOCUMENTATION GAP: No cURL, var1, or response example for verify_payment is included in the Checkout Plus pages. -->

</Accordion>

## Test Script

| Use | Script |
| --- | --- |
| Test | `https://jssdk-uat.payu.in/bolt/bolt.min.js` |
| Production | `https://jssdk.payu.in/bolt/bolt.min.js` |

<!-- DOCUMENTATION GAP: No test card, test VPA, or test OTP is documented for Checkout Plus. -->

## Related Resources

<Cards columns={2}>
  <Card title="Test the Integration" icon="fa-flask" href="./test-integration">
    UAT script and the handler scenarios you can exercise from the published sample.
  </Card>
  <Card title="Go-Live Checklist" icon="fa-rocket" href="./go-live-checklist">
    Switch the script URL to production.
  </Card>
  <Card title="Checkout Plus APIs" icon="fa-rectangle-api" href="../checkout-plus-apis">
    Bolt, collect payment, and the post-payment commands.
  </Card>
  <Card title="How It Works" icon="fa-diagram-project" href="../how-it-works">
    Flow, endpoints, and the UPI customer journey.
  </Card>
</Cards>
