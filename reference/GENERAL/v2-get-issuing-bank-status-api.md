---
title: v2 Get Issuing Bank Status API
deprecated: false
hidden: false
metadata:
  robots: index
---
This API allows merchants to check the status of an issuing bank's service using a BIN (Bank Identification Number).

HTTP post method: **POST**

## Endpoint

* **Production Environment**: `https://info.payu.in/merchant/postservice?form=2`

## Request parameters

| Parameter                         | Description                                                                                                                                             | Example |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `key`<br /><code>mandatory</code> | <code>String</code> Merchant's unique key provided by PayU.                                                                                             | JPM7Fg  |
| `bin`<br /><code>mandatory</code> | <code>String</code> Bank Identification Number (BIN), first six digits of the card. Optional value: `default` (to get all banks' statuses in an array). | 512345  |

## Sample request

```bash
curl --location 'https://info.payu.in/issuing-bank/v1/bin/?bin=512345&issuing_bank_status=true' \
--header 'Content-Type: application/json' \
--header 'date: {{date}}' \
--header 'Authorization: {{authorization}}' \
--data '{
    "bin": "512345"
}'
```

## Sample response

### Success scenario

```json
{
  "issuing_bank": "HDFC",
  "up_status": "1"
}
```

### Failure scenario (No Information Available)

```json
{
  "msg": "No information available",
  "status": 0
}
```

## Response Parameters

| Parameter      | Description                                                                                | Example                    |
| -------------- | ------------------------------------------------------------------------------------------ | -------------------------- |
| `issuing_bank` | The name of the issuing bank for the card.                                                 | `HDFC`                     |
| `up_status`    | The status of the issuing bank's service: `0` (down) or `1` (up).                          | `1`                        |
| `msg`          | Error message when no information is available.                                            | `No information available` |
| `status`       | Indicates that operation was unsuccessful (value: `0`). Only present in failure responses. | `0`                        |

## Response fields for JSON Array Requests (var1=default)

When `var1=default`, a response includes an array of JSON objects, each containing the following fields:

| Parameter    | Description                                         | Example                |
| ------------ | --------------------------------------------------- | ---------------------- |
| `ibibo_code` | Bank code for identifying the Net Banking service.  | `AXIB`                 |
| `title`      | Name and service of the bank.                       | `AXIS Bank NetBanking` |
| `up_status`  | Net Banking service status: `0` (down) or `1` (up). | `1`                    |
| `mode`       | Payment mode for which the status is displayed.     | `NB`                   |