---
title: Create Virtual Account API - PACB
deprecated: false
hidden: true
metadata:
  robots: index
---
Provision a **Virtual Account (VA)** for a Cross-Border Payments sub-merchant. PayU returns the VA number and IFSC that the payer uses for NEFT, RTGS, or IMPS transfers.

## Environment

| Environment | URL                                                      | Method |
| ----------- | -------------------------------------------------------- | ------ |
| Test        | `https://uatoneapi.payu.in/payout/v2/virtualAccounts`    | POST   |
| Production  | `https://payout.payumoney.com/payout/v2/virtualAccounts` | POST   |

## Request Parameters

### Request Header

| Parameter                      | Description                                                                                                           | Example                                                                 |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Authorization<br />`mandatory` | `String` - Bearer access token from Payouts authentication. For more information on generating Bearer token, refer to | Bearer aab9dc927c4a68af7eb95ef694f0b48bb731c5a1a7111786d6658d774db14188 |
| merchantId<br />`mandatory`    | `Integer` - PayU MID of the sub-merchant                                                                              | 12345                                                                   |
| Content-Type<br />`mandatory`  | `String` - Request body format. Set to `application/json`                                                             | application/json                                                        |

### Body Parameters

| Parameter                           | Description                                                  | Example                   |
| ----------------------------------- | ------------------------------------------------------------ | ------------------------- |
| virtualAccountName<br />`mandatory` | `String` - Display name for the VA in reports and dashboards | Storefront collections Q1 |
| externalRefId<br />`optional`       | `String` - Your reference ID for reconciliation              | merchant-va-ref-001       |

<details>
  <summary>Sample request</summary>

```curl
curl --location --request POST 'https://uatoneapi.payu.in/payout/v2/virtualAccounts' \
--header 'Authorization: Bearer <access_token>' \
--header 'merchantId: 12345' \
--header 'Content-Type: application/json' \
--data '{
  "virtualAccountName": "Storefront collections Q1",
  "externalRefId": "merchant-va-ref-001"
}'
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
    "isActive": true,
    "externalRefId": "merchant-va-ref-001"
  },
  "msg": "Virtual account created",
  "code": null
}
```

</details>

<details>
  <summary>Sample validation failure response</summary>

```json
{
  "status": 1,
  "data": "virtualAccountName is required",
  "msg": null,
  "code": 100125
}
```

</details>

<details>
  <summary>Sample generic failure response</summary>

```json
{
  "status": 1,
  "data": "Error while creating virtual account, please try again later.",
  "msg": null,
  "code": null
}
```

</details>

## Response parameters

| Parameter                   | Description                                                                               |
| --------------------------- | ----------------------------------------------------------------------------------------- |
| `data.virtualAccountId`     | PayU-assigned VA identifier. Use this in get-details, deactivate, and list-deposits APIs. |
| `data.merchantId`           | Sub-merchant MID the VA belongs to                                                        |
| `data.virtualAccountName`   | Name supplied at creation                                                                 |
| `data.virtualAccountNumber` | Account number the payer credits                                                          |
| `data.ifsc`                 | IFSC for the VA (corporate VA IFSC for Axis-backed accounts)                              |
| `data.merchantName`         | Registered merchant name                                                                  |
| `data.isActive`             | `true` when the VA accepts new credits                                                    |
| `data.externalRefId`        | Merchant reference ID, if provided                                                        |

<Callout icon="📘" theme="info">
  ### Note:

  The initial release supports **one active VA per sub-merchant MID**. Contact your PayU Key Account Manager (KAM) before creating additional VAs.
</Callout>

<br />
