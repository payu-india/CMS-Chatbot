---
title: Net Banking
excerpt: Collect a net-banking payment on your page and post it to PayU with the bank code
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Net Banking — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Accept net banking with PayU Merchant Hosted Checkout. Post pg and bankcode to _payment, verify the callback, and check bank status. Includes test credentials.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Net Banking

Collect the customer's net-banking payment from your checkout and post it to `_payment`. The parameter text says `pg=NB`. The samples post `pg=TESTPG` and `bankcode=TESTPGNB`. Production bank codes are listed in [Net Banking Codes](doc:net-banking-codes).

<!-- VALIDATION NEEDED: The steps card says pg=NEFT. The parameter description says pg=NB and the example value is TESTPG. Every sample in this guide posts pg=TESTPG and bankcode=TESTPGNB. The callback sample returns mode=NB and bankcode=TESTPGNB. -->

## Post the Payment Request

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/_payment` |
| Production | `POST https://secure.payu.in/_payment` |

### Mandatory Parameters

<!-- VALIDATION NEEDED: The source parameter table describes furl as the success URL and surl as the failure URL. The samples post surl and furl with the usual success and failure URL names. This table uses the sample field names. -->

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
| key | String | Merchant key provided by PayU. | JP\*\*\*g |
| txnid | String | Transaction ID you generate for the order. | ypl938459435 |
| amount | String | Payment amount. | 10.00 |
| productinfo | String | Short product description. | iPhone |
| firstname | String | Customer first name. | Ashish |
| email | String | Customer email. | abc@payu.in |
| phone | String | Customer phone. | 9876543210 |
| pg | String | Payment gateway. The description says `NB` for net banking. The example value is `TESTPG`. | TESTPG |
| bankcode | String | Bank code. See [Net Banking Codes](doc:net-banking-codes). The sample value is `TESTPGNB`. | TESTPGNB |
| surl | String | Success URL in the request samples. | https://apiplayground-response.herokuapp.com/ |
| furl | String | Failure URL in the request samples. | https://apiplayground-response.herokuapp.com/ |
| hash | String | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|Salt)` | calculated_hash_value |

### Optional Parameters

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
| address1 | String | First line of the billing address. The source says this helps fraud detection and chargebacks. | 123 Main Street |
| address2 | String | Second line of the billing address. | Apt 456 |
| city | String | Billing city. | Mumbai |
| state | String | Billing state. | Maharashtra |
| country | String | Billing country. | India |
| zipcode | String | Billing postal code. The source says this is mandatory for cardless EMI. Character limit 20. | 400001 |
| udf1 | String | User-defined field. Up to five fields: udf1 through udf5. | custom_value_1 |
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
  <input type="hidden" name="hash" value="HASH_GENERATED_ON_SERVER" />
  <input type="submit" value="submit" />
</form>
```

</Accordion>

## Handle the Callback

Verify the reverse hash before you accept the payment.

<Accordion title="Verify the response hash" icon="fa-shield-halved">
  <ReverseHashing />
</Accordion>

The parsed success sample includes:

| Field | Sample value |
| --- | --- |
| mihpayid | 403993715524045752 |
| mode | NB |
| status | success |
| unmappedstatus | captured |
| txnid | ewP8oRopzdHEtC |
| amount | 10.00 |
| bankcode | TESTPGNB |
| error | E000 |
| error_Message | No Error |

## Verify the Payment Server-Side

<Accordion title="Verify Payment API" icon="fa-circle-check">
  <Verify_Payment_Tabs />
</Accordion>

## Check Net Banking Health

You can check whether the net-banking server is up with the **getNetBankingStatus** API. See [Get Net Banking Status API](ref:get_net_banking_status_api).

<!-- DOCUMENTATION GAP: Request parameters, hash fields, and the response for getNetBankingStatus are not in this folder. -->

## Test Credentials

| Field | Value |
| --- | --- |
| User name | payu |
| Password | payu |
| OTP | 123456 |

The same values are on [Test Your Integration](../test-integration).

## Related Resources

<Cards columns={2}>
  <Card title="Net Banking Codes" icon="fa-building-columns" href="https://docs.payu.in/docs/net-banking-codes">
    Bank codes to send in `bankcode`.
  </Card>
  <Card title="Get Net Banking Status API" icon="fa-heart-pulse" href="https://docs.payu.in/reference/get_net_banking_status_api">
    Check whether net banking is up.
  </Card>
  <Card title="Recurring Payments" icon="fa-repeat" href="https://docs.payu.in/docs/introduction-recurring-payments-integration">
    The net-banking guide links here for subscriptions.
  </Card>
  <Card title="Test Your Integration" icon="fa-flask" href="../test-integration">
    Test key, salt, and the net-banking credentials above.
  </Card>
</Cards>
