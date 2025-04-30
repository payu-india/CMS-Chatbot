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

## Benefits & features​

- Power native experiences on cards through our native SDK​
- Offers bin eligibility api to route transactions through 3DS1 or 3DS2​
- Loosely coupled. Offers two flows​
- Everything through payu – (Device Collection + Authentication + Complete Challenge + Authorization​
- Only Device Collection + Challenge and use any other aggregator for authentication/ authorization​
- Device Collection  + Authentication + Complete Challenge​
- Fallback to 3DS 1 available in case of failures in device collection.​
- Highest uptime through multiple 3DS Server in future.​
- Compliant EMVCO certified 3DS SDK with more control across the whole customer journey.​

<Image
  src="https://files.readme.io/5013bc0-Screenshot_2023-10-16_at_11.45.39_AM.png"
  alt=""
  caption=""
  border={true}
  align="center"
/>


## Integration

PayU SDK offers the following methods to integrate with 3DS 2.0:

- **SDK Integration**:  
  Min SDK Version is v21  
  Compile SDK Version is v31 or later
- **Maven Dependency URL**  
  Please use the following code snippet in your app’s build.gradle file:

```
implementation 'in.payu:threeds-sdk:1.0.27'
```

- Use our SDK for a complete transaction

1. Collecting device details
2. Invoking an authentication request through our 3DS Server
3. Invoking challenge
4. Completing authorization through us

- Use our SDK for collecting device details and to render challenge screens.

## Using PayU implementation

Call the method to initiate payment through us and we will return a success or failure callback post-transaction completion.

```Text Kotlin
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>activity</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the <code>AppCompatActivity</code> reference.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>config</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the following properties:  </p>
<p><strong>config.uiCustomisation</strong> = Set UI customization object. For more information, refer to GUI Customisation  </p>
<p><strong>config.isProduction</strong> = Set environment where you want to test:  </p>
<p><strong>true</strong> for the Production environment  </p>
<p><strong>false</strong> for the Test environment  </p>
<p><strong>config.fallback3DS1</strong> = Set the value as true to complete payment on the bank page in case of any failure. By default, the value is false  </p>
<p>**config.autoRead **= Set the values as true to allow auto-read OTP and fill in the OTP field. By default, the value is false.  </p>
<p><strong>config.autoSubmit</strong> = Set the values as true to submit the OTP automatically without any user interaction. By default, the value is false.  </p>
<p><strong>config.authenticateOnly</strong> = Pass this as true if you want to authenticate only using PayU. By default we will authorize.  </p>
<p><strong>config.setDefaultProgressLoader(true, &quot;HexColor&quot;)</strong>: Set to show default loader instead of full page loader pass true, and to change color of progress bar pass valid hexcode.  </p>
<p>**config.enableCustomizedOtpUIFlow = //To customise UI with your content please pass as true  </p>
<p>**config.enableTxnTimeoutTimer = //pass as true to show timer for page timeout  </p>
<p>**config.merchantName = &quot;merchant name&quot;// pass merchant name  with customised OTP Flow  </p>
<p>**config.amount = &quot;txn amount&quot;// pass transaction amount with customised OTP Flow  </p>
<p>val acsContentConfig = ACSContentConfig()<br>acsContentConfig.otpContent = &quot;OTP has been sent to your registered mobile number&quot;. //you can set this value to as per your need<br>acsContentConfig.resendButtonTitle = //you can set this value to as per your need<br>acsContentConfig.submitButtonTitle = //you can set this value to as per your need<br>acsContentConfig.resendInfoContent = //you can set this value to as per your need<br>acsContentConfig.maxResendInfoContent = //you can set this value to as per your need<br>config.acsContentConfig = acsContentConfig </p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentParams</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Merchants have to create the payment param object and pass it which will contain info such as <code>cardDeatails</code>, SI details, etc. The following code has the parameters. Refer to the following &lt;<code snippet>> below the table.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>callback</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the following methods:  </p>
<p><strong>fun onPaymentSuccess(successResponse: Any)</strong>: It will contain a success response. This will be a JSON Object, parse response as per your need.  </p>
<p><strong>fun onPaymentFailure(failureResponse: Any)</strong>: It will contain a failure response. This will be a JSON Object, parse response as per your need.  </p>
<p><strong>fun onPaymentCancel(isTxnInitiated: Boolean)</strong>: It will tell if payment was canceled.  </p>
<p><strong>fun onError(errorCode: Int, errorMessage: String)</strong>: It will contain failure reason code and reason.  </p>
<p><strong>fun generateHash(map: HashMap&lt;String, String&gt;, hashGenerationListener</strong>: PayUHashGeneratedListener): Merchant will get a map with the type of hash and hash string as the value of the map. Refer for more details</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


## Decoupled Flow

### Step 1:Initialise SDK

Initialization of SDK is required if the merchant is utilizing PayU 3DS 2.0 for Decoupled functionality. For more information on properties, refer to \<\<Description of Properties in Initialization>>.

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

| Parameter         | Description                            |
| :---------------- | :------------------------------------- |
| Key               | The key provided to merchant by PayU.  |
| RequestId         | Unique request ID for the transaction. |
| AppCompatActivity | Required to initialise SDK.            |
|                   |                                        |

## GUI customisation

The following components can be customized:

- Button
- Label
- Toolbar
- Text box
- Font
- GUI
- The sample code blocks for the above:

```Text Kotlin
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

## Supported Font Type Details

```Text Kotlin
enum class FontName { 
    ROBOTO_REGULAR, 
    ROBOTO_MEDIUM
}
```

## PayU3DS2Response:

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>status</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter returns the status of the web service call. The status can be any of the following:  </p>
<p>0 - If the web service call succeeded  </p>
<p>1 - If the web service call failed.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>errorMessage</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The error message with details of what went wrong.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>result</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Success response with details. Refer to the following class (below the table) for the response structure.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


The following items are in the response:

```Text Kotlin
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

## Step 2: Device details(PArq)

To obtain device information to initiate an authentication request:

```Text Kotlin
PayU3DS2.extractDeviceDetails(cardScheme: CardScheme): PayU3DS2Response
```

cardScheme expected values:

- VISA
- MASTERCARD

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>status</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter returns the status of the web service call. The status can be any of the following:  </p>
<p>0 - If the web service call succeeded  </p>
<p>1 - If the web service call failed.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>errorMessage</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The error message with details of what went wrong.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>result</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Success response with details. Refer to the following class (below the table) for the response structure.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


```Text Kotlin
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

## Step 3: 3DS 2.0 Challenge Initiation

Call the following function to start the challenge:

```Text Kotlin
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>activity</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the <code>AppCompatActivity</code> reference.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>challengeParameter</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Create an object of ChallengeParameter class with the following parameters :  </p>
<p>ChallengeParameter(&quot;acsSignedContent&quot;, &quot;acsRefNumber&quot;, &quot;acsTransactionID&quot;, &quot;threeDSServerTransactionID&quot;)  </p>
<p><strong>acsSignedContent</strong>= Send ACS Signed Content received in ARes  </p>
<p><strong>acsRefNumber</strong>= Send ACS Ref Number Content received in ARes  </p>
<p><strong>acsTransactionID</strong>= Send ACS Transaction ID received in ARes  </p>
<p><strong>threeDSServerTransactionID</strong>= Send ThreeDS Server Transaction ID received in ARes</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


Before invoking this method, generate the authentication request through any aggregator and pass the above-defined challenge parameters to initiate challenges.

**PayU3DS2BaseCallback**: Callback consists of two methods:

```Text Kotlin
fun onSuccess(response: Any) //It will contain success response.
fun onError(errorCode: Int, errorMessage: String) //It will contain failure reason code and reason.

//Cast response to String. If value is "Y" that means challenge is successfully executed else it is failed.
```

PaymentParams Parameter Example

```Text Kotlin
var mPaymentParams =  PaymentParams();
        mPaymentParams.key = "<Your Key issued by PayU>"
        mPaymentParams.amount = "<Transaction Amount>"
        mPaymentParams.productInfo = "<Product Description>"
        mPaymentParams.firstName = "<Customer First Name>"
        mPaymentParams.email = "<Customer Email>"
        mPaymentParams.txnId = "<Transaction Id>"
        mPaymentParams.surl = "<Success URL>"
        mPaymentParams.furl = "<Failure URL>"
        mPaymentParams.udf1 = "<User Defined Fields>"
        mPaymentParams.udf2 = "<User Defined Fields>"
        mPaymentParams.udf3 = "<User Defined Fields>"
        mPaymentParams.udf4 = "<User Defined Fields>"
        mPaymentParams.udf5 = "<User Defined Fields>"
        mPaymentParams.cardNumber = "<cardNumber>"
        mPaymentParams.cardName = "<cardName>"
        mPaymentParams.nameOnCard = "<cardholderName>"
        mPaymentParams.expiryMonth = "<expiryMonth>"// MM
        mPaymentParams.expiryYear = "<expiryYear>"// YYYY
        mPaymentParams.cvv = "<cvv>"
```

## Hash Generation

You will receive a call on the generateHash method of PayU3DS2PaymentCallback.

In the method parameter, you will receive a dictionary or hashMap, and extract the value of hashString from that. Pass that value to the server, and now the server will append salt at the end and generate sha512 hash over it. The server will give that hash back to your app, and the app will provide that hash to PayU through a callback mechanism.

In the map, you have to check for the following keys to generate a hash:

- hashString
- hashName
- postSalt

At the end of that hashString, append your salt and use the SHA-512 algorithm on that final string to generate a hash.

> 🚧 Callout
> 
> - If you got postSalt also in the map, first use hash string append salt and then append postSalt value to that string and use SHA-512 algorithm on that final string to generate hash.
> - There is no need to know the formula for dynamic hashes because PayU SDK gives you the string containing all the required parameters. Your server has to append salt at the end and generate sha512 hash over it.

## Error codes

| Code | Description                      |
| :--- | :------------------------------- |
| 0    | Success                          |
| 1    | Fail                             |
| 3    | Challenge timeout                |
| 4    | Challenge protocol error         |
| 5    | Challenge cancelled              |
| 101  | Card bin or card token was empty |
| 102  | Merchant key null                |
| 103  | Amount not in correct format     |
| 104  | Transaction ID null              |
| 105  | Hash null                        |
| 106  | Card not supported on 3DS 2.0    |
| 107  | Card scheme not supported        |
| 108  | Hash incorrect                   |
| 500  | Something went wrong             |
| 504  | Gateway timeout                  |