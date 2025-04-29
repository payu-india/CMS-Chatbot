---
title: API Authentication and Security
excerpt: >-
  When you are posting requests using any of the PayU APIs, you will be posting
  the merchant key as the first parameter, so separate authentication is not
  required because these are REST APIs. For testing purposes, you can use the
  Test merchant key. For Integration APIs, use “JPTXg” as the Test merchant key.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
All the requests are accompanied by hash that is appended at the end of the request.

## Security

While posting parameters for an API, the **hash** parameter in each API must contain the hash value to be calculated at your end. The string used for calculating the hash is mentioned below:

```plaintext
sha512(key|command|var1|salt)
```

Where, sha512 is the encryption method used here. For more information on SHA, refer to [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).

> 📘 Note:
>
> You can use the Hash API of the PayU node SDK on Github to perform reverse hashing. Refer to the [PayU node SDK Readme](https://github.com/payu-india/payu-sdk-node/blob/main/README.md), download and install the PayU node SDK from the [PayU node SDK Github location](https://github.com/payu-india/payu-sdk-node).
