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

1. [Initiate payment request](#step-1-initiate-payment-request)
2. [Invoke UPI Intent on customer’s device](https://https://docs.payu.in/reference/upi-s2s-partner-integration-api/docs/whatsapp-refund-status-api#step-2-invoke-upi-intent-on-customers-device)
3. [Verify payment](#step-3-verify-payment-api)
4. [PayU sends Server-to-Server callback response](#step-4-payu-sends-server-to-server-call-back-response)

## Step 1: Initiate payment request

**Environment**

|           |                                                                                                    |
| --------- | -------------------------------------------------------------------------------------------------- |
| UAT Host  | \<[https://test-partnerapilayer.payu.in/apilayer>](https://test-partnerapilayer.payu.in/apilayer>) |
| PROD Host | \<[https://api.payu.in>](https://api.payu.in>)                                                     |

### Request headers

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Value</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Content-Type</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>application/json</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Authorization</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Bearer <token><br>Where, &lt;token&gt; must be substituted with 039e0d1d70f467f946e2d73bd43868df856cfaa352ea54591a76bfc4a08d3487</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### Request parameters

The following table lists the request parameter descriptions for Partner Payment integration.

> 📘 Extra params for Partner integration:
>
> The following params are the extra parameters (optional) used compared to the regular **_payment** API, but with a different endpoint:  partner_udf_3, partner_udf_4, shipping_firstname, shipping_lastname, shipping_address1, shipping_address2, shipping_city, shipping_state, shipping_country, shipping_zipcode,  shipping_phone

| Parameter | Description | Example |
|-----------|-------------|---------|
| merchant_id<br/>`mandatory` | `String` This parameter is the unique Merchant id provided by PayU for your merchant account. The Merchant id acts as the unique identifier (primary key) to identify a particular Merchant Account in our database. | 8488225 |
| txnid<br/>`mandatory` | `varchar` This parameter is known as Transaction ID (or OrderID). It is the order reference number generated at your (Merchant's) end. It is an identifier which you(merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of same Transaction ID again would fail. Hence, it is essential that you post us a unique transaction ID for every new transaction (Please make sure that the transaction ID being sent to us hasn't been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID'). | fd3e847h2 |
| amount<br/>`mandatory` | `float` This parameter should contain the payment amount of the particular transaction. Note: Type-cast the amount to float type | 10 |
| productinfo<br/>`mandatory` | `varchar` This parameter should contain a brief product description. It should be a string describing the product (The description type is entirely your choice). | T-shirt |
| firstname<br/>`mandatory` | `varchar` This parameter must contain the first name of the customer. | Ankit |
| email<br/>`mandatory` | `varchar` This parameter must contain the email of the customer | test@gmail.com |
| phone<br/>`mandatory` | `integer` Merchant needs to take the customer's GPay registered phone number and pass in this field. This field will be used for further mapping the customer VPA and initiate a collect request. |  |
| txn_s2s_flow<br/>`mandatory` | `integer` This parameter is to indicate the transaction is S2S flow. Pass this parameter value as 4. | 4 |
| hash<br/>`mandatory` | `varchar` Hash is a crucial parameter – used specifically to avoid any tampering during the transaction. There are two different methods to calculate hash. Please follow method 1 only. Method 2 is just there for the documentation and is not to be used This is the simplest way of calculating the hash value. Here, please make sure that the api_version parameter is NOT POSTED from your end. For hash calculation, you need to generate a string using certain parameters and apply the sha512 algorithm to this string.<br/>Note: You have to use pipe (\|) character in between these parameters as mentioned below. The parameter order is mentioned below: sha512(merchant_id\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|CLIENT_SECRET) All these parameters have already been mentioned earlier in this table. Here, SALT (to be provided by PayU), key, txnid, amount productinfo, firstname, email are mandatory parameters and hence can't be empty in hash calculation above. But, udf1-udf5 are optional and hence you need to calculate the hash based upon the fact that whether you are posting a particular udf or not. For example, if you are NOT posting udf1. Then, in the hash calculation, udf1 field will be left empty. The following examples will clarify various scenarios of hash calculation:<br/>• Case 1: If all the udf parameters (udf1-udf5) are posted by the merchant. Then, hash=sha512(merchant_id\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|CLIENT_SECRET)<br/>• Case 2: If only some of the udf parameters are posted and others are not. For example, if udf2 and udf4 are posted and udf1, udf3, udf5 are not. Then, hash=sha512(merchant_id\|txnid\|amount\|productinfo\|firstname\|email\|\|udf2\|\|udf4\|\|\|\|\|\|\|CLIENT_SECRET)<br/>• Case 3: If NONE of the udf parameters (udf1-udf5) are posted. Then, hash=sha512(merchant_id\|txnid\|amount\|productinfo\|firstname\|email\|\|\|\|\|\|\|\|\|\|\|\|CLIENT_SECRET)<br/>Example: If merchant_id=6631711, txnid=12345, amount=10, productinfo=Shopping, firstname=Test, email=test@test.com, udf2=abc, udf4=15, CLIENT_SECRET=3sf0jURk91319391949941414195821851313 and udf1, udf3, udf5 are not posted. Then, the hash would be calculated as Case 2 above: sha512(6631711\|12345\|10\|Shopping\|Test\|test@test.com\|\|abc\|\|15\|\|\|\|\|\|\|3sf0jURk91319391949941414195821851313)<br/>IMPORTANT: For details related to hash at the time of postback from PayU to the merchant, please refer to the later section. This is also absolutely mandatory to avoid any tampering. |  |
| s2s_client_ip<br/>`mandatory` | `varchar` This parameter must have the source IP of the user |  |
| s2s_device_info<br/>`mandatory` | `varchar` This parameter must have the user agent of the device |  |
| reseller_id<br/>`mandatory` | `varchar` This parameter is the unique Partner Identifier provided by PayU for your partner account. The Partner Identifier acts as the unique identifier to identify a particular Partner Account in our database. | 83fe-eb64-021844d8-9397-26535b1bf0c2 |
| udf5<br/>`mandatory` | `string` This parameter has been made for you to keep any information corresponding to the transaction. Pass **whatsapp** in this field | whatsapp |
| address1<br/>`optional` | `string` The first line of the billing address. |  |
| address2<br/>`optional` | `string` The second line of the billing address. |  |
| city<br/>`optional` | `string` The city where your customer resides as part of the billing address. |  |
| state<br/>`optional` | `string` The state where your customer resides as part of the billing address. |  |
| country<br/>`optional` | `string` The country where your customer resides. |  |
| zipcode<br/>`optional` | `string` Billing address zip code is mandatory for the cardless EMI option. |  |
| partner_udf_3<br/>`optional` | This parameter has been made for partner to pass any information corresponding to the transaction. |  |
| partner_udf_4<br/>`optional` | This parameter has been made for partner to pass any information corresponding to the transaction. |  |
| shipping_firstname<br/>`optional` | `string` The first name of shipping person. |  |
| shipping_lastname<br/>`optional` | `string` The last name of shipping person. |  |
| shipping_address1<br/>`optional` | `string` The first line of the shipping address. |  |
| shipping_address2<br/>`optional` | `string` The second line of the shipping address. |  |
| shipping_city<br/>`optional` | `string` The city where your customer resides as part of the shipping address. |  |
| shipping_state<br/>`optional` | `string` The state where your customer resides as part of the shipping address. |  |
| shipping_country<br/>`optional` | `string` The country where your customer resides as part of the shipping address. |  |
| shipping_zipcode<br/>`optional` | `string` Shipping address zip code. |  |
| shipping_phone<br/>`optional` | `string` The phone no your customer resides as part of the shipping address. |  |
| drop_category<br/>`optional` | `string` This parameter can be used if you want to hide one or multiple payment options. For example, if you want to collect the payment using debit card and Net Banking, you can hide the credit card mode of payment. |  |
| enforce_paymethod<br/>`optional` | `string` This parameter allows you to customize the payment options for each transaction. You can enforce specific payment modes, cards scheme, and specific banks under Net Banking using this method. |  |
| user_token<br/>`optional` | `string` This parameter is used to uniquely identify a user for a merchant. |  |
| offer_key<br/>`optional` | `string` List of keys to filter the offer. |  |
| offer_auto_apply<br/>`optional` | `string` This parameter contains a flag to specify whether the offer can be automatically applied. |  |
| additional_charges<br/>`optional` | `string` The additional amount that needs to be charged. The additional amount will be added to the amount of the product by PayU |  |


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

After the response is received from the transacting app (BHIM/Google Pay/PhonePe/AxisPay/Any other app), a merchant can check the status of the transaction using the **verify_payment** API**.**

#### Failed responses

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Code</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Reason</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Response</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>401</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>with invalid token</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {<br>“message”: “Invalid Auth token”<br>}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>403</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>with invalid hash</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {<br>“message”: “Invalid Hash”<br>}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>without reseller_id</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {<br>“errors”: [<br>“reseller_id is mandatory.”<br>]<br>}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>without amount</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {<br>“errors”: [  </p>
<p>“amount is mandatory param”<br>]<br>}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>without merchant_id</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {<br>“errors”: [<br>“merchant_id is mandatory param”<br>]<br>}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>without hash</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {<br>“errors”: [<br>“hash is mandatory param”<br>]<br>}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>without product_info</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {<br>“errors”: [<br>“product_info is mandatory param”<br>]<br>}</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Step 3: Verify Payment API

Check the UPI transaction status using the **Verify Payment API** (check_upi_txn_status) API.

After the response is received from your customer’s app (BHIM, Google Pay, PhonePe, AxisPay, or any other app), you can check the status of the transaction using the **Verify Payment API**. Web services can be accessed by making a server-to-server call using the following PayU URLs.

**Environment**

|           |                                                                                                    |
| --------- | -------------------------------------------------------------------------------------------------- |
| UAT Host  | \<[https://test-partnerapilayer.payu.in/apilayer>](https://test-partnerapilayer.payu.in/apilayer>) |
| PROD Host | \<[https://api.payu.in>](https://api.payu.in>)                                                     |

### Request headers

| Parameter     | Value                                                            |
| ------------- | ---------------------------------------------------------------- |
| Content-Type  | application/json                                                 |
| Authorization | 039e0d1d70f467f946e2d73bd43868df856cfaa352ea54591a76bfc4a08d3487 |

### Request parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px;"> Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txnid</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>In this parameter, you can include the txnid (Your transaction ID/order ID).</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>100123</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>merchant_id</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>It is the merchant id that PayU provided you.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>8238480</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>hash</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash is mentioned below:<br><code>sha512(merchant_id\|command\|txnid\|client_secret) sha512 </code>is the encryption method used here.  </p>
<ul>
<li><strong>client_secret</strong>– These credentials are only accessible to a partner(WhatsApp).</li>
<li><strong>command</strong> has constant value as <strong>verify_payment</strong>.</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>resseler_id</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>varchar This parameter is the unique Partner Identifier provided by PayU for your partner account. The Partner Identifier acts as the unique identifier to identify a particular Partner Account in our database.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>83fe-eb64-021844d8-9397-26535b1bf0c3</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

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

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">JSON Field</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>mihpayid</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains a unique reference number created for each transaction at PayU’s end. You must note this transaction ID as this will be used as a reference for all the future actions on this transaction like Inquiry or Refund.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>request_id</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field would contain the request ID value posted by the merchant during the transaction request.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>bankrefnum</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>For each successful transaction – this field would contain the bank reference number generated by the bank.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>amt</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the net amount debited from the customer’s account for this transaction.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>transaction_amount</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the original amount which was sent in the transaction request by the merchant</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>productinfo</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the same value of product information which was sent in the transaction request from the merchant’s end to PayU.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>firstname</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the same value of first name which was sent in the transaction request from the merchant’s end to PayU.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>bankcode</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the code indicating the payment option used for the transaction. For example, in the Debit Card mode, there are different options like Visa Debit Card, Mastercard, Maestro etc. For each option, a unique bank code exists. It would be returned in this bank code parameter. For example, Visa Debit Card – VISA, Master Debit Card – MAST.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>udf1</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the same value of udf values that were sent in the transaction request from the merchant’s end to PayU. It ranges from udf1 to udf5.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>udf3</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the same value of udf values that were sent in the transaction request from the merchant’s end to PayU. It ranges from udf1 to udf5.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>udf4</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the same value of udf values that were sent in the transaction request from the merchant’s end to PayU. It ranges from udf1 to udf5.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>udf5</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the same value of udf values that were sent in the transaction request from the merchant’s end to PayU. It ranges from udf1 to udf5.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>field2, field3</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The auth code from the bank is displayed in this field.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>field9</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the failure reason if the transaction has failed.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>error_code</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the error code for the transaction.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>net_amount_debit</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the net amount debited from the customer’s account for this transaction. It is calculated as:<br><code> transaction\_fee= actual\_discount + additional\_charges</code></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>added_on</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the transaction timestamp returned in this parameter.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>payment_source</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the payment source. PayU is returned for the transactions made with PayU.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>card_type</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the card type used for the transaction if the cards are used.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>error_Message</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the error message for the transaction (if any).</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>net_amount_debit</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the net amount debited from the customer’s account for this transaction.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>disc</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the discount amount for the customer.<br><strong>Note</strong>: For <strong>Cashback</strong> type offers, the discount amount will always be sent as <strong>zero</strong>(**0**) by PayU.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Mode</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the mode of payment.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>PG_TYPE</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the information on the payment gateway used for the transaction. For example, if CC PG was used, it would contain the value CC-PG. Similarly, it would have a unique value for all different types of payment gateways.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>card_no</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the card number for card transactions.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>name_on_card</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the name on card for card transactions.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>udf2</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the same value of udf values that were sent in the transaction request from the merchant’s end to PayU. It ranges from udf1 to udf5.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>field5</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the UPI VPA ID for UPI transactions.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>status</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the status of the transaction. For detailed information on the statuses, refer to <a href="ref:payment-state-explanations">Payment State Explanations</a></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>unmappedstatus</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the status of a transaction as per the internal database of PayU. PayU’s system has several intermediate statuses which are used for tracking various activities internal to the system. Hence, this status contains intermediate statuses of a transaction also – and hence is known as <strong>unmappedstatus</strong>. For detailed information on the statuses, refer to <a href="ref:payment-state-explanations">Payment State Explanations</a>.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Merchant_UTR</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the merchant Unique Transaction Reference (UTR) number.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Settled_at</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the time stamp of card settlement if the transaction is using credit cards.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

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

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Code</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Reason</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Response</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>401</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>with invalid token</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {  </p>
<p>“message”: “Invalid Auth token”  </p>
<p>}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>403</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>with invalid hash</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {  </p>
<p>“message”: “Invalid Hash”  </p>
<p>}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>without reseller_id</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {  </p>
<p>“errors”: [  </p>
<p>“reseller_id is mandatory.”  </p>
<p>]  </p>
<p>}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>without merchant_id</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {  </p>
<p>“errors”: [  </p>
<p>“merchant_id is mandatory param”  </p>
<p>]  </p>
<p>}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>without hash</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {  </p>
<p>“errors”: [  </p>
<p>“hash is mandatory param”  </p>
<p>]  </p>
<p>}</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

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