---
title: UPI Intent and Collect Autopay - TPV Integration
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
For recurring payment use-case, you can use UPI as a payment instrument. It requires, registration of the mandate and then doing the debit in the customer's account. During registration, customer validates the billing details of the mandate on the respective application, enters their MPIN (Mobile PIN) and authorizes the mandate. After the registration transaction is successful, you can then use the **Recurring Payment Transaction** API to charge the customer without requiring further intervention. For more information on Recurring Payment API, refer to  [Recurring Payment Transaction API](ref:recurring_payment_api)

The Third-Party Verification (TPV) functionality is now being added to the UPI Autopay too.

> 📘 Notes:
>
> * Currently, PayU supports UPI Autopay only with Seamless integration.
> * Contact your PayU Key Account Manager (KAM) or [PayU Support ](https://help.payu.in)to activate this feature.

**Steps to integrate**

<Cards columns={2}>
  <Card title="1. Validate VPA" href="#step-1-validate-vpa">
    Validate customer's Virtual Payment Address (UPI handle)

    <br />
  </Card>

  <Card title="2. Post Parameters" href="#step-2-post-the-parameters-to-payu">
    Post transaction request with SI and beneficiary details

    <br />
  </Card>

  <Card title="3. Check Response" href="#step-3-check-the-response-from-payu">
    Validate the response and reverse hash from PayU

    <br />
  </Card>

  <Card title="4. Verify Payment" href="#step-4-verify-the-payment">
    Verify the payment using verify\_payment API
  </Card>
</Cards>

## Use Cases

Merchants have use cases, which requires the transactions to be allowed only for selected accounts only. These accounts are provided by the customer before hand (during customer registration on merchant platform). Few merchant use cases are:

* Mutual Funds (SEBI guideines)
* Loan Repayment

However, as part of UPI, customer has the flexibility to link multiple accounts under the same VPA and on run-time, change the account for authorisation. So using TPV services, merchant makes sure that customer authorises the transaction using pre-registered accounts only.

## Steps to Integrate

Refer any of the following tabs based on the Intent or Collect Autopay Flow integration:

<Tabs>
  <Tab title="Intent Autopay TPV">
    ### Intent Autopay Workflow

    The merchant initiates the call to PayU with SI details, **bankcode** as **INTTPV**, and account number + IFSC details. PayU then initiates a mandate call to the bank, including all the SI and account-related parameters. The bank responds to PayU with a reference-Id, which PayU passes to the merchant in an Intent URL. When the customer authorizes the transaction, the bank will validate the account. If the account details match, a success message will be sent to PayU. However, if the account details do not match, Bank will pass validation error to PayU. Internally, Bank will cancel the mandate that has been setup on customer's account.

    <Callout icon="📘" theme="info">
      **Note**: Validation is done only in the registration step of the mandate. If the account matches, rest of the journey for UPI Autopay will remain as-is.
    </Callout>

    <Callout icon="📘" theme="info">
      **Prerequisites**

      S2S (Seamless) integration has to be done as per the standard kit. For more information, refer to [UPI Integrations - S2S](doc:upi-integrations-s2s).

      **Supported only in Seamless integration**: Currently, PayU supports UPI Intent Autopay only with Seamless integration.
    </Callout>

    ## Step 1: Validate VPA

    When your customer makes payment through UPI, you can validate the customer's Virtual Payment Address (VPA) and then initiate payment. The **validateVpa** API is used to validate the UPI handle. Validate the VPA (UPI handle) using the **validateVpa** API.  For Try-It experience of **validateVpa** API, refer to <Anchor label="Validate VPA Handle API" target="_blank" href="ref:validate_vpa_api">Validate VPA Handle API</Anchor>.

    <GENERALAPIsEnvironment />

    <Accordion title="Sample request" icon="fa-code">
      **Validate VPA**
<Validate_VPA />
    </Accordion>

    <Accordion title="Sample response" icon="fa-reply">
      **Success scenario**

      if successfully validated:

      ```plaintext
      {
         "status":"SUCCESS",
         "vpa":"9999999999@upi",
         "isVPAValid":1,
         "isAutoPayVPAValid":1,
         "isAutoPayBankValid":"NA",
         "payerAccountName":"ABC"
      }
      ```

      > 📘 Notes:
      >
      > * The **payerAccountName** parameter can be empty or NA or will have a payer name based on the value given by the bank.
      > * If both **isVPAValid** and **isAutoPayVPAValid** is 1, you must initiate payment for Recurring Payments.
      > * Ignore the **isAutoPayBankValid** parameter in the response.

      **Failure scenarios**

      * If invalid VPA, the response is similar to the following:

      ```plaintext
      {
       "status":"SUCCESS","vpa":"abc@upi","isVPAValid":0,"payerAccountName":"NA"
      }  
      ```

      * Invalid VPA but handle supporting SI (Autopay):

      ```plaintext
      {
       "status":"SUCCESS","vpa":"abc@upi","isVPAValid":0,"isAutoPayVPAValid":1,"isAutoPayBankValid":"NA","payerAccountName":"NA"
      }
      ```

      * Customer valid but handle not supporting SI (Autopay):

      ```plaintext
      {
        "status":"SUCCESS","vpa":"xyz@freecharge","isVPAValid":1,"isAutoPayVPAValid":0,"isAutoPayBankValid":"NA","payerAccountName":"XYZ"
      }
      ```

      * Neither customer valid nor handle supporting Autopay:

      ```plaintext
      {
        "status":"SUCCESS","vpa":"xyz@freecharge","isVPAValid":0,"isAutoPayVPAValid":0,"isAutoPayBankValid":"NA","payerAccountName":"NA"
      }
      ```
    </Accordion>

    <Accordion title="Sample validation JS code" icon="fa-reply">
      ```javascript
      	// JavaScript example for VPA validation before payment submission
      // This should be run on your server, not client-side

      async function validateVpa(vpa) {
          try {
              // Get hash from server endpoint
              const hashResponse = await fetch('/generate-vpa-hash', {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/json' },
                  body: JSON.stringify({ vpa })
              });
              const { hash } = await hashResponse.json();
              
              // Validate VPA with PayU
              const response = await fetch('https://test.payu.in/merchant/postservice?form=2', {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                  body: new URLSearchParams({
                      key: 'YOUR_MERCHANT_KEY',
                      command: 'validateVPA',
                      var1: vpa, // VPA to validate
                      hash: hash
                  })
              });
              
              const result = await response.json();
              
              // Sample response:
              // {"status":1,"msg":"VPA is valid","isVPAValid":1,"isUPIBarredBank":0}
              // OR
              // {"status":0,"msg":"VPA is invalid","isVPAValid":0}
              
              return {
                  isValid: result.isVPAValid === 1,
                  message: result.msg
              };
          } catch (error) {
              console.error('VPA validation error:', error);
              return { isValid: false, message: 'Validation service error' };
          }
      }

      ```
      ```curl
      # Once you have the hash, make the API call

      curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -d "key=YOUR_MERCHANT_KEY" \
        -d "command=validateVPA" \
        -d "var1=customer@upi" \
        -d "hash=$HASH"

      ```
    </Accordion>

    ## Step 2: Post the parameters to PayU

    With the following parameters, make the transaction request with the customer's bank account number to the PayU using the Collect Payment (**\_payment**) API.

    **Environment**

    | Environment            | URL                                                                 |
    | ---------------------- | ------------------------------------------------------------------- |
    | Test Environment       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |
    | Production Environment | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |

    <Accordion title="Request parameters" icon="fa-code">
      In the merchant-initiated POST REQUEST, Hash is a mandatory parameter. It is critical to calculate the hash correctly and post it to PayU in the request.

      | Parameter                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Value                                                                                                                                           |
      | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
      | key<br/><code>mandatory</code>               | `String` The merchant key is a unique identifier for a merchant account in PayU's database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Your Test Key                                                                                                                                   |
      | api\_version<br/><code>optional</code>       | `String` The API version for this API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 7                                                                                                                                               |
      | txnid<br/><code>mandatory</code>             | `String` The transaction ID is a reference number for a specific order that is generated by the merchant. It is used to track the order and must be unique. PayU's system will not accept duplicate transaction IDs.                                                                                                                                                                                                                                                                                                                                                                                                                   | s7hhDQVWvbhBdN                                                                                                                                  |
      | amount<br/><code>mandatory</code>            | `String` This field should contain the payment amount for the transaction. The limit for recurring payments using UPI payment mode: \* **Auto-debit** is Rs.15000 (the auto-debit limit is higher for below listed purpose) \* **With PIN** is Rs.1,00,00 \* **Note**: The auto-debit limit for the following UPI recurring payments is one lakh rupees (Rs.1,00,000): \* Insurance premiums \* Credit card bill payments \* Insurance premium                                                                                                                                                                                         | 10.00                                                                                                                                           |
      | productinfo<br/><code>mandatory</code>       | `String` It should be a string containing a brief description of the product. `Character Limit-100`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | iPhone                                                                                                                                          |
      | firstname<br/><code>mandatory</code>         | `String` The first name of the customer. `Character Limit-60`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Ashish                                                                                                                                          |
      | email<br/><code>mandatory</code>             | `String` The email of the customer. `Character Limit-50`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [test@gmail.com](mailto:test@gmail.com)                                                                                                         |
      | phone<br/><code>mandatory</code>             | `String` The phone number of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 9876543210                                                                                                                                      |
      | lastname<br/><code>mandatory</code>          | `String` The last name of the customer. `Character Limit-60`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Verma                                                                                                                                           |
      | address1<br/><code>optional</code>           | `String` The first line of the billing address. `Character Limit-100`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai                                                                                         |
      | address2<br/><code>optional</code>           | `String` The second line of the billing address. `Character Limit-100`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 34 Saikripa-Estate, Tilak Nagar                                                                                                                 |
      | city<br/><code>optional</code>               | `String` The city where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Mumbai                                                                                                                                          |
      | state<br/><code>optional</code>              | `String` The state where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Maharashtra                                                                                                                                     |
      | country<br/><code>optional</code>            | `String` The country where your customer resides. `Character Limit-50`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | India                                                                                                                                           |
      | zipcode<br/><code>optional</code>            | `String` Billing address zip code is mandatory for the cardless EMI option. `Character Limit-20`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 400004                                                                                                                                          |
      | surl<br/><code>mandatory</code>             | `String` The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                       | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                  |
      | furl<br/><code>mandatory</code>              | `String` The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                           | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                  |
      | hash<br/><code>mandatory</code>              | `String` It is used to avoid the possibility of transaction tampering. For the hash checksum logic, refer to [Checksum Logic for Hash](#checksum-logic-for-hash).                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `eabec285da28fd 0e3054d41a4d24fe 9f7599c9d0b6664 6f7a9984303fd612 4044b6206daf831 e9a8bda28a6200d 318293a13d6c193 109b60bd4b4f8b09 c90972`      |
      | pg<br/><code>mandatory</code>                | `varchar` The **pg** parameter for UPI must be UPI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | UPI                                                                                                                                             |
      | bankcode<br/><code>mandatory</code>          | `varchar` This parameter contains UPITPV for UPI TPV Collect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | UPITPV                                                                                                                                          |
      | si<br/><code>mandatory</code>                | This parameter signifies a successful consent taken from the user by the merchant. This parameter must contain 1 for a successful consent. Without this parameter sent as 1, subscription cannot be set up.                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                 |
      | si\_details<br/><code>mandatory</code>       | This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU. \* **Note**: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers (for more details refer – [https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0)) This is a JSON object and it includes a set of fields. For more information, refer to [SI Parameter JSON Details](ref:si-parameter-json-details) |                                                                                                                                                 |
      | vpa<br/><code>mandatory</code>               | `varchar` This parameter contains the customer's VPA handle. For the list UPI handles supported, refer to [UPI Handles](doc:upi-handles) The merchant is advised to check the validity of the VPA through using the VPA Validation API. PayU extends support for the same if required. For more information on using VPA Validation API, refer to [Validate VPA Handle API](ref:validate_vpa_api).                                                                                                                                                                                                                                     | abc\@upi                                                                                                                                        |
      | beneficiarydetail<br/><code>mandatory</code> | This is a JSON format text and there should be key named **beneficiaryAccountNumber** with the list of account numbers and the ifscCode key with the list of corresponding IFSC codes (in the same order as provided in the beneficiaryAccountNumber key). You can post up to five account details in this parameter.                                                                                                                                                                                                                                                                                                                  | Refer to [beneficiarydetail JSON Object Fields](https://docs.payu.in/docs/net-banking-integration-for-tpv#beneficiarydetail-json-object-fields) |
    </Accordion>

    <Accordion title="beneficiarydetail JSON Object Fields" icon="fa-code">
      It must contain the list of account numbers and the ifscCode key with the list of corresponding IFSC codes (in the same order as provided in the beneficiaryAccountNumber key). You can post up to five account details in this parameter. For example:

      ```
      {"beneficiaryAccountNumber":"002001600674|00000031957292212|00000035955239352|00000035955239352",  
      "ifscCode":"KTKB0000046|KTKB0000023|KTKB0000035|KTKB0000035"}
      ```

      **Checksum Logic for Hash**

      The following hash logic must be used for the parameters posted:

      > 📘 si\_details parameter in Hashing:
      >
      > The **si\_details** parameter value will be at last or the last value to be appended.
      >
      > ```plaintext
      > key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3
      > |udf4|udf5||||||si_details|SALT
      > ```
    </Accordion>

    ## Step 3: Check the response from PayU

    <Accordion title="Hash Validation Logic for Payment Response (Reverse Hashing)" icon="fa-code">
      While sending the response, PayU takes the exact same parameters that were sent in the request (in reverse order) to calculate the hash and returns it to you. You must verify the hash and then mark a transaction as a success or failure. This is to make sure the transaction has not tampered within the response.

      The order of the parameters is similar to the following code block:

      ```
      sha512(SALT|si_details|status||||||udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
      ```
    </Accordion>

    <Accordion title="Response parameters" icon="fa-code">
      For the response parameter description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis#response-for-initial-server-to-server-request).

      > 📘 Store the mihpayid and txnid parameter values in response:
      >
      > PayU recommends you to make provisions to store the **mihpayid** and **txnid** parameter values (in the response) in your server as proof that TPV has been completed for a customer.
    </Accordion>

    <Accordion title="Sample response" icon="fa-code">
      * Success scenario

      On receiving valid request over PayU's payment interface (\_payment), PayU returns JSON object as response object similar to the following in COLLECT:

      ```
      {
         "metaData":{
            "message":null,
            "referenceId":"c5161bae370de1bd4fb886c6c66567a8",
            "statusCode":null,
            "txnId":"a7440cc636e747b635df",
            "txnStatus":"pending",
            "unmappedStatus":"pending"
         },
         "result":{
            "postToBank":{
               "useMethodGet":true
            },
            "issuerUrl":"https://api.payu.in/public/#/c5161bae370de1bd4fb886c6c66567a8/upiLoader"
         }
      }
      ```

      * Failure scenario

      ```
      {
         "metaData":{
            "message":"Transaction failed due to invalid params shared by the merchant",
            "referenceId":"dde7096af9db932a9fd09b9b4383d8be",
            "statusCode":"E1101",
            "txnId":"0c4931ddee7a4f69227f",
            "txnStatus":"failed",
            "unmappedStatus":"failure"
         },
         "result":{
            
         }
      }
      ```
    </Accordion>

    ## Step 4. Verify the payment

    <Verify_Payment_Tabs />
  </Tab>

  <Tab title="Collect Autopay TPV">
    ### Collect Autopay Workflow

    The merchant initiates the call to PayU with SI details, **bankcode** as **UPITPV**, and account number + IFSC details. PayU then initiates a mandate call with all the SI and account-related parameters to the bank. After the customer authorizes the mandate, the bank will validate the account. If the account details match, only then will the success notification be sent to PayU. However, if the account details do not match, Bank will pass validation error to PayU. Internally, Bank will cancel the mandate that has been setup on customer's account.

    > 📘 **Prerequisites**:
    >
    > S2S (Seamless) integration has to be done as per the standard kit. For more information, refer to [UPI Integrations - S2S](doc:upi-integrations-s2s).
    > **PayU Hosted Checkout note supported** Currently, PayU supports UPI Collect Autopay TPV Integration with Seamless integration only.

    ## Step 1: Validate VPA

    When your customer makes payment through UPI, you can validate the customer's Virtual Payment Address (VPA) and then initiate payment. The **validateVpa** API is used to validate the UPI handle. Validate the VPA (UPI handle) using the **validateVpa** API.  For Try-It experience of **validateVpa** API, refer to <Anchor label="Validate VPA Handle API" target="_blank" href="ref:validate_vpa_api">Validate VPA Handle API</Anchor>.

    <GENERALAPIsEnvironment />

    <Accordion title="Sample request" icon="fa-code">
      **Validate VPA**

      ```curl
      curl -X POST "https://test.payu.in/merchant/postservice?form=2" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&command=validateVPA&var1=9999999999@upi&hash=75bb573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472fff9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e"
      ```
    </Accordion>

    <Accordion title="Sample response" icon="fa-reply">
      **Success scenario**

      if successfully validated:

      ```plaintext
      {
         "status":"SUCCESS",
         "vpa":"9999999999@upi",
         "isVPAValid":1,
         "isAutoPayVPAValid":1,
         "isAutoPayBankValid":"NA",
         "payerAccountName":"ABC"
      }
      ```

      > 📘 Notes:
      >
      > * The **payerAccountName** parameter can be empty or NA or will have a payer name based on the value given by the bank.
      > * If both **isVPAValid** and **isAutoPayVPAValid** is 1, you must initiate payment for Recurring Payments.
      > * Ignore the **isAutoPayBankValid** parameter in the response.

      **Failure scenarios**

      * If invalid VPA, the response is similar to the following:

      ```plaintext
      {
       "status":"SUCCESS","vpa":"abc@upi","isVPAValid":0,"payerAccountName":"NA"
      }  
      ```

      * Invalid VPA but handle supporting SI (Autopay):

      ```plaintext
      {
       "status":"SUCCESS","vpa":"abc@upi","isVPAValid":0,"isAutoPayVPAValid":1,"isAutoPayBankValid":"NA","payerAccountName":"NA"
      }
      ```

      * Customer valid but handle not supporting SI (Autopay):

      ```plaintext
      {
        "status":"SUCCESS","vpa":"xyz@freecharge","isVPAValid":1,"isAutoPayVPAValid":0,"isAutoPayBankValid":"NA","payerAccountName":"XYZ"
      }
      ```

      * Neither customer valid nor handle supporting Autopay:

      ```plaintext
      {
        "status":"SUCCESS","vpa":"xyz@freecharge","isVPAValid":0,"isAutoPayVPAValid":0,"isAutoPayBankValid":"NA","payerAccountName":"NA"
      }
      ```
    </Accordion>

    <Accordion title="Sample validation JS code" icon="fa-reply">
      ```javascript
      	// JavaScript example for VPA validation before payment submission
      // This should be run on your server, not client-side

      async function validateVpa(vpa) {
          try {
              // Get hash from server endpoint
              const hashResponse = await fetch('/generate-vpa-hash', {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/json' },
                  body: JSON.stringify({ vpa })
              });
              const { hash } = await hashResponse.json();
              
              // Validate VPA with PayU
              const response = await fetch('https://test.payu.in/merchant/postservice?form=2', {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                  body: new URLSearchParams({
                      key: 'YOUR_MERCHANT_KEY',
                      command: 'validateVPA',
                      var1: vpa, // VPA to validate
                      hash: hash
                  })
              });
              
              const result = await response.json();
              
              // Sample response:
              // {"status":1,"msg":"VPA is valid","isVPAValid":1,"isUPIBarredBank":0}
              // OR
              // {"status":0,"msg":"VPA is invalid","isVPAValid":0}
              
              return {
                  isValid: result.isVPAValid === 1,
                  message: result.msg
              };
          } catch (error) {
              console.error('VPA validation error:', error);
              return { isValid: false, message: 'Validation service error' };
          }
      }

      ```
      ```curl
      # Once you have the hash, make the API call

      curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -d "key=YOUR_MERCHANT_KEY" \
        -d "command=validateVPA" \
        -d "var1=customer@upi" \
        -d "hash=$HASH"

      ```
    </Accordion>

    ## Step 2: Post the parameters to PayU

    With the following parameters, make the transaction request with the customer's bank account number to the PayU using the Collect Payment (**\_payment**) API.

    **Environment**

    | Environment            | URL                                                                 |
    | ---------------------- | ------------------------------------------------------------------- |
    | Test Environment       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |
    | Production Environment | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |

    <Accordion title="Request parameters" icon="fa-code">
      In the merchant-initiated POST REQUEST, Hash is a mandatory parameter. It is critical to calculate the hash correctly and post it to PayU in the request.

      | Parameter                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Value                                                                                                                                           |
      | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
      | key<br/><code>mandatory</code>               | `String` The merchant key is a unique identifier for a merchant account in PayU's database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Your Test Key                                                                                                                                   |
      | api\_version<br/><code>optional</code>       | `String` The API version for this API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 7                                                                                                                                               |
      | txnid<br/><code>mandatory</code>             | `String` The transaction ID is a reference number for a specific order that is generated by the merchant. It is used to track the order and must be unique. PayU's system will not accept duplicate transaction IDs.                                                                                                                                                                                                                                                                                                                                                                                                                   | s7hhDQVWvbhBdN                                                                                                                                  |
      | amount<br/><code>mandatory</code>            | `String` This field should contain the payment amount for the transaction. The limit for recurring payments using UPI payment mode: \* **Auto-debit** is Rs.15000 (the auto-debit limit is higher for below listed purpose) \* **With PIN** is Rs.1,00,00 \* **Note**: The auto-debit limit for the following UPI recurring payments is one lakh rupees (Rs.1,00,000): \* Insurance premiums \* Credit card bill payments \* Insurance premium                                                                                                                                                                                         | 10.00                                                                                                                                           |
      | productinfo<br/><code>mandatory</code>       | `String` It should be a string containing a brief description of the product. `Character Limit-100`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | iPhone                                                                                                                                          |
      | firstname<br/><code>mandatory</code>         | `String` The first name of the customer. `Character Limit-60`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Ashish                                                                                                                                          |
      | email<br/><code>mandatory</code>             | `String` The email of the customer. `Character Limit-50`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [test@gmail.com](mailto:test@gmail.com)                                                                                                         |
      | phone<br/><code>mandatory</code>             | `String` The phone number of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 9876543210                                                                                                                                      |
      | lastname<br/><code>mandatory</code>          | `String` The last name of the customer. `Character Limit-60`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Verma                                                                                                                                           |
      | address1<br/><code>optional</code>           | `String` The first line of the billing address. `Character Limit-100`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai                                                                                         |
      | address2<br/><code>optional</code>           | `String` The second line of the billing address. `Character Limit-100`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 34 Saikripa-Estate, Tilak Nagar                                                                                                                 |
      | city<br/><code>optional</code>               | `String` The city where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Mumbai                                                                                                                                          |
      | state<br/><code>optional</code>              | `String` The state where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Maharashtra                                                                                                                                     |
      | country<br/><code>optional</code>            | `String` The country where your customer resides. `Character Limit-50`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | India                                                                                                                                           |
      | zipcode<br/><code>optional</code>            | `String` Billing address zip code is mandatory for the cardless EMI option. `Character Limit-20`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 400004                                                                                                                                          |
      | surl<br/><code>mandatory</code>             | `String` The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                       | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                  |
      | furl<br/><code>mandatory</code>              | `String` The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                           | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                  |
      | hash<br/><code>mandatory</code>              | `String` It is used to avoid the possibility of transaction tampering. For the hash checksum logic, refer to [Checksum Logic for Hash](#checksum-logic-for-hash).                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `eabec285da28fd 0e3054d41a4d24fe 9f7599c9d0b6664 6f7a9984303fd612 4044b6206daf831 e9a8bda28a6200d 318293a13d6c193 109b60bd4b4f8b09 c90972`      |
      | pg<br/><code>mandatory</code>                | `varchar` The **pg** parameter for UPI must be UPI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | UPI                                                                                                                                             |
      | bankcode<br/><code>mandatory</code>          | `varchar` This parameter contains UPITPV for UPI TPV Collect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | UPITPV                                                                                                                                          |
      | si<br/><code>mandatory</code>                | This parameter signifies a successful consent taken from the user by the merchant. This parameter must contain 1 for a successful consent. Without this parameter sent as 1, subscription cannot be set up.                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                 |
      | si\_details<br/><code>mandatory</code>       | This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU. \* **Note**: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers (for more details refer – [https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0)) This is a JSON object and it includes a set of fields. For more information, refer to [SI Parameter JSON Details](ref:si-parameter-json-details) |                                                                                                                                                 |
      | vpa<br/><code>mandatory</code>               | `varchar` This parameter contains the customer's VPA handle. For the list UPI handles supported, refer to [UPI Handles](doc:upi-handles) The merchant is advised to check the validity of the VPA through using the VPA Validation API. PayU extends support for the same if required. For more information on using VPA Validation API, refer to [Validate VPA Handle API](ref:validate_vpa_api).                                                                                                                                                                                                                                     | abc\@upi                                                                                                                                        |
      | beneficiarydetail<br/><code>mandatory</code> | This is a JSON format text and there should be key named **beneficiaryAccountNumber** with the list of account numbers and the ifscCode key with the list of corresponding IFSC codes (in the same order as provided in the beneficiaryAccountNumber key). You can post up to five account details in this parameter.                                                                                                                                                                                                                                                                                                                  | Refer to [beneficiarydetail JSON Object Fields](https://docs.payu.in/docs/net-banking-integration-for-tpv#beneficiarydetail-json-object-fields) |
    </Accordion>

    <Accordion title="beneficiarydetail JSON Object Fields" icon="fa-code">
      It must contain the list of account numbers and the ifscCode key with the list of corresponding IFSC codes (in the same order as provided in the beneficiaryAccountNumber key). You can post up to five account details in this parameter. For example:

      ```
      {"beneficiaryAccountNumber":"002001600674|00000031957292212|00000035955239352|00000035955239352",  
      "ifscCode":"KTKB0000046|KTKB0000023|KTKB0000035|KTKB0000035"}
      ```

      **Checksum Logic for Hash**

      The following hash logic must be used for the parameters posted:

      > 📘 si\_details parameter in Hashing:
      >
      > The **si\_details** parameter value will be at last or the last value to be appended.
      >
      > ```plaintext
      > key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3
      > |udf4|udf5||||||si_details|SALT
      > ```
    </Accordion>

    ## Step 3: Check the response from PayU

    <Accordion title="Hash Validation Logic for Payment Response (Reverse Hashing)" icon="fa-code">
      While sending the response, PayU takes the exact same parameters that were sent in the request (in reverse order) to calculate the hash and returns it to you. You must verify the hash and then mark a transaction as a success or failure. This is to make sure the transaction has not tampered within the response.

      The order of the parameters is similar to the following code block:

      ```
      sha512(SALT|si_details|status||||||udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
      ```
    </Accordion>

    <Accordion title="Response parameters" icon="fa-code">
      For the response parameter description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis#response-for-initial-server-to-server-request).

      > 📘 Store the mihpayid and txnid parameter values in response:
      >
      > PayU recommends you to make provisions to store the **mihpayid** and **txnid** parameter values (in the response) in your server as proof that TPV has been completed for a customer.
    </Accordion>

    <Accordion title="Sample response" icon="fa-code">
      * Success scenario

      On receiving valid request over PayU's payment interface (\_payment), PayU returns JSON object as response object similar to the following in COLLECT:

      ```
      {
         "metaData":{
            "message":null,
            "referenceId":"c5161bae370de1bd4fb886c6c66567a8",
            "statusCode":null,
            "txnId":"a7440cc636e747b635df",
            "txnStatus":"pending",
            "unmappedStatus":"pending"
         },
         "result":{
            "postToBank":{
               "useMethodGet":true
            },
            "issuerUrl":"https://api.payu.in/public/#/c5161bae370de1bd4fb886c6c66567a8/upiLoader"
         }
      }
      ```

      * Failure scenario

      ```
      {
         "metaData":{
            "message":"Transaction failed due to invalid params shared by the merchant",
            "referenceId":"dde7096af9db932a9fd09b9b4383d8be",
            "statusCode":"E1101",
            "txnId":"0c4931ddee7a4f69227f",
            "txnStatus":"failed",
            "unmappedStatus":"failure"
         },
         "result":{
            
         }
      }
      ```
    </Accordion>

    ## Step 4. Verify the payment

    <Verify_Payment_Tabs />
  </Tab>
</Tabs>