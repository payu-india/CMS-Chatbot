---
title: Partner Payment Links UPI Intent Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
Create shareable payment links that launch the customer's UPI app directly using UPI Intent flow. This provides a seamless payment experience without redirecting to PayU's hosted page.

## How it works?

1. **Create Payment Link** — Call Partner Payments API with `txn_s2s_flow=4` and S2S parameters
2. **Share Link** — Send the generated link via WhatsApp, SMS, or any messaging channel
3. **Customer Opens Link** — Link redirects to PayU's UPI Intent page
4. **UPI App Launch** — Customer's UPI app is automatically invoked
5. **Complete Payment** — Customer authorizes payment in their UPI app
6. **Webhook Notification** — Receive real-time payment status update

## Prerequisites

<Note>
✅ OAuth access token with `partner_payment_links` scope  
✅ Partner and merchant registered with PayU  
✅ Webhook URLs configured in `partner_webhook_urls` table  
✅ Customer's phone number (for link sharing)
</Note>

***

## Create UPI Intent Payment Link

### Endpoint

**HTTP Method:** POST

**Environment URLs:**

| Environment | URL                                                              |
| ----------- | ---------------------------------------------------------------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer/partner/payments` |
| Production  | `https://api.payu.in/partner/payments`                           |

### Request Headers

```
Authorization: Bearer <FINAL_ACCESS_TOKEN>
Content-Type: application/json
```

### Request Parameters

<table>
<thead>
<tr>
<th align="left">Parameter</th>
<th align="left">Type &amp; Description</th>
<th align="left">Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>txnid</code></td>
<td>string — Unique transaction ID</td>
<td>UPIPL28471834809170985</td>
</tr>
<tr>
<td><code>amount</code></td>
<td>string — Payment amount</td>
<td>500.00</td>
</tr>
<tr>
<td><code>productinfo</code></td>
<td>string — Product description</td>
<td>UPI Payment for Order #12345</td>
</tr>
<tr>
<td><code>phone</code></td>
<td>string — Customer phone number (10 digits)</td>
<td>919876543210</td>
</tr>
<tr>
<td><code>merchant_id</code></td>
<td>integer — PayU merchant ID</td>
<td>8739528</td>
</tr>
<tr>
<td><code>reseller_id</code></td>
<td>string — Partner/reseller UUID</td>
<td>11ee-0e7e-5403fde2-9523-0a696b110fde</td>
</tr>
<tr>
<td><code>txn_s2s_flow</code></td>
<td>string — Must be "4" for UPI Intent</td>
<td>4</td>
</tr>
<tr>
<td><code>s2s_client_ip</code></td>
<td>string — Customer IP address (mandatory)</td>
<td>157.240.22.9</td>
</tr>
<tr>
<td><code>s2s_device_info</code></td>
<td>string — Device user-agent (mandatory)</td>
<td>Mozilla/5.0 (Linux; Android 10)</td>
</tr>
<tr>
<td><code>hash</code></td>
<td>string — SHA-512 hash</td>
<td>(computed hash)</td>
</tr>
</tbody>
</table>

<Warning>
**Mandatory S2S Fields:** When `txn_s2s_flow=4`, both `s2s_client_ip` and `s2s_device_info` are **required**. Omitting them will cause an error.
</Warning>

**Optional Parameters:**

| Parameter            | Type & Description        | Example                                           |
| -------------------- | ------------------------- | ------------------------------------------------- |
| `firstname`, `email` | string — Customer details | Amit, [amit@example.com](mailto:amit@example.com) |
| `udf1` - `udf5`      | string — Custom fields    | upi_intent_link                                   |

### Hash Generation

```
merchant_id|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||client_secret
```

### Sample Request

```bash
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/payments' \
--header 'Authorization: Bearer 039e0d1d70f467f946e2d73bd43868df856cfaa352ea54591a76bfc4a08d3487' \
--header 'Content-Type: application/json' \
--data '{
  "txnid": "UPIPL28471834809170985",
  "amount": "500.00",
  "productinfo": "UPI Payment for Order #12345",
  "firstname": "",
  "email": "",
  "phone": "919876543210",
  "merchant_id": 8739528,
  "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
  "txn_s2s_flow": "4",
  "s2s_client_ip": "157.240.22.9",
  "s2s_device_info": "Mozilla/5.0 (Linux; Android 10)",
  "udf5": "upi_intent_link",
  "hash": "COMPUTED_HASH_VALUE"
}'
```

