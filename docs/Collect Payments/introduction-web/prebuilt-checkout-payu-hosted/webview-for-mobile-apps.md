---
title: Integrate WebView for Mobile Apps
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Integrate WebView for Mobile Apps with PayU Hosted Checkout
  description: >-
    Discover seamless integration of PayU Hosted Checkout with WebView for
    Mobile Apps. This document offers comprehensive steps to effortlessly
    incorporate PayU's secure payment solutions into your mobile app's WebView.
    Elevate user experience by enabling smooth and secure transactions through
    PayU's WebView integration, detailed in this document.
  robots: index
next:
  description: ''
---
WebView is a component that enables mobile apps to collect payments by loading the PayU checkout form within the app itself, rather than redirecting users to external browsers. It essentially embeds PayU's Hosted Checkout experience inside a WebView container within your mobile app. WebView essentially bridges the gap between web-based payment forms and native mobile app experiences, making payments feel more integrated and professional within your mobile application.

You can collect payments from your mobile apps by opening the the PayU checkout form in a WebView. This allows you to reuse your PayU Hosted Checkout integration and get started quickly.

## Key Characteristics:

1. **Embedded Payment Experience**: Users can complete payments without leaving your app, providing a seamless user experience.

2. **Reuses Existing Integration**: Developers can leverage their existing PayU Hosted Checkout integration, reducing implementation complexity.

3. **Cross-Platform Support**: Available for both Android (using WebView) and iOS (using WKWebView), with platform-specific optimizations.

4. **Comprehensive Payment Methods**: Supports all PayU payment options including:
   * Credit/Debit cards
   * UPI payments
   * Digital wallets
   * Buy Now Pay Later (BNPL) options

## How It Works

1. **Configure WebView settings** (enable JavaScript, DOM storage, etc.)
2. **POST payment data** to PayU endpoints with transaction details
3. **Handle navigation and intents** for UPI apps like Google Pay, PhonePe
4. **Manage success/failure scenarios** within the app

## Benefits

* **Better User Experience**: No app switching or external browser redirects
* **Faster Implementation**: Reuse existing PayU integration
* **Security**: Server-side hash generation for transaction authentication
* **UPI Intent Support**: Seamless integration with popular payment apps

## Configure Native Webview and Chrome Custom Tab for Android

<Accordion title="Add WebView configurations" icon="fa-code">
  To open the PayU checkout page in a WebView, add the following configurations in your Android project to allow JavaScript, DOM, and other features.

  ```java Kotlin
  val webSettings: WebSettings = mWebView.settings
  webSettings.javaScriptEnabled = true
  webSettings.builtInZoomControls = true
  webSettings.domStorageEnabled = true
  webSettings.useWideViewPort = true
  webSettings.loadWithOverviewMode = true
  webSettings.setSupportMultipleWindows(true)
  ```
</Accordion>

<Accordion title="Create postData for Payment" icon="fa-code">
  for Payment

  Build a string with the payment parameters and pass it as `postData`. For more information on the payment parameters, refer to [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout).

  ```curl
   
  "key=xxxxx&txnid=1686124341291&amount=1.0&firstname=John&productinfo=PayU&email=testUser@gmail.com&phone=7879311111&surl=https://payu.herokuapp.com/success&furl=https://payu.herokuapp.com/failure&hash=8e083ea3ec9c8d50ea9c77e157e95f91701f720c7a67f6b26bafd9c4bfd879b1c38e807285de77807ad9d5281ad56c7bf0faeb2b45a8b2f80f635a242a0fa054"
  ```

  **Note:** We recommend that you compute the hash at your server so to prevent cyber attackers from tampering your requests.
</Accordion>

