---
title: Cards
excerpt: Collect a card on your page and post it to PayU with pg CC
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Cards — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Accept Visa, Mastercard, AMEX, Diners, and Rupay on your own checkout. Post card fields to PayU _payment with pg CC, then verify the callback. PCI applies.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">
  Collecting card data on your site puts you in PCI-DSS scope. The source says that if you store or transmit cardholder data, you must complete the Self-Assessment Questionnaire A-EP and the Attestation of Compliance. International transactions must be enabled by writing to integration@pay.in.
</Callout>

# Cards

PayU accepts American Express, Visa, Mastercard, Diners, and Rupay on Merchant Hosted Checkout. The cards page posts `pg=CC`.

<!-- VALIDATION NEEDED: bankcode is not one value in the source. The overview table says CC. The cards step card says CC. The HTML form posts MAST. The parameter table says the code is based on the issuing bank and uses AMEX as the example. The cURL sample posts CC. The failure sample returns AMEX. The guest-checkout sample posts MASTERCARD. The saved-card sample posts VISA. The 3DS table example is CC. This page does not pick one. The source points at Cards Bank Codes for the list. -->

## Validate the Card Type

When the customer enters a debit or credit card, you can check the card type from the first six digits with **getBinInfo** (the BIN API).

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/merchant/postservice?form=2` |
| Production | `POST https://info.payu.in/merchant/postservice?form=2` |

<Accordion title="Request" icon="fa-code">
  The source's single-card note says `var1 = 1`, `var2 = 512345`, and `var5 = 1`. The cURL sample sends `var1=2` with the same `var2` and `var5`.

  <!-- VALIDATION NEEDED: var1 is 1 in the prose and 2 in the sample. Both are reproduced below. Do not drop either until PayU confirms which value is the single-card request. -->

```bash
curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
-H "accept: application/json" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "key=JP***g" \
-d "command=getBinInfo" \
-d "var1=2" \
-d "var2=512345" \
-d "var3=" \
-d "var4=" \
-d "var5=1" \
-d "hash={{hash_value}}"
```

  <!-- DOCUMENTATION GAP: This file has no request-parameter dictionary for getBinInfo beyond command, var1, var2, var3, var4, var5, key, and hash. The hash block on the cards page points at the general-API hash description and does not write the formula next to this call. The APIs page formula for command APIs is sha512(key|command|var1|SALT). -->
</Accordion>

<Accordion title="Response" icon="fa-table">
  Success sample from the source:

```php
$response = array(
  'status' => 1,
  'data'   => array(
      'bins_data' => array(
          'issuing_bank' => 'HDFC',
          'bin'           => '512345',
          'category'      => 'creditcard',
          'card_type'     => 'MAST',
          'is_domestic'   => 1,
      ),
  ),
);
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
| `key` | Merchant key from PayU at registration | `JP***g` |
| `txnid` | Unique transaction id you generate | `ashdfu72634` |
| `amount` | Payment amount | `1000.00` |
| `productinfo` | Product name or description | `iPhone` |
| `firstname` | Customer first name | `Ashish` |
| `email` | Customer email | `test@gmail.com` |
| `phone` | Customer phone | `9988776655` |
| `pg` | Payment gateway. For cards, `CC` | `CC` |
| `bankcode` | Based on the issuing bank. The table example is `AMEX`. See the validation note at the top of this page | `AMEX` |
| `ccnum` | Card number, 13–19 digits (15 for AMEX, 13–19 for Maestro). Validate with Luhn. PCI-DSS applies | `5123456789012346` |
| `ccname` | Name on card | `Ashish Kumar` |
| `ccvv` | CVV. 3 digits, or 4 for AMEX | `123` |
| `ccexpmon` | Expiry month, `MM`. Prefix 0 for months 1–9 | `10` |
| `ccexpyr` | Expiry year, four digits | `2026` |
| `surl` | Success URL | `https://yourwebsite.com/success` |
| `furl` | Failure URL | `https://yourwebsite.com/failure` |
| `hash` | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|Salt)` | Generated on your server |

### Optional Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| `address1` | Billing address line 1. The source says this helps fraud detection and chargebacks | `123 Main St` |
| `address2` | Billing address line 2 | `Apt 4B` |
| `city` | Billing city | `Mumbai` |
| `state` | Billing state | `Maharashtra` |
| `country` | Billing country | `India` |
| `zipcode` | Billing postal code. Mandatory for cardless EMI. Character limit 20 | `400001` |
| `udf1`–`udf5` | Your own values, up to five fields | `custom_value_1` |

<Accordion title="cURL" icon="fa-code">

The source marks this as a server-side call and says not to execute it in the browser. Replace the placeholders. `ccexpyr` in this sample is `YY`, while the parameter table says four digits.

```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=YOUR_MERCHANT_KEY" \
  -d "txnid=TXN_12345" \
  -d "amount=1000.00" \
  -d "productinfo=Product+Description" \
  -d "firstname=Customer+Name" \
  -d "email=customer@example.com" \
  -d "phone=9988776655" \
  -d "pg=CC" \
  -d "bankcode=CC" \
  -d "ccnum=CARD_NUMBER" \
  -d "ccexpmon=MM" \
  -d "ccexpyr=YY" \
  -d "ccvv=CVV" \
  -d "ccname=NAME_ON_CARD" \
  -d "surl=https://yourwebsite.com/success" \
  -d "furl=https://yourwebsite.com/failure" \
  -d "hash=HASH_GENERATED_ON_SERVER"
