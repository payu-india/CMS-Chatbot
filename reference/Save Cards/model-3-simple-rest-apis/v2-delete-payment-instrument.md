---
title: v2 Delete Payment Instrument
deprecated: false
hidden: false
metadata:
  robots: index
---
This API is used to delete an existing payment instrument stored on PayU Vault.

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
      <td><code>String</code> User authentication credential in the format specified.</td>
      <td>sms:123</td>
    </tr>
    <tr>
      <td>cardToken<br/><code>mandatory</code></td>
      <td><code>String</code> Unique token identifier for the stored card.</td>
      <td>18c7804aafdac732b5e8</td>
    </tr>
    <tr>
      <td>networkTokenissuerToken<br/><code>optional</code></td>
      <td><code>String</code> Combined network token and issuer token parameter.</td>
      <td>null</td>
    </tr>
    <tr>
      <td>bankType<br/><code>optional</code></td>
      <td><code>String</code> Type of bank or card issuer.</td>
      <td>null</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Request body

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
      <td><code>String</code> User authentication credential for card deletion.</td>
      <td>sms:123</td>
    </tr>
    <tr>
      <td>cardToken<br/><code>mandatory</code></td>
      <td><code>String</code> Unique token identifier for the card to be deleted.</td>
      <td>1f4463abae4175a70516</td>
    </tr>
    <tr>
      <td>networkToken<br/><code>optional</code></td>
      <td><code>String</code> Network-specific token for the card.</td>
      <td>4489682380100740</td>
    </tr>
    <tr>
      <td>issuerToken<br/><code>optional</code></td>
      <td><code>String</code> Issuer-specific token for enhanced security.</td>
      <td>src_wqe47hxfjksor89y4</td>
    </tr>
    <tr>
      <td>bankType<br/><code>optional</code></td>
      <td><code>String</code> Type of bank or financial institution.</td>
      <td>SODEXO</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Sample request

```
curl --location --request DELETE '<info.storecard.service.url>/storecard/card/v1?userCredential=sms%3A123&cardToken=18c7804aafdac732b5e8&networkTokenissuerToken=null&bankType=null' \
--header 'Content-Type: application/json' \
--header 'mid: 2' \
--data '{"userCredential":"sms:123",
"cardToken" : "1f4463abae4175a70516",
"networkToken" : "4489682380100740",
"issuerToken":"src_wqe47hxfjksor89y4",
"bankType":"SODEXO"
}'
```

<br />

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