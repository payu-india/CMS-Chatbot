---
title: Get Additional Charge Info API
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Get Additional Charge Info API** enables merchants to retrieve the applicable convenience fee for a payment transaction before the customer completes checkout. This API evaluates PayU pricing rules and returns the fee breakup (base amount, GST, and total) along with card BIN details, allowing merchants to display transparent pricing to customers.

## Use Cases

- Display convenience fees to customers during checkout
- Calculate total payable amount including additional charges
- Retrieve card BIN details (card type, issuing bank, domestic/international status)
- Pre-validate pricing for different payment modes (Credit Card, Debit Card, EMI, Net Banking, etc.)

---

## Endpoint

| Environment | URL |
|------------|-----|
| Test | `https://test.payu.in/merchant/postservice?form=2` |
| Production | `https://api.payu.in/merchant/postservice?form=2` |

**HTTP Method:** `POST`

**Content-Type:** `application/x-www-form-urlencoded`

---

## Sample Request

```bash
curl --location 'https://test.payu.in/merchant/postservice?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=smsplus' \
--data-urlencode 'command=get_additional_charge' \
--data-urlencode 'var1={"requestId":"abc1234","amount":10000,"category":"CC","bankCode":"CC","cardNo":"45678930013904","bin":"456789"}' \
--data-urlencode 'hash=c9c2440160a75303e1d272044dbfa5c1e5a13b225dcac11f69a9079491cf2660fd79f32e1e9c05c903ec1cc8ad0746b3989c20f922d32aab1dd124206ccdc5a1'
```

> **Note:** Replace `key`, `var1` payload values, and `hash` with your actual merchant credentials and computed hash before making the request.

---

## Request Parameters

<table>
  <thead>
    <tr>
      <th width="20%">Parameter</th>
      <th width="60%">Type &amp; Description</th>
      <th width="20%">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>key</code></td>
      <td>
        <strong>String</strong> (Mandatory)<br/>
        Merchant key provided by PayU during onboarding.
      </td>
      <td><code>smsplus</code></td>
    </tr>
    <tr>
      <td><code>command</code></td>
      <td>
        <strong>String</strong> (Mandatory)<br/>
        API command identifier. Must be set to <code>get_additional_charge</code>.
      </td>
      <td><code>get_additional_charge</code></td>
    </tr>
    <tr>
      <td><code>var1</code></td>
      <td>
        <strong>JSON String</strong> (Mandatory)<br/>
        JSON-encoded string containing the transaction details. See <strong>var1 Parameters</strong> below for structure.
      </td>
      <td><code>{"requestId":"abc1234","amount":10000,"category":"CC","bankCode":"CC","bin":"456789"}</code></td>
    </tr>
    <tr>
      <td><code>hash</code></td>
      <td>
        <strong>String</strong> (Mandatory)<br/>
        SHA-512 hash for request validation. Hash sequence:<br/>
        <code>key|command|var1|salt</code><br/>
        Compute on the server-side using your merchant salt.
      </td>
      <td><code>c9c2440160a75303...</code></td>
    </tr>
  </tbody>
</table>

### var1 Parameters

The `var1` parameter must be a JSON-encoded string containing the following fields:

