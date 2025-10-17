---
title: Hosted Checkout Integration - Partner Integration
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
To integrate with PayU Hosted Checkout for partners, you need to send a request and check the response. This will redirect the customer from the merchant’s website to PayU’s payment page to complete the payment. You can use the sample request and response in the provided documentation to get started.

The following steps allow you to integrate the PayU Hosted Checkout:

1. [Make the transaction request to PayU](#step-1-make-the-transaction-request-to-payu)
2. [Customer submits payment details on PayU page](#step-2-customer-submits-payment-details-on-payu-page)
3. [Validate the response from PayU](#step-3-validate-the-response-from-payu)
4. [Verify the Payment](#step-4-verify-the-payment)t
5. [PayU sends Server-to-Server callback response](#step-5-payu-sends-server-to-server-call-back-response)

## Step 1: Make the transaction request to PayU

|           |                                                                                                                                      |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| UAT Host- | \<[https://test-partnerapilayer.payu.in/apilayer/partner/payments>](https://test-partnerapilayer.payu.in/apilayer/partner/payments>) |
| PROD Host | \<[https://api.payu.in/partner/payments>](https://api.payu.in/partner/payments>)                                                     |

### **Request headers**

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Bearer <token><br>where, &lt;token&gt; must be substituted with 039e0d1d70f467f946e2d73bd43868df856cfaa352ea54591a76bfc4a08d3487</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### Request parameters

The following table lists the request parameter descriptions for Partner Payment integration.

<Callout icon="📘" theme="info">
  **Extra params for Partner integration**: The following params are the extra parameters (optional) used compared to the regular **_payment** API, but with a different endpoint:  partner_udf_3, partner_udf_4, shipping_firstname, shipping_lastname, shipping_address1, shipping_address2, shipping_city, shipping_state, shipping_country, shipping_zipcode,  shipping_phone
</Callout>

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>merchant_id<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter is the unique Merchant id provided by PayU for your merchant account. The Merchant id acts as the unique identifier (primary key) to identify a particular Merchant Account in our database.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>8488225</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txnid<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>varchar</code> This parameter is known as Transaction ID (or OrderID). It is the order reference number generated at your (Merchant’s) end. It is an identifier which you(merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of same Transaction ID again would fail. Hence, it is essential that you post us a unique transaction ID for every new transaction (Please make sure that the transaction ID being sent to us hasn’t been successful earlier. In case of this duplication, the customer would get an error of ‘duplicate Order ID’).</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>fd3e847h2</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>amount<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>float</code> This parameter should contain the payment amount of the particular transaction. Note: Type-cast the amount to float type</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>10</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>productinfo<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>varchar</code> This parameter should contain a brief product description. It should be a string describing the product (The description type is entirely your choice). </p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>T-shirt</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>firstname<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>varchar</code> This parameter must contain the first name of the customer.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Ankit</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>email<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>varchar</code> This parameter must contain the email of the customer)</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="mailto:test@gmail.com">test@gmail.com</a></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>phone<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>integer</code> Merchant needs to take the customer’s GPay registered phone number and pass in this field. This field will be used for further mapping the customer VPA and initiate a collect request.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>hash<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>varchar</code> Hash is a crucial parameter – used specifically to avoid any tampering during the transaction. There are two different methods to calculate hash. Please follow method 1 only. Method 2 is just there for the documentation and is not to be used This is the simplest way of calculating the hash value. Here, please make sure that the api_version parameter is NOT POSTED from your end. For hash calculation, you need to generate a string using certain parameters and apply the sha512 algorithm to this string.<br><strong>Note</strong>: You have to use pipe (|) character in between these parameters as mentioned below. The parameter order is mentioned below: sha512(merchant_id|txnid|<br/>amount|productinfo|firstname|email|<br/>udf1|udf2|udf3|udf4|u df5||||||CLIENT_SECRET) All these parameters (and their descriptions) have already been mentioned earlier in this table. Here, SALT (to be provided by PayU), key, txnid, amount productinfo, firstname, email are mandatory parameters and hence can’t b empty in hash calculation above. But, udf1-udf5 are optional and hence you nee to calculate the hash based upon the fact that whether you are posting a particular udf or not. For example, if you are NOT posting udf1. Then, in the has calculation, udf1 field will be left empty. The following examples will clarify various scenarios of hash calculation:  </p>
<ul>
<li><strong>Case 1</strong>: If all the udf parameters (udf1-udf5) are posted by the merchant. Then, hash=sha512(merchant_id|txnid<br/>|amount|productinfo|firstname|email|<br/>udf1|udf2|udf3| udf4|udf5||||||CLIENT_SECRET)</li>
<li><strong>Case 2</strong>: If only some of the udf parameters are posted and others are not. For example, if udf2 and udf4 are posted and udf1, udf3, udf5 are not. Then, hash=sha512(merchant_id|txnid|amount|productinfo|firstname|email||udf2||udf4|||||||CLIENT_SECRET) Case 3: If NONE of the udf parameters (udf1-udf5) are posted. Then, hash=sha512(merchant_id|txnid|amount|productinfo|firstname|email|||||||||||CLIENT_SECRET) Example: If merchant_id=6631711, txnid=12345, amount=10, productinfo=Shopping, firstname=Test, email=<a href="mailto:test@test.com">test@test.com</a>, udf2=abc, udf4=15, CLIENT_SECRET=3sf0jURk91319391949941414195821851313 and udf1, udf3, udf5 are not posted. Then, the hash would be calculated as Case 2 above: sha512(6631711|12345|10|Shopping|Test|<a href="mailto:test@test.com">test@test.com</a>||abc||15|||||||3sf0jURk91319391949941414195821851313) (This value comes out to be 7a83339ccf2dde9d31569b00eea70a60174b3af3ceaa773d17a84b90c9eedad5f744ba02f95a572d8fe8592346ebb537bede49ad1ec786469b4bd77531d19b87) IMPORTANT: For details related to hash at the time of postback from PayU to the merchant, please refer to the later section. This is also absolutely mandatory to avoid any tampering.</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>reseller_id<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>varchar This parameter is the unique Partner Identifier provided by PayU for your partner account. The Partner Identifier acts as the unique identifier to identify a particular Partner Account in our database.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> 83fe-eb64-021844d8-9397-26535b1bf0c2</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>udf5<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> This parameter has been made for you to keep any information corresponding to the transaction. Pass <strong>whatsapp</strong> in this field</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>whatsapp</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>surl<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The success URL must be posted using this parameter to redirect user after payment success.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>furl<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The failure URL must be posted using this parameter to redirect user after payment failure</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>curl<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The cancel URL to redirect user after payment is cancelled.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>address1<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> The first line of the billing address.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>address2<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> The second line of the billing address.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>city<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> The city where your customer resides as part of the billing address.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>state<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> The state where your customer resides as part of the billing address.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>country<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> The country where your customer resides.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>zipcode<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> Billing address zip code is mandatory for the cardless EMI option.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>partner_udf_3<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter has been made for partner to pass any information corresponding to the transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>partner_udf_4<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter has been made for partner to pass any information corresponding to the transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>shipping_firstname<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> The first name of shipping person.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>shipping_lastname<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> The last name of shipping person.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>shipping_address1<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> The first line of the shipping address.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>shipping_address2<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> The second line of the shipping address.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>shipping_city<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> The city where your customer resides as part of the shipping address.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>shipping_state<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> The state where your customer resides as part of the shipping address.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>shipping_country<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> The country where your customer resides as part of the shipping address.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>shipping_zipcode<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> Shipping address zip code.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>shipping_phone<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> The phone no your customer resides as part of the shipping address.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>drop_category<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code>  </p>
<p>This parameter can be used if you want to hide one or multiple payment options. For example, if you want to collect the payment using debit card and Net Banking, you can hide the credit card mode of payment.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>enforce_paymethod<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code><br>This parameter allows you to customize the payment options for each transaction. You can enforce specific payment modes, cards scheme, and specific banks under Net Banking using this method.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>user_token<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code>This parameter is used to uniquely identify a user for a merchant.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>offer_key<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> List of keys to filter the offer.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>offer_auto_apply</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code>This parameter contains a flag to specify whether the offer can be automatically applied.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>additional_charges<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code>The additional amount that needs to be charged. The additional amount will be added to the amount of the product by PayU</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### Sample Request

```curl
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/payments' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer 9d2ab8e1b99aa02f6b827af5b5000b277d9cb1cd037acb7cb31436a5b0da4f74' \
--data-raw '{
    "txnid": "nY3tkz3vciHFGTjblyFeycL2Zn1m",
    "amount": 1090.33,
    "productinfo": "whatsapp",
    "firstname": "Manikanta",
    "partner_uuid": "83fe-eb64-021844d8-9397-26535b1bf0c2",
    "merchant_id": 8238480,
    "phone": 7036722360,
    "hash": "5aadceaf6bec9158ccba8ec0dab32debcacbfd50e3587c077fa11107a5be0ac26712fae230522afb8908d068122c02f2d5c733a46c33ace0f66e5cc9d2ae4714",
    "lastname": "CHeruku",
    "email": "manik.cr24@gmail.com",
    "curl": "https://www.google.com",
    "furl": "https://www.google.com",
    "surl": "https://www.youtube.com",
}'
```

### Sample Response

```plaintext
{
    "redirectUri": "https://apitest.payu.in/public/#/35de666bac018494a06205addba2962cdb8d03ca9c2fa7954807098709f1b6dc"
}
```

### Failed Responses

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Code</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Reason</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Response</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>401</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>with invalid token</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{<br><br>“message”: “Invalid Auth token”<br><br>}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>403</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>with invalid hash</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{<br><br>“message”: “Invalid Hash”<br><br>}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>without reseller_id</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{<br><br>“errors”: [<br><br>“reseller_id is mandatory.”<br><br>]<br><br>}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>without amount</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{<br><br>“errors”: [<br><br>“amount is mandatory param”<br><br>]<br><br>}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>without merchant_id</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{<br><br>“errors”: [<br><br>“merchant_id is mandatory param”<br><br>]<br><br>}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>without hash</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{<br><br>“errors”: [<br><br>“hash is mandatory param”<br><br>]<br><br>}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>without product_info</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{<br><br>“errors”: [<br><br>“product_info is mandatory param”<br><br>]<br><br>}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>without surl</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{    &quot;message&quot;: &quot;surl is mandatory&quot;}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>without furl</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{    &quot;message&quot;: &quot;furl is mandatory&quot;}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>without curl</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{    &quot;message&quot;: &quot;curl is mandatory&quot;}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>incorrect reseller_id </p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{<br>    &quot;message&quot;: &quot;Partner with UUID 1212312213r is not allowed to do this action&quot;<br>}</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Step 2: Customer Submits Payment Details on PayU Page

The customer selects the appropriate payment option (Credit Card, Debit Card, Net Banking, etc.) on PayU Payment page.

The customer goes through the necessary authorization or authentication process at their bank. The bank then sends a response to PayU indicating whether the payment was successful or not

## Step 3: Validate the Response From PayU

PayU updates the transaction status based on the response from the bank. If the payment is successful, PayU will send you a success URL. Make sure to verify the hash value before accepting or declining the invoice order.

This section provides a list of parameters included in the response for PayU Hosted integration and an example response.

### Response Parameters

> 📘 Note:
>
> Verify the **amount** and **txnid** parameters at your end in response from PayU.

#### Sample Response

PayU responds to the status of the transaction:

* **Success response**: If the transaction is successful, PayU will redirect the customer’s browser to the success URL, which is a URL provided by you using the `surl` parameter.
* **Failure response**: If the transaction fails, PayU will redirect the customer’s browser to the failure URL, which is a URL provided by you using the `furl` parameter.

For more information on `surl` or `furl` parameter, refer to the [Collect Payment - Merchant Hosted Checkout](ref:_payment_merchant_hosted).

The response URL returned from PayU is similar to the following:

### **Sample Response URL**

```plaintext
mihpayid=403993715523615328&mode=CC&status=success&unmappedstatus=captured&key=JPM7Fg&txnid=50QJq6lBJBmx14&amount=10.00&cardCategory=domestic&discount=0.00&net_amount_debit=10&addedon=2021-07-28+15%3A11%3A37&productinfo=iPhone&firstname=PayU+User&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=test%40gmail.com&phone=9876543210&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=afeab9dcf4e43d47f8fbf5a6838d393c70694a58e30ada08e6cb86ac943236c05717c5f5e4872d671fe81d0d9b2d9facd44e9a061ba621aff6f20c4343ea5dfa&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=CC-PG&bank_ref_num=7f0d5ada-59bb-41d7-9e41-20a6af2406c9&bankcode=CC&error=E000&error_Message=No+Error&name_on_card=test&cardnum=411111XXXXXX1111&cardhash=This+field+is+no+longer+supported+in+postback+params.
```

The response mentioned earlier looks like the following when parsed:

### **Parsed Sample Response Body**

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
cardhash: This field is no longer supported in postback params.
```

## Step 4: Verify the payment

**Environment**

|           |                                                                                                    |
| --------- | -------------------------------------------------------------------------------------------------- |
| UAT Host  | \<[https://test-partnerapilayer.payu.in/apilayer>](https://test-partnerapilayer.payu.in/apilayer>) |
| PROD Host | \<[https://api.payu.in>](https://api.payu.in>)                                                     |

### Request headers

Content-Type:application/json

Authorization:Bearer 039e0d1d70f467f946e2d73bd43868df856cfaa352ea54591a76bfc4a08d3487

### Request parameters

| Parameter   | Description                                                                                                                                                                                                       | Example                              |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| txnid       | In this parameter, you can include the txnid (Your transaction ID/order ID).                                                                                                                                      | 100123                               |
| merchant_id | It is the merchant ID that PayU provided you.                                                                                                                                                                     | 8238480                              |
| hash        | This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash is mentioned below:                                                                             |                                      |
| reseller_id | varchar This parameter is the unique Partner Identifier provided by PayU for your partner account. The Partner Identifier acts as the unique identifier to identify a particular Partner Account in our database. | 83fe-eb64-021844d8-9397-26535b1bf0c3 |

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

### Response Values

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the status of the transaction. Possible values are success, failure, or pending.. The significance of the values for these values are:  </p>
<ul>
<li><strong>Success</strong>: If the value of <strong>status</strong> parameter is ’success’, the transaction is successful.</li>
<li><strong>Failed</strong>: If the value of <strong>status</strong> parameter is ‘failure’</li>
<li><strong>Pending</strong>: if the value of <strong>status</strong> parameter is ‘pending’ – use the verify_payment API to confirm the status of this transaction.</li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>unmappedstatus</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the status of a transaction as per the internal database of PayU. PayU’s system has several intermediate statuses which are used for tracking various activities internal to the system. Hence, this status contains intermediate statuses of a transaction also – and hence is known as <strong>unmappedstatus</strong>. For detailed information on the statuses, refer to <a href="https://docs.payu.in/reference/payment-state-explanations">Payment State Explanations</a>.</p>
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

## Step 5: PayU sends Server-to-Server call-back response

PayU can also send a server-to-server call-back response whenever the transaction status gets updated.

### Implementation

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

The response mentioned earlier looks like the following when parsed:

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
