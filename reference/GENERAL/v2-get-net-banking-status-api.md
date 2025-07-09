---
title: v2 Get Net Banking Status API
deprecated: false
hidden: false
metadata:
  robots: index
---
This API allows merchants to check the status of Net Banking services for banks, helping to filter out banks that are currently down during the payment process.

HTTP Method: **POST**

**Endpoint**

* **Production Environment**: `https://info.payu.in/merchant/postservice`
  <br />

## Request Headers

<HeaderAuthentication />



## Sample Response

### For a Specific Bank

```json
{
  "ibibo_code": "AXIB",
  "title": "AXIS Bank NetBanking",
  "up_status": 0,
  "mode": "NB"
}
```

### For All Banks (`var1=default`)

```json
{
  "AXIB": {
    "ibibo_code": "AXIB",
    "title": "AXIS Bank NetBanking",
    "up_status": 0,
    "mode": "NB"
  },
  "SBIB": {
    "ibibo_code": "SBIB",
    "title": "State Bank of India",
    "up_status": 1,
    "mode": "NB"
  },
  "UPI": {
    "ibibo_code": "UPI",
    "title": "Test UPI",
    "up_status": 1,
    "mode": "UPI"
  }
}
```

## Response Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `ibibo_code` | The bank code for which the Net Banking status is displayed. | `AXIB` |
| `title` | The bank name and the Net Banking service title. | `AXIS Bank NetBanking` |
| `up_status` | Status of the Net Banking service: `0` (down) or `1` (up). | `1` |
| `mode` | The payment mode for the bank. | `NB` |

## Notes

1. When you specify a bank code in `var1`, the response will contain a single JSON object with the status of that specific bank.
2. When you use `var1=default`, the response will contain a JSON object with the status of all available banks, organized by their bank codes.
