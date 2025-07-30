---
title: 3DS 2.0 FlashPay Coupled Flow iOS Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
The PayU 3DS 2.0 SDK with FlashPay provides EMVCo-compliant, native cardholder authentication experience for iOS applications. This comprehensive integration guide covers both decoupled and coupled flow implementations for secure payment processing.

The 3DS 2.0 FlashPay SDK enables:

* **EMVCo Compliance**: Fully compliant with EMVCo 3DS 2.0 specifications
* **Native User Experience**: Seamless in-app authentication with custom UI
* **Dual Flow Support**: Decoupled device details collection and coupled payment flow
* **Advanced Security**: Multi-factor authentication with biometric support
* **Complete Customization**: Full control over UI elements and user experience
* **Comprehensive Error Handling**: Detailed error codes and handling mechanisms

## Integration Solutions

### Decoupled flow

* Collect device details and render custom UI
* Handle authentication challenge separately
* Greater control over user experience
* Custom UI implementation required

### Coupled flow (Complete Transaction)

* End-to-end payment processing through PayU
* Simplified integration with minimal custom UI
* Automatic handling of 3DS challenges
* Recommended for faster implementation

## Prerequisites

Before you begin, ensure you have:

* Xcode 12.0 or later
  * iOS 11.0 or later as deployment target
    * Swift 5.0 or later
      * Valid PayU merchant credentials
        * CocoaPods or Swift Package Manager installed

## Step 1: Install the SDK

### Using CocoaPods

Add the following to your `Podfile`:

```ruby
target 'YourApp' do
  use_frameworks!
  pod 'PayUIndia-3DS2-SDK'
end
```

Then install using the following command:

```bash
pod install
```

### Using Swift Package Manager

#### Via Xcode

1. Open your project in Xcode
   2. Go to **File > Add Package Dependencies**
      3. Enter the repository URL:

```
https://github.com/payu-intrepos/PayU3DS2SDK-iOS
```

4. Select version `1.3.0` or later

#### Via Package.swift

Add the dependency to your `Package.swift`:

```swift
dependencies: [
    .package(
        name: "PayUIndia-3DS2-SDK",
        url: "https://github.com/payu-intrepos/PayU3DS2SDK-iOS",
        from: "1.3.0"
    )
]
```

### Import the SDK

```swift
import PayU3DS2Kit
```

## Step 2: Configure the SDK

Create a comprehensive SDK configuration:

```swift
import PayU3DS2Kit

private func createPayU3DS2Config() -> PayU3DS2Config {
    let config = PayU3DS2Config()
    
    // Environment configuration
    config.isProduction = false // Set to true for production
    
    // Fallback and timeout settings
    config.fallback3DS1 = true
    config.autoSubmit = false
    config.initialiseTimeoutTimer = true
    
    // Biometric authentication
    config.enableMFAViaBiometric = true
    
    // Progress loader customization
    config.setDefaultProgressLoader(enabled: true, color: "#007BFF")
    
    // UI customization
    config.uiCustomisation = createUICustomization()
    
    // Font customization
    config.fontFamilyCustomisation = createFontCustomization()
    
    return config
}
```

### Configuration properties

| Property               | Description                                                                 |
| ---------------------- | --------------------------------------------------------------------------- |
| isProduction           | `Boolean` Set environment (true for production). By default, it is "false". |
| fallback3DS1           | `Boolean`Enable fallback to 3DS 1.0. By default, it is "false".             |
| autoSubmit             | `Boolean`Automatically submit OTP. By default, it is "false".               |
| initialiseTimeoutTimer | `Integer`Enable transaction timeout timer. By default, the value is "5".    |
| enableMFAViaBiometric  | `Boolean`Enable biometric MFA. By default, it is "false".                   |

## Step 3: Customize UI components

### Complete UI customization

