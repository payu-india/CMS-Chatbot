---
title: List Virtual Account Deposits API
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: List Virtual Account Deposits API
deprecated: false
hidden: true
metadata:
  title: List Virtual Account Deposits API - PACB
  robots: index
---
List **bank credits** received on a Virtual Account. Use this API to reconcile incoming NEFT, RTGS, or IMPS transfers against payer references and UTRs.

## Environment

| Environment | URL                                                           | Method |
| ----------- | ------------------------------------------------------------- | ------ |
| Test        | `https://uatoneapi.payu.in/payout/v2/virtualAccounts/deposits` | GET    |
| Production  | `https://oneapi.payu.in/payout/v2/virtualAccounts/deposits`   | GET    |

## Request Parameters

### Authorization Logic in Header

<HeaderAuthentication />

<br />

### Query Parameters

| Parameter                         | Description                                                                                                                                  | Example |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| virtualAccountId<br />`mandatory` | `String` - PayU-assigned VA identifier (`virtualAccountId`) or virtual account number (for example `PURW2231266`)                            | 2231266 |
| pageOffset<br />`optional`        | `Integer` - Page number (1-based). Default: 1                                                                                                | 1       |
| pageSize<br />`optional`          | `Integer` - Records per page. Default: 10. Maximum: 50                                                                                     | 10      |

## Sample Request

```curl
curl --location --request GET 'https://uatoneapi.payu.in/payout/v2/virtualAccounts/deposits?virtualAccountId=2231266&pageOffset=1&pageSize=10' \
--header 'Authorization: {{authorization}}'
```

## Sample Response

### Success scenario

```json
{
  "status": 0,
  "data": [
    {
      "utr": "AXISUTR123456789",
      "depositDateTime": "2026-06-17T10:30:00.000+00:00",
      "amount": 5000.0,
      "remitterAccountNumber": "1234567890",
      "ifsc": "HDFC0001234"
    }
  ],
  "msg": null,
  "code": null
}
```

### When no deposits exist

```json
{
  "status": 0,
  "data": [],
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
                <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">null</td>
              </tr>
              <tr>
                <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">data</td>
                <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">This parameter contains the list of deposit records in JSON format. For more information, refer to <a href="#data-json-fields-description">data JSON Fields Description</a>
</td>
                <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">refer to <a href="#data-json-fields-description">data JSON Fields Description</a></td>
              </tr>
             
            </tbody>
          </table>
`}</HTMLBlock>

### data JSON Fields Description

| Parameter                      | Description                                                              |
| ------------------------------ | ------------------------------------------------------------------------ |
| `data[].utr`                   | Bank UTR / reference number for the credit                               |
| `data[].depositDateTime`       | Timestamp when the deposit was recorded (ISO-8601)                       |
| `data[].amount`                | Credited amount in INR                                                   |
| `data[].remitterAccountNumber` | Payer bank account number, when provided by the remitter bank            |
| `data[].ifsc`                  | Remitter bank IFSC, when provided by the remitter bank                   |

<Callout icon="📘" theme="info">
  ### Note:

  Remitter IFSC may not be present for every transfer depending on the payment mode and remitter bank. Use payment webhooks and [Verify Payment API](ref:verify_payment_api) for end-to-end transaction status after PayU creates a collection transaction from the bank credit.
</Callout>

<br />