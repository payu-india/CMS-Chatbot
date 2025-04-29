---
title: Integrate CommercePro Checkout using Callback URL
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
This section describes the procedure to integrate CommercePro Checkout using Callback URL in your website and start accepting payments.

## Step 1: Load the JS-SDK on the page

Load the the following URL using script tag on the page:

<https://jssdk.payu.in/bolt/bolt.min.js>

> 📘 Note:
> 
> To test your integration of CommercePro on UAT environment, use the following URL:  
> <https://jssdk-uat.payu.in/bolt/bolt.min.js>

```Text HTML
<script src='https://jssdk.payu.in/bolt/bolt.min.js'></script>
```

## Step 2: Pass the transaction request object

Use the following snippet to construct the initialisation object :

```Text JavaScript
// Create the express object. Refer to the table for a full list of parameters
const expressData = {
    key: '<merchant_key>',
    txnid: '<merchant_transaction_ID>',
    amount: '<total_transaction_amount>',
    phone: '<user_mobile_number>',
    firstname: '<user_first_name>',
    lastname: '<user_last_name>',
    email: '<user_email>',
    udf1: '<user_defined_parameter1>',
    udf2: '<user_defined_parameter2>',
    udf3: '<user_defined_parameter3>',
    udf4: '<user_defined_parameter4>',
    udf5: '<user_defined_parameter5>',
    isCheckoutExpress: true,
    icp_source: "express",
    productinfo: '<merchant_product_info>',
    surl: '<merchant_success_url>',
    furl: '<merchant_failure_url>',
    orderid: '<merchant_orider_ID>',
    cart_details: {
      'amount': '<total_transaction_amount>',
      'items': '<total_items_in_cart>',
      'sku_details': [
        {
          'offer_key': ['<offer_key1>', '<offer_key2>', '<offer_key3>', ... (do this for the offers configure for SKU)],
          'amount_per_sku': '<sku_amount>',
          'quantity': '<quantity_of_sku>',
          'sku_id': '<sku_ID>',
          'sku_name': '<sku_name>',
          'logo': '<url_of_sku_image>'
        },
        ... (do this for each SKU)
      ]
    },
    {
    "shipping_charges": '<shipping_charges>',
    "cod_fee": '<cod_fee>',
    "other_charges": '<other_charges>',
    "tax_info": {
        "breakup": {
            <tax_name> : '<tax_amount>'
        },
        "total": '<total_Amount_sum_all_charges>'
    }
}}

// Get date;
const date = new Date().toGMTString();

// Authentication hash supported
const AUTH_TYPE = 'sha512';

// Stringigy the express object
const stringifiedExpressData = JSON.stringify(expressData);

// Construct hash input on the backend by '|'(pipe) seperating parts
const hash_string = stringifiedExpressData + '|' + date + '|' + <merchant_salt>;

// Construct hash using SHA512 and encoding in hexadecimal
const hash = merchant_function_that_calculates_hash(hash_string)

// Construct authentication header with merchant key, authentication type, v2 hash received from the BE  
const  authHeader = 'hmac username="' + key + '", ' + 'algorithm="' + AUTH_TYPE + '", headers="date", signature="' + hash + '"';

```

### Transaction Parameters

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "key  \n`mandatory`",
    "0-1": "`string` The merchant key generated from the PayU.",
    "1-0": "txnid  \n `mandatory`",
    "1-1": "`string` The unique ID of the transaction.",
    "2-0": "amount  \n `mandatory`",
    "2-1": "`string` The transaction amount, expressed in the currency subunit, such as paise (in case of INR). For example, for an actual amount of “299.35”.",
    "3-0": "firstname  \n  `mandatory`",
    "3-1": "`string` The customer first name.",
    "4-0": "lastname  \n  `optional`",
    "4-1": "`string` The customer last name.",
    "5-0": "email  \n`optional`",
    "5-1": "`string` The email address of the customer.",
    "6-0": "phone  \n`mandatory`",
    "6-1": "`string` The mobile number of the customer. In case mobile number is not available, send empty string.",
    "7-0": "productinfo  \n`optional`",
    "7-1": "`string` The brief details of the product.",
    "8-0": "surl  \n`mandatory`",
    "8-1": "`string` The success URL provided by merchant.",
    "9-0": "furl  \n`mandatory`",
    "9-1": "`string` The failure URL provided by merchant.",
    "10-0": "isCheckoutExpress  `mandatory`",
    "10-1": "`boolean` This value is always true",
    "11-0": "icp\\_source  \n`mandatory`",
    "11-1": "`string` This value is always “express”",
    "12-0": "orderid  \n `mandatory`",
    "12-1": "`string` Use this parameter to create new order or edit existing order.",
    "13-0": "cart\\_details  \n `mandatory`",
    "13-1": "`object` Use this parameter to create cart for express transaction and to load SKU offers. The amount passed must be equal to the cart amount when there no extra charges. In case of extra charges, total ",
    "14-0": "udf1  \n`optional`",
    "14-1": "`String` User-defined fields1",
    "15-0": "udf2  \n`optional`",
    "15-1": "`String` User-defined fields2",
    "16-0": "udf3  \n`optional`",
    "16-1": "`String` User-defined fields3",
    "17-0": "udf4  `\noptional`",
    "17-1": "`String` User-defined fields4",
    "18-0": "udf5  \n`optional`",
    "18-1": "`String` User-defined fields5",
    "19-0": "custom\\_note  \n`optional`",
    "19-1": "`String` Any custom note that you want to display on the checkout screen",
    "20-0": "note\\_category  \n `optional`",
    "20-1": "`String` CC, NB will show the custom\\_note for Credit Card & Net banking only",
    "21-0": "offer\\_auto\\_apply  \n`optional` ",
    "21-1": "`Boolean` If value is true then best offer will be applied for user for the payment mode from which payment is being done.",
    "22-0": "editPhoneAllowed   \n`optional` ",
    "22-1": "`String` The value will be either **true** or **false**. In case true then phone number edit would not be allowed on express screen, and user would be allowed to login from merchant passed phone number only.",
    "23-0": "editEmailAllowed  \n`optional`",
    "23-1": "`String` The value will be either **true** or **false**. In case true then email edit would not be allowed on express screen.",
    "24-0": "emailRequired  \n`optional`",
    "24-1": "`String` The value will be either **true** or **false**.In case true then email entry, would be mandatory on login page .",
    "25-0": "extraCharges   \n`optional` ",
    "25-1": "`Static` The extra charges object will be required if merchant want to show extra charges to user on express screen. "
  },
  "cols": 2,
  "rows": 26,
  "align": [
    null,
    null
  ]
}
[/block]


