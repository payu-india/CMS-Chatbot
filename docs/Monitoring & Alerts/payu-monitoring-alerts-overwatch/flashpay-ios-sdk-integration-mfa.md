---
title: Flashpay iOS SDK Integration - MFA
deprecated: false
hidden: true
metadata:
  robots: index
---
A comprehensive guide for implementing Multi-Factor Authentication (MFA) functionality in iOS applications using the Tridentity MFA SDK.

## Step 1. SDK Integration

### Prerequisites Setup

Before integrating the TridentityMFA SDK, ensure your development environment meets the following requirements:

<Accordion title="Framework Integration Steps" icon="fa-wrench">
  1. **Add Framework to Project**
     * Drag and drop `TridentityMFASDK.xcframework` into your Xcode project
     * Ensure the framework is properly referenced in your project navigator

  2. **Configure Framework Linking**
     * Select your Xcode project Target
     * Navigate to **General** tab → **Frameworks, Libraries, and Embedded Content**
     * Select the framework and choose **"Embed & Sign"**

  3. **Import SDK Module**
     ```swift
     // Add this import statement to your Swift files
     import PayUTridentityMFAKit
     ```

  4. **Firebase Integration**
     * Integrate Firebase SDK for push notification support
     * Configure your project with Firebase console credentials

  5. **Pod Dependencies**
     Add the following dependencies to your `Podfile`:

     ```ruby
     # Required analytics and crash reporting
     pod 'PayUIndia-Analytics', '~> 4.0'
     pod 'PayUIndia-CrashReporter', '~> 4.0'
     ```

     Then execute:

     ```bash
     pod install
     ```
</Accordion>

***

## Step 2. App Permissions

### Required Permissions Configuration

The SDK requires specific permissions to function properly. **Push notification permission is mandatory** for the enrollment flow.

<Accordion title="Permission Requirements Table" icon="fa-table">
  | Permission Type              | Requirement Level | Purpose                         | Implementation Notes                       |
  | ---------------------------- | ----------------- | ------------------------------- | ------------------------------------------ |
  | **Biometric Authentication** | 🔴 Mandatory      | Transaction authentication      | Required for secure transaction processing |
  | **Push Notifications**       | 🔴 Mandatory      | Registration flow communication | Essential for enrollment completion        |
  | **Network Access**           | 🔴 Mandatory      | API communication               | Required for SDK-server communication      |
  | **Device Security**          | 🔴 Mandatory      | Security validation             | Jailbreak and debugging detection          |
</Accordion>

### Implementation Guide

```swift
// Request biometric permissions in your app initialization
// Ensure push notifications are properly configured
// Validate network connectivity before SDK operations
```

***

## Step 3. SDK Initialization

### AppDelegate Integration

Initialize the SDK early in your application lifecycle to ensure proper functionality.

```swift
// MARK: - SDK Initialization
// Add this code to your AppDelegate's didFinishLaunchingWithOptions method
// This ensures the SDK is ready for use throughout your app session

func application(_ application: UIApplication, 
                didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    
    // Initialize TridentityMFA SDK
    TridentityMFASDKInterface.shared.initializeSDK()
    
    return true
}
```

> ⚠️ **Important:** This method must be called on every app launch to maintain SDK functionality.

***

## Step 4. SDK Configuration

### Client Details and Security Setup

Configure the SDK with your client-specific parameters and security settings before initiating any enrollment flows.

<Accordion title="Configuration Parameters" icon="fa-cogs">

<br />

