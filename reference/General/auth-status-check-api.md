---
title: Auth Status Check API
deprecated: false
hidden: true
metadata:
  robots: index
---
Use this API to retrieve 3DS2 authentication results when using the `auth_only=2` flow. Unlike 3DS1.0, 3DS2.0 cannot return the authentication response via the browser, so this API must be called to check the authentication status.

<Callout icon="📘" theme="info">
  **Notes:**

  * This API is specifically for `auth_only=2` flow. For `auth_only=1`, the authentication response is returned automatically.
  * The `referenceId` is obtained from the initial payment response in `metaData.referenceId`.
  * The hash must include the literal string `"admin"` as part of the hash calculation.
  * Ensure the `Date` header matches the date used in hash calculation.
</Callout>

**API Endpoint**

| Environment | URL                                         |
| :---------- | :------------------------------------------ |
| Test        | `https://test.payu.in/decoupled/AuthData`   |
| Production  | `https://secure.payu.in/decoupled/AuthData` |

HTTP Method:  **POST**

## Request Parameters

### Headers

| Parameter                       | Description                                                                                  | Example                       |
| :------------------------------ | :------------------------------------------------------------------------------------------- | :---------------------------- |
| key<br />`mandatory`            | `String`<br />Merchant key provided by PayU during onboarding.                               | smsplus                       |
| hash<br />`mandatory`           | `String`<br />SHA512 hash calculated using the formula: `sha512(key\|mihpayid\|admin\|date)` | 5cfbd52bf5c9c11322d17868...   |
| Date<br />`mandatory`           | `String`<br />Current date and time in UTC format.                                           | Tue, 07 Mar 2023 10:46:50 GMT |
| Content-Type<br />`conditional` | `String`<br />Required for POST requests (Type 2). Must be `application/json`.               | application/json              |

### Query Parameter

| Parameter                    | Description                                                                                       | Example                          |
| :--------------------------- | :------------------------------------------------------------------------------------------------ | :------------------------------- |
| referenceId<br />`mandatory` | `String`<br />The reference ID returned in the initial payment response (`metaData.referenceId`). | 7f40a6b79403b028e824dd18d610a4e7 |

### Body Parameter

| Parameter             | Description                                                                                    | Example                |
| :-------------------- | :--------------------------------------------------------------------------------------------- | :--------------------- |
| cres<br />`mandatory` | `String`<br />Base64 encoded CRes (Challenge Response) received from ACS after authentication. | eyJtZXNzYWdlVHlwZSI... |

***

## Hash Generation

Generate the hash for the AuthData API using the following formula:

```
hash = SHA512(key | mihpayid | "admin" | date)
```

### Hash Generation Sample Code

```javascript
var referenceId = 'abf367fd2cfb7a4d3ceed0257652aef86cdc8400683aba26a838cdda6c8f29f0';
var merchantKey = pm.environment.get("merchantKey");
var merchantSalt = pm.environment.get("merchantSalt");
var date = new Date();
date = date.toUTCString();

var hashString = merchantKey + "|" + referenceId + "|" + merchantSalt + "|" + date;
console.log("Hash string: " + hashString);

var hashResult = CryptoJS.SHA512(hashString).toString(CryptoJS.enc.Hex);
console.log("Hash: " + hashResult);

// Set environment variables for request
pm.environment.set("mihpayid", mihpayid);
pm.environment.set("hash", hashResult);
pm.environment.set("key", merchantKey);
pm.environment.set("date", date);
```

## Sample Request

```bash
curl --location 'https://test.payu.in/decoupled/AuthData?referenceId=abf367fd2cfb7a4d3ceed0257652aef86cdc8400683aba26a838cdda6c8f29f0' \
--header 'key: PRiQvJ' \
--header 'hash: fe94fd6b4ef0116e33870e40301342440a588cbfbc5357795fb6cccb9cc81f122a857778963d835149e46945b6b7a9b28456b90855b46de312103e3701bdfc8e' \
--header 'Date: Mon, 27 Apr 2026 10:34:26 GMT' \
--header 'Content-Type: application/json'
```
```python
import requests
import hashlib
from datetime import datetime
import json

url = 'https://secure.payu.in/decoupled/AuthData'

mihpayid = '999000000000704'
merchant_key = 'smsplus'
reference_id = '224845c3c891a0925d0554b390d70e71'
date = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

# Generate hash
hash_string = f"{merchant_key}|{mihpayid}|admin|{date}"
hash_value = hashlib.sha512(hash_string.encode()).hexdigest()

headers = {
    'key': merchant_key,
    'hash': hash_value,
    'Date': date,
    'Content-Type': 'application/json'
}

params = {
    'referenceId': reference_id
}

data = {
    'cres': 'eyJtZXNzYWdlVHlwZSI6IkNSZXMiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMi4wIiwidGhyZWVEU1NlcnZlclRyYW5zSUQiOiJlYzI5NWMwNS0xNWViLTRjNjktYmYyNi1iMzQ4YzZjZmEwY2QiLCJ0cmFuc1N0YXR1cyI6IlkifQ=='
}

response = requests.post(url, headers=headers, params=params, json=data)

if response.status_code == 200:
    print('Response:', response.json())
else:
    print(f'Error: {response.status_code}')
```

