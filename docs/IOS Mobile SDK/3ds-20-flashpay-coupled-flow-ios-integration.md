---
title: 3DS 2.0 FlashPay Coupled Flow iOS Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
The PayU 3DS 2.0 SDK provides EMVCO-compliant, native cardholder authentication experience for iOS applications. This integration guide covers the complete setup process for implementing secure 3DS 2.0 authentication in your iOS app.

The 3DS 2.0 SDK enables:

* **EMVCO Compliance**: Fully compliant with EMVCo 3DS specifications
* **Native Authentication**: Seamless in-app authentication experience
* **Biometric Support**: Enhanced security with device biometrics
* **UI Customization**: Complete control over authentication interface
* **Challenge Flow Management**: Comprehensive handling of 3DS challenges

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

Then run:

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

## Step 2: Initialize the SDK

Initialize the SDK with your merchant configuration:

```swift
import PayU3DS2Kit

class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        initializePayU3DS2SDK()
    }
    
    private func initializePayU3DS2SDK() {
        let config = PayU3DS2Config()
        
        PayU3DS2.initialise(
            key: "YOUR_MERCHANT_KEY",
            requestId: "UNIQUE_REQUEST_ID_\(Date().timeIntervalSince1970)",
            config: config
        ) { [weak self] response in
            DispatchQueue.main.async {
                self?.handleInitializationResponse(response)
            }
        }
    }
    
    private func handleInitializationResponse(_ response: PayU3DS2Response) {
        switch response.status {
        case .success:
            print("SDK initialized successfully")
            // Proceed with device details collection
            collectDeviceDetails()
        case .failure:
            print("SDK initialization failed: \(response.error?.localizedDescription ?? "Unknown error")")
        }
    }
}
```

### Initialization parameters

| Parameter   | Type           | Description                       | Required |
| ----------- | -------------- | --------------------------------- | -------- |
| `key`       | String         | Merchant key provided by PayU     | ✅        |
| `requestId` | String         | Unique identifier for the request | ✅        |
| `config`    | PayU3DS2Config | SDK configuration object          | ✅        |

## Step 3: Configure the SDK

Customize the SDK behavior using `PayU3DS2Config`:

```swift
private func createSDKConfig() -> PayU3DS2Config {
    let config = PayU3DS2Config()
    
    // Environment configuration
    config.isProduction = false // Set to true for production
    
    // UI customization
    config.uiCustomisation = createUICustomization()
    
    // Biometric authentication
    config.enableMFAViaBiometric = true
    
    // Transaction timeout
    config.enableTxnTimeoutTimer = true
    
    // Progress loader
    config.setDefaultProgressLoader(enabled: true, color: "#007BFF")
    
    return config
}

private func createUICustomization() -> PayU3DS2UICustomisation {
    // Button customization
    let buttonCustomisation = PayU3DS2ButtonCustomisation(
        textFontColor: "#FFFFFF",
        textFontSize: 17,
        backgroundColor: "#007BFF",
        cornerRadius: 8
    )
    
    // Label customization
    let labelCustomisation = PayU3DS2LabelCustomisation(
        textFontColor: "#000000",
        textFontSize: 16,
        headingTextFontColor: "#333333",
        headingTextFontSize: 18
    )
    
    // TextBox customization
    let textBoxCustomisation = PayU3DS2TextBoxCustomisation(
        textFontColor: "#000000",
        textFontSize: 16,
        borderColor: "#CCCCCC",
        borderWidth: 1,
        cornerRadius: 4
    )
    
    // Toolbar customization
    let toolbarCustomisation = PayU3DS2ToolbarCustomisation(
        backgroundColor: "#F8F9FA",
        buttonText: "Cancel",
        headerText: "Authentication",
        textFontColor: "#000000"
    )
    
    return PayU3DS2UICustomisation(
        buttonCustomisation: buttonCustomisation,
        labelCustomisation: labelCustomisation,
        textBoxCustomisation: textBoxCustomisation,
        toolbarCustomisation: toolbarCustomisation
    )
}
```

### Configuration options

| Property                | Type                    | Description                     | Default       |
| ----------------------- | ----------------------- | ------------------------------- | ------------- |
| `isProduction`          | Bool                    | Environment setting             | false         |
| `enableMFAViaBiometric` | Bool                    | Enable biometric authentication | false         |
| `enableTxnTimeoutTimer` | Bool                    | Enable transaction timeout      | true          |
| `uiCustomisation`       | PayU3DS2UICustomisation | UI customization settings       | Default theme |

## Step 4: Collect device details

Extract device information required for 3DS authentication:

