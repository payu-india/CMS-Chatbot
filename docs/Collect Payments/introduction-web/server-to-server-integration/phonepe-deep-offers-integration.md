---
title: PhonePe Deep Offers S2S Integration
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
The following are the sequence of API calls for SDK-less Deep-Offer integration on PhonePe:

<Cards columns={3}>
  <Card title="1. Initiate S2S Transaction with PayU and Check Response" href="https://docs.payu.in/docs/phonepe-deep-offers-integration#step-1-initiate-s2s-transaction-with-payu-and-check-the-response">
    Initiate server-to-server transaction with PayU and verify the response

    <br />
  </Card>

  <Card title="2. Invoke Intent on The Customer's Device" href="https://docs.payu.in/docs/phonepe-deep-offers-integration#step-2-invoke-intent-in-the-customers-device">
    Trigger PhonePe intent on the customer's mobile device for payment completion

    <br />
  </Card>

  <Card title="3. Get Web Service Response" href="https://docs.payu.in/docs/phonepe-deep-offers-integration#step-3-get-web-service-response">
    Retrieve and process the web service response from PhonePe

    <br />
  </Card>

  <Card title="4. S2S Call Back Response" href="https://docs.payu.in/docs/phonepe-deep-offers-integration#step-4-s2s-call-back-response">
    Handle the server-to-server callback response from PayU

    <br />
  </Card>

  <Card title="5. Verify the payment" href="https://docs.payu.in/docs/phonepe-deep-offers-integration#step-5-verify-the-payment">
    Verify the payment status and ensure successful transaction completion
  </Card>

  <br />
</Cards>

<Callout icon="👍" theme="okay">
  **Before you begin**: Register for a account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Callout>

## Step 1: Initiate S2S transaction with PayU and check the response

First request from Merchant to PayU with the required transaction mandatory/ optional parameters. This needs to be a server-to-server curl call request. For the sample request and response, refer to [Collect Payment API - Server-to-Server](ref:_payment_server_to_server).

<PaymentAPIEnvironment />

> 📘 Notes:
>
> * You need to check before hand, whether the customer's device has a PhonePe app or not. If the customer's device does not have a PhonePe App, do not show this feature on your check out page
> * The highlighted parameter i.e. udf 1 parameter contains the offer details to be applied against the transaction. The offer details are pre-determined between you and PhonePe.
> * You can find the version of PhonePe app using this code:
>
> ```javascript
> public boolean doesPhonePeExist(Context context) 
> {PackageInfo packageInfo = null; 
> long phonePeVersionCode = -1L; 
> try { 
> packageInfo =  
> getPackageManager().getPackageInfo(PHONEPE_PACKAGE_NAME,PackageManager.GET_ACTIVITIES); 
> phonePeVersionCode = packageInfo.versionCode; 
> } 
> catch (PackageManager.NameNotFoundException e) { 
> Log.e(TAG, String.format("failed to get package info for package name = {%s}, 
> exception message = {%s}", 
> PHONEPE_PACKAGE_NAME, e.getMessage())); 
> } 
> if (packageInfo == null) { 
> return false; 
> } 
> if (phonePeVersionCode > 94033) { 
> return true; 
> }return false; 
> } 
> ```

Collect the response in the [Collect Payment API - Server-to-Server](ref:_payment_server_to_server) under API Reference. The response for the S2S payment request is not similar to Merchant Hosted or PayU Hosted Checkout. For description of response parameters, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis#response-for-initial-server-to-server-request).

## Step 2: Invoke Intent in the Customer's Device

After you receive a successful response, with redirect type as Intent and with a redirect URL, then the merchant invokes the Intent in the customer's device.

<Accordion title="Implementation" icon="fa-gear">
  ```javascript
  Intent i = new Intent(Intent.ACTION_VIEW); 
  i.setData(Uri.parse(redirectURL)); 
  i.setPackage(PHONEPE_PACKAGE_NAME); 
  startActivityForResult(i, PHONEPE_REQUEST); 
  ```

  You have to override on Activity Result to listen to debit result:

  ```javascript
  privatestaticfinalintPHONEPE_REQUEST=123; 
  @OverrideprotectedvoidonActivityResult(intrequestCode, intresultCode, Intentdata) 
  {
  super.onActivityResult(requestCode, resultCode, data); 
    if(requestCode==PHONEPE_REQUEST) 
    {/*This callback indicates only about completion of flow. Inform your server to make the transaction status call to get the status. Update your app with the success/failure status.*/ 
    } 
  } 
  ```
</Accordion>

***

## Step 3: Get Web Service Response

After receiving a successful debit response from the application, you check the transaction status with PayU. Based on the debit request, the transaction should not be marked as success. It has to be marked successful only after checking with PayU servers through the **get_ws_response** API and WS Call Response.

***

## Step 4: S2S Call Back Response

PayU can also send a Server to server call back response whenever the transaction status gets updated.

<Accordion title="Implementation" icon="fa-gear">
  The server to server response would be sent by PayU on a pre-set URL, which has to be provided by the merchant.  PayU will configure it at the back-end for the merchant.

  This response would be sent in key/value pair separated by '&' character. In case any parameter is not used, we would send it back to the merchant with an empty string.
</Accordion>

<Accordion title="Sample Response" icon="fa-file-code">
  ```plaintext
  unmappedstatus=success&phone=9999999999&txnid=FCDA1R100870163781&hash=84e3 35094bbcb2ddaa0f9a488eb338e143b273765d89c9dfa502402562d0b6f3c7935e28194ca92f7 380be7c84c3695415b106dcf52cb016a15fcf6adc98d724&status=success&curl=https://www. abc.in/payment/handlepayuresposne&firstname=NA&card_no=519619XXXXXX5049&furl= https://www.abc.in/payment/handlepayuresposne&productinfo=2&mode=DC&amount=800.  00&field4=6807112311042810&field3=6807112311042810&field2=838264&field9=SUCC ESS&email=NA&mihpayid=175477248&surl=https://www.ABC.in/payment/handlepayuresp osne&card_hash=9e88cb0573d4a826b61d808c0a870ed4a990682459b0ec9e95ea421e8e47b e8c&field1=42812 
  ```

  The parameter list includes: mihpayid, mode, status, key, txnid, amount, productinfo, firstname, lastname, address1, address2, city, state, country, zipcode, email, phone, udf1, udf2, udf3, udf4, udf5, udf6, udf7, udf8, udf9, udf10, card\_token, card\_no, field0, field1, field2, field3, field4, field5, field6, field7, field8, field9, offer, discount, offer\_availed, unmappedstatus, hash, bank\_ref\_no, surl, curl, furl, and card\_hash
</Accordion>

<Accordion title="Whitelisting Required" icon="fa-shield">
  Whitelisting is required at both merchant's and PayU's end to establish this connection.

  * You need to white list the following IP address on your Firewall:
    * 180.179.174.1
    * 180.179.174.2
  * PayU will white list merchant server side IP address that you have provided to PayU.
</Accordion>

## Step 5. Verify the payment

<Verify_Payment_Tabs />