<HTMLBlock>{`
<table border="1" style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
    <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
    <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <p>clientId<br/>
      <code>mandatory</code></p>
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <code>String</code> Unique client identifier (provided offline)
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      "CLIENT123"
    </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <p>bin<br/>
      <code>mandatory</code></p>
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <code>String</code> Bank Identification Number for card validation
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      "123456"
    </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <p>bankId<br/>
      <code>mandatory</code></p>
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <code>String</code> Unique bank identifier code
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      "BANK001"
    </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <p>customerId<br/>
      <code>conditional</code></p>
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <code>String</code> Required for specific integration flows
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      "CUST789"
    </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <p>themeConfig<br/>
      <code>optional</code></p>
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <code>ThemeModel</code> UI customization object (see ThemeModel section)
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      {"primaryColor": "#FF5733", "buttonStyle": "rounded"}
    </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <p>bindingType<br/>
      <code>conditional</code></p>
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <code>String</code> Skip="01", Mandatory="02", Single="03"
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      "02"
    </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <p>registrationTimeout<br/>
      <code>mandatory</code></p>
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <code>Int</code> Timeout duration for registration (seconds)
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      300
    </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <p>transactionTimeout<br/>
      <code>mandatory</code></p>
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <code>Int</code> Timeout duration for transactions (seconds)
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      120
    </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <p>authType<br/>
      <code>mandatory</code></p>
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <code>String</code> Authentication method (e.g., "Biometric")
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      "Biometric"
    </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <p>environment<br/>
      <code>optional</code></p>
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <code>String</code> "UAT" or "PROD" (default: "UAT")
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      "UAT"
    </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <p>bankLogoUrl<br/>
      <code>optional</code></p>
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      <code>String</code> URL for custom bank logo display
    </td>
    <td style="border: 1px solid #ddd; padding: 8px;">
      "https://example.com/logo.png"
    </td>
  </tr>
</table>
`}</HTMLBlock>

            |
</Accordion>

### Configuration Implementation

```swift
// MARK: - SDK Configuration
// Configure the SDK with client-specific parameters and security settings
// Ensure all mandatory fields are populated before calling this method

func configureSDK() {
    let configurationParameters: [String: Any] = [
        "clientId": "your_client_id_here",           // Provided by integration team
        "bin": "548054",                             // Your bank's BIN number
        "bankId": "8054",                           // Unique bank identifier
        "customerId": "unique_customer_id",         // Customer's unique identifier
        "registrationTimeout": 15,                  // Registration timeout in seconds
        "transactionTimeout": 45,                   // Transaction timeout in seconds
        "authType": "Biometric",                    // Authentication method
        "themeConfig": createCustomTheme(),         // Optional UI customization
        "bindingType": "02",                        // Binding requirement level
        "environment": "UAT",                       // Development environment
        "bankLogoUrl": "https://your-bank-logo.com" // Optional logo URL
    ]
    
    TridentityMFASDKInterface.shared.configureSDK(with: configurationParameters) { response in
        self.handleConfigurationResponse(response)
    }
}

private func handleConfigurationResponse(_ response: [String: Any]) {
    // Handle configuration success or failure
    // See Response Handling section for details
}
```

<Accordion title="Configuration Response Examples" icon="fa-code">
  **✅ Successful Configuration:**

  ```json
  {
      "code": 200,
      "message": "SDK configured successfully",
      "status": "SUCCESS"
  }
  ```

  **❌ Configuration Failure:**

  ```json
  {
      "code": 10,
      "message": "Push notifications are disabled",
      "status": "FAILURE"
  }
  ```
</Accordion>

***

## 👤 5. Customer Registration

### Registration Flow Overview

The registration process involves security validation, device binding, and biometric authentication setup.

```swift
// MARK: - Customer Registration
// Initiate the customer registration process with proper error handling
// The UID parameter is mandatory and must be a valid customer identifier

func initiateCustomerRegistration(customerUID: String, viewController: UIViewController) {
    let registrationParameters: [String: Any] = [
        "uid": customerUID  // Customer's unique identifier (mandatory)
    ]
    
    TridentityMFASDKInterface.shared.initiateRegistration(
        with: registrationParameters,
        in: viewController,
        completionHandler: { [weak self] response in
            self?.handleRegistrationResponse(response)
        }
    )
}
```

<Accordion title="Security Validation Process" icon="fa-shield">
  The registration process includes multiple security checks:

  1. **Device Security Validation**
     * Jailbreak detection
     * Debugging tool detection
     * Reverse engineering protection

  2. **Biometric Authentication Setup**
     * Biometric availability check
     * Biometric data enrollment
     * Authentication validation

  3. **Device Binding Process**
     * Device fingerprinting
     * Secure device registration
     * Binding verification

  > ⚠️ **Security Compliance:** If any security check fails, terminate the enrollment flow immediately for security compliance.
</Accordion>

<Accordion title="Registration Response Examples" icon="fa-mobile">
  **✅ Successful Registration:**

  ```json
  {
      "code": 200,
      "message": "Customer status retrieved",
      "status": "SUCCESS",
      "subParam": {
          "customerId": "ED30A957CE9805E2CD4DF969E10907C8366AEC68ABBF70F043599D51D54EE855",
          "customerStatus": "registration_comm_success",
          "deviceIdentificationId": "89fe8f4a-1cf3-47e4-a66f-ae7ce2760fa8"
      }
  }
  ```

  **❌ Registration Failure:**

  ```json
  {
      "code": 10,
      "message": "Registration failed",
      "status": "FAILURE",
      "reason": "Device security validation failed"
  }
  ```
