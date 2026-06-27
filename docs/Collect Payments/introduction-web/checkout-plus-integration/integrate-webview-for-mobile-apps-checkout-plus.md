---
title: Integrate WebView for Mobile Apps (Checkout Plus)
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
You can collect payments from your mobile apps by opening the the PayU checkout form in a WebView. This allows you to reuse your PayU Hosted Checkout integration and get started quickly.

- [Configure WebView for Android](#webview-integration-for-android)
- [Configure WebView for iOS](#webview-integration-for-ios)

## WebView integration for Android

### Add WebView configurations

To open the PayU checkout page in a WebView, add the following configurations in your Android project to allow JavaScript, DOM, and other features.

```java
webView.getSettings().setJavaScriptEnabled(true);
webView.getSettings().setDomStorageEnabled(true);
webView.getSettings().setLoadWithOverviewMode(true);
webView.setVerticalScrollBarEnabled(true);
webView.getSettings().setMultiScreenEnable(true);
```

### Load PayU Checkout form in WebView

```
 webView.loadUrl(<"pass the URL>);
```

### Set MyWebViewClient

Set the MyWebViewClient of the WebView object to a new instance of the MyWebViewClient class to manipulate the loading of the URLs in the WebView.

```
mWebView.setWebViewClient(new MyWebViewClient());
```

**Step 1: Add WebViewClient class in WebView**

1. Set the WebView’s client to a new instance of the WebViewClient class. Add the following methods of the WebViewClient class or handling interactions with the WebView: 
2. `shouldOverrideUrlLoading()`\_—\_method is called when the WebView is about to load a URL. The method is used to override the default behavior and handle the URL request to support UPI intents.  
3. `onPageFinished()`\_—\_method is called when the WebView has finished loading a page. The method is used to handle the success and failure scenarios of the request. 
4. `onPageStarted()`\_—\_method is called when the WebView starts loading a page. The method can be used to show a loading indicator or perform any other necessary actions before the page starts loading.

```Text Java
private class MyWebViewClient extends WebViewClient { 
    @Override
    public boolean onCreateWindow(WebView view, boolean isDialog, boolean isUserGesture, Message resultMsg) {
        WebView newWebView = new WebView(MainActivity.this);
        mWebView.addView(newWebView, ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT);
        WebView.WebViewTransport transport = (WebView.WebViewTransport) resultMsg.obj;
        transport.setWebView(newWebView);
        resultMsg.sendToTarget();
        newWebView.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                Log.d(TAG, "shouldOverrideUrlLoading: "+url);
                view.loadUrl(url);
                return true;
            }

            @Override
            public void onPageStarted(WebView view, String url, Bitmap favicon) {
                super.onPageStarted(view, url, favicon);
             }

            @Override
            public void onPageFinished(WebView view, String url) {
                super.onPageFinished(view, url);
            }
        });
        newWebView.setWebChromeClient(new WebChromeClient() {
            @Override
            public void onCloseWindow(WebView window) {
                super.onCloseWindow(window);
                if (newWebView != null) {
                    mWebView.removeView(newWebView);
                 }
            }
        });
        return true;
     }
}
```

#### Step 2 Handling the rerun callback for Specific Intent

```
@Override
protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    Log.d(TAG, "onActivityResult: " + data);
    if (requestCode == 1002) {
     // Call verify Payment API
    } else {
        // Call verify Payment API
    }
}

```

#### Step 3 Add the PSP apps package Name inside the manifest file

Please add the below line of code from the manifest file, outside of the application tag.

```
<queries>
    <package android:name="com.google.android.apps.nbu.paisa.user" />
    <package android:name="com.phonepe.app" />
    <package android:name="in.org.npci.upiapp" />
    <package android:name="net.one97.paytm" />
    <package android:name="in.amazon.mShop.android.shopping" />
    <package android:name="com.whatsapp" />
    <package android:name="com.epifi.paisa" />
    <package android:name="money.jupiter" />
    <package android:name="indwin.c3.shareapp" />
    <package android:name="com.dreamplug.androidapp" />
    <package android:name="com.mobikwik_new" />
    <package android:name="org.altruist.BajajExperia" />
    <package android:name="in.gokiwi.kiwitpap" />
</queries>
```

<br />
