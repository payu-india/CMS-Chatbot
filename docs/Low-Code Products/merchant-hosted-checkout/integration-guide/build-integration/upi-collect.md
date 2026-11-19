---
title: UPI Collect
excerpt: Validate a VPA and collect a UPI payment from your checkout for MCC 6012 and 6211
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: UPI Collect — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Integrate UPI Collect on PayU Merchant Hosted Checkout. Validate the VPA, post pg=UPI and bankcode=UPI, and verify the callback. MCC 6012 and 6211 only.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">
  **NPCI.** UPI Collect is allowed only for MCC 6012 and 6211.

  Seamless form POST must move to `txn_s2s_flow` (UPI Intent S2S). See [UPI Intent S2S](https://docs.payu.in/docs/upi-intent-server-to-server). Android must implement Smart Intent. See [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow). iOS can use a deeplink and continue with UPI Collect. Web must show a QR of the Intent deeplink instead of UPI Collect.
</Callout>

# UPI Collect

UPI Collect posts `pg=UPI`, `bankcode=UPI`, and the customer's VPA in `vpa`. The customer approves the collect request in a UPI app.

## Validate the UPI Handle

Validate the VPA with the Validate VPA API before you start the payment. The command in the sample is `validateVPA`.

| Environment | URL in the sample |
| --- | --- |
| Test | `POST https://test.payu.in/merchant/postservice?form=2` |

<Accordion title="Request" icon="fa-code">

```bash
curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=YOUR_MERCHANT_KEY" \
  -d "command=validateVPA" \
  -d "var1=customer@upi" \
  -d "hash=$HASH"
```

The post-service hash on the API index is `sha512(key|command|var1|SALT)`.

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

Invalid VPA:

```json
{"status":"SUCCESS","vpa":"abc@upi","isVPAValid":0,"payerAccountName":"NA"}
```

</Accordion>

See [Validate VPA Handle](https://docs.payu.in/reference/validate_vpa_api).

## Post the Payment Request

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/_payment` |
| Production | `POST https://secure.payu.in/_payment` |

### Mandatory Parameters

<!-- VALIDATION NEEDED: The source table's furl example is https://example.com/success and the surl example is https://example.com/failure. The descriptions say furl is the failure URL and surl is the success URL. Examples below follow the descriptions, not the swapped example URLs. -->

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
| key | String | Merchant key provided by PayU. | JPg\*\*\*r |
| txnid | String | Transaction ID you generate. | ypl938459435 |
| amount | String | Payment amount. | 10.00 |
| productinfo | String | Short product description. | iPhone |
| firstname | String | Customer first name. | Ashish |
| email | String | Customer email. | abc@payu.in |
| phone | String | Customer phone. | 9988776655 |
| pg | String | Must be `UPI`. | UPI |
| bankcode | String | `UPI` for this Collect flow. | UPI |
| vpa | String | Customer VPA. See [UPI Handles](https://docs.payu.in/docs/upi-handles). | test123@okhdfcbank |
| surl | String | Success URL. PayU redirects here when the transaction succeeds. | https://example.com/success |
| furl | String | Failure URL. PayU redirects here when the transaction fails. | https://example.com/failure |
| hash | String | `SHA-512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|Salt)` | eabec285da28fd... |

### Optional Parameters

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
| address1 | String | Billing address line 1. The source says this helps fraud detection and chargebacks. | 123 Main Street |
| address2 | String | Billing address line 2. | Apt 4B |
| city | String | Billing city. | New Delhi |
| state | String | Billing state. | Delhi |
| country | String | Billing country. | India |
| zipcode | String | Billing postal code. The source says this is mandatory for cardless EMI. Character limit 20. | 110001 |
| udf1 | String | User-defined field. | Custom Data 1 |
| udf2 | String | User-defined field. | Custom Data 2 |
| udf3 | String | User-defined field. | Custom Data 3 |
| udf4 | String | User-defined field. | Custom Data 4 |
| udf5 | String | User-defined field. | Custom Data 5 |

<Accordion title="Understanding Hashing and sample code" icon="fa-shield-halved">
  <HashingRequestParameters />
  <HashingSample />
</Accordion>

<Accordion title="cURL" icon="fa-code">

```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&txnid=xdB9G7qYpfqszo&amount=10&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=UPI&bankcode=UPI&vpa=VPA-anything@payu&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb"
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
  <input type="hidden" name="pg" value="UPI" />
  <input type="hidden" name="bankcode" value="UPI" />
  <input type="hidden" name="vpa" value="test123@okhdfcbank" />
  <input type="hidden" name="surl" value="your own success url" />
  <input type="hidden" name="furl" value="your own failure url" />
  <input type="hidden" name="phone" value="9988776655" />
  <input type="hidden" name="hash" value="HASH_GENERATED_ON_SERVER" />
  <input type="submit" value="submit" />
</form>
```

</Accordion>

## When to Use UPI Intent Instead

The UPI Collect page tells web merchants to create a deeplink with [UPI Intent S2S](https://docs.payu.in/docs/upi-intent-server-to-server) and render that deeplink as a QR. Android merchants implement [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow). iOS can keep UPI Collect with a deeplink. Seamless form POST does not support Intent, so those merchants migrate to `txn_s2s_flow`.

<!-- DOCUMENTATION GAP: Intent request parameters are not in this folder. The overview says UPI Intent uses bankcode=INTENT and UPI QR uses bankcode=UPIDBQR. -->

The test page says UPI in-app and UPI Intent are not available in test mode.

## Handle the Callback

The reverse hash on this page is:

```
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

<Accordion title="Verify the response hash" icon="fa-shield-halved">
  <ReverseHashing />
</Accordion>

The success sample includes `mode=UPI`, `status=success`, `unmappedstatus=captured`, `PG_TYPE=UPI-PG`, `bankcode=UPI`, `error=E000`, and `error_Message=No Error`.

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
  The test page says the UPI in-app flow and the UPI Intent flow are not available in test mode.
</Callout>

## Related Resources

<Cards columns={2}>
  <Card title="UPI Handles" icon="fa-at" href="https://docs.payu.in/docs/upi-handles">
    Bank-name portion of a VPA.
  </Card>
  <Card title="UPI Intent S2S" icon="fa-qrcode" href="https://docs.payu.in/docs/upi-intent-server-to-server">
    Deeplink used for web QR and for the form-post migration.
  </Card>
  <Card title="Validate VPA" icon="fa-check" href="https://docs.payu.in/reference/validate_vpa_api">
    API reference for the pre-step.
  </Card>
  <Card title="Test Your Integration" icon="fa-flask" href="../test-integration">
    Test VPAs and the test-mode limit.
  </Card>
</Cards>
