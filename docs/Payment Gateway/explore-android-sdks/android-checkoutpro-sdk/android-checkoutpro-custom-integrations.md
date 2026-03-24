---
title: Customise Your Integration
excerpt: Modify the integration to suit your use case.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The PayUCheckoutPro SDK provides several customization options allowing you to make the SDK closer to the Look & Feel of your app and control some advanced capabilities provided by the SDK.

<Callout icon="📘" theme="info">
  **Remember**: You can dynamically make the changes listed in this section using the PayU Dashboard. For more information, refer to [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).
</Callout>

<Accordion title="Modify theme" icon="fa-code">
  You can modify the color scheme and theme used in the PayUCheckoutPro SDK by providing your own set of colors. To change the color theme of the SDK, add the following color configuration to your colors.xml file. If you don't have a colors.xml, create an empty file in your app project with this name, and include the following configuration settings:

  ```xml XML
  <color name="one_payu_colorPrimary">#053bc1</color>  //primary color has changed the appbar/toolbar and background color.
  <color name="one_payu_colorPrimaryDark">#053bc1</color> //primaryDark color has changed statusbar and contextual app bar.
  <color name="one_payu_colorAccent">#053bc1</color> //colorAccent has changed such as check boxes, radio buttons, and edit text boxes, cursor.
  <color name="one_payu_baseTextColor">#ffffff</color> //baseTextcolor as changed header and button text
  ```
</Accordion>