</Accordion>

***

## 🔍 6. Customer Status Verification

### Status Check Implementation

Verify customer registration status using their unique identifier.

```swift
// MARK: - Customer Status Check
// Retrieve and validate customer registration status
// Use this method to verify enrollment completion before processing transactions

func checkCustomerRegistrationStatus(customerUID: String, biometricChanged: Bool = false) {
    let statusParameters: [String: Any] = [
        "uid": customerUID,              // Customer's unique identifier
        "clientId": "your_client_id"     // Your client identifier
    ]
    
    TridentityMFASDKInterface.shared.checkRegistrationStatus(
        isBiometricChanged: biometricChanged,
        with: statusParameters
    ) { [weak self] response in
        self?.handleStatusResponse(response)
    }
}
```

<Accordion title="Registration Status Types" icon="fa-chart-bar">
  | Status Code       | Status Value                 | Description                         | Next Action                          |
  | ----------------- | ---------------------------- | ----------------------------------- | ------------------------------------ |
  | ✅ **Success**     | `registration_comm_success`  | Registration completed successfully | Proceed with transactions            |
  | 🟡 **Pending L1** | `registration_l1_fail` (206) | Level 1 enrollment pending          | Wait for activation (up to 24 hours) |
  | 🟡 **Pending L2** | `registration_l2_fail` (207) | Level 2 enrollment pending          | Wait for activation (up to 24 hours) |
  | ❌ **Failed**      | `registration_failed`        | Registration process failed         | Re-initiate registration             |
</Accordion>

***

## 🎛️ 7. SDK Interface Protocol

### Protocol Implementation

Implement the SDK protocol to handle callbacks and status updates.

```swift
// MARK: - SDK Protocol Implementation
// Adopt TridentityMFASDKProtocol to receive SDK status updates and handle responses
// This protocol is essential for proper SDK integration and error handling

extension YourViewController: TridentityMFASDKProtocol {
    
    func sdkStatusUpdate(data: [String: Any]) {
        // Parse response data and handle different status codes
        guard let statusCode = data["code"] as? Int else {
            print("Invalid response format")
            return
        }
        
        switch statusCode {
        case 200:
            handleSuccessResponse(data)
        case 400:
            handleAPIFailure(data)
        default:
            handleErrorResponse(data, statusCode: statusCode)
        }
    }
    
    private func handleSuccessResponse(_ data: [String: Any]) {
        // Handle successful SDK operations
        // Update UI and proceed with next steps
    }
    
    private func handleAPIFailure(_ data: [String: Any]) {
        // Handle network or API related failures
        // Implement retry logic if appropriate
    }
    
    private func handleErrorResponse(_ data: [String: Any], statusCode: Int) {
        // Handle specific error codes
        // See Error Codes section for detailed handling
    }
}
```

***

## 💳 8. Transaction Processing

### Secure Transaction Flow

Process transactions with biometric authentication and real-time validation.

```swift
// MARK: - Transaction Processing
// Process secure transactions with mandatory parameters and biometric authentication
// Ensure all required parameters are provided before initiating transaction

func processSecureTransaction(transactionID: String, customerUID: String) {
    let transactionParameters: [String: String] = [
        "txnId": transactionID,              // Unique transaction identifier
        "uid": customerUID,                  // Customer's unique identifier
        "clientId": "your_client_id",        // Your client identifier
        "hashKey": "your_hash_key"           // Security hash key
    ]
    
    TridentityMFASDKInterface.shared.processTransaction(
        with: transactionParameters,
        statusDelegate: self
    )
}
```

<Accordion title="Transaction Parameters" icon="fa-table">
  | Parameter  | Requirement  | Description                   | Example              |
  | ---------- | ------------ | ----------------------------- | -------------------- |
  | `txnId`    | 🔴 Mandatory | Unique transaction identifier | "TXN\_123456789"     |
  | `uid`      | 🔴 Mandatory | Customer's unique identifier  | "customer\_uid\_001" |
  | `clientId` | 🔴 Mandatory | Client application identifier | "your\_client\_id"   |
  | `hashKey`  | 🔴 Mandatory | Security validation hash      | "secure\_hash\_key"  |
