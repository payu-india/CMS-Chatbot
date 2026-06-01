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

<Callout icon="👍" theme="okay">
  Automatically generate code including hashing for your eCommerce website to integrate UPI OTM - PayU Hosted Checkout with zero coding knowledge:

  <HTMLBlock>{`
                          <style>
                          .tooltip-btn {
                              position: relative;
                              background-color: #4CAF50;
                              color: white;
                              padding: 10px 20px;
                              border: none;
                              border-radius: 5px;
                              cursor: pointer;
                              font-weight: bold; /* Added this line */
                          }
                          .tooltip-btn:hover::after {
                              content: attr(data-tooltip);
                              position: absolute;
                              bottom: 125%;
                              left: 50%;
                              transform: translateX(-50%);
                              background-color: #333;
                              color: white;
                              padding: 5px 10px;
                              border-radius: 4px;
                              white-space: nowrap;
                              font-size: 12px;
                              z-index: 1;
                          }
                          </style>

                          <button onclick="window.open('https://payu.in/integrationlab/upiotm', '_blank')" 
                                  class="tooltip-btn" 
                                  data-tooltip="Automatically generate code including hashing for your eCommerce website to integrate One-Time Mandate - PayU Hosted Checkout with zero coding knowledge.">
                              Click Here to Generate Code
                          </button>
  `}</HTMLBlock>
</Callout>

## Step 1: Post the Pre-Authorization Request

**Environment**

<PaymentAPIEnvironment />

<Accordion title="Request parameters" icon="fa-code">
 | Parameter | Description | Example |
|---|---|---|
| key<br/><code>mandatory</code> | <code>varchar</code> This parameter is the unique Merchant Key provided by PayU for your merchant account. | Your Test Key |
| txnid<br/><code>mandatory</code> | <code>varchar</code> This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction. <code>Character limit</code>: 25<br/>**Note**: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID.' | fd3e847h2 |
| amount<br/><code>mandatory</code> | <code>float</code> This parameter should contain the payment amount of the particular transaction. **Note**: Type-cast the amount to float type. | 1000 |
| productinfo<br/><code>mandatory</code> | <code>varchar</code> This parameter should contain a brief product description. It should be a string describing the product. <code>Character limit</code>: 100. | Time Magazine Subscription |
| firstname<br/><code>mandatory</code> | <code>varchar</code> Must contain the first name of the customer. <code>Character limit</code>: 60. | Ashish |
| email<br/><code>mandatory</code> | <code>varchar</code> Must contain the email of the customer. This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information. Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions. Character limit: 50. | Ashish@test.com |
| phone<br/><code>mandatory</code> | <code>varchar</code> Must contain the phone number of the customer. This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information. Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions. Character limit: 50. | 9843176540 |
| surl<br/><code>mandatory</code> | surl is the acronym for Success URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is successful. | |
| furl<br/><code>mandatory</code> | furl is the acronym for Failure URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is failed. | |
| pg<br/><code>mandatory</code> | It defines the payment category for which you wish to perform UPI One-Time Mandate. For UPI, **pg= UPI**. | UPI |
| bankcode<br/><code>mandatory</code> | It defines the bank with which you wish to perform UPI using the bank code. Use **UPI** or **INTENT** according to the use case. | **UPI**: Used for UPI Collect<br/>**INTENT**: Used for UPI Intent |
| vpa<br/><code>mandatory for UPI Collect</code> | This parameter contains the customer's VPA handle. For the list of UPI handles supported, refer to UPI Handles. The merchant is advised to check the validity of the VPA through using the VPA Validation API. PayU extends support for the same if required. For more information on using VPA Validation API, refer to Validate VPA API. | abc@payu |
| pre_authorize<br/><code>mandatory for Pre-Auth</code> | This parameter is set to **1** to pre-authorize payment. | |
| si_Details | This parameter contains the following information in JSON format: paymentStartDate, paymentEndDate. **Example**: <code>{"paymentStartDate":"2024-07-24","paymentEndDate":"2024-07-28"}</code> | <code>{"paymentStartDate":"2024-07-24","paymentEndDate":"2024-07-28"}</code> |
| hash<br/><code>mandatory</code> | Hash is a crucial parameter used to ensure that any data is not tampered while redirecting the customer from the merchant website to PayU's payment interface during registration transactions. It is a SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si_details by merchant salt. The formula used to calculate this hash is: <code>SHA512(sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|SALT))</code> | txnid |

</Accordion>

<Accordion title="Sample request" icon="fa-code">
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

<Accordion title="Sample response" icon="fa-code">
  **Success scenario**

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

## Step 3: Capture a pre-authorized payment

To capture a pre-authorized payment, use the following command. After the API command is successful, the transaction would be captured and settled to you.

<Accordion title="Request parameters" icon="fa-code">
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
          <td>key <code>mandatory</code></td>
          <td>This parameter is the unique Merchant Key provided by PayU for your merchant account. The Merchant Key acts as the unique identifier (primary key) to identify a Merchant Account in our database.</td>
          <td>YbfVda</td>
        </tr>
        <tr>
          <td>command <code>mandatory</code></td>
          <td>For initiating a capture transaction, the value of the parameter will be passed as <strong>capture_transaction</strong></td>
          <td>capture_transaction</td>
        </tr>
        <tr>
          <td>hash <code>mandatory</code></td>
          <td>This parameter must contain the hash value to be calculated at merchant end. Hash logic for this API is:<br><code>sha512(key|command|var1|salt)</code></td>
          <td>5fcf2d7c2b...</td>
        </tr>
        <tr>
          <td>var1 <code>mandatory</code></td>
          <td>This parameter must contain the payuId that was generated by PayU as part of pre-authorize operation.</td>
          <td>403993715523409521</td>
        </tr>
        <tr>
          <td>var2 <code>mandatory</code></td>
          <td>This parameter contains the token, that is, merchant unique reference number.</td>
          <td>TXN123456789</td>
        </tr>
        <tr>
          <td>var3 <code>mandatory</code></td>
          <td>This parameter must contain the amount to be captured.</td>
          <td>100.00</td>
        </tr>
      </tbody>
    </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```
  curl --location --request POST 'https://info.payu.in/merchant/postservice.php?form=2' \   
   --header 'Content-Type: application/x-www-form-urlencoded' \   
   --form 'key="JF***g"' \   
   --form 'command="capture_transaction"' \   
   --form 'hash="67411736ab98c59522492a12751a6015c41b87764019f9dc14052690c2c7af9095d31002fc109dcf3596c2f38792d56db6f6207b1989010f2adf51c144fa3019"' \   
   --form 'var1="15246574846"' \   
   --form 'var2="authorizeTransaction123"' \   
   --form 'var3="1"'  

  ```
</Accordion>

<Accordion title="Sample response" icon="fa-code">
  ```
  {
    "msg": "Transaction Processed successfully",
    "status": 1,
    "result": {
      "payuid": 613345678912399031,
      "txnId": "upiAuthCapture_12",
      "amount": 10000.00,
      "merchantId": 3,
      "authpayuid": "3975",
      "status": "in progress",
      "mode": "UPIOTM",
      "bankRefNumber": "410700457030",
      "payerVpa": "surya@icici",
      "field5": "3159219e58ed45eda39e8914b998401a@icici",
      "field9": "0|Transaction Successful"
    }
  }
  ```
</Accordion>

## Step 4: Verify the payment

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