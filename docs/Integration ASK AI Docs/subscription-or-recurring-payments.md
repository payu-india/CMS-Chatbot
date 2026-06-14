---
title: 'Subscription or Recurring Payments '
deprecated: false
hidden: false
metadata:
  robots: index
---
**Subscription or Recurring Payments&#x20;**<br />The Recurring Payments or Standing Instruction (SI) is the mode of payment agreed by the customer to pay against a package for each payment term during the subscription.

Recurring Payments is an easy and automated method to reduce the administrative burden for periodical payments. Based on the specified pay modes, the customer gives a mandate to the bank to debit a fixed amount from the customer’s account and pay to the merchant.

Doc Reference: **Payment Method Supported: -**<br />1.CARD <br />2. UPI <br />3.NetBanking (Enach/Emandate)

&#x20;Majorly three steps involved in overall Subscription Payment Journey: - 1.Registration Transaction <br />2.Pre-Debit Notification <br />3.Recurring Call

**Customer Experience: -&#x20;**&#x52;efer below link for Customer’s UI experience for each pay mode. <br />**&#x20;----------------------------------------------------------------------------------------------------**<br />  **Paymode - UPI&#x20;**<br />**Limitations while Testing&#x20;**:- <br />·       Amount should be = > 2.

·       Billing amount should be = >200.

·       Test UPI- 9999999999\@upi

<br />

<br />

·       Mandatorily call the verify\_payment API after si\_transaction API to make the transaction status success. Initially it will be in in\_process state.

**Registration Transaction Request: -&#x20;**<br />The parameters shared below are for non-seamless integration. For seamless integration refer to the below doc link for additional parameters required for UPI Paymode:- <br />

**Request:-**<br />**hash:**&#x38;e704dd989a1b9f33202d6d725aeb61382ab9d4fa9697ec84e8cba653b25deee73e9efff33e0 6f31ecb18313e9754390951f3cfcf7e75bffdd1907fa54175fac <br />**key:&#x20;**&#x7A;8a7yT <br />**txnid:&#x20;**&#x31;4702db39d4552518127 <br />**api\_version:&#x20;**&#x37; <br />**amount:&#x20;**&#x31;00 <br />**firstname:&#x20;**&#x50;ayu-Admin <br />**email:&#x20;**<br />**phone:&#x20;**&#x31;234567890 <br />**productinfo:&#x20;**&#x50;roduct Info <br />**surl:&#x20;**<br />**furl:&#x20;**<br />**si:&#x20;**&#x31; <br />**si\_details:&#x20;**<br />{"billingAmount":"200.00","billingCurrency":"INR","billingCycle":"ADHOC","billingInterval": 1,"paymentStartDate":"2024-05-17","paymentEndDate":"2025-12-30"}

<br />

**Response**: <br />   \[mihpayid] => 403993715531561494 <br />  \[mode] => UPI <br />  \[status] => success <br />  \[unmappedstatus] => captured <br />  \[key] => z8a7yT <br />  \[txnid] => 14702db39d4552518127 <br />  \[amount] => 100.00 <br />  \[discount] => 0.00 <br />  \[net\_amount\_debit] => 100 <br />  \[addedon] => 2024-05-17 12:22:03 <br />  \[productinfo] => Product Info <br />  \[firstname] => Payu-Admin <br />  \[lastname] => <br />  \[address1] => <br />  \[address2] => <br />  \[city] => <br />  \[state] => <br />  \[country] => <br />  \[zipcode] => <br />  \[email] => <br />  \[phone] => 1234567890 <br />  \[udf1] =>

  \[udf2] => <br />  \[udf3] => <br />  \[udf4] => Executed Verified <br />  \[udf5] => <br />  \[udf6] => <br />  \[udf7] => <br />  \[udf8] => <br />  \[udf9] => <br />  \[udf10] => <br />  \[hash] => <br />0c217084e19d45d38267f0eb3d0500588aef5745c3db457c417bd66ef300a72b24d1d80e124b6937 40e413d7fef4bfbc4187cc8bdacdb46075733dd9fcee03ce <br />  \[field1] => 9999999999\@upi <br />  \[field2] => HDFXQQOF2EB513U0AJK75JSL3GRDN4AXZV59 <br />  \[field3] => 9999999999\@upi <br />  \[field4] => MASUDA BIBI DAFADAR <br />  \[field5] => 403993715531561494 <br />  \[field6] => <br />  \[field7] => Mandate Request Approved <br />  \[field8] => generic <br />  \[field9] => MD202|Mandate Request Approved|Completed Using Verify API <br />  \[payment\_source] => sist <br />  \[meCode] => {"pgMid":"HDFC000000000105"} <br />  \[PG\_TYPE] => UPI-PG

&#x20;\[bank\_ref\_num] => 1715928742512 <br /> \[bankcode] => UPI <br /> \[error] => E000 <br /> \[error\_Message] => No Error <br /> \[splitInfo] => {"splitStatus":"splitNotReceived","splitSegments":\[]}

