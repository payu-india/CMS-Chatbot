---
title: Create Virtual Account API
deprecated: false
hidden: true
metadata:
  title: Create Virtual Account API - PACB
  robots: index
---
Provision a **Virtual Account (VA)** for a Cross-Border Payments sub-merchant. PayU returns the VA number and IFSC that the payer uses for NEFT, RTGS, or IMPS transfers.

## Environment

| Environment | URL                                                   | Method |
| ----------- | ----------------------------------------------------- | ------ |
| Test        | `https://uatoneapi.payu.in/payout/v2/virtualAccounts` | POST   |
| Production  | `https://oneapi.payu.in/payout/v2/virtualAccounts`    | POST   |

## Request Parameters

### Authorization Logic in Header

<HeaderAuthentication />

<br />

### Request Header

| Parameter                      | Description                                                                                                           | Example                                                                                         |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| merchantId<br />`mandatory`    | `Integer` - PayU MID of the sub-merchant                                                                              | 12345                                                                                           |
| Content-Type<br />`mandatory`  | `String` - Request body format. Set to `application/json`                                                             | application/json                                                                                |

### Body Parameters

| Parameter                           | Description                                                  | Example                   |
| ----------------------------------- | ------------------------------------------------------------ | ------------------------- |
| virtualAccountName<br />`mandatory` | `String` - Display name for the VA in reports and dashboards | Storefront collections Q1 |
| externalRefId<br />`optional`       | `String` - Your reference ID for reconciliation              | merchant-va-ref-001       |

## Sample Request

```curl
curl --location --request POST 'https://uatoneapi.payu.in/payout/v2/virtualAccounts' \
--header 'Authorization: {{authorization}}' \
--header 'merchantId: 12345' \
--header 'Content-Type: application/json' \
--data '{
  "virtualAccountName": "Storefront collections Q1",
  "externalRefId": "merchant-va-ref-001"
}'
```

## Sample Response

### Success scenario

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

### Failure scenario

**virtualAccountName parameter value is posted blank**

```json
{
  "status": 1,
  "data": "virtualAccountName is required",
  "msg": null,
  "code": 100125
}
```

**Virtual Account Name is already present or unable to create**

```json
{
  "status": 1,
  "data": "Error while creating virtual account, please try again later.",
  "msg": null,
  "code": null
}
```

## Response Parameters

<HTMLBlock>{`
          <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
            <thead>
              <tr style="background-color: #f5f5f5;">
                <th style="padding: 10px; border: 1px solid #ddd; font-weight: bold; text-align: left;">Parameter</th>
                <th style="padding: 10px; border: 1px solid #ddd; font-weight: bold; text-align: left;">Description</th>
                <th style="padding: 10px; border: 1px solid #ddd; font-weight: bold; text-align: left;">Example</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">status</td>
                <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">
                  This parameter returns the status of web service call. The status can be any of the following: 
                  <ul style="padding-left: 20px; margin-top: 5px;">
                    <li>1 - If web service call failed.</li>
                    <li>0 - If web service call succeeded</li>
                  </ul>
                </td>
                <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">0</td>
              </tr>
              <tr>
                <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">msg</td>
                <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">This parameter returns the reason string.</td>
                <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">
                  For example, any of the following messages are displayed:
                  <ul style="padding-left: 20px; margin-top: 5px;">
                    <li>Parameter missing</li>
                    <li>Token is empty</li>
                    <li>Amount is empty</li>
                    <li>Transaction not exists</li>
                  </ul>
                </td>
              </tr>
              <tr>
                <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">data</td>
                <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">This parameter contains the virtual account details in JSON format. For more information, refer to <a href="#data-json-fields-description">data JSON Fields Description</a>
</td>
                <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">refer to <a href="#data-json-fields-description">data JSON Fields Description></td>
              </tr>
             
            </tbody>
          </table>
`}</HTMLBlock>

### data JSON Fields Description

| Parameter              | Description                                                                               |
| ---------------------- | ----------------------------------------------------------------------------------------- |
| `virtualAccountId`     | PayU-assigned VA identifier. Use this in get-details, deactivate, and list-deposits APIs. |
| `merchantId`           | Sub-merchant MID the VA belongs to                                                        |
| `virtualAccountName`   | Name supplied at creation                                                                 |
| `virtualAccountNumber` | Account number the payer credits                                                          |
| `ifsc`                 | IFSC for the VA (corporate VA IFSC for Axis-backed accounts)                              |
| `merchantName`         | Registered merchant name                                                                  |
| `isActive`             | `true` when the VA accepts new credits                                                    |
| `externalRefId`        | Merchant reference ID, if provided                                                        |

<Callout icon="📘" theme="info">
  ### Note:

  The initial release supports **one active VA per sub-merchant MID**. Contact your PayU Key Account Manager (KAM) before creating additional VAs.
</Callout>

<br />