<table>
  <thead>
    <tr>
      <th width="20%">Parameter</th>
      <th width="60%">Type &amp; Description</th>
      <th width="20%">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>requestId</code></td>
      <td>
        <strong>String</strong> (Mandatory)<br/>
        Unique UUID to identify this request. Use a unique identifier for each API call.
      </td>
      <td><code>abc1234</code></td>
    </tr>
    <tr>
      <td><code>amount</code></td>
      <td>
        <strong>Number</strong> (Mandatory)<br/>
        Transaction amount in paise (for INR). For example, ₹100.00 = 10000 paise.
      </td>
      <td><code>10000</code></td>
    </tr>
    <tr>
      <td><code>category</code></td>
      <td>
        <strong>String</strong> (Mandatory)<br/>
        Payment category/mode. Possible values:<br/>
        • <code>CC</code> — Credit Card<br/>
        • <code>DC</code> — Debit Card<br/>
        • <code>EMI</code> — EMI<br/>
        • <code>NB</code> — Net Banking<br/>
        • <code>UPI</code> — UPI<br/>
        • <code>CASH</code> — Cash Cards / Wallets
      </td>
      <td><code>CC</code></td>
    </tr>
    <tr>
      <td><code>bankCode</code></td>
      <td>
        <strong>String</strong> (Mandatory)<br/>
        Bank code or ibiboCode identifying the payment partner. Examples:<br/>
        • <code>CC</code> — Credit Card (any issuer)<br/>
        • <code>EMIIC3</code> — ICICI EMI<br/>
        • <code>AXIB</code> — Axis Bank Net Banking
      </td>
      <td><code>CC</code></td>
    </tr>
    <tr>
      <td><code>bin</code></td>
      <td>
        <strong>String</strong> (Conditional)<br/>
        Card BIN (first 6, 8, or 9 digits of the card number).<br/>
        <strong>Required</strong> for Credit Card (CC) or Debit Card (DC) transactions if <code>cardNo</code> is not provided.<br/>
        Ignored for non-card payment modes.
      </td>
      <td><code>456789</code></td>
    </tr>
    <tr>
      <td><code>cardNo</code></td>
      <td>
        <strong>String</strong> (Conditional)<br/>
        Full card number.<br/>
        <strong>Required</strong> for Credit Card (CC) or Debit Card (DC) transactions if <code>bin</code> is not provided.<br/>
        Ignored for non-card payment modes.
      </td>
      <td><code>45678930013904</code></td>
    </tr>
  </tbody>
</table>

<Info>
For **Credit Card** and **Debit Card** transactions, you must provide either `bin` or `cardNo`. For other payment modes (UPI, Net Banking, Wallets), the `bin` and `cardNo` parameters are ignored.
</Info>

---

## Sample Response

### Success Response

```json
{
  "status": 1,
  "details": {
    "requestId": "abc1234",
    "amount": 10000,
    "additionalChargeBase": 236,
    "additionalChargeGst": 42,
    "additionalChargeTotal": 278,
    "cardBinDetails": {
      "card_type": "CREDIT",
      "issuing_bank": "HDFC Bank",
      "is_domestic": true
    }
  }
}
```

### Error Response

```json
{
  "status": 0,
  "msg": "mandatory param requestId is missing",
  "errorCode": "MANDATORY_PARAMS_MISSING"
}
```

---

## Response Schema

### Success Response (status = 1)

<table>
  <thead>
    <tr>
      <th width="25%">Field</th>
      <th width="55%">Type &amp; Description</th>
      <th width="20%">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>status</code></td>
      <td>
        <strong>Integer</strong><br/>
        Response status. <code>1</code> indicates success.
      </td>
      <td><code>1</code></td>
    </tr>
    <tr>
      <td><code>details</code></td>
      <td>
        <strong>Object</strong><br/>
        Contains the convenience fee breakup and card details.
      </td>
      <td>See <strong>details</strong> object below</td>
    </tr>
  </tbody>
</table>

#### details Object

