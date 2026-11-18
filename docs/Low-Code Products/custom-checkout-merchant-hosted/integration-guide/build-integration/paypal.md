---
title: PayPal
excerpt: Post a PayPal payment with pg PAYPAL and bankcode PAYPAL
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: PayPal — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Accept PayPal on Merchant Hosted Checkout. Activate it in the Dashboard, post pg PAYPAL and bankcode PAYPAL, and settle to your PayPal wallet in INR. Read on.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">
  Activate PayPal from the PayU Dashboard before you integrate. The overview says this for both PayU Hosted Checkout and Merchant Hosted Checkout.
</Callout>

# PayPal

PayPal on this integration is for international payments. The customer can convert from INR (or another currency) into their chosen currency. The source says the money is transferred to your PayPal wallet and settlement is in INR. Transaction rates are determined by PayPal. The source also says settlement is T+1 and that there are no extra charges from PayU beyond PayPal's rates.

<!-- VALIDATION NEEDED: The PayPal page requires bankcode PAYPAL together with pg PAYPAL. The overview table says bankcode is N/A and that no bankcode is required. The samples on the PayPal page post both fields as PAYPAL. This page follows those samples. -->

## Customer Journey

The PayPal page describes this journey:

1. The customer is redirected to the PayU payment page.
2. The customer selects Wallets.
3. The customer selects PayPal.
4. The customer selects a currency and clicks PayPal. PayU sends you the success or failure response after verification.

<!-- VALIDATION NEEDED: Those steps describe a PayU payment page and a Wallets list. That is the PayU Hosted journey. The request on the same page is a merchant form POST to _payment with pg and bankcode set to PAYPAL. The screenshots in the source are the PayU wallets list and the PayPal page. Confirm which journey applies to Merchant Hosted. -->

## Post the Payment Request

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/_payment` |
| Production | `POST https://secure.payu.in/_payment` |

### Mandatory Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| `key` | Merchant key | `8488225` |
| `txnid` | Your transaction id. Must be unique | `fd3e847h2` |
| `amount` | Amount | `10` |
| `productinfo` | Product description | `T-shirt` |
| `firstname` | Customer first name | `Ankit` |
| `email` | Customer email | `test@gmail.com` |
| `phone` | Customer phone | `9876543210` |
| `pg` | `PAYPAL`. The source text says "For Wallet payment, PAYPAL must be specified." | `PAYPAL` |
| `bankcode` | `PAYPAL` | `PAYPAL` |
| `surl` | Success URL | `https://apiplayground-response.herokuapp.com/` |
| `furl` | Failure URL | `https://apiplayground-response.herokuapp.com/` |
| `hash` | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|Salt)` | Generated on your server |

### Optional Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| `lastname` | Customer last name | `Kumar` |
| `address1` | Billing line 1 | `123 Main St` |
| `address2` | Billing line 2 | `Apt 4B` |
| `city` | Billing city | `Mumbai` |
| `state` | Billing state | `Maharashtra` |
| `country` | Billing country | `India` |
| `zipcode` | Postal code. The cell says it is mandatory for cardless EMI | `400001` |
| `udf1`–`udf5` | Your own values | `custom_data_1` |

<Accordion title="cURL" icon="fa-code">

```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=J****g&txnid=aI1UM19ONxLgPz&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=PAYPAL&bankcode=PAYPAL&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=GENERATED_HASH"
```

</Accordion>

<Accordion title="Form POST" icon="fa-code">
  <!-- DOCUMENTATION GAP: The PayPal page has no HTML form. The cURL above is the sample. -->
</Accordion>

## Handle the Callback

The success sample has `mode=PAYPAL`, `status=success`, `PG_TYPE=PAYPAL-PG`, `bankcode=PAYPAL`, `field4=0.12`, `field5=USD`, `error=E000`, and `error_Message=No Error`.

<!-- DOCUMENTATION GAP: field4 and field5 are in the sample and are not defined on the PayPal page. -->

<!-- DOCUMENTATION GAP: The PayPal page does not include the reverse-hash formula or the ReverseHashing block. The formula written on the UPI Collect page is sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key). Confirm it applies to PayPal before relying on it here. -->

## Refunds

The source says the PayPal account must have enough funds before a refund. Refund from the PayU Dashboard or the Refund Transaction API.

## Verify the Payment Server-Side

<Accordion title="Verify Payment API" icon="fa-circle-check">
  <Verify_Payment_Tabs />
</Accordion>

## Test Credentials

<!-- DOCUMENTATION GAP: No PayPal sandbox buyer account, password, or test amount is in this folder. -->

## Related Resources

<Cards columns={2}>
  <Card title="Collect Payment API — Wallets" icon="fa-rectangle-api" href="https://docs.payu.in/reference/_payment_merchant_hosted_wallets">
    The reference the PayPal page cites for Try It.
  </Card>
  <Card title="Refund Transaction API" icon="fa-rotate-left" href="https://docs.payu.in/reference/refund_transaction_api">
    Linked from the PayPal refund note. Command on the APIs page is cancel_refund_transaction.
  </Card>
</Cards>
