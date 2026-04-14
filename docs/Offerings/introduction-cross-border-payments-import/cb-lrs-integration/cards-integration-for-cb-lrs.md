---
title: Cards Integration for CB LRS
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Cards Integration for CB LRS
deprecated: false
hidden: false
metadata:
  title: Cards Integration - Cross Border Transaction under LRS
  keywords:
    - Cards Integration for Cross Border Transaction under LRS
    - Cards Integration for CB LRS
  robots: index
---
This section explains how to integrate plain card payments for cross-border transactions under LRS (Liberalised Remittance Scheme) using the Server-to-Server (S2S) flow. This is the standard card transaction flow without tokenization.

<Cards columns={3}>
  <Card title="1. Validate the PAN Card" href="#step-1-validate-the-pan-card">
    Verify PAN card details for KYC compliance
  </Card>

  <Card title="2. Request Payment with PayU" href="#step-2-request-payment-with-payu">
    Post the required parameters to PayU for card payment with LRS parameters
  </Card>

  <Card title="3. Check Response from PayU" href="#step-3-check-response-from-payu">
    Verify the response hash and transaction status
  </Card>

  <Card title="4. Handle Initiate Response from PayU" href="#step-4-handle-the-initiate-response-from-payu">
    Handle the response and proceed with 3DS authentication
  </Card>

  <Card title="5. Verify the Payment" href="#step-5-verify-the-payment">
    Verify the payment status and ensure transaction completion
  </Card>

  <Card title="6. Update Invoice ID (Conditional)" href="#step-6-update-invoice-id-conditional">
    Update the invoice ID associated with the transaction
  </Card>

  <Card title="7. Upload the Invoices (Conditional)" href="#step-7-upload-the-invoices-conditional">
    Upload invoice documents related to the completed transaction
  </Card>
</Cards>

***

## Step 1: Validate the PAN Card

The PAN Card Status Check API allows merchants to verify PAN (Permanent Account Number) card details. It validates whether a given PAN number is active, confirms if the provided name and date of birth match the official PAN records, and checks the seeding status of the PAN. This API is essential for KYC (Know Your Customer) processes, identity verification, and regulatory compliance.

**Endpoint**

```
https://test10-onboarding.payu.in/dvs/kyc/check_pan_card_status
```

<Accordion title="Request parameters" icon="fa-table">
  | Parameter                     | Description                                                   | Example      |
  | ----------------------------- | ------------------------------------------------------------- | ------------ |
  | `pan_number`<br />`mandatory` | The PAN (Permanent Account Number) to be verified             | "CYCPD2784G" |
  | `name`<br />`mandatory`       | The name of the PAN card holder as it appears on the PAN card | "AKASH DEEP" |
  | `dob`<br />`mandatory`        | Date of Birth of the PAN holder in DD/MM/YYYY format          | "15/09/1993" |
</Accordion>

