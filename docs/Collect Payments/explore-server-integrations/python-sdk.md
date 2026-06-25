---
title: Python SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Python SDK for Server-side Integration
  description: ''
  keywords:
    - Python SDK for Server-side integration
    - Server-side integration Python SDK
    - Integrate Server-side with Python SDK
  robots: index
next:
  description: ''
---
---
title: Python SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Python SDK for Server-side Integration
  description: >-
    PayU Python server SDK: pip install, merchant key/salt, payment requests, verify/status APIs, sandbox credentials, production go-live.
  robots: index
  keywords:
    - payu python sdk payment gateway integration india
    - python server side payment gateway sdk integration steps
    - integrate payu payment api python django flask backend
    - payment gateway python sdk pip integration payu india
    - server to server payment integration python sdk payu
    - python payment api sdk hash verification integration payu
    - backend payment gateway integration python rest api payu
    - payu python sdk test credentials sandbox integration guide
    - enterprise python payment integration sdk payu checkout
    - python payment gateway sdk documentation integration payu
    - php java python payment gateway api sdk integration payu
    - payu server sdk node java php python payment api india

next:
  description: ''
---
Use PayU Python SDK to integrate PayU payment in your website which is built using Python. PayU Python SDK takes care of the low-level details of the API integration and help you to start collecting payment with just a few lines of code and a function call.

## Supported Payment Features

With this Python SDK you can:

* **Collect Payments** — Create a Payment form to collect payment.
* **Verify Payments** — Verify the transaction or check the transaction status
* **Handle Refunds** — Initiate/cancel refunds and check the status of a refund.
* **Check Settlements** — Retrieve settlement details that the bank has to settle you.
* **Check Bank downtime Status** — Get information on eligible payment options and PG/BANK downtime details.
* **Check Eligibility** — Check the customer’s eligibility for EMI and get the amount according to the EMI interest.
* **Manage Invoices** — Create/Expire invoice link through the function.

## Steps to Integrate

<br />

Before you start with the integration, enable the payment methods that you want to offer to your customers from Dashboard > Settings > Payment methods. We enable Cards, UPI, and other payment methods by default, and we recommend that you enable other payment methods that are relevant to you.