***

## Response Parameters

| Parameter                              | Description                                                                                          | Example                              |
| :------------------------------------- | :--------------------------------------------------------------------------------------------------- | :----------------------------------- |
| payuid<br />`String`                   | PayU transaction ID for the authenticated transaction.                                               | 999000000000542                      |
| eci<br />`String`                      | Electronic Commerce Indicator. Values: `05` (Visa), `02` (Mastercard) for successful authentication. | 05                                   |
| cavv<br />`String`                     | Cardholder Authentication Verification Value. Base64 encoded authentication token.                   | AAIBBGOAZgAAAABkNWAgdQAAAAA=         |
| threeDSTransStatus<br />`String`       | 3DS transaction status. See [Transaction Status Values](#transaction-status-values).                 | Y                                    |
| threeDSTransStatusReason<br />`String` | Reason for transaction status (if not successful). Null for successful transactions.                 | null                                 |
| flowType<br />`String`                 | Type of authentication flow: `Challenge` or `Frictionless`.                                          | Challenge                            |
| threeDSTransID<br />`String`           | 3DS Transaction ID assigned by ACS.                                                                  | c3947b6b-9f19-40fa-b184-6c489a22bedc |
| threeDSServerTransID<br />`String`     | 3DS Server Transaction ID.                                                                           | 505bbed1-fea8-42f4-a182-6b22c4a828cd |
| threeDSVersion<br />`String`           | Version of 3DS protocol used.                                                                        | 2.2.0                                |
| status<br />`String`                   | Overall API response status: `SUCCESS` or `FAILURE`.                                                 | SUCCESS                              |

***

## Transaction Status Values

| Status | Description                               |
| :----- | :---------------------------------------- |
| Y      | Authentication successful                 |
| N      | Authentication failed or not attempted    |
| U      | Unable to authenticate (technical issues) |
| A      | Authentication attempted but not verified |
| C      | Challenge required                        |
| R      | Authentication rejected                   |

***

## Sample Response

### Success Response

```json
{
    "payuid": "999000000000542",
    "eci": "05",
    "cavv": "AAIBBGOAZgAAAABkNWAgdQAAAAA=",
    "threeDSTransStatus": "Y",
    "threeDSTransStatusReason": null,
    "flowType": "Challenge",
    "threeDSTransID": "c3947b6b-9f19-40fa-b184-6c489a22bedc",
    "threeDSServerTransID": "505bbed1-fea8-42f4-a182-6b22c4a828cd",
    "threeDSVersion": "2.2.0",
    "status": "SUCCESS"
}
```

### Frictionless Flow Response

```json
{
    "payuid": "999000000000543",
    "eci": "05",
    "cavv": "AAIBBGOAZgAAAABkNWAgdQAAAAA=",
    "threeDSTransStatus": "Y",
    "threeDSTransStatusReason": null,
    "flowType": "Frictionless",
    "threeDSTransID": "46299007-eeef-4b39-aba6-d170e095bdd2",
    "threeDSServerTransID": "505bbed1-fea8-42f4-a182-6b22c4a828cd",
    "threeDSVersion": "2.1.0",
    "status": "SUCCESS"
}
```

### Failed Authentication Response

```json
{
    "payuid": "999000000000544",
    "eci": null,
    "cavv": null,
    "threeDSTransStatus": "N",
    "threeDSTransStatusReason": "Authentication failed",
    "flowType": "Challenge",
    "threeDSTransID": "c3947b6b-9f19-40fa-b184-6c489a22bedc",
    "threeDSServerTransID": "505bbed1-fea8-42f4-a182-6b22c4a828cd",
    "threeDSVersion": "2.2.0",
    "status": "FAILURE"
}
```

***