<Accordion title="Customise font" icon="fa-code">
  You can customise the font used in the PayU checkout page as per your preference. To customise the font, add the following code snippet in the `style.xml` file of your Android app.

  ```xml XML
  <style name="PayU_header">
      <item name="android:fontFamily">@font/font_name</item>
  </style>
  ```

  Here, we are setting the fontFamily attribute to the font file that you want to access. See Add a font as an XML resource in the Android developer documentation to learn more.

  <Callout icon="📘" theme="info">
    **Note**: Refer to [ Add a font as an XML resource](https://developer.android.com/develop/ui/views/text-and-emoji/fonts-in-xml)  in the Android developer documentation to learn more.
  </Callout>
</Accordion>

<Accordion title="Set WebChromeClient" icon="fa-code">
  To set your WebChromeClient in PayUCheckoutPro SDK, it must extend the PayUWebChromeClient class similar to the following code snippet:

  ```java Java
  class CheckoutProWebChromeClient extends PayUWebChromeClient{
  public CheckoutProWebChromeClient(Bank bank){
  super(bank);
  }
  @Override
  public boolean onJsConfirm(WebView view, String url, String message, JsResult result) {
  return super.onJsConfirm(view, url, message, result);
  }
  @Override
  public boolean onJsAlert(WebView view, String url, String message, JsResult result) {
  return super.onJsAlert(view, url, message, result);
  }
  }
  ```
  ```kotlin Kotlin
      class CheckoutProWebChromeClient(
          val bank: Bank
      ) : PayUWebChromeClient(bank) {
          override fun onJsConfirm(
              view: WebView?,
              url: String?,
              message: String?,
              result: JsResult?
          ): Boolean {
              return super.onJsConfirm(view, url, message, result)
          }

          override fun onJsAlert(
              view: WebView?,
              url: String?,
              message: String?,
              result: JsResult?
          ): Boolean {
              return super.onJsAlert(view, url, message, result)
          }
      }
  ```

  After creating your WebChromeClient, it can be set in PayUCheckoutPro SDK in the setWebViewProperties() callback method of PayUCheckoutProListener similar to the following code snippet:

  ```java Java
  PayUCheckoutPro.open( 
  this, 
  payUPaymentParams, 
  new PayUCheckoutProListener() { 
  @Override 
  public void onPaymentSuccess(@NotNull Object response) { 
  //Cast response object to HashMap
  HashMap<String,Object> result = (HashMap<String, Object>) response 
  String payuResponse = result.get(PayUCheckoutProConstants.CP_PAYU_RESPONSE);
  String merchantResponse = result.get(PayUCheckoutProConstants.CP_MERCHANT_RESPONSE)); 
  } 
  @Override 
  public void onPaymentFailure(@NotNull Object response) {
  //Cast response object to HashMap
  HashMap<String,Object> result = (HashMap<String, Object>) response 
  String payuResponse = result.get(PayUCheckoutProConstants.CP_PAYU_RESPONSE);
  String merchantResponse = result.get(PayUCheckoutProConstants.CP_MERCHANT_RESPONSE));
  } 
  @Override 
  public void onPaymentCancel(boolean isTxnInitiated) { 
  } 
  @Override 
  public void onError(@NotNull ErrorResponse errorResponse) { 
  String errorMessage = errorResponse.getErrorMessage(); 
  } 
  @Override
  public void setWebViewProperties(@Nullable WebView webView, @Nullable Object o) {
  webView.setWebChromeClient(new CheckoutProWebChromeClient((Bank)o));
  }
  @Override 
  public void generateHash(@NotNull HashMap<String, String> valueMap, @NotNull PayUHashGenerationListener hashGenerationListener) { 
  String hashName = valueMap.get(CP_HASH_NAME); 
  String hashData = valueMap.get(CP_HASH_STRING); 
  if (!TextUtils.isEmpty(hashName) && !TextUtils.isEmpty(hashData)) { 
  //Generate Hash from your backend here
  String hash = HashGenerationUtils.INSTANCE.generateHashFromSDK(hashData, salt); 
  HashMap<String, String> dataMap = new HashMap<>(); 
  dataMap.put(hashName, hash); 
  hashGenerationListener.onHashGenerated(dataMap); 
  } 
  } 
  } 
  } 
  );
  ```
  ```kotlin Kotlin
   PayUCheckoutPro.open( 
          this, payUPaymentParams, 
          object : PayUCheckoutProListener { 

              override fun onPaymentSuccess(response: Any) { 
                  response as HashMap<*, *> 
                  val payUResponse = response[PayUCheckoutProConstants.CP_PAYU_RESPONSE]
                  val merchantResponse = response[PayUCheckoutProConstants.CP_MERCHANT_RESPONSE]  
              } 

   
              override fun onPaymentFailure(response: Any) { 
                  response as HashMap<*, *> 
                  val payUResponse = response[PayUCheckoutProConstants.CP_PAYU_RESPONSE]
                  val merchantResponse = response[PayUCheckoutProConstants.CP_MERCHANT_RESPONSE]  
              } 

   
              override fun onPaymentCancel(isTxnInitiated:Boolean) { 
              } 

   
              override fun onError(errorResponse: ErrorResponse) { 
                  val errorMessage: String 
                  if (errorResponse != null && errorResponse.errorMessage != null && errorResponse.errorMessage!!.isNotEmpty()) 
                      errorMessage = errorResponse.errorMessage!! 
                  else 
                      errorMessage = resources.getString(R.string.some_error_occurred) 
              } 
              
              override fun setWebViewProperties(webView: WebView?, bank: Any?) {
                  webView?.webChromeClient = CheckoutProWebChromeClient(bank as Bank)
              }
                       
              override fun generateHash( 
                  valueMap: HashMap<String, String?>, 
                  hashGenerationListener: PayUHashGenerationListener 
              ) { 
                  if ( valueMap.containsKey(CP_HASH_STRING) 
                      && valueMap.containsKey(CP_HASH_STRING) != null 
                      && valueMap.containsKey(CP_HASH_NAME) 
                      && valueMap.containsKey(CP_HASH_NAME) != null) { 
   
                      val hashData = valueMap[CP_HASH_STRING] 
                      val hashName = valueMap[CP_HASH_NAME] 
   
                      val hash: String? = 
                          HashGenerationUtils.generateHashFromSDK(hashData!!, salt) 
                      if (!TextUtils.isEmpty(hash)) { 
                          val dataMap: HashMap<String, String?> = HashMap() 
                          dataMap[hashName!!] = hash!! 
                          hashGenerationListener.onHashGenerated(dataMap) 
                      } 
                  } 
              } 
          })
  ```

  ***
</Accordion>

<Accordion title="Set WebViewClient" icon="fa-code">
  To set your WebViewClient in PayUCheckoutPro SDK, it must extend the`PayUWebViewClient` class similar to the following:

  ```java Java
  class CheckoutProWebViewClient extends PayUWebViewClient{
  public CheckoutProWebViewClient(Bank bank, String merchantKey){
  super(bank, merchantKey);
  }
  }
  ```
  ```kotlin Kotlin
      class CheckoutProWebViewClient(bank: Bank, merchantKey: String): PayUWebViewClient(bank, merchantKey){ 
      
      }
  ```

  After creating your WebViewClient, it can be configured in the PayUCheckoutPro SDK in the `setWebViewProperties() `callback method of PayUCheckoutProListener similar to the following:

  ```java Java
  PayUCheckoutPro.open( 
  this, 
  payUPaymentParams, 
  new PayUCheckoutProListener() { 
  @Override 
  public void onPaymentSuccess(@NotNull Object response) { 
  //Cast response object to HashMap
  HashMap<String,Object> result = (HashMap<String, Object>) response 
  String payuResponse = result.get(PayUCheckoutProConstants.CP_PAYU_RESPONSE);
  String merchantResponse = result.get(PayUCheckoutProConstants.CP_MERCHANT_RESPONSE)); 
  } 
  @Override 
  public void onPaymentFailure(@NotNull Object response) {
  //Cast response object to HashMap
  HashMap<String,Object> result = (HashMap<String, Object>) response 
  String payuResponse = result.get(PayUCheckoutProConstants.CP_PAYU_RESPONSE);
  String merchantResponse = result.get(PayUCheckoutProConstants.CP_MERCHANT_RESPONSE));
  } 
  @Override 
  public void onPaymentCancel(boolean isTxnInitiated) { 
  } 
  @Override 
  public void onError(@NotNull ErrorResponse errorResponse) { 
  String errorMessage = errorResponse.getErrorMessage(); 
  } 
  @Override
  public void setWebViewProperties(@Nullable WebView webView, @Nullable Object o) {
  webView.setWebViewClient(new CheckoutProWebViewClient((Bank)o, <merchant-key>));
  }
  @Override 
  public void generateHash(@NotNull HashMap<String, String> valueMap, @NotNull PayUHashGenerationListener hashGenerationListener) { 
  String hashName = valueMap.get(CP_HASH_NAME); 
  String hashData = valueMap.get(CP_HASH_STRING); 
  if (!TextUtils.isEmpty(hashName) && !TextUtils.isEmpty(hashData)) { 
  //Generate Hash from your backend here
  String hash = HashGenerationUtils.INSTANCE.generateHashFromSDK(hashData, salt); 
  HashMap<String, String> dataMap = new HashMap<>(); 
  dataMap.put(hashName, hash); 
  hashGenerationListener.onHashGenerated(dataMap); 
  } 
  } 
  } 
  } 
  );
  ```
  ```kotlin Kotlin
   PayUCheckoutPro.open( 
          this, payUPaymentParams, 
          object : PayUCheckoutProListener { 

   
              override fun onPaymentSuccess(response: Any) { 
                  response as HashMap<*, *> 
                  val payUResponse = response[PayUCheckoutProConstants.CP_PAYU_RESPONSE]
                  val merchantResponse = response[PayUCheckoutProConstants.CP_MERCHANT_RESPONSE]  
              } 

   
              override fun onPaymentFailure(response: Any) { 
                  response as HashMap<*, *> 
                  val payUResponse = response[PayUCheckoutProConstants.CP_PAYU_RESPONSE]
                  val merchantResponse = response[PayUCheckoutProConstants.CP_MERCHANT_RESPONSE]  
              } 

   
              override fun onPaymentCancel(isTxnInitiated:Boolean) { 
              } 

   
              override fun onError(errorResponse: ErrorResponse) { 
                  val errorMessage: String 
                  if (errorResponse != null && errorResponse.errorMessage != null && errorResponse.errorMessage!!.isNotEmpty()) 
                      errorMessage = errorResponse.errorMessage!! 
                  else 
                      errorMessage = resources.getString(R.string.some_error_occurred) 
              } 
              
              override fun setWebViewProperties(webView: WebView?, bank: Any?) {
                  webView?.webViewClient = CheckoutProWebViewClient(bank as Bank, <merchant-key>)
              }
                       
              override fun generateHash( 
                  valueMap: HashMap<String, String?>, 
                  hashGenerationListener: PayUHashGenerationListener 
              ) { 
                  if ( valueMap.containsKey(CP_HASH_STRING) 
                      && valueMap.containsKey(CP_HASH_STRING) != null 
                      && valueMap.containsKey(CP_HASH_NAME) 
                      && valueMap.containsKey(CP_HASH_NAME) != null) { 
   
                      val hashData = valueMap[CP_HASH_STRING] 
                      val hashName = valueMap[CP_HASH_NAME] 
   
                      val hash: String? = 
                          HashGenerationUtils.generateHashFromSDK(hashData!!, salt) 
                      if (!TextUtils.isEmpty(hash)) { 
                          val dataMap: HashMap<String, String?> = HashMap() 
                          dataMap[hashName!!] = hash!! 
                          hashGenerationListener.onHashGenerated(dataMap) 
                      } 
                  } 
              } 
          })
  ```

  ***
</Accordion>

<Accordion title="SDK Configurations" icon="fa-code">
  To configure the CheckoutPro SDK, you can customise the properties in the PayUCheckoutProConfig class and pass the config object in the open method when invoking the SDK similar to the following code snippet:

  ```java Java
  PayUCheckoutPro.open( 
      Activity activity, 
      PayUPaymentParams payUPaymentParams, 
      PayUCheckoutProConfig payUCheckoutProConfig, 
      PayUCheckoutProListener payUCheckoutProListener) 
  ```
  ```kotlin Kotlin
  PayUCheckoutPro.open( 
      activity: Activity, 
      payUPaymentParams: PayUPaymentParams, 
      payUCheckoutProConfig: PayUCheckoutProConfig, 
      payUCheckoutProListener: PayUCheckoutProListener) 
  ```

  <Accordion title="Set Merchant Name" icon="fa-code">
    The merchant's name is displayed in the SDK indicating the recipient of the payment. The maximum length is 20 characters. To set your brand name or business name, set the `merchantName` property of the PayUCheckoutProConfig object as indicated in the following code snippet:

    ```java Java
    PayUCheckoutProConfig payUCheckoutProConfig = new PayUCheckoutProConfig(); 
    payUCheckoutProConfig.setMerchantName("PayU"); 
    ```
    ```kotlin Kotlin
    val payUCheckoutProConfig = PayUCheckoutProConfig() 
    payUCheckoutProConfig.merchantName = "PayU Payments Private Limited" 
    ```
  </Accordion>

  <Accordion title="Set Merchant Logo" icon="fa-code">
    You can display an image (typically, your brand logo) in the PayUCheckoutPro SDK to reinforce trust and display your brand to your customers. To set a logo in the SDK, you need to pass the drawable ID of the logo image resource from your app.

    Add the image in the **app/res/drawable** folder in the native Android app and pass the same under the merchantLogo.

    ```java Java
    PayUCheckoutProConfig payUCheckoutProConfig = new PayUCheckoutProConfig(); 
    payUCheckoutProConfig.setMerchantLogo(R.drawable.merchant_logo); 
    ```
    ```kotlin Kotlin
    val payUCheckoutProConfig = PayUCheckoutProConfig() 
    payUCheckoutProConfig.merchantLogo = R.drawable.merchant_logo 
    ```
  </Accordion>

  <Accordion title="Show/Hide Merchant Logo" icon="fa-code">
    Merchants want to show the logo on the PayU Hosted Page. By default, the logo is invisible.

    ```java Java
    PayUCheckoutProConfig payUCheckoutProConfig = new PayUCheckoutProConfig();
    payUCheckoutProConfig.setShowMerchantLogo(true); //true/false
    ```
    ```kotlin Kotlin
    val payUCheckoutProConfig = PayUCheckoutProConfig() 
    payUCheckoutProConfig.showMerchantLogo = true //true/false
    ```
  </Accordion>

  <Accordion title="Show/Hide Saved Card Features" icon="fa-code">
    Merchants want to hide Saved Card features. By default, the Saved Card feature is enabled.

    ```java Java
    PayUCheckoutProConfig payUCheckoutProConfig = new PayUCheckoutProConfig();
    payUCheckoutProConfig.setEnableSavedCard(true); //true/false
    ```
    ```kotlin Kotlin
    val payUCheckoutProConfig = PayUCheckoutProConfig() 
    payUCheckoutProConfig.enableSavedCard = true //true/false
    ```
  </Accordion>

  <Accordion title="Disable Screen Protection" icon="fa-code">
    Screen protection is enabled by default to hide sensitive information during screen recording or screenshots. When enabled, card details and credentials will be protected and not visible in screen captures.

    If you need to disable this protection (not recommended), set the value to false. When disabled, sensitive information will be visible in screen recordings and screenshots.

    ```java Java
    PayUCheckoutProConfig payUCheckoutProConfig = new PayUCheckoutProConfig();
    payUCheckoutProConfig.setProtectedScreen(false); // Disable protection (NOT RECOMMENDED)
    ```
    ```kotlin Kotlin
    val payUCheckoutProConfig = PayUCheckoutProConfig() 
    payUCheckoutProConfig.isProtectedScreen = false // Disable protection (NOT RECOMMENDED)
    ```
    
    ⚠️ **Security Warning:** Disabling screen protection may expose sensitive payment information in screenshots and recordings.
  </Accordion>

  <Accordion title="Customize UPI Apps Order" icon="fa-code">
    You can customize the display order of UPI payment apps. Define the sequence using a pipe-separated format to rearrange how UPI apps appear to users.

    ```java Java
      PayUCheckoutProConfig payUCheckoutProConfig = new PayUCheckoutProConfig();
      payUCheckoutProConfig.setUpiAppsOrder("phonepe|paytm|gpay");
    ```
    ```kotlin Kotlin
    val payUCheckoutProConfig = PayUCheckoutProConfig() 
    payUCheckoutProConfig.upiAppsOrder = "phonepe|paytm|gpay"
    ```
  </Accordion>

  <Accordion title="Show SSL Dialog Alert" icon="fa-code">
    you are trying to show the dialog from a place that isn't permitted.

    ```java Java
    PayUCheckoutProConfig payUCheckoutProConfig = new PayUCheckoutProConfig();
    payUCheckoutProConfig.setEnableSslDialog(true); //true/false
    ```
    ```kotlin Kotlin
    val payUCheckoutProConfig = PayUCheckoutProConfig() 
    payUCheckoutProConfig.enableSslDialog = true //true/false
    ```

    . The error message is shown as received from the SSL error description

    <Image align="center" src="https://files.readme.io/c19a750-MicrosoftTeams-image_8.png" width="200px" />
  </Accordion>

  <Accordion title="Hide the Toolbar in the Custom Browser (CB)" icon="fa-code">
    Merchants can choose to hide the toolbar on the custom browser. By default, the toolbar is displayed.

    ```java JAVA
    PayUCheckoutProConfig payUCheckoutProConfig = new PayUCheckoutProConfig (); 
    payUCheckoutProConfig.setShowCbToolbar(false); //hide toolbar 
    ```
    ```kotlin Kotlin
    val payUCheckoutProConfig = PayUCheckoutProConfig() 
    payUCheckoutProConfig.showCbToolbar = false //hide toolbar 
    ```
  </Accordion>

  <Accordion title="Hide Checkout Screen Back Button Dialog Box" icon="fa-code">
    You can choose to hide the dialog box that is displayed when the back button is clicked from the Level 1 screen. The default value is true.

    ```java Java
    PayUCheckoutProConfig payUCheckoutProConfig = new PayUCheckoutProConfig (); 
    payUCheckoutProConfig.setShowExitConfirmationOnCheckoutScreen(false); //hide back button dialog 
    ```
    ```kotlin Kotlin
    val payUCheckoutProConfig = PayUCheckoutProConfig () 
    payUCheckoutProConfig.showExitConfirmationOnCheckoutScreen = false//hide back button dialog 
    ```
  </Accordion>

  <Accordion title="Hide CB Back Button Dialog Box" icon="fa-code">
    You can choose to hide the dialog box that is displayed when the back button is clicked in CB. The default value is true.

    ```java Java
    PayUCheckoutProConfig payUCheckoutProConfig = new PayUCheckoutProConfig(); 
    payUCheckoutProConfig.setShowExitConfirmationOnPaymentScreen(false); //hide back button dialog 
    ```
    ```kotlin Kotlin
    PayUCheckoutProConfig payUCheckoutProConfig = new PayUCheckoutProConfig(); 
    payUCheckoutProConfig.setShowExitConfirmationOnPaymentScreen(false); //hide back button dialog 
    ```
  </Accordion>

  <Accordion title="Runtime SMS Permission" icon="fa-code">
    If you do not want Checkout Pro SDK to ask for runtime SMS permission on the bank OTP page, you can configure the runtime SMS permission flag to false. The default value is true.

    ```java Java
    val payUCheckoutProConfig = PayUCheckoutProConfig () 
    payUCheckoutProConfig.showExitConfirmationOnPaymentScreen= false //hide back button dialog 
    ```
    ```kotlin Kotlin
    PayUCheckoutProConfig payUCheckoutProConfig = new PayUCheckoutProConfig(); 
    payUCheckoutProConfig.setMerchantSmsPermission(false);  
    ```
  </Accordion>

  <Accordion title="Auto Select OTP" icon="fa-code">
    Merchants can choose to auto-select OTP flow on the bank page with the following flag. The default value is false.

    ```java Java
    PayUCheckoutProConfig payUCheckoutProConfig = new PayUCheckoutProConfig(); 
    payUCheckoutProConfig.setAutoApprove(true);  
    ```
    ```kotlin Kotlin
    val payUCheckoutProConfig = PayUCheckoutProConfig () 
    payUCheckoutProConfig.autoSelectOtp = true 
    ```
  </Accordion>

  <Accordion title="Merchant Response Timeout" icon="fa-code">
    The period that PayU will wait for you to load surl/furl before passing the transaction response back to the app. If you take longer to load surl/furl, by default, PayU has a response timeout of 10 seconds. However, if you feel that surl/furl can take longer than 10 seconds, you can set this flag.

    ```java Java
    PayUCheckoutProConfig payUCheckoutProConfig = new PayUCheckoutProConfig(); 
    payUCheckoutProConfig.setMerchantResponseTimeout(15000); // for 15 seconds timeout 
    ```
    ```kotlin Kotlin
    val payUCheckoutProConfig = PayUCheckoutProConfig() 
    payUCheckoutProConfig.merchantResponseTimeout = 15000 // for 15 seconds timeout 
    ```
  </Accordion>

  <Accordion title="Waiting for OTP Timeout" icon="fa-code">
    We wait for a specified time for the OTP after which the SDK falls back to the manual OTP screen. The default time is 30 seconds; you may change it to any other duration. PayU recommends you configure it to less than 60 seconds for a better user experience.

    ```java Java
    PayUCheckoutProConfig payUCheckoutProConfig = new PayUCheckoutProConfig(); 
    payUCheckoutProConfig.setWaitingTime(45000); 
    ```
    ```kotlin Kotlin
    PayUCheckoutProConfig payUCheckoutProConfig = PayUCheckoutProConfig()  
    payUCheckoutProConfig.waitingTime = 45000
    ```
  </Accordion>

  <Accordion title="Enable Surepay on the Bank Page" icon="fa-code">
    Merchants can enable Surepay on the bank page. When the internet is lost during the transaction, if the transaction can be retried from that bank page after the internet is resumed, the Surepay dialog box is displayed. It has legitimate values such as 0, 1, 2, and 3. Where number defines the number of times the Surepay dialog box should be displayed during the transaction for no internet connectivity. The default value is 0.

    ```java Java
    PayUCheckoutProConfig payUCheckoutProConfig = new PayUCheckoutProConfig(); 
    payUCheckoutProConfig.setSurePayCount(3); 
    ```
    ```kotlin Kotlin
    val payUCheckoutProConfig = PayUCheckoutProConfig () 
    payUCheckoutProConfig.surePayCount = 3 
    ```
  </Accordion>

  <Accordion title="Review Order" icon="fa-code">
    You can pass the checkout order details to the SDK that will be displayed in the SDK during the transaction flow.

    ```java Java
    ArrayList<OrderDetails> orderDetailsList = new ArrayList<>(); 
    orderDetailsList.add(new OrderDetails("Milk","1")); 
    orderDetailsList.add(new OrderDetails("Butter","1")); 
    PayUCheckoutProConfig payUCheckoutProConfig = new PayUCheckoutProConfig (); 
    payUCheckoutProConfig.setCartDetails(orderDetailsList); 
    ```
    ```kotlin Kotlin
    val orderDetailsList = ArrayList<OrderDetails>() 
    orderDetailsList.add(OrderDetails("Milk","1")) 
    orderDetailsList.add(OrderDetails("Butter","1")) 
    val payUCheckoutProConfig = PayUCheckoutProConfig () 
    payUCheckoutProConfig.cartDetails = orderDetailsList 
    ```
  </Accordion>

  <Accordion title="Additional Payment Options in the Checkout screen" icon="fa-code">
    Consider the following example to display Google Pay, PhonePe, and Paytm on the primary checkout screen.

    ```java Java
    ArrayList<PaymentMode> checkoutOrderList = new ArrayList<>(); 
    checkoutOrderList.add(new PaymentMode(PaymentType.UPI, PayUCheckoutProConstants.CP_GOOGLE_PAY)); 
    checkoutOrderList.add(new PaymentMode(PaymentType.WALLET, PayUCheckoutProConstants.CP_PHONEPE)); 
    checkoutOrderList.add(new PaymentMode(PaymentType.WALLET, PayUCheckoutProConstants.CP_PAYTM)); 
    PayUCheckoutProConfig payUCheckoutProConfig = new PayUCheckoutProConfig (); 
    payUCheckoutProConfig.setPaymentModesOrder(checkoutOrderList);
    ```
    ```kotlin Kotlin
    val checkoutOrderList = ArrayList<PaymentMode>() 
    checkoutOrderList.add(PaymentMode(PaymentType.UPI, PayUCheckoutProConstants.CP_GOOGLE_PAY)) 
    checkoutOrderList.add(PaymentMode(PaymentType.WALLET, PayUCheckoutProConstants.CP_PHONEPE)) 
    checkoutOrderList.add(PaymentMode(PaymentType.WALLET, PayUCheckoutProConstants.CP_PAYTM)) 
    val payUCheckoutProConfig = PayUCheckoutProConfig () 
    payUCheckoutProConfig.paymentModesOrder = checkoutOrderList 
    ```
  </Accordion>

  <Accordion title="Set Checkout Payment Modes Order" icon="fa-code">
    Default payment modes order on the checkout screen is as below: Card, NetBanking, UPI, and Wallets

    Merchants can specify the checkout payment options order. For this, the merchant needs to provide a list of payment modes. Checkout order will be the order of items in the list. If not all payment modes order is mentioned in the list the other payment modes will be displayed in their default order as shown above.

    The resulting order on the initial Checkout screen will be:

    * Cards (credit/debit)
    * UPI
    * Net Banking
    * Wallets
  </Accordion>

  <Accordion title="Enforced Payment Modes" icon="fa-code">
    You can directly open a specific payment mode like NB, WALLET, UPI, CARD, etc in SDK. Create an enforcement list similar to the following code block to enforce payment modes:

    #### Enforced Single Payment option

    ```java Java
     ArrayList<HashMap<String,String>> enforceList = new ArrayList();
     HashMap<String,String> map = new HashMap<>();
     map.put(PayUCheckoutProConstants.CP_PAYMENT_TYPE, PaymentType.NB.name());
     enforceList.add(map);
    ```
    ```kotlin Kotlin
     val enforceList = ArrayList<HashMap<String,String>>()
     enforceList.add(HashMap<String,String>().apply {
               put(PayUCheckoutProConstants.CP_PAYMENT_TYPE,PaymentType.NB.name)
               put(PayUCheckoutProConstants.ENFORCED_IBIBOCODE,"AXIB")
            })
    ```

    #### Enforced Multiple Payment option

    ```java Java
    ArrayList<HashMap<String, String>> enforceList = new ArrayList();
       HashMap<String, String> map1 = new HashMap<>();
       map1.put(PayUCheckoutProConstants.CP_PAYMENT_TYPE, PaymentType.NB.name());
       enforceList.add(map1);

       HashMap<String, String> map2 = new HashMap<>();
       map2.put(PayUCheckoutProConstants.CP_PAYMENT_TYPE, PaymentType.CARD.name());
       enforceList.add(map2);
    ```
    ```kotlin Kotlin
     val enforceList = ArrayList<HashMap<String,String>>()
     enforceList.add(HashMap<String,String>().apply {
               put(PayUCheckoutProConstants.CP_PAYMENT_TYPE,PaymentType.NB.name)
             
            })
     enforceList.add(HashMap<String,String>().apply {
               put(PayUCheckoutProConstants.CP_PAYMENT_TYPE,PaymentType.CARD.name)
             
            })       
    ```

    #### Enforced Particular Bank wise Payment Mode :

    ```java Java
     ArrayList<HashMap<String,String>> enforceList = new ArrayList();
     HashMap<String,String> map = new HashMap<>();
     map.put(PayUCheckoutProConstants.CP_PAYMENT_TYPE, PaymentType.NB.name());
     map.put(PayUCheckoutProConstants.ENFORCED_IBIBOCODE, "AXIB");
     enforceList.add(map);
    ```
    ```kotlin Kotlin
     val enforceList = ArrayList<HashMap<String,String>>()
     enforceList.add(HashMap<String,String>().apply {
               put(PayUCheckoutProConstants.CP_PAYMENT_TYPE,PaymentType.NB.name)
               put(PayUCheckoutProConstants.ENFORCED_IBIBOCODE,"AXIB")
            })
    ```

    #### Enforced Particular CardType /Scheme-wise Payment Mode :

    To enforce card type as well like CC or DC, the enforce list should have a hashmap with the PaymentType and CardType keys similar to the following code block:

    ```java Java
    ArrayList<HashMap<String,String>> enforceList = new ArrayList();
     HashMap<String,String> map = new HashMap<>();
     map.put(PayUCheckoutProConstants.CP_PAYMENT_TYPE, PaymentType.CARD.name());
     map.put(PayUCheckoutProConstants.CP_CARD_TYPE, CardType.CC.name()); // CC/DC
     map.put(PayUCheckoutProConstants.CP_CARD_SCHEME, CardScheme.MAST.name())
     enforceList.add(map);
    ```
    ```kotlin Kotlin
     val enforceList = ArrayList<HashMap<String,String>>()
     enforceList.add(HashMap<String,String>().apply {
    put(PayUCheckoutProConstants.CP_PAYMENT_TYPE,PaymentType.CARD.name)
    put(PayUCheckoutProConstants.CP_CARD_TYPE,CardType.CC.name)
    put(PayUCheckoutProConstants.CP_CARD_SCHEMA, CardScheme.AMEX.name)
            })
    ```

    | Enforced Payment Mode | Key                                        | Value                       |
    | :-------------------- | :----------------------------------------- | :-------------------------- |
    | Card                  | PayUCheckoutProConstants.CP\_PAYMENT\_TYPE | PaymentType.CARD.name()     |
    | Net Banking           | PayUCheckoutProConstants.CP\_PAYMENT\_TYPE | PaymentType.NB.name()       |
    | Wallet                | PayUCheckoutProConstants.CP\_PAYMENT\_TYPE | PaymentType.WALLET.name()   |
    | UPI                   | PayUCheckoutProConstants.CP\_PAYMENT\_TYPE | PaymentType.UPI.name()      |
    | EMI                   | PayUCheckoutProConstants.CP\_PAYMENT\_TYPE | PaymentType.EMI.name()      |
    | NEFT / RTGS           | PayUCheckoutProConstants.CP\_PAYMENT\_TYPE | PaymentType.NEFTRTGS.name() |
    | Buy Now Pay Later     | PayUCheckoutProConstants.CP\_PAYMENT\_TYPE | PaymentType.BNPL.name()     |

    Kindly refer to the below link to get the list of [Bank and Card code](https://docs.payu.in/docs/bank-and-card-codes-for-integration) details
  </Accordion>
</Accordion>
