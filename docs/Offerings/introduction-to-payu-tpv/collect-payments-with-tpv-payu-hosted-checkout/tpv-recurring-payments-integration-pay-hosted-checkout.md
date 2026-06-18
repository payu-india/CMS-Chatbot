---
title: Subscription TPV Integration
deprecated: false
hidden: false
metadata:
  title: Subscription TPV Integration - PayU Hosted
  description: This section describes how to integrate the subscription request with TPV.
  keywords:
    - Subscription TPV Integration
    - TPV Subscription Integration
    - TPV Recurring Payments Integration
    - Recurring Payments TPV Integration
  robots: index
---
PayU Hosted Checkout integration for **TPV (Third Party Verification) Payment Mode** supports both **Net Banking (NB)** and **Unified Payment Interface (UPI)** payment methods for subscription-based or autopay payments.

**Steps to integrate**

<Cards columns={3}>
  <Card title="1. Create Transaction" href="#step-1-create-transaction-with-beneficiary-and-si-details">
    Create transaction with beneficiary and SI details for autopay

    <br />
  </Card>

  <Card title="2. Post Parameters" href="#step-2-post-transaction-parameters">
    Post transaction parameters to PayU payment gateway

    <br />
  </Card>

  <Card title="3. Handle Response" href="#step-3-handle-and-validate-response">
    Handle and validate response with reverse hash
  </Card>
</Cards>

## Customer journey

The customer journey involves three key steps:

1. **Checkout Initiation**: Customer begins the payment process on the merchant's checkout page


<Image src="https://files.readme.io/8ba8dec2112adc3f7050be48a91a43cec39eb6256de01c1a4c1cca3c1d36f5e5-tpv_si_step1.png" align="center" border={true} />


2. **PayU Redirect**: Customer is redirected to PayU's hosted checkout page for payment completion


<Image src="https://files.readme.io/d2ac062dd599380f3d3a78e0158436c08750f4c13ea7be50326eba3d6e5a1994-tpv_si_step2.png" align="center" border={true} />


3. **Payment Processing**: Customer completes the payment using their preferred payment method (Net Banking or UPI)


<Image src="https://files.readme.io/a3c1a3190a1aff209b493e606bef503a5f71f58d7647e77aa9ca9cbb429996e8-tpv_si_step3.png" align="center" border={true} />


## Step 1: Create Transaction with Beneficiary and SI Details

Create a transaction request with the required beneficiary details and Standing Instruction (SI) parameters for autopay functionality.

## Step 2: Post Transaction Parameters

Submit the transaction parameters to PayU's payment gateway using the appropriate environment URL.

**Environment**

| Environment    | URL                               |
| -------------- | --------------------------------- |
| **Test**       | `https://test.payu.in/_payment`   |
| **Production** | `https://secure.payu.in/_payment` |

