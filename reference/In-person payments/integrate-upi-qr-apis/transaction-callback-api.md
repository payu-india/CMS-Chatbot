---
title: Transaction Callback API
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
The **Transaction Callback** API is a sample of the response that is posted to ws callback url/webhook after the transaction has been processed.

- All callbacks POST data on merchant’s callback URL.
- Validation of final response happens on the basis of hash value being returned in the hash value of the response.

## Reverse Hash Calculation

This is strictly recommended to avoid any tamper cases or MITM attacks. Hash string can be generated using the below logic with SHA512 algorithm. All fields are separated using pipe (|) operator.

`<salt|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|<valueOf(productinfo)|<valueOf(amount)|<valueOf(txnid)|<valueOf(key)`

## Callback structure

| Variable Name  | Description                                                                                                                                                                                                                                                                                                                                                                                                           |
| :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mihpayid       | It is a unique reference number created for each QR transaction at PayU’s end.                                                                                                                                                                                                                                                                                                                                        |
| mode           | This parameter describes the payment category by which the transaction was completed/attempted by the customer. The value will be 'DBQR'.                                                                                                                                                                                                                                                                             |
| status         | This parameter gives the status of the transaction. Hence, the value of this parameter depends on whether the transaction was successful or not. You must map the order status using this parameter only. The values are as below: If the transaction is successful, the value of ‘status’ parameter would be ‘success’. The value of ‘status’ as ‘failed’ or ‘pending’ must be treated as a failed transaction only. |
| key            | This parameter would contain the merchant key for the merchant’s account at PayU. It would be the same as the key used while the QR generation request is being posted from merchant’s end to PayU.                                                                                                                                                                                                                   |
| txnid          | This parameter would contain the unique id for every successful & failed transaction                                                                                                                                                                                                                                                                                                                                  |
| card\_no       | This parameter would contain the masked card number using which customer has made the transaction on QR for CARD transactions. Please ignore this parameter for UPI transactions on QR                                                                                                                                                                                                                                |
| amount         | This parameter would contain the transaction amount which the customer has paid                                                                                                                                                                                                                                                                                                                                       |
| productinfo    | This parameter would contain the value of productinfo, which will be 'Offline Dynamic QR'                                                                                                                                                                                                                                                                                                                             |
| address2       | This parameter would contain the same value of address which was sent in the QR generation request from merchant’s end to PayU                                                                                                                                                                                                                                                                                        |
| city           | This parameter would contain the same value of city which was sent sent in the QR generation request from merchant’s end to PayU                                                                                                                                                                                                                                                                                      |
| zipcode        | This parameter would contain the same value of pinCode which was sent in the QR generation request from merchant’s end to PayU                                                                                                                                                                                                                                                                                        |
| udf1           | This parameter would contain the same value of udf1 which was sent or set in the QR generation request from merchant’s end to PayU                                                                                                                                                                                                                                                                                    |
| udf2           | This parameter would contain the same value of udf2 which was sent or set in the QR generation request from merchant’s end to PayU                                                                                                                                                                                                                                                                                    |
| udf3           | This parameter would contain the same value of udf3 which was sent or set in the QR generation request from merchant’s end to PayU                                                                                                                                                                                                                                                                                    |
| udf4           | This parameter would contain the same value of udf4 which was sent or set in the QR generation request from merchant’s end to PayU                                                                                                                                                                                                                                                                                    |
| udf5           | This parameter would contain the same value of udf5 which was sent or set in the QR generation request from merchant’s end to PayU                                                                                                                                                                                                                                                                                    |
| field0         | QR ID will be replicated in this parameter, for example, 'DYQ10588979405'                                                                                                                                                                                                                                                                                                                                             |
| field1         | In case of BQR if it is a card transaction than this parameter will have the merchant 'Card no' and if it is s UPI transactions than it will have 'Customer name'                                                                                                                                                                                                                                                     |
| field3         | In case of UPI transaction this parameter will have 'Customer VPA'                                                                                                                                                                                                                                                                                                                                                    |
| field5         | In case of UPI transaction this parameter will have 'Merchant VPA'                                                                                                                                                                                                                                                                                                                                                    |
| field9         | This parameter would contain the status of the transaction                                                                                                                                                                                                                                                                                                                                                            |
| hash           | This parameter is absolutely crucial and is similar to the hash parameter used in the QR generation request send by the merchant to PayU. PayU calculates the hash using a string of other parameters and returns to the merchant. The merchant must verify the hash and then only mark a transaction as success/failure. This is to make sure that the transaction hasn’t been tampered with.                        |
| error          | For the failed transactions, this parameter provides the reason of failure. Please note that the reason of failure depends upon the error codes provided by different banks and hence the detailing of error reason may differ from one transaction to another. The merchant can use this parameter to retrieve the reason of failure for a particular transaction.                                                   |
| bankcode       | This parameter would contain the code indicating the payment option used for the transaction. For example, in Debit Card mode, there are different options like Visa Debit Card, Mastercard, Rupay etc. For each option, a unique bankcode exists. It would be returned in this bankcode parameter. For example, Visa Debit Card – VCCSBR, Master Credit Card – MCCSBQR.                                              |
| PG\_TYPE       | This parameter gives information on the payment gateway used for the transaction. For example, if SBI PG was used, it would contain the value SBIPG. If SBI Netbanking was used for the transaction, the value of PG\_TYPE would be SBINB.Similarly, it would have a unique value for all different type of payment gateways                                                                                          |
| bank\_ref\_num | For each successful & failed transaction, this parameter would contain the bank reference number generated by the bank                                                                                                                                                                                                                                                                                                |
| unmappedstatus | This parameter contains the status of a transaction as per the internal database of PayU. PayU’s system has several intermediate statuses which are used for tracking various activities internal to the system. Hence, this status contains intermediate states of a transaction also and hence is known as unmappedstatus. For example: dropped or autorefund etc. etc.                                             |