**Pre-Debit Notification API**

The **Pre-Debit Notification** API allows the merchants to send a pre-debit notification to the customer regarding an upcoming payment which will be deducted from the customer’s account as part of the registration. There is a mandate to send this notification to the customer at least 48 hours before the actual debit, that is, 48 hours before calling the Recurring API.

&#x20;It is Mandatory to Check the mandate status before calling the **Pre-Debit Notification** API.

**Get Mandate Status API (for UPI only)&#x20;**<br />**Request:-**<br />curl --location  \ <br />--header 'Content-Type: application/x-www-form-urlencoded' \ <br />--data-urlencode 'key=z8a7yT' \ <br />--data-urlencode 'command=upi\_mandate\_status' \ <br />--data-urlencode 'var1={"authPayuId": "403993715531561494","requestId": "12345678"}' \ --data-urlencode <br />'hash=a3ca72482efc481f34525ae99ccdc17058edd430c83b7f3fa24bf2f695f66121c8fd81d6aa237 691704efb43ea5510e518249db6348b4fea25557f0850cb9b74'

<br />

**Response:-**<br /> { <br />  "status": "active", <br />  "action": "MANDATE\_STATUS", <br />  "authpayuid": "403993715531561494", <br />  "amount": "200.00", <br />  "mandateStartDate": "2024-05-17 00:00:00", <br />  "mandateEndDate": "2025-12-30 00:00:00" <br />}

In case of Mandate already Revoked:- <br />{ <br />  "status": "revoked", <br />  "action": "MANDATE\_STATUS", <br />  "authpayuid": "403993715531561494", <br />  "amount": "200.00", <br />  "mandateStartDate": "2024-05-17 00:00:00", <br />  "mandateEndDate": "2026-12-31 00:00:00" <br />}

**Pre-Debit Notification API Call:&#x20;**&#x41;s the Mandate status is in Active State, We can call the Pre-Debit Notification. API.

**Request:-**<br /> curl --location ' \ <br />--header 'Content-Type: application/x-www-form-urlencoded' \ <br />--data-urlencode 'key=z8a7yT' \ <br />--data-urlencode 'command=pre\_debit\_SI' \ <br />--data-urlencode <br />'hash=7c8a21ecced9352dffba52149d27afc4701b8e5f7195f426365cb6d465875ea4a7e38dd13549 7ed560f48e5b05116cccd05994f9049d9aa74bc7b16c133bef59' \ <br />--data-urlencode <br />'var1={"authpayuid":"403993715531561494","requestid":"pre\_403993715531561494","debitdat e":"2024-05-17","invoiceDisplayNumber":"pre\_403993715531561494","amount":"200.00"}'

**Response:-**<br />{ <br />   "status": 1, <br />   "message": "Request Processed Successfully",    "action": "MANDATE\_PRE\_DEBIT", <br />   "invoiceid": "cnXWQ2eOGB", <br />   "approvedStatus": "NA", <br />   "invoiceStatus": "SUCCESS", <br />   "amount": "NA" <br />}

**Note**:- **In order to retrieve the status of Notification shared or Delete the shared notification. Action parameter can be passed in pre debit notification API.**

**Recurring API Request&#x20;**<br />It will be called on Debit Date provided in Pre-Debit API Call:- <br />**&#x20;Request:-**<br />curl --location  \ <br />--header 'Content-Type: application/x-www-form-urlencoded' \ <br />--data-urlencode 'key=z8a7yT' \ <br />--data-urlencode 'command=si\_transaction' \ <br />--data-urlencode <br />'hash=0285d6c5edac170d48404e8ca5213c82161f24dd880ba1bf1250ae86a2c1b40b792dcc87c40 254d5eac91fc7c7a8041ba098f51c4c3776377469adfe9856f749 ' \ <br />--data-u<br />'var1={","txnid":"rec\_403993715531561494","invoiceDisplayNumber":"pre\_4039937 15531561494"}'

**&#x20;Response:-**<br />{ <br />   "status": 1, <br />   "message": "Transaction Processed successfully", <br />   "details": { <br />   "rec\_403993715531561494": { <br />    "authpayuid": "403993715531561494", <br />    "transactionid": "rec\_403993715531561494", <br />    "amount": "200", <br />    "user\_credentials": "z8a7yT:14702db39d4552518127",     "card\_token": "",

   "payuid": "403993715531562010", <br />   "status": "in progress", <br />   "udf1": null, <br />   "field9": "MD202|Mandate Request Approved",    "udf2": "", <br />   "udf3": "", <br />   "udf4": "Executed", <br />   "udf5": "403993715531561494", <br />   "phone": "9876543210", <br />   "email": "" <br />  } <br />  } <br />}

**Note: Call verify\_payment API make the transaction status success. Initially it will be in in\_process state.**

**Verify\_Payment API:-**<br />**Request:-**<br />curl --location ' \ --header 'accept: application/json' \ <br />--header 'Content-Type: application/x-www-form-urlencoded' \ --data-urlencode 'key=z8a7yT' \ <br />--data-urlencode 'command=verify\_payment' \\

