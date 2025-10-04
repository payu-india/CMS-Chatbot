---
title: UPI Intent OTM - PayU Hosted
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The pre_authorize parameter is used to pre-authorize payments using the PayU Hosted Checkout integration with the _payment API.

You need to activate the Pre-authorize payments before you start using the functionality. Contact your PayU KAM to enable this functionality.

## Step 1: Post the Pre-Authorization Request

**Environment**

<PaymentAPIEnvironment />

<Accordion title="Request parameters" icon="fa-code">
  <Table align={["left","left","left"]}>
    <thead>
      <tr>
        <th style={{ textAlign: "left" }}>
          Parameter
        </th>

        <th style={{ textAlign: "left" }}>
          Description
        </th>

        <th style={{ textAlign: "left" }}>
          Example
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td style={{ textAlign: "left" }}>
          key  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `varchar` This parameter is the unique Merchant Key provided by PayU for your merchant account.
        </td>

        <td style={{ textAlign: "left" }}>
          Your Test Key
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          txnid  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `varchar` This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction.
          `Character limit`: 25

          * **Note**: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID.'
        </td>

        <td style={{ textAlign: "left" }}>
          fd3e847h2
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          amount  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `float` This parameter should contain the payment amount of the particular transaction.  \* **Note**: Type-cast the amount to float type
        </td>

        <td style={{ textAlign: "left" }}>
          1000
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          productinfo  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `varchar` This parameter should contain a brief product description. It should be a string describing the product.  `Character limit`: 100
        </td>

        <td style={{ textAlign: "left" }}>
          Time Magazine Subscription
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          firstname  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `varchar` Must contain the first name of the customer.  `Character limit`: 60
        </td>

        <td style={{ textAlign: "left" }}>
          Ashish
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          email  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `varchar` Must contain the email of the customer.  This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information.  Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.  Character limit: 50
        </td>

        <td style={{ textAlign: "left" }}>
          [Ashish@test.com](mailto:Ashish@test.com)
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          phone  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `varchar` Must contain the phone number of the customer.  This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.  Character limit: 50
        </td>

        <td style={{ textAlign: "left" }}>
          9843176540
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          surl  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          surl is the acronym for Success URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is successful.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          furl  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          furl is the acronym for for Failure URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is failed.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          pg  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          It defines the payment category for which you wish to perform UPI One-Time Mandate. For UPI, **pg= UPI**
        </td>

        <td style={{ textAlign: "left" }}>
          UPI
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          bankcode  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          It defines the bank with which you wish to perform UPI using the bank code. Use **UPI** or **INTENT** according to the use case.
        </td>

        <td style={{ textAlign: "left" }}>
          * **UPI**: Used for UPI Collect
          * **INTENT**: Used for UPI Intent
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          vpa  `mandatory for UPI Collect`
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the customer's VPA handle. For the list UPI handles supported, refer to UPI Handles  The merchant is advised to check the validity of the VPA through using the VPA Validation API. PayU extends support for the same if required. For more information on using VPA Validation API, refer to

          [Validate VPA API](ref:validate_vpa_api)

          .
        </td>

        <td style={{ textAlign: "left" }}>
          abc\@payu
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          pre\_authorize  `mandatory for Pre-Auth`
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter is set to **1** to pre-authorize payment.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          si\_Details
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the following information in JSON format:  \* paymentStartDate  \* paymentEndDate
          **Example**: `{"paymentStartDate":"2024-07-24","paymentEndDate":"2024-07-28"}`
        </td>

        <td style={{ textAlign: "left" }}>
          `{"paymentStartDate":"2024-07-24","paymentEndDate":"2024-07-28"}`
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          hash  `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          Hash is a crucial parameter used to ensure that any date is not tampered while redirecting customer from the merchant website to PayU's payment interface while registration transactions. It is SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si\_details by merchant salt.  In the case of registration transaction, the formula is used to calculate this hash is similar to the following:
          SHA512(sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|||SALT))
        </td>

        <td style={{ textAlign: "left" }}>
          txnid
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  #### Intent Flow

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

  #### Collect Flow

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
</Accordion>

## Step 2: Check PayU Responses

When you initiate a pre-auth transaction request:

* The PayU response contains the intentURIData parameter
* For success cases, this provides a URL to invoke the intent

<Accordion title="Intent Flow" icon="fa-code">
  \####Success scenario

  ```
  {
    "metaData": {
      "message": null,
      "referenceId": "c5161bae370de1bd4fb886c6c66567a8",
      "statusCode": null,
      "txnId": "a7440cc636e747b635df",
      "txnStatus": "pending",
      "unmappedStatus": "pending"
    },
    "result": {
      "paymentId": "99900000000001875",
      "merchantName": "Name409208872",
      "merchantVpa": "paytmqr@icici",
      "amount": "10000.00",
      "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vcHA3OHNlY3VyZS5wYXl1LmluLzY1OWFjNWRhNWUyZjlmNzM1NzhkZWYwYzVjNDM2MWFmOWJhMGVkYmExYjk3NDg2Mjg3ZDI2MzBjZDg1YmU3NWEvaW50ZW50U2VhbWxlc3NIYW5kbGVyLnBocCIgbWV0aG9kPSJwb3N0Ij48aW5..."
      },
      "otpPostUrl": "https://pp78secure.payu.in/ResponseHandler.php"
    }
  }
  ```

  **Failure scenario**

  For Intent, as part of response, Intent URL is returned. Now merchant needs to use data received in intentURIData parameter, JSON decode the response and use URL to invoke intent at their end

  Once the transaction is authorised by the customer, PayU will receive confirmation. Same will be passed to the merchant as webhook

  ```
  {
    "metaData": {
      "message": "Transaction failed due to invalid params shared by the merchant",
      "referenceId": "dde7096af9db932a9fd09b9b4383d8be",
      "statusCode": "E1101",
      "txnId": "0c4931ddee7a4f69227f",
      "txnStatus": "failed",
      "intentURIData": "upi://mandate?pa=payu24@icici&pn=Payu&tr=EZM2024042211452400151942&am=10000.00&cu=INR&orgid=400011&mc=6012&purpose=01&tn=Upi%20Mandate&validitystart=22042024&validityend=21052024&amrule=MAX&Recur=ONETIME&Rev=N&Share=Y&Block=Y&txnType=CREATE&mode=13",
      "unmappedStatus": "failure"
    },
    "result": {}
  }
  ```
</Accordion>

<Accordion title="Collect Flow" icon="fa-code">
  \####Success scenario

  ```
  mihpayid=6MAESTROMAESTRO5&mode=UPI&status=success&key=travelibibo&txnid=8286f8e3954bf669c02e&amount=10000.00&addedon=2024-04-22 15:48:45&productinfo=Product Info&firstname=CARDHOLDERXXXXXXXXNAME-Admin&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=test@example.com&phone=##########&udf1=&udf2=&udf3=&udf4=Created&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&card_token=&card_no=&field0=&field1=sur***@icici&field2=&field3=sur***icici&field4=ICICI Test Vpa&field5=3159219e58ed45eda39e8914b998401a@icici&field6=rambo|_mobilenum_&field7=00|APPROVED OR COMPLETED SUCCESSFULLY&field8=&field9=APPROVED OR COMPLETED SUCCESSFULLY|Completed Using Callback&payment_source=payuPureS2S&PG_TYPE=UPI-PG&error=E000&error_Message=No Error&net_amount_debit=10000&discount=0.00&unmappedstatus=auth&hash=3ca863c1c8148baa13891f6e8e124c07f909d9fa14d6757acc01b08b736c35bbdae9845fa445cdaf22fb190f717285d0d09c02508bbfe081b4833eaf5637ec03&bank_ref_no=410901015475&bank_ref_num=410901015475&bankcode=UPI&surl=http://local.admin.payu.in/test_response&curl=http://local.admin.payu.in/test_response&furl=http://local.admin.payu.in/test_response 
  ```

  Formatted response:

  ```
  mihpayid: 6MAESTROMAESTRO5
  mode: UPI
  status: success
  key: travelibibo
  txnid: 8286f8e3954bf669c02e
  amount: 10000.00
  addedon: 2024-04-22 15:48:45
  productinfo: Product Info
  firstname: CARDHOLDERXXXXXXXXNAME-Admin
  lastname: 
  address1: 
  address2: 
  city: 
  state: 
  country: 
  zipcode: 
  email: test@example.com
  phone: ##########
  udf1: 
  udf2: 
  udf3: 
  udf4: Created
  udf5: 
  udf6: 
  udf7: 
  udf8: 
  udf9: 
  udf10: 
  card_token: 
  card_no: 
  field0: 
  field1: sur***@icici
  field2: 
  field3: sur***@icici
  field4: ICICI Test Vpa
  field5: 3159219e58ed45eda39e8914b998401a@icici
  field6: rambo|_mobilenum_
  field7: 00|APPROVED OR COMPLETED SUCCESSFULLY
  field8: 
  field9: APPROVED OR COMPLETED SUCCESSFULLY|Completed Using Callback
  payment_source: payuPureS2S
  PG_TYPE: UPI-PG
  error: E000
  error_Message: No Error
  net_amount_debit: 10000
  discount: 0.00
  unmappedstatus: auth
  hash: 3ca863c1c8148baa13891f6e8e124c07f909d9fa14d6757acc01b08b736c35bbdae9845fa445cdaf22fb190f717285d0d09c02508bbfe081b4833eaf5637ec03
  bank_ref_no: 410901015475
  bank_ref_num: 410901015475
  bankcode: UPI
  surl: http://local.admin.payu.in/test_response
  curl: http://local.admin.payu.in/test_response
  furl: http://local.admin.payu.in/test_response
  ```
</Accordion>

## Step 3: Capture Pre-Authorized Payment

<Verify_Payment_Tabs />

<br />

<Callout icon="📘" theme="info">
  **Notes**:

  * The **unamappedstatus** to **auth** can be checked using thje <Anchor label="Verify Payment API" target="_blank" href="ref:verify_payment_api">Verify Payment API</Anchor> and in callback response in the Transaction callback.
  * To check the status of the Auth Request and then Capture Request sent, use the **check_action_status** API. For more information,  refer to  <Anchor label="Check Refund Status API with Request ID" target="_blank" href="ref:check_action_status_api_with_request_id">Check Refund Status API with Request ID</Anchor>.
  * If you want to cancel or refund a pre-authorized payment, refer to [Cancel a Pre-Authorized Payment](doc:cancel-a-pre-authorized-payment).
</Callout>

<Callout icon="👍" theme="okay">
  **Reference**: For cancelling pre-auth payments, refer to <Anchor label="Cancel a Pre-Authorized Transaction API" target="_blank" href="ref:cancel-a-pre-authorized-transaction">Cancel a Pre-Authorized Transaction API</Anchor>.
</Callout>
