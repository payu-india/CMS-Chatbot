---
title: Cocoapods Integration
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
CocoaPods manages library dependencies for your Xcode projects. The dependencies for your projects are specified in a single text file called a `podfile`. For more information on installing CocoaPods, refer to the CocoaPods Documentation. This section describes the following to integrate with CocoaPods:

* Integrate with CocoaPods
* Integrate using Swift Package Manager

## Integrate with CocoaPods

To integrate with CocoaPods:

1. Navigate inside your project directory from the terminal: `cd path/to/your/project`
2. Create a pod file using the following command on the terminal: `nano Podfile`

The editor is displayed on the terminal.

3. Add the following code in the editor: 

```
target 'YourProjectName' do
pod 'PayUIndia-PG-SDK'
end
```

Where ‘YourProjectName’ must be substituted with your project name.

4. Press the Ctrl+X key to save and close the editor.
5. Enter the following command on the terminal: `pod install`
6. Navigate to your project folder and open `<YourProjectName>.xcworkspace`.

You will find PayUIndia-PG-SDK in this pods folder.

***

## Integrate using Swift Package Manager

You can integrate PayUIndia-PG-SDK with your app or SDK using the following methods:

1. **Using Xcode** — Navigate to the File > Add Package menu and add the package in the following GitHub location: [https://github.com/payu-intrepos/iOS-SDK](https://github.com/payu-intrepos/iOS-SDK)
2. **Using Package.Swift**: Add the following line to Package.swift dependencies: `.package(name: "PayUIndia-PG-SDK", url: "https://github.com/payu-intrepos/iOS-SDK", from: "7.1.0")`