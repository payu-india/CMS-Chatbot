---
title: PayU Hosted Checkout WebView Integration
excerpt: >-
  Embed PayU Hosted Checkout inside a WebView in your Android, iOS, or Flutter
  app. Platform-specific configuration for JavaScript, DOM storage, UPI intent
  handling, and deep-link routing.
deprecated: false
hidden: true
metadata:
  title: PayU Hosted Checkout WebView Integration for Mobile Apps
  description: >-
    Integrate PayU Hosted Checkout in a WebView for Android (Kotlin/Java), iOS
    (Swift/WKWebView), and Flutter. Configure UPI intent handling, JavaScript,
    DOM storage, and deep links.
  keywords:
    - payu hosted checkout webview android
    - payu webview ios swift wkwebview
    - payu flutter webview payment integration
    - payu upi intent android webview kotlin
    - payu upi intent android webview kotlin
    - payu webview javascript dom storage setup
    - payu npci upi mandate webview
  robots: index
next:
  description: Explore related information and resources.
---
<Banner
  isInline={true}
  message="Integration effort: Some technical setup required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
 />

WebView integration lets you embed the <Anchor target="_blank" href="https://docs.payu.in/docs/payu-hosted-checkout-1">PayU Hosted Checkout</Anchor> experience inside your mobile app without redirecting users to an external browser. Your existing PayU Hosted Checkout web integration works inside a WebView with platform-specific configuration.

<Callout icon="❗️" theme="error">
  ### **Important: NPCI UPI Mandate**

  NPCI requires that UPI payment intent URLs are handled as native deep links in your app — not opened inside the WebView. If you do not configure intent handling correctly, UPI payments will fail on your Android app. Refer to the Android Platform section below.
</Callout>

<Callout icon="📘" theme="info">
  ### **UPI App List is Platform-Controlled**

  The list of UPI apps displayed on the payment screen (GPay, PhonePe, Paytm, etc.) is managed globally by PayU and cannot be customised per merchant. Contact your PayU Key Account Manager to remove specific apps.
</Callout>

Have you not built your web integration yet? Start here:

<Cards columns="1">
  <Card title="Build Integration" href="./build-integration" icon="fa-code">
    Implement request parameters, hash generation, HTML form POST, and server-side response verification — required before embedding in a WebView.
  </Card>
</Cards>

***

## Platforms Supported

<Cards columns="3">
  <Card title="Android" href="#android">
    WebView settings, POST checkout, UPI intents, Chrome Custom Tab
  </Card>

  <Card title="iOS" href="#ios">
    WKWebView POST checkout, deeplink handling, LSApplicationQueriesSchemes
  </Card>

  <Card title="Flutter" href="#flutter">
    webview_flutter, method channels, UPI launch on Android and iOS
  </Card>
</Cards>

***

## Android

A complete Android WebView integration involves these four steps:

1. Configure WebView settings
2. Handle URL navigation — intercept UPI intents and `surl`/`furl` callbacks
3. POST payment parameters to PayU via the WebView
4. Handle bank authentication with Chrome Custom Tab (Optional)

