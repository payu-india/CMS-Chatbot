---
title: PayU Hosted Integration
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
The **pre\_authorize** parameter is used to pre-authorize payments using the PayU Hosted Checkout integration with the **\_payment** API.

> 📘 Note:
>
> You need to activate the Pre-Authorize Payments before you start using this integration. Contact your PayU Key Account Manager (KAM) to activate Pre-Authorize Payments.

## Step 1: Post the pre-auth transaction request

Post the additional parameters for using the Pre-Auth. For complete list of parameters, refer to [Pre-Authorize Payment](ref:pre_authorize_payment1) for the complete list parameters with **Try It** experience.

**Environment**

|                            |                                                                       |
| :------------------------- | :-------------------------------------------------------------------- |
| **Test Environment**       | [https://test.payu.in/\_payment>](https://test.payu.in/_payment>)     |
| **Production Environment** | [https://secure.payu.in/\_payment>](https://secure.payu.in/_payment>) |

The **pre\_authorize** parameter as specified is used to pre-authorize payments using the PayU Hosted Checkout integration with the **\_payment** API.



### Hashing

You must hash the request parameters using the following hash logic:

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
```

For more information, refer to [Generate Hash](doc:generate-hash-payu-hosted).

### Sample request

```curl
curl -X POST "https://test.payu.in/_payment
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
"key=JP***g&txnid=PQI6MqpYrjEefU&amount=10.00
&firstname=PayU User&email=test@gmail.com&phone=9876543210
&productinfo=iPhone&pre_authorize=1&pg=cc&bankcode=CC&surl=
https://apiplayground-response.herokuapp.com/
&furl=https://apiplayground-response.herokuapp.com/
&pre_authorize=1&hash=05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072"
```

## Step 2: Check the response from PayU

<ReverseHashing />

### Sample response

By default, the response in HTML format. The formatted sample response body is similar to the following, and you need to look for the following parameters:

* PG\_TYPE: CC PG
* bankcode: CC
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

|                        |                                                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| Test Environment       | [https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2) |
| Production Environment | [https://info.payu.in/merchant/postservice.php?form=2](https://info.payu.in/merchant/postservice.php?form=2) |

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

## Step 3: Check Action Status

* To check the status of the transaction, use the **verify\_payment** API.  For more information, refer to [Verify Payment API](ref:verify_payment_api)
* To check the status of the Auth Request and then Capture Request sent, use the **check\_action\_status** API. For more information,  refer to  [Check Refund Status API with Request ID](ref:check_action_status_api_with_request_id).

> 📘 Note:
>
> * The **unamappedstatus** to **auth** can be checked using thje [Verify Payment API](ref:verify_payment_api) and in callback response in the Transaction callback.
> * If you want to cancel or refund a pre-authorized payment, refer to [Cancel a Pre-Authorized Payment](doc:cancel-a-pre-authorized-payment).

### Sample response

#### Failure scenario

```
{ 

    "status": 1, 

    "msg": "1 out of 1 Transactions Fetched Successfully", 

    "transaction_details": { 

        "18315176038": { 

            "12806028149": { 

                "mihpayid": "18315176038", 

                "bank_ref_num": "6969235068376733806127", 

                "request_id": "12806028149", 

                "amt": "2.00", 

                "mode": "CC", 

                "action": "auth", 

                "token": "", 

                "status": "SUCCESS", // Auth is successful 

                "bank_arn": null, 

                "settlement_id": null, 

                "amount_settled": null, 

                "UTR_no": null, 

                "value_date": null, 

                "refund_mode": "-" 

            }, 

            "12806028151": { 

                "mihpayid": "18315176038", 

                "bank_ref_num": null, 

                "request_id": "12806028151", 

                "amt": "1.00", 

                "mode": "CC", 

                "action": "capture", 

                "token": "Cap_18315176038_01", 

                "status": "QUEUED", // Capture is in queue statue  

                "bank_arn": null, 

                "settlement_id": null, 

                "amount_settled": null, 

                "UTR_no": null, 

                "value_date": null, 

                "refund_mode": "-" 

            } 

        } 

    } 
```

#### Success scenario

```
{ 
    "status": 1, 
    "msg": "1 out of 1 Transactions Fetched Successfully", 
    "transaction_details": { 
        "18283829909": { 
            "12781896792": { 
                "mihpayid": "18283829909", 
                "bank_ref_num": "6966342376826003206121", 
                "request_id": "12781896792", 
                "amt": "1031.00", 
                "mode": "CC", 
                "action": "auth", 
                "token": "", 
                "status": "SUCCESS", 
                "bank_arn": null, 
                "settlement_id": null, 
                "amount_settled": null, 
                "UTR_no": null, 
                "value_date": null, 
                "refund_mode": "-" 
            }, 
            "12781896793": { 
                "mihpayid": "18283829909", 
                "bank_ref_num": "6969233152136917105030", 
                "request_id": "12781896793", 
                "amt": "426.00", 
                "mode": "CC", 
                "action": "capture", 
                "token": "PZT2310070446VG2VC01", 
                "status": "success", // Auth is successful 
                "bank_arn": null, 
                "settlement_id": "202310111115", 
                "amount_settled": "418.7100", 
                "UTR_no": null, 
                "value_date": null, 
                "refund_mode": "-" 
            }, 
            "12806008126": { 
                "mihpayid": "18283829909", 
                "bank_ref_num": null, 
                "request_id": "12806008126", 
                "amt": "605.00", 
                "mode": "CC", 
                "action": "cancel", 
                "token": "825816e28afb809be802c7b", 
                "status": "SUCCESS", // Capture is successful 
                "bank_arn": null, 
                "settlement_id": null, 
                "amount_settled": null, 
                "UTR_no": null, 
                "value_date": null, 
                "refund_mode": "-" 
            } 
        } 
    } 

} 
```