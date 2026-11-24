---
title: WebView for Mobile Apps
excerpt: Android WebView settings from the Checkout Plus WebView article
deprecated: false
hidden: true
updatedAt: "2026-11-17"
metadata:
  title: Checkout Plus WebView for Mobile Apps | PayU Developer Docs
  description: >-
    Hidden Android WebView notes for opening a PayU checkout URL from a mobile
    app. The Bolt payment modal is not recommended inside a WebView or Custom Tab.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">

Checkout Plus is not recommended for app browsers such as WebView or Chrome Custom Tabs. This page is the existing Android WebView article. It loads a checkout URL. It does not call `bolt.launch()`.

For a redirection checkout inside an app, use [PayU Hosted Checkout WebView](../payu-hosted-checkout-1/payu-hosted-checkout-webview-integration).

</Callout>

<!-- VALIDATION NEEDED: The Checkout Plus integrate page says not to use Checkout Plus in a WebView, and it linked this article. This article's body says you reuse PayU Hosted Checkout by opening the checkout form in a WebView. The two pages describe different integrations. -->

You can collect payments from a mobile app by opening the PayU checkout form in a WebView. The current article says this lets you reuse a PayU Hosted Checkout integration.

The article links to an iOS section. That section was never written. Only Android is below.

## Before You Configure the WebView

The Android steps assume you already have a checkout URL to load. The published snippet does not name that URL.

<!-- DOCUMENTATION GAP: The load call is the placeholder webView.loadUrl(<"pass the URL>). The Checkout Plus pages do not document which URL to pass. Do not substitute a PayU endpoint that is not written here. -->

## Android — WebView Settings

Enable JavaScript, DOM storage, and the related settings from the published snippet.

```java
webView.getSettings().setJavaScriptEnabled(true);
webView.getSettings().setDomStorageEnabled(true);
webView.getSettings().setLoadWithOverviewMode(true);
webView.setVerticalScrollBarEnabled(true);
webView.getSettings().setMultiScreenEnable(true);
```

## Android — Load the Checkout URL

```java
webView.loadUrl(<"pass the URL>);
```

<!-- DOCUMENTATION GAP: Replace the placeholder only when the docs team confirms the URL this WebView should open. -->

## Android — WebViewClient

Set the client so the app can follow URLs inside the WebView:

```java
mWebView.setWebViewClient(new MyWebViewClient());
```

The published client does three things:

1. `shouldOverrideUrlLoading()` runs when the WebView is about to load a URL. The article says to use it to override the default behaviour and handle the URL for UPI intents.
2. `onPageFinished()` runs when a page has finished loading. The article says to use it for success and failure.
3. `onPageStarted()` runs when a page starts loading. The article says it can show a loading indicator or run other work before the page loads.

<Accordion title="Published MyWebViewClient" icon="fa-code">

```java
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

</Accordion>

The article says `shouldOverrideUrlLoading()` should support UPI intents. The method body in the sample loads every URL inside the WebView. It does not show an intent hand-off.

<!-- DOCUMENTATION GAP: No UPI intent-filter or deep-link sample is included beyond the package <queries> list below. -->

## Android — Return from Another App

```java
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

Both branches in the published sample say to call the Verify Payment API. The sample does not show the request.

## Android — UPI App Package Names

Add this block in the manifest, outside the `application` tag. These are the package names published on the Checkout Plus WebView page.

```xml
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

## iOS

<!-- DOCUMENTATION GAP: The legacy page links to #webview-integration-for-ios and contains no iOS steps, Swift sample, or WKWebView configuration. Do not write iOS steps until a Checkout Plus source exists. -->