```python
import requests
import hashlib
import time

def create_upi_intent_payment_link(phone, amount, description, client_ip, device_info):
    url = "https://test-partnerapilayer.payu.in/apilayer/partner/payments"
    
    txnid = f"UPIPL{int(time.time() * 1000)}"
    merchant_id = 8739528
    
    # Compute hash
    hash_string = f"{merchant_id}|{txnid}|{amount}|{description}|||||||upi_intent_link||||||YOUR_CLIENT_SECRET"
    payment_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
    
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Content-Type": "application/json"
    }
    
    payload = {
        "txnid": txnid,
        "amount": amount,
        "productinfo": description,
        "phone": phone,
        "merchant_id": merchant_id,
        "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
        "txn_s2s_flow": "4",
        "s2s_client_ip": client_ip,
        "s2s_device_info": device_info,
        "udf5": "upi_intent_link",
        "hash": payment_hash
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

# Usage
result = create_upi_intent_payment_link(
    phone="919876543210",
    amount="500.00",
    description="UPI Payment for Order #12345",
    client_ip="157.240.22.9",
    device_info="Mozilla/5.0 (Linux; Android 10)"
)

print(f"Payment Link: {result.get('redirectUri')}")
```

### Sample Response

```json
{
  "redirectUri": "https://secure.payu.in/_payment?mihpayid=403993715521855096&amount=500.00&txnid=UPIPL28471834809170985&key=JPM7Fg&productinfo=UPI+Payment+for+Order+%2312345&phone=919876543210&txn_s2s_flow=4..."
}
```

***

## Share UPI Intent Link

### Via WhatsApp

```python
def share_upi_link_whatsapp(phone, payment_link, amount):
    message = f"""Hi! You have a payment request.

Amount: Rs. {amount}
Payment Method: UPI

Click to pay with UPI:
{payment_link}

Your UPI app will open automatically.
"""
    
    send_whatsapp_message(phone, message)
```

### Via SMS

```python
def share_upi_link_sms(phone, payment_link, amount):
    message = f"Pay Rs.{amount} via UPI: {payment_link}"
    send_sms(phone, message)
```

***

## Customer Experience

When the customer opens the link:

1. **Link Opens** → PayU UPI Intent page loads
2. **UPI App Detection** → System detects installed UPI apps
3. **App Selection** → Customer selects their preferred UPI app (Google Pay, PhonePe, Paytm, etc.)
4. **App Launch** → UPI app opens with pre-filled payment details
5. **Authorization** → Customer enters UPI PIN
6. **Completion** → Payment is processed

### UPI Intent Response

After the customer clicks the payment link, PayU's page will display UPI app options. Behind the scenes, PayU uses the `intentURIData` to invoke the UPI app:

**Intent URI Format:**

```
upi://pay?pa=merchant.payu@indus&pn=MERCHANT_NAME&tr=30478359672&tid=PPPL30478359672&am=500.00&cu=INR&tn=UPIIntent
```

**Parameters:**

- `pa` — Payee VPA (merchant UPI ID)
- `pn` — Payee name
- `tr` — Transaction reference (PayU payment ID)
- `tid` — Transaction ID
- `am` — Amount
- `cu` — Currency
- `tn` — Transaction note

***

## Webhook Notification

After payment completion, PayU sends a webhook:

```json
{
  "txnid": "UPIPL28471834809170985",
  "mihpayid": "30478359672",
  "status": "success",
  "unmappedstatus": "captured",
  "mode": "UPI",
  "bankcode": "INTENT",
  "amount": "500.00",
  "phone": "919876543210",
  "udf5": "upi_intent_link",
  "hash": "WEBHOOK_HASH"
}
```

**Key Indicators for UPI Intent:**

- `mode`: "UPI"
- `bankcode`: "INTENT"

***

## Verify Payment

```python
import hashlib

def verify_upi_payment(txnid):
    url = "https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment"
    
    merchant_id = 8739528
    hash_string = f"{merchant_id}|verify_payment|{txnid}|YOUR_CLIENT_SECRET"
    verify_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
    
    payload = {
        "txnid": txnid,
        "merchant_id": merchant_id,
        "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
        "hash": verify_hash
    }
    
    response = requests.post(url, headers={"Authorization": "Bearer TOKEN"}, json=payload)
    return response.json()
```

***

## Error Handling

| Error                                      | Cause                   | Resolution                       |
| ------------------------------------------ | ----------------------- | -------------------------------- |
| s2s_client_ip or s2s_device_info mandatory | Missing S2S fields      | Include both fields in request   |
| Invalid hash                               | Hash validation failed  | Verify hash formula              |
| No UPI app installed                       | Customer has no UPI app | Suggest alternate payment method |

***

## Best Practices

✅ **Capture Device Info** — Get real device user-agent from HTTP headers<br />✅ **Capture Client IP** — Extract from `X-Forwarded-For` or request IP<br />✅ **Mobile-First** — UPI Intent works best on mobile devices<br />✅ **Fallback Option** — Provide QR code for desktop users<br />✅ **Track Clicks** — Monitor link opens to measure engagement

***

## Next Steps

- [Payment Links for UPI TPV](doc:payment-links-upi-tpv) — TPV validation for payment links
- [Partner Webhook API](ref:partner-webhook-api) — Webhook verification
- [Verify Payment API](ref:verify-payment-partner-api) — Payment verification

<Success>
**UPI Intent Payment Links Ready!** Your customers can now pay directly from their UPI apps with just one click.
</Success>