<Accordion title="Request parameters" icon="fa-code">
| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `key` *mandatory* | `String` Merchant key provided by PayU during onboarding | `JPg***r` |
| `txnid` *mandatory* | `String` Unique transaction ID for each order | `ypl938459435` |
| `amount` *mandatory* | `String` Transaction amount | `100` |
| `productinfo` *mandatory* | `String` Product description | `Test Product` |
| `firstname` *mandatory* | `String` Customer's first name | `John` |
| `email` *mandatory* | `String` Customer's email address | `john@example.com` |
| `phone` *mandatory* | `String` Customer's phone number | `9999999999` |
| `api_version` *mandatory* | `String` Version of the API | `7` |
| `beneficiarydetail` *mandatory* | `JSON Object` Account numbers and associated details for verification | See structure below |
| `si_details` *mandatory* | `JSON Object` Standing instruction details for autopay | See structure below |
| `free_trial` *optional* | `String` Parameter to set up free trial periods | `1` |
| `surl` *mandatory* | `String` Success URL for transaction response | `https://www.yoursurl.com` |
| `furl` *mandatory* | `String` Failure URL for transaction response | `https://www.yourfailureurl.com` |
| `hash` *mandatory* | `String` SHA512 hash for securing the transaction request. For more information, refer to [Hash calculation](#hash-calcuation). | Generated using hash formula |

  <Accordion title="Hash calculation" icon="fa-code">
    If UDF parameters are defined in the hash calculation, the same UDF fields must be included in the request sent to PayU.

    `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5| |||||beneficiarydetail|SALT)`

    WithOut UDF Parameters.

    `sha512(key|txnid|amount|productinfo|firstname|email|||||||||||beneficiarydetail|SAL T)`

    Replace SALT with the salt value provided during onboarding.
  </Accordion>
</Accordion>

<Accordion title="Beneficiary Detail JSON Structure" icon="fa-code">
  ```json
  {"beneficiaryName": "Sachin Tendulkar|Nitin Jaisingh|Somya|Nikita","beneficiaryAccountNumber": "1211450021|002001600674|1234673939|87669286932","beneficiaryAccountType": "SAVINGS|SAVINGS|CURRENT|CURRENT","beneficiaryIfscCode": "ICIC0000046|HDFC0000726|ICIC0000046|SBIN0098292","verificationMode": "DEBIT_CARD|NET_BANKING| |AADHAR"} 
  ```

  <HTMLBlock>{`
    <table>
        <thead>
            <tr>
                <th>Field</th>
                <th>Description</th>
                <th>Example</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>beneficiaryName</td>
                <td>String List of Beneficiary name separated by pipe symbol (|).<br>Maximum 4 names.</td>
                <td>"Sachin Tendulkar|Nitin Jaisingh|<br/>Somya|Nikita"</td>
            </tr>
            <tr>
                <td>beneficiaryAccountNumber</td>
                <td>String List of account numbers separated by pipe symbol (|).<br>Maximum 4 accounts.</td>
                <td>"002001600674|<br/>00000031957292212|<br/>00000035955239352|<br/>00000035955239352"</td>
            </tr>
            <tr>
                <td>beneficiaryAccountType</td>
                <td>String List of corresponding account type separated by pipe symbol (|). Maximum 4 types in the same order as account numbers.</td>
                <td>"SAVINGS|SAVINGS|<br/>CURRENT|CURRENT"</td>
            </tr>
            <tr>
                <td>ifscCode</td>
                <td>String List of corresponding IFSC codes separated by pipe symbol (|). Maximum 4 IFSC codes in the same order as account numbers.</td>
                <td>"ICIC0000046|<br/>HDFC0000726|<br/>ICIC0000046|<br/>SBIN0098292"</td>
            </tr>
            <tr>
                <td>verificationMode</td>
                <td>String List of verification mode separated by pipe symbol (|). Maximum 4 modes in the same order as account numbers.</td>
                <td>"DEBIT_CARD|NET_BANKING<br/>| |AADHAR"</td>
            </tr>
        </tbody>
    </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Standing Instruction (SI) Details JSON Structure" icon="fa-code">
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
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl --location 'https://test.payu.in/_payment' --data 'key=JPg***r&txnid=ypl938459435&amount=100&productinfo=Test Product&firstname=John&email=john@example.com&phone=9999999999&beneficiarydetail={"beneficiaryName":"John Doe","beneficiaryAccountNumber":"002001600674","ifscCode":"KTKB0000046"}&si_details={"billingAmount":"100.00","billingCurrency":"INR","billingCycle":"monthly"}&surl=https://www.yoursurl.com&furl=https://www.yourfailureurl.com&hash=generated_hash_value'
  ```
</Accordion>

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

<Accordion title="Response parameters" icon="fa-code">
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
</Accordion>

<Accordion title="Net Banking transaction" icon="fa-code">
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
</Accordion>

<Accordion title="UPI transaction" icon="fa-code">
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
</Accordion>

<Accordion title="Sample webhook response" icon="fa-code">
  **Net Banking webhook:**

  ```
  mihpayid=99995401486671&mode=NB&status=success&key=merchant_key&txnid=4245248agh5519827ec&amount=100.00&hash=validation_hash
  ```

  **UPI webhook:**

  ```
  amount=100.00&PG_TYPE=UPI-COLLECT&payment_source=payu&bankcode=UPITPV&mihpayid=99995401486672&status=success&hash=validation_hash
  ```

  <br />
</Accordion>

<br />
