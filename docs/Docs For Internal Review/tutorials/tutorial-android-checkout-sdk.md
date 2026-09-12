---
title: 'Tutorial: Android Checkout SDK'
deprecated: false
hidden: true
metadata:
  robots: index
---
# StoreForge Android Checkout Pro tutorial: from generated Nova Store to a production-safe payment flow

## Outcome and scope

This tutorial maps the complete StoreForge generator-to-export-to-Android flow for the supplied package. It explains how the builder chooses a store configuration, emits a Nova Store storefront, copies the web files into an Android asset tree, and hands checkout from a WebView to PayU Checkout Pro. It also identifies the changes required before using the design in a production payment system.

**Review boundary.** The archive was inspected as source. This is a static source review only. The Android project was not built, installed, or tested, and no payment was run. Statements marked **Observed** describe files in the supplied archive. Statements marked **PayU documentation** describe the retrieved PayU documentation. Statements marked **Recommendation** are production guidance, not claims about the package.

The archive contains sandbox values in source and documentation. They are deliberately not reproduced here. Refer to them as **redacted sandbox values**, and replace all placeholders through secure merchant configuration. Never put a merchant salt or other signing secret in a browser bundle or APK.

## Prerequisites

- The complete archive and its extracted review tree: `tmp/storeforge_payu_full_package.zip` and `tmp/storeforge_inspect/`.
- Android Studio and a JDK suitable for the generated Android Gradle Plugin and Java 17 settings, when you later perform your own build.
- A PayU merchant account and the Checkout Pro SDK artifact versions approved for the project. Keep test and production credentials separate.
- A merchant-owned HTTPS server for order creation, hash generation, callbacks, webhooks, and payment reconciliation. The server is a backend dependency; it is not a public static hosting recommendation.
- Familiarity with HTML, browser `localStorage`, JavaScript, Kotlin, Gradle, and JSON.
- Before implementation, read the five PayU URLs in [Sources](#sources), then confirm the API and SDK contracts against the installed artifact. The supplied package and the retrieved documentation are not identical in every detail.

## Understand the complete package

### Package map

The archive has two top-level areas:

```text
storefront-and-android/
  index.html, product.html, cart.html, checkout.html
  payment-success.html, payment-failure.html
  css/styles.css
  js/store.js
  js/payu-checkout.js
  images/*.svg
  README.md
  PAYU-SETUP.md
  android/
    settings.gradle.kts
    build.gradle.kts
    gradle.properties
    README.md
    HASH-ENDPOINT.md
    app/build.gradle.kts
    app/src/main/AndroidManifest.xml
    app/src/main/java/in/novastore/shop/MainActivity.kt
    app/src/main/java/in/novastore/shop/PayUCheckout.kt
    app/src/main/java/in/novastore/shop/PayUHashService.kt
    app/src/main/assets/index.html
    app/src/main/assets/product.html
    app/src/main/assets/cart.html
    app/src/main/assets/checkout.html
    app/src/main/assets/payment-success.html
    app/src/main/assets/payment-failure.html
    app/src/main/assets/css/styles.css
    app/src/main/assets/js/store.js
    app/src/main/assets/js/payu-checkout.js
    app/src/main/assets/images/*.svg
    app/src/main/assets/bridge.js

builder-platform/
  package.json
  src/routes/index.tsx
  src/routes/payu-checkout.tsx
  src/routes/api/public/payu/hash.ts
  src/lib/builder-data.ts
  src/lib/site-generator.ts
  src/lib/android-generator.ts
  src/lib/download-bundle.ts
  src/components/ui/*
  src/hooks/use-mobile.tsx
  src/router.tsx, src/routeTree.gen.ts, src/routes/__root.tsx
  src/server.ts, src/start.ts, src/styles.css, vite.config.ts, tsconfig.json
```

**Observed roles.** `storefront-and-android/` is a concrete generated sample: static storefront files, SVG artwork, `README.md`, and `PAYU-SETUP.md`; its nested `android/` tree is an Android project and bundled asset copy. `builder-platform/` is the generator application. Its UI and configuration files select category, layout, brand, currency, support address, and whether Android is included. The four generator modules are the important implementation seam:

- `builder-data.ts` defines `Category`, `Product`, `Layout`, `Palette`, `StoreConfig`, the six categories, five layouts, five palettes, and the default configuration.

For avoidance of doubt, the exact builder source paths are `builder-platform/src/routes/index.tsx`, `builder-platform/src/routes/payu-checkout.tsx`, `builder-platform/src/routes/api/public/payu/hash.ts`, `builder-platform/src/lib/site-generator.ts`, `builder-platform/src/lib/android-generator.ts`, and `builder-platform/src/lib/download-bundle.ts`. The surrounding UI/configuration includes `builder-platform/src/components/ui/*`, `builder-platform/src/hooks/use-mobile.tsx`, `builder-platform/src/router.tsx`, `builder-platform/src/routes/__root.tsx`, `builder-platform/src/styles.css`, `builder-platform/src/server.ts`, `builder-platform/src/start.ts`, `builder-platform/package.json`, `builder-platform/tsconfig.json`, and `builder-platform/vite.config.ts`. The exact sample Android Kotlin paths are `storefront-and-android/android/app/src/main/java/in/novastore/shop/MainActivity.kt`, `storefront-and-android/android/app/src/main/java/in/novastore/shop/PayUCheckout.kt`, and `storefront-and-android/android/app/src/main/java/in/novastore/shop/PayUHashService.kt`; the sample Android module is `storefront-and-android/android/app/build.gradle.kts` and its manifest is `storefront-and-android/android/app/src/main/AndroidManifest.xml`.
- `builder-platform/src/lib/site-generator.ts` creates HTML, CSS, JavaScript, SVG, README, setup notes, and `robots.txt`.
- `builder-platform/src/lib/android-generator.ts` creates the Gradle files, manifest, Kotlin classes, bridge, and Android setup notes.
- `builder-platform/src/lib/download-bundle.ts` combines both outputs and creates a ZIP in the browser with JSZip.

### Builder workflow

1. `builder-platform/src/routes/index.tsx` keeps a `StoreConfig` in React state. The wizard steps are Category, Layout, Brand, and Export. The UI changes `categoryId`, `layoutId`, `paletteId`, `storeName`, `tagline`, `supportEmail`, `currency`, and `includeAndroid`.
2. The selected category supplies the hero copy, collection labels, and six products. The selected layout changes the home-page composition. The palette supplies CSS and SVG colours.
3. `buildFileList(config)` calls `generateSite(config)`. If `includeAndroid` is false, it returns only the site. Otherwise it calls `generateAndroid(config)` and then copies every generated site file except Markdown and `robots.txt` into `android/app/src/main/assets/`.
4. `downloadBundle(config)` makes a folder named from the store name, with a `-website` suffix, places every generated file below that folder, compresses it with JSZip, and starts a browser download. It does not build the Android project.
5. Generated values are interpolated into page titles, descriptions, logo SVG text, collection links, product cards, product catalog JavaScript, the package/application ID, Android label, Kotlin package, `CP_UDF2`, and README/setup content. `site-generator.ts` removes markup-significant characters from store name, tagline, and support email before interpolation. The Android generator uses the trimmed store name for package derivation and does not apply the same clean function, so production code should validate configuration consistently before generating.

For the inspected default-like Nova Store output, the generated paths are exactly the paths shown above. In particular, the Android assets are a second copy of the web output at `storefront-and-android/android/app/src/main/assets/`. The copy excludes `README.md`, `PAYU-SETUP.md`, and `robots.txt`. `bridge.js` is added to the Android asset tree but the generated checkout page does not load it as a script; the direct `typeof AndroidBridge` branch in `js/payu-checkout.js` is what performs the handoff.

### Source/documentation conflicts to resolve before implementation

These conflicts are material:

1. **SDK versions.** The package declares Checkout Pro `2.6.0`, UPI add-on `1.7.4`, custom-browser add-on `8.4.1`, AGP `8.5.2`, Kotlin `1.9.24`, Java/Kotlin target 17, compile/target SDK 34, and min SDK 24. The retrieved integration page shows Checkout Pro `3.3.7`, Java 8 source/target examples, minimum SDK 21, compile SDK 31 or later, and documentation metadata mentioning Kotlin 1.6.10. These are not interchangeable claims. Confirm the coordinates, transitive dependencies, listener signatures, constants, and supported Android levels against the exact artifacts selected for the build.
2. **Hash contract.** The generated Android endpoint sends `{ "hashString": "..." }` and expects `{ "hash": "..." }`. The builder API route also accepts only `hashString` and returns only `hash`. PayU documentation additionally documents `CP_HASH_NAME`, `CP_HASH_STRING`, optional `CP_POST_SALT`, a hash type for V2, and operation-specific handling. The simple route is therefore not a demonstrated full Checkout Pro hash service.
3. **SURL/FURL.** The package uses static web pages for browser `surl` and `furl`, but uses PayU-hosted sample callback URLs in the Android params. PayU documentation says those sample Android URLs are for testing and recommends merchant-owned URLs for live use.
4. **Responses.** The package wraps the SDK callback object as `Any?` and only chooses a success/failure page. PayU documentation shows response extraction using `CP_PAYU_RESPONSE` and `CP_MERCHANT_RESPONSE`, and notes a different response situation for UPI intent/in-app. Confirm the response model for the installed SDK before parsing or fulfilling an order.
5. **UPI test behavior.** The package README says to use a device or emulator with Play Services and presents UPI as available through Checkout Pro. The retrieved documentation says UPI in-app and UPI intent are not available in test mode. Treat the documentation statement as the test-planning constraint and verify current PayU guidance.

## End-to-end architecture and sequence

The following diagram separates observed package behavior from the production order decision. The `success/failure` assets are presentation only; the merchant server remains authoritative.

```mermaid
sequenceDiagram
    participant B as StoreForge builder
    participant Z as Exported web files + Android assets
    participant W as Browser or Android WebView
    participant J as payu-checkout.js / JS bridge
    participant A as MainActivity + CheckoutPro SDK
    participant H as Merchant HTTPS hash/order server
    participant P as PayU
    participant R as Callback/webhook/Verify Payment
    participant O as Order and fulfilment system

    B->>Z: Generate StoreConfig, storefront, Android project
    B->>Z: Copy site files to android/app/src/main/assets and ZIP
    W->>J: Customer visits home -> product -> cart -> checkout
    J->>J: Read localStorage and build displayed order
    alt Android WebView branch
        J->>A: AndroidBridge.pay(JSON)
        A->>H: Request each SDK hash (exact string + name/type)
        H-->>A: Hash only; salt stays on server
        A->>P: PayUCheckoutPro.open(params, listener)
        P-->>A: SDK success/failure/cancel/error callback
        A-->>W: Load success/failure asset or pending UI
    else Browser-only branch
        J->>H: POST /api/payu/hash with web checkout data
        H-->>J: key/txnid/hash under the web contract
        J->>P: POST hidden form to PayU payment endpoint
        P-->>W: SURL/FURL browser return
    end
    P-->>R: Callback/webhook or status available
    R->>H: Verify authenticity, reverse hash/signature, amount, txnid
    H->>O: Idempotently mark paid/pending/failed
    O-->>H: Fulfil only after verified paid state
```

## Trace the generated storefront

### Home, product, cart, and checkout pages

The six Apparel & Fashion products observed in the generated Nova Store are:

| SKU derived from name | Product | Display price in the supplied output |
| --- | --- | ---: |
| `oversized-cotton-tee` | Oversized cotton tee | INR 1,299 |
| `relaxed-linen-shirt` | Relaxed linen shirt | INR 2,499 |
| `high-rise-straight-jeans` | High-rise straight jeans | INR 3,199 |
| `knit-summer-dress` | Knit summer dress | INR 2,899 |
| `canvas-sneakers` | Canvas sneakers | INR 2,199 |
| `quilted-tote-bag` | Quilted tote bag | INR 1,899 |

These are generated demo catalog values, not authoritative prices. The browser can alter them. A real order must be priced from server-side SKU records.

- `index.html` renders the announcement bar, sticky navigation, hero, collection pills, product cards, cart count, trust copy, and footer. Product links use `product.html?sku=<sku>`.
- `product.html` provides a product detail shell. `js/store.js` hydrates it from a generated catalog when `?sku=` is present, updates product name, blurb, price, image, and attaches the Add to cart handler.
- `cart.html` renders the lines generated by `store.js`, quantity inputs, subtotal, shipping, total, and a Checkout link.
- `checkout.html` contains required fields for full name, email, phone, delivery address, and city/PIN. It includes the PayU web script URL `https://jssdk-uat.payu.in/bolt/bolt.min.js`, although the supplied checkout implementation does not call that script directly. It displays a browser-calculated payable amount and says the next screen provides cards, UPI, netbanking, and wallet options.
- `payment-success.html` shows an order-confirmed page and removes the cart key. `payment-failure.html` shows a failure page. Neither page independently proves payment, creates an order, verifies a PayU response, or authorizes fulfilment.

### Browser cart model and shipping calculation

`js/store.js` uses the `localStorage` key `nova-store-cart` in the inspected Nova Store. Each line is a JSON object with this shape:

```json
{
  "sku": "oversized-cotton-tee",
  "name": "Oversized cotton tee",
  "price": 1299,
  "qty": 1
}
```

`Store.add` increments an existing SKU or pushes a new line; `Store.setQty` replaces a quantity and filters quantities at or below zero; `Store.clear` writes an empty array. `Store.totals()` computes:

```text
subtotal = sum(price * qty)
shipping = 0 when subtotal is 0 or subtotal >= 999; otherwise 79
payable = subtotal + shipping
count = sum(qty)
```

The generated non-Nova variant uses `<store-name-slug>-cart` rather than the fixed Nova key. Do not assume the sample key is a stable integration contract. More importantly, all of the line values, quantity, threshold, shipping fee, product name, and displayed total are browser-controlled. They are useful for presentation only.

### PayU web handoff

`js/payu-checkout.js` contains the following observed configuration:

- `TEST_MODE = true`.
- `PAYU_ACTION` is the test payment URL when true and the live payment URL when false.
- `HASH_ENDPOINT = "/api/payu/hash"`, described as a route to implement on the merchant backend.
- `SURL = location.origin + "/payment-success.html"` and `FURL = location.origin + "/payment-failure.html"`.

On submit it rejects an empty cart, checks browser form validity, and creates this request object:

```json
{
  "amount": "<browser total with two decimal places>",
  "productinfo": "Nova Store order",
  "firstname": "<full name>",
  "email": "<email>",
  "phone": "<phone>",
  "udf1": "<address>",
  "udf2": "<city and PIN>"
}
```

If `AndroidBridge.pay` exists, it serializes that object and calls the native bridge. Otherwise it POSTs the object to `HASH_ENDPOINT`, expects JSON shaped like `{ key, txnid, hash }`, creates a hidden HTML form, and submits the order fields plus `key`, `txnid`, `hash`, `surl`, and `furl` to `PAYU_ACTION`.

This is not the same input shape as the Android hash service. The browser route is expected to create or return a transaction ID and key, whereas the Android route signs an SDK-provided `hashString` and returns only `hash`. The builder route at `builder-platform/src/routes/api/public/payu/hash.ts` only implements the latter. As supplied, a browser request containing `amount`, `productinfo`, and customer fields does not match that route's accepted body and cannot be assumed to work.

## Trace the Android integration

### Gradle, repositories, and app configuration

Observed `android/settings.gradle.kts` uses `google()`, `mavenCentral()`, Gradle Plugin Portal for plugins, plus a PayU GitHub Maven repository and JitPack for dependency resolution. The root build file declares AGP `8.5.2` and Kotlin Android `1.9.24`.

Observed `android/app/build.gradle.kts` sets:

- Namespace and application ID derived from the store name, `compileSdk = 34`, `minSdk = 24`, `targetSdk = 34`.
- `versionCode = 1` and `versionName = "1.0"`.
- BuildConfig fields for a PayU key and `HASH_ENDPOINT`. The key in the supplied generated source is a test value and the endpoint is a placeholder. No salt is declared in the APK configuration.
- Java source and target compatibility 17 and Kotlin JVM target 17.
- AndroidX Core KTX, AppCompat, Material, and coroutines dependencies.
- PayU Checkout Pro plus UPI and custom-browser add-on artifacts, at the versions listed in the conflict note above.

The manifest requests `INTERNET` and `ACCESS_NETWORK_STATE`, declares an `upi` VIEW query for app handoff, sets `android:usesCleartextTraffic="false"`, allows backup, supports RTL, uses a Material 3 no-action-bar theme, and declares `MainActivity` exported with a launcher intent filter and orientation/screen-size/keyboard-hidden `configChanges`. It does not declare a network security configuration, deep-link callback intent filter, or strict WebView origin policy.

### WebView and JavaScript bridge

`MainActivity.kt` creates a WebView in `onCreate`, enables JavaScript and DOM storage, installs a default `WebViewClient`, adds `Bridge()` under the name `AndroidBridge`, and loads `file:///android_asset/index.html`. `onBackPressed` navigates WebView history or exits.

`Bridge.pay(orderJson)` parses the JSON with `JSONObject` and uses `optString` defaults. It constructs a `PayUOrder` with amount, product info, first name, email, and phone. Address and city are not passed to the native order object. It then starts `PayUCheckout` on the UI thread. On the result it shows a toast and loads the bundled success or failure HTML; cancellation only shows a toast.

`android/app/src/main/assets/bridge.js` is a helper that sets `window.__PAYU_NATIVE__` and exposes `payWithPayUNative`, but the observed HTML does not include a script tag for it. The actual checkout branch detects the injected object directly. Also, `MainActivity.kt` comments that the app can point to a hosted storefront, but `storeUrl` is fixed to the bundled asset URL. That comment and behavior conflict until a deliberate remote-store design, origin allowlist, and navigation policy are implemented.

### Checkout Pro parameters and callbacks

`PayUCheckout.kt` defines `PayUOrder`, `PaymentResult`, and a thin `PayUCheckout` wrapper. It creates a transaction ID from `"TXN" + System.currentTimeMillis()`, then builds `PayUPaymentParams` with:

- `.setAmount(order.amount)`
- `.setIsProduction(false)`
- `.setProductInfo(order.productInfo)`
- `.setKey(BuildConfig.PAYU_KEY)`
- `.setPhone(order.phone)`
- `.setTransactionId(txnId)`
- `.setFirstName(order.firstName)`
- `.setEmail(order.email)`
- `.setSurl("https://cbjs.payu.in/sdk/success")`
- `.setFurl("https://cbjs.payu.in/sdk/failure")`
- `.setUserCredential(order.userCredentials)`
- `.setAdditionalParams(additionalParams)`
- `.build()`

The additional parameter map puts `CP_UDF1` to `android-app` and `CP_UDF2` to `apparel` in the observed sample. The default user credential is formed from the BuildConfig key and a placeholder email. That is a client-originated identity and must be replaced with a merchant-controlled, documented design if the feature is actually needed.

The package calls `PayUCheckoutPro.open(activity, params, listener)`. Its `PayUCheckoutProListener` implementation:

- Maps `onPaymentSuccess(response: Any)` to `PaymentResult.Success(response)`.
- Maps `onPaymentFailure(response: Any)` to `PaymentResult.Failure(response)`.
- Maps `onPaymentCancel(isTxnInitiated: Boolean)` to `PaymentResult.Cancelled`, discarding the boolean.
- Maps `onError(errorResponse: ErrorResponse)` to a failure containing `errorMessage`.
- Implements `setWebViewProperties` as a no-op.
- Implements `generateHash` by reading `CP_HASH_NAME` and `CP_HASH_STRING`, calling `PayUHashService.fetchHash(hashString)`, and returning a map whose key is the requested hash name.

The last item follows the documented dynamic callback shape, but it does not handle `CP_POST_SALT` or a documented hash type. See [Generate and verify hashes](#generate-and-verify-hashes).

### Hash service behavior

`PayUHashService.kt` launches an unstructured `CoroutineScope(Dispatchers.IO)`. It POSTs JSON `{ "hashString": "<SDK string>" }` to `BuildConfig.HASH_ENDPOINT` with `HttpURLConnection`, `Content-Type: application/json`, and 15-second connect and read timeouts. A non-200 response returns null. The response body is parsed as JSON and its `hash` property is returned, or null if empty. Any exception is swallowed by `runCatching { ... }.getOrNull()`, and the callback is dispatched to `Dispatchers.Main`.

Failure therefore becomes a null hash and no call to `onHashGenerated`. There is no lifecycle cancellation, retry/backoff, correlation ID, HTTP response-body handling, authentication, certificate pinning, response schema validation, or user-visible hash error. It also does not close the connection explicitly or validate the endpoint scheme at runtime.

## Generate and verify hashes

### What PayU documents for dynamic hashes

**PayU documentation.** The Checkout Pro listener is called whenever the SDK needs an individual hash. The map contains:

- `CP_HASH_NAME`: the name of the hash the SDK is requesting.
- `CP_HASH_STRING`: the complete string to sign, excluding the merchant salt. The merchant should send this exact string to the server rather than reconstructing it from browser or app fields.
- `CP_POST_SALT`: documented as an optional value in the listener examples, and required for additional charges and split payment handling in the retrieved integration page. Its use must be confirmed for the installed SDK and enabled features.
- A hash type value may be present. The retrieved V2 hash page says that when the type is `V2`, the server uses SHA-256 with the salt as the key and the received hash string as the signed value, then returns the result through the same callback. Confirm the current SDK constants and exact server algorithm before enabling V2 features.

The normal documented dynamic flow is:

```text
SDK -> app generateHash(map)
map -> app extracts hash name, exact hash string, optional post-salt/type
app -> merchant HTTPS hash server
server -> signs according to hash name/type, never exposes salt
server -> app returns hash
app -> onHashGenerated({ requested hash name: generated hash })
```

Do not generate the dynamic hash locally and do not rebuild the string from `amount`, `txnid`, or other fields. The SDK has already provided the string and its operation context.

### Static hashes and symbolic formulas

The retrieved static-hash documentation describes hashes for enabled payment options, EMI, payment, and tokenized-card operations. The following are intentionally symbolic and redacted. They are not values to copy into a client:

- **Payment-related details for the mobile SDK:** `SHA-512(<merchant-key>|payment_related_details_for_mobile_sdk|<user-credential>|<merchant-salt>)`. This is passed through the appropriate additional parameter when the selected SDK flow requires it.
- **EMI eligible bins:** `SHA-512(<merchant-key>|eligibleBinsForEMI|default|<merchant-salt>)`.
- **EMI details:** `SHA-512(<merchant-key>|vas_for_mobile_sdk|<amount>|<merchant-salt>)` according to the retrieved static-hash page's EMI description.
- **Payment hash:** `SHA-512(<merchant-key>|<txnid>|<amount>|<productinfo>|<firstname>|<email>|<udf1>|<udf2>|<udf3>|<udf4>|<udf5>||||||<merchant-salt>)`.
- **Tokenized-card operations:** operation-specific formulas for delete, get, edit, save, or payment-instrument details, using the merchant key, documented command, user credential, separators, and merchant salt. Use the exact operation formula in the installed PayU documentation, not a generic concatenation.

These formulas describe PayU-documented static operations, not a license to expose a salt or calculate on the device. The package does not populate the full static additional-parameter set; it only sets two UDF entries and relies on dynamic callbacks.

### Exact package gap

The builder API route `builder-platform/src/routes/api/public/payu/hash.ts`:

- Responds to `OPTIONS` with 204 and permissive CORS headers.
- Reads `PAYU_SALT` from the environment, but falls back to an embedded sandbox salt when the variable is absent.
- Parses JSON and accepts only an object property named `hashString`.
- Requires a string length from 8 through 4096 characters.
- Returns `SHA-512(hashString + salt)` as `{ hash }` with permissive CORS.

The generated `HASH-ENDPOINT.md` has a similar route, but its observed example uses a maximum length of 1000 and has no minimum length. The generated web checkout instead sends order fields and expects `{ key, txnid, hash }`. Therefore:

- The browser route contract and Android route contract do not match.
- The Android route does not accept or return `hashName`, so it cannot itself select a name, although the client does map the returned hash to the SDK-provided name.
- Neither supplied route accepts `postSalt` or hash type.
- Neither route demonstrates the operation-specific lookup-API special algorithm or V2 SHA-256 path described in the retrieved material.
- The API route's fallback sandbox salt is a credential-handling defect and must be removed.
- `Access-Control-Allow-Origin: *` makes the signing endpoint callable by any origin; CORS is not authentication.

## Build the integration

The package is a useful shape for a proof-of-concept, not a production order system. The recommended build separates the browser display model from the merchant order model.

### 1. Create an order on the merchant server

The client should submit SKU IDs and quantities, not prices or a payable amount. The server authenticates the customer or checkout session, loads current catalog rows, validates stock and quantity limits, calculates shipping/tax/discounts, creates an order with an immutable total and a unique transaction ID, and returns only the fields required to start Checkout Pro.

The following is **illustrative TypeScript-like pseudocode**, not a claim about a PayU response schema:

```ts
// PSEUDOCODE. Merchant API contract, not PayU code.
app.post("/api/orders", requireCheckoutSession, async (req, res) => {
  const lines = parseSkuQuantities(req.body.lines); // reject unknown fields
  const catalog = await db.products.findBySkus(lines.map(x => x.sku));
  const priced = priceFromCatalog(catalog, lines);   // never trust client price
  const shipping = calculateShipping(priced, req.body.shippingAddress);
  const total = priced.subtotal + shipping + priced.tax - priced.discount;
  const order = await db.transaction(async tx => {
    const created = await tx.orders.insert({
      status: "created",
      currency: "INR",
      subtotal: priced.subtotal,
      shipping,
      tax: priced.tax,
      discount: priced.discount,
      total,
      idempotencyKey: req.header("Idempotency-Key"),
    });
    await tx.orderLines.insertMany(created.id, priced.lines);
    return created;
  });
  res.json({ orderId: order.id, txnId: order.txnId, amount: order.total.toFixed(2) });
});
```

The Android bridge should receive an opaque `orderId` and server-authoritative payment context, or receive the server-calculated fields after the app has authenticated the session. It should not accept arbitrary customer-controlled `amount`, product information, or transaction identity from WebView JavaScript.

### 2. Authenticate the hash endpoint

The server endpoint should authenticate the app/session where feasible, rate limit by merchant/session/device risk signals, allow only known hash operations, validate lengths and character sets, and keep the merchant key and salt in secret storage. It should log a redacted correlation ID, not the hash string, PII, salt, or full callback payload.

**Illustrative pseudocode.** The exact operation algorithms and parameter names must be filled from the installed PayU artifact and the current PayU documentation. Do not invent a response schema:

```ts
// PSEUDOCODE. Replace algorithm details with the installed PayU contract.
app.post("/api/payu/hash", requireAppAuth, rateLimit, async (req, res) => {
  const { hashName, hashString, hashType, postSalt } = validateHashRequest(req.body);
  const config = await merchantConfigFor(req.auth.merchantId);

  // The server signs the SDK-supplied string. It does not reconstruct it.
  let digest: string;
  if (hashType === "V2") {
    digest = sha256WithMerchantSaltAsKey(hashString, config.salt);
  } else {
    const suffix = postSalt ?? "";
    digest = sha512(hashString + config.salt + suffix);
  }
  // In production, allowlist hashName and select the documented algorithm
  // per operation. Reject unknown names instead of signing arbitrary input.
  assertAllowedHashName(hashName, config.enabledFeatures);
  res.json({ hash: digest }); // Preserve the installed SDK's required contract.
});
```

The pseudocode deliberately does not provide a lookup-API special algorithm or undocumented response fields. If the current PayU contract requires a server-side lookup before signing a particular operation, implement that exact algorithm in the allowlisted operation handler.

### 3. Construct Checkout Pro parameters

Use the installed SDK's exact builder and listener signatures. The observed package's parameter list is a useful checklist: amount, production flag, product info, key, phone, transaction ID, first name, email, SURL, FURL, user credential, and additional parameters. Add only documented features such as UDFs, user token, SKU details, EMI, split, TPV, or standing-instruction parameters.

**Illustrative Kotlin pseudocode:**

```kotlin
// PSEUDOCODE. Verify names and types against the installed Checkout Pro artifact.
val params = PayUPaymentParams.Builder()
    .setAmount(serverOrder.amount)
    .setIsProduction(environment.isProduction)
    .setProductInfo(serverOrder.productInfo)
    .setKey(environment.merchantKey)
    .setPhone(customer.phone)
    .setTransactionId(serverOrder.txnId)
    .setFirstName(customer.firstName)
    .setEmail(customer.email)
    .setSurl(environment.merchantSuccessUrl)
    .setFurl(environment.merchantFailureUrl)
    .setUserCredential(serverOrder.userCredential)
    .setAdditionalParams(documentedAdditionalParams)
    .build()

PayUCheckoutPro.open(this, params, listener)
```

Use merchant-owned HTTPS SURL/FURL for the live design, and do not treat them as the reconciliation system. The merchant server must separately consume callbacks, webhooks, or Verify Payment results as supported by the chosen PayU integration.

### 4. Make the native hash request lifecycle-aware

**Illustrative Kotlin pseudocode:**

```kotlin
// PSEUDOCODE. Use the project's HTTP client and lifecycle scope.
class CheckoutViewModel(
    private val api: MerchantHashApi
) : ViewModel() {
    fun generateHash(
        request: HashRequest,
        callback: (Result<String>) -> Unit
    ) {
        viewModelScope.launch {
            val result = runCatching {
                require(request.hashName.isNotBlank())
                require(request.hashString.length <= MAX_HASH_INPUT)
                api.sign(request) // HTTPS, authenticated, bounded timeout
            }
            callback(result)
        }
    }
}
```

Call `onHashGenerated` exactly once for each SDK request, including the requested name in the map. On a failure, surface a controlled checkout error and record a redacted event; do not silently abandon the callback. Tie work to the Activity/ViewModel lifecycle, cancel in-flight work when checkout is destroyed, and use bounded retries only when safe.

## Handle responses and fulfilment

The package currently navigates to a success page as soon as the SDK reports `onPaymentSuccess`. That is not sufficient. The page can be reached directly, the response is not parsed, and no server reconciliation is demonstrated.

**PayU documentation.** The retrieved integration example extracts `CP_PAYU_RESPONSE` and `CP_MERCHANT_RESPONSE` from the callback object. It also says UPI intent/in-app may not return a callback response through SURL/FURL and may have a different response format. Do not invent a universal response JSON schema. Capture the exact SDK response object for the selected artifact, map only documented fields, and send a server-verifiable transaction reference to the merchant backend.

**Illustrative Kotlin pseudocode for extraction:**

```kotlin
// PSEUDOCODE. Response keys and types must be checked against the installed SDK.
override fun onPaymentSuccess(response: Any) {
    val result = response as? Map<*, *> ?: return showPending()
    val payuResponse = result[PayUCheckoutProConstants.CP_PAYU_RESPONSE]
    val merchantResponse = result[PayUCheckoutProConstants.CP_MERCHANT_RESPONSE]
    merchantApi.reportClientResult(
        orderId = currentOrderId,
        txnId = currentTxnId,
        payuResponse = redactForTransport(payuResponse),
        merchantResponse = redactForTransport(merchantResponse)
    )
    showPendingUntilServerConfirms()
}

override fun onPaymentCancel(isTxnInitiated: Boolean) {
    if (isTxnInitiated) verifyOrPoll(currentOrderId, currentTxnId)
    else showCancelled()
}
```

**Illustrative server reconciliation pseudocode:**

```ts
// PSEUDOCODE. Use the current PayU callback/webhook/Verify Payment contracts.
app.post("/payu/callback", async (req, res) => {
  const event = parseDocumentedPayUCallback(req.body);
  await reconcileIdempotently(event.txnid, async (tx) => {
    const order = await tx.orders.lockByTxnId(event.txnid);
    if (!order) return recordUnknownTransaction(event);
    verifyReverseHashOrDocumentedSignature(event);
    const authoritative = await payuVerifyPayment(event.txnid); // exact API contract
    if (isPaidForExactOrder(authoritative, order)) {
      await tx.orders.markPaid(order.id, authoritative.reference);
      await tx.fulfilment.enqueueOnce(order.id);
    } else {
      await tx.orders.recordUnconfirmed(order.id, safeStatus(authoritative));
    }
  });
  res.status(200).send("ok");
});
```

The callback/webhook handler must verify authenticity, compare transaction ID, amount, currency, merchant key, and order ID, handle duplicate delivery idempotently, and use Verify Payment as a recovery path when a callback is missing or ambiguous. Fulfilment should happen only after the server marks the order paid, never because a browser loaded `payment-success.html`, a WebView showed a toast, or a client reported success.

## WebView bridge

The bridge is an attack boundary. A safe design should:

1. Prefer bundled, integrity-controlled assets. If remote storefront loading is required, allow only a fixed HTTPS origin and reject every other navigation, frame, and redirect.
2. Add a JavaScript interface only for trusted content. `addJavascriptInterface` exposes annotated methods to JavaScript; do not expose it to arbitrary remote pages.
3. Pass an opaque order/session reference or server-issued checkout token, not a client-selected amount, price, quantity, product info, or transaction ID.
4. Validate JSON size, required fields, types, lengths, allowed characters, and order ownership on the native side. Reject malformed JSON rather than using permissive defaults such as a fallback amount or email.
5. Disable unnecessary file access, universal access from file URLs, mixed content, debugging, and multiple-window behavior. Use the minimum settings required by the SDK and app.
6. Handle `shouldOverrideUrlLoading`, external intents, redirects, and back navigation deliberately. Do not let payment or arbitrary content escape into an untrusted external intent.
7. Do not load an unverified `HASH_ENDPOINT` or accept a remote URL from generated configuration. Require HTTPS and environment-controlled allowlists.

**Illustrative validation pseudocode:**

```kotlin
// PSEUDOCODE. Keep this boundary small and strict.
@JavascriptInterface
fun pay(raw: String) {
    require(raw.length <= 4096)
    val input = parseAndValidateOrderReference(raw) // rejects amount/price fields
    require(currentOrigin == "file:///android_asset/" || isAllowedMerchantOrigin(currentOrigin))
    lifecycleScope.launch {
        val serverOrder = merchantApi.getCheckoutContext(input.orderId)
        checkout.start(serverOrder)
    }
}
```

The supplied bridge currently permits any page loaded in the WebView to call `pay`, uses permissive `optString` defaults, and trusts browser-derived payment data. Those defaults are acceptable only as a source-review observation, not as a production security posture.

## UPI and lifecycle

The manifest's `upi` query allows the SDK to discover UPI-capable apps for intent handoff. The package also includes a UPI add-on dependency and a custom-browser dependency. That does not prove that UPI works in this source tree, because the project was not built or run, and the retrieved PayU documentation says UPI in-app and intent are unavailable in test mode.

For UPI and other flows that may leave the app:

- Preserve the transaction ID and order ID before opening Checkout Pro.
- Treat `onPaymentCancel(true)` as potentially initiated, not automatically unpaid. Call the merchant Verify Payment flow or mark the order pending.
- Implement lifecycle-safe restoration after rotation, process recreation, external UPI app return, and Activity recreation. The package has no `onNewIntent` handling, Activity Result flow, or persistent checkout state.
- Do not fulfil from an immediate callback. UPI intent may have a distinct result path, and a delayed bank status must be reconciled server-side.
- Check production manifest requirements from the current PayU documentation, including any test metadata or endpoint declarations that must be removed or changed. The supplied manifest contains no explicit debug metadata, but the Gradle and code are fixed to test mode.

## Test

The following facts are **PayU documentation examples retrieved for planning**, not tests run against this package:

- The integration documentation provides sandbox card, net-banking, and UPI test examples. This tutorial intentionally omits their values and credentials.
- The documentation states that UPI in-app and UPI intent are not available in test mode. Confirm the current limitation with PayU before designing a UPI test matrix.
- PayU documents an SDK callback example with separate PayU and merchant response entries and says to use Verify Payment when a transaction is initiated but the callback is uncertain.

A complete test plan for this package should include:

1. **Static checks.** Verify UTF-8, balanced Markdown and source fences, no salt or sandbox credential in generated browser assets/APK configuration, exact `HASH_ENDPOINT` replacement, consistent package IDs, and no test-only legal copy in the production build.
2. **Generator checks.** For every category/layout/palette combination, assert generated links, SKU slugs, image paths, localStorage key, HTML escaping, Android asset copies, and ZIP paths. Assert that `includeAndroid = false` excludes the Android tree.
3. **Backend contract checks.** Test authenticated and unauthenticated hash requests, invalid JSON, empty/oversized strings, unknown hash names, V2/type handling, post-salt handling, CORS policy, rate limits, redacted logs, and response shape required by the installed SDK. Test that the web order endpoint and Android dynamic-hash endpoint are separate, explicit contracts.
4. **Order integrity checks.** Change browser prices, quantities, SKU names, address fields, and total; verify that the server ignores forged price data and recalculates from SKU IDs. Replay idempotency keys and transaction IDs.
5. **SDK callback checks.** Exercise success, failure, error, cancellation before initiation, cancellation after initiation, missing hash response, malformed response, timeout, rotation, process recreation, and back navigation. Extract documented callback fields without logging PII.
6. **WebView checks.** Verify origin allowlisting, asset navigation, blocked external redirects, JavaScript interface exposure, malformed bridge payloads, oversized payloads, and external-intent handling.
7. **Callback and reconciliation checks.** Send duplicate callbacks, out-of-order statuses, incorrect amounts, incorrect transaction IDs, forged reverse hashes, missing callbacks, delayed Verify Payment success, and already-fulfilled orders. Confirm idempotent fulfilment.
8. **Documentation examples.** If using PayU's documented test card or UPI examples, copy them only from the current PayU pages at test time. Do not copy the attachment's sandbox key, salt, or other credential into this tutorial or production source.

## Go live

Before live payments:

1. Complete merchant onboarding/KYC and obtain production credentials through the approved PayU process. Store key and salt in server-side secret storage. Remove all embedded sandbox values from source, generated docs, BuildConfig, screenshots, logs, and sample code.
2. Replace the test endpoint and set the installed SDK's production flag to true. Do not rely only on a client boolean; make environment selection an audited server/build configuration.
3. Replace the placeholder hash endpoint with the merchant's authenticated HTTPS server. Remove the builder route's sandbox fallback and permissive wildcard CORS.
4. Use merchant-owned HTTPS SURL/FURL and configure server callbacks/webhooks or the documented Verify Payment recovery path. Do not use PayU's sample Android callback URLs in production.
5. Replace browser totals with a server-created order and authoritative SKU pricing. Persist the order before opening Checkout Pro.
6. Confirm exact dependency versions, repositories, transitive artifacts, listener signatures, and constants against a clean build. Resolve the package-versus-documentation version conflict rather than assuming either version is correct.
7. Add origin restrictions, strict bridge validation, lifecycle-safe coroutines, retry policy, idempotency, response parsing, reverse-hash/signature validation, and PII-safe observability.
8. Remove test-only copy such as “test mode”, test cards, sandbox URLs, and sample values from customer-facing production assets. Retain a separate controlled test environment.
9. Test production-like UPI return, cancellation, timeout, callback loss, and Verify Payment recovery. A successful UI callback is not a fulfilment decision.

## Troubleshooting

| Symptom | Likely source-review cause | Investigation and correction |
| --- | --- | --- |
| Browser checkout receives a 400 | Web script sends order fields, while builder route accepts only `hashString` | Create a separate web order/hash contract or change both sides deliberately; verify server response before posting to PayU. |
| Android checkout hangs before payment options | Hash callback returns without `onHashGenerated`, or endpoint response is not `{hash}` | Inspect redacted server status and correlation ID; handle `CP_HASH_NAME`, exact string, post-salt/type, and failures. |
| Hash works for one flow but not EMI, split, or add-ons | Simple `SHA-512(hashString + salt)` route ignores operation-specific behavior | Implement the documented operation allowlist and algorithms after artifact-level confirmation. |
| Checkout SDK symbols do not compile | Supplied dependency versions differ from current docs or artifact signatures | Resolve versions and imports from the actual Gradle artifacts; do not patch by guessing. |
| UPI app is not discovered | Manifest query, device, SDK artifact, or test-mode limitation | Check the current PayU UPI guidance, device capabilities, and the retrieved limitation on test intent/in-app flows. |
| Success page appears for an unpaid order | Static HTML can be opened directly; client callback is trusted | Make the page pending-only and have the server mark paid after verified reconciliation. |
| Amount differs between cart and PayU | Browser `localStorage` and `price` fields are mutable | Create the order server-side from SKU IDs and compare the PayU transaction to the persisted order. |
| Remote storefront cannot be used safely | Code comment suggests a remote URL, but `storeUrl` is fixed to assets and bridge policy is absent | Choose bundled assets or implement a strict HTTPS origin allowlist and navigation policy. |
| Payment state disappears after rotation or app return | Unstructured coroutine and no lifecycle/result restoration | Persist order/transaction state, use lifecycle-aware scopes, and reconcile after Activity recreation. |
| Callback logs expose sensitive data | Raw `Any` responses and ad hoc logging | Redact PII and payment payloads; log only event type, transaction correlation, and safe status. |

## Security and remediation

| Severity | Observed gap or risk | Required remediation |
| --- | --- | --- |
| Critical | sandbox values are embedded in generated documentation/source, and a test key is embedded in BuildConfig. | Rotate any exposed merchant credentials, remove values from generated output, inject environment-specific configuration, and keep salt only on the merchant server. |
| High | `HASH_ENDPOINT` is a placeholder and the backend is required for every SDK hash. | Make backend configuration mandatory, fail closed, use HTTPS, authenticate requests, and health-check the contract. |
| Critical | browser controls amount, prices, quantities, and product information. | Server-create orders from SKU IDs, authoritative catalog data, and an authenticated checkout session. |
| Critical | The server hash route signs client-supplied data and may not create or persist an order. | Bind signing to a persisted order and allowed transaction context; do not let a public route become a generic signing oracle. |
| High | The hash route has no authentication, rate limiting, strong operation validation, or safe CORS policy. | Require authentication or short-lived signed checkout tokens, allowlist operations, rate limit, validate inputs, restrict origins, and monitor abuse. |
| High | Web and Android hash response contracts differ. | Define separate versioned web and SDK contracts and test each against the installed SDK. |
| High | Browser SURL/FURL are static pages; Android SURL/FURL are PayU-hosted sample URLs. No demonstrated merchant callback/webhook/Verify Payment reconciliation exists. | Use merchant-owned HTTPS endpoints and a server reconciliation state machine with Verify Payment recovery. |
| Critical | Success/failure UI can be reached without proof and must not authorize fulfilment. | Treat UI as informational; fulfil only after verified server status and idempotent order transition. |
| High | Android bridge has no origin/trust restriction and permissive default values. | Restrict content origin, validate every field, remove dangerous defaults, and expose the smallest possible interface. |
| Medium | The remote-store comment conflicts with the fixed asset URL; WebView navigation/external-intent handling is not restricted. | Choose bundled assets or implement a reviewed remote mode with allowlisted navigation and safe intent handling. |
| High | timestamp-based transaction IDs are predictable and the order identity originates in the client flow. | Generate collision-resistant server transaction IDs and bind them to a persisted order. |
| Medium | `CoroutineScope(Dispatchers.IO)` is unstructured, hash failure is silent, and there is no lifecycle cleanup. | Use a ViewModel/lifecycle scope, explicit error states, bounded retry, cancellation, and one callback completion path. |
| High | No robust response parsing, reverse-hash/signature verification, idempotency, or PII-safe observability is demonstrated. | Parse documented fields, verify authenticity and amount, make callbacks idempotent, and redact telemetry. |
| High | SDK dependency and add-on versions differ from retrieved PayU documentation; artifact signatures may differ. | Confirm every version and API at artifact level, pin approved versions, and run clean build/instrumentation checks. |

## Sources

PayU documentation retrieved for this review:

- [Android Checkout Pro SDK](https://docs.payu.in/docs/android-checkoutpro-sdk)
- [Integration steps for Android Checkout Pro](https://docs.payu.in/docs/integration-steps-android-checkout-pro)
- [Hash generation for Checkout Pro SDK](https://docs.payu.in/docs/hash-generation-for-checkoutpro-sdk)
- [Generate static hash for Android SDK Pro](https://docs.payu.in/docs/generate-static-hash-android-sdk-pro)
- [PayU Android Checkout Pro sample app](https://docs.payu.in/docs/sample-app)

The package itself was inspected from the supplied archive and extracted tree, especially `builder-platform/src/lib/builder-data.ts`, `site-generator.ts`, `android-generator.ts`, `download-bundle.ts`, `builder-platform/src/routes/api/public/payu/hash.ts`, the generated `storefront-and-android/` files, and the generated Android Kotlin/Gradle/manifest files. This tutorial does not reproduce any key, salt, secret, sandbox credential, or attachment credential.
