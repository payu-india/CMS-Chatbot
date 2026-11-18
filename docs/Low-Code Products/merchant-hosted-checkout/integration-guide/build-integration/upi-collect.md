---
title: UPI Collect
excerpt: Validate a VPA and collect a UPI payment with pg=UPI and bankcode=UPI
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: UPI Collect — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Merchant Hosted UPI Collect: validate the VPA, post pg=UPI and bankcode=UPI with the VPA, then verify the reverse hash. MCC 6012 and 6211 only.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">
  As per NPCI guidelines in the source, UPI Collect is allowed only for MCC 6012 and 6211. Seamless form-post users must move to `txn_s2s_flow` (UPI Intent S2S). Android must implement Smart Intent. Web must use the Intent S2S deeplink to build a QR instead of UPI Collect. iOS may keep a deeplink and continue UPI Collect. Intent is not supported on the seamless form POST.
</Callout>

# UPI Collect

UPI Collect on this page uses `pg=UPI`, `bankcode=UPI`, and the customer's `vpa`. This is not UPI Intent (`bankcode=INTENT` in the legacy overview) and not UPI QR (`bankcode=UPIDBQR` in the legacy overview).

## Validate the UPI Handle

Validate the VPA with `command=validateVPA` before you post the payment. The sample posts to the test post-service URL.

<Accordion title="Request" icon="fa-code">
  ```bash
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=YOUR_MERCHANT_KEY" \
    -d "command=validateVPA" \
    -d "var1=customer@upi" \
    -d "hash=$HASH"
  ```

  Hash formula for post-service commands, from the legacy APIs page:

  ```
  sha512(key|command|var1|SALT)
  ```

  <!-- DOCUMENTATION GAP: The UPI Collect page does not include a full Validate VPA parameter table. It links https://docs.payu.in/reference/validate_vpa_api -->
</Accordion>

<Accordion title="Response" icon="fa-table">
  Success sample: `status` SUCCESS, `vpa` `9999999999@upi`, `isVPAValid` 1, `isAutoPayVPAValid` 1, `payerAccountName` ABC.

  Invalid VPA sample: `status` SUCCESS, `vpa` `abc@upi`, `isVPAValid` 0, `payerAccountName` NA.
</Accordion>

## Post the Payment Request

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/_payment` |
| Production | `POST https://secure.payu.in/_payment` |