```swift
private func createUICustomization() -> PayU3DS2UICustomisation {
    // Button customization
    let buttonCustomisation = PayU3DS2ButtonCustomisation(
        textFontColor: "#FFFFFF",
        textFontSize: 17,
        backgroundColor: "#007BFF",
        cornerRadius: 10,
        resendButtonTextFontColor: "#007BFF",
        resendButtonBackgroundColor: "#F8F9FA"
    )
    
    // Label customization
    let labelCustomisation = PayU3DS2LabelCustomisation(
        textFontColor: "#333333",
        textFontSize: 16,
        headingTextFontColor: "#000000",
        headingTextFontSize: 20
    )
    
    // TextBox customization
    let textBoxCustomisation = PayU3DS2TextBoxCustomisation(
        textFontColor: "#000000",
        textFontSize: 16,
        borderColor: "#CCCCCC",
        borderWidth: 1,
        cornerRadius: 8,
        backgroundColor: "#FFFFFF",
        placeholderTextColor: "#999999"
    )
    
    // Toolbar customization
    let toolbarCustomisation = PayU3DS2ToolbarCustomisation(
        backgroundColor: "#007BFF",
        buttonText: "Cancel",
        headerText: "Secure Authentication",
        textFontColor: "#FFFFFF",
        textFontSize: 18
    )
    
    return PayU3DS2UICustomisation(
        buttonCustomisation: buttonCustomisation,
        labelCustomisation: labelCustomisation,
        textBoxCustomisation: textBoxCustomisation,
        toolbarCustomisation: toolbarCustomisation
    )
}
```

### Font family customization

```swift
private func createFontCustomization() -> PayU3DS2FontFamilyCustomisation {
    return PayU3DS2FontFamilyCustomisation(
        headerFontFamily: "Roboto-Medium",
        subTextFontFamily: "Roboto-Regular",
        buttonFontFamily: "Roboto-Medium",
        inputFieldFontFamily: "Roboto-Regular"
    )
}
```

### Content customization

```swift
private func createContentCustomization() -> PayU3DS2ContentCustomisation {
    return PayU3DS2ContentCustomisation(
        merchantName: "Your Store Name",
        submitButtonTitle: "Verify",
        resendButtonTitle: "Resend OTP",
        cancelButtonTitle: "Cancel",
        otpPlaceholder: "Enter OTP",
        timerText: "Resend OTP in %d seconds"
    )
}
```

## Step 4: Initialize payment

### Basic payment implementation

```swift
class PaymentViewController: UIViewController {
    
    private let config = createPayU3DS2Config()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupPaymentFlow()
    }
    
    private func setupPaymentFlow() {
        let paymentParams = createPaymentParameters()
        
        PayU3DS2.initiatePayment(
            vc: self,
            config: config,
            paymentParams: paymentParams,
            delegate: self
        )
    }
    
    private func createPaymentParameters() -> PayU3DS2PaymentParam {
        let paymentParam = PayU3DS2PaymentParam(
            key: "YOUR_MERCHANT_KEY",
            transactionId: "TXN_\(Date().timeIntervalSince1970)",
            amount: "100.00",
            productInfo: "Test Product",
            firstName: "John",
            email: "john@example.com",
            phone: "9876543210",
            surl: "https://example.com/success",
            furl: "https://example.com/failure"
        )
        
        // Add card details
        paymentParam.cardNumber = "4111111111111111"
        paymentParam.expiryMonth = "12"
        paymentParam.expiryYear = "2025"
        paymentParam.cvv = "123"
        paymentParam.nameOnCard = "JOHN DOE"
        
        // Optional parameters
        paymentParam.udf1 = "User Defined Field 1"
        paymentParam.udf2 = "User Defined Field 2"
        paymentParam.udf3 = "User Defined Field 3"
        paymentParam.udf4 = "User Defined Field 4"
        paymentParam.udf5 = "User Defined Field 5"
        
        return paymentParam
    }
}
```