## Sample request

```Text cURL
curl --location -g --request POST '{{ws_online_response}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'unmappedstatus=success' \
--data-urlencode 'phone=9933208175' \
--data-urlencode 'txnid=DBQRTEST1' \
--data-urlencode 'hash=84e335094bbcb2ddaa0f9a488eb338e143b273765d89c9dfa502402562d
0b6f3c7935e28194ca92f7380be7c84c3695415b106dcf52cb016a15fcf6adc98d7
24' \
--data-urlencode 'status=success' \
--data-urlencode 'first name=Sunil' \
--data-urlencode 'productinfo=Offline Dynamic QR' \
--data-urlencode 'mode=DBQR' \
--data-urlencode 'amount=800.00' \
--data-urlencode 'field0=DBQRTest004' \
--data-urlencode 'field1=6807112311042810' \
--data-urlencode 'field3=2017419933606' \
--data-urlencode 'mihpayid=10564834663' \
--data-urlencode 'field1=42812' \
--data-urlencode 'key=smsplus' \
--data-urlencode 'status=success' \
--data-urlencode 'address1=402, bewest high' \
--data-urlencode 'city=Mumbai' \
--data-urlencode 'zipcode=400092' \
--data-urlencode 'email=payu@payu.in' \
--data-urlencode 'udf1=Barclays' \
--data-urlencode 'bank_ref_no=017415495720' \
--data-urlencode 'PG_TYPE=SBINB' \
--data-urlencode 'card_no=428090XXXXXX0203'
```
```Text JAVA
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/x-www-form-urlencoded");
RequestBody body = RequestBody.create(mediaType, "unmappedstatus=success&phone=9933208175&txnid=DBQRTEST1&hash=84e335094bbcb2ddaa0f9a488eb338e143b273765d89c9dfa502402562d
0b6f3c7935e28194ca92f7380be7c84c3695415b106dcf52cb016a15fcf6adc98d7
24&status=success&first name=Sunil&productinfo=Offline Dynamic QR&mode=DBQR&amount=800.00&field0=DBQRTest004&field1=6807112311042810&field3=2017419933606&mihpayid=10564834663&field1=42812&key=smsplus&status=success&address1=402, bewest high&city=Mumbai&zipcode=400092&email=payu@payu.in&udf1=Barclays&bank_ref_no=017415495720&PG_TYPE=SBINB&card_no=428090XXXXXX0203");
Request request = new Request.Builder()
  .url("{{ws_online_response}}")
  .method("POST", body)
  .addHeader("Content-Type", "application/x-www-form-urlencoded")
  .build();
Response response = client.newCall(request).execute();
```
```Text php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{ws_online_response}}');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/x-www-form-urlencoded'
));
$request->addPostParameter(array(
  'unmappedstatus' => 'success',
  'phone' => '9933208175',
  'txnid' => 'DBQRTEST1',
  'hash' => '84e335094bbcb2ddaa0f9a488eb338e143b273765d89c9dfa502402562d\n0b6f3c7935e28194ca92f7380be7c84c3695415b106dcf52cb016a15fcf6adc98d7\n24',
  'status' => 'success',
  'first name' => 'Sunil',
  'productinfo' => 'Offline Dynamic QR',
  'mode' => 'DBQR',
  'amount' => '800.00',
  'field0' => 'DBQRTest004',
  'field1' => '6807112311042810',
  'field3' => '2017419933606',
  'mihpayid' => '10564834663',
  'field1' => '42812',
  'key' => 'smsplus',
  'status' => 'success',
  'address1' => '402, bewest high',
  'city' => 'Mumbai',
  'zipcode' => '400092',
  'email' => 'payu@payu.in',
  'udf1' => 'Barclays',
  'bank_ref_no' => '017415495720',
  'PG_TYPE' => 'SBINB',
  'card_no' => '428090XXXXXX0203'
));
try {
  $response = $request->send();
  if ($response->getStatus() == 200) {
    echo $response->getBody();
  }
  else {
    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .
    $response->getReasonPhrase();
  }
}
catch(HTTP_Request2_Exception $e) {
  echo 'Error: ' . $e->getMessage();
}
```
```Text Python
import http.client

conn = http.client.HTTPSConnection("{{ws_online_response}}")
payload = 'unmappedstatus=success&phone=9933208175&txnid=DBQRTEST1&hash=84e335094bbcb2ddaa0f9a488eb338e143b273765d89c9dfa502402562d%0A0b6f3c7935e28194ca92f7380be7c84c3695415b106dcf52cb016a15fcf6adc98d7%0A24&status=success&first%20name=Sunil&productinfo=Offline%20Dynamic%20QR&mode=DBQR&amount=800.00&field0=DBQRTest004&field1=6807112311042810&field3=2017419933606&mihpayid=10564834663&field1=42812&key=smsplus&status=success&address1=402%2C%20bewest%20high&city=Mumbai&zipcode=400092&email=payu%40payu.in&udf1=Barclays&bank_ref_no=017415495720&PG_TYPE=SBINB&card_no=428090XXXXXX0203'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}
conn.request("POST", "/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

## Sample callback response

This response is sent in a key or value pair separated by ‘&’ character. In case any parameter is not used, we would send it back to the merchant with an empty string. The sample response is similar to the following:

```
unmappedstatus=success&phone=9833207342&txnid=STQ1R1008701!3212446&hash=84e335094bbcb2ddaa0f9a488eb338e143b273765d89c9dfa502402562d0b6f3c7935e28194ca92f7380be7c84c3695415b106dcf52cb016a15fcf6adc98d724&status=success&card_no=519619XXXXXX5049&productinfo=StaticQR&mode=SBQR&amount=800.00&field4=smsplus.payu@indus&field3=9833208175@ybl&field9=SUCCESS&field0=test12423&bank_ref_no=121345432769&mihpayid=175477248&card_hash=9e88cb0573d4a826b61d808c0a870ed4a990682459b0ec9 e95ea421e8e47be8c&field1=42812key=smsplus
```

<br />
