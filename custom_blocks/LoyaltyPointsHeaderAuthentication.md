---
name: LoyaltyPointsHeaderAuthentication
---
---
name: LoyaltyPointsHeaderAuthentication
---

All PayU Loyalty Points API requests require **HMAC-SHA512** header authentication.

### Required request headers

| Header | Description |
| :----- | :---------- |
| Content-Type | `application/json` |
| Accept | `application/json` |
| mid | Merchant ID (MID) provided by PayU during onboarding. Some Loyalty Points APIs accept `MID` instead of `mid`. |
| Date | Current UTC timestamp in RFC 1123 format (for example, `Fri, 24 Jul 2026 05:51:20 GMT`). |
| Authorization | HMAC signature. Format: `hmac username="<merchant_key>", algorithm="sha512", headers="date", signature="<computed_signature>"`. For field descriptions, refer to [authorization fields description](#authorization-fields-description). |

#### authorization fields description

| Parameter | Description |
| --------- | ----------- |
| username | Merchant key provided by PayU during onboarding. |
| algorithm | Hashing algorithm used for the signature. Use `sha512`. |
| headers | Headers included in the signature. Use `date`. |
| signature | SHA-512 hash of the signing string, in lowercase hexadecimal. For more information, refer to [hashing algorithm](#hashing-algorithm). |

#### hashing algorithm

Build the signing string using the **exact raw JSON request body** sent with the request:

```
sha512(<raw_request_body>|<Date>|<merchant_secret>)
```

Where:

* `<raw_request_body>` is the exact JSON body string posted with the request.
* `<Date>` is the same value sent in the `Date` header.
* `<merchant_secret>` is the merchant Salt provided by PayU during onboarding.

Convert the SHA-512 output to **lowercase hexadecimal** and pass it as `signature` in the `Authorization` header:

```
hmac username="<merchant_key>", algorithm="sha512", headers="date", signature="<signature>"
```

#### Signing rules

* Use the exact raw JSON request body.
* The `Date` value in the signature must exactly match the `Date` header.
* Regenerate `Date` and `Authorization` for every request.

<Accordion title="Sample header authentication code" icon="fa-code">
  ```javascript
  var merchant_key = 'YOUR_MERCHANT_KEY';
  var merchant_secret = 'YOUR_MERCHANT_SALT';

  // date
  var date = new Date();
  date = date.toUTCString();

  // authorization
  var authorization = getAuthHeader(date);
  console.log(authorization);

  function getAuthHeader(date) {
    var AUTH_TYPE = 'sha512';
    var data = isEmpty(request['data']) ? "" : request['data'];
    var hash_string = data + '|' + date + '|' + merchant_secret;
    console.log("Hash String is ", hash_string);
    var hash = CryptoJS.SHA512(hash_string).toString(CryptoJS.enc.Hex);
    var authHeader = 'hmac username="' + merchant_key + '", ' +
      'algorithm="' + AUTH_TYPE + '", headers="date", signature="' + hash + '"';
    return authHeader;
  }

  function isEmpty(obj) {
    for (var key in obj) {
      if (obj.hasOwnProperty(key)) return false;
    }
    return true;
  }
  ```
</Accordion>
