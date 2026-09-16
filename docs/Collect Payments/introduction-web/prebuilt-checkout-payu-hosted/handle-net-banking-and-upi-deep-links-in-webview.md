---
title: '[Internal Review]Handle Net Banking Deep-Links in WebView'
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
Handle Net Banking payment deep-links in your mobile WebView (Android and iOS). When users select Net Banking, PayU redirects to custom URL schemes (`nb://` and bank-specific schemes). Your app must intercept these URLs and launch the corresponding native app.

<Callout icon="📘" theme="info">
  ### **What You'll Build**

  A WebView integration that:

  - Intercepts payment deep-links before the WebView loads them
  - Launches the banking app installed on the device
  - Handles fallback when the app is not installed
  - Receives payment status via callback URLs
</Callout>

***

## Prerequisites

Before you begin, ensure you have:

- ✅ An active PayU merchant account with API credentials
- ✅ **Android:** Minimum SDK API 21 (Lollipop) or higher
- ✅ **iOS:** Deployment target iOS 11.0 or higher
- ✅ A WebView configured to load the PayU payment page
- ✅ Basic knowledge of WebView navigation interception

***

## Quick Integration Overview

Here's the end-to-end flow:

1. **User selects Net Banking** → PayU gateway generates a deep-link
2. **WebView intercepts the deep-link** → Your app catches the URL before loading
3. **Check if banking app is installed** → Use platform APIs to verify
4. **Launch the banking app** → Hand off the payment to the native app
5. **User completes payment** → Banking app processes the transaction
6. **Gateway redirects to callback URL** → WebView receives `surl` (success) or `furl` (failure)
7. **Parse response & update UI** → Display payment status to user

***

## Step 1: Configure URL Scheme Declarations

Both Android and iOS require you to declare which external app URL schemes you intend to query.

<Accordion title="Android: Configure AndroidManifest.xml" icon="fab fa-android">
  Add this `<queries>` block to your `AndroidManifest.xml` **outside** the `<application>` tag:

  ```xml
  <manifest xmlns:android="http://schemas.android.com/apk/res/android"
      package="com.yourapp.package">

      <!-- Required for Android 11+ (API 30+) -->
      <queries>
          <!-- Net Banking URL Schemes -->
          <intent>
              <action android:name="android.intent.action.VIEW" />
              <data android:scheme="nb" />
          </intent>
          <intent>
              <action android:name="android.intent.action.VIEW" />
              <data android:scheme="imobileappnb" />
          </intent>
          <intent>
              <action android:name="android.intent.action.VIEW" />
              <data android:scheme="hdfcbanknb" />
          </intent>
          <intent>
              <action android:name="android.intent.action.VIEW" />
              <data android:scheme="axisbanknb" />
          </intent>
          <intent>
              <action android:name="android.intent.action.VIEW" />
              <data android:scheme="yesirisnb" />
          </intent>
          
          <!-- Intent URL Scheme -->
          <intent>
              <action android:name="android.intent.action.VIEW" />
              <data android:scheme="intent" />
          </intent>
      </queries>

      <application>
          <!-- Your app configuration -->
      </application>
  </manifest>
  ```

  <Callout icon="⚠️" theme="warn">
    ### **Android 11+ Requirement**

    Without this configuration, `packageManager.resolveActivity()` will return `null` even if the banking app is installed.
  </Callout>
</Accordion>

<Accordion title="iOS: Configure Info.plist" icon="fab fa-apple">
  Add the `LSApplicationQueriesSchemes` array to your `Info.plist`:

  ```xml
  <key>LSApplicationQueriesSchemes</key>
  <array>
      <!-- Net Banking URL Schemes -->
      <string>nb</string>
      <string>imobileappnb</string>
      <string>hdfcbanknb</string>
      <string>axisbanknb</string>
      <string>yesirisnb</string>
      
      <!-- Intent URL Scheme -->
      <string>intent</string>
  </array>
  ```

  **Alternative:** Right-click `Info.plist` → Open As → Source Code, then paste the XML snippet inside the root `<dict>` tag.

  <Callout icon="⚠️" theme="warn">
    ### **iOS Requirement**

    Without this, `UIApplication.shared.canOpenURL()` will always return `false` for these custom schemes.
  </Callout>
