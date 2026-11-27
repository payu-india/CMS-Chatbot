---
title: Pre-Auth PayU Hosted Checkout Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
In PayU Hosted Checkout, PayU collects payment details, processes 3DS authentication, and manages PCI-DSS compliance. You initiate the transaction with `pre_authorize=1`, and PayU holds the customer's funds without capturing them immediately.

***

## Integration Workflow

```text
[Step 1: Initiate Pre-Auth] ➔ POST _payment with pre_authorize=1
[Step 2: Customer Authenticates] ➔ Customer completes 3DS/OTP on PayU Hosted page
[Step 3: Handle Callback] ➔ Verify reverse hash and unmappedstatus == "auth"
[Step 4: Capture or Cancel] ➔ Settle funds via capture_transaction or release via cancel_transaction
```

***

## Step 1: Post the Pre-Auth Transaction Request

Submit the transaction details as an HTML form post or HTTP POST to PayU's `_payment` endpoint.

### Environment

| Environment        | URL                                                                                                   |
| :----------------- | :---------------------------------------------------------------------------------------------------- |
| **Test (Sandbox)** | [https://test.payu.in/\_payment](https://test.payu.in/_payment)                                       |
| **Production**     | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment "https://secure.payu.in/_payment") |

### Hash Calculation Formula

Generate the SHA-512 request hash on your secure backend server:

```text
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
```

<Tabs>
  <Tab title="Request Parameters">
    **Mandatory Parameters**

    | Parameter                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Example                                                            |
    | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
    | <Glossary>key</Glossary><br /><code>mandatory</code>                                      | <code>varchar</code> This parameter is the unique Merchant Key provided by PayU for your merchant account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Your Test Key                                                      |
    | <Glossary>txnid</Glossary><br /><code>mandatory</code>                                    | <code>varchar</code> This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction. <code>Character limit</code>: 25<br />**Note**: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID.' | fd3e847h2                                                          |
    | amount<br /><code>mandatory</code>                                                        | <code>float</code> This parameter should contain the payment amount of the particular transaction. **Note**: Type-cast the amount to float type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 1000                                                               |
    | <Glossary>productinfo</Glossary><br /><code>mandatory</code>                              | <code>varchar</code> This parameter should contain a brief product description. It should be a string describing the product. <code>Character limit</code>: 100.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Time Magazine Subscription                                         |
    | firstname<br /><code>mandatory</code>                                                     | <code>varchar</code> Must contain the first name of the customer. <code>Character limit</code>: 60.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Ashish                                                             |
    | email<br /><code>mandatory</code>                                                         | <code>varchar</code> Must contain the email of the customer. This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information. Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions. Character limit: 50.                                                                                                                                                                                                                                                                                           | [Ashish@test.com](mailto:Ashish@test.com)                          |
    | phone<br /><code>mandatory</code>                                                         | <code>varchar</code> Must contain the phone number of the customer. This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is required to provide the correct information. Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions. Character limit: 50.                                                                                                                                                                                                                                                                                  | 9843176540                                                         |
    | <Glossary>surl</Glossary><br /><code>mandatory</code>                                     | surl is the acronym for Success URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is successful.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                    |
    | <Glossary>furl</Glossary><br /><code>mandatory</code>                                     | furl is the acronym for Failure URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is failed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                    |
    | <Glossary>pg</Glossary><br /><code>mandatory</code>                                       | It defines the payment category for which you wish to perform UPI One-Time Mandate. For UPI, **pg= UPI**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | UPI                                                                |
    | <Glossary>bankcode</Glossary><br /><code>mandatory</code>                                 | It defines the bank with which you wish to perform UPI using the bank code. Use **UPI** or **INTENT** according to the use case.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | **UPI**: Used for UPI Collect<br />**INTENT**: Used for UPI Intent |
    | <Glossary>vpa</Glossary><br /><code>mandatory for <Glossary>UPI</Glossary> Collect</code> | This parameter contains the customer's VPA handle. For the list of UPI handles supported, refer to UPI Handles. The merchant is advised to check the validity of the VPA through using the VPA Validation API. PayU extends support for the same if required. For more information on using VPA Validation API, refer to Validate VPA API.                                                                                                                                                                                                                                                                                                                                   | abc\@payu                                                          |
    | pre_authorize<br /><code>mandatory for Pre-Auth</code>                                    | This parameter is set to **1** to pre-authorize payment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                    |
    | <Glossary>hash</Glossary><br /><code>mandatory</code>                                     | Hash is a crucial parameter used to ensure that any data is not tampered while redirecting the customer from the merchant website to PayU's payment interface during registration transactions. It is a SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si_details by merchant salt. The formula used to calculate this hash is: <code>SHA512(sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|SALT))</code>                                                                                                                                                    | txnid                                                              |
  </Tab>

  <Tab title="Sample Request">
    ```bash
    curl --request POST   
    --url https://test.payu.in/_payment   
    --header 'accept: text/plain'   
    --header 'content-type: application/x-www-form-urlencoded'   
    --data key=JPM7Fg   
    --data txnid=aso6787   
    --data siDetails='{"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"}'   
    --data pre_authorize=1   
    --data amount=100.00   
    --data productinfo=iPhone   
    --data firstname=Ashish   
    --data email=ashish@abc.com   
    --data phone=9876543210   
    --data surl=https://apiplayground-response.herokuapp.com/   
    --data furl=https://apiplayground-response.herokuapp.com/   
    --data hash=8e8de8a3cf2ba999e16c0ffdb63a645074af4ad1aa0a8d66d81555a119c004e1791173fe6199084f256623664b250d3aeb50fc2c4cfc155e729d8811a157c98b
    ```
  </Tab>
