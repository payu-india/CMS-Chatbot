---
title: PayPal
excerpt: Collect a PayPal payment from your checkout with pg PAYPAL and bankcode PAYPAL
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: PayPal — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Accept PayPal on PayU Merchant Hosted Checkout. Activate PayPal in the Dashboard, post pg=PAYPAL and bankcode=PAYPAL, and verify the payment. INR settlement.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">
  Activate PayPal from the PayU Dashboard before you integrate. The overview states this for both PayU Hosted Checkout and Merchant Hosted Checkout.
</Callout>

# PayPal

PayPal on Merchant Hosted Checkout is a form POST with `pg=PAYPAL` and `bankcode=PAYPAL`. Customers can use PayPal currency conversion. Payments are transferred to your PayPal wallet. Settlements are processed in INR.

The source lists these benefits: success rates up to 20% higher, T+1 settlement, access to the PayPal user base, transaction rates determined by PayPal, and currency conversion from INR to the customer's currency.

## Customer Journey

1. The customer is redirected to the PayU payment page.
2. The customer selects **Wallets**.
3. The customer selects **PayPal**.
4. The customer selects a currency and clicks **PayPal**. PayU sends the success or failure response after verification.

<!-- VALIDATION NEEDED: This journey is copied from the PayPal page and describes selection on the PayU payment page. The request on the same page is a merchant form POST to _payment with pg=PAYPAL and bankcode=PAYPAL. Confirm which journey applies to Merchant Hosted Checkout. -->

## Post the Payment Request

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/_payment` |
| Production | `POST https://secure.payu.in/_payment` |

### Mandatory Parameters

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
| key | String | Merchant key. | 8488225 |
| txnid | varchar | Order reference you generate. Must be unique for every new transaction. | fd3e847h2 |
| amount | float | Payment amount. | 10 |
| productinfo | varchar | Short product description. | T-shirt |
| firstname | varchar | Customer first name. | Ankit |
| email | varchar | Customer email. | test@gmail.com |
| phone | integer | Customer phone, as typed in the source table. | 9876543210 |
| pg | String | `PAYPAL`. | PAYPAL |
| bankcode | String | `PAYPAL`. | PAYPAL |
| surl | String | Success URL. | https://apiplayground-response.herokuapp.com/ |
| furl | String | Failure URL. | https://apiplayground-response.herokuapp.com/ |
| hash | String | `SHA-512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|Salt)` | calculated_hash_value |

### Optional Parameters

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
| lastname | String | Customer last name. | Kumar |
| address1 | String | Billing address line 1. | 123 Main St |
| address2 | String | Billing address line 2. | Apt 4B |
| city | String | Billing city. | Mumbai |
| state | String | Billing state. | Maharashtra |
| country | String | Billing country. | India |
| zipcode | String | Billing postal code. The source says this is mandatory for cardless EMI. | 400001 |
| udf1 | String | User-defined field. | custom_data_1 |
| udf2 | String | User-defined field. | custom_data_2 |
| udf3 | String | User-defined field. | custom_data_3 |
| udf4 | String | User-defined field. | custom_data_4 |
| udf5 | String | User-defined field. | custom_data_5 |

<Accordion title="Understanding Hashing and sample code" icon="fa-shield-halved">
  <HashingRequestParameters />
  <HashingSample />
</Accordion>

<Accordion title="cURL" icon="fa-code">

```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=J****g&txnid=aI1UM19ONxLgPz&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=PAYPAL&bankcode=PAYPAL&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
```

</Accordion>

## Handle the Callback

<Accordion title="Sample response" icon="fa-code">

```
Array
(
    [mihpayid] => 403993715527518775
    [mode] => PAYPAL
    [status] => success
    [PG_TYPE] => PAYPAL-PG
    [bank_ref_num] => 540898ed-72e7-40a8-a96e-f17de621cbb4
    [bankcode] => PAYPAL
    [field4] => 0.12
    [field5] => USD
    [error] => E000
    [error_Message] => No Error
)
```

</Accordion>

<Accordion title="Verify the response hash" icon="fa-shield-halved">
  <!-- DOCUMENTATION GAP: The PayPal page does not include a reverse-hash sample. The formula below is the one on the UPI Collect page and in the ReverseHashing block. Confirm it for PayPal responses. -->

  ```
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  <ReverseHashing />
</Accordion>

## Verify the Payment Server-Side

<Accordion title="Verify Payment API" icon="fa-circle-check">
  <Verify_Payment_Tabs />
</Accordion>

## Refunds

Keep enough funds in the PayPal account before you refund. Refunds can be started from the PayU Dashboard or the Refund Transaction API.

- [Refunds Dashboard](https://docs.payu.in/docs/refunds-dashboard)
- [Refund Transaction API](https://docs.payu.in/reference/refund_transaction_api) (`cancel_refund_transaction` on the API index)

## Test Credentials

<!-- DOCUMENTATION GAP: This folder does not list a PayPal sandbox buyer, test amount, or test account. -->

## Related Resources

<Cards columns={2}>
  <Card title="Refund Transaction API" icon="fa-rotate-left" href="https://docs.payu.in/reference/refund_transaction_api">
    Refund a PayPal payment when the PayPal wallet has funds.
  </Card>
  <Card title="Refunds Dashboard" icon="fa-gauge" href="https://docs.payu.in/docs/refunds-dashboard">
    Refund from the PayU Dashboard.
  </Card>
  <Card title="Collect Payments API" icon="fa-rectangle-api" href="https://docs.payu.in/reference/_payment_merchant_hosted_wallets">
    The PayPal page points the Try It flow here.
  </Card>
</Cards>
