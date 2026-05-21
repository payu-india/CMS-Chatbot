---
title: Integrate Checkout Plus
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
PayU Checkout Plus is the most convenient way to collect payment on your website. Add the inline JS script to your website's header section, then call the bolt.launch() function and pass the transaction data objects when your customers click **Payment**. PayU will take care of the payment and returns to your page when it is done.

<Callout icon="👍" theme="okay">
  Experience the end-to-end **_Checkout Plus_** flow for instant, seamless website integration.

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
                                  font-weight: bold;
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

                              <button onclick="window.open('https://www.payu.in/integrationlab/checkoutplus', '_blank')"
                                  
                                   class="tooltip-btn"  >
                                  Explore the demo
                              </button>
  `}</HTMLBlock>
</Callout>

<Callout icon="📘" theme="info">
  **Note**: The Checkout Plus integration is not recommended for the app browsers. For example, WebView, Chrome Custom tab, etc. Although there is Redirection Web Checkout which can be integrated. For more information, refer to following:

  * Redirection-based Web Checkout: [PayU Hosted Checkout](https://docs.payu.in/docs/prebuilt-checkout-payu-hosted).
  * [Webview configurations](https://docs.payu.in/docs/integrate-webview-for-mobile-apps-checkout-plus/)
</Callout>

***

**Steps to integrate**

<Cards cols={3}>
  <Card title="Add Meta-tags & Scripts" icon="fa-file-code">
    Add the required meta tags and inline scripts in your HTML header to initialize PayU.
  </Card>
  <Card title="Pass Transaction Request Objects" icon="fa-layer-group">
    Configure and pass the transaction request objects with all necessary payment parameters.
  </Card>
  <Card title="Fetch Response via responseHandler" icon="fa-reply">
    Implement the responseHandler function to capture and process payment responses.
  </Card>
</Cards>

For more information on handling any errors during a transaction, refer to the [CatchException](https://docs.payu.in/docs/integrate-checkout-plus#catchexception) section of this document.

## Step 1: Add Meta-tags & Scripts in the HTML Header

Add the following meta-tag & JS script in the HTML header section of your website:

<Accordion title="Code Snippet" icon="fa-code">

```javascript
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://jssdk.payu.in/bolt/bolt.min.js"></script>
```

</Accordion>

<Callout icon="📘" theme="info">
  **Test Script**: Replace the script mentioned in the earlier code snippet with [https://jssdk-uat.payu.in/bolt/bolt.min.js](https://jssdk-uat.payu.in/bolt/bolt.min.js) to test the integration.
</Callout>

## Step 2: Pass Transaction Request Objects

The `bolt.launch()` function takes two arguments.

* In the first argument, the data objects contain the transaction request data (see the [Request parameters](#request-parameters) section for the details of the parameters to be passed as data objects). The format of the data object is as shown below:

<Accordion title="Request Data Object" icon="fa-code">

```plaintext
var data = { key: 'O85456',
                    hash: hash,
                    txnid: tnxID,
                    amount: '1',
                    firstname: 'surbhi',
                    email: "text@example.com",
                    phone: "1234567890",
                    productinfo: 'BOLT',
                    surl: 'http://thirdparty.com/testresponse.php',
                    furl: 'http://thirdparty.com/testresponse.php',
                    lastname: 'soni',
                    enforce_paymethod: "creditcard|debitcard|HDFB|AXIB",
                    display_lang: "Hindi",
                    drop_category: "creditcard|debitcard",
                    pg: "CC",
                    custom_note: "You will be charged an extra amount of Rs 100 on this transaction"
                };
```

</Accordion>

* The second argument is the Handler which contains two functions. The [`responseHandler()`](https://docs.payu.in/docs/android-checkoutpro-closedloopwallet) function and the [`catchException()`](https://docs.payu.in/docs/android-checkoutpro-closedloopwallet) function.

<Accordion title="Handlers Object" icon="fa-code">

```plaintext
var handlers = {responseHandler: function (BOLT) {
                        if(BOLT.response.txnStatus == "SUCCESS"){
                          console.log('Your payment has been successful');
                        }
                        if (BOLT.response.txnStatus == "FAILED") {
                           console.log('Payment failed. Please try again.');
                        }
                        if(BOLT.response.txnStatus == "CANCEL"){
                           console.log('Payment failed. Please try again.');
                        }
                    },
                    catchException: function (BOLT) {
                        console.log('Payment failed. Please try again.');
                    }};
