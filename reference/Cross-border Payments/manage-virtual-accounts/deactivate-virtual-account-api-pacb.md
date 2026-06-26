---
title: ' Deactivate Virtual Account API'
deprecated: false
hidden: true
metadata:
  title: ' Deactivate Virtual Account API - PACB'
  robots: index
---
Deactivate a **Virtual Account** so it no longer accepts new bank credits. Historic VA details and deposit records remain available through list and transaction APIs.

For the full VA management set, refer to [PACB Virtual Account APIs](ref:pacb-virtual-account-apis).

## Environment

| Environment | URL                                                                 | Method |
| ----------- | ------------------------------------------------------------------- | ------ |
| Test        | `https://uatoneapi.payu.in/payout/v2/virtualAccounts/deactivate`    | PATCH  |
| Production  | `https://payout.payumoney.com/payout/v2/virtualAccounts/deactivate` | PATCH  |

## Request Header

| Parameter                         | Description                                                | Example                                                                                     |
| --------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Authorization<br />`mandatory`    | `String` - Bearer access token from Payouts authentication | Bearer aab9dc927c4a<br />68af7eb95ef694f0b4<br />8bb731c5a1a7111786d<br />\|6658d774db14188 |
| merchantId<br />`mandatory`       | `Integer` - PayU MID of the sub-merchant                   | 12345                                                                                       |
| virtualAccountId<br />`mandatory` | `Integer` - PayU-assigned VA identifier to deactivate      | 987654                                                                                      |

## Sample Request

```curl
curl --location --request PATCH 'https://uatoneapi.payu.in/payout/v2/virtualAccounts/deactivate' \
--header 'Authorization: Bearer <access_token>' \
--header 'merchantId: 12345' \
--header 'virtualAccountId: 987654'
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
    "isActive": false,
    "externalRefId": "merchant-va-ref-001"
  },
  "msg": "Virtual account deactivated",
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
                <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">refer to <a href="data-json-fields-description">data JSON Fields Descriptiont></td>
              </tr>
             
            </tbody>
          </table>
`}</HTMLBlock>

### data JSON Fields Description

| Parameter           | Description                                                                                |
| ------------------- | ------------------------------------------------------------------------------------------ |
| isActive`     | `false` after successful deactivation                                                      |


<Callout icon="📘" theme="info">
Note:

  Deactivation blocks **new** incoming transfers to the VA. Credits already received and linked PayU transactions are not removed. Contact your PayU Key Account Manager (KAM) if you need to reactivate a VA.
</Callout>

<br />
