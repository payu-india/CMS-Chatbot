---
title: TWID Refund Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Refund** API is used to initiate refund and **Refund Status** API used to check the status of refund for TWID API integration. This section describes the steps to integrate TWID Refund integration.

## Step 1: Initiate the refund

#### Environment

|            |                                     |
| :--------- | :---------------------------------- |
| Production | \{\{loyalty-service-url}}/refund/v1 |

### Request parameters

<Accordion title="Request header" icon="fa-info-table">
  **Request header for authentication**

  | Parameter     | Description                                                                                                                                                                                                    |
  | :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | date          | The current date and time. For example,  format of the date is Wed, 28 Jun 2023 11:25:19 GMT.                                                                                                                  |
  | authorization | The actual HMAC signature generated using the specified algorithm (sha512) and includes the hashed data. For more information, refer to[ authorization fields description](#authorization-fields-description). |

  #### authorization fields description

  | Parameter | Description                                                                                                                                                                      |
  | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | username  | Represents the username or identifier for the client or merchant, in this case, it's "smsplus".                                                                                  |
  | algorithm | Indicates the hashing algorithm used for the HMAC signature. Here, it is set to "sha512".                                                                                        |
  | headers   | Specifies which headers have been used in generating the hash. In this case, only the "date" header is used.                                                                     |
  | signature | The actual HMAC signature generated using the specified algorithm (sha512) and includes the hashed data. For more information, refer to [hashing algorithm](#hashing-algorithm). |

  #### hashing algorithm

  You must hash the request parameters using the following hash logic:

  ```
  sha512(<Body data> + '|' + date + '|' + merchant_secret}
  ```

  Where, \<Body data> contains the request Body posted with the request.

  <details>
    <summary>Sample header code</summary>

    ```
    var merchant_key = 'smsplus';
    var merchant_secret = 'izF09TlpX4ZOwmf9MvXijwYsBPUmxYHD';

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
  </details>
</Accordion>

#### Body parameters

<HTMLBlock>{`
    <table>
    <thead>
    <tr>
    <th>Parameter</th>
    <th>Description</th>
    <th>Example</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>parentTxnId </br><code>mandatory</code></td>
    <td><code>String</code> - Parent PayU transaction ID</td>
    <td><code>"bd1a77b6-1596-46e1-b79f-2770bcb636c7"</code></td>
    </tr>
    <tr>
    <td>merchantReferenceId </br><code>mandatory</code></td>
    <td><code>String</code> - Merchant reference ID</td>
    <td><code>"56as67ds7678asd"</code></td>
    </tr>
    <tr>
    <td>refundAmount </br><code>mandatory</code></td>
    <td><code>Number</code> - Amount requested for refund</td>
    <td><code>200</code></td>
    </tr>
    <tr>
    <td>refundId </br><code>mandatory</code></td>
    <td><code>String</code> - Unique refund ID</td>
    <td><code>"4656526"</code></td>
    </tr>
    </tbody>
    </table>
`}</HTMLBlock>

### Sample request

**Non-seamless integration**

```bash
curl -X POST "{{loyalty-service-url}}/refund/v1" \
  -H "Content-Type: application/json" \
  -H "mid: YOUR_MERCHANT_ID" \
  -d '{
    "parentTxnId": "9090909090909111",
    "merchantReferenceId": "56as67ds7678asd",
    "refundAmount": 200,
    "refundId": "4656526"
  }'
```

**Seamless integration**

```bash
curl -X POST "{{loyalty-service-url}}/refund/v1" \
  -H "Content-Type: application/json" \
  -H "Date: Wed, 08 Sep 2025 13:22:43 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"" \
  -d '{
    "parentTxnId": "9090909090909111",
    "merchantReferenceId": "56as67ds7678asd",
    "refundAmount": 200,
    "refundId": "4656526"
  }'
