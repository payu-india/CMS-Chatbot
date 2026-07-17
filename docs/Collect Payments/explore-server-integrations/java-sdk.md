---
title: Java SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Java SDK for Server-side Integration
  description: ''
  keywords:
    - Java SDK for Server-side integration
    - Server-side integration Java SDK
    - Integrate Server-side with Java SDK
  robots: index
next:
  description: ''
---
The PayU SDK for java enables you to easily work with the APIs of PayU by integrating this SDK within your base system. With our SDK, you do not need to worry about low-level details for API integration and with a few lines of code and a function call, get started within a few minutes. To install Java Web SDK, refer to [Integraton Steps](#integration-steps).

## Features Supported

The following features are supported in the Java SDK:

- Create a Payment form.
- Verify the transaction or check the transaction status.
- Initiate/cancel refunds and check the status of a refund.
- Retrieve settlement details that the bank has to settle you.
- Get information on eligible payment options and PG/BANK downtime details.
- Check the customer’s eligibility for EMI and get the amount according to the EMI interest.
- Create/Expire invoice link through the function.

## Integration Steps

Before you start with the integration, enable the payment methods that you want to offer to your customers from Dashboard > Settings > Payment methods. We enable Cards, UPI, and other payment methods by default, and we recommend that you enable other payment methods that are relevant to you.

<Accordion title="Create a PayU account" icon="fa-code">
  First, create a PayU account. See [Register for a Merchant Account](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard).

  > 🚧 Download Java SDK
  >
  > You can download the Java web SDK from the following GitHub link: [https://github.com/payu-intrepos/web-sdk-java](https://github.com/payu-intrepos/web-sdk-java)
</Accordion>

<Accordion title="Install the SDK" icon="fa-code">
  To install the PayU Java SDK using the terminal:

  1. Install the latest version of Java from [https://java.com](https://java.com) and Maven from [https://maven.apache.org/download.html](https://maven.apache.org/download.html).
  2. Set the environment variable: `export GOOGLE_APPLICATION_CREDENTIALS=your-key-filename.json
     Configure JAVA_HOME.`

  ```bash
  cd java-docs-samples/storage/xml-api/cmdline-sample
  #Compile and run
  mvn compile install
  mvn -q exec:java -Dexec.args="your-bucket-name"
  ```

  ### Run the SDK

  1. Right-click on project
  2. Run As > Java Application
  3. If asked, type "StorageSample" and click OK

  ***
</Accordion>

<Accordion title="Build the PayU object" icon="fa-code">
  Use the sample code snippet to build an instance of PayU Object for Java SDK:

  ```java
  PayuClient payuClient = PayuClient.init("KEY", "SALT");
  // Need to set merchant key and salt
  ```
</Accordion>

<Accordion title="Verify payment" icon="fa-code">
  The Verify Payment (verify\_payment) API gives you the status of the transaction. PayU recommends using this API to reconcile with PayU's database after you receive the response.

  * **Method**: `Post`
  * **Request header**: `Content-Type  multipart/form-data`

  ```java

    PayuClient payuClient = PayuClient.init("Key", "salt");

    String HashForverify_payment =  verifyPaymentHash.generateHashForverify_payment();

    Verify_Payment obj1 = new Verify_Payment();
    obj1.key = "key";
    obj1.var1 = "txnid";
    obj1.environment = "env";   //(Test / Production)
    obj1.hash = HashForverify_payment;
    String response1 = obj1.Get_Verify_Payment();



  ```
</Accordion>

<Accordion title="Get BIN type" icon="fa-code">
  The BIN API or check\_isDomestic API is used to detect whether a particular BIN number is international or domestic. It is also useful to determine:

  1. card's issuing bank
  2. card type such as, Visa, Master, etc.,
  3. card category such as Credit/Debit, etc.
  4. var1 is bin number which is the first 6 digits of a Credit/Debit card.

  * **Method**: `POST`
  * **Request header**: `Content-Type  multipart/form-data`

  ```java

    PayuClient payuClient = PayuClient.init("Key", "salt");

        String HashForcheckdomastic =  checkdomastic.generateHashForcheckisDomestic();

    CheckisDomestic checkdomasticObj = new CheckisDomestic();
        checkdomasticObj.key = "QyT13U";
        checkdomasticObj.environment = "Test";
        checkdomasticObj.var1 = "512345";                       //This is the Card Number(First 6 digits of a card)
        checkdomasticObj.hash = HashForcheckdomastic;
        String response3 = checkdomasticObj.Get_Check_is_Domestic();


  ```
</Accordion>

<Accordion title="Get checkout details" icon="fa-code">
  The get\_checkout\_details API is a generic API using which they can get information when you create the custom checkout-pages, that will contain the payment options, offers, recommendations, and downtime details. The API provides the following details:

  Payment option details: The extended details for each payment option available for the merchant. Additional charges: The additional charges configured for all payment options. eligibility details Downtime details: The downtime status of the payment options.

  * **Method**: `POST`
  * **Request header**: `multipart/form-data`

  ```java

    PayuClient payuClient = PayuClient.init("Key", "salt");

    String HashForcheckoutDtls =  checkoutDtls.generateHashForcheckoutDtls();

    CheckoutDetails checkoutdtl = new CheckoutDetails();
    checkoutdtl.key = "key";
    checkoutdtl.environment = "Test";
    checkoutdtl.var1 = json;
    checkoutdtl.hash = HashForcheckoutDtls;
    String response5 = checkoutdtl.Get_Checkout_Details();



  ```
</Accordion>

<Accordion title="Check downtime" icon="fa-code">
  The Downtime Check APIs help you get the downtime of the Net Banking or card BINs for all the banks which are observing either full downtime or partial downtime.

  This API is used to help you in handling the credit card/debit card issuing bank's downtime. It allows you to get the present status of the issuing bank using the specific Bank Identification Number (BIN). BIN is identified as the first six digits of a credit or debit card. You need to provide the BIN number as input and the corresponding issuing bank's status would be returned in the output (whether up or down). This API is used to retrieve the card BINs for all banks which are observing either full downtime or partial downtime at an instant. The information related to full/partial downtime depends on the input. This section describes how to use the following APIs:

  1. getNetbankingStatus
  2. getIssuingBankStatus

  **Method**: POST

  **Request type**: multipart/form-data

  ```java

    PayuClient payuClient = PayuClient.init("Key", "salt");

     //getNetbankingStatus
    String HashFornetbankingStatus= netbankingStatus.generateHashForNetbankingStatus();

    DowntimeCheckAPI obj1 = new DowntimeCheckAPI();
        obj1.key = "QyT13U";
        obj1.var1 = "AXIB";
        obj1.environment = "Test";
        obj1.hash = HashFornetbankingStatus;
        String response1 = obj1.getNetbankingStatus();

     //getIssuingBankStatus
     String HashForissuingBankStatus= issuingBankStatus.generateHashForissuingBankStatus();

    DowntimeCheckAPI obj2 = new DowntimeCheckAPI();
        obj2.key = "QyT13U";
        obj2.var1 = "512345";
        obj2.environment = "Test";
        obj2.hash = HashForissuingBankStatus;
        String response2 = obj2.getissuingBankStatus();


  ```
</Accordion>

<Accordion title="Validate VPA" icon="fa-code">
  This web service will let you validate VPA if it is a valid VPA or not.

  After the customer enters VPA on the merchant page, you need to call this API to check for VPA validation. If VPA is valid only then, the second call should be made.

  * **Method**: `POST`
  * **Request type**: `multipart/form-data`

  ```java

    PayuClient payuClient = PayuClient.init("Key", "salt");

        String HashForvalidateVPA =  validateVPA.generateHashForvalidateVPA();

    ValidateVPA validate_VPA = new ValidateVPA();
        validate_VPA.key = "QyT13U";
        validate_VPA.environment = "Test";
        validate_VPA.var1 = "9999999999@upi";                           //customerVPA
        validate_VPA.hash = HashForvalidateVPA;
        String response4 = validate_VPA.Get_validateVPA();



  ```

  ***
</Accordion>

<Accordion title="Get transaction details" icon="fa-code">
  The Get Transaction Details (get\_Transaction\_Details) API takes works on basis input as two dates (initial and final), between which the transaction details are needed. The output consists of the status of the API (success or failed) and all the transaction details in an array format.

  * **Method**: `POST`
  * **Request header**: `multipart/form-data`

  ```java

    PayuClient payuClient = PayuClient.init("Key", "salt");

    String HashFortransactionDtls =  transactionDtls.generateHashFortransactionDtls();


    Get_Transaction_Details txndtls = new Get_Transaction_Details();
    txndtls.key = "key";
    txndtls.environment = "Test";
    txndtls.var1 = "startdate";                                //parameter must contain the starting date
    txndtls.var2 = "enddate";                                //This parameter must contain the end date
    txndtls.hash = HashFortransactionDtls;
    String response5 = txndtls.GetTransactionDetails();


  ```
</Accordion>

<Accordion title="Invoices" icon="fa-code">
  Create an email professional invoices so that your customers, wherever they are, can pay you faster. Use the PayU Invoicing solution to send or manage invoices.

  PayU helps you send Invoices to your customers through email using the following APIs:

  1. create\_invoice
  2. expire\_invoice

  * **Method**: `POST`
  * **Request header**: `multipart/form-data`

  ```java

    PayuClient payuClient = PayuClient.init("Key", "salt");

     //create_invoice
        String HashForcreateinvoice = crate_invoiceHash.generateHashForCreateInvoice();

    Invoice obj1 = new Invoice();
        obj1.key = "QyT13U";
        obj1.var1 = json;
        obj1.environment = "Test";
        obj1.hash = HashForcreateinvoice;
        String response1 = obj1.Get_Create_invoic();

     //expire_invoice
        String HashForexpireinvoice = expire_invoiceHash.generateHashForexpireInvoice();

    DowntimeCheckAPI obj2 = new DowntimeCheckAPI();
        Invoice obj2 = new Invoice();
        obj2.key = "QyT13U";
        obj2.var1 = "oknjhyg64tgd";
        obj2.environment = "Test";
        obj2.hash = HashForexpireinvoice;
        String response2 = obj2.Get_expire_invoic();

  ```
</Accordion>

<Accordion title="EMI APIs" icon="fa-code">
  The EMI APIs allows you to check the customer's eligibility for EMI and get the EMI amount according to interest using the following APIS:

  1. eligibleBinsForEMI
  2. getEmiAmountAccordingToInterest

  * **Method**: `POST`
  * **Request header**: `multipart/form-data`

  ```java

    PayuClient payuClient = PayuClient.init("Key", "salt");

     //eligibleBinsForEMI
        String HashForeligibleBinsForEMI= eligibleBinsForEMI.generateHashForeligibleBinsForEMI();

    DowntimeCheckAPI obj1 = new DowntimeCheckAPI();
        EMI_APIs obj1 = new EMI_APIs();
        obj1.key = "QyT13U";
        obj1.var1 = "bin";
        obj1.var2 = "512345";
        obj1.environment = "Test";
        obj1.hash = HashForeligibleBinsForEMI;
        String response1 = obj1.geteligibleBinsForEMI();

     //getEmiAmountAccordingToInterest
        String HashForEmiAmountAccordingToInterest= EmiAmountAccordingToInterest.generateHashForEmiAmountAccordingToInterest();

    DowntimeCheckAPI obj2 = new DowntimeCheckAPI();
         EMI_APIs obj2 = new EMI_APIs();
        obj2.key = "QyT13U";
        obj2.var1 = "100";
        obj2.environment = "Test";
        obj2.hash = HashForEmiAmountAccordingToInterest;
        String response2 = obj2.getEmiAmountAccordingToInterest();


  ```

  ***
</Accordion>

<Accordion title="Refund transaction" icon="fa-code">
  The Cancel Refund Transaction API (cancel\_refund\_transaction) can be used for the following purposes:

  Cancel a transaction that is in 'auth' state at the moment Refund a transaction that is in a 'captured' state at the moment. In this API: var1 is the Payu ID (mihpayid) of the transaction, var2 should contain the Token ID (unique token from the merchant), and va

  * **Method**: `POST`
  * **Request header**: `multipart/form-data`

  ```java

    PayuClient payuClient = PayuClient.init("Key", "salt");

    String HashForrefund =  refund.generateHashForrefund();

    Refund refundObj = new Refund();
        refundObj.key = "QyT13U";
        refundObj.environment = "Test";
        refundObj.var1 = "403993715527261883";                      //This parameter must contain the Payu ID
        refundObj.var2 = "rfveds238456uyt8yh34";                    //unique token from the merchant
        refundObj.var3 = "05.00";                                   //Refund Amount
        refundObj.hash = HashForrefund;
        String response2 = refundObj.Get_cancel_refund_transaction();



  ```
</Accordion>

## Test and Go-live

<Test_your_integration />

<br />

<Go_Live_Checklist />

<br />
