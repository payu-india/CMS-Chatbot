---
title: ' Update Virtual Account API'
deprecated: false
hidden: true
metadata:
  title: ' Update Virtual Account API - PACB'
  robots: index
---
---
title: Update Virtual Account API
deprecated: false
hidden: true
metadata:
  title: Update Virtual Account API - PACB
  robots: index
---
Update a **Virtual Account** display name or active status. Set `isActive` to `false` to deactivate the VA and block new bank credits. Historic VA details and deposit records remain available through list and transaction APIs.

## Environment

| Environment | URL                                                   | Method |
| ----------- | ----------------------------------------------------- | ------ |
| Test        | `https://uatoneapi.payu.in/payout/v2/virtualAccounts` | PATCH  |
| Production  | `https://oneapi.payu.in/payout/v2/virtualAccounts`    | PATCH  |

## Request Parameters

### Authorization Logic in Header

<HeaderAuthentication />

### Request Header

| Parameter                     | Description                                              | Example          |
| ----------------------------- | -------------------------------------------------------- | ---------------- |
| Content-Type<br />`mandatory` | `String` - Request body format. Set to `application/json` | application/json |

### Query Parameters

| Parameter                         | Description                                                                                                                                  | Example     |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| virtualAccountId<br />`mandatory` | `String` - PayU-assigned VA identifier (`virtualAccountId`) or virtual account number (for example `PURW2231266`)                            | 2231266     |

### Body Parameters
<Callout icon="📘" theme="info">
  **Note:**

At least one of `virtualAccountName` or `isActive` is required.
</Callout>

| Parameter                           | Description                                                                                                      | Example                   |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------- |
| virtualAccountName<br />`optional` | `String` - Updated display name for the VA. Maximum 255 characters                                               | Storefront collections Q2 |
| isActive<br />`optional`           | `Boolean` - Set to `false` to deactivate the VA. New deposits are rejected at validation when `isActive` is `false` | false                     |


## Sample Request

### Rename virtual account
```curl
curl --location --request PATCH 'https://uatoneapi.payu.in/payout/v2/virtualAccounts?virtualAccountId=2231266' \
--header 'Authorization: {{authorization}}' \
--header 'Content-Type: application/json' \
--data '{
  "virtualAccountName": "Storefront collections Q2"
}'
```
### Deactivate virtual account
```curl
curl --location --request PATCH 'https://uatoneapi.payu.in/payout/v2/virtualAccounts?virtualAccountId=2231266' \
--header 'Authorization: {{authorization}}' \
--header 'Content-Type: application/json' \
--data '{
  "isActive": false
}'
```

### Rename and deactivate
```curl
curl --location --request PATCH 'https://uatoneapi.payu.in/payout/v2/virtualAccounts?virtualAccountId=PURW2231266' \
--header 'Authorization: {{authorization}}' \
--header 'Content-Type: application/json' \
--data '{
  "virtualAccountName": "Storefront collections Q2",
  "isActive": false
}'
```

## Sample Response

### Success scenario

```json
{
  "status": 0,
  "data": {
    "virtualAccountId": 2231266,
    "merchantId": 5014182,
    "virtualAccountNumber": "PURW2231266",
    "ifsc": "UTIB0CCH274",
    "merchantName": "Acme Pvt Ltd",
    "virtualAccountName": "Storefront collections Q2",
    "isActive": false,
    "externalRefId": "merchant-va-ref-001"
  },
  "msg": "Virtual account updated",
  "code": null
}
```

### Failure scenario

```json
{
  "status": 1,
  "data": "Error while updating virtual account.",
  "msg": null,
  "code": null
}
```

## Response Parameters

### data JSON Fields Description

| Parameter              | Description                                                                 |
| ---------------------- | --------------------------------------------------------------------------- |
| `virtualAccountId`     | PayU-assigned VA identifier                                                 |
| `merchantId`           | Sub-merchant MID                                                            |
| `virtualAccountName`   | Updated display name for the VA                                             |
| `virtualAccountNumber` | Account number shared with payers                                           |
| `ifsc`                 | IFSC for bank transfers to this VA                                          |
| `merchantName`         | Registered merchant name                                                    |
| `isActive`             | `false` after deactivation; `true` when the VA accepts new credits          |
| `externalRefId`        | Merchant reference ID, if provided at creation                              |

<Callout icon="📘" theme="info">
  ### Note:

  Deactivation blocks **new** incoming transfers to the VA. Credits already received and linked PayU transactions are not removed. Contact your PayU Key Account Manager (KAM) if you need to reactivate a VA.
</Callout>