```

<Accordion title="Response details" icon="fa-info-table">
  **Response parameters**

  | Parameter       | Description                                     | Example    |
  | --------------- | ----------------------------------------------- | ---------- |
  | message         | `String` - Status message of the refund request | `"Queued"` |
  | loyaltyRefundId | `String` - Loyalty refund ID for tracking       | `"1213"`   |

  **Sample response**

  ```json
  {
    "message": "Queued",
    "loyaltyRefundId": "1213"
  }
  ```
</Accordion>

<Callout icon="📘" theme="info">
  **Notes:**

  * When the refund is queued, the status must be verified using the **Refund Status API** for confirmation.
  * The `loyaltyRefundId` returned should be used to check the refund status
</Callout>

## Step 2: Capture the loyaltyRefundId from the response

You have to capture the **loyaltyRefundId** parameter value from the response similar to the following:

```json
{
  "message": "Queued",
  "loyaltyRefundId": "1213"
}
```

## Step 3: Check the status of the refund

Use the **loyaltyRefundId** parameter value and check the status of the refund.

#### Environment

|            |                                                        |
| :--------- | :----------------------------------------------------- |
| Production | \{\{loyalty-service-url}}/refund/v1/\{loyaltyRefundId} |

### Request parameters

<Accordion title="Request header" icon="fa-info-table">
  **Request header for authentication**

  | Parameter     | Description                                                                                                                                                                                                    |
  | :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | date          | The current date and time. For example,  format of the date is Wed, 28 Jun 2023 11:25:19 GMT.                                                                                                                  |
  | authorization | The actual HMAC signature generated using the specified algorithm (sha512) and includes the hashed data. For more information, refer to[ authorization fields description](#authorization-fields-description). |

  #### authorization fields description

  | Parameter | Description                                                                                                                                                                      |
  | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | username  | Represents the username or identifier for the client or merchant, in this case, it's "smsplus".                                                                                  |
  | algorithm | Indicates the hashing algorithm used for the HMAC signature. Here, it is set to "sha512".                                                                                        |
  | headers   | Specifies which headers have been used in generating the hash. In this case, only the "date" header is used.                                                                     |
  | signature | The actual HMAC signature generated using the specified algorithm (sha512) and includes the hashed data. For more information, refer to [hashing algorithm](#hashing-algorithm). |

  #### hashing algorithm

  You must hash the request parameters using the following hash logic:

  ```
  sha512(<Body data> + '|' + date + '|' + merchant_secret}
  ```

  Where, \<Body data> contains the request Body posted with the request.

  <details>
    <summary>Sample header code</summary>

    ```
    var merchant_key = 'smsplus';
    var merchant_secret = 'izF09TlpX4ZOwmf9MvXijwYsBPUmxYHD';

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
  </details>
</Accordion>

#### Request path parameters

<HTMLBlock>{`
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>loyaltyRefundId <code>mandatory</code></td>
<td><code>String</code> - Unique loyalty refund ID returned by Refund API</td>
<td><code>"1213"</code></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### Sample request

_**Non-seamless integration**_

```bash
curl -X GET "\{\{loyalty-service-url}}/refund/v1/1213" \
  -H "Content-Type: application/json" \
  -H "mid: YOUR_MERCHANT_ID"
```

_**Seamless integration**_

```bash
curl -X GET "\{\{loyalty-service-url}}/refund/v1/1213" \
  -H "Content-Type: application/json" \
  -H "Date: Wed, 08 Sep 2025 13:22:43 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\""
```

<Accordion title="Response details" icon="fa-info-table">
  **Response parameters**

  | Parameter          | Description                                                            | Example                                |
  | ------------------ | ---------------------------------------------------------------------- | -------------------------------------- |
  | message            | `String` - Refund process status (`Success`, `Failed`, or `Pending`)   | `"Success"` / `"Failed"` / `"Pending"` |
  | loyaltyRefundId    | `String` - Loyalty refund ID                                           | `"1213"`                               |
  | rewardPartnerRefId | `String` - Reference ID provided by the reward partner (if successful) | `"7251637276230479872"`                |

  **Sample response**

  * Success scenario

  ```json
  {
    "message": "Success",
    "loyaltyRefundId": 83,
    "rewardPartnerRefId": "7251637276230479872"
  }
  ```

  * Failure scenario

    * Failed refund

  ```json
  {
    "message": "Failed",
    "loyaltyRefundId": "1213"
  }
  ```

  * Pending refund

  ```json
  {
    "message": "Pending",
    "loyaltyRefundId": "1213"
  }
  ```
</Accordion>

<Callout icon="📘" theme="info">
  **Notes:**

  * Both APIs are part of the **Loyalty Points Network** and must be called within a secure server-to-server (S2S) framework
  * Regular status checks are recommended for pending refunds
</Callout>