<table>
  <thead>
    <tr>
      <th width="30%">Field</th>
      <th width="50%">Type &amp; Description</th>
      <th width="20%">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>requestId</code></td>
      <td>
        <strong>String</strong><br/>
        The unique request identifier sent in the request.
      </td>
      <td><code>abc1234</code></td>
    </tr>
    <tr>
      <td><code>amount</code></td>
      <td>
        <strong>Number</strong><br/>
        Original transaction amount (in paise).
      </td>
      <td><code>10000</code></td>
    </tr>
    <tr>
      <td><code>additionalChargeBase</code></td>
      <td>
        <strong>Number</strong><br/>
        Base convenience fee amount (in paise), before GST.
      </td>
      <td><code>236</code></td>
    </tr>
    <tr>
      <td><code>additionalChargeGst</code></td>
      <td>
        <strong>Number</strong><br/>
        GST applied on the convenience fee (in paise).
      </td>
      <td><code>42</code></td>
    </tr>
    <tr>
      <td><code>additionalChargeTotal</code></td>
      <td>
        <strong>Number</strong><br/>
        Total convenience fee including GST (in paise).<br/>
        <code>additionalChargeTotal = additionalChargeBase + additionalChargeGst</code>
      </td>
      <td><code>278</code></td>
    </tr>
    <tr>
      <td><code>cardBinDetails</code></td>
      <td>
        <strong>Object | null</strong><br/>
        Card BIN information. Returns <code>null</code> for non-card payment modes or if BIN lookup fails.
      </td>
      <td>See <strong>cardBinDetails</strong> object below</td>
    </tr>
  </tbody>
</table>

#### cardBinDetails Object

<table>
  <thead>
    <tr>
      <th width="30%">Field</th>
      <th width="50%">Type &amp; Description</th>
      <th width="20%">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>card_type</code></td>
      <td>
        <strong>String</strong><br/>
        Type of card. Values: <code>CREDIT</code>, <code>DEBIT</code>
      </td>
      <td><code>CREDIT</code></td>
    </tr>
    <tr>
      <td><code>issuing_bank</code></td>
      <td>
        <strong>String</strong><br/>
        Name of the card issuing bank.
      </td>
      <td><code>HDFC Bank</code></td>
    </tr>
    <tr>
      <td><code>is_domestic</code></td>
      <td>
        <strong>Boolean</strong><br/>
        Indicates whether the card is domestic (<code>true</code>) or international (<code>false</code>).
      </td>
      <td><code>true</code></td>
    </tr>
  </tbody>
</table>

---

### Error Response (status = 0)

<table>
  <thead>
    <tr>
      <th width="25%">Field</th>
      <th width="55%">Type &amp; Description</th>
      <th width="20%">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>status</code></td>
      <td>
        <strong>Integer</strong><br/>
        Response status. <code>0</code> indicates an error.
      </td>
      <td><code>0</code></td>
    </tr>
    <tr>
      <td><code>msg</code></td>
      <td>
        <strong>String</strong><br/>
        Human-readable error message describing what went wrong.
      </td>
      <td><code>mandatory param requestId is missing</code></td>
    </tr>
    <tr>
      <td><code>errorCode</code></td>
      <td>
        <strong>String</strong><br/>
        Machine-readable error code for programmatic handling.
      </td>
      <td><code>MANDATORY_PARAMS_MISSING</code></td>
    </tr>
  </tbody>
</table>

---

## Error Codes

<table>
  <thead>
    <tr>
      <th width="35%">Error Code</th>
      <th width="45%">Error Message</th>
      <th width="20%">Cause</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>MANDATORY_PARAMS_MISSING</code></td>
      <td>
        • <code>mandatory param requestId is missing</code><br/>
        • <code>mandatory param amount is missing</code><br/>
        • <code>mandatory param category is missing</code><br/>
        • <code>mandatory param bankCode is missing</code><br/>
        • <code>Either of bin or cardNo should be non null for CC</code>
      </td>
      <td>One or more required parameters are missing from the request.</td>
    </tr>
    <tr>
      <td><code>INVALID_BIN</code></td>
      <td><code>invalid bin</code></td>
      <td>The provided BIN is not valid (must be 6, 8, or 9 digits).</td>
    </tr>
    <tr>
      <td><code>INVALID_CARDNO</code></td>
      <td><code>invalid card number</code></td>
      <td>The provided card number is not valid or does not pass Luhn check.</td>
    </tr>
    <tr>
      <td><code>INVALID_CATEGORY_BANKCODE_MAPPING</code></td>
      <td><code>bank code should be mapped to correct category</code></td>
      <td>The <code>bankCode</code> does not match the provided <code>category</code>. For example, using a Net Banking bank code with category <code>CC</code>.</td>
    </tr>
    <tr>
      <td><code>INVALID_BIN_CATEGORY_MAPPING</code></td>
      <td><code>Respective Bin belongs to creditcard</code></td>
      <td>The BIN belongs to a different card type than the specified <code>category</code>. For example, using a credit card BIN with category <code>DC</code>.</td>
    </tr>
  </tbody>
