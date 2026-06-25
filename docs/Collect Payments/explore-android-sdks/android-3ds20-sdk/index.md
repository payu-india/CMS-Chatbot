---
title: Android 3DS 2.0 SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Android 3DS 2.0 SDK
  description: ''
  keywords:
    - PayU 3DS 2.0 SDK integration steps
    - PayU India 3DS 2.0 SDK for Android Integration Steps
    - Android 3DS 2.0 SDK integration Steps
    - 3DS 2.0 SDK integration steps
    - PayU 3DS 2.0 integration guide
    - >-
      How to integrate PayU 3DS 2.0 SDK in Android.Step-by-step PayU 3DS 2.0 SDK
      integration
    - PayU 3DS 2.0 SDK integration for Android apps
    - Detailed guide for PayU 3DS 2.0 SDK integration steps
    - PayU 3DS2.0 SDK integration steps
    - PayU India 3DS2.0 SDK steps
    - Android 3DS2.0 SDK integration
    - 3DS2.0 SDK integration steps
    - PayU 3DS2.0 integration guide
  robots: index
next:
  description: ''
---

---
title: Android 3DS 2.0 SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Android 3DS 2.0 SDK
  description: ''
  keywords:
    - PayU 3DS 2.0 SDK integration steps
    - PayU India 3DS 2.0 SDK for Android Integration Steps
    - Android 3DS 2.0 SDK integration Steps
    - 3DS 2.0 SDK integration steps
    - PayU 3DS 2.0 integration guide
    - >-
      How to integrate PayU 3DS 2.0 SDK in Android.Step-by-step PayU 3DS 2.0 SDK
      integration
    - PayU 3DS 2.0 SDK integration for Android apps
    - Detailed guide for PayU 3DS 2.0 SDK integration steps
    - PayU 3DS2.0 SDK integration steps
    - PayU India 3DS2.0 SDK steps
    - Android 3DS2.0 SDK integration
    - 3DS2.0 SDK integration steps
    - PayU 3DS2.0 integration guide
  robots: index
next:
  description: ''
---
Power native experience on the new 3DS 2.0 protocol for card transactions. Less latent, highly customisable, highest uptime with option to fallback in case of failures. Going forward from October 2023, only through a certified 3DS SDK can a merchant power native experience on app.

