---
title: UPI S2S Integration API - Partner Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
In order to initiate payments for partners, WhatsApp should use the **access token** (Bearer) instead of key/salt. Follow the steps below to integrate the **server-to-server UPI Intent** flow.

## Steps

1. **Initiate payment request**
2. **Invoke UPI Intent on customer's device**
3. **Verify payment**
4. **Receive Server-to-Server callback from PayU**

---

## Step 1: Initiate payment request

### Environment


### Request headers

Parameter | Description | Example
---|---|---
Content-Type | **mandatory** — The content type of the request | `application/json`
Authorization | **mandatory** — Bearer token for authentication. Replace `<ACCESS_TOKEN>` with your token | `Bearer <ACCESS_TOKEN>`

### Request parameters

> 📘 **Extra params for Partner integration**  
> The following params are the extra (optional) parameters compared to the regular **_payment** API, but with a different endpoint: `partner_udf_3`, `partner_udf_4`, `shipping_firstname`, `shipping_lastname`, `shipping_address1`, `shipping_address2`, `shipping_city`, `shipping_state`, `shipping_country`, `shipping_zipcode`, `shipping_phone`.

Parameter | Description | Example
---|---|---
merchant_id | **mandatory** — Unique Merchant ID provided by PayU | `8488225`
txnid | **mandatory** — Transaction/Order ID unique at merchant end | `fd3e847h2`
amount | **mandatory** — Payment amount (float) | `10`
productinfo | **mandatory** — Brief product description | `T-shirt`
firstname | **mandatory** — Customer first name | `Ankit`
email | **mandatory** — Customer email | `test@gmail.com`
phone | **mandatory** — GPay registered phone number (used to map VPA and initiate collect) | `9876543210`
txn_s2s_flow | **mandatory** — Indicates S2S flow; pass value `4` | `4`
hash | **mandatory** — SHA512 hash to prevent tampering. Use pipe (`|`) between params:  
`sha512(merchant_id|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|CLIENT_SECRET)` | —
s2s_client_ip | **mandatory** — Source IP of the user | —
s2s_device_info | **mandatory** — User agent/device info | —
reseller_id | **mandatory** — Unique Partner Identifier provided by PayU | `83fe-eb64-021844d8-9397-26535b1bf0c2`
udf5 | **mandatory** — For WhatsApp integration, pass `whatsapp` | `whatsapp`
address1 | optional — Billing address line 1 | —
address2 | optional — Billing address line 2 | —
city | optional — Billing city | —
state | optional — Billing state | —
country | optional — Billing country | —
zipcode | optional — Billing ZIP (mandatory for **cardless EMI**) | —
partner_udf_3 | optional — Partner custom field | —
partner_udf_4 | optional — Partner custom field | —
shipping_firstname | optional — Shipping first name | —
shipping_lastname | optional — Shipping last name | —
shipping_address1 | optional — Shipping address line 1 | —
shipping_address2 | optional — Shipping address line 2 | —
shipping_city | optional — Shipping city | —
shipping_state | optional — Shipping state | —
shipping_country | optional — Shipping country | —
shipping_zipcode | optional — Shipping ZIP | —
shipping_phone | optional — Shipping phone | —
drop_category | optional — Hide one/multiple payment options | —
enforce_paymethod | optional — Enforce specific payment modes/schemes/banks | —
user_token | optional — Uniquely identify a user for a merchant | —
offer_key | optional — Keys to filter offers | —
offer_auto_apply | optional — Auto-apply offer flag | —
additional_charges | optional — Additional amount to be added by PayU | —

### Sample request

```bash
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/payments' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer <ACCESS_TOKEN>' \
  --data-raw '{
    "txnid": "nY3tkz3vciHFGTjblyFeycL2Zn1m",
    "amount": 1090.33,
    "productinfo": "whatsapp",
    "firstname": "Manikanta",
    "reseller_id": "83fe-eb64-021844d8-9397-26535b1bf0c2",
    "merchant_id": 8238480,
    "phone": 7036722360,
    "hash": "<HASH>",
    "lastname": "CHeruku",
    "email": "manik.cr24@gmail.com",
    "curl": "https://www.google.com",
    "furl": "https://www.google.com",
    "surl": "https://www.youtube.com",
    "txn_s2s_flow": "4",
    "s2s_device_info": "ewew",
    "s2s_client_ip": "ewew"
  }'
```

### Sample response

```json
{
  "metaData": {
    "message": null,
    "referenceId": "024d9afbdbf85bd35b25649ccf983e16ee3d4646c2cdcffada88bd2df371fd43",
    "txnId": "nY3tkz3vciHFGTjblyFeycL2Zn1m",
    "txnStatus": "pending",
    "unmappedStatus": "pending"
  },
  "result": {
    "paymentId": 403993715529028543,
    "merchantName": "Merchant",
    "amount": "1090.33",
    "intentURIData": "pa=&pn=&tr=403993715529028543&tid=PPPL403993715529028543290523133325&am=1090.33&cu=INR&tn=UPI Transaction for PPPL403993715529028543290523133325",
    "acsTemplate": "<html>...form + script auto-submit...</html>",
    "otpPostUrl": "https://test.payu.in/ResponseHandler.php"
  }
}
```

---

