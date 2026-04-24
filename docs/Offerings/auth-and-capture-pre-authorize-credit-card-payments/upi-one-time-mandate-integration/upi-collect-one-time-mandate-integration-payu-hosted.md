---
title: UPI Collect OTM - PayU Hosted
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
The merchant initiates a call to PayU with the SI details, pg, bankcode, and pre-authorization amount. This amount is considered the Block Amount. Using these details, PayU will then relay the callback with the current status to the merchant.

The **pre_authorize** parameter is used for pre-authorize payments using the seamless integration with the **_payment** API.

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

  <Card title="3. Capture a Pre-Authorized Payment" href="s#step-3-capture-a-pre-authorized-payment">
    Complete the payment capture process for the pre-authorized transaction
  </Card>

  <Card title="4. Check Transaction Status" href="#step-4-check-transaction-status">
    Verify the current status of the transaction and confirm payment completion

    <br />
  </Card>
</Cards>

## Step 1: Post the Pre-Auth transaction request

Post the additional parameters for with the Pre-Authorization using the Merchant Hosted Checkout. For API Reference, refer to [UPI One-Time Mandate Consent API](ref:upi-one-time-mandate-transaction-api-payu-hosted).

**Environment**

|                            |                                                                     |
| :------------------------- | :------------------------------------------------------------------ |
| **Test Environment**       | [https://test.payu.in/_payment](https://test.payu.in/_payment)      |
| **Production Environment** | [https://secure.payu.in/_payment>](https://secure.payu.in/_payment) |

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key
        `mandatory`
      </td>

      <td>
        `varchar` This parameter is the unique Merchant Key provided by PayU for your merchant account.
      </td>

      <td>
        Your Test Key
      </td>
    </tr>

    <tr>
      <td>
        txnid
        `mandatory`
      </td>

      <td>
        `varchar` This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction.
        `Character limit`: 25

        * _Note_*: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID.'
      </td>

      <td>
        fd3e847h2
      </td>
    </tr>

    <tr>
      <td>
        amount
        `mandatory`
      </td>

      <td>
        `float` This parameter should contain the payment amount of the particular transaction.

        * _Note_*: Type-cast the amount to float type
      </td>

      <td>
        1000
      </td>
    </tr>

    <tr>
      <td>
        productinfo
        `mandatory`
      </td>

      <td>
        `varchar` This parameter should contain a brief product description. It should be a string describing the product.
        `Character limit`: 100
      </td>

      <td>
        Time Magazine Subscription
      </td>
    </tr>

    <tr>
      <td>
        firstname
        `mandatory`
      </td>

      <td>
        `varchar` Must contain the first name of the customer.
        `Character limit`: 60
      </td>

      <td>
        Ashish
      </td>
    </tr>

    <tr>
      <td>
        email
        `mandatory`
      </td>

      <td>
        `varchar` Must contain the email of the customer.
        This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information.
        Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.
        Character limit: 50
      </td>

      <td>
        [Ashish@test.com](mailto:Ashish@test.com)
      </td>
    </tr>

    <tr>
      <td>
        phone
        `mandatory`
      </td>

      <td>
        `varchar` Must contain the phone number of the customer.

        This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.
        Character limit: 50
      </td>

      <td>
        9843176540
      </td>
    </tr>

    <tr>
      <td>
        surl
        `mandatory`
      </td>

      <td>
        surL is the acronym for Success URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is successful.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        furl
        `mandatory`
      </td>

      <td>
        furl is the acronym for for Failure URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is failed.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        txn_s2s_flow
        `mandatory`
      </td>

      <td>
        This parameter must be passed with the values as **4** for UPI Intent.
      </td>

      <td>
        4
      </td>
    </tr>

    <tr>
      <td>
        pre_authorize
        `mandatory for Pre-Auth`
      </td>

      <td>
        This parameter is set to**1** to pre-authorize payment.
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

        * paymentStartDate
        * paymentEndDate**Example**:  \{"paymentStartDate":"2024-07-24","paymentEndDate":"2024-07-28"}
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        hash
        `mandatory`
      </td>

      <td>
        Hash is a crucial parameter used to ensure that any date is not tampered while redirecting customer from the merchant website to PayU's payment interface while registration transactions.

        It is SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si_details by merchant salt.

        In the case of registration transaction, the formula is used to calculate this hash is similar to the following:
        `HASH = sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

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
</Accordion>

## Step 2: Check the response from PayU

On receiving valid request over PayU's payment interface (_payment), PayU returns:

<Accordion title="Sample response" icon="fa-code">
  ```text
  mihpayid=6MAESTROMAESTRO5&mode=UPI&status=success&key=travelibibo&txnid=8286f8e3954bf669c02e&amount=10000.00&addedon=2024-04-22 15:48:45&productinfo=Product Info&firstname=CARDHOLDERXXXXXXXXNAME-Admin&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=test@example.com&"phone":"##########"&udf1=&udf2=&udf3=&udf4=Created&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&card_token=&card_no=&field0=&field1=sur***@icici&field2=&field3=sur***icici&field4=ICICI Test Vpa&field5=3159219e58ed45eda39e8914b998401a@icici&field6=rambo|_mobilenum_&field7=00|APPROVED OR COMPLETED SUCCESSFULLY&field8=&field9=APPROVED OR COMPLETED SUCCESSFULLY|Completed Using Callback&payment_source=payuPureS2S&PG_TYPE=UPI-PG&error=E000&error_Message=No Error&net_amount_debit=10000&discount=0.00&unmappedstatus=auth&hash=3ca863c1c8148baa13891f6e8e124c07f909d9fa14d6757acc01b08b736c35bbdae9845fa445cdaf22fb190f717285d0d09c02508bbfe081b4833eaf5637ec03&bank_ref_no=410901015475&bank_ref_num=410901015475&bankcode=UPI&surl=http://local.admin.payu.in/test_response&curl=http://local.admin.payu.in/test_response&furl=http://local.admin.payu.in/test_response 
  ```

  The formatted response is similar to the file:

  ```
  # PayU Hosted Checkout Response (v1)

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

## Step 3: Capture a pre-authorized payment

To capture a pre-authorized payment, use the following command. After the API command is successful, the transaction would be captured and settled to you.=

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

## Step 4: Check Transaction Status

<Verify_Payment_Tabs />

<br />

<Callout icon="👍" theme="okay">
  **Reference**: For cancelling pre-auth payments, refer to [Cancel a Pre-Authorized Transaction API](ref:cancel-a-pre-authorized-transaction).
</Callout>