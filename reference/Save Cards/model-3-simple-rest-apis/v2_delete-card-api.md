---
title: Delete a Saved Card API
deprecated: false
hidden: false
metadata:
  robots: index
---
This API is used to delete an existing card stored on PayU Vault.

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

```
curl --location --request DELETE '<info.storecard.service.url>/storecard/card/v1?userCredential=sms%3A123&cardToken=18c7804aafdac732b5e8&networkTokene=null&issuerToken=null&bankType=null' \
  --header 'authorization: {{authorization}}' \
  --header 'date: {{date}}'
```

## Sample Response

* On successful deletion

  ```plaintext
  {
      "message": "testAll card deleted successfully",
      "status": 1
  }
  ```

  * On failure of deletion

  ```plaintext
  {
  "status": 0,
  "msg": card not found
  }
  ```