### Payment parameters

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key
        `mandatory`
      </td>

      <td>
        `String` Merchant key provided by PayU
      </td>
    </tr>

    <tr>
      <td>
        transactionId
        `mandatory`
      </td>

      <td>
        `String`Unique transaction identifier
      </td>
    </tr>

    <tr>
      <td>
        amount
        `mandatory`
      </td>

      <td>
        `String`Transaction amount
      </td>
    </tr>

    <tr>
      <td>
        productInfo
        `mandatory`
      </td>

      <td>
        `String`Product description
      </td>
    </tr>

    <tr>
      <td>
        firstName
        `mandatory`
      </td>

      <td>
        `String`Customer first name
      </td>
    </tr>

    <tr>
      <td>
        email
        `mandatory`
      </td>

      <td>
        `String`Customer email address
      </td>
    </tr>

    <tr>
      <td>
        phone
        `mandatory`
      </td>

      <td>
        `String`Customer phone number
      </td>
    </tr>

    <tr>
      <td>
        surl
        `mandatory`
      </td>

      <td>
        `String`Success callback URL
      </td>
    </tr>

    <tr>
      <td>
        furl
        `mandatory`
      </td>

      <td>
        `String`Failure callback URL
      </td>
    </tr>

    <tr>
      <td>
        cardNumber
        `mandatory`
      </td>

      <td>
        `String`Card number for payment
      </td>
    </tr>

    <tr>
      <td>
        expiryMonth
        `mandatory`
      </td>

      <td>
        `String`Card expiry month (MM)
      </td>
    </tr>

    <tr>
      <td>
        expiryYear
        `mandatory`
      </td>

      <td>
        `String`Card expiry year (YYYY)
      </td>
    </tr>

    <tr>
      <td>
        cvv
        `mandatory`
      </td>

      <td>
        `String`Card CVV
      </td>
    </tr>

    <tr>
      <td>
        nameOnCard
        `mandatory`
      </td>

      <td>
        `String`Cardholder name
      </td>
    </tr>
  </tbody>
</Table>

### Optional Parameters

| Parameter    | Description                     |
| ------------ | ------------------------------- |
| udf1 to udf5 | `String`User defined fields     |
| address1     | `String`Customer address        |
| address2     | `String`Additional address info |
| city         | `String`Customer city           |
| state        | `String`Customer state          |
| country      | `String`Customer country        |
| zipcode      | `String`Customer zip code       |

## Step 5: Implement payment delegate

### Complete delegate implementation

```swift
extension PaymentViewController: PayU3DS2Delegate {
    
    func onPaymentSuccess(_ response: [String: Any]) {
        DispatchQueue.main.async { [weak self] in
            print("Payment Success: \(response)")
            self?.handlePaymentSuccess(response)
        }
    }
    
    func onPaymentFailure(_ response: [String: Any]) {
        DispatchQueue.main.async { [weak self] in
            print("Payment Failure: \(response)")
            self?.handlePaymentFailure(response)
        }
    }
    
    func onPaymentCancel(_ isTxnInitiated: Bool) {
        DispatchQueue.main.async { [weak self] in
            print("Payment Cancelled. Transaction Initiated: \(isTxnInitiated)")
            self?.handlePaymentCancellation(isTxnInitiated)
        }
    }
    
    func onError(_ error: [String: Any]) {
        DispatchQueue.main.async { [weak self] in
            print("Payment Error: \(error)")
            self?.handlePaymentError(error)
        }
    }
    
    func generateHash(
        _ data: [String: String],
        onHashGenerated: @escaping ([String: String]) -> Void
    ) {
        // Generate hash on your server (recommended) or locally for testing
        DispatchQueue.global().async {
            let hashValue = self.generateSHA512Hash(from: data)
            let hashData = ["payment_hash": hashValue]
            
            DispatchQueue.main.async {
                onHashGenerated(hashData)
            }
        }
    }
}
```

### Response handling methods

```swift
private func handlePaymentSuccess(_ response: [String: Any]) {
    guard let txnId = response["txnid"] as? String,
          let amount = response["amount"] as? String else {
        showAlert(title: "Success", message: "Payment completed successfully")
        return
    }
    
    let message = "Payment successful!\nTransaction ID: \(txnId)\nAmount: ₹\(amount)"
    showAlert(title: "Payment Success", message: message) { [weak self] in
        self?.navigationController?.popViewController(animated: true)
    }
}

private func handlePaymentFailure(_ response: [String: Any]) {
    let errorMessage = response["error"] as? String ?? "Payment failed"
    showAlert(title: "Payment Failed", message: errorMessage)
}

private func handlePaymentCancellation(_ isTxnInitiated: Bool) {
    let message = isTxnInitiated ? 
        "Payment was cancelled after transaction initiation" : 
        "Payment was cancelled by user"
    showAlert(title: "Payment Cancelled", message: message)
}

private func handlePaymentError(_ error: [String: Any]) {
    let errorCode = error["code"] as? Int ?? -1
    let errorMessage = getErrorMessage(for: errorCode)
    showAlert(title: "Error", message: errorMessage)
}
```

