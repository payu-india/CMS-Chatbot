---
name: V2_payment_header_params
---
| Parameter     | Description                                                                                                                                                                                                    |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| date          | The current date and time. For example,  format of the date is Wed, 28 Jun 2023 11:25:19 GMT.                                                                                                                  |
| authorization | The actual HMAC signature generated using the specified algorithm (sha512) and includes the hashed data. For more information, refer to[ authorization fields description](#authorization-fields-description). |

#### authorization fields description

| Field     | Description                                                                                                                         |
| :-------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| username  | Represents the username or identifier for the client or merchant, for example smsplus.                                              |
| algorithm | Use SHA512 algorithm for hashing and send this as header value.                                                                     |
| headers   | Specifies which headers have been used in generating the hash, for example date.                                                    |
| signature | The HMAC signature generated using the specified algorithm. For more information, refer to [hashing algorithm](#hashing-algorithm). |

#### hashing algorithm

You must hash the request parameters using the following hash logic:

**Hash logic**: ``sha512(`<Body data>` + '|' + date + '|' + merchant_secret)``

Where `<Body data>` contains the request body posted with the request.

<br />

<Accordion title="Sample header code" icon="fa-code">
  ```javascript
    var merchant_key = 'smsplus';
    var merchant_secret = 'izF09TlpX4ZOwmf9MvXijwYsBPUmxYHD';
    // date
    var date = new Date();
    date = date.toUTCString();

    // authorization
    var authorization = getAuthHeader(date);

    function getAuthHeader(date) {
        var AUTH_TYPE = 'sha512';
        var data = isEmpty(request['data']) ? "" : request['data'];
        var hash_string = data + '|' + date + '|' + merchant_secret;
        var hash = CryptoJS.SHA512(hash_string).toString(CryptoJS.enc.Hex);
        return `hmac username="${merchant_key}", algorithm="${AUTH_TYPE}", headers="date", signature="${hash}"`;
    }
  ```
</Accordion>

<br />
