---
title: Get Virtual Accounts API - PACB
deprecated: false
hidden: false
metadata:
  robots: index
---
Retrieve a **paginated list** of Virtual Accounts provisioned for a Cross-Border Payments sub-merchant MID.

## Environment

| Environment | URL                                                      | Method |
| ----------- | -------------------------------------------------------- | ------ |
| Test        | `https://uatoneapi.payu.in/payout/v2/virtualAccounts`    | GET    |
| Production  | `https://payout.payumoney.com/payout/v2/virtualAccounts` | GET    |

## Request headers

| Parameter                      | Description                                                | Example                                                                 |
| ------------------------------ | ---------------------------------------------------------- | ----------------------------------------------------------------------- |
| Authorization<br />`mandatory` | `String` - Bearer access token from Payouts authentication | Bearer aab9dc927c4a68af7eb95ef694f0b48bb731c5a1a7111786d6658d774db14188 |
| merchantId<br />`mandatory`    | `Integer` - PayU MID of the sub-merchant                   | 12345                                                                   |

## Request parameters

| Parameter                  | Description                                            | Example |
| -------------------------- | ------------------------------------------------------ | ------- |
| pageOffset<br />`optional` | `Integer` - Page number (1-based). Default: 1          | 1       |
| pageSize<br />`optional`   | `Integer` - Records per page. Default: 10. Maximum: 50 | 10      |

<details>
  <summary>Sample request</summary>

```curl
curl --location --request GET 'https://uatoneapi.payu.in/payout/v2/virtualAccounts?pageOffset=1&pageSize=10' \
--header 'Authorization: Bearer <access_token>' \
--header 'merchantId: 12345'
```

</details>

<details>
  <summary>Sample success response</summary>

```json
{
  "status": 0,
  "data": {
    "noOfPages": 2,
    "totalElements": 15,
    "currentPage": 1,
    "virtualAccounts": [
      {
        "virtualAccountId": 987654,
        "merchantId": 12345,
        "virtualAccountName": "Storefront collections Q1",
        "virtualAccountNumber": "PUIN987654",
        "ifsc": "UTIB0CCH274",
        "merchantName": "Acme Pvt Ltd",
        "isActive": true,
        "externalRefId": "merchant-va-ref-001"
      }
    ]
  },
  "msg": null,
  "code": null
}
```

</details>

<details>
  <summary>Sample empty response</summary>

```json
{
  "status": 0,
  "data": {
    "noOfPages": 0,
    "totalElements": 0,
    "currentPage": 1,
    "virtualAccounts": []
  },
  "msg": null,
  "code": null
}
```

</details>

## Response parameters

| Parameter              | Description                                                                                                            |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `data.noOfPages`       | Total pages for the current `pageSize`                                                                                 |
| `data.totalElements`   | Total VA records for the MID                                                                                           |
| `data.currentPage`     | Current page number                                                                                                    |
| `data.virtualAccounts` | Array of VA objects (same fields as [Create Virtual Account API - PACB](ref:create-virtual-account-api-pacb) response) |

For a single VA by ID, use [Get Virtual Account Details API - PACB](ref:get-virtual-account-details-api-pacb).