\--data-urlencode 'var1=rec\_403993715531561494' \ --data-urlencode 'hash={{hash}}'

**&#x20;Response:-**<br /> { <br />  "status": 1, <br />  "msg": "1 out of 1 Transactions Fetched Successfully",   "transaction\_details": { <br />  "rec\_403993715531561494": { <br />   "mihpayid": "403993715531562010", <br />   "request\_id": "", <br />   "bank\_ref\_num": "1715928742512", <br />   "amt": "200.00", <br />   "transaction\_amount": "200.00", <br />   "txnid": "rec\_403993715531561494", <br />   "additional\_charges": "0.00", <br />   "productinfo": "SI", <br />   "firstname": "", <br />   "bankcode": "UPISI", <br />   "udf1": null, <br />   "udf3": null, <br />   "udf4": "Executed Verified", <br />   "udf5": "403993715531561494",

   "field2": "HDFXQQOF2EB513U0AJK75JSL3GRDN4AXZV59", <br />   "field9": "MD202|Mandate Request Approved|Completed Using Verify API",    "error\_code": "E000", <br />   "addedon": "2024-05-17 12:53:21", <br />   "payment\_source": "sirecurring", <br />   "card\_type": null, <br />   "error\_Message": "No Error", <br />   "meCode": "{\\"pgMid\\":\\"HDFC000000000105\\"}", <br />   "net\_amount\_debit": 200, <br />   "disc": "0.00", <br />   "mode": "UPISI", <br />   "PG\_TYPE": "UPISI-PG", <br />   "card\_no": "", <br />   "udf2": null, <br />   "status": "success", <br />   "unmappedstatus": "captured", <br />   "Merchant\_UTR": null, <br />   "Settled\_At": "0000-00-00 00:00:00" <br />  } <br />  } <br />}

**Manage UPI Recurring:-**

We have 3 more APIs in order to Manage the UPI Transaction:- 1.Cancel Mandate API <br />2.Modification API <br />3.Validate VPA API

**Cancel Mandate API:-**<br />**Cancel Recurring Registration** API allows the merchants to cancel the UPI registration from their website. It is a mandate to implement the **Cancel Recurring Registration** API so that your customers can use Recurring Payments as per their need.

**Request:-**<br />curl --location ' \ <br />--header 'Content-Type: application/x-www-form-urlencoded' \ <br />--data-urlencode 'key=z8a7yT' \ <br />--data-urlencode 'command=upi\_mandate\_revoke' \ <br />--data-urlencode 'var1={"authPayuId": "403993715531561494","requestId": "170520241329"}' \ --data-urlencode <br />'hash=0faa5e95829bb2466acc934e0f863ebfdbce24674cb148174f63fd78ec48c56a4a16d10367ed ec60c02748d0fe36dff13a0eb3b8b399034e50ce95be06878ad2'

**Response:-**<br />{ <br />   "status": 1, <br />   "action": "MANDATE\_REVOKE", <br />   "message": "Mandate Revoked Successfully"

}

**Modification API:-**<br /> This API can be used to update the Subscription end Date or Billing amount. If you do not wish to modify, You can directly Revoke the current Subscription and create the new one.

**Request:-**<br /> curl --location ' \ <br />--header 'accept: application/json' \ <br />--header 'Content-Type: application/x-www-form-urlencoded' \ <br />--data-urlencode 'key=z8a7yT' \ <br />--data-urlencode 'command=upi\_mandate\_modify' \ <br />--data-urlencode 'var1={"authPayuId": "403993715531561494","amount": 200,"endDate": "2026-12-31","requestId": "170520241321"}' \ <br />--data-urlencode <br />'hash=5b40d077756080ecee220a578654d790b6d72b66dda4c4d5d6221df7402cc58f1c9a4e188a 7626251931e1b7a6b15f35bebffda45dae77778b4d6fb18aa5500b'

**Response:-**<br /> { <br />  "status": 1, <br />  "action": "MANDATE\_UPDATE", <br />  "message": "Mandate update pending at PG. Please wait for webhook or use upi\_mandate\_status service to confirm updated status" <br />}

**Validate VPA API :-**<br />This API is required only for seamless integration. After the customer enters VPA on the merchant page, you need to call this API to check for VPA validation. If VPA is valid only then, the second call should be made.

**Request:-**<br /> curl --location  \ <br />--header 'accept: application/json' \ <br />--header 'Content-Type: application/x-www-form-urlencoded' \ <br />--data-urlencode 'key=z8a7yT' \ <br />--data-urlencode 'command=validateVPA' \ <br />--data-urlencode 'var1=9999999999\@upi' \ <br />--data-urlencode <br />'hash=5c787cff9c9c2525def4f0af0d47b527f4e5a7ac5b3de578ccc50c8e33c4ffc1fb12ac254285d4 35502bec1e7f65b3981565716bf44dc3bf4fd6bc536d44ebe9' \ <br />--data-urlencode 'var2={"validateAutoPayVPA":"1"}'

