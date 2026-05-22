---
title: '[Internal Review]Integrate Cross-Border Payments with PayU '
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  title: Integrate Cross-Border Payments for PayU Biz
  description: ' Learn how to integrate cross-border payments using PayUBiz. This guide provides detailed instructions, request parameters, and sample responses for seamless international transactions.'
  keywords:
    - Integrate Import for PayUBiz
    - Cross-Border Import for PayUBiz Integration
    - Cross Border Import for PayUBiz Integration
    - Integrate Cross-Border Import for PayUBiz
    - Cross-Border Import for PayUBiz Integration
    - ''' cross-border payments'''
    - ''' PayUBiz'''
    - ''' international transactions'''
    - ''' secure payment integration'''
    - ''' tokenization'''
    - ''' cross-border payments'''
    - ''' cross border payments'''
    - ''' PayUBiz integration for cross-border payments'''
    - ''' PayUBiz integration for cross border payments'''
  robots: index
---
The cross-border payment integration for PayU involves the following steps:

<Cards columns={3}>
  <Card title="1. Make Payment Using Web Checkout Integration" href="#step-1-make-payment-using-web-checkout-integration">
    Complete the payment process using PayU's web checkout integration

    <br />
  </Card>

  <Card title="2. Update Invoice ID (Conditional)" href="#step-2-update-invoice-id-optional">
    Optionally update the invoice ID associated with the transaction

    <br />
  </Card>

  <Card title="3. Upload the Invoices & AWBs(Conditional)" href="#step-3-upload-the-invoices--awbs-conditional">
    Upload invoice documents related to the completed transaction
  </Card>
</Cards>

## Step 1: Make Payment using Web Checkout Integration

The following parameters (mandatory) must be posted using any of the following Web Checkout integration and refer to the corresponding section of [Web Checkout Integration](doc:introduction-web) documentation for the complete list of parameters to be posted:

* <Anchor label="PayU Hosted Integration" target="_blank" href="https://docs.payu.in/docs/prebuilt-checkout-page-integration">PayU Hosted Integration</Anchor>
* [Merchant Hosted Checkout > Cards](https://docs.payu.in/docs/collect-payments-with-cards-seamless)
* [Server-to-Server > General Integration](https://docs.payu.in/docs/server-to-server-integration)

<Callout icon="👍" theme="okay">
  Experience the end-to-end **PayU Hosted > Cross-Border Payments** flow and instantly generate the complete code for seamless, zero-coding integration into your website.

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

                                  <button onclick="window.open('https://payu.in/integrationlab/crossborder', '_blank')" 
                                          class="tooltip-btn" 
                                          data-tooltip="Automatically generate code including hashing for your eCommerce website to integrate Offers - PayU Hosted Checkout with zero coding knowledge.">
                                       Experience the flow and get the code
                                  </button>
  `}</HTMLBlock>
</Callout>

<Accordion title="Request parameters" icon="fa-code">
  The following are the additional request parameter required for cross-border payments with all of the above integrations.

  <PaymentAPIEnvironment />

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
                                           <td>key <br/> <code>mandatory</code></td>
                                           <td><code>String</code> Merchant key provided by PayU during onboarding.</td>
                                           <td>JPg****f</td>
                                         </tr>
                                         <tr>
                                           <td>txnid <br/> <code>mandatory</code></td>
                                           <td><code>String</code> The transaction ID is a reference number for a specific order that is generated by the merchant.</td>
                                           <td>ypl938459435</td>
                                         </tr>
                                         <tr>
                                           <td>amount<br/> <code>mandatory</code></td>
                                           <td><code>String</code> The payment amount for the transaction.</td>
                                           <td>10.00</td>
                                         </tr>
                                         <tr>
                                           <td>productinfo<br/> <code>mandatory</code></td>
                                           <td><code>String</code> A brief description of the product.</td>
                                           <td>iPhone</td>
                                         </tr>
                                         <tr>
                                           <td>firstname<br/> <code>mandatory</code></td>
                                           <td><code>String</code> The first name of the customer.</td>
                                           <td>Ashish</td>
                                         </tr>
                                         <tr>
                                           <td>lastname<br/> <code>mandatory</code></td>
                                           <td><code>String</code> The last name of the customer.</td>
                                           <td>Kumar</td>
                                         </tr>
                                         <tr>
                                           <td>email<br/> <code>mandatory</code></td>
                                           <td><code>String</code> The email address of the customer.</td>
                                           <td>abc@payu.in</td>
                                         </tr>
                                         <tr>
                                           <td>phone<br/> <code>mandatory</code></td>
                                           <td><code>String</code> The phone number of the customer.</td>
                                           <td>9876543210</td>
                                         </tr>
                                         <tr>
                                           <td>address1<br/> <code>mandatory</code></td>
                                           <td><code>String</code> The first line of the billing address.<br><strong>Note</strong>: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.</td>
                                           <td>34 Saikripa-Estate, Tilak Nagar</td>
                                         </tr>
                                         <tr>
                                           <td>address2<br/> <code>mandatory</code></td>
                                           <td><code>String</code> The second line of the billing address.</td>
                                           <td>Near Metro Station</td>
                                         </tr>
                                         <tr>
                                           <td>city<br/> <code>mandatory</code></td>
                                           <td><code>String</code> The city where your customer resides as part of the billing address.</td>
                                           <td>Mumbai</td>
                                         </tr>
                                         <tr>
                                           <td>state<br/> <code>mandatory</code></td>
                                           <td><code>String</code> The state where your customer resides as part of the billing address.</td>
                                           <td>Maharashtra</td>
                                         </tr>
                                         <tr>
                                           <td>country<br/> <code>mandatory</code></td>
                                           <td><code>String</code> The country where your customer resides.</td>
                                           <td>India</td>
                                         </tr>
                                         <tr>
                                           <td>zipcode<br/> <code>mandatory</code></td>
                                           <td><code>String</code> Billing address zip code is mandatory for the cardless EMI option.<br><code>Character Limit</code>: 20</td>
                                           <td>400004</td>
                                         </tr>
                                         <tr>
                                           <td>pg<br/> <code>mandatory for seamless/s2s flow</code></td>
                                           <td><code>String</code> It defines the payment category that the merchant wants the customer to see by default on the PayU's payment page. If this field is empty, the system assumes the credit card payment option by default.</td>
                                           <td>CC, NB or UPI</td>
                                         </tr>
                                         <tr>
                                           <td>bankcode<br/> <code>mandatory for seamless/s2s flow</code></td>
                                           <td><code>String</code> Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it.</td>
                                           <td>AMEX</td>
                                         </tr>
                                         <tr>
                                           <td>ccnum<br/> <code>mandatory for cards</code></td>
                                           <td><code>String</code> Use 13-19 digit card number for credit/debit cards (15 digits for AMEX, 13-19 for Maestro) and validate with LUHN algorithm. Refer to Card Number Formats and display error message on invalid input.</td>
                                           <td>5506900480000008</td>
                                         </tr>
                                         <tr>
                                           <td>ccname<br/> <code>mandatory for cards</code></td>
                                           <td><code>String</code> This parameter must contain the name on card – as entered by the customer for the transaction.</td>
                                           <td>John Doe</td>
                                         </tr>
                                         <tr>
                                           <td>ccvv <code>mandatory for cards</code></td>
                                           <td><code>String</code> Use 3-digit CVV number for credit/debit cards and 4-digit security code (4DBC/CID) for AMEX cards.</td>
                                           <td>123</td>
                                         </tr>
                                         <tr>
                                           <td>ccexpmon<br/> <code>mandatory for cards</code></td>
                                           <td><code>String</code> This parameter must contain the card's expiry month – as entered by the user for the transaction. It must always be in 2 digits or in MM format. For months 1-9, this parameter must be appended with 0 – like 01, 02…09. For months 10-12, this parameter must not be appended – It should be 10,11 and 12 respectively.</td>
                                           <td>09</td>
                                         </tr>
                                         <tr>
                                           <td>ccexpyr<br/> <code>mandatory for cards</code></td>
                                           <td><code>String</code> This parameter must contain the card's expiry year – as entered by the customer for the transaction. It must be of four digits.</td>
                                           <td>2025</td>
                                         </tr>
                                         <tr>
                                           <td>surl<br/> <code>mandatory</code></td>
                                           <td><code>String</code> The success URL, which is the page PayU will redirect to if the transaction is successful.</td>
                                           <td>https://test.payu.in/admin/test_response</td>
                                         </tr>
                                         <tr>
                                           <td>furl<br/> <code>mandatory</code></td>
                                           <td><code>String</code> The Failure URL, which is the page PayU will redirect to if the transaction is failed.</td>
                                           <td>https://test.payu.in/admin/test_response</td>
                                         </tr>
                                        <tr>
                                          <td>udf1<br/> <code>mandatory if AD bank request this detail</code></td>
                                          <td><code>String</code> The Permanent Account Number of the buyer must be collected in this field.</td>
                                          <td>AELPR****E</td>
                                        </tr>
                                        <tr>
                                          <td>udf2<br/> <code>optional</code></td>
                                          <td><code>String</code> User-defined field for storing transaction-specific data. Character limit: 255.</td>
                                          <td>Additional transaction data</td>
                                        </tr>
                                        <tr>
                                          <td>udf3 <code>mandatory if AD bank request this detail</code></td>
                                          <td><code>String</code> The date of birth of the buyer must be collected using this field in the DD-MM-YYYY format.</td>
                                          <td>02-02-1980</td>
                                        </tr>
                                        <tr>
                                          <td>udf4<br/> <code>mandatory for payment aggregators</code></td>
                                          <td><code>String</code> This parameter must include end merchant legal entity name.</td>
                                          <td>XYZ Pvt. Ltd.</td>
                                        </tr>
                                        <tr>
                                          <td>udf5<br/> <code>mandatory</code></td>
                                          <td><code>String</code> The invoice ID or invoice number must be collected using this field.</td>
                                          <td>098450845</td>
                                        </tr>
                                        <tr>
                                          <td>buyer_type_business<br/> <code>optional in case of B2B transaction for cross-border payments</code></td>
                                          <td><code>Binary</code> To be sent as "1" in case the buyer is a business. In case of individual buyers, it can be skipped. Default is "0". <strong>Note</strong>: This will be included in hash if posted.</td>
                                          <td>1</td>
                                        </tr>
                                        <tr>
                                          <td>udf_params<br/> <code>optional</code></td>
                                          <td><code>String JSON</code> UDF7 value to capture "Import or Export Code" of the buyer. UDF8 value to capture Airway Bill Number / Consignment Number (in case of goods imports).</td>
                                          <td>{"udf7":"0100000029","udf8":"99953729071"}</td>
                                        </tr>
                                        <tr>
                                          <td>hash<br/> <code>mandatory</code></td>
                                          <td><code>String</code> Crucial security parameter using SHA512 hash encryption. Formula incorporates key, txnid, amount, productinfo, firstname, email, udf fields, si_details, and merchant salt.</td>
                                          <td>&lt;Generated Hash&gt;</td>
                                        </tr>
                                      </tbody>
                                     </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location 'https://test.payu.in/_payment' --header 'Content-Type: application/x-www-form-urlencoded' --data-urlencode 'key=PRiQvJ' --data-urlencode 'txnid=my_order_64240' --data-urlencode 'amount=5' --data-urlencode 'productinfo=asfas' --data-urlencode 'email=test@test.com' --data-urlencode 'phone=8688359250' --data-urlencode 'txn_s2s_flow=4' --data-urlencode 'hash={{hash}}' --data-urlencode 'pg=CC' --data-urlencode 'bankcode=CC' --data-urlencode 'surl=https://test.payu.in/admin/test_response' --data-urlencode 'furl=https://test.payu.in/admin/test_response' --data-urlencode 'udf1=' --data-urlencode 'udf2=' --data-urlencode 'udf3=' --data-urlencode 'udf4=' --data-urlencode 'udf5=' --data-urlencode 'ccnum=5506900480000008' --data-urlencode 'ccexpyr=2025' --data-urlencode 'ccexpmon=09' --data-urlencode 'ccvv=123' --data-urlencode 'ccname=test' --data-urlencode 'si_details={"billingAmount":"10.00","billingCurrency":"INR","billingCycle":"ADHOC","billingInterval": 1,"paymentStartDate":"2024-11-19","paymentEndDate":"2025-12-01"}' --data-urlencode 'api_version=7' --data-urlencode 'si=1' --data-urlencode 'firstname=sudhanshu' --data-urlencode 'user_credentials=T58CQx:sudhanshu' --data-urlencode 'lastname=kr' --data-urlencode 'address1=308,third floor' --data-urlencode 'address2=testing' --data-urlencode 'city=ggn' --data-urlencode 'state=UP' --data-urlencode 'country=IND' --data-urlencode 'zipcode=122018'
  ```
</Accordion>

## Step 2: Update Invoice ID [Conditional]

If the Invoice ID value was unavailable when posting the transaction at [Step 1](#step-1-make-payment-using-web-checkout-integration), it can be updated using the **UDF Update** API by posting it in the UDF5 parameter.

<GENERALAPIsEnvironment />

<Accordion title="Sample request other then UPI AutoPay" icon="fa-code">
  ```
    curl --location --globoff 'https://test.payu.in/merchant/postservice.php?form=2' \
    --form 'key="PRiQvJ"' \
    --form 'command="udf_update"' \
    --form 'var1="my_order_642"' \
    --form 'var2="AAAPZ1234C"' \
    --form 'var4="22/08/1972"' \
    --form 'var5="SellerName"' \
    --form 'var6="INV000000005"' \
    --form 'hash="{{hash}}"'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  ### Success Scenario

  * If successfully updated for cards

  ```JSON
  {
      "status": "UDF values updated",
      "transaction_id": "my_order_64240",
      "udf1": "AAAPZ1234C",
      "udf2": "",
      "udf3": "22/08/1972",
      "udf4": "SellerName",
      "udf5": "INV000000005"
  }
  ```

  * If successfully updated for UPI autopay:

  ```JSON
  {
      "status": "UDF values updated",
      "transaction_id": "my_order_64240",
      "udf1": "AAAPZ1234C",
      "udf2": "",
      "udf3": "22/08/1972",
      "udf4": "SellerName",
      "udf5": "INV000000005"
  }
  ```

  ### Failure Scenarios

  * If the transaction ID is empty

  ```JSON
  ( 
  [status] => 0 
  [msg] => Parameter missing 
  ) 
  ```

  * If the transaction ID is invalid

  ```JSON
  ( 
  [status] => 0 
  [msg] => Invalid TXN ID 
  ) 
  ```

  * If Hash is invalid:

  ```JSON
  {
      "status": 0,
      "msg": "Invalid Hash."
  }
  ```

  * If the merchant is not enabled for UDF updates:

  ```JSON
  {
    "status": "0",
    "msg": "Update not allowed on provided Field"
  }
  ```

  * If no data found in the transaction ID:

  ```JSON
  {
    "status": "0",
    "msg": "No Data Found for txnid: 3424"
  }
  ```

  * If the merchant is inactive:

  ```JSON
  {
    "msg": "Merchant is not authorized to use PayU API",
    "status": 0
  }
  ```
</Accordion>

<br />

## Step 3: Upload the Invoices & AWBs [Conditional]

The invoices / Airway Bill can be uploaded using the **Invoice Upload API** API. AWB details are mandatory for Goods transactions. Invoice copies can be uploaded optionally.

<GENERALAPIsEnvironment />

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location -g --request POST '{{baseUrl}}/merchant/postservice?form=2' \ 
  --form 'key="{{merchantKey}}"' \ 
  --form 'command="opgsp_upload_invoice_awb"' \ 
  --form 'var1="403993715525825059"' \  - PayuId 
  --form 'var2="TestInv0001234568"' \ - invoice Id 
  --form 'var3="Invoice"' \ - type of upload - Invoice/AWB 
  --form 'file=@"/path/to/file"' \ - file 
  --form 'hash="{{hash}}"' 
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  <Accordion title="Success Scenario" icon="fa-check-circle">
    * When a file is uploaded successfully:

    ```plaintext
    {
    "responseCode":"00",
    "responseMsg":"File Uploaded Successfully"
    }
    ```
  </Accordion>

  <Accordion title="Failure Scenarios" icon="fa-exclamation-triangle">
    * When there is an error in uploading the file:

    ```plaintext
    { 
    "responseCode": "103", 
    "responseMsg": "Failed to Upload" 
    } 
    ```

    * When the file format is not supported:

    ```plaintext
    { 
    "responseCode": "105", 
    "responseMsg": "Not an PACB merchant, contact KAM" 
    } 
    ```

    * When the payuid is invalid:

    ```plaintext
    {
    "responseCode":"107",
    "responseMsg":"The PayuID in request is invalid"
    }
    ```

    * When a mandatory field is missing:

    ```plaintext
    {
    "responseCode":"109",
    "responseMsg":"All fields are mandatory, please check!"
    } 
    ```
  </Accordion>
</Accordion>

<Accordion title="Response Code and Description" icon="fa-list">
  Refer to [Response Code and Description - Invoice Upload API](ref:response-code-and-description-invoice-upload-api).
</Accordion>

<br />