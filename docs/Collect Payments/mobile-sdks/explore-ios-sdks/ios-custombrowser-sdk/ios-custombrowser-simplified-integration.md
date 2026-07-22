---
title: Simplified Integration
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
---
title: Simplified Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: >-
    Simplified PayU Custom Browser iOS integration: minimal setup steps, payment request, hash, surl/furl, and quick sandbox test.
  keywords:
    - payu ios custom browser simplified integration steps
    - ios custom browser sdk simplified checkout integration payu
    - integrate custom browser ios simplified guide payu india
    - iphone payment sdk simplified custom browser payu gateway
    - payment gateway ios simplified sdk integration payu browser
    - payu custom browser ios quick integration developer guide
    - mobile payment sdk ios simplified webview checkout payu
    - ios webview payment simplified integration custom browser
    - payu ios custombrowser simplified setup hash integration
    - native ios custom browser simplified payment sdk payu
    - ios in app payment simplified custom browser sdk payu
    - swift ios custom browser simplified integration guide payu
  robots: index
next:
  description: ''
---
You can use PayU’s view controller, that is, `PUCBWebVC` for making payment. This view controller creates a `UIWebView` or `WKWebview` based on configuration and loads it to facilitate payment.

## Using Cocoapods

1. Add the following line to Podfile:` PayUIndia-Custom-Browser`
2. Execute the following command: `pod install`

<Callout icon="📘" theme="info">
  **Integrate the latest Custom Browser SDK**: PayU recommends that you integrate the latest version of Custom Browser SDK. To check the latest version, refer to PayU Github Release page.
</Callout>

### Reinstall Custom Browser on latest Cocoapods release

If the above procedure installs the older version of the Custom Browser's pod, use the following steps to reinstall CB with the latest release.

1. Uninstall older CB and remove the following line from your pod file: `PayUIndia-Custom-Browser`
2. Execute the following command: `pod install`
3. Update the pods local repository using the following command: `pod repo update`
4. Clean the pods cache using the following command: `pod cache clean --all`
5. Download CB from the following location and install CB: [https://github.com/payu-intrepos/Documentations/wiki/9.-iOS-Custom-Browser/\_edit#using-cocoapods](https://github.com/payu-intrepos/Documentations/wiki/9.-iOS-Custom-Browser/_edit#using-cocoapods)