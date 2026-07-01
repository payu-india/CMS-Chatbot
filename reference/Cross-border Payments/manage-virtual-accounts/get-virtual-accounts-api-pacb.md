---
title: Get Virtual Accounts API
deprecated: false
hidden: true
metadata:
  title: Get Virtual Accounts API - PACB
  robots: index
---
Retrieve a **paginated list** of Virtual Accounts provisioned for a Cross-Border Payments sub-merchant MID.

## Environment

| Environment | URL                                                   | Method |
| ----------- | ----------------------------------------------------- | ------ |
| Test        | `https://uatoneapi.payu.in/payout/v2/virtualAccounts` | GET    |
| Production  | `https://oneapi.payu.in/payout/v2/virtualAccounts`    | GET    |

## Request Parameters

### Authentication Logic

<HeaderAuthentication />

### Request Header

| Parameter                   | Description                              | Example |
| --------------------------- | ---------------------------------------- | ------- |
| merchantId<br />`mandatory` | `Integer` - PayU MID of the sub-merchant | 12345   |

## Request parameters

| Parameter                  | Description                                            | Example |
| -------------------------- | ------------------------------------------------------ | ------- |
| pageOffset<br />`optional` | `Integer` - Page number (1-based). Default: 1          | 1       |
| pageSize<br />`optional`   | `Integer` - Records per page. Default: 10. Maximum: 50 | 10      |

## Sample Request

```curl
curl --location --request GET 'https://uatoneapi.payu.in/payout/v2/virtualAccounts?pageOffset=1&pageSize=10' \
--header 'Authorization: {{authorization}}' \
--header 'merchantId: 12345'
```

## Sample Response

### Success scenario

#### When a list of virtual accounts exist

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

#### When no virtual accounts exist

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
                    <li>0 - If web service call failed.</li>
                    <li>1 - If web service call succeeded</li>
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
                <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">refer to <a href="data-json-fields-description">#data JSON Fields Description></td>
              </tr>
             
            </tbody>
          </table>
`}</HTMLBlock>

### data JSON Fields Description

| Parameter         | Description                            |
| ----------------- | -------------------------------------- |
| `noOfPages`       | Total pages for the current `pageSize` |
| `totalElements`   | Total VA records for the MID           |
| `currentPage`     | Current page number                    |
| `virtualAccounts` | Array of VA objects                    |

<br />