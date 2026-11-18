---
title: Net Banking
excerpt: Collect a net banking payment with a bank-specific bankcode on _payment
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Net Banking — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Merchant Hosted net banking: post pg and bankcode to PayU _payment, handle the callback, verify the payment, and check net banking health.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Net Banking

Collect the bank choice on your site and post the payment to PayU. The parameter table says `pg=NB`. The HTML and cURL samples use `pg=TESTPG` and `bankcode=TESTPGNB`.

<!-- VALIDATION NEEDED: The steps card on the legacy net banking page says pg=NEFT. The parameter description says pg=NB. Every sample uses pg=TESTPG and bankcode=TESTPGNB. The legacy overview says merchants must always send the customer account number and IFSC on a net banking request. Those two fields are not in this parameter table. That sentence matches TPV wording, not this page. -->

## Post the Payment Request

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/_payment` |
| Production | `POST https://secure.payu.in/_payment` |

### Mandatory Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| key | Merchant key provided by PayU | JP\*\*\*g |
| txnid | Merchant transaction reference | ypl938459435 |
| amount | Payment amount | 10.00 |
| productinfo | Product description | iPhone |
| firstname | Customer first name | Ashish |
| email | Customer email | abc@payu.in |
| phone | Customer phone | 9876543210 |
| pg | The parameter text says `pg=NB` for net banking | TESTPG |
| bankcode | Bank code. The page points to Net Banking Codes. The test example is TESTPGNB | TESTPGNB |
| surl | See the callout under this table. The legacy table's description does not match the other method pages | https://merchant.com/failure |
| furl | See the callout under this table | https://merchant.com/success |
| hash | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|Salt)` | |

<Callout icon="⚠️" theme="warn">
  <!-- VALIDATION NEEDED: The legacy net banking table describes furl as the success URL and surl as the failure URL. Cards, UPI Collect, PayPal, and Pluxee describe surl as success and furl as failure. The examples in the table follow the swapped descriptions. -->
</Callout>

### Optional Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| address1 | Billing address line 1. Source says this helps fraud detection and chargebacks | 123 Main Street |
| address2 | Billing address line 2 | Apt 456 |
| city | Billing city | Mumbai |
| state | Billing state | Maharashtra |
| country | Billing country | India |
| zipcode | Billing zip. Mandatory for cardless EMI. Character limit 20 | 400001 |
| udf1 | User-defined field | custom_value_1 |
| udf2 | User-defined field | custom_value_2 |
| udf3 | User-defined field | custom_value_3 |
| udf4 | User-defined field | custom_value_4 |
| udf5 | User-defined field | custom_value_5 |

Bank codes are not listed on this page. The source points to [Net Banking Codes](https://docs.payu.in/docs/net-banking-codes).

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
  <form action='https://test.payu.in/_payment' method='post'>
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
  <input type="hidden" name="hash" value="generated_on_your_server" />
  <input type="submit" value="submit">
  </form>
  ```

  The legacy page says this HTML is for testing Merchant Hosted Checkout with net banking.
</Accordion>

## Handle the Callback

<Accordion title="Verify the response hash" icon="fa-shield-halved">
  <ReverseHashing />

  Sample response fields: `mihpayid`, `mode=NB`, `status=success`, `unmappedstatus=captured`, `txnid`, `amount=10.00`, `bank_ref_num`, `bankcode=TESTPGNB`, `error=E000`, `error_Message=No Error`.
</Accordion>

## Verify the Payment Server-Side

<Accordion title="Verify Payment API" icon="fa-circle-check">
  <Verify_Payment_Tabs />
</Accordion>

## Check Net Banking Health

You can check whether the net banking server is up with the `getNetBankingStatus` API.

<!-- DOCUMENTATION GAP: The request and response for getNetBankingStatus are not in this folder. The legacy page links the Get Net Banking Status API. -->

## Test Credentials

| Field | Value |
| --- | --- |
| Username | payu |
| Password | payu |
| OTP | 123456 |

## Related Resources

<Cards columns={2}>
  <Card title="Net Banking Codes" icon="fa-list" href="https://docs.payu.in/docs/net-banking-codes">
    Bank codes to send in `bankcode`.
  </Card>
  <Card title="Integration Lab — Net Banking" icon="fa-flask" href="https://payu.in/integrationlab/seamless/sm-nb-status">
    The legacy page links this flow for an end-to-end net banking sample.
  </Card>
  <Card title="Recurring Payments" icon="fa-rotate" href="https://docs.payu.in/docs/introduction-recurring-payments-integration">
    Linked from the legacy net banking page as a related integration.
  </Card>
  <Card title="Test your integration" icon="fa-vial" href="../../test-integration">
    Test key, salt, and the net banking test login.
  </Card>
</Cards>