```

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
<input type="hidden" name="pg" value="CC" />
<input type="hidden" name="bankcode" value="MAST" />
<input type="hidden" name="ccnum" value="5123456789012346" />
<input type="hidden" name="ccname" value="Ashish Kumar" />
<input type="hidden" name="ccvv" value="123" />
<input type="hidden" name="ccexpmon" value="12" />
<input type="hidden" name="ccexpyr" value="2021" />
<input type="hidden" name="surl" value="your own success url" />
<input type="hidden" name="furl" value="your own failure url" />
<input type="hidden" name="phone" value="9988776655" />
<input type="hidden" name="hash" value="HASH" />
<input type="submit" value="submit">
</form>
```

</Accordion>

<Accordion title="Hash sample" icon="fa-shield-halved">
  <HashingRequestParameters />
  <HashingSample />
</Accordion>

## Saved Card Payment

Use this when you pay with a saved-card network token instead of the full card number.

### Mandatory Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| `key` | Merchant key | Your test key |
| `txnid` | Unique id. The source says PayU will not accept a duplicate transaction id | `s7hhDQVWvbhBdN` |
| `amount` | Amount. The same table says cardless EMI must be at least Rs. 8000 | `10.00` |
| `productinfo` | Product description. Character limit 100 | `iPhone` |
| `firstname` | Customer first name. Character limit 60 | `Ashish` |
| `email` | Customer email. Character limit 50 | `test@gmail.com` |
| `phone` | Customer phone. The source says a correct phone helps fraud detection and chargebacks | `9876543210` |
| `lastname` | Customer last name. Character limit 60 | `Verma` |
| `surl` | Success URL | `https://apiplayground-response.herokuapp.com/` |
| `furl` | Failure URL | `https://apiplayground-response.herokuapp.com/` |
| `hash` | Request hash. The source points at the Merchant Hosted hash doc | Generated on your server |
| `pg` | `CC` | `CC` |
| `bankcode` | Bank code for the card. Example in this table is `AMEX`. The cURL sample uses `VISA` | `AMEX` |
| `ccexpmon` | Network token expiry month | `10` |
| `ccexpyr` | Network token expiry year | `2022` |
| `store_card_token` | Saved-card network token generated at your end | `1234 4567 2456 3566` |
| `storecard_token_type` | Token type. The source says include `1` for this scenario | `1` |
| `additional_info` | JSON with `last4Digits`, `TAVV`, `trid`, and `tokenRefNo` | `{"last4Digits":"1234","TAVV":"ABCDEFGH","trid":"1234567890","tokenRefNo":"abcde123456"}` |

### Optional Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| `api_version` | API version | `1` |
| `address1` | Billing line 1. Character limit 100 | Address text |
| `address2` | Billing line 2. Character limit 100 | Address text |
| `city` | Billing city | `Mumbai` |
| `state` | Billing state | `Maharashtra` |
| `country` | Billing country. Character limit 50 | `India` |
| `zipcode` | Postal code. Mandatory for cardless EMI. Character limit 20 | `400004` |
| `udf1`–`udf5` | Your own fields. Character limit 255 each | |
| `ccnum` | Card number, 13–19 digits | Masked example in the source |
| `ccname` | Name on card | `Ashish` |
| `ccvv` | CVV entered by the customer | `123` |

<Accordion title="cURL" icon="fa-code">

