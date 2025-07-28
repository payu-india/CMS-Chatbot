---
title: S2S - Pre-Authorize Payment
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **pre\_authorize** parameter is used to pre-authorize payments using the S2S integration with the **\_payment** API.

> 📘 Note:
>
> You need to activate the Pre-Authorize Payments before you start using this integration. Contact your PayU Key Account Manager (KAM) to activate Pre-Authorize Payments.

## Step 1: Post the Pre-Auth transaction request

Post the additional parameters for with the Pre-Authorization using the Merchant Hosted Checkout. For complete list of parameters, refer to [Pre-Authorize Payment](ref:pre_authorize_payment1) for the complete list parameters with **Try It** experience.

**Environment**

`<PaymentAPIEnvironment />`

The **pre\_authorize** parameter as specified is used to pre-authorize payments using the PayU Hosted Checkout integration with the **\_payment** API. For the complete list of parameters for **\_payment** API, refer to [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout).

| **Parameter**  | **Reference**                                                                   |
| -------------- | ------------------------------------------------------------------------------- |
| pre\_authorize | This parameter is set to 1 to pre-authorize payment using PayU Hosted Checkout. |

> 📘 Note:
>
> I

### Sample request

```curl
curl -X POST "https://test.payu.in/_payment
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
"key=JP***g&txnid=PQI6MqpYrjEefU&amount=10.00
&firstname=PayU User&email=test@gmail.com&phone=9876543210
&productinfo=iPhone&pre_authorize=1&surl=
https://apiplayground-response.herokuapp.com/
&furl=https://apiplayground-response.herokuapp.com/
&pre_authorize=1&hash=05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072"
```

## Step 2: Check the PayU response

The formatted sample response body is similar to the following, and you need to look for the following parameters:

* PG\_TYPE: CC PG
* bankcode: PG
* **unamappedstatus: auth**

```
mihpayid: 403993715523615328
mode: CC
status: success
unmappedstatus: auth
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
error_Message: No Error
name_on_card: test
cardnum: 411111XXXXXX1111
cardhash: This field is no longer supported in postback params.

```

## Step 3: Capture a Pre-authorized payment

To capture a pre-authorized payment, use the following command. After the API command is successful, the transaction would be captured and settled to you.

**Environment**

`<GENERALAPIsEnvironment />`

### Sample request

```curl
curl --location --request POST 'https://info.payu.in/merchant/postservice.php?form=2' \ 
--header 'Content-Type: application/x-www-form-urlencoded' \ 
--form 'key="JF***g"' \ 
--form 'command="capture_transaction"' \ 
--form 'hash="67411736ab98c59522492a12751a6015c41b87764019f9dc14052690c2c7af9095d31002fc109dcf3596c2f38792d56db6f6207b1989010f2adf51c144fa3019"' \ 
--form 'var1="15246574846"' \ 
--form 'var2="authorizeTransaction123"' \ 
--form 'var3="1"' 
```

### Sample response

```plaintext
{ 
    "status": 1, 
    "msg": "Capture Request Queued", 
    "request_id": "Request ID", 
    "bank_ref_num": "Bank Reference Number" 
} 
```