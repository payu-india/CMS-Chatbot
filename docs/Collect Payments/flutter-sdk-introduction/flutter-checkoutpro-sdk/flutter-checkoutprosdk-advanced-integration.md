---
title: Advanced Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This section describes how to integrate the following advanced features with Flutter SDK:

<Callout icon="📘" theme="info">
  **Prerequisites**:
  Before you start with the advanced integration with PayUCheckoutPro, the payUCheckoutProConfig object needs to be passed with payUPaymentParams in the openCheckoutScreen method of the PayU SDK. The sample code snippet is similar to the following:

  ```Text Dart
  _checkoutPro.openCheckoutScreen(
  payUPaymentParams: payUPaymentParams,
  payUCheckoutProConfig: payUCheckoutProConfig,
  );
  ```
</Callout>

<Accordion title="Change theme" icon="fa-code">
  <Accordion title="For iOS" icon="fa-code">
    You can change the primary and the secondary color of the UI to match the theme of your app:

    ```Text Dart
    var payUCheckoutProConfig = {
     PayUCheckoutProConfigKeys.primaryColor: "<Color Hex Code e.g. #aabbcc>",
     PayUCheckoutProConfigKeys.secondaryColor: "<Color Hex Code e.g. #000000>",
    }
    ```
  </Accordion>

  <Accordion title="For Android" icon="fa-code">
    You can modify the color scheme and theme used in the PayUCheckoutPro SDK by providing your own set of colors. To change the color theme of the SDK, add the following color configuration to your **colors.xml** file.

    If you don't have a **colors.xml**, create an empty file in your app project with this name, and include the following configuration settings:

    ```Text color.xml
    <color name="one_payu_colorPrimary">#053bc1</color>  //primary color has changed the appbar/toolbar and background color.  
    <color name="one_payu_colorPrimaryDark">#053bc1</color> //primaryDark color has changed statusbar and contextual app bar.  
    <color name="one_payu_colorAccent">#053bc1</color> //colorAccent has changed such as check boxes, radio buttons, and edit text boxes, cursor.  
    <color name="one_payu_baseTextColor">#ffffff</color> //baseTextcolor as changed header and button text
    ```
  </Accordion>
</Accordion>

