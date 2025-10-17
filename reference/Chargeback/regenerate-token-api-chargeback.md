---
title: Regenerate Token API - Chargeback
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Regenerate Token** API for Chargeback allows users to regenerate authentication tokens with a specified expiration date. This endpoint is part of the Optimus platform and provides a secure way to refresh API tokens while maintaining authentication integrity.

**Environment**

|            |                                              |
| :--------- | :------------------------------------------- |
| Production | \<Optimus endpoint>/api/v1/tokens/regenerate |

<Callout icon="📘" theme="info">
  **Contact for Optimus endpoint**: Contact your WIBMO key account manager or support for the Optimus endpoint.
</Callout>

## Request header

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Header
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        X-Optimus-API-Key <br />
        <code>mandatory</code>
      </td>

      <td>
        <code>String</code>- The unique API key for authentication
      </td>

      <td>
        your_api_key_here
      </td>
    </tr>

    <tr>
      <td>
        Content-Type<br />
        <code>mandatory</code>
      </td>

      <td>
        <code>string</code> - Must be set to application/json
      </td>

      <td>
        application/json
      </td>
    </tr>
  </tbody>
</Table>

## Request parameters

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
      <td>expires_at <br/>
 <code>mandatory</code> </td>
      <td><code>String</code> <code>mandatory</code> - Specifies the expiration date for the regenerated token. Must be in YYYY-MM-DD format and cannot be a past date. <br/>Note: The valid date format is YYYY-MM-DD.</td>
      <td>* 2025-12-21<br/>
   * 2025-12-21<br/>
    * 2025-01-15<br/>
    * 2024-12-31<br/>
    </td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Sample request

```bash
curl --location 'http://localhost:3000/api/v1/tokens/regenerate' \
--header 'X-Optimus-API-Key: {your_old_api_key}' \
--header 'Content-Type: application/json' \
--data '{ "expires_at": "2025-12-21" }'
```

## Sample response

### Success scenario

```json
{
  "success": true,
  "message": "Token regenerated successfully",
  "token": "78fe93bd_5fc3_4df2_a54a_e04fdfbce95e",
  "name": "test api token",
  "expires_at": "2025-11-26 23:59:59"
}
```

### Failure scenarios

* 400 Bad Request: **Invalid request format or parameters**

```json
{
  "error": "Invalid expiry date format",
  "message": "Expiry date must be in YYYY-MM-DD format"
}
```

* 401 Unauthorized:  **Missing or invalid API key**

```json
{
  "errors": "Invalid Token"
}
```

## Response parameters

| Parameter                 | Description                                                                             | Example                                    |
| :------------------------ | :-------------------------------------------------------------------------------------- | :----------------------------------------- |
| <h3>Success scenario</h3> |                                                                                         |                                            |
| success                   | <code>boolean</code> - Indicates whether the request was successful                     | true                                       |
| message                   | <code>string</code> - Human-readable message about the result                           | "Token regenerated successfully"           |
| token                     | <code>string</code> - The newly generated authentication token                          | "78fe93bd_5fc3_4df2_a54a_e04fdfbce95e"     |
| name                      | <code>string</code> - The name of the regenerated token                                 | "test api token"                           |
| expires_at                | <code>string</code> - Timestamp of the token's expiration in YYYY-MM-DD HH:MM:SS format | "2025-11-26 23:59:59"                      |
| <h3>Failure scnario</h3>  |                                                                                         |                                            |
| error                     | <code>string</code> - Error type identifier                                             | "Invalid expiry date format"               |
| message                   | <code>string</code> - Detailed error description                                        | "Expiry date must be in YYYY-MM-DD format" |

## HTTP Status Codes

| Status Code | Description                                        |
| ----------- | -------------------------------------------------- |
| 200         | OK - Token regenerated successfully                |
| 400         | Bad Request - Invalid request format or parameters |
| 401         | Unauthorized - Missing or invalid API key          |
