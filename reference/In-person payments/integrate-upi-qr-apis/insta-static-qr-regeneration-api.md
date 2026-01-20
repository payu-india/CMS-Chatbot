---
title: Insta Static QR Regeneration API
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
The **Insta Static QR Re-Generation** API is used to regenerate a previously generated Static UPI or Bharat QR.

<Callout icon="📘" theme="info">
  **Note**: This API only allows you to regenerate, not edit the previously generated QR.
</Callout>

| Environments | URL                                                                                            |
| :----------- | :--------------------------------------------------------------------------------------------- |
| Production   | [https://info.payu.in/merchant/postservice.php](https://info.payu.in/merchant/postservice.php) |

## Request parameters

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>key <code>mandatory</code></td>
      <td>This parameter must contain the merchant key provided by PayU. For more information, refer to <a href="doc:generate-merchant-key-and-salt-on-payu-dashboard">Access Production Key and Salt</a>.</td>
      <td>Your Test Key</td>
    </tr>
    <tr>
      <td>command <code>mandatory</code></td>
      <td>This parameter must have the API command name.</td>
      <td>generate_insta_account</td>
    </tr>
    <tr>
      <td>hash <code>mandatory</code></td>
      <td>This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash as follows:<br><code>sha512(key|command|var1|salt)</code></td>
      <td>c24ee06c7cf40314ede424b1 fcc2b97a12f97a7d3 dd206876eef16660eb09 fd374fd82861f66d8152e</td>
    </tr>
    <tr>
      <td>var1 <code>mandatory</code></td>
      <td>This parameter must contain the fields in a JSON format. For more information, refer to <a href="https://docs.payu.in/reference/insta-static-qr-regeneration-api#description-of-var1-parameter-fields">Description of var1 parameter fields</a>.</td>
      <td>Refer to Sample var1 section.</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

### Description of var1 parameter fields

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Key</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>customerId <code>conditional</code></td>
      <td>Data type: <code>string</code><br>Merchant Transaction Identifier. Should be unique and alphanumeric (less than or equal to 20 characters & Only "@", ".", "," are allowed)</td>
      <td>1234abcd</td>
    </tr>
    <tr>
      <td>merchantVpa <code>conditional</code></td>
      <td>Data type: <code>string</code><br>Merchant's VPA in which payment will be collected. VPA to be embedded in QR. Should be unique & alphanumeric (less than or equal to 50 characters & Only "@", ".", "," are allowed)</td>
      <td>instadummy.001@hdfcban</td>
    </tr>
    <tr>
      <td>instaProduct <code>mandatory</code></td>
      <td>Data type: <code>string</code><br>The QR generation flag. Fixed value = qr</td>
      <td>qr</td>
    </tr>
    <tr>
      <td>getAccount <code>mandatory</code></td>
      <td>Data type: <code>string</code><br>Pass the value of this parameter as 1 to regenerate previously generated QR.</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

> 🚧 Callout
>
> * **var1** is a json. All the parameters in var1 are to be sent as a json. Remember that the whole json string should be used for hash generation.
> * To Re-Generate a static QR you may pass either the example **var1** parameters mentioned in this document or pass all the **var1** parameters that you have passed while generating the static QR for the first time. Remember that passing the parameter 'getAccount=1' indicates that the request is for re-generating a previously generated QR.

## Sample request

```
curl --location --request POST 'https://info.payu.in/merchant/postservice.php' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=YOUR_MERCHANT_KEY' \
--data-urlencode 'command=generate_insta_account' \
--data-urlencode 'hash=YOUR_CALCULATED_HASH' \
--data-urlencode 'var1={
  "merchantVpa": "qr.6879729.prod12@indus",
  "instaProduct": "qr",
  "getAccount": "1"
}'
```

<br />

### Sample var1

```json JSON
{
  "merchantVpa": "qr.6879729.prod12@indus",
  "instaProduct": "qr",
  "getAccount": "1"
}
```

## Sample response

```curl cURL
curl --location --request POST 'https://info.payu.in/merchant/postservice.php' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=JF***g' \
--data-urlencode 'command=generate_insta_account' \
--data-urlencode 'hash=b7815c44e1852d76322730a483c0b51d39b0657ed90e01da6108bf60249e6da9f8c5a4b0ffbb7f6c7b6d772ed1c8b2984f9be6ef037b142a391221186b5ce3c2' \
--data-urlencode 'var1={"name":"BFL Live test","merchantVpa":"bfltestqr.6879728.prod12@indus","qrType":"upi","city":"South West","pinCode":"122002","address":"sector 46","udf5":"BFL113","instaProduct":"qr","submerchantRegistration":"1","mebussname":"Suniltest1","outputType":"string","awlmcc":"7999","legalStrName":"Testaly","panNo":"BPEPK5431F","strCntMobile":"9833208174","getAccount":"1"}'
```

## Response parameters

The transaction_details parameter of the response is in JSON format and the parameters in this JSON are described in the following table:

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>qrString</td>
      <td>The value received in this parameter is based on the value passed in the outputType (var1) in the request. It will be in any of the following format containing information associated to the QR, the QR string can be converted into image and used for accepting transactions.<br>Plain text format if the value in the outputType request parameter is string<br>base64 format if the value in the outputType request parameter is base64</td>
    </tr>
    <tr>
      <td>qrId</td>
      <td>This parameter contains the QR ID.</td>
    </tr>
    <tr>
      <td>vpa</td>
      <td>This parameter contains the VPA.</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Sample response

```json JSON
{
  "qrString": "upi//pay?pa=testqr.6879.prod4@indus&pn=BFL%20Live%20test&mc=7999&tr=STQ9BJpCzJezI76879729&ver=01&mode=01&orgid=000000&qrMedium=04&cu=INR&pinCode=122002",
  "qrId": "STQ9BJpCzJezI76879729",
  "merchantVpa": "testqr.6879.prod4@indus"
}
```
