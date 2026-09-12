---
title: 'Tutorial: iOS Checkout Pro integration'
deprecated: false
hidden: true
metadata:
  robots: index
---
#

**Review status:** Static source review only. This tutorial analyses `tmp/marigold_studio_storefront.zip` after extraction to `tmp/marigold_inspect/` and the retrieved PayU page [iOS Checkout Pro SDK](https://docs.payu.in/docs/ios-checkoutpro-sdk). The iOS files were **not** built, installed, run, or tested. The archive contains Swift source and a Podfile, not a complete Xcode project or proven build output.

> Source labels used below:
>
> - **Observed source fact** means it is present in the archive.
> - **PayU documentation fact** means it was visible on the retrieved main PayU page.
> - **Recommendation** means a production change or verification step, not a claim about the archive or the page.

## Outcome and scope

The outcome is to map the complete storefront-to-server-to-iOS Checkout Pro flow and identify the production changes needed for trusted order amounts, server-side signing, response verification, and safe fulfilment.

This is a tutorial for iOS developers and technical writers explaining how the Marigold Studio storefront, its Node/Express backend, and its iOS Checkout Pro starter fit together. It is not a claim that the starter is production-ready. In particular, client data and the current demo flow must be replaced by a server-created order, server-side hash and response verification, durable order state, and an idempotent fulfilment workflow.

## Prerequisites

- An Apple developer project and a merchant-owned HTTPS backend. Do not substitute a public hosting service for the backend.
- A PayU merchant account, with test and production credentials obtained through the merchant’s approved PayU channels. Keep the salt only in server-side secret storage; do not paste credentials into this tutorial or the app.
- Xcode, Swift, the selected SDK version, and either CocoaPods or Swift Package Manager. The archive does not pin or include the SDK artifact.
- A product catalogue and order service that can calculate authoritative prices from product IDs.
- HTTPS callback URLs, server storage, authentication between the app and backend, logging with PII minimisation, and a plan for reconciliation/webhooks.
- Before implementation, confirm the current PayU iOS installation, dynamic-hash, response, redirect, UPI, and privacy-manifest pages. The retrieved main page links to more specific pages but their detailed content was not independently fetched for this review.

## Understand the complete package

### Package map

| Archive path                                                                                   | Role                                                                                       | Classification                                    |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------- |
| `marigold-studio/index.html`                                                                   | Home page, hero, featured product, six-product grid, cart drawer                           | Observed source fact                              |
| `marigold-studio/product.html`                                                                 | Product-detail shell; `assets/app.js` hydrates it from `?id=`                              | Observed source fact                              |
| `marigold-studio/checkout.html`                                                                | Contact/delivery form, payment choices, order summary, browser PayU launch point           | Observed source fact                              |
| `marigold-studio/success.html`                                                                 | Static confirmation page that tells the customer to verify server-side                     | Observed source fact                              |
| `marigold-studio/assets/styles.css`                                                            | Storefront styling and layout                                                              | Observed source fact                              |
| `marigold-studio/assets/app.js`                                                                | Product array, cart, `localStorage`, drawer, quantity controls, product hydration          | Observed source fact                              |
| `marigold-studio/assets/payu.js`                                                               | Browser-side amount calculation, hash request, hidden PayU form POST                       | Observed source fact                              |
| `marigold-studio/assets/logo.svg`, `product-1.svg` through `product-6.svg`, `hero-apparel.jpg` | Brand, placeholder product art, and hero image                                             | Observed source fact                              |
| `marigold-studio/ios/Podfile`                                                                  | CocoaPods declaration; iOS 13 deployment setting                                           | Observed source fact                              |
| `marigold-studio/ios/PayUConfig.swift`                                                         | Placeholder merchant configuration, environment, hash and callback URLs                    | Observed source fact                              |
| `marigold-studio/ios/PayUHashService.swift`                                                    | Async JSON request to the merchant hash endpoint                                           | Observed source fact                              |
| `marigold-studio/ios/PayUCheckoutManager.swift`                                                | `PayUPaymentParam` construction, Checkout Pro presentation, hash delegate, result delegate | Observed source fact                              |
| `marigold-studio/ios/CheckoutViewController.swift`                                             | Fixed demonstration checkout screen and UI result handling                                 | Observed source fact                              |
| `marigold-studio/ios/README.md`                                                                | Setup notes, SDK alternatives, example Info.plist entries, and test notes                  | Observed source fact; not independently validated |
| `marigold-studio/server/payu-hashes.js`                                                        | Express hash and verification routes                                                       | Observed source fact                              |
| `marigold-studio/robots.txt`                                                                   | Allows all crawlers                                                                        | Observed source fact                              |
| `marigold-studio/sitemap.xml`                                                                  | Example sitemap for home, product, and checkout paths                                      | Observed source fact                              |

No `.xcodeproj`, `.xcworkspace`, `Info.plist`, entitlements, privacy manifest, app delegate/scene delegate, URL scheme, or SDK binary/source artifact is present in the archive. The Swift signatures therefore require compile-time confirmation against the installed SDK version.

### End-to-end architecture and sequence

```mermaid
sequenceDiagram
    participant W as Storefront (browser)
    participant I as iOS view/controller
    participant B as Merchant HTTPS backend
    participant SDK as PayU Checkout Pro SDK
    participant P as PayU
    participant O as Order store/state

    W->>B: Send product IDs, quantities, and customer input
    I->>B: Create or fetch pending order for the app customer
    B->>O: Store authoritative lines, amount, customer, unique transaction ID
    B-->>I: Pending order snapshot
    I->>SDK: Build PayUPaymentParam from server snapshot
    SDK->>I: Request hash names/strings
    I->>B: Forward authenticated hash request
    B-->>I: Mapped hashes only; salt remains server-side
    I->>SDK: Complete hash callback
    SDK->>P: Open Checkout Pro and submit payment
    P-->>SDK: UI result/callback (provisional)
    P-->>B: Redirect/webhook or server-observed transaction result
    B->>P: Verify payment using the applicable server API
    B->>O: Idempotently transition pending to verified/fulfilment state
    I->>B: Fetch confirmed order status
    O-->>I: Paid/failed/pending state for UI

    rect rgb(245,245,245)
    Note over W,P: Browser-only branch observed in the archive
    W->>W: Read client cart/localStorage amount
    W->>B: POST payload to /payu/hashes
    B-->>W: hashes.payment
    W->>P: Hidden form POST to test payment action
    P-->>W: Redirect to static success.html or checkout failure URL
    end
```

The browser branch is not a substitute for server-created order state. The archive has no full iOS Xcode project and no proven build output; the diagram describes the target production shape, while the browser branch reflects the observed starter behavior.

## Trace the Marigold storefront

### Catalogue and cart

**Observed source fact:** `assets/app.js` defines six catalogue entries, with numeric IDs and prices in INR:

|  ID | Product                | Price in source |
| --: | ---------------------- | --------------: |
| `0` | Sandwash Linen Shirt   |          ₹2,490 |
| `1` | Wide-Leg Linen Trouser |          ₹2,890 |
| `2` | Cotton Poplin Dress    |          ₹3,290 |
| `3` | Ribbed Knit Tee        |          ₹1,290 |
| `4` | Overdyed Chino         |          ₹2,690 |
| `5` | Linen Blend Blazer     |          ₹4,990 |

The same identity and price data also appear in the home-page cards. A browser visitor can edit `localStorage`, product objects, quantities, and totals. These values are display/cart inputs only, not an order authority. A production backend must accept product IDs and quantities, look up price and availability itself, and return the calculated order total.

The cart is stored under the exact localStorage key `cart`. Each line is a copied product object plus `qty`, therefore the practical line model is `{ id, name, price, blurb, image, qty }`. `render()` calculates item count and subtotal, populates all `[data-cart-items]` and `[data-cart-total]` elements, and writes line controls. `add()` uses a numeric product ID, increments an existing line or appends a copied product, then saves and opens the drawer. `data-inc` and `data-dec` adjust quantity; a quantity below one removes the line.

### Pages and browser flow

- `index.html` renders the hero, featured product, six cards, cart button, drawer, and checkout link. Product links use `product.html?id=0` through `product.html?id=5`.
- `product.html` is a reusable shell. `assets/app.js` reads `?id=`, selects the corresponding catalogue entry, then changes the name, blurb, price, image, breadcrumb, document title, and add-to-cart ID. It also has a quantity selector.
- `checkout.html` collects `firstname`, `email`, `phone`, `address`, and `pincode`. Its payment radio values are `upi`, `card`, `netbanking`, and `wallet`; the current `payu.js` does not use the selected payment value in its payload. The page shows the cart and a client-calculated total.
- `success.html` is a static page. It says the order is confirmed and advises server-side `verify_payment` before shipping, but it does not itself inspect a verified order state.

The HTML references Google Fonts at `fonts.googleapis.com` and `fonts.gstatic.com`. This is an asset/deployment consideration: production can self-host or approve the dependency, and should account for privacy, CSP, availability, and offline behavior. It is not a PayU documentation fact.

### Exact browser PayU path

**Observed source fact from&#x20;**`assets/payu.js`**:**

1. Read `cart` from `localStorage`.
2. Calculate `amount` as the sum of each line’s `qty * price`, formatted to two decimal places.
3. Create a timestamp transaction ID using the browser clock.
4. Build a payload containing the placeholder merchant key, transaction ID, amount, product description, `firstname`, `email`, `phone`, and `surl`/`furl`.
5. POST the payload as JSON to the configured `hashEndpoint`.
6. Expect a JSON object containing `hashes`, then use `hashes.payment`.
7. Create a hidden HTML form and POST the payload plus `hash` to the configured PayU test payment action.
8. Let PayU redirect to the configured success or failure URL.

The browser path does not include a durable order creation step, server ownership of the cart amount, authenticated customer/order binding, response-hash validation, webhook, or idempotent fulfilment. Treat `success.html`, its redirect, and any browser callback as presentation only.

## Trace the iOS integration

### Dependency and environment observations

**Observed source fact:** `ios/Podfile` selects `platform :ios, '13.0'`, enables frameworks, and declares the CocoaPods pod `PayUIndia-CheckoutPro`. Its post-install hook also forces the Pods deployment target to iOS 13.0.

**Observed source fact:** `ios/README.md` presents Swift Package Manager as an alternative at `https://github.com/payu-intrepos/iOS-SDK-Checkout-Pro` and names modules `PayUCheckoutProKit`, `PayUParamsKit`, `PayUNetworkingKit`, and `PayUCustomBrowser`.

**PayU documentation fact:** the retrieved main iOS Checkout Pro page says the SDK is compatible with iOS 11 or higher. The archive chooses iOS 13. This is not necessarily an error: iOS 13 can be a project policy, while the page states a lower SDK compatibility floor. Confirm the current SDK release’s actual minimum and module packaging before choosing a deployment target.

### Configuration

`PayUConfig.swift` defines an environment enum with `.test` and `.production`. It contains a placeholder merchant key, an HTTPS placeholder hash endpoint, placeholder success and failure URLs, and defaults to `.test`. The file explicitly warns that the salt must never be in the app. Replace these values through build configuration or secure deployment configuration, never by committing secrets.

The source uses `surl` and `furl` as strings. Confirm the current iOS SDK’s redirect contract and ensure both URLs belong to the merchant-owned HTTPS backend or a verified app flow that can safely hand off to it.

### Hash service

**Observed source fact:** `PayUHashService.Request` is `Encodable` and contains `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `udf1`, and `hashStrings: [String: String]`. `fetchHashes` encodes the request as JSON, sends an asynchronous `POST` through `URLSession.shared` to `PayUConfig.hashEndpoint`, requires a 2xx response, and decodes `{ "hashes": { ... } }` into `[String: String]`.

The service has useful separation of concerns, but it has no request schema validation, auth, explicit timeout, retry policy, cancellation ownership, response-size limit, or per-hash format validation. It also does not prove that returned names correspond to the SDK request. Those are production requirements.

### Checkout manager

**Observed source fact:** `PayUCheckoutManager.Order` has `amount: Decimal`, `productInfo`, `firstName`, `email`, `phone`, and `transactionId`. `start` constructs `PayUPaymentParam` with those values plus the configured merchant key and `surl`/`furl`, maps the local environment to `.test` or `.production`, constructs a `userCredential` from the merchant key and customer email, and enables saved cards.

The manager sets a primary colour, merchant name, exit confirmation, OTP auto-selection, and saved-card setting on `PayUCheckoutProConfig`, then calls `PayUCheckoutPro.open` with the presenting view controller and itself as delegate.

**Compile-time verification item:** the imported modules, initialiser labels, environment enum values, config properties, `PayUCheckoutProDelegate` signatures, `PayUHashes` properties, completion type, and `open` call must be checked against the installed SDK artifact and current official documentation. The archive does not include that artifact, so this tutorial does not claim these snippets compile.

When the SDK calls `generateHash`, the source converts String-valued entries from the SDK dictionary into `raw` and forwards them as `hashStrings`. It then maps returned names into `PayUHashes`, including a payment-related mobile SDK hash, payment, VAS, saved-card, offer-status, and checkout-detail fields. The fallback mapping and empty-string defaults are risky until the exact SDK contract is confirmed. Do not silently return an empty hash for a required field.

### Checkout view controller

`CheckoutViewController` is a minimal screen with a fixed demonstration total of ₹1,499. It constructs a fixed demonstration order description and redacted demo customer data, and makes a timestamp-based transaction ID. These are demonstrations, not a cart or server-created order. On a success result it immediately pushes `OrderConfirmedViewController`; on failure it shows an alert. The success path must be changed to await server confirmation before displaying a paid/fulfilled state.

## Build the integration

Build from the server outward. A safe production flow is:

1. The storefront or app sends only product IDs, quantities, and validated customer/delivery inputs to the merchant backend.
2. The backend authenticates the caller, resolves products and prices, creates a pending order, assigns a unique transaction ID, and returns an order snapshot.
3. The app creates `PayUPaymentParam` from that server snapshot. It never selects the amount from `localStorage` or a UI label.
4. When the SDK requests a hash, the app forwards the SDK-provided request fields to the authenticated merchant hash endpoint over HTTPS.
5. The backend signs with the server-only salt and returns only the mapped hashes needed by the SDK.
6. The SDK handles payment UI and invokes the delegate. The delegate result is provisional.
7. The backend verifies the transaction through the applicable PayU verification/webhook/reconciliation path, validates response integrity and amount/order identity, and performs an idempotent state transition.
8. The app polls or fetches the backend order status and presents a confirmation based on that server state.

### Illustrative server-created order

```js
// Illustrative shape only. Product lookup, auth, validation, storage, and tax/shipping rules are omitted.
app.post('/api/orders', requireAuthenticatedCustomer, async (req, res) => {
  const items = validateProductIdsAndQuantities(req.body.items);
  const catalogue = await catalogueService.getAvailableById(items.map(i => i.productId));
  const priced = priceFromCatalogue(items, catalogue); // never trust client price/name
  const order = await orders.createPending({
    customerId: req.user.id,
    lines: priced.lines,
    amount: priced.total,
    transactionId: await ids.uniqueTransactionId(),
  });
  res.status(201).json({
    orderId: order.id,
    transactionId: order.transactionId,
    amount: order.amount,
    currency: 'INR',
    lines: order.lines,
  });
});
```

### Illustrative authenticated hash endpoint

The endpoint should accept the SDK’s `hashName`, `hashString`, `hashType`, and any other fields required by the applicable PayU iOS hash documentation. It should authenticate the app/session, validate that the request matches a pending server order, and return only the approved mapping. It must not reconstruct or normalise SDK hash strings unless the applicable PayU contract explicitly requires that operation. Algorithm differences, post-salt rules, and special hashes must follow the applicable PayU iOS documentation, not an assumption based on the generic payment formula.

```js
app.post('/api/payu/hashes', requireAppAuth, async (req, res) => {
  const request = validatePayUHashRequest(req.body); // names, types, order, and pending order binding
  const order = await orders.authorisePaymentAttempt(request.transactionId, req.user.id);
  const hashes = await payuSigner.signRequestedHashes({
    request,
    order,
    salt: secretStore.payuSalt,
  });
  res.json({ hashes: allowListedHashNames(hashes) });
});
```

This is illustrative. The source’s `server/payu-hashes.js` currently signs the payment hash from its own fixed field sequence and then applies `SHA-512(hashString + salt)` to every supplied pair. That implementation must be compared with the applicable current PayU iOS hash pages before reuse.

### What the supplied backend actually implements

**Observed source fact:** `server/payu-hashes.js` reads `PAYU_MERCHANT_KEY` and `PAYU_MERCHANT_SALT` from process environment variables. It defines a SHA-512 helper, exposes `POST /payu/hashes`, constructs `hashes.payment` from a fixed sequence of key, transaction ID, amount, product info, first name, email, one user-defined field, empty placeholders, and salt, then loops over the SDK-supplied `hashStrings` object and returns `{ hashes }`. It does not authenticate callers, validate that fields belong to a stored order, allow-list hash names, or persist an order.

The same file exposes `POST /payu/verify`. It reads `txnid`, constructs a `verify_payment` command hash from the key, command, transaction ID, and salt, posts `key`, `command`, `var1`, and `hash` to the hard-coded test PayU `postservice.php?form=2` endpoint, and returns the parsed PayU response. The source does not implement persistence, authentication, rate limiting, robust request/response validation, production environment switching, webhook handling, idempotency, or a safe fulfilment workflow. Treat it as a demonstration server, not a deployable production service.

The source also has no explicit order creation route or relationship between `/payu/hashes` and `/payu/verify`. A production implementation must establish that relationship and must not allow an arbitrary caller to ask the server to sign arbitrary amount, customer, or transaction fields.

### Illustrative Swift service shape

```swift
// Illustrative pseudocode. Confirm SDK field names and response contract first.
struct HashRequest: Encodable {
    let orderID: String
    let sdkHashRequests: [SDKHashRequest]
}

func fetchHashes(_ body: HashRequest,
                 session: URLSession,
                 bearerToken: String,
                 taskStore: TaskStore) async throws -> [String: String] {
    var request = URLRequest(url: merchantHTTPSHashURL)
    request.httpMethod = "POST"
    request.timeoutInterval = 15
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")
    request.setValue("Bearer \(bearerToken)", forHTTPHeaderField: "Authorization")
    request.httpBody = try JSONEncoder().encode(body)

    let task = Task { try await session.data(for: request) }
    taskStore.replaceHashTask(task)
    defer { taskStore.clearHashTask(task) }
    let (data, response) = try await task.value
    try validateHTTPS2xxAndJSONSize(response, data)
    let result = try JSONDecoder().decode(HashResponse.self, from: data)
    try validateRequiredHashNamesAndFormats(result.hashes)
    return result.hashes
}
```

Own and cancel the task when the checkout attempt or screen ends. Avoid logging request bodies, names, email addresses, phone numbers, or hash material.

### Illustrative strict payment setup

```swift
// Illustrative: amount and transaction ID come from the server-created pending order.
let param = PayUPaymentParam(
    key: merchantKeyFromBuildConfiguration,
    transactionId: pendingOrder.transactionId,
    amount: pendingOrder.amountString,
    productInfo: pendingOrder.displayDescription,
    firstName: customer.firstName,
    email: customer.email,
    phone: customer.phone,
    surl: merchantSURL,
    furl: merchantFURL
)
param.environment = selectedPayUEnvironment
// Set userCredential and saved-card options only after consent and SDK confirmation.
```

The server must guarantee transaction-ID uniqueness and bind the amount, customer, and order ID. Do not use a timestamp alone as the uniqueness mechanism.

## Generate and verify hashes

The security model is straightforward even where the exact SDK contract is not: the SDK can request hashes, but the merchant server signs them. The salt never belongs in the app, browser, source repository, logs, or client response.

### Dynamic and static distinction

- **Dynamic/request hash:** derived from transaction-specific values such as merchant key, transaction ID, amount, product information, customer fields, user-defined fields, and salt according to the applicable PayU payment contract. The amount and order identity must come from the server-created order.
- **SDK-requested dynamic hash:** the SDK supplies a hash name and string (and possibly type or related metadata). The app forwards it; the merchant server applies precisely the algorithm and suffix/prefix rules documented for that named hash.
- **Static/configuration hash or value:** a value that does not change per payment, if a specific PayU feature requires one. Never infer support for static hashes from this archive alone. Confirm the relevant PayU page and SDK release.

A symbolic/redacted request-payment formula, only where the applicable PayU contract supports it, is:

```text
SHA-512(<merchant-key>|<transaction-id>|<amount>|<product-info>|<first-name>|<email>|<udf fields>|<salt>)
```

The exact number and ordering of empty fields, optional fields, hash name, and any post-salt or special algorithm are contract-sensitive. Do not copy this as a universal formula. The archive’s Node code uses a fixed sequence with empty placeholders followed by the salt for `payment`; that is an **observed implementation**, not proof that it is the correct formula for every iOS SDK hash.

For a supplied SDK hash string, the archive currently uses a symbolic form equivalent to:

```text
SHA-512(<SDK-supplied hash string> + <server-only salt>)
```

Again, this is what the archive implements for each `hashStrings` pair. The exact operation must be checked against the linked iOS hash documentation, especially for hash name, post-salt, hash type, special algorithms, and completion mapping. The retrieved main iOS page did not expose those details.

### Verification items before implementation

- Identify the installed SDK version and its exact dynamic-hash request/response contract.
- Confirm whether the SDK expects `payment`, `payment_related_details_for_mobile_sdk`, or another name for each callback.
- Confirm hash type, post-salt, special hashes, empty-field semantics, and whether hash strings must be returned without transformation.
- Confirm the exact iOS completion type and what happens when hash generation fails. The archive catches an error and invokes `onResult`, but it does not necessarily call the SDK’s `onCompletion` with a failure signal.
- Add golden test vectors in a secure test suite without publishing merchant secrets.

## Handle responses and fulfilment

The archive supplies these delegate signatures: success with `response` and `extraMessage`, failure with the same shape, cancel with `isTxnInitiated`, and `onError(_:)`. Its current behavior is:

- `onPaymentSuccess` reports `.success` to the view controller.
- `onPaymentFailure` reports a generic failure error.
- `onPaymentCancel` reports a generic cancellation error.
- `onError` reports the SDK error or a generic error.
- `CheckoutViewController` navigates to order confirmation immediately on `.success`.

The supplied success callback is not authoritative. Change it to record the callback as a pending signal, send the transaction/order identity to the merchant backend, and wait for server confirmation. The server should validate response integrity, amount, currency, transaction ID, merchant account, and expected order state; use PayU Verify Payment and/or configured webhooks and reconciliation as the authoritative payment evidence. Update order state idempotently, for example `pending -> payment_verified -> fulfilment_queued -> fulfilled`, with explicit failure/refund/manual-review states.

Never fulfil based only on `success.html`, a client callback, a UI result, or an unverified redirect. Handle duplicate callbacks, delayed callbacks, app termination, retries, and out-of-order webhook/verify responses.

## Configuration and privacy

- **Deployment target:** PayU’s retrieved main page says iOS 11 or higher; the archive forces iOS 13 in `Podfile`. Verify the SDK release and choose a deliberate project minimum.
- **Dependency choice:** CocoaPods and SPM are both described in the archive. Treat them as alternatives, not simultaneous dependencies. Follow the official current installation instructions and confirm module names and versions.
- **UPI app discovery:** the archive README suggests `LSApplicationQueriesSchemes` entries for UPI apps and says UPI intent apps appear only on a real device. These are archive observations, not proof that every listed scheme is required by PayU. Confirm the current SDK’s documented list and Apple policy; include only schemes the app actually needs.
- **ATS:** the README shows `NSAllowsArbitraryLoads=true`. Do not copy this broad exception. Use HTTPS and default App Transport Security; if a narrow exception is genuinely required, document and scope it to the specific domain and confirm with security review.
- **Privacy manifest:** the retrieved page links to “Update Apple Privacy manifest files”, but that linked page was not separately fetched. Confirm current Apple and PayU privacy-manifest requirements, SDK declarations, and App Store submission requirements before release.
- **Lifecycle and links:** the archive has no Info.plist, URL schemes, entitlements, scene lifecycle, Universal Links/deep links, or `openURL`/UPI callback implementation. Add and test the required app lifecycle and callback wiring rather than assuming the starter has it.
- **Data handling:** customer name, email, phone, address, and PIN code are collected. Minimise retention, encrypt at rest and in transit, redact logs, define retention/deletion, and document consent and notices. Confirm whether saved-card use and `userCredential` are appropriate for the consent model.

## UPI and lifecycle

UPI intent is a device/lifecycle concern, not just a payment radio button. The archive’s browser radio selection is not wired into the browser PayU payload, while the iOS README mentions UPI schemes but supplies no native app lifecycle implementation. Confirm the Checkout Pro SDK’s current UPI handoff and return contract, then test on supported real devices with installed UPI apps. Do not infer UPI behavior from simulator results.

Own the checkout attempt in a coordinator or view-model that outlives transient view presentation as needed. Cancel the hash task when the attempt is abandoned, prevent callbacks after deallocation, and make repeated taps safe. The archive creates an unlabelled `Task` inside `generateHash`; a callback can therefore arrive after the screen or order context has changed. Store the task, associate it with an attempt ID, and discard stale results.

## Test

### Static and compile checks

- Confirm every required archive path and check that no credential, test card, phone, email, salt, or real merchant key is copied into source control or documentation.
- Verify Markdown links, code fences, JSON field names, endpoint routes, and the server/client hash response shape.
- Create a real Xcode host project, install exactly one dependency method, and compile against the selected SDK. Resolve all imports, initialisers, delegate signatures, config properties, and privacy-manifest warnings.
- Test order pricing with modified browser storage and altered request fields; the server must reject or ignore client prices.

### Backend and payment-contract tests

- Authenticate the hash request and bind it to a pending server order.
- Test valid and invalid hash names, hash strings, hash types, missing fields, extra fields, wrong order IDs, wrong amounts, and malformed response schemas.
- Test dynamic payment hashes and every SDK-requested hash required by the installed version against secure golden vectors.
- Test callback success, failure, cancel, error, duplicate callback, delayed callback, malformed response, mismatched amount, and mismatched transaction ID.
- Test PayU Verify Payment and configured webhooks, including timeouts, retries, duplicate delivery, signature/response validation, and reconciliation against the internal ledger.
- Test idempotent fulfilment and safe recovery after app termination, backend outage, or network loss. A verified payment should not produce two fulfilments.

### Device and release tests

- Test supported real devices for UPI app discovery, handoff, return, cold start, backgrounding, killed-app recovery, deep links/Universal Links, and `openURL` handling. Do not assume simulator behavior is representative.
- Test ATS, callback URLs, privacy manifests, entitlements, and production build configuration.
- Use only PayU test facts explicitly present in the retrieved documentation. The retrieved main page describes payment methods and compatibility, but did not provide detailed card or UPI test values. Do not reuse or publish the archive’s test credentials or payment values.

## Go live

Before switching from test to production:

1. Create a production server configuration with production merchant credentials in secret storage; never place the salt in the app.
2. Replace the test PayU action and test verification endpoint with the current production endpoints confirmed from PayU documentation and merchant configuration.
3. Replace placeholder hash, SURL, FURL, webhook, and order-status URLs with merchant-owned HTTPS endpoints.
4. Remove test metadata, demonstration amounts, demonstration customer data, and test legal copy.
5. Resolve catalogue, tax, shipping, refund, inventory, and fulfilment rules on the server.
6. Confirm the installed SDK version, deployment target, dependency modules, entitlements, Info.plist, UPI schemes, callback handling, privacy manifests, and App Store requirements.
7. Run a controlled production smoke test with monitoring and reconciliation, then verify that the customer-facing confirmation is driven by server order state.
8. Ensure `robots.txt`, `sitemap.xml`, and static deployment do not expose checkout implementation details or imply that a static success page is payment proof. The example sitemap includes a placeholder domain and omits product query variants; update it only as appropriate for the merchant’s real site.

## Troubleshooting

| Symptom                                       | Likely source-level cause                                                                | Investigation/remediation                                                                                                     |
| --------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Hash callback never completes                 | Hash service error path calls `onResult` but may not call the SDK completion             | Confirm the SDK failure contract; always complete or explicitly fail the SDK request; add timeout/cancellation handling       |
| Hash rejected by PayU                         | Wrong hash name, sequence, post-salt, type, or SDK version                               | Compare the installed artifact with the applicable official iOS hash page; use a redacted golden vector                       |
| Payment amount is wrong                       | Browser `localStorage`, UI total, or iOS demo amount is trusted                          | Create and bind the order on the server; send only the server amount to Checkout Pro                                          |
| Saved cards behave unexpectedly               | `userCredential` is built from merchant key and email and saved cards are enabled        | Obtain consent, confirm the SDK contract, and use the documented customer identifier; do not assume this construction is safe |
| UPI apps do not appear                        | Simulator, missing schemes, lifecycle wiring, or unsupported device path                 | Test on real devices, confirm current SDK/Apple requirements, and implement verified return handling                          |
| App fails to compile                          | Missing Xcode host project or SDK/module/API drift                                       | Add a host project, install one supported dependency path, and compile against the exact selected SDK                         |
| Customer sees “confirmed” but order is unpaid | Immediate UI navigation and static `success.html`                                        | Gate confirmation and fulfilment on server verification and idempotent order state                                            |
| Verification route fails                      | Archive hardcodes the test verification URL and has no robust validation                 | Configure by environment, validate transaction ownership, add timeout/retry/circuit-breaker policy, and reconcile             |
| Callback arrives after screen closes          | Unowned `Task` and closure state                                                         | Store/cancel tasks, use weak ownership, and discard stale attempt IDs                                                         |
| Static site is incomplete in production       | Placeholder URLs, external fonts, missing privacy/legal pages, and static-only callbacks | Use merchant-owned HTTPS services, self-host or approve assets, add backend-driven order status, CSP, and legal review        |

## Security and remediation

| Severity | Risk observed in archive                                                                                                                               | Remediation                                                                                                      |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| Critical | Client controls cart amount, product data, and customer fields                                                                                         | Server-create the order from product IDs; validate identity, price, availability, amount, and delivery data      |
| Critical | Server signs client-supplied fields and creates no persistent order                                                                                    | Authenticate the hash call, bind it to a pending order, and persist an order/payment-attempt record              |
| High     | Test environment, placeholder backend URLs, test endpoint, and test legal/demo copy                                                                    | Separate environment configuration, replace all endpoints and copy before release, and add deployment assertions |
| High     | Timestamp transaction IDs and no server uniqueness/idempotency                                                                                         | Generate collision-resistant server IDs and enforce unique constraints per payment attempt                       |
| High     | Potentially unsafe `userCredential` construction and saved-card setting                                                                                | Obtain consent, confirm SDK semantics, use the supported customer identifier, and default off until reviewed     |
| High     | SDK dependency/module/API contracts are incomplete or uncertain                                                                                        | Pin and audit the SDK, compile in a host project, and test the exact delegate/hash contracts                     |
| High     | No native project files, Info.plist, privacy manifests, URL schemes, entitlements, app lifecycle, Universal Links/deep links, or UPI callback handling | Add and security-review the missing native integration; test real-device return paths                            |
| High     | `URLSession.shared` has no auth, timeout policy, retry strategy, response-schema validation, or lifecycle cancellation                                 | Use authenticated HTTPS, bounded timeouts, safe retries, strict schemas, task ownership, and redacted telemetry  |
| High     | Hash failure maps to a result but does not necessarily call PayU completion                                                                            | Implement the SDK-specific failure completion contract and test all error paths                                  |
| High     | No PII-safe observability, webhook, reconciliation, or fulfilment state machine                                                                        | Add structured redacted events, durable payment states, webhook/verify jobs, and idempotent fulfilment           |
| Medium   | External Google Fonts/CDN dependencies                                                                                                                 | Self-host or approve with CSP/privacy/availability review                                                        |
| Medium   | Static HTML has limited order state and success redirects                                                                                              | Make success/failure pages read a server status, and never treat a static page as proof of payment               |
| Medium   | Browser payment radio is not included in `payu.js` payload                                                                                             | Either remove the misleading control or implement and verify the supported payment-method contract               |

## Sources

### Retrieved official source

- [PayU: iOS Checkout Pro SDK](https://docs.payu.in/docs/ios-checkoutpro-sdk) — retrieved for this review. The visible page describes Checkout Pro, supported payment categories, customization, and a minimum iOS version of iOS 11 or higher. Its detailed integration and hash sections are linked but were not exposed in the retrieved page content used here; this tutorial does not attribute unreviewed details to that page.

### Analysed archive inputs

- `tmp/marigold_studio_storefront.zip`, extracted to `tmp/marigold_inspect/`
- `marigold-studio/index.html`
- `marigold-studio/product.html`
- `marigold-studio/checkout.html`
- `marigold-studio/success.html`
- `marigold-studio/assets/app.js`
- `marigold-studio/assets/payu.js`
- `marigold-studio/assets/styles.css`
- `marigold-studio/assets/logo.svg`, `product-1.svg` through `product-6.svg`, `hero-apparel.jpg`
- `marigold-studio/ios/Podfile`
- `marigold-studio/ios/PayUConfig.swift`
- `marigold-studio/ios/PayUHashService.swift`
- `marigold-studio/ios/PayUCheckoutManager.swift`
- `marigold-studio/ios/CheckoutViewController.swift`
- `marigold-studio/ios/README.md`
- `marigold-studio/server/payu-hashes.js`
- `marigold-studio/robots.txt` and `marigold-studio/sitemap.xml`

### Further PayU pages to confirm

The main page identified these topics/pages, but they were **not independently reviewed** for this tutorial: iOS Checkout Pro **Integration Steps**, **Generate Dynamic Hash**, **Advanced Integration**, **Handling Redirect (surl/furl) URLs with iOS**, **Update Apple Privacy manifest files**, and the current installation/dependency instructions. Confirm their current URLs and content from the main page before implementation.