<Accordion title="Benefits & features​" icon="fa-code">
  * Power native experiences on cards through our native SDK​
  * Offers bin eligibility api to route transactions through 3DS1 or 3DS2​
  * Loosely coupled. Offers two flows​
  * Everything through payu – (Device Collection + Authentication + Complete Challenge + Authorization​
  * Only Device Collection + Challenge and use any other aggregator for authentication/ authorization​
  * Device Collection  + Authentication + Complete Challenge​
  * Fallback to 3DS 1 available in case of failures in device collection.​
  * Highest uptime through multiple 3DS Server in future.​
  * Compliant EMVCO certified 3DS SDK with more control across the whole customer journey.​

  <Image align="center" border={true} src="https://files.readme.io/5013bc0-Screenshot_2023-10-16_at_11.45.39_AM.png" />
</Accordion>

<Accordion title="Integration" icon="fa-code">
  PayU SDK offers the following methods to integrate with 3DS 2.0:

  * **SDK Integration**:
    Min SDK Version is v21
    Compile SDK Version is v31 or later
  * **Maven Dependency URL**
    Use the following code snippet in your app’s build.gradle file:

  ```
  implementation 'in.payu:threeds-sdk:2.0.2'
  ```

  * Use our SDK for a complete transaction:
    * Collecting device details
    * Invoking an authentication request through our 3DS Server
    * Invoking challenge
    * Completing authorization through PayU
  * Use our SDK for collecting device details and to render challenge screens.
</Accordion>

<Accordion title="Using PayU implementation" icon="fa-code">
  Call the method to initiate payment through us and we will return a success or failure callback post-transaction completion.

  ```kotlin Kotlin
  fun initiatePayment(
          activity: AppCompatActivity,
          config: PayU3DS2Config,
          paymentParams: PaymentParams,
          callback: PayU3DS2PaymentCallback
      )
  ```

  You have to pass the following parameters:

  <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
      <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>activity</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the <code>AppCompatActivity</code> reference.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>config</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the following fields in a JSON format. For more information, refer to <a href="#config-json-fields-description">config JSON Fields Description</a>.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentParams</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Merchants have to create the payment param object and pass it which will contain info such as <code>cardDetails</code>, SI details, etc. For more information, refer to <a href="https://docs.payu.in/docs/integration-steps-android-checkout-pro#step-3-build-the-payment-parameters-mandatory-step">SDK Integration &gt; Build the payment parameters</a>.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>callback</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the fields as a JSON object. For more information, refer to <a href="#callback-json-fields-description">callback JSON Fields Description</a>.</p></td>
    </tr>
  </tbody>
</table>
  `}</HTMLBlock>

  <h4 id="config-json-fields-description">config JSON Fields Description</h4>

  <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
      <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>config.uiCustomisation</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Set UI customization object. For more information, refer to <a href="#gui-customization">GUI Customisation</a>.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>config.isProduction</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Set the environment where you want to test: <code>true</code> for the Production environment; <code>false</code> for the Test environment.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>config.fallback3DS1</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Set the value as <code>true</code> to complete payment on the bank page in case of any failure. By default, the value is <code>false</code>.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>config.autoRead</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Set the value as <code>true</code> to allow auto-read OTP and fill in the OTP field. By default, the value is <code>false</code>.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>config.autoSubmit</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Set the value as <code>true</code> to submit the OTP automatically without any user interaction. By default, the value is <code>false</code>.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>config.authenticateOnly</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Pass this as <code>true</code> if you want to authenticate only using PayU. By default, PayU will authorize.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>config.setDefaultProgressLoader(true, &quot;HexColor&quot;)</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Set to show the default loader instead of the full-page loader by passing <code>true</code>; to change the color of the progress bar, pass a valid hex code.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>config.enableCustomizedOtpUIFlow</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>To customise the UI with your content, pass as <code>true</code>.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>config.enableTxnTimeoutTimer</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Pass as <code>true</code> to show a timer for page timeout.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>config.merchantName</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Pass the merchant name with customised OTP flow (e.g. <code>&quot;merchant name&quot;</code>).</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>config.amount</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Pass the transaction amount with customised OTP flow (e.g. <code>&quot;txn amount&quot;</code>).</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>val acsContentConfig</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>ACSContentConfig()</code></p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>acsContentConfig.otpContent</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>OTP message text (e.g. <code>&quot;OTP has been sent to your registered mobile number&quot;</code>). You can set this value as per your need.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>acsContentConfig.resendButtonTitle</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Resend button title. You can set this value as per your need.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>acsContentConfig.submitButtonTitle</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Submit button title. You can set this value as per your need.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>acsContentConfig.resendInfoContent</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Resend info content. You can set this value as per your need.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>acsContentConfig.maxResendInfoContent</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Max resend info content. You can set this value as per your need.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>config.acsContentConfig</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>acsContentConfig</code></p></td>
    </tr>
  </tbody>
</table>
  `}</HTMLBlock>

  <h4 id="callback-json-fields-description">callback JSON Fields Description</h4>
  <p>This parameter contains the following methods:</p>
  <ul>
    <li><code>fun onPaymentSuccess(successResponse: Any)</code>: It will contain a success response. This will be a JSON Object, parse response as per your need.</li>
    <li><code>fun onPaymentFailure(failureResponse: Any)</code>: It will contain a failure response. This will be a JSON Object, parse response as per your need.</li>
    <li><code>fun onPaymentCancel(isTxnInitiated: Boolean)</code>: It will tell if payment was canceled.</li>
    <li><code>fun onError(errorCode: Int, errorMessage: String)</code>: It will contain failure reason code and reason.</li>
    <li><code>fun generateHash(map: HashMap&lt;String, String&gt;, hashGenerationListener: PayUHashGeneratedListener)</code>: Merchant will get a map with the type of hash and hash string as the value of the map. Refer to <a href="#sample-code-for-callback-generateHash">Sample code for callback - generateHash</a>.</li>
  </ul>

  <Accordion title="Sample code for callback - generateHash" icon="fa-code">
    ```kotlin
    if (map.containsKey("hashString") && map.containsKey("hashName")) {
        val hashData = map["hashString"]
        val hashName = map["hashName"]
        val postSalt = map["postSalt"]
        var newsalt = salt
        
        if (!postSalt.isNullOrEmpty()) {
            newsalt += postSalt
        }
        
        Log.d("TAG", "generateHash: " + hashData)
        Log.d("TAG", "generateHash: " + hashName)
        Log.d("TAG", "generateHash: " + newsalt)
        
        var hash: String? 
        // Do not generate hash from local, it needs to be calculated from server side only.
        // Here, hashString contains hash created from your server side.
        
        if (!TextUtils.isEmpty(hash)) {
            val dataMap = HashMap<String, String>()
            dataMap[hashName!!] = hash!!
            hashGenerationListener.onHashGenerated(dataMap)
        }
    }

    ```
  </Accordion>