**Response:-**<br /> { <br />   "status": "SUCCESS", <br />   "vpa": "9999999999\@upi", <br />   "isVPAValid": 1, <br />   "payerAccountName": "MASUDA BIBI DAFADAR",    "isAutoPayVPAValid": 1, <br />   "isAutoPayBankValid": "NA"

} <br />**&#x20;----------------------------------------------------------------------------------------------------** **Paymode – E-Nach**

**Limitations**<br />·       Free trial should be 1 for test for non seamless flow, for seamless amount should b 0 and there is no use of field free trial in case of seamless.

·       Billing amount needs to be 1 for testing.

·       Payment starts date should be day+1 or any other date, current date doesn’t support.

·       Test Credentials: - <br /> Beneficiary Name: Sachin Tendulkar  <br /> Beneficiary Account Number: 1211450021   Beneficiary Account Type: SAVINGS   Beneficiary Ifsc Code: ICIC0000046  <br /> Verification Mode: DEBIT\_CARD

**Registration Transaction Request: -&#x20;**<br />The parameters shared below are for seamless integration. For Non- seamless integration only standard parameters needs to be passed likewise shared above for UPI pay mode:-

**Request:-**<br />**hash:**&#x63;2ee7e1a0d7b1fd7040e85eedf06cfd6928e734251313e738fb2e9a3ec9931b478519bcbc65c 79018866a8accbfcb390bda4c1abba72c728d69906e1c523c8e3 <br />**key:&#x20;**&#x7A;8a7yT

**txnid:&#x20;**&#x38;59370d845f484493c8d <br />**api\_version:&#x20;**&#x37; <br />**amount:&#x20;**&#x31;0 <br />**firstname:&#x20;**&#x50;ayu-Admin <br />**email:&#x20;**<br />**phone:&#x20;**&#x31;234567890 <br />**productinfo:&#x20;**&#x50;roduct Info <br />**surl:&#x20;**<br />**furl:&#x20;**<br />**si:&#x20;**&#x31; <br />**free\_trial:&#x20;**&#x31; <br />**beneficiarydetail:&#x20;**{"beneficiaryName":"Sachin Tendulkar","beneficiaryAccountNumber": "1211450021","beneficiaryAccountType":"SAVINGS", "beneficiaryIfscCode":"ICIC0000046", "verificationMode":"DEBIT\_CARD"} <br />**pg:&#x20;**&#x45;NACH <br />**bankcode:&#x20;**&#x49;CICENCC <br />**si\_details:**{"billingAmount":"1.00","billingCurrency":"INR","billingCycle":"ADHOC","billingI nterval":1,"paymentStartDate":"2024-05-21","paymentEndDate":"2025-12-30"}

**Response:-**<br />\[mihpayid] => 403993715531574955 <br />  \[mode] => ENACH <br />  \[status] => success <br />  \[unmappedstatus] => captured <br />  \[key] => z8a7yT

&#x20;\[txnid] => 859370d845f484493c8d <br /> \[amount] => 0.00 <br /> \[discount] => 0.00 <br /> \[net\_amount\_debit] => 0 <br /> \[addedon] => 2024-05-20 14:22:46 <br /> \[productinfo] => Product Info <br /> \[firstname] => Payu-Admin <br /> \[lastname] => <br /> \[address1] => <br /> \[address2] => <br /> \[city] => <br /> \[state] => <br /> \[country] => <br /> \[zipcode] => <br /> \[email] => <br /> \[phone] => 1234567890 <br /> \[udf1] => <br /> \[udf2] => <br /> \[udf3] => <br /> \[udf4] => <br /> \[udf5] => <br /> \[udf6] => <br /> \[udf7] =>

  \[udf8] => <br />  \[udf9] => <br />  \[udf10] => <br />  \[hash] => <br />05fa2a831243d868d26f7ec92df74d10178b3a5940c5b0766d1ab62d51a3cc44ea800e3f01552fe43 c1ca8dafe3a08e37efa06f006e024d667df0d81979e3ed2 <br />  \[field1] => ENACH443662560604006640 <br />  \[field2] => 815166426722674149 <br />  \[field3] => <br />  \[field4] => <br />  \[field5] => <br />  \[field6] => <br />  \[field7] => <br />  \[field8] => <br />  \[field9] => Mandate successfully scheduled at bank end: Your payment is scheduled successfully <br />  \[payment\_source] => sist <br />  \[meCode] => {"payeeId":"000000000722"} <br />  \[PG\_TYPE] => ENACH-PG <br />  \[bank\_ref\_num] => 428500781657255627 <br />  \[bankcode] => ICICENCC <br />  \[error] => E000 <br />  \[error\_Message] => No Error <br />  \[splitInfo] => {"splitStatus":"splitNotReceived","splitSegments":\[]}

**Pre-Debit Notification API&#x20;**<br />This API is not required for Enach. Hence we can directly proceed with Recurring API call, Post mandate status Check API.