## Step 2: Invoke UPI Intent on Customer's Device

Open the UPI Intent as per **NPCI Guidelines**. Fire the URL using an Intent or a hyperlink to open the app tray on the user's device.

**Format (per NPCI guidance):**

```text
upi://pay?pa=<payee_vpa>&pn=<payee_name>&tr=<txn_ref>&tid=<txn_id>&am=<amount>&cu=INR&tn=<note>
```

> Replace placeholders using values received in `intentURIData`.

---

## Step 3: Verify Payment API

Check the UPI transaction status using the **Verify Payment API** (`check_upi_txn_status`).

### Environment


### Request headers

Parameter | Value
---|---
Content-Type | `application/json`
Authorization | `Bearer <ACCESS_TOKEN>`

### Request parameters

Parameter | Description | Example
---|---|---
txnid | **mandatory** — Your transaction/order ID | `100123`
merchant_id | **mandatory** — Merchant ID provided by PayU | `8238480`
hash | **mandatory** — `sha512(merchant_id|command|txnid|client_secret)` where `command=verify_payment` | —
reseller_id | **mandatory** — Unique Partner Identifier | `83fe-eb64-021844d8-9397-26535b1bf0c3`

### Sample request

```bash
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment' \
  --header 'Authorization: Bearer <ACCESS_TOKEN>' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "txnid": "nY3tkz3vciHFGTjblyFeycL2Zn2c",
    "merchant_id": "8238480",
    "reseller_id": "83fe-eb64-021844d8-9397-26535b1bf0c2",
    "hash": "<HASH>"
  }'
```

### Response parameters

Parameter | Description
---|---
mihpayid | Unique PayU reference for the transaction.
request_id | Request ID posted during transaction.
bankrefnum | Bank reference number for successful transactions.
amt | Net amount debited.
transaction_amount | Original amount sent by merchant.
productinfo | Product info as sent in transaction request.
firstname | First name as sent in transaction request.
bankcode | Code indicating payment option used.
udf1..udf5 | UDFs as sent by merchant.
field2, field3 | Bank auth code.
field9 | Failure reason if any.
error_code | Error code.
net_amount_debit | Net amount debited (`transaction_fee = actual_discount + additional_charges`).
added_on | Transaction timestamp.
payment_source | Payment source (PayU).
card_type | Card type (if cards used).
error_Message | Error message if any.
disc | Discount amount (for Cashback offers this is always `0`).
mode | Mode of payment.
PG_TYPE | Payment gateway used (e.g., `UPI-PG`).
card_no | Masked card number (if card).
name_on_card | Name on card (if card).
status | Status of the transaction.
unmappedstatus | Internal PayU status (intermediate states).
Merchant_UTR | Merchant Unique Transaction Reference.
Settled_At | Timestamp of card settlement (if applicable).

### Sample response

```json
{
  "msg": "1 out of 1 Transactions Fetched Successfully",
  "transaction_details": {
    "wtsapp_txn_id5": {
      "mihpayid": "403993715529051451",
      "amt": "2.00",
      "transaction_amount": "2.00",
      "txnid": "wtsapp_txn_id5",
      "productinfo": "WA productinfo",
      "firstname": "WAfirstname",
      "bankcode": "INTENT",
      "net_amount_debit": "0.00",
      "mode": "UPI",
      "PG_TYPE": "UPI-PG",
      "status": "pending",
      "unmappedstatus": "in progress"
    }
  },
  "status": 1.0
}
```

---

## Step 4: PayU sends Server-to-Server callback response

PayU can send a server-to-server callback when the transaction status updates. The response is **key/value pairs** separated by `&`. If any parameter is unused, it is sent as an empty string.

### Sample callback payload

```text
mihpayid=403993715523615328&mode=CC&status=success&unmappedstatus=captured&key=JPM7Fg&txnid=50QJq6lBJBmx14&amount=10.00&cardCategory=domestic&discount=0.00&net_amount_debit=10&addedon=2021-07-28 15:11:37&productinfo=iPhone&firstname=PayU User&email=test@gmail.com&phone=9876543210&hash=<HASH>&PG_TYPE=CC-PG&bank_ref_num=7f0d5ada-59bb-41d7-9e41-20a6af2406c9&bankcode=CC
```

---

## Failed responses

Code | Reason | Response
---|---|---
401 | Invalid token | `{ "message": "Invalid Auth token" }`
403 | Invalid hash | `{ "message": "Invalid Hash" }`
400 | Missing reseller_id | `{ "errors": [ "reseller_id is mandatory." ] }`
400 | Missing amount | `{ "errors": [ "amount is mandatory param" ] }`
400 | Missing merchant_id | `{ "errors": [ "merchant_id is mandatory param" ] }`
400 | Missing hash | `{ "errors": [ "hash is mandatory param" ] }`
400 | Missing product_info | `{ "errors": [ "product_info is mandatory param" ] }`

---

## Notes & Best Practices

- Use **HTTPS** endpoints and valid **Bearer tokens** for authentication.
- Ensure **hash** values are calculated exactly as specified (parameter order and separator matter).
- For UPI Intent, follow **NPCI deep-link format** and populate fields from `intentURIData`.
- Prefer **JSON** content-type and avoid control characters/extra backslashes in Markdown if this page is rendered via MDX.