```

</Accordion>

<Accordion title="Sample Request" icon="fa-code">

  ```javascript
  $(document).on('click','#submit',function () {
  var data = { key: 'O85456',
                      hash: hash,
                      txnid: tnxID,
                      amount: '1',
                      firstname: 'surbhi',
                      email: "text@example.com",
                      phone: "1234567890",
                      productinfo: 'BOLT',
                      surl: 'http://thirdparty.com/testresponse.php',
                      furl: 'http://thirdparty.com/testresponse.php',
                      lastname: 'soni',
                      enforce_paymethod: "creditcard|debitcard|HDFB|AXIB",
                      display_lang: "Hindi",
                      drop_category: "creditcard|debitcard",
                      pg: "CC",
                      custom_note: "You will be charged an extra amount of Rs 100 on this transaction"
                  };
  var handlers = {responseHandler: function (BOLT) {
                          if(BOLT.response.txnStatus == "SUCCESS"){
                            console.log('Your payment has been successful');
                          }
                          if (BOLT.response.txnStatus == "FAILED") {
                             console.log('Payment failed. Please try again.');
                          }
                          if(BOLT.response.txnStatus == "CANCEL"){
                             console.log('Payment failed. Please try again.');
                          }
                      },
                      catchException: function (BOLT) {
                          console.log('Payment failed. Please try again.');
                      }};
                  bolt.launch( data , handlers );
          });
  ```

<Callout icon="📘" theme="info">
  **Note**: Here, when your customer clicks on the payment button (#submit), this code triggers the `bolt.launch()` function that passes the transaction parameters along with the `responseHandler()` and `catchException()` functions as arguments.
</Callout>

</Accordion>

<Accordion title="Request Parameters" icon="fa-table">

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>**Parameter**</th>
      <th>**Description**</th>
      <th>**Example**</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>key**mandatory**</td>
      <td>`String` The merchant key is provided by PayU and acts as a unique identifier for a specific merchant account in the PayU's database.</td>
      <td>Your Test Key</td>
    </tr>
    <tr>
      <td>hash**mandatory**</td>
      <td>`String` This field must contain the hash and it is used to avoid the possibility of transaction tampering. For more information on hash generation process, refer to [Encryption of Request](https://docs.payu.in/docs/generate-hash-merchant-hosted).</td>
      <td>`eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972`</td>
    </tr>
    <tr>
      <td>txnid**mandatory**</td>
      <td>`String` The transaction ID is the order reference number generated by the merchant to track a particular order. It can be used only once and PayU's system does not accept a duplicate Transaction ID.</td>
      <td>s7hhDQVWvbhBdN</td>
    </tr>
    <tr>
      <td>amount**mandatory**</td>
      <td>integer The transaction amount, expressed in the currency subunit, such as paise (in case of INR). For example, for an actual amount of "299.35" it should be "29935"</td>
      <td>29935</td>
    </tr>
    <tr>
      <td>firstname**mandatory**</td>
      <td>`String` This parameter must contain the first name of the customer.</td>
      <td>Ashish</td>
    </tr>
    <tr>
      <td>lastname**optional**</td>
      <td>`String` This parameter must contain the last name of the customer.</td>
      <td>Verma</td>
    </tr>
    <tr>
      <td>email**mandatory**</td>
      <td>`String` This parameter must contain the email ID of the customer.</td>
      <td>[test@gmail.com](mailto:test@gmail.com)</td>
    </tr>
    <tr>
      <td>phone**mandatory**</td>
      <td>`String` This parameter must contain the phone number of the customer.</td>
      <td>9876543210</td>
    </tr>
    <tr>
      <td>productinfo**mandatory**</td>
      <td>`String` This parameter must contain a brief description of the product.</td>
      <td>iPhone</td>
    </tr>
    <tr>
      <td>surl**mandatory**</td>
      <td>`String` Success URL(surl) – This must contain the URL on which PayU will redirect the final response if the transaction is successful.</td>
      <td>[https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)</td>
    </tr>
    <tr>
      <td>furl**mandatory**</td>
      <td>`String` Failure URL (furl) – This must contain the URL on which PayU will redirect the final response in case of failure.</td>
      <td>[https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)</td>
    </tr>
    <tr>
      <td>udf1**optional**</td>
      <td>`String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. Merchants can use up to 5 udfs designated as udf1, udf2, udf3, udf4, udf5.</td>
      <td>Payment Preference</td>
    </tr>
    <tr>
      <td>udf2**optional**</td>
      <td>`String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. Merchants can use up to 5 udfs designated as udf1, udf2, udf3, udf4, udf5.</td>
      <td>Shipping Method</td>
    </tr>
    <tr>
      <td>udf3**optional**</td>
      <td>`String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. Merchants can use up to 5 udfs designated as udf1, udf2, udf3, udf4, udf5.</td>
      <td>Shipping Address1</td>
    </tr>
    <tr>
      <td>udf4**optional**</td>
      <td>`String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. Merchants can use up to 5 udfs designated as udf1, udf2, udf3, udf4, udf5.</td>
      <td>Shipping City</td>
    </tr>
    <tr>
      <td>udf5**optional**</td>
      <td>`String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. Merchants can use up to 5 udfs designated as udf1, udf2, udf3, udf4, udf5.</td>
      <td>Shipping Zip Code</td>
    </tr>
    <tr>
      <td>pg**optional**</td>
      <td>`String` Pass the payment category that you want to display on your payment page. The default value is CC (Credit Card). Checkout Plus supports: Net Banking, Credit/Debit Cards, UPI, Wallet.</td>
      <td></td>
    </tr>
    <tr>
      <td>bankcode**optional**</td>
      <td>`String` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it.</td>
      <td></td>
    </tr>
    <tr>
      <td>codurl**optional**</td>
      <td>`String` This field must contain the address of the customer if the Cash on Delivery option is chosen for the payment.</td>
      <td></td>
    </tr>
    <tr>
      <td>drop_category**optional**</td>
      <td>`String` This parameter is used if you want to hide one or multiple payment options.</td>
      <td>creditcard|debitcard</td>
    </tr>
    <tr>
      <td>enforce_paymethod**optional**</td>
      <td>`String` This parameter allows you to customize the payment options for each transaction. You can enforce specific payment modes, card schemes, and specific banks under Net Banking.</td>
      <td>creditcard|debitcard|HDFB|AXIB</td>
    </tr>
    <tr>
      <td>custom_note**optional**</td>
      <td>`String` This parameter allows you to pass any custom note for the transaction.</td>
      <td>You will be charged an extra amount of Rs 100 on this transaction</td>
    </tr>
    <tr>
      <td>note_category**optional**</td>
      <td>`String` This parameter allows you to define the category of the note. Example - CC, NB will show the custom_note for Credit Card & Net banking only.</td>
      <td></td>
    </tr>
  </tbody>
