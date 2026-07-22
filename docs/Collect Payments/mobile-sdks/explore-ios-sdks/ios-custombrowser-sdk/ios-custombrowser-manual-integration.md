---
title: Manual Integration
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
title: Manual Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: >-
    Manually integrate PayU Custom Browser iOS SDK: download framework, Xcode linking, headers, and WebView payment checkout setup.
  keywords:
    - payu ios custom browser manual integration guide india
    - ios custom browser sdk manual framework integration payu
    - integrate custom browser ios manually xcode payu sdk
    - iphone payment sdk manual integration custom browser payu
    - payment gateway ios manual sdk integration steps payu
    - payu custom browser ios framework manual install guide
    - mobile payment sdk ios manual custom browser integration
    - ios webview payment manual sdk integration payu gateway
    - payu ios custombrowser manual xcode linking integration
    - native ios custom browser manual payment sdk payu
    - ios in app payment manual custom browser integration payu
    - swift objective c custom browser manual sdk payu ios
  robots: index
next:
  description: ''
---
To integrate with CustomBrowser in iOS manually:

1. Download the latest custom browser archive from the following PayU Github location and extract it:
   [https://github.com/payu-intrepos/iOS-Custom-Browser/releases](https://github.com/payu-intrepos/iOS-Custom-Browser/releases)
2. Drag and drop PayUCustomBrowser.framework into your project.
3. Add `libz.tbd` libraries into your project target’s build phases.
4. Add` SystemConfiguration` framework into your project target’s Build Phases.
5. Add -ObjC in Other Linker Flags in Project Build Settings.
6. Add PayUCustomBrowser.framework in Embedded Binaries in General Settings.

After the CustomBrowser library is added to your project, you can go ahead and use it to make payments.

**Import PayU SDK**

While working with a Swift project, add the above code in the `Bridging-Header.h` file. This is applicable to Objective-C or Swift programming language.

```objectivec Objective-C
#import <PayUCustomBrowser/PayUCustomBrowser.h>
```

<br />