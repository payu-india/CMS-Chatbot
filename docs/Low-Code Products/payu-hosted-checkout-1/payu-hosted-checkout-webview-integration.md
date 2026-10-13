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
  message="Integration effort: Minimal technical setup required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
 />

WebView integration lets you embed the PayU Hosted Checkout experience inside your mobile app without redirecting users to an external browser. Your existing PayU Hosted Checkout web integration works inside a WebView with platform-specific configuration.

<Callout icon="❗️" theme="error">
  **NPCI UPI mandate — required reading before you build**

  NPCI requires that UPI payment intent URLs are handled as native deep links in your app — not opened inside the WebView. If you do not configure intent handling correctly, UPI payments will fail on your Android app. See the Android platform guide below.
</Callout>

<Callout icon="📘" theme="info">
  **UPI App List is platform-controlled**

  The list of UPI apps displayed on the payment screen (GPay, PhonePe, Paytm, etc.) is managed globally by PayU and cannot be customised per merchant. Contact your PayU Key Account Manager to remove specific apps.
</Callout>

***

## Platform Guides

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

### Required WebView Configuration

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

### POST the Payment Form to WebView

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

val postData = paymentParams.entries
    .joinToString("&") { "${it.key}=${URLEncoder.encode(it.value, "UTF-8")}" }
    .toByteArray()

webView.postUrl("https://secure.payu.in/_payment", postData)
```

### Handle UPI Intents

Override `shouldOverrideUrlLoading` to launch UPI apps as native intents:

```kotlin
webView.webViewClient = object : WebViewClient() {
    override fun shouldOverrideUrlLoading(view: WebView?, request: WebResourceRequest?): Boolean {
        val url = request?.url?.toString() ?: return false

        return when {
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
            url.startsWith(successUrl) -> {
                // Handle payment success
                true
            }
            url.startsWith(failureUrl) -> {
                // Handle payment failure
                true
            }
            else -> false
        }
    }
}
```

### Chrome Custom Tab for Bank Authentication

Some bank 3DS flows and netbanking portals require Chrome Custom Tab. Add the dependency:

```groovy
implementation 'androidx.browser:browser:1.5.0'
```

Open bank redirects in Chrome Custom Tab:

```kotlin
val bankUrl = "https://bank-authentication-url.com"
val customTabsIntent = CustomTabsIntent.Builder()
    .setShowTitle(true)
    .build()
customTabsIntent.launchUrl(context, Uri.parse(bankUrl))
```

***

## iOS

### Required WKWebView Configuration

```swift
let config = WKWebViewConfiguration()
let preferences = WKPreferences()
preferences.javaScriptEnabled = true
config.preferences = preferences

// Enable DOM storage
let userContentController = WKUserContentController()
config.userContentController = userContentController
config.websiteDataStore = WKWebsiteDataStore.default()
```

### POST the Payment Form

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

### Handle Deep Links for UPI

Declare UPI schemes in `Info.plist` under `LSApplicationQueriesSchemes`:

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

In your `WKNavigationDelegate`:

```swift
func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction,
             decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {
    guard let url = navigationAction.request.url else {
        decisionHandler(.allow)
        return
    }

    let urlString = url.absoluteString

    if urlString.hasPrefix("upi://") {
        if UIApplication.shared.canOpenURL(url) {
            UIApplication.shared.open(url)
        }
        decisionHandler(.cancel)
        return
    }

    if urlString.hasPrefix(successUrl) {
        // Handle success
        decisionHandler(.cancel)
        return
    }

    if urlString.hasPrefix(failureUrl) {
        // Handle failure
        decisionHandler(.cancel)
        return
    }

    decisionHandler(.allow)
}
```

***

## Flutter

### Add webview_flutter

```yaml
dependencies:
  webview_flutter: ^4.4.1
  url_launcher: ^6.1.14
```

### Build the WebView Widget

```dart
import 'package:webview_flutter/webview_flutter.dart';
import 'package:url_launcher/url_launcher.dart';

class PaymentWebView extends StatefulWidget {
  final String merchantKey;
  final String txnId;
  final String amount;
  final String productInfo;
  final String firstName;
  final String email;
  final String phone;
  final String successUrl;
  final String failureUrl;
  final String hash;

  const PaymentWebView({super.key, required this.merchantKey, required this.txnId,
      required this.amount, required this.productInfo, required this.firstName,
      required this.email, required this.phone, required this.successUrl,
      required this.failureUrl, required this.hash});

  @override
  State<PaymentWebView> createState() => _PaymentWebViewState();
}

class _PaymentWebViewState extends State<PaymentWebView> {
  late final WebViewController _controller;

  @override
  void initState() {
    super.initState();
    _controller = WebViewController()
      ..setJavaScriptMode(JavaScriptMode.unrestricted)
      ..setNavigationDelegate(NavigationDelegate(
        onNavigationRequest: (NavigationRequest request) {
          final url = request.url;
          if (url.startsWith('upi://') || url.startsWith('intent://')) {
            _handleUpiIntent(url);
            return NavigationDecision.prevent;
          }
          if (url.startsWith(widget.successUrl)) {
            // Handle success
            return NavigationDecision.prevent;
          }
          if (url.startsWith(widget.failureUrl)) {
            // Handle failure
            return NavigationDecision.prevent;
          }
          return NavigationDecision.navigate;
        },
      ));

    _submitPaymentForm();
  }

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

    final postBody = params.entries
        .map((e) => '${Uri.encodeComponent(e.key)}=${Uri.encodeComponent(e.value)}')
        .join('&');

    _controller.loadRequest(
      Uri.parse('https://secure.payu.in/_payment'),
      method: LoadRequestMethod.post,
      body: postBody.codeUnits,
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
    );
  }

  Future<void> _handleUpiIntent(String url) async {
    final uri = Uri.parse(url);
    if (await canLaunchUrl(uri)) {
      await launchUrl(uri, mode: LaunchMode.externalApplication);
    }
  }

  @override
  Widget build(BuildContext context) {
    return WebViewWidget(controller: _controller);
  }
}
```

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

<Callout icon="🔐" theme="warn">
  **Never embed your merchant salt or hash generation logic in the app binary.**

  Mobile app binaries can be decompiled. If the salt is in the app — even obfuscated — an attacker can extract it and generate valid hashes for arbitrary amounts, effectively forging payment requests.
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