<Accordion title="Step 1: Configure WebView Settings" icon="fa-gear">
  PayU's checkout page is a JavaScript application that uses DOM storage for session management. Without the settings below, the checkout will either fail to render or break mid-payment.

  <Tabs>
    <Tab title="Sample Payload">
      ```kotlin
      webView.settings.apply {
          javaScriptEnabled = true
          domStorageEnabled = true
          loadWithOverviewMode = true
          useWideViewPort = true
          setSupportMultipleWindows(true)
          mixedContentMode = WebSettings.MIXED_CONTENT_COMPATIBILITY_MODE
      }
      ```
    </Tab>

    <Tab title="Parameter Description">
      | Setting                                               | Required    | Why                                                                                              |
      | ----------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------ |
      | `javaScriptEnabled = true`                            | ✅           | PayU checkout requires JavaScript to render and function                                         |
      | `domStorageEnabled = true`                            | ✅           | PayU uses DOM storage for session management — disabling this causes checkout failures           |
      | `loadWithOverviewMode = true`                         | ✅           | Ensures the checkout page fits the screen width without horizontal scrolling                     |
      | `useWideViewPort = true`                              | ✅           | Tells the WebView to respect the viewport meta tag from PayU's page for correct layout           |
      | `setSupportMultipleWindows(true)`                     | Recommended | Some bank authentication flows open a new window; this setting allows it                         |
      | `mixedContentMode = MIXED_CONTENT_COMPATIBILITY_MODE` | Recommended | Allows the checkout to load assets from both HTTPS and HTTP origins, required by some bank pages |
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Step 2: Handle URL Navigation" icon="fa-arrows-alt-h">
  During the payment flow, PayU's checkout page triggers URL redirects for these 3 scenarios you must handle explicitly:

  - **UPI intent launch**: When a customer selects a UPI app (Google Pay, PhonePe, Paytm), PayU generates a `upi://` or `intent://` URL. This must be passed to Android's intent system to open the correct UPI app; The WebView cannot open it on its own.
  - **Payment success**: When payment completes, PayU redirects the WebView to your `surl`.
  - **Payment failure**: When payment fails or is cancelled, PayU redirects to your `furl`.

  Override `shouldOverrideUrlLoading` in your `WebViewClient` to intercept and handle each case:

  ```kotlin
  webView.webViewClient = object : WebViewClient() {
      override fun shouldOverrideUrlLoading(view: WebView?, request: WebResourceRequest?): Boolean {
          val url = request?.url?.toString() ?: return false

          return when {
              // UPI intent — pass to Android intent system to open the correct UPI app
              url.startsWith("upi://") || url.startsWith("intent://") -> {
                  try {
                      val intent = Intent.parseUri(url, Intent.URI_INTENT_SCHEME)
                      startActivity(intent)
                  } catch (e: ActivityNotFoundException) {
                      Toast.makeText(context, "UPI app not found", Toast.LENGTH_SHORT).show()
                  } catch (e: URISyntaxException) {
                      Toast.makeText(context, "Invalid UPI intent", Toast.LENGTH_SHORT).show()
                  }
                  true
              }
              // Payment success — send response to your backend for verification
              url.startsWith(successUrl) -> {
                  // Do not update order status here — verify the reverse hash on your server first
                  true
              }
              // Payment failure — navigate to your failure screen
              url.startsWith(failureUrl) -> {
                  true
              }
              else -> false
          }
      }
  }
  ```

  <Callout icon="fad fa-bell-exclamation" theme="error">
    ### Important: **Do not update order status in the app**

    When `surl` or `furl` is triggered, pass the response parameters to your backend for reverse hash verification before marking any order as paid. The URL can be intercepted or spoofed.
  </Callout>
</Accordion>

<Accordion title="Step 3: POST Payment Parameters to PayU" icon="fa-paper-plane">
  Use `webView.postUrl()` to POST the payment parameters to PayU's `_payment` endpoint. This is the WebView equivalent of the HTML form POST used in the web integration. Here, the parameters and endpoint are identical.<br />

  Your app must call your backend first to retrieve the signed payment parameters including the server-generated hash. Never generate the hash in the app.

  <Tabs>
    <Tab title="Request Payload">
      ```kotlin
      val paymentParams = mapOf(
          "key"         to merchantKey,
          "txnid"       to txnId,
          "amount"      to amount,
          "productinfo" to productInfo,
          "firstname"   to firstName,
          "email"       to email,
          "phone"       to phone,
          "surl"        to successUrl,
          "furl"        to failureUrl,
          "hash"        to generatedHash
      )

      // URL-encode each parameter value and join as an application/x-www-form-urlencoded body
      val postData = paymentParams.entries
          .joinToString("&") { "${it.key}=${URLEncoder.encode(it.value, "UTF-8")}" }
          .toByteArray()

      // POST to PayU — use test.payu.in for sandbox, secure.payu.in for production
      webView.postUrl("https://secure.payu.in/_payment", postData)
      ```
    </Tab>

    <Tab title="Parameter Description">
      | Parameter       | Description                                                                               |
      | --------------- | ----------------------------------------------------------------------------------------- |
      | `merchantKey`   | Your PayU merchant key                                                                    |
      | `txnId`         | Unique transaction ID generated by your backend — store it before posting                 |
      | `amount`        | Payment amount, two decimal places (e.g. `499.00`)                                        |
      | `productInfo`   | Brief product description                                                                 |
      | `firstName`     | Customer's first name                                                                     |
      | `email`         | Customer's email address                                                                  |
      | `phone`         | Customer's phone number                                                                   |
      | `successUrl`    | Your `surl` — must be a publicly reachable HTTPS URL                                      |
      | `failureUrl`    | Your `furl` — must be a publicly reachable HTTPS URL                                      |
      | `generatedHash` | SHA-512 hash generated server-side. See [Build Integration](./build-integration) Step 1.2 |

      For the full parameter list including optional fields (address, UDFs, `enforce_paymethod`, etc.), see [Build Integration → Step 1.1](./build-integration).
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Step 4: Handle Bank Authentication with Chrome Custom Tab (Optional)" icon="fa-window-restore">
  Some bank 3DS flows and NetBanking portals do not render correctly inside a WebView. Chrome Custom Tab provides a full browser environment and improves compatibility with these bank pages.<br />

  Add the below dependency to your `build.gradle`:

  ```groovy
  implementation 'androidx.browser:browser:1.5.0'
  ```

  Open bank redirect URLs in Chrome Custom Tab:

  ```kotlin
  val bankUrl = "https://bank-authentication-url.com"
  val customTabsIntent = CustomTabsIntent.Builder()
      .setShowTitle(true)
      .build()
  customTabsIntent.launchUrl(context, Uri.parse(bankUrl))
  ```

  <Callout icon="📘" theme="info">
    ### **Tips:**

    This step is optional. Add it if your users report bank authentication pages not loading or rendering incorrectly inside the WebView.
  </Callout>
