---
excerpt: ''
api:
  file: emi-apis-6.json
  operationId: CapturePreAuth
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
To capture a pre-authorized payment, use the following command. After the API command is successful, the transaction would be captured and settled to you.

<br />

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

                              <button onclick="window.open('https://payu.in/integrationlab/seamless/sm-capture', '_blank')" 
                                      class="tooltip-btn" 
                                      data-tooltip="Click here to see the Merchant Hosted Checkout > UPI Capture Payment API and instantly generate the complete code needed for a zero-coding setup on your website.">
                                  Experience the flow and get the code
                              </button>
  `}</HTMLBlock>
</Callout>

HTTP Method: **POST**

<GENERALAPIsEnvironment />

<Accordion title="Sample request" icon="fa-code">
  ### Cards

  ```curl
  curl --location --request POST 'https://info.payu.in/merchant/postservice.php?form=2' \ 
  --header 'Content-Type: application/x-www-form-urlencoded' \ 
  --form 'key="JF***g"' \ 
  --form 'command="capture_transaction"' \ 
  --form 'hash="67411736ab98c59522492a12751a6015c41b87764019f9dc14052690c2c7af9095d31002fc109dcf3596c2f38792d56db6f6207b1989010f2adf51c144fa3019"' \ 
  --form 'var1="15246574846"' \ 
  --form 'var2="authorizeTransaction123"' \ 
  --form 'var3="1"' 
  ```

  ### UPI

  ```curl
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

<Accordion title="Sample response" icon="fa-reply">
  ### Cards

  ```plaintext
  { 
      "status": 1, 
      "msg": "Capture Request Queued", 
      "request_id": "Request ID", 
      "bank_ref_num": "Bank Reference Number" 
  } 
  ```

  ### UPI

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

<Accordion title="Response parameters" icon="fa-list">
  <HTMLBlock>{`
  <table>
    <thead>
      <tr>
        <th><strong>Parameter</strong></th>
        <th><strong>Description</strong></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>status</td>
        <td>
          This parameter returns the status of web service call. The status can be any of the following:
          <ul>
            <li>0 - If web service call failed</li>
            <li>1 - If web service call succeeded</li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>msg</td>
        <td>This parameter returns the following message if the pre-auth transaction was successful: Capture Request Queued</td>
      </tr>
      <tr>
        <td>request_id</td>
        <td>This parameter returns the request ID for the transaction.</td>
      </tr>
      <tr>
        <td>bank_ref_num</td>
        <td>This parameter returns the bank reference number for the transaction.</td>
      </tr>
    </tbody>
  </table>
  `}</HTMLBlock>
</Accordion>

## Request parameters

<Accordion title="Additional info" icon="fa-flask">
  <KeyHashForGeneralParametersDescription />
</Accordion>
