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

## Header parameters

### Authentication header

<HeaderAuthentication />

### Query parameters


| Parameter | Description | Example |
|---|---|---|
| userCredential<br/>`mandatory` | `String` User authentication credential in the format `username:userid`. | testuser:testuser123 |
| getSoftDeleted<br/>`optional` | `Integer` Flag to include soft-deleted records in the response. Set to `1` to include, `0` to exclude. | 1 |


## Request header
| Parameter | Description | Example |
|---|---|---|
| mid<br/>`mandatory` | `String` Merchant identifier for the API request. | 2 |

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
