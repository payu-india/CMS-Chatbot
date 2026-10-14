---
title: PayU's iOS WebView SDK Integration
deprecated: false
hidden: true
icon: far fa-mobile-retro
metadata:
  robots: index
---
Integrate PayU's WebView SDK into your iOS app to accept payments via Cards, Net Banking, UPI, and Wallets using a secure, PCI-compliant checkout flow powered by WKWebView.

<Callout>
**SDK version:** 1.0.0 | **Platform:** iOS 13.0+ | **Language:** Swift 5.0+

**Prerequisites:**
- Active PayU merchant account ([Sign up here](https://onboarding.payu.in/app/account))
{/* SME-CHECK: Confirm the Dashboard navigation path "Settings → Account & API Keys" is correct and publishable. */}
- Merchant Key and Salt from [PayU Dashboard](https://dashboard.payu.in) → Settings → Account & API Keys
- iOS 13.0+ deployment target
- Xcode 14.0 or later
- Swift 5.0 or later
- Enable preferred payment methods on the PayU Dashboard under **Settings** → **Payment Methods**.
</Callout>

<Warning>
**Security:** Never store your PayU Salt in the iOS application. Generate the payment hash on your backend and send the hash to the app.
</Warning>

***

## Quick Steps

<Cards columns={3}>

<Card title="1. Set Up Your Environment" icon="fa-gear">
Install PayU WebView SDK via CocoaPods or Swift Package Manager, add a full-screen WKWebView, and import the SDK framework into your project.
</Card>

<Card title="2. Build Payment Parameters" icon="fa-list-check">
Prepare POST parameters: `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `surl`, and `furl` — never store your merchant salt client-side.
</Card>

<Card title="3. Create Transaction and Hash on Backend" icon="fa-lock">
Your backend creates the transaction (`txnid`) and computes the SHA-512 hash using the 17-position formula — use the same `txnid` in the hash AND the POST body.
</Card>

<Card title="4. Initialize PayU WebView" icon="fa-mobile">
Create a `WebViewSDK` instance, set the delegate, and call `load()` with the payment URL and `postString`.
</Card>

<Card title="5. Handle Payment Callbacks" icon="fa-webhook">
Implement the `PayUDelegate` protocol: `payUonSuccess`, `payUonFailure`, `payUonError` — always verify payment on backend before fulfillment.
</Card>

<Card title="6. Verify Payment" icon="fa-shield-check">
Use the Verify Payment API to confirm transaction status server-side — never trust client-side responses alone.
</Card>

</Cards>

### Integration Flow

```mermaid
Create Transaction (backend)
       ↓
Get Hash from Backend
       ↓
Build POST Parameters
       ↓
Initialize WebViewSDK
       ↓
Load PayU Checkout
       ↓
Customer Completes Payment
       ↓
PayUDelegate Callback
       ↓
Success / Failure / Error
       ↓
Verify Payment (backend)
```

<Info>
**Production recommendation:** Your backend should create the transaction, generate the hash, and validate the final payment response before marking an order as paid. Never trust a client-side success callback alone.
</Info>

***

## Step 1: Set Up Your Environment

**What you need:** Xcode 14.0+ project, CocoaPods or Swift Package Manager, merchant credentials from PayU Dashboard.

Choose one of the following installation methods:

<Accordion title="Option 1: Install via CocoaPods" icon="fa-cube">
  ### 1.1 Add PayU SDK to Podfile

  ```ruby
  platform :ios, '13.0'

  target 'YourApp' do
    use_frameworks!
    pod 'PayUIndia-Webview'
  end
  ```

  ### 1.2 Install Dependencies

  ```bash
  cd /path/to/your/project
  pod install
  ```

  <Warning>
  After running `pod install`, **always open the `.xcworkspace` file**, not the `.xcodeproj` file.
  </Warning>
</Accordion>

<Accordion title="Option 2: Install via Swift Package Manager" icon="fa-box">
  ### 1.1 Add Package Dependency

  1. In Xcode, go to **File** → **Add Package Dependencies**
  2. Enter the repository URL:
     ```
     <redacted URL>
     ```
  3. Select **Up to Next Major Version** with version `1.0.0`
  4. Click **Add Package**
  5. Select the **PayUWebView** product and add it to your application target.
</Accordion>

### 1.2 Import the SDK

```swift
import UIKit
import WebKit
import PayUWebView
```

If you generate the hash locally for testing (see Step 3.2), also import:

```swift
import CryptoKit
```

<Info>
For production integrations, hash generation must be performed on your backend.
</Info>

### 1.3 Add WKWebView

The WKWebView should **fill the available screen area**. Use one of the following options:

<Tabs>
  <Tab title="Storyboard">
    1. Add a **WKWebView** to your View Controller in Interface Builder.
    2. Pin its leading, trailing, top, and bottom edges to the Safe Area (or superview) so it fills the screen.
    3. Connect it to an outlet:

    ```swift
    import UIKit
    import WebKit
    import PayUWebView

    class PaymentViewController: UIViewController {

        @IBOutlet weak var webView: WKWebView!
    }
    ```

    <Warning>
    **Critical:** Ensure the outlet is connected in Interface Builder **before** calling `load()` on the SDK. A nil webView will cause a crash.
    </Warning>
  </Tab>

  <Tab title="Programmatic">
    Create the WKWebView in code if you want to control its configuration, for example to use a non-persistent data store:

    ```swift
    import UIKit
    import WebKit
    import PayUWebView

    class PaymentViewController: UIViewController {

        var webView: WKWebView!

        override func viewDidLoad() {
            super.viewDidLoad()
            setUpWebView()
        }

        func setUpWebView() {
            let config = WKWebViewConfiguration()
            config.websiteDataStore = .nonPersistent()

            webView = WKWebView(frame: .zero, configuration: config)
            webView.translatesAutoresizingMaskIntoConstraints = false
            view.addSubview(webView)

            // Fill the available screen area
            NSLayoutConstraint.activate([
                webView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
                webView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
                webView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
                webView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor)
            ])
        }
    }
    ```

    <Info>
    A `nonPersistent()` data store ensures cookies and local storage from previous transactions don't interfere with new payments. This configuration only takes effect when the WKWebView is created in code; a storyboard WKWebView uses the default data store.
    </Info>
  </Tab>
</Tabs>

### 1.4 App Transport Security (ATS)

{/* SME-CHECK: Confirm whether merchants need any ATS entry at all for PayU domains, or whether the default ATS configuration is sufficient. */}
PayU payment endpoints use HTTPS, so the default ATS configuration typically works without changes. If your app customizes ATS:

- **Do not** set `NSAllowsArbitraryLoads = YES` unless it is specifically required.
- Configure exceptions only for the specific domains you need, rather than disabling ATS globally.
- Make sure your ATS configuration does not block the PayU domains used in the payment flow.

**Checkpoint:** ✅ SDK installed, PayUWebView product added to your target, full-screen WKWebView in place, no build errors.

***

## Step 2: Build Payment Parameters

**What you need:** Transaction details (amount, order ID, customer info), and the `key`, `txnid`, and `hash` returned by your backend (Step 3).

### 2.1 Prepare Request Parameters

<Tabs>
  <Tab title="Mandatory Parameters">

    | Parameter                    | Type & Description                                                                                                                                         | Example                            |
    | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
    | `<Glossary>key</Glossary>`   | String `Mandatory` — Merchant key from PayU Dashboard                                                                                                      | `<Your Test Key>`                  |
    | `<Glossary>txnid</Glossary>` | String `Mandatory` — Unique transaction ID (alphanumeric, max 25 chars), created by your backend. **Must be identical in hash calculation and POST body.** | `iOS_A1B2C3D4E5`                   |
    | `amount`                     | String `Mandatory` — Transaction amount (decimal format, 2 decimal places)                                                                                 | `100.00`                           |
    | `productinfo`                | String `Mandatory` — Product or service description                                                                                                        | `iPhone 14`                        |
    | `firstname`                  | String `Mandatory` — Customer's first name                                                                                                                 | `John`                             |
    | `email`                      | String `Mandatory` — Customer's email address                                                                                                              | `john@example.com`                 |
    | `phone`                      | String `Mandatory` — Customer's phone number                                                                                                               | `9876543210`                       |
    | `<Glossary>surl</Glossary>`  | String `Mandatory` — PayU SDK success callback URL (see note below)                                                                                        | `https://cbjs.payu.in/sdk/success` |
    | `<Glossary>furl</Glossary>`  | String `Mandatory` — PayU SDK failure callback URL (see note below)                                                                                        | `https://cbjs.payu.in/sdk/failure` |
    | `hash`                       | String `Mandatory` — `<Glossary>SHA-512</Glossary>` hash of transaction parameters (see Step 3)                                                            | `d1e2f3a4b5c6...`                  |
  </Tab>

  <Tab title="Optional Parameters">
    PayU supports the following optional parameters to support metadata:

    | Field  | Purpose              | Example                   |
    | ------ | -------------------- | ------------------------- |
    | `udf1` | User-defined field 1 | `OrderID_12345`           |
    | `udf2` | User-defined field 2 | `CouponCode_ABC`          |
    | `udf3` | User-defined field 3 | `CustomerSegment_Premium` |
    | `udf4` | User-defined field 4 | `ReferralSource_Mobile`   |
    | `udf5` | User-defined field 5 | `CampaignID_SUMMER2024`   |

    <Info>
    If not using UDF fields, pass empty strings (`""`) in both the hash calculation and POST body.
    </Info>
  </Tab>
</Tabs>

<Info>
**About surl/furl:** The `https://cbjs.payu.in/sdk/success` and `https://cbjs.payu.in/sdk/failure` URLs are the PayU SDK callback URLs that trigger the `PayUDelegate` callbacks. If you want to use your own surl/furl, follow [Handling Redirect URLs (SURL/FURL) with iOS](https://docs.payu.in/docs/handling-redirect-surlfurl-urls-with-ios) so that the SDK callbacks continue to work.
</Info>

### 2.2 Sample Request Values

```swift
let amount = "100.00"
let productinfo = "iPhone 14"
let firstname = "John"
let email = "john@example.com"
let phone = "9876543210"
let surl = "https://cbjs.payu.in/sdk/success"
let furl = "https://cbjs.payu.in/sdk/failure"

// UDF fields (optional)
let udf1 = ""
let udf2 = ""
let udf3 = ""
let udf4 = ""
let udf5 = ""

// key, txnid, and hash are returned by your backend (Step 3)
```

### 2.3 Build the POST String

Construct the URL-encoded POST body. Add this method to your view controller:

```swift
extension PaymentViewController {

    // RFC 3986 unreserved characters. Everything else (including &, =, +, and spaces) is percent-encoded.
    private static let formValueAllowed: CharacterSet = {
        var set = CharacterSet.alphanumerics
        set.insert(charactersIn: "-._~")
        return set
    }()

    private func formEncode(_ value: String) -> String {
        return value.addingPercentEncoding(withAllowedCharacters: Self.formValueAllowed) ?? value
    }

    func buildPostString(
        key: String,
        txnid: String,
        amount: String,
        productinfo: String,
        firstname: String,
        email: String,
        phone: String,
        surl: String,
        furl: String,
        hash: String,
        udf1: String = "",
        udf2: String = "",
        udf3: String = "",
        udf4: String = "",
        udf5: String = ""
    ) -> String {

        let params: [(String, String)] = [
            ("key", key),
            ("txnid", txnid),
            ("amount", amount),
            ("productinfo", productinfo),
            ("firstname", firstname),
            ("email", email),
            ("phone", phone),
            ("surl", surl),
            ("furl", furl),
            ("hash", hash),
            ("udf1", udf1),
            ("udf2", udf2),
            ("udf3", udf3),
            ("udf4", udf4),
            ("udf5", udf5)
        ]

        return params
            .map { "\(formEncode($0.0))=\(formEncode($0.1))" }
            .joined(separator: "&")
    }
}
```

<Warning>
**URL Encoding:** URL-encode every parameter value. Do not use `.urlQueryAllowed` — it leaves `&`, `=`, and `+` unencoded, so a value such as `productinfo = "A&B"` would break the POST body. Compute the hash on the **raw (unencoded)** values.
</Warning>

**Checkpoint:** ✅ All 10 mandatory parameters prepared, POST string builder implemented, UDF fields configured if needed.

***

## Step 3: Create the Transaction and Generate the Payment Hash

**What you need:** Merchant key and salt (from Dashboard), a backend API endpoint, the payment parameters from Step 2.

<Warning>
**Hashing on Server-side:** Hash generation must be done on your backend server. **NEVER** include your merchant salt in the iOS app source code or binary. Hardcoded salts expose your account to fraud and unauthorized transactions.
</Warning>

### 3.1 Hash Calculation Formula

PayU uses a **17-position pipe-separated formula** to generate the SHA-512 hash:

<Accordion title="Hash Parameter Sequence (17 Positions)" icon="fa-lock">
  | Position | Parameter     | Value Type                                    | Example            |
  | -------- | ------------- | --------------------------------------------- | ------------------ |
  | 1        | `key`         | Merchant key                                  | `<Your Test Key>`  |
  | 2        | `txnid`       | Transaction ID                                | `iOS_A1B2C3D4E5`   |
  | 3        | `amount`      | Amount (decimal)                              | `100.00`           |
  | 4        | `productinfo` | Product name                                  | `iPhone 14`        |
  | 5        | `firstname`   | First name                                    | `John`             |
  | 6        | `email`       | Email address                                 | `john@example.com` |
  | 7        | `udf1`        | User-defined field 1 (empty string if unused) | \`\`               |
  | 8        | `udf2`        | User-defined field 2                          | \`\`               |
  | 9        | `udf3`        | User-defined field 3                          | \`\`               |
  | 10       | `udf4`        | User-defined field 4                          | \`\`               |
  | 11       | `udf5`        | User-defined field 5                          | \`\`               |
  | 12–16    | (empty)       | Always empty                                  | \`\`               |
  | 17       | `salt`        | Merchant salt from Dashboard                  | `<Your Test Salt>` |

  **Formula:**

  ```
  key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt
  ```

  **Example Hash String (no UDFs):**

  ```
  <Your Test Key>|iOS_A1B2C3D4E5|100.00|iPhone 14|John|john@example.com|||||||||||<Your Test Salt>
  ```
</Accordion>

### Hash Generation Rules

1. **Use pipe (`|`) as separator** between all fields.
2. **Empty UDF fields:** If not using `udf1`–`udf5`, leave those positions empty (but keep the pipes).
3. **Reserved empty positions:** Positions 12–16 are always empty. After `udf5`, the string therefore contains **6 consecutive pipes** (`||||||`) — five for the empty positions plus the separator before `salt`. When no UDFs are used, there are **11 consecutive pipes** between `email` and `salt`.
4. **Use lowercase hexadecimal:** Convert the SHA-512 digest to a lowercase hex string.
5. **Do not generate `txnid` separately** for the hash and POST request. The values must match exactly.

***

### 3.2 Test Hash Generation (Development Only)

<Warning>
**FOR TESTING ONLY:** This code demonstrates the hash algorithm. In production, **all hash generation must happen on your backend server**.
</Warning>

<Accordion title="Test Implementation Using CryptoKit" icon="fa-flask">
  ```swift
  import Foundation
  import CryptoKit

  func generateTestHash(
      key: String,
      txnid: String,
      amount: String,
      productinfo: String,
      firstname: String,
      email: String,
      udf1: String = "",
      udf2: String = "",
      udf3: String = "",
      udf4: String = "",
      udf5: String = "",
      salt: String // NEVER hardcode in production!
  ) -> String {

      let hashString = "\(key)|\(txnid)|\(amount)|\(productinfo)|\(firstname)|\(email)|\(udf1)|\(udf2)|\(udf3)|\(udf4)|\(udf5)||||||\(salt)"

      let digest = SHA512.hash(data: Data(hashString.utf8))
      return digest.map { String(format: "%02x", $0) }.joined()
  }

  // TEST USAGE (Development only)
  // Generate the txnid ONCE and reuse it in the hash and the POST body (23 characters)
  let txnid = "iOS" + String(UUID().uuidString.replacingOccurrences(of: "-", with: "").prefix(20))

  let testHash = generateTestHash(
      key: "<Your Test Key>",
      txnid: txnid,
      amount: "100.00",
      productinfo: "iPhone 14",
      firstname: "John",
      email: "john@example.com",
      salt: "<Your Test Salt>" // NEVER hardcode in production
  )

  print("Test Hash: \(testHash)")
  ```

  **Output:** a 128-character lowercase hexadecimal string, for example:

  ```
  Test Hash: d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2
  ```
</Accordion>

***

### 3.3 Production: Create Transaction and Hash on Backend

<Accordion title="Backend Create-Transaction API (Production)" icon="fa-server">
  Create a secure API endpoint (e.g., `POST /api/payment/create-transaction`) on your backend.

  **Requirements:**
  ✅ Accept order details: `amount`, `productinfo`, `firstname`, `email`, `udf1`–`udf5`<br />✅ Generate a unique `txnid` and store it with the order<br />✅ Retrieve merchant key and salt from environment variables (never from the request)<br />✅ Compute the SHA-512 hash using the 17-position formula<br />✅ Return JSON: `{ "key": "...", "txnid": "...", "hash": "..." }`<br />✅ Use HTTPS only; validate the authentication token before processing

  <Info>
  For production, take the `amount` from your own order record rather than trusting the value sent by the app.
  </Info>

  **iOS Client Code:**

  ```swift
  struct PayUTransaction: Decodable {
      let key: String
      let txnid: String
      let hash: String
  }

  extension PaymentViewController {

      func createTransactionOnBackend(
          amount: String,
          productinfo: String,
          firstname: String,
          email: String,
          udf1: String = "",
          udf2: String = "",
          udf3: String = "",
          udf4: String = "",
          udf5: String = "",
          completion: @escaping (PayUTransaction?) -> Void
      ) {

          guard let url = URL(string: "<redacted URL>") else {
              completion(nil)
              return
          }

          var request = URLRequest(url: url)
          request.httpMethod = "POST"
          request.setValue("application/json", forHTTPHeaderField: "Content-Type")
          request.setValue("Bearer YOUR_AUTH_TOKEN", forHTTPHeaderField: "Authorization")

          let params: [String: String] = [
              "amount": amount,
              "productinfo": productinfo,
              "firstname": firstname,
              "email": email,
              "udf1": udf1,
              "udf2": udf2,
              "udf3": udf3,
              "udf4": udf4,
              "udf5": udf5
          ]

          request.httpBody = try? JSONSerialization.data(withJSONObject: params)

          URLSession.shared.dataTask(with: request) { data, _, _ in
              guard let data = data,
                    let transaction = try? JSONDecoder().decode(PayUTransaction.self, from: data) else {
                  completion(nil)
                  return
              }
              completion(transaction)
          }.resume()
      }
  }
  ```

  **Backend Example (Node.js):**

  ```javascript
  const crypto = require('crypto');

  app.post('/api/payment/create-transaction', (req, res) => {
      const {
          amount, productinfo, firstname, email,
          udf1 = '', udf2 = '', udf3 = '', udf4 = '', udf5 = ''
      } = req.body;

      const key = process.env.PAYU_MERCHANT_KEY;   // Retrieve from environment
      const salt = process.env.PAYU_MERCHANT_SALT; // Retrieve from environment

      // Generate the transaction ID once (23 characters)
      const txnid = 'iOS' + crypto.randomBytes(10).toString('hex');

      // Save txnid, amount, and order details in your database here

      const hashString = `${key}|${txnid}|${amount}|${productinfo}|${firstname}|${email}|${udf1}|${udf2}|${udf3}|${udf4}|${udf5}||||||${salt}`;

      const hash = crypto.createHash('sha512').update(hashString).digest('hex').toLowerCase();

      res.json({ key, txnid, hash });
  });
  ```
</Accordion>

**Checkpoint:** ✅ Backend API creates the transaction and returns `key`, `txnid`, and `hash` over HTTPS; merchant salt never exposed client-side.

***

## Step 4: Initialize PayU WebView

**What you need:** Payment URL, transaction details from Step 3, POST string builder from Step 2, WKWebView in place.

### 4.1 Initialize WebViewSDK

```swift
import UIKit
import WebKit
import PayUWebView

class PaymentViewController: UIViewController {

    @IBOutlet weak var webView: WKWebView!

    // Retain the SDK instance as an instance variable
    var webViewManager: WebViewSDK?

    override func viewDidLoad() {
        super.viewDidLoad()
        initiatePayment()
    }

    func initiatePayment() {
        // 1. Prepare parameters
        let amount = "100.00"
        let productinfo = "iPhone 14"
        let firstname = "John"
        let email = "john@example.com"
        let phone = "9876543210"
        let surl = "https://cbjs.payu.in/sdk/success"
        let furl = "https://cbjs.payu.in/sdk/failure"

        // 2. Create the transaction and get the hash from your backend
        createTransactionOnBackend(
            amount: amount,
            productinfo: productinfo,
            firstname: firstname,
            email: email
        ) { [weak self] transaction in
            guard let self = self, let transaction = transaction else {
                print("Failed to create transaction")
                return
            }

            // 3. Build the POST string using the SAME txnid that was used in the hash
            let postString = self.buildPostString(
                key: transaction.key,
                txnid: transaction.txnid,
                amount: amount,
                productinfo: productinfo,
                firstname: firstname,
                email: email,
                phone: phone,
                surl: surl,
                furl: furl,
                hash: transaction.hash
            )

            // 4. Load PayU Checkout on the main thread
            DispatchQueue.main.async {
                self.loadPayUWebView(postString: postString)
            }
        }
    }
}
```

<Info>
`PaymentViewController` must also conform to `PayUDelegate` (see Step 5). For a single copy-paste example, see [Complete Integration Example](#complete-integration-example).
</Info>

<Warning>
**Memory Management:** Do not declare `webViewManager` as a local variable inside a function. If the SDK instance is deallocated before payment completes, delegate callbacks will not fire. The SDK instance must remain alive for the duration of the payment.
</Warning>

### 4.2 Payment Environment URLs

| Environment    | URL                               |
| -------------- | --------------------------------- |
| **Test**       | `https://test.payu.in/_payment`   |
| **Production** | `https://secure.payu.in/_payment` |

<Info>
Always use the **test endpoint** during development and testing. Switch to the **production endpoint** only after completing all test scenarios in Step 7.
</Info>

### 4.3 Load the Payment Page

```swift
extension PaymentViewController {

    func loadPayUWebView(postString: String) {
        // Test endpoint
        let paymentURL = "https://test.payu.in/_payment"

        // Production endpoint (use after testing):
        // let paymentURL = "https://secure.payu.in/_payment"

        webViewManager = WebViewSDK(webView: webView)
        webViewManager?.delegate = self
        webViewManager?.load(urlString: paymentURL, postString: postString)
    }
}
```

<Warning>
Always set `delegate` **before** calling `load()`.
</Warning>

**Checkpoint:** ✅ WebViewSDK initialized, delegate assigned, payment page loads in WKWebView.

***

## Step 5: Handle Payment Callbacks

**What you need:** `PayUDelegate` protocol implemented, backend API for payment verification.

Conform your view controller to `PayUDelegate`. The SDK calls one of the following methods:

| Method          | Description                    |
| --------------- | ------------------------------ |
| `payUonSuccess` | Payment completed successfully |
| `payUonFailure` | Payment failed or was declined |
| `payUonError`   | Technical or processing error  |

Each method receives a `WKScriptMessage`. The payment response is available through `message.body`.

<Accordion title="Step 5.1: Implement PayUDelegate Protocol" icon="fa-code">
  ```swift
  extension PaymentViewController: PayUDelegate {

      func payUonSuccess(_ message: WKScriptMessage) {
          print("✅ Payment success: \(message.body)")

          let response = parsePayUResponse(message.body)
          let txnid = response["txnid"] as? String ?? ""

          // CRITICAL: Verify payment on backend before fulfillment
          verifyPaymentOnBackend(txnid: txnid)
      }

      func payUonFailure(_ message: WKScriptMessage) {
          print("❌ Payment failed: \(message.body)")

          let response = parsePayUResponse(message.body)
          let errorMessage = response["error_Message"] as? String ?? "Payment failed."

          showAlert(title: "Payment Failed", message: errorMessage)
          logPaymentFailure(response: response)
      }

      func payUonError(_ message: WKScriptMessage) {
          print("⚠️ Payment error: \(message.body)")

          showAlert(title: "Error", message: "Payment could not be completed. Please try again.")
          logSDKError(message: message.body)
      }
  }
  ```

  The following helper converts `message.body` into a dictionary, whether the SDK delivers it as a JSON string or as a dictionary:

  {/* SME-CHECK: Confirm the exact type and format of message.body (JSON string or dictionary) for each callback. */}

  ```swift
  extension PaymentViewController {

      func parsePayUResponse(_ body: Any) -> [String: Any] {
          if let dictionary = body as? [String: Any] {
              return dictionary
          }
          if let json = body as? String,
             let data = json.data(using: .utf8),
             let dictionary = try? JSONSerialization.jsonObject(with: data) as? [String: Any] {
              return dictionary
          }
          return [:]
      }
  }
  ```
</Accordion>

<Accordion title="Step 5.2: Handling Payment Success — payUonSuccess" icon="fa-circle-check">
  The `payUonSuccess` callback is triggered when the payment gateway returns a success response.

  ```swift
  func payUonSuccess(_ message: WKScriptMessage) {
      let response = parsePayUResponse(message.body)

      // Extract key parameters
      let txnid = response["txnid"] as? String ?? ""
      let mihpayid = response["mihpayid"] as? String ?? "" // PayU transaction ID
      let amount = response["amount"] as? String ?? ""

      // Display success message
      let summary = """
      Payment Successful!

      Transaction ID: \(txnid)
      PayU ID: \(mihpayid)
      Amount: ₹\(amount)
      """

      showAlert(title: "Success", message: summary) {
          // CRITICAL: Always verify on backend before order fulfillment
          self.verifyPaymentOnBackend(txnid: txnid)
      }
  }
  ```

  <Warning>
  **CRITICAL:** Receiving the `payUonSuccess` callback does **not** guarantee the payment actually succeeded. Always verify the transaction status on your backend using PayU's Verify Payment API before marking an order as paid or delivering goods/services.
  </Warning>
</Accordion>

<Accordion title="Step 5.3: Handling Payment Failure — payUonFailure" icon="fa-circle-xmark">
  The `payUonFailure` callback is triggered when payment is declined, cancelled, or fails validation.

  ```swift
  func payUonFailure(_ message: WKScriptMessage) {
      let response = parsePayUResponse(message.body)

      let status = response["status"] as? String ?? ""
      let errorMessage = response["error_Message"] as? String ?? "Payment failed."
      let field = response["field"] as? String ?? ""

      var displayMessage = errorMessage

      // Handle specific failure scenarios
      if status == "userCancelled" {
          displayMessage = "Payment was cancelled by you."
      } else if status == "failed" && field == "card" {
          displayMessage = "Card payment failed. Please check card details and try again."
      } else if errorMessage.lowercased().contains("insufficient") {
          displayMessage = "Insufficient balance. Please try a different payment method."
      }

      showAlert(title: "Payment Failed", message: displayMessage)

      // Log for analytics
      logPaymentFailure(response: response)
  }
  ```

  **Common Failure Scenarios:**

  - User cancelled payment
  - Insufficient balance
  - Card declined by bank
  - Invalid CVV or expiry date
  - Network timeout during payment
</Accordion>

<Accordion title="Step 5.4: Handling Errors — payUonError" icon="fa-triangle-exclamation">
  The `payUonError` callback handles technical or processing errors. Inspect `message.body` for details.

  ```swift
  func payUonError(_ message: WKScriptMessage) {
      print("Payment error: \(message.body)")

      showAlert(
          title: "Error",
          message: "An error occurred while processing the payment. Please try again."
      )

      // Send to crash reporting/analytics
      logSDKError(message: message.body)
  }
  ```
</Accordion>

### 5.5 Helper Functions

```swift
extension PaymentViewController {

    // Display alert with UIAlertController
    func showAlert(title: String, message: String, completion: (() -> Void)? = nil) {
        let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default) { _ in
            completion?()
        })
        present(alert, animated: true)
    }

    // Verify payment on backend
    func verifyPaymentOnBackend(txnid: String) {
        // Call your backend API, which uses PayU's Verify Payment API (see Step 6)
    }

    // Log payment failure
    func logPaymentFailure(response: [String: Any]) {
        // Send to analytics (Firebase, Mixpanel, etc.)
    }

    // Log payment error
    func logSDKError(message: Any) {
        // Send to crash reporting (Crashlytics, Sentry, etc.)
    }
}
```

### 5.6 Sample Payment Responses

{/* SME-CHECK: Confirm these sample payloads match what the SDK actually delivers in message.body. */}

<Info>
The samples below are illustrative. The fields returned can vary by payment mode. Always parse `message.body` defensively.
</Info>

<Accordion title="Success Response JSON" icon="fa-file-code">
  ```json
  {
    "error": "E000",
    "error_Message": "No Error",
    "mihpayid": "403993715527698466",
    "mode": "CC",
    "status": "success",
    "unmappedstatus": "captured",
    "key": "<Your Test Key>",
    "txnid": "iOS_A1B2C3D4E5",
    "amount": "100.00",
    "cardCategory": "domestic",
    "discount": "0.00",
    "net_amount_debit": "100.00",
    "addedon": "2024-01-15 14:23:45",
    "productinfo": "iPhone 14",
    "firstname": "John",
    "lastname": "",
    "address1": "",
    "address2": "",
    "city": "",
    "state": "",
    "country": "",
    "zipcode": "",
    "email": "john@example.com",
    "phone": "9876543210",
    "udf1": "",
    "udf2": "",
    "udf3": "",
    "udf4": "",
    "udf5": "",
    "hash": "a1b2c3d4e5f6...",
    "bank_ref_num": "1234567890",
    "bankcode": "CC",
    "PG_TYPE": "AXISPG",
    "encryptedPaymentId": "...",
    "payuMoneyId": ""
  }
  ```
</Accordion>

<Accordion title="Failure Response JSON" icon="fa-file-code">
  ```json
  {
    "error": "E001",
    "error_Message": "Transaction declined by bank",
    "mihpayid": "403993715527698467",
    "mode": "CC",
    "status": "failed",
    "unmappedstatus": "failed",
    "key": "<Your Test Key>",
    "txnid": "iOS_A1B2C3D4E5",
    "amount": "100.00",
    "productinfo": "iPhone 14",
    "firstname": "John",
    "email": "john@example.com",
    "phone": "9876543210",
    "hash": "d4e5f6a7b8c9...",
    "field": "card"
  }
  ```
</Accordion>

**Checkpoint:** ✅ All three delegate methods implemented, success/failure/error responses handled, backend verification triggered.

***

## Complete Integration Example

The following example shows the full flow in a single view controller: create the transaction on your backend, build the POST string, load PayU Checkout, and handle the callbacks.

```swift
import UIKit
import WebKit
import PayUWebView

struct PayUTransaction: Decodable {
    let key: String
    let txnid: String
    let hash: String
}

class PaymentViewController: UIViewController {

    @IBOutlet weak var webView: WKWebView!

    // Keep the SDK instance alive for the duration of the payment
    var webViewManager: WebViewSDK?

    let amount = "499.99"
    let productInfo = "Product"
    let firstName = "John"
    let email = "john@example.com"
    let phoneNumber = "9999999999"

    let surl = "https://cbjs.payu.in/sdk/success"
    let furl = "https://cbjs.payu.in/sdk/failure"

    // Test: https://test.payu.in/_payment | Production: https://secure.payu.in/_payment
    let paymentURL = "https://test.payu.in/_payment"

    override func viewDidLoad() {
        super.viewDidLoad()
        startPayment()
    }

    private func startPayment() {
        // 1. Your backend creates the transaction and returns key, txnid, and hash
        createTransactionOnBackend { [weak self] transaction in
            guard let self = self, let transaction = transaction else { return }

            // 2. Build the POST body with the SAME txnid used in the hash
            let postString = self.formBody([
                ("key", transaction.key),
                ("txnid", transaction.txnid),
                ("amount", self.amount),
                ("productinfo", self.productInfo),
                ("firstname", self.firstName),
                ("email", self.email),
                ("phone", self.phoneNumber),
                ("surl", self.surl),
                ("furl", self.furl),
                ("hash", transaction.hash)
            ])

            // 3. Initialize the SDK, set the delegate, then load
            DispatchQueue.main.async {
                self.webViewManager = WebViewSDK(webView: self.webView)
                self.webViewManager?.delegate = self
                self.webViewManager?.load(urlString: self.paymentURL, postString: postString)
            }
        }
    }

    private func createTransactionOnBackend(completion: @escaping (PayUTransaction?) -> Void) {
        guard let url = URL(string: "<redacted URL>") else {
            completion(nil)
            return
        }

        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.setValue("Bearer YOUR_AUTH_TOKEN", forHTTPHeaderField: "Authorization")
        request.httpBody = try? JSONSerialization.data(withJSONObject: [
            "amount": amount,
            "productinfo": productInfo,
            "firstname": firstName,
            "email": email
        ])

        URLSession.shared.dataTask(with: request) { data, _, _ in
            let transaction = data.flatMap { try? JSONDecoder().decode(PayUTransaction.self, from: $0) }
            completion(transaction)
        }.resume()
    }

    private func formBody(_ params: [(String, String)]) -> String {
        var allowed = CharacterSet.alphanumerics
        allowed.insert(charactersIn: "-._~")
        return params
            .map { key, value in
                "\(key)=\(value.addingPercentEncoding(withAllowedCharacters: allowed) ?? value)"
            }
            .joined(separator: "&")
    }
}

extension PaymentViewController: PayUDelegate {

    func payUonSuccess(_ message: WKScriptMessage) {
        print("Success: \(message.body)")
        // Verify the payment on your backend, then navigate to your success screen
    }

    func payUonFailure(_ message: WKScriptMessage) {
        print("Failure: \(message.body)")
        // Show payment failure UI
    }

    func payUonError(_ message: WKScriptMessage) {
        print("Error: \(message.body)")
        // Show error UI
    }
}
```

<Info>
To try the flow before your backend is ready, you can generate the hash locally with the test code in Step 3.2. Remove it before going to production.
</Info>

***

## Step 6: Verify the Payment

**What you need:** Backend server with PayU Verify Payment API integration, `txnid` from the payment response.

<Warning>
**CRITICAL SECURITY RULE:** Never trust client-side payment responses alone. Always verify the transaction status on your backend server using PayU's Verify Payment API before:
- Marking an order as "paid"
- Delivering digital goods
- Shipping physical products
- Updating user account balances
</Warning>

Use PayU's **Verify Payment API** to confirm transaction status server-side:

📘 [Verify Payment API Documentation](https://docs.payu.in/docs/verify-payment-api/)

### 6.1 Backend Implementation Example

**Endpoint:** `POST /api/payment/verify`

**Request to PayU:**

```bash
curl --location 'https://test.payu.in/merchant/postservice?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=<Your Test Key>' \
--data-urlencode 'command=verify_payment' \
--data-urlencode 'var1=iOS_A1B2C3D4E5' \
--data-urlencode 'hash=<computed_hash>'
```

**Hash Formula for Verify Payment:**

```
key|command|var1|salt
```

**Backend Example (Node.js):**

```javascript
const crypto = require('crypto');
const axios = require('axios');

app.post('/api/payment/verify', async (req, res) => {
    const { txnid } = req.body;
    const key = process.env.PAYU_MERCHANT_KEY;
    const salt = process.env.PAYU_MERCHANT_SALT;
    const command = 'verify_payment';

    // Generate hash: key|command|var1|salt
    const hashString = `${key}|${command}|${txnid}|${salt}`;
    const hash = crypto.createHash('sha512').update(hashString).digest('hex').toLowerCase();

    try {
        const response = await axios.post(
            'https://test.payu.in/merchant/postservice?form=2',
            new URLSearchParams({
                key: key,
                command: command,
                var1: txnid,
                hash: hash
            }),
            { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } }
        );

        const paymentStatus = response.data.transaction_details[txnid].status;

        if (paymentStatus === 'success') {
            // Update order status in database
            // Send confirmation email
            res.json({ verified: true, status: 'success' });
        } else {
            res.json({ verified: true, status: paymentStatus });
        }

    } catch (error) {
        res.status(500).json({ error: 'Verification failed' });
    }
});
```

**Checkpoint:** ✅ Backend verification API created, hash generation implemented, transaction status verified before order fulfillment.

***

## Step 7: Test Your Integration

**What you need:** Test merchant credentials, iOS Simulator or physical device, test payment instruments.

### 7.1 Pre-Integration Testing Checklist

Before making your first test payment, verify:

✅ **Test endpoint configured:** Using `https://test.payu.in/_payment`<br />✅ **Test credentials active:** Using test `key` and `salt` from Dashboard<br />✅ **Backend create-transaction API working:** Returns `key`, `txnid`, and a valid SHA-512 hash<br />✅ **All 10 mandatory parameters included** in `postString`<br />✅ **txnid consistency:** Same `txnid` is used in hash calculation AND POST body<br />✅ **Delegate configured:** `delegate` is set **before** calling `load()`<br />✅ **All three delegate methods implemented:** `payUonSuccess`, `payUonFailure`, `payUonError`<br />✅ **WebView in place:** Outlet connected (or WebView created in code) and fills the screen<br />✅ **ATS:** No `NSAllowsArbitraryLoads`; PayU domains are not blocked by any custom ATS rules<br />✅ **Memory management:** `webViewManager` retained as an instance variable

***

{/* SME-CHECK: Verify ALL test credentials in 7.2–7.5 against PayU's official test credentials before publishing. In particular, 4111111111111111 and 4000000000000002 look like generic test cards rather than PayU-specific ones. */}

### 7.2 Test Credentials — Card Payments

<Accordion title="Test Card Details" icon="fa-credit-card">
  Use the following test cards on the PayU test environment:

  | Card Type                | Card Number        | Expiry Date     | CVV    | Name on Card |
  | ------------------------ | ------------------ | --------------- | ------ | ------------ |
  | **Visa (Success)**       | `4111111111111111` | Any future date | `123`  | Test User    |
  | **Mastercard (Success)** | `5123456789012346` | Any future date | `123`  | Test User    |
  | **Visa (Failure)**       | `4000000000000002` | Any future date | `123`  | Test User    |
  | **Amex (Success)**       | `341111111111111`  | Any future date | `1234` | Test User    |

    <Info>
    For EMI testing, use amount `10,000` or higher with Visa/Mastercard test cards.
    </Info>
</Accordion>

***

### 7.3 Test Credentials — Net Banking

<Accordion title="Net Banking Test Credentials" icon="fa-building-columns">
  Select any bank from the Net Banking list and use these credentials:

  | Field        | Value    |
  | ------------ | -------- |
  | **Username** | `test`   |
  | **Password** | `test`   |
  | **OTP**      | `123456` |

    <Info>
    To simulate a **failure**, enter incorrect credentials or close the payment page during payment.
    </Info>
</Accordion>

***

### 7.4 Test Credentials — UPI

<Accordion title="UPI Test IDs" icon="fa-mobile">
  Use the following test UPI IDs for the **UPI collect** flow (entering a UPI ID on the checkout page):

  | UPI ID         | Transaction Result |
  | -------------- | ------------------ |
  | `success@payu` | Success            |
  | `failure@payu` | Failure            |

    <Warning>
    **UPI intent** (opening a UPI app such as Google Pay, PhonePe, Paytm, or BHIM) cannot be tested on the iOS Simulator, because UPI apps can't be installed there. Test UPI intent on a **physical iOS device** with UPI apps installed. The UPI collect flow with the test IDs above does not require a UPI app.
    </Warning>
</Accordion>

***

### 7.5 Test Credentials — Wallets

<Accordion title="Wallet Test Credentials" icon="fa-wallet">
  For wallet payments (Paytm, PhonePe, Mobikwik), use:

  | Field             | Value        |
  | ----------------- | ------------ |
  | **Mobile Number** | `9876543210` |
  | **OTP**           | `123456`     |
</Accordion>

***

### 7.6 Pre-Launch Testing Checklist

Before switching to production, complete these test scenarios:

✅ **Successful card payment:** Receive `payUonSuccess` callback with valid `mihpayid` in `message.body`<br />✅ **Failed card payment:** Test with failure card, receive `payUonFailure` callback<br />✅ **User-cancelled payment:** Close payment page, verify callback handling<br />✅ **Network timeout:** Disable Wi-Fi mid-payment, verify error handling<br />✅ **Backend verification:** Confirm Verify Payment API returns correct status<br />✅ **Hash mismatch:** Send invalid hash, verify error handling<br />✅ **Empty parameters:** Test with missing mandatory fields<br />✅ **Special characters:** Test `productinfo` with `&`, `+`, `=`, emojis, and Unicode<br />✅ **Multiple payment methods:** Test cards, Net Banking, UPI, wallets<br />✅ **Device rotation:** Verify WebView persists during orientation changes

**Checkpoint:** ✅ All test scenarios passed, delegate callbacks working correctly, backend verification confirmed.

***

## Step 8: Go Live — Production Checklist

**What you need:** Production merchant credentials, backend API updated, App Store compliance verified.

### 8.1 Update to Production Credentials

<Accordion title="Checklist 1: Retrieve Production Credentials" icon="fa-key">
  {/* SME-CHECK: Confirm the Dashboard navigation path. */}
  1. Log in to [PayU Dashboard](https://dashboard.payu.in)
  2. Navigate to **Settings** → **Account & API Keys**
  3. Copy **Production Key** and **Production Salt**
  4. Store them securely in your backend environment variables (never in iOS code)

  ```bash
  # Backend .env file
  PAYU_MERCHANT_KEY=your_production_key
  PAYU_MERCHANT_SALT=your_production_salt
  ```

    <Warning>
    Verify production credentials are **never committed** to version control (Git, Bitbucket, etc.). Add `.env` to `.gitignore`.
    </Warning>
</Accordion>

<Accordion title="Checklist 2: Point to Production Endpoint" icon="fa-globe">
  Update the payment URL in your iOS code:

  ```swift
  // Remove test endpoint
  // let paymentURL = "https://test.payu.in/_payment"

  // Use production endpoint
  let paymentURL = "https://secure.payu.in/_payment"
  ```
</Accordion>

<Accordion title="Checklist 3: Secure Hash Generation" icon="fa-lock">
  ✅ Verify all hash generation happens on backend (no client-side SHA-512)<br />✅ Test hash code from Step 3.2 removed from the app<br />✅ Merchant salt is stored in environment variables, not hardcoded<br />✅ Backend API uses HTTPS only<br />✅ Authentication tokens validated before hash generation<br />✅ Hash formula matches PayU specification exactly (17 positions)
</Accordion>

<Accordion title="Checklist 4: Confirm SURL/FURL Configuration" icon="fa-link">
  The `PayUDelegate` callbacks are triggered by the PayU SDK callback URLs:

  ```swift
  let surl = "https://cbjs.payu.in/sdk/success"
  let furl = "https://cbjs.payu.in/sdk/failure"
  ```

  <Warning>
  If you replace these with your own surl/furl, you **must** follow [Handling Redirect URLs (SURL/FURL) with iOS](https://docs.payu.in/docs/handling-redirect-surlfurl-urls-with-ios). Otherwise, the SDK callbacks may never fire.
  </Warning>

  Whichever URLs you use, your backend should:
  ✅ Log transaction responses<br />✅ Verify payment via Verify Payment API<br />✅ Update order status in database<br />✅ Send confirmation emails/SMS
</Accordion>

<Accordion title="Checklist 5: App Store Compliance" icon="fa-apple">
  Before submitting to App Store:

  ✅ **Privacy Policy URL:** Added to App Store Connect<br />✅ **Terms & Conditions:** Include payment and refund policies<br />✅ **Data Security:** App uses HTTPS for all network calls<br />✅ **No hardcoded credentials:** No payment credentials stored locally on device<br />✅ **PCI-DSS compliance:** Confirmed with PayU integration<br />✅ **User consent:** Payment terms shown before initiating payment
</Accordion>

<Accordion title="Checklist 6: Test Production Flow (TestFlight)" icon="fa-flask">
  Before public release:

  ✅ Deploy app via TestFlight<br />✅ Make a **real payment** using production credentials<br />✅ Verify `payUonSuccess` callback fires correctly<br />✅ Confirm backend receives payment confirmation<br />✅ Check transaction appears in PayU Dashboard → Transactions<br />✅ Verify Verify Payment API returns correct status<br />✅ Test refund flow (if applicable)
</Accordion>

<Accordion title="Checklist 7: Monitoring & Alerts" icon="fa-chart-line">
  Set up production monitoring:

  ✅ **Transaction logging:** All payments logged with timestamps<br />✅ **Error tracking:** Crashlytics/Sentry configured for `payUonError` events<br />✅ **Dashboard monitoring:** Daily checks of PayU Dashboard for disputes<br />✅ **Alert thresholds:** Notifications for payment failure rate > 5%<br />✅ **Webhook backup:** S2S webhooks configured for redundancy
</Accordion>

**Checkpoint:** ✅ Production credentials active, endpoint updated, App Store compliance verified, real payment tested successfully.

***

## Step 9: Troubleshooting

<Accordion title="9.1 WebView Not Loading / Blank Page" icon="fa-browser">
  **Symptoms:** WKWebView shows a blank white page, no payment form loads.

  **Causes & Solutions:**

  1. **No network connectivity:** Confirm the device is online.

  2. **WebView not connected:** Verify the WKWebView outlet is connected (or the WebView is created in code) before calling `load()`.

  3. **Incorrect payment URL:** Verify you're using the correct endpoint:
     - Test: `https://test.payu.in/_payment`
     - Production: `https://secure.payu.in/_payment`

  4. **ATS blocking PayU domains:** Make sure your app's ATS configuration permits the required PayU domains (see Step 1.4). Avoid `NSAllowsArbitraryLoads = YES` unless it is specifically required; prefer configuring only the required domains.

  5. **Invalid POST string:** Enable the web inspector to check for HTTP errors:
     ```swift
     if #available(iOS 16.4, *) {
         webView.isInspectable = true
     }
     ```
     Then use Safari → Develop → \[Your Device] to debug.

  6. **Hash mismatch:** PayU rejects requests with invalid hashes. See 9.3.
</Accordion>

<Accordion title="9.2 Delegate Callbacks Not Firing" icon="fa-bell-slash">
  **Symptoms:** Payment completes but no `payUonSuccess` or `payUonFailure` callback is triggered.

  **Causes & Solutions:**

  1. **Delegate not set:** Ensure you call:
     ```swift
     webViewManager?.delegate = self
     ```
     **before** calling `webViewManager?.load(...)`.

  2. **SDK instance deallocated:** Declare `webViewManager` as an instance variable, not a local variable:
     ```swift
     class PaymentViewController: UIViewController {
         var webViewManager: WebViewSDK? // ✅ Correct
     }
     ```

  3. **Protocol not adopted:** Verify your class conforms to `PayUDelegate` with the correct method signatures:
     ```swift
     extension PaymentViewController: PayUDelegate {
         func payUonSuccess(_ message: WKScriptMessage) { ... }
         func payUonFailure(_ message: WKScriptMessage) { ... }
         func payUonError(_ message: WKScriptMessage) { ... }
     }
     ```

  4. **Custom surl/furl:** If you replaced `https://cbjs.payu.in/sdk/success` / `failure` with your own URLs, follow [Handling Redirect URLs (SURL/FURL) with iOS](https://docs.payu.in/docs/handling-redirect-surlfurl-urls-with-ios).

  5. **UI updates off the main thread:** Make sure any UI updates triggered from network completions run on the main thread:
     ```swift
     DispatchQueue.main.async {
         self.showAlert(title: "Success", message: "Payment completed")
     }
     ```
</Accordion>

<Accordion title="9.3 Hash Generation Errors" icon="fa-hashtag">
  **Symptoms:** Payment fails with "Invalid Hash" or "Authentication Failed" error.

  **Causes & Solutions:**

  1. **Wrong hash formula:** PayU uses 17 positions:
     ```
     key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt
     ```
     Positions 12–16 are always empty, so there are **6 consecutive pipes** after `udf5` (11 between `email` and `salt` when no UDFs are used).

  2. **txnid mismatch:** The `txnid` used in the hash **must be identical** to the one in the POST body. Common mistake:
     ```swift
     // ❌ Wrong: Generating a new ID for the POST body
     let postTxnid = UUID().uuidString

     // ✅ Correct: Generate once (ideally on your backend) and reuse the same value
     let txnid = "iOS" + String(UUID().uuidString.replacingOccurrences(of: "-", with: "").prefix(20))
     // Use this txnid in the hash, then the same value in the POST body
     ```

  3. **Wrong key or salt:** Verify the `key` is correct and the salt matches the merchant environment (test salt with test endpoint, production salt with production endpoint).

  4. **Parameter order changed:** Keep the exact order shown in the formula.

  5. **Case sensitivity:** Hash must be **lowercase** hexadecimal.

  6. **Whitespace/newlines:** No extra spaces or newlines in the hash string:
     ```swift
     // ❌ Wrong
     let hashString = "\(key) | \(txnid) | \(amount)"

     // ✅ Correct
     let hashString = "\(key)|\(txnid)|\(amount)"
     ```

  7. **Empty UDF handling:** Empty UDF fields must be preserved in the hash string as empty strings:
     ```swift
     let udf1 = "" // Not nil or "null"
     ```

  8. **Hashing encoded values:** Compute the hash on the raw values, not on URL-encoded values.
</Accordion>

<Accordion title="9.4 CocoaPods / Build Issues" icon="fa-wrench">
  **Symptoms:** Build fails, module not found, linker errors.

  **Solutions:**

  1. **Clean derived data:**
     ```bash
     rm -rf ~/Library/Developer/Xcode/DerivedData/*
     ```

  2. **Reinstall pods:**
     ```bash
     pod deintegrate
     pod install
     ```

  3. **Verify Podfile:**
     ```ruby
     platform :ios, '13.0'

     target 'YourApp' do
       use_frameworks!
       pod 'PayUIndia-Webview'
     end
     ```

  4. **Open workspace, not project:** After `pod install`, always open `YourApp.xcworkspace`.

  5. **SPM product not linked:** If you installed via Swift Package Manager, confirm the **PayUWebView** product is added to your app target (Target → General → Frameworks, Libraries, and Embedded Content).

  6. **Framework search paths:** In Xcode → Build Settings → Framework Search Paths, make sure `$(inherited)` is present.

  7. **Clean build folder:** Xcode → Product → Clean Build Folder (Cmd+Shift+K), then rebuild.
</Accordion>

**Checkpoint:** ✅ Troubleshooting steps documented, common issues resolved, app is production-ready.

***

