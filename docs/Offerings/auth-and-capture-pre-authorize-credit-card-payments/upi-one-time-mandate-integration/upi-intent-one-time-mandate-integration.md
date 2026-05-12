---
title: UPI Intent OTM - Merchant Hosted
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
The merchant initiates a call to PayU with the SI details, pg., bankcode, and pre-authorization amount. This amount is considered the Block Amount. Using these details, PayU will then relay the callback with the current status to the merchant.

The **pre_authorize** parameter is used for pre-authorize payments using the seamless integration with the **_payment** API.

<Callout icon="👍" theme="okay">
  Experience the end-to-end **Merchant Hosted Checkout**> **UPI** flow and instantly generate the complete code for seamless, zero-coding integration into your website.

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

                      <button onclick="window.open('https://payu.in/integrationlab/seamless/sm-otm', '_blank')" 
                              class="tooltip-btn" 
                              data-tooltip="Click here to see the Merchant Hosted Checkout > UPI end-to-end integration and instantly generate the complete code needed for a zero-coding setup on your website.">
                          Experience the flow and get the code
                      </button>
  `}</HTMLBlock>
</Callout>

<br />

**Steps to integrate**

<Cards columns={2}>
  <Card title="1. Post the Pre-Auth Transaction Request" href="#step-1-post-the-pre-auth-transaction-request">
    Submit the pre-authorization transaction request to PayU for payment hold

    <br />
  </Card>

  <Card title="2. Check the Response from PayU" href="#step-2-check-the-response-from-payu">
    Handle and process the response received from PayU after pre-auth request submission

    <br />
  </Card>

  <Card title="3. Capture a Pre-Authorized Payment" href="#step-3-capture-a-pre-authorized-payment">
    Complete the payment capture process for the pre-authorized transaction
  </Card>

  <Card title="4. Check Transaction Status" href="#step-4-check-transaction-status">
    Verify the current status of the transaction and confirm payment completion

    <br />
  </Card>
</Cards>

## Step 1: Post the Pre-Auth transaction request

Post the additional parameters for with the Pre-Authorization using the Merchant Hosted Checkout.

<Accordion title="Request parameters" icon="fa-code">
  **Environment**

  |                            |                                                                         |
  | :------------------------- | :---------------------------------------------------------------------- |
  | **Test Environment**       | \<[https://test.payu.in/\_payment>](https://test.payu.in/_payment>)     |
  | **Production Environment** | \<[https://secure.payu.in/\_payment>](https://secure.payu.in/_payment>) |

  The **pre\_authorize** parameter as specified is used to pre-authorize payments using the Merchant Hosted Checkout integration with the **\_payment** API.

  <HTMLBlock>{`
                 <table border="1" cellpadding="6" cellspacing="0">
                   <thead>
                     <tr>
                       <th>Parameter</th>
                       <th>Description</th>
                       <th>Example</th>
                     </tr>
                   </thead>
                   <tbody>
                     <tr>
                       <td>
                         key <br>
                         <code>mandatory</code>
                       </td>
                       <td>
                         <code>varchar</code> This parameter is the unique Merchant Key provided by PayU for your merchant account.
                       </td>
                       <td>
                         Your Test Key
                       </td>
                     </tr>
                     <tr>
                       <td>
                         txnid <br>
                         <code>mandatory</code>
                       </td>
                       <td>
                         <code>varchar</code> This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction.<br>
                         <b>Character limit</b>: 25<br>
                         <b>Note:</b> Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID.'
                       </td>
                       <td>
                         fd3e847h2
                       </td>
                     </tr>
                     <tr>
                       <td>
                         amount <br>
                         <code>mandatory</code>
                       </td>
                       <td>
                         <code>float</code> This parameter should contain the payment amount of the particular transaction.<br>
                         <b>Note:</b> Type-cast the amount to float type
                       </td>
                       <td>
                         1000
                       </td>
                     </tr>
                     <tr>
                       <td>
                         productinfo <br>
                         <code>mandatory</code>
                       </td>
                       <td>
                         <code>varchar</code> This parameter should contain a brief product description. It should be a string describing the product.<br>
                         <b>Character limit</b>: 100
                       </td>
                       <td>
                         Time Magazine Subscription
                       </td>
                     </tr>
                     <tr>
                       <td>
                         firstname <br>
                         <code>mandatory</code>
                       </td>
                       <td>
                         <code>varchar</code> Must contain the first name of the customer.<br>
                         <b>Character limit</b>: 60
                       </td>
                       <td>
                         Ashish
                       </td>
                     </tr>
                     <tr>
                       <td>
                         email <br>
                         <code>mandatory</code>
                       </td>
                       <td>
                         <code>varchar</code> Must contain the email of the customer.<br>
                         This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information.<br>
                         Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.<br>
                         <b>Character limit</b>: 50
                       </td>
                       <td>
                         <a href="mailto:Ashish@test.com">Ashish@test.com</a>
                       </td>
                     </tr>
                     <tr>
                       <td>
                         phone <br>
                         <code>mandatory</code>
                       </td>
                       <td>
                         <code>varchar</code> Must contain the phone number of the customer.<br>
                         This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.<br>
                         <b>Character limit</b>: 50
                       </td>
                       <td>
                         9843176540
                       </td>
                     </tr>
                     <tr>
                       <td>
                         surl <br>
                         <code>mandatory</code>
                       </td>
                       <td>
                         surL is the acronym for Success URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is successful.
                       </td>
                       <td></td>
                     </tr>
                     <tr>
                       <td>
                         furl <br>
                         <code>mandatory</code>
                       </td>
                       <td>
                         furl is the acronym for for Failure URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is failed.
                       </td>
                       <td></td>
                     </tr>
                     <tr>
                       <td>
                         pg <br>
                         <code>mandatory</code>
                       </td>
                       <td>
                         It defines the payment category for which you wish to perform UPI One-Time Mandate integration. For UPI, <b>pg = UPI</b>
                       </td>
                       <td>
                         UPI
                       </td>
                     </tr>
                     <tr>
                       <td>
                         bankcode <br>
                         <code>mandatory</code>
                       </td>
                       <td>
                         It defines the bank with which you wish to perform UPI Intent One-Time Mandate integration using the bank code. For UPI Intent, use <b>INTENT</b>.
                       </td>
                       <td>
                         UPI
                       </td>
                     </tr>
                     <tr>
                       <td>
                         txn_s2s_flow <br>
                         <code>mandatory</code>
                       </td>
                       <td>
                         This parameter must be passed with the values as <b>4</b> for UPI Intent.
                       </td>
                       <td></td>
                     </tr>
                     <tr>
                       <td>
                         pre_authorize <br>
                         <code>mandatory for Pre-Auth</code>
                       </td>
                       <td>
                         This parameter is set to <b>1</b> to pre-authorize payment.
                       </td>
                       <td>
                         1
                       </td>
                     </tr>
                     <tr>
                       <td>
                         si_details
                       </td>
                       <td>
                         This parameter contains the following information in JSON format:
                         <ul>
                           <li>paymentStartDate</li>
                           <li>paymentEndDate</li>
                         </ul>
                         <b>Example</b>: <br>
                         <code>{"paymentStartDate":"2024-07-24","paymentEndDate":"2024-07-28"}</code>
                       </td>
                       <td>
                         <code>{"paymentStartDate":"2024-07-24","paymentEndDate":"2024-07-28"}</code>
                       </td>
                     </tr>
                     <tr>
                       <td>
                         hash <br>
                         <code>mandatory</code>
                       </td>
                       <td>
                         Hash is a crucial parameter used to ensure that any data is not tampered while redirecting customer from the merchant website to PayU's payment interface while registration transactions.<br>
                         It is SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si_details by merchant salt.<br>
                         In the case of registration transaction, the formula used to calculate this hash is similar to the following:<br>
                         <code>HASH = SHA512(sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT))</code>
                       </td>
                       <td></td>
                     </tr>
                   </tbody>
                 </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Hashing" icon="fa-code">
  You must hash the request parameters using the following hash logic:

  ```
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
  ```

  For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted).
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```
  curl --request POST  

  --url https://test.payu.in/_payment  
  --header 'accept: text/plain'  
  --header 'content-type: application/x-www-form-urlencoded'  
  --data key=JPM7Fg  
  --data pg=UPI  
  --data bankcode=INTENT 
  --data txn_s2s_flow=4  
  --data txnid=aso6787  
  --data siDetails="{"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"}"  
  --data pre_authorize=1 \ 
   --data amount=100.00  
  --data productinfo=iPhone  
  --data firstname=Ashish  
  --data email=ashish@abc.com  
  --data phone=9876543210  
  --data surl=https://apiplayground-response.herokuapp.com/  
  --data furl=https://apiplayground-response.herokuapp.com/  
  --data hash=8e8de8a3cf2ba999e16c0ffdb63a645074af4ad1aa0a8d66d81555a119c004e1791173fe6199084f256623664b250d3aeb50fc2c4cfc155e729d8811a157c98b 
  ```

  <br />
