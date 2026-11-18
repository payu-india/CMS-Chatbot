---
title: UPI Collect
excerpt: Collect a UPI VPA on your page and post it with pg UPI and bankcode UPI
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: UPI Collect — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Integrate UPI Collect on Merchant Hosted Checkout. Validate the VPA, post pg UPI and bankcode UPI, and note the MCC 6012 and 6211 limit. MCC rules apply.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">
  As per NPCI guidelines in the source, UPI Collect is allowed only for MCC 6012 and 6211.

  Seamless form post must move to UPI Intent S2S. Android must use Smart Intent. iOS can keep Collect with a deeplink. Web must build a QR from the Intent deeplink instead of Collect.
</Callout>

<NPCI_Mandate />

# UPI Collect

UPI Collect on your checkout posts `pg=UPI` and `bankcode=UPI`, with the customer's VPA in `vpa`.

<!-- VALIDATION NEEDED: The overview table says UPI bankcode is N/A, then INTENT for Intent and UPIDBQR for QR. It does not list bankcode UPI. This page follows the UPI Collect parameter table and form, which post bankcode UPI. -->

## Validate the UPI Handle

Validate the VPA with the Validate VPA API before you start the payment.

<Accordion title="Request" icon="fa-code">
  The sample posts `command=validateVPA` and `var1` as the VPA.

```bash
curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "key=YOUR_MERCHANT_KEY" \
     -d "command=validateVPA" \
     -d "var1=customer@upi" \
     -d "hash=$HASH"
```

  <Validate_VPA />

  <!-- DOCUMENTATION GAP: The hash string for validateVPA is not written out on this page. The APIs page gives sha512(key|command|var1|SALT) for postservice commands. Confirm that formula covers validateVPA. -->
</Accordion>

<Accordion title="Response" icon="fa-table">
  Success:

```json
{
   "status": "SUCCESS",
   "vpa": "9999999999@upi",
   "isVPAValid": 1,
   "isAutoPayVPAValid": 1,
   "payerAccountName": "ABC"
}
```

  Failure sample from the source, which still has `status` SUCCESS:

```json
{"status":"SUCCESS","vpa":"abc@upi","isVPAValid":0,"payerAccountName":"NA"}
```
</Accordion>

## Post the Payment Request

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/_payment` |
| Production | `POST https://secure.payu.in/_payment` |

### Mandatory Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| `key` | Merchant key | `JP***g` |
| `txnid` | Your transaction id | `ypl938459435` |
| `amount` | Amount | `10.00` |
| `productinfo` | Product description | `iPhone` |
| `firstname` | Customer first name | `Ashish` |
| `email` | Customer email | `abc@payu.in` |
| `phone` | Customer phone | `9988776655` |
| `pg` | Must be `UPI` | `UPI` |
| `bankcode` | Bank code for this option. The table and the form use `UPI` | `UPI` |
| `vpa` | Customer VPA. The source points at UPI Handles for the bank part of the handle | `test123@okhdfcbank` |
| `surl` | Success URL. The table description says success. The example cell in the source is `https://example.com/failure` | `https://example.com/success` |
| `furl` | Failure URL. The table description says failure. The example cell in the source is `https://example.com/success` | `https://example.com/failure` |
| `hash` | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|Salt)` | Generated on your server |

<!-- VALIDATION NEEDED: In the UPI Collect mandatory table, the furl example URL is a success URL and the surl example URL is a failure URL. The descriptions say the opposite. The HTML form labels surl as "your own success url" and furl as "your own failure url". The examples in the table above follow the descriptions and the HTML, not the swapped example cells. -->

### Optional Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| `address1` | Billing line 1. Used for fraud detection and chargebacks | `123 Main Street` |
| `address2` | Billing line 2 | `Apt 4B` |
| `city` | Billing city | `New Delhi` |
| `state` | Billing state | `Delhi` |
| `country` | Billing country | `India` |
| `zipcode` | Postal code. Mandatory for cardless EMI. Limit 20 | `110001` |
| `udf1`–`udf5` | Your own fields | `Custom Data 1` |

<Accordion title="Form POST" icon="fa-code">

```html
<form action="https://test.payu.in/_payment" method="post">
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
<input type="hidden" name="hash" value="HASH" />
<input type="submit" value="submit">
</form>
```

</Accordion>

<Accordion title="cURL" icon="fa-code">

```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&txnid=xdB9G7qYpfqszo&amount=10&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=UPI&bankcode=UPI&vpa=VPA-anything@payu&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=GENERATED_HASH"
```

The source cURL uses `vpa=VPA-anything@payu`. The test-credentials section lists `anything@payu` without the `VPA-` prefix.

</Accordion>

## Handle the Callback

<ReverseHashing />

The reverse-hash order written on this page is:

```text
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

The success sample has `mode=UPI`, `status=success`, `unmappedstatus=captured`, `bankcode=UPI`, `error=E000`, and `error_Message=No Error`.

## Verify the Payment Server-Side

<Accordion title="Verify Payment API" icon="fa-circle-check">
  <Verify_Payment_Tabs />
</Accordion>

## Test Credentials

| VPA |
| --- |
| `anything@payu` |
| `9999999999@payu.in` |

<Callout icon="⚠️" theme="warn">
  The test page says the UPI in-app flow and the UPI intent flow are not available in test mode.
</Callout>

## Related Resources

<Cards columns={2}>
  <Card title="UPI Intent" icon="fa-qrcode" href="./upi-intent">
    The flow the NPCI note says web and Android seamless form post must move to.
  </Card>
  <Card title="UPI Handles" icon="fa-at" href="https://docs.payu.in/docs/upi-handles">
    Bank-name portion of a VPA, linked from the parameter table.
  </Card>
  <Card title="Test Your Integration" icon="fa-flask" href="../test-integration">
    Test key, salt, and these VPAs.
  </Card>
</Cards>