```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=YourMerchantKey" \
  -d "txnid=NT_TXN_1234567890" \
  -d "amount=250.00" \
  -d "productinfo=Premium Subscription Plan" \
  -d "firstname=John" \
  -d "lastname=Doe" \
  -d "email=john.doe@example.com" \
  -d "phone=9876543210" \
  -d "surl=https://yourwebsite.com/payment/success" \
  -d "furl=https://yourwebsite.com/payment/failure" \
  -d "pg=CC" \
  -d "bankcode=VISA" \
  -d "ccexpmon=12" \
  -d "ccexpyr=2025" \
  -d "ccname=John Doe" \
  -d "store_card_token=4111111111111111" \
  -d "storecard_token_type=1" \
  -d "additional_info={\"last4Digits\":\"1111\",\"TAVV\":\"ABCD1234EFGH5678\",\"trid\":\"987654321012345\",\"tokenRefNo\":\"TKN_REF_12345678\"}" \
  -d "api_version=1" \
  -d "hash=GENERATED_HASH"
```

</Accordion>

## Guest Checkout and Alt ID

<Callout icon="📘" theme="info">
  Guest checkout has to be enabled. Contact your PayU Key Account Manager or PayU Integration Support.
</Callout>

The source says acquirers are not allowed to store card details after a stipulated timeline, and that guest checkout transactions would not be allowed after 31 October 2023. The plain card number is replaced with an Alternative ID (Alt ID).

<Accordion title="Scenario 1: PayU provisions the Alt ID and processes the payment" icon="fa-circle-1">
  No change to the `_payment` request you use to collect the payment.
</Accordion>

<Accordion title="Scenario 2: You provision the Alt ID outside PayU" icon="fa-circle-2">
  Post `alt_id`, and put TAVV (the cryptogram), the last four digits, and `par` in `additional_info`. The source says `par` is optional. The response is unchanged from the normal cards response.

  `tokenReferenceId` is required in `additional_info` when you provision the Alt ID outside PayU for a Diners card.

  | Parameter | Description | Example |
  | --- | --- | --- |
  | `pg` | `CC` | `CC` |
  | `bankcode` | Card bank code. Table example `AMEX`. Sample posts `MASTERCARD` | `AMEX` |
  | `ccname` | Name on card | `Ashish Kumar` |
  | `ccvv` | CVV | `123` |
  | `ccexpmon` | Card expiry month, or Alt ID expiry month. For Visa, post the plain card's expiry month. `MM` | `10` |
  | `ccexpyr` | Card or Alt ID expiry year, four digits. For Visa, post the plain card's expiry year | `2021` |
  | `alt_id` | Alt ID for the guest checkout | |
  | `additional_info` | JSON with TAVV, last four digits, and par | See the sample below |
  | `surl` / `furl` / `hash` | Same roles as the card payment | |

  The other mandatory fields in this scenario are `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, and `phone`. Optional fields are `address1`, `address2`, `city`, `state`, `country`, `zipcode`, and `udf1`–`udf5`.

  Sample `additional_info` from the source:

```json
{
  "tavv": "AKF/FaM3BPWoAAEWYTiQAAADFA==",
  "last4Digits": "2346",
  "par": "799F3ED865F5965CC760A32682BA8A80F19E99ECB3F7F03574C14F5B6C3EB2C1",
  "tokenReferenceId": "3acdd709-3c4b-4280-a6db-3f02271d09a3"
}
```

  | Field | Description in the source |
  | --- | --- |
  | `trid` | Token Requestor ID from the card network, via your token provider |
  | `tokenReferenceID` | Token reference id generated with the network token |
  | `TAVV` | Token authentication verification value, also called the cryptogram |

  <!-- VALIDATION NEEDED: The field table lists trid, tokenReferenceID, and TAVV. The JSON sample uses tavv, last4Digits, par, and tokenReferenceId. last4Digits and par are not in the field table. The key spelling differs (tokenReferenceID, tokenReferenceId, tokenRefNo on the saved-card table). -->

  The sample request posts to `http://local.secure.payu.in/_payment`. That host is what the source file contains. It is not the test URL (`https://test.payu.in/_payment`) and it is not the production URL (`https://secure.payu.in/_payment`).