</Accordion>

***

## iOS

A complete iOS WebView integration involves four steps:

1. Configure WKWebView
2. Declare UPI URL schemes in `Info.plist`
3. Handle navigation and deep links via `WKNavigationDelegate`
4. POST payment parameters to PayU

<Accordion title="Step 1: Configure WKWebView" icon="fa-gear">
  iOS uses `WKWebView` (WebKit). Configure it with JavaScript enabled and DOM storage support before loading any content. Here, both are required for PayU's checkout page to function.

  <Tabs>
    <Tab title="Request Payload">
      ```swift
      let config = WKWebViewConfiguration()
      let preferences = WKPreferences()

      // Required: PayU checkout requires JavaScript to render and function
      preferences.javaScriptEnabled = true
      config.preferences = preferences

      // Required: enables DOM storage for PayU's checkout session management
      let userContentController = WKUserContentController()
      config.userContentController = userContentController
      config.websiteDataStore = WKWebsiteDataStore.default()
      ```
    </Tab>

    <Tab title="Parameter Description">
      | Setting                        | Required | Why                                                                               |
      | ------------------------------ | -------- | --------------------------------------------------------------------------------- |
      | `javaScriptEnabled = true`     | ✅        | PayU checkout requires JavaScript to render and function                          |
      | `WKWebsiteDataStore.default()` | ✅        | Enables DOM and session storage. This is required for checkout session management |
    </Tab>
  </Tabs>

  Create the `WKWebView` with this configuration and add it to your view hierarchy before submitting the payment form.
</Accordion>

<Accordion title="Step 2: Declare UPI URL Schemes in Info.plist" icon="fa-file-code">
  iOS requires apps to explicitly declare any URL schemes they intend to open. Without this, `canOpenURL()` always returns `false` for UPI app schemes and UPI payments will silently fail to launch.<br />

  Add the following to your `Info.plist` under the `LSApplicationQueriesSchemes` key:

  <Tabs>
    <Tab title="Request Payload">
      ```xml
      <key>LSApplicationQueriesSchemes</key>
      <array>
          <string>upi</string>
          <string>gpay</string>
          <string>phonepe</string>
          <string>paytm</string>
          <string>bhim</string>
      </array>
      ```
    </Tab>

    <Tab title="Parameter Description">
      | Scheme    | UPI App                                             |
      | --------- | --------------------------------------------------- |
      | `upi`     | Generic UPI handler — required for all UPI payments |
      | `gpay`    | Google Pay                                          |
      | `phonepe` | PhonePe                                             |
      | `paytm`   | Paytm                                               |
      | `bhim`    | BHIM / NPCI                                         |
    </Tab>
  </Tabs>

  <Callout icon="📘" theme="info">
    ### **Tips:**

    Add only the schemes for UPI apps your customers are likely to use. Apple caps the total number of `LSApplicationQueriesSchemes` entries at 50.
  </Callout>
</Accordion>