</Accordion>

## Step 2: Check the response from PayU

<Accordion title="Success scenario" icon="fa-code">
  For Intent, as part of response, Intent URL is returned. Now, merchant needs to use data received in intentURIData parameter, JSON decode the response and use URL to invoke intent at their end

  ```curl
  {
    "metaData": {
      "message": null,
      "referenceId": "test123",
      "statusCode": null,
      "txnId": "test989",
      "txnStatus": "pending",
      "unmappedStatus": "pending"
    },
    "result": {
      "paymentId": "99999999",
      "merchantName": "abc",
      "merchantVpa": "abc@sbi",
      "amount": "166.00",
      "intentURIData": "upi://mandate?pa=abc@upi&pn=abc&mn=ONETIME&tid=test123&validitystart=02102024&validityend=15112024&am=166.00&amrule=MAX&recur=ONETIME&tr=test989&cu=INR&mc=6300&tn=UPIIntent&mode=13&purpose=01&orgid=400011&rev=N&block=Y&txnType=CREATE",
      "acsTemplate": "PGh0bWw+PGJvZH... (truncated for brevity)",
      "otpPostUrl": "https://pp78secure.payu.in/ResponseHandler.php"
    }
  }

  ```
</Accordion>

<Accordion title="Failure scenarios" icon="fa-code">
  After the transaction is authorised by the customer, PayU will receive confirmation. Same will be passed to the merchant as webhook.

  ```
  {
    "metaData": {
      "message": "Transaction failed due to invalid params shared by the merchant",
      "referenceId": "dde7096af9db932a9fd09b9b4383d8be",
      "statusCode": "E1101",
      "txnId": "0c4931ddee7a4f69227f",
      "txnStatus": "failed",
      "unmappedStatus": "failure"
    },
    "result": {}
  }
  ```