</Accordion>

***

## Step 2: Set Up WebView and Intercept Deep-Links

Configure your WebView to intercept navigation requests and detect deep-link URLs.

<Accordion title="Android: WebViewClient Implementation" icon="fab fa-android">
  ### 2.1: Create Custom WebViewClient

  ```kotlin
  import android.webkit.WebView
  import android.webkit.WebViewClient
  import android.webkit.WebResourceRequest

  class PaymentWebViewClient : WebViewClient() {
      
      override fun shouldOverrideUrlLoading(view: WebView?, request: WebResourceRequest?): Boolean {
          val url = request?.url?.toString() ?: return false
          
          // Check if URL matches any deep-link scheme
          if (isDeepLink(url)) {
              handleDeepLink(view?.context, url)
              return true  // Prevent WebView from loading this URL
          }
          
          return false  // Let WebView handle other URLs
      }
      
      private fun isDeepLink(url: String): Boolean {
          return url.startsWith("nb://") ||
                 url.startsWith("intent://") ||
                 url.startsWith("imobileappnb://") ||
                 url.startsWith("hdfcbanknb://") ||
                 url.startsWith("axisbanknb://") ||
                 url.startsWith("yesirisnb://")
      }
      
      private fun handleDeepLink(context: Context?, url: String) {
          context?.let {
              if (it is PaymentActivity) {
                  it.launchBankingApp(url)
              }
          }
      }
  }
  ```

  ### 2.2: Attach to WebView

  ```kotlin
  import android.webkit.WebView
  import androidx.appcompat.app.AppCompatActivity

  class PaymentActivity : AppCompatActivity() {
      
      private lateinit var webView: WebView
      
      override fun onCreate(savedInstanceState: Bundle?) {
          super.onCreate(savedInstanceState)
          setContentView(R.layout.activity_payment)
          
          webView = findViewById(R.id.payment_webview)
          webView.settings.javaScriptEnabled = true
          webView.settings.domStorageEnabled = true
          
          // Attach custom client
          webView.webViewClient = PaymentWebViewClient()
          
          // Load PayU payment page
          webView.loadUrl("https://secure.payu.in/_payment")
      }
  }
  ```
</Accordion>

<Accordion title="iOS: WKNavigationDelegate Implementation" icon="fab fa-apple">
  ### 2.1: Set Up WKWebView

  ```swift
  import UIKit
  import WebKit

  class PaymentViewController: UIViewController, WKNavigationDelegate {
      
      var webView: WKWebView!
      
      override func viewDidLoad() {
          super.viewDidLoad()
          
          // Initialize WKWebView
          let webConfiguration = WKWebViewConfiguration()
          webView = WKWebView(frame: .zero, configuration: webConfiguration)
          webView.navigationDelegate = self
          
          // Add to view hierarchy
          view.addSubview(webView)
          webView.translatesAutoresizingMaskIntoConstraints = false
          NSLayoutConstraint.activate([
              webView.topAnchor.constraint(equalTo: view.topAnchor),
              webView.bottomAnchor.constraint(equalTo: view.bottomAnchor),
              webView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
              webView.trailingAnchor.constraint(equalTo: view.trailingAnchor)
          ])
          
          // Load PayU payment page
          if let url = URL(string: "https://secure.payu.in/_payment") {
              webView.load(URLRequest(url: url))
          }
      }
  }
  ```

  ### 2.2: Implement Navigation Delegate

  ```swift
  extension PaymentViewController {
      
      func webView(_ webView: WKWebView, 
                   decidePolicyFor navigationAction: WKNavigationAction, 
                   decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {
          
          guard let url = navigationAction.request.url else {
              decisionHandler(.allow)
              return
          }
          
          let urlString = url.absoluteString
          
          // Check if URL matches any deep-link scheme
          if isDeepLink(urlString) {
              launchBankingApp(url: url)
              decisionHandler(.cancel)  // Prevent WebView from loading
              return
          }
          
          decisionHandler(.allow)  // Let WebView handle other URLs
      }
      
      private func isDeepLink(_ urlString: String) -> Bool {
          return urlString.hasPrefix("nb://") ||
                 urlString.hasPrefix("intent://") ||
                 urlString.hasPrefix("imobileappnb://") ||
                 urlString.hasPrefix("hdfcbanknb://") ||
                 urlString.hasPrefix("axisbanknb://") ||
                 urlString.hasPrefix("yesirisnb://")
      }
  }
  ```