```swift
private func collectDeviceDetails() {
    let cardData = PayU3DS2CardData(
        scheme: .mastercard, // or .visa, .americanExpress
        protocolVersion: "2.2.0"
    )
    
    let deviceDetails = PayU3DS2.extractDeviceDetails(cardData: cardData)
    
    if let details = deviceDetails {
        print("Device details collected successfully")
        // Send device details to your server for ACS URL retrieval
        sendDeviceDetailsToServer(details)
    } else {
        print("Failed to collect device details")
    }
}

private func sendDeviceDetailsToServer(_ deviceDetails: PayU3DS2DeviceDetails) {
    // Implement your server communication logic here
    // This should include sending device details and receiving challenge parameters
    
    // Example server request structure:
    let requestData = [
        "deviceDetails": deviceDetails.toDictionary(),
        "cardNumber": "4111111111111111",
        "amount": "100.00",
        "currency": "INR",
        "merchantId": "YOUR_MERCHANT_ID"
    ]
    
    // After receiving response from server, initiate challenge
    // initiateChallenge(with: challengeParameters)
}
```

## Step 5: Initiate 3DS challenge

Start the authentication challenge flow:

```swift
private func initiateChallenge(with parameters: PayU3DS2ChallengeParameter) {
    PayU3DS2.initiateChallenge(
        challengeParameter: parameters
    ) { [weak self] response in
        DispatchQueue.main.async {
            self?.handleChallengeResponse(response)
        }
    }
}

private func handleChallengeResponse(_ response: PayU3DS2Response) {
    switch response.status {
    case .success:
        print("Challenge completed successfully")
        handleSuccessfulAuthentication(response)
    case .failure:
        print("Challenge failed: \(response.error?.localizedDescription ?? "Unknown error")")
        handleAuthenticationFailure(response)
    case .cancelled:
        print("Challenge cancelled by user")
        handleAuthenticationCancellation()
    }
}

private func handleSuccessfulAuthentication(_ response: PayU3DS2Response) {
    // Process successful authentication
    // Extract authentication results and proceed with payment
    if let authResult = response.authenticationResult {
        processPayment(with: authResult)
    }
}

private func handleAuthenticationFailure(_ response: PayU3DS2Response) {
    // Handle authentication failure
    let errorMessage = response.error?.localizedDescription ?? "Authentication failed"
    showErrorAlert(message: errorMessage)
}

private func handleAuthenticationCancellation() {
    // Handle user cancellation
    showErrorAlert(message: "Authentication was cancelled by user")
}
```

### Challenge parameters

```swift
struct PayU3DS2ChallengeParameter {
    let acsTransactionId: String
    let acsReferenceNumber: String
    let acsSignedContent: String
    let threeDSServerTransactionId: String
    // Additional parameters as required
}
```

## Step 6: Handle Challenge actions

Manage user interactions during the challenge flow:

```swift
private func handleChallengeAction(_ action: PayU3DS2ChallengeAction) {
    switch action.type {
    case .submit:
        // Handle OTP submission
        handleOTPSubmission(action.data)
    case .resend:
        // Handle OTP resend request
        handleOTPResend()
    case .cancel:
        // Handle cancellation
        handleChallengeCancellation()
    default:
        print("Unknown challenge action: \(action.type)")
    }
}

private func handleOTPSubmission(_ data: [String: Any]) {
    // Process OTP submission
    if let otp = data["otp"] as? String {
        validateOTP(otp)
    }
}

private func handleOTPResend() {
    // Request OTP resend
    PayU3DS2.resendOTP { response in
        DispatchQueue.main.async {
            // Handle resend response
            print("OTP resend status: \(response.status)")
        }
    }
}

private func validateOTP(_ otp: String) {
    PayU3DS2.submitOTP(otp) { [weak self] response in
        DispatchQueue.main.async {
            self?.handleOTPValidationResponse(response)
        }
    }
}
```

## Step 7: Complete payment flow

### Using "Everything Through Us" approach

For a fully managed payment experience:

```swift
private func initiateCompletePayment() {
    let paymentParams = PayU3DS2PaymentParams(
        key: "YOUR_MERCHANT_KEY",
        amount: "100.00",
        txnId: "TXN_\(Date().timeIntervalSince1970)",
        productInfo: "Test Product",
        firstName: "John",
        email: "john@example.com",
        phone: "9876543210",
        surl: "https://example.com/success",
        furl: "https://example.com/failure"
    )
    
    // Add card details
    paymentParams.cardNumber = "4111111111111111"
    paymentParams.expiryMonth = "12"
    paymentParams.expiryYear = "2025"
    paymentParams.cvv = "123"
    paymentParams.nameOnCard = "JOHN DOE"
    
    PayU3DS2.initiatePayment(
        paymentParams: paymentParams,
        config: createSDKConfig()
    ) { [weak self] response in
        DispatchQueue.main.async {
            self?.handlePaymentResponse(response)
        }
    }
}

private func handlePaymentResponse(_ response: PayU3DS2PaymentResponse) {
    switch response.status {
    case .success:
        print("Payment successful: \(response.transactionId ?? "")")
        showSuccessAlert()
    case .failure:
        print("Payment failed: \(response.error?.localizedDescription ?? "")")
        showErrorAlert(message: "Payment failed. Please try again.")
    case .pending:
        print("Payment pending verification")
        showPendingAlert()
    }
}
```

