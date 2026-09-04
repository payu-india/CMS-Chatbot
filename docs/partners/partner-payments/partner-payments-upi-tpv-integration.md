---
title: Partner Payments UPI TPV Integration
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
UPI TPV (Third-Party Validation) enables partners to validate beneficiary account details during payment initiation. This is particularly useful for compliance scenarios where beneficiary verification is required before payment processing.

When you initiate a UPI TPV payment through the Partner Payments API, PayU automatically:

- Sets `bankcode=INTTPV` internally
- Sets `api_version=6` for TPV processing
- Validates the beneficiary account details against the customer's UPI account
- Ensures funds are transferred only if validation succeeds

## Prerequisites

Before integrating UPI TPV, ensure you have:

<Note>
✅ Completed the standard [Partner Payments Integration](doc:partner-payments-integration-guide)  
✅ Generated OAuth access token with `partner_payments` scope  
✅ Beneficiary account details (IFSC code, account number, account holder name)  
✅ UPI S2S integration enabled (requires `txn_s2s_flow=4`)
</Note>

***

## Step 1: Prepare Beneficiary Details

Construct the `beneficiarydetail` parameter as a JSON string containing the beneficiary's bank account information.

### Beneficiary Detail Schema

> **⚠️ Info Gap:** The exact schema for `beneficiarydetail` should be confirmed with the PayU integration team. The following structure is based on available documentation:

```json
{
  "ifscCode": "ICIC0001234",
  "accountNumber": "123456789012",
  "accountHolderName": "Test User"
}
```

**Field Descriptions:**

| Field               | Type   | Description                                | Example      |
| ------------------- | ------ | ------------------------------------------ | ------------ |
| `ifscCode`          | string | 11-character IFSC code of beneficiary bank | ICIC0001234  |
| `accountNumber`     | string | Beneficiary account number                 | 123456789012 |
| `accountHolderName` | string | Name as per bank account                   | Test User    |

### JSON String Conversion

Convert the JSON object to a **string** before including it in the payment request:

**Java Example:**

```java
import com.fasterxml.jackson.databind.ObjectMapper;

ObjectMapper mapper = new ObjectMapper();
Map<String, String> beneficiary = new HashMap<>();
beneficiary.put("ifscCode", "ICIC0001234");
beneficiary.put("accountNumber", "123456789012");
beneficiary.put("accountHolderName", "Test User");

String beneficiarydetail = mapper.writeValueAsString(beneficiary);
// Result: {"ifscCode":"ICIC0001234","accountNumber":"123456789012","accountHolderName":"Test User"}
```

**Python Example:**

```python
import json

beneficiary = {
    "ifscCode": "ICIC0001234",
    "accountNumber": "123456789012",
    "accountHolderName": "Test User"
}

beneficiarydetail = json.dumps(beneficiary)
# Result: '{"ifscCode": "ICIC0001234", "accountNumber": "123456789012", "accountHolderName": "Test User"}'
```

***

## Step 2: Initiate TPV Payment

Include the `beneficiarydetail` parameter in your Partner Payments API request along with the mandatory UPI S2S fields.

### Required Parameters for UPI TPV

