---
title: Process Transaction with a Saved Card
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
If you have not received a response from PayU with First-Time Payment Workflow, use the get_user_card API as described in [Get User Cards API](ref:get_user_cards_api) (previous section).

HTTP Method: **POST**

**Environment**

| Test Environment       | <https://test.payu.in/_payment> |
| :--------------------- | :------------------------------ |
| Production Environment | <https://info.payu.in/_payment> |

## Extra parameters to be posted with saved card using \_payment API

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "user\\_credentials  \n**mandatory**",
    "0-1": "`varchar`  It contains the merchant ID and a unique customer identifier. In this example, the user credentials that you submitted with the var1 parameter using the save\\_user\\_cards API.",
    "0-2": "a:b",
    "1-0": "store\\_card\\_token  \n**mandatory**",
    "1-1": "`varchar`  It is the card token for a card that is returned by PayU when you store a card. When you store a card using the save\\_user\\_cards API, the response from PayU contains the card token value in the cardToken parameter.",
    "1-2": "57cb996f2eaeee525765a",
    "2-0": "storecard\\_token\\_type   \n**optional for PayU token flow**",
    "2-1": "`integer` This parameter can be posted with the value as **0** as you are using PayU token hub.",
    "2-2": "0"
  },
  "cols": 3,
  "rows": 3,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


> 📘 Note
> 
> Only the fields needed for this operation are mentioned here. For the complete API details of the \_payment API, refer to [Collect Payment API - Merchant Hosted Checkout](ref:_payment_merchant_hosted).

## Sample request

```curl
curl -X \
 POST "https://test.payu.in/_payment-H "accept: application/json" -H \
 "Content-Type: application/x-www-form-urlencoded" -d"key=JP***g&txnid=EaE4ZO3vU4iPsp&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cc&bankcode=MAST&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=51234567890***46&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=undefined$&user_credentials=a:b&hash=fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304"
```
```python
$url = "https://test.payu.in/_payment";$req = req_init($url);req_setopt($req, CURLOPT_URL, $url);req_setopt($req, CURLOPT_POST, true); req_setopt($req, CURLOPT_RETURNTRANSFER, true);$headers = array( "Content-Type: application/x-www-form-urlencoded", ); req_setopt($curl, CURLOPT_HTTPHEADER, $headers);$data = "key=JP***g&txnid=EaE4ZO3vU4iPsp&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cc&bankcode=MAST&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=51***56789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=undefined&user_credentials=a:b&store_card=1&hash=fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304"req_setopt($curl, CURLOPT_POSTFIELDS, $data);$resp = req_exec($req);req_close($req);var_dump($resp);
```
```php
$url = "https://test.payu.in/_payment";$req = req_init($url);req_setopt($req, CURLOPT_URL, $url);req_setopt($req, CURLOPT_POST, true); req_setopt($req, CURLOPT_RETURNTRANSFER, true);$headers = array( "Content-Type: application/x-www-form-urlencoded", ); req_setopt($curl, CURLOPT_HTTPHEADER, $headers);$data = "key=JP***g&txnid=leiMrpxBWCQGMV&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cc&bankcode=cc&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=51***56789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=undefined&user_credentials=a:b&store_card=1&hash=2c70a41d4faf6adef7840b643fa5f244dc8bfba044d58f5c602d3dcc6aba3b7ce8a409bf01bb4cbf460ae1b4e791a5178f5d9050854e88d41bad6a100905882f"req_setopt($curl, CURLOPT_POSTFIELDS, $data);$resp = req_exec($req);req_close($req);var_dump($resp);
```
```java
Request request = Request.Post("https://test.payu.in/_payment -H");String body = “key=JP***g&txnid=EaE4ZO3vU4iPsp&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cc&bankcode=MAST&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&user_credentials=a:b&store_card_token=i***uy***oio&storecard_token_type=0&hash=fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304”request.bodyString(body,ContentType.APPLICATION_FORM_URLENCODED);request.setHeader(“Content-Type”, "application/x-www-form-urlencoded");HttpResponse httpResponse = request.execute().returnResponse();System.out.println(httpResponse.getStatusLine());if (httpResponse.getEntity() != null) {String html = EntityUtils.toString(httpResponse.getEntity());System.out.println(html);}
```

## Sample response

```
Array
(
    [mihpayid] => 403993715524069222
    [mode] => CC
    [status] => success
    [unmappedstatus] => captured
    [key] => JPM7Fg
    [txnid] => EaE4ZO3vU4iPsp
    [amount] => 10.00
    [cardCategory] => domestic
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2021-09-08 19:37:19
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
    [phone] => 98765***10
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
    [hash] => ed99957adb08fea56c907b88e8d158a79c3562c67f96c298461509826f77a7ae9e88b2a176b3234c25f50bcd451271728719656f3bb59c13a52bebabc468615a
    [field1] => 06***733***32718***015
    [field2] => 986987
    [field3] => 10.00
    [field4] => 40***371552***9222
    [field5] => 100
    [field6] => 02
    [field7] => AUTHPOSITIVE
    [field8] => 
    [field9] => Transaction is Successful
    [payment_source] => payu
    [PG_TYPE] => CC-PG
    [bank_ref_num] => 06***733***32718***015
    [bankcode] => CC
    [error] => E000
    [error_Message] => No Error
    [name_on_card] => undefined
    [cardnum] => XXXXXXXXXXXX2346
    [cardToken] => 745***2fd9b***8824***4e7ed***c1fe***7
)
```