## Step 8: Check Card Compatibility

Check card compatibility with 3DS versions:

```swift
private func checkCardCompatibility(cardNumber: String) {
    let binInfo = PayU3DS2.cardBinInfo(cardNumber: cardNumber)
    
    switch binInfo.threeDSSupport {
    case .version1:
        print("Card supports 3DS 1.0")
        // Handle 3DS 1.0 flow
    case .version2:
        print("Card supports 3DS 2.0")
        // Proceed with 3DS 2.0 flow
    case .notSupported:
        print("Card does not support 3DS")
        // Handle non-3DS flow
    case .unknown:
        print("3DS support unknown")
        // Handle as appropriate
    }
}
```

### BIN Info Response

```swift
struct PayU3DS2BinInfo {
    let cardScheme: PayU3DS2CardScheme
    let threeDSSupport: ThreeDSSupport
    let issuerName: String?
    let cardType: String?
}

enum ThreeDSSupport {
    case version1
    case version2
    case notSupported
    case unknown
}
```

## Step 9: Hash Generation

Implement secure hash generation:

```swift
import CryptoKit

private func generateHash(for parameters: [String: String], salt: String) -> String {
    // Construct hash string based on PayU documentation
    let hashString = constructHashString(parameters)
    let hashInput = hashString + salt
    
    // Generate SHA-512 hash
    let inputData = Data(hashInput.utf8)
    let hashed = SHA512.hash(data: inputData)
    
    return hashed.compactMap { String(format: "%02x", $0) }.joined()
}

private func constructHashString(_ parameters: [String: String]) -> String {
    // Construct hash string according to PayU guidelines
    // Order: key|txnid|amount|productinfo|firstname|email|udf1|udf2|...
    let orderedKeys = ["key", "txnid", "amount", "productinfo", "firstname", "email"]
    
    return orderedKeys.compactMap { parameters[$0] }.joined(separator: "|")
}
```

## Error Handling

### Common Error Codes

| Error Code | Description                | Solution                           |
| ---------- | -------------------------- | ---------------------------------- |
| `100`      | Transaction timeout        | Check network connection and retry |
| `101`      | Invalid merchant key       | Verify merchant credentials        |
| `102`      | Card scheme not supported  | Use supported card types           |
| `103`      | Device not compatible      | Check device requirements          |
| `104`      | Invalid card details       | Validate card information          |
| `105`      | Authentication failed      | Check 3DS configuration            |
| `106`      | User cancelled transaction | Handle cancellation gracefully     |
| `107`      | Network error              | Check connectivity and retry       |

### Error Handling Implementation

```swift
private func handleError(_ error: PayU3DS2Error) {
    let alertController = UIAlertController(
        title: "Error",
        message: getErrorMessage(for: error.code),
        preferredStyle: .alert
    )
    
    alertController.addAction(UIAlertAction(title: "OK", style: .default))
    present(alertController, animated: true)
}

private func getErrorMessage(for errorCode: Int) -> String {
    switch errorCode {
    case 100:
        return "Transaction timeout. Please try again."
    case 101:
        return "Invalid merchant configuration."
    case 102:
        return "Card type not supported."
    case 103:
        return "Device not compatible with 3DS 2.0."
    case 104:
        return "Invalid card details. Please check and try again."
    case 105:
        return "Authentication failed. Please retry."
    case 106:
        return "Transaction was cancelled."
    case 107:
        return "Network error. Please check your connection."
    default:
        return "An unknown error occurred."
    }
}
```

## Complete implementation example

