---
title: 1. Integration Steps
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
Before you start with the integration, enable the payment methods that you want to offer to your customers from Dashboard > Settings > Payment methods. We enable Cards, UPI, and other payment methods by default, and we recommend that you enable other payment methods that are relevant to you.

## Create a PayU account

First, create a PayU account. See [Register for a Merchant Account.](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard)

> 🚧 Download Python SDK
> 
> You can download the Python web SDK from the following GitHub link: <https://github.com/payu-india/web-sdk-python>

## Install Using PIP

To install the PayU Python SDK using PIP, run the following command:

```
pip install payu-websdk
```

***

## Enviroments, method, and request header

| Enviroment | URI                                                    |
| :--------- | :----------------------------------------------------- |
| Test       | <https://test.payu.in/merchant/postservice.php?form=2> |
| Production | <https://info.payu.in/merchant/postservice.php?form=2> |

- **Method** — `POST`
- **Request header** — `Content-Type`:`multipart/form-data`

## Build PayU Object

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

## Get checkout details

The `get_checkout_details API` is a generic API using which they can get information when you create the custom checkout-pages, that will contain the payment options, offers, recommendations, and downtime details. The API provides the following details:

Payment option details: The extended details for each payment option available for the merchant. Additional charges: The additional charges configured for all payment options. eligibility details Downtime details: The downtime status of the payment options.

```Text Python

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

## Get transaction details

The Get Transaction Details (get_Transaction_Details) API takes works on basis input as two dates (initial and final), between which the transaction details are needed. The output consists of the status of the API (success or failed) and all the transaction details in an array format.

```Text Python

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

## Refund transaction

The Cancel Refund Transaction API (cancel_refund_transaction) can be used for the following purposes:

Cancel a transaction that is in ‘auth’ state at the moment Refund a transaction that is in a ‘captured’ state at the moment. In this API: var1 is the Payu ID (mihpayid) of the transaction, var2 should contain the Token ID (unique token from the merchant)

```Text Python

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

## Invoices

Create an email professional invoices so that your customers, wherever they are, can pay you faster. Use the PayU Invoicing solution to send or manage invoices.

PayU helps you send Invoices to your customers through email using the following APIs:

### Create Invoice

Use the following sample code to create an Invoice.

```Text Python
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

```Text Python
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

## Validate VPA

This web service will let you validate VPA if it is a valid VPA or not.

After the customer enters VPA on the merchant page, you need to call this API to check for VPA validation. If VPA is valid only then, the second call should be made.

```Text Python

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

## Check downtime

The Downtime Check APIs help you get the downtime of the Net Banking or card BINs for all the banks which are observing either full downtime or partial downtime.

This API is used to help you in handling the credit card/debit card issuing bank’s downtime. It allows you to get the present status of the issuing bank using the specific Bank Identification Number (BIN). BIN is identified as the first six digits of a credit or debit card. You need to provide the BIN number as input and the corresponding issuing bank’s status would be returned in the output (whether up or down). This API is used to retrieve the card BINs for all banks which are observing either full downtime or partial downtime at an instant. The information related to full/partial downtime depends on the input. This section describes how to use the following APIs:

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

## EMI

The EMI APIs allows you to check the customer’s eligibility for EMI and get the EMI amount according to interest using the following APIS:

### eligibleBinsForEMI

```Text Python
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

```Text Python
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

## Check bin type

The BIN API or check_isDomestic API is used to detect whether a particular BIN number is international or domestic. It is also useful to determine:

- card’s issuing bank
- card type such as, Visa, Master, etc.
- card category such as Credit/Debit, etc.
- var1 is bin number which is the first 6 digits of a Credit/Debit card.

```Text Python

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

## Verify payment

The Verify Payment (verify_payment) API gives you the status of the transaction. PayU recommends using this API to reconcile with PayU’s database after you receive the response.

```Text Python

  PayuClient payuClient = PayuClient.init("Key", "salt");

  String HashForverify_payment =  verifyPaymentHash.generateHashForverify_payment();

  Verify_Payment obj1 = new Verify_Payment();
  obj1.key = "key";
  obj1.var1 = "txnid";
  obj1.environment = "env";   //(Test / Production)
  obj1.hash = HashForverify_payment;
  String response1 = obj1.Get_Verify_Payment();



```