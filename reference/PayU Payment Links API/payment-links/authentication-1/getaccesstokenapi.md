---
api:
  file: pl-test-oas.yaml
  operationId: GetAccessTokenAPI
hidden: false
link:
  new_tab: false
---
Use this endpoint to generate and cache the token. You do not have to generate a new token before every API call.<br />

Token validity is returned as `expires_in` seconds (typically 7200 — 2 hours). You should Calculate expiry as `created_at + expires_in` and regenerate before that moment.

***

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /oauth/token
  </Card>
</Cards>

***

## Environments

| **Environment** | **Base URL**                   |
| :-------------- | :----------------------------- |
| **Test**        | `https://uat-accounts.payu.in` |
| **Production**  | `https://accounts.payu.in`     |

<Callout icon="📘" theme="info">
  ### **Get Your Client ID and Secret**

  Go to your PayU Dashboard → **Developers** → **Client ID & Client secret details**. See [Get Client ID and Secret](doc:get-client-id-and-secret-from-dashboard) for a step-by-step walkthrough.
</Callout>

***

## Sample Request

<Tabs>
  <Tab title="Request Payload">
    ```curl
    curl --location --request POST 'https://uat-accounts.payu.in/oauth/token' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'client_id={{client_id}}' \
    --data-urlencode 'client_secret={{client_secret}}' \
    --data-urlencode 'grant_type=client_credentials' \
    --data-urlencode 'scope=create_payment_links update_payment_links read_payment_links'
    ```
    ```python
    import requests

    url = "https://uat-accounts.payu.in/oauth/token"

    payload = {
        "client_id":     "{{client_id}}",
        "client_secret": "{{client_secret}}",
        "grant_type":    "client_credentials",
        "scope":         "create_payment_links update_payment_links read_payment_links"
    }

    response = requests.post(url, data=payload)
    token_data = response.json()
    access_token = token_data["access_token"]
    print(access_token)
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const response = await axios.post(
      'https://uat-accounts.payu.in/oauth/token',
      qs.stringify({
        client_id:     '{{client_id}}',
        client_secret: '{{client_secret}}',
        grant_type:    'client_credentials',
        scope:         'create_payment_links update_payment_links read_payment_links'
      }),
      { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } }
    );

    const { access_token, expires_in } = response.data;
    console.log(access_token);
    ```
    ```php
    <?php
    $ch = curl_init('https://uat-accounts.payu.in/oauth/token');
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST           => true,
        CURLOPT_POSTFIELDS     => http_build_query([
            'client_id'     => '{{client_id}}',
            'client_secret' => '{{client_secret}}',
            'grant_type'    => 'client_credentials',
            'scope'         => 'create_payment_links update_payment_links read_payment_links'
        ]),
        CURLOPT_HTTPHEADER     => ['Content-Type: application/x-www-form-urlencoded']
    ]);
    $response = json_decode(curl_exec($ch), true);
    curl_close($ch);
    echo $response['access_token'];
    ```
  </Tab>

  <Tab title="Parameter Description">
    Refer to the [Body Params](ref:create-payment-links#body-params) section for a full description of all request parameters and use cases.
  </Tab>
</Tabs>
