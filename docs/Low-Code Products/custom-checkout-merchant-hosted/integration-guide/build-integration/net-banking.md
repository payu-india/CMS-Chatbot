---
title: Net Banking
excerpt: Post a net-banking payment with a bank code to PayU _payment
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Net Banking — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Collect net banking on your own checkout. Test with pg TESTPG and bankcode TESTPGNB, then verify the PayU callback and the payment on your server. See steps.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Net Banking

Collect the bank choice on your site and post it to PayU. The customer completes net banking on the bank page. PayU redirects back to your `surl` or `furl`.

<!-- VALIDATION NEEDED: pg and bankcode disagree inside the net-banking page and the overview.
- Parameter description: pg=NB.
- Step card: pg=NEFT.
- HTML, cURL, and the success sample: pg=TESTPG, bankcode=TESTPGNB.
- Overview table: pg=NB, bankcode varies by bank.
This page shows the test sample as the test sample. It does not replace NB with TESTPG for production. Production bank codes are in Net Banking Codes, which the source links. -->

<!-- VALIDATION NEEDED: The overview says every net-banking request must include the customer account number and IFSC. Those fields are not in this page's parameter table. They are treated on the Net Banking TPV page until PayU confirms they belong on every net-banking payment. -->

## Post the Payment Request

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/_payment` |
| Production | `POST https://secure.payu.in/_payment` |

### Mandatory Parameters

| Parameter | Description from the source | Example |
| --- | --- | --- |
| `key` | Merchant key | `JP***g` |
| `txnid` | Your transaction id | `ypl938459435` |
| `amount` | Amount | `10.00` |
| `productinfo` | Product description | `iPhone` |
| `firstname` | Customer first name | `Ashish` |
| `email` | Customer email | `abc@payu.in` |
| `phone` | Customer phone | `9876543210` |
| `pg` | The description says `NB`. The example cell is `TESTPG` | `TESTPG` in the test sample |
| `bankcode` | Bank code. The source links Net Banking Codes. The test example is `TESTPGNB` | `TESTPGNB` |
| `surl` | Success URL in the HTML sample | `https://merchant.com/success` |
| `furl` | Failure URL in the HTML sample | `https://merchant.com/failure` |
| `hash` | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|Salt)` | Generated on your server |

<!-- VALIDATION NEEDED: The source table calls furl the success URL and surl the failure URL, and its example URLs follow that swap. The HTML form on the same page sets surl to "your own success url" and furl to "your own failure url". This table follows the HTML form. -->

### Optional Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| `address1` | Billing line 1. The source says this helps fraud detection and chargebacks | `123 Main Street` |
| `address2` | Billing line 2 | `Apt 456` |
| `city` | Billing city | `Mumbai` |
| `state` | Billing state | `Maharashtra` |
| `country` | Billing country | `India` |
| `zipcode` | Postal code. The source says it is mandatory for cardless EMI. Limit 20 | `400001` |
| `udf1`–`udf5` | Your own fields | `custom_value_1` |

<Accordion title="Form POST" icon="fa-code">

```html
<form action="https://test.payu.in/_payment" method="post">
<input type="hidden" name="key" value="JP***g" />
<input type="hidden" name="txnid" value="t6svtqtjRdl34W" />
<input type="hidden" name="productinfo" value="iPhone" />
<input type="hidden" name="amount" value="10" />
<input type="hidden" name="email" value="test@gmail.com" />
<input type="hidden" name="firstname" value="Ashish" />
<input type="hidden" name="lastname" value="Kumar" />
<input type="hidden" name="pg" value="TESTPG" />
<input type="hidden" name="bankcode" value="TESTPGNB" />
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
-d "key=JP***g" \
-d "txnid=ewP8oRopzdHEtC" \
-d "amount=10.00" \
-d "firstname=Ashish" \
-d "email=test@gmail.com" \
-d "phone=9876543210" \
-d "productinfo=iPhone" \
-d "pg=TESTPG" \
-d "bankcode=TESTPGNB" \
-d "surl=https://apiplayground-response.herokuapp.com/" \
-d "furl=https://apiplayground-response.herokuapp.com/" \
-d "hash={{hash_value}}"
```

</Accordion>

<Accordion title="Hash sample" icon="fa-shield-halved">
  <HashingRequestParameters />
  <HashingSample />
</Accordion>

## Handle the Callback

<ReverseHashing />

The parsed success sample has `mode=NB`, `status=success`, `unmappedstatus=captured`, `bankcode=TESTPGNB`, `error=E000`, and `error_Message=No Error`. `mihpayid` in that sample is `403993715524045752`.

## Verify the Payment Server-Side

<Accordion title="Verify Payment API" icon="fa-circle-check">
  <Verify_Payment_Tabs />
</Accordion>

## Check Net Banking Health

You can check whether a net-banking bank is up with **getNetBankingStatus**. The source links the Get Net Banking Status API and does not include the request or response.

<!-- DOCUMENTATION GAP: getNetBankingStatus parameters and response fields are not in this folder. -->

## Test Credentials

| Field | Value |
| --- | --- |
| Username | `payu` |
| Password | `payu` |
| OTP | `123456` |

## Related Resources

<Cards columns={2}>
  <Card title="Net Banking Codes" icon="fa-building-columns" href="https://docs.payu.in/docs/net-banking-codes">
    Bank codes the parameter table says to post as bankcode.
  </Card>
  <Card title="Net Banking TPV" icon="fa-link" href="./net-banking-tpv">
    Account number and IFSC. Not specified on this page.
  </Card>
  <Card title="Integration Lab" icon="fa-flask" href="https://payu.in/integrationlab/seamless/sm-nb-status">
    The net-banking flow linked from the source page.
  </Card>
  <Card title="Test Your Integration" icon="fa-vial" href="../test-integration">
    Test key, salt, and these net-banking credentials.
  </Card>
</Cards>
