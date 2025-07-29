---
title: S2S Eligible BINs API
deprecated: false
hidden: false
metadata:
  robots: index
---
The **S2S Eligible BINs** API is similar to the **Get BIN Info** API, but used in S2S environment. For more information on Get BIN Info API, refer to [Get Bin Info API](ref:v2-get-bin-info-api).

## Environment

| Environment            | URL                                                                                          |
| :--------------------- | :------------------------------------------------------------------------------------------- |
| Production Environment | [https://info.payu.in/issuing-bank/v1/bin?s2s](https://info.payu.in/issuing-bank/v1/bin?s2s) |
| Test Environment       | [https://test.payu.in/issuing-bank/v1/bin?s2s](https://test.payu.in/issuing-bank/v1/bin?s2s) |

## Request header

<V2_payment_header_params />

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
      <td>s2s<br/><code>optional</code></td>
      <td><code>String</code> Flag to indicate server-to-server communication mode.</td>
      <td>s2s</td>
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
      <td>bin<br/><code>mandatory</code></td>
      <td><code>String</code> The first six digits ofcard (card BIN) must be specified here.</td>
      <td>512345</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Sample request

```
curl --location 'https://info.payu.in/issuing-bank/v1/bin?s2s' \
--header 'Content-Type: application/json' \
--header 'date: {{date}}' \
--header 'Authorization: {{authorization}}' \
--data '{
    "bin": "512345"
  }'
```