```swift
import UIKit
import PayU3DS2Kit

class PaymentViewController: UIViewController {
    
    @IBOutlet weak var cardNumberTextField: UITextField!
    @IBOutlet weak var expiryTextField: UITextField!
    @IBOutlet weak var cvvTextField: UITextField!
    @IBOutlet weak var payButton: UIButton!
    @IBOutlet weak var activityIndicator: UIActivityIndicatorView!
    
    private var isSDKInitialized = false
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
        initializePayU3DS2()
    }
    
    private func setupUI() {
        payButton.layer.cornerRadius = 8
        payButton.backgroundColor = .systemBlue
        activityIndicator.isHidden = true
    }
    
    private func initializePayU3DS2() {
        showLoading(true)
        
        let config = PayU3DS2Config()
        config.isProduction = false
        config.uiCustomisation = createUICustomization()
        config.enableMFAViaBiometric = true
        
        PayU3DS2.initialise(
            key: "YOUR_MERCHANT_KEY",
            requestId: "REQ_\(Date().timeIntervalSince1970)",
            config: config
        ) { [weak self] response in
            DispatchQueue.main.async {
                self?.showLoading(false)
                self?.handleInitializationResponse(response)
            }
        }
    }
    
    @IBAction func payButtonTapped(_ sender: UIButton) {
        guard isSDKInitialized else {
            showAlert(message: "SDK not initialized. Please wait.")
            return
        }
        
        guard validateInputs() else {
            return
        }
        
        startPaymentFlow()
    }
    
    private func validateInputs() -> Bool {
        guard let cardNumber = cardNumberTextField.text,
              !cardNumber.isEmpty,
              cardNumber.count >= 13 else {
            showAlert(message: "Please enter a valid card number")
            return false
        }
        
        guard let expiry = expiryTextField.text,
              !expiry.isEmpty,
              expiry.count == 5 else {
            showAlert(message: "Please enter expiry in MM/YY format")
            return false
        }
        
        guard let cvv = cvvTextField.text,
              !cvv.isEmpty,
              cvv.count >= 3 else {
            showAlert(message: "Please enter a valid CVV")
            return false
        }
        
        return true
    }
    
    private func startPaymentFlow() {
        showLoading(true)
        
        // First check card compatibility
        let cardNumber = cardNumberTextField.text!
        let binInfo = PayU3DS2.cardBinInfo(cardNumber: cardNumber)
        
        if binInfo.threeDSSupport == .version2 {
            proceed3DS2Flow()
        } else {
            showAlert(message: "Card does not support 3DS 2.0")
            showLoading(false)
        }
    }
    
    private func proceed3DS2Flow() {
        let cardData = PayU3DS2CardData(
            scheme: .mastercard, // Determine from card number
            protocolVersion: "2.2.0"
        )
        
        let deviceDetails = PayU3DS2.extractDeviceDetails(cardData: cardData)
        
        if let details = deviceDetails {
            // In a real implementation, send device details to server
            // and receive challenge parameters
            initiateChallenge()
        } else {
            showAlert(message: "Failed to extract device details")
            showLoading(false)
        }
    }
    
    private func initiateChallenge() {
        // Create challenge parameters (normally received from server)
        let challengeParams = PayU3DS2ChallengeParameter(
            acsTransactionId: "sample_acs_txn_id",
            acsReferenceNumber: "sample_ref_number",
            acsSignedContent: "sample_signed_content",
            threeDSServerTransactionId: "sample_3ds_server_txn_id"
        )
        
        PayU3DS2.initiateChallenge(
            challengeParameter: challengeParams
        ) { [weak self] response in
            DispatchQueue.main.async {
                self?.showLoading(false)
                self?.handleChallengeResponse(response)
            }
        }
    }
    
    private func handleInitializationResponse(_ response: PayU3DS2Response) {
        switch response.status {
        case .success:
            isSDKInitialized = true
            payButton.isEnabled = true
        case .failure:
            showAlert(message: "SDK initialization failed")
        }
    }
    
    private func handleChallengeResponse(_ response: PayU3DS2Response) {
        switch response.status {
        case .success:
            showAlert(message: "Authentication successful!")
        case .failure:
            showAlert(message: "Authentication failed")
        case .cancelled:
            showAlert(message: "Authentication cancelled")
        }
    }
    
    private func createUICustomization() -> PayU3DS2UICustomisation {
        let buttonCustomisation = PayU3DS2ButtonCustomisation(
            textFontColor: "#FFFFFF",
            textFontSize: 16,
            backgroundColor: "#007BFF",
            cornerRadius: 8
        )
        
        let labelCustomisation = PayU3DS2LabelCustomisation(
            textFontColor: "#333333",
            textFontSize: 14
        )
        
        return PayU3DS2UICustomisation(
            buttonCustomisation: buttonCustomisation,
            labelCustomisation: labelCustomisation
        )
    }
    
    private func showLoading(_ show: Bool) {
        activityIndicator.isHidden = !show
        payButton.isEnabled = !show
        
        if show {
            activityIndicator.startAnimating()
        } else {
            activityIndicator.stopAnimating()
        }
    }
    
    private func showAlert(message: String) {
        let alertController = UIAlertController(
            title: "3DS Authentication",
            message: message,
            preferredStyle: .alert
        )
        
        alertController.addAction(UIAlertAction(title: "OK", style: .default))
        present(alertController, animated: true)
    }
}
```