```bash
curl --location 'http://local.secure.payu.in/_payment' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=smsplus' \
--data-urlencode 'pg=CC' \
--data-urlencode 'bankcode=MASTERCARD' \
--data-urlencode 'alt_id=5123456789012346' \
--data-urlencode 'additional_info={"tavv":"AKF/FaM3BPWoAAEWYTiQAAADFA==","last4Digits":"2346","par":"799F3ED865F5965CC760A32682BA8A80F19E99ECB3F7F03574C14F5B6C3EB2C1","tokenReferenceId":"3acdd709-3c4b-4280-a6db-3f02271d09a3"}' \
--data-urlencode 'ccname=Flipkart' \
--data-urlencode 'ccvv=126' \
--data-urlencode 'ccexpmon=05' \
--data-urlencode 'ccexpyr=2024' \
--data-urlencode 'phone=9999999999' \
--data-urlencode 'txnid={{txnid}}' \
--data-urlencode 'hash={{hash}}'
```

  The source also sends `firstname`, `email`, `amount`, `productinfo`, `surl`, and `furl` in that request.

  `authRefNo` on the response holds the AEVV for an AMEX transaction (the source says this is mandatory for AMEX CoFT provisioning) and `rupayAuthRefId` for Rupay. To receive `authRefNo`, contact your Key Account Manager or PayU Support. The sample response in the source is a failure and includes `authRefNo`, `corporate_card`, and `cobranded_card`.
</Accordion>

<Accordion title="Scenario 3: PayU provisions the Alt ID and you process elsewhere" icon="fa-circle-3">
  The source says to use the Provision Alt ID API and links to it. The request and response are not in this folder.

  <!-- DOCUMENTATION GAP: Provision Alt ID request parameters are not in the Merchant Hosted cards page. Use the linked Provision Alt ID API reference. Do not reconstruct the body. -->
</Accordion>

## 3DS Secure 2.0

PayU supports 3DS 2.0 on Merchant Hosted Checkout. Include `threeDS2RequestData` with the cards `_payment` request.

The 3DS parameter table lists `threeDS2RequestData` and `txn_s2s_flow` as optional. The prose says you must include `threeDS2RequestData`.

<!-- VALIDATION NEEDED: The cards page says you must include threeDS2RequestData, and the same page lists threeDS2RequestData and txn_s2s_flow (example 4) under optional parameters. -->

`threeDS2RequestData` carries `browserInfo`:

| Field | Description | Example |
| --- | --- | --- |
| `userAgent` | Browser user agent | |
| `acceptHeader` | Header format | `application/json` |
| `language` | Language for the 3DS challenge | `en-US` |
| `colorDepth` | Screen color depth | `24` |
| `screenHeight` | Screen height | `640` |
| `screenWidth` | Screen width | `480` |
| `javaEnabled` | Whether Java is enabled | `true` |
| `timeZone` | Time zone code | `273` |
| `ip` | IP of the device | `10.248.2.71` |

The JSON example in the source uses `screenHeight` 600, `screenWidth` 800, and `timeZone` `-300`. The field table examples differ. Both sets are in the source file.

Card fields for this request are the same mandatory card set (`pg=CC`, card number, name, CVV, expiry, `surl`, `furl`, `hash`). The table's `bankcode` example is `CC`. The `ccnum` example is `4012000000002004`. `lastname` is optional.

## Handle the Callback

<ReverseHashing />

<Accordion title="Sample response" icon="fa-code">

Success: `status=success`, `unmappedstatus=captured`, `mode=CC`, `error=E000`, `error_Message=No Error`, `field7=AUTHPOSITIVE`, `field9=Transaction is Successful`. `bankcode` in that sample is `CC`. `cardnum` is masked (`512345XXXXXX2346`).

Failure: `status=failure`, `unmappedstatus=failed`, `error=E1903`, `error_Message=Authorization failed at Bank`, `field7=AUTHNEGATIVE`, `field9=Authorization failed at Bank`. `bankcode` in that sample is `AMEX`. The source says `cardhash` is no longer supported in postback params.

</Accordion>

## Verify the Payment Server-Side

<Accordion title="Verify Payment API" icon="fa-circle-check">
  <Verify_Payment_Tabs />
</Accordion>

## Test Credentials

<!-- DOCUMENTATION GAP: The cards page numbers 5123456789012346 and 4012000000002004 are request examples. They are not labeled as sandbox test cards. The test page lists EMI cards only. Do not treat the examples above as test credentials. EMI test cards are on the Test Your Integration page. -->

## Related Resources

<Cards columns={2}>
  <Card title="Collect Payment API — Cards" icon="fa-rectangle-api" href="https://docs.payu.in/reference/_payment_merchant_hosted_cards">
    API reference linked from the cards page.
  </Card>
  <Card title="BIN API" icon="fa-credit-card" href="https://docs.payu.in/reference/get_bin_info_api">
    getBinInfo, linked from the card-type step.
  </Card>
  <Card title="Test Your Integration" icon="fa-flask" href="../test-integration">
    Test key, salt, and the EMI card numbers that are actually labeled as test data.
  </Card>
  <Card title="Best Practices" icon="fa-shield-halved" href="../../best-practices">
    What not to store, and how to confirm the payment.
  </Card>
</Cards>
