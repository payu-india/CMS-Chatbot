---
title: Install and Configure the SDK
excerpt: >-
  To get started with the POS SDK follow the installation process mentioned
  below:
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Prerequisites

* Java JDK (Java Development Kit).
* Eclipse ADT (Android Development Tool with Android SDK).

***

## Installation

Add dependency libraries \*.aar into your existing Android project libs folder.

> 👍 Callout!
>
> If your project does not already have a libs folder, create one in the root of the project by\
> right clicking the project and choosing New and then Folder and add latest PayUsdk `aar’s` into libs folder in the demo source code

***

## Configuration

Add the following configurations to start working with PayU’s POS Android SDK.

### App build.gradle Configuration

Add the following code to the build.gradle folder of your project

```Text JAVA
compile files('libs/mPaySdk_2.0.3_15072019.aar')
implementation 'com.google.code.gson:gson:2.8.2'
compile group: 'org.codehaus.jackson', name: 'jackson-core-asl', version: '1.9.13'
compile group: 'commons-io', name: 'commons-io', version: '2.4'
compile group: 'commons-lang', name: 'commons-lang', version: '2.3'
compile group: 'de.mindpipe.android', name: 'android-logging-log4j', version: '1.0.3'
compile group: 'log4j', name: 'log4j', version: '1.2.17'
compile group: 'org.codehaus.jackson', name: 'jackson-mapper-asl', version: '1.9.13'
compile group: 'org.bouncycastle', name: 'bcprov-ext-jdk15on', version: '1.54'
packagingOptions {
exclude 'META-INF/LICENSE'
exclude 'META-INF/ASL2.0'
exclude 'VERSION.txt'
}
```

***

## App manifest configuration

```Text JAVA
<uses-permission android:name="android.permission.BLUETOOTH" />
<uses-permission android:name="android.permission.BLUETOOTH_ADMIN" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.ACCESS_MOCK_LOCATION" />
<uses-permission android:name="android.permission.BATTERY_STATS" />
<uses-permission android:name="android.permission.CALL_PHONE" />
<uses-permission android:name="android.permission.MANAGE_NEWLAND"/>
<uses-permission android:name="android.permission.MANAGE_NEWLANDUART3"/>
```

***

## Pro-guard configuration

```Text JAVA
-keep class com.pnsol.sdk.newland.listener.** { *; }
-keep class com.pnsol.sdk.auth.** {*;}
-keep class com.pnsol.sdk.payment.PaymentInitialization {*;}
-keep class com.pnsol.sdk.payment.PaymentProcessThread {*;}
-keep class com.pnsol.sdk.payment.PaymentModeThread {*;}
-keep class com.pnsol.sdk.payment.** {*;}
-keep class com.pnsol.sdk.qpos.listener.QPOSListener {*;}
-keep class com.pnsol.sdk.payment.MiuraUpdates {*;}
-keep class com.pnsol.sdk.interfaces.** {*;}
-keep class com.pnsol.sdk.enums.** {*;}
-keep class com.pnsol.sdk.miura.emv.tlv.ISOUtil {*;}
-keep class com.pnsol.sdk.miura.response.ResponseManager {*;}
-keep class com.pnsol.sdk.miura.messages.Message {*;}
-keep class com.pnsol.sdk.usb.USBClass{*;}
-keep class com.dspread.xpos.BLE.** { *; }
-keep class com.pnsol.sdk.util.** { *; }
-keep class com.newland.mpos.payswiff.**{*;}
-keep class org.codehaus.jackson.** { *; }
-keep class com.pnsol.sdk.n910.** { *; }
-keep class com.pnsol.sdk.n3.** { *; }
-keep class android.a.a.** { *; }
-keep class android.misc.** { *; }
-keep class android.newland.** { *; }
-keep class android.psam.** { *; }
-keep class com.a.a.** { *; }
-keep class com.newland.** { *; }
-keep class com.nlscan.android.scan.** { *; }
```

***

## Go live requirements

To go live with the SDK:

Configure Merchant Salt and Merchant Key at Development Phase.\
Get in touch with the integration team to get the production SDK.
