---
title: Pluxee Card
excerpt: Collect a Pluxee card with pg MC and bankcode SODEXO
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Pluxee Card — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Accept a Pluxee (Sodexo) card on your checkout. Post pg MC and bankcode
    SODEXO. Check the balance first. Do not store the card number, expiry, or CVV.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">
  The source says you are not allowed to store the complete Pluxee card number, expiry, or CVV, even if the customer allows you to save the card.
</Callout>

# Pluxee Card

Pluxee (formerly Sodexo) uses `pg=MC` and `bankcode=SODEXO` on `_payment`. The source recommends calling the Fetch Balance API (`check_balance`) before you start the payment, and showing the balance on your checkout.

## Check the Card Balance

<!-- DOCUMENTATION GAP: The check_balance request and response are not in this folder. The source links the Fetch Balance API. -->

The Fetch Balance API reference linked from the page is [Fetch Balance API](https://docs.payu.in/reference/fetch-balance-api-sodexo).

`is_check_balance` on `_payment` is optional. `0` means do not check. `1` means check. The source says to use it only for a saved card, together with `source_id`.

## Post the Payment Request

The customer selects Pluxee on your site and enters the card details.

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/_payment` |
| Production | `POST https://secure.payu.in/_payment` |

### Mandatory Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| `key` | Merchant key | `JP***g` |
| `txnid` | Your transaction id | `bvRCCBO4YiGGHE` |
| `amount` | Amount | `10.00` |
| `productinfo` | Product description | `iPhone` |
| `firstname` | Customer first name | `Ashish` |
| `email` | Customer email | `test@gmail.com` |
| `phone` | Customer phone | `9876543210` |
| `pg` | `MC` for Pluxee | `MC` |
| `bankcode` | `SODEXO` | `SODEXO` |
| `ccnum` | 16-digit Sodexo card number. Validate with Luhn | `5123456789012346` |
| `ccname` | Name on card | `Ashish Kumar` |
| `ccvv` | CVV. The source also mentions a 4-digit code for AMEX in this cell | `123` |
| `ccexpmon` | Expiry month, `MM` | `10` |
| `ccexpyr` | Expiry year, four digits | `2021` |
| `surl` | Success URL | `https://example.com/success` |
| `furl` | Failure URL | `https://example.com/failure` |
| `hash` | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|Salt)` | Generated on your server |

The cURL sample uses a masked card number, `637513XXXXXX9318`, not the example in the table.

### Optional Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| `save_sodexo_card` | `0` do not save. `1` save. After a successful save, Sodexo shares a sourceId with PayU and PayU returns it in `field3` | `1` |
| `source_id` | Pay again with a card you saved earlier. Card details are not sent | `source_12345` |
| `is_check_balance` | `0` or `1`. Only with `source_id` for a saved card | `1` |
| `address1`, `address2`, `city`, `state`, `country`, `zipcode` | Billing fields. The source marks several of these mandatory for cross-border payments | |
| `udf1` | The Pluxee table says that for cross-border, if the AD bank asks, this must be the buyer's PAN | `ABCDE1234F` |
| `udf2` | Your own value | `custom_data_2` |
| `udf3` | The Pluxee table says that for cross-border this may be the buyer's date of birth, `DD-MM-YYYY` | `15-01-1990` |
| `udf4` | The Pluxee table says that for cross-border payment aggregators this is the end-merchant legal name | `Merchant Corp Ltd` |
| `udf5` | The Pluxee table says that for cross-border this is the invoice id | `INV_2024_001` |

<!-- VALIDATION NEEDED: udf1–udf5 and several address fields on the Pluxee page are described with cross-border rules (PAN, date of birth, end-merchant name, invoice id). This page is the Pluxee integration. Confirm whether those cross-border meanings apply when the payment is a domestic Pluxee card. -->

<Accordion title="cURL" icon="fa-code">

```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&txnid=bvRCCBO4YiGGHE&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=MC&bankcode=SODEXO&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=637513XXXXXX9318&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=Ashish&hash=GENERATED_HASH"
```

</Accordion>

<Accordion title="Form POST" icon="fa-code">
  <!-- DOCUMENTATION GAP: The Pluxee page has a cURL sample and no HTML form. Do not invent a form. The field names are the parameters above. -->
</Accordion>

## Handle the Callback

<ReverseHashing />

The success sample has `mode=MC`, `status=success`, `unmappedstatus=captured`, `PG_TYPE=MC-PG`, `bankcode=SODEXO`, `error=E000`, and `error_Message=No Error`. `cardnum` is masked. `name_on_card` is in the sample.

## Verify the Payment Server-Side

<Accordion title="Verify Payment API" icon="fa-circle-check">
  <Verify_Payment_Tabs />
</Accordion>

## Test Credentials

<!-- DOCUMENTATION GAP: The Pluxee cURL uses a masked number (637513XXXXXX9318). The parameter example 5123456789012346 is not labeled as a Pluxee sandbox card. The test page has no Pluxee row. -->

## Related Resources

<Cards columns={2}>
  <Card title="Fetch Balance API" icon="fa-wallet" href="https://docs.payu.in/reference/fetch-balance-api-sodexo">
    check_balance, linked from the Pluxee page.
  </Card>
  <Card title="Collect Payment API" icon="fa-rectangle-api" href="https://docs.payu.in/reference/_payment_merchant_hosted">
    The reference the Pluxee page cites for the response body.
  </Card>
</Cards>
