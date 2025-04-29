---
title: Insta Static QR Generation API
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
This API is used to generate Static UPI or Bharat QR. The QR generated through this API is interoperable, can be used by any UPI applications like Google Pay, PhonePe, etc.. These QR codes can be used for accepting multiple transactions where customer can select the desired amount by themselves before making the payment. Bharat QR can also be scanned using mobile banking and credit card applications like (iMobile, SBI cards, etc.) to make transactions using debit cards and credit cards.

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
    "2-1": "This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash as follows:  \nsha512(key|command|var1|salt)",
    "2-2": "c24ee06c7cf40314ede424 b1fcc2b97a12f97a7d3dd2 06876eef16660eb09fd374 fd82861f66d8152e",
    "3-0": "var1  \n`mandatory`",
    "3-1": "This parameter must contain the fields in a JSON format. For more information, refer to <<Description of var1 Parameter Fields>>.",
    "3-2": "Refer to Sample var1 section."
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


> 🚧 Callouts
> 
> - In case the optional details are not posted, PayU will use the details registered against the merchant during the on-boarding process. If the details are not present at merchant-level, PayU will use PayU Payments Pvt. Ltd., Gurgaon & 122001 respectively.
> - The parameters udf1, udf2, udf3, udf4 & udf5 which are sent at the time of QR generation are recorded against every payment made on that QR. These parameters can be used to internally reconcile the payments at individual customer level & is the best possible way to reconcile payments for every transaction.
> - Merchant VPA series should be configured against the merchant ID before you start generating QR on production environment (not required in case `subMerchantRegistration` is passed as 1). Contact your PayU account manager & integration POC before you go live on production.
> - For real-time registration of sub-merchant, parameters such as `mebussname`, `strCntMobile` , `panNo`, `legalStrName`, and `awlmcc` are mandatory parameters for this API.

### var1 JSON fields description