<table>
<thead>
<tr>
<th align="left">Parameter</th>
<th align="left">Type &amp; Description</th>
<th align="left">Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>txnid</code></td>
<td>string — Unique transaction ID</td>
<td>28471834809170982</td>
</tr>
<tr>
<td><code>amount</code></td>
<td>string — Transaction amount</td>
<td>518.02</td>
</tr>
<tr>
<td><code>productinfo</code></td>
<td>string — Product description</td>
<td>TPV Payment</td>
</tr>
<tr>
<td><code>phone</code></td>
<td>string — Customer phone number</td>
<td>919820988398</td>
</tr>
<tr>
<td><code>merchant_id</code></td>
<td>integer — PayU merchant ID</td>
<td>8739528</td>
</tr>
<tr>
<td><code>reseller_id</code></td>
<td>string — Partner UUID</td>
<td>11ee-0e7e-5403fde2-9523-0a696b110fde</td>
</tr>
<tr>
<td><code>txn_s2s_flow</code></td>
<td>string — Must be "4" for UPI Intent S2S</td>
<td>4</td>
</tr>
<tr>
<td><code>s2s_client_ip</code></td>
<td>string — Customer IP address</td>
<td>157.240.22.9</td>
</tr>
<tr>
<td><code>s2s_device_info</code></td>
<td>string — Device user-agent</td>
<td>Mozilla/5.0 (iPhone)...</td>
</tr>
<tr>
<td><code>beneficiarydetail</code></td>
<td>string — JSON string with beneficiary details</td>
<td>{"ifscCode":"ICIC0001234",...}</td>
</tr>
<tr>
<td><code>hash</code></td>
<td>string — SHA-512 payment request hash</td>
<td>(computed hash)</td>
</tr>
</tbody>
</table>

### Hash Generation for TPV

Use the same payment request hash formula as standard partner payments:

```
merchant_id|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||client_secret
```

<Info>
**Note:** The `beneficiarydetail` field is **not included** in the hash formula. Only the standard payment fields are used for hash computation.
</Info>

### Sample TPV Payment Request

**Endpoint:** `POST /partner/payments`

**Environment URLs:**

| Environment | URL                                                              |
| ----------- | ---------------------------------------------------------------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer/partner/payments` |
| Production  | `https://api.payu.in/partner/payments`                           |

**Request:**

```bash
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/payments' \
--header 'Authorization: Bearer 039e0d1d70f467f946e2d73bd43868df856cfaa352ea54591a76bfc4a08d3487' \
--header 'Content-Type: application/json' \
--data '{
  "txnid": "28471834809170982",
  "amount": "518.02",
  "productinfo": "TPV Payment",
  "firstname": "",
  "email": "",
  "phone": "919820988398",
  "merchant_id": 8739528,
  "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
  "udf1": "",
  "udf2": "1370625260",
  "udf3": "r-hway-TPV-REFERENCE",
  "udf4": "",
  "udf5": "whatsapp",
  "txn_s2s_flow": "4",
  "s2s_client_ip": "157.240.22.9",
  "s2s_device_info": "Mozilla/5.0 (iPhone) AppleWebKit/602.4.6",
  "beneficiarydetail": "{\"ifscCode\":\"ICIC0001234\",\"accountNumber\":\"123456789012\",\"accountHolderName\":\"Test User\"}",
  "hash": "COMPUTED_HASH_VALUE_HERE"
}'
```

> **Note:** In the cURL example above, the JSON string `beneficiarydetail` has escaped quotes (`\"`) to be valid within the outer JSON payload.

***

## Step 3: Handle TPV Response

The response structure for UPI TPV is identical to standard UPI Intent S2S responses.

### Sample TPV Response

```json
{
  "metaData": {
    "message": null,
    "referenceId": "7a3060b7462bd2ce6d025c9997220e01",
    "statusCode": null,
    "txnId": "28471834809170982",
    "txnStatus": "pending",
    "unmappedStatus": "pending"
  },
  "result": {
    "paymentId": "30478359672",
    "merchantName": "HathwayCableAndDatacomLimited",
    "merchantVpa": "hathway.payu@indus",
    "amount": "518.02",
    "intentURIData": "pa=hathway.payu@indus&pn=HATHWAY...&tr=30478359672&tid=PPPL304...&am=518.02&cu=INR&tn=UPIIntent",
    "acsTemplate": "PGh0bWw+PGhlYWQ+...",
    "otpPostUrl": "https://secure.payu.in/ResponseHandler.php"
  }
}
```

**Processing Steps:**

1. Extract `result.intentURIData` and `result.acsTemplate`
2. Render UPI intent link or QR code for the customer
3. Customer selects UPI app and completes authentication
4. PayU validates beneficiary details during payment processing
5. If validation fails, payment is declined automatically