**Mandate Status Check API**

**Request:-&#x20;**<br />curl --location ' \ <br />--header 'Content-Type: application/x-www-form-urlencoded' \ <br />--data-urlencode 'key=z8a7yT' \ <br />--data-urlencode 'command=NB\_mandate\_status' \ <br />--data-urlencode 'var1={"authPayuId": "403993715531574955","requestId": "202405201420"}' \ --data-urlencode 'hash= <br />c57de6a378619d725118431000d11b9278e2267118f49f1fc7e1566d5dd589aa633d7bd438647f9a f5e8fea6b032b6f182ed9428d091fdf740fe93b40afebe72'

**Response:-**<br />{ <br />   "status": "SUCCESS", <br />   "action": "NB\_mandate\_status", <br />   "authpayuid": "403993715531574955", <br />   "amount": "1.00", <br />   "mandateStartDate": "2024-05-21",

&#x20;"mandateEndDate": "2025-12-30"

}

**&#x20;Recurring API**

For ENACH, pending status  is common with most Net Banking (except ICICI in the specific scenario). In that case, the merchant should consider this as successful initiation of payment with bank / NPCI. The status will be notified back to the merchant over payment processing with individual bank gets completed. It is suggested to call the verify\_payment API up to T+2 once a day means “pending” transaction gets converted into “captured” or “failed” from the same day till T+2 anytime, depending upon the bank account used by the customer in setting up <br />registration.

**Request:-**

&#x20;curl --location  \\

\--header 'Content-Type: application/x-www-form-urlencoded' \\

\--data-urlencode 'key=z8a7yT' \\

\--data-urlencode 'command=si\_transaction' \\

\--data-urlencode <br />'hash=6377f0340136bfa26b146a95b541421fa0660167ac236c6c5aa5c7c295611577b1a86693dac cf4af31cb3b9c9964267a6668e71dfc87c26cc458ce3d37a0c4b4' \\

\--data-u<br />,"txnid":"rec\_403993715531574955","invoiceDisplayNumber":"pre\_403993715 531574955"}'

**Response:-**

{

&#x20;"status": 1,

<br />

<br />

  "message": "Transaction Processed successfully", <br />  "details": { <br />  "rec\_403993715531574955": { <br />   "authpayuid": "403993715531574955", <br />   "transactionid": "rec\_403993715531574955", <br />   "amount": "1", <br />   "user\_credentials": "z8a7yT:859370d845f484493c8d",    "card\_token": "", <br />   "payuid": "403993715531575128", <br />   "status": "captured", <br />   "udf1": null, <br />   "field9": "Payment Successful", <br />   "udf2": "", <br />   "udf3": "", <br />   "udf4": "", <br />   "udf5": "", <br />   "phone": "9876543210", <br />   "email": "" <br />  } <br />  } <br />}

**Manage E-Mandates**

<br />

&#x20;We have Cancel Mandate API in order to Manage the ENACH Transaction:- 1.Cancel Mandate API

**Cancel Mandate API:- (Currently not Working in UAT)**<br /> The **Cancel Recurring Payments** API allows the merchants to cancel their Cards or Net Banking registration from their website. After the registration is cancelled for a customer, the merchant cannot restore it, and the customer must register a fresh mandate with the merchant.

**Request:-**<br /> curl --location ' \ <br />--header 'Content-Type: application/x-www-form-urlencoded' \ <br />--data-urlencode 'key=z8a7yT' \ <br />--data-urlencode 'command=mandate\_revoke' \ <br />--data-urlencode 'var1={"authPayuId": "403993715531574955","requestId": "202405201452"}' \ --data-urlencode <br />'hash=f365dfa8dc2934247778d8078ec9225fe5c8512e8765ca8a78ccb8c5c3e1bfeedbd5439071a6 29508e129bf386825c0cd27f9d8582c02e5a0dd7620a12e27d87'

**Response:-**<br /> { <br />  "action": "MANDATE\_REVOKE", <br />  "status": 0, <br />  "Message": "Invalid bank received for cancellation",   "authpayuid": 403993715531574955 <br />}

<br />

<br />

**Paymode – Cards**

**&#x20;Limitations:** - <br />Test Card Details: - <br />Card number- 5506900480000008 <br />expiry - 05/25 <br />cvv- 123 <br />otp – 123456

Card number- 4761360079851258 <br />expiry - 05/25 <br />cvv- 123 <br />otp – 123456

**Registration Transaction Request: -&#x20;**<br />The parameters shared below are for seamless integration. For Non- seamless integration only standard parameters needs to be passed likewise shared above for UPI pay mode:-

**Request:-**<br />hash:9fe9f6f43792fc1f7bd91b69663f49efd3e6f8da0f7dec8761d4394d1ba47d9994f308a3ad5f4fa 285cafbf49595042f04681cdec77ac15b92729395d08c28d1 <br />key: z8a7yT

<br />

<br />

