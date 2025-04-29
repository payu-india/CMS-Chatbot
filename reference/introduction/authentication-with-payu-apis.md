---
title: Authentication Header for v2 APIs
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: Authentication with PayU APIs
  description: >-
    Learn how to securely authenticate and integrate with PayU India’s APIs.
    Explore topics such as merchant keys, salt, REST API authentication, hash
    parameters, and SHA512 encryption. Enhance your payment gateway integration
    with PayU’s robust security features.
  keywords:
    - PayU India API authentication
    - Merchant key and salt for PayU APIs
    - REST API authentication with PayU
    - Hash parameter in PayU API requests
    - SHA512 encryption for PayU API security
    - Reverse hashing using PayU node SDK
    - Generate hash for PayU API parameters
  robots: index
next:
  description: ''
---
The PayU India API requires authentication using a merchant key and a salt. When you post requests using any of the PayU APIs, you will be posting the merchant key as the first parameter, so separate authentication is not required because these are REST APIs  All requests are accompanied by a hash that is appended at the end of the request. While posting parameters for an API, the hash parameter in each API must contain the hash value to be calculated at your end. The following hash logic used in PayU India APIs:

<V2_paymentHeader />