</Table>

</Accordion>

## Step 3: Fetch the Response Using responseHandler

The `responseHandler()` function fetches the response from PayU once the transaction is completed. In case of a successful, failed, or canceled transaction, the [Response parameters](#response-parameters) will be returned to the `responseHandler()` function based on the corresponding logic defined by the merchant.

<Accordion title="CatchException" icon="fa-exclamation-triangle">

The `catchException()` function captures the transaction message in case of any exceptions.

</Accordion>

<Accordion title="Sample Response" icon="fa-reply">

  ```plaintext
  mihpayid: 403993715523615328
  mode: CC
  status: success
  unmappedstatus: captured
  key: JPM7Fg
  txnid: 50QJq6lBJBmx14
  amount: 10.00
  cardCategory: domestic
  discount: 0.00
  net_amount_debit: 10
  addedon: 2021-07-28 15:11:37
  productinfo: iPhone
  firstname: PayU User
  lastname:
  address1:
  address2:
  city:
  state:
  country:
  zipcode:
  email: test@gmail.com
  phone: 9876543210
  udf1:
  udf2:
  udf3:
  udf4:
  udf5:
  udf6:
  udf7:
  udf8:
  udf9:
  udf10:
  hash: afeab9dcf4e43d47f8fbf5a6838d393c70694a58e30ada08e6cb86ac943236c05717c5f5e4872d671fe81d0d9b2d9facd44e9a061ba621aff6f20c4343ea5dfa
  field1:
  field2:
  field3:
  field4:
  field5:
  field6:
  field7:
  field8:
  field9: Transaction Completed Successfully
  payment_source: payu
  PG_TYPE: CC-PG
  bank_ref_num: 7f0d5ada-59bb-41d7-9e41-20a6af2406c9
  bankcode: CC
  error: E000
  error_Message: No Error
  name_on_card: test
  cardnum: 411111XXXXXX1111
  cardhash: This field is no longer supported in postback params.
  ```

</Accordion>

<Accordion title="Response Parameters" icon="fa-table">

<Table>
  <thead>
    <tr>
      <th>**Parameter**</th>
      <th>**Description**</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>mihpayid</td>
      <td>It is a unique reference number created for each transaction at PayU's end which is used to identify a transaction in case of a refund.</td>
    </tr>
    <tr>
      <td>mode</td>
      <td>This parameter describes the payment category by which the transaction was completed/attempted by the customer. The values are: CC (Credit Card), DC (Debit Card), NB (Net Banking), CASH (Cash Card), EMI, CLEMI (Cardless EMI), BNPL (Buy Now Pay Later).</td>
    </tr>
    <tr>
      <td>bankcode</td>
      <td>This parameter contains the code indicating the payment option used for the transaction. For example, Visa Debit Card – VISA, Master Debit Card – MAST.</td>
    </tr>
    <tr>
      <td>status</td>
      <td>This parameter returns the status of the transaction and must be used to map the order status. Possible values are success, failure, or pending. **Success**: transaction is successful. **Failed**: if status is 'failure' or 'pending', treat as a failed transaction.</td>
    </tr>
    <tr>
      <td>unmappedstatus</td>
      <td>This parameter holds the status of a transaction in PayU's internal database, which can include intermediate states. Possible values: dropped, bounced, captured, auth, failed, usercancelled, or pending. For information on status description, refer to [Payment State Explanations](ref:payment-state-explanations).</td>
    </tr>
    <tr>
      <td>key</td>
      <td>This parameter contains the merchant key.</td>
    </tr>
    <tr>
      <td>error</td>
      <td>For the failed transactions, this parameter provides the reason for failure.</td>
    </tr>
    <tr>
      <td>error_message</td>
      <td>This parameter contains the error message. For the list of error messages, refer to [Error Codes](ref:error-codes).</td>
    </tr>
    <tr>
      <td>bank_ref_num</td>
      <td>For each successful transaction – this parameter contains the bank reference number generated by the bank.</td>
    </tr>
    <tr>
      <td>txnid</td>
      <td>This parameter contains the transaction ID value posted by the merchant during the transaction request.</td>
    </tr>
    <tr>
      <td>amount</td>
      <td>This parameter contains the original amount which was sent in the transaction request by the merchant.</td>
    </tr>
    <tr>
      <td>productinfo</td>
      <td>This parameter contains the same value of product information which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>firstname</td>
      <td>This parameter contains the same value of first name which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>lastname</td>
      <td>This parameter contains the same value of last name which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>email</td>
      <td>This parameter contains the same value of email which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>phone</td>
      <td>This parameter contains the same value of phone which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>hash</td>
      <td>This parameter is crucial and is similar to the hash parameter used in the transaction request. For more information, refer to [Generate Hash](generate-hash-merchant-hosted).</td>
    </tr>
    <tr>
      <td>PG_TYPE</td>
      <td>This parameter gives information on the payment gateway used for the transaction.</td>
    </tr>
    <tr>
      <td>udf1</td>
      <td>This parameter contains the same value of udf1 which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>udf2</td>
      <td>This parameter contains the same value of udf2 which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>udf3</td>
      <td>This parameter contains the same value of udf3 which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>udf4</td>
      <td>This parameter contains the same value of udf4 which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
    <tr>
      <td>udf5</td>
      <td>This parameter contains the same value of udf5 which was sent in the transaction request from the merchant's end to PayU.</td>
    </tr>
  </tbody>
</Table>

</Accordion>