</table>

---

## Hash Generation

The `hash` parameter ensures request integrity and authenticity. It must be computed on the **server-side** using SHA-512.

### Hash Sequence

```
key|command|var1|salt
```

### Example Hash Calculation (PHP)

```php
<?php
$key = "smsplus";
$command = "get_additional_charge";
$var1 = '{"requestId":"abc1234","amount":10000,"category":"CC","bankCode":"CC","bin":"456789"}';
$salt = "your_merchant_salt";

$hashString = $key . '|' . $command . '|' . $var1 . '|' . $salt;
$hash = strtolower(hash('sha512', $hashString));

echo $hash;
?>
```

### Example Hash Calculation (Python)

```python
import hashlib

key = "smsplus"
command = "get_additional_charge"
var1 = '{"requestId":"abc1234","amount":10000,"category":"CC","bankCode":"CC","bin":"456789"}'
salt = "your_merchant_salt"

hash_string = f"{key}|{command}|{var1}|{salt}"
hash_value = hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()

print(hash_value)
```

<Warning>
**Security Best Practice:** Always compute the hash on your server. Never expose your merchant salt to client-side code or share it in version control systems.
</Warning>

---

## Integration Notes

1. **Amount Format:** All monetary values (`amount`, `additionalChargeBase`, `additionalChargeGst`, `additionalChargeTotal`) are in **paise** for INR. Divide by 100 to get the rupee value.

2. **Display to Customer:** Use the `additionalChargeTotal` to show the total convenience fee to customers during checkout. Example:
   ```
   Order Amount: ₹100.00
   Convenience Fee: ₹2.78
   Total Payable: ₹102.78
   ```

3. **Card Details:** The `cardBinDetails` object is useful for:
   - Displaying card issuer to the customer
   - Applying different pricing for domestic vs. international cards
   - Validation and fraud prevention

4. **Error Handling:** Always check the `status` field first. If `status = 0`, parse the `errorCode` for programmatic handling and display the `msg` to help debug the issue.

5. **Request Uniqueness:** Use a unique `requestId` (UUID recommended) for each API call to ensure idempotency and aid in troubleshooting.

---

## Testing

Use the test environment URL with your test merchant credentials:

- **Test URL:** `https://test.payu.in/merchant/postservice?form=2`
- **Test Card BINs:** Use standard test card numbers provided by PayU to simulate different scenarios

### Test Scenarios to Validate

| Scenario | Test Case |
|----------|-----------|
| ✅ Valid Credit Card | Provide valid `bin` or `cardNo` with `category=CC` and `bankCode=CC` |
| ✅ Valid Debit Card | Provide valid `bin` or `cardNo` with `category=DC` and appropriate `bankCode` |
| ✅ Net Banking | Provide `category=NB` with appropriate `bankCode` (omit `bin` and `cardNo`) |
| ✅ UPI | Provide `category=UPI` with appropriate `bankCode` |
| ❌ Missing Mandatory Param | Omit `requestId`, `amount`, `category`, or `bankCode` to test error handling |
| ❌ Invalid BIN | Provide invalid BIN (e.g., 5 digits or alphabetic characters) |
| ❌ Wrong Category-BankCode | Use Net Banking `bankCode` with `category=CC` |

---

## Support

For technical assistance or questions about this API:
- **Merchant Dashboard:** [https://merchant.payu.in](https://merchant.payu.in)
- **Integration Support:** integration@payu.in
- **Developer Documentation:** [https://docs.payu.in](https://docs.payu.in)
