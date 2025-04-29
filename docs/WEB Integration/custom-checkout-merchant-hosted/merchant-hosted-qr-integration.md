---
title: QR Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: QR Integration with Merchant Hosted Checkout
  description: >-
    To integrate Bharat or UPI QR payments with Merchant Hosted Checkout, follow
    these steps: initiate the payment to PayU, check the response from PayU, and
    verify the payment using the provided APIs. Ensure you have a registered
    PayU merchant account before starting.
  robots: index
next:
  description: ''
---
Collect payments using Bharat or UPI QR with Merchant Hosted Checkout integration as described in this section. After collecting the details from the customer, make the transaction request with the payment details to PayU.

**Steps to Integrate**

1. [Initiate the payment to PayU](#step-1-initiate-the-payment-to-payu)
2. [Check the response from PayU](#step-2-check-response-from-payu)
3. [Verify Payment](#step-3-verify-the-payment)

<RegisterMerchantPrerequiste />

## Step 1: Initiate the payment to PayU

### Post request syntax & composition

Post Request Syntax & Composition for QR

```html
<body>
<form action='https://secure.payu.in/_payment' method='post'>
<input type="hidden" name="key" value="JP***g" />
<input type="hidden" name="txnid" value="t6svtqtjRdl34W" />
<input type="hidden" name="productinfo" value="iPhone" />
<input type="hidden" name="amount" value="10" />
<input type="hidden" name="email" value="test@gmail.com" />
<input type="hidden" name="firstname" value="Ashish" />
<input type="hidden" name="lastname" value="Kumar" />
<input type="hidden" name="pg" value="QR" />
<input type="hidden" name="bankcode" value="UPIQR" />
<input type="hidden" name="enforce_paymethod" value="qr" />
<input type="hidden" name="surl" value="your own success url" />
<input type="hidden" name="furl" value="your own failure url" />
<input type="hidden" name="phone" value="9988776655” />
<input type="hidden" name="hash" value="eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972" />
<input type="submit" value="submit"> </form>
</body>
</html>
```

> 📘 Note
> 
> The above HTML code block is for Merchant Checkout integration for QR call for the test environment.

### Post parameters

The following parameters vary for the QR payment in the **Collect Payment** API (**\_payment** API). 

<PaymentAPIEnvironment />

<br />

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "<<glossary:key>>  \n**mandatory**",
    "0-1": "`String` This parameter is the unique merchant key provided by PayU for your merchant account. For more information, refer to  <a href=\"generate-merchant-key-and-salt-on-payu-dashboard\" target=\"_blank\">Access Production Key and Salt</a>.",
    "0-2": "8488225",
    "1-0": "txnid  \n**mandatory**",
    "1-1": "`String` This parameter is known as Transaction ID (or OrderID). It is the order reference number generated at your (Merchant’s) end. It is an identifier which you(merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of same Transaction ID again would fail. Hence, it is essential that you post us a unique transaction ID for every new transaction (Please make sure that the transaction ID being sent to us hasn’t been successful earlier. In case of this duplication, the customer would get an error of ‘duplicate Order ID’).",
    "1-2": "fd3e847h2",
    "2-0": "amount  \n**mandatory**",
    "2-1": "`String` This parameter should contain the payment amount of the particular transaction. Note: Type-cast the amount to float type",
    "2-2": "10",
    "3-0": "productinfo  \n**mandatory**",
    "3-1": "`String` This parameter should contain a brief product description. It should be a string describing the product (The description type is entirely your choice). ",
    "3-2": "T-shirt",
    "4-0": "firstname  \n**mandatory**",
    "4-1": "`String` This parameter must contain the first name of the customer.",
    "4-2": "Ankit",
    "5-0": "email  \n**mandatory**",
    "5-1": "`String` This parameter must contain the email of the customer)",
    "5-2": "[test@gmail.com](mailto:test@gmail.com)",
    "6-0": "phone  \n**mandatory**",
    "6-1": "`integer` Merchant needs to take the customer’s GPay registered phone number and pass in this field. This field will be used for further mapping the customer VPA and initiate a collect request.",
    "6-2": " ",
    "7-0": "<<glossary:pg>>  \n**mandatory**",
    "7-1": "`String` The payment gateway is specified in this parameter. For QR,  specifiy **QR**.",
    "7-2": "QR",
    "8-0": "<<glossary:bankcode>>  \n**mandatory**",
    "8-1": "`String` Each payment option is identified with a unique bank code at PayU. You must use any of the following bank code for QR:  \n  \n- **UPIQR** for accepting payments with UPI QR.\n- **BQR** for accepting payments with Bharath QR",
    "8-2": "UPIQR",
    "9-0": "surl  \n**mandatory**",
    "9-1": " `String`The \"surl\" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.",
    "9-2": "<https://apiplayground-response.herokuapp.com/>",
    "10-0": "furl  \n**mandatory**",
    "10-1": "`String`The \"furl\" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.",
    "10-2": "<https://apiplayground-response.herokuapp.com/>",
    "11-0": "<<glossary:hash>>  \n**mandatory**",
    "11-1": "`String`The hash calculated by the merchant using the key and salt provided by PayU. The format for calculating the hash: `sha512(key\\|txnid\\|amount\\|productinfo\\|firstname\\|email\\|udf1\\|udf2\\|udf3\\|udf4\\|udf5\\||\\||\\||SALT)\n`For more information, refer to [Generate Hash](doc:hashing-request-and-response).",
    "11-2": " ",
    "12-0": "lastname  \n**optional**",
    "12-1": "`string`The last name of the customer.",
    "12-2": "",
    "13-0": "address1  \n**optional**",
    "13-1": "`string`The first line of the billing address.",
    "13-2": "",
    "14-0": "address2  \n**optional**",
    "14-1": "`string`The second line of the billing address.",
    "14-2": "",
    "15-0": "city  \n**optional**",
    "15-1": "`string`The city where your customer resides as part of the billing address.",
    "15-2": "",
    "16-0": "state  \n**optional**",
    "16-1": "`string`The state where your customer resides as part of the billing address,",
    "16-2": "",
    "17-0": "country  \n**optional**",
    "17-1": "`string`The country where your customer resides.",
    "17-2": "",
    "18-0": "zipcode  \n**optional**",
    "18-1": "`string`Billing address zip code is mandatory for the cardless EMI option.",
    "18-2": "",
    "19-0": "udf1",
    "19-1": "`string`This parameter has been made for you to keep any information corresponding to the transaction.",
    "19-2": "",
    "20-0": "udf2  \n**optional**",
    "20-1": "`string` This parameter has been made for you to keep any information corresponding to the transaction.",
    "20-2": "",
    "21-0": "udf3",
    "21-1": "`string` This parameter has been made for you to keep any information corresponding to the transaction.",
    "21-2": "",
    "22-0": "udf4  \n**optional**",
    "22-1": "`string` This parameter has been made for you to keep any information corresponding to the transaction.",
    "22-2": "",
    "23-0": "udf5",
    "23-1": "`string` This parameter has been made for you to keep any information corresponding to the transaction.",
    "23-2": ""
  },
  "cols": 3,
  "rows": 24,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


<HashingRequestParameters />

### Sample request

```curl
curl -X \
 POST "https://test.payu.in/_payment" -H \
 "accept: application/json" -H \
 "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=ewP8oRopzdHEtC&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=QR&bankcode=UPIQR&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"
```

## Step 2: Check response from PayU

<ReverseHashing />

### Sample response (parsed)

```
(
    [mihpayid] => 403993715524045752
    [mode] => QR
    [status] => success
    [unmappedstatus] => captured
    [key] => JPM7Fg
    [txnid] => ewP8oRopzdHEtC
    [amount] => 10.00
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2021-09-06 13:27:08
    [productinfo] => iPhone
    [firstname] => Ashish
    [lastname] =>
    [address1] =>
    [address2] =>
    [city] =>
    [state] =>
    [country] =>
    [zipcode] =>
    [email] => test@gmail.com
    [phone] => 9876543210
    [udf1] =>
    [udf2] =>
    [udf3] =>
    [udf4] =>
    [udf5] =>
    [udf6] =>
    [udf7] =>
    [udf8] =>
    [udf9] =>
    [udf10] =>
    [hash] => 1be7e6e97ab1ea9034b9a107e7cf9718308aa9637b4dbbd1a3343c91b0da02b34a40d00ac7267ebe81c20ea1129b931371c555d565bc6e11f470c3d2cf69b5a3
    [field1] =>
    [field2] =>
    [field3] =>
    [field4] =>
    [field5] =>
    [field6] =>
    [field7] =>
    [field8] =>
    [field9] => Transaction Completed Successfully
    [payment_source] => payu
    [PG_TYPE] => QR-PG
    [bank_ref_num] => 87d3b2a1-5a60-4169-8692-649f61923b3d
    [bankcode] => UPIQR
    [error] => E000
    [error_Message] => No Error
)
```

## Step 3: Verify the payment

Verify the transaction details using the Verification APIs. For more information, refer to <a href="verify_payment_api" target="_blank">Verify Payment API</a> under API Reference.

> 📘 Tip
> 
> The transaction ID that you posted in Step 1 with PayU must be used here.