---
title: UPI S2S Integration API - Partner Integration
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
In order to initiate payments for partners, Whatsapp needs to use the access token instead of key/salt.

The following steps allow you to integrate the server-to-server UPI intent:

1. [Initiate payment request](https://payu-hosted-checkout.readme.io/docs/whatsapp-refund-status-api#step-1-initiate-payment-request)
2. [Invoke UPI Intent on customer’s device](https://payu-hosted-checkout.readme.io/docs/whatsapp-refund-status-api#step-2-invoke-upi-intent-on-customers-device)
3. [Verify payment](https://payu-hosted-checkout.readme.io/docs/whatsapp-refund-status-api#step-3-verify-payment-api)
4. [PayU sends Server-to-Server callback response](https://payu-hosted-checkout.readme.io/docs/whatsapp-refund-status-api#step-4-payu-sends-server-to-server-call-back-response)

## Step 1: Initiate payment request

**Environment**

|           |                                                 |
| --------- | ----------------------------------------------- |
| UAT Host  | <https://test-partnerapilayer.payu.in/apilayer> |
| PROD Host | <https://api.payu.in>                           |

### Request headers

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Value",
    "0-0": "Content-Type",
    "0-1": "application/json",
    "1-0": "Authorization",
    "1-1": "Bearer <token>  \nWhere, \\<token> must be substituted with 039e0d1d70f467f946e2d73bd43868df856cfaa352ea54591a76bfc4a08d3487"
  },
  "cols": 2,
  "rows": 2,
  "align": [
    null,
    null
  ]
}
[/block]


### Request parameters

The following table lists the request parameter descriptions for Partner Payment integration.

> 📘 Extra params for Partner integration:
> 
> The following params are the extra parameters (optional) used compared to the regular **\_payment** API, but with a different endpoint:  partner_udf_3, partner_udf_4, shipping_firstname, shipping_lastname, shipping_address1, shipping_address2, shipping_city, shipping_state, shipping_country, shipping_zipcode,  shipping_phone

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "merchant\\_id  **mandatory**",
    "0-1": "`String` This parameter is the unique Merchant id provided by PayU for your merchant account. The Merchant id acts as the unique identifier (primary key) to identify a particular Merchant Account in our database.",
    "0-2": "8488225",
    "1-0": "txnid  \n**mandatory**",
    "1-1": "`varchar` This parameter is known as Transaction ID (or OrderID). It is the order reference number generated at your (Merchant’s) end. It is an identifier which you(merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of same Transaction ID again would fail. Hence, it is essential that you post us a unique transaction ID for every new transaction (Please make sure that the transaction ID being sent to us hasn’t been successful earlier. In case of this duplication, the customer would get an error of ‘duplicate Order ID’).",
    "1-2": "fd3e847h2",
    "2-0": "amount  **mandatory**",
    "2-1": "`float` This parameter should contain the payment amount of the particular transaction. Note: Type-cast the amount to float type",
    "2-2": "10",
    "3-0": "productinfo  **mandatory**",
    "3-1": "`varchar` This parameter should contain a brief product description. It should be a string describing the product (The description type is entirely your choice). ",
    "3-2": "T-shirt",
    "4-0": "firstname  **mandatory**",
    "4-1": "`varchar` This parameter must contain the first name of the customer.",
    "4-2": "Ankit",
    "5-0": "email  \n**mandatory**",
    "5-1": "`varchar` This parameter must contain the email of the customer)",
    "5-2": "[test@gmail.com](mailto:test@gmail.com)",
    "6-0": "phone  **mandatory**",
    "6-1": "`integer` Merchant needs to take the customer’s GPay registered phone number and pass in this field. This field will be used for further mapping the customer VPA and initiate a collect request.",
    "6-2": " ",
    "7-0": "txn\\_s2s\\_flow  **mandatory**",
    "7-1": "`integer` This parameter is to indicate the transaction is S2S flow. Pass this parameter value as 4.",
    "7-2": "4",
    "8-0": "hash  \n**mandatory**",
    "8-1": "`varchar` varchar Hash is a crucial parameter – used specifically to avoid any tampering during the transaction. There are two different methods to calculate hash. Please follow method 1 only. Method 2 is just there for the documentation and is not to be used This is the simplest way of calculating the hash value. Here, please make sure that the api_version parameter is NOT POSTED from your end. For hash calculation, you need to generate a string using certain parameters and apply the sha512 algorithm to this string.  \nNote: You have to use pipe (|) character in between these parameters as mentioned below. The parameter order is mentioned below: sha512(merchant_id|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|u df5||||||CLIENT_SECRET) All these parameters (and their descriptions) have already been mentioned earlier in this table. Here, SALT (to be provided by PayU), key, txnid, amount productinfo, firstname, email are mandatory parameters and hence can’t b empty in hash calculation above. But, udf1-udf5 are optional and hence you nee to calculate the hash based upon the fact that whether you are posting a particular udf or not. For example, if you are NOT posting udf1. Then, in the has calculation, udf1 field will be left empty. The following examples will clarify various scenarios of hash calculation:  \n  \n- Case 1: If all the udf parameters (udf1-udf5) are posted by the merchant. Then, hash=sha512(merchant_id|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3| udf4|udf5||||||CLIENT_SECRET)\n- Case 2: If only some of the udf parameters are posted and others are not. For example, if udf2 and udf4 are posted and udf1, udf3, udf5 are not. Then, hash=sha512(merchant_id|txnid|amount|productinfo|firstname|email||udf2||udf4|||||||CLIENT_SECRET) Case 3: If NONE of the udf parameters (udf1-udf5) are posted. Then, hash=sha512(merchant_id|txnid|amount|productinfo|firstname|email|||||||||||CLIENT_SECRET) Example: If merchant_id=6631711, txnid=12345, amount=10, productinfo=Shopping, firstname=Test, email=[test@test.com](mailto:test@test.com), udf2=abc, udf4=15, CLIENT_SECRET=3sf0jURk91319391949941414195821851313 and udf1, udf3, udf5 are not posted. Then, the hash would be calculated as Case 2 above: sha512(6631711|12345|10|Shopping|Test|[test@test.com](mailto:test@test.com)||abc||15|||||||3sf0jURk91319391949941414195821851313) (This value comes out to be 7a83339ccf2dde9d31569b00eea70a60174b3af3ceaa773d17a84b90c9eedad5f744ba02f95a572d8fe8592346ebb537bede49ad1ec786469b4bd77531d19b87) IMPORTANT: For details related to hash at the time of postback from PayU to the merchant, please refer to the later section. This is also absolutely mandatory to avoid any tampering.",
    "8-2": " ",
    "9-0": "s2s\\_client\\_ip  **mandatory**",
    "9-1": "varchar This parameter must have the source IP of the user",
    "9-2": " ",
    "10-0": "s2s\\_device\\_info  **mandatory**",
    "10-1": "varchar This parameter must have the user agent of the device",
    "10-2": " ",
    "11-0": "reseller\\_id  **mandatory**",
    "11-1": "varchar This parameter is the unique Partner Identifier provided by PayU for your partner account. The Partner Identifier acts as the unique identifier to identify a particular Partner Account in our database.",
    "11-2": " 83fe-eb64-021844d8-9397-26535b1bf0c2",
    "12-0": "udf5  \n**mandatory**",
    "12-1": "`string` This parameter has been made for you to keep any information corresponding to the transaction. Pass **whatsapp** in this field",
    "12-2": "whatsapp",
    "13-0": "address1  **optional**",
    "13-1": "`string` The first line of the billing address.",
    "13-2": " ",
    "14-0": "address2  **optional**",
    "14-1": "`string` The second line of the billing address.",
    "14-2": " ",
    "15-0": "city  \n**optional**",
    "15-1": "`string` The city where your customer resides as part of the billing address.",
    "15-2": " ",
    "16-0": "state  \n**optional**",
    "16-1": "`string` The state where your customer resides as part of the billing address.",
    "16-2": " ",
    "17-0": "country  \n**optional**",
    "17-1": "`string` The country where your customer resides.",
    "17-2": " ",
    "18-0": "zipcode  \n**optional**",
    "18-1": "`string` Billing address zip code is mandatory for the cardless EMI option.",
    "18-2": " ",
    "19-0": "partner_udf_3  \n**optional**",
    "19-1": "This parameter has been made for partner to pass any information corresponding to the transaction.",
    "19-2": "",
    "20-0": "partner_udf_4  \n**optional**",
    "20-1": "This parameter has been made for partner to pass any information corresponding to the transaction.",
    "20-2": "",
    "21-0": "shipping\\_firstname  **optional**",
    "21-1": "`string` The first name of shipping person.",
    "21-2": " ",
    "22-0": "shipping\\_lastname  **optional**",
    "22-1": "`string` The last name of shipping person.",
    "22-2": " ",
    "23-0": "shipping\\_address1  **optional**",
    "23-1": "`string` The first line of the shipping address.",
    "23-2": " ",
    "24-0": "shipping\\_address2  **optional**",
    "24-1": "`string` The second line of the shipping address.",
    "24-2": " ",
    "25-0": "shipping\\_city  **optional**",
    "25-1": "`string` The city where your customer resides as part of the shipping address.",
    "25-2": " ",
    "26-0": "shipping\\_state  **optional**",
    "26-1": "`string` The state where your customer resides as part of the shipping address.",
    "26-2": " ",
    "27-0": "shipping\\_country  **optional**",
    "27-1": "`string` The country where your customer resides as part of the shipping address.",
    "27-2": " ",
    "28-0": "shipping\\_zipcode  **optional**",
    "28-1": "`string` Shipping address zip code.",
    "28-2": " ",
    "29-0": "shipping\\_phone  **optional**",
    "29-1": "`string` The phone no your customer resides as part of the shipping address.",
    "29-2": " ",
    "30-0": "drop\\_category  **optional**",
    "30-1": "`string`  This parameter can be used if you want to hide one or multiple payment options. For example, if you want to collect the payment using debit card and Net Banking, you can hide the credit card mode of payment.",
    "30-2": " ",
    "31-0": "enforce\\_paymethod  **optional**",
    "31-1": "`string`  This parameter allows you to customize the payment options for each transaction. You can enforce specific payment modes, cards scheme, and specific banks under Net Banking using this method.",
    "31-2": " ",
    "32-0": "user\\_token  **optional**",
    "32-1": "`string`This parameter is used to uniquely identify a user for a merchant.",
    "32-2": " ",
    "33-0": "offer\\_key  **optional**",
    "33-1": "`string` List of keys to filter the offer.",
    "33-2": " ",
    "34-0": "offer\\_auto\\_apply",
    "34-1": "`string`This parameter contains a flag to specify whether the offer can be automatically applied.",
    "34-2": " ",
    "35-0": "additional\\_charges  **optional**",
    "35-1": "`string`The additional amount that needs to be charged. The additional amount will be added to the amount of the product by PayU",
    "35-2": " "
  },
  "cols": 3,
  "rows": 36,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


### Sample request

```curl
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/payments' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer 9d2ab8e1b99aa02f6b827af5b5000b277d9cb1cd037acb7cb31436a5b0da4f74' \
--data-raw '{
    "txnid": "nY3tkz3vciHFGTjblyFeycL2Zn1m",
    "amount": 1090.33,
    "productinfo": "whatsapp",
    "firstname": "Manikanta",
    "reseller_id": "83fe-eb64-021844d8-9397-26535b1bf0c2",
    "merchant_id": 8238480,
    "phone": 7036722360,
    "hash": "5aadceaf6bec9158ccba8ec0dab32debcacbfd50e3587c077fa11107a5be0ac26712fae230522afb8908d068122c02f2d5c733a46c33ace0f66e5cc9d2ae4714",
    "lastname": "CHeruku",
    "email": "manik.cr24@gmail.com",
    "curl": "https://www.google.com",
    "furl": "https://www.google.com",
    "surl": "https://www.youtube.com",
    "txn_s2s_flow": "4",
    "s2s_device_info": "ewew",
    "s2s_client_ip": "ewew"
}'
```

### Sample response

```plaintext
{
    "metaData": {
        "message": null,
        "referenceId": "024d9afbdbf85bd35b25649ccf983e16ee3d4646c2cdcffada88bd2df371fd43",
        "statusCode": null,
        "txnId": "nY3tkz3vciHFGTjblyFeycL2Zn1m",
        "txnStatus": "pending",
        "unmappedStatus": "pending"
    },
    "result": {
        "paymentId": 403993715529028543,
        "merchantName": "Merchant",
        "merchantVpa": null,
        "amount": "1090.33",
        "intentURIData": "pa=&pn=&tr=403993715529028543&tid=PPPL403993715529028543290523133325&am=1090.33&cu=INR&tn=UPI Transaction for PPPL403993715529028543290523133325",
        "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vdGVzdC5wYXl1LmluLzAyNGQ5YWZiZGJmODViZDM1YjI1NjQ5Y2NmOTgzZTE2NGQ0YTUxYzYzNjcyODAxNjRkMDlkNDg2YjRkYWI1ZmEvaW50ZW50U2VhbWxlc3NIYW5kbGVyLnBocCIgbWV0aG9kPSJwb3N0Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJ0b2tlbiIgdmFsdWU9IjE2NTIyQTgxLTUwMjYtMUUyRi0zNDFCLTJFQ0MyQ0Y5RTE1QyI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iYW1vdW50IiB2YWx1ZT0iMTA5MC4zMyI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0ibWlocGF5aWQiIHZhbHVlPSIwMjRkOWFmYmRiZjg1YmQzNWIyNTY0OWNjZjk4M2UxNmVlM2Q0NjQ2YzJjZGNmZmFkYTg4YmQyZGYzNzFmZDQzIj48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJkaXNhYmxlSW50ZW50U2VhbWxlc3NGYWlsdXJlIiB2YWx1ZT0iMSI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0icGF5ZWVWcGEiIHZhbHVlPSIiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InBheWVlTmFtZSIgdmFsdWU9Ik1lcmNoYW50Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJhZGRpdGlvbmFsQ2hhcmdlcyIgdmFsdWU9IjAiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InRyYW5zYWN0aW9uRmVlIiB2YWx1ZT0iMTA5MC4zMyI+PC9mb3JtPjxzY3JpcHQgdHlwZT0ndGV4dC9qYXZhc2NyaXB0Jz4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdpbmRvdy5vbmxvYWQ9ZnVuY3Rpb24oKXsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBkb2N1bWVudC5mb3Jtc1sncGF5bWVudF9wb3N0J10uc3VibWl0KCk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAgICAgICAgIDwvc2NyaXB0PjwvYm9keT48L2h0bWw+",
        "otpPostUrl": "https://test.payu.in/ResponseHandler.php"
    }
}
```

## Step 2: Invoke UPI Intent on Customer’s Device

Partner to open the UPI Intent as per the **NPCI Guidelines**. This URL can then be fired using an Intent or a hyperlink which would open an Intent tray with a list of available supporting apps in the user’s mobile device. Below is a sample UPI deep link URL and the format used for creating the URL:

**Sample URL** (with values from above sample JSON): 

```plaintext
upi://pay?<IntentURIData>
```

**Format for UPI Deep Linking URL** (as per NPCI guidelines):

```plaintext
"upi://pay"+ <intentURIData>
```

After the response is received from the transacting app (BHIM/Google Pay/PhonePe/AxisPay/Any other app), a merchant can check the status of the transaction using the **verify\_payment** API**.**

#### Failed responses

[block:parameters]
{
  "data": {
    "h-0": "**Code**",
    "h-1": "**Reason**",
    "h-2": "**Response**",
    "0-0": "401",
    "0-1": "with invalid token",
    "0-2": " {  \n“message”: “Invalid Auth token”  \n}",
    "1-0": "403",
    "1-1": "with invalid hash",
    "1-2": " {  \n“message”: “Invalid Hash”  \n}",
    "2-0": "400",
    "2-1": "without reseller\\_id",
    "2-2": " {  \n“errors”: [  \n“reseller_id is mandatory.”  \n]  \n}",
    "3-0": "400",
    "3-1": "without amount",
    "3-2": " {  \n“errors”: \\[  \n  \n“amount is mandatory param”  \n]  \n}",
    "4-0": "400",
    "4-1": "without merchant\\_id",
    "4-2": " {  \n“errors”: [  \n“merchant_id is mandatory param”  \n]  \n}",
    "5-0": "400",
    "5-1": "without hash",
    "5-2": " {  \n“errors”: [  \n“hash is mandatory param”  \n]  \n}",
    "6-0": "400",
    "6-1": "without product\\_info",
    "6-2": " {  \n“errors”: [  \n“product_info is mandatory param”  \n]  \n}"
  },
  "cols": 3,
  "rows": 7,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


## Step 3: Verify Payment API

Check the UPI transaction status using the **Verify Payment API** (check\_upi\_txn\_status) API.

After the response is received from your customer’s app (BHIM, Google Pay, PhonePe, AxisPay, or any other app), you can check the status of the transaction using the **Verify Payment API**. Web services can be accessed by making a server-to-server call using the following PayU URLs.

**Environment**

|           |                                                 |
| --------- | ----------------------------------------------- |
| UAT Host  | <https://test-partnerapilayer.payu.in/apilayer> |
| PROD Host | <https://api.payu.in>                           |

### Request headers

| Parameter     | Value                                                            |
| ------------- | ---------------------------------------------------------------- |
| Content-Type  | application/json                                                 |
| Authorization | 039e0d1d70f467f946e2d73bd43868df856cfaa352ea54591a76bfc4a08d3487 |

### Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": " Example",
    "0-0": "txnid",
    "0-1": "In this parameter, you can include the txnid (Your transaction ID/order ID).",
    "0-2": "100123",
    "1-0": "merchant\\_id",
    "1-1": "It is the merchant id that PayU provided you.",
    "1-2": "8238480",
    "2-0": "hash",
    "2-1": "This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash is mentioned below:  \n`sha512(merchant_id\\|command\\|txnid\\|client_secret) sha512 `is the encryption method used here.  \n  \n- **client_secret**– These credentials are only accessible to a partner(WhatsApp).\n- **command** has constant value as **verify_payment**.",
    "2-2": "",
    "3-0": "resseler\\_id",
    "3-1": "varchar This parameter is the unique Partner Identifier provided by PayU for your partner account. The Partner Identifier acts as the unique identifier to identify a particular Partner Account in our database.",
    "3-2": "83fe-eb64-021844d8-9397-26535b1bf0c3"
  },
  "cols": 3,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Sample Request

```curl
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment' \
--header 'Authorization: Bearer 9d2ab8e1b99aa02f6b827af5b5000b277d9cb1cd037acb7cb31436a5b0da4f74' \
--header 'Content-Type: application/json' \
--header 'Cookie: PHPSESSID=p576r3mrpdm29sersr0emhmc53' \
--data-raw '{
    "txnid": "nY3tkz3vciHFGTjblyFeycL2Zn2c",
    "merchant_id": "8238480",
    "reseller_id": "83fe-eb64-021844d8-9397-26535b1bf0c2",
    "hash": "0dd9057a6575f2f5531880b83f2f119356b9a841df18fc4487c1ab0fee8477d15d15cf43e37656b55a8bde0dbe048f0ef93b62420864ecbd7d7a5965300a4399"
}'
```

### Response parameters

[block:parameters]
{
  "data": {
    "h-0": "JSON Field",
    "h-1": "Description",
    "0-0": "mihpayid",
    "0-1": "This field contains a unique reference number created for each transaction at PayU’s end. You must note this transaction ID as this will be used as a reference for all the future actions on this transaction like Inquiry or Refund.",
    "1-0": "request\\_id",
    "1-1": "This field would contain the request ID value posted by the merchant during the transaction request.",
    "2-0": "bankrefnum",
    "2-1": "For each successful transaction – this field would contain the bank reference number generated by the bank.",
    "3-0": "amt",
    "3-1": "This field contains the net amount debited from the customer’s account for this transaction.",
    "4-0": "transaction\\_amount",
    "4-1": "This field contains the original amount which was sent in the transaction request by the merchant",
    "5-0": "productinfo",
    "5-1": "This field contains the same value of product information which was sent in the transaction request from the merchant’s end to PayU.",
    "6-0": "firstname",
    "6-1": "This field contains the same value of first name which was sent in the transaction request from the merchant’s end to PayU.",
    "7-0": "bankcode",
    "7-1": "This field contains the code indicating the payment option used for the transaction. For example, in the Debit Card mode, there are different options like Visa Debit Card, Mastercard, Maestro etc. For each option, a unique bank code exists. It would be returned in this bank code parameter. For example, Visa Debit Card – VISA, Master Debit Card – MAST.",
    "8-0": "udf1",
    "8-1": "This field contains the same value of udf values that were sent in the transaction request from the merchant’s end to PayU. It ranges from udf1 to udf5.",
    "9-0": "udf3",
    "9-1": "This field contains the same value of udf values that were sent in the transaction request from the merchant’s end to PayU. It ranges from udf1 to udf5.",
    "10-0": "udf4",
    "10-1": "This field contains the same value of udf values that were sent in the transaction request from the merchant’s end to PayU. It ranges from udf1 to udf5.",
    "11-0": "udf5",
    "11-1": "This field contains the same value of udf values that were sent in the transaction request from the merchant’s end to PayU. It ranges from udf1 to udf5.",
    "12-0": "field2, field3",
    "12-1": "The auth code from the bank is displayed in this field.",
    "13-0": "field9",
    "13-1": "This field contains the failure reason if the transaction has failed.",
    "14-0": "error\\_code",
    "14-1": "This field contains the error code for the transaction.",
    "15-0": "net\\_amount\\_debit",
    "15-1": "This field contains the net amount debited from the customer’s account for this transaction. It is calculated as:  \n` transaction\\_fee= actual\\_discount + additional\\_charges`",
    "16-0": "added\\_on",
    "16-1": "This field contains the transaction timestamp returned in this parameter.",
    "17-0": "payment\\_source",
    "17-1": "This field contains the payment source. PayU is returned for the transactions made with PayU.",
    "18-0": "card\\_type",
    "18-1": "This field contains the card type used for the transaction if the cards are used.",
    "19-0": "error\\_Message",
    "19-1": "This field contains the error message for the transaction (if any).",
    "20-0": "net\\_amount\\_debit",
    "20-1": "This field contains the net amount debited from the customer’s account for this transaction.",
    "21-0": "disc",
    "21-1": "This field contains the discount amount for the customer.  \n**Note**: For **Cashback** type offers, the discount amount will always be sent as **zero**(\\*\\*0\\*\\*) by PayU.",
    "22-0": "Mode",
    "22-1": "This field contains the mode of payment.",
    "23-0": "PG\\_TYPE",
    "23-1": "This field contains the information on the payment gateway used for the transaction. For example, if CC PG was used, it would contain the value CC-PG. Similarly, it would have a unique value for all different types of payment gateways.",
    "24-0": "card\\_no",
    "24-1": "This field contains the card number for card transactions.",
    "25-0": "name\\_on\\_card",
    "25-1": "This field contains the name on card for card transactions.",
    "26-0": "udf2",
    "26-1": "This field contains the same value of udf values that were sent in the transaction request from the merchant’s end to PayU. It ranges from udf1 to udf5.",
    "27-0": "field5",
    "27-1": "This field contains the UPI VPA ID for UPI transactions.",
    "28-0": "status",
    "28-1": "This field contains the status of the transaction. For detailed information on the statuses, refer to [Payment State Explanations](ref:payment-state-explanations)",
    "29-0": "unmappedstatus",
    "29-1": "This field contains the status of a transaction as per the internal database of PayU. PayU’s system has several intermediate statuses which are used for tracking various activities internal to the system. Hence, this status contains intermediate statuses of a transaction also – and hence is known as **unmappedstatus**. For detailed information on the statuses, refer to [Payment State Explanations](ref:payment-state-explanations).",
    "30-0": "Merchant\\_UTR",
    "30-1": "This field contains the merchant Unique Transaction Reference (UTR) number.",
    "31-0": "Settled\\_at",
    "31-1": "This field contains the time stamp of card settlement if the transaction is using credit cards."
  },
  "cols": 2,
  "rows": 32,
  "align": [
    null,
    null
  ]
}
[/block]


### Sample response

```plaintext
{
    "msg": "1 out of 1 Transactions Fetched Successfully",
    "transaction_details": {
        "wtsapp_txn_id5": {
            "mihpayid": "403993715529051451",
            "request_id": null,
            "bank_ref_num": null,
            "amt": "2.00",
            "transaction_amount": "2.00",
            "txnid": "wtsapp_txn_id5",
            "additional_charges": "0.00",
            "productinfo": "WA productinfo",
            "firstname": "WAfirstname",
            "bankcode": "INTENT",
            "udf1": null,
            "udf3": null,
            "udf4": null,
            "udf5": "",
            "field2": null,
            "field9": null,
            "error_code": null,
            "addedon": "2023-05-31 18:56:08",
            "payment_source": "payuPureS2S",
            "card_type": null,
            "error_Message": "",
            "meCode": "{\"pgMerchantId\":\"HDFC000000000106\",\"payu_aggregator\":\"1\",\"merchantVpa\":\"payu@axisbank\"}",
            "net_amount_debit": "0.00",
            "disc": "0.00",
            "mode": "UPI",
            "PG_TYPE": "UPI-PG",
            "card_no": "",
            "udf2": null,
            "status": "pending",
            "unmappedstatus": "in progress",
            "Merchant_UTR": null,
            "Settled_At": null,
            "App_Name": null
        }
    },
    "status": 1.0
}
```

#### Failed Responses

[block:parameters]
{
  "data": {
    "h-0": "**Code**",
    "h-1": "**Reason**",
    "h-2": "**Response**",
    "0-0": "401",
    "0-1": "with invalid token",
    "0-2": " {  \n  \n“message”: “Invalid Auth token”  \n  \n}",
    "1-0": "403",
    "1-1": "with invalid hash",
    "1-2": " {  \n  \n“message”: “Invalid Hash”  \n  \n}",
    "2-0": "400",
    "2-1": "without reseller\\_id",
    "2-2": " {  \n  \n“errors”: \\[  \n  \n“reseller_id is mandatory.”  \n  \n]  \n  \n}",
    "3-0": "400",
    "3-1": "without merchant\\_id",
    "3-2": " {  \n  \n“errors”: \\[  \n  \n“merchant_id is mandatory param”  \n  \n]  \n  \n}",
    "4-0": "400",
    "4-1": "without hash",
    "4-2": " {  \n  \n“errors”: \\[  \n  \n“hash is mandatory param”  \n  \n]  \n  \n}"
  },
  "cols": 3,
  "rows": 5,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


## Step 4: PayU sends Server-to-Server call-back response

PayU can also send a server-to-server call-back response whenever the transaction status gets updated.

#### Implementation

The server-to-server response would be sent by PayU on a pre-set URL, which has to be provided by you. PayU will configure it at your back end. This response would be sent in key/value pair separated by the ampersand (&) character. In case any parameter is not used, we would send it back to you with an empty string. The sample response is similar to the following:

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
error_message: No Error
name_on_card: test
cardnum: 411111XXXXXX1111
```