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
  ```
  var merchant_key = 'smsplus';
  var merchant_secret = '<merchant_salt>';

  // date
  var date = new Date();
  // var date = "Wed, 28 Jun 2023 11:25:19 GMT";
  date = date.toUTCString();

  // authorization
  var authorization = getAuthHeader(date);
  console.log(authorization);

  function getAuthHeader(date) {
  var AUTH_TYPE = 'sha512';
  var data = isEmpty(request['data'])?"":request['data'];
  var hash_string = data + '|' + date + '|' + merchant_secret;
  console.log("Hash String is ", hash_string);
  var hash = CryptoJS.SHA512(hash_string).toString(CryptoJS.enc.Hex);
  var authHeader = 'hmac username="' + merchant_key + '", ' + 'algorithm="' + AUTH_TYPE + '", headers="date", signature="' + hash + '"'
  return authHeader;
  }

  pm.environment.set('date', date);
  pm.environment.set('authorization', authorization);
  pm.environment.set('merchant_key',merchant_key);
  pm.environment.set('merchant_secret',merchant_secret);

  function isEmpty(obj) {
  for(var key in obj) {
  if(obj.hasOwnProperty(key))
  return false;
  }
  return true;
  }
  ```
</Accordion>

<br />