</Accordion>

<Accordion title="Transaction Response Example" icon="fa-mobile">
  **✅ Successful Transaction:**

  ```json
  {
      "code": 200,
      "message": "Transaction updated successfully",
      "status": "SUCCESS",
      "subParam": {
          "status": "SUCCESS",
          "txnId": "TXN_123456789",
          "timestamp": "2024-01-01T12:00:00Z"
      }
  }
  ```
</Accordion>

***

## 🗑️ 9. Customer De-registration

### User Removal Process

Remove registered customers from the SDK when needed.

```swift
// MARK: - Customer De-registration
// Remove customer registration and clean up associated data
// Use this method when customers need to be removed from the system

func deregisterCustomer(bctIDs: [String]) {
    TridentitySDKInterface.shared.deRegisterUser(
        withBCTIDs: bctIDs,
        statusDelegate: self
    )
}

// MARK: - De-registration Response Handling
extension YourViewController: TridentityMFASDKProtocol {
    func sdkStatusUpdate(data: [String: Any]) {
        guard let statusCode = data["code"] as? Int,
              let dataKey = data["dataKey"] as? String else { return }
        
        if statusCode == 200 && dataKey == "deregistrationData" {
            handleSuccessfulDeregistration(data)
        } else {
            handleDeregistrationError(data)
        }
    }
    
    private func handleSuccessfulDeregistration(_ data: [String: Any]) {
        // Customer successfully deregistered
        // Update local data and UI accordingly
    }
}
```

<Accordion title="De-registration Response" icon="fa-mobile">
  **✅ Successful De-registration:**

  ```json
  {
      "dataKey": "deregistrationData",
      "message": "Device deregistered successfully",
      "status": "SUCCESS",
      "code": 200
  }
  ```
</Accordion>

***

## ⚠️ 10. Error Codes Reference

<Accordion title="Complete Error Codes Table" icon="fa-exclamation-triangle">
  | Error Code | Category      | Description                          | Recommended Action            |
  | ---------- | ------------- | ------------------------------------ | ----------------------------- |
  | **1**      | Security      | Device is jailbroken                 | Block enrollment for security |
  | **2**      | Security      | Debugger is attached                 | Terminate app session         |
  | **3**      | Security      | Device is reverse engineered         | Block SDK operations          |
  | **5**      | Validation    | Invalid mobile number                | Validate input format         |
  | **7**      | Device        | SIM not present or movement detected | Check device status           |
  | **8**      | Network       | Network unavailable                  | Check connectivity            |
  | **9**      | Device        | Flight mode is on                    | Request user to disable       |
  | **10**     | Permissions   | Push notifications are disabled      | Request permission            |
  | **12**     | Registration  | Customer already registered          | Check registration status     |
  | **15**     | Registration  | Customer not registered              | Initiate registration         |
  | **16**     | Validation    | Customer ID mismatch                 | Verify customer data          |
  | **17**     | Validation    | Invalid parameter details            | Validate input parameters     |
  | **20**     | Configuration | SDK not configured                   | Configure SDK first           |
</Accordion>

***

## 🎨 11. UI Theme Customization

### ThemeModel Implementation

Customize the SDK's user interface to match your application's branding.

