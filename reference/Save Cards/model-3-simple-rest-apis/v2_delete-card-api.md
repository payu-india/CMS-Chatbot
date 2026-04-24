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

|            |                                                                                        |
| :--------- | :------------------------------------------------------------------------------------- |
| Test       | [https://apitest.payu.in/storecard/card/v1](https://apitest.payu.in/storecard/card/v1) |
| Production | [https://info.payu.in/storecard/card/v1](https://info.payu.in/storecard/card/v1)       |

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
curl --location --request DELETE 'https://apitest.payu.in/storecard/card/v1?userCredential=sms%3A123&cardToken=2d1e569bf1f6b150a32f70' \
--header 'date: Fri, 24 Apr 2026 07:05:59 GMT' \
--header 'authorization: hmac username="PRiQvJ", algorithm="sha512", headers="date", signature="30d8f518edda5b0962c35c0057024cabb6e7f19727488cb1874e75652bcea7499811dbf3ddac419c50c2fe56a8e032129bb0d6eaeaa3f971b3c2b5ccbfd12aa3"' \
--header 'Cookie: PHPSESSID=krida5voc39gqosfud8tt6n8as'
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
      "message": "cardToken is invalid",
      "status": 0
  }
  ```