<Accordion title="Customise font" icon="fa-code">
  You can customize the font used in the PayU checkout page as per your preference. To customize the font, add the following code snippet in the `style.xml` file of your Android app.

  ```Text XML
  <style name="PayU_header">
      <item name="android:fontFamily">@font/font_name</item>
  </style>
  ```

  Here, we are setting the fontFamily attribute to the font file that you want to access. See Add a font as an XML resource in the Android developer documentation to learn more.

  > 📘 Note
  >
  > See[ Add a font as an XML resource](https://developer.android.com/develop/ui/views/text-and-emoji/fonts-in-xml)  in the Android developer documentation to learn more.
</Accordion>

<Accordion title="Set merchant name" icon="fa-code">
  You can customize the name to personalize the checkout screen.

  ```Text Dart
  var payUCheckoutProConfig = {
   	PayUCheckoutProConfigKeys.merchantName: "<Merchant Name>",
  }
  ```
</Accordion>

<Accordion title="Set merchant logo" icon="fa-code">
  You can customize the logo to personalize the checkout screen for iOS or Android platforms.

  <Accordion title="For iOS" icon="fa-code">
    ```Text Dart
    var payUCheckoutProConfig = {
     PayUCheckoutProConfigKeys.merchantLogo: "<Image asset name like 'Jio'>",
    }
    ```
  </Accordion>

  <Accordion title="For Android" icon="fa-code">
    Add the image in the app/res/drawable folder of the native Android app and pass the same under the merchantLogo key.
  </Accordion>
</Accordion>

<Accordion title="Show/Hide Merchant Logo" icon="fa-code">
  Merchants want to show the logo on the PayU Hosted Page. By default, the logo is invisible.

  ```Text Dart
  var payUCheckoutProConfig = {
    PayUCheckoutProConfigKeys.showMerchantLogo: false, //true/false
  }
  ```
</Accordion>

<Accordion title="Show/Hide Saved Card Features" icon="fa-code">
  Merchants want to hide Saved Card features. By default, the Saved Card feature is enabled.

  ```Text Dart
  var payUCheckoutProConfig = {
    PayUCheckoutProConfigKeys.enableSavedCard: false, //true/false
  }
  ```
</Accordion>

<Accordion title="Hide Checkout screen Back button dialog box" icon="fa-code">
  You can choose to hide the dialog box that is displayed when the Back button is clicked from the L1 screen. The default value is true.

  ```Text Dart
  var payUCheckoutProConfig = {
   	PayUCheckoutProConfigKeys.showExitConfirmationOnCheckoutScreen: true/false,
  }
  ```
</Accordion>

<Accordion title="Hide Back button dialog box after payment initialisation" icon="fa-code">
  You can choose to hide the dialog that is displayed when the Back button is clicked after payment is initialized. The default value is true.

  ```Text Dart
  var payUCheckoutProConfig = {
  PayUCheckoutProConfigKeys.showExitConfirmationOnPaymentScreen: true/false,
  }
  ```
</Accordion>

<Accordion title="Auto Select OTP" icon="fa-code">
  You can choose to auto-select OTP flow on the bank page with the flag as in the following code block. The default value is false.

  ```Text Dart
  var payUCheckoutProConfig = {
  PayUCheckoutProConfigKeys.autoSelectOtp:: true/false,
  }
  ```
</Accordion>

<Accordion title="Set merchant response timeout" icon="fa-code">
  The merchant response timeout is the time interval that PayU waits for merchant surl/furl to load before passing the transaction response back to the app. If merchant surl/furl pages take longer to load, PayU has a response timeout of 5000 milliseconds by default. However, if you feel that their surl/furl can take longer than 5000 milliseconds, you can set this flag.

  ```Text Dart
  var payUCheckoutProConfig = {
   PayUCheckoutProConfigKeys.merchantResponseTimeout: 5000,
  }
  ```
</Accordion>

<Accordion title="Review order" icon="fa-code">
  You can pass the checkout order details to the SDK that will be displayed in the SDK during the transaction flow.

  ```Text Dart
  var payUCheckoutProConfig = {
   PayUCheckoutProConfigKeys.cartDetails: [{ 'Order': 'Value' }, { 'Key Name': 'Value1' }]
  }
  ```

  For example:

  ```Text Dart
  var cartDetails = [ 
           {"GST": "5%"},      
           {"Delivery Date": "25 Dec"},      
           {"Status": "In Progress"}    
  ];
  ```
</Accordion>

<Accordion title="Additional payment options on the Checkout screen" icon="fa-code">
  The following code snippet is used to display Google Pay, PhonePe, and Paytm on the primary Checkout screen.

  ```Text Dart
  var payUCheckoutProConfig = {
  PayUCheckoutProConfigKeys.paymentModesOrder: [{ 'UPI': 'TEZ' }, { 'Wallets': 'PAYTM' }, { 'Wallets': 'PHONEPE' }]
  }
  ```

  This will display Google Pay, PhonePe, and Paytm respectively on top of available payment options.
</Accordion>

<Accordion title="Configure checkout payment modes order" icon="fa-code">
  Default payment modes order on the checkout screen, as illustrated in the following code block, is:

  * Card
  * NetBanking
  * UPI
  * Wallets

  You can configure the checkout payment options order. You need to provide a list of payment modes to configure the payment options order. Checkout order will be the order of items in the list. If not all payment modes' order is mentioned in the list, all other payment modes will be displayed in their default order as shown above.

  The following code snippet is used to order the payment modes on the L1 screen:

  ```Text Dart
  var payUCheckoutProConfig = {
  PayUCheckoutProConfigKeys.paymentModesOrder: [{ 'cards': '' }, { 'net banking': '' }, { 'upi': '' }, { 'wallets':'' }, { 'emi': '' }]
  }
  ```

  The resulting payment order on the initial Checkout screen will be:

  * Cards (Credit or Debit)
  * Net Banking
  * UPI
  * Wallets
  * EMI
</Accordion>

<Accordion title="Offers integration" icon="fa-code">
  To pass offers in the CheckoutPro SDK, use the following code snippet:

  ```Text Dart
  	var payUPaymentParams = {
  PayUPaymentParamKey.userToken:           "<Pass a unique token to fetch offers>", // OPTIONAL
  }
  ```
</Accordion>

<Accordion title="Native OTP assist" icon="fa-code">
  To enable Native OTP assistance in iOS, use the following code. In Android, this will be added by default.

  ```Text Dart
  var payUPaymentParams = {
  PayUPaymentParamKey.enableNativeOTP: true, // OPTIONAL
  }
  ```
</Accordion>

<Accordion title="Customize UPI Apps Order" icon="fa-code">
  You can customize the display order of UPI payment apps. Define the sequence using a pipe-separated format to rearrange how UPI apps appear to users.

  ```Text Dart
  var payUCheckoutProConfig = {
  PayUCheckoutProConfigKeys.upiAppsOrder: "phonepe|paytm|gpay"
  }
  ```
</Accordion>

<Accordion title="Custom Note integration" icon="fa-code">
  This subsection describes how to integrate custom notes in PayUCheckoutPro SDK. To integrate custom notes in PayUCheckoutPro SDK:

  * Create a custom note list
  * Pass custom note list to SDK

  <Accordion title="Step 1: Create a Custom Note list" icon="fa-code">
    Create a list of custom notes that you want to pass to the CheckoutPro SDK. For each custom note, custom\_note and custom\_note\_category need to be passed.

    ```Text Dart
    var customNotes = [       {         "custom_note": "Its Common custom note for testing purpose",         "custom_note_category": [           PayUPaymentTypeKeys.emi,           PayUPaymentTypeKeys.card         ]       },       {         "custom_note": "Payment options custom note",         "custom_note_category": null       }     ];
    ```
  </Accordion>

  <Accordion title="Step 2: Add in PayU Checkout config" icon="fa-code">
    Add in the PayU Checkout Config similar to the following code snippet:

    ```Text Dart
    var payUCheckoutProConfig = {  		     	PayUCheckoutProConfigKeys.customNotes: customNotes
    }
    ```
  </Accordion>
</Accordion>

<Accordion title="Enforced Payment Modes" icon="fa-code">
  You can directly open a specific payment mode like NB, WALLET, UPI, CARD, etc in SDK. To enforce payments:

  1. Create an enforced payment list
  2. Add in PayU Checkout Config

  <Accordion title="Step 1: Create an enforced payment list" icon="fa-code">
    For each enforce payment, payment\_type needs to be passed.

    ```Text Dart
    var enforcePaymentList = [  
    {"payment_type": "CARD"},  {"payment_type": "NB"}, {"payment_type": "EMI"}, {payment_type": "WALLET"}, {"payment_type": "UPI"},{"payment_type": "BNPL"},{"payment_type": "NEFTRTGS"}];
    ```

    <Accordion title="Advanced Card Payment Enforcement" icon="fa-code">
      <Accordion title="Card Type Enforcement (CC/DC Only)" icon="fa-code">
        Enforce payment based on card type - Credit Card (CC) or Debit Card (DC):

        ```Text Dart
        var enforcePaymentList = [{"payment_type": "CARD", "card_type": "DC"}, {"payment_type": "CARD", "card_type": "CC"}];
        ```

        This configuration allows all debit cards and all credit cards, regardless of the card scheme.
      </Accordion>

      <Accordion title="Card Scheme Enforcement (VISA, MASTERCARD, AMEX, etc.)" icon="fa-code">
        Enforce payment based on specific card schemes along with card type:

        ```Text Dart
        var enforcePaymentList = [{"payment_type": "CARD", "card_type": "DC", "card_scheme": "VISA"}, {"payment_type": "CARD", "card_type": "CC", "card_scheme": "MAST"}];
        ```
      </Accordion>
      </Accordion>
<Accordion title="Enforce Specific Bank/Wallet Provider" icon="fa-code">
  You can enforce specific banks for Net Banking (NB) and specific wallet providers for Wallet payments using the `enforce_ibiboCode` parameter:

  **Net Banking - Specific Bank:**
  ```javascript
  var enforcePaymentList = [{"payment_type": "NB", "enforce_ibiboCode": "AXIS"}];
  ```

**Wallet - Specific Provider:**

```javascript
var enforcePaymentList = [{"payment_type": "WALLET", "enforce_ibiboCode": "PAYTM"}];
```
</Accordion>
  </Accordion>

  <Accordion title="Step 2: Add in PayU Checkout config" icon="fa-code">
    Add in PayU Checkout Config similar to the following snippet:

    ```Text Dart
    var payUCheckoutProConfig = {
     PayUCheckoutProConfigKeys.enforcePaymentList: enforcePaymentList, 
    }
    ```
  </Accordion>
</Accordion>

<Accordion title="Android specific configurations" icon="fa-code">
  <Accordion title="Runtime SMS permission" icon="fa-code">
    You can set this flag to false if you do not want CheckoutPro SDK to ask for runtime SMS permission on the bank OTP page. The default value is true.

    ```Text Dart
    var payUCheckoutProConfig = {
    PayUCheckoutProConfigKeys .merchantSMSPermission: true/false
    }
    ```
  </Accordion>

  <Accordion title="Auto Approve OTP" icon="fa-code">
    You can choose to automatically approve OTP flow on the bank page with the flag specified in the following code block. The default value is false.

    ```Text Dart
    var payUCheckoutProConfig = {
    PayUCheckoutProConfigKeys.autoApprove: true/false
    }
    ```
  </Accordion>

  <Accordion title="Hide toolbar in the Custom Browser (CB)" icon="fa-code">
    You can choose to hide the toolbar on CB. By default, the CB toolbar is displayed.

    ```Text Dart
    var payUCheckoutProConfig = {
    PayUCheckoutProConfigKeys.showCbToolbar: true/false
    }
    ```
  </Accordion>

  <Accordion title="Show SSL Dialog Alert" icon="fa-code">
    you are trying to show the dialog from a place that isn't permitted.

    ```Text Dart
     var payUCheckoutProConfig = {
      payUCheckoutProConfig.enableSslDialog = true //true/false
    }
    ```

    . The error message is shown as received from the SSL error description

    <Image align="center" src="https://files.readme.io/c19a750-MicrosoftTeams-image_8.png" width="200px" />
  </Accordion>
</Accordion>
