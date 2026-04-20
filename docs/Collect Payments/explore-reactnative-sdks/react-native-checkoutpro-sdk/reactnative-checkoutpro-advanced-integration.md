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
This section includes the following advanced integrations with React Native Checkout Pro SDK:

<Callout icon="📘" theme="info">
  **Prerequisites**:  Before you start with the advanced integration with PayUCheckoutPro, the payUCheckoutProConfig the object needs to be passed with payUPaymentParams in the openCheckoutScreen method of PayUBizSdk. Sample code for can be 1.

  ```javascript React.js
  var paymentObject = {
      payUPaymentParams: payUPaymentParams,
      payUCheckoutProConfig: payUCheckoutProConfig
  }
  PayUBizSdk.openCheckoutScreen(paymentObject);
  ```
</Callout>

<Accordion title="Change theme" icon="fa-code">
  **For iOS**: You can change the primary and the secondary color of the UI to match the theme of your app:

  ```javascript React.js
  var payUCheckoutProConfig = {
    primaryColor: "<Color Hex Code e.g. #aabbcc>",
    secondaryColor: "<Color Hex Code e.g. #000000>",
  }
  ```

  **For Android**: To change the primary color, add the color values in your Android colors.xml. For more information, refer to [Customize your Integration](https://docs.payu.in/docs/android-checkoutpro-custom-integrations).

  ***
</Accordion>

<Accordion title="Set merchant name" icon="fa-code">
  You can customize the name to personalize the checkout screen.

  ```Text React.js
  var payUCheckoutProConfig = {
    merchantName: "<Merchant Name>",
  }
  ```

  ***
</Accordion>

<Accordion title="Set merchant logo" icon="fa-code">
  You can customize the logo to personalize the checkout screen.

  **For iOS**

  ```Text React.js
  var payUCheckoutProConfig = {
    merchantLogo: "<Image asset name like 'Jio'>",
  }
  ```

  **For Android**: Add the image in the app/res/drawable folder of the native Android app and pass the same under the merchantLogo key.

  ***
</Accordion>

<Accordion title="Show/Hide Merchant Logo" icon="fa-code">
  Merchants want to show the logo on the PayU Hosted Page. By default, the logo is invisible.

  ```Text React.js
  var payUCheckoutProConfig = {
    showMerchantLogo: false, //true/false
  }
  ```
</Accordion>

<Accordion title="Show/Hide Saved Card Features" icon="fa-code">
  Merchants want to hide Saved Card features. By default, the Saved Card feature is enabled.

  ```Text React.js
  var payUCheckoutProConfig = {
    enableSavedCard: false, //true/false
  }
  ```
</Accordion>

<Accordion title="Hide Checkout screen Back button dialog box" icon="fa-code">
  Merchants can choose to hide the dialog box that appears when the Back button is clicked from the L1 screen. The default value is true.

  ```Text React.js
  var payUCheckoutProConfig = {
    showExitConfirmationOnCheckoutScreen: true/false,
  }
  ```

  ***
</Accordion>

<Accordion title="Hide Back button dialog box after payment initialisation" icon="fa-code">
  Merchants can choose to hide the dialog that appears when the back button is pressed after payment is initialized. The default value is true.

  ```Text React.js
  var payUCheckoutProConfig = {
    showExitConfirmationOnCheckoutScreen: true/false,
  }
  ```

  ***
</Accordion>

<Accordion title="Auto Select OTP" icon="fa-code">
  Merchants can choose to auto-select OTP flow on the bank page with the flag as in the following code block. The default value is false.

  ```Text React.js
  var payUCheckoutProConfig = {
    autoSelectOtp: true/false,
  }
  ```

  ***
</Accordion>

<Accordion title="Set Merchant Response Timeout" icon="fa-code">
  The merchant response timeout is the time interval that PayU waits for merchant surl/furl to load before passing the transaction response back to the app. If merchant surl/furl pages take longer to load, PayU has a response timeout of 5000 milliseconds by default. However, if merchants feel that their surl/furl can take longer than 5000 milliseconds, they can set this flag.

  ```Text React.js
  var payUCheckoutProConfig = {
    merchantResponseTimeout: 5000,
  }
  ```

  ***
</Accordion>

<Accordion title="Enable SurePay on bank page" icon="fa-code">
  Merchants can enable SurePay on the bank page. When the internet is lost during the transaction, if the transaction can be retried from that bank page after the internet is resumed, the SurePay dialog box is displayed. It has legitimate values such as 0, 1, 2, and 3. Where the number defines how many times the SurePay dialog box should be displayed during the transaction without internet connectivity. The default value is 0.

  ```Text React.js
  var payUCheckoutProConfig = {
    surePayCount: 0-3,
  }
  ```

  ***
</Accordion>

<Accordion title="Review order" icon="fa-code">
  Merchants can pass the checkout order details to the SDK that will be displayed in the SDK during the transaction flow.

  ```Text React.js
  var payUCheckoutProConfig = {
    cartDetails: [{ 'Order': 'Value' }, { 'Key Name': 'Value1' }]
  }
  ```

  ***
</Accordion>

<Accordion title="Additional payment options on the Checkout screen" icon="fa-code">
  The following code snippet is used to display Google Pay, PhonePe, and Paytm on the primary Checkout screen.

  ```Text React.js
  var payUCheckoutProConfig = {
  paymentModesOrder: [{ 'UPI': 'TEZ' }, { 'Wallets': 'PAYTM' }, { 'Wallets': 'PHONEPE' }]
  }
  ```

  This will display Google Pay, PhonePe, and Paytm respectively on top of available payment options.

  ***
</Accordion>

<Accordion title="Configure checkout payment modes order" icon="fa-code">
  Default payment modes order on the checkout screen as in the following code block: Card, NetBanking, UPI, and Wallets.

  Merchants can specify the checkout payment options order. For this, the merchant needs to provide a list of payment modes. Checkout order will be the order of items in the list. If not all payment mode's order is mentioned in the list, all other payment modes will be displayed in their default order as shown above.

  The following code snippet is used to order the payment modes on the L1 screen.

  ```Text React.js
  var payUCheckoutProConfig = {
  paymentModesOrder: [{ 'cards': '' }, { 'net banking': '' }, { 'upi': '' }, { 'wallets': '' }, { 'emi': '' }]
  }
  ```

  The resulting payment order on the initial Checkout screen will be:

  * Cards (Credit or Debit)
  * Net Banking
  * UPI
  * Wallets
  * EMI

  ***
</Accordion>

<Accordion title="Enforced payment modes" icon="fa-code">
  You can directly open a specific payment mode like NB, WALLET, UPI, CARD, NB, BNPL, NEFTRTGS etc in SDK.

  Create an enforce list similar to the following code block to enforce payment modes:

  <Accordion title="Step 1: Create an enforced payment list" icon="fa-code">
    For each enforced payment, the payment\_type parameters need to be passed.

    ```
    var enforcePaymentList = [  
    {"payment_type": "CARD"},  {"payment_type": "NB"}, {"payment_type": "EMI"}, {payment_type": "WALLET"}, {"payment_type": "UPI"},{"payment_type": "BNPL"},{"payment_type": "NEFTRTGS"}];
    ```

    <Accordion title="Advanced Card Payment Enforcement" icon="fa-code">
      <Accordion title="Card Type Enforcement (CC/DC Only)" icon="fa-credit-card">
  Enforce payment based on card type - Credit Card (CC) or Debit Card (DC):

  ```javascript
  var enforcePaymentList = [{"payment_type": "CARD", "card_type": "DC"}, {"payment_type": "CARD", "card_type": "CC"}];
  ```
  
  This configuration allows all debit cards and all credit cards, regardless of the card scheme.
</Accordion>

<Accordion title="Card Scheme Enforcement (VISA, MASTERCARD, AMEX, etc.)" icon="fa-code">
  Enforce payment based on specific card schemes along with card type:

  ```javascript
  var enforcePaymentList = [{"payment_type": "CARD", "card_type": "DC", "card_scheme": "VISA"}, {"payment_type": "CARD", "card_type": "CC", "card_scheme": "MAST"}];
  ```
  
  This configuration allows only VISA debit cards and MASTERCARD credit cards.
</Accordion>
    </Accordion>
  </Accordion>

  <Accordion title="Step 2: Add in PayU Checkout config" icon="fa-code">
    ```
    var payUCheckoutProConfig = {  
    enforcePaymentList: enforcePaymentList,  
    }
    ```
  </Accordion>

  ***
</Accordion>

<Accordion title="Customize UPI Apps Order" icon="fa-code">
  You can customize the display order of UPI payment apps. Define the sequence using a pipe-separated format to rearrange how UPI apps appear to users.

  ```Text React.js
  var payUCheckoutProConfig = {
  upiAppsOrder: "phonepe|paytm|gpay"
  }
  ```
</Accordion>

<Accordion title="Android specific configurations" icon="fa-code">
  <Accordion title="Runtime SMS permission" icon="fa-code">
    Merchants can set this flag to false if they do not want CheckoutPro SDK to ask for runtime SMS permission on the bank OTP page. The default value is true.

    ```Text React.js
    var payUCheckoutProConfig = {
    merchantSMSPermission: true/false
    }
    ```
  </Accordion>

  <Accordion title="Auto approve OTP" icon="fa-code">
    Merchants can choose to automatically approve OTP flow on the bank page with the flag specified in the following code block. The default value is false.

    ```javascript React.js
    var payUCheckoutProConfig = {
    autoApprove: true/false
    }
    ```
  </Accordion>

  <Accordion title="Hide toolbar in Custom Browser (CB)" icon="fa-code">
    Merchants can choose to hide the toolbar on CB. By default, the CB toolbar is displayed.

    ```javascript React.js
    var payUCheckoutProConfig = {
    showCbToolbar: true/false
    }
    ```
  </Accordion>
</Accordion>