</Accordion>

<Accordion title="Decoupled Flow" icon="fa-code">
  <Accordion title="Step 1:Initialise SDK" icon="fa-code">
    Initialization of SDK is required if the merchant is utilizing PayU 3DS 2.0 for Decoupled functionality. For more information on properties, refer to <a href="#gui-customization">GUI customisation</a>.

    ```Text Kotlin
    PayU3DS2.initialise(
     key: String,
     requestId: String,
     activity: AppCompatActivity,
     config: PayU3DS2Config): PayU3DSResponse
    ```

    > 🚧 Callout
    >
    > If auto-read is false, auto-submit will not work whereas auto-read will work in case of auto-submit is false.

    <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
      <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Key</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>The key provided to merchant by PayU.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>RequestId</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Unique request ID for the transaction.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>AppCompatActivity</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Required to initialise SDK.</p></td>
    </tr>
  </tbody>
</table>
    `}</HTMLBlock>

    <Accordion title="GUI customisation" icon="fa-code">
      The following components can be customized:

      * Button
      * Label
      * Toolbar
      * Text box
      * Font
      * GUI
      * The sample code blocks for the above:

      ```kotlin Kotlin
      var buttonCustomisation = ButtonCustomisation.Builder()
                                .setBackgroundColor("colorCode") //HEX CODE
                                .setCornerRadius(5).build() //Integer
      var labelCustomisation = LabelCustomisation.Builder()
                              .setHeadingTextColor("colorCode") //HEX CODE
                              .setHeadingTextFontName(FontName.ROBOTO_REGULAR) 
                              .setHeadingTextFontSize(10) //Integer
                              .setTextColor("colorCode") //HEX CODE
      .setTextFontName(FontName.ROBOTO_REGULAR) 
                              .setTextFontSize(10) //Integer
                              .build()
      var toolbarCustomisation = ToolbarCustomisation.Builder()
                                .setBackgroundColor("colorCode") //HEXCODE
                                .setButtonText("ButtonText") //String
                                .setHeaderText("HeaderText) //String
                                .setTextColor("colorCode") //HEXCODE
                                .setTextFontSize(18) //Integer
      .setTextFontName(FontName.ROBOTO_REGULAR)
                                .build()
      var textBoxCustomisation = TextBoxCustomisation.Builder()
                                .setTextColor("colorCode") //HEXCODE
                                .setBorderColor("colorCode) //HEXCODE
                                .setCornerRadius(5) //Integer
                                .setTextFontSize(5) //Integer
                                .setBorderWidth(5) //Integer
      .setTextFontName(FontName.ROBOTO_REGULAR) 
                                .build()
      val fontFamilyCustomisation = FontFamilyCustomisation.Builder()
                                     .setHeaderFontFamily("Header Font family path") 
                                     .setSubTextFontFamily("Sub text font family path") 
                                     .build()
      var uiCustomisation = UICustomisation.Builder()
                            .setButtonCustomisation(buttonCustomisation)
                            .setToolbarCustomisation(toolbarCustomisation)
                            .setTextBoxCustomisation(textBoxCustomisation)
      .setLabelCustomisation(labelCustomisation)
      .setFontFamilyCustomisation(fontFamilyCustomisation)
                            .build()
      ```
    </Accordion>

    <Accordion title="Supported Font Type Details" icon="fa-code">
      ```kotlin Kotlin
      enum class FontName { 
          ROBOTO_REGULAR, 
          ROBOTO_MEDIUM
      }
      ```
    </Accordion>

    <Accordion title="PayU3DS2Response:" icon="fa-code">
      The response includes the following parameters:

      <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
      <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>status</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter returns the status of the web service call. The status can be any of the following:</p><p>0 - If the web service call succeeded</p><p>1 - If the web service call failed.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>errorMessage</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>The error message with details of what went wrong.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>result</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Success response with details. Refer to the following class (below the table) for the response structure.</p></td>
    </tr>
  </tbody>
</table>
      `}</HTMLBlock>

      The following items are in the response:

      ```kotlin Kotlin
      data class PayU3DS2DeviceWarning(
          val id: String? = null,
          val message: String? = null,
          val severity: DeviceSeverity? = null
      )

      enum class DeviceSeverity {
          LOW,
          MEDIUM,
          HIGH
      }
      ```
    </Accordion>
  </Accordion>

  <Accordion title="Step 2: Device details(PArq)" icon="fa-code">
    To obtain device information to initiate an authentication request:

    ```kotlin Kotlin
    PayU3DS2.extractDeviceDetails(cardScheme: CardScheme): PayU3DS2Response
    ```

    cardScheme expected values:

    * VISA
    * MASTERCARD

    **PayU3DS2Response**: Three items are in the response:

    <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
      <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>status</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter returns the status of the web service call. The status can be any of the following:</p><p>0 - If the web service call succeeded</p><p>1 - If the web service call failed.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>errorMessage</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>The error message with details of what went wrong.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>result</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Success response with details. Refer to the following class (below the table) for the response structure.</p></td>
    </tr>
  </tbody>
</table>
    `}</HTMLBlock>

    ```kotlin Kotlin
    data class PArqResponse(
        val sdkAppID: String,
        val sdkEncData: String,
        val crv: String,
        val kty: String,
        val x: String,
        val y: String,
        val sdkTransID: String,
        val sdkReferenceNumber: String
    )
    ```

    Now, these device details can be used to initiate an authentication request with us or any other aggregator.

    After the authentication request has been initiated and a response has been received, the same is used to initiate a challenge which basically means opening a UI screen to do user authentication.
  </Accordion>

  <Accordion title="Step 3: 3DS 2.0 Challenge Initiation" icon="fa-code">
    Call the following function to start the challenge:

    ```kotlin Kotlin
    PayU3DS2.initiateChallenge(activity: Activity, challengeParameter: ChallengeParameter, listener: PayU3DS2BaseCallback)
    ```

    <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
      <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>activity</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the <code>AppCompatActivity</code> reference.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>challengeParameter</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Create an object of ChallengeParameter class with the following parameters:</p><p>ChallengeParameter(&quot;acsSignedContent&quot;, &quot;acsRefNumber&quot;, &quot;acsTransactionID&quot;, &quot;threeDSServerTransactionID&quot;)</p><p><strong>acsSignedContent</strong>= Send ACS Signed Content received in ARes</p><p><strong>acsRefNumber</strong>= Send ACS Ref Number Content received in ARes</p><p><strong>acsTransactionID</strong>= Send ACS Transaction ID received in ARes</p><p><strong>threeDSServerTransactionID</strong>= Send ThreeDS Server Transaction ID received in ARes</p></td>
    </tr>
  </tbody>
</table>
    `}</HTMLBlock>

    Before invoking this method, generate the authentication request through any aggregator and pass the above-defined challenge parameters to initiate challenges.

    **PayU3DS2BaseCallback**: Callback consists of two methods:

    ```kotlin Kotlin
    fun onSuccess(response: Any) //It will contain success response.
    fun onError(errorCode: Int, errorMessage: String) //It will contain failure reason code and reason.

    //Cast response to String. If value is "Y" that means challenge is successfully executed else it is failed.
    ```
  </Accordion>