txnid: 99390ee3cf2695c66857 <br />api\_version: 7 <br />amount: 10 <br />firstname: Payu-Admin <br />email: <br />phone: 1234567890 <br />productinfo: Product Info <br />surl: <br />furl: <br />si: 1 <br />free\_trial: 1 <br />pg: CC <br />bankcode: VISA <br />ccnum: 5506900480000008 <br />ccname: Test User <br />ccvv: 123 <br />ccexpmon: 05 <br />ccexpyr: 2025 <br />si\_details:{"billingAmount":"200.00","billingCurrency":"INR","billingCycle":"ADHOC","billin gInterval":1,"paymentStartDate":"2024-05-20","paymentEndDate":"2025-12-30"}

**&#x20;Response: -**

\[mihpayid] => 403993715531577472

<br />

<br />

&#x20;\[mode] => CC <br /> \[status] => success <br /> \[unmappedstatus] => captured <br /> \[key] => z8a7yT <br /> \[txnid] => 99390ee3cf2695c66857 <br /> \[amount] => 2.00 <br /> \[cardCategory] => domestic <br /> \[discount] => 0.00 <br /> \[net\_amount\_debit] => 2 <br /> \[addedon] => 2024-05-20 18:51:36 <br /> \[productinfo] => Product Info <br /> \[firstname] => Payu-Admin <br /> \[lastname] => <br /> \[address1] => <br /> \[address2] => <br /> \[city] => <br /> \[state] => <br /> \[country] => <br /> \[zipcode] => <br /> \[email] => <br /> \[phone] => 1234567890 <br /> \[udf1] => <br /> \[udf2] =>

<br />

