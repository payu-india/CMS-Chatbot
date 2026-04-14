---
title: UPI Integration for CB LRS
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: UPI Integration for CB LRS
deprecated: false
hidden: false
metadata:
  title: UPI Integration - Cross Border Transaction under LRS
  keywords:
    - UPI Integration for Cross Border Transaction under LRS
    - UPI Integration for CB LRS
  robots: index
---

This section explains how to integrate UPI Intent payments for cross-border transactions under LRS (Liberalised Remittance Scheme) using the Server-to-Server (S2S) flow.

<Cards columns={3}>
  <Card title="1. Validate the PAN Card" href="#step-1-validate-the-pan-card">
    Verify PAN card details for KYC compliance
  </Card>

  <Card title="2. Request Payment with PayU" href="#step-2-request-payment-with-payu">
    Initiate the UPI Intent payment request with LRS parameters
  </Card>

  <Card title="3. Invoke UPI Intent on Customer's Device" href="#step-3-invoke-upi-intent-on-customers-device">
    Trigger the UPI Intent on the customer's mobile device
  </Card>

  <Card title="4. Verify the Payment" href="#step-4-verify-the-payment">
    Verify the payment status using webhooks
  </Card>
</Cards>

<RegisterMerchantPrerequiste />

<Callout icon="❗️" theme="error">
  **Important UPI Integration Changes as per NPCI Mandate on UPI Collect Disablement**:

  * **For Android Apps**: Merchants must implement the Smart Intent implementation. Refer to [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow) for non-SDK implementation, or use [PayU Android SDKs](doc:explore-android-sdks) which have Smart Intent built-in.

  * **For iOS Apps**: Merchants can implement the specific deeplink handling and continue using the UPI flow as is. Refer to [iOS UPI SDK](doc:ios-upi-sdk) for SDK-based implementation.

  * **For Web**: Use the deeplink returned in the API response to generate a QR code that customers can scan with their UPI app.
</Callout>

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

Post the payment parameters to PayU's `_payment` API endpoint to initiate a UPI Intent transaction with LRS parameters.

**Environment**

