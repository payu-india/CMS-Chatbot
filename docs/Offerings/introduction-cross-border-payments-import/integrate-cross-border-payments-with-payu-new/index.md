---
title: '[Review]Integrate Cross-Border Payments with PayU '
deprecated: false
hidden: true
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
  <Card title="1. Make Payment Using Web Checkout Integration" href="https://docs.payu.in/docs/payu-hosted-checkout-integration-with-offers#step-1-make-payment-using-web-checkout-integration">
    Complete the payment process using PayU's web checkout integration

    <br />
  </Card>

  <Card title="2. Update Invoice ID (Conditional)" href="https://docs.payu.in/docs/payu-hosted-checkout-integration-with-offers#step-2-update-invoice-id-optional">
    Optionally update the invoice ID associated with the transaction

    <br />
  </Card>

  <Card title="3. Upload the Invoices / Shipping Document (Conditional)" href="https://docs.payu.in/docs/payu-hosted-checkout-integration-with-offers#step-3-upload-the-invoices">
    Upload invoice documents related to the completed transaction
  </Card>
</Cards>

## Step 1: Make Payment using Web Checkout Integration

The following parameters (mandatory) must be posted using any of the following Web Checkout integration:

* [PayU Hosted Payment](https://docs.payu.in/docs/cb-integration-non-seamless)
* Merchant Hosted Checkout
  * [NetBanking Integration](https://docs.payu.in/docs/netbanking-integration-merchant-hosted-integration-cb)
  * Cards
    * [Plain Cards](https://docs.payu.in/docs/plain-cards-integration-one-time-pacb)
    * [Plain Cards with Tokenization](https://docs.payu.in/docs/plain-cards-with-tokenization-integration-one-time-pacb)
    * [Cards with PayU Tokenization](https://docs.payu.in/docs/cards-with-payu-tokenization-one-time-pacb)
    * [Network Tokens Integration](https://docs.payu.in/docs/network-tokens-one-time-payment-pacb)
  * [UPI Intent with S2S Integration ](https://docs.payu.in/docs/pacb-upi-intent-with-s2s-integration)

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

## Step 3: Upload the Invoices [Optional]

According to the RBI guidelines, the invoice file must be shared with PayU within 10 days of the transaction. The invoices can be uploaded using the **Invoice Upload** API.

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