<Accordion title="Sample Request" icon="fa-code">
  ```bash
  curl --location 'https://test10-onboarding.payu.in/dvs/kyc/check_pan_card_status' \
  --header 'Content-Type: application/json' \
  --header 'Date: Thu, 17 Jun 2025 08:17:59 GMT' \
  --header 'Digest: DFXmqI0rFnXlmHLlsRwdDMw9vUSVzyYQzGP+MKLo8f8=' \
  --header 'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="7qjgpH9B4QALxDR0nVlHdEKEYMZ0XeJ0QpnvveSyqMo="' \
  --header 'platformId: 1' \
  --data '{
      "pan_number": "CYCPD2784G",
      "name": "AKASH DEEP",
      "dob": "15/09/1993"
  }'
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-reply">
  ```json
  {
      "id": 86235,
      "api_name": "pan_status_check",
      "identifier": "79c0d918a4f4661cb9cb17d96d24ac1cf04b6013d504cc766ac5235380bfc0d5",
      "response": {
          "result": {
              "status": "Active",
              "nameMatch": "Y",
              "dobMatch": "Y",
              "seedingStatus": "Y"
          }
      },
      "status": "success",
      "http_status": 200,
      "client_id": "195ab95fa4700eeaaf38b7f5b538d2979f0f281e0a4eaedca1aa675b79b331a2",
      "created_at": "2025-04-30T05:51:40.000Z",
      "updated_at": "2025-04-30T05:51:40.000Z",
      "client_name": "SignzyClient"
  }
  ```
</Accordion>

<Accordion title="Response Parameters" icon="fa-table">
  | Parameter    | Description                                             | Example                                                              |
  | ------------ | ------------------------------------------------------- | -------------------------------------------------------------------- |
  | id           | Unique identifier for the verification request          | `86235`                                                              |
  | api\_name    | Identifier of the API that was called                   | `"pan_status_check"`                                                 |
  | identifier   | A unique hash identifier for the verification request   | `"79c0d918a4f4661cb9cb17d96d24ac1cf04b6013d504cc766ac5235380bfc0d5"` |
  | response     | Contains the verification results                       | See result table below                                               |
  | status       | Overall status of the API call                          | `"success"`                                                          |
  | http\_status | HTTP status code of the response                        | `200`                                                                |
  | client\_id   | Unique identifier of the client making the request      | `"195ab95fa4700eeaaf38b7f5b538d2979f0f281e0a4eaedca1aa675b79b331a2"` |
  | created\_at  | Timestamp when the verification record was created      | `"2025-04-30T05:51:40.000Z"`                                         |
  | updated\_at  | Timestamp when the verification record was last updated | `"2025-04-30T05:51:40.000Z"`                                         |
  | client\_name | Name of the client account                              | `"SignzyClient"`                                                     |

  #### Response Result Object

  | Parameter     | Description                                                        | Example    |
  | ------------- | ------------------------------------------------------------------ | ---------- |
  | status        | Status of the PAN card                                             | `"Active"` |
  | nameMatch     | Indicates if the provided name matches with PAN records (Y/N)      | `"Y"`      |
  | dobMatch      | Indicates if the provided DOB matches with PAN records (Y/N)       | `"Y"`      |
  | seedingStatus | Indicates if the PAN is seeded with additional verifications (Y/N) | `"Y"`      |
</Accordion>

***

## Step 2: Request Payment with PayU

Post the payment parameters to PayU's `_payment` API endpoint to initiate a card transaction with LRS parameters.

**Environment**

|                            |                                                                        |
| :------------------------- | :--------------------------------------------------------------------- |
| **Test Environment**       | \<[https://test.payu.in/_payment>](https://test.payu.in/_payment>)     |
| **Production Environment** | \<[https://secure.payu.in/_payment>](https://secure.payu.in/_payment>) |

<Accordion title="Request Parameters" icon="fa-table">
  ### Standard Parameters

  | Parameter                                          | Description                                                                                                                                                                                              | Example                                                       |
  | -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
  | key<br />`mandatory`                               | `String` Merchant key provided by PayU during onboarding.                                                                                                                                                | `JPM7Fg`                                                      |
  | txnid<br />`mandatory`                             | `String` The transaction ID is a reference number for a specific order generated by the merchant. Must be unique.                                                                                        | `payuTestTxn12345`                                            |
  | amount<br />`mandatory`                            | `String` The payment amount for the transaction.                                                                                                                                                         | `100.00`                                                      |
  | productinfo<br />`mandatory`                       | `String` Name or brief description of the goods/services being sold. In case of physical goods, please include name / description of all products. Character Limit: 100                                  | `iPhone`                                                      |
  | firstname<br />`mandatory`                         | `String` The first name of the customer as on their Permanent Account Number (PAN). This should be validated by PAN Status Check API. Character Limit: 60                                                | `Ashish`                                                      |
  | lastname<br />`mandatory`                          | `String` The last name of the customer as on their Permanent Account Number (PAN). This should be validated by PAN Status Check API. Character Limit: 60                                                 | `Kumar`                                                       |
  | email<br />`mandatory`                             | `String` The email address of the customer. Character Limit: 50                                                                                                                                          | `test@gmail.com`                                              |
  | phone<br />`mandatory`                             | `String` The phone number of the customer.                                                                                                                                                               | `9876543210`                                                  |
  | address1<br />`mandatory`                          | `varchar` The customer's primary billing address line. This field is required for billing and fraud prevention purposes. Character limit: 255.                                                           | 123 Main Street                                               |
  | city<br />`mandatory`                              | `varchar` The customer's billing city. This field is required for billing and fraud prevention purposes. Character limit: 50.                                                                            | New Delhi                                                     |
  | state<br />`mandatory`                             | `varchar` The customer's billing state or province. This field is required for billing and fraud prevention purposes. Character limit: 50.                                                               | Delhi                                                         |
  | country<br />`mandatory`                           | `varchar` The customer's billing country. This field is required for billing and fraud prevention purposes.                                                                                              | India                                                         |
  | zipcode<br />`mandatory`                           | `varchar` The customer's billing postal/zip code. This field is required for billing and fraud prevention purposes. Character limit: 6 digit (India Zipcode)                                             | 110075                                                        |
  | surl<br />`mandatory`                              | `String` The Success URL - page PayU will redirect to if the transaction is successful.                                                                                                                  | `https://example.com/success`                                 |
  | furl<br />`mandatory`                              | `String` The Failure URL - page PayU will redirect to if the transaction fails.                                                                                                                          | `https://example.com/failure`                                 |
  | pg<br />`mandatory`                                | `String` Payment gateway type. For cards, use `CC`.                                                                                                                                                      | `CC`                                                          |
  | bankcode<br />`mandatory`                          | `String` Bank code for the payment option. Use `CC` for credit cards, `DC` for debit cards.                                                                                                              | `CC`                                                          |
  | ccnum<br />`mandatory`                             | `String` 13-19 digit card number (15 for AMEX, 13-19 for Maestro). Validate with LUHN algorithm.                                                                                                         | `5506900480000008`                                            |
  | ccvv<br />`mandatory`                              | `String` 3-digit CVV (4 digits for AMEX).                                                                                                                                                                | `123`                                                         |
  | ccname<br />`mandatory`                            | `String` Cardholder name as entered by the customer.                                                                                                                                                     | `Test User`                                                   |
  | ccexpmon<br />`mandatory`                          | `String` Card expiry month in MM format (01-12).                                                                                                                                                         | `09`                                                          |
  | ccexpyr<br />`mandatory`                           | `String` Card expiry year in YYYY format.                                                                                                                                                                | `2026`                                                        |
  | txn\_s2s\_flow<br />`mandatory`                    | `Integer` Parameter to enable S2S flow. Set to `4` for S2S4 flow.                                                                                                                                        | `4`                                                           |
  | s2s\_client\_ip<br />`mandatory`                   | `String` Client IP captured by merchant in S2S flow. Required for fraud detection.                                                                                                                       | `10.200.12.12`                                                |
  | s2s\_device\_info<br />`mandatory`                 | `String` User Agent captured by merchant in S2S flow.                                                                                                                                                    | `Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0` |
  | udf1<br />`mandatory for LRS`                      | `String` The Permanent Account Number (PAN) of the buyer must be collected in this field. Character limit: 10 character alphanumeric                                                                     | ABCDE1234K                                                    |
  | udf2<br />`optional`                               | `String` User-defined field for storing transaction-specific data. Character limit: 255.                                                                                                                 | Additional transaction data                                   |
  | udf3<br />`mandatory for LRS`                      | `String` Date of Birth (DOB) of buyer in DD-MM-YYYY format as on their PAN. This should be validated by PAN Status Check API.                                                                            | 02-02-1980                                                    |
  | udf4<br />`mandatory for payment aggregators`      | `String` End merchant legal entity name. Character limit: 255.                                                                                                                                           | XYZ Pvt. Ltd.                                                 |
  | udf5<br />`mandatory`                              | `String` Contains invoice ID for the transaction. Invoice ID / number should be the ID present on the invoice issued to the customer. Character limit: 255.                                              | INV123456                                                     |
  | udf\_params<br />`optional`                        | `String JSON` UDF7 value to capture "Import or Export Code" of the buyer. UDF8 value to capture Airway Bill Number / Consignment Number (in case of goods imports)                                       | \{"udf7":"0100000029","udf8":"99953729071"}                   |
  | hash<br />`mandatory`                              | `String` This must include the generated hash. For more information, refer to Hash Generation below this table.                                                                                          | Your Generated Hash                                           |

  ### LRS-Specific Parameters

  | Parameter                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Example  |
  | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
  | `buyer_type_business`<br />`conditional for cross-border transactions`      | This parameter is used to identify whether it is a business-to-business transaction. If 1 is posted, it is a B2B transaction.<br /><br />In case of B2B, no other LRS specific parameters (listed below) need to be sent, as B2B transactions are outside the scope of the regulation.                                                                                                                                                                                                                                                                                                 | 0        |
  | `lrs_mandatory_limit_declaration`<br />`mandatory for LRS S2S transactions` | `String` Mandatory declaration from buyer that they have remitted less than $250,000 USD under Liberalised Remittance Scheme.<br /><br />**Note**: The limit is as per RBI regulation and needs to be mandatorily collected on the checkout page.                                                                                                                                                                                                                                                                                                                                      | 1        |
  | `lrs_tnc`<br />`mandatory for LRS S2S transactions`                         | `String` Mandatory declaration from buyer that they agree to PayU's terms & conditions.<br /><br />**Note**: The declaration needs to be taken mandatorily from the buyer on the checkout page.                                                                                                                                                                                                                                                                                                                                                                                        | 1        |
  | `lrs_service_type`<br />`mandatory for LRS S2S transactions`                | `String` The LRS service type describes the nature of service & decides the tax amount based on it. For more information, refer to the [lrs\_service\_type parameter values](#lrs_service_type-parameter-values) table.                                                                                                                                                                                                                                                                                                                                                                | travel   |
  | `tcs_amount`<br />`mandatory for LRS S2S transactions`                      | `String` Amount of TCS (Tax Collected at Source) to be charged.<br /><br />**Note**: The amount needs to be captured as per guidance in the [lrs\_service\_type parameter values](#lrs_service_type-parameter-values) table.                                                                                                                                                                                                                                                                                                                                                           | 2.00     |
  | `lrs_tcs_declaration_under_limit`<br />`mandatory for LRS S2S transactions` | `String` Declaration from buyer that they are either under or over INR 1,00,000 based on which TCS will be collected.<br /><br />Values expected:<br /><br />**0** (in case of under the limit)<br />**1** (in case of over the limit)<br /><br />**Note**: The declaration needs to be taken mandatorily from the buyer on the checkout page. Also, when user declares they are over the limit (i.e. when this param is sent as "1", the "tcs\_amount" field to contain amount calculated as per the [lrs\_service\_type parameter values](#lrs_service_type-parameter-values) table. | 0 / 1    |

  #### lrs\_service\_type parameter values

  | **lrs\_service\_type** | **Txn Amount \<= INR 10 lacs** | **Txn Amount > INR 10 lacs** |
  | ---------------------- | ------------------------------ | ---------------------------- |
  | education\_loan        | 0                              | 0                            |
  | education\_non\_loan   | 0                              | 5%                           |
  | medical                | 0                              | 5%                           |
  | travel                 | 0                              | 20%                          |
  | others                 | 0                              | 20%                          |

  <Accordion title="Hash Generation" icon="fa-lock">
    <PACB_Hashing />

    ```
    key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|salt|additional_charges|buyer_type_business
    ```

    * **Case4 example**: if the merchant wants to pass the api\_version = 7 and buyer\_type\_business, udf\_params in the payment request.

    ```
    key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|si_details|salt|udf_params|buyer_type_business
    ```

    <Callout icon="📘" theme="info">
      **Reference:** PayU recommends you to use PayU Hash Verification Tool to verify the hashing. For more information, refer to [Using PayU Hash Verification Tool](doc:using-payu-hash-verification-tool)
    </Callout>
  </Accordion>
</Accordion>

<Accordion title="Sample Request" icon="fa-code">
  ```curl
  curl --location --request POST 'https://test.payu.in/_payment' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=JPM7Fg' \
  --data-urlencode 'txnid=payuTestTransaction12345' \
  --data-urlencode 'amount=100.00' \
  --data-urlencode 'firstname=Ashish' \
  --data-urlencode 'lastname=Kumar' \
  --data-urlencode 'email=test@payu.in' \
  --data-urlencode 'phone=9988776655' \
  --data-urlencode 'productinfo=Product Info' \
  --data-urlencode 'address1=123 Main Street' \
  --data-urlencode 'city=New Delhi' \
  --data-urlencode 'state=Delhi' \
  --data-urlencode 'country=India' \
  --data-urlencode 'zipcode=110001' \
  --data-urlencode 'surl=https://test.payu.in/admin/test_response' \
  --data-urlencode 'furl=https://test.payu.in/admin/test_response' \
  --data-urlencode 'pg=CC' \
  --data-urlencode 'bankcode=CC' \
  --data-urlencode 'ccnum=5506900480000008' \
  --data-urlencode 'ccname=Test User' \
  --data-urlencode 'ccvv=123' \
  --data-urlencode 'ccexpmon=09' \
  --data-urlencode 'ccexpyr=2026' \
  --data-urlencode 'txn_s2s_flow=4' \
  --data-urlencode 's2s_client_ip=10.200.12.12' \
  --data-urlencode 's2s_device_info=Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0' \
  --data-urlencode 'udf1=CYCPD2784G' \
  --data-urlencode 'udf3=02-02-1980' \
  --data-urlencode 'udf4=XYZ Pvt. Ltd.' \
  --data-urlencode 'udf5=INV123456' \
  --data-urlencode 'buyer_type_business=0' \
  --data-urlencode 'lrs_mandatory_limit_declaration=1' \
  --data-urlencode 'lrs_tnc=1' \
  --data-urlencode 'lrs_service_type=travel' \
  --data-urlencode 'tcs_amount=2.00' \
  --data-urlencode 'lrs_tcs_declaration_under_limit=0' \
  --data-urlencode 'hash=YOUR_CALCULATED_HASH'
  ```
</Accordion>

***

## Step 3: Check Response from PayU

<ReverseHashing />

<Accordion title="Sample response [Parsed]" icon="fa-reply">
  * Success scenario

  ```
  Array
  (
      [mihpayid] => 403993715524069222
      [mode] => CC
      [status] => success
      [unmappedstatus] => captured
      [key] => JF***g
      [txnid] => EaE4ZO3vU4iPsp
      [amount] => 100.00
      [cardCategory] => domestic
      [discount] => 0.00
      [net_amount_debit] => 102
      [addedon] => 2021-09-08 19:37:19
      [productinfo] => iPhone
      [firstname] => Ashish
      [lastname] => Kumar
      [address1] => 123 Main Street
      [address2] => 
      [city] => New Delhi
      [state] => Delhi
      [country] => India
      [zipcode] => 110001
      [email] => test@gmail.com
      [phone] => 9876543210
      [udf1] => CYCPD2784G
      [udf2] => 
      [udf3] => 02-02-1980
      [udf4] => XYZ Pvt. Ltd.
      [udf5] => INV123456
      [udf6] => 
      [udf7] => 
      [udf8] => 
      [udf9] => 
      [udf10] => 
      [hash] => ed99957adb08fea56c907b88e8d158a79c3562c67f96c298461509826f77a7ae9e88b2a176b3234c25f50bcd451271728719656f3bb59c13a52bebabc468615a
      [field1] => 0608273386032718000015
      [field2] => 986987
      [field3] => 100.00
      [field4] => 403993715524069222
      [field5] => 100
      [field6] => 02
      [field7] => AUTHPOSITIVE
      [field8] => 
      [field9] => Transaction is Successful
      [payment_source] => payu
      [PG_TYPE] => CC-PG
      [bank_ref_num] => 0608273386032718000015
      [bankcode] => CC
      [error] => E000
      [error_Message] => No Error
      [name_on_card] => payu
      [cardnum] => 512345XXXXXX2346
      [tcs_amount] => 2
  )
  ```

  * Failure scenario

  ```
  Array
  (
      [mihpayid] => 20869277619
      [mode] => CC
      [status] => failure
      [unmappedstatus] => failed
      [key] => L43t1c
      [txnid] => 26ba7cd6a67b0a010542
      [amount] => 100.00
      [cardCategory] => domestic
      [discount] => 0.00
      [net_amount_debit] => 0.00
      [addedon] => 2024-09-05 17:46:10
      [productinfo] => Product Info
      [firstname] => Payu-Admin
      [lastname] => 
      [address1] => 
      [address2] => 
      [city] => 
      [state] => 
      [country] => 
      [zipcode] => 
      [email] => test@example.com
      [phone] => 1234567890
      [udf1] => CYCPD2784G
      [udf2] => 
      [udf3] => 02-02-1980
      [udf4] => XYZ Pvt. Ltd.
      [udf5] => INV123456
      [udf6] => 
      [udf7] => 
      [udf8] => 
      [udf9] => 
      [udf10] => 
      [hash] => ac7720e4bc33e5494bec6d37302e522171175a987f9d47286bfd29e8a7fc794f56433fcacf0bc120db781c4dc1d05a4857d71e83f00f6ed6aa9c97a1938b9467
      [field1] => 
      [field2] => 
      [field3] => 
      [field4] => 
      [field5] => 05
      [field6] => 
      [field7] => AUTHNEGATIVE
      [field8] => 
      [field9] => Authorization failed at Bank
      [payment_source] => payu
      [pa_name] => PayU
      [PG_TYPE] => CC-PG
      [bank_ref_num] => 2409052690
      [bankcode] => AMEX
      [error] => E1903
      [error_Message] => Authorization failed at Bank
      [cardnum] => XXXXXXXXXXXX2003
      [cardhash] => This field is no longer supported in postback params.
      [tcs_amount] => 2
  )
  ```
</Accordion>

***

## Step 4: Handle the Initiate Response from PayU

After posting the payment request, PayU returns a response containing transaction status and next steps for 3DS authentication.

<Accordion title="Response Parameters" icon="fa-table">
  | Parameter                | Description                                                                | Example                                                            |
  | ------------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------------------ |
  | metaData                 | `Object`<br />JSON object containing transaction metadata.                 | -                                                                  |
  | metaData.referenceId     | `String`<br />PayU reference ID to be sent back in subsequent calls.       | `5a3e7cb9884e003dce1f28f965478a9a12fb9244fc15be91b0b3de48763a12e7` |
  | metaData.txnId           | `String`<br />Merchant's transaction ID.                                   | `payuTestTransaction12345`                                         |
  | metaData.txnStatus       | `String`<br />Transaction status (e.g., "Enrolled").                       | `Enrolled`                                                         |
  | metaData.unmappedStatus  | `String`<br />Status for flow control: `pending`, `captured`, or `failed`. | `pending`                                                          |
  | result.otpPostUrl        | `String`<br />URL to post OTP for verification.                            | `https://test.payu.in/ResponseHandler.php`                         |
  | result.acsTemplate       | `String`<br />Base64 encoded HTML form for bank ACS redirect.              | `PGh0bWw+PGJvZHk+...`                                              |
  | binData.pureS2SSupported | `Boolean`<br />Whether native S2S OTP flow is supported.                   | `true`                                                             |
  | binData.issuingBank      | `String`<br />Card issuing bank.                                           | `AXIS`                                                             |
  | binData.category         | `String`<br />Card category (`creditcard` or `debitcard`).                 | `creditcard`                                                       |
  | binData.cardType         | `String`<br />Card network (`VISA`, `MAST`, `RUPAY`).                      | `MAST`                                                             |
  | binData.isDomestic       | `Boolean`<br />Whether the card is domestic.                               | `true`                                                             |
</Accordion>

<Accordion title="Sample Response" icon="fa-code">
  ```json
  {
    "metaData": {
      "message": null,
      "referenceId": "5a3e7cb9884e003dce1f28f965478a9a12fb9244fc15be91b0b3de48763a12e7",
      "statusCode": null,
      "txnId": "payuTestTransaction12345",
      "txnStatus": "Enrolled",
      "unmappedStatus": "pending",
      "resendOtp": {
        "isSupported": true,
        "attemptsLeft": 2
      },
      "submitOtp": {
        "attemptsLeft": 3
      }
    },
    "result": {
      "otpPostUrl": "https://test.payu.in/ResponseHandler.php",
      "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0i..."
    },
    "binData": {
      "pureS2SSupported": true,
      "issuingBank": "AXIS",
      "category": "creditcard",
      "cardType": "MAST",
      "isDomestic": true
    }
  }
  ```
</Accordion>

<Accordion title="Handling the Response" icon="fa-info-circle">
  In S2S4, rely on the metaData.unmappedStatus field from the response JSON. Perform the following actions based on its value: 

  1. If metaData.unmappedStatus = 'pending': 
     * Check the value of the binData.pureS2SSupported parameter: 
       * If binData.pureS2SSupported = true: 
       * Invoke the OTP page and present it to the customer, Use Submit OTP API to Collect & Submit OTP from your Page.
       * If the customer opts to redirect to the bank ACS for entering the OTP, provide a "Redirect to Bank Page" link. Upon selection, load the value of the result.acsTemplate parameter as the Bank Form by decoding it using base64 encoding formula.
     * If binData.pureS2SSupported = false: 
       * Redirect the customer using the result.acsTemplate parameter, which contains a Base64-encoded HTML form. 
  2. The metaData.referenceId value from the response JSON will be used as the input for the referenceId parameter in both the submitOtp and resentOtp APIs. 
     * If metaData.unmappedStatus = 'failure', refer to the metaData.statusCode and metaData.msg fields for details on the failure reasons.

  Based on the `unmappedStatus` value, take the following actions:

  | Status     | Action                                                              |
  | ---------- | ------------------------------------------------------------------- |
  | `pending`  | Proceed with 3DS authentication using the `acsTemplate` or OTP flow |
  | `captured` | Transaction successful, no further action needed                    |
  | `failed`   | Transaction failed, display error to customer                       |
</Accordion>

<Callout icon="📘" theme="info">
  **Redirect** the customer using the result.acsTemplate(base64encoded) to their bank's page for authentication. The final response will be posted to surl/furl and the configured Webhook.
</Callout>

<Callout icon="👍" theme="okay">
  **Reference:** PayU recommends you to use PayU Hash Verification Tool to verify the reverse hashing. For more information, refer to [Using PayU Hash Verification Tool](doc:using-payu-hash-verification-tool)
</Callout>

***

## Step 5: Verify the Payment

<PACB_Verify_Payment />

***

## Step 6: Update Invoice ID [Conditional]

<Update_Invoice_ID />

***

## Step 7: Upload the Invoices [Conditional]

<Upload_Invoices />

***

## Error Handling

If any error message is displayed with an error code, refer to [Error Codes](ref:error-codes) to understand the reason. For error codes during various transaction stages, refer to [Transaction Stages - Error References](ref:transaction-stages-error-references-on-field7-field8).

> 📘 Reference
>
> For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).
