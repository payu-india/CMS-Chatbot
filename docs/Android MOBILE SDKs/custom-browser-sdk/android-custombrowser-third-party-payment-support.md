---
title: Third-Party Payment Support
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
If you want to make payments by any third-party payment application, such as GooglePay, PhonePe, Samsung Pay, etc, you have to include the changes as described in this section.

## Google Pay

### Integration

Configure the following in the payment post data:

* Bank code parameter with the value as TEZ
* PG parameter with the value of as UPI

### Gradle dependency

Add the following dependency in the application’s build.gradle.

```
implementation 'in.payu:payu-gpay:3.1.5'
```

## PhonePe

## Integration

Configure the following in the payment post data:

* Bankcode parameter with the value as PPINTENT.
* PG parameter with the value as CASH.

### Gradle dependency

Add the PhonePeIntent SDK URL in the root project’s build.gradle similar to the following:

```
allprojects {
  repositories {
    maven {
    url "https://phonepe.mycloudrepo.io/public/repositories/phonepe-intentsdk-android"
    }
  }
}
```

Add the following dependency in your application’s build.gradle:

```
implementation 'in.payu:phonepe-intent:1.8.4'
```