---
title: Pluxee Card
excerpt: Collect a Pluxee card payment with pg MC and bankcode SODEXO
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Pluxee Card — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Accept Pluxee (Sodexo) cards on PayU Merchant Hosted Checkout with pg=MC and bankcode=SODEXO. Check balance, save a source ID, and verify the payment.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">
  Do not store the full Pluxee card number, expiry, or CVV, even if the customer agrees. PCI-DSS applies to the card number. Check the balance with the Fetch Balance API before you call `_payment`.
</Callout>

# Pluxee Card

Pluxee (formerly Sodexo) uses the same `_payment` API as other Merchant Hosted methods. `pg=MC` and `bankcode=SODEXO`.

## Check the Card Balance

The Pluxee page recommends the Fetch Balance API (`check_balance`) before `_payment`, and showing the balance on your checkout.

[Fetch Balance API](https://docs.payu.in/reference/fetch-balance-api-sodexo)

<!-- DOCUMENTATION GAP: The check_balance request and response are not in this folder. -->

For a card already saved with PayU, the `_payment` request can set `is_check_balance=1` together with `source_id`. The page says to use that flag only for saved cards.

## Post the Payment Request

The customer selects Pluxee on your site and enters the card details.

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/_payment` |
| Production | `POST https://secure.payu.in/_payment` |

### Mandatory Parameters

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
| key | String | Merchant key. | JP\*\*\*g |
| txnid | String | Transaction ID you generate. | bvRCCBO4YiGGHE |
| amount | String | Payment amount. | 10.00 |
| productinfo | String | Short product description. | iPhone |
| firstname | String | Customer first name. | Ashish |
| email | String | Customer email. | test@gmail.com |
| phone | String | Customer phone. | 9876543210 |
| pg | String | `MC` for Pluxee. | MC |
| bankcode | String | `SODEXO`. | SODEXO |
| ccnum | String | 16-digit Pluxee card number. Validate with the LUHN algorithm. Handle it under PCI-DSS. | 5123456789012346 |
| ccname | String | Name on card. | Ashish Kumar |
| ccvv | String | Card CVV. The source also mentions a 4-digit code for AMEX. | 123 |
| ccexpmon | String | Expiry month, `MM`. Prefix 0 for months 1–9. | 10 |
| ccexpyr | String | Expiry year, four digits. | 2021 |
| surl | String | Success URL. | https://example.com/success |
| furl | String | Failure URL. | https://example.com/failure |
| hash | String | `SHA-512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|Salt)` | calculated_hash_value |

### Optional Parameters

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
| save_sodexo_card | String | `0` do not save. `1` save the card with the payment. | 1 |
| source_id | String | Pays with a Pluxee card saved earlier. Card details are not sent. | source_12345 |
| is_check_balance | String | `0` do not check. `1` check. Only with `source_id` for a saved card. | 1 |
| address1 | String | Billing address line 1. The source marks this mandatory for cross-border payments. | 123 Main St |
| address2 | String | Billing address line 2. | Apt 4B |
| city | String | Billing city. Mandatory for cross-border payments in the source table. | Mumbai |
| state | String | Billing state. Mandatory for cross-border payments in the source table. | Maharashtra |
| country | String | Billing country. Mandatory for cross-border payments in the source table. | India |
| zipcode | String | Billing postal code. Character limit 20. Mandatory for cardless EMI and for cross-border payments in the source table. | 400001 |
| udf1 | String | User-defined field. For cross-border payments the source says this must include the buyer's PAN when the AD bank requests it. | ABCDE1234F |
| udf2 | String | User-defined field. | custom_data_2 |
| udf3 | String | User-defined field. For cross-border payments the source says this is the buyer's date of birth in `DD-MM-YYYY` when the AD bank requests it. | 15-01-1990 |
| udf4 | String | User-defined field. For cross-border payments the source says payment aggregators must send the end-merchant legal entity name. | Merchant Corp Ltd |
| udf5 | String | User-defined field. For cross-border payments the source says this is the invoice ID or invoice number. | INV_2024_001 |

<Accordion title="Understanding Hashing and sample code" icon="fa-shield-halved">
  <HashingRequestParameters />
  <HashingSample />
</Accordion>

<Accordion title="cURL" icon="fa-code">

```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&txnid=bvRCCBO4YiGGHE&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=MC&bankcode=SODEXO&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=637513XXXXXX9318&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=Ashish&hash=ad36b3253313753088c662053b043fbe6d7a10112b31fbf20c4b0945b6a70c3a12239c5330ec2d0a0956bcd28a689f08c94fbb9cc2c5e06bb08dc81968672f64"
```

</Accordion>

## Save the Card and Pay Again

If the customer agrees to save the card on your checkout:

- Post `save_sodexo_card=1` on `_payment`.
- After a successful payment, Sodexo shares the sourceId with PayU, and PayU returns it to you in `field3`.

You can charge that saved card later by posting `source_id`. Do not send the card number, expiry, or CVV on that request. You may post `is_check_balance=1` with `source_id`.

<!-- DOCUMENTATION GAP: This folder has no sample request that contains only source_id and omits the card fields. -->

## Handle the Callback

PayU sets the status from the bank response. Verify the hash before you accept or reject the order. The response field list is on [Collect Payment API - Merchant Hosted Checkout](https://docs.payu.in/reference/_payment_merchant_hosted).

<Accordion title="Verify the response hash" icon="fa-shield-halved">
  <ReverseHashing />
</Accordion>

The parsed success sample includes `mode=MC`, `status=success`, `unmappedstatus=captured`, `PG_TYPE=MC-PG`, `bankcode=SODEXO`, `error=E000`, `error_Message=No Error`, `name_on_card`, and a masked `cardnum`.

## Verify the Payment Server-Side

<Accordion title="Verify Payment API" icon="fa-circle-check">
  <Verify_Payment_Tabs />
</Accordion>

## Test Credentials

<!-- DOCUMENTATION GAP: The Pluxee sample uses a masked card number 637513XXXXXX9318. No test card, OTP, or test balance is documented in this folder. -->

## Related Resources

<Cards columns={2}>
  <Card title="Fetch Balance API" icon="fa-wallet" href="https://docs.payu.in/reference/fetch-balance-api-sodexo">
    `check_balance` before you start the payment.
  </Card>
  <Card title="Collect Payment API" icon="fa-rectangle-api" href="https://docs.payu.in/reference/_payment_merchant_hosted">
    Response fields for `_payment`.
  </Card>
</Cards>
