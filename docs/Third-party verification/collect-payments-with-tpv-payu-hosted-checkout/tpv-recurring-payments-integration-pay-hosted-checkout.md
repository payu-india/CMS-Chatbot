---
title: Recurring Payments Integration
deprecated: false
hidden: true
metadata:
  title: TPV Recurring Payments Integration - PayU Hosted Checkout
  robots: index
---
PayU Hosted Checkout integration for **TPV (Third Party Verification) Payment Mode** supports both **Net Banking (NB)** and **Unified Payment Interface (UPI)** payment methods for subscription-based or autopay payments.

## Customer journey

The customer journey involves three key steps:

1. **Checkout Initiation**: Customer begins the payment process on the merchant's checkout page
2. **PayU Redirect**: Customer is redirected to PayU's hosted checkout page for payment completion
3. **Payment Processing**: Customer completes the payment using their preferred payment method (Net Banking or UPI)

## Environment

| Environment    | URL                               |
| -------------- | --------------------------------- |
| **Test**       | `https://test.payu.in/_payment`   |
| **Production** | `https://secure.payu.in/_payment` |

## Step 1: Create Transaction with Beneficiary and SI Details

Create a transaction request with the required beneficiary details and Standing Instruction (SI) parameters for autopay functionality.

## Step 2: Post Transaction Parameters

Submit the transaction parameters to PayU's payment gateway using the appropriate environment URL.

### Request parameters

<HTMLBlock>{`
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>key<br/><code>mandatory</code></td>
<td>String - Merchant key provided by PayU during onboarding</td>
<td>"JPg***r"</td>
</tr>
<tr>
<td>txnid<br/><code>mandatory</code></td>
<td>String - Unique transaction ID for each order</td>
<td>"ypl938459435"</td>
</tr>
<tr>
<td>amount<br/><code>mandatory</code></td>
<td>String - Transaction amount</td>
<td>"100"</td>
</tr>
<tr>
<td>productinfo<br/><code>mandatory</code></td>
<td>String - Product description</td>
<td>"Test Product"</td>
</tr>
<tr>
<td>firstname<br/><code>mandatory</code></td>
<td>String - Customer's first name</td>
<td>"John"</td>
</tr>
<tr>
<td>email<br/><code>mandatory</code></td>
<td>String - Customer's email address</td>
<td>"john@example.com"</td>
</tr>
<tr>
<td>phone<br/><code>mandatory</code></td>
<td>String - Customer's phone number</td>
<td>"9999999999"</td>
</tr>
<tr>
<td>beneficiarydetail<br/><code>mandatory</code></td>
<td>JSON Object - Account numbers and associated details for verification</td>
<td>See structure below</td>
</tr>
<tr>
<td>si_details<br/><code>mandatory</code></td>
<td>JSON Object - Standing instruction details for autopay</td>
<td>See structure below</td>
</tr>
<tr>
<td>free_trial<br/><code>optional</code></td>
<td>String - Parameter to setup free trial periods</td>
<td>"1"</td>
</tr>
<tr>
<td>surl<br/><code>mandatory</code></td>
<td>String - Success URL for transaction response</td>
<td>"https://www.yoursurl.com"</td>
</tr>
<tr>
<td>furl<br/><code>mandatory</code></td>
<td>String - Failure URL for transaction response</td>
<td>"https://www.yourfailureurl.com"</td>
</tr>
<tr>
<td>hash<br/><code>mandatory</code></td>
<td>String - SHA512 Hash for securing the transaction request</td>
<td>Generated using hash formula</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### Beneficiary Detail JSON Structure

```json
{
    "beneficiaryName": "John Doe",
    "beneficiaryAccountNumber": "002001600674|00000031957292212",
    "ifscCode": "KTKB0000046|KTKB0000023"
}
```

### Standing Instruction (SI) Details JSON Structure

```json
{
    "billingAmount": "100.00",
    "billingCurrency": "INR",
    "billingCycle": "monthly",
    "paymentStartDate": "2024-01-15",
    "paymentEndDate": "2025-01-15",
    "billingInterval": "1"
}
```

> 📘 Hash Calculation:
>
> Use the following hash logic for Recurring Payments integration and your must note that **beneficiarydetail**parameter value is included here:\
> sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|||||||beneficiarydetail|SALT)

### Sample request

```bash
curl --location 'https://test.payu.in/_payment' \
--data 'key=JPg***r&txnid=ypl938459435&amount=100&productinfo=Test Product&firstname=John&email=john@example.com&phone=9999999999&beneficiarydetail={"beneficiaryName":"John Doe","beneficiaryAccountNumber":"002001600674","ifscCode":"KTKB0000046"}&si_details={"billingAmount":"100.00","billingCurrency":"INR","billingCycle":"monthly"}&surl=https://www.yoursurl.com&furl=https://www.yourfailureurl.com&hash=generated_hash_value'
```

## Step 3: Handle and Validate Response

Process the response from PayU and perform reverse hash validation to ensure transaction authenticity.

> 📘 Response Hash Validation (Reverse Hash):
>
> The `beneficiarydetail` parameter is excluded during reverse hash calculation:
>
> **With UDFs:**
>
> ```
> sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
> ```
>
> **Without UDFs:**
>
> ```
> sha512(SALT|status|||||||||||email|firstname|productinfo|amount|txnid|key)
> ```
>
>

### Response parameters

| Parameter        | Description                                                          | Example                               |
| ---------------- | -------------------------------------------------------------------- | ------------------------------------- |
| `mihpayid`       | Unique reference number created for the transaction on PayU's system | `"99995401486671"`                    |
| `merchantid`     | Merchant's unique ID                                                 | `"12345"`                             |
| `txnid`          | Transaction ID provided in the request                               | `"ypl938459435"`                      |
| `status`         | Status of the transaction                                            | `"success"`, `"failure"`, `"pending"` |
| `amount`         | Transaction amount post adjustments                                  | `"100.00"`                            |
| `bankcode`       | Bank code used in the transaction                                    | `"SBITPV"`, `"UPITPV"`                |
| `error`          | Error code indicating issues with the transaction                    | `"E000"`                              |
| `error_Message`  | Description of any errors                                            | `"Transaction failed"`                |
| `payment_source` | Indicates the payment source                                         | `"payu"`                              |
| `hash`           | Hash provided in the response for validation                         | Generated hash string                 |

### Net Banking transaction

```php
Array(
    [mihpayid] => 99995401486671
    [status] => success
    [key] => travelibibo
    [txnid] => 4245248agh5519827ec
    [amount] => 100.00
    [bankcode] => SBITPV
    [hash] => e9272f99eace9f6e0a52c871cc0226ac...
    [payment_source] => payu
)
```

### UPI transaction

```php
Array(
    [mihpayid] => 99995401486672
    [status] => success
    [key] => merchant_key
    [txnid] => upi_txn_12345
    [amount] => 100.00
    [bankcode] => UPITPV
    [hash] => d8374b99face8e6e0b53d981dd0337bd...
    [payment_source] => payu
)
```

### Sample webhook response

**Net Banking webhook:**

```
mihpayid=99995401486671&mode=NB&status=success&key=merchant_key&txnid=4245248agh5519827ec&amount=100.00&hash=validation_hash
```

**UPI webhook:**

```
amount=100.00&PG_TYPE=UPI-COLLECT&payment_source=payu&bankcode=UPITPV&mihpayid=99995401486672&status=success&hash=validation_hash
```