</Tabs>

## Step 2: Handle the Response from PayU

Upon successful authorization, PayU redirects the customer and posts transaction data to your `surl`.

### Reverse Hash Verification Formula

Verify that the callback has not been tampered with:

```text
sha512(SALT|status|udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

### Key Response Parameters to Inspect

* `status`: Must equal `"success"`.
* `unmappedstatus`: Must equal `"auth"` (indicates funds are held, not captured).
* `mihpayid`: Unique PayU transaction ID. Store this value to execute capture or cancellation.

#### Sample Callback Payload

```text
mihpayid: 403993715523615328
mode: CC
status: success
unmappedstatus: auth
key: JPM7Fg
txnid: ORD_20261120_001
amount: 1000.00
net_amount_debit: 1000.00
productinfo: Hotel_Booking
firstname: Ashish
email: ashish@example.com
phone: 9876543210
bank_ref_num: 7f0d5ada-59bb-41d7-9e41-20a6af2406c9
bankcode: CC
PG_TYPE: CC-PG
hash: afeab9dcf4e43d47f8fbf5a6838d393c70694a58e30ada08e6cb86ac943236c0...
error: E000
error_Message: No Error
```

***

## Step 3: Capture the Pre-Authorized Payment

To capture and settle all or part of the held funds, call the `capture_transaction` API command.

### Endpoints

| Environment    | URL              |
| :------------- | :--------------- |
| **Test**       | `<redacted URL>` |
| **Production** | `<redacted URL>` |

### Hash Formula

```text
sha512(key|command|var1|salt)
```

_(Where&#x20;_`var1`_&#x20;is the&#x20;_`mihpayid`_)._

### Capture Parameters

#### Mandatory Parameters

| Parameter | Type   | Description                                                  | Example               |
| :-------- | :----- | :----------------------------------------------------------- | :-------------------- |
| `key`     | String | Merchant Key provided by PayU.                               | `JPM7Fg`              |
| `command` | String | Must be set to `capture_transaction`.                        | `capture_transaction` |
| `hash`    | String | Calculated SHA-512 hash: `sha512(key\|command\|var1\|salt)`. | `67411736ab...`       |
| `var1`    | String | PayU Transaction ID (`mihpayid`) received in Step 2.         | `403993715523615328`  |
| `var2`    | String | Merchant Transaction ID (`txnid`).                           | `ORD_20261120_001`    |
| `var3`    | String | Amount to capture (up to authorized amount).                 | `850.00`              |

### Sample Capture Request

```bash
curl -X POST "https://test.payu.in/merchant/postservice.php?form=2" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JPM7Fg" \
  -d "command=capture_transaction" \
  -d "var1=403993715523615328" \
  -d "var2=ORD_20261120_001" \
  -d "var3=850.00" \
  -d "hash=CALCULATED_CAPTURE_HASH"
```

#### Sample Response

```json
{
  "status": 1,
  "msg": "Capture Request Queued",
  "request_id": "REQ_CAP_9845123",
  "bank_ref_num": "261005309469848160"
}
```

***

## Step 4: Verify and Track Status

* **Verify Payment (**`verify_payment`**)**: Query transaction status anytime. Active pre-auth holds return `unmappedstatus: auth`. Captured transactions return `unmappedstatus: captured`.
* **Check Action Status (**`check_action_status`**)**: Check the progress of queued captures using `request_id`.
* **Cancel Hold (**`cancel_transaction`**)**: If order is cancelled, refer to [Cancel a Pre-Authorized Payment](doc:cancel-a-pre-authorized-payment).