</Accordion>

<Callout icon="🚨" theme="default">
  ### **Critical Rule: Never Modify the Deep-Link URL**

  Do NOT URL-encode, decode, or alter the deep-link in any way. The URL contains cryptographic signatures that will break if modified. Pass it exactly as received.
</Callout>

***

## Step 3: Launch Banking App with Fallback

Check if the banking app is installed, launch it if available, or show a fallback if not.

<Accordion title="Android: Intent Handling" icon="fab fa-android">
  ```kotlin
  import android.content.Intent
  import android.content.pm.PackageManager
  import android.net.Uri
  import androidx.appcompat.app.AlertDialog

  class PaymentActivity : AppCompatActivity() {
      
      fun launchBankingApp(deepLinkUrl: String) {
          try {
              val intent = Intent(Intent.ACTION_VIEW, Uri.parse(deepLinkUrl))
              val packageManager: PackageManager = packageManager
              
              // Check if any app can handle this Intent
              if (intent.resolveActivity(packageManager) != null) {
                  // Banking app is installed - launch it
                  startActivity(intent)
              } else {
                  // App not installed - show fallback
                  showFallback()
              }
              
          } catch (e: Exception) {
              e.printStackTrace()
              showFallback()
          }
      }
      
      private fun showFallback() {
          AlertDialog.Builder(this)
              .setTitle("Banking App Required")
              .setMessage("The selected bank's app is not installed. Please install it or choose a different payment method.")
              .setPositiveButton("Choose Another Method") { dialog, _ ->
                  dialog.dismiss()
                  webView.goBack()  // Return to payment method selection
              }
              .setNegativeButton("Cancel") { dialog, _ ->
                  dialog.dismiss()
              }
              .show()
      }
  }
  ```

  **What Happens Next:**

  - If the app is installed → Banking app opens and processes payment
  - After payment → PayU redirects to your callback URL (`surl` or `furl`)
  - Your WebView loads the callback → Parse the response parameters
</Accordion>

<Accordion title="iOS: URL Opening" icon="fab fa-apple">
  ```swift
  import UIKit

  extension PaymentViewController {
      
      func launchBankingApp(url: URL) {
          // Check if any app can handle this URL
          if UIApplication.shared.canOpenURL(url) {
              // Banking app is installed - launch it
              UIApplication.shared.open(url, options: [:]) { success in
                  if !success {
                      self.showFallback()
                  }
              }
          } else {
              // App not installed - show fallback
              showFallback()
          }
      }
      
      private func showFallback() {
          let alert = UIAlertController(
              title: "Banking App Required",
              message: "The selected bank's app is not installed. Please install it or choose a different payment method.",
              preferredStyle: .alert
          )
          
          alert.addAction(UIAlertAction(title: "Choose Another Method", style: .default) { _ in
              self.webView.goBack()  // Return to payment method selection
          })
          
          alert.addAction(UIAlertAction(title: "Cancel", style: .cancel))
          
          present(alert, animated: true)
      }
  }
  ```

  **What Happens Next:**

  - If the app is installed → Banking app opens and processes payment
  - After payment → PayU redirects to your callback URL (`surl` or `furl`)
  - Your WebView loads the callback → Parse the response parameters
