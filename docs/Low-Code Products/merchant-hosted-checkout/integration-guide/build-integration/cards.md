---
title: Cards
excerpt: Collect card details on your page, validate the BIN, and post pg CC to PayU
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Cards — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Accept Visa, Mastercard, American Express, Diners, and RuPay on your checkout. Validate the BIN, post to _payment, and support saved cards, Alt ID, and 3DS 2.0.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">
  Collecting card details on your site is in PCI-DSS scope. The cards page names the Self-Assessment Questionnaire A-EP and Attestation of Compliance. International transactions must be enabled by the PayU Integration Team at integration@pay.in.
</Callout>

# Cards

PayU accepts American Express, Visa, Mastercard, Diners, and RuPay on Merchant Hosted Checkout. The overview and the steps card use `pg=CC`.

<!-- VALIDATION NEEDED: bankcode is CC on the overview table, the steps card, the cURL sample, and the 3DS sample. The HTML form sends MAST. The mandatory-parameter example is AMEX and points to Cards Bank Codes. Saved-card samples use AMEX and VISA. The guest-checkout sample uses MASTERCARD. -->

## Validate the Card Type

Validate the card with the first six digits before you take payment. The API is `getBinInfo` (BIN API). See [BIN APIs](https://docs.payu.in/reference/get_bin_info_api).

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/merchant/postservice?form=2` |
| Production | `POST https://info.payu.in/merchant/postservice?form=2` |

<!-- VALIDATION NEEDED: The prose says var1=1, var2=512345, and var5=1. The sample request sends var1=2, var2=512345, and var5=1. The sample is shown below. -->

<Accordion title="Request" icon="fa-code">

Hash post-service commands as `sha512(key|command|var1|SALT)`. See [API index](../../merchant-hosted-checkout-apis).

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

</Accordion>

<Accordion title="Response" icon="fa-table">

Success sample from the cards page:

| Field | Sample value |
| --- | --- |
| status | 1 |
| data.bins_data.issuing_bank | HDFC |
| data.bins_data.bin | 512345 |
| data.bins_data.category | creditcard |
| data.bins_data.card_type | MAST |
| data.bins_data.is_domestic | 1 |

</Accordion>

## Post the Payment Request

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/_payment` |
| Production | `POST https://secure.payu.in/_payment` |

Try It and the response reference: [Collect Payment API - Merchant Hosted Checkout](https://docs.payu.in/reference/_payment_merchant_hosted).

### Mandatory Parameters

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
| key | String | Merchant key. | JP\*\*\*g |
| txnid | String | Unique transaction ID you generate. | ashdfu72634 |
| amount | String | Payment amount. | 1000.00 |
| productinfo | String | Product description. | iPhone |
| firstname | String | Customer first name. | Ashish |
| email | String | Customer email. | test@gmail.com |
| phone | String | Customer phone. | 9988776655 |
| pg | String | `CC` for card payments. | CC |
| bankcode | String | The parameter text says this is based on the issuing bank. See [Cards Bank Codes](doc:cards-bank-codes). The example in that table is `AMEX`. Other samples use `CC`, `MAST`, `VISA`, and `MASTERCARD`. | AMEX |
| ccnum | String | 13–19 digit card number (15 for AMEX, 13–19 for Maestro). PCI-DSS applies. Validate with the LUHN algorithm. | 5123456789012346 |
| ccname | String | Name on card. | Ashish Kumar |
| ccvv | String | CVV. 3 digits, or 4 for AMEX. | 123 |
| ccexpmon | String | Expiry month, `MM`. Prefix 0 for months 1–9. | 10 |
| ccexpyr | String | Expiry year, four digits. | 2026 |
| surl | String | Success URL. | https://yourwebsite.com/success |
| furl | String | Failure URL. | https://yourwebsite.com/failure |
| hash | String | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|Salt)` | |

### Optional Parameters

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
| address1 | String | Billing address line 1. The source says this helps fraud detection and chargebacks. | 123 Main St |
| address2 | String | Billing address line 2. | Apt 4B |
| city | String | Billing city. | Mumbai |
| state | String | Billing state. | Maharashtra |
| country | String | Billing country. | India |
| zipcode | String | Billing postal code. Mandatory for cardless EMI. Character limit 20. | 400001 |
| udf1 | String | User-defined field. Up to udf5. | custom_value_1 |
| udf2 | String | User-defined field. | custom_value_2 |
| udf3 | String | User-defined field. | custom_value_3 |
| udf4 | String | User-defined field. | custom_value_4 |
| udf5 | String | User-defined field. | custom_value_5 |

<Accordion title="Understanding Hashing and sample code" icon="fa-shield-halved">
  <HashingRequestParameters />
  <HashingSample />
</Accordion>

<Accordion title="cURL" icon="fa-code">

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
  <input type="hidden" name="hash" value="HASH_GENERATED_ON_SERVER" />
  <input type="submit" value="submit" />
</form>
```

</Accordion>

## Pay with a Saved Card

Send the network token instead of the plain card number. `storecard_token_type` is `1` for this scenario.

### Mandatory Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| key | Merchant key. | Your Test Key |
| txnid | Unique ID. The source says PayU will not accept a duplicate transaction ID. | s7hhDQVWvbhBdN |
| amount | Payment amount. The source says cardless EMI must be at least Rs. 8000. | 10.00 |
| productinfo | Product description. Character limit 100. | iPhone |
| firstname | Customer first name. Character limit 60. | Ashish |
| email | Customer email. Character limit 50. | test@gmail.com |
| phone | Customer phone. The source says this is required for fraud detection and chargebacks. | 9876543210 |
| lastname | Customer last name. Character limit 60. | Verma |
| surl | Success URL. | https://apiplayground-response.herokuapp.com/ |
| furl | Failure URL. | https://apiplayground-response.herokuapp.com/ |
| hash | Request hash. See [Generate Hash](doc:generate-hash-merchant-hosted). | |
| pg | `CC`. | CC |
| bankcode | Scheme or bank code. The table example is `AMEX`. The sample request uses `VISA`. | AMEX |
| ccexpmon | Network token expiry month. | 10 |
| ccexpyr | Network token expiry year. | 2022 |
| store_card_token | Saved-card network token generated at your end. | 1234 4567 2456 3566 |
| storecard_token_type | Token type. The source says to send `1` for this scenario. | 1 |
| additional_info | JSON with `last4Digits`, `TAVV`, `trid`, and `tokenRefNo`. | `{"last4Digits": "1234", "TAVV": "ABCDEFGH", "trid": "1234567890", "tokenRefNo": "abcde123456"}` |

### Optional Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| api_version | API version. | 1 |
| address1 | Billing address line 1. Character limit 100. | H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai |
| address2 | Billing address line 2. Character limit 100. | 34 Saikripa-Estate, Tilak Nagar |
| city | Billing city. | Mumbai |
| state | Billing state. | Maharashtra |
| country | Billing country. Character limit 50. | India |
| zipcode | Billing postal code. Mandatory for cardless EMI. Character limit 20. | 400004 |
| udf1 | User-defined field. Character limit 255. | Payment Preference |
| udf2 | User-defined field. Character limit 255. | Shipping Method |
| udf3 | User-defined field. Character limit 255. | Shipping Address |
| udf4 | User-defined field. Character limit 255. | Shipping City |
| udf5 | User-defined field. Character limit 255. | Shipping Zip Code |
| ccnum | Card number, listed as optional on the saved-card table. | 512\*\*\*6789012346 |
| ccname | Name on card, listed as optional on the saved-card table. | Ashish |
| ccvv | CVV, listed as optional on the saved-card table. | 123 |

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
  -d "hash=HASH_GENERATED_ON_SERVER"
```

</Accordion>

## Guest Checkout and Alt ID

Guest checkout lets a customer pay without an account on your site. To enable it, contact your PayU Key Account Manager or PayU Integration Support.

The cards page says acquirers may not store card details after the timeline set by the RBI, and that guest checkout with a plain card number was not allowed after 31 October 2023. The plain card number is replaced with an Alternative ID (Alt ID).

### Scenario 1 — PayU provisions and processes

No change to the `_payment` request used to collect the payment.

### Scenario 2 — Alt ID provisioned outside PayU

Pass `alt_id` and send `TAVV` (cryptogram), the last four digits, and `par` inside `additional_info`. The cards page says the response does not change. `par` is optional. For Diners, `tokenReferenceId` is required in `additional_info` when you provision the Alt ID outside PayU.

| Parameter | Description | Example |
| --- | --- | --- |
| pg | `CC`. | CC |
| bankcode | Scheme code. The sample uses `MASTERCARD`. | MASTERCARD |
| ccname | Name on card. | Ashish Kumar |
| ccvv | CVV. | 123 |
| ccexpmon | Card expiry month, or Alt ID expiry month. For Visa, post the plain card expiry month. `MM`. | 10 |
| ccexpyr | Card expiry year, or Alt ID expiry year. For Visa, post the plain card expiry year. Four digits. | 2021 |
| alt_id | Alt ID for the guest checkout. | |
| additional_info | JSON with `tavv`, `last4Digits`, `par`, and `tokenReferenceId`. | See the sample below |

`additional_info` sample:

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
| trid | Token Requestor ID from the card network, via your token provider. |
| tokenReferenceID | Token reference generated with the network token. |
| TAVV | Token authentication verification value, also called the cryptogram. |

The guest-checkout sample posts to `http://local.secure.payu.in/_payment` with `pg=CC`, `bankcode=MASTERCARD`, and `alt_id`.

<!-- VALIDATION NEEDED: The guest-checkout cURL uses http://local.secure.payu.in/_payment. Every other card sample uses https://test.payu.in/_payment. -->

### Scenario 3 — Provision Alt ID from PayU

The Provision Alt ID API provisions an Alt ID from PayU when you process the transaction outside PayU. See [Provision Alt ID API](https://docs.payu.in/reference/provision-alt-id-api).

<!-- DOCUMENTATION GAP: Scenario 3 has no request or response sample in this folder. -->

## 3DS Secure 2.0

Send `threeDS2RequestData` with the card `_payment` request. The sample also sends `txn_s2s_flow=4`. The parameter table lists `threeDS2RequestData` and `txn_s2s_flow` as optional, together with `lastname`.

Reference: [Collect Payment API - Cards (Merchant Hosted Checkout)](https://docs.payu.in/reference/_payment_merchant_hosted_cards).

### Additional Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| txn_s2s_flow | Server-to-server flow type. | 4 |
| threeDS2RequestData | Browser information for 3DS 2.0. | JSON below |
| lastname | Customer last name. | Test |

`threeDS2RequestData` wraps `browserInfo`:

```json
{
  "browserInfo": {
    "userAgent": "Mozilla/5.0",
    "acceptHeader": "*/*",
    "language": "en-US",
    "colorDepth": "24",
    "screenHeight": "600",
    "screenWidth": "800",
    "timeZone": "-300",
    "javaEnabled": true,
    "ip": "10.248.2.71"
  }
}
```

| Field | Description | Example |
| --- | --- | --- |
| userAgent | Device browser user agent. | |
| acceptHeader | Header format. | application/json |
| language | Language for the 3DS challenge. | en-US |
| colorDepth | Screen color depth. | 24 |
| screenHeight | Screen height. | 640 |
| screenWidth | Screen width. | 480 |
| javaEnabled | Whether Java is enabled. | true |
| timeZone | Time-zone code. | 273 |
| ip | IP address of the device. | 10.248.2.71 |

<Accordion title="cURL" icon="fa-code">

```bash
curl --location 'https://test.payu.in/_payment' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=JF****g' \
  --data-urlencode 'firstname=Ashish' \
  --data-urlencode 'email=test@example.com' \
  --data-urlencode 'amount=10' \
  --data-urlencode 'phone=9876543210' \
  --data-urlencode 'productinfo=Product_info' \
  --data-urlencode 'surl=http://pp30admin.payu.in/test_response' \
  --data-urlencode 'furl=http://pp30admin.payu.in/test_response' \
  --data-urlencode 'pg=CC' \
  --data-urlencode 'bankcode=CC' \
  --data-urlencode 'ccnum=4012000000002004' \
  --data-urlencode 'ccname=Test User' \
  --data-urlencode 'ccvv=123' \
  --data-urlencode 'ccexpmon=06' \
  --data-urlencode 'ccexpyr=2024' \
  --data-urlencode 'txnid=jYhbOYH9o4' \
  --data-urlencode 'hash=HASH_GENERATED_ON_SERVER' \
  --data-urlencode 'txn_s2s_flow=4' \
  --data-urlencode 'threeDS2RequestData={"browserInfo":{"userAgent":"Mozilla/5.0","acceptHeader":"*/*","language":"en-US","colorDepth":"24","screenHeight":"600","screenWidth":"800","timeZone":"-300","javaEnabled":true,"ip":"10.248.2.71"}}'
```

</Accordion>

## Handle the Callback

<Accordion title="Verify the response hash" icon="fa-shield-halved">
  <ReverseHashing />
</Accordion>

Success sample values include `mode=CC`, `status=success`, `unmappedstatus=captured`, `error=E000`, `error_Message=No Error`, `field7=AUTHPOSITIVE`, `field9=Transaction is Successful`, `bankcode=CC`, and a masked `cardnum`.

Failure sample values include `status=failure`, `unmappedstatus=failed`, `field7=AUTHNEGATIVE`, `field9=Authorization failed at Bank`, `error=E1903`, `error_Message=Authorization failed at Bank`, and `bankcode=AMEX`. The failure sample says `cardhash` is no longer supported in postback params.

## Verify the Payment Server-Side

<Accordion title="Verify Payment API" icon="fa-circle-check">
  <Verify_Payment_Tabs />
</Accordion>

## Test Credentials

<!-- DOCUMENTATION GAP: The test page has EMI card numbers, not a plain credit or debit test card. EMI numbers are on the test page. Card numbers inside the request samples on this page are not labeled as test credentials. -->

## Related Resources

<Cards columns={2}>
  <Card title="BIN API" icon="fa-credit-card" href="https://docs.payu.in/reference/get_bin_info_api">
    `getBinInfo` reference.
  </Card>
  <Card title="Cards Bank Codes" icon="fa-list" href="https://docs.payu.in/docs/cards-bank-codes">
    Values the parameter table points to for `bankcode`.
  </Card>
  <Card title="Cards Collect Payment API" icon="fa-rectangle-api" href="https://docs.payu.in/reference/_payment_merchant_hosted_cards">
    Merchant Hosted cards reference, including 3DS.
  </Card>
  <Card title="Test Your Integration" icon="fa-flask" href="../test-integration">
    Test key, salt, and EMI test cards.
  </Card>
</Cards>
