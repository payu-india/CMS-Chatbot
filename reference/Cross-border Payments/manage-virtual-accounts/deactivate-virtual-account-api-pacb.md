---
title: ' Deactivate Virtual Account API - PACB'
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: Deactivate Virtual Account API - PACB
deprecated: false
hidden: false
metadata:
  robots: index
---
Deactivate a **Virtual Account** so it no longer accepts new bank credits. Historic VA details and deposit records remain available through list and transaction APIs.

For the full VA management set, refer to [PACB Virtual Account APIs](ref:pacb-virtual-account-apis).

## Environment

| Environment | URL | Method |
| --- | --- | --- |
| Test | `https://uatoneapi.payu.in/payout/v2/virtualAccounts/deactivate` | PATCH |
| Production | `https://payout.payumoney.com/payout/v2/virtualAccounts/deactivate` | PATCH |

## Request headers

| Parameter | Description | Example |
| --- | --- | --- |
| Authorization<br />`mandatory` | `String` - Bearer access token from Payouts authentication | Bearer aab9dc927c4a68af7eb95ef694f0b48bb731c5a1a7111786d6658d774db14188 |
| merchantId<br />`mandatory` | `Integer` - PayU MID of the sub-merchant | 12345 |
| virtualAccountId<br />`mandatory` | `Integer` - PayU-assigned VA identifier to deactivate | 987654 |

<details>
  <summary>Sample request</summary>

  ```curl
  curl --location --request PATCH 'https://uatoneapi.payu.in/payout/v2/virtualAccounts/deactivate' \
  --header 'Authorization: Bearer <access_token>' \
  --header 'merchantId: 12345' \
  --header 'virtualAccountId: 987654'
  ```
</details>

<details>
  <summary>Sample success response</summary>

  ```json
  {
    "status": 0,
    "data": {
      "virtualAccountId": 987654,
      "merchantId": 12345,
      "virtualAccountName": "Storefront collections Q1",
      "virtualAccountNumber": "PUIN987654",
      "ifsc": "UTIB0CCH274",
      "merchantName": "Acme Pvt Ltd",
      "isActive": false,
      "externalRefId": "merchant-va-ref-001"
    },
    "msg": "Virtual account deactivated",
    "code": null
  }
  ```
</details>

## Response parameters

| Parameter | Description |
| --- | --- |
| `data.isActive` | `false` after successful deactivation |
| `msg` | Confirmation message (`Virtual account deactivated`) |
| Other `data` fields | Same as [Get Virtual Account Details API - PACB](ref:get-virtual-account-details-api-pacb) |

> 📘 Note:
>
> Deactivation blocks **new** incoming transfers to the VA. Credits already received and linked PayU transactions are not removed. Contact your PayU Key Account Manager (KAM) if you need to reactivate a VA.
