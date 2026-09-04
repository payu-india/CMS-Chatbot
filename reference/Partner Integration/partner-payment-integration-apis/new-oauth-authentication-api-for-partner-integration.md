---
title: '[NEW] OAuth Authentication API for Partner Integration'
deprecated: false
hidden: true
metadata:
  robots: index
---
This endpoint is the first step in the three-step OAuth authentication flow for Partner Payments. Use your reseller credentials to obtain an initial access token with `hub_session` scope.

## Endpoint

**HTTP Method:** POST

**Environment URLs:**

| Environment | URL                                        |
| ----------- | ------------------------------------------ |
| Test        | `https://uat-accounts.payu.in/oauth/token` |
| Production  | `https://accounts.payu.in/oauth/token`     |

***

## Request Headers

```
Content-Type: application/x-www-form-urlencoded
```

***

## Request Parameters

All parameters must be sent as form-urlencoded data.

<table>
  <thead>
    <tr>
      <th align="left">Parameter</th>
      <th align="left">Type &amp; Description</th>
      <th align="left">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>client_id</td>
      <td><strong>String</strong><br>OAuth client ID issued by PayU to the partner.</td>
      <td>abc123clientid</td>
    </tr>
    <tr>
      <td>client_secret</td>
      <td><strong>String</strong><br>OAuth client secret issued by PayU to the partner.</td>
      <td>s3cr3t_v4lue_xyz</td>
    </tr>
    <tr>
      <td>grant_type</td>
      <td><strong>String</strong><br>Must be <code>password</code> for this step.</td>
      <td>password</td>
    </tr>
    <tr>
      <td>username</td>
      <td><strong>String</strong><br>Reseller username.</td>
      <td>reseller_user</td>
    </tr>
    <tr>
      <td>password</td>
      <td><strong>String</strong><br>Reseller password.</td>
      <td>P@ssw0rd!</td>
    </tr>
    <tr>
      <td>scope</td>
      <td><strong>String</strong><br>Must be <code>hub_session</code> for initial token.</td>
      <td>hub_session</td>
    </tr>
  </tbody>
</table>

***

## Sample Request

```bash
curl --location 'https://uat-accounts.payu.in/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=YOUR_CLIENT_ID' \
--data-urlencode 'client_secret=YOUR_CLIENT_SECRET' \
--data-urlencode 'grant_type=password' \
--data-urlencode 'username=YOUR_RESELLER_USERNAME' \
--data-urlencode 'password=YOUR_RESELLER_PASSWORD' \
--data-urlencode 'scope=hub_session'
```

```python
import requests

url = "https://uat-accounts.payu.in/oauth/token"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

payload = {
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET",
    "grant_type": "password",
    "username": "YOUR_RESELLER_USERNAME",
    "password": "YOUR_RESELLER_PASSWORD",
    "scope": "hub_session"
}

try:
    response = requests.post(url, headers=headers, data=payload)
    response.raise_for_status()
    
    data = response.json()
    print("Status Code:", response.status_code)
    print("Response:", data)
    
except requests.exceptions.RequestException as e:
    print("Error:", e)
```

```php
<?php

$url = "https://uat-accounts.payu.in/oauth/token";

$payload = [
    "client_id" => "YOUR_CLIENT_ID",
    "client_secret" => "YOUR_CLIENT_SECRET",
    "grant_type" => "password",
    "username" => "YOUR_RESELLER_USERNAME",
    "password" => "YOUR_RESELLER_PASSWORD",
    "scope" => "hub_session"
];

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Content-Type: application/x-www-form-urlencoded"
]);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

if (curl_errno($ch)) {
    echo "Error: " . curl_error($ch);
} else {
    echo "Status Code: " . $httpCode . "\n";
    echo "Response: " . $response;
}

curl_close($ch);
?>
```

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class OAuthPasswordGrant {
    public static void main(String[] args) {
        try {
            String url = "https://uat-accounts.payu.in/oauth/token";
            
            String payload = "client_id=YOUR_CLIENT_ID" +
                           "&client_secret=YOUR_CLIENT_SECRET" +
                           "&grant_type=password" +
                           "&username=YOUR_RESELLER_USERNAME" +
                           "&password=YOUR_RESELLER_PASSWORD" +
                           "&scope=hub_session";
            
            HttpClient client = HttpClient.newHttpClient();
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(payload))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println("Status Code: " + response.statusCode());
            System.out.println("Response: " + response.body());
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

```javascript
async function getOAuthToken() {
    const url = "https://uat-accounts.payu.in/oauth/token";
    
    const payload = new URLSearchParams({
        client_id: "YOUR_CLIENT_ID",
        client_secret: "YOUR_CLIENT_SECRET",
        grant_type: "password",
        username: "YOUR_RESELLER_USERNAME",
        password: "YOUR_RESELLER_PASSWORD",
        scope: "hub_session"
    });
    
    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: payload
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log("Status Code:", response.status);
        console.log("Response:", data);
        
    } catch (error) {
        console.error("Error:", error);
    }
}

getOAuthToken();
```

> **Note:** Replace all placeholder values (`YOUR_CLIENT_ID`, `YOUR_CLIENT_SECRET`, etc.) with your actual credentials.

***

## Sample Response

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsicGF5dS1wYXJ0bmVyLXNlcnZpY2UiXSwi...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "hub_session"
}
```

***

## Response Parameters

| Parameter      | Type    | Description                                                    |
| -------------- | ------- | -------------------------------------------------------------- |
| `access_token` | string  | JWT access token to use in Step 2 (authorization code request) |
| `token_type`   | string  | Always "Bearer"                                                |
| `expires_in`   | integer | Token validity duration in seconds (typically 3600 = 1 hour)   |
| `scope`        | string  | Granted scope (should be "hub_session")                        |

***

## Error Codes

| HTTP Status | Error                    | Description                            |
| ----------- | ------------------------ | -------------------------------------- |
| 400         | `invalid_request`        | Missing or invalid required parameters |
| 401         | `invalid_client`         | Invalid `client_id` or `client_secret` |
| 401         | `invalid_grant`          | Invalid `username` or `password`       |
| 400         | `unsupported_grant_type` | `grant_type` is not "password"         |

**Error Response Example:**

```json
{
  "error": "invalid_client",
  "error_description": "Client authentication failed"
}
```

***

## Next Steps

After obtaining the access token:

1. Use it in the `Authorization: Bearer` header for [POST /api/v1/merchants/auth_code](ref:get-authorization-code-api)
2. Complete Step 2 to obtain an authorization code for your merchant
3. Exchange the authorization code for the final access token in Step 3

<Info>
This token is **only valid for Step 2** of the OAuth flow. Do not use it for Partner Payments API calls. You need the final access token from Step 3 for that purpose.
</Info>