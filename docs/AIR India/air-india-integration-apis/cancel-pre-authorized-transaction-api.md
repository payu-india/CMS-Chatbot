---
title: Cancel Pre-Authorized Transaction API
deprecated: false
hidden: true
metadata:
  robots: index
---
Cancels a pre-authorized transaction, releasing the held funds back to the customer. Used when a booking is cancelled before capture.

## Endpoint

| Environment | Base URL |
|-------------|----------|
| Test | `https://test.payu.in/merchant/postservice.php?form=2` |
| Production | `https://info.payu.in/merchant/postservice.php?form=2` |

## Sample Request

```bash
curl -X POST 'https://test.payu.in/merchant/postservice.php?form=2' \
  -H 'Content-Type: multipart/form-data' \
  -F 'key=<merchant-key>' \
  -F 'hash=<sha512-hash>' \
  -F 'var1=999000000008527' \
  -F 'var2=ad800ef0ccc2f4ad9aasd' \
  -F 'command=cancel_transaction'
```

## Sample Response

### Success Response

```json
{
  "status": 1,
  "msg": "Cancellation Successful"
}
```

### Failure Response

```json
{
  "status": 0,
  "msg": "Cancelled failed",
  "error_code": 105
}
```

## Request Parameters
### Header Authentication Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| Content-Type<br/>`mandatory` | `string` Media type of the form request. Must be `multipart/form-data` or `application/x-www-form-urlencoded`. | `multipart/form-data` |

### Body Parameters

Form parameters (not JSON):

| Parameter | Description | Example |
|-----------|-------------|---------|
| key<br/>`mandatory` | `string` Merchant key. | `smsplus` |
| command<br/>`mandatory` | `string` Must be `cancel_transaction` (case-sensitive). | `cancel_transaction` |
| var1<br/>`mandatory` | `string` **PayU ID** (payuId) from pre-authorize operation. | `999000000008527` |
| var2<br/>`mandatory` | `string` **Merchant unique reference token** for this cancellation. | `ad800ef0ccc2f4ad9aasd` |
| hash<br/>`mandatory` | `string` SHA512 hash calculated as: `SHA512(key + "|" + command + "|" + var1 + "|" + salt)`. Note: Use pipe character (|) as separator. | `912b83345ad3ed35cece78cf7696f71a...` |

## Response Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| status | `number` `1` = success, `0` = failure. | `1` |
| msg | `string` Success or failure message. | `Cancellation Successful` |
| error_code | `number` Error code (only on failure). | `105` |