</Accordion>

***

## Step 4: Handle Payment Callbacks

After the user completes payment, PayU redirects back to your WebView via the success (`surl`) or failure (`furl`) URL you configured.

<Accordion title="Android: Callback Detection" icon="fab fa-android">
  ```kotlin
  override fun onPageFinished(view: WebView?, url: String?) {
      super.onPageFinished(view, url)
      
      url?.let {
          when {
              it.contains("yoursite.com/payment/success") -> {
                  handlePaymentSuccess(it)
              }
              it.contains("yoursite.com/payment/failure") -> {
                  handlePaymentFailure(it)
              }
          }
      }
  }

  private fun handlePaymentSuccess(url: String) {
      // Parse query parameters from callback URL
      val uri = Uri.parse(url)
      val txnid = uri.getQueryParameter("txnid")
      val status = uri.getQueryParameter("status")
      val hash = uri.getQueryParameter("hash")
      
      // Verify hash and update UI
      // ... your verification logic ...
  }

  private fun handlePaymentFailure(url: String) {
      // Handle failed payment
      // ... show error message ...
  }
  ```
</Accordion>

<Accordion title="iOS: Callback Detection" icon="fab fa-apple">
  ```swift
  func webView(_ webView: WKWebView, 
               decidePolicyFor navigationAction: WKNavigationAction, 
               decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {
      
      guard let url = navigationAction.request.url else {
          decisionHandler(.allow)
          return
      }
      
      let urlString = url.absoluteString
      
      // Check for callback URLs
      if urlString.contains("yoursite.com/payment/success") {
          handlePaymentSuccess(url: url)
          decisionHandler(.allow)
          return
      } else if urlString.contains("yoursite.com/payment/failure") {
          handlePaymentFailure(url: url)
          decisionHandler(.allow)
          return
      }
      
      // ... deep-link handling logic ...
      
      decisionHandler(.allow)
  }

  private func handlePaymentSuccess(url: URL) {
      // Parse query parameters from callback URL
      guard let components = URLComponents(url: url, resolvingAgainstBaseURL: false),
            let queryItems = components.queryItems else { return }
      
      let txnid = queryItems.first(where: { $0.name == "txnid" })?.value
      let status = queryItems.first(where: { $0.name == "status" })?.value
      let hash = queryItems.first(where: { $0.name == "hash" })?.value
      
      // Verify hash and update UI
      // ... your verification logic ...
  }

  private func handlePaymentFailure(url: URL) {
      // Handle failed payment
      // ... show error message ...
  }
  ```
</Accordion>

<Callout icon="🔐" theme="default">
  ### **Security Best Practice**

  Always verify the response hash before trusting the payment status. Compare the received hash against a hash computed using your merchant salt to ensure the response hasn't been tampered with.
</Callout>

***

## Step 5: Testing Your Integration

<Accordion title="Test Scenario 1: Banking App Installed" icon="far fa-check-double">
  **Setup:** Install at least one banking on your test device

  **Steps:**

  1. Launch your app and initiate a test payment
  2. Select Net Banking as the payment method
  3. Choose a bank whose app is installed
  4. Verify the banking app launches successfully
  5. Complete or cancel the payment in the banking app
  6. Verify your WebView receives the callback URL
  7. Confirm payment status is correctly displayed in your app

  **Expected Result:** ✅ Banking app opens → Payment completes → Callback received → Status shown
</Accordion>

<Accordion title="Test Scenario 2: Banking App Not Installed" icon="far fa-triangle-exclamation">
  **Setup:** Use a device/emulator without the selected banking app

  **Steps:**

  1. Launch your app and initiate a test payment
  2. Select a bank whose app is NOT installed
  3. Verify your fallback dialog/alert is shown
  4. Confirm the user can navigate back or choose another method
  5. Ensure no crashes or blank screens occur

  **Expected Result:** ✅ Fallback shown → User can retry or cancel → App remains stable
