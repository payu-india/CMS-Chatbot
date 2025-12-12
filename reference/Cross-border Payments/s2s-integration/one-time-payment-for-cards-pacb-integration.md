---
title: One-Time Payment for Cards - PACB Integration
deprecated: false
hidden: true
metadata:
  robots: index
---

For CIT (Customer Initiated Transaction) card payments, append the following parameters to your basic S2S payload.

## Payment Options

### Option A: Plain Cards

For standard card transactions without tokenization. Refer to [Complete Card Details Payment](ref:complete-card-details-payment).

```bash
--data-urlencode 'pg=CC' \
--data-urlencode 'bankcode=CC' \
--data-urlencode 'ccnum=5506900480000008' \
--data-urlencode 'ccexpyr=2026' \
--data-urlencode 'ccexpmon=09' \
--data-urlencode 'ccvv=123' \
--data-urlencode 'ccname=TEST'
```

| Parameter | Description | Example |
|-----------|-------------|---------|
| `ccnum` | Full card number | `5506900480000008` |
| `ccexpyr` | Card expiry year (4 digits) | `2026` |
| `ccexpmon` | Card expiry month (2 digits) | `09` |
| `ccvv` | Card CVV/CVC | `123` |
| `ccname` | Cardholder name | `TEST` |

---

### Option B: Plain Cards + Tokenization

To store the card for future use, append these parameters to Option A:

```bash
--data-urlencode 'user_credentials=PRiQvJ:customer_1112' \
--data-urlencode 'store_card=1'
```

| Parameter | Description | Required |
|-----------|-------------|----------|
| `user_credentials` | Format: `merchant_key:customer_id`. Mandatory for token provisioning & PayU token processing flows. | Yes |
| `store_card` | Set to `1` to store the card token | Yes |

---

### Option C: Using PayU Tokens

For transactions using previously stored PayU tokens. Refer to [Using Card Tokenized with PayU](ref:using-card-tokenized-with-payu).

```bash
--data-urlencode 'user_credentials=PRiQvJ:customer_1112' \
--data-urlencode 'storecard_token_type=0' \
--data-urlencode 'store_card_token=10a7d7a45b72644460f108'
```

| Parameter | Description |
|-----------|-------------|
| `user_credentials` | Format: `merchant_key:customer_id` |
| `storecard_token_type` | Set to `0` for PayU tokens |
| `store_card_token` | Token value from [Get User Cards API](ref:get_user_cards_api) |

> 📘 Note:
>
> Use the [Get User Cards API](ref:get_user_cards_api) with the same `user_credentials` used when storing the card to retrieve the `store_card_token` value.

---

### Option D: Using Network Tokens

For transactions using network tokens (Visa/Mastercard tokens). Refer to [Using Network Tokens](ref:using-network-tokens).

```bash
--data-urlencode 'additional_info={"last4Digits":"0008","tavv":"UAQAAAAMKJAQg+w+0IagAAAAAAAA","trid":"400000340044","tokenRefNo":"DM4MMC1US00000003e1ebda85d81490d97cdc87975c7c3bc"}' \
--data-urlencode 'storecard_token_type=1' \
--data-urlencode 'store_card_token=5506900495826660' \
--data-urlencode 'ccexpyr=2026' \
--data-urlencode 'ccexpmon=09'
```

| Parameter | Description |
|-----------|-------------|
| `additional_info` | JSON object containing network token metadata |
| `storecard_token_type` | Set to `1` for network tokens |
| `store_card_token` | Network Token value |
| `ccexpyr` | Token expiry year (not card expiry) |
| `ccexpmon` | Token expiry month (not card expiry) |

#### additional_info Object Structure

| Field | Description |
|-------|-------------|
| `last4Digits` | Last 4 digits of the original card |
| `tavv` | Token Authentication Verification Value |
| `trid` | Token Requestor ID |
| `tokenRefNo` | Token Reference Number |

> ⚠️ Important:
>
> When using network tokens, the `ccexpyr` and `ccexpmon` should contain the **token expiry** values, not the original card expiry values.