</Accordion>

<Accordion title="PaymentParams Parameter Example" icon="fa-code">
  <Accordion title="Basic Payment Parameters" icon="fa-code">
    The PaymentParams object contains key fields required for initiating a payment request with PayU. These parameters are critical for identifying the transaction, the customer, and the product.

    ```kotlin
    var mPaymentParams = PaymentParams()
    mPaymentParams.key = "<Your Key issued by PayU>"  // Merchant key provided by PayU
    mPaymentParams.amount = "<Transaction Amount>"     // The total amount of the transaction
    mPaymentParams.productInfo = "<Product Description>"  // Description of the product being purchased
    mPaymentParams.firstName = "<Customer First Name>"    // Customer's first name
    mPaymentParams.email = "<Customer Email>"             // Customer's email address
    mPaymentParams.txnId = "<Transaction Id>"             // Unique transaction ID for this payment
    mPaymentParams.surl = "<Success URL>"                 // URL to redirect on successful payment
    mPaymentParams.furl = "<Failure URL>"                 // URL to redirect on failed payment
    mPaymentParams.udf1 = "<User Defined Fields>"         // User-defined field 1
    mPaymentParams.udf2 = "<User Defined Fields>"         // User-defined field 2
    mPaymentParams.udf3 = "<User Defined Fields>"         // User-defined field 3
    mPaymentParams.udf4 = "<User Defined Fields>"         // User-defined field 4
    mPaymentParams.udf5 = "<User Defined Fields>"         // User-defined field 5
    ```

    <Accordion title="Credit/Debit Card Payment" icon="fa-code">
      To process payments using a credit or debit card, the following parameters need to be included in the PaymentParams object..

      ```kotlin Kotlin
      mPaymentParams.cardNumber = "<cardNumber>"          // Credit/Debit card number
      mPaymentParams.cardName = "<cardName>"              // Card type (e.g., Visa, MasterCard)
      mPaymentParams.nameOnCard = "<cardholderName>"      // Name of the cardholder
      mPaymentParams.expiryMonth = "<expiryMonth>"        // Card expiry month (MM)
      mPaymentParams.expiryYear = "<expiryYear>"          // Card expiry year (YYYY)
      mPaymentParams.cvv = "<cvv>"                        // CVV code on the back of the card
      ```
    </Accordion>

    <Accordion title="Store Credit/Debit Card" icon="fa-code">
      To store the card for future transactions (such as recurring payments), the StoreCard option should be enabled. This allows the card to be saved securely for later use..

      ```kotlin
      mPaymentParams.setCardNumber(cardNumber);
      mPaymentParams.setCardName(cardName);
      mPaymentParams.setNameOnCard(cardholderName);
      mPaymentParams.setExpiryMonth(expiryMonth);// MM
      mPaymentParams.setExpiryYear(expiryYear);// YYYY
      mPaymentParams.setCvv(cvv);
       
      mPaymentParam.setUserCredentials(userCredentials);
      mPaymentParam.setStoreCard(1);
      ```
    </Accordion>

    <Accordion title="Recurring Payments via Card" icon="fa-code">
      For recurring payments, you need to configure SIParams (Subscription Information). This includes the billing cycle, amount, and other details regarding the recurring payment setup.:

      ```kotlin
      fun getSIDetails(): SIParams {
          var siParams = SIParams()
          siParams.api_version = "7"                       // API version
          siParams.si = "1"                                // Indicates recurring payment
          siParams.isFree_trial = false                    // Free trial flag (if applicable)

          var siParamDetails = SIParamsDetails()
          siParamDetails.billingAmount = "1.0"             // Recurring billing amount
          siParamDetails.billingCurrency = "INR"           // Currency (INR in this example)
          siParamDetails.billingInterval = 1               // Interval between payments (e.g., monthly)
          siParamDetails.billingCycle = BillingCycle.ADHOC // Recurring cycle type
          siParamDetails.paymentStartDate = "2025-09-26"   // Start date of the recurring payments
          siParamDetails.paymentEndDate = "2025-10-26"     // End date of the recurring payments
          
          siParams.si_details = siParamDetails
          return siParams
      }

      mPaymentParams.siParams = getSIDetails() // Add subscription details to the payment parameters
      ```
    </Accordion>
  </Accordion>

  <Accordion title="Card Tokenization" icon="fa-code">
    Tokenization is used to securely store card details without exposing sensitive information. There are two main types of card tokenization:

    <Accordion title="Card Tokenization with PayU" icon="fa-code">
      To make payments using a previously saved card, you need to pass both the network token and the card token..

      ```kotlin
       cardDetails.networkToken = "<networkToken>"
       cardDetails.cardToken = "<cardToken>"
      ```
    </Accordion>

    <Accordion title="Third-Party Card Tokenization" icon="fa-code">
      If the card has been tokenized outside of PayU’s platform (via a third-party service), you need to provide additional tokenization information.

      ```kotlin
       private fun getTokenizedDetails(): TokenizedCardAdditionalParam? {
          var token = TokenizedCardAdditionalParam()
          token.last4Digits = "XXXX"                // Last 4 digits of the card
          token.tavv = "XXXXXXXXXXXXXX"             // Transaction authorization verification value
          token.tokenRefNo = "XXXXXXXXXXXXXX"       // Reference number for tokenized card
          token.trid = "XXXXXXXXXXXXXX"             // Transaction ID for this payment
          return token
      }

      mPaymentParams.expiryMonth = "XX"              // Card expiry month (MM)
      mPaymentParams.expiryYear = "XXXX"             // Card expiry year (YYYY)
      mPaymentParams.cardToken = "XXXXXXXXXXXXXXXXX" // The token representing the saved card
      mPaymentParams.cardTokenType = 1               // Type of tokenization (e.g., 1 = PayU token, 2 = third-party token)

      mPaymentParams.tokenizedCardAdditionalParam = getTokenizedDetails() // Add token details
      ```
    </Accordion>
  </Accordion>

  <Accordion title="EMI" icon="fa-code">
    To process payments using EMI (Equated Monthly Installments), you need to specify the card details along with the bank code for EMI and set the payment gateway (PG) to "EMI"..

    ```kotlin
    mPaymentParams.setCardNumber("5123456789012346")   // Card number used for EMI payment
    mPaymentParams.setNameOnCard("test")               // Name on the card
    mPaymentParams.setExpiryMonth("06")                // Expiry month (MM)
    mPaymentParams.setExpiryYear("2023")               // Expiry year (YYYY)
    mPaymentParams.setCvv("123")                        // CVV of the card
    mPaymentParams.setBankCode("EMI03")                 // Bank code for EMI (e.g., EMI03)
    mPaymentParams.setPg("EMI")                         // Set payment gateway to EMI
    ```
  </Accordion>
