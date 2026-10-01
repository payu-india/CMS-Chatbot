---
name: HeaderAuthentication
---
| Parameter     | Description                                                                                                                                                                           |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| date          | The current date and time. Use the date format only after the Authentication contract has been confirmed; the value here is an illustrative format.                                                                                         |
| authorization | Authorization value. The format and algorithm are pending engineering confirmation. For more information, refer to authorization fields description table below. |

<Accordion title="authorization fields description" icon="fa-table">
  | Parameter | Description                                                                                                                                                                      |
  | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | username  | Represents the username or identifier for the client or merchant, in this case, it's "<Your_TEST_KEY>".                                                                                  |
  | algorithm | Use SHA512 algorithm for hashing and send this as header value.                                                                                                                  |
  | headers   | Specifies which headers have been used in generating the hash. In this case, only the "date" header is used.                                                                     |
  | signature | Authorization value. The format and algorithm are pending engineering confirmation. For more information, refer to [hashing algorithm](#hashing-algorithm). |

  #### hashing algorithm

  The following formula appears in the current source but is disputed by the audit. Do not use it until the API team confirms it:

  ```
  sha512(<Body data> + '|' + date + '|' + merchant_secret}
  ```

  Where, \<Body data> contains the request Body posted with the request.
</Accordion>

<Accordion title="Sample authorization header code" icon="fa-info-circle">
```javascript
var merchant_key = pm.environment.get('merchantKey') || '<YOUR_TEST_KEY>';
var merchant_secret = pm.environment.get('merchantSalt') || '<YOUR_TEST_SALT>';

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