## Step 6: Hash Generation

### Secure hash generation

```swift
import CryptoKit

private func generateSHA512Hash(from data: [String: String]) -> String {
    // Extract required parameters for hash generation
    let key = data["key"] ?? ""
    let txnid = data["txnid"] ?? ""
    let amount = data["amount"] ?? ""
    let productinfo = data["productinfo"] ?? ""
    let firstname = data["firstname"] ?? ""
    let email = data["email"] ?? ""
    
    // Construct hash string according to PayU guidelines
    let hashString = "\(key)|\(txnid)|\(amount)|\(productinfo)|\(firstname)|\(email)|||||||||||"
    
    // Add salt (replace with your actual salt)
    let salt = "YOUR_MERCHANT_SALT"
    let hashInput = hashString + salt
    
    // Generate SHA-512 hash
    let inputData = Data(hashInput.utf8)
    let hashed = SHA512.hash(data: inputData)
    
    return hashed.compactMap { String(format: "%02x", $0) }.joined()
}
```

### Server-Side hash generation (recommended)

```swift
private func generateHashFromServer(
    _ data: [String: String],
    completion: @escaping ([String: String]) -> Void
) {
    guard let url = URL(string: "https://your-server.com/generate-hash") else {
        completion(["payment_hash": ""])
        return
    }
    
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")
    
    do {
        request.httpBody = try JSONSerialization.data(withJSONObject: data)
    } catch {
        completion(["payment_hash": ""])
        return
    }
    
    URLSession.shared.dataTask(with: request) { data, response, error in
        guard let data = data,
              let json = try? JSONSerialization.jsonObject(with: data) as? [String: String],
              let hash = json["hash"] else {
            completion(["payment_hash": ""])
            return
        }
        
        completion(["payment_hash": hash])
    }.resume()
}
```

## Error handling

### Error codes and messages

| Error Code | Description                            | Solution                       |
| ---------- | -------------------------------------- | ------------------------------ |
| `0`        | Success                                | Payment completed successfully |
| `1`        | Invalid parameters                     | Check payment parameters       |
| `2`        | Network error                          | Check internet connection      |
| `3`        | Invalid merchant key                   | Verify merchant credentials    |
| `4`        | Invalid card details                   | Validate card information      |
| `5`        | User cancelled transaction             | Handle cancellation gracefully |
| `6`        | Hash generation failed                 | Check hash generation logic    |
| `7`        | 3DS authentication failed              | Retry authentication           |
| `8`        | Transaction timeout                    | Check network and retry        |
| `9`        | Card scheme not supported              | Use supported card types       |
| `10`       | RBA (Risk Based Authentication) failed | Contact PayU support           |

### Error handling implementation

```swift
private func getErrorMessage(for errorCode: Int) -> String {
    switch errorCode {
    case 0:
        return "Payment completed successfully"
    case 1:
        return "Invalid payment parameters. Please check your input."
    case 2:
        return "Network error. Please check your internet connection and try again."
    case 3:
        return "Invalid merchant configuration. Please contact support."
    case 4:
        return "Invalid card details. Please check your card information."
    case 5:
        return "Transaction was cancelled by user."
    case 6:
        return "Hash generation failed. Please try again."
    case 7:
        return "3DS authentication failed. Please retry."
    case 8:
        return "Transaction timeout. Please try again."
    case 9:
        return "Card scheme not supported. Please use a different card."
    case 10:
        return "Risk-based authentication failed. Please contact support."
    default:
        return "An unknown error occurred. Please try again."
    }
}

private func showAlert(
    title: String,
    message: String,
    completion: (() -> Void)? = nil
) {
    let alertController = UIAlertController(
        title: title,
        message: message,
        preferredStyle: .alert
    )
    
    let okAction = UIAlertAction(title: "OK", style: .default) { _ in
        completion?()
    }
    
    alertController.addAction(okAction)
    present(alertController, animated: true)
}
```