[block:parameters]
{
  "data": {
    "h-0": "Key",
    "h-1": "Data Type",
    "h-2": "Sample",
    "0-0": "customerId  \n`conditional`",
    "0-1": "`numeric` This parameter must contain the merchant transaction identifier. The value must be unique & numeric special (less than or equal to 20 characters & Only \".\" is allowed).",
    "0-2": "1234",
    "1-0": "merchantVpa  \n`conditional`",
    "1-1": "`string` This parameter must contain the merchant's VPA in which payment will be collected.VPA to be embedded in QR. This value must be unique & alphanumeric special (less than or equal to 50 characters & Only \"@\", \".\", \",\" are allowed). The variable part of the VPA series can only be numeric. For example, if the series configured is _.payu@hdfc then the VPA can only be 123445.payu@hdfc and not a13s.payu@hdfc (_ part of the series will always be numeric).",
    "1-2": "[1202020@hdfc.bank](mailto:1202020@hdfc.bank)",
    "2-0": "name  \n`optional`",
    "2-1": "string This parameter contains the customer name part of the customer details, to be embedded in QR (less than or equal to 20 characters). If this value is not sent, merchant’s name registered during the onboarding process will be used.",
    "2-2": "Test User",
    "3-0": "city  \n`optional`",
    "3-1": "`string` This parameter contains the customer city as part of the customer details, to be embedded in QR (less than or equal to 15 characters).If the value is not sent, merchant’s city registered during the onboarding process will be used.",
    "3-2": "Gurgaon",
    "4-0": "pinCode  \n`optional`",
    "4-1": "`string` This parameter contains the PIN code as part of the customer details, to be embedded in the QR(less than or equal to 10 characters). If not sent, merchant’s PIN code registered during the onboarding process will be used.",
    "4-2": "122001",
    "5-0": "instaProduct  \n`mandatory`",
    "5-1": "`string` This parameter contains the QR generation flag and must be qr.",
    "5-2": "qr",
    "6-0": "address  \n`optional`",
    "6-1": "`string` This parameter must contain the customer address (less than or equal to 100 characters).",
    "6-2": "Payu, Bestech Business Tower, Gurgaon",
    "7-0": "udf1 - udf5  \n`optional`",
    "7-1": "`string` This parameter must contain the udf1, udf2, udf3, udf4 and udf5 can be sent in request to include any transactional information.",
    "7-2": "-",
    "8-0": "outputType  \n`optional`",
    "8-1": "`string` This parameter must contain the flag for outputType and can be any of the following  \n  \n'' (blank)  \n'string'  \n'base64'  \n  \nBy default, base64 JSPN encoded qrSting in response is sent.",
    "8-2": "string",
    "9-0": "submerchantRegistration  \n`optional`",
    "9-1": "`string` This parameter can contain any of the following:  \n`1`: This is passed then the request is passed to the acquiring bank.  \n`0`: This is passed the request is processed internally at PayU end.",
    "9-2": "1 or 0",
    "10-0": "mebussname  \n`conditional`",
    "10-1": "`string` This parameter contains the mebussname. It will be visible to the customers upon scanning this QR.  \n  \n**For non-aggregator** merchants, the mebussname will be picked up from the details registered with PayU. Any detail passed by the merchant would be ignored.  \n  \n**For aggregator-merchants**, the mebussname passed in this parameter should largely match with the name on the PAN card of the details passed in the panNo parameter.  \n  \nThis parameter is mandatory for the aggregator-merchant.",
    "10-2": "PayU",
    "11-0": "strCntMobile  \n`conditional`",
    "11-1": "`string` This parameter must contain the phone number associated for the entity for whom VPA is being created.  \n  \n**For non-aggregator merchants**, it will be picked up from the details registered with PayU. Any detail passed by the merchant would be ignored.  \n  \n**For aggregator-merchants**, the strCntMobile is mandatory.",
    "11-2": "9833270176",
    "12-0": "panNo  \n`conditional`",
    "12-1": "`string` This parameter must contain the PAN number associated for the entity for whom VPA is being created.  \n  \n`For non-aggregator merchants`, the panNo will be picked up from the details registered with PayU. Any detail passed by the merchant would be ignored.  \n  \n`For aggregator-merchants`, the panNo of the actual beneficiary needs to be passed. This key is mandatory for the aggregator-merchants.",
    "12-2": "BPEPK5437G",
    "13-0": "legalStrName  \n`conditional`",
    "13-1": "`string` This parameter must contain the legal name associated for the entity for whom VPA is being created.  \n  \n**For non-aggregator merchants**, it will be picked up from the details registered with PayU. Any detail passed by the merchant would be ignored.  \n  \n**For aggregator-merchants**, the legalStrName should largely match with the name on the PAN card of the details passed in the panNo key.  \n  \nThis parameter is mandatory for the aggregator-merchants.",
    "13-2": "PayU payments pvt ltd",
    "14-0": "awlmcc  \n`conditional`",
    "14-1": "`string` This parameter must contain the merchant category code as per NPCI guidelines and is typically a numeric value of length = 4.  \n  \n**For non-aggregator merchants**, the merchant category code will be picked up from the details registered with PayU. Any detail passed by the merchant would be ignored.  \n  \n**For aggregator-merchants**, the merchant category code of the actual beneficiary needs to be passed.  \n  \nThis parameter is mandatory for the aggregator-merchants",
    "14-2": "7999"
  },
  "cols": 3,
  "rows": 15,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Sample vat1

```Text JSON
{
  "name": "Test Live test",
  "merchantVpa": "qr.6879729.prod12@indus",
  "qrType": "upi",
  "city": "South West",
  "pinCode": "122002",
  "address": "sector 46",
  "udf5": "BFL113",
  "instaProduct": "qr",
  "submerchantRegistration": "1",
  "mebussname": "Sltest1",
  "outputType": "string",
  "awlmcc": "7999",
  "legalStrName": "Testaly",
  "panNo": "BPEPK5437G",
  "strCntMobile": "9833270176"
}
```

## Sample request

```Text cURL
curl --location --request POST 'https://info.payu.in/merchant/postservice.php' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=J***'g \
--data-urlencode 'command=generate_insta_account' \
--data-urlencode 'hash=b7815c44e1852d76322730a483c0b51d39b0657ed90e01da6108bf60249e6da9f8c5a4b0ffbb7f6c7b6d772ed1c8b2984f9be6ef037b142a391221186b5ce3c2' \
--data-urlencode 'var1={"name":"BFL Live test","merchantVpa":"bfltestqr.6879728.prod12@indus","qrType":"upi","city":"South West","pinCode":"122002","address":"sector 46","udf5":"BFL113","instaProduct":"qr","submerchantRegistration":"1","mebussname":"Suniltest1","outputType":"string","awlmcc":"7999","legalStrName":"Testaly","panNo":"BPEPK5431F","strCntMobile":"9833208174"}'
```
```Text Python
import http.client

conn = http.client.HTTPSConnection("info.payu.in")
payload = 'key=J***'g&command=generate_insta_account&hash=b7815c44e1852d76322730a483c0b51d39b0657ed90e01da6108bf60249e6da9f8c5a4b0ffbb7f6c7b6d772ed1c8b2984f9be6ef037b142a391221186b5ce3c2&var1=%7B%22name%22%3A%22BFL%20Live%20test%22%2C%22merchantVpa%22%3A%22bfltestqr.6879728.prod12%40indus%22%2C%22qrType%22%3A%22upi%22%2C%22city%22%3A%22South%20West%22%2C%22pinCode%22%3A%22122002%22%2C%22address%22%3A%22sector%2046%22%2C%22udf5%22%3A%22BFL113%22%2C%22instaProduct%22%3A%22qr%22%2C%22submerchantRegistration%22%3A%221%22%2C%22mebussname%22%3A%22Suniltest1%22%2C%22outputType%22%3A%22string%22%2C%22awlmcc%22%3A%227999%22%2C%22legalStrName%22%3A%22Testaly%22%2C%22panNo%22%3A%22BPEPK5431F%22%2C%22strCntMobile%22%3A%229833208174%22%7D'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}
conn.request("POST", "/merchant/postservice.php", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```
```Text PHP
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://info.payu.in/merchant/postservice.php',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS => 'key=vDy3i7&command=generate_insta_account&hash=b7815c44e1852d76322730a483c0b51d39b0657ed90e01da6108bf60249e6da9f8c5a4b0ffbb7f6c7b6d772ed1c8b2984f9be6ef037b142a391221186b5ce3c2&var1=%7B%22name%22%3A%22BFL%20Live%20test%22%2C%22merchantVpa%22%3A%22bfltestqr.6879728.prod12%40indus%22%2C%22qrType%22%3A%22upi%22%2C%22city%22%3A%22South%20West%22%2C%22pinCode%22%3A%22122002%22%2C%22address%22%3A%22sector%2046%22%2C%22udf5%22%3A%22BFL113%22%2C%22instaProduct%22%3A%22qr%22%2C%22submerchantRegistration%22%3A%221%22%2C%22mebussname%22%3A%22Suniltest1%22%2C%22outputType%22%3A%22string%22%2C%22awlmcc%22%3A%227999%22%2C%22legalStrName%22%3A%22Testaly%22%2C%22panNo%22%3A%22BPEPK5431F%22%2C%22strCntMobile%22%3A%229833208174%22%7D',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/x-www-form-urlencoded'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```
```Text Java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/x-www-form-urlencoded");
RequestBody body = RequestBody.create(mediaType, "key=J***'g&command=generate_insta_account&hash=b7815c44e1852d76322730a483c0b51d39b0657ed90e01da6108bf60249e6da9f8c5a4b0ffbb7f6c7b6d772ed1c8b2984f9be6ef037b142a391221186b5ce3c2&var1={\"name\":\"BFL Live test\",\"merchantVpa\":\"bfltestqr.6879728.prod12@indus\",\"qrType\":\"upi\",\"city\":\"South West\",\"pinCode\":\"122002\",\"address\":\"sector 46\",\"udf5\":\"BFL113\",\"instaProduct\":\"qr\",\"submerchantRegistration\":\"1\",\"mebussname\":\"Suniltest1\",\"outputType\":\"string\",\"awlmcc\":\"7999\",\"legalStrName\":\"Testaly\",\"panNo\":\"BPEPK5431F\",\"strCntMobile\":\"9833208174\"}");
Request request = new Request.Builder()
  .url("https://info.payu.in/merchant/postservice.php")
  .method("POST", body)
  .addHeader("Content-Type", "application/x-www-form-urlencoded")
  .build();
Response response = client.newCall(request).execute();
```

## Response parameters

The transaction_details parameter of the response is in JSON format and the parameters in this JSON are described in the following table:

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "qrString",
    "0-1": "The value received in this parameter is based on the value passed in the outputType (var1) in the request. It will be in any of the following format containing information associated to the QR, the QR string can be converted into image and used for accepting transactions.  \n  \nPlain text format if the value in the outputType request parameter is string  \n  \nbase64 format if the value in the outputType request parameter is base64",
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

### Success scenario

- UPI QR String response

```Text JSON
{
  "qrString": "upi//pay?pa=testqr.6879.prod4@indus&pn=BFL%20Live%20test&mc=7999&tr=STQ9BJpCzJezI76879729&ver=01&mode=01&orgid=000000&qrMedium=04&cu=INR&pinCode=122002",
  "qrId": "STQ9BJpCzJezI76879729",
  "merchantVpa": "testqr.6879.prod4@indus"
}
```

- UPI QR base64 response

```Text JSON
{
  "qrString": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAR0AAAEdAQMAAAALpCE4AAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAADaklEQVRoge1ZQa7iUAwLYtFlj/BuAherRKVeDG7SI7DsApGxndJ2/lzA80UXUPrMwkqcOGnE9/pev/7qM/PNm0uf83LNMfLdjzyYcJKjLwhflxiiezzx65SvFqfnjfBprlNX0JTLhfckFjxaIs7zcsLdytMYFEMDu3MmPzqGAxTP/wPoXEnF4zkT50GK3iDlU0R3hxC6tyICinh2/pl0ZiAquEcWXf75+CFzM9CKnCFeVh0GIyFjkD2cO4J6JlCKzthQcFaycUX9UbxcQXHLvOOLQmg4GmJj1yAJX1AxOc8oOK/oyLO7B4o9Vb2cPklnCMIDsMMDEGuo86yeqD/4GKHqLSx+ICgYTG6sOkF2YwB+S7ZX1P5d5oYgsKOXOT3LHLSssEDBeBa+IDgY6JZuAOzePFeDepSWR1sQnqJckiLsWLmBO/4I8ULLj03mhqCQ/yKTV4NkZYUhaAXo2KXsQDJhN5qwaB2QUR4eLjiWjy9wBYFOKpVYhNibbonSU53LFiQF03+xZn7IBsRLdsce7Aeqmql+pbAsbFqLTPH1R2F1AiEEVDDj8GKABloC3CXT6+EMkoPBXAQmjRNSeV8IGvebjzQE0TjKubNmpiQBdiHvexiT/EDUAG2vSs9KLCSEw0TtCcqFPVbtVVOdvK82A3vsPEF1ccbgN2om57u1X4UvaAixy/IyvdRAE5ZaZBiD2FSDZhcDHXXLsq9GOx2cmCGIdDhtCK4hDz+HxlRqu/e1BK1d9MqmGpuhYVJ1e830A4EJ1xd0A5jvCE/VTEliTzo/EPcuV+23apuRTCp6GWbWvu4yBL041ck9RtPPXImxJm3znR+Ixb42o7WdA4iNlndt32E4guDEVDMfmk5pwphZGqu7fQj0A33ioFUAlxZtUXrJmO1jtx9om6PhfTlCI7P0HoA189jKHEHqp6FZjksBTRvyvqqjtiDmE23vvZ/WDUxWROgLjkIwA6lm1ozBFR2rDiulQMeJ2g5UyCm1bSnve6+Zb/x7a+QGWt+3ZGyvWmRo6qXL1Rk0UgMapmkh6clOTy1fjuwcQXqLq73utGXWpDVv7r7AFcT91vtDscunVkccQyK8QSXekeuuWhiJ7GGH4QhSPmXqLW5oKaDlLhlvg6klSAouL1Nx4NQ016u5zTwYgr7X9/rV1x9Shwri/uMTPgAAAABJRU5ErkJggg==",
  "qrId": "STQ9vDy3i7dEW6136226",
  "merchantVpa": "instadummy.001@hdfcbank"
}
```

- Bharat QR String Response

```Text JSON
{
  "qrString": "000201010211021644038470007469080415522024070007469061661000307000746960825HDFC00006225020001855322626470010A0000005240129yellowqr.payutest.94@hdfcbank27370010A0000005240119STQ9y45z1cv3z5450925204569153033565802IN5910vendorName6010vendorCity610650017262350519STQ9y45z1cv3z545092070870007469630417EF",
  "qrId": "STQ9y45z1cv3z545093",
  "merchantVpa": "yellowqr.payutest.94@hdfcbank"
}
```

- Bharat QR base64 response

```Text JSON
{
  "qrString": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAR0AAAEdAQMAAAALpCE4AAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAADaklEQVRoge1ZQa7iUAwLYtFlj/BuAherRKVeDG7SI7DsApGxndJ2/lzA80UXUPrMwkqcOGnE9/pev/7qM/PNm0uf83LNMfLdjzyYcJKjLwhflxiiezzx65SvFqfnjfBprlNX0JTLhfckFjxaIs7zcsLdytMYFEMDu3MmPzqGAxTP/wPoXEnF4zkT50GK3iDlU0R3hxC6tyICinh2/pl0ZiAquEcWXf75+CFzM9CKnCFeVh0GIyFjkD2cO4J6JlCKzthQcFaycUX9UbxcQXHLvOOLQmg4GmJj1yAJX1AxOc8oOK/oyLO7B4o9Vb2cPklnCMIDsMMDEGuo86yeqD/4GKHqLSx+ICgYTG6sOkF2YwB+S7ZX1P5d5oYgsKOXOT3LHLSssEDBeBa+IDgY6JZuAOzePFeDepSWR1sQnqJckiLsWLmBO/4I8ULLj03mhqCQ/yKTV4NkZYUhaAXo2KXsQDJhN5qwaB2QUR4eLjiWjy9wBYFOKpVYhNibbonSU53LFiQF03+xZn7IBsRLdsce7Aeqmql+pbAsbFqLTPH1R2F1AiEEVDDj8GKABloC3CXT6+EMkoPBXAQmjRNSeV8IGvebjzQE0TjKubNmpiQBdiHvexiT/EDUAG2vSs9KLCSEw0TtCcqFPVbtVVOdvK82A3vsPEF1ccbgN2om57u1X4UvaAixy/IyvdRAE5ZaZBiD2FSDZhcDHXXLsq9GOx2cmCGIdDhtCK4hDz+HxlRqu/e1BK1d9MqmGpuhYVJ1e830A4EJ1xd0A5jvCE/VTEliTzo/EPcuV+23apuRTCp6GWbWvu4yBL041ck9RtPPXImxJm3znR+Ixb42o7WdA4iNlndt32E4guDEVDMfmk5pwphZGqu7fQj0A33ioFUAlxZtUXrJmO1jtx9om6PhfTlCI7P0HoA189jKHEHqp6FZjksBTRvyvqqjtiDmE23vvZ/WDUxWROgLjkIwA6lm1ozBFR2rDiulQMeJ2g5UyCm1bSnve6+Zb/x7a+QGWt+3ZGyvWmRo6qXL1Rk0UgMapmkh6clOTy1fjuwcQXqLq73utGXWpDVv7r7AFcT91vtDscunVkccQyK8QSXekeuuWhiJ7GGH4QhSPmXqLW5oKaDlLhlvg6klSAouL1Nx4NQ016u5zTwYgr7X9/rV1x9Shwri/uMTPgAAAABJRU5ErkJggg==",
  "qrId": "STQ9vDy3i7dEW6136226",
  "merchantVpa": "instadummy.001@hdfcbank"
}
```

### Failure scenario

- VPA ID already exists

```
{
  "status": "failed",
  "message": "customerId or VPA should be unique",
  "errorCode": "E2013"
}
```

> 🚧 Callout
> 
> - The response sent for QR generation request is json encoded and will be a base64 encoded string of the actual QR image, in case outputType is not shared
> - To obtain the actual QR image, first decode the json encoded response and then convert the base64 encoded string to actual QR image.
> - For every QR generation request, in the response we will share back the unique identifier, qrId, embedded in the QR & merchantVpa, embedded in the QR.
> - Map the QR image to this qrId and merchantVpa and also with respective customer/entity who will use this QR for making payments to you. This qrId or merchantVpa will be available at the time of transaction callback which you can use to identify the customer who made the payment.
> - In some scenarios, qrId will not be available in the transaction callback details. In such scenarios, use the merchantVpa field4 in the transaction callback details to identify the customer who made the payment.