</Accordion>

<Accordion title="Start Redirection Flow" icon="fa-code">
  To authenticate the transaction using PayU’s 3DS2 redirection flow, use the startRedirectionFlow function. This method handles the authentication process via the ACS (Access Control Server) template or post data and provides callbacks for success, failure, or errors..

  ```kotlin
  fun startRedirectionFlow(
      activity: Activity,
      params: Map<String, Any>,
      uiCustomisation: UICustomisation,
      callback: PayU3DS2PaymentBaseCallback
  )
  ```

  <Accordion title="Parameters" icon="fa-code">
    <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
      <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><strong>activity</strong></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Pass the current <code>Activity</code> instance where the WebView will be launched.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><strong>params</strong></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>A map containing key-value pairs for configuration. Valid keys include:</p><ul><li><code>APIConstants.ACS_TEMPLATE</code> — Contains the ACS template.</li><li><code>APIConstants.AUTO_READ</code> — Pass <code>true</code> to enable auto-reading of the data.</li><li><code>APIConstants.AUTO_SUBMIT</code> — Pass <code>true</code> to enable auto-submission of the form.</li><li><code>APIConstants.SURL</code> — Success URL to redirect after successful payment.</li><li><code>APIConstants.FURL</code> — Failure URL to redirect after failed payment.</li></ul></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><strong>uiCustomisation</strong></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Customize the bottom sheet UI for the redirection flow. Use the <code>UICustomisation</code> object.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><strong>callback</strong></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Callback interface to receive the payment status: success, failure, or error.</p></td>
    </tr>
  </tbody>