## Advanced features

### Biometric authentication setup

```swift
private func setupBiometricAuthentication() {
    let config = PayU3DS2Config()
    config.enableMFAViaBiometric = true
    
    // Configure biometric options
    config.biometricPromptTitle = "Authenticate Payment"
    config.biometricPromptSubtitle = "Use your biometric to complete the payment"
    config.biometricNegativeButtonText = "Use PIN"
    
    // Set fallback options
    config.biometricFallbackToDeviceCredential = true
}
```

### Custom progress loader

```swift
private func setupCustomProgressLoader() {
    let config = PayU3DS2Config()
    
    // Enable custom progress loader
    config.setDefaultProgressLoader(enabled: true, color: "#007BFF")
    
    // Or implement custom loader
    config.showCustomProgressLoader = false // Disable default
    
    // Implement your custom loader in delegate methods
}
```

### Environment configuration

```swift
private func setupEnvironment() {
    let config = PayU3DS2Config()
    
    #if DEBUG
    config.isProduction = false
    config.enableDebugMode = true
    #else
    config.isProduction = true
    config.enableDebugMode = false
    #endif
}
```

## Complete implementation example

```swift
import UIKit
import PayU3DS2Kit

class FlashPayViewController: UIViewController {
    
    @IBOutlet weak var cardNumberTextField: UITextField!
    @IBOutlet weak var expiryTextField: UITextField!
    @IBOutlet weak var cvvTextField: UITextField!
    @IBOutlet weak var nameTextField: UITextField!
    @IBOutlet weak var amountTextField: UITextField!
    @IBOutlet weak var payButton: UIButton!
    @IBOutlet weak var activityIndicator: UIActivityIndicatorView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
    }
    
    private func setupUI() {
        title = "FlashPay 3DS 2.0"
        
        payButton.layer.cornerRadius = 8
        payButton.backgroundColor = .systemBlue
        payButton.setTitle("Pay Now", for: .normal)
        
        activityIndicator.isHidden = true
        
        // Pre-fill with test data in debug mode
        #if DEBUG
        setupTestData()
        #endif
    }
    
    private func setupTestData() {
        cardNumberTextField.text = "4111111111111111"
        expiryTextField.text = "12/25"
        cvvTextField.text = "123"
        nameTextField.text = "TEST USER"
        amountTextField.text = "100.00"
    }
    
    @IBAction func payButtonTapped(_ sender: UIButton) {
        guard validateInputs() else { return }
        initiatePayment()
    }
    
    private func validateInputs() -> Bool {
        guard let cardNumber = cardNumberTextField.text,
              !cardNumber.isEmpty,
              cardNumber.count >= 13 else {
            showAlert(title: "Invalid Input", message: "Please enter a valid card number")
            return false
        }
        
        guard let expiry = expiryTextField.text,
              !expiry.isEmpty,
              expiry.count >= 5 else {
            showAlert(title: "Invalid Input", message: "Please enter expiry in MM/YY format")
            return false
        }
        
        guard let cvv = cvvTextField.text,
              !cvv.isEmpty,
              cvv.count >= 3 else {
            showAlert(title: "Invalid Input", message: "Please enter a valid CVV")
            return false
        }
        
        guard let name = nameTextField.text,
              !name.isEmpty else {
            showAlert(title: "Invalid Input", message: "Please enter cardholder name")
            return false
        }
        
        guard let amount = amountTextField.text,
              !amount.isEmpty,
              Double(amount) != nil else {
            showAlert(title: "Invalid Input", message: "Please enter a valid amount")
            return false
        }
        
        return true
    }
    
    private func initiatePayment() {
        showLoading(true)
        
        let config = createPayU3DS2Config()
        let paymentParams = createPaymentParameters()
        
        PayU3DS2.initiatePayment(
            vc: self,
            config: config,
            paymentParams: paymentParams,
            delegate: self
        )
    }
    
    private func createPayU3DS2Config() -> PayU3DS2Config {
        let config = PayU3DS2Config()
        
        // Environment
        config.isProduction = false
        
        // Features
        config.fallback3DS1 = true
        config.autoSubmit = false
        config.enableMFAViaBiometric = true
        config.initialiseTimeoutTimer = true
        
        // UI Customization
        config.uiCustomisation = createUICustomization()
        config.fontFamilyCustomisation = createFontCustomization()
        
        // Progress loader
        config.setDefaultProgressLoader(enabled: true, color: "#007BFF")
        
        return config
    }
    
    private func createPaymentParameters() -> PayU3DS2PaymentParam {
        let paymentParam = PayU3DS2PaymentParam(
            key: "YOUR_MERCHANT_KEY",
            transactionId: "FP_TXN_\(Date().timeIntervalSince1970)",
            amount: amountTextField.text!,
            productInfo: "FlashPay Test Product",
            firstName: "Test",
            email: "test@example.com",
            phone: "9876543210",
            surl: "https://example.com/success",
            furl: "https://example.com/failure"
        )
        
        // Card details
        paymentParam.cardNumber = cardNumberTextField.text!.replacingOccurrences(of: " ", with: "")
        
        let expiryComponents = expiryTextField.text!.components(separatedBy: "/")
        paymentParam.expiryMonth = expiryComponents[0]
        paymentParam.expiryYear = "20\(expiryComponents[1])"
        
        paymentParam.cvv = cvvTextField.text!
        paymentParam.nameOnCard = nameTextField.text!.uppercased()
        
        return paymentParam
    }
    
    private func showLoading(_ show: Bool) {
        DispatchQueue.main.async { [weak self] in
            self?.activityIndicator.isHidden = !show
            self?.payButton.isEnabled = !show
            
            if show {
                self?.activityIndicator.startAnimating()
            } else {
                self?.activityIndicator.stopAnimating()
            }
        }
    }
}

// MARK: - PayU3DS2Delegate
extension FlashPayViewController: PayU3DS2Delegate {
    
    func onPaymentSuccess(_ response: [String: Any]) {
        showLoading(false)
        
        DispatchQueue.main.async { [weak self] in
            let txnId = response["txnid"] as? String ?? "N/A"
            let amount = response["amount"] as? String ?? "N/A"
            let message = "Payment Successful!\n\nTransaction ID: \(txnId)\nAmount: ₹\(amount)"
            
            self?.showAlert(title: "Success", message: message) {
                self?.navigationController?.popViewController(animated: true)
            }
        }
    }
    
    func onPaymentFailure(_ response: [String: Any]) {
        showLoading(false)
        
        DispatchQueue.main.async { [weak self] in
            let errorMsg = response["error"] as? String ?? "Payment failed"
            self?.showAlert(title: "Payment Failed", message: errorMsg)
        }
    }
    
    func onPaymentCancel(_ isTxnInitiated: Bool) {
        showLoading(false)
        
        DispatchQueue.main.async { [weak self] in
            let message = isTxnInitiated ? 
                "Payment cancelled after transaction initiation" : 
                "Payment cancelled by user"
            self?.showAlert(title: "Cancelled", message: message)
        }
    }
    
    func onError(_ error: [String: Any]) {
        showLoading(false)
        
        DispatchQueue.main.async { [weak self] in
            let errorCode = error["code"] as? Int ?? -1
            let errorMessage = self?.getErrorMessage(for: errorCode) ?? "Unknown error"
            self?.showAlert(title: "Error", message: errorMessage)
        }
    }
    
    func generateHash(
        _ data: [String: String],
        onHashGenerated: @escaping ([String: String]) -> Void
    ) {
        // Generate hash (preferably on server)
        DispatchQueue.global().async { [weak self] in
            let hash = self?.generateSHA512Hash(from: data) ?? ""
            
            DispatchQueue.main.async {
                onHashGenerated(["payment_hash": hash])
            }
        }
    }
}
```