---
title: Handling 3DS Secure 2.0 Transaction
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: Handling 3DS Secure 2.0 Transaction
  description: >-
    PayU supports 3DS Secure 2.0 transactions with Merchant Hosted Checkout
    integration, requiring the inclusion of `threeDS2RequestData` in the JSON
    format for card payments.
  robots: index
next:
  description: ''
---
PayU supports 3DS Secure 2.0 transaction with Merchant Hosted Checkout integration. This section provides the information relevant to 3DS Secure 2.0 transaction.

## Request Parameters for 3DS Secure 2.0 Transaction

Along with the parameters mentioned in the [Collect Payment API - Cards (Merchant Hosted Checkout)](ref:https://docs.payu.in/reference/_payment_merchant_hosted_cards), you must include the `threeDS2RequestData` parameter in the following JSON format for 3DS Secure 2.0 support for cards:

```plaintext
 "browserInfo": {
        "userAgent": "Mozilla\/5.0 (X11 Linux x86_64) AppleWebKit\/537.36 (KHTML, like Gecko) HeadlessChrome\/93.0.4577.0 Safari\/537.36",
        "acceptHeader": "*\/*",
        "language": "en-US",
        "colorDepth": "24",
        "screenHeight": "600",
        "screenWidth": "800",
        "timeZone": "-300",
        "javaEnabled": true,
        "ip": "10.248.2.71"
    }
```

### 3DS Secure 2.0 browserDetails JSON Fields Description

| **Field**    | **Description**                                                                             | **Example**      |
| ------------ | ------------------------------------------------------------------------------------------- | ---------------- |
| userAgent    | This field must include user agent of the device browser.                                   |                  |
| acceptHeader | This field contains the format of the header.                                               | application/json |
| language     | This field contains the language for the 3D Secure Challenge.                               | en-US            |
| colorDepth   | This field contains the color depth of the screen.                                          | 24               |
| screenHeight | This field contains the screen height of the device displaying the 3D Secure Challenge.     | 640              |
| screenWidth  | This field contains the screen width of the device displaying the 3D Secure Challenge.      | 480              |
| javaEnabled  | This field contains whether Java is enabled for the device. It can be any of the following: | true             |
| timeZone     | This field contains the time zone code where the payment is accepted.                       | 273              |
| ip           | This should include the IP address of the device from which the browser is accessed.        | 10.248.2.71      |

### Sample cURL Request with 3DS Secure 2.0

The sample cURL request with 3DS Secure 2.0:

```curl
curl --location 'https://test.payu.in/_payment' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e' \
--data-urlencode 'key=JF****g' \
--data-urlencode 'firstname=Ashish' \
--data-urlencode 'email=test@example.com' \
--data-urlencode 'amount=10' \
--data-urlencode 'phone= 9876543210' \
--data-urlencode 'productinfo=Product_info' \
--data-urlencode 'surl=http://pp30admin.payu.in/test_response' \
--data-urlencode 'furl=http://pp30admin.payu.in/test_response' \
--data-urlencode 'pg=CC' \
--data-urlencode 'bankcode=CC' \
--data-urlencode 'lastname=Test' \
--data-urlencode 'ccname=Test User' \
--data-urlencode 'ccvv=123' \
--data-urlencode 'ccexpmon=06' \
--data-urlencode 'ccexpyr=2024' \
--data-urlencode 'txnid=jYhbOYH9o4' \
--data-urlencode 'hash=e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184' \
--data-urlencode 'ccnum=4012000000002004' \
--data-urlencode 'txn_s2s_flow=4' \
--data-urlencode 'threeDS2RequestData={
    "browserInfo": {
        "userAgent": "Mozilla\/5.0 (X11 Linux x86_64) AppleWebKit\/537.36 (KHTML, like Gecko) HeadlessChrome\/93.0.4577.0 Safari\/537.36",
        "acceptHeader": "*\/*",
        "language": "en-US",
        "colorDepth": "24",
        "screenHeight": "600",
        "screenWidth": "800",
        "timeZone": "-300",
        "javaEnabled": true,
        "ip": "10.248.2.71"
    }
}'
```