<Accordion title="Step 3: Handle Navigation and Deep Links" icon="fa-arrows-alt-h">
  Implement `WKNavigationDelegate` to intercept three types of navigation events during the payment flow:

  - **UPI deep links** (`upi://`): When a customer selects a UPI app, open it via `UIApplication.shared.open(url)` and cancel the WebView navigation
  - **Success callback**: When PayU redirects to your `surl`, intercept it and route to your success screen
  - **Failure callback**: When PayU redirects to your `furl`, intercept it and route to your failure screen

  ```swift
  func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction,
               decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {
      guard let url = navigationAction.request.url else {
          decisionHandler(.allow)
          return
      }

      let urlString = url.absoluteString

      // UPI deep link — open the UPI app natively, cancel WebView navigation
      if urlString.hasPrefix("upi://") {
          if UIApplication.shared.canOpenURL(url) {
              UIApplication.shared.open(url)
          }
          decisionHandler(.cancel)
          return
      }

      // Payment success — pass response to your backend for reverse hash verification
      if urlString.hasPrefix(successUrl) {
          // Do not update order status here — verify the reverse hash on your server first
          decisionHandler(.cancel)
          return
      }

      // Payment failure — navigate to your failure screen
      if urlString.hasPrefix(failureUrl) {
          decisionHandler(.cancel)
          return
      }

      decisionHandler(.allow)
  }
  ```

  <Callout icon="fad fa-bell-exclamation" theme="error">
    ### Impotant: **Do not update order status in the app**

    When `surl` or `furl` is triggered, pass the response parameters to your backend for reverse hash verification before marking any order as paid.
  </Callout>
</Accordion>

<Accordion title="Step 4: POST Payment Parameters to PayU" icon="fa-paper-plane">
  Construct a `URLRequest` with `httpMethod = "POST"` and a URL-encoded body, then load it into the `WKWebView`. This is the iOS equivalent of the HTML form POST from the web integration.<br />

  Retrieve the signed payment parameters, including the server-generated hash from your backend before constructing the request. Never generate the hash in the app.

  <Tabs>
    <Tab title="Request Payload">
      ```swift
      func submitPaymentForm() {
          let paymentParams: [String: String] = [
              "key":         merchantKey,
              "txnid":       txnId,
              "amount":      amount,
              "productinfo": productInfo,
              "firstname":   firstName,
              "email":       email,
              "phone":       phone,
              "surl":        successUrl,
              "furl":        failureUrl,
              "hash":        generatedHash
          ]

          // URL-encode each value and join as an application/x-www-form-urlencoded body
          let postBody = paymentParams
              .map { "\($0.key)=\($0.value.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) ?? "")" }
              .joined(separator: "&")

          var request = URLRequest(url: URL(string: "https://secure.payu.in/_payment")!)
          request.httpMethod = "POST"
          request.httpBody = postBody.data(using: .utf8)
          request.setValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")

          webView.load(request)
      }
      ```
    </Tab>

    <Tab title="Parameter Description">
      | Parameter       | Description                                                                          |
      | --------------- | ------------------------------------------------------------------------------------ |
      | `merchantKey`   | Your PayU merchant key                                                               |
      | `txnId`         | Unique transaction ID generated by your backend — store it before posting            |
      | `amount`        | Payment amount, two decimal places (e.g. `499.00`)                                   |
      | `productInfo`   | Brief product description                                                            |
      | `firstName`     | Customer's first name                                                                |
      | `email`         | Customer's email address                                                             |
      | `phone`         | Customer's phone number                                                              |
      | `successUrl`    | Your `surl` — publicly reachable HTTPS URL                                           |
      | `failureUrl`    | Your `furl` — publicly reachable HTTPS URL                                           |
      | `generatedHash` | SHA-512 hash generated server-side. See [Build Integration](./build-integration) 1.2 |

      For the full parameter list including optional fields, see [Build Integration → Step 1](./build-integration).
    </Tab>

    <Tab title="New Tab">

    </Tab>
  </Tabs>
</Accordion>

***

## Flutter

A complete Flutter WebView integration involves four steps:

1. Add dependencies
2. Configure the WebView controller and JavaScript mode
3. Handle navigation and UPI intents via `NavigationDelegate`
4. POST payment parameters to PayU

<Accordion title="Step 1 — Add Dependencies" icon="fa-cube">
  Add the following to your `pubspec.yaml` and run `flutter pub get`:

  | Package           | Purpose                                                                                  |
  | ----------------- | ---------------------------------------------------------------------------------------- |
  | `webview_flutter` | Renders the WebView widget and exposes a `NavigationDelegate` for intercepting URL loads |
  | `url_launcher`    | Opens UPI payment apps and other external URLs from inside the Flutter app               |

  ```yaml
  dependencies:
    webview_flutter: ^4.4.1
    url_launcher: ^6.1.14
  ```
</Accordion>