## Step 3: Fetch the response with Callback URL

On successful payment or payment failure, the success or failure information posted to the success URL (sURL) or failure URL (fURL) provide by the merchant, through a HTML form POST.

The customer is redirected to the sURL/fURL. Call the following method on click of the **Pay** button for integration type as callback URL:

```javascript
bolt.launch({
  data: stringifiedExpressData,
  date: date,
  isCheckoutExpress: true,
  v2Hash: authHeader,
  mode: 'dropOut' // Parameter for callback URL method
}, {
  responseHandler: function(express) {
    if(express.response.txnStatus == "CANCEL"){
        console.log('Payment Cancelled.');
    } 
  },
  catchException: function(express) {
    console.log('Exception occured');
  }
}) 
```

### Response parameters description

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Descruiption",
    "0-0": "mihpayid",
    "0-1": "It is a unique reference number created for each transaction at PayU’s end which is used to identify a transaction in case of a refund.",
    "1-0": "mode",
    "1-1": "This parameter describes the payment category by which the transaction was completed/attempted by the customer. The values are:  <br><br>_ Credit Card – CC <br>_ Debit Card – DC <br>_ Net Banking – NB<br>_ Cash Card – CASH<br>_ EMI – EMI <br>_ Cardless EMI – CLEMI<br>\\* Buy Now Pay Later - BNPL",
    "2-0": "bankcode",
    "2-1": "This parameter contains the code indicating the payment option used for the transaction. For example, Visa Debit Card – VISA, Master Debit Card – MAST.",
    "3-0": "txnStatus",
    "3-1": "This parameter returns the status of the transaction and must be used to map the order status. Possible values are SUCCESS, FAILED and CANCEL",
    "4-0": "unmappedstatus",
    "4-1": "This parameter holds the status of a transaction in PayU's internal database, which can include intermediate states. Possible values include: dropped, bounced, captured, auth, failed, usercancelled, or pending. For information on status description, refer to  [Payment State Explanations](https://docs.payu.in/reference/payment-state-explanations).",
    "5-0": "key",
    "5-1": "This parameter contains the merchant key.",
    "6-0": "error",
    "6-1": "For the failed transactions, this parameter provides the reason for failure.",
    "7-0": "error_Message",
    "7-1": "This parameter contains the error message. For the list of error message, refer to [Error Codes](https://docs.payu.in/reference/error-codes).",
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
    "16-1": "This parameter is crucial and is similar to the hash parameter used in the transaction request. For more information, refer to  <a href=\"generate-hash-merchant-hosted\" target=\"_blank\"> Generate Hash</a>.",
    "17-0": "udf1",
    "17-1": "This parameter contains the same value of udf1 which was sent in the transaction request from the merchant’s end to PayU.",
    "18-0": "udf2",
    "18-1": "This parameter contains the same value of udf2 which was sent in the transaction request from the merchant’s end to PayU.",
    "19-0": "udf3",
    "19-1": "This parameter contains the same value of udf3 which was sent in the transaction request from the merchant’s end to PayU.",
    "20-0": "udf4",
    "20-1": "This parameter contains the same value of udf4 which was sent in the transaction request from the merchant’s end to PayU.",
    "21-0": "udf5",
    "21-1": "This parameter contains the same value of udf5 which was sent in the transaction request from the merchant’s end to PayU.",
    "22-0": "shipping_address",
    "22-1": "This parameter is an object containing address the customer chose to make payment with. Example:  <br>{  <br>    \"name\": \"\\<name\\_with\\_saved_address>\",  <br>    \"email\": \"\\<email\\_with\\_the\\_saved\\_address>\",  <br>    \"addressLine\": \"\\<address_string>\",  <br>    \"addressPhoneNumber\": \"\\<address_number>\",  <br>    \"landmark\": ‘\\<landmark\\_with\\_address>’,  <br>    \"pincode\": \\<pincode\\_with\\_address>,  <br>    \"city\": \"\\<city\\_with\\_address>\",  <br>    \"state\": “\\<state\\_with\\_address>\"  <br>}"
  },
  "cols": 2,
  "rows": 23,
  "align": [
    null,
    null
  ]
}
[/block]


## Step 4: Catch Exceptions

The `catchException`() function captures the transaction message in case of any exceptions.

## Next Steps

You can use the [Get Order Details API](https://docs.payu.in/reference/get-order-details-api) if you want to fetch the order details and order status for a given transaction id (txn id).