---
title: Wallets
excerpt: Post a wallet payment with pg CASH and the wallet bankcode
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Wallets — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Accept wallets on Merchant Hosted Checkout. Post pg CASH and the wallet bankcode. Advantage Club uses pg RD and bankcode ADVCLUB on production. See test values.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Wallets

Post `pg=CASH` and the wallet's `bankcode`. The source says to take the code from Wallet Codes. Advantage Club is the exception in this file: `pg=RD` and `bankcode=ADVCLUB`.

## Post the Payment Request

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/_payment` |
| Production | `POST https://secure.payu.in/_payment` |

<Callout icon="🚧" theme="warn">
  The source says there are no test credentials and no test environment for Advantage Club. Test that wallet on production. The Java sample in the same section posts to `https://test.payu.in/_payment` while the cURL and the other samples post to `https://secure.payu.in/_payment`.
</Callout>

<!-- VALIDATION NEEDED: Advantage Club has no test environment in the callout, and one code sample still uses the test host. -->

### Mandatory Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| `key` | Merchant key | `JP***g` |
| `txnid` | Your transaction id | `ypl938459435` |
| `amount` | Amount | `10.00` |
| `productinfo` | Product description | `iPhone` |
| `firstname` | Customer first name | `Ashish` |
| `email` | Customer email | `abc@payu.in` |
| `phone` | Customer phone | `9876543210` |
| `pg` | `CASH` for wallets in general. `RD` for Advantage Club | `CASH` |
| `bankcode` | Wallet code from Wallet Codes. The table example is `PAYTM`. Advantage Club is `ADVCLUB` | `PAYTM` |
| `surl` | Success URL in the HTML form | Your success URL |
| `furl` | Failure URL in the HTML form | Your failure URL |
| `hash` | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|SALT)` | Generated on your server |

<!-- VALIDATION NEEDED: The wallets parameter table describes furl as the success URL and surl as the failure URL. The HTML form sets surl to "your own success url" and furl to "your own failure url". This table follows the HTML form. -->

<!-- VALIDATION NEEDED: The parameter table uses pg CASH and bankcode PAYTM. The Paytm cURL posts pg=cash and bankcode=paytm. The overview says bankcode is case-sensitive. The success sample's bankcode is CASH, not PAYTM. -->

### Optional Parameters

<!-- DOCUMENTATION GAP: The wallets page has no optional-parameter table. Do not copy the card optional fields onto wallets. -->

### Advantage Club

| Parameter | Value in the source |
| --- | --- |
| `pg` | `RD` |
| `bankcode` | `ADVCLUB` |
| URL in the cURL | `https://secure.payu.in/_payment` |

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
<input type="hidden" name="pg" value="CASH" />
<input type="hidden" name="bankcode" value="PAYTM" />
<input type="hidden" name="surl" value="your own success url" />
<input type="hidden" name="furl" value="your own failure url" />
<input type="hidden" name="phone" value="9988776655" />
<input type="hidden" name="hash" value="HASH" />
<input type="submit" value="submit">
</form>
```

</Accordion>

<Accordion title="cURL" icon="fa-code">

Paytm sample from the source. Note the lowercase `pg` and `bankcode`.

```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=J****g&txnid=aI1UM19ONxLgPz&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cash&bankcode=paytm&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=GENERATED_HASH"
```

Advantage Club sample from the source:

```bash
curl -X POST "https://secure.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=YOUR_MERCHANT_KEY" \
  -d "txnid=ADVCLUB_TXN_001" \
  -d "amount=10.00" \
  -d "productinfo=iPhone" \
  -d "firstname=Ashish" \
  -d "email=test@gmail.com" \
  -d "phone=9876543210" \
  -d "pg=RD" \
  -d "bankcode=ADVCLUB" \
  -d "surl=https://yourwebsite.com/success" \
  -d "furl=https://yourwebsite.com/failure" \
  -d "hash=YOUR_CALCULATED_HASH"
```

</Accordion>

## Handle the Callback

<ReverseHashing />

The success sample has `mode=CASH`, `status=success`, `unmappedstatus=captured`, `PG_TYPE=CASH-PG`, `bankcode=CASH`, `error=E000`, and `error_Message=No Error`. `field9` is `Transaction Completed Successfully`.

## Verify the Payment Server-Side

<Accordion title="Verify Payment API" icon="fa-circle-check">
  <Verify_Payment_Tabs />
</Accordion>

## Test Credentials

| Wallet | What the source says |
| --- | --- |
| Paytm | Mobile `7777777777`, OTP `888888`. The wallets page and the test page agree |
| PhonePe | Use the PhonePe pre-prod app. The test page links `https://developer.phonepe.com/v1/docs/setting-up-test-account`. OTP is `NA` |
| Amazon Pay | Use your real Amazon account. The test page says the same |
| Airtel | The wallets page says to use your mobile number. The test page does not list Airtel |

<Callout icon="🚧" theme="warn">
  Advantage Club has no test credentials in the source.
</Callout>

## Related Resources

<Cards columns={2}>
  <Card title="Wallet Codes" icon="fa-wallet" href="https://docs.payu.in/docs/wallet-codes/">
    bankcode values the parameter table says to use.
  </Card>
  <Card title="Test Your Integration" icon="fa-flask" href="../test-integration">
    Test key, salt, and the wallet values above.
  </Card>
</Cards>
