---
title: v2 Get BIN Info API
deprecated: false
hidden: true
metadata:
  robots: index
---
This API allows merchants to retrieve information about a specific Bank Identification Number (BIN) or a list of BINs.

HTTP Method: **POST**

## Request header

<HeaderAuthentication />

<br />

## Request parameters

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
      <td><code>key</code><br/><code>mandatory</code></td>
      <td><code>String</code> Merchant's unique key generated through PayU dashboard.</td>
      <td>JPM7Fg</td>
    </tr>
    <tr>
      <td><code>scope</code><br/><code>mandatory</code></td>
      <td><code>String</code> Specifies the scope of search: <br/> <code>1</code>: Single BIN<br/><code>2</code>: Specific feature-level BIN list<br/><code>3</code>: All BIN details.</td>
      <td>1</td>
    </tr>
    <tr>
      <td><code>binNumber</code><br/><code>mandatory/optional</code></td>
      <td><code>String</code> Based on <code>scope</code> value: BIN number (for <code>scope=1</code> or <code>scope=2</code>), or empty for <code>scope=3</code>.</td>
      <td>512345</td>
    </tr>
    <tr>
      <td><code>startIndex</code><br/><code>optional</code></td>
      <td><code>String</code> Start index for multiple BINs. Default: <code>0</code></td>
      <td>0</td>
    </tr>
    <tr>
      <td><code>limit</code><br/><code>optional</code></td>
      <td><code>String</code> Limit (offset) the number of BINs fetched in a single response. Default: <code>100</code></td>
      <td>100</td>
    </tr>
    <tr>
      <td><code>checkNativeOTPAndSI</code><br/><code>optional</code></td>
      <td><code>String</code> Check for Native OTP and SI support (<code>1</code> enables relevant fields in the response).</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Sample request

```bash
curl --location 'https://info.payu.in/issuing-bank/v1/bin' \
--header 'Content-Type: application/json' \
--header 'date: {{date}}' \
--header 'Authorization: {{authorization}}' \
--data '{
    "bin": "512345"
  }'
```

## Sample response

### For single card

```json
{
  "status": 1,
  "data": {
    "bins_data": {
      "issuing_bank": "HDFC",
      "bin": "512345",
      "category": "creditcard",
      "card_type": "MAST",
      "is_domestic": 1,
      "is_atmpin_card": 1,
      "is_otp_on_the_fly": 1,
      "is_zero_redirect_supported": 1,
      "is_si_supported": 0
    }
  }
}
```

### For multiple cards

```json
{
  "status": 1,
  "data": {
    "total_count": 2580,
    "last": 0,
    "bins_data": {
      "37100": {
        "issuing_bank": "AMEX",
        "bin": "37100",
        "category": "UNKNOWN",
        "card_type": "AMEX",
        "is_domestic": 1,
        "is_atmpin_card": 1,
        "is_otp_on_the_fly": 1
      },
      "37101": {
        "issuing_bank": "AMEX",
        "bin": "37101",
        "category": "UNKNOWN",
        "card_type": "AMEX",
        "is_domestic": 1,
        "is_atmpin_card": 1,
        "is_otp_on_the_fly": 1
      }
      // More BINs...
    },
    "nextStart": 6
  }
}
```

### Failure response

```json
{
  "status": 0,
  "data": "Invalid bin passed in var2"
}
```

## Response parameters

| Parameter | Description                                               | Example   |
| --------- | --------------------------------------------------------- | --------- |
| `status`  | Status of the API call: `1` for success, `0` for failure. | `1`       |
| `data`    | Contains the BIN information or error message.            | See below |

### BIN Data Fields (for Single Card)

| Field                        | Description                                                    | Example      |
| ---------------------------- | -------------------------------------------------------------- | ------------ |
| `issuing_bank`               | Issuing bank for the provided BIN.                             | `HDFC`       |
| `bin`                        | Card BIN number.                                               | `512345`     |
| `category`                   | Card category: `creditcard` or `debitcard`.                    | `creditcard` |
| `card_type`                  | Card type: MAST (MasterCard), VISA, AMEX, etc.                 | `MAST`       |
| `is_domestic`                | `1`: Domestic card, `0`: International card.                   | `1`          |
| `is_atmpin_card`             | `1`: ATM PIN supported, `0`: Not supported.                    | `1`          |
| `is_otp_on_the_fly`          | `1`: OTP-on-the-fly enabled, `0`: Not enabled.                 | `1`          |
| `is_zero_redirect_supported` | `1`: Zero Redirect supported, `0`: Not supported.              | `1`          |
| `is_si_supported`            | `1`: Standing Instructions (SI) supported, `0`: Not supported. | `0`          |

### Multiple Cards Response Fields

| Field         | Description                                                                                            | Example           |
| ------------- | ------------------------------------------------------------------------------------------------------ | ----------------- |
| `total_count` | Total number of cards available for the provided request.                                              | `2580`            |
| `last`        | `1`: Last set of BIN information returned. `0`: More BIN information available for further pagination. | `0`               |
| `bins_data`   | List of bins in JSON array, each having the same structure as for single card response.                | See example above |
| `nextStart`   | Indicates the index for the next batch of cards in case of pagination.                                 | `6`               |