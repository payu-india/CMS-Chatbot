---
title: Wallets
excerpt: Collect a wallet payment with pg=CASH and the wallet bankcode
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Wallets — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Merchant Hosted wallet payments: post pg=CASH and a wallet bankcode to PayU _payment. Advantage Club uses pg=RD and bankcode=ADVCLUB.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Wallets

Post `pg=CASH` and the wallet's `bankcode`. Advantage Club is the exception in the source: `pg=RD` and `bankcode=ADVCLUB`. Wallet codes are listed in [Wallet Codes](https://docs.payu.in/docs/wallet-codes), not on this page. The Paytm sample uses `PAYTM`.

## Post the Payment Request

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/_payment` |
| Production | `POST https://secure.payu.in/_payment` |

### Mandatory Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| key | Merchant key | JP\*\*\*g |
| txnid | Merchant transaction reference | ypl938459435 |
| amount | Payment amount | 10.00 |
| productinfo | Product description | iPhone |
| firstname | Customer first name | Ashish |
| email | Customer email | abc@payu.in |
| phone | Customer phone | 9876543210 |
| pg | `CASH` for wallets. `RD` for Advantage Club | CASH |
| bankcode | Wallet code from Wallet Codes. Paytm sample is PAYTM. Advantage Club is ADVCLUB | PAYTM |
| surl | See the callout. The legacy wallets table's description does not match the other method pages | https://example.com/failure |
| furl | See the callout | https://example.com/success |
| hash | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|SALT)` | |

<Callout icon="⚠️" theme="warn">
  <!-- VALIDATION NEEDED: The legacy wallets table describes furl as the success URL and surl as the failure URL. Cards, UPI Collect, PayPal, and Pluxee describe surl as success and furl as failure. The Paytm cURL uses lowercase pg=cash and bankcode=paytm. The legacy overview says bank codes are case-sensitive. -->
</Callout>

### Optional Parameters

<!-- DOCUMENTATION GAP: The wallets page does not publish a separate optional-parameter table. Do not copy the card or net banking optional list onto wallets. -->

<Accordion title="Form POST" icon="fa-code">
  ```html
  <form action='https://test.payu.in/_payment' method='post'>
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
  <input type="hidden" name="hash" value="generated_on_your_server" />
  <input type="submit" value="submit">
  </form>
  ```
</Accordion>

<Accordion title="cURL" icon="fa-code">
  Paytm sample, as written, with lowercase `pg` and `bankcode`:

  ```bash
  curl -X POST "https://test.payu.in/_payment" \
    -H "accept: application/json" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=J****g&txnid=aI1UM19ONxLgPz&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cash&bankcode=paytm&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
  ```
</Accordion>

### Advantage Club

Advantage Club uses `pg=RD` and `bankcode=ADVCLUB`. The legacy page says there is no test environment and no test credentials. Test on the production environment.

```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=J****g" \
  -d "txnid=aI1UM19ONxLgPz" \
  -d "amount=10.00" \
  -d "firstname=Ashish" \
  -d "email=test@gmail.com" \
  -d "phone=9876543210" \
  -d "productinfo=iPhone" \
  -d "pg=RD" \
  -d "bankcode=ADVCLUB" \
  -d "surl=https://apiplayground-response.herokuapp.com/" \
  -d "furl=https://apiplayground-response.herokuapp.com/" \
  -d "hash=GENERATED_ON_YOUR_SERVER"
```

<!-- VALIDATION NEEDED: The Advantage Club section says there is no test environment, and the sample still posts to https://test.payu.in/_payment. The hash in the legacy sample is not repeated here. -->

## Handle the Callback

<Accordion title="Verify the response hash" icon="fa-shield-halved">
  <ReverseHashing />

  Sample response fields: `mode=CASH`, `PG_TYPE=CASH-PG`, `bankcode=CASH`, `error=E000`, `error_Message=No Error`. The sample also includes `splitInfo`.
</Accordion>

## Verify the Payment Server-Side

<Accordion title="Verify Payment API" icon="fa-circle-check">
  <Verify_Payment_Tabs />
</Accordion>

## Test Credentials

| Wallet | Test details in source |
| --- | --- |
| Paytm | Mobile `7777777777`, OTP `888888`. The same pair is on the product test page |
| PhonePe | Product test page: use the PhonePe pre-prod app described at https://developer.phonepe.com/v1/docs/setting-up-test-account |
| Amazon Pay | Product test page: use your original Amazon account. The wallets page says the same |
| Airtel | Wallets page only: use your mobile number. The product test page does not list Airtel |

<!-- VALIDATION NEEDED: PhonePe is on the product test page and not in the wallets-page test table. Airtel is on the wallets page and not on the product test page. -->

## Related Resources

<Cards columns={2}>
  <Card title="Wallet Codes" icon="fa-list" href="https://docs.payu.in/docs/wallet-codes">
    Values to send in `bankcode`.
  </Card>
  <Card title="Collect Payment API" icon="fa-rectangle-api" href="https://docs.payu.in/reference/_payment_merchant_hosted">
    Try-it reference linked from the wallets page.
  </Card>
  <Card title="Recurring Payments" icon="fa-rotate" href="https://docs.payu.in/docs/introduction-recurring-payments-integration">
    Linked from the legacy wallets page.
  </Card>
  <Card title="Test your integration" icon="fa-flask" href="../../test-integration">
    Test key, salt, and wallet test numbers.
  </Card>
</Cards>
