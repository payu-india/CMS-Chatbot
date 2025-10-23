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

### Payment API

While posting parameters for an API, the **hash** parameter in each API must contain the hash value to be calculated at your end. You must hash the request parameters using the following hash logic:

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
```

Where, sha512 is the encryption method used here. For more information on SHA, refer to [Wikipedia](https://en.wikipedia.org/wiki/SHA-2). For more information on hashing for **_payment** API, refer to  <a href="generate-hash-merchant-hosted" target="_blank"> Generate Hash</a>.

<Callout icon="📘" theme="info">
  **Reference**: You can use the Hash API of the PayU node SDK on Github to perform reverse hashing. Refer to the [PayU node SDK Readme](https://github.com/payu-india/payu-sdk-node/blob/main/README.md), download and install the PayU node SDK from the [PayU node SDK Github location](https://github.com/payu-india/payu-sdk-node).
</Callout>

### General APIs

While posting parameters for an API, the **hash** parameter in each API must contain the hash value to be calculated at your end. The string used for calculating the hash is mentioned below for command based APIs:

```plaintext
sha512(key|command|var1|salt)
```

Where, sha512 is the encryption method used here. For more information on SHA, refer to [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).