<Accordion title="Step 2 — Configure the WebView Controller" icon="fa-gear">
  Create a `WebViewController` in `initState` with unrestricted JavaScript mode and a `NavigationDelegate`. Call `_submitPaymentForm()` immediately after configuration so the checkout loads as soon as the widget mounts.

  | Setting                       | Why                                                                          |
  | ----------------------------- | ---------------------------------------------------------------------------- |
  | `JavaScriptMode.unrestricted` | PayU checkout requires JavaScript — without this the page will not render    |
  | `NavigationDelegate`          | Intercepts all URL loads so you can handle UPI intents and payment callbacks |

  ```dart
  @override
  void initState() {
    super.initState();
    _controller = WebViewController()
      // Required: PayU checkout requires JavaScript to function
      ..setJavaScriptMode(JavaScriptMode.unrestricted)
      ..setNavigationDelegate(NavigationDelegate(
        onNavigationRequest: (NavigationRequest request) {
          // URL interception is handled in Step 3
          return NavigationDecision.navigate;
        },
      ));

    // Submit the payment form immediately after configuring the controller
    _submitPaymentForm();
  }
  ```
</Accordion>

<Accordion title="Step 3 — Handle Navigation and UPI Intents" icon="fa-arrows-alt-h">
  The `onNavigationRequest` callback fires for every URL the WebView attempts to load. Intercept three types:

  - **UPI and intent URLs** (`upi://` or `intent://`) — launch the UPI app externally using `url_launcher` with `LaunchMode.externalApplication`, then prevent the WebView from loading the URL
  - **Success callback** — when PayU navigates to your `surl`, prevent WebView navigation and route to your success screen
  - **Failure callback** — when PayU navigates to your `furl`, prevent WebView navigation and route to your failure screen

  ```dart
  onNavigationRequest: (NavigationRequest request) {
    final url = request.url;

    // UPI or intent URL — open the UPI app externally
    if (url.startsWith('upi://') || url.startsWith('intent://')) {
      _handleUpiIntent(url);
      return NavigationDecision.prevent;
    }

    // Payment success — pass response to your backend for reverse hash verification
    if (url.startsWith(widget.successUrl)) {
      // Do not update order status here — verify the reverse hash on your server first
      return NavigationDecision.prevent;
    }

    // Payment failure — navigate to your failure screen
    if (url.startsWith(widget.failureUrl)) {
      return NavigationDecision.prevent;
    }

    return NavigationDecision.navigate;
  },
  ```

  The `_handleUpiIntent` helper uses `url_launcher` to open the UPI app as a native external application:

  ```dart
  Future<void> _handleUpiIntent(String url) async {
    final uri = Uri.parse(url);
    if (await canLaunchUrl(uri)) {
      // externalApplication opens the UPI app outside Flutter (e.g. Google Pay, PhonePe)
      await launchUrl(uri, mode: LaunchMode.externalApplication);
    }
  }
  ```

  <Callout icon="⚠️" theme="warn">
    **Do not update order status in the app.** When `surl` or `furl` is triggered, pass the response parameters to your backend for reverse hash verification before marking any order as paid.
  </Callout>
</Accordion>

<Accordion title="Step 4 — POST Payment Parameters to PayU" icon="fa-paper-plane">
  Use `_controller.loadRequest()` with `LoadRequestMethod.post` to POST the payment parameters to PayU's endpoint. This is the Flutter equivalent of the HTML form POST from the web integration.

  Retrieve the signed payment parameters — including the server-generated hash — from your backend before calling `loadRequest`. Never generate the hash in the app.

  | Parameter     | Description                                                                               |
  | ------------- | ----------------------------------------------------------------------------------------- |
  | `merchantKey` | Your PayU merchant key                                                                    |
  | `txnId`       | Unique transaction ID generated by your backend — store it before posting                 |
  | `amount`      | Payment amount, two decimal places (e.g. `499.00`)                                        |
  | `productInfo` | Brief product description                                                                 |
  | `firstName`   | Customer's first name                                                                     |
  | `email`       | Customer's email address                                                                  |
  | `phone`       | Customer's phone number                                                                   |
  | `successUrl`  | Your `surl` — publicly reachable HTTPS URL                                                |
  | `failureUrl`  | Your `furl` — publicly reachable HTTPS URL                                                |
  | `hash`        | SHA-512 hash generated server-side. See [Build Integration](./build-integration) Step 1.2 |

  ```dart
  void _submitPaymentForm() {
    final params = {
      'key':         widget.merchantKey,
      'txnid':       widget.txnId,
      'amount':      widget.amount,
      'productinfo': widget.productInfo,
      'firstname':   widget.firstName,
      'email':       widget.email,
      'phone':       widget.phone,
      'surl':        widget.successUrl,
      'furl':        widget.failureUrl,
      'hash':        widget.hash,
    };

    // URL-encode each key and value, join as an application/x-www-form-urlencoded body
    final postBody = params.entries
        .map((e) => '${Uri.encodeComponent(e.key)}=${Uri.encodeComponent(e.value)}')
        .join('&');

    _controller.loadRequest(
      Uri.parse('https://secure.payu.in/_payment'),
      // POST sends parameters in the request body, not the URL
      method: LoadRequestMethod.post,
      body: postBody.codeUnits,
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
    );
  }
  ```

  For the full parameter list including optional fields, see [Build Integration → Step 1.1](./build-integration).
