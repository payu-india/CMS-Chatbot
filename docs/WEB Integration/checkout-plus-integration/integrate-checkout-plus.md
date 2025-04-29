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
PayU Checkout Plus is the most convenient way to collect payment on your website. Add the inline JS script to your website’s header section, then call the bolt.launch() function and pass the transaction data objects when your customers click the payment button. PayU will take care of the payment and returns to your page when it is done.

> 📘 Notes:
> 
> The Checkout Plus integration is not recommended for the app browsers. For example, WebView, Chrome Custom tab, etc. Although there is Redirection Web Checkout which can be integrated. For more information, refer to following: 
> 
> - Redirection Web Checkout: [PayU Hosted Checkout](https://docs.payu.in/docs/prebuilt-checkout-payu-hosted) .
> - Webview configurations: 
>   - [Webview Integration in Android](https://docs.payu.in/docs/webview-integration-in-android) 
>   - [Webview Integration in iOS](https://docs.payu.in/docs/webview-intgration-in-ios)

***

### Steps to integrate

1. [Add the inline script in the HTML Header](#step-1-add-meta-tags--scripts-in-the-html-meader)
2. [Pass the transaction request objects](#step-2-pass-transaction-request-objects)
3. [Fetch the response using the responseHandler function](#step-3-fetch-the-response-using-responsehandler)

***

For more information on handling any errors during a transaction, refer to the [CatchException](https://docs.payu.in/docs/integrate-checkout-plus#catchexception) section of this document.

## Step 1: Add meta-tags & scripts in the HTML header

Add the following meta-tag & JS script in the HTML header section of your website:

```javascript
 <meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://jssdk.payu.in/bolt/bolt.min.js"></script>
```

> 📘 Test Script
> 
> Replace the script mentioned in the earlier code snippet with <https://jssdk-uat.payu.in/bolt/bolt.min.js> to test the integration.

## Step 2: Pass transaction request objects

The `bolt.launch()` function takes two arguments.

- In the first argument, the data objects contain the transaction request data see the [request parameters](https://docs.payu.in/docs/introduction-web) section for the details of the parameters to be passed as data objects). The format of the data object is as shown below:

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

- The second argument is the Handler which contains two functions. The [`responseHandler()`](https://docs.payu.in/docs/android-checkoutpro-closedloopwallet) function and the [`catchException()`](https://docs.payu.in/docs/android-checkoutpro-closedloopwallet) function.

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

### Sample request

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

> 📘 Note:
> 
> Here, when your customer clicks on the payment button (#submit), this code triggers the `bolt.launch() `function that passes the transaction parameters along with the `responseHandler()` and `catchException()`functions as arguments.

### Request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "<<glossary:key>> **mandatory**",
    "0-1": "`String` The merchant key is provided by PayU and acts as a unique identifier for a specific merchant account in the PayU’s database.",
    "0-2": "Your Test Key",
    "1-0": "hash **mandatory**",
    "1-1": "`String` This field must contain the has and it is used to avoid the possibility of transaction tampering. For more information on hash generation process, refer to [Encryption of Request](https://docs.payu.in/docs/generate-hash-merchant-hosted).",
    "1-2": "`eabec285da28fd 0e3054d41a4d24fe 9f7599c9d0b6664 6f7a9984303fd612 4044b6206daf831 e9a8bda28a6200d 318293a13d6c193 109b60bd4b4f8b09 c90972`",
    "2-0": "txnid **mandatory**",
    "2-1": "`String` The transaction ID is the order reference number generated by the merchant to track a particular order. It can be used only once and PayU’s system does not accept a duplicate Transaction ID.",
    "2-2": "s7hhDQVWvbhBdN",
    "3-0": "amount **mandatory**",
    "3-1": "integer The transaction amount, expressed in the currency subunit, such as paise (in case of INR). For example, for an actual amount of “299.35” it should be \"29935\"",
    "3-2": "29935",
    "4-0": "firstname **mandatory**",
    "4-1": "`String` This parameter must contain the first name of the customer.",
    "4-2": "Ashish",
    "5-0": "lastname **optional**",
    "5-1": "`String` This parameter must contain the last name of the customer.",
    "5-2": "Verma",
    "6-0": "email **mandatory**",
    "6-1": "`String` This parameter must contain the email ID of the customer.",
    "6-2": "[test@gmail.com](mailto:test@gmail.com)",
    "7-0": "phone **mandatory**",
    "7-1": "`String` This parameter must contain the phone number of the customer.",
    "7-2": "9876543210",
    "8-0": "productinfo **mandatory**",
    "8-1": "`String` This parameter must contain a brief description of the product.\\`",
    "8-2": "iPhone",
    "9-0": "surl **mandatory**",
    "9-1": "`String` Success URL(surl) – This must contain the URL on which PayU will redirect the final response if the transaction is successful.",
    "9-2": "<https://apiplayground-response.herokuapp.com/>",
    "10-0": "furl **mandatory**",
    "10-1": "`String` Failure URL (furl) – This must contain the URL on which PayU will redirect the final response in case of failure.",
    "10-2": "<https://apiplayground-response.herokuapp.com/>",
    "11-0": "udf1   \n**optional**",
    "11-1": "`String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. Merchants can use up to 5 udfs in the post designated as udf1, udf2, udf3, udf4, udf5. For example, you can store customer's preferred payment.",
    "11-2": "Payment Preference",
    "12-0": "udf2   \n**optional**",
    "12-1": "`String` User-defined fields(udf) are used to store any information corresponding to a particular transaction. Merchants can use up to 5 udfs in the post designated as udf1, udf2, udf3, udf4, udf5. For example, you can store customer's preferred payment.",
    "12-2": "Shipping Method",
    "13-0": "udf3  \n **optional**",
    "13-1": "`String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. Merchants can use up to 5 udfs in the post designated as udf1, udf2, udf3, udf4, udf5. For example, you can store customer's preferred payment.",
    "13-2": "Shipping Address1",
    "14-0": "udf4  \n **optional**",
    "14-1": "`String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. Merchants can use up to 5 udfs in the post designated as udf1, udf2, udf3, udf4, udf5. For example, you can store customer's preferred payment.",
    "14-2": "Shipping City",
    "15-0": "udf5   \n**optional**",
    "15-1": "`String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. Merchants can use up to 5 udfs in the post designated as udf1, udf2, udf3, udf4, udf5. For example, you can store customer's preferred payment.",
    "15-2": "Shipping Zip Code",
    "16-0": "pg  \n **optional**",
    "16-1": "`String `Pass the payment category that you want to display on your payment page. The default value for this parameter is CC (Credit Card).  \n**Note**: Checkout Plus only supports the following payment methods:  \n  \n- [Net Banking](https://docs.payu.in/docs/collect-payments-with-net-banking-seamless)\n- [Credit/Debit Cards](https://docs.payu.in/docs/collect-payments-with-cards-seamless)\n- [UPI](https://docs.payu.in/docs/collect-payments-with-upi-seamless)\n- [Wallet](https://docs.payu.in/docs/collect-payments-with-wallets-seamless)",
    "16-2": "",
    "17-0": "bankcode  \n **optional**",
    "17-1": "`String`Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option’s bank code value in it.",
    "17-2": "",
    "18-0": "codurl **optional**",
    "18-1": "`String` This field must contains the address of the customer if the Cash on Delivery option is chosen for the payment",
    "18-2": "",
    "19-0": "drop\\_category **optional** ",
    "19-1": "`String` This parameter is used if you want to hide one or multiple payment options. For example, if you consider the payment options such as credit card, debit card, and net banking, you can hide the credit card mode of payment.",
    "19-2": "creditcard|debitcard",
    "20-0": " enforce \\_paymethod **optional**",
    "20-1": "String\\`This parameter allows you to customize the payment options for each transaction. You can enforce specific payment modes, cards scheme, specific banks under Net Banking using this method. ",
    "20-2": "creditcard|debitcard|HDFB|AXIB",
    "21-0": "custom\\_note \\*optional\\*\\*",
    "21-1": "String\\` This parameter allows yo pass any custom note for the transaction. ",
    "21-2": "You will be charged an extra amount of Rs 100 on this transaction",
    "22-0": " note\\_category **optional**",
    "22-1": " `String` This parameter allows you to define the category of the note. Example - CC, NB will show the custom\\_note for Credit Card & Net banking only.",
    "22-2": ""
  },
  "cols": 3,
  "rows": 23,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


## Step 3: Fetch the response using responseHandler

The `responseHandler()` function fetches the response from PayU once the transaction is completed. In case of a successful, failed, or canceled transaction, the [response parameters](https://docs.payu.in/docs/integrate-checkout-plus#response-parameters) will be returned to the `responseHandler()` function based on the corresponding logic defined by the merchant.

### **CatchException**

The `catchException()` function captures the transaction message in case of any exceptions.

### **Sample response**

Sample Response URL

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

### Response parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "0-0": "mihpayid",
    "0-1": "It is a unique reference number created for each transaction at PayU’s end which is used to identify a transaction in case of a refund.",
    "1-0": "mode",
    "1-1": "This parameter describes the payment category by which the transaction was completed/attempted by the customer. The values are:    \n\t•\tCredit Card – CC   \n\t•\tDebit Card – DC   \n\t•\tNet Banking – NB  \n\t•\tCash Card – CASH  \n\t•\tEMI – EMI   \n\t•\tCardless EMI – CLEMI  \n\t•\tBuy Now Pay Later - BNPL",
    "2-0": "bankcode",
    "2-1": "This parameter contains the code indicating the payment option used for the transaction. For example, Visa Debit Card – VISA, Master Debit Card – MAST.",
    "3-0": "status",
    "3-1": "This parameter returns the status of the transaction and must be used to map the order status. Possible values are success, failure, or pending. The significance of the values for these values are:    \n\t•\t**Success**: If the value of status parameter is ’success’, the transaction is successful.   \n\t•\t**Failed**: If the value of status parameter is ‘failure’ or ‘pending’, must only be treated as a failed transaction.",
    "4-0": "unmappedstatus",
    "4-1": "This parameter holds the status of a transaction in PayU's internal database, which can include intermediate states. Possible values include: dropped, bounced, captured, auth, failed, usercancelled, or pending. For information on status description, refer to  [Payment State Explanations](ref:payment-state-explanations).",
    "5-0": "key",
    "5-1": "This parameter contains the merchant key.",
    "6-0": "error",
    "6-1": "For the failed transactions, this parameter provides the reason for failure.",
    "7-0": "error\\_message",
    "7-1": "This parameter contains the error message. For the list of error message, refer to [Error Codes](ref:error-codes).",
    "8-0": "bank\\_ref\\_num",
    "8-1": "For each successful transaction – this parameter contains the bank reference number generated by the bank.",
    "9-0": "txnid",
    "9-1": "This parameter contains the transaction ID value posted by the merchant during the transaction request.",
    "10-0": "amount",
    "10-1": "This parameter contains the original amount which was sent in the transaction request by the merchant.",
    "11-0": "productinfo",
    "11-1": "This parameter contains the same value of product information which was sent in the transaction request from the merchant’s end to PayU.",
    "12-0": "firstname",
    "12-1": "This parameter contains the same value of first name which was sent in the transaction request from the merchant’s end to PayU.",
    "13-0": "lastname",
    "13-1": "This parameter contains the same value of last name which was sent in the transaction request from the merchant’s end to PayU.",
    "14-0": "email",
    "14-1": "This parameter contains the same value of email which was sent in the transaction request from the merchant’s end to PayU.",
    "15-0": "phone",
    "15-1": "This parameter contains the same value of phone which was sent in the transaction request from the merchant’s end to PayU.",
    "16-0": "hash",
    "16-1": "This parameter is crucial and is similar to the hash parameter used in the transaction request. For more information, refer to  <a href=\"generate-hash-merchant-hosted\" target=\"_blank\"> Generate Hash</a>.",
    "17-0": "PG\\_TYPE",
    "17-1": "This parameter gives information on the payment gateway used for the transaction.",
    "18-0": "udf1",
    "18-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.",
    "19-0": "udf2",
    "19-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.",
    "20-0": "udf3",
    "20-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5 which was sent in the transaction request from the merchant’s end to PayU.",
    "21-0": "udf4",
    "21-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.",
    "22-0": "udf5",
    "22-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU."
  },
  "cols": 2,
  "rows": 23,
  "align": [
    null,
    null
  ]
}
[/block]