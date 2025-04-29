---
title: Webview Integration in iOS
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
### Create postData for Payment

Build a string with the payment parameters and pass it as postData. See Collect Payment API to learn more about the payment parameters.

```plaintext
 
“key=xxxxxx&txnid=1686124341291&amount=1.0&firstname=John&productinfo=PayU&email=testUser@gmail.com&phone=7879311111&surl=https://payu.herokuapp.com/success&furl=https://payu.herokuapp.com/failure&hash=8e083ea3ec9c8d50ea9c77e157e95f91701f720c7a67f6b26bafd9c4bfd879b1c38e807285de77807ad9d5281ad56c7bf0faeb2b45a8b2f80f635a242a0fa054”
```

**Note:** We recommend that you compute the hash at your server so to prevent cyber attackers from tampering your requests.

### Load PayU checkout form in WebView

Make a POST request to PayU endpoint by creating a URLRequest object and set its httpMethod property to “POST”.

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

### Display alert message (Optional)

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

## UPI intent for WebView – iOS

To support UPI intent in WebView:

## Step 1: Add LSApplicationQueriesSchemes

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
</array> 
```

Each string in the array is the name of the PSP apps (in lowercase) for which you want to enable the UPI intent.

## Step 2: Handle DeepLinks

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

### UPI in SafariViewController

For SafariViewController just need to present SFSafariViewController with payment URL, Intent handling is done by Safari itself.

```swift
 guard let url = URL(string: urlString) else { return }  
            let safariVC = SFSafariViewController(url: url)  
            present(safariVC, animated: true, completion: nil)
```

### FAQ

#### 1. Do we need to add configuration to use checkout to use local storage -

```
webView.configuration.websiteDataStore = WKWebsiteDataStore.default()
```

#### 2. In the ICP checkout being opened within a webview inside the application. This configuration is leading to unexpected and unusual behavior, likely due to the way the webview is interacting with the ICP checkout:

 Set Correct User Agent String value otherwise may get unexpected UI and function Issues in custom webView. Ex:- For IOS device (Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1).

#### 3. Some issues arise when merchants configure their system to close the webview whenever an error occurs on the checkout page Eg ERR_BLOCKED_BY_ORB:

This may be because web Page is not loaded/rendered properly. this type of error can be ignored.

#### 4. Integration Code of WebView - Given above.

#### 5. Merchant App Issues: After successfully completing a transaction on checkout using UPI, everything functioned smoothly. Following a proper socket connection response, the user was redirected to a secure page. However, instead of being redirected to either the success URL (surl) or failure URL (furl)

 Make sure to write Url load logic inside viewDidLoad() function, never write logic inside  viewWillDisappear() function.

#### 6. User was not redirected to merchant page after making success payments.

Always use Universal links and set proper surl and furl values

#### 7. payuHandleIntent should be set as true in session for fallback to work. Intent is fired differently in custom browsers.

Set `self.webView.evaluateJavaScript("sessionStorage.setItem('payuHandleIntent', true)")` and Intent app will be open if proper Queried schemes added in info.plist

#### 8. CSS Issues: Since different merchants use various languages in their applications, CSS issues have occasionally been reported in Flutter applications. While the layout may display correctly in web browsers like Safari and Chrome, it sometimes encounters problems when viewed in a Flutter webview. Eg android:windowSoftInputMode="adjustResize"

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

extension WebViewController: WKScriptMessageHandler {

```
func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {

   print("User message got") }}
```

#### 10. How to handle window.open in Webview

As webview did not support multiple tab need to implement below function and create new webview to handle window.open()

```
func webView(_ webView: WKWebView, createWebViewWith configuration: WKWebViewConfiguration, for navigationAction: WKNavigationAction, windowFeatures: WKWindowFeatures) -> WKWebView? {
    
    let calledWebView = WKWebView(frame: self.sharedVars.calledView.frame, configuration: configuration)
    
    calledWebView.navigationDelegate = self.vcToPresentAlert as? WKNavigationDelegate
    calledWebView.uiDelegate = self.vcToPresentAlert as? WKUIDelegate
    
    return calledWebView
}

```