</table>
    `}</HTMLBlock>
  </Accordion>

  <Accordion title="Sample Code" icon="fa-code">
    ```kotlin
    val params = mapOf(
        APIConstants.ACS_TEMPLATE to "<pass acs_templete>",
        APIConstants.AUTO_READ to true,
        APIConstants.AUTO_SUBMIT to true,
        APIConstants.SURL to "<success_url>",
        APIConstants.FURL to "<failure_url>"
    )

    val uiCustomization = UICustomisation()
    // Customize uiCustomization as needed

    startRedirectionFlow(
        activity = this,
        params = params,
        uiCustomisation = uiCustomization,
        callback = object : PayU3DS2PaymentCallback {
            override fun onPaymentSuccess() {
                // Handle success
            }

            override fun onPaymentFailure() {
                // Handle failure
            }

            override fun onError(errorCode: Int, errorMessage: String) {
                // Handle error
            }
    				override fun onPaymentCancel(isTxnInitiated: Boolean) {	
              // Handle erro
            }
    				override fun onPaymentCancel(isTxnInitiated: Boolean) {	
              // Handle erro
            }
    				override fun generateHash(map: HashMap<String, String>,hashGenerationListener: 			 PayUHashGeneratedListener) {
              //// Handle Hash
    				}	
        }
    )
    ```
  </Accordion>
</Accordion>

<Accordion title="Hash Generation" icon="fa-code">
  You will receive a call on the generateHash method of PayU3DS2PaymentCallback.

  In the method parameter, you will receive a dictionary or hashMap, and extract the value of hashString from that. Pass that value to the server, and now the server will append salt at the end and generate sha512 hash over it. The server will give that hash back to your app, and the app will provide that hash to PayU through a callback mechanism.

  In the map, you have to check for the following keys to generate a hash:

  * hashString
  * hashName
  * postSalt

  At the end of that hashString, append your salt and use the SHA-512 algorithm on that final string to generate a hash.

  > 🚧 Callout
  >
  > * If you got postSalt also in the map, first use hash string append salt and then append postSalt value to that string and use SHA-512 algorithm on that final string to generate hash.
  > * There is no need to know the formula for dynamic hashes because PayU SDK gives you the string containing all the required parameters. Your server has to append salt at the end and generate sha512 hash over it.
</Accordion>

<Accordion title="Error codes" icon="fa-code">
  <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;">Code</th>
      <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border: 1px solid #ddd; padding: 8px;"><p>0</p></td><td style="border: 1px solid #ddd; padding: 8px;"><p>Success</p></td></tr>
    <tr><td style="border: 1px solid #ddd; padding: 8px;"><p>1</p></td><td style="border: 1px solid #ddd; padding: 8px;"><p>Fail</p></td></tr>
    <tr><td style="border: 1px solid #ddd; padding: 8px;"><p>3</p></td><td style="border: 1px solid #ddd; padding: 8px;"><p>Challenge timeout</p></td></tr>
    <tr><td style="border: 1px solid #ddd; padding: 8px;"><p>4</p></td><td style="border: 1px solid #ddd; padding: 8px;"><p>Challenge protocol error</p></td></tr>
    <tr><td style="border: 1px solid #ddd; padding: 8px;"><p>5</p></td><td style="border: 1px solid #ddd; padding: 8px;"><p>Challenge cancelled</p></td></tr>
    <tr><td style="border: 1px solid #ddd; padding: 8px;"><p>101</p></td><td style="border: 1px solid #ddd; padding: 8px;"><p>Card bin or card token was empty</p></td></tr>
    <tr><td style="border: 1px solid #ddd; padding: 8px;"><p>102</p></td><td style="border: 1px solid #ddd; padding: 8px;"><p>Merchant key null</p></td></tr>
    <tr><td style="border: 1px solid #ddd; padding: 8px;"><p>103</p></td><td style="border: 1px solid #ddd; padding: 8px;"><p>Amount not in correct format</p></td></tr>
    <tr><td style="border: 1px solid #ddd; padding: 8px;"><p>104</p></td><td style="border: 1px solid #ddd; padding: 8px;"><p>Transaction ID null</p></td></tr>
    <tr><td style="border: 1px solid #ddd; padding: 8px;"><p>105</p></td><td style="border: 1px solid #ddd; padding: 8px;"><p>Hash null</p></td></tr>
    <tr><td style="border: 1px solid #ddd; padding: 8px;"><p>106</p></td><td style="border: 1px solid #ddd; padding: 8px;"><p>Card not supported on 3DS 2.0</p></td></tr>
    <tr><td style="border: 1px solid #ddd; padding: 8px;"><p>107</p></td><td style="border: 1px solid #ddd; padding: 8px;"><p>Card scheme not supported</p></td></tr>
    <tr><td style="border: 1px solid #ddd; padding: 8px;"><p>108</p></td><td style="border: 1px solid #ddd; padding: 8px;"><p>Hash incorrect</p></td></tr>
    <tr><td style="border: 1px solid #ddd; padding: 8px;"><p>500</p></td><td style="border: 1px solid #ddd; padding: 8px;"><p>Something went wrong</p></td></tr>
    <tr><td style="border: 1px solid #ddd; padding: 8px;"><p>504</p></td><td style="border: 1px solid #ddd; padding: 8px;"><p>Gateway timeout</p></td></tr>
  </tbody>
</table>
  `}</HTMLBlock>
</Accordion>

## Sample App

The sample application for integration with 3DS 2.0 SDK sample app :

<a href="https://github.com/payu-intrepos/FlashPay-3ds-Android">https://github.com/payu-intrepos/FlashPay-3ds-Android</a>