</Accordion>

## Step 3: Capture a pre-authorized payment

To capture a pre-authorized payment, use the following command. After the API command is successful, the transaction would be captured and settled to you.=

<Accordion title="Sample request" icon="fa-code">
  ```
  curl --location --request POST 'https://info.payu.in/merchant/postservice.php?form=2' --header 'Content-Type: application/x-www-form-urlencoded' --form 'key="JF***g"' --form 'command="capture_transaction"' --form 'hash="67411736ab98c59522492a12751a6015c41b87764019f9dc14052690c2c7af9095d31002fc109dcf3596c2f38792d56db6f6207b1989010f2adf51c144fa3019"' --form 'var1="15246574846"' --form 'var2="authorizeTransaction123"' --form 'var3="1"'

  ```
</Accordion>

<Accordion title="Sample response" icon="fa-code">
  ```
  {  
      "status": 1,  
      "msg": "Capture Request Queued",  
      "request_id": "Request ID",  
      "bank_ref_num": "Bank Reference Number"  
  } 
  ```
</Accordion>

## Step 4: Check Transaction Status

<Verify_Payment_Tabs />

<Callout icon="👍" theme="okay">
  **Reference**: For cancelling pre-auth payments, refer to [Cancel a Pre-Authorized Transaction API](ref:cancel-a-pre-authorized-transaction).
</Callout>
