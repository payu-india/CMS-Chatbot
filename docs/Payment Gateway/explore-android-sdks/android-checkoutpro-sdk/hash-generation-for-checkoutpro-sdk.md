---
title: Generate Dynamic Hash
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
<DynamicHashGeneration />

## V2 Hashes

For passing V2 dynamic hashes, you will receive a call on the generateHash method of `PayUCheckoutProListener`.

In the method parameter, you will receive a dictionary or hashMap, and extract the value of hashString and hashType from that. if hashType is “V2” Pass that value to the server, and now the server generate sha256 hash with salt as key and hashString as signedString over it. The server will give that hash back to your app, and the app will provide that hash to PayU through a callback mechanism.
