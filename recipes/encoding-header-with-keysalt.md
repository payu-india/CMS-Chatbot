---
title: Encoding Header with Key/Salt
description: Recipe Description
hidden: false
recipe:
  color: '#018FF4'
  icon: 🦉
---
```javascript JavaScript
var CryptoJS = require("crypto-js"); // Include this if you're running this in a Node.js environment

var merchant_key = '<key>';
var merchant_secret = '<salt or secret>';

// date
var date = new Date().toUTCString();

// request data - define this as per your requirements
var request = {
    'data': '<your data here>'
};

// authorization
var authorization = getAuthHeader(date);

function getAuthHeader(date) {
    var AUTH_TYPE = 'sha512';
    var data = request['data'].trim().length === 0 ? "" : request['data'];
    var hash_string = data + '|' + date + '|' + merchant_secret;
    console.log("Hash String is ", hash_string);
    var hash = CryptoJS.SHA512(hash_string).toString(CryptoJS.enc.Hex);
    var authHeader = 'hmac username="' + merchant_key + '", ' +
        'algorithm="' + AUTH_TYPE + '", headers="date", signature="' + hash + '"';
    return authHeader;
}

console.log(authorization);
```

```json Response Example
{"success":true}
```

# Variable Declarations:

<!-- javascript@3-4 -->

The merchant_key and merchant_secret variables are declared and assigned placeholder values. These would typically be your merchant key and secret provided by your payment gateway or API provider.

# Date Generation

<!-- javascript@7 -->

A new Date object is created and converted to a UTC string. This is often used as part of the data to be hashed to ensure that the hash changes over time and cannot be reused.

# Authorization Header Generation

<!-- javascript@15 -->

The getAuthHeader function is called with the date as an argument. The result is stored in the authorization variable.

# getAuthHeader Function

<!-- javascript@17-26 -->

