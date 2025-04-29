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

> 📘 Note:
> 
> This API only allows you to regenerate, not edit the previously generated QR.

| Environments | URL                                             |
| :----------- | :---------------------------------------------- |
| Production   | <https://info.payu.in/merchant/postservice.php> |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Value",
    "0-0": "key  \n`mandatory`",
    "0-1": "This parameter must contain the merchant key provided by PayU.  \nReference: For more information on how to generate the Key and Salt, refer to any of the following:  \n**Production**: Generate Production Merchant Key and Sat.  \n**Test**: Generate Test Merchant Key and Salt.",
    "0-2": "Your Test Key",
    "1-0": "command  \n`mandatory`",
    "1-1": "This parameter must have the API command name.",
    "1-2": "generate_insta_account",
    "2-0": "hash  \nmandatory",
    "2-1": "This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash as follows:  \n  \n`sha512(key\\|command\\|var1\\|salt)`",
    "2-2": "c24ee06c7cf40314ede424 b1fcc2b97a12f97a7d3dd2 06876eef16660eb09fd374 fd82861f66d8152e",
    "3-0": "var1  \n`mandatory`",
    "3-1": "This parameter must contain the fields in a JSON format. For more information, refer to <<Description of var1 Parameter Fields.>>",
    "3-2": "Refer to <<Sample var1>> section."
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


### Description of var1 parameter fields

[block:parameters]
{
  "data": {
    "h-0": "Key",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "customerId  \nconditional",
    "0-1": "`string` Merchant Transaction Identifier. Should be unique snd alphanumeric (less than or equal to 20 characters & Only \"@\", \".\", \",\" are allowed)",
    "0-2": "1234abcd",
    "1-0": "merchantVpa customerId  \n`conditional`",
    "1-1": "`string` Merchant's VPA in which payment will be collected.VPA to be embedded in QR. Should be unique & alphanumeric (less than or equal to 50 characters & Only \"@\", \".\", \",\" are allowed)",
    "1-2": "instadummy.001@hdfcban",
    "2-0": "instaProduct customerId  \n`mandatory`",
    "2-1": "`string` The QR generation flag. Fixed value = qr",
    "2-2": "qr",
    "3-0": "getAccount    \n`mandatory`",
    "3-1": "`string` Pass the value of this parameter as 1 to regenerate previously generated QR.",
    "3-2": "1"
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


> 🚧 Callout
> 
> - **var1** is a json. All the parameters in var1 are to be sent as a json. Remember that the whole json string should be used for hash generation.
> - To Re-Generate a static QR you may pass either the example **var1** parameters mentioned in this document or pass all the **var1** parameters that you have passed while generating the static QR for the first time. Remember that passing the parameter 'getAccount=1' indicates that the request is for re-generating a previously generated QR.

### Sample var1

```Text JSON
{
  "merchantVpa": "qr.6879729.prod12@indus",
  "instaProduct": "qr",
  "getAccount": "1"
}
```

## Sample response

```Text cURL
curl --location --request POST 'https://info.payu.in/merchant/postservice.php' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=JF***g' \
--data-urlencode 'command=generate_insta_account' \
--data-urlencode 'hash=b7815c44e1852d76322730a483c0b51d39b0657ed90e01da6108bf60249e6da9f8c5a4b0ffbb7f6c7b6d772ed1c8b2984f9be6ef037b142a391221186b5ce3c2' \
--data-urlencode 'var1={"name":"BFL Live test","merchantVpa":"bfltestqr.6879728.prod12@indus","qrType":"upi","city":"South West","pinCode":"122002","address":"sector 46","udf5":"BFL113","instaProduct":"qr","submerchantRegistration":"1","mebussname":"Suniltest1","outputType":"string","awlmcc":"7999","legalStrName":"Testaly","panNo":"BPEPK5431F","strCntMobile":"9833208174","getAccount":"1"}'
```

## Response parameters

The transaction_details parameter of the response is in JSON format and the parameters in this JSON are described in the following table:

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "qrString",
    "0-1": "The value received in this parameter is based on the value passed in the outputType (var1) in the request. It will be in any of the following format containing information associated to the QR, the QR string can be converted into image and used for accepting transactions.  \nPlain text format if the value in the outputType request parameter is string  \nbase64 format if the value in the outputType request parameter is base64",
    "1-0": "qrId",
    "1-1": "This parameter contains the QR ID.",
    "2-0": "vpa",
    "2-1": "This parameter contains the VPA."
  },
  "cols": 2,
  "rows": 3,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Sample response

```Text JSON
{
  "qrString": "upi//pay?pa=testqr.6879.prod4@indus&pn=BFL%20Live%20test&mc=7999&tr=STQ9BJpCzJezI76879729&ver=01&mode=01&orgid=000000&qrMedium=04&cu=INR&pinCode=122002",
  "qrId": "STQ9BJpCzJezI76879729",
  "merchantVpa": "testqr.6879.prod4@indus"
}
```