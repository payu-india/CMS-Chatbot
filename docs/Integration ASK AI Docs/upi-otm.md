---
title: UPI OTM
excerpt: >-
  Integrate UPI One-Time Mandate to block funds, capture the final amount,
  verify status, and cancel blocked registrations.
deprecated: false
hidden: true
metadata:
  robots: index
---
**<br />UPI OTM&#x20;**<br />The feature is intended to the use case of Block and Capture, where merchant generally blocks the amount initially and basis the service provided, debits the amount from the customer’s account.

Similar to Cards, UPI OTM also requires merchant to perform “Block/Auth payment” also called as Mandate Registrations followed by “Recurring/Capture payment”.

Registration transaction is completed with 2nd factor authentication where customer input his MPIN and authorize mandate details / billing details. Once registration transaction is successful, amount <br />gets blocked in the customer’s account then merchant can call Capture API for charging customer <br />without customer’s intervention.

**Registration Transaction (Mandate Registration) –**<br />•UPI instrument provides total flexibility on designing registration flow for merchants.

•Merchant presents option to customer to setup block in their account <br />•Billing details like amount getting blocked, start date and end date of the block needs to  be <br />presented to customer on merchant’s website <br />•Customer is asked to enter their VPA (for collect) and select Payer App (for Intent) and  same <br />details are passed to PayU during registration transaction request over API interface <br />•On receiving request over PSP app, customer needs to approve registration request by entering M-PIN <br />•After successful mandate registration, amount is blocked in the customer’s account.

Registration transaction gets completed and response of registration transaction along with unique registration Id is returned to merchant via webhook <br />**Capture Transaction –**

<br />

<br />

•Once registration transaction is successful, merchant can invoke debit/capture API of  PayU <br />by passing unique PayU id received in the response of registration transaction.

•Merchant will be able to debit customer for less than or equal to blocked amount without requiring any inputs or interventions from customers <br />•Since payment processing of UPI recurring is an asynchronous process with banks, real  time <br />response for capture transaction API is always returned as “Pending” if valid request is passed by merchant.• This state then gets converted into either “Success” or “Failure” once bank confirms status <br />of the transaction to PayU over call back interface.

•So, merchant can either implement Inquiry API or use PayU’s Webhook support to get  real <br />time status of the recurring transaction once bank provides real time confirmation.

**Note:-&#x20;**<br />•**Seamless and Non-Seamless Integration both are supported for UPI OTM flow.**

• **_Maximum block can be of 60 days only&#x20;_&#x42;ut as per IRDAI guidelines, few MCC's can&#x20;**&#x2003;**only block upto 14 days,MCC- 6300/5960/6529.**

**Integration:-&#x20;**<br />**Amount Limitations for Auth call:-&#x20;**<br />amount>=50 <br />amount>=10 <br />**Amount Limitations for capture call:-&#x20;**<br />amount >=150 - Captured <br />amount between 25 and 50 - Failed with Insufficient amount amount between 50 and 100 - Failed with Invalid data

<br />

<br />

Rest - Transaction initiated

**UPI Collect**

**Step -1**

**API Request:-**

curl --location  \ <br />--header 'Content-Type: application/x-www-form-urlencoded' \ <br />--header 'Cookie: PHPSESSID=34tk7kqalfa05u8qja8ptuc0hs; <br />USERTXNINFO=678e2ef51c8dc2.87238836; PHPSESSID=67f7a004ef404' \ <br />--form 'key="Py06cB"' \ <br />--form 'txnid="Txn\_202504101609"' \ <br />--form 'amount="150"' \ <br />--form 'productinfo="iPhone"' \ <br />--form 'firstname="Test User"' \ <br />--form 'email="' \ <br />--form 'phone<br />--form 'surl= "' \ <br />--form 'furl=" "' \ <br />--form 'api\_version="7"' \ <br />--form 'pre\_authorize="1"' \ <br />--form 'si\_details="{\\"paymentStartDate\\": \\"2025-04-10\\",\\"paymentEndDate\\": \\"2025-05-10\\"}"' \ <br />--form <br />'hash="3deda7f803fa8d929c65b25c88116092a1d9c0123be29c8f44f0337068680f4a408f2662611 349704ab775ab085a992e4c966d8bc57d7f6ccaf30cd244dadcc9"' \ <br />--form 'pg="UPI"' \ <br />--form 'bankcode="UPI"' \ <br />--form 'vpa="9999999999\@upi"' \ <br />--form 'txn\_s2s\_flow="4"'