### Mandatory Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| key | Merchant key | JPg\*\*\*r |
| txnid | Merchant transaction reference | ypl938459435 |
| amount | Payment amount | 10.00 |
| productinfo | Product description | iPhone |
| firstname | Customer first name | Ashish |
| email | Customer email | abc@payu.in |
| phone | Customer phone | 9988776655 |
| pg | Must be UPI | UPI |
| bankcode | UPI for this Collect flow | UPI |
| vpa | Customer VPA. The page points to UPI Handles for the bank part of the handle | test123@okhdfcbank |
| surl | Success URL. The description says success. The example URL on the legacy table is `https://example.com/failure` | https://example.com/success |
| furl | Failure URL. The description says failure. The example URL on the legacy table is `https://example.com/success` | https://example.com/failure |
| hash | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|Salt)` | |

<!-- VALIDATION NEEDED: UPI Collect descriptions of surl and furl match success and failure. The example URLs in that table are swapped. -->

### Optional Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| address1 | Billing address line 1. Source says this helps fraud detection and chargebacks | 123 Main Street |
| address2 | Billing address line 2 | Apt 4B |
| city | Billing city | New Delhi |
| state | Billing state | Delhi |
| country | Billing country | India |
| zipcode | Billing zip. Mandatory for cardless EMI. Character limit 20 | 110001 |
| udf1 | User-defined field | Custom Data 1 |
| udf2 | User-defined field | Custom Data 2 |
| udf3 | User-defined field | Custom Data 3 |
| udf4 | User-defined field | Custom Data 4 |
| udf5 | User-defined field | Custom Data 5 |

<Accordion title="Form POST" icon="fa-code">
  ```html
  <form action='https://test.payu.in/_payment' method='post'>
  <input type="hidden" name="key" value="JP***g" />
  <input type="hidden" name="txnid" value="t6svtqtjRdl34W" />
  <input type="hidden" name="productinfo" value="iPhone" />
  <input type="hidden" name="amount" value="10" />
  <input type="hidden" name="email" value="test@gmail.com" />
  <input type="hidden" name="firstname" value="Ashish" />
  <input type="hidden" name="pg" value="UPI" />
  <input type="hidden" name="bankcode" value="UPI" />
  <input type="hidden" name="vpa" value="test123@okhdfcbank" />
  <input type="hidden" name="surl" value="your own success url" />
  <input type="hidden" name="furl" value="your own failure url" />
  <input type="hidden" name="phone" value="9988776655" />
  <input type="hidden" name="hash" value="generated_on_your_server" />
  <input type="submit" value="submit">
  </form>
  ```
</Accordion>

<Accordion title="cURL" icon="fa-code">
  ```bash
  curl -X POST "https://test.payu.in/_payment" \
    -H "accept: application/json" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=JP***g" \
    -d "txnid=xdB9G7qYpfqszo" \
    -d "amount=10" \
    -d "firstname=PayU User" \
    -d "email=test@gmail.com" \
    -d "phone=9876543210" \
    -d "productinfo=iPhone" \
    -d "pg=UPI" \
    -d "bankcode=UPI" \
    -d "vpa=VPA-anything@payu" \
    -d "surl=https://apiplayground-response.herokuapp.com/" \
    -d "furl=https://apiplayground-response.herokuapp.com/" \
    -d "hash=649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb"
  ```
</Accordion>

## Handle the Callback

The UPI Collect page prints the reverse-hash order:

```
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

<Accordion title="Verify the response hash" icon="fa-shield-halved">
  <ReverseHashing />

  Sample response fields: `mihpayid`, `mode=UPI`, `status=success`, `unmappedstatus=captured`, `amount=10.00`, `PG_TYPE=UPI-PG`, `bankcode=UPI`, `error=E000`, `error_Message=No Error`.
</Accordion>

## Verify the Payment Server-Side

<Accordion title="Verify Payment API" icon="fa-circle-check">
  <Verify_Payment_Tabs />
</Accordion>

## Test Credentials

| VPA |
| --- |
| anything@payu |
| 9999999999@payu.in |

<Callout icon="⚠️" theme="warn">
  The legacy test page says the UPI in-app flow and the UPI Intent flow are not available in test mode.
</Callout>

## UPI Intent and QR

UPI Intent is not a form post on this page. The legacy UPI Intent page only links to [UPI Intent S2S](https://docs.payu.in/docs/upi-intent-server-to-server). The legacy overview points QR to [Dynamic Storefront QR](https://docs.payu.in/docs/integrated-dynamic-storefront) and [UPI QR](https://docs.payu.in/docs/integrate-upi-qr). Those flows are not copied here.

Integration Lab link from the UPI Collect page: https://payu.in/integrationlab/seamless/sm-upiflow

## Related Resources

<Cards columns={2}>
  <Card title="UPI Handles" icon="fa-at" href="https://docs.payu.in/docs/upi-handles">
    Bank-name portion of a VPA, linked from the vpa parameter.
  </Card>
  <Card title="Validate VPA API" icon="fa-check" href="https://docs.payu.in/reference/validate_vpa_api">
    Full request for the pre-step, which this page does not reproduce.
  </Card>
  <Card title="UPI Intent S2S" icon="fa-arrow-up-right-from-square" href="https://docs.payu.in/docs/upi-intent-server-to-server">
    The flow the NPCI note says web and seamless form-post merchants must use.
  </Card>
  <Card title="Test your integration" icon="fa-flask" href="../../test-integration">
    Test VPAs and the test key and salt.
  </Card>
</Cards>