<Warning>
**TPV Validation:** The beneficiary account number entered by the customer in their UPI app must match the `accountNumber` provided in `beneficiarydetail`. If there's a mismatch, the transaction will be rejected.
</Warning>

***

## Step 4: Verify TPV Transaction

Use the same verification process as standard partner payments:

1. Receive webhook payload with payment status
2. Verify webhook hash using reverse hash formula
3. Call `/partner/verifyPayment` API to confirm final status

**Webhook Indicators for TPV:**

- `mode`: "UPI"
- `bankcode`: "INTTPV" (automatically set by PayU for TPV transactions)

### Sample Verify Payment Request for TPV

```bash
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment' \
--header 'Authorization: Bearer 039e0d1d70f467f946e2d73bd43868df856cfaa352ea54591a76bfc4a08d3487' \
--header 'Content-Type: application/json' \
--data '{
  "txnid": "28471834809170982",
  "merchant_id": 8739528,
  "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
  "hash": "COMPUTED_VERIFY_HASH"
}'
```

***

## Alternative: Using encrypted_data

Instead of `beneficiarydetail`, you can optionally send encrypted beneficiary details using the `encrypted_data` parameter.

> **⚠️ Info Gap:** The encryption method, key management, and exact format for `encrypted_data` should be confirmed with the PayU integration team.

**Sample Request with encrypted_data:**

```json
{
  "txnid": "28471834809170982",
  "amount": "518.02",
  "productinfo": "TPV Payment",
  "phone": "919820988398",
  "merchant_id": 8739528,
  "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
  "txn_s2s_flow": "4",
  "s2s_client_ip": "157.240.22.9",
  "s2s_device_info": "Mozilla/5.0 (iPhone)...",
  "encrypted_data": "BASE64_ENCRYPTED_STRING_HERE",
  "hash": "COMPUTED_HASH_VALUE"
}
```

***

## Testing UPI TPV

### Test Beneficiary Details

Use the following test data for UAT/sandbox testing:

> **⚠️ Info Gap:** Test IFSC codes, account numbers, and account holder names for UAT should be provided by PayU. Consult your integration team for valid test data.

**Sample Test Data (to be confirmed):**

```json
{
  "ifscCode": "ICIC0001234",
  "accountNumber": "123456789012",
  "accountHolderName": "Test User"
}
```

### Expected Behavior

**Success Scenario:**

1. Customer initiates payment with matching account details
2. PayU validates beneficiary account
3. Payment proceeds to UPI authorization
4. Customer completes payment in UPI app
5. Webhook delivered with `status: "success"` and `bankcode: "INTTPV"`

**Failure Scenario:**

1. Customer initiates payment with mismatched account details
2. PayU detects validation failure
3. Payment is declined before UPI authorization
4. Webhook delivered with `status: "failure"` and appropriate error code

***

## Common TPV Errors

| Error                            | Cause                                                     | Resolution                                       |
| -------------------------------- | --------------------------------------------------------- | ------------------------------------------------ |
| Invalid beneficiarydetail format | JSON string is malformed or contains invalid characters   | Validate JSON structure before stringifying      |
| Beneficiary account mismatch     | Account number in UPI app doesn't match beneficiarydetail | Ensure customer uses correct account in UPI app  |
| IFSC code invalid                | Provided IFSC code doesn't exist or is incorrect          | Validate IFSC code against RBI master list       |
| Missing TPV fields               | beneficiarydetail or encrypted_data not provided          | Include at least one of these parameters for TPV |

***

## Next Steps

- [Partner Payments Integration Guide](doc:partner-payments-integration-guide) — Main integration flow
- [Testing and Troubleshooting](doc:testing-and-troubleshooting-partner-payments) — Error resolution guide
- [API Reference: POST /partner/payments](ref:partner-payments-api) — Complete API specification

<Success>
**UPI TPV Integration Complete!** You can now process payments with beneficiary validation for enhanced security and compliance.
</Success>