|                            |                                                                        |
| :------------------------- | :--------------------------------------------------------------------- |
| **Test Environment**       | \<[https://test.payu.in/_payment>](https://test.payu.in/_payment>)     |
| **Production Environment** | \<[https://secure.payu.in/_payment>](https://secure.payu.in/_payment>) |

<Accordion title="Request Parameters" icon="fa-table">
  ### Standard Parameters

  | Parameter                                     | Description                                                                                                                                                                                                                                                                                                                                                        | Example                                                                                        |
  | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
  | key<br />`mandatory`                          | `String` The merchant key provided by PayU must be included. **Reference**: For more information on how to generate the Key and Salt, refer to any of the following: **Production**: [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard) **Test**: [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt) |                                                                                                |
  | txnid<br />`mandatory`                        | `String` (alphanumeric) Merchant transaction identifier - This parameter must be unique (after a successful transaction) & alphanumeric special (\<= 50 characters & excluding >,\<, =,:,&, ').                                                                                                                                                                    | 1234\_abcdedf                                                                                  |
  | amount<br />`mandatory`                       | `String` (rounded to two decimal places) This parameter must contain the amount for which QR needs to be generated. The amount should be greater than or equal to Rs.1.00.                                                                                                                                                                                         | 1000                                                                                           |
  | phone<br />`mandatory`                        | `String` This parameter must contain the customer phone number (10 characters).                                                                                                                                                                                                                                                                                    | 9876786756                                                                                     |
  | productinfo<br />`mandatory`                  | `String` (alphanumeric) Name or brief description of the goods/services being sold. In case of physical goods, please include name / description of all products. (max. 100 characters).                                                                                                                                                                           | iPhone 12                                                                                      |
  | firstname<br />`mandatory`                    | `String` The first name of the customer as on their Permanent Account Number (PAN). This should be validated by PAN Status Check API (max. 60 characters).                                                                                                                                                                                                         | Sundar                                                                                         |
  | lastname<br />`mandatory`                     | `String` The last name of the customer as on their Permanent Account Number (PAN). This should be validated by PAN Status Check API (max. 20 characters).                                                                                                                                                                                                          | Teja                                                                                           |
  | email<br />`mandatory`                        | `String` This parameter must contain the customer email ID.                                                                                                                                                                                                                                                                                                        | [hello@payu.in](mailto:hello@payu.in)                                                          |
  | pg<br />`mandatory`                           | `String` The payment method is specified in this field. For UPI INTENT, specify the parameter value as **UPI**.                                                                                                                                                                                                                                                    | UPI                                                                                            |
  | bankcode<br />`mandatory`                     | `String` Each payment option is identified with a unique bank code at PayU. For UPI Intent, specify the value as **INTENT**.                                                                                                                                                                                                                                       | INTENT                                                                                         |
  | surl<br />`mandatory`                         | `String` Success URL(surl) – It must contain the URL on which PayU will redirect the final response if the transaction is successful.                                                                                                                                                                                                                              | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/) |
  | furl<br />`mandatory`                         | `String` Failure URL (furl) – It must contain the URL on which PayU will redirect the final response in case of failure.                                                                                                                                                                                                                                           | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/) |
  | address1<br />`mandatory`                     | `String` This parameter must contain the first line of customer address (up to 100 characters).                                                                                                                                                                                                                                                                    | PayU, Bestech Business Tower, Gurgaon                                                          |
  | address2<br />`optional`                      | `String` This parameter must contain the second line of the customer address (up to 100 characters).                                                                                                                                                                                                                                                               | Sohna Road                                                                                     |
  | city<br />`mandatory`                         | `String` This parameter must contain the customer city (max. 50 characters).                                                                                                                                                                                                                                                                                       | Gurgaon                                                                                        |
  | country<br />`mandatory`                      | `String` This parameter must contain the customer's country that is part of the address (max. 50 characters).                                                                                                                                                                                                                                                      | India                                                                                          |
  | state<br />`mandatory`                        | `String` This parameter must contain the customer state that is part of the address (max 50 characters).                                                                                                                                                                                                                                                           | Haryana                                                                                        |
  | zipcode<br />`mandatory`                      | `Numeric` This parameter must contain the customer's PIN code (6 digits).                                                                                                                                                                                                                                                                                          | 122018                                                                                         |
  | udf1<br />`mandatory for LRS`                 | `String` The Permanent Account Number (PAN) of the buyer must be collected in this field.                                                                                                                                                                                                                                                                          | AELPR\*\*\*\*E                                                                                 |
  | udf2<br />`optional`                          | `String` This parameter can include any custom information in request (up to 255 characters.).                                                                                                                                                                                                                                                                     |                                                                                                |
  | udf3<br />`mandatory for LRS`                 | `String` Date of Birth (DOB) of buyer in DD-MM-YYYY format as on their PAN. This should be validated by PAN Status Check API.                                                                                                                                                                                                                                      | 02-02-1980                                                                                     |
  | udf4<br />`mandatory for payment aggregators` | `String` End merchant legal entity name. For UPI, this field should not be passed. (up to 255 characters.)                                                                                                                                                                                                                                                         |                                                                                                |
  | udf5<br />`mandatory`                         | `String` Contains invoice ID for the transaction. Invoice ID / number should be the ID present on the invoice issued to the customer. (up to 255 characters.)                                                                                                                                                                                                      | INV123456                                                                                      |
  | udf\_params<br />`optional`                   | `String JSON` UDF7 value to capture "Import or Export Code" of the buyer. UDF8 value to capture Airway Bill Number / Consignment Number (in case of goods imports). *Note*: This must be included in hash if posted.                                                                                                                                               | \{"udf7":"0100000029","udf8":"99953729071"}                                                    |
  | hash<br />`mandatory`                         | `String` Crucial security parameter using SHA512 hash encryption. For more information, refer to [Generate Hash](doc:hashing-request-and-response)                                                                                                                                                                                                                 |                                                                                                |
  | txn\_s2s\_flow<br />`mandatory`               | `Numeric` This parameter must be passed with the value as 4                                                                                                                                                                                                                                                                                                        | 4                                                                                              |
  | s2s\_client\_ip<br />`mandatory`              | `String` This parameter must have the source IP of the user's device.                                                                                                                                                                                                                                                                                              |                                                                                                |
  | s2s\_device\_info<br />`mandatory`            | `String` This parameter must have the user agent of device.                                                                                                                                                                                                                                                                                                        |                                                                                                |
  | upiAppName<br />`mandatory`                   | `String` For Specific Intent, merchant should share the app name which is selected by customer on the merchant check-out page. The following are the enum's expected for major apps: phonepe, googlepay, paytm, bhim, cred, amazonpay, whatsapp, genericintent – For any other app apart from above                                                                | phonepe                                                                                        |
  | `buyer_type_business`<br />`conditional for cross-border transactions`      | This parameter is used to identify whether it is a business-to-business transaction. If 1 is posted, it is a B2B transaction.<br /><br />In case of B2B, no other LRS specific parameters (listed below) need to be sent, as B2B transactions are outside the scope of the regulation.                                                                                                                                                                                                                                                                                                 | 0       |
  | `lrs_mandatory_limit_declaration`<br />`mandatory for LRS S2S transactions` | `String` Mandatory declaration from buyer that they have remitted less than $250,000 USD under Liberalised Remittance Scheme.<br /><br />**Note**: The limit is as per RBI regulation and needs to be mandatorily collected on the checkout page.                                                                                                                                                                                                                                                                                                                                      | 1       |
  | `lrs_tnc`<br />`mandatory for LRS S2S transactions`                         | `String` Mandatory declaration from buyer that they agree to PayU's terms & conditions.<br /><br />**Note**: The declaration needs to be taken mandatorily from the buyer on the checkout page.                                                                                                                                                                                                                                                                                                                                                                                        | 1       |
  | `lrs_service_type`<br />`mandatory for LRS S2S transactions`                | `String` The LRS service type describes the nature of service & decides the tax amount based on it. For more information, refer to the [lrs\_service\_type parameter values](#lrs_service_type-parameter-values) table.                                                                                                                                                                                                                                                                                                                                                                | travel  |
  | `tcs_amount`<br />`mandatory for LRS S2S transactions`                      | `String` Amount of TCS (Tax Collected at Source) to be charged.<br /><br />**Note**: The amount needs to be captured as per guidance in the [lrs\_service\_type parameter values](#lrs_service_type-parameter-values) table.                                                                                                                                                                                                                                                                                                                                                           | 2.00    |
  | `lrs_tcs_declaration_under_limit`<br />`mandatory for LRS S2S transactions` | `String` Declaration from buyer that they are either under or over INR 1,00,000 based on which TCS will be collected.<br /><br />Values expected:<br /><br />**0** (in case of under the limit)<br />**1** (in case of over the limit)<br /><br />**Note**: The declaration needs to be taken mandatorily from the buyer on the checkout page. Also, when user declares they are over the limit (i.e. when this param is sent as "1", the "tcs\_amount" field to contain amount calculated as per the [lrs\_service\_type parameter values](#lrs_service_type-parameter-values) table. | 0 / 1   |

  #### lrs\_service\_type parameter values

  | **lrs\_service\_type** | **Txn Amount \<= INR 10 lacs** | **Txn Amount > INR 10 lacs** |
  | ---------------------- | ------------------------------ | ---------------------------- |
  | education\_loan        | 0                              | 0                            |
  | education\_non\_loan   | 0                              | 5%                           |
  | medical                | 0                              | 5%                           |
  | travel                 | 0                              | 20%                          |
  | others                 | 0                              | 20%                          |

  <Accordion title="Hashing Logic" icon="fa-lock">
    <PACB_Hashing />

    ```
    key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|salt|additional_charges|buyer_type_business
    ```

    * **Case4 example**: if the merchant wants to pass the api\_version = 7 and buyer\_type\_business, udf\_params in the payment request.

    ```
    key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|si_details|salt|udf_params|buyer_type_business
    ```

    For more information, refer to <a href="generate-hash-merchant-hosted" target="_blank">Generate Hash</a>.
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
  --data-urlencode 'surl=https://test.payu.in/admin/test_response' \
  --data-urlencode 'furl=https://test.payu.in/admin/test_response' \
  --data-urlencode 'address1=308,third floor' \
  --data-urlencode 'address2=testing' \
  --data-urlencode 'city=Gurugram' \
  --data-urlencode 'state=Haryana' \
  --data-urlencode 'country=India' \
  --data-urlencode 'zipcode=122018' \
  --data-urlencode 'pg=UPI' \
  --data-urlencode 'bankcode=INTENT' \
  --data-urlencode 'txn_s2s_flow=4' \
  --data-urlencode 's2s_client_ip=10.200.12.12' \
  --data-urlencode 's2s_device_info=Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0' \
  --data-urlencode 'udf1=CYCPD2784G' \
  --data-urlencode 'udf3=02-02-1980' \
  --data-urlencode 'udf5=INV123456' \
  --data-urlencode 'upiAppName=phonepe' \
  --data-urlencode 'buyer_type_business=0' \
  --data-urlencode 'lrs_mandatory_limit_declaration=1' \
  --data-urlencode 'lrs_tnc=1' \
  --data-urlencode 'lrs_service_type=travel' \
  --data-urlencode 'tcs_amount=2.00' \
  --data-urlencode 'lrs_tcs_declaration_under_limit=0' \
  --data-urlencode 'hash=YOUR_CALCULATED_HASH'
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-code">
  ```json
  {
      "metaData": {
          "message": null,
          "referenceId": "c99a6455b3e0dc5cd7167ab8c8cc10d2fa153cb509e3f64c6cd0ed9c5b64a8c9",
          "statusCode": null,
          "txnId": "payuTestTransaction12345",
          "txnStatus": "pending",
          "unmappedStatus": "pending"
      },
      "result": {
          "paymentId": "403993715535965242",
          "merchantName": "Sudhanshu",
          "merchantVpa": "payutest@hdfcbank",
          "amount": "100.00",
          "intentURIData": "pa=payutest@hdfcbank&pn=Kumar&tr=403993715535965242&tid=PPPL403993715535965242080126220900&am=100.00&cu=INR&tn=UPIIntent",
          "acsTemplate": "PGh0bWw+PGJvZHk+...",
          "otpPostUrl": "https://test.payu.in/ResponseHandler.php"
      }
  }
  ```
</Accordion>

***

## Step 3: Invoke UPI Intent on Customer's Device

<Accordion title="Implementation" icon="fa-monitor">
  You need to invoke intent in the customer's mobile device using the merchant VPA URL. Make sure that only this merchant VPA is embedded in the intent call since this helps to track the status of the transaction.

  Open the UPI Intent as per the NPCI Guidelines. Merchants can also open any specific app instead of making the Generic Intent call. For example, Google Pay, PhonePe, etc. This URL can then be fired using an Intent or a hyperlink which would open an Intent tray with a list of available supporting apps on the user's mobile device. The following sample UPI Deep Link URL and the format used for creating the URL:

  **Sample URL** (with values from the above sample JSON):

  ```plaintext
  upi://pay?pa=payu@axisbank&pn=SMSPLUS&tr=8312916361&am=100.00
  ```

  **Format for UPI Deep Linking URL** (as per NPCI guidelines):

  ```plaintext
  "upi://pay?pa=" + merchantVpa + "&pn=" + merchantName + "&tr=" + referenceId + "&am=" + amount 
  ```

  Where the description of the parameters used in the URL is as described in the following table:

  | **Parameter** | **Description**                                                                                   |
  | ------------- | ------------------------------------------------------------------------------------------------- |
  | merchantVpa   | As received in JSON response in key merchantVPA'                                                  |
  | merchantName  | As received in JSON response in key merchantName.                                                 |
  | referenceId   | As received in JSON response in key referenceId.                                                  |
  | amount        | Amount of transaction. This must be the same as the amount passed to the **initiatePayment** API. |
</Accordion>

> 📘 Notes:
>
> * Every time there is a change, you need to incorporate the changes to avoid breaking the transactions.
> * The **tid** value which is passed in the intent URI acts as a validation check at NPCI's end which do not allow duplicate transaction.
> * The tr value not necessary and it is a payU_id. It can be any reference id for PayU's internal reconciliation.

***

## Step 4: Verify the Payment

Use the webhooks to verify the payment. The following is the sample webhook payload in response. For more information, refer to [Webhook Events and Sample Payloads](doc:webhook-events-and-sample-payloads).

Verify the transaction details using the Verification APIs. For API reference, refer to [Verify Payment API](doc:verify_payment_api) under API Reference.

***