<Accordion title="Create a PayU account" icon="fa-code">
  First, create a PayU account. See [Register for a Merchant Account.](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard)

  > 🚧 Download Python SDK
  >
  > You can download the Python web SDK from the following GitHub link: [https://github.com/payu-india/web-sdk-python](https://github.com/payu-india/web-sdk-python)
</Accordion>

<Accordion title="Install Using PIP" icon="fa-code">
  To install the PayU Python SDK using PIP, run the following command:

  ```
  pip install payu-websdk
  ```

  ***
</Accordion>

<Accordion title="Enviroments, method, and request header" icon="fa-code">
  | Enviroment | URI                                                                                                          |
  | :--------- | :----------------------------------------------------------------------------------------------------------- |
  | Test       | [https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2) |
  | Production | [https://info.payu.in/merchant/postservice.php?form=2](https://info.payu.in/merchant/postservice.php?form=2) |

  * **Method** — `POST`
  * **Request header** — `Content-Type`:`multipart/form-data`
</Accordion>

<Accordion title="Build PayU Object" icon="fa-code">
  Use the following sample code for creating an instance of the PayU Object:

  ```
  client = payu_sdk.payUClient({
      "key": <YOUR_MERCHANT_KEY>,
      "salt": <YOUR_MERCHANT_SALT>,
      "env": <ENVIRONMENT>
    }
  )
  ```

  ***
</Accordion>

<Accordion title="Get checkout details" icon="fa-code">
  The `get_checkout_details API` is a generic API using which they can get information when you create the custom checkout-pages, that will contain the payment options, offers, recommendations, and downtime details. The API provides the following details:

  Payment option details: The extended details for each payment option available for the merchant. Additional charges: The additional charges configured for all payment options. eligibility details Downtime details: The downtime status of the payment options.

  ```python

    PayuClient payuClient = PayuClient.init("Key", "salt");

    String HashForcheckoutDtls =  checkoutDtls.generateHashForcheckoutDtls();

    CheckoutDetails checkoutdtl = new CheckoutDetails();
    checkoutdtl.key = "key";
    checkoutdtl.environment = "Test";
    checkoutdtl.var1 = json;
    checkoutdtl.hash = HashForcheckoutDtls;
    String response5 = checkoutdtl.Get_Checkout_Details();
  ```

  ***
</Accordion>

<Accordion title="Get transaction details" icon="fa-code">
  The Get Transaction Details (get\_Transaction\_Details) API takes works on basis input as two dates (initial and final), between which the transaction details are needed. The output consists of the status of the API (success or failed) and all the transaction details in an array format.

  ```python

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

  ***
</Accordion>

<Accordion title="Refund transaction" icon="fa-code">
  The Cancel Refund Transaction API (cancel\_refund\_transaction) can be used for the following purposes:

  Cancel a transaction that is in 'auth' state at the moment Refund a transaction that is in a 'captured' state at the moment. In this API: var1 is the Payu ID (mihpayid) of the transaction, var2 should contain the Token ID (unique token from the merchant)

  ```python

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

  ***
</Accordion>

<Accordion title="Invoices" icon="fa-code">
  Create an email professional invoices so that your customers, wherever they are, can pay you faster. Use the PayU Invoicing solution to send or manage invoices.

  PayU helps you send Invoices to your customers through email using the following APIs:

  ### Create Invoice

  Use the following sample code to create an Invoice.

  ```python
  PayuClient payuClient = PayuClient.init("Key", "salt");
        String HashForcreateinvoice = crate_invoiceHash.generateHashForCreateInvoice();
    Invoice obj1 = new Invoice();
        obj1.key = "QyT13U";
        obj1.var1 = json;
        obj1.environment = "Test";
        obj1.hash = HashForcreateinvoice;
        String response1 = obj1.Get_Create_invoic();
  ```

  ### Expire Invoice

  Use the following sample code to expire an invoice.

  ```python
   PayuClient payuClient = PayuClient.init("Key", "salt");
   String HashForexpireinvoice = expire_invoiceHash.generateHashForexpireInvoice();
    DowntimeCheckAPI obj2 = new DowntimeCheckAPI();
        Invoice obj2 = new Invoice();
        obj2.key = "QyT13U";
        obj2.var1 = "oknjhyg64tgd";
        obj2.environment = "Test";
        obj2.hash = HashForexpireinvoice;
        String response2 = obj2.Get_expire_invoic();
  ```

  ***
</Accordion>

<Accordion title="Validate VPA" icon="fa-code">
  This web service will let you validate VPA if it is a valid VPA or not.

  After the customer enters VPA on the merchant page, you need to call this API to check for VPA validation. If VPA is valid only then, the second call should be made.

  ```python

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

<Accordion title="Check downtime" icon="fa-code">
  The Downtime Check APIs help you get the downtime of the Net Banking or card BINs for all the banks which are observing either full downtime or partial downtime.

  This API is used to help you in handling the credit card/debit card issuing bank's downtime. It allows you to get the present status of the issuing bank using the specific Bank Identification Number (BIN). BIN is identified as the first six digits of a credit or debit card. You need to provide the BIN number as input and the corresponding issuing bank's status would be returned in the output (whether up or down). This API is used to retrieve the card BINs for all banks which are observing either full downtime or partial downtime at an instant. The information related to full/partial downtime depends on the input. This section describes how to use the following APIs:

  ### Get net banking status

  ```
   PayuClient payuClient = PayuClient.init("Key", "salt");
    String HashFornetbankingStatus= netbankingStatus.generateHashForNetbankingStatus();
    DowntimeCheckAPI obj1 = new DowntimeCheckAPI();
        obj1.key = "******";
        obj1.var1 = "AXIB";
        obj1.environment = "Test";
        obj1.hash = HashFornetbankingStatus;
        String response1 = obj1.getNetbankingStatus();

  ```

  ### Get issuing bank status

  ```
   PayuClient payuClient = PayuClient.init("Key", "salt");
  String HashForissuingBankStatus= issuingBankStatus.generateHashForissuingBankStatus();
    DowntimeCheckAPI obj2 = new DowntimeCheckAPI();
        obj2.key = "******";
        obj2.var1 = "512345";
        obj2.environment = "Test";
        obj2.hash = HashForissuingBankStatus;
        String response2 = obj2.getissuingBankStatus();
  ```

  ***
</Accordion>

<Accordion title="EMI" icon="fa-code">
  The EMI APIs allows you to check the customer's eligibility for EMI and get the EMI amount according to interest using the following APIS:

  ### eligibleBinsForEMI

  ```python
   PayuClient payuClient = PayuClient.init("Key", "salt");
        String HashForeligibleBinsForEMI= eligibleBinsForEMI.generateHashForeligibleBinsForEMI()
    DowntimeCheckAPI obj1 = new DowntimeCheckAPI();
        EMI_APIs obj1 = new EMI_APIs();
        obj1.key = "QyT13U";
        obj1.var1 = "bin";
        obj1.var2 = "512345";
        obj1.environment = "Test";
        obj1.hash = HashForeligibleBinsForEMI;
        String response1 = obj1.geteligibleBinsForEMI();
  ```

  ### getEmiAmountAccordingToInterest

  ```python
   PayuClient payuClient = PayuClient.init("Key", "salt");
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

<Accordion title="Check bin type" icon="fa-code">
  The BIN API or check\_isDomestic API is used to detect whether a particular BIN number is international or domestic. It is also useful to determine:

  * card's issuing bank
  * card type such as, Visa, Master, etc.
  * card category such as Credit/Debit, etc.
  * var1 is bin number which is the first 6 digits of a Credit/Debit card.

  ```python

    PayuClient payuClient = PayuClient.init("Key", "salt");

        String HashForcheckdomastic =  checkdomastic.generateHashForcheckisDomestic();

    CheckisDomestic checkdomasticObj = new CheckisDomestic();
        checkdomasticObj.key = "QyT13U";
        checkdomasticObj.environment = "Test";
        checkdomasticObj.var1 = "512345";                       //This is the Card Number(First 6 digits of a card)
        checkdomasticObj.hash = HashForcheckdomastic;
        String response3 = checkdomasticObj.Get_Check_is_Domestic();


  ```

  ***
</Accordion>

<Accordion title="Verify payment" icon="fa-code">
  The Verify Payment (verify\_payment) API gives you the status of the transaction. PayU recommends using this API to reconcile with PayU's database after you receive the response.

  ```python

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

## Test and Go-live

<Test_your_integration />

<br />

<Go_Live_Checklist />