```swift
// MARK: - Theme Customization
// Create a comprehensive theme configuration to match your app's branding
// This example demonstrates all available customization options

private func createCustomTheme() -> ThemeModel {
    return ThemeModel(
        // UI Component Customization
        uiCustomization: UICustomization(
            processingCircleColor: "#66676b",
            
            // Button Styling Configuration
            buttonCustomization: ButtonCustomization(
                // Primary Button Theme (Main Action Buttons)
                primaryButtonCustomization: ButtonStyleCustomization(
                    disabledBackgroundColor: "#9e9e9d",    // Disabled state background
                    disabledTextColor: "#FFFFFF",          // Disabled state text
                    enabledBackgroundColor: "#F26522",     // Active state background (Orange)
                    enabledTextColor: "#FFFFFF"            // Active state text
                ),
                
                // Secondary Button Theme (Alternative Actions)
                secondaryButtonCustomization: ButtonStyleCustomization(
                    disabledBackgroundColor: "#F26522",    // Disabled state background
                    disabledTextColor: "#FFFFFF",          // Disabled state text
                    enabledBackgroundColor: "#E02020",     // Active state background (Red)
                    enabledTextColor: "#FFFFFF"            // Active state text
                ),
                
                // Typography and Layout
                fontName: "Avenir-Medium",                 // Button font family
                fontSize: 16,                              // Button text size
                cornerRadius: 8                            // Button corner rounding
            ),
            
            // Toolbar Styling Configuration
            toolbarCustomization: ToolbarCustomization(
                backgroundColor: "#F26522",               // Toolbar background color
                textColor: "#FFFFFF",                     // Toolbar text color
                fontName: "Avenir-Medium",                // Toolbar font family
                fontSize: 10                              // Toolbar text size
            ),
            
            // Label and Text Styling
            labelCustomization: LabelCustomization(
                // Main Heading Style
                headingCustomization: TextStyleCustomization(
                    textColor: "#25272C",                 // Heading text color
                    fontName: "Avenir-Heavy",             // Heading font family
                    fontSize: 18                          // Heading text size
                ),
                
                // Sub-heading Style
                subHeadingCustomization: TextStyleCustomization(
                    textColor: "#25272C",                 // Sub-heading text color
                    fontName: "Avenir-Book",              // Sub-heading font family
                    fontSize: 14                          // Sub-heading text size
                )
            )
        ),
        
        // Text Content Customization
        textCustomization: TextCustomization(
            // Processing Screen Configuration
            bottomSheetSimBindingProcessingPopupConfiguration: BottomSheetSimBindingProcessingPopupConfiguration(
                topHeaderText: "Set-up Biometric",
                topSubHeaderText: "Please wait",
                headerTextForContents: "Verifying Details",
                subTextForContents: "This may take a moment.",
                numberVerificationProcessingText: "Please wait while we verify your mobile number...",
                numberVerifiedText: "Mobile number successfully verified.",
                biometricSetupText: "Biometric set-up",
                biometricVerifiedText: "Finalizing your biometric set-up.."
            ),
            
            // Success Screen Configuration
            bottomSheetRegistrationSuccessfulPopupConfiguration: BottomSheetRegistrationSuccessfulPopupConfiguration(
                topHeaderText: "",
                topSubHeaderText: "",
                headerTextForContents: "Congratulations",
                subTextForContents: "Flash Pay is setup now! All future payments can be done via your biometric verification.",
                buttonText: "RETURN TO MERCHANT"
            ),
            
            // Error Screen Configuration
            bottomSheetFailureScreenConfiguration: BottomSheetFailureScreenConfiguration(
                topHeaderText: "Failed!",
                topSubHeaderText: "",
                headerTextForContents: "Could not verify mobile number with Bank",
                subTextForContents: "There was an error verifying your mobile number. Please try in future payments again to enrol for biometric.",
                buttonText: "RETURN TO MERCHANT"
            )
        )
    )
}
```

<Accordion title="Theme Customization Options" icon="fa-palette">
  ### Button Customization

  * **Primary Buttons**: Main action buttons (confirm, proceed, submit)
  * **Secondary Buttons**: Alternative actions (cancel, back, skip)
  * **Disabled States**: Visual feedback for inactive buttons
  * **Typography**: Font family, size, and styling options

  ### Toolbar Customization

  * **Background Colors**: Match your app's primary branding
  * **Text Colors**: Ensure proper contrast and readability
  * **Typography**: Consistent font choices across the interface

  ### Label and Text Styling

  * **Headings**: Main section titles and important information
  * **Sub-headings**: Secondary information and descriptions
  * **Body Text**: General content and instructional text

  ### Screen Configuration

  * **Processing Screens**: Loading and verification states
  * **Success Screens**: Completion confirmations
  * **Error Screens**: Failure states and recovery options
</Accordion>

***

## 📚 Additional Resources

### Best Practices

1. **Security First**: Always validate security checks before proceeding with enrollment
2. **Error Handling**: Implement comprehensive error handling for all SDK operations
3. **User Experience**: Provide clear feedback during biometric setup and transaction processing
4. **Testing**: Test thoroughly in both UAT and production environments
5. **Monitoring**: Implement logging and monitoring for SDK operations

### Support and Documentation

For additional support and detailed API documentation, contact the integration team or refer to the official SDK documentation.

***

_This documentation is maintained by the TridentityMFA development team. Last updated: 2024_
