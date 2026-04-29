---
title: Create Payment Links via Bulk Upload - APIs
excerpt: Know how to create payment links via bulk upload option using APIs.
deprecated: false
hidden: true
metadata:
  robots: index
---
The bulk upload option using APIs lets you create many payment links by uploading a `.csv` file.

## Integration Steps

Below are the integration steps:

<Cards columns={3}>
  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-key" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }} />

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Fetch the Access Token</h4>

      <p style={{ margin: 0 }}>
        Fetch the Bearer Token.
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-file-upload" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }} />

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Bulk Upload</h4>

      <p style={{ margin: 0 }}>
        Upload the Bulk File.
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-link" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }} />

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Get Payment Links</h4>

      <p style={{ margin: 0 }}>
        Get the Created Payment Links Using the Batch ID.
      </p>
    </div>
  </Card>
</Cards>

### Step 1. Get the Access Token

The first step is to obtain an access token using the following API. Refer to the <Anchor label="Get Access Token API" target="_blank" href="https://docs.payu.in/reference/get-token-api-for-payment-links">Get Access Token API</Anchor> for more information.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /oauth/token
  </Card>
</Cards>

<Accordion title="Environment Details" icon="fa-cogs">
  |                |                                                              |
  | :------------- | :----------------------------------------------------------- |
  | **Test**       | [https://uat-accounts.payu.in](https://uat-accounts.payu.in) |
  | **Production** | [https://accounts.payu.in](https://accounts.payu.in)         |
</Accordion>

<Accordion title="Sample Request" icon="fa-code">

```curl
curl --location -g --request POST '{{hub_base_url}}/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id={{client_id}}' \
--data-urlencode 'client_secret={{client_secret}}' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode 'scope=read_payment_links'
```

</Accordion>

<Accordion title="Sample Response" icon="fa-code">

```json Success Response
{
"access_token": "ea4ed864b4d2a04b90c1e987a5d25a5da1d43fa5f7d123be6814a1e973f196c4",
"token_type": "Bearer",
"expires_in": 7011,
"scope": "create_payment_links",
"created_at": 1763036368
}
```
```json Error Response
{
  "error": "invalid_client",
  "error_description": "Client authentication failed",
  "status": 401
}
```

</Accordion>

<Accordion title="Request Parameters" icon="fa-table">

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `client_id` *mandatory*
      </td>

      <td>
        `string` Your OAuth 2.0 client ID issued by PayU. Refer to the <Anchor label="Get Client ID and Secret from Dashboard" target="_blank" href="/docs/get-client-id-and-secret-from-dashboard">Get Client ID and Secret from Dashboard</Anchor> page for more information.
      </td>
    </tr>

    <tr>
      <td>
        `client_secret` *mandatory*
      </td>

      <td>
        `string` Your OAuth 2.0 client secret (keep this secure). Refer to the <Anchor label="Get Client ID and Secret from Dashboard" target="_blank" href="/docs/get-client-id-and-secret-from-dashboard">Get Client ID and Secret from Dashboard</Anchor> page for more information.
      </td>
    </tr>

    <tr>
      <td>
        `grant_type` *mandatory*
      </td>

      <td>
        `string/enum` The OAuth 2.0 grant type for server-to-server authentication. Allowed value is `client_credentials`.
      </td>
    </tr>

    <tr>
      <td>
        `scope` *optional*
      </td>

      <td>
        `string` The scope that must be used for payment links are: <ul><li>Create Link: create_payment_links</li> <li>Change status and expiry: update_payment_links</li> <li>Get a single payment link: read_payment_links</li> <li>Get all payment links: read_payment_links</li> <li>Share payment links: read_payment_links</li></ul>  

        <strong>Note:</strong> Merchant can pass up to three scopes simultaneously for an access token value. This is done by passing scopes separated by a space between them. For example: `create_payment_links update_payment_links read_payment_links`.
      </td>
    </tr>
  </tbody>
</Table>

</Accordion>

<Accordion title="Response Parameters" icon="fa-table">

| **Parameter**  | **Description**                                                |
| :------------- | :------------------------------------------------------------- |
| `access_token` | `string` The generated access token.                           |
| `token_type`   | `string` The type of the generated token. Here it is `Bearer`. |
| `expires_in`   | `string` The token expiry timestamp.                           |
| `scope`        | `string` The scope of the token.                               |
| `created_at`   | `string` The timestamp at which the token was created.         |

</Accordion>

<br />
