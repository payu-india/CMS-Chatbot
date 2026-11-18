---
title: PayPal
excerpt: Collect a PayPal payment with pg=PAYPAL and bankcode=PAYPAL
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: PayPal — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Merchant Hosted PayPal: activate PayPal on the PayU Dashboard, post pg=PAYPAL and bankcode=PAYPAL to _payment, then verify the callback.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">
  Activate PayPal from the PayU Dashboard before you integrate. Refunds need sufficient funds in the PayPal account. The source says you can refund from the PayU Dashboard or the Refund Transaction API.
</Callout>

# PayPal

PayPal on the integration page uses `pg=PAYPAL` and `bankcode=PAYPAL`. Settlements are processed in INR. The page says customers can use PayPal currency conversion.

<!-- VALIDATION NEEDED: The legacy Merchant Hosted overview table says PayPal bankcode is N/A. This page follows the PayPal integration page, which says bankcode=PAYPAL, and flags the conflict. -->

## Customer Journey

The PayPal page describes this journey:

1. The customer is redirected to the PayU payment page.
2. The customer selects Wallets.
3. The customer selects PayPal.
4. The customer selects a currency and clicks PayPal. PayU sends the success or failure response after verification.

<!-- VALIDATION NEEDED: That journey describes a PayU-hosted wallet list. It does not describe a merchant-hosted form post. The request on the same page is a form post to _payment with pg=PAYPAL. -->

## Post the Payment Request

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/_payment` |
| Production | `POST https://secure.payu.in/_payment` |

### Mandatory Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| key | Merchant key | 8488225 |
| txnid | Unique order reference from the merchant | fd3e847h2 |
| amount | Payment amount | 10 |
| productinfo | Product description | T-shirt |
| firstname | Customer first name | Ankit |
| email | Customer email | test@gmail.com |
| phone | Customer phone | 9876543210 |
| pg | PAYPAL | PAYPAL |
| bankcode | PAYPAL | PAYPAL |
| surl | Success URL | https://apiplayground-response.herokuapp.com/ |
| furl | Failure URL | https://apiplayground-response.herokuapp.com/ |
| hash | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|Salt)` | |

### Optional Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| lastname | Customer last name | Kumar |
| address1 | Billing address line 1 | 123 Main St |
| address2 | Billing address line 2 | Apt 4B |
| city | Billing city | Mumbai |
| state | Billing state | Maharashtra |
| country | Billing country | India |
| zipcode | Billing zip. The PayPal table says this is mandatory for cardless EMI | 400001 |
| udf1 | User-defined field | custom_data_1 |
| udf2 | User-defined field | custom_data_2 |
| udf3 | User-defined field | custom_data_3 |
| udf4 | User-defined field | custom_data_4 |
| udf5 | User-defined field | custom_data_5 |

The PayPal page has no HTML form sample.

<Accordion title="cURL" icon="fa-code">
  ```bash
  curl -X POST "https://test.payu.in/_payment" \
    -H "accept: application/json" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=J****g&txnid=aI1UM19ONxLgPz&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=PAYPAL&bankcode=PAYPAL&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
  ```
</Accordion>

## Handle the Callback

<!-- DOCUMENTATION GAP: The PayPal page does not print the reverse-hash formula. The formula used on UPI Collect and in the ReverseHashing block is sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key). -->

<Accordion title="Verify the response hash" icon="fa-shield-halved">
  <ReverseHashing />

  Sample response fields: `mihpayid`, `mode=PAYPAL`, `status=success`, `PG_TYPE=PAYPAL-PG`, `bank_ref_num`, `bankcode=PAYPAL`, `field4=0.12`, `field5=USD`, `error=E000`, `error_Message=No Error`.
</Accordion>

## Verify the Payment Server-Side

<Accordion title="Verify Payment API" icon="fa-circle-check">
  <Verify_Payment_Tabs />
</Accordion>

## Refunds

The PayPal page says the PayPal account needs sufficient funds before a refund. Refund from the [Refunds Dashboard](https://docs.payu.in/docs/refunds-dashboard) or the [Refund Transaction API](https://docs.payu.in/reference/refund_transaction_api). Refund request fields are not on the PayPal page.

## Test Credentials

<!-- DOCUMENTATION GAP: The PayPal integration page and the Merchant Hosted test page do not list a PayPal sandbox buyer, test amount, or test currency. -->

## Related Resources

<Cards columns={2}>
  <Card title="Collect Payment API — Wallets" icon="fa-rectangle-api" href="https://docs.payu.in/reference/_payment_merchant_hosted_wallets">
    The PayPal page points its Try-it link here.
  </Card>
  <Card title="Refund Transaction API" icon="fa-rotate-left" href="https://docs.payu.in/reference/refund_transaction_api">
    Refund command referenced from the PayPal page.
  </Card>
</Cards>