</Accordion>

<Accordion title="Test Scenario 3: Callback Verification" icon="far fa-shield">
  **Steps:**

  1. Complete a test payment
  2. Monitor WebView navigation events
  3. Verify the callback URL is detected
  4. Extract and log all query parameters (`txnid`, `status`, `hash`, etc.)
  5. Verify the hash matches your server-side computation
  6. Confirm UI updates correctly based on `status` value

  **Expected Result:** ✅ Callback detected → Parameters extracted → Hash verified → UI updated
</Accordion>

***

## Going Live Checklist

Before deploying to production:

- [x] **Environment URLs updated** — Replace sandbox URLs with production endpoints
- [x] **Live credentials configured** — Use production merchant key and salt (not test credentials)
- [x] **Manifest/Info.plist verified** — All URL schemes declared correctly
- [x] **Deep-link URLs unmodified** — No encoding/decoding in your code
- [x] **Fallback implemented** — Graceful handling when banking apps are missing
- [x] **Callback verification** — Hash validation is implemented
- [x] **Error handling** — Proper logging and error messages
- [x] **Multi-device testing** — Tested on Android 11+ and latest iOS versions
- [x] **Performance tested** — No memory leaks or WebView crashes

***

## Supported URL Schemes

Your integration should handle these custom URL schemes:

| Scheme            | Description           | Example                          |
| ----------------- | --------------------- | -------------------------------- |
| `nb://`           | Generic Net Banking   | `nb://netbanking?ver=1&mode=...` |
| `intent://`       | Android Intent scheme | `intent://netbanking#Intent;...` |
| `imobileappnb://` | ICICI Bank iMobile    | `imobileappnb://netbanking?...`  |
| `hdfcbanknb://`   | HDFC Bank             | `hdfcbanknb://netbanking?...`    |
| `axisbanknb://`   | Axis Bank             | `axisbanknb://netbanking?...`    |
| `yesirisnb://`    | Yes Bank IRIS         | `yesirisnb://netbanking?...`     |

<Callout icon="📌" theme="default">
  ### **Note:**&#x20;

  This list covers the most common banking apps. Additional bank-specific schemes may be added in future updates.
</Callout>

***

## Troubleshooting

<Accordion title="Banking app doesn't launch on Android 11+" icon="far fa-bug">
  **Problem:** `resolveActivity()` returns `null` even though the app is installed.

  **Solution:** Verify your `AndroidManifest.xml` includes the `<queries>` block with the correct URL scheme. Without this, Android 11+ blocks package visibility.
</Accordion>

<Accordion title="iOS canOpenURL() always returns false" icon="far fa-bug">
  **Problem:** `UIApplication.shared.canOpenURL()` returns `false` for all banking schemes.

  **Solution:** Add the URL schemes to `LSApplicationQueriesSchemes` in your `Info.plist`. iOS requires explicit declaration of queryable schemes.
</Accordion>

<Accordion title="Callback URL not detected" icon="far fa-bug">
  **Problem:** Payment completes but WebView doesn't detect the callback.

  **Solution:**

  - Ensure your `surl`/`furl` URLs are correctly configured during payment initiation
  - Check that your navigation delegate is detecting URL changes
  - Verify the callback URL pattern matches your detection logic
  - Test with a simple pattern match (e.g., `contains("payment/success")`)
</Accordion>

<Accordion title="Deep-link signature validation fails" icon="far fa-bug">
  **Problem:** Banking app shows "Invalid request" or signature errors.

  **Solution:** You're likely modifying the deep-link URL. Never encode, decode, or alter the URL in any way. Pass it exactly as received from the WebView navigation event.
</Accordion>

***

## Need Help?

- 📧 **Support:** [support@payu.in](mailto:support@payu.in) (include your merchant ID)
