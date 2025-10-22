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

**Steps to integrate**

<Cards columns={2}>
  <Card title="1. Load the JS-SDK on the page" href="https://docs.payu.in/?isFramePreview=true#step-1-load-the-js-sdk-on-the-page" target="_blank">
    Load and initialize the PayU JavaScript SDK on your webpage to enable payment processing capabilities

    <br />
  </Card>

  <Card title="2. Pass the transaction request object" href="https://docs.payu.in/?isFramePreview=true#step-2-pass-the-transaction-request-object" target="_blank">
    Configure and pass the transaction request object with all required payment parameters

    <br />
  </Card>

  <Card title="3. Fetch the response with Callback URL" href="https://docs.payu.in/?isFramePreview=true#step-3-fetch-the-response-with-callback-url" target="_blank">
    Configure callback URL to receive and process payment responses from PayU

    <br />
  </Card>

  <Card title="4. Catch Exceptions" href="https://docs.payu.in/?isFramePreview=true#step-4-catch-exceptions" target="_blank">
    Handle errors and exceptions that may occur during the payment process

    <br />
  </Card>
</Cards>

## Step 1: Load the JS-SDK on the page

Load the the following URL using script tag on the page:

[https://jssdk.payu.in/bolt/bolt.min.js](https://jssdk.payu.in/bolt/bolt.min.js)

> 📘 Note:
>
> To test your integration of CommercePro on UAT environment, use the following URL:  
> [https://jssdk-uat.payu.in/bolt/bolt.min.js](https://jssdk-uat.payu.in/bolt/bolt.min.js)

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

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key
        `mandatory`
      </td>

      <td>
        `string` The merchant key generated from the PayU.
      </td>
    </tr>

    <tr>
      <td>
        txnid  
        `mandatory`
      </td>

      <td>
        `string` The unique ID of the transaction.
      </td>
    </tr>

    <tr>
      <td>
        amount  
        `mandatory`
      </td>

      <td>
        `string` The transaction amount, expressed in the currency subunit, such as paise (in case of INR). For example, for an actual amount of “299.35”.
      </td>
    </tr>

    <tr>
      <td>
        firstname  
        `mandatory`
      </td>

      <td>
        `string` The customer first name.
      </td>
    </tr>

    <tr>
      <td>
        lastname  
        `optional`
      </td>

      <td>
        `string` The customer last name.
      </td>
    </tr>

    <tr>
      <td>
        email  
        `optional`
      </td>

      <td>
        `string` The email address of the customer.
      </td>
    </tr>

    <tr>
      <td>
        phone  
        `mandatory`
      </td>

      <td>
        `string` The mobile number of the customer. In case mobile number is not available, send empty string.
      </td>
    </tr>

    <tr>
      <td>
        productinfo  
        `optional`
      </td>

      <td>
        `string` The brief details of the product.
      </td>
    </tr>

    <tr>
      <td>
        surl  
        `mandatory`
      </td>

      <td>
        `string` The success URL provided by merchant.
      </td>
    </tr>

    <tr>
      <td>
        furl  
        `mandatory`
      </td>

      <td>
        `string` The failure URL provided by merchant.
      </td>
    </tr>

    <tr>
      <td>
        isCheckoutExpress  `mandatory`
      </td>

      <td>
        `boolean` This value is always true
      </td>
    </tr>

    <tr>
      <td>
        icp_source  
        `mandatory`
      </td>

      <td>
        `string` This value is always “express”
      </td>
    </tr>

    <tr>
      <td>
        orderid  
        `mandatory`
      </td>

      <td>
        `string` Use this parameter to create new order or edit existing order.
      </td>
    </tr>

    <tr>
      <td>
        cart_details  
        `mandatory`
      </td>

      <td>
        `object` Use this parameter to create cart for express transaction and to load SKU offers. The amount passed must be equal to the cart amount when there no extra charges. In case of extra charges, total 
      </td>
    </tr>

    <tr>
      <td>
        udf1  
        `optional`
      </td>

      <td>
        `String` User-defined fields1
      </td>
    </tr>

    <tr>
      <td>
        udf2  
        `optional`
      </td>

      <td>
        `String` User-defined fields2
      </td>
    </tr>

    <tr>
      <td>
        udf3  
        `optional`
      </td>

      <td>
        `String` User-defined fields3
      </td>
    </tr>

    <tr>
      <td>
        udf4

        ```

        optional
        ```
      </td>

      <td>
        `String` User-defined fields4
      </td>
    </tr>

    <tr>
      <td>
        udf5  
        `optional`
      </td>

      <td>
        `String` User-defined fields5
      </td>
    </tr>

    <tr>
      <td>
        custom_note  
        `optional`
      </td>

      <td>
        `String` Any custom note that you want to display on the checkout screen
      </td>
    </tr>

    <tr>
      <td>
        note_category  
        `optional`
      </td>

      <td>
        `String` CC, NB will show the custom_note for Credit Card & Net banking only
      </td>
    </tr>

    <tr>
      <td>
        offer_auto_apply  
        `optional` 
      </td>

      <td>
        `Boolean` If value is true then best offer will be applied for user for the payment mode from which payment is being done.
      </td>
    </tr>

    <tr>
      <td>
        editPhoneAllowed   
        `optional` 
      </td>

      <td>
        `String` The value will be either **true** or **false**. In case true then phone number edit would not be allowed on express screen, and user would be allowed to login from merchant passed phone number only.
      </td>
    </tr>

    <tr>
      <td>
        editEmailAllowed  
        `optional`
      </td>

      <td>
        `String` The value will be either **true** or **false**. In case true then email edit would not be allowed on express screen.
      </td>
    </tr>

    <tr>
      <td>
        emailRequired  
        `optional`
      </td>

      <td>
        `String` The value will be either **true** or **false**.In case true then email entry, would be mandatory on login page .
      </td>
    </tr>

    <tr>
      <td>
        extraCharges   
        `optional` 
      </td>

      <td>
        `Static` The extra charges object will be required if merchant want to show extra charges to user on express screen. 
      </td>
    </tr>
  </tbody>
</Table>

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

| Parameter        | Descruiption                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mihpayid         | It is a unique reference number created for each transaction at PayU’s end which is used to identify a transaction in case of a refund.                                                                                                                                                                                                                                                                                                                                                                                   |
| mode             | This parameter describes the payment category by which the transaction was completed/attempted by the customer. The values are:  <br /><br />_Credit Card – CC<br />_ Debit Card – DC <br />_Net Banking – NB<br />_ Cash Card – CASH<br />_EMI – EMI<br />_ Cardless EMI – CLEMI<br />* Buy Now Pay Later - BNPL                                                                                                                                                                                                         |
| bankcode         | This parameter contains the code indicating the payment option used for the transaction. For example, Visa Debit Card – VISA, Master Debit Card – MAST.                                                                                                                                                                                                                                                                                                                                                                   |
| txnStatus        | This parameter returns the status of the transaction and must be used to map the order status. Possible values are SUCCESS, FAILED and CANCEL                                                                                                                                                                                                                                                                                                                                                                             |
| unmappedstatus   | This parameter holds the status of a transaction in PayU's internal database, which can include intermediate states. Possible values include: dropped, bounced, captured, auth, failed, usercancelled, or pending. For information on status description, refer to  [Payment State Explanations](https://docs.payu.in/reference/payment-state-explanations).                                                                                                                                                              |
| key              | This parameter contains the merchant key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| error            | For the failed transactions, this parameter provides the reason for failure.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| error_Message    | This parameter contains the error message. For the list of error message, refer to [Error Codes](https://docs.payu.in/reference/error-codes).                                                                                                                                                                                                                                                                                                                                                                             |
| bank_ref_num     | For each successful transaction – this parameter contains the bank reference number generated by the bank.                                                                                                                                                                                                                                                                                                                                                                                                                |
| txnid            | This parameter contains the transaction ID value posted by the merchant during the transaction request.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| amount           | This parameter contains the original amount which was sent in the transaction request by the merchant.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| productinfo      | This parameter contains the same value of product information which was sent in the transaction request from the merchant’s end to PayU.                                                                                                                                                                                                                                                                                                                                                                                  |
| firstname        | This parameter contains the same value of first name which was sent in the transaction request from the merchant’s end to PayU.                                                                                                                                                                                                                                                                                                                                                                                           |
| lastname         | This parameter contains the same value of last name which was sent in the transaction request from the merchant’s end to PayU.                                                                                                                                                                                                                                                                                                                                                                                            |
| email            | This parameter contains the same value of email which was sent in the transaction request from the merchant’s end to PayU.                                                                                                                                                                                                                                                                                                                                                                                                |
| phone            | This parameter contains the same value of phone which was sent in the transaction request from the merchant’s end to PayU.                                                                                                                                                                                                                                                                                                                                                                                                |
| hash             | This parameter is crucial and is similar to the hash parameter used in the transaction request. For more information, refer to  <a href="generate-hash-merchant-hosted" target="_blank"> Generate Hash</a>.                                                                                                                                                                                                                                                                                                               |
| udf1             | This parameter contains the same value of udf1 which was sent in the transaction request from the merchant’s end to PayU.                                                                                                                                                                                                                                                                                                                                                                                                 |
| udf2             | This parameter contains the same value of udf2 which was sent in the transaction request from the merchant’s end to PayU.                                                                                                                                                                                                                                                                                                                                                                                                 |
| udf3             | This parameter contains the same value of udf3 which was sent in the transaction request from the merchant’s end to PayU.                                                                                                                                                                                                                                                                                                                                                                                                 |
| udf4             | This parameter contains the same value of udf4 which was sent in the transaction request from the merchant’s end to PayU.                                                                                                                                                                                                                                                                                                                                                                                                 |
| udf5             | This parameter contains the same value of udf5 which was sent in the transaction request from the merchant’s end to PayU.                                                                                                                                                                                                                                                                                                                                                                                                 |
| shipping_address | This parameter is an object containing address the customer chose to make payment with. Example:  <br />\{  <br />    "name": "\<name_with_saved_address>",  <br />    "email": "\<email_with_the_saved_address>",  <br />    "addressLine": "\<address_string>",  <br />    "addressPhoneNumber": "\<address_number>",  <br />    "landmark": ‘\<landmark_with_address>’,  <br />    "pincode": \<pincode_with_address>,  <br />    "city": "\<city_with_address>",  <br />    "state": “\<state_with_address>"  <br />} |

## Step 4: Catch Exceptions

The `catchException`() function captures the transaction message in case of any exceptions.

## Next Steps

You can use the [Get Order Details API](https://docs.payu.in/reference/get-order-details-api) if you want to fetch the order details and order status for a given transaction id (txn id).