</Accordion>

***

## Common Issues

**UPI payments not launching on Android** — Ensure `shouldOverrideUrlLoading` intercepts `upi://` and `intent://` URLs and passes them to `Intent.parseUri`. Without this, UPI intent URLs are treated as web URLs and fail.

**Payment page not loading** — Check that `javaScriptEnabled = true` and `domStorageEnabled = true` are both set. The PayU checkout page requires JavaScript.

**Back button dismisses the WebView instead of navigating back** — Override the device back button press to call `webView.goBack()` if `webView.canGoBack()` is true.

**surl/furl not triggering on iOS** — Implement `decidePolicyFor navigationAction` in `WKNavigationDelegate` and match against your callback URLs.

For additional issues, see [Errors and Troubleshooting](../errors-and-troubleshooting).

***

## Security Notes

{/* Source: Salt-in-app-binary risk from general mobile security practice, consistent with "never client-side" rule in build-integration.md Step 1.2 callout and accept-payments-using-payu-hosted-checkout.md. Reverse hash requirement from build-integration.md Step 1.4. */}

<Callout icon="fad fa-bell-exclamation" theme="error">
  ### **Important: Do not embed your merchant salt or hash generation logic in the app binary.**

  Mobile app binaries can be decompiled. If the salt is in the app — even harder to understand — an attacker can extract it and generate valid hashes for arbitrary amounts, effectively forging payment requests.
</Callout>

**Correct pattern for WebView integration:**

1. Customer taps **Pay Now** in your app.
2. Your app calls your backend with the order details.
3. Your backend generates the SHA-512 hash using the stored salt and returns the signed payment parameters.
4. Your app POSTs those parameters to PayU via WebView using `postUrl` (Android) or a URLRequest (iOS/Flutter).

The merchant salt never leaves your server. Your app handles the WebView and UPI intents — it never touches credentials.

**Verify the response on your server, not in the app.** When the WebView navigates to your `surl` or `furl`, intercept the URL and pass the response parameters to your backend. Your backend validates the reverse hash and returns the verified payment status to the app. Do not update order status based on URL parameters in the app directly — the URL can be intercepted or modified.

See [Build Integration → Security](../integrate/build-integration#security) for the complete list of security requirements.

***

## Platform FAQs

**Can I use the same PayU Hosted Checkout web integration in my app?**
Yes. The WebView loads your existing payment form or directly POSTs parameters to the `_payment` endpoint. No separate mobile integration is needed.

**Does UPI work inside WebView?**
UPI collect works. UPI intent (which launches the UPI app) requires that you intercept the `upi://` or `intent://` URL and pass it to the device's intent system. Without this interception, UPI app launch fails.

**Do I need to generate the hash in the app?**
No. The hash must be generated on your server. The WebView integration calls your server to get the hash and other parameters, then POSTs them to PayU.

***

## Next Steps

<Cards columns="2">
  <Card title="Test Integration" href="./test-integration" icon="fa-flask">
    Test your WebView payment flow end-to-end using sandbox credentials — including UPI intent handling and callback routing.
  </Card>

  <Card title="Go-live Checklist" href="./go-live-checklist" icon="fa-circle-check">
    Switch to production credentials, verify security requirements, configure webhooks, and confirm production readiness.
  </Card>
</Cards>

<Callout icon="📘" theme="info">
  **Prefer a fully native mobile integration?**

  If you want native payment UI without a WebView, PayU offers dedicated mobile SDKs for Android, iOS, React Native, and Flutter. See [Mobile SDKs](../../../../mobile-sdks) for the native integration path.
</Callout>
