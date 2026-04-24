---
name: HeaderAuthentication
---
| Parameter     | Description                                                                                                                                                                           |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| date          | The current date and time. For example,  format of the date is Wed, 28 Jun 2023 11:25:19 GMT.                                                                                         |
| authorization | The actual HMAC signature generated using the specified algorithm (sha512) and includes the hashed data. For more information, refer to authorization fields description table below. |

<Accordion title="authorization fields description" icon="fa-table">
  | Parameter | Description                                                                                                                                                                      |
  | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | username  | Represents the username or identifier for the client or merchant, in this case, it's "smsplus".                                                                                  |
  | algorithm | Use SHA512 algorithm for hashing and send this as header value.                                                                                                                  |
  | headers   | Specifies which headers have been used in generating the hash. In this case, only the "date" header is used.                                                                     |
  | signature | The actual HMAC signature generated using the specified algorithm (sha512) and includes the hashed data. For more information, refer to [hashing algorithm](#hashing-algorithm). |

  #### hashing algorithm

  You must hash the request parameters using the following hash logic:

  ```
  sha512(<Body data> + '|' + date + '|' + merchant_secret}
  ```

  Where, \<Body data> contains the request Body posted with the request.
</Accordion>

<Accordion title="Sample authorization header code" icon="fa-info-circle">
```javascript
var merchant_key = pm.environment.get('merchantKey') || 'PRiQvJ';
var merchant_secret = pm.environment.get('merchantSalt') || 'mGHSxpD2iBVywParGQrGBlaXjnwkGJMQ';

// Generate current date in RFC 1123 format
var date = new Date().toUTCString();

// Get request body data (empty for GET/DELETE)
var data = "";
if (pm.request.method === "POST" && pm.request.body && pm.request.body.raw) {
    data = pm.request.body.raw;
}

// Generate authorization header
var hash_string = data + '|' + date + '|' + merchant_secret;
var hash = CryptoJS.SHA512(hash_string).toString(CryptoJS.enc.Hex);
var authorization = 'hmac username="' + merchant_key + '", algorithm="sha512", headers="date", signature="' + hash + '"';

// Set environment variables
pm.environment.set('date', date);
pm.environment.set('authorization', authorization);
```
<br />
</Accordion>