---
title: WebView Integration in Android
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
### Add WebView configurations

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

### Create postData for Payment

 for Payment

Build a string with the payment parameters and pass it as `postData`. For more information on the payment parameters, refer to [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout).

```plaintext
 
“key=xxxxx&txnid=1686124341291&amount=1.0&firstname=John&productinfo=PayU&email=testUser@gmail.com&phone=7879311111&surl=https://payu.herokuapp.com/success&furl=https://payu.herokuapp.com/failure&hash=8e083ea3ec9c8d50ea9c77e157e95f91701f720c7a67f6b26bafd9c4bfd879b1c38e807285de77807ad9d5281ad56c7bf0faeb2b45a8b2f80f635a242a0fa054”
```

**Note:** We recommend that you compute the hash at your server so to prevent cyber attackers from tampering your requests.

### Load PayU Checkout form in WebView

```java
 webView.postUrl("URL", postData);
```

Pass the postData to load the PayU checkout form with the transaction data using _postUrl_() method.

[block:parameters]
{
  "data": {
    "h-0": "URL",
    "h-1": "String. The endpoint of the API.  \nTest URL: <https://test.payu.in/_payment>  \nProduction URL: <https://secure.payu.in/_payment>",
    "0-0": "postData",
    "0-1": "byte. Create the postData and send it in this field. The value of this parameter cannot be null."
  },
  "cols": 2,
  "rows": 1,
  "align": [
    "left",
    "left"
  ]
}
[/block]


### Set WebViewClient

Set the WebViewClient of the WebView object to a new instance of the WebViewClient class to manipulate the loading of the URLs in the WebView.

**Step 1: Add WebViewClient class in WebView**

1. Set the WebView’s client to a new instance of the WebViewClient class. Add the following methods of the WebViewClient class or handling interactions with the WebView: 
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

#### Step 2 Add the PSP apps package Name inside the manifest file

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

### Display alert message (Optional)

Add the following configuration to display an alert message when user clicks on the back button on the browser:

```java
 webView.setWebChromeClient(new WebChromeClient());
```

## Handle in Chrome Custom Tab

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

### FAQ

#### 1. Variable  should be set as true in session for fallback to work

 \-> PayuHandleIntent should be set as true in session for fallback to work.

#### 2. Some issues arise when merchants configure their system to close the webview whenever an error occurs on the checkout page

\-> Merchant need not to handel such error like ERR_BLOCKED_BY_ORB , let webview default behaviour handle it

#### 3. Integration Code of Webview - Given above

#### 4. WebView loading again and again

\-> Call webview.loadUrl(url) only once in a session like in OnCreate of Activity or fragment(once in a session) , Please do not loadURL in onResume. 

#### 5. Do we need to add  configuration  to use checkout to  use local storage

\-> WebSettings.domStorageEnabled = true 

#### 6. User was not redirected to merchant page after making success payments.

\-> Need to implement webchromeClient with payuhandleIntent 

```
view!!.evaluateJavascript(  
  "sessionStorage.setItem(\"payuHandleIntent\", true);sessionStorage.setItem(\"payuCBVersion\", \"1.0.0\");"  
) { s ->  
  Log.d("LogName", s!!) // Prints: "this"  
        }
```

and need to open new url in new webView or merchant need to call activity.startActivityForResult(intent,101) instead of  mWebView.context.startActivity(intent) launch intent  and listen psp app response in activity in onActivityResult 

#### 7. In the ICP checkout being opened within a webview inside the application. This configuration is leading to unexpected and unusual behavior, likely due to the way the webview is interacting with the ICP checkout

\-> Merchant needs to pass userAgent in webViewSetting -  (webSettings.userAgentString = userAgent)

Example value of userAgent - Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36

#### 8. CSS Issues: Since different merchants use various languages in their applications, CSS issues have occasionally been reported in Flutter applications. While the layout may display correctly in web browsers like Safari and Chrome, it sometimes encounters problems when viewed in a Flutter webview. Eg android:windowSoftInputMode="adjustResize" - if in manifest file this is not added, keyboard opens on top of input field.

 \-> This may be due to wrong User Agent. always pass right User Agent to webView

#### 9. How to handle window.open in Webview

\-> First set for multiple window in webview setting `webSettings.setSupportMultipleWindows(true)` and then set webview client for same and override onCreateWindow function. In onCreateWindow create new webView.

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