---
title: Pluxee Card
excerpt: Collect a Pluxee card payment with pg=MC and bankcode=SODEXO
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Pluxee Card — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Merchant Hosted Pluxee (Sodexo): check the card balance, post pg=MC and bankcode=SODEXO, and optionally save the card with source_id.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">
  Do not store the full card number, expiry, or CVV, even if the customer agrees to save the card. The source recommends the Fetch Balance API (`check_balance`) before `_payment`. Pluxee uses `pg=MC` and `bankcode=SODEXO`.
</Callout>

# Pluxee Card

Pluxee was formerly Sodexo. This page posts a Pluxee card on Merchant Hosted Checkout with the `_payment` API.

## Check Card Balance

The source says to call the Fetch Balance API (`check_balance`) and show the balance on your checkout before you collect the payment. `is_check_balance` on `_payment` is a separate flag, and the page says to use it only with a saved card and `source_id`.

<!-- DOCUMENTATION GAP: The check_balance request and response are not in this folder. The page links https://docs.payu.in/reference/fetch-balance-api-sodexo -->

## Post the Payment Request

The customer selects Pluxee on your site and enters the card details.

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/_payment` |
| Production | `POST https://secure.payu.in/_payment` |

### Mandatory Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| key | Merchant key | JP\*\*\*g |
| txnid | Merchant transaction reference | bvRCCBO4YiGGHE |
| amount | Payment amount | 10.00 |
| productinfo | Product description | iPhone |
| firstname | Customer first name | Ashish |
| email | Customer email | test@gmail.com |
| phone | Customer phone | 9876543210 |
| pg | MC for Pluxee | MC |
| bankcode | SODEXO | SODEXO |
| ccnum | 16-digit Sodexo card number. Validate with LUHN | 5123456789012346 |
| ccname | Name on card | Ashish Kumar |
| ccvv | CVV | 123 |
| ccexpmon | Expiry month, MM | 10 |
| ccexpyr | Expiry year, four digits | 2021 |
| surl | Success URL | https://example.com/success |
| furl | Failure URL | https://example.com/failure |
| hash | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|Salt)` | |

### Optional Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| save_sodexo_card | 0 = do not save. 1 = save. Used when the customer consents to save the card | 1 |
| source_id | Pay a card saved earlier. Card details are not sent | source_12345 |
| is_check_balance | 0 = do not check. 1 = check. Only with `source_id` for a saved card | 1 |
| address1 | Billing address line 1. Mandatory for cross-border payments in this table | 123 Main St |
| address2 | Billing address line 2 | Apt 4B |
| city | Billing city. Mandatory for cross-border in this table | Mumbai |
| state | Billing state. Mandatory for cross-border in this table | Maharashtra |
| country | Billing country. Mandatory for cross-border in this table | India |
| zipcode | Billing zip. Character limit 20. Mandatory for cross-border in this table | 400001 |
| udf1 | For cross-border, the table says this must include the buyer's PAN when the AD bank requests it | ABCDE1234F |
| udf2 | User-defined field | custom_data_2 |
| udf3 | For cross-border, date of birth DD-MM-YYYY when the AD bank requests it | 15-01-1990 |
| udf4 | For cross-border, the table says payment aggregators must send the end-merchant legal name | Merchant Corp Ltd |
| udf5 | For cross-border, invoice id or invoice number | INV_2024_001 |

When `save_sodexo_card=1` and the payment succeeds, the source says Sodexo shares a sourceId with PayU and PayU returns it in `field3`. A later payment can send that value in `source_id` and omit the card fields.

The Pluxee page has no separate HTML form. The sample is cURL.

<Accordion title="cURL" icon="fa-code">
  ```bash
  curl -X POST "https://test.payu.in/_payment" \
    -H "accept: application/json" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=JP***g&txnid=bvRCCBO4YiGGHE&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=MC&bankcode=SODEXO&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=637513XXXXXX9318&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=Ashish&hash=ad36b3253313753088c662053b043fbe6d7a10112b31fbf20c4b0945b6a70c3a12239c5330ec2d0a0956bcd28a689f08c94fbb9cc2c5e06bb08dc81968672f64"
  ```
</Accordion>

## Handle the Callback

<Accordion title="Verify the response hash" icon="fa-shield-halved">
  <ReverseHashing />

  Sample response fields: `mihpayid`, `mode=MC`, `status=success`, `unmappedstatus=captured`, `amount=10.00`, `PG_TYPE=MC-PG`, `bank_ref_num`, `bankcode=SODEXO`, `error=E000`, `error_Message=No Error`, `name_on_card=Ashish`, `cardnum=637513XXXXXX3104`.
</Accordion>

## Verify the Payment Server-Side

<Accordion title="Verify Payment API" icon="fa-circle-check">
  <Verify_Payment_Tabs />
</Accordion>

## Test Credentials

<!-- DOCUMENTATION GAP: The Pluxee sample uses a masked card number 637513XXXXXX9318. This folder does not list a Pluxee test card, OTP, or balance fixture. -->

## Related Resources

<Cards columns={2}>
  <Card title="Fetch Balance API" icon="fa-wallet" href="https://docs.payu.in/reference/fetch-balance-api-sodexo">
    check_balance, recommended before _payment. The request is not copied here.
  </Card>
  <Card title="Collect Payment API" icon="fa-rectangle-api" href="https://docs.payu.in/reference/_payment_merchant_hosted">
    Response fields the Pluxee page tells you to read.
  </Card>
</Cards>