**Response:-**

{"metaData":{"message":null,"referenceId":"5656c9bdbeb4cf2714f48b2506d0f178e20404e1c58 1b7d163d89a3702adcf16","statusCode":null,"txnId":"Txn\_202504101609","txnStatus":"pending ","unmappedStatus":"pending"},"result":{"acsTemplate":"PGh0bWw+PGJvZHk+PGZvcm0gbm FtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vY XBpdGVzdC5wYXl1LmluL3B1YmxpYy8jLzU2NTZjOWJkYmViNGNmMjcxNGY0OGIyNT A2ZDBmMTc4ZTIwNDA0ZTFjNTgxYjdkMTYzZDg5YTM3MDJhZGNmMTYvdXBpTG9hZ GVyIiBtZXRob2Q9ImdldCI+PC9mb3JtPjxzY3JpcHQgdHlwZT0ndGV4dC9qYXZhc2NyaXB0 Jz4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdpbmRvdy5vbmxvYWQ9ZnVuY3Rpb 24oKXsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBkb2N1bWVudC5mb3Jtc1s ncGF5bWVudF9wb3N0J10uc3VibWl0KCk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgI

<br />

<br />

CB9CiAgICAgICAgICAgICAgICAgICAgICAgIDwvc2NyaXB0PjwvYm9keT48L2h0bWw+"," otpPostUrl":"https:\\/\\/test.payu.in\\/ResponseHandler.php"}}

Once Received, decode the acs template and make the auth transaction as successful.

**Step-2 Capture API Request:-**

**Request:-**

curl --location ' \ <br />--header 'Content-Type: application/x-www-form-urlencoded' \ <br />--header 'Cookie: PHPSESSID=34tk7kqalfa05u8qja8ptuc0hs; <br />USERTXNINFO=678e2ef51c8dc2.87238836; PHPSESSID=67f7a004ef404' \ --form 'key="Py06cB"' \ <br />--form 'hash="{{hash}}"' \ <br />--form 'command="capture\_transaction"' \ <br />--form 'var1="403993715533712528"' \ <br />--form 'var2="cap\_403993715533712528"' \ <br />--form 'var3="150"'

**Response:-**

{"msg":"Transaction Processed <br />successfully","result":{"mode":"UPIOTM","amount":150.0,"merchantId":8297436,"payuid":403 993715533712551,"authpayuid":"403993715533712528","bankRefNumber":"ICI3X0MY3HCK LT2N9SZPPQ2IAC0BHMVRSIZT","field9":"92|Transaction <br />Initiated","payerVpa":"9999999999\@upi","field5":"403993715533712528","txnId":"cap\_40399 3715533712528","status":"in progress"},"status":1}

**Step-3 Once Capture call is successfull, Call the verify\_payment API**

**Request:-**

curl --location ' \ --header 'accept: application/json' \ <br />--header 'Content-Type: application/x-www-form-urlencoded' \ --header 'Content-Type: application/x-www-form-urlencoded' \ --header 'Cookie: PHPSESSID=34tk7kqalfa05u8qja8ptuc0hs; <br />USERTXNINFO=678e2ef51c8dc2.87238836' \ <br />--data-urlencode 'key=Py06cB' \ <br />--data-urlencode 'command=verify\_payment' \ <br />--data-urlencode 'var1=cap\_403993715533712528' \ <br />--data-urlencode 'hash={{hash}}'

**Response:-**

<br />

<br />

{"status":1,"msg":"1 out of 1 Transactions Fetched <br />Successfully","transaction\_details":{"cap\_403993715533712528":{"mihpayid":"403993715533 712551","request\_id":"","bank\_ref\_num":"1744281709095","amt":"150.00","transaction\_amoun t":"150.00","txnid":"cap\_403993715533712528","additional\_charges":"0.00","productinfo":"iPh one","firstname":null,"bankcode":"UPIOTM","udf1":null,"udf2":null,"udf3":null,"udf4":"Execut ed","udf5":"403993715533712528","field2":null,"field9":"Transaction Successful|Completed Using Verify API","error\_code":"E000","addedon":"2025-04-10 <br />16:11:45","payment\_source":"payuPureS2S","card\_type":null,"error\_Message":"NO <br />ERROR","net\_amount\_debit":150.00,"disc":"0.00","mode":"UPIOTM","PG\_TYPE":"UPIOTM-PG","card\_no":"","status":"success","unmappedstatus":"captured","Merchant\_UTR":null,"Settle d\_At":"0000-00-00 <br />00:00:00","App\_Name":"Bhim","card\_token":null,"payment\_aggregator":"PayU","offerAvailed ":null}}}

**UPI Intent**

**Step-1 API Request:-**

curl --location  \ <br />--header 'Content-Type: application/x-www-form-urlencoded' \ <br />--header 'Cookie: PHPSESSID=34tk7kqalfa05u8qja8ptuc0hs; <br />USERTXNINFO=678e2ef51c8dc2.87238836; PHPSESSID=67f7a947a6446' \ <br />--form 'key="Py06cB"' \ <br />--form 'txnid="Txn\_202504101618"' \ <br />--form 'amount="100"' \ <br />--form 'productinfo="iPhone"' \ <br />--form 'firstname="Test User"' \ <br />--form 'email="' \ <br />--form 'phone<br />--form 'surl=" "' \ <br />--form 'furl=" "' \ <br />--form 'api\_version="7"' \ <br />--form 'pre\_authorize="1"' \ <br />--form 'si\_details="{\\"paymentStartDate\\": \\"2025-04-10\\",\\"paymentEndDate\\": \\"2025-05-10\\"}"' \ <br />--form <br />'hash="77557625fbaef605ec28b4c6417c5ee3b7d8c1349e24f884bc2c04b93765440a5f4d280a8e9 aac1191601dffba3fd2fe38f90ae82b318a4e3059cff683fcf97e"' \ <br />--form 'pg="UPI"' \ <br />--form 'bankcode="INTENT"' \ <br />--form 'txn\_s2s\_flow="4"'

**Response:-**

{"metaData":{"message":null,"referenceId":"f7c43002e9a697b278d42141b90299c858948119a3 3d203d418973bc648cbe6d","statusCode":null,"txnId":"Txn\_202504101618","txnStatus":"pendi

<br />

<br />

ng","unmappedStatus":"pending"},"result":{"paymentId":"403993715533713038","merchantNa me":"Merchant","merchantVpa":"payutesting\@icici","amount":"100.00","intentURIData":"upi:\ /\\/mandate?pa=payutesting\@icici\&pn=PAYU%20PAYMENTS%20PRIVATE%20LIMITED\&t r=EZM2022083118055810866491\&am=100.00\&cu=INR\&orgid=400011\&mc=4816\&purpose= 14\&tn=Upi%20Mandate\&validitystart=10\\/04\\/2025\&validityend=10\\/05\\/2025\&amrule=M\&re cur=OT\&recurvalue=NA\&recurtype=NA\&rev=Y\&share=Y\&block=N\&umn=null\&txnType=C REATE\&mode=13\&sign=MEQCIDXKTwZbrUnMqXnnDsCE5SMuquTQ1WWpYiiGrNAQh BWPAiAu\\/nz4GV8UH1JrF5duPoeiOPk1\r\nYRZAx+B5rhNHDcgN7g==\r\n","acsTemplate":" PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9w b3N0IiBhY3Rpb249Imh0dHBzOi8vdGVzdC5wYXl1LmluL2Y3YzQzMDAyZTlhNjk3YjI3OG Q0MjE0MWI5MDI5OWM4NDIxZDcyODA4ZjJiYmNiZjcyODljN2MyOWI4MTI1NzcvaW50 ZW50U2VhbWxlc3NIYW5kbGVyLnBocCIgbWV0aG9kPSJwb3N0Ij48aW5wdXQgdHlwZT0i aGlkZGVuIiBuYW1lPSJ0b2tlbiIgdmFsdWU9IjFBNjZGMDFGLTU3QTctQkY2OS01ODNCL Tg5Qjc5N0I5MzAzQyI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iYW1vdW50IiB2YWx1 ZT0iMTAwLjAwIj48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJtaWhwYXlpZCIgdmFsd WU9ImY3YzQzMDAyZTlhNjk3YjI3OGQ0MjE0MWI5MDI5OWM4NTg5NDgxMTlhMzNk MjAzZDQxODk3M2JjNjQ4Y2JlNmQiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9ImRpc 2FibGVJbnRlbnRTZWFtbGVzc0ZhaWx1cmUiIHZhbHVlPSIwIj48aW5wdXQgdHlwZT0iaGlk ZGVuIiBuYW1lPSJwYXllZVZwYSIgdmFsdWU9InBheXV0ZXN0aW5nQGljaWNpIj48aW5w dXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJwYXllZU5hbWUiIHZhbHVlPSJNZXJjaGFudCI+PGl ucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iYWRkaXRpb25hbENoYXJnZXMiIHZhbHVlPSIiPj xpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InRyYW5zYWN0aW9uRmVlIiB2YWx1ZT0iM TAwLjAwIj48L2Zvcm0+PHNjcmlwdCB0eXBlPSd0ZXh0L2phdmFzY3JpcHQnPgogICAgICA gICAgICAgICAgICAgICAgICAgICAgd2luZG93Lm9ubG9hZD1mdW5jdGlvbigpewogICAgIC AgICAgICAgICAgICAgICAgICAgICAgICAgIGRvY3VtZW50LmZvcm1zWydwYXltZW50X 3Bvc3QnXS5zdWJtaXQoKTsKICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0KICAgIC AgICAgICAgICAgICAgICAgICAgPC9zY3JpcHQ+PC9ib2R5PjwvaHRtbD4=","otpPostUrl":"h ttps:\\/\\/test.payu.in\\/ResponseHandler.php"}}

**Step - 2**

Once the request is completed successfully, Call the verify\_payment API to make the transaction in auth state.

**Request:-**

curl --location  \ --header 'accept: application/json' \ <br />--header 'Content-Type: application/x-www-form-urlencoded' \ --header 'Content-Type: application/x-www-form-urlencoded' \ --header 'Cookie: PHPSESSID=34tk7kqalfa05u8qja8ptuc0hs; <br />USERTXNINFO=678e2ef51c8dc2.87238836' \ <br />--data-urlencode 'key=Py06cB' \ <br />--data-urlencode 'command=verify\_payment' \ <br />--data-urlencode 'var1=Txn\_202504101618' \ <br />--data-urlencode 'hash={{hash}}'

<br />

<br />

**Response:-**

{"status":1,"msg":"1 out of 1 Transactions Fetched <br />Successfully","transaction\_details":{"Txn\_202504101618":{"mihpayid":"403993715533713038 ","request\_id":"","bank\_ref\_num":"1744283979836","amt":"100.00","transaction\_amount":"100 .00","txnid":"Txn\_202504101618","additional\_charges":"0.00","productinfo":"iPhone","firstna me":"Test <br />User","bankcode":"INTENT","udf1":"","udf2":"","udf3":"","udf4":"Created","udf5":"","field2": null,"field9":"Transaction Successful|Completed Using Verify <br />API","error\_code":null,"addedon":"2025-04-10 <br />16:49:35","payment\_source":"payuPureS2S","card\_type":null,"error\_Message":"NO <br />ERROR","net\_amount\_debit":100.00,"disc":"0.00","mode":"UPI","PG\_TYPE":"UPI-<br />PG","card\_no":"","status":"success","unmappedstatus":"auth","Merchant\_UTR":null,"Settled\_At ":"0000-00-00 <br />00:00:00","App\_Name":"Paytm","card\_token":null,"payment\_aggregator":"PayU","offerAvaile d":null}}}

**Step -3**

**Capture API Call:-**

All successful registration transactions can be captured with server to server API without any additional factor authentication or customers’ involvement.

**Sample Request:-**

curl --location  \ <br />--header 'Content-Type: application/x-www-form-urlencoded' \ <br />--header 'Cookie: PHPSESSID=34tk7kqalfa05u8qja8ptuc0hs; <br />USERTXNINFO=678e2ef51c8dc2.87238836; PHPSESSID=67f7ab59a1415' \ --form 'key="Py06cB"' \ <br />--form 'hash="{{hash}}"' \ <br />--form 'command="capture\_transaction"' \ <br />--form 'var1="403993715533713169"' \ <br />--form 'var2="cap\_403993715533713169"' \ <br />--form 'var3="150"'

**Sample Response**

{"msg":"Transaction Processed <br />successfully","result":{"mode":"UPIOTM","amount":150.0,"merchantId":8297436,"payuid":403 993715533713181,"authpayuid":"403993715533713169","bankRefNumber":"ICIPHBNLP4YZ UYFMS00V34MLWGOWA3HKAN55","field9":"92|Transaction <br />Initiated","payerVpa":"ps\@paytm","field5":"403993715533713169","txnId":"cap\_40399371553 3713169","status":"in progress"},"status":1}

<br />

<br />

**Step-4**

Call the verify\_payment API to make the transaction successful:-

**Request:-**

curl --location ' \ --header 'accept: application/json' \ <br />--header 'Content-Type: application/x-www-form-urlencoded' \ --header 'Content-Type: application/x-www-form-urlencoded' \ --header 'Cookie: PHPSESSID=34tk7kqalfa05u8qja8ptuc0hs; <br />USERTXNINFO=678e2ef51c8dc2.87238836' \ <br />--data-urlencode 'key=Py06cB' \ <br />--data-urlencode 'command=verify\_payment' \ <br />--data-urlencode 'var1=cap\_403993715533713169' \ <br />--data-urlencode 'hash={{hash}}'

**Response:-**

{"status":1,"msg":"1 out of 1 Transactions Fetched <br />Successfully","transaction\_details":{"cap\_403993715533713169":{"mihpayid":"403993715533 713181","request\_id":"","bank\_ref\_num":"1744284562714","amt":"150.00","transaction\_amoun t":"150.00","txnid":"cap\_403993715533713169","additional\_charges":"0.00","productinfo":"iPh one","firstname":null,"bankcode":"INTOTM","udf1":null,"udf2":null,"udf3":null,"udf4":"Execut ed","udf5":"403993715533713169","field2":null,"field9":"Transaction Successful|Completed Using Verify API","error\_code":"E000","addedon":"2025-04-10 <br />16:59:19","payment\_source":"payuPureS2S","card\_type":null,"error\_Message":"NO <br />ERROR","net\_amount\_debit":150.00,"disc":"0.00","mode":"UPIOTM","PG\_TYPE":"UPIOTM-PG","card\_no":"","status":"success","unmappedstatus":"captured","Merchant\_UTR":null,"Settle d\_At":"0000-00-00 <br />00:00:00","App\_Name":"Paytm","card\_token":null,"payment\_aggregator":"PayU","offerAvaile d":null}}}

**In case of UPI, capture payments are not synchronous in nature and final response of the transaction is not communicated over real time. For these “inprogress” cases, PayU can notify merchant the exact status of the transaction as either “success” or “failure” over Webhook in a same way shared for auth transaction during transaction call or can call verify\_payment API to get the status.**

**Step-4 (Optional):**

**Cancelling Blocked registration**

This interface allows merchants to cancel UPI registration from their website. Once registration is cancelled the amount will be released and there is no way to restore it and customer has to register fresh mandate with merchant.

<br />

<br />

PayU’s Refund API is used for cancellation of the Mandate or Auth Transactions:-

<br />

<br />