<Accordion title="Load PayU Checkout form in WebView" icon="fa-code">
  ```java
   webView.postUrl("URL", postData);
  ```

  Pass the postData to load the PayU checkout form with the transaction data using *postUrl*() method.

  <Table align={["left","left"]}>
    <thead>
      <tr>
        <th>
          URL
        </th>

        <th>
          String. The endpoint of the API.

          Test URL:

          [https://test.payu.in/\_payment](https://test.payu.in/_payment)

          Production URL:

          [https://secure.payu.in/\_payment](https://secure.payu.in/_payment)
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          postData
        </td>

        <td>
          byte. Create the postData and send it in this field. The value of this parameter cannot be null.
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>

<Accordion title="Set WebViewClient" icon="fa-code">
  Set the WebViewClient of the WebView object to a new instance of the WebViewClient class to manipulate the loading of the URLs in the WebView.

  **Step 1: Add WebViewClient class in WebView**

  1. Set the WebView's client to a new instance of the WebViewClient class. Add the following methods of the WebViewClient class or handling interactions with the WebView:
  2. `shouldOverrideUrlLoading()`\_—\_method is called when the WebView is about to load a URL. The method is used to override the default behavior and handle the URL request to support UPI intents.
  3. `onPageFinished()`\_—\_method is called when the WebView has finished loading a page. The method is used to handle the success and failure scenarios of the request.
  4. `onPageStarted()`\_—\_method is called when the WebView starts loading a page. The method can be used to show a loading indicator or perform any other necessary actions before the page starts loading.

  ```java Kotlin
       private fun initWebViewClient(mWebView: WebView){
           mWebView.webViewClient = object : WebViewClient() {

               override fun shouldOverrideUrlLoading(view: WebView, url: String): Boolean {
                   try {
                       handleIntentFlow(url, view)
                   } catch (e: Exception) {
                       Log.e("intent", "Can't resolve url " + e.localizedMessage, e)
                   }
                   return false
               }

               override fun onPageFinished(view: WebView?, url: String?) {
                   super.onPageFinished(view, url)
                   
               }
             
             override fun onReceivedSslError(view: WebView?, handler: SslErrorHandler?, error: SslError?) {
      					Log.e(TAG, "Error: ${error.toString()}")
     						 handler?.proceed()
  						}

               override fun doUpdateVisitedHistory(view: WebView?, url: String?, isReload: Boolean) {
                   view?.requestFocus()
                   view?.setOnKeyListener(View.OnKeyListener { v, keyCode, event ->
                       if (keyCode == KeyEvent.KEYCODE_BACK && (event.action == MotionEvent.ACTION_UP || event.action == MotionEvent.ACTION_DOWN)) {
                           if (view.canGoBack()) {
                               view.goBack()
                           } else {
                               viewModel.onBackPress()
                           }
                           return@OnKeyListener true
                       }
                       return@OnKeyListener false
                   })
                   super.doUpdateVisitedHistory(view, url, isReload)
               }
           }
       }

  		private fun handleIntentFlow(url: String, mWebView: WebView): Boolean {
          if (url.startsWith("intent://")) {
              val intent = Intent.parseUri(url, Intent.URI_INTENT_SCHEME)
              if (intent != null) {
                  val packageManager = mWebView.context.packageManager
                  val info = packageManager.resolveActivity(
                      intent,
                      PackageManager.MATCH_DEFAULT_ONLY
                  )
                  if (info != null) {
                      mWebView.context.startActivity(intent)
                      // if merchant want to listen psp app response in activity
                      // activity.startActivityForResult(intent,101) 
                  } else {
                      val fallbackUrl =
                          intent.getStringExtra(Constant.BROWSER_FALLBACK_URL)
                      if (!fallbackUrl.isNullOrEmpty()) {
                          mWebView.loadUrl(fallbackUrl)
                      }
                  }
                  return true
              }
          } else if (url.startsWith("upi://")) {
              val intent = Intent(Intent.ACTION_VIEW, Uri.parse(url))
              mWebView.context.startActivity(intent)
              return true
          }
          return false
      }


  ```
  ```Text Java
  private class MyWebViewClient extends WebViewClient { 
   @Override 
   public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) { 
   String url = request.getUrl().toString(); 
   //Generic Intent flow   
   if (url.contains("upi://pay")) { 
   try { 
   	Intent intent = new Intent(Intent.ACTION_VIEW); 
   	intent.setData(Uri.parse(url)); 
   	startActivity(intent);
     return true; 
   }catch (Exception e){ 
  	 view.loadUrl(url); 
   } 
   // Handling the Specific Intent flow  
   }else if (url.startsWith("intent://")) {
         try {
          Context context = view.getContext();
          Intent intent = Intent.parseUri(url, Intent.URI_INTENT_SCHEME);
           if (intent != null) {
              PackageManager packageManager = context.getPackageManager();
              ResolveInfo info = packageManager.resolveActivity(intent, PackageManager.MATCH_DEFAULT_ONLY);
               if (info != null) {
                 context.startActivity(intent);
                } else {
                   String fallbackUrl = intent.getStringExtra("browser_fallback_url");
                    view.loadUrl(fallbackUrl);
                 }
            return true;
        }
     } catch (URISyntaxException e) {
           Log.e(TAG, "Can't resolve intent://", e);
       }
   }
   return false; 
   } 
   
   @Override 
   public void onPageFinished(WebView view, String url) { 
   	Log.d(TAG, "onPageFinished: " + url); 
   } 
   
   @Override 
   public void onPageStarted(WebView view, String url, Bitmap favicon) { 
   super.onPageStarted(view, url, favicon); 
   	Log.d(TAG, "onPageStarted: " + url); 
   } 
   
   @Override
   public void onReceivedSslError(WebView view, SslErrorHandler handler, SslError error) {   
   	Log.e(TAG, "Error: " + error.toString());    
   	handler.proceed();
   }
   
   @Override 
   public void onReceivedError(WebView view, WebResourceRequest request, WebResourceError error) { 
   super.onReceivedError(view, request, error); 
   	Log.d(TAG, "onPageFinished: " + error.toString()); 
   } 
  } 
  ```

  <Accordion title="Step 2 Add the PSP apps package Name inside the manifest file" icon="fa-code">
    Please add the below line of code from the manifest file, outside of the application tag.

    ```
    <queries>
        <intent>
           <action android:name="android.intent.action.VIEW" />
           <category android:name="android.intent.category.BROWSABLE" />
             <data
                android:host="pay"
                android:scheme="upi" />
        </intent>
    </queries>

    ```
  </Accordion>
</Accordion>

<Accordion title="Display alert message (Optional)" icon="fa-code">
  Add the following configuration to display an alert message when user clicks on the back button on the browser:

  ```java
   webView.setWebChromeClient(new WebChromeClient());
  ```
</Accordion>

<Accordion title="Handle in Chrome Custom Tab" icon="fa-code">
  Open url in cct(chrome custom tab) -

  ```
  val builder = CustomTabsIntent.Builder()  
  val customBuilder = builder.build()  
  if (context.isPackageInstalled("com.android.chrome")) {  
    // if chrome is available use chrome custom tabs  
    customBuilder.intent.setPackage(CHROME_PACKAGE_NAME)  
    uri.let { customBuilder.launchUrl(context, Uri.parse(it)) }  
  } else {  
    Toast.makeText(context,"Chrome is not installed ",Toast.LENGTH_LONG).show()  
  }
  ```

  Code to check if chrome is installed -

  ```
   private fun Context.isPackageInstalled(packageName: String): Boolean {  
          // check if chrome is installed or not  
          return try {  
              packageManager.getPackageInfo(packageName, 0)  
              true  
          } catch (e: PackageManager.NameNotFoundException) {  
              false  
          }  
      }
  ```
</Accordion>

<Accordion title="FAQ" icon="fa-code">
  1. Variable  should be set as true in session for fallback to work

     -> PayuHandleIntent should be set as true in session for fallback to work.

  2. Some issues arise when merchants configure their system to close the webview whenever an error occurs on the checkout page

     -> Merchant need not to handle such error like ERR\_BLOCKED\_BY\_ORB , let webview default behaviour handle it

  3. WebView loading again and again

     -> Call webview\.loadUrl(url) only once in a session like in OnCreate of Activity or fragment(once in a session) , Please do not loadURL in onResume.

  4. Do we need to add  configuration  to use checkout to  use local storage

     -> WebSettings.domStorageEnabled = true

  5. User was not redirected to merchant page after making success payments.

     -> Need to implement webchromeClient with payuhandleIntent

     ```
     view!!.evaluateJavascript(  
       "sessionStorage.setItem("payuHandleIntent", true);sessionStorage.setItem("payuCBVersion", "1.0.0");"  
     ) { s ->  
       Log.d("LogName", s!!) // Prints: "this"  
             }
     ```

     and need to open new url in new webView or merchant need to call activity.startActivityForResult(intent,101) instead of  mWebView\.context.startActivity(intent) launch intent  and listen psp app response in activity in onActivityResult

  6. In the ICP checkout being opened within a webview inside the application. This configuration is leading to unexpected and unusual behavior, likely due to the way the webview is interacting with the ICP checkout

     -> Merchant needs to pass userAgent in webViewSetting -  (webSettings.userAgentString = userAgent)

     Example value of userAgent - Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36

  7. CSS Issues: Since different merchants use various languages in their applications, CSS issues have occasionally been reported in Flutter applications. While the layout may display correctly in web browsers like Safari and Chrome, it sometimes encounters problems when viewed in a Flutter webview. Eg android:windowSoftInputMode="adjustResize" - if in manifest file this is not added, keyboard opens on top of input field."

     -> This may be due to wrong User Agent. always pass right User Agent to webView

  8. How to handle window\.open in Webview

     -> First set for multiple window in webview setting `webSettings.setSupportMultipleWindows(true)` and then set webview client for same and override onCreateWindow function. In onCreateWindow create new webView.

     ```
       // To support multiple windows
             myWebView.setWebChromeClient(new WebChromeClient() {
                 @Override
                 public boolean onCreateWindow(WebView view, boolean isDialog, boolean isUserGesture, android.os.Message resultMsg) {
                     WebView newWebView = new WebView(MainActivity.this);
                     newWebView.getSettings().setJavaScriptEnabled(true);
                     newWebView.setWebChromeClient(this);
                     newWebView.setWebViewClient(new WebViewClient()); // optional
                     
                     // Open a new WebView in a dialog or new activity (simplified example)
                     view.addView(newWebView);
                     resultMsg.obj.setWebView(newWebView);
                     resultMsg.sendToTarget();
                     return true;
                 }

                 @Override
                 public void onCloseWindow(WebView window) {
                     // Remove the WebView
                     window.setVisibility(View.GONE);
                     // Optionally, remove it from the parent as well
                 }
             });
     ```
</Accordion>

## Webview Native Integration on iOS

<Accordion title="Create postData for Payment" icon="fa-code">
  Build a string with the payment parameters and pass it as postData. See Collect Payment API to learn more about the payment parameters.

  ```plaintext
   
  "key=xxxxxx&txnid=1686124341291&amount=1.0&firstname=John&productinfo=PayU&email=testUser@gmail.com&phone=7879311111&surl=https://payu.herokuapp.com/success&furl=https://payu.herokuapp.com/failure&hash=8e083ea3ec9c8d50ea9c77e157e95f91701f720c7a67f6b26bafd9c4bfd879b1c38e807285de77807ad9d5281ad56c7bf0faeb2b45a8b2f80f635a242a0fa054"
  ```

  **Note:** We recommend that you compute the hash at your server so to prevent cyber attackers from tampering your requests.
</Accordion>

<Accordion title="Load PayU checkout form in WebView" icon="fa-code">
  Make a POST request to PayU endpoint by creating a URLRequest object and set its httpMethod property to "POST".

  Build a postString with the payment parameters and set the `httpBody` property of the URLRequest object to the postString. Set the `javaScriptCanOpenWindowsAutomatically` property of the webView object to `true` to allow the webView object to open new windows automatically. Finally load the `URLRequest` object in the webView.

  ```swift
  webView.navigationDelegate = self  
  webView.customUserAgent = userAgent // if youb are setting custom agent, please make sure mentioning correct one
  var request = URLRequest(url: URL(string: "https://secure.payu.in/_payment") !)
  request.httpMethod = "POST"
  let postString = "key=******&txnid=9sbcsjhsf9637&productinfo=iPhoneXS&amount=1&email=admin%40gmail.com&firstname=John&lastname=&surl=https%3A%2F%2Fpayu.herokuapp.com%2Fios_success&furl=https%3A%2F%2Fpayu.herokuapp.com%2Fios_failure&hash=3547411bc86e1a96bbb9985debc8786b14f43b2a7604f08a82420d2d0336f708dfa54734332c91418400bbfdf6249761567e3281d28589a8c6748ce40e367fb5"
  request.httpBody = postString.data(using: .utf8)
  webView.configuration.preferences.javaScriptCanOpenWindowsAutomatically = true
  webView.load(request)
  ```
</Accordion>

<Accordion title="Display alert message (Optional)" icon="fa-code">
  Add the following configuration to display an alert message when user clicks on the back button on the browser:

  ```swift
   func webView(_ webView: WKWebView, runJavaScriptConfirmPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping(Bool) - > Void) {
       let alertController = UIAlertController(title: nil, message: message, preferredStyle: .alert)
       alertController.addAction(UIAlertAction(title: "OK", style: .default, handler: {
           (action) in completionHandler(true)
       }))
       alertController.addAction(UIAlertAction(title: "Cancel", style: .default, handler: {
           (action) in completionHandler(false)
       }))
       present(alertController, animated: true, completion: nil)
   }
  ```
</Accordion>

<Accordion title="UPI intent for WebView – iOS" icon="fa-code">
  To support UPI intent in WebView:

  <Accordion title="Step 1: Add LSApplicationQueriesSchemes" icon="fa-code">
    To allow your application to support UPI intent, you must add the PSP applications for which you want to enable UPI intents to the **LSApplicationQueriesSchemes** in the info.plist file of your project.

    ```plaintext
    <key>LSApplicationQueriesSchemes</key> 
    <array> 
    		<string>phonepe</string>
    		<string>bhim</string>
    		<string>tez</string>
    		<string>paytm</string>
    		<string>gpay</string>
    		<string>credpay</string>
    		<string>icici</string>
    		<string>myairtel</string>
    		<string>payzapp</string>
    		<string>axismobile</string>
    		<string>freecharge</string>
        <string>slice-upi</string>
    		<string>olamoney</string>
    		<string>sbiyono</string>
        <string>kmb</string>
        <string>navipay</string>
    </array> 
    ```

    Each string in the array is the name of the PSP apps (in lowercase) for which you want to enable the UPI intent.

    Note:- If a new app is onboarded during checkout the corresponding PSP (Payment Service Provider) scheme must be added to the Info.plist file to support the new app intent.
  </Accordion>

  <Accordion title="Step 2: Handle DeepLinks" icon="fa-code">
    Here, the `decidePolicyFor` method checks if the URL in the naviagtion action is an HTTP or HTTPS schema. If it is not, then the code checks if UIApplication can open the URL.  it is needed when new url loaded in webView and also handle intent flow.

    ```swift
    class WebViewController: UIViewController, WKNavigationDelegate {
        func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {
            if  let url = navigationAction.request.url, !url.absoluteString.hasPrefix("http://"), !url.absoluteString.hasPrefix("https://") {
                if UIApplication.shared.canOpenURL(url) {
                    UIApplication.shared.open(url, options: [:], completionHandler: nil)
                    decisionHandler(WKNavigationActionPolicy.cancel)
                    return
                } else if url.absoluteString.contains("browser_fallback_url=") {
                    let fallbackURLString = url.absoluteString.components(separatedBy: "browser_fallback_url=").last
                    let fallbackURL = URL(string: fallbackURLString?.removingPercentEncoding ?? "")
                    if fallbackURL != nil && (url.absoluteString != fallbackURLString) {
                        if (url.absoluteString != fallbackURLString) {
                            webView.load(URLRequest(url: fallbackURL!))
                            decisionHandler(WKNavigationActionPolicy.cancel)
                            return
                        }
                    }
                    decisionHandler(WKNavigationActionPolicy.allow);
                    return;
                }
            }
            decisionHandler(WKNavigationActionPolicy.allow);
        }
     }

      func webView(_ webView: WKWebView,
                     didStartProvisionalNavigation navigation: WKNavigation!)
    {
      self.webView.evaluateJavaScript("sessionStorage.setItem('payuHandleIntent', true)") 
      { (result, error) -> Void in
      	 print("Finished evaluateJavaScript.")
      }
    }
    ```

    <Accordion title="UPI in SafariViewController" icon="fa-code">
      For SafariViewController just need to present SFSafariViewController with payment URL, Intent handling is done by Safari itself.

      ```swift
       guard let url = URL(string: urlString) else { return }  
                  let safariVC = SFSafariViewController(url: url)  
                  present(safariVC, animated: true, completion: nil)
      ```
    </Accordion>
  </Accordion>
</Accordion>

<Accordion title="FAQ" icon="fa-code">
  #### 1. Do we need to add configuration to use checkout to use local storage -

  ```
  webView.configuration.websiteDataStore = WKWebsiteDataStore.default()
  ```

  #### 2. In the ICP checkout being opened within a webview inside the application. This configuration is leading to unexpected and unusual behavior, likely due to the way the webview is interacting with the ICP checkout:

  Set Correct User Agent String value otherwise may get unexpected UI and function Issues in custom webView. Ex:- For IOS device (Mozilla/5.0 (iPhone; CPU iPhone OS 12\_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1).

  #### 3. Some issues arise when merchants configure their system to close the webview whenever an error occurs on the checkout page Eg ERR\_BLOCKED\_BY\_ORB:

  This may be because web Page is not loaded/rendered properly. this type of error can be ignored.

  #### 4. Integration Code of WebView - Given above.

  #### 5. Merchant App Issues: After successfully completing a transaction on checkout using UPI, everything functioned smoothly. Following a proper socket connection response, the user was redirected to a secure page. However, instead of being redirected to either the success URL (surl) or failure URL (furl)

  Make sure to write Url load logic inside viewDidLoad() function, never write logic inside  viewWillDisappear() function.

  #### 6. User was not redirected to merchant page after making success payments.

  Always use Universal links and set proper surl and furl values

  #### 7. payuHandleIntent should be set as true in session for fallback to work. Intent is fired differently in custom browsers.

  Set `self.webView.evaluateJavaScript("sessionStorage.setItem('payuHandleIntent', true)")` and Intent app will be open if proper Queried schemes added in info.plist

  #### 8. CSS Issues: Since different merchants use various languages in their applications, CSS issues have occasionally been reported in Flutter applications. While the layout may display correctly in web browsers like Safari and Chrome, it sometimes encounters problems when viewed in a Flutter webview. Eg android:windowSoftInputMode=

  If in manifest file this is not added, keyboard opens on top of input field. :- This may be due to wrong User Agent. always pass right User Agent to webView

  #### 9. Sending Data from WKWebview's Webpage to Native Code

  To achieve this, the WKWebview needs to have a WKUserContentController configured that uses message handlers. Here is a sample configuration and definition. ex. let controller = WKUserContentController()

  ```
      controller.add(self, name: "observe")

      let configuration = WKWebViewConfiguration()

      configuration.userContentController = controller

      webView = WKWebView(frame: view.frame, configuration: configuration)
  ```

  In the above example, "observe" defines the message thread over which the Javascript code can call a native swift method

  a simple string is sent from Javascript to native swift code via WKScriptMessageHandler interface

  extension WebViewController: WKScriptMessageHandler \{

  ```
  func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {

     print("User message got") }}
  ```

  #### 10. How to handle window\.open in Webview

  As webview did not support multiple tab need to implement below function and create new webview to handle window\.open()

  ```
  func webView(_ webView: WKWebView, createWebViewWith configuration: WKWebViewConfiguration, for navigationAction: WKNavigationAction, windowFeatures: WKWindowFeatures) -> WKWebView? {
      
      let calledWebView = WKWebView(frame: self.sharedVars.calledView.frame, configuration: configuration)
      
      calledWebView.navigationDelegate = self.vcToPresentAlert as? WKNavigationDelegate
      calledWebView.uiDelegate = self.vcToPresentAlert as? WKUIDelegate
      
      return calledWebView
  }

  ```
</Accordion>

<br />

## Webview Flutter Integration on Android/IOS

<Accordion title="Add below dependencies in pubspec.yaml file" icon="fa-code">

  ```Dependencies
 dependencies:
 flutter:
 sdk: flutter
 url_launcher: ^6.3.1
 webview_flutter: ^4.13.0
  ```
</Accordion>

<Accordion title="Import necessary packages" icon="fa-code">
  ```Packages
import 'package:webview_flutter/webview_flutter.dart';
import 'package:url_launcher/url_launcher.dart';
  ```
</Accordion>

<br />

<Accordion title="Create postData for Payment" icon="fa-code">
  for Payment

  Build a string with the payment parameters and pass it as `postData`. For more information on the payment parameters, refer to [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout).

  ```curl
   
  "key=xxxxx&txnid=1686124341291&amount=1.0&firstname=John&productinfo=PayU&email=testUser@gmail.com&phone=7879311111&surl=https://payu.herokuapp.com/success&furl=https://payu.herokuapp.com/failure&hash=8e083ea3ec9c8d50ea9c77e157e95f91701f720c7a67f6b26bafd9c4bfd879b1c38e807285de77807ad9d5281ad56c7bf0faeb2b45a8b2f80f635a242a0fa054"
  ```

  **Note:** We recommend that you compute the hash at your server so to prevent cyber attackers from tampering your requests.
</Accordion>


<Accordion title="Set up WebView with UPI launch capability" icon="fa-code">
  ```Packages
      ..setNavigationDelegate(
        NavigationDelegate(
          onNavigationRequest: (NavigationRequest request) async {
            debugPrint("request_url: ${request.url}");
            final url = request.url;
            if (!url.startsWith('http://') && !url.startsWith('https://')) {
              final ok = await _launchUpiIntent(url);
              debugPrint("UPI launch result: $ok");
              return NavigationDecision.prevent;
            }
            return NavigationDecision.navigate;
          },
        ),
      )
  ```
</Accordion>
