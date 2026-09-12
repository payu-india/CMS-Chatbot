---
title: 'Tutorial: Net Banking Seamless Checkout Integration'
deprecated: false
hidden: true
metadata:
  robots: index
---
## Outcome and scope

By the end of this tutorial, a developer should be able to replace the Kettle & Co. sample's demonstration wiring with a server-authoritative PayU Net Banking merchant-hosted checkout. The resulting design creates the payable order on the server, calculates the PayU request hash without exposing the salt, lets the shopper choose a bank, posts the signed fields to PayU's `_payment` endpoint, validates the `surl`/`furl` response, and reconciles the transaction with `verify_payment` and webhooks before fulfilment.

This page is an integration tutorial and a static code review. It covers the Net Banking path only. It does not claim that the archive was run, that a payment was made, or that any payment flow, callback, webhook, bank, or PayU endpoint was tested. Snippets marked **Illustrative pseudocode** are framework-neutral examples to adapt to the current PayU contract and the application's database layer.

### Evidence labels

Use these labels while reading the page:

- **Observed source fact**: behaviour or value read from the Kettle archive paths listed in [Sources](#sources).
- **PayU documentation fact**: behaviour, parameter, environment, or formula present on the retrieved Net Banking documentation page.
- **Recommendation**: a safer production design or an implementation decision proposed by this tutorial. Recommendations are not claims about what the sample currently does.

## What the Kettle sample is

**Observed source fact.** Kettle & Co. is a static apparel storefront. `app.js` defines a small catalogue, stores cart rows in `localStorage`, calculates a browser-side total, and renders the catalogue and cart. The checkout page collects a name, email, phone, and address, displays the cart total, and links to separate payment-mode pages. `README.md` describes the site as static, with no build step.

For the Net Banking path, the relevant pages and helpers are:

- `checkout.html`: shopper contact form, cart summary, and payment-mode links.
- `payu-common.js`: shared order storage, client request helper, and hidden-form POST helper.
- `payu-netbanking.html`: bank selector and payment button.
- `server/payu-netbanking-server.js`: Node/Express reference route, request hash helper, command hash helper, and optional Net Banking status route.
- `success.html` and `failure.html`: simple landing pages.
- `app.js`: the cart/catalogue implementation that supplies the sample amount.
- `README.md`: run instructions, payment-mode mapping, and general PayU cautions.

## The exact sample flow

The conceptual flow is:

1. A shopper views Kettle & Co. products and adds catalogue IDs to the cart. The cart is held in browser `localStorage`.
2. On checkout, the page reads the cart and the shopper's contact fields.
3. `PayU.saveOrder()` stores an object under `sessionStorage` key `payu_order`.
4. The shopper opens `payu-netbanking.html`, the bank-selection page.
5. `PayU.getOrder()` reads `payu_order`, with browser-side fallbacks for amount, product description, name, email, and phone.
6. The page calls `PayU.createPayment(order)`. The shared helper sends JSON to `/api/payu/create-payment`.
7. The server-side Net Banking example exposes `POST /api/payu/netbanking/initiate`. It creates a timestamp-based transaction ID, formats the amount, hashes the request, and returns the payment fields.
8. The page adds `pg=NB` and the selected `bankcode` to the returned object.
9. `PayU.postToPayU()` builds a hidden HTML form and submits it with `POST` to the returned `action`. Browser form submission uses `application/x-www-form-urlencoded` semantics.
10. PayU processes the Net Banking payment and redirects to `surl` or `furl`.
11. The merchant callback handler must validate the returned hash and transaction details. A visual landing page alone is not proof of payment.
12. The server must reconcile the result with `verify_payment` and/or a configured PayU webhook, then apply an idempotent order-state update.

### Important wiring discrepancy in the supplied sample

**Observed source fact.** The supplied browser helper posts to `/api/payu/create-payment`, but the supplied Net Banking server file defines `/api/payu/netbanking/initiate`. No route alias or demonstrated application mount connects those two paths in the analysed files. The tutorial therefore describes the intended flow, but this mismatch must be fixed before the sample can be treated as an integrated Net Banking flow. The browser should call the route actually mounted for Net Banking, or the server should deliberately provide a documented compatibility route. Do not silently assume that the two paths are interchangeable.

There is a second navigation detail:

- The primary button in `checkout.html` calls `PayU.saveOrder()` and then navigates to `payu-cards.html`.
- The Net Banking mode is an anchor to `payu-netbanking.html`; that anchor does not itself call `saveOrder()`.

**Recommendation.** Make the mode-selection action save or create a server order before navigation, or make every payment-mode link use a common checkout handler. Otherwise, `payu-netbanking.html` may rely on an earlier `payu_order` or on the helper's guest/default fallbacks.

## PayU contract to implement

### Environments and endpoints

**PayU documentation fact.** The retrieved page identifies these `_payment` endpoints:

- Test: `https://test.payu.in/_payment`
- Production: `https://secure.payu.in/_payment`

**PayU documentation fact.** For Verify Payments, the page identifies:

- Test: `https://test.payu.in/merchant/postservice.php?form=2`
- Production: `https://info.payu.in/merchant/postservice.php?form=2`

Keep the environment as configuration selected on the server. Never allow a browser-supplied action URL or environment flag to select production.

### Net Banking parameters

**PayU documentation fact.** The page's mandatory parameter table includes `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `pg`, `bankcode`, `surl`, `furl`, and `hash`. It describes `txnid` as a merchant-generated reference for a specific order. It describes `bankcode` as the unique PayU code for the selected payment option and points merchants to the Net Banking code list.

**PayU documentation fact.** For Net Banking, the parameter table identifies `pg=NB`. The page's step summary contains a conflicting shorthand that says `pg=NEFT`; the parameter table and the Kettle Net Banking page use `NB`. Treat the current PayU parameter definition and the bank's supported code as authoritative, and confirm any future documentation change before release.

The documentation also lists optional address fields (`address1`, `address2`, `city`, `state`, `country`, and `zipcode`) and up to five user-defined fields (`udf1` through `udf5`). Include them only when they are part of the merchant's order model and use the exact hash position described below.

### Request hash

**PayU documentation fact.** The documented request hash is SHA-512 over this exact pipe-delimited sequence:

```text
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
```

An absent UDF is an empty string. The literal empty positions must not be removed. The salt is server-only.

### Response or reverse hash

**PayU documentation fact.** The retrieved page says that PayU returns a response hash based on the request parameters in reverse order. It gives this sequence:

```text
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

The callback handler should recompute this value from the received fields and compare it with the received hash using a constant-time comparison. It should then check that the transaction ID and amount correspond to the merchant's stored order before changing state.

### Verify Payments and webhooks

**PayU documentation fact.** The page recommends reconciliation using webhooks and/or the Verify Payments API. It describes webhooks as server-to-server callbacks and names the `verify_payment` command.

**PayU documentation fact.** The Verify Payments request hash is:

```text
sha512(key|command|var1|salt)
```

For `verify_payment`, `var1` is the transaction ID to verify. The page's documented Verify Payments request is form-encoded and contains `key`, `command=verify_payment`, `var1`, and `hash`. The retrieved page's response-parameter description identifies an outer service `status`, a `msg`, and `transaction_details`; its example shows a transaction status under the transaction ID. Do not mark an order paid from a browser redirect alone.

The page also says that Net Banking health can be checked with `getNetBankingStatus`. The sample includes a route that calls that service, but it does not show a robust interpretation, cache policy, or fallback UX.

## What the supplied source actually does

### `checkout.html` and `payu-common.js`

**Observed source fact.** The checkout inputs have IDs `firstname`, `email`, `phone`, and `address`. `PayU.saveOrder()` stores the following in `sessionStorage` under `payu_order`:

- `amount`: `Cart.total()` when `window.Cart` exists, otherwise `100`.
- `productinfo`: the literal `Kettle & Co. order`.
- `firstname`, `email`, and `phone`: values read from the checkout inputs.

The address is displayed as a field but is not stored in this object by `saveOrder()`.

**Observed source fact.** `PayU.getOrder()` attempts to parse `payu_order`. It returns `amount`, `productinfo`, `firstname`, `email`, and `phone`, using fallbacks when saved values are absent. Its fallbacks include a `100` amount, `Kettle & Co. order`, `Guest`, a guest email address, and a placeholder phone number. These are demonstration defaults, not acceptable order-authority rules.

**Observed source fact.** `PayU.createPayment(order)` sends a `POST` with JSON content type to `/api/payu/create-payment` and returns parsed JSON without checking the HTTP status first.

**Observed source fact.** `PayU.postToPayU(fields)` creates a form with `method="POST"`, uses `fields.action` or the shared test action as its action, creates hidden inputs for every non-null field except `action`, appends the form to the document, and calls `form.submit()`. The helper does not explicitly set a content type; normal browser form submission is the intended `application/x-www-form-urlencoded` POST.

### `payu-netbanking.html`

**Observed source fact.** The page displays `pg=NB` and has a `bankcode` selector with these values:

| Displayed bank           | Source value |
| ------------------------ | ------------ |
| HDFC Bank                | `HDFB`       |
| State Bank of India      | `SBIB`       |
| ICICI Bank               | `ICIB`       |
| Axis Bank                | `UTIB`       |
| Kotak Mahindra Bank      | `KKBK`       |
| Test Bank (sandbox only) | `TESTPGNB`   |

These are the values statically present in the archive. They are not a complete guarantee of current availability. Bank codes and health should be maintained against the merchant's current PayU configuration and documentation.

**Observed source fact.** On the payment button click, the page gets an order, awaits `PayU.createPayment(order)`, and passes the response fields together with `pg: "NB"` and the selected `bankcode` to `PayU.postToPayU()`. Thus `pg` and `bankcode` are added in the browser, while the server example returns the signed order fields and URLs.

### `server/payu-netbanking-server.js`

**Observed source fact.** The reference server uses Express JSON parsing and Node's `crypto` module. It defines a `paymentHash()` helper with the documented request sequence and a `commandHash()` helper with `key|command|var1|SALT`.

**Observed source fact.** `POST /api/payu/netbanking/initiate` builds a new object from client request data:

- `txnid`: `TXN` followed by `Date.now()`.
- `amount`: `Number(req.body.amount).toFixed(2)`.
- `productinfo`, `firstname`, `email`, and `phone`: copied from the request body.

It returns that object plus `key`, `hash`, an action pointing to the PayU test `_payment` endpoint, and `surl` and `furl` read from environment variables. The source does not include `pg` or `bankcode` in this server response; the client adds them before the form POST.

**Observed source fact.** The server reads a key and salt from environment variables with fallback values in the source. The literal fallback values are intentionally not reproduced in this tutorial. Sandbox credentials were present in the archive and must be removed or rotated rather than copied into an application, document, log, or example.

**Observed source fact.** The optional `GET /api/payu/netbanking/banks` route posts `getNetbankingStatus` with `var1=default` to the PayU information service and returns the parsed response. The source does not authenticate a caller to this route, validate the upstream response, cache it, or map it safely to the selector.

### `success.html`, `failure.html`, and `app.js`

**Observed source fact.** `success.html` displays a success message and a note telling the implementer to perform reverse-hash validation and `verify_payment`. `failure.html` displays a failure message and a link back to checkout. Neither page is a server callback handler in the analysed files. There is no demonstrated callback route, webhook receiver, persistence layer, order update, idempotency key, or server-side fulfilment decision.

**Observed source fact.** `app.js` uses `localStorage` for the cart. `Cart.total()` recomputes the amount from the browser's local catalogue and quantities. It contains product IDs such as `p1` through `p6`, but no server-side price authority is shown.

## Prerequisites

1. A PayU merchant account and the merchant key and salt obtained through the appropriate PayU dashboard or onboarding process. Keep these in a secret manager or deployment secret store. Do not place the salt in HTML, JavaScript served to the browser, source control, screenshots, or documentation.
2. A server-side order store with a unique internal order ID and a unique PayU `txnid` constraint.
3. A trusted product catalogue on the server. The browser may send product IDs and quantities, but not the payable total as an authority.
4. Public HTTPS callback endpoints for success and failure. Also prepare a public HTTPS webhook endpoint if webhooks are enabled for the merchant.
5. A configured test environment first. The retrieved PayU page identifies `https://test.payu.in/_payment` as the test payment endpoint and the test Verify Payments endpoint listed above.
6. A policy for order states, for example `created`, `payment_pending`, `paid`, `failed`, and `review`. Define allowed transitions before writing the callback.
7. A mechanism for structured, redacted logs and alerting. Never log salts, request hashes, full customer records, or bank credentials.

## Build the integration

The sections below show a production-shaped seam around the Kettle pages. They are not drop-in code and are deliberately labelled **Illustrative pseudocode**.

### 1. Create the order from product IDs on the server

**Recommendation.** Treat the browser cart as a proposal. Resolve every product ID against the server catalogue, calculate quantity and price on the server, create the order, and return only the identifiers and payment-safe fields needed to begin checkout.

**Illustrative pseudocode - authoritative server order creation:**

```js
// Illustrative pseudocode. Adapt validation, pricing, tax, inventory, and DB APIs.
app.post('/api/orders', requireAuthenticatedOrGuestCheckout, async (req, res) => {
  const lines = validateLineItems(req.body.items); // IDs and positive integer quantities only
  const customer = validateCustomer(req.body.customer);

  const catalogueRows = await catalogue.findByIds(lines.map(line => line.productId));
  assertEveryRequestedProductExists(lines, catalogueRows);

  const pricedLines = priceFromServerCatalogue(lines, catalogueRows);
  const total = calculateOrderTotal(pricedLines); // never req.body.amount
  const order = await orders.create({
    customer,
    lines: pricedLines,
    amount: formatAmountForPayU(total),
    currency: 'INR',
    state: 'payment_pending'
  });

  // Keep the PayU txnid stable for retries of this order, or create it once here.
  const txnid = await payuTxnIds.createForOrder(order.id);
  res.json({
    orderId: order.id,
    txnid,
    amount: order.amount,
    productinfo: buildProductInfo(order),
    firstname: customer.firstname,
    email: customer.email,
    phone: customer.phone
  });
});
```

The Kettle client can retain `sessionStorage` as a convenience for navigation, but the server order ID and server-calculated amount should be the source of truth. The Net Banking initiation route should accept an internal order ID, load the stored values, and ignore or reject client-supplied amount, product description, and customer identity fields that do not match the order.

### 2. Generate the request hash on the server

**Illustrative pseudocode - request hash:**

```js
import crypto from 'node:crypto';

function sha512(value) {
  return crypto.createHash('sha512').update(value, 'utf8').digest('hex');
}

function paymentHash({ key, salt, txnid, amount, productinfo, firstname, email,
                      udf1 = '', udf2 = '', udf3 = '', udf4 = '', udf5 = '' }) {
  const value = [
    key, txnid, amount, productinfo, firstname, email,
    udf1, udf2, udf3, udf4, udf5,
    '', '', '', '', '',
    salt
  ].join('|');
  return sha512(value);
}
```

The six empty strings after `udf5` preserve the documented `||||||` segment. Use the same normalized string values for hashing and for the fields posted to PayU. In particular, do not hash one amount representation and post another.

### 3. Select a bank and create the form POST

**Recommendation.** Keep the selector's display label separate from its PayU bank code. Populate the code list from a controlled server configuration and health policy rather than treating an archive snapshot as current.

**Illustrative pseudocode - browser bank selection and form POST:**

```js
// Illustrative pseudocode. The server has already created orderId and signed fields.
const bankcode = document.querySelector('#bankcode').value;
const signed = await fetch('/api/payu/netbanking/initiate', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ orderId, bankcode })
}).then(async response => {
  if (!response.ok) throw new Error('Payment initiation failed');
  return response.json();
});

const form = document.createElement('form');
form.method = 'POST';
form.action = signed.action; // server-selected test or production URL
for (const [name, value] of Object.entries({
  key: signed.key,
  txnid: signed.txnid,
  amount: signed.amount,
  productinfo: signed.productinfo,
  firstname: signed.firstname,
  email: signed.email,
  phone: signed.phone,
  pg: 'NB',
  bankcode,
  surl: signed.surl,
  furl: signed.furl,
  hash: signed.hash
})) {
  const input = document.createElement('input');
  input.type = 'hidden';
  input.name = name;
  input.value = value;
  form.appendChild(input);
}
document.body.appendChild(form);
form.submit(); // browser sends a form-encoded POST to PayU
```

The exact Kettle helper is more general: it accepts all returned fields, skips `action`, and submits the rest. For production, allowlist the fields rather than forwarding arbitrary JSON keys from a client or upstream response.

### 4. Implement the initiation route

**Recommendation.** Have the route load the order by `orderId`, validate the selected bank code, choose the environment from server configuration, and return the public payment fields. The route should not trust `amount`, `productinfo`, `firstname`, or `email` from the browser.

**Illustrative pseudocode - initiation:**

```js
app.post('/api/payu/netbanking/initiate', async (req, res) => {
  try {
    const { orderId, bankcode } = validateInitiationInput(req.body);
    const order = await orders.getForPayment(orderId);
    assertPaymentPending(order);
    assertAllowedBankCode(bankcode); // also apply current health policy

    const fields = {
      key: config.payu.key,
      txnid: order.payuTxnid,
      amount: order.amount,
      productinfo: order.productinfo,
      firstname: order.customer.firstname,
      email: order.customer.email,
      phone: order.customer.phone,
      pg: 'NB',
      bankcode,
      surl: config.payu.surl,
      furl: config.payu.furl
    };
    fields.hash = paymentHash({ ...fields, salt: config.payu.salt });

    await orders.markSubmitted(order.id, { bankcode });
    res.json({ ...fields, action: config.payu.paymentAction });
  } catch (error) {
    logPaymentError(error, { operation: 'initiate' });
    res.status(publicStatusFor(error)).json({ error: 'Unable to start payment' });
  }
});
```

Do not expose `salt` in `fields`, logs, JSON responses, or client JavaScript. The response shape above is an implementation contract for the merchant's own route, not an undocumented PayU response schema.

### 5. Validate the callback response

**PayU documentation fact.** The page says to validate the reverse hash before marking the transaction successful. The following is **Illustrative pseudocode** for a callback endpoint and uses only fields described by the retrieved page's reverse-hash discussion and sample response. Adapt the parser to the actual callback encoding and retain the raw response only under the merchant's privacy and retention policy.

```js
function reverseHash({ salt, status, udf1 = '', udf2 = '', udf3 = '', udf4 = '', udf5 = '',
                       email, firstname, productinfo, amount, txnid, key }) {
  return sha512([
    salt, status,
    '', '', '', '', '', '',
    udf5, udf4, udf3, udf2, udf1,
    email, firstname, productinfo, amount, txnid, key
  ].join('|'));
}

function constantTimeHexEqual(left, right) {
  if (typeof left !== 'string' || typeof right !== 'string') return false;
  const a = Buffer.from(left.toLowerCase(), 'utf8');
  const b = Buffer.from(right.toLowerCase(), 'utf8');
  return a.length === b.length && crypto.timingSafeEqual(a, b);
}

app.post('/payu/callback', async (req, res) => {
  const p = normalizeCallbackFields(req.body);
  try {
    const expected = reverseHash({ ...p, salt: config.payu.salt });
    if (!constantTimeHexEqual(expected, p.hash)) {
      await orders.recordPaymentAnomaly(p.txnid, 'reverse_hash_mismatch');
      return res.status(400).send('Invalid payment response');
    }

    const order = await orders.findByPayuTxnid(p.txnid);
    if (!order || !amountsEqual(order.amount, p.amount)) {
      await orders.recordPaymentAnomaly(p.txnid, 'unknown_or_amount_mismatch');
      return res.status(400).send('Payment could not be matched');
    }

    // Do not fulfil here solely from status. Reconcile below first.
    await orders.recordCallback(order.id, {
      status: p.status,
      mode: p.mode,
      bankcode: p.bankcode,
      bankRefNum: p.bank_ref_num
    });
    return res.redirect('/payment/pending?orderId=' + encodeURIComponent(order.id));
  } catch (error) {
    logPaymentError(error, { operation: 'callback', txnid: p.txnid });
    return res.status(500).send('Callback received; reconciliation pending');
  }
});
```

Use separate success and failure callback URLs only if both routes perform the same security checks. A success-looking callback is evidence to evaluate, not a fulfilment command. The callback handler should also verify the expected merchant key, payment mode, transaction, amount, and order state according to the merchant's policy.

### 6. Verify and reconcile with Verify Payments or webhooks

**PayU documentation fact.** The page identifies the Verify Payments command and the hash formula. **Illustrative pseudocode** for a server-side Verify Payments request:

```js
async function verifyPayment(txnid) {
  const command = 'verify_payment';
  const hash = sha512([
    config.payu.key, command, txnid, config.payu.salt
  ].join('|'));

  const body = new URLSearchParams({
    key: config.payu.key,
    command,
    var1: txnid,
    hash
  });

  const response = await fetch(config.payu.verifyAction, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body
  });
  if (!response.ok) throw new Error('Verify Payments request failed');
  return response.json(); // persist and interpret according to the current PayU contract
}
```

The retrieved page's example describes `transaction_details` keyed by transaction ID and a nested status. Do not manufacture fields when a response differs. Persist the raw response under controlled access, validate the transaction and amount against the order, and map only known payment states to the application's state machine.

For webhooks, expose an HTTPS server-to-server endpoint, authenticate or validate it using the current PayU webhook guidance configured for the merchant, parse only documented event fields, and enqueue reconciliation. If webhook delivery and callback delivery describe the same transaction, they must converge on one idempotent update path.

**Illustrative pseudocode - idempotent update:**

```js
async function reconcileAndUpdate(txnid, evidence) {
  return db.transaction(async tx => {
    const order = await tx.orders.lockByPayuTxnid(txnid);
    if (!order) throw new Error('Unknown transaction');
    if (!amountsEqual(order.amount, evidence.amount)) {
      await tx.paymentEvents.record(txnid, 'amount_mismatch', evidence);
      return { state: 'review' };
    }

    await tx.paymentEvents.insertIfAbsent({
      eventId: evidence.eventId || stableFingerprint(txnid, evidence),
      txnid,
      payload: evidence
    });

    if (order.state === 'paid') return { state: 'paid', changed: false };
    if (evidence.confirmed === true) {
      await tx.orders.updateState(order.id, 'paid');
      await tx.fulfilment.enqueueOnce(order.id);
      return { state: 'paid', changed: true };
    }
    if (evidence.finalFailure === true) {
      await tx.orders.updateState(order.id, 'failed');
      return { state: 'failed', changed: true };
    }
    await tx.orders.updateState(order.id, 'payment_pending');
    return { state: 'payment_pending', changed: true };
  });
}
```

The booleans in this snippet are application-level results after validating PayU evidence, not claims about undocumented PayU fields. `verifyPayment()` or a webhook adapter should produce them only after it has applied the current PayU response contract.

### 7. Handle errors without leaking payment data

**Recommendation.** Return a generic user-facing error, record a correlation ID, and send the detailed, redacted diagnostic to protected logs. Distinguish initiation failure, hash failure, callback mismatch, PayU pending state, upstream timeout, and reconciliation failure. Never ask a shopper to paste a bank password, OTP, or full payment response into support chat.

```js
// Illustrative pseudocode
try {
  const result = await verifyPayment(txnid);
  await reconcileAndUpdate(txnid, mapVerifiedResult(result));
} catch (error) {
  const correlationId = createCorrelationId();
  secureLogger.error({ correlationId, txnid, errorClass: classify(error) });
  await orders.markReconciliationPending(txnid, { correlationId });
  // The response contains no salt, hash, bank credential, or full customer record.
  res.status(202).json({ state: 'pending', correlationId });
}
```

## Architecture and sequence

```mermaid
sequenceDiagram
    participant Shopper
    participant Kettle as Kettle browser
    participant App as Merchant server
    participant DB as Order store
    participant PayU as PayU _payment
    participant Bank as Shopper bank
    participant Verify as PayU Verify/Webhook

    Shopper->>Kettle: Checkout and choose Net Banking
    Kettle->>App: Create order with product IDs and quantities
    App->>DB: Price from server catalogue; create payment_pending order
    DB-->>App: Internal order ID and stable txnid
    App-->>Kettle: Order reference and customer/payment fields
    Kettle->>App: Initiate with orderId and selected bankcode
    App->>DB: Load order; validate bank; compute request hash
    App-->>Kettle: key, txnid, amount, fields, hash, surl, furl, action
    Kettle->>PayU: application/x-www-form-urlencoded POST, pg=NB, bankcode
    PayU->>Bank: Redirect for bank authorisation
    Bank-->>PayU: Authorisation result
    PayU-->>Kettle: Redirect POST to surl or furl
    Kettle->>App: Callback fields
    App->>App: Reverse-hash and order/amount checks
    App->>Verify: verify_payment and/or receive webhook
    Verify-->>App: Reconciliation evidence
    App->>DB: Idempotent state update and fulfilment enqueue
    App-->>Shopper: Pending, success, or failure view
```

## Gaps, severity, and remediation

| Severity | Gap found by static inspection                                                                                                                           | Remediation                                                                                                                                                                                                     |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Critical | Sandbox credentials are present in the archive. This tutorial intentionally does not reproduce them.                                                     | Remove them from the repository and rotate them if they were ever exposed beyond the intended sandbox. Inject secrets only at runtime. Scan commits, artefacts, logs, and documentation.                        |
| Critical | The initiation route copies client-supplied amount, product information, name, email, and phone into the signed request.                                 | Accept an internal order ID, reload the order, calculate the amount from a server catalogue, validate customer data, and sign only server-owned values.                                                         |
| Critical | `payu-common.js` contains a client-visible key and a test action; the server also has fallback credentials.                                              | Keep environment selection and key configuration on the server. Remove fallback secrets, fail closed when configuration is missing, and return only the public key and signed fields needed for the form.       |
| High     | `txnid` is generated as `TXN` plus `Date.now()`.                                                                                                         | Generate a collision-resistant, auditable ID once per order, enforce uniqueness in the database, and define retry behaviour.                                                                                    |
| High     | There is no demonstrated persistence, authentication or abuse control, rate limiting, or robust input validation.                                        | Add order persistence, checkout authorization or abuse controls appropriate to the business, schema validation, request size limits, rate limiting, CSRF protection where applicable, and database constraints. |
| High     | No callback route, webhook receiver, or idempotent payment update is demonstrated.                                                                       | Implement HTTPS callback endpoints, configured webhooks, reverse-hash validation, Verify Payments reconciliation, an event log, and one idempotent state-transition function.                                   |
| High     | `success.html` can be reached directly and displays success without proof.                                                                               | Render success only after server-side reconciliation of the order. A direct page visit must show an unknown or pending state, never fulfilment.                                                                 |
| High     | The sample is test-oriented and does not demonstrate production switching.                                                                               | Select test or production endpoints through server deployment configuration, use separate credentials and callback URLs, and gate live mode with an explicit release checklist.                                 |
| Medium   | The bank selector contains a static snapshot of bank codes, including a sandbox-only entry.                                                              | Maintain codes from the current PayU configuration/documentation, validate them server-side, and hide or disable unhealthy options based on a controlled status policy.                                         |
| Medium   | The optional `getNetbankingStatus` route returns upstream JSON directly and has no access control, timeout, caching, schema validation, or safe mapping. | Protect the route, apply an upstream timeout, validate and cache the response, expose only the fields the UI needs, and define an outage fallback.                                                              |
| Medium   | `PayU.createPayment()` parses JSON without checking `response.ok`; the click handler has no visible error path.                                          | Check HTTP status, handle malformed JSON and timeouts, disable duplicate submits, show a retry-safe state, and retain the order for reconciliation.                                                             |
| Medium   | Address is collected but not persisted by `saveOrder()`; customer and payment data are browser-controlled.                                               | Decide which billing/shipping fields are needed, validate them server-side, and include optional PayU fields only when appropriate and consistently hashed.                                                     |
| Medium   | Logging and security behaviour are not defined.                                                                                                          | Use redacted structured logs, correlation IDs, secret scanning, TLS, dependency updates, CSP and security headers, and an access-controlled audit trail.                                                        |
| Medium   | The browser can reuse stale `sessionStorage` data, and the cart is local-only.                                                                           | Bind checkout to a server order with an expiry, reprice before payment, handle cart changes, and make replay/retry semantics explicit.                                                                          |

## Verify callbacks and reconcile

Use this checklist for every callback and webhook adapter:

1. Accept only HTTPS traffic at the edge and enforce the expected HTTP method and content type.
2. Parse the callback without assuming that a redirect to a success page means success.
3. Recompute the reverse hash using the exact field order and server-side salt.
4. Compare hashes in constant time and reject mismatches.
5. Find the order by the merchant's stored `txnid`; do not create an order from callback data.
6. Compare the callback amount and merchant key with the stored order.
7. Record the event and raw evidence under controlled retention, redacting secrets and unnecessary personal data.
8. Call `verify_payment` using the correct environment, command, transaction ID, and `sha512(key|command|var1|salt)` hash, unless a validated webhook is the chosen authoritative signal. Use both when the merchant's risk policy requires it.
9. Treat an outer verification failure, unknown transaction, amount mismatch, or unavailable response as pending/review, not paid.
10. Apply a database-guarded, idempotent transition. Enqueue fulfilment once, after confirmed payment.
11. Return a safe response quickly. Retry reconciliation asynchronously when upstream or database work cannot complete synchronously.

## Test the integration

The following are **documentation-based test facts and recommendations**, not test results from this task. The archive and this page were inspected statically; the payment flow was not run.

1. Configure a dedicated PayU test merchant and keep its values in runtime secrets. The retrieved PayU page identifies `https://test.payu.in/_payment` as the test `_payment` endpoint.
2. Configure the test Verify Payments endpoint as `https://test.payu.in/merchant/postservice.php?form=2`.
3. Use `pg=NB` for the Net Banking request and a bank code currently supported by the test merchant. The retrieved page shows `TESTPGNB` in its test-oriented material; do not infer that every code in the archive remains available.
4. Verify that the server computes the request hash using the exact documented formula, including empty UDF positions, and that the posted amount string is the string that was hashed.
5. Use HTTPS callback URLs that are reachable by the test environment. Exercise both success and failure outcomes using only PayU's current sandbox instructions and test credentials. Do not use production credentials or real bank credentials.
6. Inspect the callback handler with a controlled, non-live fixture: a valid reverse-hash fixture, a modified hash, an unknown `txnid`, and an amount mismatch. These are local validation fixtures, not PayU payment results.
7. Exercise Verify Payments using the test endpoint and confirm that the integration handles the documented outer service result and transaction details without assuming an undocumented response shape.
8. Deliver a duplicate callback and duplicate webhook fixture for the same transaction and verify that the order and fulfilment records change once.
9. Exercise a PayU health/status outage path and confirm that the UI does not offer a known unhealthy bank or incorrectly label an order as failed when the status is unknown.
10. Before release, record the exact test date, environment, merchant configuration version, callback evidence, reconciliation evidence, and reviewer. Do not put keys, salts, customer data, card values, bank passwords, or OTPs in the record.

## Go live

This is a **recommendation checklist** based on the PayU environments and verification requirements retrieved from the Net Banking page:

- Replace the test `_payment` action with `https://secure.payu.in/_payment` only in a production server configuration.
- Replace the test Verify Payments action with `https://info.payu.in/merchant/postservice.php?form=2` only in a production server configuration.
- Use production key and salt from the production secret store. Never copy a test secret from the archive or a browser bundle.
- Set distinct HTTPS `surl`, `furl`, and webhook URLs for the production domain. Verify that they resolve to authenticated application routes and not static success pages.
- Confirm `pg=NB` and all enabled bank codes against the merchant's current PayU configuration. Remove sandbox-only options.
- Confirm request-hash and reverse-hash tests with a reviewer and ensure the server never trusts a client amount.
- Confirm webhook configuration, Verify Payments reconciliation, retry policy, duplicate-event handling, and fulfilment idempotency.
- Add monitoring for initiation errors, callback hash failures, reconciliation lag, unknown transactions, amount mismatches, bank health changes, and callback delivery failures.
- Run secret scanning and dependency/security checks before deployment. Review CSP, TLS, cookie, CORS, CSRF, rate-limit, and PII-retention settings.
- Perform a controlled production smoke test according to the merchant's approved release process. This tutorial does not claim that one was performed.

## Troubleshooting

### The browser gets a 404 from payment initiation

Compare the client URL with the mounted server route. The analysed helper uses `/api/payu/create-payment`; the analysed Net Banking server defines `/api/payu/netbanking/initiate`. Align them deliberately and add an integration test for the route contract.

### PayU reports an invalid hash

Log only a correlation ID and a hash-input fingerprint. Check that the same exact strings were used for `amount`, `productinfo`, `firstname`, `email`, and each UDF in both the request and the hash. Confirm that missing UDFs are empty positions and that the correct environment's salt is loaded. Do not print the salt or full hash input.

### The callback says success but the order is not paid

This is expected until reverse-hash and reconciliation pass. Confirm that `txnid` maps to an existing order, the amount matches, the reverse hash is valid, and Verify Payments or a validated webhook confirms the result. Do not change this policy to trust `success.html`.

### A bank is missing or failing

The archive's selector is static. Check the current PayU bank-code configuration and the `getNetbankingStatus` result through a protected, timeout-bounded server route. Do not expose raw upstream responses or assume a stale bank code is active.

### Verify Payments returns no transaction

Keep the order in a pending or review state, check the environment and transaction ID, and retry according to the backoff policy. The retrieved page's example includes a transaction-details result indicating that a transaction may not be found; treat that as an outcome to interpret, not as proof of payment.

### Users see guest or default values

The shared helper's fallbacks are demonstration behaviour. Ensure that the client has a server order reference and that the initiation route loads the customer and amount from that order rather than accepting the helper's fallback values.

## Security

- Keep the PayU salt exclusively on the server and out of the archive, client bundle, browser storage, URLs, logs, screenshots, and support tickets.
- Treat all browser data, including product IDs, quantities, selected bank, amount, name, email, phone, and `sessionStorage`, as untrusted input.
- Use a server-side catalogue and order total. Validate product existence, quantity, currency, amount precision, customer fields, and bank code.
- Use HTTPS for the storefront, initiation endpoint, `surl`, `furl`, and webhook endpoint. Do not accept callback or action URLs from the browser.
- Apply authentication or abuse controls appropriate to the checkout model, CSRF protection for cookie-authenticated browser routes, CORS restrictions, request-size limits, rate limits, and replay protections.
- Use a unique order-to-`txnid` mapping and database uniqueness constraints. Do not use a timestamp alone as a transaction identity.
- Compute and compare request and reverse hashes exactly. Use constant-time comparison for received hashes.
- Never log bank login credentials, OTPs, card data, salts, full hashes, or unnecessary personal data. Redact payment evidence before debugging output.
- Make callback, webhook, Verify Payments, and fulfilment operations idempotent. Use event IDs or stable fingerprints and transactionally guarded state transitions.
- Do not render a success state or ship an order until server-side reconciliation confirms the transaction.
- Add dependency scanning, secret scanning, security headers, CSP, monitored error handling, and alerting for hash failures and reconciliation anomalies.

## Sources

### Retrieved PayU documentation

- [Net Banking Integration](https://docs.payu.in/docs/collect-payments-with-net-banking-seamless) - retrieved for the Net Banking merchant-hosted flow, environment endpoints, mandatory and optional parameters, `pg` and `bankcode`, request and reverse hash formulas, Verify Payments, webhooks, and Net Banking health guidance.

The page's example values are intentionally not reproduced here. No other PayU documentation page is cited in this tutorial.

### Kettle archive paths analysed

- `tmp/kettle_inspect/README.md`
- `tmp/kettle_inspect/checkout.html`
- `tmp/kettle_inspect/payu-common.js`
- `tmp/kettle_inspect/payu-netbanking.html`
- `tmp/kettle_inspect/server/payu-netbanking-server.js`
- `tmp/kettle_inspect/success.html`
- `tmp/kettle_inspect/failure.html`
- `tmp/kettle_inspect/app.js`

Archive root inspected: `tmp/kettle_inspect/`. The archive was inspected statically; this page makes no claim that its code was run or that a payment flow was tested.
