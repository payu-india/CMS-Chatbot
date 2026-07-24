---
title: Hosted Checkout Integration Demo
deprecated: false
hidden: false
metadata:
  robots: index
---
**`data/payu-hosted-demo/server.js`**

The checkout page submits customer and order data to the server, the server creates the PayU request, generates the hash, and returns an auto-submitting form to PayU.

## 1. Checkout form and initial parameters

The browser-side checkout form is in:

**`public/assets/app.js`**

The form submits to:

```html
<form action="/payu/checkout" method="post">
```

It sends:

```html
<input type="hidden" name="amount" value="...">
<input type="hidden" name="productinfo" value="...">

<input name="firstname">
<input name="email">
<input name="phone">
```

The storefront collects only:

- Order amount
- Product information
- Customer name
- Email
- Optional phone number

It does **not** collect card, CVV, UPI, banking, or wallet information. Those details are handled by PayU after the hosted redirect.

## 2. Receiving and normalising the checkout request

The route is registered in `server.js`:

```js
if (cleanPath === '/payu/checkout' && req.method === 'POST') {
  await handlePayUCheckout(req, res);
  return;
}
```

The request body is parsed by `readRequestBody()`.

Then the order is normalised:

```js
const order = normaliseOrder(input, createTransactionId());
```

The server creates the transaction ID itself:

```js
function createTransactionId() {
  return `serein-${Date.now()}-${crypto.randomBytes(6).toString('hex')}`;
}
```

This produces a value such as:

```text
serein-1710000000000-a1b2c3d4e5f6
```

The important point is that `txnid` is not accepted directly from the browser. It is generated server-side.

The normalised order contains:

```js
{
  txnid,
  amount,
  productinfo,
  firstname,
  email,
  phone,
  udf1,
  udf2,
  udf3,
  udf4,
  udf5
}
```

The `udf` fields are optional PayU custom fields.

## 3. Basic validation

The amount is validated before continuing:

```js
if (!validAmount(order.amount)) {
  send(res, 400, renderCheckoutError(
    'Please provide a valid order amount.'
  ), 'text/html; charset=utf-8');
  return;
}
```

The validation allows a positive amount with up to two decimal places.

The email is also validated:

```js
if (!order.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(order.email)) {
  send(res, 400, renderCheckoutError(
    'Please provide a valid customer email.'
  ), 'text/html; charset=utf-8');
  return;
}
```

## 4. Demo mode when credentials are absent

The application checks whether both credentials are available:

```js
function hasPayUCredentials() {
  return Boolean(
    String(process.env.PAYU_KEY || '').trim() &&
    String(process.env.PAYU_SALT || '').trim()
  );
}
```

If either credential is missing, the application does not contact PayU:

```js
if (!hasPayUCredentials()) {
  send(
    res,
    200,
    renderPaymentResult('success', order, true),
    'text/html; charset=utf-8'
  );
  return;
}
```

The user sees a clearly labelled simulated result:

> Simulated checkout complete  
> No request was sent to PayU and no payment was taken.

This makes the demo usable without exposing or hardcoding credentials.

## 5. PayU environment and endpoint

The endpoint is selected here:

```js
function getPayUEndpoint() {
  return getPayUEnvironment() === 'production'
    ? PAYU_PRODUCTION_ENDPOINT
    : PAYU_TEST_ENDPOINT;
}
```

The endpoints are defined as:

```js
const PAYU_TEST_ENDPOINT = 'https://test.payu.in/_payment';
const PAYU_PRODUCTION_ENDPOINT = 'https://secure.payu.in/_payment';
```

The default is the test environment:

```js
function getPayUEnvironment() {
  return String(process.env.PAYU_ENV || 'test')
    .trim()
    .toLowerCase() === 'production'
      ? 'production'
      : 'test';
}
```

Therefore:

- `PAYU_ENV` omitted → test endpoint
- `PAYU_ENV=test` → test endpoint
- `PAYU_ENV=production` → production endpoint

## 6. PayU request parameters

The actual PayU request is assembled in `renderPayUForm()`:

```js
const fields = {
  key: merchantKey,
  txnid: order.txnid,
  amount: order.amount,
  productinfo: order.productinfo,
  firstname: order.firstname,
  email: order.email,
  phone: order.phone,
  udf1: order.udf1,
  udf2: order.udf2,
  udf3: order.udf3,
  udf4: order.udf4,
  udf5: order.udf5,
  surl: `${baseUrl}/payu/success`,
  furl: `${baseUrl}/payu/failure`,
  hash: createPayUHash(
    { ...order, key: merchantKey },
    String(process.env.PAYU_SALT || '').trim()
  )
};
```

The main parameters are:

| Parameter | Purpose |
|---|---|
| `key` | PayU merchant key |
| `txnid` | Unique transaction ID |
| `amount` | Order amount |
| `productinfo` | Description of the order |
| `firstname` | Customer name |
| `email` | Customer email |
| `phone` | Customer phone |
| `udf1`–`udf5` | Optional merchant-defined fields |
| `surl` | Success callback URL |
| `furl` | Failure callback URL |
| `hash` | SHA-512 request signature |

The server converts these values into hidden HTML inputs:

```js
const inputs = Object.entries(fields)
  .map(([name, fieldValue]) => hiddenInput(name, fieldValue))
  .join('');
```

The generated HTML form posts to PayU:

```html
<form method="post" action="https://test.payu.in/_payment">
  ...
</form>
```

It automatically submits in the browser:

```html
<script>
  document.getElementById('payu-form').submit();
</script>
```

So the flow is:

```text
Storefront
   ↓
POST /payu/checkout
   ↓
Server generates signed PayU form
   ↓
Browser POSTs form to PayU Hosted Checkout
```

## 7. Server-side SHA-512 hash

The hash is created in `createPayUHash()`:

```js
function createPayUHash(fields, salt) {
  const sequence = [
    fields.key,
    fields.txnid,
    fields.amount,
    fields.productinfo,
    fields.firstname,
    fields.email,
    fields.udf1,
    fields.udf2,
    fields.udf3,
    fields.udf4,
    fields.udf5
  ]
    .map((item) => String(item == null ? '' : item))
    .join('|');

  return crypto
    .createHash('sha512')
    .update(`${sequence}||||||${salt}`, 'utf8')
    .digest('hex');
}
```

The resulting string follows this structure:

```text
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT
```

The important security properties are:

- The merchant salt is read only from `PAYU_SALT`
- The hash is generated on the server
- The salt is never sent to the browser
- The client-side JavaScript never creates the hash

## 8. Building success and failure URLs

The callback base URL is determined in `getBaseUrl()`:

```js
function getBaseUrl(req) {
  if (process.env.PUBLIC_URL) {
    return process.env.PUBLIC_URL.replace(/\/$/, '');
  }

  const forwardedProto = String(
    req.headers['x-forwarded-proto'] || ''
  ).split(',')[0].trim();

  const protocol = forwardedProto === 'https' ? 'https' : 'http';

  return `${protocol}://${req.headers.host || 'localhost:' + port}`;
}
```

The PayU request receives:

```js
surl: `${baseUrl}/payu/success`,
furl: `${baseUrl}/payu/failure`
```

For a deployed application, `PUBLIC_URL` should normally be configured so PayU can reach the correct callback address.

## 9. Handling PayU's response

The success and failure routes are registered here:

```js
if (cleanPath === '/payu/success' &&
    ['GET', 'POST'].includes(req.method)) {
  await handlePayUReturn(req, res, 'success');
  return;
}

if (cleanPath === '/payu/failure' &&
    ['GET', 'POST'].includes(req.method)) {
  await handlePayUReturn(req, res, 'failure');
  return;
}
```

The handler accepts either:

- PayU's normal POST callback
- A GET request for local testing or inspection

```js
async function handlePayUReturn(req, res, status) {
  let input = {};

  try {
    input = req.method === 'POST'
      ? await readRequestBody(req)
      : Object.fromEntries(
          new URL(req.url, 'http://localhost').searchParams
        );
  } catch {
    input = {};
  }

  send(
    res,
    status === 'success' ? 200 : 400,
    renderPaymentResult(status, input),
    'text/html; charset=utf-8'
  );
}
```

The result page displays safe order details such as:

- Transaction ID
- Amount
- Product information
- Customer name
- Email

Before rendering, values are HTML-escaped:

```js
function escapeHtml(value) {
  return String(value == null ? '' : value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}
```

This prevents returned values from being interpreted as HTML.

The response messages are:

```js
PayU returned a success response for this order.
```

or:

```js
PayU returned a failure response.
You can return to the storefront and try again.
```

## Important production limitation

This demo handles the response display, but it does **not yet verify PayU's response hash**.

That means the current success URL should be treated as a demonstration callback, not as authoritative proof that payment succeeded. Someone could theoretically call `/payu/success` directly with fabricated values.

A production implementation should additionally:

1. Verify PayU's response hash.
2. Confirm the returned transaction ID exists in the merchant database.
3. Compare the returned amount with the original order amount.
4. Check the returned payment status.
5. Make the callback idempotent so duplicate callbacks do not duplicate fulfillment.
6. Update the order status only after successful verification.
7. Avoid trusting the amount supplied by the browser; calculate the total from server-side cart or order data.

The README in the project also calls out this limitation:

> A production implementation should additionally verify PayU's response hash and persist order state before treating a callback as authoritative.

One further demo-specific limitation is that the cart and total are calculated in the browser. For a real payment flow, the server should load the order from a server-side store and calculate the payable amount independently before generating the PayU request.