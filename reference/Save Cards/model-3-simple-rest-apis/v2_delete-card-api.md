---
title: Delete a Saved Card API
deprecated: false
hidden: false
metadata:
  robots: index
---
This API is used to delete an existing card stored on PayU Vault.

HTTP Method: **POST**

**Environment**

|            |                                                 |
| :--------- | :---------------------------------------------- |
| Production | \<info.storecard.service.url>/storecard/card/v1 |

## Query parameters

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
      <td>userCredential<br/><code>mandatory</code></td>
      <td><code>String</code> User authentication credential in the format <code>username:userid</code>.</td>
      <td>testuser:testuser123</td>
    </tr>
    <tr>
      <td>getSoftDeleted<br/><code>optional</code></td>
      <td><code>Integer</code> Flag to include soft-deleted records in the response. Set to <code>1</code> to include, <code>0</code> to exclude.</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Request header

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
      <td>mid<br/><code>mandatory</code></td>
      <td><code>String</code> Merchant identifier for the API request.</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Sample request

```
curl --location --request DELETE '<info.storecard.service.url>/storecard/card/v1?userCredential=sartaj%3Ainfo&cardToken=18ca2c6b01be04fd0248b' \
--header 'Content-Type: application/json' \
--header 'mid: 2' \
--data ''
```

## Sample Response

* On successful deletion

  ```plaintext
  {
          status: 1,
          msg: "My_card card deleted successfully",
  }
  ```

  * On failure of deletion

  ```plaintext
  {
  "status": 0,
  "msg": card not found
  }
  ```