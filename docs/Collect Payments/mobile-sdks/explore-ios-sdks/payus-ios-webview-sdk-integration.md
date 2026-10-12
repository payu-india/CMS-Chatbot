---
title: PayU's iOS WebView SDK Integration
deprecated: false
hidden: true
icon: far fa-mobile-retro
metadata:
  robots: index
---
---
title: PayU WebView SDK for iOS — Integration Guide
category: 65e0e7c3243acd003dea90e3
slug: ios-webview-sdk-integration
---

Integrate PayU's WebView SDK into your iOS app to accept payments via Cards, Net Banking, UPI, and Wallets using a secure, PCI-compliant checkout flow powered by WKWebView.

<Note>
**Prerequisites:**
- Active PayU merchant account ([Sign up here](https://onboarding.payu.in/app/account))
- Merchant Key and Salt from [PayU Dashboard](https://dashboard.payu.in) → Settings → Account & API Keys
- iOS 12.0+ deployment target
- Xcode 12.0 or later
- Enable preferred payment methods on the PayU Dashboard under **Settings** → **Payment Methods**.
</Note>

---

## Quick Steps

<CardGroup columns={3}>

<Card title="1. Set Up Your Environment" icon="gear">
Install PayU WebView SDK via CocoaPods or Swift Package Manager, configure WKWebView outlet, import SDK framework into your project.
</Card>

<Card title="2. Build Payment Parameters" icon="list-check">
Prepare POST parameters: `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `surl`, and `furl` — never store your merchant salt client-side.
</Card>

<Card title="3. Generate Payment Hash" icon="lock">
Use backend API to compute SHA-512 hash using 17-position formula — use single consistent `txnid` across hash generation AND POST body.
</Card>

<Card title="4. Initialize PayU WebView" icon="mobile">
Set delegate, call `load()` with payment URL and `postString`, handle WKWebView navigation.
</Card>

<Card title="5. Handle Payment Callbacks" icon="webhook">
Implement `PayUDelegate` protocol: `payUonSuccess`, `payUonFailure`, `payUonError` — always verify payment on backend before fulfillment.
</Card>

<Card title="6. Verify Payment" icon="shield-check">
Use Verify Payment API to confirm transaction status server-side — never trust client-side responses alone.
</Card>

</CardGroup>

---

## Step 1: Set Up Your Environment

**What you need:** Xcode project, CocoaPods or Swift Package Manager installed, merchant credentials from PayU Dashboard.

Choose one of the following installation methods:

<Accordion title="Option 1: Install via CocoaPods" icon="fa-cube">

### 1.1 Add PayU SDK to Podfile

```ruby
platform :ios, '12.0'
use_frameworks!

target 'YourAppTarget' do
  pod 'PayUWebViewSDK', '~> 1.0'
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

### 1.3 Import the SDK

```swift
import UIKit
import WebKit
import PayUWebView
```

</Accordion>

<Accordion title="Option 2: Install via Swift Package Manager" icon="fa-box">

### 2.1 Add Package Dependency

1. In Xcode, go to **File** → **Add Packages...**
2. Enter the repository URL:
   ```
   https://github.com/payu-intrepos/PayUWebViewSDK-iOS
   ```
3. Select **Up to Next Major Version** with version `1.0.0`
4. Click **Add Package**

### 2.2 Import the SDK

```swift
import UIKit
import WebKit
import PayUWebView
```

</Accordion>

### 1.3 Configure WKWebView in Storyboard

Create an `@IBOutlet` connection to your WKWebView:

```swift
import UIKit
import WebKit
import PayUWebView

class PaymentViewController: UIViewController {
    
    @IBOutlet weak var webView: WKWebView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        configureWebView()
    }
    
    func configureWebView() {
        let config = WKWebViewConfiguration()
        config.websiteDataStore = WKWebsiteDataStore.nonPersistent()
        
        // If creating webView programmatically:
        // webView = WKWebView(frame: view.bounds, configuration: config)
        // view.addSubview(webView)
    }
}
```

<Warning>
**Critical:** Ensure the outlet is properly connected in Interface Builder **before** calling `load()` on the SDK. A nil webView will cause a crash.
</Warning>

<Info>
Using `nonPersistent()` data store ensures cookies and local storage from previous transactions don't interfere with new payments.
</Info>

### 1.4 Configure App Transport Security (ATS)

Add PayU domain exceptions to your `Info.plist`:

```xml
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSExceptionDomains</key>
    <dict>
        <key>payu.in</key>
        <dict>
            <key>NSIncludesSubdomains</key>
            <true/>
            <key>NSTemporaryExceptionAllowsInsecureHTTPLoads</key>
            <true/>
        </dict>
        <key>payumoney.com</key>
        <dict>
            <key>NSIncludesSubdomains</key>
            <true/>
            <key>NSTemporaryExceptionAllowsInsecureHTTPLoads</key>
            <true/>
        </dict>
        <key>secure.payu.in</key>
        <dict>
            <key>NSIncludesSubdomains</key>
            <true/>
            <key>NSTemporaryExceptionAllowsInsecureHTTPLoads</key>
            <true/>
        </dict>
    </dict>
</dict>
```

**Checkpoint:** ✅ SDK installed, WKWebView outlet connected, ATS configured, no build errors.

---

## Step 2: Build Payment Parameters

**What you need:** Transaction details (amount, order ID, customer info), merchant key from Dashboard.

### 2.1 Prepare Mandatory Parameters

<Tabs>
  <Tab title="Request Parameters">

| Parameter | Type & Description | Example |
|-----------|-------------------|---------|
| `<Glossary>key</Glossary>` | String `Mandatory` — Merchant key from PayU Dashboard | `gtKFFx` |
| `<Glossary>txnid</Glossary>` | String `Mandatory` — Unique transaction ID (alphanumeric, max 25 chars). **Must be identical in hash calculation and POST body.** | `iOS_A1B2C3D4E5` |
| `amount` | String `Mandatory` — Transaction amount (decimal format, 2 decimal places) | `100.00` |
| `productinfo` | String `Mandatory` — Product or service description | `iPhone 14` |
| `firstname` | String `Mandatory` — Customer's first name | `John` |
| `email` | String `Mandatory` — Customer's email address | `john@example.com` |
| `phone` | String `Mandatory` — Customer's phone number | `9876543210` |
| `<Glossary>surl</Glossary>` | String `Mandatory` — Success redirect URL. Can use PayU's test URL for development. | `https://cbjs.payu.in/sdk/success` |
| `<Glossary>furl</Glossary>` | String `Mandatory` — Failure redirect URL. Can use PayU's test URL for development. | `https://cbjs.payu.in/sdk/failure` |
| `hash` | String `Mandatory` — `<Glossary>SHA-512</Glossary>` hash of transaction parameters (see Step 3) | `d1e2f3a4b5c6...` |

  </Tab>
  
  <Tab title="Sample Request">

```swift
let key = "gtKFFx"
let txnid = "iOS_" + UUID().uuidString.prefix(10)
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

// Hash will be generated in Step 3
let hash = "" // Fetch from backend API
```

  </Tab>
</Tabs>

### 2.2 Build POST String

Construct the URL-encoded POST body:

```swift
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
    
    let params: [String: String] = [
        "key": key,
        "txnid": txnid,
        "amount": amount,
        "productinfo": productinfo,
        "firstname": firstname,
        "email": email,
        "phone": phone,
        "surl": surl,
        "furl": furl,
        "hash": hash,
        "udf1": udf1,
        "udf2": udf2,
        "udf3": udf3,
        "udf4": udf4,
        "udf5": udf5
    ]
    
    return params.map { key, value in
        let encodedKey = key.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) ?? key
        let encodedValue = value.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) ?? value
        return "\(encodedKey)=\(encodedValue)"
    }.joined(separator: "&")
}
```

<Warning>
**Critical:** All parameter values must be URL-encoded using `addingPercentEncoding(withAllowedCharacters:)`.
</Warning>

### 2.3 Optional Parameters — User Defined Fields (UDF)

PayU supports 5 custom fields (`udf1`–`udf5`) for passing additional metadata:

| Field | Purpose | Example |
|-------|---------|---------|
| `udf1` | User-defined field 1 | `OrderID_12345` |
| `udf2` | User-defined field 2 | `CouponCode_ABC` |
| `udf3` | User-defined field 3 | `CustomerSegment_Premium` |
| `udf4` | User-defined field 4 | `ReferralSource_Mobile` |
| `udf5` | User-defined field 5 | `CampaignID_SUMMER2024` |

<Info>
If not using UDF fields, pass empty strings (`""`) in both the hash calculation and POST body.
</Info>

**Checkpoint:** ✅ All 10 mandatory parameters prepared, POST string builder function implemented, UDF fields configured if needed.

---

## Step 3: Generate Payment Hash

**What you need:** Merchant salt (from Dashboard), backend API endpoint, all payment parameters from Step 2.

<Warning>
**SECURITY CRITICAL:** Hash generation **MUST** be done on your backend server. **NEVER** include your merchant salt in the iOS app source code or binary. Hardcoded salts expose your account to fraud and unauthorized transactions.
</Warning>

### 3.1 Hash Calculation Formula

PayU uses a **17-position pipe-separated formula** to generate the SHA-512 hash:

<Accordion title="Hash Parameter Sequence (17 Positions)" icon="fa-lock">

| Position | Parameter | Value Type | Example |
|----------|-----------|------------|---------|
| 1 | `key` | Merchant key | `gtKFFx` |
| 2 | `txnid` | Transaction ID | `iOS_A1B2C3D4E5` |
| 3 | `amount` | Amount (decimal) | `100.00` |
| 4 | `productinfo` | Product name | `iPhone 14` |
| 5 | `firstname` | First name | `John` |
| 6 | `email` | Email address | `john@example.com` |
| 7 | `udf1` | User-defined field 1 (empty string if unused) | `` |
| 8 | `udf2` | User-defined field 2 | `` |
| 9 | `udf3` | User-defined field 3 | `` |
| 10 | `udf4` | User-defined field 4 | `` |
| 11 | `udf5` | User-defined field 5 | `` |
| 12–16 | (empty) | Always leave empty (5 consecutive pipe characters) | `` |
| 17 | `salt` | Merchant salt from Dashboard | `eCwWELxi` |

**Formula:**
```
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt
```

**Example Hash String:**
```
gtKFFx|iOS_A1B2C3D4E5|100.00|iPhone 14|John|john@example.com|||||||||||eCwWELxi
```

</Accordion>

### Hash Generation Rules

1. **Use pipe (`|`) as separator** between all fields
2. **Empty UDF fields:** If not using `udf1`–`udf5`, leave those positions empty (but keep the pipes)
3. **Five empty positions:** Positions 12–16 are always empty (5 consecutive `|||||`)
4. **Use lowercase hexadecimal:** Convert SHA-512 digest to lowercase hex string

---

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
    
    guard let data = hashString.data(using: .utf8) else {
        return ""
    }
    
    let digest = SHA512.hash(data: data)
    let hashHex = digest.map { String(format: "%02x", $0) }.joined()
    
    return hashHex.lowercased()
}

// TEST USAGE (Development only)
let testHash = generateTestHash(
    key: "gtKFFx",
    txnid: "iOS_A1B2C3D4E5",
    amount: "100.00",
    productinfo: "iPhone 14",
    firstname: "John",
    email: "john@example.com",
    salt: "eCwWELxi" // NEVER hardcode in production
)

print("Test Hash: \(testHash)")
```

**Output:**
```
Test Hash: d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2
```

</Accordion>

---

### 3.3 Production Hash Generation (Backend API)

<Accordion title="Backend Hash Generation (Production)" icon="fa-server">

Create a secure API endpoint (e.g., `POST /api/payment/generate-hash`) on your backend:

**Requirements:**
✅ Accept parameters: `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `udf1`–`udf5`  
✅ Retrieve merchant salt from environment variables (never from request)  
✅ Compute SHA-512 hash using the 17-position formula  
✅ Return hash as JSON: `{ "hash": "<computed_hash>" }`  
✅ Use HTTPS only; validate authentication token before processing

**iOS Client Code:**

```swift
func fetchHashFromBackend(
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
    completion: @escaping (String?) -> Void
) {
    
    guard let url = URL(string: "https://yourbackend.com/api/payment/generate-hash") else {
        completion(nil)
        return
    }
    
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")
    request.setValue("Bearer YOUR_AUTH_TOKEN", forHTTPHeaderField: "Authorization")
    
    let params: [String: Any] = [
        "key": key,
        "txnid": txnid,
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
    
    URLSession.shared.dataTask(with: request) { data, response, error in
        guard let data = data,
              let json = try? JSONSerialization.jsonObject(with: data) as? [String: String],
              let hash = json["hash"] else {
            completion(nil)
            return
        }
        completion(hash)
    }.resume()
}
```

**Backend Example (Node.js):**

```javascript
const crypto = require('crypto');

app.post('/api/payment/generate-hash', (req, res) => {
    const { key, txnid, amount, productinfo, firstname, email, udf1, udf2, udf3, udf4, udf5 } = req.body;
    const salt = process.env.PAYU_MERCHANT_SALT; // Retrieve from environment
    
    const hashString = `${key}|${txnid}|${amount}|${productinfo}|${firstname}|${email}|${udf1||''}|${udf2||''}|${udf3||''}|${udf4||''}|${udf5||''}||||||${salt}`;
    
    const hash = crypto.createHash('sha512').update(hashString).digest('hex').toLowerCase();
    
    res.json({ hash });
});
```

</Accordion>

**Checkpoint:** ✅ Backend API created and tested, iOS client can fetch hash via HTTPS, merchant salt never exposed client-side.

---

## Step 4: Initialize PayU WebView

**What you need:** Payment URL, POST string from Step 2, hash from Step 3, WKWebView outlet configured.

### 4.1 Initialize WebViewManager

```swift
import UIKit
import WebKit
import PayUWebView

class PaymentViewController: UIViewController {
    
    @IBOutlet weak var webView: WKWebView!
    
    // Retain the manager as an instance variable
    var webViewManager: WebViewManager?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        initiatePayment()
    }
    
    func initiatePayment() {
        // Step 1: Prepare parameters
        let key = "gtKFFx"
        let txnid = "iOS_" + UUID().uuidString.prefix(10)
        let amount = "100.00"
        let productinfo = "iPhone 14"
        let firstname = "John"
        let email = "john@example.com"
        let phone = "9876543210"
        let surl = "https://cbjs.payu.in/sdk/success"
        let furl = "https://cbjs.payu.in/sdk/failure"
        
        // Step 2: Fetch hash from backend
        fetchHashFromBackend(
            key: key,
            txnid: txnid,
            amount: amount,
            productinfo: productinfo,
            firstname: firstname,
            email: email
        ) { [weak self] hash in
            guard let self = self, let hash = hash else {
                print("Failed to fetch hash")
                return
            }
            
            // Step 3: Build POST string
            let postString = self.buildPostString(
                key: key,
                txnid: txnid,
                amount: amount,
                productinfo: productinfo,
                firstname: firstname,
                email: email,
                phone: phone,
                surl: surl,
                furl: furl,
                hash: hash
            )
            
            // Step 4: Initialize PayU WebView
            DispatchQueue.main.async {
                self.loadPayUWebView(postString: postString)
            }
        }
    }
    
    func loadPayUWebView(postString: String) {
        // Test endpoint
        let paymentURL = "https://test.payu.in/_payment"
        
        // Production endpoint (use after testing):
        // let paymentURL = "https://secure.payu.in/_payment"
        
        webViewManager = WebViewManager(webView: webView)
        webViewManager?.delegate = self
        webViewManager?.load(urlString: paymentURL, postString: postString)
    }
}
```

<Warning>
**Memory Management:** Do not declare `webViewManager` as a local variable inside a function. If the manager is deallocated before payment completes, delegate callbacks will not fire.
</Warning>

### 4.2 Payment Environment URLs

| Environment | URL |
|-------------|-----|
| **Test** | `https://test.payu.in/_payment` |
| **Production** | `https://secure.payu.in/_payment` |

<Info>
Always use the **test endpoint** during development and testing. Switch to the **production endpoint** only after completing all test scenarios in Step 7.
</Info>

### 4.3 Load the Payment Page

```swift
func loadPayUWebView(postString: String) {
    let paymentURL = "https://test.payu.in/_payment"
    
    webViewManager = WebViewManager(webView: webView)
    webViewManager?.delegate = self
    webViewManager?.load(urlString: paymentURL, postString: postString)
}
```

<Warning>
Always set `delegate` **before** calling `load()`.
</Warning>

**Checkpoint:** ✅ WebViewManager initialized, delegate assigned, payment page loads in WKWebView.

---

## Step 5: Handle Payment Callbacks

**What you need:** `PayUDelegate` protocol implemented, backend API for payment verification.

<Accordion title="Step 5.1: Implement PayUDelegate Protocol" icon="fa-code">

```swift
extension PaymentViewController: PayUDelegate {
    
    func payUonSuccess(_ response: [AnyHashable : Any]) {
        print("✅ Payment Success Response: \(response)")
        
        guard let txnid = response["txnid"] as? String,
              let mihpayid = response["mihpayid"] as? String else {
            return
        }
        
        // CRITICAL: Verify payment on backend before fulfillment
        verifyPaymentOnBackend(txnid: txnid, mihpayid: mihpayid)
    }
    
    func payUonFailure(_ response: [AnyHashable : Any]) {
        print("❌ Payment Failure Response: \(response)")
        
        if let errorMessage = response["error_Message"] as? String {
            showAlert(title: "Payment Failed", message: errorMessage)
        }
        
        // Log failure for analytics
        logPaymentFailure(response: response)
    }
    
    func payUonError(_ code: Int32, description errorMessage: String) {
        print("⚠️ SDK Error [\(code)]: \(errorMessage)")
        
        var userMessage = "Payment could not be completed."
        
        if errorMessage.contains("1002") {
            // Error code 1002 - Invalid configuration
            userMessage = "Invalid payment configuration. Please contact support."
        } else if errorMessage.contains("1003") {
            // Error code 1003 - WebView load error
            userMessage = "Payment page failed to load. Please try again."
        } else if errorMessage.contains("1004") {
            // Error code 1004 - Session timeout
            userMessage = "Payment session expired. Please restart payment."
        }
        
        showAlert(title: "Error", message: userMessage)
        logSDKError(code: code, message: errorMessage)
    }
}
```

</Accordion>

<Accordion title="Step 5.2: Handling Payment Success — payUonSuccess" icon="fa-circle-check">

The `payUonSuccess` callback is triggered when the payment gateway returns a success response.

```swift
func payUonSuccess(_ response: [AnyHashable : Any]) {
    print("Payment Success Response: \(response)")
    
    // Extract key parameters
    let txnid = response["txnid"] as? String ?? ""
    let mihpayid = response["mihpayid"] as? String ?? "" // PayU transaction ID
    let status = response["status"] as? String ?? ""
    let amount = response["amount"] as? String ?? ""
    let firstname = response["firstname"] as? String ?? ""
    let email = response["email"] as? String ?? ""
    
    // Display success message
    let message = """
    Payment Successful!
    
    Transaction ID: \(txnid)
    PayU ID: \(mihpayid)
    Amount: ₹\(amount)
    """
    
    showAlert(title: "Success", message: message) {
        // CRITICAL: Always verify on backend before order fulfillment
        self.verifyPaymentOnBackend(txnid: txnid, mihpayid: mihpayid)
    }
}
```

<Warning>
**CRITICAL:** Receiving `payUonSuccess` callback does **not** guarantee the payment actually succeeded. Always verify transaction status on your backend using PayU's Verify Payment API before marking an order as paid or delivering goods/services.
</Warning>

</Accordion>

<Accordion title="Step 5.3: Handling Payment Failure — payUonFailure" icon="fa-circle-xmark">

The `payUonFailure` callback is triggered when payment is declined, cancelled, or fails validation.

```swift
func payUonFailure(_ response: [AnyHashable : Any]) {
    print("Payment Failure Response: \(response)")
    
    let txnid = response["txnid"] as? String ?? ""
    let status = response["status"] as? String ?? ""
    let errorMessage = response["error_Message"] as? String ?? "Payment failed"
    let field = response["field"] as? String ?? ""
    
    var displayMessage = errorMessage
    
    // Handle specific failure scenarios
    if status == "userCancelled" {
        displayMessage = "Payment was cancelled by you."
    } else if status == "failed" && field == "card" {
        displayMessage = "Card payment failed. Please check card details and try again."
    } else if errorMessage.contains("insufficient") {
        displayMessage = "Insufficient balance. Please try a different payment method."
    }
    
    showAlert(title: "Payment Failed", message: displayMessage)
    
    // Log for analytics
    logPaymentFailure(txnid: txnid, status: status, error: errorMessage)
}
```

**Common Failure Scenarios:**
- User cancelled payment
- Insufficient balance
- Card declined by bank
- Invalid CVV or expiry date
- Network timeout during payment

</Accordion>

<Accordion title="Step 5.4: Handling SDK Errors — payUonError" icon="fa-triangle-exclamation">

The `payUonError` callback handles SDK-level errors (configuration, network, WebView failures).

```swift
func payUonError(_ code: Int32, description errorMessage: String) {
    print("SDK Error Code: \(code)")
    print("Error Description: \(errorMessage)")
    
    var userMessage = "An error occurred. Please try again."
    var errorCode = ""
    
    if errorMessage.contains("1002") {
        errorCode = "1002"
        userMessage = "Invalid payment configuration. Please contact support."
    } else if errorMessage.contains("1003") {
        errorCode = "1003"
        userMessage = "Payment page failed to load. Please check your internet connection."
    } else if errorMessage.contains("1004") {
        errorCode = "1004"
        userMessage = "Payment session expired. Please restart the payment."
    } else if errorMessage.contains("network") || errorMessage.contains("timeout") {
        errorCode = "1001"
        userMessage = "Network error. Please check your connection and try again."
    }
    
    showAlert(title: "Error \(errorCode)", message: userMessage)
    
    // Send to crash reporting/analytics
    logSDKError(code: code, message: errorMessage)
}
```

**SDK Error Codes:**

| Code | Meaning | Resolution |
|------|---------|------------|
| `1001` | Network error | Check internet connectivity |
| `1002` | Invalid merchant credentials | Verify key/salt configuration |
| `1003` | WebView load failure | Check ATS settings and endpoint URL |
| `1004` | Payment session timeout | Restart payment flow |

</Accordion>

### 5.5 Helper Functions

```swift
// Display alert with UIAlertController
func showAlert(title: String, message: String, completion: (() -> Void)? = nil) {
    let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)
    alert.addAction(UIAlertAction(title: "OK", style: .default) { _ in
        completion?()
    })
    present(alert, animated: true)
}

// Verify payment on backend
func verifyPaymentOnBackend(txnid: String, mihpayid: String) {
    // Call your backend API to verify payment status using PayU's Verify Payment API
    // See Step 6 for implementation details
}

// Log payment failure
func logPaymentFailure(response: [AnyHashable: Any]) {
    // Send to analytics (Firebase, Mixpanel, etc.)
}

// Log SDK error
func logSDKError(code: Int32, message: String) {
    // Send to crash reporting (Crashlytics, Sentry, etc.)
}
```

### 5.6 Sample Payment Responses

<Accordion title="Success Response JSON" icon="fa-file-code">

```json
{
  "error": "E000",
  "error_Message": "No Error",
  "mihpayid": "403993715527698466",
  "mode": "CC",
  "status": "success",
  "unmappedstatus": "captured",
  "key": "gtKFFx",
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
  "key": "gtKFFx",
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

---

## Step 6: Verify the Payment

**What you need:** Backend server with PayU Verify Payment API integration, `txnid` or `mihpayid` from payment response.

<Warning>
**CRITICAL SECURITY RULE:** Never trust client-side payment responses alone. Always verify the transaction status on your backend server using PayU's Verify Payment API before:
- Marking an order as "paid"
- Delivering digital goods
- Shipping physical products
- Updating user account balances
</Warning>

Use PayU's **Verify Payment API** to confirm transaction status server-side:

📘 **[Verify Payment API Documentation](https://docs.payu.in/docs/verify-payment-api/)**

### 6.1 Backend Implementation Example

**Endpoint:** `POST /api/payment/verify`

**Request to PayU:**

```bash
curl --location 'https://test.payu.in/merchant/postservice?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=gtKFFx' \
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

---

## Step 7: Test Your Integration

**What you need:** Test merchant credentials, iOS Simulator or physical device, test payment instruments.

### 7.1 Pre-Integration Testing Checklist

Before making your first test payment, verify:

✅ **Test endpoint configured:** Using `https://test.payu.in/_payment`  
✅ **Test credentials active:** Using test `key` and `salt` from Dashboard  
✅ **Backend hash API working:** Successfully returns valid SHA-512 hash  
✅ **All 10 mandatory parameters included** in `postString`  
✅ **txnid consistency:** Same `txnid` is used in hash calculation AND POST body  
✅ **Delegate configured:** `PayUDelegate` is set **before** calling `load()`  
✅ **All three delegate methods implemented:** `payUonSuccess`, `payUonFailure`, `payUonError`  
✅ **WebView outlet connected:** No crashes when `load()` is called  
✅ **ATS exceptions added:** PayU domains whitelisted in `Info.plist`  
✅ **Memory management:** `webViewManager` retained as instance variable

---

### 7.2 Test Credentials — Card Payments

<Accordion title="Test Card Details" icon="fa-credit-card">

Use the following test cards on the PayU test environment:

| Card Type | Card Number | Expiry Date | CVV | Name on Card |
|-----------|-------------|-------------|-----|--------------|
| **Visa (Success)** | `4111111111111111` | Any future date | `123` | Test User |
| **Mastercard (Success)** | `5123456789012346` | Any future date | `123` | Test User |
| **Visa (Failure)** | `4000000000000002` | Any future date | `123` | Test User |
| **Amex (Success)** | `341111111111111` | Any future date | `1234` | Test User |

<Info>
For EMI testing, use amount `10,000` or higher with Visa/Mastercard test cards.
</Info>

</Accordion>

---

### 7.3 Test Credentials — Net Banking

<Accordion title="Net Banking Test Credentials" icon="fa-building-columns">

Select any bank from the Net Banking list and use these credentials:

| Field | Value |
|-------|-------|
| **Username** | `test` |
| **Password** | `test` |
| **OTP** | `123456` |

<Info>
To simulate a **failure**, enter incorrect credentials or close the browser window during payment.
</Info>

</Accordion>

---

### 7.4 Test Credentials — UPI

<Accordion title="UPI Test IDs" icon="fa-mobile">

Use the following test UPI IDs:

| UPI ID | Transaction Result |
|--------|-------------------|
| `success@payu` | Success |
| `failure@payu` | Failure |

<Warning>
UPI testing is **not supported on iOS Simulator**. You must test UPI payments on a **physical iOS device** with UPI apps installed (Google Pay, PhonePe, Paytm, BHIM).
</Warning>

</Accordion>

---

### 7.5 Test Credentials — Wallets

<Accordion title="Wallet Test Credentials" icon="fa-wallet">

For wallet payments (Paytm, PhonePe, Mobikwik), use:

| Field | Value |
|-------|-------|
| **Mobile Number** | `9876543210` |
| **OTP** | `123456` |

</Accordion>

---

### 7.6 Pre-Launch Testing Checklist

Before switching to production, complete these test scenarios:

✅ **Successful card payment:** Receive `payUonSuccess` callback with valid `mihpayid`  
✅ **Failed card payment:** Test with failure card, receive `payUonFailure` callback  
✅ **User-cancelled payment:** Close payment page, verify callback handling  
✅ **Network timeout:** Disable Wi-Fi mid-payment, verify `payUonError` handling  
✅ **Backend verification:** Confirm Verify Payment API returns correct status  
✅ **Hash mismatch:** Send invalid hash, verify error handling  
✅ **Empty parameters:** Test with missing mandatory fields  
✅ **Special characters:** Test `productinfo` with emojis/unicode  
✅ **Multiple payment methods:** Test cards, Net Banking, UPI, wallets  
✅ **Device rotation:** Verify WebView persists during orientation changes

**Checkpoint:** ✅ All test scenarios passed, delegate callbacks working correctly, backend verification confirmed.

---

## Step 8: Go Live — Production Checklist

**What you need:** Production merchant credentials, backend API updated, App Store compliance verified.

### 8.1 Update to Production Credentials

<Accordion title="Checklist 1: Retrieve Production Credentials" icon="fa-key">

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

✅ Verify all hash generation happens on backend (no client-side SHA-512)  
✅ Merchant salt is stored in environment variables, not hardcoded  
✅ Backend API uses HTTPS only  
✅ Authentication tokens validated before hash generation  
✅ Hash formula matches PayU specification exactly (17 positions)

</Accordion>

<Accordion title="Checklist 4: Configure Production SURL/FURL" icon="fa-link">

Update success and failure URLs to your backend endpoints:

```swift
// Replace test URLs
// let surl = "https://cbjs.payu.in/sdk/success"
// let furl = "https://cbjs.payu.in/sdk/failure"

// Production URLs
let surl = "https://yourbackend.com/payment/success"
let furl = "https://yourbackend.com/payment/failure"
```

These endpoints should:
✅ Log transaction responses  
✅ Verify payment via Verify Payment API  
✅ Update order status in database  
✅ Send confirmation emails/SMS

</Accordion>

<Accordion title="Checklist 5: App Store Compliance" icon="fa-apple">

Before submitting to App Store:

✅ **Privacy Policy URL:** Added to App Store Connect  
✅ **Terms & Conditions:** Include payment and refund policies  
✅ **Data Security:** App uses HTTPS for all network calls  
✅ **No hardcoded credentials:** No payment credentials stored locally on device  
✅ **PCI-DSS compliance:** Confirmed with PayU integration  
✅ **User consent:** Payment terms shown before initiating payment

</Accordion>

<Accordion title="Checklist 6: Test Production Flow (TestFlight)" icon="fa-flask">

Before public release:

✅ Deploy app via TestFlight  
✅ Make a **real payment** using production credentials  
✅ Verify `payUonSuccess` callback fires correctly  
✅ Confirm backend receives payment confirmation  
✅ Check transaction appears in PayU Dashboard → Transactions  
✅ Verify Verify Payment API returns correct status  
✅ Test refund flow (if applicable)

</Accordion>

<Accordion title="Checklist 7: Monitoring & Alerts" icon="fa-chart-line">

Set up production monitoring:

✅ **Transaction logging:** All payments logged with timestamps  
✅ **Error tracking:** Crashlytics/Sentry configured for `payUonError` events  
✅ **Dashboard monitoring:** Daily checks of PayU Dashboard for disputes  
✅ **Alert thresholds:** Notifications for payment failure rate > 5%  
✅ **Webhook backup:** S2S webhooks configured for redundancy

</Accordion>

**Checkpoint:** ✅ Production credentials active, endpoint updated, App Store compliance verified, real payment tested successfully.

---

## Step 9: Troubleshooting

<Accordion title="9.1 WebView Not Loading / Blank Page" icon="fa-browser">

**Symptoms:** WKWebView shows blank white page, no payment form loads.

**Causes & Solutions:**

1. **ATS not configured:** Add PayU domain exceptions to `Info.plist` (see Step 1.4)

2. **Incorrect payment URL:** Verify you're using the correct endpoint:
   - Test: `https://test.payu.in/_payment`
   - Production: `https://secure.payu.in/_payment`

3. **Invalid POST string:** Enable web inspector to check for HTTP errors:
   ```swift
   if #available(iOS 16.4, *) {
       webView.isInspectable = true
   }
   ```
   Then use Safari → Develop → [Your Device] to debug.

4. **Hash mismatch:** PayU rejects requests with invalid hashes. Verify:
   - Hash uses lowercase hexadecimal
   - All 17 positions in hash formula are correct
   - `txnid` is identical in hash and POST body

</Accordion>

<Accordion title="9.2 Delegate Callbacks Not Firing" icon="fa-bell-slash">

**Symptoms:** Payment completes but no `payUonSuccess` or `payUonFailure` callback is triggered.

**Causes & Solutions:**

1. **Delegate not set:** Ensure you call:
   ```swift
   webViewManager?.delegate = self
   ```
   **before** calling `load()`.

2. **WebViewManager deallocated:** Declare `webViewManager` as an instance variable, not local:
   ```swift
   class PaymentViewController: UIViewController {
       var webViewManager: WebViewManager? // ✅ Correct
   }
   ```

3. **Protocol not adopted:** Verify your class adopts `PayUDelegate`:
   ```swift
   extension PaymentViewController: PayUDelegate { ... }
   ```

4. **Wrong thread:** Callbacks must update UI on main thread:
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
   Note the **5 empty positions** (positions 12-16).

2. **txnid mismatch:** The `txnid` used in hash **must be identical** to the one in POST body. Common mistake:
   ```swift
   // ❌ Wrong: Generating new UUID each time
   let txnid = UUID().uuidString
   
   // ✅ Correct: Use same txnid for hash AND POST
   let txnid = "iOS_" + UUID().uuidString.prefix(10)
   // Store txnid, use in hash, then use same value in POST body
   ```

3. **Case sensitivity:** Hash must be **lowercase**:
   ```swift
   let hash = sha512(hashString).lowercased() // ✅
   ```

4. **Whitespace/newlines:** No extra spaces or newlines in hash string:
   ```swift
   // ❌ Wrong
   let hashString = "\(key) | \(txnid) | \(amount)"
   
   // ✅ Correct
   let hashString = "\(key)|\(txnid)|\(amount)"
   ```

5. **Empty UDF handling:** If not using UDF fields, use empty strings:
   ```swift
   let udf1 = "" // Not nil or "null"
   ```

6. **Environment mismatch:** Use test salt with test endpoint, production salt with production endpoint.

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
   platform :ios, '12.0'
   use_frameworks!
   
   target 'YourApp' do
     pod 'PayUWebViewSDK', '~> 1.0'
   end
   ```

4. **Open workspace, not project:** After `pod install`, always open `YourApp.xcworkspace`.

5. **Framework search paths:** In Xcode → Build Settings → Framework Search Paths, verify:
   ```
   $(inherited)
   ${PODS_CONFIGURATION_BUILD_DIR}/PayUWebViewSDK
   ```

6. **Clean build folder:** Xcode → Product → Clean Build Folder (Cmd+Shift+K), then rebuild.

</Accordion>

**Checkpoint:** ✅ Troubleshooting steps documented, common issues resolved, app is production-ready.

---

## Additional Resources

📘 **[PayU iOS SDK GitHub Repository](https://github.com/payu-intrepos/PayUWebViewSDK-iOS)**  
📘 **[Verify Payment API Documentation](https://docs.payu.in/docs/verify-payment-api/)**  
📘 **[Webhook Integration Guide](https://docs.payu.in/docs/webhooks/)**  
📘 **[EMI Integration](https://docs.payu.in/docs/emi-ios/)**  
📘 **[Offers & Discounts](https://docs.payu.in/docs/offers-ios/)**  
📘 **[Saved Cards (Tokenization)](https://docs.payu.in/docs/tokenization-ios/)**  
📘 **[Split Payments](https://docs.payu.in/docs/split-payment-ios/)**


