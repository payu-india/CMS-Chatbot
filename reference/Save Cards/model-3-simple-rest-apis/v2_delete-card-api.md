---
title: Delete a Saved Card API
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: Delete a Saved Card API
deprecated: false
hidden: false
metadata:
  robots: index
---
This v2 API is used to delete an existing card stored on PayU Vault.

HTTP Method: **DELETE**

**Environment**

|            |                                                                                  |
| :--------- | :------------------------------------------------------------------------------- |
| Test       | [https://test.payu.in/storecard/card/v1](https://test.payu.in/storecard/card/v1) |
| Production | [https://info.payu.in/storecard/card/v1](https://info.payu.in/storecard/card/v1) |

## Request parameters

### Authentication header

<HeaderAuthentication />

### Query parameters

| Parameter                       | Description                                                                                | Example              |
| ------------------------------- | ------------------------------------------------------------------------------------------ | -------------------- |
| userCredential<br />`mandatory` | `String` User authentication credential in the format `username:userid`.                   | testuser:testuser123 |
| cardToken<br />`mandatory`      | `String` Card token of the saved card.                                                     |                      |
| networkToken<br />`optional`    | `String` Network issuer token.                                                             |                      |
| issuerToken  <br />`optional`   | `String` Issuer token.                                                                     |                      |
| bankType <br />`optional`       | `String` The bank type of card. It can be any of the following: Credit, Debit, or Prepaid. | Credit               |

### Header parameters

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        date  
        `mandatory`
      </td>

      <td>
        The current date and time. For example, format of the date is Wed, 28 Jun 2023 11:25:19 GMT.
      </td>
    </tr>
  </tbody>
</Table>

### Body parameters

No body parameters for this API

## Sample request

```bash
curl --location --request DELETE 'https://test.payu.in/storecard/card/v1?userCredential=sms%3A123&cardToken=2d1ab4c2f453f25bc9b2d8' \
  --header 'authorization: {{authorization}}' \
  --header 'date: {{date}}'
```

## Sample Response

* On successful deletion

  ```json
  {
    "message": "testAll card deleted successfully",
    "status": 1
  }
  ```

* On failure of deletion

  ```json
  {
    "message": "card not found",
    "status": 0
  }
  ```
