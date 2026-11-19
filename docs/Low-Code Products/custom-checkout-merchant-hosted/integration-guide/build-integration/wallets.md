---
title: Wallets
excerpt: Collect a wallet payment on your page with pg CASH and the wallet bank code
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Wallets — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Accept wallets with PayU Merchant Hosted Checkout. Post pg=CASH and the wallet bankcode. Advantage Club uses pg=RD and bankcode=ADVCLUB. Test values included.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Wallets

Collect wallet payments from your checkout. Post `pg=CASH` and the wallet's `bankcode`. Wallet codes are listed in [Wallet Codes](https://docs.payu.in/docs/wallet-codes/). Advantage Club is the exception: `pg=RD` and `bankcode=ADVCLUB`.

## Post the Payment Request

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/_payment` |
| Production | `POST https://secure.payu.in/_payment` |

### Mandatory Parameters

<!-- VALIDATION NEEDED: The source table describes furl as the success URL and surl as the failure URL. Request samples use surl for the success URL and furl for the failure URL. This table follows the samples. The Paytm cURL posts pg=cash and bankcode=paytm. The parameter table examples are CASH and PAYTM. -->

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
| key | String | Merchant key provided by PayU. | JP\*\*\*g |
| txnid | String | Transaction ID you generate. | ypl938459435 |
| amount | String | Payment amount. | 10.00 |
| productinfo | String | Short product description. | iPhone |
| firstname | String | Customer first name. | Ashish |
| email | String | Customer email. | abc@payu.in |
| phone | String | Customer phone. | 9876543210 |
| pg | String | `CASH` for wallets. `RD` for Advantage Club. | CASH |
| bankcode | String | Wallet code from [Wallet Codes](https://docs.payu.in/docs/wallet-codes/). | PAYTM |
| surl | String | Success URL in the request samples. | https://example.com/success |
| furl | String | Failure URL in the request samples. | https://example.com/failure |
| hash | String | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|SALT)` | calculated_hash_value |

### Optional Parameters

<!-- DOCUMENTATION GAP: The wallets page does not list optional parameters. Address and udf fields are not copied from other methods. -->

<Accordion title="Understanding Hashing and sample code" icon="fa-shield-halved">
  <HashingRequestParameters />
  <HashingSample />
</Accordion>

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
  <input type="hidden" name="hash" value="HASH_GENERATED_ON_SERVER" />
  <input type="submit" value="submit" />
</form>
```

The source says this HTML block is the wallet call for the test environment.

</Accordion>

<Accordion title="cURL" icon="fa-code">

Paytm sample from the wallets page. It posts lowercase `pg` and `bankcode`.

```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=J****g&txnid=aI1UM19ONxLgPz&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cash&bankcode=paytm&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
```

</Accordion>

## Advantage Club

<Callout icon="⚠️" theme="warn">
  There are no test credentials and no test environment for Advantage Club. The source says to test on the production environment.
</Callout>

| Parameter | Value |
| --- | --- |
| Endpoint in the sample | `POST https://secure.payu.in/_payment` |
| pg | RD |
| bankcode | ADVCLUB |

<Accordion title="cURL" icon="fa-code">

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

<Accordion title="Verify the response hash" icon="fa-shield-halved">
  <ReverseHashing />
</Accordion>

The success sample includes `mode=CASH`, `status=success`, `unmappedstatus=captured`, `PG_TYPE=CASH-PG`, `bankcode=CASH`, `error=E000`, and `error_Message=No Error`.

## Verify the Payment Server-Side

<Accordion title="Verify Payment API" icon="fa-circle-check">
  <Verify_Payment_Tabs />
</Accordion>

## Test Credentials

<!-- VALIDATION NEEDED: test-integration.md lists PayTM, PhonePe, and AmazonPay. The wallets page lists Paytm, Amazon, and Airtel. Both are shown. -->

From [Test Your Integration](../test-integration):

| Wallet | Mobile number | OTP |
| --- | --- | --- |
| PayTM | 7777777777 | 888888 |
| PhonePe | Use the PhonePe pre-prod app described in the PhonePe test-account docs linked from the test page | Not stated |
| AmazonPay | Use your original Amazon account details | Not stated |

From the wallets page:

| Wallet | Test details |
| --- | --- |
| Paytm | Mobile `7777777777`, OTP `888888` |
| Amazon | Use your real Amazon account in sandbox |
| Airtel | Use your mobile number |

## Related Resources

<Cards columns={2}>
  <Card title="Wallet Codes" icon="fa-wallet" href="https://docs.payu.in/docs/wallet-codes/">
    Values to post in `bankcode`.
  </Card>
  <Card title="Test Your Integration" icon="fa-flask" href="../test-integration">
    Test key, salt, and wallet test values.
  </Card>
  <Card title="Recurring Payments" icon="fa-repeat" href="https://docs.payu.in/docs/introduction-recurring-payments-integration">
    The wallets guide links here for subscriptions.
  </Card>
  <Card title="Offers" icon="fa-tags" href="https://docs.payu.in/docs/offers-integration">
    The wallets guide links to offers you configure on the Dashboard.
  </Card>
</Cards>