<br />

  \[udf3] => <br />  \[udf4] => <br />  \[udf5] => <br />  \[udf6] => <br />  \[udf7] => <br />  \[udf8] => <br />  \[udf9] => <br />  \[udf10] => <br />  \[hash] => <br />f90b7e5f05542b93d5a1c8d8beed53bbb1cece2d2befe4dbc81cf113fd666c099fe7351f31d6d8447e f87d76572628b525013d6587309bad4e2304dee0addc8f <br />  \[field1] => 726669248540510100 <br />  \[field2] => 394084 <br />  \[field3] => 2.00 <br />  \[field4] => <br />  \[field5] => 00 <br />  \[field6] => 02 <br />  \[field7] => AUTHPOSITIVE <br />  \[field8] => AUTHORIZED <br />  \[field9] => Transaction is Successful <br />  \[payment\_source] => sist <br />  \[meCode] => <br />{"MID":"PAYUPAYMENTCYBS","TKey":"XkxU7gtGQxXVJbT9csM6tACIwtKvg2rZcQ95S 0PR+cp+5Hw9fYvUzZr/wIAkldIU3wlM3NSYKQFxBFfSKYl4QrRobSPu1IVR37PqnJ9BQgJ G7tCh3w9vEhasJxn85jdTvD4DPpci9qJZw797cPFXSnU9mmq4Yxnm0pVSOH3Sz/NIWVy2p GaRrq9XdISlEmd7MSv1X4wDFck0/Pl51mBLVMWvZYfXsCRJdITUy7aHDO5gb6FRBwDjd

<br />

<br />

G9Fdwv7n5sLaFdiVGfhBMWNNWzWSIzovVdCnfln4sFv1zl70j2tP4+wwBLf/znoEtFq3YpCe 0fE/BbNNwdNwNkzxcghUyhkBg=="} <br />  \[PG\_TYPE] => CC-PG <br />  \[bank\_ref\_num] => 726669248540510100 <br />  \[bankcode] => CC <br />  \[error] => E000 <br />  \[error\_Message] => No Error <br />  \[cardToken] => 9d9953d2ee4d11e07b376 <br />  \[cardnum] => XXXXXXXXXXXX0008 <br />  \[cardhash] => This field is no longer supported in postback params. <br />  \[splitInfo] => {"splitStatus":"splitNotReceived","splitSegments":\[]}

**Registration with Stored Card Token or Network Token**

**Request:-**<br />**&#x20;hash:**&#x31;a6b21b6a09078cc6b35a2d35e1efe5e42f6f121639ab8d20eba8709d02b207cca2707330e0 ec383d69f0b236df0faf80ee8cca200bf6831fae3e86202779dac <br />**key:&#x20;**&#x7A;8a7yT <br />**txnid:&#x20;**&#x32;f27b48f97790b3a50dc <br />**api\_version:&#x20;**&#x37; <br />**amount:&#x20;**&#x31;0 <br />**firstname:&#x20;**&#x50;ayu-Admin <br />**email:&#x20;**<br />**phone:&#x20;**&#x31;234567890

<br />

<br />

**productinfo:&#x20;**&#x50;roduct Info <br />**surl:&#x20;**<br />**furl:&#x20;**<br />**si:&#x20;**&#x31; <br />**free\_trial:&#x20;**&#x31; <br />**pg:&#x20;**&#x43;C <br />**bankcode:&#x20;**&#x4D;AST <br />**ccvv:&#x20;**&#x31;23 <br />**storecard\_token\_type:&#x20;**&#x31; <br />**additional\_info:&#x20;**{"last4Digits":"0008", "tavv": <br />"AD3QxzbRDQHJAAExNCkGAAADFA==","trid":"400000340044", <br />"tokenRefNo":"DM4MMC000014413691ffbba4dc814d8096cd3af521b45ec5"} **ccexpmon:&#x20;**&#x30;6 <br />**ccexpyr:&#x20;**&#x32;027 <br />**store\_card\_token:&#x20;**&#x35;506900498476257

**&#x20;Response:-**<br /> \[mihpayid] => 403993715531581427 <br />   \[mode] => CC <br />   \[status] => success <br />   \[unmappedstatus] => captured <br />   \[key] => z8a7yT <br />   \[txnid] => 2f27b48f97790b3a50dc <br />   \[amount] => 2.00

<br />

<br />

&#x20;\[cardCategory] => domestic <br /> \[discount] => 0.00 <br /> \[net\_amount\_debit] => 2 <br /> \[addedon] => 2024-05-21 13:22:48 <br /> \[productinfo] => Product Info <br /> \[firstname] => Payu-Admin <br /> \[lastname] => <br /> \[address1] => <br /> \[address2] => <br /> \[city] => <br /> \[state] => <br /> \[country] => <br /> \[zipcode] => <br /> \[email] => <br /> \[phone] => 1234567890 <br /> \[udf1] => <br /> \[udf2] => <br /> \[udf3] => <br /> \[udf4] => <br /> \[udf5] => <br /> \[udf6] => <br /> \[udf7] => <br /> \[udf8] =>

<br />

<br />

  \[udf9] => <br />  \[udf10] => <br />  \[hash] => <br />f258659a436b7c2a674dd3c8ded5769c1fd1cdf5b3a7198f10dc2518b0d5c80062a70bc2f10d871c3 270a7752725c05d3a4c2ca54bd37ca83614115fe0167bc1 <br />  \[field1] => 275755070436281730 <br />  \[field2] => 206174 <br />  \[field3] => 2.00 <br />  \[field4] => <br />  \[field5] => 00 <br />  \[field6] => 02 <br />  \[field7] => AUTHPOSITIVE <br />  \[field8] => AUTHORIZED <br />  \[field9] => Transaction is Successful <br />  \[payment\_source] => sist <br />  \[meCode] => <br />{"MID":"PAYUPAYMENTCYBS","TKey":"XkxU7gtGQxXVJbT9csM6tACIwtKvg2rZcQ95S 0PR+cp+5Hw9fYvUzZr/wIAkldIU3wlM3NSYKQFxBFfSKYl4QrRobSPu1IVR37PqnJ9BQgJ G7tCh3w9vEhasJxn85jdTvD4DPpci9qJZw797cPFXSnU9mmq4Yxnm0pVSOH3Sz/NIWVy2p GaRrq9XdISlEmd7MSv1X4wDFck0/Pl51mBLVMWvZYfXsCRJdITUy7aHDO5gb6FRBwDjd G9Fdwv7n5sLaFdiVGfhBMWNNWzWSIzovVdCnfln4sFv1zl70j2tP4+wwBLf/znoEtFq3YpCe 0fE/BbNNwdNwNkzxcghUyhkBg=="} <br />  \[PG\_TYPE] => CC-PG <br />  \[bank\_ref\_num] => 275755070436281730 <br />  \[bankcode] => CC <br />  \[error] => E000 <br />  \[error\_Message] => No Error

<br />

<br />

&#x20;\[cardnum] => XXXXXXXXXXXX0008 <br /> \[cardhash] => This field is no longer supported in postback params.

&#x20;\[splitInfo] => {"splitStatus":"splitNotReceived","splitSegments":\[]}   <br />**Pre-Debit Notification API**<br /> The **Pre-Debit Notification** API allows the merchants to send a pre-debit notification to the customer regarding an upcoming payment which will be deducted from the customer’s account as part of the registration. There is a mandate to send this notification to the customer at least 48 hours before the actual debit, that is, 48 hours before calling the Recurring API.

&#x20;It is Mandatory to Check the mandate status before calling the **Pre-Debit Notification** API.

**Mandate Status Check API (Not Working in UAT)**

**Request: -**<br />curl --location ' \ <br />--header 'Content-Type: application/x-www-form-urlencoded' \ <br />--data-urlencode 'key=z8a7yT' \ <br />--data-urlencode 'command=check\_mandate\_status' \ <br />--data-urlencode 'var1={"authPayuId": "403993715531577472","requestId": "202405211421"}' \ --data-urlencode 'hash={{hash}}'

**Response: -**<br />{ <br />   "status": 0,

<br />

<br />

  "message": "Consent is Not Mandated", <br />  "action": "check\_mandate\_status" <br />}

**Pre-Debit Notification API Call**

**Request:-**<br />curl --location ' \ <br />--header 'Content-Type: application/x-www-form-urlencoded' \ <br />--data-urlencode 'key=z8a7yT' \ <br />--data-urlencode 'command=pre\_debit\_SI' \ <br />--data-urlencode <br />'hash=b49888227454e3936c155c886e30c344c9225a35015fb430d6337560f33d56714d2e9f5c4ff afdcb038babf248a1de3806d198dbc47a31cc02c363687d53f6eb' \ <br />--data-urlencode <br />'var1={"authpayuid":"403993715531577472","requestid":"rec\_403993715531577472","debitdat e":"2024-05-21","invoiceDisplayNumber":"pre\_403993715531577472","amount":"200.00"}'

**Response:-**<br />{ <br />   "status": 1, <br />   "message": "Request Processed Successfully",    "action": "MANDATE\_PRE\_DEBIT", <br />   "invoiceid": "47DnIBfFDe", <br />   "approvedStatus": "NA",

<br />

<br />

  "invoiceStatus": "SUCCESS", <br />  "amount": "NA" <br />}

**Recurring API Request: -**<br />It will be called on Debit Date provided in Pre-Debit API Call:-

**Request:-**<br /> curl --location  \ <br />--header 'Content-Type: application/x-www-form-urlencoded' \ <br />--data-urlencode 'key=z8a7yT' \ <br />--data-urlencode 'command=si\_transaction' \ <br />--data-urlencode <br />'hash=8d5323ef942cbcf7ad773021bbc3db7bac072b56cebdfb8fbeccee5fd23411c94ace32ffcf105 c46dfce124d5cec8a8de662cb2a556352ec9d9e3c22791aebcc' \ <br />--data-u<br />'var1={","txnid":"rec\_403993715531577472","invoiceDisplayNumber":"pre\_4039937 15531577472"}'

**Response: -**<br /> { <br />  "status": 1, <br />  "message": "Transaction Processed successfully",   "details": {

<br />

<br />

  "rec\_403993715531577472": { <br />   "authpayuid": "403993715531577472", <br />   "transactionid": "rec\_403993715531577472", <br />   "amount": "200", <br />   "user\_credentials": "z8a7yT:99390ee3cf2695c66857",    "card\_token": "9d9953d2ee4d11e07b376", <br />   "payuid": "403993715531582144", <br />   "status": "captured", <br />   "udf1": null, <br />   "field9": "Transaction is Successful", <br />   "udf2": "", <br />   "udf3": "", <br />   "udf4": "", <br />   "udf5": "", <br />   "phone": "9876543210", <br />   "email": "" <br />  } <br />  } <br />}

**Manage Cards Recurring:-**<br /> We have 2 more APIs in order to Manage the Cards Transaction:- 1.Cancel Mandate API <br />2.Modification API

<br />

<br />

**Cancel Mandate API:- (Not Working in UAT)**

**Cancel Recurring Registration** API allows the merchants to cancel the Cards registration from their website. It is a mandate to implement the **Cancel Recurring Registration** API so that your customers can use Recurring Payments as per their need.

**Request:-**<br />curl --location ' \ <br />--header 'Content-Type: application/x-www-form-urlencoded' \ <br />--data-urlencode 'key=z8a7yT' \ <br />--data-urlencode 'command=mandate\_revoke' \ <br />--data-urlencode 'var1={"authPayuId": "403993715531577472","requestId": "202405211451"}' \ --data-urlencode <br />'hash=e218513bb0255b6831d990fdf3a97c6c069bf15c18baded7099bf27f63f118d4a223972e613 847b29663d40dfe84a2612ca185a0e3994072da088416fadd6186'

**&#x20;Response:-**<br />{ <br />   "status": 0, <br />   "message": "Mandate flow not set", <br />   "action": "MANDATE\_REVOKE" <br />}

**One-Time Mandate Consent Transaction using PayU Hosted Checkout**

<br />

<br />

To make an One-Time Mandate transaction, you must post the **SI=4** instead of **SI=1** in case of payment consent transaction. You will share the billing details such as billing amount, start date, end date, billing interval, billing currency, billing cycle, etc. using the **\_payment** API. After your user is redirected to the PayU Checkout page, all the eligible autopay payment modes will have **Register AutoDebit&#x20;**&#x6F;ption in specific section along with the enabled payment modes.

**Webhook**

Transaction Status Webhook is being triggered to the configured url for payment status including Registration and Recurring Transactions as well.

**&#x20;Events :-** Success/Failed

**Webhooks for third Party cancellation or Modification**

If any activity performed on the Subscription via third party PSP app or issuing bank on the mandate then the specific event is also triggered to the webhook configured.

• **Event Covered for UPI:** Pause/Active/Revoked <br />• **Event Covered for Cards:** Active/Deleted <br />• **Event Covered for NB**: CANCEL\_FAILURE/ CANCEL\_SUCCESS

**For Sample Response received for third party Modification, Refer:-**

<br />

<br />

-
- •••
-
- Go toPage

<br />
